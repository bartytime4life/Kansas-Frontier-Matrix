// One bounded operator-initiated poll. The existing pipeline owns storage and release.
import { setTimeout as pause } from 'node:timers/promises';
import { captureRequest, fetchCapture } from '../../server/ingestion-sources.mjs';
import { execFile } from 'node:child_process';
import { promisify } from 'node:util';
import { resolve } from 'node:path';
import { canonical, sha, fail } from '../../server/pipeline-contract.mjs';
import { immutable, readRegular, storageGuard } from '../../server/pipeline-files.mjs';
import { GRAIN_SOURCE, GRAIN_URL, parseGrainReport } from '../../server/grain-market.mjs';

const extractText = promisify(execFile);

export const reports = Object.freeze([
  { id:GRAIN_SOURCE, url:GRAIN_URL, kind:'pdf' },
  { id:'usda-illinois-production-cost', url:'https://www.ams.usda.gov/mnreports/ams_3195.pdf', kind:'pdf' },
  { id:'eia-midwest-diesel', url:'https://www.eia.gov/dnav/pet/hist_xls/EMD_EPD2D_PTE_R20_DPGw.xls', kind:'xls' },
]);
const limit = 2 * 1024 * 1024;
export async function captureReport(source, fetcher = fetch) {
  if (!reports.includes(source)) fail('SOURCE_NOT_ALLOWED');
  const signal = AbortSignal.timeout(15000);
  const response = await fetcher(source.url, { redirect:'error', signal });
  if (response.status !== 200 || !response.body || Number(response.headers.get('content-length')) > limit) {
    await response.body?.cancel(); fail('MARKET_SOURCE_UNAVAILABLE');
  }
  const reader = response.body.getReader(), parts = [];
  let size = 0;
  try {
    for (;;) {
      const {done,value} = await reader.read();
      if (done) break;
      size += value.length;
      if (size > limit) { await reader.cancel(); fail('MARKET_RESPONSE_TOO_LARGE'); }
      parts.push(value);
    }
  } finally { reader.releaseLock(); }
  const body = Buffer.concat(parts,size);
  const magic = source.kind === 'pdf' ? Buffer.from('%PDF-') : Buffer.from('d0cf11e0a1b11ae1','hex');
  if (!body.subarray(0,magic.length).equals(magic)) fail('MARKET_RESPONSE_FORMAT');
  return body;
}

export async function grainFromCapture(root, digest, retrievedAt) {
  if (typeof digest !== 'string' || !/^[a-f0-9]{64}$/.test(digest)) fail('DIGEST_INVALID');
  const raw = resolve(root,'data/quarantine',GRAIN_SOURCE,'objects/sha256',digest,'payload');
  const original = await readRegular(raw,limit);
  if (sha(original) !== digest) fail('ARTIFACT_INTEGRITY_FAILED');
  let text;
  try {
    const result = await extractText('pdftotext',['-layout',raw,'-'],{encoding:'utf8',timeout:8000,maxBuffer:512*1024});
    text = result.stdout;
  } catch { fail('GRAIN_TEXT_EXTRACTION_FAILED'); }
  if (sha(await readRegular(raw,limit)) !== digest) fail('ARTIFACT_INTEGRITY_FAILED');
  return parseGrainReport(text,digest,retrievedAt);
}

export async function watchMarket(config, { fetcher = fetch, guard = storageGuard, clock = () => new Date() } = {}) {
  const outcomes = [];
  for (const source of reports) {
    await guard(config, {reserve:4*limit});
    try {
      const body = await captureReport(source,fetcher);
      const captureSha256 = sha(body), retrievedAt = clock().toISOString();
      const rawPath = resolve(config.root,'data/quarantine',source.id,'objects/sha256',captureSha256,'payload');
      await immutable(rawPath,body);
      const receipt = { sourceId:source.id, sourceUrl:source.url, captureSha256, byteLength:body.length, retrievedAt,
        lifecycle:'WORK/QUARANTINE', releaseState:'unreleased' };
      const receiptBytes = Buffer.from(canonical(receipt));
      await immutable(resolve(config.root,'data/receipts/ingest/pc-pipeline',sha(receiptBytes)+'.json'),receiptBytes);
      if (source.id !== GRAIN_SOURCE) { outcomes.push({...receipt,state:'captured'}); continue; }
      const product = await grainFromCapture(config.root,captureSha256,retrievedAt);
      const payload = Buffer.from(canonical(product)), digest = sha(payload);
      await immutable(resolve(config.root,'data/processed',source.id,digest+'.json'),payload);
      outcomes.push({...receipt,state:'candidate-only',reportDate:product.reportDate,rows:product.rows.length,payloadSha256:digest});
    } catch (error) {
      outcomes.push({sourceId:source.id,state:'held',reason:/^[A-Z_]{1,64}$/.test(error?.message) ? error.message : 'MARKET_CAPTURE_FAILED'});
    }
  }
  // Existing NWS adapter owns the active Kansas alert request and its original receipt.
  await guard(config, {reserve:16*1024*1024});
  try {
    const req = captureRequest('nws-alerts',clock().getTime());
    const capture = await fetchCapture(req,{fetcher});
    const receiptBytes = Buffer.from(canonical(capture.receipt));
    await immutable(resolve(config.root,'data/quarantine',req.sourceId,'objects/sha256',sha(capture.bytes),'payload'),capture.bytes);
    await immutable(resolve(config.root,'data/receipts/ingest/pc-pipeline',sha(receiptBytes)+'.json'),receiptBytes);
    if (capture.receipt.validation !== 'structure-valid' || capture.receipt.partial) fail('ALERT_CAPTURE_INCOMPLETE');
    const alerts = JSON.parse(capture.bytes).features.map(f=>{
      const p=f.properties;
      if (typeof f.id!=='string' || typeof p.sent!=='string' || typeof p.event!=='string' || typeof p.expires!=='string') fail('ALERT_SCHEMA_CHANGED');
      return [f.id,p.sent,p.event,p.expires];
    });
    const signals=alerts.map(row=>canonical(row)).sort();
    outcomes.push({sourceId:req.sourceId,state:'captured',captureSha256:sha(capture.bytes),signalSha256:sha(canonical(signals)),activeAlerts:alerts.length});
  } catch (error) {
    outcomes.push({sourceId:'nws-alerts',state:'held',reason:/^[A-Z_]{1,64}$/.test(error?.message)?error.message:'ALERT_CAPTURE_FAILED'});
  }
  return {state:outcomes.some(x=>x.state==='held')?'partial':'complete',outcomes};
}

/** Compare successful captures within one listening session. A failed poll never clears the last observation. */
export function reportChanges(outcomes, previous) {
  return outcomes.map(outcome=>{
    if (outcome.state === 'held') return outcome;
    const digest = outcome.signalSha256 ?? outcome.captureSha256;
    const prior = previous.get(outcome.sourceId);
    previous.set(outcome.sourceId,digest);
    return {...outcome, change:prior === undefined ? 'baseline' : prior === digest ? 'unchanged' : 'changed'};
  });
}

export async function listenMarket(load, emit) {
  const previous = new Map();
  for (;;) {
    const result = await watchMarket(await load());
    emit({...result,outcomes:reportChanges(result.outcomes,previous)});
    await pause(6*60*60*1000);
  }
}
