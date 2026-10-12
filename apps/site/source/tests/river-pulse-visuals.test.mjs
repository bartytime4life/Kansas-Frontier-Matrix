import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import ts from 'typescript';
const code = ts.transpileModule(await readFile('app/river-pulse-visuals.ts', 'utf8'), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const { riverSignalGroups, nearestRiverSample } = await import(`data:text/javascript;base64,${Buffer.from(code).toString('base64')}`);

test('network segments partition gauges without counting zero as flowing or stale as measured', () => {
  const values = [{ value: 5, trend: 'rising' }, { value: 3, trend: 'falling' }, { value: 9, trend: 'steady' }, { value: 2, trend: 'unknown' }, { value: 0, trend: 'falling' }, { value: 4, missing: true, trend: 'rising' }, { value: null }];
  const groups = riverSignalGroups({ features: values.map((properties, i) => ({ properties: { ...properties, stationId: String(i) } })) });
  assert.deepEqual(groups.map(g => g.stations.length), [1, 1, 1, 1, 1, 2]);
  assert.equal(new Set(groups.flatMap(g => g.stations)).size, values.length);
  assert.ok(riverSignalGroups(null).every(g => g.stations.length === 0));
});

test('sample inspection chooses actual nulls and boundaries without interpolation', () => {
  const values = [0, 15, 60].map((minute, i) => ({ observedAt: new Date(Date.UTC(2026, 9, 4, 0, minute)).toISOString(), value: i === 1 ? null : i }));
  const origin = Date.parse(values[0].observedAt);
  assert.equal(nearestRiverSample(values, origin + 15 * 60000), 1);
  assert.equal(nearestRiverSample(values, origin + 30 * 60000), 1);
  assert.equal(nearestRiverSample(values, origin - 60000), 0);
  assert.equal(nearestRiverSample(values, origin + 100 * 60000), 2);
  assert.equal(nearestRiverSample([], origin), -1);
  assert.equal(nearestRiverSample(values, NaN), -1);
});
