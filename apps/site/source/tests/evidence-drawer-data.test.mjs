import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const source = await readFile(new URL("../app/evidence-drawer-data.ts", import.meta.url), "utf8");
const javascript = ts.transpileModule(source, {
  compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
  fileName: "evidence-drawer-data.ts",
}).outputText;
const { drawerArtifactAttributes, parseUsgsStageDetail } = await import(`data:text/javascript;base64,${Buffer.from(javascript).toString("base64")}`);

test("artifact fields expose allowlisted provider data but omit arbitrary and sensitive keys", () => {
  const fields = drawerArtifactAttributes("census-counties", { geoid: "20139", population: 0, housingUnits: 12, privateNote: "withhold", latitude: 38.7 });
  assert.deepEqual(fields, [
    { label: "County GEOID", value: "20139" },
    { label: "Population count", value: "0" },
    { label: "Housing units", value: "12" },
  ]);
  assert.deepEqual(drawerArtifactAttributes("usgs-wbd-watersheds", { arbitrary: "unsafe" }), []);
  assert.deepEqual(drawerArtifactAttributes("basemap", { name: "Creek", secret: "withhold" }), [{ label: "Name", value: "Creek" }]);
});

const stageResponse = {
  kind: "usgs-streamflow-bundle", mode: "station", parameterCode: "00065",
  queryStart: "2026-09-16T00:00:00.000Z", queryEnd: "2026-09-23T00:00:00.000Z", retrievedAt: "2026-09-23T00:01:00.000Z",
  partial: false, truncated: false,
  stations: [{ stationId: "USGS-06911900", agencyCode: "USGS", name: "DRAGOON C NR BURLINGAME, KS", county: "Osage County", huc: "10290101", drainageArea: 114, contributingDrainageArea: 114, siteTypeCode: "ST", latitude: 38.7, longitude: -95.8 }],
  observations: [
    { stationId: "USGS-06911900", parameterCode: "00065", observedAt: "2026-09-20T00:00:00.000Z", value: 3.25, unit: "ft", approvalStatus: "Provisional", qualifiers: [] },
    { stationId: "USGS-06911900", parameterCode: "00065", observedAt: "2026-09-21T00:00:00.000Z", value: null, unit: "ft", approvalStatus: null, qualifiers: [] },
  ],
};

test("stage detail keeps station metadata and dated history when the selected discharge frame is empty", () => {
  const detail = parseUsgsStageDetail(stageResponse, "USGS-06911900");
  assert.equal(detail.county, "Osage County");
  assert.equal(detail.drainageArea, 114);
  assert.equal(detail.observationCount, 2);
  assert.equal(detail.latest.value, 3.25);
  assert.equal(detail.recent[0].value, null);
});

test("stage detail rejects a different station or discharge masquerading as gauge height", () => {
  assert.throws(() => parseUsgsStageDetail(stageResponse, "USGS-06911901"));
  assert.throws(() => parseUsgsStageDetail({ ...stageResponse, parameterCode: "00060" }, "USGS-06911900"));
  assert.throws(() => parseUsgsStageDetail({ ...stageResponse, observations: [{ ...stageResponse.observations[0], stationId: "USGS-06911901" }] }, "USGS-06911900"));
});

test("stage detail rejects invalid windows and stale, future or impossible observation clocks", () => {
  for (const patch of [
    { queryStart: stageResponse.queryEnd }, { queryStart: "2026-09-24T00:00:00Z" },
    { queryStart: "2026-02-30T00:00:00Z" }, { queryEnd: "2026-09-23" },
    { queryEnd: "2026-09-23T24:00:00Z" }, { retrievedAt: "2026-09-22T23:59:59Z" },
  ]) assert.throws(() => parseUsgsStageDetail({ ...stageResponse, ...patch }, "USGS-06911900"));
  for (const observedAt of ["2026-09-01T00:00:00Z", "2026-09-30T00:00:00Z", "2026-09-15T23:59:59.999999999Z", "2026-09-23T00:00:00.000000001Z", "2026-09-20T24:00:00Z", "2026-09-31T00:00:00Z", "2026-09-20", "2026-09-20T00:00:00.1234567890Z"]) {
    const payload = structuredClone(stageResponse); payload.observations[0].observedAt = observedAt;
    assert.throws(() => parseUsgsStageDetail(payload, "USGS-06911900"), /observations were invalid/, observedAt);
  }
});

test("stage detail keeps inclusive endpoints, zero, null, qualifiers and exact fractional ordering", () => {
  const payload = structuredClone(stageResponse), row = payload.observations[0];
  payload.observations = [
    { ...row, observedAt: payload.queryStart, value: 0, qualifiers: ["P"] },
    { ...row, observedAt: payload.queryEnd, value: null, approvalStatus: null },
  ];
  const endpoints = parseUsgsStageDetail(payload, "USGS-06911900");
  assert.equal(endpoints.latest.value, 0); assert.equal(endpoints.latest.observedAt, payload.queryStart);
  assert.deepEqual(endpoints.latest.qualifiers, ["P"]); assert.equal(endpoints.recent[0].value, null);
  payload.observations = [
    { ...row, observedAt: "2026-09-22T12:00:00.123100Z", value: 1 },
    { ...row, observedAt: "2026-09-22T12:00:00.123900001Z", value: 2 },
  ];
  const exact = parseUsgsStageDetail(payload, "USGS-06911900");
  assert.equal(exact.latest.value, 2); assert.equal(exact.latest.observedAt, "2026-09-22T12:00:00.123900001Z");
  assert.equal(exact.recent[1].value, 1);
});

