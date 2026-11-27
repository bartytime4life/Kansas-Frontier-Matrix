import assert from 'node:assert/strict';
import { webcrypto } from 'node:crypto';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import { loadAirSnapshot } from '../app/labs/daily-air-quality/snapshot-loader.mjs';
import { loadClimateSnapshot } from '../app/labs/heat-and-rain/snapshot-loader.mjs';
import { loadDroughtSnapshot } from '../app/labs/county-drought/snapshot-loader.mjs';
import { loadSunlightSnapshot } from '../app/labs/sunlight-and-sky/snapshot-loader.mjs';
import { buildScienceComparison, COMPARISON_METRICS, COMPARISON_YEARS } from '../app/science/compare/comparison-model.mjs';
import { COMPARISON_PLACES, comparisonPlace } from '../app/science/compare/comparison-places.mjs';

const manifest = async lab => JSON.parse(await readFile(new URL(`../app/labs/${lab}/snapshot-manifest.json`, import.meta.url)));
const [climateManifest, droughtManifest, airManifest, sunlightManifest] = await Promise.all([
  manifest('heat-and-rain'), manifest('county-drought'), manifest('daily-air-quality'), manifest('sunlight-and-sky'),
]);
const areaDescriptors = ({ climateId, sunlightId }) => ({
  climate: climateManifest.stations.find(station => station.id === climateId),
  drought: droughtManifest,
  air: airManifest,
  sunlight: sunlightManifest.points.find(point => point.id === sunlightId),
});
const descriptors = areaDescriptors(comparisonPlace('topeka'));
const options = {
  cryptoImpl: webcrypto,
  fetchImpl: async path => new Response(await readFile(new URL(`../public${path}`, import.meta.url))),
};
const [climate, drought, air, sunlight] = await Promise.all([
  loadClimateSnapshot(descriptors.climate, options), loadDroughtSnapshot(descriptors.drought, options),
  loadAirSnapshot(descriptors.air, options), loadSunlightSnapshot(descriptors.sunlight, options),
]);
const samples = { climate, drought, air, sunlight };

const byId = (report, id) => report.series.find(series => series.id === id);

// Exercise the genuine checked-in provider-context snapshots rather than placing sample values behind their digests.
test('comparison combines only supported source locations and independently supported year windows', () => {
  const report = buildScienceComparison(samples, undefined, descriptors);
  assert.equal(report.schema, 'kfm.science-comparison/v1');
  assert.equal(report.scope, 'provider-context');
  assert.deepEqual(report.location, { id: 'topeka', name: 'Topeka and Shawnee County' });
  assert.deepEqual(report.selection, { year: 2025, compareYear: 2024 });
  assert.deepEqual(report.series.map(row => row.id), COMPARISON_METRICS.map(metric => metric.id));
  assert.deepEqual(report.series.map(row => row.location.id), ['USW00013996', '20177', '20177', 'topeka']);
  assert.deepEqual(report.series.map(row => row.kind), ['observed', 'assessed', 'reported', 'modeled']);
  assert.deepEqual(report.series.map(row => row.annual.selected.expected), [365, 52, 365, 365]);
  assert.deepEqual(report.series.map(row => row.annual.comparison.expected), [366, 53, 366, 366]);
  for (const series of report.series) {
    assert.deepEqual(series.monthly.map(row => row.month), Array.from({ length: 12 }, (_, index) => index + 1));
    for (const side of ['selected', 'comparison']) {
      assert.equal(series.monthly.reduce((sum, month) => sum + month[side].expected, 0), series.annual[side].expected);
      assert.equal(series.monthly.reduce((sum, month) => sum + month[side].valid, 0), series.annual[side].valid);
    }
  }
});

test('Wichita and Dodge City bind each local station and model to the corresponding county records', async () => {
  const expected = [
    ['wichita', 'Wichita and Sedgwick County', 'USW00003928', '20173', 2192],
    ['dodge-city', 'Dodge City and Ford County', 'USW00013985', '20057', 2058],
  ];
  assert.deepEqual(COMPARISON_PLACES.map(area => area.id), ['topeka', 'wichita', 'dodge-city']);
  for (const [place, name, station, county, allAirDays] of expected) {
    const inputs = areaDescriptors(comparisonPlace(place));
    const [areaClimate, areaSunlight] = await Promise.all([
      loadClimateSnapshot(inputs.climate, options), loadSunlightSnapshot(inputs.sunlight, options),
    ]);
    const areaSamples = { climate: areaClimate, drought, air, sunlight: areaSunlight };
    let totalAirDays = 0;
    for (const year of COMPARISON_YEARS) {
      const report = buildScienceComparison(areaSamples, { year, compareYear: year === 2025 ? 2024 : 2025, place }, inputs);
      assert.deepEqual(report.location, { id: place, name });
      assert.deepEqual(report.series.map(metric => metric.location.id), [station, county, county, place]);
      assert.equal(byId(report, 'climate').display.sha256, inputs.climate.sha256);
      assert.equal(byId(report, 'sunlight').display.sha256, inputs.sunlight.sha256);
      totalAirDays += byId(report, 'air').annual.selected.valid;
    }
    assert.equal(totalAirDays, allAirDays);
  }
});

