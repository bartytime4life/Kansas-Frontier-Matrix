import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { pathToFileURL } from 'node:url';
import path from 'node:path';
import test from 'node:test';
import ts from 'typescript';
const transportJs = ts.transpileModule(await readFile('app/streamflow-transport.ts', 'utf8'), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const transportUrl = `data:text/javascript;base64,${Buffer.from(transportJs).toString('base64')}`;
const { decodeStreamflowTransport } = await import(transportUrl);
const boundedJs = ts.transpileModule(await readFile('app/bounded-json.ts', 'utf8'), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const boundedUrl = `data:text/javascript;base64,${Buffer.from(boundedJs).toString('base64')}`;
const bounded = await import(boundedUrl);

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
    .replace('from "../../../streamflow-transport"', `from ${JSON.stringify(transportUrl)}`).replace('from "../../../bounded-json"', `from ${JSON.stringify(boundedUrl)}`).replace('from "next/server"', `from ${JSON.stringify(pathToFileURL(path.resolve('node_modules/next/server.js')).href)}`);
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

// Execute the actual private readers as well as GET, with only provider I/O and
// timers supplied by each fixture. This avoids a production-only test export.
const bodyJavaScript = ts.transpileModule((await readFile('app/api/hydrology/streamflow/route.ts', 'utf8')) + '\nexport { readBoundedBody, fetchCollection, NetworkBudgetExceeded, UsgsUpstreamError };', {
  compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 },
}).outputText;
const wire = await import(transportUrl);
function transportFixture(fetcher = async () => { throw new Error('Unexpected fixture transport'); }, timers = { setTimeout, clearTimeout }) {
  const mod = { exports: {} };
  new Function('require', 'module', 'exports', 'fetch', 'setTimeout', 'clearTimeout', 'console', bodyJavaScript)(name => {
    if (name === '../../../bounded-json') return bounded;
    if (name === '../../../streamflow-transport') return wire;
    if (name === 'cloudflare:workers') return { env: { USGS_WATER_API_KEY: 'test-key-only-not-a-real-key' } };
    if (name === 'next/server') return { NextResponse: Response };
    throw new Error(`Unexpected streamflow fixture import: ${name}`);
  }, mod, mod.exports, fetcher, timers.setTimeout, timers.clearTimeout, { error() {} });
  return mod.exports;
}
const responseLimit = 12 * 1024 * 1024;
const budgetFor = remainingBytes => ({ deadline: Date.now() + 60_000, remainingBytes, exhausted: false });
const latestUrl = () => new URL('https://api.waterdata.usgs.gov/ogcapi/v1/collections/latest-continuous/items');

test('both streamflow readers release valid, errored and malformed UTF-8 bodies', async () => {
  const route = transportFixture();
  for (const aggregate of [false, true]) {
    const budget = aggregate ? budgetFor(20) : undefined;
    const response = new Response('{}');
    assert.equal(await route.readBoundedBody(response, new AbortController(), budget), '{}');
    assert.equal(response.body.locked, false); if (budget) assert.equal(budget.remainingBytes, 18);
    const invalid = new Response(Uint8Array.of(0xc3));
    await assert.rejects(route.readBoundedBody(invalid, new AbortController(), aggregate ? budgetFor(20) : undefined), TypeError);
    assert.equal(invalid.body.locked, false);
    const failure = new Error('Fixture body failed');
    const broken = new Response(new ReadableStream({ pull(controller) { controller.error(failure); } }, { highWaterMark: 0 }));
    await assert.rejects(route.readBoundedBody(broken, new AbortController(), aggregate ? budgetFor(20) : undefined), error => error === failure);
    assert.equal(broken.body.locked, false);
  }
});

test('streamflow per-response caps settle despite uncooperative cancellation and release both reader kinds', { timeout: 5000 }, async () => {
  const route = transportFixture();
  for (const aggregate of [false, true]) {
    let pulls = 0, canceled = 0;
    const response = new Response(new ReadableStream({
      pull(controller) { pulls++; controller.enqueue(new Uint8Array(responseLimit / 3)); },
      cancel() { canceled++; return new Promise(() => {}); },
    }, { highWaterMark: 0 }), { headers: { 'Content-Length': '1' } });
    const controller = new AbortController();
    await assert.rejects(route.readBoundedBody(response, controller, aggregate ? budgetFor(responseLimit * 3) : undefined), error => error instanceof route.UsgsUpstreamError && /12 MB adapter limit/.test(error.message));
    assert.equal(pulls, 4); assert.equal(canceled, 1); assert.equal(controller.signal.aborted, true); assert.equal(response.body.locked, false);
  }
});

test('concurrent streamflow bodies debit the shared budget per chunk without starving a healthy response', { timeout: 1000 }, async () => {
  const route = transportFixture(), budget = budgetFor(8);
  let releaseA, releaseB, waiting = 0, started, canceled = 0;
  const ready = new Promise(resolve => { started = resolve; });
  const gates = [new Promise(resolve => { releaseA = resolve; }), new Promise(resolve => { releaseB = resolve; })];
  const streams = gates.map((gate, index) => {
    let step = 0;
    return new Response(new ReadableStream({
      async pull(controller) {
        if (step++ === 0) { controller.enqueue(Uint8Array.of(97, 98, 99)); return; }
        if (step === 2) { if (++waiting === 2) started(); await gate; controller.enqueue(new Uint8Array(index === 0 ? [100] : [101, 102])); return; }
        controller.close();
      },
      cancel() { canceled++; return new Promise(() => {}); },
    }, { highWaterMark: 0 }));
  });
  const first = route.readBoundedBody(streams[0], new AbortController(), budget);
  const second = route.readBoundedBody(streams[1], new AbortController(), budget);
  await ready; assert.equal(budget.remainingBytes, 2);
  releaseA(); assert.equal(await first, 'abcd'); assert.equal(budget.remainingBytes, 1);
  releaseB(); await assert.rejects(second, route.NetworkBudgetExceeded);
  assert.equal(budget.remainingBytes, 1); assert.equal(budget.exhausted, true); assert.equal(canceled, 1);
  assert.equal(streams[0].body.locked, false); assert.equal(streams[1].body.locked, false);
});

test('USGS early status, media, announced-size and malformed-header failures cancel bodies before a read', { timeout: 1000 }, async () => {
  for (const [init, status, code] of [
    [{ status: 302, headers: { Location: 'http://127.0.0.1/private' } }, 502, 'USGS_STREAMFLOW_UNAVAILABLE'],
    [{ status: 503 }, 502, 'USGS_STREAMFLOW_UNAVAILABLE'],
    [{ status: 429, headers: { 'Retry-After': '600' } }, 429, 'USGS_STREAMFLOW_RATE_LIMITED'],
    [{ headers: { 'Content-Type': 'text/html' } }, 502, 'USGS_STREAMFLOW_UNAVAILABLE'],
    [{ headers: { 'Content-Type': 'application/json', 'Content-Length': String(responseLimit + 1) } }, 502, 'USGS_STREAMFLOW_UNAVAILABLE'],
    [{ headers: { 'Content-Type': 'application/json', 'Content-Length': 'unverifiable' } }, 502, 'USGS_STREAMFLOW_UNAVAILABLE'],
  ]) {
    let calls = 0, pulls = 0, canceled = 0;
    const upstream = new Response(new ReadableStream({ pull() { pulls++; }, cancel() { canceled++; return new Promise(() => {}); } }, { highWaterMark: 0 }), init);
    const route = transportFixture(async (url, options) => {
      calls++; assert.equal(new URL(url).origin, 'https://api.waterdata.usgs.gov');
      assert.equal(options.redirect, 'manual'); assert.equal(options.cache, 'no-store');
      assert.match(options.headers.Accept, /application\/geo\+json/); return upstream;
    });
    const response = await route.GET(request()); assert.equal(response.status, status); assert.equal((await response.json()).code, code);
    assert.equal(response.headers.get('cache-control'), 'no-store'); assert.equal(calls, 1); assert.equal(pulls, 0); assert.equal(canceled, 1); assert.equal(upstream.body.locked, false);
    if (status === 429) assert.equal(response.headers.get('retry-after'), '600');
  }
});

test('streamflow stalled bodies honor request and aggregate deadlines without awaiting cancellation', { timeout: 1000 }, async t => {
  for (const aggregate of [false, true]) {
    let expire, cleared = 0, started, signal, canceled;
    const reading = new Promise(resolve => { started = resolve; });
    const budget = aggregate ? { deadline: Date.now() + 1000, remainingBytes: 100, exhausted: false } : undefined;
    let pulls = 0;
    const upstream = new Response(new ReadableStream({
      pull(controller) { if (pulls++ === 0) controller.enqueue(Uint8Array.of(123)); else started(); },
      cancel(reason) { canceled = reason; return new Promise(() => {}); },
    }, { highWaterMark: 0 }), { headers: { 'Content-Type': 'application/json' } });
    const route = transportFixture(async (_url, options) => { signal = options.signal; return upstream; }, {
      setTimeout(callback, delay) { assert.equal(aggregate ? delay <= 1000 && delay > 0 : delay === 25_000, true); expire = callback; return 1; },
      clearTimeout() { cleared++; },
    });
    const pending = route.fetchCollection(latestUrl(), budget); await reading;
    const clock = aggregate ? t.mock.method(Date, 'now', () => budget.deadline) : null;
    try {
      expire();
      await assert.rejects(pending, error => aggregate ? error instanceof route.NetworkBudgetExceeded : error instanceof route.UsgsUpstreamError && error.timeout);
      if (budget) assert.equal(budget.exhausted, true);
      assert.equal(signal.aborted, true); assert.equal(canceled.name, 'AbortError'); assert.equal(upstream.body.locked, false); assert.equal(cleared, 1);
    } finally { clock?.mock.restore(); }
  }
});

test('USGS collection schema and missing-body checks remain strict after bounded reading', async () => {
  for (const payload of [null, '{', '[]', '{}', JSON.stringify({ type: 'FeatureCollection', features: [], numberReturned: 1, links: [], timeStamp: time })]) {
    const upstream = new Response(payload, { headers: { 'Content-Type': 'application/json' } });
    const route = transportFixture(async () => upstream), response = await route.GET(request());
    assert.equal(response.status, 502); assert.equal((await response.json()).code, 'USGS_STREAMFLOW_UNAVAILABLE'); assert.equal(upstream.body?.locked ?? false, false);
  }
  const upstream = collection([], { links: [{ rel: 'next', href: 'https://untrusted.test/never-followed' }] });
  let calls = 0;
  const route = transportFixture(async () => { calls++; return upstream; });
  const result = await route.fetchCollection(latestUrl());
  assert.deepEqual(result.features, []); assert.equal(result.hasNextPage, true); assert.equal(calls, 1); assert.equal(upstream.body.locked, false);
});
