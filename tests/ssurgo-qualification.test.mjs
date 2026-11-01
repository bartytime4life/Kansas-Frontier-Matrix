import test from 'node:test';
import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { queries, qualifySsurgo, SDA_URL, HORIZON_COLUMNS } from '../scripts/qualify-ssurgo.mjs';

const table = (columns, rows) => JSON.stringify({ Table: [columns, ...rows] });
const unitColumns = ['attributekey', 'attributecolumnname', 'attributename', 'attributeuomabbrev', 'horzaggmeth'];
const componentColumns = ['mukey', 'components', 'unique_components', 'pct_count', 'min_pct', 'max_pct', 'pct', 'major'];
const polygonColumns = ['mukey', 'polygons', 'unique_polygons'];
const surveyColumns = ['areasymbol', 'areaname', 'saversion', 'saverest'];
const rawUnits = ['cm/cm', 'percent', 'g/cm3', 'um/s', 'percent', null, 'percent'];
const units = [...HORIZON_COLUMNS.map((column, i) => [String(i + 1), column, `${column} attribute`, rawUnits[i], 'Weighted Average']),
  ['101', 'awc_r', 'Available Water Storage', 'cm', 'Weighted Sum']];
/** A fake Soil Data Access that answers each fixed query by name; `change` replaces one answer. */
function sda(area, change = {}) {
  const text = queries(area), seen = [];
  const answers = {
    survey: table(surveyColumns, [[area, 'Fixture County, Kansas', '7', '8/27/2026 2:33:36 PM']]),
    mapunits: table(['mukey', 'musym', 'muname', 'mukind', 'muacres'], [['1', 'A', 'Alpha silt loam', 'Consociation', '300'], ['2', 'B', 'Beta-Gamma complex', 'Complex', '700']]),
    components: table(componentColumns, [['1', '2', '2', '2', '30', '70', '100', '1'], ['2', '3', '3', '3', '20', '50', '100', '2']]),
    polygons: table(polygonColumns, [['1', '4', '4'], ['2', '9', '9']]),
    units: table(unitColumns, units),
    ...change,
  };
  const fetcher = async (url, init) => {
    assert.equal(url, SDA_URL); assert.equal(init.method, 'POST');
    const { query, format } = JSON.parse(init.body); assert.equal(format, 'JSON+COLUMNNAME');
    let name = Object.keys(text).find(key => text[key] === query); assert.ok(name, 'only the fixed queries are sent');
    if (name === 'survey' && seen.includes('survey')) name = 'surveyEnd';
    seen.push(name);
    return new Response(name === 'surveyEnd' ? answers.surveyEnd ?? answers.survey : answers[name], { status: 200 });
  };
  return { fetcher, seen, answers };
}

test('a whole survey area is ready for owner review, with every query and response digested', async () => {
  const { fetcher, seen, answers } = sda('KS999');
  const report = await qualifySsurgo('KS999', { fetcher, expectedVersion: 7, now: () => Date.parse('2026-10-31T20:00:00Z') });
  assert.deepEqual(seen, ['survey', 'mapunits', 'components', 'polygons', 'units', 'surveyEnd']);
  assert.equal(report.format, 'kfm-ssurgo-qualification-v2'); assert.equal(report.expectedVersion, 7);
  assert.equal(report.state, 'ready-for-owner-review'); assert.deepEqual(report.holds, []);
  assert.deepEqual(report.survey, { name: 'Fixture County, Kansas', version: '7', savedAt: '8/27/2026 2:33:36 PM' });
  assert.deepEqual({ count: report.mapUnits.count, acres: report.mapUnits.acres, byKind: report.mapUnits.byKind }, { count: 2, acres: 1000, byKind: { Consociation: 1, Complex: 1 } });
  assert.equal(report.mapUnits.largest[0].mukey, '2');
  assert.deepEqual(report.components, { mapUnitsWithComponents: 2, total: 5 });
  assert.deepEqual(report.polygons, { count: 13, mapUnits: 2, unmapped: [], orphaned: [] });
  // awc_r is published per horizon and as depth-summed storage, so its unit depends on the attribute.
  assert.deepEqual(report.findings, [{ code: 'UNIT_DEPENDS_ON_ATTRIBUTE', columns: [{ column: 'awc_r', units: ['cm/cm', 'cm'] }] }]);
  assert.equal(report.horizonUnits.find(u => u.column === 'awc_r').rawUnit, 'cm/cm');
  assert.deepEqual(report.horizonUnits.find(u => u.column === 'ph1to1h2o_r').units, [null], 'pH is published without a unit');
  assert.equal(report.receipts.length, 6);
  const sha = s => createHash('sha256').update(s).digest('hex');
  for (const receipt of report.receipts) {
    assert.equal(receipt.querySha256, sha(receipt.query));
    assert.equal(receipt.responseSha256, sha(answers[receipt.name === 'surveyEnd' ? 'survey' : receipt.name]));
  }
  assert.deepEqual([report.rights, report.admitted, report.capture, report.publication], ['REVIEW_REQUIRED', false, false, false]);
});

