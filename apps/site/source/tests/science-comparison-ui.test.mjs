import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import { COMPARISON_PLACES } from '../app/science/compare/comparison-places.mjs';
import { comparisonLabPath, comparisonPath, comparisonSelection } from '../app/science/compare/comparison-selection.mjs';
import { componentHarness, findNode, settle } from './component-harness.mjs';

const styleNames = new Proxy({}, { get: (_target, name) => String(name) });

test('comparison URLs reject repeated, malformed and unsupported years and areas', () => {
  assert.deepEqual(comparisonSelection(''), { year: 2025, compareYear: 2024, place: 'topeka' });
  assert.deepEqual(comparisonSelection('?year=2020&compare=2022'), { year: 2020, compareYear: 2022, place: 'topeka' });
  assert.deepEqual(comparisonSelection('?year=2021&year=2022&compare=2025'), { year: 2025, compareYear: 2024, place: 'topeka' });
  assert.deepEqual(comparisonSelection('?year=2025e0&compare=2028'), { year: 2025, compareYear: 2024, place: 'topeka' });
  assert.deepEqual(comparisonSelection('?year=2022&compare=2022&place=wichita'), { year: 2022, compareYear: 2025, place: 'wichita' });
  for (const query of ['?place=foo', '?place=wichita&place=dodge-city', '?place=Wichita']) {
    assert.equal(comparisonSelection(query).place, 'topeka');
  }
  assert.equal(comparisonPath({ year: 2021, compareYear: 2024 }), '/science/compare?year=2021&compare=2024');
  assert.equal(comparisonPath({ year: 2021, compareYear: 2024, place: 'topeka' }), '/science/compare?year=2021&compare=2024');
  assert.equal(comparisonPath({ year: 2021, compareYear: 2024, place: 'dodge-city' }), '/science/compare?year=2021&compare=2024&place=dodge-city');
  assert.throws(() => comparisonPath({ year: 2024, compareYear: 2024 }), /distinct/);
  assert.throws(() => comparisonPath({ year: 2024, compareYear: 2025, place: 'unknown' }), /supported Kansas/);
});

async function comparisonHarness(t, search = '') {
  const calls = [];
  const downloads = [];
  const clipboard = [];
  const window = new EventTarget();
  window.location = { search, origin: 'https://kansasfrontiermatrix.com' };
  window.history = { pushState(_state, _title, url) { window.location.search = new URL(url, window.location.origin).search; } };
  window.print = () => { window.printed = true; };
  class DownloadUrl extends URL {
    static createObjectURL(blob) { downloads.push({ blob }); return 'blob:comparison'; }
    static revokeObjectURL() {}
  }
  const document = {
    createElement() { return { click() { downloads.at(-1).filename = this.download; }, remove() {} }; },
    body: { appendChild() {} },
  };
  const navigator = { clipboard: { async writeText(value) { clipboard.push(value); } } };
  const harness = await componentHarness('app/science/compare/comparison-client.tsx', {
    '../science-nav': { default: 'science-nav' },
    'next/link': { default: 'a' },
    './comparison-model.mjs': { buildScienceComparison: (_snapshots, selection) => ({ selection }) },
    './comparison-places.mjs': { COMPARISON_PLACES },
    './comparison-report.mjs': {
      comparisonCsv: report => `year\n${report.selection.year}\n`,
      comparisonJson: report => JSON.stringify(report),
      comparisonExportFilename: (report, ext) => `${report.selection.year}.${ext}`,
    },
    './comparison-selection.mjs': { comparisonLabPath, comparisonPath, comparisonSelection, comparisonYears: [2025, 2024, 2023, 2022, 2021, 2020] },
    './comparison-snapshots': { loadComparisonInputs: (place, signal, shared) => new Promise((resolve, reject) => calls.push({ place, signal, shared, resolve, reject })) },
    './comparison-view': { default: 'comparison-view' },
    './comparison.module.css': { default: styleNames },
  }, { window, document, navigator, URL: DownloadUrl, Blob, setTimeout: () => 0 });
  t.after(() => harness.dispose());
  function render() { const tree = harness.render(harness.exports.default); harness.commit(); return tree; }
  return { calls, downloads, clipboard, navigator, window, render };
}

