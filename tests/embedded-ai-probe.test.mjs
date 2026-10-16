import test from 'node:test';
import assert from 'node:assert/strict';
import { EventEmitter } from 'node:events';
import { watchEmbeddedWorker, startEmbeddedAiProbe } from '../server/embedded-ai-probe.mjs';

const worker = () => { const w = new EventEmitter(); w.terminate = async () => { w.terminated = true; }; return w; };
test('disabled startup never starts inference or installation', async () => {
  let calls = 0;
  assert.deepEqual(await startEmbeddedAiProbe(false, async () => { calls++; }), { status: 'DISABLED' });
  assert.equal(calls, 0);
});
test('worker deadline requests termination', async () => {
  const w = worker();
  const result = await watchEmbeddedWorker(w, { timeoutMs: 10 });
  assert.equal(result.reason, 'EMBEDDED_TIMEOUT'); assert.equal(w.terminated, true);
});
test('sampled memory budget stops a worker and records the observed peak', async () => {
  const w = worker();
  const result = await watchEmbeddedWorker(w, { maximumRssBytes: 10, memoryUsage: () => ({ rss: 11 }) });
  assert.equal(result.reason, 'EMBEDDED_MEMORY_LIMIT'); assert.equal(result.peakRssBytes, 11); assert.equal(w.terminated, true);
});
test('native errors never copy arbitrary error messages into a receipt', async () => {
  const w = worker(); const result = watchEmbeddedWorker(w);
  w.emit('error', Object.assign(new Error('private text'), { code: 'bad secret value' }));
  assert.equal((await result).reason, 'EMBEDDED_TEST_FAILED'); assert.equal(w.terminated, true);
});
test('unexpected worker exit is finite failure', async () => {
  const w = worker(); const result = watchEmbeddedWorker(w);
  w.emit('exit', 1); assert.equal((await result).reason, 'EMBEDDED_WORKER_EXIT');
});
test('synthetic worker result remains distinct from production acceptance', async () => {
  const w = worker(); const result = watchEmbeddedWorker(w);
  w.emit('message', { type: 'stage', stage: 'INFERENCE' });
  w.emit('message', { type: 'result', result: { status: 'SYNTHETIC_INFERENCE_PASS' } });
  assert.equal((await result).status, 'SYNTHETIC_INFERENCE_PASS'); assert.equal(w.terminated, true);
});
