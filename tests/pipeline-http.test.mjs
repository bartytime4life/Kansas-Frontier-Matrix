import test from 'node:test';
import assert from 'node:assert/strict';
const origin = process.env.KFM_NODE_TEST_ORIGIN;
test('built HTTP routes expose honest disabled state and no anonymous writes', { skip: !origin }, async () => {
  const url = new URL(origin); assert.equal(url.hostname, '127.0.0.1');
  for (const path of ['/api/curated/usgs-streamflow','/api/pipeline-status']) {
    const r = await fetch(origin + path); assert.equal(r.status, 200); assert.match(r.headers.get('cache-control'), /no-store/);
    const value = await r.json(); assert.ok(value.state); assert.ok(!value.data); assert.ok(!value.workerSecret);
  }
  const denied = await fetch(origin + '/api/pipeline/v1/stage', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: '{}' });
  assert.equal(denied.status, 404); assert.deepEqual(await denied.json(), { error: 'PIPELINE_DISABLED' });
  const page = await fetch(origin + '/curated'); assert.equal(page.status, 200); assert.match(await page.text(), /Curated source snapshots/);
});
