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
  if (manifest.id !== 'HuggingFaceTB/SmolLM2-135M-Instruct' || !/^[a-f0-9]{40}$/.test(manifest.revision) || manifest.license !== 'apache-2.0') fail('MODEL_MANIFEST_INVALID');
  const allowed = new Set(['README.md', 'config.json', 'generation_config.json', 'onnx/model_q4.onnx', 'special_tokens_map.json', 'tokenizer.json', 'tokenizer_config.json']);
  if (!Array.isArray(manifest.files) || manifest.files.length !== allowed.size || new Set(manifest.files.map(x => x.path)).size !== allowed.size) fail('MODEL_MANIFEST_INVALID');
  for (const entry of manifest.files) {
    if (!allowed.has(entry.path) || !Number.isSafeInteger(entry.size) || entry.size <= 0 || entry.size > 200000000 || !/^[a-f0-9]{64}$/.test(entry.sha256)) fail('MODEL_MANIFEST_INVALID');
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
  // The Node export uses WebAssembly; no onnxruntime-node / .node addon is imported.
  stage('WASM_IMPORT');
  const ort = await import('onnxruntime-web');
  const { Tokenizer } = await import('@huggingface/tokenizers');
  ort.env.wasm.numThreads = 1; ort.env.wasm.proxy = false;
  stage('WASM_READY');
  const manifest = JSON.parse(await readFile(new URL('./embedded-ai-model.json', import.meta.url), 'utf8'));
  stage('DOWNLOAD'); const downloadBegan = performance.now();
  const modelDirectory = await installModel(workerData.directory, manifest);
  const downloadMs = Math.round(performance.now() - downloadBegan);
  stage('MODEL_LOAD'); const loadBegan = performance.now();
  const session = await ort.InferenceSession.create(join(modelDirectory, 'onnx/model_q4.onnx'), {
    executionProviders: ['wasm'], executionMode: 'sequential',
    graphOptimizationLevel: 'disabled', enableCpuMemArena: false, enableMemPattern: false,
    extra: { session: { disable_prepacking: '1' } },
  });
  const loadMs = Math.round(performance.now() - loadBegan);
  let past = {};
  try {
    const config = JSON.parse(await readFile(join(modelDirectory, 'config.json'), 'utf8'));
    const tc = JSON.parse(await readFile(join(modelDirectory, 'tokenizer_config.json'), 'utf8'));
    const tokenizer = new Tokenizer(JSON.parse(await readFile(join(modelDirectory, 'tokenizer.json'), 'utf8')), tc);
    if (config.hidden_size !== 576 || config.num_attention_heads !== 9 || config.num_key_value_heads !== 3 || config.num_hidden_layers !== 30) fail('MODEL_CONFIG_UNSUPPORTED');
    const expectedInputs = ['input_ids', 'attention_mask', 'position_ids'];
    for (let layer = 0; layer < config.num_hidden_layers; layer++) {
      for (const kind of ['key', 'value']) expectedInputs.push('past_key_values.' + layer + '.' + kind);
    }
    if (session.inputNames.length !== expectedInputs.length || expectedInputs.some(name => !session.inputNames.includes(name))) fail('MODEL_INPUTS_UNSUPPORTED');
    for (const meta of session.inputMetadata) {
      if (!meta.isTensor || meta.type !== (meta.name.startsWith('past_key_values.') ? 'float32' : 'int64')) fail('MODEL_INPUT_TYPE_UNSUPPORTED');
    }
    // Fixed synthetic ChatML, matching the pinned publisher's chat template.
    const prompt = '<|im_start|>system\nAnswer using only the supplied synthetic test sentence.<|im_end|>\n<|im_start|>user\nSynthetic test: The sample marker is blue. What color is the sample marker? Answer with one word.<|im_end|>\n<|im_start|>assistant\n';
    const eos = tokenizer.encode(tc.eos_token).ids;
    if (eos.length !== 1 || eos[0] !== config.eos_token_id) fail('MODEL_EOS_UNSUPPORTED');
    const ids = tokenizer.encode(prompt).ids, generated = [];
    const i64 = values => new ort.Tensor('int64', BigInt64Array.from(values.map(BigInt)), [1, values.length]);
    for (const name of expectedInputs.filter(name => name.startsWith('past_key_values.'))) {
      past[name] = new ort.Tensor('float32', new Float32Array(0), [1, 3, 0, 64]);
    }
    stage('INFERENCE'); const inferenceBegan = performance.now();
    let current = ids, pastLength = 0;
    for (let step = 0; step < 16; step++) {
      const feeds = { ...past, input_ids: i64(current), attention_mask: i64(Array(pastLength + current.length).fill(1)),
        position_ids: i64(current.map((_, index) => pastLength + index)) };
      const outputs = await session.run(feeds);
      const logits = outputs.logits;
      if (!logits || logits.type !== 'float32' || logits.dims.at(-1) !== config.vocab_size) fail('MODEL_LOGITS_UNSUPPORTED');
      const vocab = logits.dims.at(-1), offset = logits.data.length - vocab;
      let next = 0;
      for (let index = 1; index < vocab; index++) if (logits.data[offset + index] > logits.data[offset + next]) next = index;
      for (const tensor of Object.values(feeds)) tensor.dispose();
      past = {};
      for (const name of expectedInputs.filter(name => name.startsWith('past_key_values.'))) {
        const outputName = name.replace('past_key_values.', 'present.');
        if (!outputs[outputName]) fail('MODEL_KV_OUTPUT_MISSING');
        past[name] = outputs[outputName]; delete outputs[outputName];
      }
      for (const tensor of Object.values(outputs)) tensor.dispose();
      if (next === eos[0]) break;
      generated.push(next); pastLength += current.length; current = [next];
    }
    const answer = tokenizer.decode(generated, { skip_special_tokens: true });
    if (typeof answer !== 'string' || answer.length > 256 || !/\bblue\b/i.test(answer) || /[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]/.test(answer)) fail('SYNTHETIC_RESPONSE_UNQUALIFIED');
    parentPort.postMessage({ type: 'result', result: { status: 'SYNTHETIC_INFERENCE_PASS',
      model: { id: manifest.id, revision: manifest.revision, license: manifest.license, dtype: 'q4' },
      runtime: 'onnxruntime-web@1.31.0-dev.20260914-8d85527a0 / @huggingface/tokenizers@0.2.0 / wasm single-threaded',
      syntheticAnswer: answer, downloadMs, loadMs, inferenceMs: Math.round(performance.now() - inferenceBegan),
      inferenceRssBytes: process.memoryUsage().rss, modelFilesVerified: true,
      networkDuringInference: 'LOCAL_FILES_ONLY_NO_REMOTE_MODEL_LOADER', maximumOutputTokens: 16,
    } });
  } finally {
    for (const tensor of Object.values(past)) tensor.dispose();
    await session.release();
  }
} catch (error) {
  parentPort.postMessage({ type: 'result', result: { status: 'LIMITED', reason: safeReason(error) } });
}
