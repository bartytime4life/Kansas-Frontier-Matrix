import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { PUBLIC_LAB_SNAPSHOTS } from '../app/labs/public-snapshots.mjs';
import { COUNTY_LAB_SNAPSHOTS } from '../app/labs/county-snapshots.mjs';
import { buildCountyModel, countyMetric, describeCounty, populationChange, KANSAS_COUNTIES, normalizeCountyName } from '../app/labs/county-model.mjs';

const snapshots = { ...PUBLIC_LAB_SNAPSHOTS, ...COUNTY_LAB_SNAPSHOTS };
const bundles = Object.fromEntries(await Promise.all(['census-mosaic', 'county-conditions', 'built-kansas', 'air-and-health'].map(async id => [id, JSON.parse(await readFile(new URL('../public' + snapshots[id].path, import.meta.url)))])));
const recordBundle = (story, records, extra = {}) => ({ story, data: { kind: 'records', records, ...extra } });

test('County Observatory joins all 105 source-backed counties while retaining sparse AQI coverage and source periods', () => {
  const model = buildCountyModel(bundles, { snapshots });
  assert.equal(model.rows.length, 105);
  assert.deepEqual(model.rows.map(row => row.fips), KANSAS_COUNTIES.map(row => row.fips));
  assert.equal(model.rows.filter(row => row.geometry).length, 105);
  assert.equal(model.rows.filter(row => row.population !== null).length, 105);
  assert.equal(model.rows.filter(row => row.medianIncome !== null).length, 105);
  assert.equal(model.rows.filter(row => row.aqi90th !== null).length, 12);
  assert.equal(model.rows.filter(row => row.aqi90th === null).length, 93, 'unmonitored counties never become AQI zeroes');
  assert.deepEqual(model.options.populationYears, [2020, 2021, 2022, 2023, 2024, 2025]);
  assert.deepEqual(model.options.acsYears, [2014, 2019, 2024]);
  assert.match(model.periods.acs, /2020–2024/);
  assert.match(model.periods.bridges, /2026-11-16/);
  assert.match(countyMetric(model, 'medianIncome').unit, /2024 dollars/);
  assert.equal(countyMetric(model, 'povertyPct').moeKey, 'povertyPctMoe');
  assert.equal(model.sourceBindings.length, 4);
  assert.ok(model.sourceBindings.every(source => source.sha256 === snapshots[source.id].sha256));
  assert.equal(model.diagnostics.bridgeTotalRecords, 24877);
  assert.equal(model.diagnostics.bridgeMatchedRecords, 24877);
  assert.equal(model.diagnostics.bridgeUnmatchedRecords, 0);
  assert.equal(model.rows.reduce((sum, row) => sum + row.bridgeRecords, 0), 24877);
});

test('county profile population change uses the selected PEP year and never substitutes ACS population or dollar trends', () => {
  const model = buildCountyModel(bundles, { populationYear: 2023, acsYear: 2014, aqiYear: 2000, snapshots });
  const county = describeCounty(model, '20173');
  assert.equal(county.populationHistory.length, 6);
  assert.equal(county.acsHistory.length, 3);
  assert.equal(county.row.acsYear, 2014);
  assert.equal(county.row.medianIncome, bundles['county-conditions'].data.records.find(row => row.fips === '20173' && row.year === 2014).medianIncome);
  const start = county.populationHistory.find(row => row.year === 2020).population;
  const end = county.populationHistory.find(row => row.year === 2023).population;
  assert.equal(county.populationChange.start, start);
  assert.equal(county.populationChange.end, end);
  assert.equal(county.populationChange.difference, end - start);
  assert.equal(county.row.populationChange, end - start);
  assert.ok(Math.abs(county.row.populationChangePct - 100 * (end - start) / start) < 1e-10);
  assert.equal(populationChange(model, '20173', 2019, 2023).percent, null);
  assert.equal(populationChange(model, '20173', 2020, 2026).difference, null);
  assert.equal(describeCounty(model, '99999'), null);
  assert.match(countyMetric(model, 'medianIncome').unit, /2014 dollars/);
});

