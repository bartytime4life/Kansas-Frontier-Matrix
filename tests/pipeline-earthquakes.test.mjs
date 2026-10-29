import test from 'node:test';
import assert from 'node:assert/strict';
import { generateKeyPairSync, sign } from 'node:crypto';
import { readFile, writeFile, mkdtemp } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { loadConfig } from '../scripts/pc-pipeline/worker.mjs';
import { canonical, recipeDigest, verifyProfile, MAX_PACKAGE, SOURCES } from '../server/pipeline-contract.mjs';
import { captureRequest, fetchCapture, CAPTURE_SOURCES } from '../server/ingestion-sources.mjs';
import { normalizeCapture, validateContext } from '../server/pipeline-normalize.mjs';
import { publicContext } from '../server/pipeline-handler.mjs';
import { storagePolicy } from '../scripts/pc-pipeline/storage-policy.mjs';

const now = Date.now();
const request = captureRequest('usgs-earthquakes', now);
// The shape USGS FDSN returns for format=geojson: depth as the third coordinate, epoch-millisecond times.
const quake = (id, props = {}, coordinates = [-97.6, 37.2, 5.3]) => ({ type: 'Feature', id, geometry: { type: 'Point', coordinates },
  properties: { mag: 2.7, magType: 'ml', place: '10 km SW of Medford, Oklahoma', time: request.slot - 3600000, updated: request.slot - 1800000, status: 'reviewed', type: 'earthquake',
    url: 'https://example.invalid/not-the-usgs-page', felt: 3, net: 'us', code: 'x', privateField: 'MUST_NOT_PUBLISH', ...props } });
async function normalized(features) {
  const capture = await fetchCapture(request, { fetcher: async () => Response.json({ type: 'FeatureCollection', features }) });
  return normalizeCapture(request, capture);
}

test('earthquakes are a fourth released source, captured hourly inside the release profiles\' freshness', () => {
  assert.ok(SOURCES.includes('usgs-earthquakes'));
  assert.equal(CAPTURE_SOURCES.find(s => s.id === 'usgs-earthquakes').intervalMs, 3_600_000);
  assert.match(request.url, /^https:\/\/earthquake\.usgs\.gov\/fdsnws\/event\/1\/query\?/);
});

test('the normalizer keeps an allowlisted, two-dimensional earthquake with its depth, and drops retracted events', async () => {
  const { product } = await normalized([quake('us7000abcd'), quake('ok2026xyz', { status: 'automatic', mag: null, magType: null }, [-97.9, 36.95, 7.1]), quake('us7000gone', { status: 'deleted' })]);
  assert.deepEqual(product.data.features.map(f => f.id), ['ok2026xyz', 'us7000abcd'], 'deleted events are not shown; ids sorted');
  const f = product.data.features[1];
  assert.deepEqual(f.geometry, { type: 'Point', coordinates: [-97.6, 37.2] });
  assert.deepEqual(f.properties, { magnitude: 2.7, magnitudeType: 'ml', place: '10 km SW of Medford, Oklahoma', depthKm: 5.3,
    observedAt: new Date(request.slot - 3600000).toISOString(), updatedAt: new Date(request.slot - 1800000).toISOString(), status: 'reviewed',
    eventUrl: 'https://earthquake.usgs.gov/earthquakes/eventpage/us7000abcd', sourceFeatureId: 'us7000abcd' }, 'provider url and private fields never travel');
  assert.equal(product.data.features[0].properties.magnitude, null);
  assert.equal(product.evidenceRole, 'EXTERNAL_CONTEXT_ONLY');
  assert.equal(validateContext(JSON.parse(canonical(product))).sourceId, 'usgs-earthquakes');
});

test('schema drift, out-of-window events and odd ids fail closed', async () => {
  await assert.rejects(normalized([quake('us1', { status: 'preliminary' })]), /EARTHQUAKE_SCHEMA_CHANGED/);
  await assert.rejects(normalized([quake('us1', { type: 'quarry blast' })]), /EARTHQUAKE_SCHEMA_CHANGED/);
  await assert.rejects(normalized([quake('US-1/../x')]), /EARTHQUAKE_SCHEMA_CHANGED/);
  await assert.rejects(normalized([quake('us1', { mag: 12 })]), /EARTHQUAKE_SCHEMA_CHANGED/);
  await assert.rejects(normalized([quake('us1', { time: request.slot - 31 * 86400000 })]), /OBSERVATION_OUTSIDE_WINDOW/);
  await assert.rejects(normalized([quake('us1', {}, [-90, 37.2, 5])]), /GEOGRAPHIC_SCOPE_INVALID/);
  await assert.rejects(normalized([quake('us1', {}, [-97.6, 37.2])]), /GEOMETRY_INVALID/);
});

