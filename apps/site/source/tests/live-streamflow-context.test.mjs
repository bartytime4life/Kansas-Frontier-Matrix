import assert from "node:assert/strict";
import "./cloudflare-register.mjs";
import test, { after } from "node:test";

// Initialize the Worker while transport is denied: its first-request fetch
// patch must be installed before any observation fixture replaces fetch.
const blockedRequests = [];
const denyFetch = async input => { blockedRequests.push(String(input)); throw new Error("Unexpected transport outside a river fixture."); };
globalThis.fetch = denyFetch;
const workerUrl = new URL("../dist/server/index.js", import.meta.url);
workerUrl.searchParams.set("test", `latest-river-context-${process.pid}`);
const { default: worker } = await import(workerUrl.href);
const context = { waitUntil() {}, passThroughOnException() {} };
const primed = await worker.fetch(new Request("http://localhost/api/live-context?feed=unsupported-test-fixture"), {}, context);
assert.equal(primed.status, 400);
await primed.arrayBuffer();
assert.deepEqual(blockedRequests, []);
globalThis.fetch = denyFetch;
after(() => assert.deepEqual(blockedRequests, [], "all provider access must belong to an explicit fixture"));
const station = "USGS-06892518";
const iso = milliseconds => new Date(milliseconds).toISOString();
const observation = (time, value = 10, id = station) => ({
  type: "Feature", id, geometry: { type: "Point", coordinates: [-98, 38] },
  properties: { monitoring_location_id: id, time, value, unit_of_measure: "ft3/s", parameter_code: "00060", statistic_id: null,
    approval_status: "Provisional", qualifier: "fixture qualifier", last_modified: "2026-11-09T00:00:00Z" },
});
const request = () => worker.fetch(new Request("http://localhost/api/live-context?feed=usgs-streamflow"), {}, context);

async function withObservations(makePayload, run) {
  const originalFetch = globalThis.fetch;
  let window, requestCount = 0;
  globalThis.fetch = async (input, init) => {
    const url = new URL(input);
    assert.equal(url.origin, "https://api.waterdata.usgs.gov");
    assert.equal(url.pathname, "/ogcapi/v1/collections/latest-continuous/items");
    assert.equal(url.searchParams.get("limit"), "1000"); assert.equal(url.searchParams.get("parameter_code"), "00060");
    assert.equal(init.redirect, "manual");
    const [start, end] = url.searchParams.get("datetime").split("/");
    assert.notEqual(end, ".."); assert.equal(Date.parse(end) - Date.parse(start), 86_400_000);
    window = { start, end, startMs: Date.parse(start), endMs: Date.parse(end), requestCount: ++requestCount };
    return Response.json({ type: "FeatureCollection", links: [], ...makePayload(window) });
  };
  try {
    await run(() => window);
    assert.equal(requestCount, 1, "exactly one bounded observation request belongs to this fixture");
  } finally { globalThis.fetch = originalFetch; }
}

test("latest river context chooses actual instants across offsets and preserves station provenance", async () => {
  await withObservations(({ endMs }) => ({ features: [
    observation(iso(endMs - 2 * 3_600_000), 10),
    observation(iso(endMs - 7 * 3_600_000).replace("Z", "-06:00"), 20),
    observation(iso(endMs - 12 * 3_600_000), 5),
  ] }), async getWindow => {
    const response = await request(), body = await response.json();
    assert.equal(response.status, 200); assert.equal(body.state, "ready"); assert.equal(body.truncated, false);
    assert.equal(body.featureCount, 1); assert.equal(body.upstreamUpdatedAt, iso(getWindow().endMs - 3_600_000));
    const feature = body.data.features[0];
    assert.equal(feature.id, station); assert.deepEqual(feature.geometry.coordinates, [-98, 38]);
    assert.equal(feature.properties.observedAt, body.upstreamUpdatedAt); assert.equal(feature.properties.value, 20);
    assert.equal(feature.properties.unit, "ft3/s"); assert.equal(feature.properties.parameterCode, "00060");
    assert.equal(feature.properties.approvalStatus, "Provisional"); assert.equal(feature.properties.qualifier, "fixture qualifier");
    assert.equal(feature.properties.lastModified, "2026-11-09T00:00:00Z");
    assert.equal(feature.properties.evidenceRole, "EXTERNAL_CONTEXT_ONLY");
  });
});

