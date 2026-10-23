import test from 'node:test';
import assert from 'node:assert/strict';
import { storagePolicy, storagePlan } from '../scripts/pc-pipeline/storage-policy.mjs';
test('defaults reserve hosting for one compact release; settings cannot remove hard bounds', () => {
  assert.deepEqual(storagePolicy({}), { priority: ['nws-alerts','usgs-streamflow'], maxPublicationsPerTick: 1, maxBytesPerTick: 8388608 });
  for (const storagePolicyValue of [null, [], { priority: ['nws-alerts','nws-alerts'] }, { maxBytesPerTick: Infinity }, { maxBytesPerTick: 1 }, { maxPublicationsPerTick: 3 }, { uploadRaw: true }]) {
    assert.throws(() => storagePolicy({ storagePolicy: storagePolicyValue }), /STORAGE_POLICY_INVALID/);
  }
  const policy = storagePolicy({ storagePolicy: { priority: ['usgs-streamflow','nws-alerts'], maxPublicationsPerTick: 2, maxBytesPerTick: 16777216 } });
  assert.equal(policy.priority[0], 'usgs-streamflow');
  const plan = storagePlan({ publish: false, sources: ['nws-alerts'], root: '/private/not-for-export' });
  assert.equal(plan.publicationEnabled, false); assert.equal(plan.capacity, 'unverified'); assert.doesNotMatch(JSON.stringify(plan), /not-for-export/);
});
test('planner edits produce valid bounded policy without network writes', async () => {
  const { componentHarness, findNode } = await import('./component-harness.mjs');
  let calls = 0;
  const h = await componentHarness(new URL('../app/acquisition/storage-panel.tsx', import.meta.url), { './workspace.module.css': { default: {} } }, { fetch: () => { calls++; throw Error('unexpected network'); } });
  try {
    let tree = h.render(h.exports.default);
    const first = findNode(tree, n => n.type === 'select' && n.props.value === 'nws-alerts');
    first.props.onChange({ target: { value: 'usgs-streamflow' } });
    tree = h.render(h.exports.default);
    const field = findNode(tree, n => n.type === 'textarea');
    const config = JSON.parse(field.props.value);
    assert.equal(storagePolicy(config).priority[0], 'usgs-streamflow');
    assert.equal(field.props.readOnly, true); assert.equal(calls, 0);
  } finally { h.dispose(); }
});
