import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const moduleUrl = async (name, transform = (source) => source) => {
  const source = await readFile(new URL(`../app/${name}.ts`, import.meta.url), "utf8");
  const output = ts.transpileModule(transform(source), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
  return `data:text/javascript;base64,${Buffer.from(output).toString("base64")}`;
};
const editionsUrl = await moduleUrl("road-map-editions");
const importUrl = await moduleUrl("import-preview");
const editions = await import(editionsUrl);
const study = await import(await moduleUrl("road-year-study", (source) => source
  .replace('from "./import-preview";', `from "${importUrl}";`)
  .replace('from "./road-map-editions";', `from "${editionsUrl}";`)));
const bounds = { west: -102.1, south: 36.9, east: -94.5, north: 40.1 };
const geojson = (geometry) => JSON.stringify({ type: "FeatureCollection", features: [{ type: "Feature", properties: { route: "study only" }, geometry }] });
const input = (editionId, text) => ({ editionId, fileName: `${editionId}.geojson`, fileSizeBytes: Buffer.byteLength(text), text, color: "#ffbd69", supportedBounds: bounds });

test("inventory keeps distinct editions and holds the blank local PDF", () => {
  assert.equal(editions.ROAD_MAP_EDITIONS.length, 55);
  assert.equal(new Set(editions.ROAD_MAP_EDITIONS.map((edition) => edition.id)).size, 55);
  assert.equal(editions.ROAD_MAP_EDITION_BY_ID["1967"].localPdfState, "BLANK");
  assert.equal(editions.ROAD_MAP_EDITION_BY_ID["1950-1951"].endYear, 1951);
  assert.notEqual(editions.ROAD_MAP_EDITION_BY_ID["1938"].sha256, editions.ROAD_MAP_EDITION_BY_ID["1938-2"].sha256);
  assert.ok(editions.ROAD_MAP_EDITIONS.every((edition) => /^[a-f0-9]{64}$/.test(edition.sha256)));
});

test("road study accepts only local Kansas lines and strips properties", () => {
  const text = geojson({ type: "LineString", coordinates: [[-99, 38], [-98, 38.2]] });
  const result = study.inspectRoadStudyFile(input("1941", text));
  assert.equal(result.featureCount, 1);
  assert.equal(result.editionLabel, "1941");
  assert.deepEqual(result.data.features[0].properties, {});
  assert.throws(() => study.inspectRoadStudyFile(input("1967", text)), /usable map edition/);
  assert.throws(() => study.inspectRoadStudyFile(input("1941", geojson({ type: "Point", coordinates: [-98, 38] }))), /Only road line geometry/);
  assert.throws(() => study.inspectRoadStudyFile(input("1941", geojson({ type: "LineString", coordinates: [[-80, 38], [-79, 38]] }))), /inside the Kansas study area/);
});

test("source-bound graphic traces must match the selected map edition", () => {
  const text = JSON.stringify({
    type: "FeatureCollection",
    metadata: { source_edition: "1941", source_sha256: editions.ROAD_MAP_EDITION_BY_ID["1941"].sha256 },
    features: [{ type: "Feature", geometry: { type: "LineString", coordinates: [[-99, 38], [-98, 38.2]] }, properties: {} }],
  });
  assert.equal(study.inspectRoadStudyFile(input("1941", text)).featureCount, 1);
  assert.throws(() => study.inspectRoadStudyFile(input("1945", text)), /source edition does not match/);
  const wrongHash = text.replace(editions.ROAD_MAP_EDITION_BY_ID["1941"].sha256, "0".repeat(64));
  assert.throws(() => study.inspectRoadStudyFile(input("1941", wrongHash)), /source PDF hash does not match/);
});

test("road editions retain independent color and opacity through map updates", () => {
  const text = geojson({ type: "LineString", coordinates: [[-99, 38], [-98, 38.2]] });
  const first = study.inspectRoadStudyFile(input("1941", text));
  const second = { ...study.inspectRoadStudyFile(input("1984", text)), color: "#60d3e8", opacity: 0.35 };
  const sources = new Map();
  const layers = new Map();
  const map = {
    getStyle: () => ({ layers: [...layers.values()] }),
    getSource: (id) => sources.get(id),
    addSource: (id, source) => sources.set(id, { ...source, setData(data) { this.data = data; } }),
    removeSource: (id) => sources.delete(id),
    getLayer: (id) => layers.get(id),
    addLayer: (layer) => layers.set(layer.id, layer),
    removeLayer: (id) => layers.delete(id),
    setPaintProperty: (id, name, value) => { layers.get(id).paint[name] = value; },
    setLayoutProperty: (id, name, value) => { layers.get(id).layout[name] = value; },
  };
  study.applyRoadStudyLayers(map, [first, second]);
  assert.equal(layers.get("kfm-road-study-line-1941").paint["line-color"], "#ffbd69");
  assert.equal(layers.get("kfm-road-study-line-1984").paint["line-opacity"], 0.35);
  study.applyRoadStudyLayers(map, [{ ...second, visible: false, opacity: 0.6 }]);
  assert.equal(layers.has("kfm-road-study-line-1941"), false);
  assert.equal(sources.has("kfm-road-study-source-1941"), false);
  assert.equal(layers.get("kfm-road-study-line-1984").layout.visibility, "none");
  assert.equal(layers.get("kfm-road-study-line-1984").paint["line-opacity"], 0.6);
});
