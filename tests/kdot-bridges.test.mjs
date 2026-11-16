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
const model = await import(await load("app/kdot-bridges.ts"));
const server = await import(await load("app/api/live-context/kdot-bridges.ts"));
const filters = (await import(await load("app/kansas-bridge-records.ts"))).BRIDGE_FILTERS;
const now = new Date("2026-11-15T12:00:00Z");

// Synthetic records in the provider's shape; none describes a real bridge.
const local = (id, attributes = {}, geometry = { x: -96.5 + id / 1000, y: 39.1 }) => ({ geometry, attributes: { OBJECTID: id, STRUCT_NUM: `SYN${id}`, FACILITY: "RS 100   Y.0", FEATINT: "SYNTHETIC CREEK, TRIB.",
  LOCATION: "1.0E 2.0N OF NOWHERE", COUNTY: "Riley", YEARBUILT: 1936, YEARRECON: null, MATERIALMAIN: "Steel", DESIGNMAIN: "Truss-Thru", LENGTH_ENG: 142.26, MAINSPANS: 2, LANES: 2, ADTTOTAL: 85, ADTYEAR: 2019,
  OPPOSTCL: "Open, no restriction", POSTING: "> 39.9% below", HISTSIGN: "Not eligible for NRHP", OWNER: "County Hwy Agency", SUFF_RATE: 61.23, DKRATING: "6 - Satisfactory", SUPRATING: "5 - Fair",
  SUBRATING: "NA", CULVRATING: "NA", INSPDATE: Date.UTC(2025, 4, 1), ...attributes } });
const state = (id, attributes = {}, geometry = { x: -97.3, y: 37.7 + id / 1000 }) => ({ geometry, attributes: { OBJECTID: id, STR_NAME: `0000-B${id}`, FACILITY: "US-99 HWY NB", FEATINT: "SYNTHETIC RIVER",
  LOCATION: "1.00 MI N K0 JCT", COUNTYNAME: "SEDGWICK", BUILT_DATE: 1977, MATERIALMAIN: "Reinforced Concrete", DESIGNMAIN: "Box Girder", STR_LENGTH: 2400.5, LANES_CARRIED: 3, STR_AADT: 45050,
  OPPOSTCL: "Open", SUF_RATE: 98.9, OWNER: "S01 State transportation department ", UNDER_CONSTRUCTION: "N", ...attributes } });
const page = features => ({ geometryType: "esriGeometryPoint", spatialReference: { wkid: 4326 }, features });

test("provider pages become bounded, readable records and skip points outside Kansas", () => {
  const { bridges, skipped, received } = model.parseBridgePage(page([local(1), local(2, {}, { x: 95.2, y: 37.7 }), local(3, {}, null), { attributes: { OBJECTID: "x" }, geometry: { x: -97, y: 38 } },
    local(4, { YEARBUILT: -1, OPPOSTCL: "Closed to all traffic", HISTSIGN: "Br eligible for NRHP", FEATINT: "<script>alert(1)</script>", INSPDATE: Date.UTC(2099, 0, 1), DKRATING: "Unknown (NBI)" })]), "local", now);
  assert.equal(received, 5); assert.equal(skipped, 3); assert.equal(bridges.length, 2);
  const [first, closed] = bridges;
  assert.deepEqual({ id: first.id, carries: first.carries, crosses: first.crosses, built: first.built, lengthFt: first.lengthFt, statusClass: first.statusClass, loadPosting: first.loadPosting, substructure: first.substructure, inspected: first.inspected, sufficiency: first.sufficiency },
    { id: "kdot-local-1", carries: "RS 100 Y.0", crosses: "Synthetic Creek, Trib.", built: 1936, lengthFt: 142.3, statusClass: "open", loadPosting: "More than 39.9% below", substructure: null, inspected: "2025-05-01", sufficiency: 61.2 });
  assert.equal(closed.built, null, "a placeholder year is not a build year");
  assert.equal(closed.statusClass, "closed"); assert.equal(closed.historicListed, true);
  assert.equal(closed.inspected, null, "a future inspection date is dropped"); assert.equal(closed.deck, null);
  assert.equal(/[<>]/.test(closed.crosses), false, "angle brackets never reach the map or panel");
  const [highway] = model.parseBridgePage(page([state(7, { OPPOSTCL: "Weight" })]), "state", now).bridges;
  assert.deepEqual({ id: highway.id, carries: highway.carries, county: highway.county, owner: highway.owner, statusClass: highway.statusClass, structureId: highway.structureId },
    { id: "kdot-state-7", carries: "US-99 Hwy NB", county: "Sedgwick", owner: "State transportation department", statusClass: "posted", structureId: "0000-B7" });
  for (const bad of [null, {}, { features: [] }, { ...page([]), error: { code: 400 } }, { ...page([]), spatialReference: { wkid: 3857 } }, page(Array.from({ length: 5001 }, (_, i) => local(i)))]) {
    assert.throws(() => model.parseBridgePage(bad, "local", now), /Invalid provider response/);
  }
});

