import assert from 'node:assert/strict';
import test from 'node:test';
import { componentHarness, findNode, settle } from './component-harness.mjs';

const text = node => {
  if (typeof node === 'string' || typeof node === 'number') return String(node);
  if (!node || typeof node !== 'object') return '';
  return [node.props?.children].flat(Infinity).map(text).join('');
};
const empty = tree => findNode(tree, node => node.type === 'p' && node.props.role === 'status' && (
  /^(Checking for source records|Source records are withheld|Source records are unavailable|No approved snapshot|No records in this snapshot|This partial snapshot)/.test(text(node))
));
const product = (overrides = {}) => ({
  state: 'empty', sourceId: 'usgs-streamflow', evidenceRole: 'EXTERNAL_CONTEXT_ONLY',
  releaseId: 'a'.repeat(64), approvalExpiresAt: '2099-01-01T00:00:00Z',
  data: { type: 'FeatureCollection', features: [] }, ...overrides,
});

async function workspace() {
  let resolve, reject;
  const response = new Promise((yes, no) => { resolve = yes; reject = no; });
  const h = await componentHarness(new URL('../app/curated/workspace.tsx', import.meta.url), {
    'next/link': { default: 'a' },
    '../maplibre-seam': { loadMapLibre: async () => ({}) },
    '../kansas-orientation': { ORIENTATION_SOURCE_ID: 'orientation', orientationSource() {}, orientationLayers: () => [] },
    '../bounded-json': { readBoundedJson: async response => response.json() },
    './workspace.css': {},
  }, {
    queueMicrotask, setInterval: () => 1, clearInterval() {},
    document: { visibilityState: 'visible' },
    fetch: url => url.endsWith('/history') ? Promise.resolve({ json: async () => ({ items: [] }) }) : response,
  });
  const render = () => { const tree = h.render(h.exports.default); h.commit(); return tree; };
  render(); await settle();
  return {
    h, render,
    async show(value) { resolve({ json: async () => value }); await settle(); return render(); },
    async fail() { reject(new Error('network unavailable')); await settle(); return render(); },
  };
}

test('records explain a pending read without claiming a zero result', async t => {
  const w = await workspace(); t.after(() => w.h.dispose());
  const tree = w.render();
  assert.equal(text(empty(tree)), 'Checking for source records…');
  assert.ok(findNode(tree, node => node.type === 'button' && node.props.disabled && text(node) === 'Checking…'));
  assert.ok(findNode(tree, node => node.type === 'div' && node.props['aria-label'] === 'Dated Kansas provider context map'));
  assert.ok(findNode(tree, node => node.type === 'a' && node.props.href === '/'));
});

test('withheld and missing approvals explain why records are not listed and retain the source reason', async t => {
  for (const [reason, message, sourceReason] of [
    ['PIPELINE_NOT_CONFIGURED', 'Source records are withheld. See the publication reason above.', 'Published snapshots are not configured yet.'],
    ['APPROVAL_REVOKED', 'Source records are withheld. See the publication reason above.', 'This snapshot has been withheld following review.'],
    ['NO_APPROVED_RELEASE', 'No approved snapshot is available to list records.', 'No approved snapshot is available.'],
  ]) {
    const w = await workspace(); t.after(() => w.h.dispose());
    const tree = await w.show({ state: 'withheld', reason });
    assert.equal(text(empty(tree)), message);
    assert.ok(findNode(tree, node => node.type === 'p' && text(node) === sourceReason));
    assert.ok(findNode(tree, node => node.type === 'button' && text(node) === 'Refresh'));
    assert.doesNotMatch(text(tree), /No records in this snapshot/);
  }
});

test('failed reads and incomplete responses are unavailable, not successful empty snapshots', async t => {
  const failed = await workspace(); t.after(() => failed.h.dispose());
  assert.equal(text(empty(await failed.fail())), 'Source records are unavailable. Refresh to check again.');
  for (const value of [
    { state: 'unavailable' }, { state: 'empty' },
    product({ sourceId: 'nws-alerts' }), product({ evidenceRole: 'EVIDENCE' }),
    product({ data: { type: 'FeatureCollection', features: null } }),
    product({ state: 'withheld', reason: 'APPROVAL_REVOKED' }),
  ]) {
    const w = await workspace(); t.after(() => w.h.dispose());
    const tree = await w.show(value);
    assert.doesNotMatch(text(tree), /No records in this snapshot/);
    assert.ok(empty(tree), 'an empty records section still explains its state');
  }
});

test('only a compatible successful zero-record collection is described as an empty snapshot', async t => {
  for (const state of ['empty', 'available']) {
    const w = await workspace(); t.after(() => w.h.dispose());
    const tree = await w.show(product({ state }));
    assert.equal(text(empty(tree)), 'No records in this snapshot.');
    assert.equal(findNode(tree, node => node.type === 'ul' && node.props.className === 'curated-records'), undefined);
  }
});

test('a partial zero-record publication preserves the incomplete-coverage distinction', async t => {
  const w = await workspace(); t.after(() => w.h.dispose());
  const tree = await w.show(product({ state: 'partial' }));
  assert.equal(text(empty(tree)), 'This partial snapshot supplies no records; coverage may be incomplete.');
  assert.doesNotMatch(text(tree), /No records in this snapshot/);
});

test('a populated snapshot retains its record list and free provenance download without an empty message', async t => {
  const w = await workspace(); t.after(() => w.h.dispose());
  const tree = await w.show(product({ state: 'available', data: { type: 'FeatureCollection', features: [
    { type: 'Feature', id: 'gauge-1', geometry: null, properties: { stationId: 'USGS-test-gauge', value: 12, unit: 'ft³/s' } },
  ] } }));
  assert.equal(empty(tree), undefined);
  const list = findNode(tree, node => node.type === 'ul' && node.props.className === 'curated-records');
  assert.match(text(list), /USGS-test-gauge/);
  assert.ok(findNode(tree, node => node.type === 'a' && node.props.download === 'usgs-streamflow-' + 'a'.repeat(64) + '.json'));
  assert.match(text(tree), /not admitted evidence or an emergency notification service/);
});
