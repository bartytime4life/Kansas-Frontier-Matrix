import assert from "node:assert/strict";
import "./cloudflare-register.mjs";
import test from "node:test";

const workerUrl = new URL("../dist/server/index.js", import.meta.url);
workerUrl.searchParams.set("test", `earthquake-bounds-${process.pid}`);
const { default: worker } = await import(workerUrl.href);
const context = { waitUntil() {}, passThroughOnException() {} };
const day = "2020-01-01";
const event = (index, overrides = {}) => ({
  type: "Feature", id: `event-${index}`,
  geometry: { type: "Point", coordinates: [-97, 38, 2] },
  properties: { time: Date.parse(`${day}T12:00:00.000Z`) + index, mag: 1, updated: Date.parse(`${day}T13:00:00.000Z`) },
  ...overrides,
});
const request = (path = `/api/live-context?feed=usgs-earthquakes&day=${day}`) =>
  worker.fetch(new Request(`http://localhost${path}`), {}, context);

async function withCatalog(features, run) {
  const originalFetch = globalThis.fetch;
  const queries = [];
  globalThis.fetch = async (input, init) => {
    const url = new URL(input);
    assert.equal(url.origin, "https://earthquake.usgs.gov");
    assert.equal(url.pathname, "/fdsnws/event/1/query");
    assert.equal(url.searchParams.get("limit"), "251");
    assert.equal(init.redirect, "manual");
    queries.push(url);
    return Response.json({ type: "FeatureCollection", features, metadata: { count: features.length } });
  };
  try { await run(queries); } finally { globalThis.fetch = originalFetch; }
}

test("earthquake lookahead distinguishes exactly 250 events from an incomplete bounded view", async () => {
  for (const count of [0, 249, 250, 251]) {
    await withCatalog(Array.from({ length: count }, (_, index) => event(index)), async () => {
      const response = await request();
      assert.equal(response.status, 200);
      const body = await response.json();
      const state = count === 251 ? "partial" : count ? "ready" : "empty";
      assert.equal(body.state, state);
      assert.equal(response.headers.get("x-kfm-context-state"), state);
      assert.equal(body.featureCount, Math.min(count, 250));
      assert.equal(body.data.features.length, Math.min(count, 250));
      assert.equal(body.truncated, count === 251);
      if (count === 251) {
        assert.match(body.limitation, /at most 250 returned records.*additional catalog records were omitted/);
        assert.equal(body.data.features.some(feature => feature.id === "event-250"), false);
      }
    });
  }
});

test("invalid and outside-window earthquake records make the response partial without claiming truncation", async () => {
  const features = [event(0), event(1, { geometry: null }), event(2, {
    properties: { time: Date.parse("2020-01-02T00:00:00.000Z"), mag: 1 },
  }), event(3, { properties: { time: 1e100, mag: 1 } })];
  await withCatalog(features, async () => {
    const response = await request();
    assert.equal(response.status, 200);
    const body = await response.json();
    assert.equal(body.state, "partial");
    assert.equal(response.headers.get("x-kfm-context-state"), "partial");
    assert.equal(body.truncated, false);
    assert.equal(body.featureCount, 1);
    assert.deepEqual(body.data.features.map(feature => feature.id), ["event-0"]);
    assert.match(body.limitation, /3 invalid or outside-window returned records withheld/);
    assert.match(body.limitation, /end excluded/);
  });
});

test("all-withheld earthquake responses remain partial and an invalid update time stays unreported", async () => {
  await withCatalog([event(0, { properties: { time: 1e100 } })], async () => {
    const response = await request();
    const body = await response.json();
    assert.equal(body.state, "partial");
    assert.equal(body.featureCount, 0);
    assert.equal(body.truncated, false);
  });
  await withCatalog([event(0, { properties: { time: Date.parse(`${day}T12:00:00.000Z`), updated: 1e100 } })], async () => {
    const response = await request();
    assert.equal(response.status, 200);
    const body = await response.json();
    assert.equal(body.state, "ready");
    assert.equal(body.featureCount, 1);
    assert.equal(body.data.features[0].properties.updatedAt, null);
  });
});

test("downloaded earthquake context retains partial state, record count and truncation provenance", async () => {
  await withCatalog(Array.from({ length: 251 }, (_, index) => event(index)), async () => {
    const response = await request(`/api/source-download?source=usgs-earthquakes&day=${day}`);
    assert.equal(response.status, 200);
    assert.equal(response.headers.get("x-kfm-context-state"), "partial");
    const body = await response.json();
    assert.equal(body.type, "FeatureCollection");
    assert.equal(body.features.length, 250);
    assert.equal(body.kfm.requestedDay, day);
    assert.equal(body.kfm.state, "partial");
    assert.equal(body.kfm.featureCount, body.features.length);
    assert.equal(body.kfm.truncated, true);
    assert.match(body.kfm.limitation, /additional catalog records were omitted/);
  });
});

test("unavailable earthquake upstreams return an error instead of an empty catalog", async () => {
  const originalFetch = globalThis.fetch;
  globalThis.fetch = async () => new Response("Unavailable", { status: 503 });
  try {
    const response = await request();
    assert.equal(response.status, 502);
    assert.equal(response.headers.get("x-kfm-context-state"), "error");
    assert.equal(response.headers.get("cache-control"), "no-store");
    const body = await response.json();
    assert.equal(body.state, "error");
    assert.equal("data" in body, false);
    assert.match(body.fallback, /No fallback inference/);
  } finally { globalThis.fetch = originalFetch; }
});
