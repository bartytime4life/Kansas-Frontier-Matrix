import test from 'node:test';
import assert from 'node:assert/strict';
import { climateAnnualAnalysis, groupSummaries, quantile, rankRecords, relationship, sampledPairs, scienceMetrics, scientificSummary, yearlySeries } from '../app/living-welcome/stories/science-model.mjs';

const near = (actual, expected) => assert.ok(Math.abs(actual - expected) < 1e-10, `${actual} != ${expected}`);
test('type 7 quartiles and sample standard deviation preserve zero and ignore missing values', () => {
  const summary = scientificSummary([0, 2, 4, 6, null, '8'].map(value => ({ value })), 'value');
  assert.equal(summary.count, 4); assert.equal(summary.missing, 2); assert.equal(summary.q1, 1.5); assert.equal(summary.median, 3); assert.equal(summary.q3, 4.5);
  near(summary.standardDeviation, Math.sqrt(20 / 3));
  assert.equal(quantile([], .5), null); assert.equal(quantile([0], .5), 0);
  assert.equal(scientificSummary([{ v: 2 }], 'v').standardDeviation, null);
});
test('complete-case Pearson and OLS recover exact positive and negative relationships', () => {
  const rows = [{ x: 0, y: 1 }, { x: 1, y: 3 }, { x: 2, y: 5 }, { x: null, y: 7 }, { x: 4, y: '9' }];
  const fit = relationship(rows, 'x', 'y');
  assert.equal(fit.count, 3); assert.equal(fit.excluded, 2); near(fit.pearson, 1); near(fit.spearman, 1); near(fit.slope, 2); near(fit.intercept, 1); near(fit.rSquared, 1);
  near(relationship(rows.slice(0, 3).map(row => ({ x: row.x, y: -row.y })), 'x', 'y').pearson, -1);
});
test('Spearman uses average ranks for ties rather than the untied shortcut', () => {
  const fit = relationship([{ x: 1, y: 1 }, { x: 1, y: 2 }, { x: 2, y: 3 }, { x: 3, y: 3 }], 'x', 'y');
  near(fit.spearman, 8 / 9);
});
test('constant axes and insufficient pairs never emit a false coefficient', () => {
  for (const rows of [[{ x: 1, y: 1 }, { x: 2, y: 2 }], [1, 2, 3].map(y => ({ x: 2, y }))]) {
    const fit = relationship(rows, 'x', 'y');
    assert.equal(fit.pearson, null); assert.equal(fit.spearman, null); assert.equal(fit.rSquared, null); assert.equal(fit.slope, null); assert.ok(fit.reason);
  }
});
test('groups retain missing measurements and unclassified source rows; rankings ignore missing', () => {
  const records = [{ id: 'a', g: 'A', v: 0 }, { id: 'b', g: 'A', v: null }, { id: 'c', g: null, v: 6 }], groups = groupSummaries(records, 'v', 'g');
  assert.deepEqual(groups.map(g => [g.label, g.total, g.count, g.missing, g.mean]), [['A', 2, 1, 1, 0], ['Not recorded', 1, 1, 0, 6]]);
  assert.deepEqual(rankRecords(records, 'v', 'asc').map(row => row.id), ['a', 'c']);
  assert.deepEqual(rankRecords(records, 'v').map(row => row.id), ['c', 'a']);
});
test('deterministic mark sampling never changes the full analytical pair count', () => {
  const fit = relationship(Array.from({ length: 5000 }, (_, x) => ({ x, y: x * 2 })), 'x', 'y');
  assert.equal(sampledPairs(fit.pairs).length, 1800); assert.equal(fit.count, 5000); near(fit.pearson, 1);
  assert.deepEqual(sampledPairs(fit.pairs, 3).map(pair => pair.x), [0, 1666, 3333]);
});
test('scientific measure choices exclude flags and explicit non-analysis fields', () => {
  assert.deepEqual(scienceMetrics({ metrics: [{ key: 'length' }, { key: 'estimatedRatingFlag' }, { key: 'conditionCode' }, { key: 'value', analysis: false }] }).map(c => c.key), ['length']);
});
test('numeric year trends preserve sources and missing-only years without invented dates', () => {
  assert.deepEqual(yearlySeries([{ year: 2000, v: 0, g: 'A' }, { year: 2000, v: 2, g: 'A' }, { year: 2000, v: 8, g: 'B' }, { year: 2001, v: null, g: 'A' }], 'year', 'v', 'g').map(row => [row.year, row.category, row.mean, row.missing]), [[2000, 'A', 1, 0], [2000, 'B', 8, 0], [2001, 'A', null, 1]]);
});
test('climate trend uses complete years from the selected analysis period and precipitation sums', () => {
  const years = [2000, 2001, 2002, 2003, 2004], values = [0, 1, 3, 5, 100].flatMap(value => Array(12).fill(value)); values[59] = null;
  const bundle = { data: { years, values: { tmpc: { '20': values }, pcpn: { '20': values } }, normals: { '1901-2000': { tmpc: { '20': Array(12).fill(1) }, pcpn: { '20': Array(12).fill(1) } } } } };
  const result = climateAnnualAnalysis(bundle, { from: 2001, to: 2004 });
  assert.equal(result.count, 3); assert.equal(result.incomplete, 1); near(result.slopePerDecade, 20); near(result.rSquared, 1);
  assert.equal(result.lowest.year, 2001); assert.equal(result.highest.year, 2003); assert.equal(result.rows[0].anomaly, 0);
  near(climateAnnualAnalysis(bundle, { element: 'pcpn', from: 2001, to: 2003 }).slopePerDecade, 240);
  assert.equal(climateAnnualAnalysis(bundle, { from: 2003, to: 2001 }).count, 0);
  bundle.data.elements = { tmpc: { scale: 10, annual: 'mean' } };
  const scaled = climateAnnualAnalysis(bundle, { from: 2001, to: 2003 });
  near(scaled.slopePerDecade, 2); near(scaled.rows[0].value, .1); near(scaled.rows[0].anomaly, 0);
});
