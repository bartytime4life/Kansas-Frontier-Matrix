import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { pathToFileURL } from 'node:url';
import path from 'node:path';
import test from 'node:test';
import ts from 'typescript';

const time = new Date(Date.now() - 600_000).toISOString();
const ids = ['USGS-06800001', 'USGS-06800002', 'USGS-06800003'];
const observation = (id) => ({ type: 'Feature', id, geometry: { type: 'Point', coordinates: [-98, 38] }, properties: {
  time_series_id: id, monitoring_location_id: id, parameter_code: '00060', statistic_id: '00011',
  time, value: 10, unit_of_measure: 'ft^3/s', approval_status: 'Provisional', qualifier: null, last_modified: time,
} });
const metadata = (id) => ({ type: 'Feature', id, geometry: { type: 'Point', coordinates: [-98, 38] }, properties: {
  id, agency_code: 'USGS', monitoring_location_number: id.slice(5), monitoring_location_name: id,
  site_type_code: 'ST', hydrologic_unit_code: null, county_name: null, drainage_area: null, contributing_drainage_area: null,
} });
const collection = (features, extra = {}) => Response.json({ type: 'FeatureCollection', features, numberReturned: features.length,
  links: [], timeStamp: time, ...extra });
const request = () => ({ nextUrl: new URL('https://local/api/hydrology/streamflow?mode=network&range=24h') });

async function routeWithLimits(byteCap, observationCap = 100_000, deadlineMs = 60_000) {
  let source = await readFile('app/api/hydrology/streamflow/route.ts', 'utf8');
  source = source.replace('const NETWORK_RESPONSE_BYTES_CAP = 24 * 1024 * 1024;', `const NETWORK_RESPONSE_BYTES_CAP = ${byteCap};`)
    .replace('const NETWORK_OBSERVATION_CAP = 100_000;', `const NETWORK_OBSERVATION_CAP = ${observationCap};`)
    .replace('const NETWORK_DEADLINE_MS = 60_000;', `const NETWORK_DEADLINE_MS = ${deadlineMs};`);
  assert.match(source, new RegExp(`NETWORK_RESPONSE_BYTES_CAP = ${byteCap}`));
  const js = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText.replace('import { env } from "cloudflare:workers";', 'const env = { USGS_WATER_API_KEY: "test-key-only-not-a-real-key" };')
    .replace('from "next/server"', `from ${JSON.stringify(pathToFileURL(path.resolve('node_modules/next/server.js')).href)}`);
  return (await import(`data:text/javascript;base64,${Buffer.from(js).toString('base64')}`)).GET;
}

test('aggregate byte budget holds remaining network groups without inventing readings', async () => {
  const GET = await routeWithLimits(4_000);
  const original = globalThis.fetch;
  globalThis.fetch = async input => {
    const url = new URL(input);
    if (url.pathname.includes('latest-continuous')) return collection(ids.map(observation));
    if (url.pathname.includes('monitoring-locations')) return collection(ids.map(metadata));
    return collection(ids.map(observation), { padding: 'x'.repeat(4_000) });
  };
  try {
    const response = await GET(request());
    assert.equal(response.status, 200);
    const body = await response.json();
    assert.equal(body.partial, true);
    assert.equal(body.truncated, true);
    assert.equal(body.stations.length, 3);
    assert.equal(body.observations.length, 0);
    assert.match(body.limitation, /request-wide time, byte, or observation budget/);
  } finally { globalThis.fetch = original; }
});

test('deadline before a usable inventory fails without a fabricated network', async () => {
  const GET = await routeWithLimits(64_000, 100_000, 5);
  const original = globalThis.fetch;
  globalThis.fetch = async () => {
    await new Promise(resolve => setTimeout(resolve, 20));
    return collection(ids.map(observation));
  };
  try {
    const response = await GET(request());
    assert.equal(response.status, 503);
    assert.equal((await response.json()).code, 'USGS_STREAMFLOW_BUDGET_EXCEEDED');
  } finally { globalThis.fetch = original; }
});

test('observation budget is applied before aggregate sort and disclosed as partial', async () => {
  const GET = await routeWithLimits(64_000, 2);
  const original = globalThis.fetch;
  globalThis.fetch = async input => {
    const url = new URL(input);
    if (url.pathname.includes('latest-continuous')) return collection(ids.map(observation));
    if (url.pathname.includes('monitoring-locations')) return collection(ids.map(metadata));
    return collection(ids.map(observation));
  };
  try {
    const response = await GET(request());
    assert.equal(response.status, 200);
    const body = await response.json();
    assert.equal(body.observations.length, 2);
    assert.equal(body.partial, true);
    assert.equal(body.truncated, true);
  } finally { globalThis.fetch = original; }
});

test('a second in-flight network request is rejected before provider fan-out', async () => {
  const GET = await routeWithLimits(64_000);
  const original = globalThis.fetch;
  let releaseInventory;
  const inventoryHeld = new Promise(resolve => { releaseInventory = resolve; });
  let inventoryStarted;
  const started = new Promise(resolve => { inventoryStarted = resolve; });
  let calls = 0;
  globalThis.fetch = async input => {
    calls++;
    const url = new URL(input);
    if (url.pathname.includes('latest-continuous')) {
      inventoryStarted();
      await inventoryHeld;
      return collection(ids.map(observation));
    }
    if (url.pathname.includes('monitoring-locations')) return collection(ids.map(metadata));
    return collection(ids.map(observation));
  };
  try {
    const first = GET(request());
    await started;
    const second = await GET(request());
    assert.equal(second.status, 429);
    assert.equal(calls, 1);
    releaseInventory();
    assert.equal((await first).status, 200);
  } finally { releaseInventory(); globalThis.fetch = original; }
});
