// Supply-chain captures are private operator signals. The signed grain recipe stays independent.
import { setTimeout as pause } from 'node:timers/promises';
import { resolve } from 'node:path';
import { boundedBody, canonical, fail, parse, sha } from '../../server/pipeline-contract.mjs';
import { immutable, storageGuard } from '../../server/pipeline-files.mjs';
import { reportChanges, watchMarket } from './market-watch.mjs';

const noticeLimit = 50;
const noticeQuery = new URLSearchParams({
  per_page: String(noticeLimit),
  order: 'newest',
  'conditions[agencies][]': 'trade-representative-office-of-united-states',
});
for (const field of ['document_number', 'publication_date', 'title', 'type', 'pdf_url']) {
  noticeQuery.append('fields[]', field);
}
const supplyChainReports = Object.freeze([
  Object.freeze({ id: 'usda-grain-freight-indicators', url: 'https://www.ams.usda.gov/sites/default/files/media/GTRTable1.xlsx', kind: 'xlsx' }),
  Object.freeze({ id: 'federal-register-ustr-notices', url: 'https://www.federalregister.gov/api/v1/documents.json?' + noticeQuery, kind: 'json' }),
]);
const tradeTerms = /\b(?:agricultur\w*|grain|wheat|corn|maize|sorghum|soybeans?|ethanol|fertiliz\w*|potash|urea|livestock|beef|dairy|maritime|shipping|shipbuilding)\b/i;
const limit = 2 * 1024 * 1024;

export function tradeNoticeSignals(body) {
  const page = parse(body, limit);
  if (!Number.isSafeInteger(page?.count) || page.count < 0 || !Array.isArray(page.results) ||
      page.results.length !== Math.min(page.count, noticeLimit)) fail('TRADE_NOTICE_PAGE_INVALID');

  const notices = [];
  const seen = new Set();
  for (const record of page.results) {
    const { document_number: id, publication_date: published, pdf_url: pdf, title, type } = record ?? {};
    if (typeof id !== 'string' || !/^\d{4}-\d{5}$/.test(id) || seen.has(id) ||
        typeof published !== 'string' || !/^\d{4}-\d{2}-\d{2}$/.test(published) ||
        !Number.isFinite(Date.parse(published)) || new Date(published).toISOString().slice(0, 10) !== published ||
        typeof title !== 'string' || !title.trim() || title.length > 1500 ||
        typeof type !== 'string' || !type.trim() || type.length > 80 ||
        pdf !== `https://www.govinfo.gov/content/pkg/FR-${published}/pdf/${id}.pdf`) fail('TRADE_NOTICE_RECORD_INVALID');
    seen.add(id);
    if (tradeTerms.test(title)) notices.push({ id, published, type, title, pdf });
  }
  return notices.sort((a, b) => a.id.localeCompare(b.id, 'en'));
}
async function capture(source, fetcher, config, clock) {
  const response = await fetcher(source.url, {
    redirect: 'error',
    headers: { 'Accept-Encoding': 'identity' },
    signal: AbortSignal.timeout(15000),
  });
  if (response.status !== 200 || !response.body) {
    await response.body?.cancel();
    fail('MARKET_SOURCE_UNAVAILABLE');
  }
  const body = await boundedBody(response, limit);
  if (source.kind === 'xlsx') {
    if (!body.subarray(0, 4).equals(Buffer.from('504b0304', 'hex')) ||
        !body.includes('[Content_Types].xml') || !body.includes('xl/workbook.xml')) fail('MARKET_RESPONSE_FORMAT');
  } else if (response.headers.get('content-type')?.split(';')[0].trim().toLowerCase() !== 'application/json') {
    fail('MARKET_RESPONSE_FORMAT');
  }

  const captureSha256 = sha(body);
  const receipt = {
    sourceId: source.id, sourceUrl: source.url, captureSha256, byteLength: body.length,
    retrievedAt: clock().toISOString(), lifecycle: 'WORK/QUARANTINE', releaseState: 'unreleased',
  };
  await immutable(resolve(config.root, 'data/quarantine', source.id, 'objects/sha256', captureSha256, 'payload'), body);
  const receiptBytes = Buffer.from(canonical(receipt));
  await immutable(resolve(config.root, 'data/receipts/ingest/pc-pipeline', sha(receiptBytes) + '.json'), receiptBytes);
  if (source.kind === 'xlsx') return { ...receipt, state: 'captured' };
  const notices = tradeNoticeSignals(body);
  return { ...receipt, state: 'captured', signalSha256: sha(canonical(notices)), notices };
}

export async function watchSupplyChain(config, { fetcher = fetch, guard = storageGuard, clock = () => new Date() } = {}) {
  const { outcomes } = await watchMarket(config, { fetcher, guard, clock });
  for (const source of supplyChainReports) {
    await guard(config, { reserve: 4 * limit });
    try {
      outcomes.push(await capture(source, fetcher, config, clock));
    } catch (error) {
      outcomes.push({ sourceId: source.id, state: 'held',
        reason: /^[A-Z_]{1,64}$/.test(error?.message) ? error.message : 'MARKET_CAPTURE_FAILED' });
    }
  }
  return { state: outcomes.some(outcome => outcome.state === 'held') ? 'partial' : 'complete', outcomes };
}

export async function listenSupplyChain(load, emit) {
  const previous = new Map();
  for (;;) {
    const result = await watchSupplyChain(await load());
    emit({ ...result, outcomes: reportChanges(result.outcomes, previous) });
    await pause(6 * 60 * 60 * 1000);
  }
}
