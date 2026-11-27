import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import { comparisonLabPath, comparisonPath, comparisonSelection } from '../app/science/compare/comparison-selection.mjs';
import { componentHarness, findNode, settle } from './component-harness.mjs';

const styleNames = new Proxy({}, { get: (_target, name) => String(name) });

test('comparison URLs reject repeated, malformed and unsupported years', () => {
  assert.deepEqual(comparisonSelection(''), { year: 2025, compareYear: 2024 });
  assert.deepEqual(comparisonSelection('?year=2020&compare=2022'), { year: 2020, compareYear: 2022 });
  assert.deepEqual(comparisonSelection('?year=2021&year=2022&compare=2025'), { year: 2025, compareYear: 2024 });
  assert.deepEqual(comparisonSelection('?year=2025e0&compare=2028'), { year: 2025, compareYear: 2024 });
  assert.deepEqual(comparisonSelection('?year=2022&compare=2022'), { year: 2022, compareYear: 2025 });
  assert.equal(comparisonPath({ year: 2021, compareYear: 2024 }), '/science/compare?year=2021&compare=2024');
  assert.throws(() => comparisonPath({ year: 2024, compareYear: 2024 }), /distinct/);
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
    'next/link': { default: 'a' },
    './comparison-model.mjs': { buildScienceComparison: (_snapshots, selection) => ({ selection }) },
    './comparison-report.mjs': {
      comparisonCsv: report => `year\n${report.selection.year}\n`,
      comparisonJson: report => JSON.stringify(report),
      comparisonExportFilename: (report, ext) => `${report.selection.year}.${ext}`,
    },
    './comparison-selection.mjs': { comparisonLabPath, comparisonPath, comparisonSelection, comparisonYears: [2025, 2024, 2023, 2022, 2021, 2020] },
    './comparison-snapshots': { loadComparisonInputs: signal => new Promise((resolve, reject) => calls.push({ signal, resolve, reject })) },
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
  assert.deepEqual(JSON.parse(await view.downloads[1].blob.text()).selection, { year: 2020, compareYear: 2022 });

  await button(tree, 'Copy comparison link').props.onClick();
  assert.deepEqual(view.clipboard, ['https://kansasfrontiermatrix.com/science/compare?year=2020&compare=2022']);
  view.navigator.clipboard = undefined;
  await button(tree, 'Copy comparison link').props.onClick();
  const fallback = findNode(view.render(), node => node.type === 'input' && node.props.readOnly);
  assert.equal(fallback.props.value, view.clipboard[0]);
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
