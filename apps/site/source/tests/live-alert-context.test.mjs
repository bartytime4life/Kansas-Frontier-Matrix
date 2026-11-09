import assert from "node:assert/strict";
import "./cloudflare-register.mjs";
import test, { after } from "node:test";

// Vinext captures fetch during import and patches it on the first request.
// Deny transport before either step so initialization cannot escape a fixture.
const blockedRequests = [];
const denyFetch = async input => { blockedRequests.push(String(input)); throw new Error("Unexpected transport outside an alert fixture."); };
globalThis.fetch = denyFetch;
const workerUrl = new URL("../dist/server/index.js", import.meta.url);
workerUrl.searchParams.set("test", `alert-context-${process.pid}`);
const { default: worker } = await import(workerUrl.href);
const context = { waitUntil() {}, passThroughOnException() {} };
const primed = await worker.fetch(new Request("http://localhost/api/live-context?feed=unsupported-test-fixture"), {}, context);
assert.equal(primed.status, 400);
await primed.arrayBuffer();
assert.deepEqual(blockedRequests, []);
globalThis.fetch = denyFetch;
after(() => assert.deepEqual(blockedRequests, [], "all provider access must belong to an explicit fixture"));
const polygon = { type: "Polygon", coordinates: [[[-98, 38], [-97, 38], [-97, 39], [-98, 38]]] };
const zoneUrl = "https://api.weather.gov/zones/county/KSC001";
const alert = (id = "alert-1", geometry = polygon, affectedZones = []) => ({
  type: "Feature", id, geometry, properties: { id, event: "Flood Warning", effective: "2026-11-09T12:00:00Z",
    expires: "2026-11-09T18:00:00Z", headline: "Synthetic alert fixture", affectedZones },
});
const request = (path = "/api/live-context?feed=nws-alerts") => worker.fetch(new Request(`http://localhost${path}`), {}, context);

async function withAlerts(payload, zoneResponse, run) {
  const originalFetch = globalThis.fetch, calls = [];
  globalThis.fetch = async (input, init) => {
    const url = new URL(input); calls.push(url.href);
    assert.equal(url.origin, "https://api.weather.gov");
    assert.equal(init.redirect, "manual");
    if (url.pathname === "/alerts/active") {
      assert.equal(url.search, "?area=KS", "pagination URLs are never followed");
      return Response.json({ type: "FeatureCollection", ...payload });
    }
    assert.match(url.pathname, /^\/zones\/(forecast|county|fire)\/(KSZ|KSC)\d{3}$/);
    return typeof zoneResponse === "function" ? zoneResponse(url) : Response.json(zoneResponse);
  };
  try {
    await run(calls);
    const zones = [...new Set(payload.features.flatMap(feature => feature.properties.affectedZones))].slice(0, 36);
    assert.deepEqual(calls, ["https://api.weather.gov/alerts/active?area=KS", ...zones], "every fixture request is accounted for");
  } finally { globalThis.fetch = originalFetch; }
}

test("NWS keeps confirmed empty, direct polygons and usable zone fallback complete", async () => {
  for (const pagination of [undefined, {}, { next: null }]) {
    await withAlerts({ features: [], ...(pagination === undefined ? {} : { pagination }) }, null, async () => {
      const response = await request(), body = await response.json();
      assert.equal(response.status, 200); assert.equal(body.state, "empty"); assert.equal(body.truncated, false);
      assert.equal(response.headers.get("x-kfm-context-state"), "empty");
    });
  }
  for (const geometry of [polygon, { type: "MultiPolygon", coordinates: [polygon.coordinates] }]) {
    await withAlerts({ features: [alert("direct", geometry)] }, null, async calls => {
      const body = await (await request()).json();
      assert.equal(body.state, "ready"); assert.equal(body.featureCount, 1); assert.equal(body.truncated, false);
      assert.deepEqual(body.data.features[0].geometry, geometry); assert.equal(calls.length, 1);
      assert.equal(body.data.features[0].properties.evidenceRole, "EXTERNAL_CONTEXT_ONLY");
    });
  }
  await withAlerts({ features: [alert("fallback", null, [zoneUrl])] }, { type: "Feature", geometry: polygon, properties: { name: "Fixture county" } }, async () => {
    const body = await (await request()).json();
    assert.equal(body.state, "ready"); assert.equal(body.featureCount, 1); assert.equal(body.truncated, false);
    assert.equal(body.data.features[0].properties.zoneName, "Fixture county");
  });
});

