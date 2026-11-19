import test from 'node:test';
import assert from 'node:assert/strict';
import { encodeLabView, decodeLabView } from '../app/labs/view-state.mjs';
import { storyLocation } from '../app/labs/atlas-model.mjs';
const binding = { story: 'built-kansas', snapshotSha256: 'a'.repeat(64) };
test('view replay retains Unicode, zero values, filters and scientific controls against exact source bytes', () => {
  const state = { controls: { query: 'São → Kansas', minValue: 0, category: 'Local road', selectedId: 'kdot-1', view: 'relationships', xMetric: 'length', yMetric: 'traffic', showFit: true, scienceFrom: 1950 }, time: 2025 };
  const token = encodeLabView({ ...binding, ...state });
  assert.match(token, /^[\w-]+$/);
  assert.deepEqual(decodeLabView(token, binding), state);
  assert.equal(decodeLabView(token, { ...binding, story: 'energy-shift' }), null);
  assert.equal(decodeLabView(token, { ...binding, snapshotSha256: 'b'.repeat(64) }), null);
});
test('untrusted view input rejects oversized, unknown, nested, nonfinite and malformed states', () => {
  for (const controls of [{ query: 'x'.repeat(301) }, { fetch: 'https://example.com' }, { metric: {} }, { query: true }, { showFit: 'yes' }, { view: 'arbitrary' }, JSON.parse('{"__proto__":"x"}'), { scienceFrom: Infinity }]) {
    assert.throws(() => encodeLabView({ ...binding, controls }), /Invalid/);
    const untrusted = Buffer.from(JSON.stringify({ v: 1, s: binding.story, h: binding.snapshotSha256, c: controls, t: null })).toString('base64url');
    // JSON converts infinity to null; null numerical filters are an allowed empty value.
    if (controls.scienceFrom !== Infinity) assert.equal(decodeLabView(untrusted, binding), null);
  }
  for (const token of ['', 'x'.repeat(8193), '<script>', 'e30', '____']) assert.equal(decodeLabView(token, binding), null);
  assert.throws(() => encodeLabView({ ...binding, time: NaN }), /Invalid/);
});
test('story navigation drops another instrument replay while preserving unrelated location state', () => {
  assert.equal(storyLocation('https://example.com/labs?story=built-kansas&view=abc&q=hi#sources', 'energy-shift'), '/labs?story=energy-shift&q=hi#sources');
  assert.equal(storyLocation('https://example.com/labs?story=built-kansas&view=abc', 'built-kansas'), '/labs?story=built-kansas&view=abc');
  assert.equal(storyLocation('https://example.com/labs?story=built-kansas&view=abc', null), '/labs');
});