test('a map unit without polygons, a stray polygon or missing components holds the area', async () => {
  const { fetcher } = sda('KS998', {
    components: table(componentColumns, [['1', '2', '2', '2', '40', '50', '90', '0']]),
    polygons: table(polygonColumns, [['1', '4', '4'], ['3', '1', '1']]),
  });
  const report = await qualifySsurgo('KS998', { fetcher });
  assert.equal(report.state, 'held');
  assert.deepEqual(report.holds, ['MAP_UNITS_WITHOUT_COMPONENTS', 'COMPONENT_PERCENT_NOT_100', 'NO_MAJOR_COMPONENT', 'SPATIAL_TABULAR_MISMATCH']);
  assert.deepEqual(report.polygons, { count: 5, mapUnits: 2, unmapped: ['2'], orphaned: ['3'] });
  assert.deepEqual(report.findings.slice(0, 2), [{ code: 'COMPONENT_PERCENT_NOT_100', mapUnits: [{ mukey: '1', pct: 90 }] }, { code: 'NO_MAJOR_COMPONENT', mapUnits: ['1'] }]);
});

test('an unknown survey area and an unpublished unit are holds, not empty success', async () => {
  const { fetcher } = sda('KS997', { survey: '{}', mapunits: '{}', components: '{}', polygons: '{}',
    units: table(unitColumns, units.filter(([, column]) => column !== 'om_r')) });
  const report = await qualifySsurgo('KS997', { fetcher });
  assert.deepEqual(report.holds, ['SURVEY_AREA_NOT_FOUND', 'SURVEY_IDENTITY_INVALID', 'NO_MAP_UNITS', 'HORIZON_UNITS_UNPUBLISHED']);
  assert.equal(report.survey, null);
});

test('a dimensional property published without a unit is a hold; unitless pH is not', async () => {
  const blank = units.map(([id, column, name, unit, agg]) => [id, column, name, column === 'ksat_r' ? null : column === 'dbthirdbar_r' ? '' : unit, agg]);
  const { fetcher } = sda('KS996', { units: table(unitColumns, blank) });
  const report = await qualifySsurgo('KS996', { fetcher });
  assert.equal(report.state, 'held'); assert.deepEqual(report.holds, ['HORIZON_UNITS_UNPUBLISHED']);
  assert.deepEqual(report.findings.find(f => f.code === 'HORIZON_UNITS_UNPUBLISHED'), { code: 'HORIZON_UNITS_UNPUBLISHED', columns: ['dbthirdbar_r', 'ksat_r'] });
  assert.deepEqual(report.horizonUnits.find(u => u.column === 'dbthirdbar_r').units, [null], 'an empty unit is no unit');
  const none = units.map(([id, column, name, , agg]) => [id, column, name, null, agg]);
  const all = await qualifySsurgo('KS996', { fetcher: sda('KS996', { units: table(unitColumns, none) }).fetcher });
  assert.deepEqual(all.findings.find(f => f.code === 'HORIZON_UNITS_UNPUBLISHED').columns, HORIZON_COLUMNS.filter(c => c !== 'ph1to1h2o_r'));
});

test('only a Kansas survey area symbol reaches a query, and a failed query fails closed', async () => {
  let calls = 0; const counting = async () => { calls++; return new Response('{}'); };
  for (const area of ['NE001', 'KS16', "KS169' OR 1=1 --", undefined]) await assert.rejects(qualifySsurgo(area, { fetcher: counting }), /AREA_SYMBOL_INVALID/);
  assert.equal(calls, 0);
  const xml = async () => new Response('<?xml version="1.0"?><ServiceExceptionReport><ServiceException>Invalid query</ServiceException></ServiceExceptionReport>');
  await assert.rejects(qualifySsurgo('KS169', { fetcher: xml }), /SDA_QUERY_FAILED/);
  await assert.rejects(qualifySsurgo('KS169', { fetcher: async () => new Response('busy', { status: 503 }) }), /SDA_QUERY_FAILED/);
  await assert.rejects(qualifySsurgo('KS169', { fetcher: async () => new Response(JSON.stringify({ Table: [['a', 'b'], ['1']] })) }), /SDA_RESPONSE_INVALID/);
});

