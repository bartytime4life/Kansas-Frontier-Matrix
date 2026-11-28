import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import { PUBLIC_LAB_SNAPSHOTS } from '../app/labs/public-snapshots.mjs';
import { COMPONENT_YEARS, populationBalance, populationBalanceReport, populationBalanceCsv } from '../app/labs/population-components.mjs';

const manifest = PUBLIC_LAB_SNAPSHOTS['census-mosaic'];
const bytes = await readFile(new URL('../public' + manifest.path, import.meta.url));
const bundle = JSON.parse(bytes);
const records = bundle.data.records;
const countyIds = [...new Set(records.map(row => row.fips))].sort();
const sourceRow = (fips, year) => records.find(row => row.fips === fips && row.year === year);
const close = (actual, expected) => assert.ok(Math.abs(actual - expected) <= 1e-12 * Math.max(1, Math.abs(expected)), `${actual} ~= ${expected}`);
const pair = () => [
  { fips: '20001', name: 'Allen County', year: 2024, population: 100 },
  { fips: '20001', name: 'Allen County', year: 2025, population: 110, births: 10, deaths: 4, naturalChange: 6, netMigration: 3 },
];
const chosen = { fips: '20001', year: 2025 };
function assertUnavailable(result, reasonCode) {
  assert.equal(result.status, 'unavailable');
  assert.equal(result.reasonCode, reasonCode);
  assert.ok(result.reason.length > 15);
  for (const key of ['beginPopulation', 'endPopulation', 'change', 'births', 'deaths', 'naturalChange', 'netMigration', 'remainder', 'meanPopulation', 'changePer1000']) assert.equal(result[key], null, key);
  assert.deepEqual(result.contributions, []);
}

test('all 525 complete county intervals reconcile against the exact shipping Census snapshot', () => {
  assert.equal(bytes.byteLength, manifest.bytes);
  assert.equal(createHash('sha256').update(bytes).digest('hex'), manifest.sha256);
  assert.equal(manifest.sha256, 'a3c82ebd5d89619c498db370861f1288eed6199c3ae8ec0407aea999410c7399');
  assert.equal(bundle.story, 'census-mosaic');
  assert.equal(records.length, 630);
  assert.equal(countyIds.length, 105);
  assert.deepEqual(COMPONENT_YEARS, [2021, 2022, 2023, 2024, 2025]);
  const original = JSON.stringify(records);
  let intervals = 0, nonzeroRemainders = 0;
  const remainders = [];
  for (const fips of countyIds) for (const year of COMPONENT_YEARS) {
    const before = sourceRow(fips, year - 1), after = sourceRow(fips, year);
    const result = populationBalance(records, { fips, year });
    assert.equal(result.status, 'ready', `${fips}/${year}: ${result.reason}`);
    assert.equal(result.name, after.name);
    assert.equal(result.beginPopulation, before.population);
    assert.equal(result.endPopulation, after.population);
    assert.equal(result.change, after.population - before.population);
    assert.equal(result.naturalChange, after.births - after.deaths);
    assert.equal(result.remainder, after.population - before.population - after.births + after.deaths - after.netMigration);
    assert.equal(result.contributions.reduce((sum, entry) => sum + entry.people, 0), result.change);
    assert.deepEqual(result.contributions.map(entry => entry.key), ['births', 'deaths', 'netMigration', 'remainder']);
    assert.equal(result.contributions[1].people, after.deaths === 0 ? 0 : -after.deaths);
    assert.equal(result.meanPopulation, (before.population + after.population) / 2);
    for (const entry of result.contributions) close(entry.per1000, entry.people * 1000 / ((before.population + after.population) / 2));
    close(result.changePer1000, result.change * 1000 / result.meanPopulation);
    close(result.contributions.reduce((sum, entry) => sum + entry.per1000, 0), result.changePer1000);
    assert.equal(result.beginDate, `${year - 1}-07-01`);
    assert.equal(result.endDate, `${year}-07-01`);
    assert.equal(result.componentFrom, `${year - 1}-07-01`);
    assert.equal(result.componentTo, `${year}-06-30`);
    intervals++;
    if (result.remainder !== 0) nonzeroRemainders++;
    remainders.push(result.remainder);
  }
  assert.equal(intervals, 525);
  assert.equal(nonzeroRemainders, 422);
  assert.equal(Math.min(...remainders), -435);
  assert.equal(Math.max(...remainders), 609);
  assert.equal(JSON.stringify(records), original, 'analysis never changes the shipping records');
});