test("positive offsets, explicit lower-case UTC and fractional source clocks normalize to UTC", async () => {
  await withObservations(({ endMs }) => ({ features: [
    observation(iso(endMs - 3_600_000 + 150 * 60_000).replace("Z", "+02:30"), 1, "USGS-00000001"),
    observation(iso(endMs - 2 * 3_600_000).toLowerCase(), 2, "USGS-00000002"),
    observation(iso(endMs - 3 * 3_600_000).replace(/\.\d{3}Z$/, ".123456789Z"), 3, "USGS-00000003"),
  ] }), async getWindow => {
    const body = await (await request()).json();
    assert.equal(body.state, "ready"); assert.equal(body.featureCount, 3);
    assert.deepEqual(body.data.features.map(feature => feature.properties.observedAt), [
      iso(getWindow().endMs - 3_600_000), iso(getWindow().endMs - 2 * 3_600_000),
      iso(getWindow().endMs - 3 * 3_600_000).replace(/\.\d{3}Z$/, ".123456789Z"),
    ]);
    assert.equal(body.data.features[2].properties.sourceObservedAt, body.data.features[2].properties.observedAt);
  });
});

test("river latest selection preserves submillisecond ordering and the original fractional source clock", async () => {
  for (const reverse of [false, true]) {
    let earlier, later;
    await withObservations(({ endMs }) => {
      const second = iso(endMs - 3_600_000).replace(/\.\d{3}Z$/, "");
      earlier = `${second}.123100Z`; later = `${second}.123900Z`;
      const features = [observation(earlier, 1), observation(later, 9)];
      return { features: reverse ? features.reverse() : features };
    }, async () => {
      const body = await (await request()).json();
      assert.equal(body.state, "ready"); assert.equal(body.featureCount, 1);
      assert.equal(body.data.features[0].properties.value, 9);
      assert.equal(body.data.features[0].properties.observedAt, later);
      assert.equal(body.data.features[0].properties.sourceObservedAt, later);
      assert.equal(body.upstreamUpdatedAt, later);
    });
  }
});

test("offset source clocks in the same millisecond are ordered after exact UTC normalization", async () => {
  let expected, sourceClock;
  await withObservations(({ endMs }) => {
    const utcSecond = iso(endMs - 3_600_000).replace(/\.\d{3}Z$/, "");
    const localSecond = iso(endMs - 7 * 3_600_000).replace(/\.\d{3}Z$/, "");
    sourceClock = `${localSecond}.123850-06:00`; expected = `${utcSecond}.123850Z`;
    return { features: [observation(`${utcSecond}.123800Z`, 8), observation(sourceClock, 9)] };
  }, async () => {
    const body = await (await request()).json();
    assert.equal(body.state, "ready"); assert.equal(body.data.features[0].properties.value, 9);
    assert.equal(body.data.features[0].properties.observedAt, expected);
    assert.equal(body.data.features[0].properties.sourceObservedAt, sourceClock);
    assert.equal(body.upstreamUpdatedAt, expected);
  });
});

test("a sample finer than a millisecond after the upper bound is withheld without rounding into the window", async () => {
  await withObservations(({ end }) => ({ features: [observation(end, 1, "USGS-00000001"),
    observation(end.replace("Z", "000001Z"), 2, "USGS-00000002")] }), async getWindow => {
    const response = await request(), body = await response.json();
    assert.equal(body.state, "partial"); assert.equal(body.featureCount, 1); assert.equal(body.truncated, false);
    assert.equal(body.data.features[0].id, "USGS-00000001");
    assert.equal(body.data.features[0].properties.observedAt, getWindow().end);
    assert.equal(body.upstreamUpdatedAt, getWindow().end);
    assert.match(body.limitation, /1 invalid or outside-window returned observation withheld/);
  });
});

test("river context keeps exact inclusive 24-hour boundaries and withholds old or future observations", async () => {
  await withObservations(({ startMs, endMs }) => ({ features: [observation(iso(startMs), 1, "USGS-00000001"),
    observation(iso(endMs), 2, "USGS-00000002"), observation(iso(startMs - 1), 3, "USGS-00000003"),
    observation(iso(endMs + 1), 4, "USGS-00000004")] }), async getWindow => {
    const response = await request(), body = await response.json();
    assert.equal(body.state, "partial"); assert.equal(response.headers.get("x-kfm-context-state"), "partial");
    assert.equal(body.truncated, false); assert.equal(body.featureCount, 2);
    assert.deepEqual(body.data.features.map(feature => feature.properties.observedAt), [getWindow().start, getWindow().end]);
    assert.equal(body.upstreamUpdatedAt, getWindow().end);
    assert.match(body.limitation, /2 invalid or outside-window returned observations withheld/);
  });
});