test("each layer keeps the record set its earlier provider filter named", () => {
  const { bridges } = model.parseBridgePage(page([local(1), local(2, { YEARBUILT: 1949 }), local(3, { YEARBUILT: 1950 }), local(4, { YEARBUILT: null }),
    local(5, { HISTSIGN: "Br on Natl Reg Hist Place", YEARBUILT: 1990 }), local(6, { HISTSIGN: "Possibly eligible for", YEARBUILT: 1990 }), local(7, { OPPOSTCL: "Closed to all traffic", YEARBUILT: 1990 }), local(8, { OPPOSTCL: "Posted for load", YEARBUILT: 1990 })]), "local", now);
  const kept = feed => bridges.filter(model.BRIDGE_FEEDS[feed].keep).map(bridge => bridge.id.split("-").pop()).join("");
  assert.equal(kept("kdot-bridges-local"), "12345678");
  assert.equal(kept("kdot-bridges-old"), "12"); assert.match(filters["kdot-bridges-old"].where, /YEARBUILT >= 1800 AND YEARBUILT < 1950/);
  assert.equal(kept("kdot-bridges-historic"), "5"); assert.match(filters["kdot-bridges-historic"].where, /Br eligible for NRHP.*Br on Natl Reg Hist Place/);
  assert.equal(kept("kdot-bridges-closed"), "7"); assert.match(filters["kdot-bridges-closed"].where, /Closed to all traffic/);
  assert.deepEqual(Object.keys(model.BRIDGE_FEEDS), Object.keys(filters));
});