test('bridge county joins normalize exact labels and reconcile unknown labels without using coordinates', () => {
  const bridges = [
    { id: '1', county: 'JOHNSON', structure: 'x', network: 'state', sufficiency: 90, year: 2000, traffic: 0, trafficYear: 2018 },
    { id: '2', county: 'Johnson County, Kansas', structure: 'x', network: 'state', sufficiency: 90, year: 2000, traffic: 100, trafficYear: null },
    { id: '3', county: ' Johnson ', structure: 'y', network: 'local', sufficiency: 0, year: 2027, traffic: 50, trafficYear: 2022 },
    { id: '4', county: 'Johns', latitude: 38.8, longitude: -94.7, sufficiency: 99 },
    { id: '5', county: null, latitude: 38.8, longitude: -94.7 },
  ];
  const model = buildCountyModel({
    'built-kansas': recordBundle('built-kansas', bridges, { inventoryAsOf: '2026-11-16' }),
    'census-mosaic': recordBundle('census-mosaic', [{ id: 'pop', fips: '20091', year: 2025, population: 10000 }]),
  });
  const row = model.rows.find(row => row.fips === '20091');
  assert.equal(normalizeCountyName(' JOHNSON County, Kansas '), 'johnson');
  assert.equal(row.bridgeRecords, 3, 'repeated source identities stay separate inventory records');
  assert.equal(row.bridgeScoreMean, 60, 'unweighted source record mean includes valid zero score');
  assert.equal(row.bridgeMedianAge, 26, 'age uses inventory2026; future recorded built years excluded');
  assert.equal(row.bridgeAgeCount, 2);
  assert.equal(row.bridgeAgeMissing, 1);
  assert.equal(row.bridgeTrafficMedian, 50, 'valid zero traffic remains an observation');
  assert.equal(row.bridgeTrafficDatedCount, 2);
  assert.equal(row.bridgeTrafficUndatedCount, 1);
  assert.equal(row.bridgeTrafficFirstYear, 2018);
  assert.equal(row.bridgeTrafficLastYear, 2022);
  assert.equal(row.bridgeRecordsPer10k, 3);
  assert.equal(model.diagnostics.bridgeTotalRecords, 5);
  assert.equal(model.diagnostics.bridgeMatchedRecords, 3);
  assert.equal(model.diagnostics.bridgeUnmatchedRecords, 2);
  assert.equal(model.diagnostics.bridgeRepeatedIdentityExtraRecords, 1);
  assert.equal(model.diagnostics.bridgeUnmatchedCountyLabels.reduce((sum, item) => sum + item.records, 0), 2);
  assert.match(countyMetric(model, 'bridgeTrafficMedian').note, /Not road capacity/);
});

test('absent data remain null across all 105 counties, while a loaded empty inventory contains zero records', () => {
  const missing = buildCountyModel({});
  assert.equal(missing.rows.length, 105);
  assert.ok(missing.rows.every(row => row.population === null && row.bridgeRecords === null && row.medianIncomeMoe === null && row.aqi90th === null));
  const empty = buildCountyModel({ 'built-kansas': recordBundle('built-kansas', [], { inventoryAsOf: '2026-11-16' }) });
  assert.ok(empty.rows.every(row => row.bridgeRecords === 0 && row.bridgeScoreMean === null && row.bridgeMedianAge === null && row.bridgeRecordsPer10k === null));
  const unsupported = buildCountyModel(bundles, { acsYear: 2020, populationYear: 2026, aqiYear: 1990, inventoryYear: 2020 });
  assert.ok(unsupported.rows.every(row => row.population === null && row.populationChange === null && row.medianIncome === null && row.aqi90th === null));
  assert.equal(unsupported.selection.inventoryYear, 2026, 'present inventory cannot reconstruct an earlier inventory');
  assert.equal(unsupported.diagnostics.warnings.length, 1);
});

test('rate descriptors retain numerator, denominator and independent source-period semantics', () => {
  const model = buildCountyModel(bundles, { snapshots });
  for (const metric of model.metrics.filter(metric => metric.kind === 'rate')) {
    assert.ok(metric.rate && metric.rate.numerator && metric.rate.denominator && metric.rate.denominatorPeriod);
    assert.ok(metric.unit && metric.period && metric.sourceId);
    for (const row of model.rows) {
      if (row[metric.key] === null || !row[metric.rate.denominator]) continue;
      // EPA derivative percentages are rounded in the original public snapshot.
      assert.ok(Math.abs(row[metric.key] - metric.rate.scale * row[metric.rate.numerator] / row[metric.rate.denominator]) <= .0051, metric.key);
    }
  }
  assert.deepEqual(countyMetric(model, 'bridgeRecordsPer10k').sourceIds, ['built-kansas', 'census-mosaic']);
  assert.match(countyMetric(model, 'bridgeRecordsPer10k').period, /2026-11-16/);
  assert.match(countyMetric(model, 'bridgeRecordsPer10k').rate.denominatorPeriod, /2025/);
  assert.match(countyMetric(model, 'bridgeRecords').note, /Not a unique physical bridge count/);
});

test('duplicate county/year observations fail a join rather than silently selecting an arbitrary row', () => {
  const duplicated = recordBundle('county-conditions', [{ id: 'a', fips: '20091', year: 2024 }, { id: 'b', fips: '20091', year: 2024 }]);
  assert.throws(() => buildCountyModel({ 'county-conditions': duplicated }), /Duplicate county\/year/);
});
