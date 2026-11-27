import assert from 'node:assert/strict';
import test from 'node:test';
import { comparisonCsv, comparisonExportFilename, comparisonJson } from '../app/science/compare/comparison-report.mjs';

const point = (value, valid, expected) => ({ value, valid, expected });
const capture = (year, digit) => ({ year, url: `https://example.invalid/${year}.zip`, sha256: digit.repeat(64),
  bytes: 1200, capturedAt: '2026-11-26T12:00:00Z', providerCreated: '2026-11-24' });

function fixture() {
  return {
    schema: 'kfm.science-comparison/v1', scope: 'provider-context', location: { id: 'topeka', name: 'Topeka and Shawnee County' },
    selection: { year: 2025, compareYear: 2024 }, limitations: ['No shared spatial footprint or daily clock.'],
    series: [{
      id: 'climate', label: 'Precipitation, liquid equivalent', kind: 'observed', unit: 'mm', supportUnit: 'days',
      location: { id: 'test-station', name: 'Topeka station', scale: 'station' }, timeStandard: 'Station observation day',
      method: 'Sum quantified daily precipitation', limitation: 'Partial support retains only qualified observations',
      attribution: 'Test provider, "Weather archive"', documentation: 'https://example.invalid/method', labPath: '/labs/heat-and-rain',
      display: { url: '/science-data/test.json', sha256: 'a'.repeat(64), bytes: 1234 },
      sources: [capture(2024, 'b'), capture(2025, 'c'), capture(2023, 'd')],
      annual: { selected: point(12.5, 360, 365), comparison: point(32, 366, 366) },
      monthly: [
        { month: 1, selected: point(null, 0, 31), comparison: point(0, 31, 31) },
        { month: 2, selected: point(0, 20, 28), comparison: point(6.3, 29, 29) },
      ],
    }],
  };
}

function readCsv(text) {
  const [headers, ...rows] = text.trimEnd().split('\r\n').map((line) =>
    Array.from(`${line},`.matchAll(/(?:"((?:[^"]|"")*)"|()),/g), ([, quoted]) => quoted?.replaceAll('""', '"') ?? ''));
  return rows.map((row) => Object.fromEntries(headers.map((column, index) => [column, row[index]])));
}

test('CSV binds each report row to year-specific provider and display identities', () => {
  const report = fixture();
  const [annual, missing, february, previous, previousJanuary, previousFebruary] = readCsv(comparisonCsv(report));
  assert.equal(annual.calendar_year, '2025');
  assert.equal(annual.selection_role, 'selected');
  assert.equal(annual.period, 'annual');
  assert.equal(annual.calendar_month, '');
  assert.equal(annual.scope, 'provider-context');
  assert.equal(annual.metric, 'Precipitation, liquid equivalent');
  assert.equal(annual.unit, 'mm');
  assert.equal(annual.time_standard, 'Station observation day');
  assert.equal(annual.geographic_support, 'station');
  assert.equal(annual.attribution, report.series[0].attribution);
  assert.equal(annual.snapshot_sha256, 'a'.repeat(64));
  assert.equal(annual.snapshot_url, '/science-data/test.json');
  assert.equal(annual.source_urls, 'https://example.invalid/2025.zip');
  assert.equal(annual.source_capture_sha256, 'c'.repeat(64));
  assert.equal(annual.source_captured_at, '2026-11-26T12:00:00Z');
  assert.deepEqual(JSON.parse(annual.provider_sources_json), [capture(2025, 'c')]);
  assert.deepEqual(JSON.parse(annual.comparison_limitations_json), report.limitations);
  assert.equal(previous.source_urls, 'https://example.invalid/2024.zip');
  assert.equal(previous.selection_role, 'comparison');
  assert.equal(previousFebruary.expected_count, '29');
  assert.equal(previousJanuary.value, '0');
  assert.equal(previousJanuary.support_state, 'complete-support');
  assert.equal(february.value, '0');
  assert.equal(february.support_state, 'partial-support');
  assert.equal(missing.period, 'monthly');
  assert.equal(missing.calendar_month, '1');
  assert.equal(missing.value, '');
  assert.equal(missing.support_state, 'unavailable');
  assert.equal(missing.valid_count, '0');
  assert.equal(missing.expected_count, '31');
});

test('text exports neutralize formula-like prefixes while leaving negative numbers numeric', () => {
  const report = fixture();
  const [series] = report.series;
  series.location.name = '\u200b\t=1+1';
  series.label = '  +1+1';
  series.timeStandard = '@SUM(1,1)';
  series.attribution = '－SUM(1,1)';
  series.annual.selected.value = -3.5;
  const [first] = readCsv(comparisonCsv(report));
  assert.equal(first.metric, "'  +1+1");
  assert.equal(first.place, "'\u200b\t=1+1");
  assert.equal(first.time_standard, "'@SUM(1,1)");
  assert.equal(first.attribution, "'－SUM(1,1)");
  assert.equal(first.value, '-3.5');
});

test('JSON is deterministic and preserves unavailable values, limitations, and provider metadata', () => {
  const report = fixture();
  assert.equal(comparisonJson(report), comparisonJson(structuredClone(report)));
  assert.deepEqual(JSON.parse(comparisonJson(report)), report);
  assert.equal(comparisonExportFilename(report, 'csv'), 'kfm-science-comparison-2025-vs-2024.csv');
  assert.equal(comparisonExportFilename(report, 'json'), 'kfm-science-comparison-2025-vs-2024.json');
  assert.throws(() => comparisonExportFilename(report, 'html'));
  assert.throws(() => comparisonJson({ ...report, selection: { year: 2025, compareYear: 2025 } }));
  assert.throws(() => comparisonJson({ ...report, series: [] }));
  assert.throws(() => comparisonCsv(null));
});

test('area identity survives exports and distinguishes the two new comparison filenames', () => {
  const report = fixture();
  for (const [id, name] of [['wichita', 'Wichita and Sedgwick County'], ['dodge-city', 'Dodge City and Ford County']]) {
    const moved = { ...report, location: { id, name } };
    assert.equal(comparisonExportFilename(moved, 'csv'), `kfm-science-comparison-${id}-2025-vs-2024.csv`);
    assert.deepEqual(JSON.parse(comparisonJson(moved)).location, { id, name });
    assert.equal(readCsv(comparisonCsv(moved))[0].comparison_place, name);
  }
});