test('the context validator rejects anything the normalizer would not produce', async () => {
  const { product } = await normalized([quake('us7000abcd')]);
  const tamper = change => { const copy = JSON.parse(canonical(product)); change(copy.data.features[0]); return copy; };
  assert.throws(() => validateContext(tamper(f => { f.properties.felt = 3; })), /CONTEXT_INVALID/);
  assert.throws(() => validateContext(tamper(f => { f.properties.eventUrl = 'https://example.invalid/'; })), /CONTEXT_INVALID/);
  assert.throws(() => validateContext(tamper(f => { f.properties.status = 'deleted'; })), /CONTEXT_INVALID/);
  assert.throws(() => validateContext(tamper(f => { f.properties.depthKm = 9000; })), /CONTEXT_INVALID/);
});

test('an earthquake release profile verifies as external context, and the public read admits the source', async () => {
  const keys = generateKeyPairSync('ed25519');
  const profile = { format: 'kfm-pc-release-delegation-v1', id: 'quake-fixture', sourceId: 'usgs-earthquakes', recipeSha256: await recipeDigest(), approver: 'fixture-owner',
    validFrom: new Date(now - 60000).toISOString(), expiresAt: new Date(now + 86400000).toISOString(), rights: 'redistribution-allowed', sensitivity: 'public',
    sourceRef: 'kfm://source/usgs-earthquakes', rightsRef: 'kfm://review/r', reviewRef: 'kfm://review/x', releaseProfileRef: 'kfm://release/profile/q',
    maxBytes: MAX_PACKAGE, maxRows: 1000, staleAfterSeconds: 7200, role: 'external-context' };
  const signed = { profile, signature: sign(null, Buffer.from(canonical(profile)), keys.privateKey).toString('base64url') };
  assert.equal(verifyProfile(signed, keys.publicKey.export({ format: 'pem', type: 'spki' }), { now, recipe: profile.recipeSha256, sourceId: 'usgs-earthquakes' }).id, 'quake-fixture');
  const store = { active: async () => null };
  assert.deepEqual(await publicContext('usgs-earthquakes', { store, environment: {}, now }), { state: 'withheld', reason: 'NO_APPROVED_RELEASE', sourceId: 'usgs-earthquakes' });
});

test('the PC worker publishes earthquakes only when its config names them; the schema has their head row', async () => {
  assert.deepEqual(storagePolicy({}).priority, ['nws-alerts', 'usgs-streamflow', 'usgs-earthquakes']);
  assert.deepEqual(storagePolicy({ storagePolicy: { priority: ['usgs-streamflow', 'nws-alerts'] } }).priority, ['usgs-streamflow', 'nws-alerts'], 'earlier two-source configs still load');
  assert.throws(() => storagePolicy({ storagePolicy: { priority: ['nws-alerts', 'nws-alerts'] } }), /STORAGE_POLICY_INVALID/);
  assert.throws(() => storagePolicy({ storagePolicy: { priority: ['nws-alerts', 'usgs-streamflow', 'water'] } }), /STORAGE_POLICY_INVALID/);
  const worker = await readFile('scripts/pc-pipeline/worker.mjs', 'utf8'), cli = await readFile('scripts/pc-pipeline/cli.mjs', 'utf8'), schema = await readFile('server/pipeline-schema.sql', 'utf8');
  assert.match(worker, /for \(const sourceId of policy\.priority\.filter\(id => config\.sources\.includes\(id\)\)\)/, 'opt-in through config.sources');
  assert.match(cli, /sources: \['usgs-streamflow','nws-alerts'\], publish: false/, 'new installs start with the original two');
  assert.match(schema, /\('usgs-earthquakes'\)/);
});

test('a worker config that opts into earthquakes loads; one naming a source twice or a fourth does not', async () => {
  const dir = await mkdtemp(join(tmpdir(), 'kfm-quake-config-'));
  const base = { format: 'kfm-pc-pipeline-config-v1', root: '/srv/kfm', mount: '/srv', device: 2049, storeId: 'a'.repeat(32), publish: false, approvalDirectory: '/etc/kfm-pipeline/approvals' };
  const write = async (name, sources) => { const path = join(dir, name); await writeFile(path, JSON.stringify({ ...base, sources })); return path; };
  assert.deepEqual((await loadConfig(await write('two.json', ['usgs-streamflow', 'nws-alerts']))).sources, ['usgs-streamflow', 'nws-alerts']);
  assert.deepEqual((await loadConfig(await write('three.json', ['usgs-streamflow', 'nws-alerts', 'usgs-earthquakes']))).sources, ['usgs-streamflow', 'nws-alerts', 'usgs-earthquakes'],
    'the documented opt-in adds a third source');
  await assert.rejects(loadConfig(await write('twice.json', ['usgs-streamflow', 'usgs-earthquakes', 'usgs-earthquakes'])), /CONFIG_INVALID/);
  await assert.rejects(loadConfig(await write('four.json', ['usgs-streamflow', 'nws-alerts', 'usgs-earthquakes', 'water'])), /CONFIG_INVALID/);
});
