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
const { KANSAS_REFERENCE_SOURCES: allReferences, BLM_MLRS_DIRECT_KANSAS_WHERE } = await import(await moduleUrl("app/kansas-reference-layers.ts"));
// Provider-drawn reference images. The five KDOT bridge layers are clustered point feeds and are checked separately below.
const references = allReferences.filter(source => source.mapUrl);
const bridgeLayers = allReferences.filter(source => source.id.startsWith("kdot-bridges-"));
const bridgeModel = await import(await moduleUrl("app/kdot-bridges.ts"));

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

test("Kansas reference overlays stay independent and do not request images while disabled", () => {
  const { map, sources, layers } = mapHarness();
  context.applyOfficialContextState(map, visibility([]), opacity, {});
  for (const source of references) assert.equal(sources.has(source.sourceId), false);
  const ids = [...references.map(s => s.id), ...workspaces.LAND_SOURCE_IDS];
  const choices = { ...opacity, "kdot-roads": 0.47, "kdot-rail-active": 0.82, "blm-plss-sections": 0.63, "blm-mlrs-leases-authorized": 0.4, "blm-mlrs-leases-closed": 0.73 };
  context.applyOfficialContextState(map, visibility(ids), choices, {});
  for (const id of ids) {
    const source = context.OFFICIAL_CONTEXT_BY_ID[id], layer = layers.get(source.layerIds[0]);
    assert.equal(layer.minzoom, source.minDisplayZoom);
    assert.equal(sources.get(source.sourceId).minzoom, source.minDisplayZoom);
    assert.deepEqual(sources.get(source.sourceId).bounds, [-102.06, 36.99, -94.58, 40.01]);
    assert.equal(layer.layout?.visibility ?? "visible", "visible");
  }
  for (const id of ["kdot-roads", "kdot-rail-active", "blm-plss-sections", "blm-mlrs-leases-authorized", "blm-mlrs-leases-closed"]) {
    assert.equal(layers.get(context.OFFICIAL_CONTEXT_BY_ID[id].layerIds[0]).paint["raster-opacity"], choices[id], "line references retain each slider instead of dimming one another");
  }
  context.applyOfficialContextState(map, visibility(ids.filter(id => id !== "kdot-roads")), choices, {});
  assert.equal(layers.get("external-kdot-roads-raster").layout.visibility, "none");
  assert.equal(layers.get("external-kdot-rail-active-raster").layout?.visibility ?? "visible", "visible");
  map.setProjection("globe");
  context.applyOfficialContextState(map, visibility(ids), choices, {});
  for (const id of ids) assert.equal(layers.get(context.OFFICIAL_CONTEXT_BY_ID[id].layerIds[0]).layout.visibility, "none");
  map.setProjection("mercator");
  context.applyOfficialContextState(map, visibility(ids), choices, {});
  assert.equal(layers.get("external-kdot-roads-raster").paint["raster-opacity"], 0.47);
  const swapped = mapHarness();
  context.applyOfficialContextState(swapped.map, visibility(ids), choices, {});
  assert.equal(swapped.layers.get("external-kdot-roads-raster").paint["raster-opacity"], 0.47, "a new basemap style restores independent source choices");
});

test("BLM, roads, rail, and hazards remain searchable through focused topics", () => {
  const all = context.OFFICIAL_CONTEXT_SOURCES;
  assert.deepEqual(workspaces.filterOfficialSources(all, "transport", "").map(s => s.id), workspaces.TRANSPORT_SOURCE_IDS);
  assert.equal(workspaces.filterOfficialSources(all, "transport", "railroad").length, 2);
  assert.equal(workspaces.filterOfficialSources(all, "land", "BLM").length, 5);
  assert.equal(workspaces.filterOfficialSources(all, "disaster", "flood").some(s => s.id === "fema-flood-zones"), true);
  assert.equal(workspaces.filterOfficialSources(all, "transport", "nonexistent").length, 0);
});

test("scale guidance never mistakes a connected source for visible detail", () => {
  for (const source of [...references, ...workspaces.LAND_SOURCE_IDS.map(id => context.OFFICIAL_CONTEXT_BY_ID[id])]) {
    const zoom = source.minDisplayZoom;
    for (const state of ["idle", "loading", "ready", "partial"]) assert.equal(workspaces.sourceNeedsCloserView(source, true, false, state, zoom - 0.1), true);
    assert.equal(workspaces.sourceNeedsCloserView(source, true, false, "ready", zoom), false);
    assert.equal(workspaces.sourceNeedsCloserView(source, true, true, "ready", 3), false);
    assert.equal(workspaces.sourceNeedsCloserView(source, false, false, "ready", 3), false);
    assert.equal(workspaces.sourceNeedsCloserView(source, true, false, "error", 3), false);
  }
});

