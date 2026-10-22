import { readFile } from 'node:fs/promises';
import { resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { freemem } from 'node:os';
import { captureRequest, fetchCapture } from '../../server/ingestion-sources.mjs';
import { normalizeCapture } from '../../server/pipeline-normalize.mjs';
import { canonical, sha, parse, fail, recipeDigest } from '../../server/pipeline-contract.mjs';
import { immutable, readRegular, storageGuard } from '../../server/pipeline-files.mjs';
import { Journal } from './journal.mjs';
import { pipelineCall, publish } from './publisher.mjs';

const SAFE = /^[A-Z][A-Z_]{1,63}$/;
export async function tick(config, { fetcher = fetch, now = Date.now(), acquire = fetchCapture, memory = freemem, guard = storageGuard } = {}) {
  await guard(config, { reserve: 64 * 1024 ** 2 });
  if (memory() < 3 * 1024 ** 3) fail('MEMORY_RESERVE_REQUIRED');
  const journal = await Journal.open(resolve(config.root, 'pipeline-journal.sqlite'));
  const outcomes = [];
  let secret;
  try {
  if (config.publish === true) {
    const credentialRoot = process.env.CREDENTIALS_DIRECTORY;
    if (!credentialRoot) fail('SYSTEMD_CREDENTIAL_REQUIRED');
    secret = (await readFile(resolve(credentialRoot, 'pipeline-worker-key'))).toString().trim();
  }
    if (secret) await pipelineCall('heartbeat', { state: 'running' }, secret, { fetcher });
    for (const sourceId of config.sources) {
      if (!['usgs-streamflow','nws-alerts'].includes(sourceId)) fail('SOURCE_NOT_ALLOWED');
      await guard(config, { reserve: 64 * 1024 ** 2 });
      if (memory() < 3 * 1024 ** 3) fail('MEMORY_RESERVE_REQUIRED');
      const request = captureRequest(sourceId, now); const job = journal.claim(sourceId, request.slot, now);
      if (!job) { outcomes.push({ sourceId, state: 'already-complete-or-held' }); continue; }
      try {
        let productPath = job.product_path;
        if (!productPath) {
          const capture = await acquire(request, { fetcher, apiKey: process.env.USGS_WATER_API_KEY });
          // Raw bytes survive a normalization/schema failure and never enter the public transfer.
          const captureBase = resolve(config.root, 'data/quarantine', sourceId, 'objects/sha256', sha(capture.bytes));
          await immutable(resolve(captureBase, 'payload'), capture.bytes);
          const receiptBytes = Buffer.from(canonical(capture.receipt));
          await immutable(resolve(config.root, 'data/receipts/ingest/pc-pipeline', sha(receiptBytes) + '.json'), receiptBytes);
          const normalized = normalizeCapture(request, capture); const id = sha(normalized.bytes);
          productPath = 'data/processed/' + sourceId + '/' + id + '.json';
          await immutable(resolve(config.root, productPath), normalized.bytes);
          journal.update(job, { product_path: productPath });
        }
        const payload = await readRegular(resolve(config.root, productPath), 8 * 1024 ** 2);
        if (secret) {
          let transfer;
          if (job.transfer_path) transfer = parse(await readRegular(resolve(config.root, job.transfer_path), 65536));
          else {
            const approval = parse(await readRegular(resolve(config.approvalDirectory, sourceId + '.json'), 32768));
            const head = await pipelineCall('release', { sourceId }, secret, { fetcher });
            transfer = { format: 'kfm-pc-release-transfer-v1', sourceId, recipeSha256: await recipeDigest(), byteLength: payload.length, payloadSha256: sha(payload), approval, expectedActive: head.releaseId };
            const relative = 'data/receipts/pipeline/transfers/' + sha(canonical(transfer)) + '.json';
            await immutable(resolve(config.root, relative), Buffer.from(canonical(transfer)));
            journal.update(job, { transfer_path: relative });
          }
          const receipt = await publish(transfer, payload, secret, { fetcher });
          await immutable(resolve(config.root, 'data/receipts/pipeline/published', receipt.releaseId + '.json'), Buffer.from(canonical(receipt)));
          journal.update(job, { release_id: receipt.releaseId });
        }
        journal.finish(job); outcomes.push({ sourceId, state: secret ? 'published' : 'candidate-only' });
      } catch (e) {
        const code = SAFE.test(e.message ?? '') ? e.message : 'PIPELINE_OPERATION_FAILED';
        journal.finish(job, code); outcomes.push({ sourceId, state: 'held', reason: code });
      }
    }
    if (secret) await pipelineCall('heartbeat', { state: outcomes.some(x => x.state === 'held') ? 'held' : 'idle' }, secret, { fetcher });
    return { format: 'kfm-pc-pipeline-tick-v1', at: new Date(now).toISOString(), outcomes, authority: 'APPROVED_PROFILE_REQUIRED_FOR_PUBLICATION' };
  } finally { journal.close(); }
}
export async function loadConfig(path) {
  const config = parse(await readRegular(path, 16384));
  if (config.format !== 'kfm-pc-pipeline-config-v1' || typeof config.root !== 'string' || typeof config.mount !== 'string' || typeof config.storeId !== 'string'
    || !/^[a-f0-9]{32}$/.test(config.storeId) || !Array.isArray(config.sources) || config.sources.length > 2 || new Set(config.sources).size !== config.sources.length
    || config.sources.some(s => !['usgs-streamflow','nws-alerts'].includes(s)) || typeof config.publish !== 'boolean' || !/^\d+$/.test(String(config.device))
    || !config.approvalDirectory?.startsWith('/')) fail('CONFIG_INVALID');
  return config;
}
if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  try { console.log(canonical(await tick(await loadConfig(process.argv[2] ?? '/etc/kfm-pipeline/config.json')))); }
  catch (e) { console.error(canonical({ state: 'held', reason: SAFE.test(e.message ?? '') ? e.message : 'PIPELINE_OPERATION_FAILED' })); process.exitCode = 1; }
}
