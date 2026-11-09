import assert from "node:assert/strict";
import "./cloudflare-register.mjs";
import test from "node:test";

const workerUrl = new URL("../dist/server/index.js", import.meta.url);
workerUrl.searchParams.set("test", `fire-context-${process.pid}`);
const { default: worker } = await import(workerUrl.href);
const context = { waitUntil() {}, passThroughOnException() {} };
const now = Date.now();
const discovery = now - 3_600_000;
const modified = now - 1_000;
const incident = (index, properties = {}) => ({
  type: "Feature", id: index,
  geometry: { type: "Point", coordinates: [-97, 38] },
  properties: { UniqueFireIdentifier: `fire-${index}`, IncidentName: `Incident ${index}`, IncidentTypeCategory: "WF", POOState: "US-KS",
    FireDiscoveryDateTime: discovery, ModifiedOnDateTime_dt: modified, FireOutDateTime: null, IncidentSize: 25, PercentContained: 10, ...properties },
});
const request = (path = "/api/live-context?feed=nifc-fire-reports") =>
  worker.fetch(new Request(`http://localhost${path}`), {}, context);

async function withCatalog(payload, run) {
  const originalFetch = globalThis.fetch;
  globalThis.fetch = async (input, init) => {
    const url = new URL(input);
    assert.equal(url.origin, "https://services3.arcgis.com");
    assert.match(url.pathname, /WFIGS_Incident_Locations_YearToDate\/FeatureServer\/0\/query$/);
    assert.equal(url.searchParams.get("resultRecordCount"), "251");
    assert.equal(url.searchParams.get("f"), "geojson");
    assert.match(url.searchParams.get("where"), /POOState='US-KS'/);
    assert.equal(init.redirect, "manual");
    return Response.json({ type: "FeatureCollection", ...payload });
  };
  try { await run(); } finally { globalThis.fetch = originalFetch; }
}

test("NIFC keeps the 250-incident display bound and distinguishes empty, complete and capped responses", async () => {
  for (const count of [0, 250, 251]) {
    await withCatalog({ features: Array.from({ length: count }, (_, index) => incident(index)) }, async () => {
      const response = await request();
      assert.equal(response.status, 200);
      const body = await response.json();
      const state = count > 250 ? "partial" : count ? "ready" : "empty";
      assert.equal(body.state, state);
      assert.equal(response.headers.get("x-kfm-context-state"), state);
      assert.equal(body.featureCount, Math.min(count, 250));
      assert.equal(body.data.features.length, body.featureCount);
      assert.equal(body.truncated, count > 250);
      if (count > 250) assert.match(body.limitation, /capped at 250/);
    });
  }
});

test("provider transfer limits remain partial even below the display cap or with zero incidents", async () => {
  for (const featureCount of [0, 1]) {
    for (const metadata of [{ exceededTransferLimit: true }, { properties: { exceededTransferLimit: true } }]) {
      await withCatalog({ features: Array.from({ length: featureCount }, (_, index) => incident(index)), ...metadata }, async () => {
        const response = await request();
        assert.equal(response.status, 200);
        const body = await response.json();
        assert.equal(body.state, "partial");
        assert.equal(response.headers.get("x-kfm-context-state"), "partial");
        assert.equal(body.featureCount, featureCount);
        assert.equal(body.truncated, true);
        assert.match(body.limitation, /provider reported a transfer limit/);
        assert.doesNotMatch(body.limitation, /capped at 250/);
      });
    }
  }
  await withCatalog({ features: [incident(0)], properties: { exceededTransferLimit: false } }, async () => {
    const body = await (await request()).json();
    assert.equal(body.state, "ready");
    assert.equal(body.truncated, false);
  });
});

test("malformed NIFC transfer-limit metadata fails without claiming empty coverage", async () => {
  for (const flag of ["true", 0, null]) {
    for (const metadata of [{ exceededTransferLimit: flag }, { properties: { exceededTransferLimit: flag } }]) {
      await withCatalog({ features: [], ...metadata }, async () => {
        const response = await request();
        assert.equal(response.status, 502);
        assert.equal(response.headers.get("x-kfm-context-state"), "error");
        assert.equal(response.headers.get("cache-control"), "no-store");
        const body = await response.json();
        assert.equal(body.state, "error");
        assert.equal("data" in body, false);
        assert.match(body.error, /invalid transfer-limit metadata/);
      });
    }
  }
});

