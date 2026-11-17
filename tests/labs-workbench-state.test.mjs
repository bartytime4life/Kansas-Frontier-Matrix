import test from 'node:test';
import assert from 'node:assert/strict';
import { parseCountyCSV, readCountyCSV } from '../app/labs/county-csv.mjs';
import { saveLocalInvestigation, listLocalInvestigations, deleteLocalInvestigation, exportLocalInvestigations, sourceBindingsMatch } from '../app/labs/notebook.mjs';
import { encodeWorkbenchView, decodeWorkbenchView } from '../app/labs/workbench-view.mjs';
const bindings = { 'census-mosaic': 'a'.repeat(64) };
const memory = () => { const map = new Map(); return { getItem: key => map.get(key), setItem: (key, value) => map.set(key, value) }; };
test('county CSV handles quoted Unicode headers, blank measures, BOM and exact FIPS joins', () => {
  const parsed = parseCountyCSV('\uFEFFFIPS,"My measure, μ",Other\r\n20001,0,NA\r\n20209,-2.5,3e2\r\n');
  assert.deepEqual(parsed.rows, [{ fips: '20001', csv_0: 0, csv_1: null }, { fips: '20209', csv_0: -2.5, csv_1: 300 }]);
  assert.equal(parsed.columns[0].label, 'My measure, μ'); assert.equal(parsed.diagnostics.missingValues, 1);
});
test('county CSV rejects ambiguous identifiers, duplicate counties, ragged rows and formulas', () => {
  for (const csv of ['FIPS,x\n20002,1', 'FIPS,x\n20001,1\n20001,2', 'FIPS,x\n20001,1,2', 'FIPS,x\n20001,=1+2', 'FIPS,x\n20001,Infinity', 'FIPS,x\n20001,"2', 'FIPS,FIPS\n20001,1', 'FIPS,x,x\n20001,1,2', 'FIPS,x\n20001,"2"abc']) assert.throws(() => parseCountyCSV(csv));
});
test('private CSV hash binds exact file bytes and read limit is enforced before reading', async () => {
  const file = new File(['FIPS,x\n20001,2'], 'private.csv'); const parsed = await readCountyCSV(file);
  assert.match(parsed.sha256, /^[a-f0-9]{64}$/); assert.equal(parsed.bytes, file.size); assert.equal(parsed.fileName, 'private.csv');
  await assert.rejects(readCountyCSV({ size: 524289, arrayBuffer: () => { throw new Error('must not read'); } }), /512 KB/);
});
test('local notebook persists/reopens private rows, exact source bindings and settings', async () => {
  const storage = memory(), privateData = await readCountyCSV(new File(['FIPS,x\n20001,2'], 'private.csv'));
  const saved = saveLocalInvestigation({ workspace: 'county', title: 'Income vs my data', state: { x: 'csv_0', year: 2024 }, sourceBindings: bindings, privateData }, storage);
  assert.deepEqual(listLocalInvestigations(storage), [saved]); assert.equal(JSON.parse(exportLocalInvestigations(storage)).entries[0].privateData.rows[0].csv_0, 2);
  assert.ok(sourceBindingsMatch(bindings, saved.sourceBindings)); assert.ok(!sourceBindingsMatch(bindings, { ...bindings, extra: 'b'.repeat(64) }));
  deleteLocalInvestigation(saved.id, storage); assert.deepEqual(listLocalInvestigations(storage), []);
});
test('notebook rejects nested state, untrusted private data and storage failures', () => {
  const storage = memory(), input = { workspace: 'signal', title: 'Test', state: { x: 'a' }, sourceBindings: bindings };
  assert.throws(() => saveLocalInvestigation({ ...input, state: { x: { url: 'https://example.com' } } }, storage));
  assert.throws(() => saveLocalInvestigation({ ...input, state: JSON.parse('{"__proto__":1}') }, storage));
  assert.throws(() => saveLocalInvestigation({ ...input, privateData: { rows: [] } }, storage));
  assert.throws(() => saveLocalInvestigation(input, { getItem: () => null, setItem: () => { throw new Error('quota'); } }), /could not save/);
  for (let index = 0; index < 12; index++) saveLocalInvestigation(input, storage);
  assert.throws(() => saveLocalInvestigation(input, storage), /12 investigations/);
});
test('share codec preserves Unicode controls and rejects changed sources, other workspaces and private attachments', () => {
  const state = { x: 'climate:20:tmpc', label: 'Δ temperature', from: 1960, to: 2024, lag: -2 }, token = encodeWorkbenchView({ workspace: 'signal', state, sourceBindings: bindings });
  assert.deepEqual(decodeWorkbenchView(token, { workspace: 'signal', sourceBindings: bindings }), { state });
  assert.equal(decodeWorkbenchView(token, { workspace: 'county', sourceBindings: bindings }), null);
  assert.equal(decodeWorkbenchView(token, { workspace: 'signal', sourceBindings: { 'census-mosaic': 'b'.repeat(64) } }), null);
  for (const bad of ['', 'e30', '____', '<script>', 'a'.repeat(12001)]) assert.equal(decodeWorkbenchView(bad, { workspace: 'signal', sourceBindings: bindings }), null);
  const encoded = encodeWorkbenchView({ workspace: 'county', state: { x: 'csv_0' }, sourceBindings: bindings, privateData: { secret: 'private' } });
  assert.ok(!atob(encoded.replace(/-/g, '+').replace(/_/g, '/')).includes('private'));
  assert.throws(() => encodeWorkbenchView({ workspace: 'county', state: Object.fromEntries(Array.from({ length: 15 }, (_, index) => ['key' + index, '🌾'.repeat(150)])), sourceBindings: bindings }), /too large/);
});