test('real county anchors retain the signed remainder and use the mean of both endpoints', () => {
  const sedgwick = populationBalance(records, { fips: '20173', year: 2025 });
  assert.deepEqual([sedgwick.beginPopulation, sedgwick.endPopulation, sedgwick.change, sedgwick.births, sedgwick.deaths, sedgwick.naturalChange, sedgwick.netMigration, sedgwick.remainder], [534386, 538433, 4047, 6645, 5093, 1552, 2447, 48]);
  assert.equal(sedgwick.meanPopulation, 536409.5);
  close(sedgwick.changePer1000, 4047 / 536409.5 * 1000);
  assert.notEqual(sedgwick.changePer1000, 4047 / 534386 * 1000, 'normalization must not use only the beginning population');
  const haskell = populationBalance(records, { fips: '20081', year: 2025 });
  assert.equal(haskell.change, 41);
  assert.equal(haskell.remainder, -1);
  assert.equal(haskell.contributions.at(-1).people, -1);
  const migrationLoss = populationBalance(records, { fips: '20003', year: 2021 });
  assert.equal(migrationLoss.netMigration, -24);
  assert.equal(migrationLoss.contributions[2].people, migrationLoss.netMigration);
});

test('invalid selectors and the partial 2020 interval never produce guessed values', () => {
  for (const fips of [null, undefined, 20001, '20000', '20002', '20211', '19001', '20001 ', '__proto__']) {
    assertUnavailable(populationBalance(pair(), { fips, year: 2025 }), 'INVALID_FIPS');
  }
  for (const year of [null, undefined, '2025', true, NaN, Infinity, 2024.5, 2019, 2020, 2026]) {
    assertUnavailable(populationBalance(pair(), { fips: '20001', year }), 'UNSUPPORTED_YEAR');
  }
  const partial = populationBalance(records, { fips: '20001', year: 2020 });
  assert.equal(partial.year, 2020);
  assert.equal(partial.name, 'Allen County', 'a known county remains named even when its selected interval is unsupported');
  assert.equal(partial.beginDate, null);
  assert.equal(partial.componentFrom, null);
  assertUnavailable(populationBalance(pair(), null), 'INVALID_FIPS');
});

test('missing and duplicate endpoint rows remain unavailable rather than averaged or zero-filled', () => {
  assertUnavailable(populationBalance([], chosen), 'MISSING_ENDPOINT');
  assertUnavailable(populationBalance(pair().slice(1), chosen), 'MISSING_ENDPOINT');
  assertUnavailable(populationBalance(pair().slice(0, 1), chosen), 'MISSING_ENDPOINT');
  assertUnavailable(populationBalance([...pair(), { ...pair()[0] }], chosen), 'DUPLICATE_ENDPOINT');
  assertUnavailable(populationBalance([...pair(), { ...pair()[1], population: 999 }], chosen), 'DUPLICATE_ENDPOINT');
  assertUnavailable(populationBalance(null, chosen), 'INVALID_RECORDS');
  assertUnavailable(populationBalance([null], chosen), 'INVALID_RECORDS');
  assertUnavailable(populationBalance({}, chosen), 'INVALID_RECORDS');
  const stringYear = pair(); stringYear[1].year = '2025';
  assertUnavailable(populationBalance(stringYear, chosen), 'MISSING_ENDPOINT');
});

test('non-numeric counts, conflicting natural change and invalid denominators block the entire decomposition', () => {
  for (const key of ['population', 'births', 'deaths', 'naturalChange', 'netMigration']) {
    for (const value of [undefined, null, '', '10', true, NaN, Infinity, 1.5]) {
      const rows = pair(); rows[1][key] = value;
      assertUnavailable(populationBalance(rows, chosen), key === 'population' ? 'INVALID_POPULATION' : 'INVALID_COMPONENT');
    }
  }
  const missingBegin = pair(); missingBegin[0].population = null;
  assertUnavailable(populationBalance(missingBegin, chosen), 'INVALID_POPULATION');
  for (const key of ['births', 'deaths']) {
    const rows = pair(); rows[1][key] = -1;
    assertUnavailable(populationBalance(rows, chosen), 'NEGATIVE_COUNT');
  }
  const conflict = pair(); conflict[1].naturalChange = 5;
  assertUnavailable(populationBalance(conflict, chosen), 'INCONSISTENT_NATURAL_CHANGE');
  const zero = pair(); zero[0].population = 0; zero[1].population = 0;
  assertUnavailable(populationBalance(zero, chosen), 'INVALID_DENOMINATOR');
  const negative = pair(); negative[0].population = -1;
  assertUnavailable(populationBalance(negative, chosen), 'INVALID_POPULATION');
  const unsafe = pair(); unsafe[0].population = Number.MAX_SAFE_INTEGER; unsafe[1].population = 0; unsafe[1].births = Number.MAX_SAFE_INTEGER; unsafe[1].deaths = 0; unsafe[1].naturalChange = Number.MAX_SAFE_INTEGER; unsafe[1].netMigration = 0;
  assertUnavailable(populationBalance(unsafe, chosen), 'UNSAFE_ARITHMETIC');
  const cancelAfterNatural = pair(); cancelAfterNatural[0].population = Number.MAX_SAFE_INTEGER; cancelAfterNatural[1].population = 0;
  cancelAfterNatural[1].births = Number.MAX_SAFE_INTEGER; cancelAfterNatural[1].deaths = 0;
  cancelAfterNatural[1].naturalChange = Number.MAX_SAFE_INTEGER; cancelAfterNatural[1].netMigration = -Number.MAX_SAFE_INTEGER;
  assertUnavailable(populationBalance(cancelAfterNatural, chosen), 'UNSAFE_ARITHMETIC');
  const cancelCumulative = pair(); cancelCumulative[0].population = 0; cancelCumulative[1].population = Number.MAX_SAFE_INTEGER;
  cancelCumulative[1].births = Number.MAX_SAFE_INTEGER; cancelCumulative[1].deaths = 0;
  cancelCumulative[1].naturalChange = Number.MAX_SAFE_INTEGER; cancelCumulative[1].netMigration = 1;
  assertUnavailable(populationBalance(cancelCumulative, chosen), 'UNSAFE_ARITHMETIC');
});

