import test from 'node:test';
import assert from 'node:assert/strict';
import { queries, qualifySsurgo, SDA_URL, HORIZON_COLUMNS } from '../scripts/qualify-ssurgo.mjs';

const table = (columns, rows) => JSON.stringify({ Table: [columns, ...rows] });
const units = [...HORIZON_COLUMNS.map(column => [column, `${column} attribute`, column === 'ph1to1h2o_r' ? null : 'percent']),
  ['awc_r', 'Available Water Storage', 'cm']];
/** A fake Soil Data Access that answers each fixed query by name; `change` replaces one answer. */
function sda(area, change = {}) {
  const text = queries(area), seen = [];
  const answers = {
    survey: table(['areasymbol', 'areaname', 'saversion', 'saverest'], [[area, 'Fixture County, Kansas', '7', '8/27/2026 2:33:36 PM']]),
    mapunits: table(['mukey', 'musym', 'muname', 'mukind', 'muacres'], [['1', 'A', 'Alpha silt loam', 'Consociation', '300'], ['2', 'B', 'Beta-Gamma complex', 'Complex', '700']]),
    components: table(['mukey', 'components', 'pct', 'major'], [['1', '2', '100', '1'], ['2', '3', '100', '2']]),
    polygons: table(['mukey', 'polygons'], [['1', '4'], ['2', '9']]),
    units: table(['attributecolumnname', 'attributename', 'attributeuomabbrev'], units),
    ...change,
  };
  const fetcher = async (url, init) => {
    assert.equal(url, SDA_URL); assert.equal(init.method, 'POST');
    const { query, format } = JSON.parse(init.body); assert.equal(format, 'JSON+COLUMNNAME');
    const name = Object.keys(text).find(key => text[key] === query); assert.ok(name, 'only the fixed queries are sent');
    seen.push(name);
    return new Response(answers[name], { status: 200 });
  };
  return { fetcher, seen };
}

test('a whole survey area is ready for owner review, with every query and response digested', async () => {
  const { fetcher, seen } = sda('KS999');
  const report = await qualifySsurgo('KS999', { fetcher, now: () => Date.parse('2026-10-31T20:00:00Z') });
  assert.deepEqual(seen, ['survey', 'mapunits', 'components', 'polygons', 'units']);
  assert.equal(report.state, 'ready-for-owner-review'); assert.deepEqual(report.holds, []);
  assert.deepEqual(report.survey, { name: 'Fixture County, Kansas', version: '7', savedAt: '8/27/2026 2:33:36 PM' });
  assert.deepEqual({ count: report.mapUnits.count, acres: report.mapUnits.acres, byKind: report.mapUnits.byKind }, { count: 2, acres: 1000, byKind: { Consociation: 1, Complex: 1 } });
  assert.equal(report.mapUnits.largest[0].mukey, '2');
  assert.deepEqual(report.components, { mapUnitsWithComponents: 2, total: 5 });
  assert.deepEqual(report.polygons, { count: 13, mapUnits: 2, unmapped: [], orphaned: [] });
  // awc_r is published per horizon and as depth-summed storage, so its unit depends on the attribute.
  assert.deepEqual(report.findings, [{ code: 'UNIT_DEPENDS_ON_ATTRIBUTE', columns: [{ column: 'awc_r', units: ['percent', 'cm'] }] }]);
  assert.deepEqual(report.horizonUnits.find(u => u.column === 'ph1to1h2o_r').units, [null], 'pH is published without a unit');
  assert.equal(report.receipts.length, 5);
  assert.ok(report.receipts.every(r => /^[a-f0-9]{64}$/.test(r.querySha256) && /^[a-f0-9]{64}$/.test(r.responseSha256)));
  assert.deepEqual([report.rights, report.admitted, report.publication], ['REVIEW_REQUIRED', false, false]);
});

test('a map unit without polygons, a stray polygon or missing components holds the area', async () => {
  const { fetcher } = sda('KS998', {
    components: table(['mukey', 'components', 'pct', 'major'], [['1', '2', '90', '0']]),
    polygons: table(['mukey', 'polygons'], [['1', '4'], ['3', '1']]),
  });
  const report = await qualifySsurgo('KS998', { fetcher });
  assert.equal(report.state, 'held');
  assert.deepEqual(report.holds, ['MAP_UNITS_WITHOUT_COMPONENTS', 'SPATIAL_TABULAR_MISMATCH']);
  assert.deepEqual(report.polygons, { count: 5, mapUnits: 2, unmapped: ['2'], orphaned: ['3'] });
  assert.deepEqual(report.findings.slice(0, 2), [{ code: 'COMPONENT_PERCENT_NOT_100', mapUnits: [{ mukey: '1', pct: 90 }] }, { code: 'NO_MAJOR_COMPONENT', mapUnits: ['1'] }]);
});

test('an unknown survey area and an unpublished unit are holds, not empty success', async () => {
  const { fetcher } = sda('KS997', { survey: '{}', mapunits: '{}', components: '{}', polygons: '{}',
    units: table(['attributecolumnname', 'attributename', 'attributeuomabbrev'], units.filter(([column]) => column !== 'om_r')) });
  const report = await qualifySsurgo('KS997', { fetcher });
  assert.deepEqual(report.holds, ['SURVEY_AREA_NOT_FOUND', 'NO_MAP_UNITS', 'HORIZON_UNITS_UNPUBLISHED']);
  assert.equal(report.survey, null);
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
