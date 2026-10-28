import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

// Execute the actual export builder; no replacement implementation or GPS read.
const source = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
const tree = ts.createSourceFile("page.tsx", source, ts.ScriptTarget.Latest, true, ts.ScriptKind.TSX);
let builder, emptyFindings;
const walk = node => {
  if (ts.isVariableDeclaration(node) && node.name.getText(tree) === "buildCustomReportPayload") builder = node.initializer;
  if (ts.isVariableDeclaration(node) && node.name.getText(tree) === "emptyReportFindings") emptyFindings = node.initializer;
  ts.forEachChild(node, walk);
};
walk(tree);
assert.ok(builder);
const js = ts.transpileModule(`const build = ${builder.getText(tree)};`, { compilerOptions: {target: ts.ScriptTarget.ES2022} }).outputText;
const emptyReportFindings = new Function(ts.transpileModule(`return ${emptyFindings.getText(tree)};`, { compilerOptions: {target: ts.ScriptTarget.ES2022} }).outputText)();

const coordinate = [-97.1234567, 38.7654321];
const bounds = {west: -97.1298765, east: -97.1176543, south: 38.7601234, north: 38.7705678};
function context({privateState = false, privateRef = false, scope = "VIEWPORT"} = {}) {
  return {
    LAYER_REGISTRY: [],
    reportDetail: "STANDARD", reportRecords: [], scenePreset: "elevation-3d", terrainState: "READY",
    attachedTerrainProviderRef: {current: "usgs-3dep"}, terrainProvider: "usgs-3dep", topographicOverlay: true,
    reportTitle: "Fixture report", reportScope: scope, reportQuery: "", mapEvidenceFilter: "ALL", reportEvidenceFilter: "ALL", reportLayerIds: [],
    temporalQuery: {frame: 2026}, temporalScopeLabel: "2026", temporalMode: "snapshot", reportTemporalComparison: {},
    locationCameraRedacted: privateState, locationDerivedViewRef: {current: privateRef},
    view: {center: coordinate, zoom: 13.5, pitch: 48, bearing: 12}, mapRepresentationLabel: "Terrain 3D", verticalExaggeration: 1,
    lockedTerrainElevation: {meters: 400, feet: 1312, longitude: coordinate[0], latitude: coordinate[1], provider: "usgs-3dep"},
    projection: "mercator", basemap: "vector", mapViewportBounds: bounds, analysisArea: bounds,
    measurementGeometryMode: "point", measureUnit: "metric", measurement: `Point ${coordinate.join(", ")}`,
    measureCoordinatesRef: {current: [coordinate]}, selected: null, selectedTimeMismatch: false,
    reportSections: {summary: true, findings: true, records: true, evidence: true, limitations: true},
    reportLayerSummary: [], reportEvidenceCounts: {}, reportFindings: [], terrainSourceFor: () => ({attribution: "USGS display DEM"}),
  };
}
const run = values => new Function('emptyReportFindings', ...Object.keys(values), `${js}; return build("2026-10-11T20:00:00Z");`)(emptyReportFindings, ...Object.values(values));

test("private report JSON withholds every geometry carrier and point label for both export scopes", () => {
  for (const scope of ["VIEWPORT", "ANALYSIS_AREA"]) for (const [privateState, privateRef] of [[true,false], [false,true], [true,true]]) {
    const values = context({scope,privateState,privateRef});
    const before = structuredClone({...values, terrainSourceFor: undefined});
    const result = run(values);
    assert.equal(result.mapContext.center, "WITHHELD_BROWSER_LOCATION");
    assert.equal(result.mapContext[scope === "VIEWPORT" ? "viewport" : "analysisArea"], "WITHHELD_BROWSER_LOCATION");
    assert.equal(result.measurements.label, "WITHHELD_BROWSER_LOCATION");
    assert.equal(result.measurements.coordinates, "WITHHELD_BROWSER_LOCATION");
    assert.equal(result.mapContext.terrain.heightOverlay.lockedReading.coordinate, "WITHHELD_BROWSER_LOCATION");
    for (const number of [...coordinate,...Object.values(bounds)]) assert.ok(!JSON.stringify(result).includes(String(number)), `private coordinate ${number} cannot survive serialization`);
    assert.deepEqual({...values,terrainSourceFor: undefined}, before, "export redaction does not mutate local inspection state");
  }
});

test("non-private reports retain deliberate geometry, source height and measurement output", () => {
  for (const scope of ["VIEWPORT", "ANALYSIS_AREA"]) {
    const result = run(context({scope}));
    assert.deepEqual(result.mapContext.center, coordinate);
    assert.deepEqual(result.mapContext[scope === "VIEWPORT" ? "viewport" : "analysisArea"], bounds);
    assert.deepEqual(result.measurements.coordinates, [coordinate]);
    assert.equal(result.measurements.label, `Point ${coordinate.join(", ")}`);
    assert.equal(result.mapContext.terrain.heightOverlay.lockedReading.elevationMeters, 400);
  }
});
