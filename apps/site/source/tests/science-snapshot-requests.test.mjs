import assert from 'node:assert/strict';
import { webcrypto } from 'node:crypto';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import { brotliCompressSync, brotliDecompressSync, gzipSync, gunzipSync } from 'node:zlib';
import { loadAirSnapshot } from '../app/labs/daily-air-quality/snapshot-loader.mjs';
import { loadClimateSnapshot } from '../app/labs/heat-and-rain/snapshot-loader.mjs';
import { loadDroughtSnapshot } from '../app/labs/county-drought/snapshot-loader.mjs';
import { loadSoilSnapshot } from '../app/labs/soil-profile/snapshot-loader.mjs';
import { loadSunlightSnapshot } from '../app/labs/sunlight-and-sky/snapshot-loader.mjs';

const manifest = async (lab) => JSON.parse(await readFile(new URL(`../app/labs/${lab}/snapshot-manifest.json`, import.meta.url)));
const [air, climate, drought, soil, sunlight] = await Promise.all([
  manifest('daily-air-quality'), manifest('heat-and-rain'), manifest('county-drought'),
  manifest('soil-profile'), manifest('sunlight-and-sky'),
]);

test('all shipped science manifests resolve to fixed same-origin GET requests', async () => {
  const cases = [
    [loadAirSnapshot, air, air.snapshot],
    [loadDroughtSnapshot, drought, drought.snapshot],
    ...climate.stations.map((item) => [loadClimateSnapshot, item, item]),
    ...soil.stations.map((item) => [loadSoilSnapshot, item, item]),
    ...sunlight.points.map((item) => [loadSunlightSnapshot, item, item]),
  ];
  for (const [load, input, descriptor] of cases) {
    const data = await readFile(new URL(`../public${descriptor.url}`, import.meta.url));
    let requests = 0;
    const result = await load(input, {
      cryptoImpl: webcrypto,
      fetchImpl: async (url, options) => {
        requests += 1;
        assert.equal(url, descriptor.url);
        assert.equal(options.method, 'GET');
        assert.equal(options.mode, 'same-origin');
        assert.equal(options.credentials, 'same-origin');
        assert.equal(options.redirect, 'error');
        assert.equal(options.body, undefined);
        return new Response(data, { headers: { 'content-length': String(data.byteLength) } });
      },
    });
    assert.ok(result);
    assert.equal(requests, 1);
  }
});

test('both reported loaders reject unregistered destinations before reading the transport', async () => {
  const options = { fetchImpl: () => assert.fail('unexpected snapshot request') };
  const climateDescriptor = climate.stations[0];
  for (const [load, descriptor] of [[loadClimateSnapshot, climateDescriptor], [loadSoilSnapshot, soil.stations[0]]]) {
    const url = descriptor.url;
    const differentHash = '0'.repeat(64);
    await assert.rejects(load({ ...descriptor, sha256: differentHash,
      url: url.replace(descriptor.sha256.slice(0, 16), differentHash.slice(0, 16)) }, options), /Invalid science snapshot manifest/);
    for (const other of ['https://example.invalid/data.json', `//example.invalid${url}`, `${url}?format=json`, `${url}#fragment`]) {
      await assert.rejects(load({ ...descriptor, url: other }, options), /Invalid science snapshot manifest/);
    }
  }
  await assert.rejects(loadClimateSnapshot({ ...climateDescriptor, id: null }, options), /Invalid science snapshot manifest/);
});

test('climate snapshots retain decoded size and hash checks when the wire length is compressed', async () => {
  const descriptor = climate.stations[0];
  const data = await readFile(new URL(`../public${descriptor.url}`, import.meta.url));
  for (const [encoding, compress, decompress] of [['gzip', gzipSync, gunzipSync], ['br', brotliCompressSync, brotliDecompressSync]]) {
    const wired = compress(data);
    assert.notEqual(wired.byteLength, data.byteLength);
    const options = {
      cryptoImpl: webcrypto,
      fetchImpl: async () => new Response(decompress(wired), { headers: { 'content-encoding': encoding, 'content-length': String(wired.byteLength) } }),
    };
    assert.equal((await loadClimateSnapshot(descriptor, options)).station.id, descriptor.id);
    const tampered = Buffer.from(data);
    tampered[100] ^= 1;
    await assert.rejects(loadClimateSnapshot(descriptor, {
      ...options, fetchImpl: async () => new Response(tampered, { headers: { 'content-encoding': encoding } }),
    }), /integrity check/);
  }
});