test("the map record is slim; the selected bridge's full record is readable text only", () => {
  const { bridges } = model.parseBridgePage(page([local(1), local(2, { OPPOSTCL: "Closed to all traffic", LENGTH_ENG: 3451, ADTTOTAL: 9000 })]), "local", now);
  const feature = model.bridgeMapFeature(bridges[0]);
  assert.deepEqual(feature, { type: "Feature", geometry: { type: "Point", coordinates: [-96.499, 39.1] }, properties: { featureId: "kdot-local-1", name: "Synthetic Creek, Trib.", built: 1936, lengthFt: 142.3 } });
  assert.equal(model.bridgeMapFeature(bridges[1]).properties.statusClass, "closed");
  const peers = model.bridgeHighlights(bridges);
  assert.deepEqual({ longest: peers.longest.id, busiest: peers.busiest.id, earliest: peers.earliestBuilt, closed: peers.closed, before1950: peers.before1950 }, { longest: "kdot-local-2", busiest: "kdot-local-2", earliest: 1936, closed: 1, before1950: 2 });
  const detail = model.bridgeDetailProperties(bridges[0], peers, now);
  assert.deepEqual(detail, { name: "RS 100 Y.0 at Synthetic Creek, Trib.", carries: "RS 100 Y.0", crosses: "Synthetic Creek, Trib.", location: "1.0E 2.0N of Nowhere", county: "Riley",
    builtLabel: "1936 · about 90 years ago", structureType: "Steel · Truss-Thru", lengthLabel: "142.3 ft · 2 main spans", lanesLabel: "2 lanes", trafficLabel: "About 85 vehicles a day (2019 count)",
    status: "Open, no restriction", loadPosting: "More than 39.9% below", historic: "Not eligible for NRHP", condition: "Deck 6 - Satisfactory · Superstructure 5 - Fair",
    sufficiencyLabel: "61.2 of 100", inspected: "2025-05-01", owner: "County Hwy Agency", structureId: "SYN1", network: "Local road (county or city)" });
  assert.match(model.bridgeDetailProperties(bridges[1], peers, now).highlight, /Longest structure in KDOT's local road inventory · Busiest/);
  for (const value of Object.values(detail)) assert.equal(typeof value, "string");
  const summary = model.bridgeSummary("kdot-bridges-local", bridges, 1, false);
  assert.match(summary, /^2 local road bridges in KDOT's inventory\. Longest: RS 100 Y\.0 at Synthetic Creek, Trib\., 3,451 ft \(Riley County\)\./);
  assert.match(summary, /1 record without a usable Kansas location is left out/);
  assert.match(summary, /not a live closure feed, a safety determination or navigation advice/);
});

function provider(overrides = {}) {
  const calls = [];
  const data = { state: Array.from({ length: 1500 }, (_, i) => state(i + 1)), local: Array.from({ length: 3 }, (_, i) => local(i + 1)), ...overrides.data };
  const fetcher = async (url, init) => {
    const u = new URL(url), network = u.pathname.includes("/State_Bridges/") ? "state" : "local";
    calls.push({ network, count: u.searchParams.has("returnCountOnly"), offset: u.searchParams.get("resultOffset"), init });
    if (overrides.fail?.(network)) return new Response("provider detail that must not leak", { status: 500 });
    assert.equal(u.hostname, "kanplan.ksdot.gov"); assert.equal(u.searchParams.get("where"), "1=1");
    if (u.searchParams.has("returnCountOnly")) return Response.json({ count: overrides.count?.[network] ?? data[network].length });
    const offset = Number(u.searchParams.get("resultOffset")), size = Number(u.searchParams.get("resultRecordCount"));
    assert.equal(u.searchParams.get("outSR"), "4326"); assert.equal(u.searchParams.get("orderByFields"), "OBJECTID");
    return Response.json(page(data[network].slice(offset, offset + size)));
  };
  return { fetcher, calls };
}

test("one inventory read per network serves every layer and bridge detail for a day", async () => {
  let time = now.getTime(); const { fetcher, calls } = provider();
  const reader = server.createBridgeReader(fetcher, () => time);
  const [a, b] = await Promise.all([reader.feed("kdot-bridges-state"), reader.feed("kdot-bridges-state")]);
  assert.equal(a, b, "concurrent readers share one read and one payload");
  assert.deepEqual(calls.map(call => `${call.network}:${call.count ? "count" : call.offset}`), ["state:count", "state:0", "state:1000"]);
  assert.equal(calls[0].init.redirect, "manual");
  assert.deepEqual({ feed: a.feed, state: a.state, featureCount: a.featureCount, truncated: a.truncated, count: a.data.features.length }, { feed: "kdot-bridges-state", state: "ready", featureCount: 1500, truncated: false, count: 1500 });
  assert.match(a.source, /Kansas Department of Transportation · State Bridges inventory/);
  assert.equal((await reader.detail("kdot-state-3")).properties.structureId, "0000-B3");
  assert.equal(await reader.detail("kdot-state-999999"), null); assert.equal(await reader.detail("kdot-other-1"), null);
  assert.equal(calls.length, 3, "detail reuses the cached inventory");
  // The four local layers share the other network's single read.
  for (const feed of ["kdot-bridges-local", "kdot-bridges-old", "kdot-bridges-historic", "kdot-bridges-closed"]) await reader.feed(feed);
  assert.deepEqual(calls.slice(3).map(call => `${call.network}:${call.count ? "count" : call.offset}`), ["local:count", "local:0"]);
  assert.equal((await reader.feed("kdot-bridges-old")).featureCount, 3); assert.equal((await reader.feed("kdot-bridges-closed")).state, "empty");
  time += server.BRIDGE_CACHE_MS - 1; await reader.feed("kdot-bridges-state"); assert.equal(calls.length, 5);
  time += 2; await reader.feed("kdot-bridges-state"); assert.equal(calls.length, 8, "a day-old inventory is read again");
});

test("duplicate provider rows, missing points and an over-long inventory are reported, not hidden", async () => {
  const rows = [state(1), state(1), state(2, {}, { x: 0, y: 0 }), state(3)];
  const reader = server.createBridgeReader(provider({ data: { state: rows } }).fetcher, () => now.getTime());
  const payload = await reader.feed("kdot-bridges-state");
  assert.deepEqual({ state: payload.state, count: payload.featureCount, truncated: payload.truncated }, { state: "partial", count: 2, truncated: false });
  assert.match(payload.limitation, /1 record without a usable Kansas location is left out/);
  const long = server.createBridgeReader(provider({ count: { state: 10_001 } }).fetcher, () => now.getTime());
  const capped = await long.feed("kdot-bridges-state");
  assert.equal(capped.truncated, true); assert.equal(capped.state, "partial"); assert.match(capped.limitation, /some bridges are missing/);
});

test("a provider outage fails fast with a waiting time, serves no old data and recovers", async () => {
  let time = now.getTime(), down = false; const { fetcher, calls } = provider({ fail: () => down });
  const reader = server.createBridgeReader(fetcher, () => time);
  await reader.feed("kdot-bridges-local");
  down = true; time += server.BRIDGE_CACHE_MS + 1;
  await assert.rejects(reader.feed("kdot-bridges-local"), error => /KDOT bridge records are unavailable\. No bridge locations, status or absence can be inferred\. Next provider check in about 1 minute\.$/.test(error.message) && !/provider detail/.test(error.message));
  const attempts = calls.length;
  await assert.rejects(reader.detail("kdot-local-1"), /Next provider check in about 1 minute/);
  assert.equal(calls.length, attempts, "no provider request inside the waiting time");
  time += 60_001; await assert.rejects(reader.feed("kdot-bridges-old"), /about 2 minutes/);
  // The state network is independent of the local outage.
  down = false; time += 1; assert.equal((await reader.feed("kdot-bridges-state")).featureCount, 1500);
  time += 120_001; assert.equal((await reader.feed("kdot-bridges-local")).featureCount, 3);
});

test("the detail route accepts only a bridge id from the map and reads no visitor query", async () => {
  const route = await readFile("app/api/bridge-detail/route.ts", "utf8");
  assert.match(route, /const BRIDGE_ID = \/\^kdot-\(\?:state\|local\)-\\d\{1,9\}\$\/;/);
  assert.match(route, /params\.getAll\("id"\)\.length !== 1 \|\| !BRIDGE_ID\.test\(id\)/);
  assert.match(route, /"Cache-Control": "no-store"/);
  assert.doesNotMatch(route, /fetch\(|where|longitude|latitude/);
  const feed = await readFile("app/api/live-context/route.ts", "utf8");
  assert.match(feed, /isBridgeFeed\(feed\) \? await kdotBridges\.feed\(feed\)/);
  const page = await readFile("app/page.tsx", "utf8");
  assert.match(page, /fetch\(`\/api\/bridge-detail\?id=\$\{encodeURIComponent\(selectedBridgeId\)\}`/);
  assert.match(page, /body\.id !== selectedBridgeId/, "a late answer for another bridge is ignored");
  assert.match(page, /const clusterSummary = officialClusterSummary\(externalCandidate\?\.source \? OFFICIAL_CONTEXT_BY_SOURCE_ID\[externalCandidate\.source\]\?\.id : undefined, externalCandidate\?\.properties\);/);
  assert.match(page, /getClusterExpansionZoom\(Number\(externalCandidate\.properties\?\.cluster_id\)\)/);
});