test('valid zeroes and negative balances remain values with signed contributions', () => {
  const rows = pair(); rows[0].population = 110; rows[1].population = 100;
  rows[1].births = 0; rows[1].deaths = 0; rows[1].naturalChange = 0; rows[1].netMigration = -9;
  const result = populationBalance(rows, chosen);
  assert.equal(result.status, 'ready');
  assert.equal(result.births, 0);
  assert.equal(result.deaths, 0);
  assert.equal(result.contributions[1].people, 0);
  assert.equal(Object.is(result.contributions[1].people, -0), false);
  assert.equal(result.change, -10);
  assert.equal(result.netMigration, -9);
  assert.equal(result.remainder, -1);
  const oneZero = pair(); oneZero[0].population = 0;
  assert.equal(populationBalance(oneZero, chosen).meanPopulation, 55, 'a zero beginning endpoint can still have a positive mean denominator');
});

test('reports bind both selected counties and all five histories to exact source and method metadata', () => {
  const report = populationBalanceReport(bundle, { fipsA: '20173', fipsB: '20081', year: 2025 }, manifest);
  assert.equal(report.schema, 'kfm.population-components/v1');
  assert.equal(report.method.id, report.schema);
  assert.equal(report.source.sha256, manifest.sha256);
  assert.equal(report.source.snapshotPath, manifest.path);
  assert.equal(report.source.bytes, bytes.byteLength);
  assert.equal(report.source.capturedAt, bundle.data.sourceSnapshot.retrievedAt);
  assert.equal(report.source.preparedAt, bundle.built_at);
  assert.deepEqual(report.source.sourceSnapshot, bundle.data.sourceSnapshot);
  assert.deepEqual(report.source.sourceSnapshots, bundle.data.sourceSnapshots);
  assert.notEqual(report.source.sourceSnapshot, bundle.data.sourceSnapshot);
  assert.notEqual(report.source.sourceSnapshots[0], bundle.data.sourceSnapshots[0]);
  assert.deepEqual(report.source.observed, { from: '2020', to: '2025' });
  assert.deepEqual(report.selection, { fipsA: '20173', fipsB: '20081', year: 2025 });
  assert.equal(report.countyA.remainder, 48);
  assert.equal(report.countyB.remainder, -1);
  assert.deepEqual(report.history.a.map(entry => entry.year), COMPONENT_YEARS);
  assert.deepEqual(report.history.b.map(entry => entry.year), COMPONENT_YEARS);
  assert.ok(report.history.a.every(entry => entry.fips === '20173' && entry.status === 'ready'));
  assert.ok(report.history.b.every(entry => entry.fips === '20081' && entry.status === 'ready'));
  assert.match(report.method.denominatorLabel, /Mean of beginning and ending/);
  assert.match(report.method.limits.join(' '), /KFM calculated normalizations/);
  assert.match(report.method.limits.join(' '), /not an independently captured Census residual/);
  assert.match(report.method.limits.join(' '), /CSV retains full calculation precision/);
  assert.match(report.method.documentation[0].href, /CO-EST2025-ALLDATA\.pdf$/);
  report.source.sources[0].name = 'Changed only in the report';
  report.source.limits.push('Changed only in the report');
  assert.notEqual(bundle.sources[0].name, report.source.sources[0].name);
  assert.notEqual(bundle.data.limits.at(-1), report.source.limits.at(-1));
});