const button = (tree, label) => findNode(tree, node => node.type === 'button' && node.props.children === label);
const report = tree => findNode(tree, node => node.type === 'comparison-view')?.props.report;

test('requested years change the report and downloads without refetching verified sources', async t => {
  const view = await comparisonHarness(t, '?year=2022&compare=2020');
  let tree = view.render();
  assert.equal(button(tree, 'Download CSV').props.disabled, true);
  assert.equal(view.calls.length, 1);
  view.calls[0].resolve({ snapshots: {}, evidence: {} });
  await settle();
  tree = view.render();
  assert.equal(report(tree).selection.year, 2022);
  assert.equal(report(tree).selection.compareYear, 2020);
  const select = findNode(tree, node => node.type === 'select' && node.props.value === 2022);
  select.props.onChange({ target: { value: '2020' } });
  tree = view.render();
  assert.equal(report(tree).selection.year, 2020);
  assert.equal(report(tree).selection.compareYear, 2022);
  assert.equal(view.calls.length, 1);
  assert.equal(view.window.location.search, '?year=2020&compare=2022');
  assert.ok(findNode(tree, node => node.props?.href === '/labs/daily-air-quality?county=20177&year=2020'));

  button(tree, 'Download CSV').props.onClick();
  button(tree, 'Download JSON').props.onClick();
  button(tree, 'Print report').props.onClick();
  assert.equal(view.window.printed, true);
  assert.deepEqual(view.downloads.map(item => item.filename), ['2020.csv', '2020.json']);
  assert.equal(await view.downloads[0].blob.text(), 'year\n2020\n');
  assert.deepEqual(JSON.parse(await view.downloads[1].blob.text()).selection, { year: 2020, compareYear: 2022, place: 'topeka' });

  await button(tree, 'Copy comparison link').props.onClick();
  assert.deepEqual(view.clipboard, ['https://kansasfrontiermatrix.com/science/compare?year=2020&compare=2022']);
  view.navigator.clipboard = undefined;
  await button(tree, 'Copy comparison link').props.onClick();
  const fallback = findNode(view.render(), node => node.type === 'input' && node.props.readOnly);
  assert.equal(fallback.props.value, view.clipboard[0]);
});

test('area changes share verified county data, cancel obsolete reads, and never export a stale area', async t => {
  const view = await comparisonHarness(t, '?year=2022&compare=2020&place=wichita');
  const selectArea = (tree, before, after) => findNode(tree, node => node.type === 'select' && node.props.value === before).props.onChange({ target: { value: after } });
  view.render();
  assert.equal(view.calls[0].place, 'wichita');
  const counties = { drought: {}, air: {} };
  view.calls[0].resolve({ snapshots: counties, evidence: {} });
  await settle();
  let tree = view.render();
  assert.equal(report(tree).selection.place, 'wichita');
  assert.ok(findNode(tree, node => node.props?.href === '/labs/daily-air-quality?county=20173&year=2022'));

  selectArea(tree, 'wichita', 'topeka');
  tree = view.render();
  assert.equal(button(tree, 'Download JSON').props.disabled, true);
  assert.equal(report(tree), undefined);
  assert.equal(view.calls[1].place, 'topeka');
  assert.equal(view.calls[1].shared.drought, counties.drought);
  assert.equal(view.calls[1].shared.air, counties.air);

  selectArea(tree, 'topeka', 'dodge-city');
  tree = view.render();
  assert.equal(view.calls[1].signal.aborted, true);
  assert.equal(view.calls[2].place, 'dodge-city');
  view.calls[1].resolve({ snapshots: counties, evidence: {} });
  await settle();
  assert.equal(report(view.render()), undefined);
  view.calls[2].resolve({ snapshots: counties, evidence: {} });
  await settle();
  tree = view.render();
  assert.equal(report(tree).selection.place, 'dodge-city');
  assert.equal(view.window.location.search, '?year=2022&compare=2020&place=dodge-city');
  assert.ok(findNode(tree, node => node.props?.href === '/labs/heat-and-rain?station=USW00013985&year=2022'));
  await button(tree, 'Copy comparison link').props.onClick();
  assert.match(view.clipboard[0], /&place=dodge-city$/);

  // Back to already verified data does not download any snapshot.
  selectArea(tree, 'dodge-city', 'wichita');
  assert.equal(report(view.render()).selection.place, 'wichita');
  assert.equal(view.calls.length, 3);
});

