import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

async function loadPure(path) {
  const source = await readFile(new URL(`../app/${path}`, import.meta.url), "utf8");
  const js = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
  return import(`data:text/javascript;base64,${Buffer.from(js).toString("base64")}`);
}
const workspace = await loadPure("layer-workspaces.ts");
const fema = await loadPure("fema-declarations.ts");

test("disaster and land workspaces retain independent source choices", () => {
  const sources = [
    { id: "nws-radar", title: "Radar", shortTitle: "Radar", organization: "NOAA", domain: "Weather", defaultVisibility: false },
    { id: "blm-plss-sections", title: "Sections", shortTitle: "Sections", organization: "BLM", domain: "Land", defaultVisibility: false },
    { id: "fema-disaster-declarations", title: "Declarations", shortTitle: "Declarations", organization: "FEMA", domain: "Disaster", defaultVisibility: false },
  ];
  assert.deepEqual(workspace.filterOfficialSources(sources, "disaster", "").map(s => s.id), ["nws-radar", "fema-disaster-declarations"]);
  assert.deepEqual(workspace.filterOfficialSources(sources, "land", "sections").map(s => s.id), ["blm-plss-sections"]);
  assert.equal(workspace.DISASTER_COVERAGE_HOLDS.some(item => item.title === "FEMA disaster declarations"), false);
});

test("FEMA county designation uses reference geometry and withholds invalid or statewide records", () => {
  const geometry = { type: "Polygon", coordinates: [[[-101, 38], [-100, 38], [-100, 39], [-101, 38]]] };
  const counties = { type: "FeatureCollection", features: Array.from({ length: 105 }, (_, i) => ({ type: "Feature", geometry, properties: { geoid: `20${String(i + 1).padStart(3, "0")}`, name: `County ${i}` } })) };
  const valid = { id: "abc-123", state: "KS", fipsStateCode: "20", fipsCountyCode: "001", disasterNumber: 4943, declarationDate: "2026-09-01T00:00:00.000Z", incidentType: "Severe Storm", designatedArea: "County 0" };
  const result = fema.parseFemaDeclarations({ DisasterDeclarationsSummaries: [valid, { ...valid, id: "statewide", fipsCountyCode: "000" }, { ...valid, id: "wrong", state: "OK" }] }, counties, "2026-09-30T12:00:00Z");
  assert.equal(result.data.features.length, 1);
  assert.equal(result.skipped, 2);
  assert.equal(result.partial, true);
  assert.equal(result.data.features[0].geometry, geometry);
  assert.match(result.data.features[0].properties.geometryRole, /not disaster footprint/);
  assert.equal(result.data.features[0].properties.declarationAt, "2026-09-01T00:00:00.000Z");
});

test("BLM image URLs are fixed to Kansas filters and source scale", async () => {
  const source = await readFile(new URL("../app/live-context.ts", import.meta.url), "utf8");
  assert.match(source, /blmPlssImageUrl\(1, "STATEABBR='KS'"\)/);
  assert.match(source, /blmPlssImageUrl\(2, "PLSSID LIKE 'KS%'"\)/);
  assert.match(source, /blmPlssImageUrl\(3, "STATEABBR='KS'"\)/);
  assert.match(source, /minDisplayZoom: 8[\s\S]*id: "blm-plss-townships"/);
  assert.match(source, /minDisplayZoom: 11[\s\S]*id: "blm-plss-sections"/);
  assert.match(source, /minDisplayZoom: 12[\s\S]*id: "blm-plss-intersected"/);
});
