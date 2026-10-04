import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import ts from "typescript";

const modules = new Map();
async function moduleUrl(file) {
  file = path.resolve(file);
  if (modules.has(file)) return modules.get(file);
  let js = ts.transpileModule(await readFile(file, "utf8"), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
  for (const match of [...js.matchAll(/from ["'](\.[^"']+)["']/g)]) js = js.replace(match[0], `from ${JSON.stringify(await moduleUrl(path.resolve(path.dirname(file), match[1]) + ".ts"))}`);
  const url = `data:text/javascript;base64,${Buffer.from(js).toString("base64")}`;
  modules.set(file, url); return url;
}
const context = await import(await moduleUrl("app/live-context.ts"));
const workspaces = await import(await moduleUrl("app/layer-workspaces.ts"));
const { KANSAS_REFERENCE_SOURCES: references, BLM_MLRS_DIRECT_KANSAS_WHERE } = await import(await moduleUrl("app/kansas-reference-layers.ts"));

function mapHarness() {
  const sources = new Map(), layers = new Map();
  let projection = "mercator";
  const map = {
    getSource: id => sources.get(id), getLayer: id => layers.get(id), getStyle: () => ({ layers: [...layers.values()] }),
    moveLayer(id) { const layer = layers.get(id); layers.delete(id); layers.set(id, layer); },
    getProjection: () => ({ type: projection }), setProjection(value) { projection = value; },
    addSource(id, spec) { sources.set(id, { ...spec, setData(data) { this.data = data; } }); },
    addLayer(layer) { layers.set(layer.id, structuredClone(layer)); },
    getLayoutProperty: (id, key) => layers.get(id)?.layout?.[key], getPaintProperty: (id, key) => layers.get(id)?.paint?.[key],
    setLayoutProperty(id, key, value) { const layer = layers.get(id); layer.layout = { ...layer.layout, [key]: value }; },
    setPaintProperty(id, key, value) { const layer = layers.get(id); layer.paint = { ...layer.paint, [key]: value }; },
  };
  return { map, sources, layers };
}
const visibility = ids => Object.fromEntries(context.OFFICIAL_CONTEXT_SOURCES.map(s => [s.id, ids.includes(s.id)]));
const opacity = Object.fromEntries(context.OFFICIAL_CONTEXT_SOURCES.map(s => [s.id, s.defaultOpacity]));

const aquifers = await import(await moduleUrl("app/aquifer-layers.ts"));

test("aquifer layers load only when selected and keep their independent controls", () => {
  const { map, sources, layers } = mapHarness();
  const all = [...aquifers.AQUIFER_RASTER_SOURCES, ...aquifers.GROUNDWATER_SNAPSHOT_SOURCES];
  context.applyOfficialContextState(map, visibility([]), opacity, {});
  for (const source of all) assert.equal(sources.has(source.sourceId), false);
  const ids = all.map(s => s.id);
  context.applyOfficialContextState(map, visibility(ids), { ...opacity, "kgs-monitoring-wells": 0.42 }, {});
  for (const source of all) {
    assert.ok(sources.has(source.sourceId));
    assert.equal(layers.get(source.layerIds[0]).layout?.visibility ?? "visible", "visible");
  }
  assert.equal(layers.get("external-kgs-monitoring-wells-points").paint["circle-opacity"], 0.42);
  context.applyOfficialContextState(map, visibility(["kgs-water-table"]), opacity, {});
  assert.equal(layers.get("external-kgs-monitoring-wells-points").layout.visibility, "none");
  assert.deepEqual(layers.get("external-kgs-water-table-fill").filter, ["==", ["get", "hasValue"], true]);
  assert.equal(workspaces.filterOfficialSources(context.OFFICIAL_CONTEXT_SOURCES, "groundwater", "").length, 11);
  for (const source of all) assert.equal(context.officialContextVisibilityForFrame(visibility(ids), context.OFFICIAL_CONTEXT_PRESENT_FRAME - 1)[source.id], false);
});

test("snapshots preserve provider classes, missing values and bounded well links", async () => {
  for (const item of aquifers.GROUNDWATER_MANIFEST) {
    const data = JSON.parse(await readFile(`public/data/groundwater/${item.id}.geojson`, "utf8"));
    assert.equal(data.features.length, item.featureCount);
    assert.equal(data.exceededTransferLimit ?? false, false);
    for (const feature of data.features) {
      const p = feature.properties;
      if (item.id === "kgs-monitoring-wells") {
        assert.equal(feature.geometry.type, "Point");
        assert.ok(aquifers.safeKgsWellUrl(p.recordUrl));
        assert.equal(p.period, "2026 monitoring locations");
      } else {
        assert.equal(p.period, "2022–2024");
        const category = item.legend.find(x => x.value === p[item.field]);
        assert.equal(p.hasValue, Boolean(category));
        if (category) { assert.equal(p.classLabel, category.label); assert.equal(p.color, category.color); }
      }
    }
  }
  assert.equal(aquifers.safeKgsWellUrl("javascript:alert(1)"), null);
  assert.equal(aquifers.safeKgsWellUrl("https://evil.example/geohydro/wizard/wizardwelldetail.cfm?usgs_id=370012101070901"), null);
});