test('unsupported selections, missing records and malformed bundles stay visible in report statuses', () => {
  const unsupported = populationBalanceReport(bundle, { fipsA: '20173', fipsB: '20081', year: 2020 }, manifest);
  assertUnavailable(unsupported.countyA, 'UNSUPPORTED_YEAR');
  assertUnavailable(unsupported.countyB, 'UNSUPPORTED_YEAR');
  assert.ok(unsupported.history.a.every(entry => entry.status === 'ready'), 'valid historical intervals are not replaced with the unsupported selected interval');
  const duplicate = structuredClone(bundle); duplicate.data.records.push({ ...sourceRow('20173', 2025) });
  const report = populationBalanceReport(duplicate, { fipsA: '20173', fipsB: '20081', year: 2025 }, manifest);
  assertUnavailable(report.countyA, 'DUPLICATE_ENDPOINT');
  assert.equal(report.countyB.status, 'ready');
  for (const invalid of [null, {}, { ...bundle, story: 'other' }, { ...bundle, data: [] }]) {
    const broken = populationBalanceReport(invalid, { fipsA: '20173', fipsB: '20081', year: 2025 }, manifest);
    assertUnavailable(broken.countyA, 'INVALID_BUNDLE');
    assert.ok(broken.history.a.every(entry => entry.status === 'unavailable'));
    assert.equal(broken.source.capturedAt, null);
    assert.equal(broken.source.preparedAt, null);
  }
  const noSourceIdentity = populationBalanceReport(bundle, { fipsA: '20173', fipsB: '20081', year: 2025 }, { path: '//other.example/data', sha256: 'not-a-hash', bytes: '223032' });
  assert.equal(noSourceIdentity.source.snapshotPath, null);
  assert.equal(noSourceIdentity.source.sha256, null);
  assert.equal(noSourceIdentity.source.bytes, null);
});

test('CSV contains both complete histories, selected flags, signed values, dates and exact normalization provenance', () => {
  const report = populationBalanceReport(bundle, { fipsA: '20173', fipsB: '20081', year: 2025 }, manifest);
  const [header, ...rows] = populationBalanceCsv(report);
  assert.equal(rows.length, 10);
  assert.equal(new Set(header).size, header.length);
  assert.ok(rows.every(row => row.length === header.length));
  const objects = rows.map(row => Object.fromEntries(header.map((key, index) => [key, row[index]])));
  assert.equal(objects.filter(row => row.selected_interval).length, 2);
  for (const row of objects) {
    const balance = report.history[row.county_slot.toLowerCase()].find(entry => entry.year === row.year);
    assert.equal(row.county_fips, balance.fips);
    assert.equal(row.calculated_balance_remainder_people, balance.remainder);
    assert.equal(row.change_people, balance.change);
    assert.equal(row.deaths_contribution_people, -balance.deaths);
    assert.equal(row.mean_estimated_residents, balance.meanPopulation);
    assert.equal(row.change_per_1000_mean_residents, balance.changePer1000);
    assert.equal(row.components_from, balance.componentFrom);
    assert.equal(row.components_to, balance.componentTo);
    assert.equal(row.source_snapshot_sha256, manifest.sha256);
    assert.equal(row.raw_source_sha256, bundle.data.sourceSnapshot.rawSha256);
    assert.equal(row.raw_source_bytes, bundle.data.sourceSnapshot.rawBytes);
    assert.equal(row.raw_source_retrieved_at, bundle.data.sourceSnapshot.retrievedAt);
    assert.equal(row.source_captured_at, bundle.data.sourceSnapshot.retrievedAt);
    assert.equal(row.public_snapshot_prepared_at, bundle.built_at);
    assert.deepEqual(JSON.parse(row.raw_source_snapshots_json), bundle.data.sourceSnapshots);
    assert.equal(row.method_id, report.method.id);
    assert.equal(row.normalization_denominator, report.method.denominatorLabel);
    assert.equal(row.people_unit, 'people');
    assert.equal(row.normalized_unit, report.method.rateUnit);
    assert.equal(row.selected_interval, row.year === 2025);
  }
  const partial = populationBalanceReport({ ...bundle, data: { ...bundle.data, records: records.filter(row => !(row.fips === '20173' && row.year === 2024)) } }, { fipsA: '20173', fipsB: '20081', year: 2025 }, manifest);
  const unavailable = populationBalanceCsv(partial).slice(1).map(row => Object.fromEntries(header.map((key, index) => [key, row[index]]))).find(row => row.county_slot === 'A' && row.year === 2025);
  assert.equal(unavailable.status, 'unavailable');
  assert.equal(unavailable.reason_code, 'MISSING_ENDPOINT');
  assert.equal(unavailable.change_people, '');
  assert.equal(unavailable.births_people, '');
  assert.equal(unavailable.mean_estimated_residents, '');
  assert.throws(() => populationBalanceCsv({}), /report unavailable/);
});