// Exercise the actual route and actual drawer parser together, with only fixed
// time and two allowlisted provider collections supplied by the local fixture.
const compileModule = async (file, imports = {}, globals = {}) => {
  const output = ts.transpileModule(await readFile(new URL(`../app/${file}.ts`, import.meta.url), "utf8"), {
    compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 },
  }).outputText;
  const mod = { exports: {} };
  new Function("require", "module", "exports", ...Object.keys(globals), output)(name => {
    if (!(name in imports)) throw new Error(`Unexpected stage fixture import: ${name}`);
    return imports[name];
  }, mod, mod.exports, ...Object.values(globals));
  return mod.exports;
};
const routeSource = await readFile(new URL("../app/api/hydrology/streamflow/route.ts", import.meta.url), "utf8");
const routeCode = ts.transpileModule(routeSource, { compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 } }).outputText;
const bounded = await compileModule("bounded-json"), transport = await compileModule("streamflow-transport");
const stationId = "USGS-06911900", queryEnd = "2026-09-23T00:00:00.123Z", queryStart = "2026-09-16T00:00:00.123Z";
class FixedDate extends Date { constructor(...args) { super(...(args.length ? args : [Date.parse(queryEnd)])); } static now() { return Date.parse(queryEnd); } }
const stageFeature = (observedAt, value) => ({ type: "Feature", id: `fixture-${observedAt}`, geometry: { type: "Point", coordinates: [-95.8, 38.7] }, properties: {
  time_series_id: "fixture-stage", monitoring_location_id: stationId, parameter_code: "00065", statistic_id: null, time: observedAt,
  value, unit_of_measure: "ft", approval_status: "Provisional", qualifier: ["P"], last_modified: queryEnd,
} });
async function stationResponse(features) {
  const calls = [], mod = { exports: {} };
  new Function("require", "module", "exports", "fetch", "Date", "console", routeCode)(name => {
    if (name === "../../../bounded-json") return bounded;
    if (name === "../../../streamflow-transport") return transport;
    if (name === "cloudflare:workers") return { env: {} };
    if (name === "next/server") return { NextResponse: Response };
    throw new Error(`Unexpected stage route import: ${name}`);
  }, mod, mod.exports, async (input, options) => {
    const url = new URL(input); calls.push(url);
    assert.equal(url.origin, "https://api.waterdata.usgs.gov"); assert.equal(options.redirect, "manual");
    const rows = url.pathname.includes("monitoring-locations") ? [{ type: "Feature", id: stationId, geometry: { type: "Point", coordinates: [-95.8, 38.7] }, properties: {
      id: stationId, agency_code: "USGS", monitoring_location_number: stationId.slice(5), monitoring_location_name: "Synthetic selected gauge", site_type_code: "ST",
      hydrologic_unit_code: null, county_name: null, drainage_area: null, contributing_drainage_area: null,
    } }] : features;
    return Response.json({ type: "FeatureCollection", features: rows, numberReturned: rows.length, links: [], timeStamp: queryEnd });
  }, FixedDate, { error() {} });
  const response = await mod.exports.GET({ nextUrl: new URL(`https://site.test/api/hydrology/streamflow?mode=station&range=7d&station=${stationId}&parameter=00065&resolution=continuous`) });
  assert.equal(calls.length, 2);
  const query = calls.find(url => url.pathname.includes("/continuous/"));
  assert.equal(query.searchParams.get("datetime"), `${queryStart}/${queryEnd}`); assert.equal(query.searchParams.get("parameter_code"), "00065");
  return response;
}

test("the actual seven-day station route and drawer preserve valid inclusive endpoints", async () => {
  const response = await stationResponse([stageFeature(queryStart, null), stageFeature("2026-09-22T19:00:00.123000000-05:00", 0)]);
  assert.equal(response.status, 200);
  const body = await response.json(), detail = parseUsgsStageDetail(body, stationId);
  assert.equal(body.partial, false); assert.equal(body.truncated, false); assert.equal(detail.observationCount, 2);
  assert.equal(detail.latest.value, 0); assert.equal(detail.latest.observedAt, queryEnd); assert.deepEqual(detail.latest.qualifiers, ["P"]);
  assert.equal(detail.recent[1].value, null); assert.equal(detail.queryStart, queryStart); assert.equal(detail.queryEnd, queryEnd);
});

test("the actual station route withholds stale, future, rollover and nanosecond-outside provider samples", async () => {
  for (const observedAt of ["2026-09-01T00:00:00Z", "2026-09-30T00:00:00Z", "2026-09-16T00:00:00.122999999Z", "2026-09-23T00:00:00.123000001Z", "2026-09-22T19:00:00.123000001-05:00", "2026-09-22T24:00:00Z", "2026-09-31T00:00:00Z", "2026-09-22T00:00:00.1234567890Z"]) {
    const response = await stationResponse([stageFeature("2026-09-22T12:00:00Z", 3.25), stageFeature(observedAt, 42)]);
    assert.equal(response.status, 502, observedAt);
    const body = await response.json(); assert.equal(body.code, "USGS_STREAMFLOW_UNAVAILABLE"); assert.equal("observations" in body, false);
    assert.equal(response.headers.get("cache-control"), "no-store"); assert.throws(() => parseUsgsStageDetail(body, stationId));
  }
});