test("invalid clocks and calendar rollovers remain partial without hiding a valid river reading", async () => {
  const invalidTimes = ["not-a-time", "2026-02-30T12:00:00Z", "2026-11-09", "2026-11-09T12:00:00",
    "2026-11-09T24:00:00Z", "2026-11-09T12:00:00+24:00", "2026-11-09T12:00:00+00:60", "", null];
  await withObservations(({ endMs }) => ({ features: [observation(iso(endMs - 1_000), 9), ...invalidTimes.map(time => observation(time, 30))] }), async () => {
    const response = await request(), body = await response.json();
    assert.equal(response.status, 200); assert.equal(body.state, "partial"); assert.equal(body.featureCount, 1);
    assert.equal(body.truncated, false); assert.equal(body.data.features[0].properties.value, 9);
    assert.match(body.limitation, /9 invalid or outside-window returned observations withheld/);
  });
});

test("all-withheld river clocks cannot become a confirmed empty response or a zero reading", async () => {
  await withObservations(() => ({ features: [observation("not-a-time"), observation("2099-01-01T00:00:00Z")] }), async () => {
    const body = await (await request()).json();
    assert.equal(body.state, "partial"); assert.equal(body.featureCount, 0); assert.equal(body.upstreamUpdatedAt, null);
    assert.equal(body.truncated, false); assert.deepEqual(body.data.features, []);
  });
  await withObservations(({ endMs }) => ({ features: [observation(iso(endMs - 1_000), null)] }), async () => {
    const body = await (await request()).json();
    assert.equal(body.state, "ready"); assert.equal(body.data.features[0].properties.value, null);
    assert.equal(body.data.features[0].properties.displayValue, "not reported");
  });
});

test("a verified empty river response remains empty and provider pagination remains partial", async () => {
  for (const nextPage of [false, true]) {
    await withObservations(() => ({ features: [], links: nextPage ? [{ rel: "next", href: "https://untrusted.test/not-followed" }] : [] }), async () => {
      const body = await (await request()).json();
      assert.equal(body.state, nextPage ? "partial" : "empty"); assert.equal(body.featureCount, 0);
      assert.equal(body.upstreamUpdatedAt, null); assert.equal(body.truncated, nextPage);
    });
  }
});

test("latest river processing considers at most the first 1000 returned records and never follows another page", async () => {
  for (const count of [1000, 1001]) {
    for (const pagination of [false, true]) {
      await withObservations(({ endMs }) => ({
        features: Array.from({ length: count }, (_, index) => observation(iso(endMs - 1_000), index, `USGS-${String(index).padStart(8, "0")}`)),
        links: pagination ? [{ rel: "next", href: "https://api.waterdata.usgs.gov/ogcapi/v1/collections/latest-continuous/items?cursor=next" }] : [],
      }), async getWindow => {
        const response = await request(), body = await response.json();
        const partial = count > 1000 || pagination;
        assert.equal(response.status, 200); assert.equal(body.state, partial ? "partial" : "ready");
        assert.equal(body.truncated, partial); assert.equal(body.featureCount, 1000); assert.equal(body.data.features.length, 1000);
        assert.equal(getWindow().requestCount, 1);
        assert.equal(body.data.features.some(feature => feature.id === "USGS-00001000"), false);
        if (count > 1000) assert.match(body.limitation, /only the first 1000 were considered/);
        else assert.doesNotMatch(body.limitation, /only the first 1000 were considered/);
        if (pagination) assert.match(body.limitation, /advertised another page/);
        else assert.doesNotMatch(body.limitation, /advertised another page/);
      });
    }
  }
});

test("an invalid first 1000 records do not make processing scan later records or claim empty coverage", async () => {
  await withObservations(({ endMs }) => ({ features: [...Array(1000).fill(null), observation(iso(endMs - 1_000), 5)] }), async getWindow => {
    const response = await request(), body = await response.json();
    assert.equal(response.status, 200); assert.equal(body.state, "partial"); assert.equal(body.truncated, true);
    assert.equal(body.featureCount, 0); assert.deepEqual(body.data.features, []); assert.equal(body.upstreamUpdatedAt, null);
    assert.equal(getWindow().requestCount, 1);
    assert.match(body.limitation, /only the first 1000 were considered/);
    assert.match(body.limitation, /1000 invalid or outside-window returned observations withheld/);
  });
});

test("an unavailable USGS latest-observation source remains an error", async () => {
  const originalFetch = globalThis.fetch, calls = [];
  globalThis.fetch = async input => { calls.push(new URL(input)); return new Response("Unavailable", { status: 503 }); };
  try {
    const response = await request(), body = await response.json();
    assert.equal(response.status, 502); assert.equal(body.state, "error"); assert.equal("data" in body, false);
    assert.equal(response.headers.get("cache-control"), "no-store");
    assert.equal(calls.length, 1);
    assert.equal(calls[0].origin, "https://api.waterdata.usgs.gov");
    assert.equal(calls[0].pathname, "/ogcapi/v1/collections/latest-continuous/items");
  } finally { globalThis.fetch = originalFetch; }
});