test("reference images use fixed Kansas services; MLRS excludes generalized locations", () => {
  for (const source of references) {
    const url = new URL(source.mapUrl);
    assert.equal(url.protocol, "https:");
    assert.equal(url.searchParams.get("bboxSR"), "3857");
    assert.equal(url.searchParams.get("imageSR"), "3857");
    assert.equal(url.searchParams.get("size"), "256,256");
    assert.equal(url.searchParams.get("transparent"), "true");
    if (source.id === "fema-flood-zones") {
      assert.equal(url.hostname, "hazards.fema.gov");
      assert.deepEqual(JSON.parse(url.searchParams.get("layerDefs")), { 28: "DFIRM_ID LIKE '20%'" });
      assert.equal(url.searchParams.get("layers"), "show:28");
    } else if (source.id.startsWith("blm-mlrs-leases-")) {
      const layer = source.id.endsWith("authorized") ? 0 : 3;
      assert.equal(url.hostname, "gis.blm.gov");
      assert.equal(url.pathname, "/nlsdb/rest/services/Fluid_Minerals/Oil_Gas_Leases_Case_Disp/MapServer/export");
      assert.equal(url.searchParams.get("layers"), `show:${layer}`);
      assert.deepEqual(JSON.parse(url.searchParams.get("layerDefs")), { [layer]: BLM_MLRS_DIRECT_KANSAS_WHERE });
      assert.equal(url.searchParams.has("dynamicLayers"), false);
      assert.equal(source.minDisplayZoom, 9);
      assert.equal(source.boundary.includes("not an exact lease"), true);
    } else if (source.id.startsWith("kdot-bridges-")) {
      assert.equal(url.hostname, "kanplan.ksdot.gov");
      assert.equal(url.searchParams.has("dynamicLayers"), false);
      assert.equal(typeof JSON.parse(url.searchParams.get("layerDefs"))[0], "string");
    } else {
      assert.equal(url.hostname, "kanplan.ksdot.gov");
      const [dynamic] = JSON.parse(url.searchParams.get("dynamicLayers"));
      const id = source.id === "kdot-roads" ? 4 : ["kdot-rail-active", "kdot-roads-1918"].includes(source.id) ? 0 : 1;
      assert.equal(dynamic.source.mapLayerId, id);
      assert.equal(url.searchParams.get("layers"), `show:${id}`);
      // Only former rail is dashed: the 1918 roads differ from it by line as well as colour (map-keys.ts).
      assert.equal(dynamic.drawingInfo.renderer.symbol.style, source.id === "kdot-rail-abandoned" ? "esriSLSDash" : "esriSLSSolid");
    }
    assert.equal(source.evidenceRole, "EXTERNAL_CONTEXT_ONLY");
    assert.deepEqual(context.OFFICIAL_CONTEXT_TEMPORAL_SUPPORT[source.id].supportedFrames, [context.OFFICIAL_CONTEXT_PRESENT_FRAME]);
  }
});

test("HMS transition opacity survives ordinary layer reapplication and restores exactly", () => {
  const { map, layers } = mapHarness();
  const visible = visibility(["noaa-hms-smoke"]);
  const choices = { ...opacity, "noaa-hms-smoke": 0.38 };
  context.applyOfficialContextState(map, visible, choices, {});
  context.setHmsSmokeFade(map, 0, .38);
  context.applyOfficialContextState(map, visible, choices, {});
  const ids = context.OFFICIAL_CONTEXT_BY_ID["noaa-hms-smoke"].layerIds;
  assert.equal(layers.get(ids[0]).paint["fill-opacity"], 0);
  context.setHmsSmokeFade(map, 1, .38);
  context.applyOfficialContextState(map, visible, choices, {});
  assert.equal(layers.get(ids[0]).paint["fill-opacity"], .38);
});

