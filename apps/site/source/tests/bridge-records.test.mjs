import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import ts from "typescript";
const modules = new Map();
async function load(file) {
  file = path.resolve(file); if (modules.has(file)) return modules.get(file);
  let js = ts.transpileModule(await readFile(file, "utf8"), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
  for (const match of [...js.matchAll(/from ["'](\.[^"']+)["']/g)]) js = js.replace(match[0], `from ${JSON.stringify(await load(path.resolve(path.dirname(file), match[1]) + ".ts"))}`);
  const url = `data:text/javascript;base64,${Buffer.from(js).toString("base64")}`; modules.set(file, url); return url;
}
const bridge = await import(await load("app/kansas-bridge-records.ts"));
const route = await import(await load("app/api/bridge-records/route.ts"));
const { KANSAS_REFERENCE_SOURCES } = await import(await load("app/kansas-reference-layers.ts"));
const query = { layer: "kdot-bridges-local", longitude: -98, latitude: 38, radius: 500 };
const feature = (attributes = {}, geometry = { x: -98, y: 38 }) => ({ attributes: { OBJECTID: 1, BRKEY: "SYNTHETIC-1", FIPS_STATE: "KANSAS", YEARBUILT: 1930, YEARRECON: 1998, OPPOSTCL: "Closed to all traffic", HISTSIGN: "Br eligible for NRHP", INSPDATE: Date.UTC(2024, 4, 1), LASTINSP: Date.UTC(2022, 4, 1), ...attributes }, geometry });
const body = (features = [feature()], extra = {}) => ({ geometryType: "esriGeometryPoint", spatialReference: { wkid: 4326 }, features, ...extra });
const request = params => new Request(`http://localhost/api/bridge-records?${new URLSearchParams(params)}`);

test("bridge inspector uses the exact displayed filters and separate provider schemas", () => {
  for (const layer of Object.keys(bridge.BRIDGE_FILTERS)) {
    const url = new URL(bridge.bridgeProviderUrl({ ...query, layer }));
    const map = new URL(KANSAS_REFERENCE_SOURCES.find(s => s.id === layer).mapUrl);
    assert.equal(url.searchParams.get("where"), JSON.parse(map.searchParams.get("layerDefs"))[0]);
    assert.equal(url.hostname, "kanplan.ksdot.gov");
    assert.equal(url.searchParams.get("outSR"), "4326");
    assert.equal(url.searchParams.get("resultRecordCount"), "50");
    assert.equal(url.searchParams.get("distance"), "500");
    assert.equal(url.searchParams.get("orderByFields"), "OBJECTID");
    assert.equal(url.searchParams.get("resultOffset"), "0");
    assert.equal(url.searchParams.get("outFields").includes("BUILT_DATE"), layer === "kdot-bridges-state");
    assert.equal(url.searchParams.get("outFields").includes("YEARBUILT"), layer !== "kdot-bridges-state");
  }
  const count = new URL(bridge.bridgeProviderCountUrl(query));
  assert.equal(count.searchParams.get("returnCountOnly"), "true");
  assert.equal(count.searchParams.get("where"), bridge.BRIDGE_FILTERS[query.layer].where);
  assert.equal(count.searchParams.get("resultOffset"), null);
  assert.equal(new URL(bridge.bridgeProviderUrl(query, 50)).searchParams.get("resultOffset"), "50");
  for (const offset of [-1, 1, 250, Number.NaN]) assert.throws(() => bridge.bridgeProviderUrl(query, offset));
});
test("query bounds reject arbitrary URLs, SQL, unknown filters and non-Kansas searches before I/O", async () => {
  assert.deepEqual(bridge.parseBridgeSearch(request(query).url), query);
  for (const change of [{ longitude: -95, latitude: 36 }, { radius: 1001 }, { radius: "Infinity" }, { layer: "__proto__" }, { where: "1=1" }, { url: "http://127.0.0.1/" }, { latitude: "NaN" }]) {
    assert.throws(() => bridge.parseBridgeSearch(request({ ...query, ...change }).url));
    assert.equal((await route.GET(request({ ...query, ...change }))).status, 400);
  }
  assert.throws(() => bridge.parseBridgeSearch(request(query).url + "&radius=1000"));
});
test("construction, designation, status and inspection dates remain independent", () => {
  const result = bridge.parseBridgeRecords(body(), query), r = result.records[0];
  assert.equal(r.builtYear, 1930); assert.equal(r.reconstructedYear, 1998);
  assert.equal(r.recordedStatus, "Closed to all traffic"); assert.equal(r.inspectionDate, "2024-05-01"); assert.equal(r.previousInspectionDate, "2022-05-01");
  assert.equal(r.historicDesignation, "Br eligible for NRHP");
  assert.match(r.sourceUrl, /objectIds=1&/); assert.equal(result.role, "EXTERNAL_CONTEXT_ONLY");
  const state = bridge.parseBridgeRecords(body([feature({ STR_NAME: "STATE-SYNTHETIC", BUILT_DATE: 1957, MODIFIED_DATE: "unknown", OPPOSTCL: "Open" })]), { ...query, layer: "kdot-bridges-state" }).records[0];
  assert.equal(state.builtYear, 1957); assert.equal(state.inspectionDate, null); assert.equal(state.historicDesignation, null); assert.equal(state.recordedStatus, "Open");
  const unknown = bridge.parseBridgeRecords(body([feature({ YEARBUILT: -1, YEARRECON: 0, INSPDATE: "2024", LASTINSP: Date.UTC(2099, 0, 1) })]), query).records[0];
  assert.equal(unknown.builtYear, null); assert.equal(unknown.reconstructedYear, null); assert.equal(unknown.inspectionDate, null); assert.equal(unknown.previousInspectionDate, null);
});
test("empty, capped, malformed, duplicate, ignored filters and out-of-scope geometries fail honestly", () => {
  assert.equal(bridge.parseBridgeRecords(body([]), query).state, "empty");
  assert.equal(bridge.parseBridgeRecords(body([], { exceededTransferLimit: true }), query).state, "partial");
  assert.equal(bridge.parseBridgeRecords(body(Array.from({ length: 50 }, (_, OBJECTID) => feature({ OBJECTID }))), query).partial, true);
  for (const bad of [{ error: { code: 400 } }, {}, body([feature()], { geometryType: "esriGeometryPolyline" }), body([feature()], { spatialReference: { wkid: 3857 } }), body([feature()], { exceededTransferLimit: "false" }), body([feature(), feature()]), body(Array(51).fill(feature()))]) assert.throws(() => bridge.parseBridgeRecords(bad, query));
  for (const [record, layer] of [[feature({ FIPS_STATE: "OKLAHOMA" }), query.layer], [feature({}, { x: -98, y: 36 }), query.layer], [feature({}, { x: -98, y: 38.1 }), query.layer], [feature({ YEARBUILT: null }), "kdot-bridges-old"], [feature({ OPPOSTCL: "Posted for load" }), "kdot-bridges-closed"], [feature({ HISTSIGN: "Possibly eligible for" }), "kdot-bridges-historic"], [null, query.layer]]) {
    const result = bridge.parseBridgeRecords(body([record]), { ...query, layer });
    assert.equal(result.state, "partial"); assert.equal(result.records.length, 0); assert.equal(result.omittedRecords, 1);
  }
});
test("ordered pages disclose provider count, cap and data-quality holds", () => {
  const batch = (start, length) => body(Array.from({ length }, (_, i) => feature({ OBJECTID: start + i })));
  assert.equal(bridge.parseBridgeCount({ count: 0 }), 0);
  for (const invalid of [{ count: -1 }, { count: 1.5 }, { count: "2" }, { error: { code: 400 } }]) assert.throws(() => bridge.parseBridgeCount(invalid));
  assert.equal(bridge.assembleBridgePages([], query, 0).state, "empty");
  const complete = bridge.assembleBridgePages([batch(1, 50), batch(51, 25)], query, 75);
  assert.equal(complete.state, "ready"); assert.equal(complete.partial, false);
  assert.equal(complete.providerCount, 75); assert.equal(complete.pagesRead, 2);
  assert.equal(complete.records.length, 75); assert.equal(complete.records[74].objectId, 75);
  const capped = bridge.assembleBridgePages(Array.from({ length: 5 }, (_, i) => batch(i * 50 + 1, 50)), query, 251);
  assert.equal(capped.state, "partial"); assert.equal(capped.records.length, 250);
  assert.equal(bridge.assembleBridgePages([batch(1, 10)], query, 15).partial, true);
  assert.equal(bridge.assembleBridgePages([body([feature({ OBJECTID: 1, FIPS_STATE: "OKLAHOMA" })])], query, 1).omittedRecords, 1);
  for (const pages of [[batch(1, 50), batch(50, 1)], [body([feature({ OBJECTID: 2 }), feature({ OBJECTID: 1 })])], [body([], { exceededTransferLimit: true })]]) assert.throws(() => bridge.assembleBridgePages(pages, query, 51));
  assert.throws(() => bridge.assembleBridgePages([batch(1, 2)], query, 1));
});
test("API rejects provider HTTP-200 errors, redirects, byte overflow and cancellation", async () => {
  const original = globalThis.fetch;
  try {
    for (const response of [Response.json({ error: { code: 400, message: "secret provider detail" } }), new Response(null, { status: 302, headers: { Location: "http://127.0.0.1" } }), new Response(" ".repeat(128 * 1024 + 1))]) {
      globalThis.fetch = async (_url, options) => { assert.equal(options.redirect, "manual"); return response; };
      const result = await route.GET(request(query)); assert.equal(result.status, 502); assert.equal((await result.text()).includes("secret provider detail"), false);
    }
    const abort = new AbortController(); abort.abort(); globalThis.fetch = () => assert.fail("aborted request reached provider");
    assert.equal((await route.GET(new Request(request(query), { signal: abort.signal }))).status, 502);
    globalThis.fetch = async url => Response.json(new URL(url).searchParams.has("returnCountOnly") ? { count: 1 } : body());
    const result = await route.GET(request(query)); assert.equal(result.status, 200); assert.equal(result.headers.get("cache-control"), "no-store"); assert.equal((await result.json()).records.length, 1);
  } finally { globalThis.fetch = original; }
});
test("API reads bounded sequential pages and fails closed on page errors", async () => {
  const original = globalThis.fetch;
  const offsets = [];
  try {
    globalThis.fetch = async (url, options) => {
      assert.equal(options.redirect, "manual");
      const params = new URL(url).searchParams;
      if (params.has("returnCountOnly")) return Response.json({ count: 105 });
      const offset = Number(params.get("resultOffset")); offsets.push(offset);
      return Response.json(body(Array.from({ length: Math.min(50, 105 - offset) }, (_, i) => feature({ OBJECTID: offset + i + 1 }))));
    };
    const response = await route.GET(request(query)), result = await response.json();
    assert.equal(response.status, 200); assert.deepEqual(offsets, [0, 50, 100]);
    assert.equal(result.records.length, 105); assert.equal(result.providerCount, 105);
    assert.equal(result.pagesRead, 3); assert.equal(result.partial, false);
    offsets.length = 0;
    globalThis.fetch = async url => new URL(url).searchParams.has("returnCountOnly") ? Response.json({ count: 0 }) : assert.fail("zero count requested a page");
    const empty = await (await route.GET(request(query))).json();
    assert.equal(empty.state, "empty"); assert.equal(empty.pagesRead, 0);
    globalThis.fetch = async url => {
      const params = new URL(url).searchParams;
      if (params.has("returnCountOnly")) return Response.json({ count: 251 });
      const offset = Number(params.get("resultOffset")); offsets.push(offset);
      return Response.json(body(Array.from({ length: 50 }, (_, i) => feature({ OBJECTID: offset + i + 1 }))));
    };
    const capped = await (await route.GET(request(query))).json();
    assert.deepEqual(offsets, [0, 50, 100, 150, 200]);
    assert.equal(capped.state, "partial"); assert.equal(capped.records.length, 250); assert.equal(capped.providerCount, 251);
    const aborted = new AbortController(); let calls = 0;
    globalThis.fetch = async url => {
      const params = new URL(url).searchParams;
      if (params.has("returnCountOnly")) return Response.json({ count: 60 });
      calls++;
      aborted.abort();
      return Response.json(body(Array.from({ length: 50 }, (_, i) => feature({ OBJECTID: i + 1 }))));
    };
    assert.equal((await route.GET(new Request(request(query), { signal: aborted.signal }))).status, 502);
    assert.equal(calls, 1);
    globalThis.fetch = async url => {
      const params = new URL(url).searchParams;
      if (params.has("returnCountOnly")) return Response.json({ count: 51 });
      return Number(params.get("resultOffset")) === 0 ? Response.json(body(Array.from({ length: 50 }, (_, i) => feature({ OBJECTID: i + 1 })))) : Response.json({ error: { code: 500, message: "internal" } });
    };
    assert.equal((await route.GET(request(query))).status, 502);
  } finally { globalThis.fetch = original; }
});