test("HTTP-success zone responses with unusable geometry are partial instead of empty coverage", async () => {
  for (const geometry of [null, {}, { type: "Polygon", coordinates: [] }, { type: "Polygon", coordinates: [[[-98, 38], [-97, 38], [-97, 39], [-98, 39]]] },
    { type: "MultiPolygon", coordinates: [[[]]] }, { type: "Polygon", coordinates: [[[-198, 38], [-97, 38], [-97, 39], [-198, 38]]] }]) {
    await withAlerts({ features: [alert("unmapped", null, [zoneUrl])] }, { type: "Feature", geometry, properties: {} }, async () => {
      const response = await request(), body = await response.json();
      assert.equal(response.status, 200); assert.equal(body.state, "partial");
      assert.equal(response.headers.get("x-kfm-context-state"), "partial");
      assert.equal(body.featureCount, 0); assert.equal(body.truncated, false);
      assert.match(body.limitation, /1 selected zone lookup failed or returned unusable geometry/);
      assert.match(body.limitation, /1 returned alert could not be mapped/);
    });
  }
});

test("unmappable alerts and invalid supplied polygons do not erase valid returned alerts", async () => {
  await withAlerts({ features: [alert("valid"), alert("missing", null), alert("broken", { type: "Polygon", coordinates: [] })] }, null, async () => {
    const body = await (await request()).json();
    assert.equal(body.state, "partial"); assert.equal(body.truncated, false); assert.equal(body.featureCount, 1);
    assert.equal(body.data.features[0].id, "valid-geometry");
    assert.match(body.limitation, /2 returned alerts could not be mapped/);
    assert.match(body.limitation, /1 supplied alert polygon withheld as unusable/);
  });
});

test("advertised or unverifiable alert pagination stays partial without following next URLs", async () => {
  const validNext = "https://api.weather.gov/alerts/active?area=KS&cursor=fixture";
  for (const features of [[], [alert()]]) {
    for (const pagination of [{ next: validNext }, null, [], "unrecognized", { next: "" }, { next: true },
      { next: "not a URL" }, { next: "https://untrusted.test/alerts/active" }, { next: "https://api.weather.gov/private" }]) {
      await withAlerts({ features, pagination }, null, async calls => {
        const response = await request(), body = await response.json();
        assert.equal(response.status, 200); assert.equal(body.state, "partial"); assert.equal(body.truncated, true);
        assert.equal(body.featureCount, features.length); assert.equal(calls.length, 1);
        assert.match(body.limitation, pagination?.next === validNext ? /Another alert page was advertised/ : /Pagination metadata could not be verified/);
      });
    }
  }
});

test("NWS zone lookup and mapped-feature caps stay bounded and disclosed", async () => {
  const zones = Array.from({ length: 37 }, (_, index) => `https://api.weather.gov/zones/county/KSC${String(index).padStart(3, "0")}`);
  await withAlerts({ features: [alert("zones", null, zones)] }, { type: "Feature", geometry: polygon, properties: {} }, async calls => {
    const body = await (await request()).json();
    assert.equal(calls.length, 37); assert.equal(body.state, "partial"); assert.equal(body.truncated, true);
    assert.equal(body.featureCount, 36); assert.match(body.limitation, /Zone lookups were bounded to 36/);
  });
  await withAlerts({ features: Array.from({ length: 161 }, (_, index) => alert(`alert-${index}`)) }, null, async calls => {
    const body = await (await request()).json();
    assert.equal(calls.length, 1); assert.equal(body.state, "partial"); assert.equal(body.truncated, true);
    assert.equal(body.featureCount, 160); assert.equal(body.data.features.length, 160);
    assert.match(body.limitation, /Mapped features were capped at 160/);
  });
});

test("zone network failures preserve direct polygons with explicit partial coverage", async () => {
  await withAlerts({ features: [alert("direct", polygon, [zoneUrl])] }, () => new Response("Unavailable", { status: 503 }), async () => {
    const body = await (await request()).json();
    assert.equal(body.state, "partial"); assert.equal(body.featureCount, 1); assert.equal(body.truncated, false);
    assert.match(body.limitation, /1 selected zone lookup failed or returned unusable geometry/);
  });
});

test("alert downloads preserve partial coverage and unusable-zone provenance", async () => {
  await withAlerts({ features: [alert("unmapped", null, [zoneUrl])] }, { geometry: null }, async () => {
    const response = await request("/api/source-download?source=nws-alerts"), body = await response.json();
    assert.equal(response.status, 200); assert.equal(response.headers.get("x-kfm-context-state"), "partial");
    assert.equal(body.kfm.state, "partial"); assert.equal(body.kfm.featureCount, 0); assert.equal(body.kfm.truncated, false);
    assert.deepEqual(body.features, []); assert.match(body.kfm.limitation, /1 returned alert could not be mapped/);
  });
});

test("an unavailable NWS alert list remains an error instead of empty coverage", async () => {
  const originalFetch = globalThis.fetch, calls = [];
  globalThis.fetch = async input => { calls.push(String(input)); return new Response("Unavailable", { status: 503 }); };
  try {
    const response = await request(), body = await response.json();
    assert.equal(response.status, 502); assert.equal(body.state, "error"); assert.equal("data" in body, false);
    assert.equal(response.headers.get("cache-control"), "no-store");
    assert.deepEqual(calls, ["https://api.weather.gov/alerts/active?area=KS"]);
  } finally { globalThis.fetch = originalFetch; }
});