test('place loading resolves approved descriptors and reuses both previously verified county snapshots', async () => {
  const entries = ['daily-air-quality', 'heat-and-rain', 'county-drought', 'sunlight-and-sky'];
  const manifests = await Promise.all(entries.map(lab => readFile(new URL(`../app/labs/${lab}/snapshot-manifest.json`, import.meta.url), 'utf8').then(JSON.parse)));
  const calls = [];
  const loader = prefix => async (descriptor, { signal }) => {
    assert.equal(signal.aborted, false);
    calls.push(prefix);
    return { descriptor };
  };
  const harness = await componentHarness('app/science/compare/comparison-snapshots.ts', {
    ...Object.fromEntries(entries.map((lab, index) => [`../../labs/${lab}/snapshot-manifest.json`, { default: manifests[index] }])),
    '../../labs/daily-air-quality/snapshot-loader.mjs': { loadAirSnapshot: loader('air') },
    '../../labs/heat-and-rain/snapshot-loader.mjs': { loadClimateSnapshot: loader('climate') },
    '../../labs/county-drought/snapshot-loader.mjs': { loadDroughtSnapshot: loader('drought') },
    '../../labs/sunlight-and-sky/snapshot-loader.mjs': { loadSunlightSnapshot: loader('sunlight') },
    './comparison-places.mjs': await import('../app/science/compare/comparison-places.mjs'),
  });
  const signal = new AbortController().signal;
  const { loadComparisonInputs } = harness.exports;
  const wichita = await loadComparisonInputs('wichita', signal);
  assert.deepEqual(calls, ['climate', 'drought', 'air', 'sunlight']);
  assert.equal(wichita.evidence.climate.id, 'USW00003928');
  assert.equal(wichita.evidence.sunlight.id, 'wichita');
  calls.length = 0;
  const dodge = await loadComparisonInputs('dodge-city', signal, { drought: wichita.snapshots.drought, air: wichita.snapshots.air });
  assert.deepEqual(calls, ['climate', 'sunlight']);
  assert.equal(dodge.evidence.climate.id, 'USW00013985');
  assert.equal(dodge.evidence.sunlight.id, 'dodge-city');
  assert.equal(dodge.snapshots.drought, wichita.snapshots.drought);
  assert.equal(dodge.snapshots.air, wichita.snapshots.air);
  await assert.rejects(loadComparisonInputs('lawrence', signal), /supported Kansas comparison area/);
});

test('a failed snapshot aborts sibling reads and retry keeps exports disabled until all inputs verify', async t => {
  const view = await comparisonHarness(t);
  view.render();
  view.calls[0].reject(new Error('Snapshot unavailable'));
  await settle();
  const failed = view.render();
  assert.equal(view.calls[0].signal.aborted, true);
  assert.equal(button(failed, 'Download JSON').props.disabled, true);
  assert.ok(findNode(failed, node => node.props?.role === 'alert'));
  button(failed, 'Retry comparison').props.onClick();
  assert.equal(button(view.render(), 'Download JSON').props.disabled, true);
  assert.equal(view.calls.length, 2);
  view.calls[1].resolve({ snapshots: {}, evidence: {} });
  await settle();
  const ready = view.render();
  assert.equal(report(ready).selection.year, 2025);
  assert.equal(button(ready, 'Download JSON').props.disabled, false);
});

test('the science landing page links to the comparison route', async () => {
  const science = await readFile(new URL('../app/science/page.tsx', import.meta.url), 'utf8');
  assert.match(science, /href="\/science\/compare"/);
});
