import assert from 'node:assert/strict';
import test from 'node:test';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';
import { componentHarness, findNode } from './component-harness.mjs';
const model = await import(`data:text/javascript;base64,${Buffer.from(ts.transpileModule(await readFile('app/public-map-catalog.ts', 'utf8'), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText).toString('base64')}`);
const css = { default: new Proxy({}, { get: (_target, key) => key }) };
const base = 'https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/';
const year = (y, kinds = ['details', 'fatalities', 'locations']) => ({ id: `publisher-noaa-storm-events-${y}`, sourceId: 'publisher-noaa-storm-events', publisher: 'NOAA NCEI', title: `Storm Events ${y}`, counties: [], mapYear: y,
  assets: kinds.map(kind => ({ id: `publisher-noaa-storm-events-${y}-${kind}`, title: `StormEvents_${kind}-ftp_v1.0_d${y}_c20250401.csv.gz`, format: 'GZIP', url: `${base}StormEvents_${kind}-ftp_v1.0_d${y}_c20250401.csv.gz`, expectedBytes: null, kind: 'download', availability: 'verified', checkedAt: '2026-10-09' })) });
const records = Array.from({ length: 15 }, (_, i) => year(2010 + i));
const text = node => typeof node === 'string' || typeof node === 'number' ? String(node) : [node?.props?.children].flat(Infinity).filter(c => c != null && c !== false).map(text).join('');
async function harness(statusPatch = {}) {
  const calls = [];
  const downloads = { connection: 'connected', busy: null, notice: '', status: { active: null, limitBytes: 500_000_000_000, jobs: [], ...statusPatch },
    startQueue: async (assets, maximum) => calls.push({ ids: assets.map(a => a.id), maximum }), cancelQueue: async () => calls.push('cancel-queue') };
  const h = await componentHarness('app/storm-events-queue.tsx', { './public-map-catalog': model, './local-download-client': { formatDownloadBytes: v => `${v} bytes` }, './downloads/workspace.module.css': css, './public-map-browser.module.css': css });
  const render = () => { const tree = h.render(h.exports.default, { records, downloads, blocked: false, showNotice: true }); h.commit(); return tree; };
  return { h, calls, render, downloads };
}
const button = (tree, label) => findNode(tree, n => n.type === 'button' && text(n).startsWith(label));

test('the queue defaults to the latest ten years of event details and needs an explicit per-file maximum', async () => {
  const q = await harness(); let tree = q.render();
  assert.match(text(tree), /File sizes are not captured by this catalog/);
  assert.doesNotMatch(text(tree), /NCEI does not list exact sizes/);
  const select = h => q.h.exports.stormEventsSelection(records, ...h);
  assert.deepEqual(select([['details'], 2023, 2024]).map(a => a.id), ['publisher-noaa-storm-events-2023-details', 'publisher-noaa-storm-events-2024-details']);
  assert.deepEqual(select([['locations', 'details'], 2024, 2024]).map(a => a.id), ['publisher-noaa-storm-events-2024-details', 'publisher-noaa-storm-events-2024-locations'], 'kind order is fixed');
  assert.equal(q.h.exports.stormEventsSelection([{ ...year(2024), assets: year(2024).assets.map(a => ({ ...a, availability: 'unverified' })) }], ['details'], 2024, 2024).length, 0);
  for (const value of ['', '0', '-1', '1e3', 'NaN']) assert.equal(q.h.exports.stormEventsLimit(value, 500_000_000_000), null);
  assert.equal(q.h.exports.stormEventsLimit('80', 500_000_000_000), 80 * 1_048_576);
  let queue = button(tree, 'Queue 10 files'); assert.ok(queue, 'latest ten years of details by default'); assert.equal(queue.props.disabled, true, 'no maximum yet');
  findNode(tree, n => n.type === 'input' && n.props.type === 'number').props.onChange({ target: { value: '80' } }); tree = q.render();
  findNode(tree, n => n.type === 'input' && n.props.type === 'checkbox' && text(findNode(tree, m => m.type === 'label' && m.props.children?.[0] === n)) === 'Fatalities')?.props.onChange();
  tree = q.render();
  queue = button(tree, 'Queue '); assert.equal(queue.props.disabled, false); queue.props.onClick();
  assert.equal(q.calls[0].maximum, 80 * 1_048_576); assert.equal(q.calls[0].ids.length, 20, 'details and fatalities for ten years');
  assert.deepEqual(q.calls[0].ids.slice(0, 2), ['publisher-noaa-storm-events-2015-details', 'publisher-noaa-storm-events-2015-fatalities']);
  assert.equal(q.calls[0].ids.at(-1), 'publisher-noaa-storm-events-2024-fatalities');
  q.h.dispose();
});

test('a running queue shows its waiting count, blocks a second queue and can be cancelled', async () => {
  const q = await harness({ active: '1'.repeat(32), queued: 7 }); const tree = q.render();
  assert.match(text(tree), /7 files are waiting after the current download/);
  findNode(tree, n => n.type === 'input' && n.props.type === 'number').props.onChange({ target: { value: '80' } });
  assert.equal(button(q.render(), 'Queue ').props.disabled, true);
  button(q.render(), 'Cancel queued files').props.onClick(); assert.deepEqual(q.calls, ['cancel-queue']); q.h.dispose();
});