test("KDOT bridges draw as numbered clusters that split into exact points, and load nothing while off", () => {
  assert.deepEqual(bridgeLayers.map(source => source.id), bridgeModel.BRIDGE_FEED_IDS);
  assert.equal(references.some(source => source.id.startsWith("kdot-bridges-")), false, "no bridge layer is a provider image any more");
  const { map, sources, layers } = mapHarness();
  context.applyOfficialContextState(map, visibility([]), opacity, {});
  for (const source of bridgeLayers) assert.equal(sources.has(source.sourceId), false, `${source.id} adds no source while off`);
  const point = (featureId, built, extra = {}) => ({ type: "Feature", geometry: { type: "Point", coordinates: [-96.5, 39.1] }, properties: { featureId, name: "Synthetic Creek", built, lengthFt: 120, ...extra } });
  const data = { type: "FeatureCollection", features: [point("kdot-local-1", 1925), point("kdot-local-2", 1988, { statusClass: "closed" })] };
  context.applyOfficialContextState(map, visibility(["kdot-bridges-local"]), opacity, { "kdot-bridges-local": { feed: "kdot-bridges-local", state: "ready", featureCount: 2, data } });
  const source = context.OFFICIAL_CONTEXT_BY_ID["kdot-bridges-local"], added = sources.get(source.sourceId);
  assert.equal(source.kind, "OPERATIONAL_GEOJSON");
  assert.equal(source.minDisplayZoom, undefined, "counted circles are readable statewide, so no closer-view hold applies");
  assert.equal(added.type, "geojson"); assert.equal(added.cluster, true); assert.equal(added.promoteId, "featureId");
  assert.equal(added.clusterMaxZoom, bridgeModel.BRIDGE_CLUSTER_MAX_ZOOM); assert.equal(added.clusterRadius, bridgeModel.BRIDGE_CLUSTER_RADIUS);
  assert.deepEqual(Object.keys(added.clusterProperties).sort(), ["builtCount", "builtSum", "closed", "earliest", "longestFt", "posted"]);
  assert.equal(added.data, data);
  const [clusters, count, points, labels] = source.layerIds.map(id => layers.get(id));
  assert.deepEqual(clusters.filter, ["has", "point_count"]); assert.deepEqual(count.filter, ["has", "point_count"]);
  assert.deepEqual(points.filter, ["!", ["has", "point_count"]]); assert.deepEqual(labels.filter, ["!", ["has", "point_count"]]);
  assert.deepEqual(count.layout["text-field"], ["get", "point_count_abbreviated"]);
  assert.equal(clusters.paint["circle-radius"][0], "step"); assert.deepEqual(clusters.paint["circle-radius"][1], ["get", "point_count"]);
  assert.equal(labels.minzoom > bridgeModel.BRIDGE_CLUSTER_MAX_ZOOM - 1, true, "names appear once bridges have split apart");
  assert.deepEqual(source.interactiveLayerIds, [source.layerIds[0], source.layerIds[2]]);
  // The map key repeats the colours the paint expression uses.
  const colors = JSON.stringify(points.paint["circle-color"]);
  for (const stop of bridgeModel.BRIDGE_ERA_STOPS) assert.equal(colors.includes(stop.color), true, stop.label);
  assert.equal(JSON.stringify(points.paint["circle-stroke-color"]).includes(bridgeModel.BRIDGE_CLOSED_COLOR), true);
  // Vector points stay visible on the globe, unlike the Mercator-only images.
  map.setProjection("globe");
  context.applyOfficialContextState(map, visibility(["kdot-bridges-local"]), opacity, {});
  assert.equal(layers.get(source.layerIds[0]).layout?.visibility ?? "visible", "visible");
});

test("a numbered bridge circle is summarised from its totals and never treated as one record", () => {
  assert.equal(bridgeModel.bridgeClusterSummary({ featureId: "kdot-local-1", name: "Synthetic Creek" }), null);
  assert.equal(bridgeModel.bridgeClusterSummary(null), null);
  assert.deepEqual(bridgeModel.bridgeClusterSummary({ cluster: true, cluster_id: 4, point_count: 1280, earliest: 1899, longestFt: 1204.4, closed: 3, posted: 22 }),
    { title: "1,280 bridges in this area", detail: "earliest recorded build year 1899 · longest 1,204 ft · 3 recorded closed · 22 posted with a restriction" });
  assert.deepEqual(bridgeModel.bridgeClusterSummary({ cluster: true, point_count: 2, earliest: 9999, longestFt: 0, closed: 0, posted: 0 }), { title: "2 bridges in this area", detail: "Select to zoom in" });
});
