import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import { componentHarness, findNode } from './component-harness.mjs';
import { PUBLIC_LAB_SNAPSHOTS } from '../app/labs/public-snapshots.mjs';
import * as model from '../app/labs/population-components.mjs';

const manifest = PUBLIC_LAB_SNAPSHOTS['census-mosaic'];
const bundle = JSON.parse(await readFile('public' + manifest.path, 'utf8'));
const styles = new Proxy({}, { get: (_target, key) => String(key) });
const text = node => typeof node === 'string' || typeof node === 'number' ? String(node)
  : node && typeof node === 'object' ? [node.props?.children].flat(Infinity).map(text).join('') : '';
function nodes(tree, predicate) {
  const result = [];
  function visit(node) {
    if (!node || typeof node !== 'object') return;
    if (predicate(node)) result.push(node);
    for (const child of [node.props?.children].flat(Infinity)) visit(child);
  }
  visit(tree);
  return result;
}
async function component(t) {
  const downloads = [];
  const harness = await componentHarness('app/labs/observatory/PopulationBalance.jsx', {
    '../../living-welcome/stories/story-kit.mjs': { downloadCSV: (filename, rows) => downloads.push({ filename, rows }) },
    '../population-components.mjs': model,
    './population-balance.module.css': { default: styles },
  });
  t.after(() => harness.dispose());
  const expand = node => {
    if (Array.isArray(node)) return node.map(expand);
    if (!node || typeof node !== 'object') return node;
    if (typeof node.type === 'function') return expand(harness.render(node.type, node.props));
    return { ...node, props: { ...node.props, children: expand(node.props?.children) } };
  };
  return { harness, downloads, render: (analysis, name = 'default') => expand(harness.render(harness.exports[name], { analysis })) };
}

test('the real population analysis composes both public counties, signed quantitative bars and exact subtotals', async t => {
  const ui = await component(t);
  const analysis = model.populationBalanceReport(bundle, { fipsA: '20177', fipsB: '20001', year: 2021 }, manifest);
  const tree = ui.render(analysis);
  assert.equal(tree.props.id, 'population-balance'); assert.equal(tree.props['data-year'], 2021);
  const counties = nodes(tree, node => node.type === 'article' && node.props['data-population-county']);
  assert.deepEqual(counties.map(node => node.props['data-population-county']), ['20177', '20001']);
  for (const [index, result] of [analysis.countyA, analysis.countyB].entries()) {
    const county = counties[index];
    assert.equal(county.props['data-status'], 'ready'); assert.ok(text(county).includes(result.name));
    const rows = nodes(county, node => node.type === 'tr' && node.props['data-component']);
    assert.equal(rows.length, 6);
    const deaths = rows.find(row => row.props['data-component'] === 'deaths');
    assert.equal(deaths.props['data-people'], -result.deaths);
    const subtotal = rows.find(row => row.props['data-component'] === 'naturalChange');
    assert.equal(subtotal.props['data-subtotal'], true);
    assert.ok(text(subtotal).includes('not an additional component'));
    const bars = nodes(county, node => node.type === 'rect' && node.props['data-waterfall-component']);
    assert.deepEqual(bars.map(node => node.props['data-waterfall-component']), ['births', 'deaths', 'netMigration', 'remainder', 'change']);
    assert.equal(bars.at(-1).props['data-from'], 0); assert.equal(bars.at(-1).props['data-to'], result.change);
    for (const bar of bars) assert.ok(Math.abs(bar.props['data-to'] - bar.props['data-from'] - bar.props['data-people']) < 1e-9);
    assert.ok(bars.some(bar => bar.props.height > 0));
    const plot = findNode(county, node => node.type === 'svg');
    assert.ok(plot.props['aria-label'].includes('Exact values follow in the table'));
    assert.equal(plot.props['aria-describedby'], `population-balance-values-${index ? 'B' : 'A'}`);
    assert.ok(text(county).includes('mean estimated residents'));
  }
  assert.ok(text(tree).includes(manifest.sha256));
  assert.ok(findNode(tree, node => node.type === 'a' && node.props.href === manifest.path && node.props.download));
  const download = findNode(tree, node => node.type === 'button' && text(node) === 'Download population history CSV ↓');
  download.props.onClick();
  assert.equal(ui.downloads[0].filename, 'kfm-population-components-history.csv');
  assert.equal(ui.downloads[0].rows.length, 11, 'the real export function supplies both full five-year histories');
  assert.deepEqual(ui.downloads[0].rows, model.populationBalanceCsv(analysis));
});

test('2020 keeps named county context and real history while selected and print views explain unavailable balances', async t => {
  const ui = await component(t);
  const analysis = model.populationBalanceReport(bundle, { fipsA: '20177', fipsB: '20001', year: 2020 }, manifest);
  const tree = ui.render(analysis);
  const counties = nodes(tree, node => node.type === 'article' && node.props['data-population-county']);
  for (const [index, result] of [analysis.countyA, analysis.countyB].entries()) {
    assert.equal(counties[index].props['data-status'], 'unavailable');
    assert.ok(text(counties[index]).includes(result.name));
    assert.match(text(counties[index]), /partial year/);
    assert.equal(nodes(counties[index], node => node.type === 'svg').length, 0, 'unavailable does not become a zero plot');
    assert.equal(nodes(counties[index], node => node.props?.['data-component']).length, 0);
  }
  assert.equal(nodes(tree, node => node.type === 'tr' && node.props['data-history-year']).length, 10);
  const print = ui.render(analysis, 'PopulationBalancePrint');
  assert.match(text(print), /2020/); assert.match(text(print), /partial year/);
  assert.ok(text(print).includes(manifest.sha256));
  assert.equal(nodes(print, node => node.type === 'svg').length, 0);
});

test('ready population print tables inherit report styling and retain exact signed counts and calculated rates', async t => {
  const ui = await component(t);
  const analysis = model.populationBalanceReport(bundle, { fipsA: '20177', fipsB: '20001', year: 2021 }, manifest);
  const screen = ui.render(analysis);
  const screenTables = nodes(screen, node => node.type === 'table' && node.props.className === 'exactTable');
  assert.equal(screenTables.length, 2, 'the real screen composition still applies its named table style');
  const print = ui.render(analysis, 'PopulationBalancePrint');
  const printTables = nodes(print, node => node.type === 'table');
  assert.equal(printTables.length, 2, 'both ready counties print their real exact-value tables');
  const values = table => nodes(table, node => node.type === 'tr' && node.props['data-component']).map(row => ({
    component: row.props['data-component'], people: row.props['data-people'], per1000: row.props['data-per1000'],
    cells: nodes(row, node => node.type === 'td').map(text),
  }));
  for (const [index, result] of [analysis.countyA, analysis.countyB].entries()) {
    assert.equal(printTables[index].props.className, undefined, 'printed exact-value tables inherit the white report styling instead of the dark screen class');
    const rows = values(printTables[index]);
    assert.equal(rows.length, 6, 'print retains four contributions, the natural-change subtotal and net change');
    assert.deepEqual(rows, values(screenTables[index]), 'print retains the full-precision signed metadata and rendered count/rate cells');
    for (const contribution of result.contributions) {
      const row = rows.find(row => row.component === contribution.key);
      assert.equal(row.people, contribution.people); assert.equal(row.per1000, contribution.per1000);
    }
    assert.ok(text(print).includes(result.name));
  }
  assert.ok(text(print).includes('Mean estimated population denominator'));
  assert.ok(text(print).includes(manifest.sha256));
});
