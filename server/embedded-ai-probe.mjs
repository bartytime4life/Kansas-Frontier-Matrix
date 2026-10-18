// Preview-only qualification. No public route or access to KFM accounts/evidence.
import { Worker } from 'node:worker_threads';
import { mkdir, lstat, chmod, readdir, writeFile, readFile } from 'node:fs/promises';
import { resolve, join } from 'node:path';
import { createHash, randomUUID } from 'node:crypto';

// Isolated qualification branch only. This is not a verified GoDaddy quota.
export const EMBEDDED_PROBE_LIMITS = Object.freeze({ timeoutMs: 240000, maximumRssBytes: 4096 * 1024 * 1024 });
const reason = error => /^[A-Z][A-Z0-9_]{0,63}$/.test(error?.code ?? '') ? error.code : 'EMBEDDED_TEST_FAILED';
const failure = code => Object.assign(new Error(code), { code });

export async function watchEmbeddedWorker(worker, { timeoutMs = EMBEDDED_PROBE_LIMITS.timeoutMs,
  maximumRssBytes = EMBEDDED_PROBE_LIMITS.maximumRssBytes, memoryUsage = process.memoryUsage } = {}) {
  let timer, monitor, peakRssBytes = memoryUsage().rss, stage = 'WORKER_START';
  try {
    return await new Promise(resolveResult => {
      let settled = false;
      const finish = result => {
        if (settled) return;
        settled = true;
        clearTimeout(timer); clearInterval(monitor);
        resolveResult({ ...result, stage, peakRssBytes });
      };
      timer = setTimeout(() => finish({ status: 'LIMITED', reason: 'EMBEDDED_TIMEOUT' }), timeoutMs);
      monitor = setInterval(() => {
        peakRssBytes = Math.max(peakRssBytes, memoryUsage().rss);
        if (peakRssBytes > maximumRssBytes) finish({ status: 'LIMITED', reason: 'EMBEDDED_MEMORY_LIMIT' });
      }, 100);
      worker.on('message', value => {
        if (value?.type === 'stage' && ['WASM_IMPORT', 'WASM_READY', 'DOWNLOAD', 'MODEL_LOAD', 'INFERENCE'].includes(value.stage)) stage = value.stage;
        if (value?.type === 'result' && value.result && JSON.stringify(value.result).length <= 8192) {
          peakRssBytes = Math.max(peakRssBytes, memoryUsage().rss);
          if (peakRssBytes > maximumRssBytes) finish({ status: 'LIMITED', reason: 'EMBEDDED_MEMORY_LIMIT' });
          else finish(value.result);
        }
      });
      worker.once('error', error => finish({ status: 'LIMITED', reason: reason(error) }));
      worker.once('exit', () => finish({ status: 'LIMITED', reason: 'EMBEDDED_WORKER_EXIT' }));
    });
  } finally {
    clearTimeout(timer); clearInterval(monitor);
    await worker.terminate();
  }
}

export async function qualifyEmbeddedAi({ root = '/private', workerFactory = path => new Worker(path, {
  workerData: { directory: join(resolve(root), 'kfm-embedded-qwen3-06b-int8-wasm-20261018') },
  // --input-type applies to stdin/eval entrypoints, never to a worker file.
  execArgv: process.execArgv.filter(flag => !flag.startsWith('--input-type=')),
  resourceLimits: { maxOldGenerationSizeMb: 256 },
}) } = {}) {
  const directory = join(resolve(root), 'kfm-embedded-qwen3-06b-int8-wasm-20261018');
  const rootInfo = await lstat(root);
  if (!rootInfo.isDirectory() || rootInfo.isSymbolicLink()) throw failure('EMBEDDED_ROOT_UNSAFE');
  try { await mkdir(directory, { mode: 0o700 }); } catch (error) { if (error.code !== 'EEXIST') throw error; }
  const info = await lstat(directory);
  if (!info.isDirectory() || info.isSymbolicLink() || info.uid !== process.getuid()) throw failure('EMBEDDED_DIRECTORY_UNSAFE');
  await chmod(directory, 0o700);
  if ((await readdir(directory)).length) throw failure('EMBEDDED_ALREADY_ATTEMPTED');
  await writeFile(join(directory, '.attempt'), 'kfm.embedded-qwen3-06b-int8-wasm/20261018/v1\n', { flag: 'wx', mode: 0o600 });
  const runId = randomUUID(), began = performance.now();
  const workerPath = resolve('server/embedded-ai-probe-worker.mjs');
  const sources = {};
  for (const name of ['embedded-ai-probe.mjs', 'embedded-ai-probe-worker.mjs', 'embedded-ai-model.json']) {
    sources[`server/${name}`] = createHash('sha256').update(await readFile(resolve('server', name))).digest('hex');
  }
  let result;
  try { result = await watchEmbeddedWorker(workerFactory(workerPath)); }
  catch (error) { result = { status: 'LIMITED', reason: reason(error) }; }
  const receipt = { profile: 'kfm.embedded-qwen3-06b-int8-wasm/20261018/v1', runId, observedAt: new Date().toISOString(),
    node: process.versions.node, platform: process.platform, arch: process.arch,
    ...result, elapsedMs: Math.round(performance.now() - began), limits: EMBEDDED_PROBE_LIMITS, sources,
    scope: 'One fixed synthetic prompt in a Node worker thread. No KFM/user data, public endpoint, paid API, PC inference, daemon, subprocess, or extra listening port.',
    interpretation: 'A working runtime is not a released-evidence answer or acceptance of model quality. RSS is sampled process-wide, not an enforced provider quota; runtime memory may grow between samples.',
  };
  await writeFile(join(directory, `receipt-${runId}.json`), JSON.stringify(receipt, null, 2) + '\n', { flag: 'wx', mode: 0o600 });
  return receipt;
}

let started;
export function startEmbeddedAiProbe(enabled = process.env.KFM_EMBEDDED_AI_PROBE === '1', qualify = qualifyEmbeddedAi) {
  if (!enabled) return Promise.resolve({ status: 'DISABLED' });
  if (!started) started = qualify().then(receipt => {
    console.info(`KFM embedded Qwen3: ${receipt.status}${receipt.reason ? '; ' + receipt.reason : ''}; private receipt saved.`);
    return receipt;
  }).catch(error => {
    const result = { status: 'LIMITED', reason: reason(error) };
    console.info(`KFM embedded Qwen3: ${result.reason}; web startup remains independent.`);
    return result;
  });
  return started;
}
