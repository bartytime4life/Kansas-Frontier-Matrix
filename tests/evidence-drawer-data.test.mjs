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
