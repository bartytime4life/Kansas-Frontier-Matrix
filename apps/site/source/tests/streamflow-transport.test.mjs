import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import ts from 'typescript';
const moduleFor = async path => import(`data:text/javascript;base64,${Buffer.from(ts.transpileModule(await readFile(path, 'utf8'), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText).toString('base64')}`);
const { encodeStreamflowTransport: encode, decodeStreamflowTransport: decode, STREAMFLOW_TRANSPORT } = await moduleFor('app/streamflow-transport.ts');
const { parseStreamflowBundle, buildStreamflowFrame, streamflowDisplayFrames } = await moduleFor('app/streamflow.ts');
const stationId = 'USGS-06864500';
const observation = (value, patch = {}) => ({ stationId, observedAt: '2026-10-11T00:15:00.000Z', value, unit: 'ft^3/s', parameterCode: '00060', statisticId: null, approvalStatus: 'Provisional', qualifier: ['P'], qualifiers: ['P'], lastModified: '2026-10-11T00:20:00.000Z', ...patch });
const packet = (observations, state = 'ready') => ({ format: 'kfm-usgs-streamflow-v1', feed: 'usgs-streamflow', state, retrievedAt: '2026-10-11T01:00:00.000Z', query: { mode: 'recent-series', start: '2026-10-10T01:00:00.000Z', end: '2026-10-11T01:00:00.000Z', parameterCode: '00060' }, stations: [{ stationId, name: 'Ellsworth', longitude: -98.23, latitude: 38.73, agencyCode: 'USGS', siteTypeCode: 'ST' }], observations, source: 'https://api.waterdata.usgs.gov/ogcapi/v1/collections/continuous', limitation: 'Source-specific qualification retained', truncated: false, interpolation: false, evidenceRole: 'EXTERNAL_CONTEXT_ONLY' });

test('wire roundtrip preserves zero, null, precision, dates, qualifiers, revision and all source metadata', () => {
  const original = packet([observation(0), observation(null, { observedAt: '2026-10-11T00:30:00.000Z', qualifier: null, qualifiers: [] }), observation(1.23456789012345, { observedAt: '2026-10-11T00:45:00.000Z', approvalStatus: 'Approved', statisticId: '00011', lastModified: null })], 'partial');
  original.truncated = true;
  const wire = JSON.parse(JSON.stringify(encode(original)));
  assert.equal(wire.transport, STREAMFLOW_TRANSPORT);
  assert.deepEqual(decode(wire), original);
  const legacy = parseStreamflowBundle(original), compact = parseStreamflowBundle(decode(wire));
  assert.deepEqual(compact, legacy);
  assert.deepEqual(streamflowDisplayFrames(compact), streamflowDisplayFrames(legacy));
  assert.deepEqual(buildStreamflowFrame(compact, '2026-10-11T00:45:00.000Z', 30), buildStreamflowFrame(legacy, '2026-10-11T00:45:00.000Z', 30));
});

test('empty and legacy packets remain compatible; future observation attributes cannot be silently discarded', () => {
  const empty = packet([], 'empty'); assert.deepEqual(decode(JSON.parse(JSON.stringify(encode(empty)))), empty);
  assert.equal(decode(empty), empty);
  const future = packet([observation(0, { providerUncertainty: 'new field' })]); assert.equal(encode(future), future);
});

test('hostile compact dimensions, indices and parameter values fail rather than bypass canonical validation', () => {
  const make = () => structuredClone(encode(packet([observation(0)])));
  for (const change of [w => w.transport = 'unknown', w => w.observations.rows = Array(100001).fill([]), w => w.observations.values.push([]), w => w.observations.rows[0].pop(), w => w.observations.rows[0][0] = -1, w => w.observations.rows[0][0] = .5, w => w.observations.rows[0][0] = 1, w => w.observations.values[0].push('unused')]) {
    const wire = make(); change(wire); assert.throws(() => decode(wire));
  }
  const wire = make(); wire.observations.values[4][0] = '00065'; assert.throws(() => parseStreamflowBundle(decode(wire)), /invalid bundle/);
});

test('a realistic repeated-observation window shrinks without changing the full sample count', () => {
  const original = packet(Array.from({ length: 18000 }, (_, i) => observation(i % 100 + .012345, { stationId: `USGS-${String(6800000 + i % 150).padStart(8, '0')}`, observedAt: new Date(Date.parse('2026-10-10T01:00:00Z') + Math.floor(i / 150) * 600000).toISOString() })));
  const wire = encode(original);
  assert.deepEqual(decode(wire), original);
  assert.ok(Buffer.byteLength(JSON.stringify(wire)) < Buffer.byteLength(JSON.stringify(original)) * .25);
});