test('a valid sibling never masks absent units, including whitespace', async () => {
  for (const unit of [null, '', ' \t ']) {
    const changed = [...units, ['900', 'ksat_r', 'Second Ksat attribute', unit, 'Weighted Average']];
    const report = await qualifySsurgo('KS169', { fetcher: sda('KS169', { units: table(unitColumns, changed) }).fetcher });
    assert.equal(report.state, 'held');
    assert.ok(report.findings.find(f => f.code === 'HORIZON_UNITS_UNPUBLISHED').columns.includes('ksat_r'));
  }
});

test('contradictory units fail closed for every dimensional column and pH', async () => {
  for (const column of HORIZON_COLUMNS) {
    const changed = units.map(row => row[1] === column ? row.map((v, i) => i === 3 ? 'meters' : v) : row);
    const report = await qualifySsurgo('KS169', { fetcher: sda('KS169', { units: table(unitColumns, changed) }).fetcher });
    assert.equal(report.state, 'held', column); assert.ok(report.holds.includes('HORIZON_UNITS_CONTRADICTORY'), column);
  }
});

test('AWC capacity and depth-integrated storage retain separate meanings', async () => {
  for (const [index, value] of [[0, '999'], [2, 'Unreviewed storage'], [3, 'cm/cm'], [4, 'Weighted Average']]) {
    const changed = units.map(row => row[0] === '101' ? row.map((v, i) => i === index ? value : v) : row);
    const report = await qualifySsurgo('KS169', { fetcher: sda('KS169', { units: table(unitColumns, changed) }).fetcher });
    assert.equal(report.state, 'held'); assert.ok(report.holds.includes('HORIZON_UNITS_CONTRADICTORY'));
  }
  const storageOnly = units.filter(row => row[1] !== 'awc_r' || row[0] === '101');
  const report = await qualifySsurgo('KS169', { fetcher: sda('KS169', { units: table(unitColumns, storageOnly) }).fetcher });
  assert.ok(report.holds.includes('HORIZON_UNITS_UNPUBLISHED'), 'storage does not qualify raw AWC');
});

test('duplicate attribute identities and unknown aggregation cannot qualify', async () => {
  for (const changed of [[...units, units[0]], [...units, ['999', 'unexpected_r', 'Unexpected property', 'cm', 'Weighted Average']],
    units.map((row, i) => i === 1 ? row.map((v, j) => j === 0 ? '1' : v) : row),
    units.map((row, i) => i === 1 ? row.map((v, j) => j === 2 ? units[0][2] : v) : row),
    units.map((row, i) => i === 0 ? row.map((v, j) => j === 4 ? 'Unreviewed' : v) : row)]) {
    const report = await qualifySsurgo('KS169', { fetcher: sda('KS169', { units: table(unitColumns, changed) }).fetcher });
    assert.ok(report.holds.includes('HORIZON_UNITS_CONTRADICTORY'));
  }
});

test('component counts, individual percentages and relationship groups fail closed', async () => {
  const good = ['1', '2', '2', '2', '30', '70', '100', '1'];
  for (const [index, value] of [[0, null], [1, '0'], [1, '1.5'], [1, ''], [2, '1'], [3, '1'], [4, null],
    [4, '-5'], [5, '101'], [5, '20'], [6, null], [6, '99'], [7, '0'], [7, '3']]) {
    const row = good.map((v, i) => i === index ? value : v);
    const report = await qualifySsurgo('KS169', { fetcher: sda('KS169', { components: table(componentColumns, [row, ['2', '1', '1', '1', '100', '100', '100', '1']]) }).fetcher });
    assert.equal(report.state, 'held', `${index}: ${value}`);
  }
  for (const rows of [[good, good], [good, ['9', '1', '1', '1', '100', '100', '100', '1']]]) {
    const report = await qualifySsurgo('KS169', { fetcher: sda('KS169', { components: table(componentColumns, rows) }).fetcher });
    assert.ok(report.holds.includes('COMPONENT_VALUES_INVALID'));
  }
});

test('polygon presence requires positive integer counts and unique groups', async () => {
  for (const value of [null, '', ' ', '0', '-1', '1.5', 'NaN']) {
    const report = await qualifySsurgo('KS169', { fetcher: sda('KS169', { polygons: table(polygonColumns, [['1', value, value], ['2', '1', '1']]) }).fetcher });
    assert.ok(report.holds.includes('POLYGON_VALUES_INVALID'), String(value));
  }
  for (const rows of [[['1', '1', '1'], ['1', '2', '2']], [['1', '2', '1'], ['2', '1', '1']]]) {
    const report = await qualifySsurgo('KS169', { fetcher: sda('KS169', { polygons: table(polygonColumns, rows) }).fetcher });
    assert.ok(report.holds.includes('POLYGON_VALUES_INVALID'));
  }
});

