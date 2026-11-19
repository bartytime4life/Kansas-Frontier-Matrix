import { readFileSync } from 'node:fs';
import assert from 'node:assert/strict';
import test from 'node:test';
import {
  observationDate, rangeLabel, reportingLimit, resultText,
  waterBrief, waterComparison, waterCsvRecords, waterRecordSelection,
} from '../app/labs/water-chemistry/water-model.mjs';

const snapshot = JSON.parse(readFileSync(new URL('../app/labs/water-chemistry/water-snapshot.json', import.meta.url), 'utf8'));

test('Water Chemistry snapshot binds source receipts, station, dated windows and exact analysis context', () => {
  assert.equal(snapshot.format, 'kfm-water-chemistry-v1');
  assert.equal(snapshot.station.id, 'USGS-07144100');
  assert.equal(snapshot.station.datum, 'NAD83');
  assert.equal(snapshot.context.USGSPCode, '00618');
  assert.equal(snapshot.context['ResultAnalyticalMethod/MethodIdentifier'], 'ALGOR');
  assert.equal(snapshot.context['SampleCollectionMethod/MethodIdentifier'], '15');
  assert.equal(snapshot.context.SampleCollectionEquipmentName, 'US DH-81');
  assert.equal(new Set(snapshot.records.map(record => record.activityId)).size, 28);
  for (const source of Object.values(snapshot.sources)) {
    assert.equal(new URL(source.url).hostname, 'waterqualitydata.us');
    assert.match(source.sha256, /^[a-f0-9]{64}$/);
    assert.ok(source.rawBytes > 0 && source.rawBytes < 500_000);
    assert.ok(Number.isFinite(Date.parse(source.retrievedAt)));
  }
  for (const record of snapshot.records) {
    assert.equal(record.activityId, record.source.ActivityIdentifier);
    for (const [field, value] of Object.entries(snapshot.context)) assert.equal(record.source[field], value);
    const period = snapshot.periods.find(entry => entry.id === record.period);
    assert.ok(observationDate(record) >= period.from && observationDate(record) <= period.to);
  }
});

test('Water Chemistry counts reconcile within each period and both distributions use shared boundaries', () => {
  const { summaries, bins } = waterComparison(snapshot);
  assert.deepEqual(summaries.map(period => [period.retained, period.quantified, period.nonDetects, period.sampledMonths]), [
    [15, 14, 1, 14], [13, 13, 0, 12],
  ]);
  for (const period of summaries) {
    assert.equal(period.returned, period.retained + period.otherContext + period.qualifiedOther);
  }
  assert.deepEqual(bins.map(bin => bin.records.length), [4, 8, 8, 6, 0, 1]);
  assert.equal(bins.flatMap(bin => bin.records).length, 27);
  assert.equal(new Set(bins.flatMap(bin => bin.records.map(record => record.activityId))).size, 27);
  assert.equal(bins[1].records.find(record => record.source.ResultMeasureValue === '0.300')?.period, 'later');
  assert.ok(!bins[0].records.some(record => record.source.ResultMeasureValue === '0.300'));
  assert.equal(rangeLabel(bins.at(-1)), '1.5 to 1.8 inclusive');
});

test('Water Chemistry inspection and exports preserve non-detects and original record identities', () => {
  const rows = waterRecordSelection(snapshot, { detection: 'not-detected', period: 'earlier' });
  assert.equal(rows.length, 1);
  assert.equal(observationDate(rows[0]), '2020-04-21');
  assert.equal(resultText(rows[0]), 'Not detected');
  assert.equal(reportingLimit(rows[0]), '0.035');
  assert.equal(waterRecordSelection(snapshot, { detection: 'not-detected', period: 'later' }).length, 0);
  const [header, exported] = waterCsvRecords(rows);
  assert.equal(exported[header.indexOf('result_value')], '');
  assert.equal(exported[header.indexOf('reporting_limit')], '0.035');
  const brief = waterBrief(snapshot);
  assert.ok(brief.includes(rows[0].activityId));
  assert.ok(brief.includes(snapshot.sources.results.sha256));
  assert.ok(brief.includes('14/24'));
  assert.match(brief, /cannot establish a trend/);
});
