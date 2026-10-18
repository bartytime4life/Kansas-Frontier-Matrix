import { parentPort, workerData } from 'node:worker_threads';
import { readFile } from 'node:fs/promises';
import { join } from 'node:path';
import { performance } from 'node:perf_hooks';
import { installModel } from './hosted-ai-artifacts.mjs';

const stage = value => parentPort.postMessage({ type: 'stage', stage: value });
const fail = code => { throw Object.assign(new Error(code), { code }); };
const safeReason = error => /^[A-Z][A-Z0-9_]{0,63}$/.test(error?.code ?? '') ? error.code : 'EMBEDDED_TEST_FAILED';

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
  const session = await ort.InferenceSession.create(await readFile(join(modelDirectory, 'onnx/model_int8.onnx')), {
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
    if (config.hidden_size !== 1024 || config.num_attention_heads !== 16 || config.num_key_value_heads !== 8 || config.num_hidden_layers !== 28) fail('MODEL_CONFIG_UNSUPPORTED');
    const expectedInputs = ['input_ids', 'attention_mask', 'position_ids'];
    for (let layer = 0; layer < config.num_hidden_layers; layer++) {
      for (const kind of ['key', 'value']) expectedInputs.push('past_key_values.' + layer + '.' + kind);
    }
    if (session.inputNames.length !== expectedInputs.length || expectedInputs.some(name => !session.inputNames.includes(name))) fail('MODEL_INPUTS_UNSUPPORTED');
    for (const meta of session.inputMetadata) {
      if (!meta.isTensor || meta.type !== (meta.name.startsWith('past_key_values.') ? 'float32' : 'int64')) fail('MODEL_INPUT_TYPE_UNSUPPORTED');
    }
    // Fixed synthetic ChatML, matching the pinned publisher's chat template.
    const prompt = '<|im_start|>system\nAnswer using only the supplied synthetic test sentence.<|im_end|>\n<|im_start|>user\nSynthetic test: The sample marker is blue. What color is the sample marker? Answer with one word.<|im_end|>\n<|im_start|>assistant\n<think>\n\n</think>\n\n';
    const eos = tokenizer.encode(tc.eos_token).ids;
    if (eos.length !== 1 || eos[0] !== config.eos_token_id) fail('MODEL_EOS_UNSUPPORTED');
    const ids = tokenizer.encode(prompt).ids, generated = [];
    const i64 = values => new ort.Tensor('int64', BigInt64Array.from(values.map(BigInt)), [1, values.length]);
    for (const name of expectedInputs.filter(name => name.startsWith('past_key_values.'))) {
      past[name] = new ort.Tensor('float32', new Float32Array(0), [1, 8, 0, 128]);
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