test("NIFC does not relabel foreign-state or unreported-state incidents as Kansas", async () => {
  await withCatalog({ features: [incident(0), incident(1, { POOState: "US-OK" }), incident(2, { POOState: null })] }, async () => {
    const response = await request();
    const body = await response.json();
    assert.equal(body.state, "partial");
    assert.equal(body.truncated, false);
    assert.equal(body.featureCount, 1);
    assert.deepEqual(body.data.features.map(feature => feature.properties.uniqueFireIdentifier), ["fire-0"]);
    assert.equal(body.data.features[0].properties.state, "Kansas");
    assert.match(body.limitation, /2 records withheld because required fields, Kansas scope or discovery times did not match/);
  });
  await withCatalog({ features: [incident(0, { POOState: "US-OK" })] }, async () => {
    const body = await (await request()).json();
    assert.equal(body.state, "partial");
    assert.equal(body.featureCount, 0);
    assert.equal(body.truncated, false);
  });
});

test("invalid optional incident dates stay unreported while valid incidents and source times survive", async () => {
  await withCatalog({ features: [incident(0, { ModifiedOnDateTime_dt: 1e100, FireOutDateTime: -1e100 }),
    incident(1, { ModifiedOnDateTime_dt: "not a timestamp", FireOutDateTime: "not a timestamp" }), incident(2)] }, async () => {
    const response = await request();
    assert.equal(response.status, 200);
    const body = await response.json();
    assert.equal(body.state, "partial");
    assert.equal(body.featureCount, 3);
    assert.equal(body.truncated, false);
    assert.equal(body.upstreamUpdatedAt, new Date(modified).toISOString());
    for (const feature of body.data.features.slice(0, 2)) {
      assert.equal(feature.properties.modifiedAt, null);
      assert.equal(feature.properties.reportedOutAt, null);
      assert.equal(feature.properties.reportState, "No out date in record; current activity unverified");
      assert.equal(feature.properties.discoveryAt, new Date(discovery).toISOString());
    }
    assert.equal(body.data.features[2].properties.modifiedAt, new Date(modified).toISOString());
    assert.match(body.limitation, /4 invalid optional date values withheld/);
  });
});

test("invalid required discovery times are withheld without losing a valid incident", async () => {
  await withCatalog({ features: [incident(0), incident(1, { FireDiscoveryDateTime: 1e100 }), incident(2, { FireDiscoveryDateTime: -1e100 })] }, async () => {
    const response = await request();
    assert.equal(response.status, 200);
    const body = await response.json();
    assert.equal(body.state, "partial");
    assert.equal(body.featureCount, 1);
    assert.equal(body.truncated, false);
    assert.equal(body.data.features[0].properties.uniqueFireIdentifier, "fire-0");
  });
});

test("NIFC downloads retain provider-limit provenance and exact returned counts", async () => {
  await withCatalog({ features: [incident(0)], properties: { exceededTransferLimit: true } }, async () => {
    const response = await request("/api/source-download?source=nifc-fire-reports");
    assert.equal(response.status, 200);
    assert.equal(response.headers.get("x-kfm-context-state"), "partial");
    const body = await response.json();
    assert.equal(body.type, "FeatureCollection");
    assert.equal(body.features.length, 1);
    assert.equal(body.kfm.featureCount, body.features.length);
    assert.equal(body.kfm.state, "partial");
    assert.equal(body.kfm.truncated, true);
    assert.match(body.kfm.limitation, /provider reported a transfer limit/);
  });
});

test("unavailable NIFC upstreams remain errors instead of empty incident lists", async () => {
  const originalFetch = globalThis.fetch;
  globalThis.fetch = async () => new Response("Unavailable", { status: 503 });
  try {
    const response = await request();
    assert.equal(response.status, 502);
    assert.equal(response.headers.get("x-kfm-context-state"), "error");
    const body = await response.json();
    assert.equal(body.state, "error");
    assert.equal("data" in body, false);
    assert.match(body.fallback, /No fallback inference/);
  } finally { globalThis.fetch = originalFetch; }
});