test('the four indicators retain source-native arithmetic, missing support and a reported zero', () => {
  const report = buildScienceComparison(samples, { year: 2023, compareYear: 2022 }, descriptors);
  const precipitation = byId(report, 'climate');
  assert.deepEqual(precipitation.annual.selected, { value: 695.1, valid: 321, expected: 365 });
  const droughtSeries = byId(report, 'drought');
  const droughtCounty = drought.counties.find(county => county.id === '20177');
  const droughtValues = drought.weeks.flatMap((date, index) => date.startsWith('2023-08-') ? [droughtCounty.values[index][3]] : []);
  assert.deepEqual(droughtSeries.monthly[7].selected, { value: Math.max(...droughtValues), valid: droughtValues.length, expected: 5 });
  assert.ok(droughtSeries.monthly.some(month => month.selected.value === 0 && month.selected.valid > 0));
  const airSeries = byId(report, 'air');
  const august = airSeries.monthly[7].comparison;
  assert.equal(august.valid, 16);
  assert.equal(august.expected, 31);
  assert.equal(airSeries.annual.comparison.valid, 350);
  const augustAqi = air.dates.flatMap((date, index) => {
    const value = air.counties.find(county => county.id === '20177').values[index];
    return date.startsWith('2022-08-') && value !== null ? [Number(value[0])] : [];
  });
  assert.equal(august.value, Math.max(...augustAqi));
  assert.ok(Math.abs(byId(report, 'sunlight').annual.selected.value - 4.437364931506846) < 1e-12);
});

test('source and display digests, year scope, time conventions and attribution survive serialization', () => {
  const report = buildScienceComparison(samples, undefined, descriptors);
  assert.deepEqual(JSON.parse(JSON.stringify(report)), report);
  for (const [index, descriptor] of [descriptors.climate, descriptors.drought.snapshot, descriptors.air.snapshot, descriptors.sunlight].entries()) {
    const series = report.series[index];
    assert.deepEqual(series.display, { url: descriptor.url, sha256: descriptor.sha256, bytes: descriptor.bytes });
    assert.deepEqual(series.sources.map(source => source.year), [2025, 2024]);
    assert.ok(series.sources.every(source => /^[a-f0-9]{64}$/.test(source.sha256) && source.url.startsWith('https://') && source.capturedAt));
    assert.ok(series.location.scale && series.timeStandard && series.method && series.attribution && series.documentation.startsWith('https://'));
  }
  assert.equal(byId(report, 'drought').attribution, droughtManifest.attribution);
  assert.equal(byId(report, 'sunlight').timeStandard, 'NASA Local Solar Time (LST)');
});

test('rejects unsupported years, mismatched weather and mismatched snapshot descriptors', () => {
  assert.deepEqual(COMPARISON_YEARS, [2020, 2021, 2022, 2023, 2024, 2025]);
  for (const year of [2019, '2023', 2024, 2026]) {
    assert.throws(() => buildScienceComparison(samples, { year, compareYear: 2024 }, descriptors), /different calendar years/);
  }
  assert.throws(() => buildScienceComparison(samples, { place: 'lawrence' }, descriptors), /supported Kansas/);
  assert.throws(() => buildScienceComparison(samples, { place: 'wichita' }, descriptors), /verified source snapshots/);
  const otherClimate = climateManifest.stations.find(station => station.id !== descriptors.climate.id);
  assert.throws(() => buildScienceComparison(samples, undefined, { ...descriptors, climate: otherClimate }), /verified source snapshots/);
  const badAir = { ...descriptors.air, snapshot: { ...descriptors.air.snapshot, bytes: descriptors.air.snapshot.bytes + 1 } };
  assert.throws(() => buildScienceComparison(samples, undefined, { ...descriptors, air: badAir }), /matching verified display/);
  const badSunlight = { ...descriptors.sunlight, bytes: descriptors.sunlight.bytes + 1 };
  assert.throws(() => buildScienceComparison(samples, undefined, { ...descriptors, sunlight: badSunlight }), /matching verified sunlight/);
});
