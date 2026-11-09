import test from 'node:test';
import assert from 'node:assert/strict';
import { activatedOfflineWorker } from '../src/offline-worker.ts';

function worker(state) {
  const listeners = new Set();
  return {state, addEventListener:(_, fn)=>listeners.add(fn), removeEventListener:(_, fn)=>listeners.delete(fn),
    setState(next) { this.state=next; for (const fn of [...listeners]) fn(); }, get listeners() { return listeners.size; }};
}

test('cache preparation waits for a replacement worker instead of using the stale active worker', async () => {
  const old = worker('activated');
  const next = worker('installing');
  const prepared = activatedOfflineWorker({active:old,installing:next,waiting:null});
  assert.equal(next.listeners,1);
  next.setState('activated');
  assert.equal(await prepared,next);
  assert.equal(next.listeners,0);
});

test('already-active workers resolve and failed replacement workers do not report readiness', async () => {
  const active = worker('activated');
  assert.equal(await activatedOfflineWorker({active,installing:null,waiting:null}),active);
  const next = worker('installing');
  const prepared = activatedOfflineWorker({active,installing:next,waiting:null});
  next.setState('redundant');
  await assert.rejects(prepared,/unavailable/);
  assert.equal(next.listeners,0);
});