test('invalid map-unit identity or acreage is never coerced into success', async () => {
  for (const [index, value] of [[0, null], [0, ''], [1, ' '], [2, null], [3, ''], [4, null], [4, ''], [4, '-1'], [4, 'NaN']]) {
    const row = ['1', 'A', 'Alpha', 'Consociation', '1'].map((v, i) => i === index ? value : v);
    const report = await qualifySsurgo('KS169', { fetcher: sda('KS169', { mapunits: table(['mukey', 'musym', 'muname', 'mukind', 'muacres'], [row]) }).fetcher });
    assert.ok(report.holds.includes('MAP_UNIT_VALUES_INVALID'), `${index}: ${value}`);
  }
});

test('survey identity, expected version and before/after revision checks fail closed', async () => {
  const good = ['KS169', 'Fixture County, Kansas', '7', '8/27/2026 2:33:36 PM'];
  for (const [index, value] of [[0, 'KS170'], [1, ''], [2, null], [2, '0'], [2, '1.5'], [3, null], [3, 'invalid']]) {
    const row = good.map((v, i) => i === index ? value : v);
    const report = await qualifySsurgo('KS169', { fetcher: sda('KS169', { survey: table(surveyColumns, [row]) }).fetcher });
    assert.ok(report.holds.includes('SURVEY_IDENTITY_INVALID'), `${index}: ${value}`);
  }
  const mismatch = await qualifySsurgo('KS169', { fetcher: sda('KS169').fetcher, expectedVersion: 23 });
  assert.ok(mismatch.holds.includes('SURVEY_VERSION_MISMATCH'));
  for (const row of [good.map((v, i) => i === 2 ? '8' : v), good.map((v, i) => i === 3 ? '8/28/2026 2:33:36 PM' : v)]) {
    const drift = await qualifySsurgo('KS169', { fetcher: sda('KS169', { surveyEnd: table(surveyColumns, [row]) }).fetcher, expectedVersion: 7 });
    assert.ok(drift.holds.includes('SURVEY_CHANGED_DURING_QUALIFICATION'));
    assert.equal(drift.admitted, false); assert.equal(drift.capture, false); assert.equal(drift.publication, false);
  }
  let calls = 0;
  for (const expectedVersion of [null, '', 0, -1, 1.5, '23 OR 1=1']) {
    await assert.rejects(qualifySsurgo('KS169', { expectedVersion, fetcher: async () => { calls++; } }), /SURVEY_VERSION_INVALID/);
  }
  assert.equal(calls, 0);
});

test('wrong, duplicate, missing and malformed response columns fail closed', async () => {
  const good = ['KS169', 'Fixture County, Kansas', '7', '8/27/2026 2:33:36 PM'];
  for (const response of [null, [], { Error: 'bad query' }, { Table: [] }, { Table: null },
    { Table: [['areasymbol', 'areaname', 'saversion', 'saversion'], good] },
    { Table: [['areasymbol', 'areaname', 'saversion', 'unexpected'], good] },
    { Table: [surveyColumns, [good[0], {}, good[2], good[3]]] },
    { Table: [surveyColumns, good], Table1: [surveyColumns, good] }]) {
    await assert.rejects(qualifySsurgo('KS169', { fetcher: async () => new Response(JSON.stringify(response)) }), /SDA_RESPONSE_INVALID/);
  }
  const oversized = ' '.repeat(4 * 1024 ** 2 + 1);
  await assert.rejects(qualifySsurgo('KS169', { fetcher: async () => new Response(oversized) }), /SDA_QUERY_FAILED/);
  await assert.rejects(qualifySsurgo('KS169', { fetcher: async () => { throw new Error('network'); } }), /network/);
});

test('CLI rejects incomplete, repeated and unknown options before requesting data', () => {
  const script = fileURLToPath(new URL('../scripts/qualify-ssurgo.mjs', import.meta.url));
  for (const args of [['KS169', '--expected-version'], ['KS169', '--expected-version', '0'],
    ['KS169', '--expected-version', '23', '--expected-version', '23'], ['KS169', '--out'],
    ['KS169', '--out', 'a.json', '--out', 'b.json'], ['KS169', '--out', 'a.json', 'extra']]) {
    const result = spawnSync(process.execPath, [script, ...args], { encoding: 'utf8', timeout: 5000 });
    assert.equal(result.status, 1, JSON.stringify(args)); assert.equal(result.stdout, '');
    assert.equal(JSON.parse(result.stderr).state, 'held');
  }
});
