import assert from 'node:assert/strict';
import test from 'node:test';
import { componentHarness, findNode } from './component-harness.mjs';

const text = node => node == null || typeof node === 'boolean' ? '' : typeof node !== 'object' ? String(node) : [node.props?.children].flat(Infinity).map(text).join(' ');
const row = async (payload, state = 'ready') => {
  const h = await componentHarness('app/source-quality-row.tsx', {
    './live-context': { TERRAIN_DISPLAY_MIN_ZOOM: 12 },
    './layer-workspaces': { sourceNeedsCloserView: () => false, sourceMinimumZoom: () => 0 },
    './source-downloads': { SOURCE_DOWNLOADS: { 'nws-alerts': { href: '/source', label: 'Download' } }, sourceDownloadHref: () => '/source' },
  });
  return h.render(h.exports.SourceQualityRow, { source: { id: 'nws-alerts', shortTitle: 'Alerts', cadence: 'Provider cadence' }, state, payload, selected: true, held: false, viewZoom: 8, onToggle() {} });
};

test('a new retrieval keeps an older provider timestamp distinct', async () => {
  const tree = await row({ featureCount: 1, retrievedAt: '2026-11-06T12:00:00Z', upstreamUpdatedAt: '2024-06-01T12:00:00Z' });
  const clocks = [];
  findNode(tree, node => { if (node.props?.className === 'source-quality-clock') clocks.push(text(node)); return false; });
  assert.match(clocks[0], /retrieved by KFM.*2026/);
  assert.match(clocks[1], /Provider timestamp:.*2024/);
  assert.doesNotMatch(clocks[1], /2026/);
});

test('a missing provider timestamp stays unknown after a successful download', async () => {
  const tree = await row({ featureCount: 0, retrievedAt: '2026-11-06T12:00:00Z', upstreamUpdatedAt: null });
  assert.match(text(tree), /Provider timestamp:\s+Not supplied by provider/);
  assert.match(text(tree), /0 records/);
});

test('a failed refresh preserves the original payload clocks without claiming an update', async () => {
  const tree = await row({ featureCount: 2, retrievedAt: '2025-05-03T12:00:00Z', upstreamUpdatedAt: '2024-06-01T12:00:00Z' }, 'error');
  assert.match(text(tree), /Unavailable/);
  assert.match(text(tree), /retrieved by KFM.*2025/);
  assert.match(text(tree), /Provider timestamp:.*2024/);
  assert.doesNotMatch(text(tree), /2026/);
});
