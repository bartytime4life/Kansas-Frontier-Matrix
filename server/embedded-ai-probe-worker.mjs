import { parentPort, workerData } from 'node:worker_threads';
import { readFile, mkdir, lstat, chmod, open, writeFile } from 'node:fs/promises';
import { createHash } from 'node:crypto';
import { join } from 'node:path';
import { performance } from 'node:perf_hooks';

const stage = value => parentPort.postMessage({ type: 'stage', stage: value });
const fail = code => { throw Object.assign(new Error(code), { code }); };
const safeReason = error => /^[A-Z][A-Z0-9_]{0,63}$/.test(error?.code ?? '') ? error.code : 'EMBEDDED_TEST_FAILED';
const safeHost = host => host === 'huggingface.co' || host.endsWith('.huggingface.co') || host.endsWith('.hf.co');

async function providerDownload(url, signal) {
  for (let count = 0; count < 6; count++) {
    const target = new URL(url);
    if (target.protocol !== 'https:' || target.username || target.password || target.port || !safeHost(target.hostname)) fail('MODEL_DOWNLOAD_DESTINATION');
    const response = await fetch(target, { redirect: 'manual', signal });
    if ([301, 302, 303, 307, 308].includes(response.status)) {
      const location = response.headers.get('location'); await response.body?.cancel();
      if (!location) fail('MODEL_DOWNLOAD_REDIRECT');
      url = new URL(location, target).href; continue;
    }
    if (!response.ok || !response.body) fail('MODEL_DOWNLOAD_UNAVAILABLE');
    return response;
  }
  fail('MODEL_DOWNLOAD_REDIRECT_LIMIT');
}

async function privateDirectory(path) {
  await mkdir(path, { mode: 0o700, recursive: true });
  const info = await lstat(path);
  if (!info.isDirectory() || info.isSymbolicLink() || info.uid !== process.getuid()) fail('MODEL_DIRECTORY_UNSAFE');
  await chmod(path, 0o700);
}

async function installModel(directory, manifest) {
  if (manifest.id !== 'HuggingFaceTB/SmolLM2-360M-Instruct' || !/^[a-f0-9]{40}$/.test(manifest.revision) || manifest.license !== 'apache-2.0') fail('MODEL_MANIFEST_INVALID');
  const allowed = new Set(['README.md', 'config.json', 'generation_config.json', 'onnx/model_q4.onnx', 'special_tokens_map.json', 'tokenizer.json', 'tokenizer_config.json']);
  if (!Array.isArray(manifest.files) || manifest.files.length !== allowed.size || new Set(manifest.files.map(x => x.path)).size !== allowed.size) fail('MODEL_MANIFEST_INVALID');
  for (const entry of manifest.files) {
    if (!allowed.has(entry.path) || !Number.isSafeInteger(entry.size) || entry.size <= 0 || entry.size > 400000000 || !/^[a-f0-9]{64}$/.test(entry.sha256)) fail('MODEL_MANIFEST_INVALID');
  }
  const modelDirectory = join(directory, 'model');
  await privateDirectory(modelDirectory); await privateDirectory(join(modelDirectory, 'onnx'));
  const files = [];
  for (const entry of manifest.files) {
    const signal = AbortSignal.timeout(120000);
    const response = await providerDownload(`https://huggingface.co/${manifest.id}/resolve/${manifest.revision}/${entry.path}`, signal);
    const file = await open(join(modelDirectory, entry.path), 'wx', 0o600);
    const hash = createHash('sha256'), reader = response.body.getReader(); let bytes = 0;
    try {
      while (true) {
        const { done, value } = await reader.read(); if (done) break;
        bytes += value.length; if (bytes > entry.size) fail('MODEL_FILE_SIZE_MISMATCH');
        hash.update(value); await file.writeFile(value);
      }
      await file.sync();
      if (bytes !== entry.size || hash.digest('hex') !== entry.sha256) fail('MODEL_FILE_INTEGRITY_MISMATCH');
      files.push({ path: entry.path, size: bytes, sha256: entry.sha256 });
    } finally { await reader.cancel().catch(() => {}); reader.releaseLock(); await file.close(); }
  }
  await writeFile(join(directory, 'verified-model.json'), JSON.stringify({ ...manifest, files }, null, 2) + '\n', { flag: 'wx', mode: 0o600 });
  return modelDirectory;
}

try {
  // A normal npm native library loaded inside Node; no executable subprocess.
  stage('NATIVE_IMPORT');
  const { pipeline, env } = await import('@huggingface/transformers');
  stage('NATIVE_READY');
  const manifest = JSON.parse(await readFile(new URL('./embedded-ai-model.json', import.meta.url), 'utf8'));
  stage('DOWNLOAD'); const downloadBegan = performance.now();
  const modelDirectory = await installModel(workerData.directory, manifest);
  const downloadMs = Math.round(performance.now() - downloadBegan);
  env.allowRemoteModels = false; env.allowLocalModels = true; env.useBrowserCache = false;
  env.cacheDir = join(workerData.directory, 'cache');
  stage('MODEL_LOAD'); const loadBegan = performance.now();
  const pipe = await pipeline('text-generation', modelDirectory + '/', { device: 'cpu', dtype: 'q4', local_files_only: true,
    session_options: { intraOpNumThreads: 1, interOpNumThreads: 1, executionMode: 'sequential' } });
  const loadMs = Math.round(performance.now() - loadBegan);
  try {
    stage('INFERENCE'); const inferenceBegan = performance.now();
    const output = await pipe([
      { role: 'system', content: 'Answer using only the supplied synthetic test sentence.' },
      { role: 'user', content: 'Synthetic test: The sample marker is blue. What color is the sample marker? Answer with one word.' },
    ], { max_new_tokens: 16, do_sample: false });
    const answer = output[0]?.generated_text?.at(-1)?.content;
    if (typeof answer !== 'string' || answer.length > 256 || !/\bblue\b/i.test(answer) || /[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]/.test(answer)) fail('SYNTHETIC_RESPONSE_UNQUALIFIED');
    parentPort.postMessage({ type: 'result', result: { status: 'SYNTHETIC_INFERENCE_PASS',
      model: { id: manifest.id, revision: manifest.revision, license: manifest.license, dtype: 'q4' },
      runtime: '@huggingface/transformers@4.3.1 / onnxruntime-node@1.30.0 / cpu',
      syntheticAnswer: answer, downloadMs, loadMs, inferenceMs: Math.round(performance.now() - inferenceBegan),
      inferenceRssBytes: process.memoryUsage().rss, modelFilesVerified: true,
      networkDuringInference: 'DISABLED_REMOTE_MODELS', maximumOutputTokens: 16,
    } });
  } finally { await pipe.dispose(); }
} catch (error) {
  parentPort.postMessage({ type: 'result', result: { status: 'LIMITED', reason: safeReason(error) } });
}
