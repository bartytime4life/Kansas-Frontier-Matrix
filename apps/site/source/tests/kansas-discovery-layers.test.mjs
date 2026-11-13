import "./cloudflare-register.mjs";
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { pathToFileURL } from "node:url";
import test from "node:test";
import ts from "typescript";

// Compile the real TypeScript module graph to data URLs; bare package imports
// resolve to installed files so the actual route handler runs unmodified.
const dataModule = source => `data:text/javascript;base64,${Buffer.from(source).toString("base64")}`;
// Minimal Next.js request/response surface used by route handlers, as in the other route tests.
const NEXT_SERVER = dataModule(`export class NextRequest extends Request { get nextUrl() { return new URL(this.url); } }
export const NextResponse = { json: (body, init = {}) => Response.json(body, init) };`);
const STUBS = { "next/server": NEXT_SERVER };
const modules = new Map();
async function moduleUrl(file) {
  file = path.resolve(file);
  if (modules.has(file)) return modules.get(file);
  let js = ts.transpileModule(await readFile(file, "utf8"), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
  for (const match of [...js.matchAll(/from ["']([^"']+)["']/g)]) {
    const specifier = match[1];
    let resolved;
    if (specifier.startsWith(".")) resolved = await moduleUrl(path.resolve(path.dirname(file), specifier) + ".ts");
    else if (specifier.startsWith("cloudflare:")) resolved = specifier;
    else if (STUBS[specifier]) resolved = STUBS[specifier];
    else resolved = import.meta.resolve(specifier, pathToFileURL(file).href);
    js = js.replace(match[0], `from ${JSON.stringify(resolved)}`);
  }
  const url = `data:text/javascript;base64,${Buffer.from(js).toString("base64")}`;
  modules.set(file, url); return url;
}

const context = await import(await moduleUrl("app/live-context.ts"));
const discovery = await import(await moduleUrl("app/kansas-discovery-layers.ts"));
const topics = await import(await moduleUrl("app/layer-workspaces.ts"));
const downloads = await import(await moduleUrl("app/source-downloads.ts"));
const drawer = await import(await moduleUrl("app/evidence-drawer-data.ts"));
const registry = await import(await moduleUrl("app/site-registry.ts"));
const globe = await import(await moduleUrl("app/globe-context.ts"));

const ALLOWED_TILE_HOSTS = new Set(["mapservices.weather.noaa.gov", "www.mrlc.gov", "edits.nationalmap.gov"]);
const FEEDS = ["nws-storm-reports", "nps-nrhp-places"];

test("discovery layers are fixed, provider-rendered, off by default and never admitted as evidence", () => {
  assert.equal(discovery.KANSAS_DISCOVERY_SOURCES.length, 7);
  for (const source of discovery.KANSAS_DISCOVERY_SOURCES) {
    assert.equal(context.OFFICIAL_CONTEXT_BY_ID[source.id], source);
    assert.equal(source.kind, "OPERATIONAL_WMS");
    assert.equal(source.evidenceRole, "EXTERNAL_CONTEXT_ONLY");
    assert.equal(source.defaultVisibility, false);
    assert.equal(source.interactiveLayerIds.length, 0);
    const url = new URL(source.mapUrl.replace("{bbox-epsg-3857}", "0,0,1,1"));
    assert.equal(url.protocol, "https:");
    assert.ok(ALLOWED_TILE_HOSTS.has(url.hostname), `${source.id} uses a fixed provider host`);
    assert.ok(source.mapUrl.includes("{bbox-epsg-3857}"), "tiles are requested per Mercator tile");
    assert.ok(!/\$\{|undefined/.test(source.mapUrl));
    assert.ok(source.boundary.length > 120 && source.fallback.length > 60);
    assert.match(`${source.boundary} ${source.fallback}`, /not|never/i);
    assert.ok(discovery.discoveryLegend(source.id)?.length >= 3, `${source.id} has legend chips`);
    for (const stop of discovery.discoveryLegend(source.id)) assert.match(stop.color, /^#[0-9a-f]{6}$/);
    assert.ok(context.OFFICIAL_CONTEXT_TEMPORAL_SUPPORT[source.id], `${source.id} declares its clock`);
    assert.ok(topics.officialSourceTopics(source.id).length >= 2, `${source.id} is reachable from topics`);
    assert.match(downloads.SOURCE_DOWNLOADS[source.id].href, /^https:\/\//);
    assert.deepEqual(drawer.drawerArtifactAttributes(source.id, { anything: "x" }), []);
  }
  assert.match(context.OFFICIAL_CONTEXT_BY_ID["noaa-spc-convective-outlook"].boundary, /not an observed storm, a watch, a warning/);
  assert.match(context.OFFICIAL_CONTEXT_BY_ID["noaa-mrms-qpe-24h"].mapUrl, /renderingRule=%7B%22rasterFunction%22%3A%22rft_24hr%22%7D/);
  assert.match(context.OFFICIAL_CONTEXT_BY_ID["usgs-padus-lands"].boundary, /does not grant public access/);
  assert.equal(context.OFFICIAL_CONTEXT_TEMPORAL_SUPPORT["mrlc-nlcd-land-cover"].axis, "fixed-historical-composite");
});

test("new topics stay specific: people keeps only population counts; weather, ecology and history gain the new layers", () => {
  const ids = topic => topics.filterOfficialSources(context.OFFICIAL_CONTEXT_SOURCES, topic, "").map(source => source.id);
  assert.deepEqual(ids("people"), ["census-counties"]);
  for (const id of ["noaa-spc-convective-outlook", "nws-storm-reports", "noaa-mrms-qpe-24h", "noaa-wpc-qpf-5day"]) assert.ok(ids("weather").includes(id), id);
  for (const id of ["noaa-spc-convective-outlook", "noaa-spc-fire-weather", "nws-storm-reports"]) assert.ok(ids("disaster").includes(id), id);
  for (const id of ["mrlc-nlcd-land-cover", "usgs-padus-lands"]) assert.ok(ids("ecology").includes(id), id);
  assert.ok(ids("history").includes("nps-nrhp-places"));
  assert.ok(ids("agriculture").includes("noaa-cpc-drought-outlook"));
  assert.ok(!ids("history").includes("nws-storm-reports"));
  assert.deepEqual(topics.filterOfficialSources(context.OFFICIAL_CONTEXT_SOURCES, "all", "national register").map(source => source.id), ["nps-nrhp-places"]);
  assert.deepEqual(registry.SITE_REGISTRY_VALIDATION, { ok: true, errors: [] });
  for (const id of [...discovery.DISCOVERY_LAYER_IDS, ...FEEDS]) assert.ok(discovery.NEW_LAYER_IDS.has(id));
});

function mapHarness(projection = "mercator") {
  const sources = new Map(), layers = new Map();
  const map = {
    getSource: id => sources.get(id), getLayer: id => layers.get(id), getStyle: () => ({ layers: [...layers.values()] }),
    moveLayer(id) { const layer = layers.get(id); layers.delete(id); layers.set(id, layer); },
    getProjection: () => ({ type: projection }),
    addSource(id, spec) { sources.set(id, { ...spec, setData(data) { this.data = data; } }); },
    addLayer(layer) { layers.set(layer.id, structuredClone(layer)); },
    getLayoutProperty: (id, key) => layers.get(id)?.layout?.[key], getPaintProperty: (id, key) => layers.get(id)?.paint?.[key],
    setLayoutProperty(id, key, value) { const layer = layers.get(id); layer.layout = { ...layer.layout, [key]: value }; },
    setPaintProperty(id, key, value) { const layer = layers.get(id); layer.paint = { ...layer.paint, [key]: value }; },
  };
  return { map, sources, layers };
}

test("discovery rasters request no tiles until selected, then keep independent opacity and regional bounds", () => {
  const visibility = ids => Object.fromEntries(context.OFFICIAL_CONTEXT_SOURCES.map(s => [s.id, ids.includes(s.id)]));
  const opacity = Object.fromEntries(context.OFFICIAL_CONTEXT_SOURCES.map(s => [s.id, s.defaultOpacity]));
  const { map, sources, layers } = mapHarness();
  context.applyOfficialContextState(map, visibility([]), opacity, {});
  for (const source of discovery.KANSAS_DISCOVERY_SOURCES) assert.equal(sources.has(source.sourceId), false);
  const ids = discovery.DISCOVERY_LAYER_IDS;
  context.applyOfficialContextState(map, visibility(ids), opacity, {});
  for (const id of ids) {
    const source = context.OFFICIAL_CONTEXT_BY_ID[id];
    const spec = sources.get(source.sourceId);
    assert.equal(spec.type, "raster");
    assert.deepEqual(spec.tiles, [source.mapUrl]);
    assert.equal(spec.maxzoom, source.maxNativeZoom);
    assert.equal(layers.get(source.layerIds[0]).layout?.visibility ?? "visible", "visible");
  }
  context.applyOfficialContextState(map, visibility(ids.filter(id => id !== "noaa-mrms-qpe-24h")), opacity, {});
  assert.equal(layers.get("external-noaa-mrms-qpe-24h-raster").layout.visibility, "none");
  // One selected raster keeps the opacity chosen on its own slider.
  const single = mapHarness();
  context.applyOfficialContextState(single.map, visibility(["mrlc-nlcd-land-cover"]), { ...opacity, "mrlc-nlcd-land-cover": 0.81 }, {});
  assert.equal(single.layers.get("external-mrlc-nlcd-land-cover-raster").paint["raster-opacity"], 0.81);
  assert.equal(single.sources.has(context.OFFICIAL_CONTEXT_BY_ID["noaa-mrms-qpe-24h"].sourceId), false);
});

test("point feeds draw categorized storm reports and National Register places from their payloads", () => {
  const { map, sources, layers } = mapHarness();
  const visibility = Object.fromEntries(context.OFFICIAL_CONTEXT_SOURCES.map(s => [s.id, FEEDS.includes(s.id)]));
  const opacity = Object.fromEntries(context.OFFICIAL_CONTEXT_SOURCES.map(s => [s.id, s.defaultOpacity]));
  const point = (properties) => ({ type: "Feature", geometry: { type: "Point", coordinates: [-97, 38.5] }, properties });
  const payloads = {
    "nws-storm-reports": { data: { type: "FeatureCollection", features: [point({ featureId: "lsr-1", category: "Hail", sizeRank: 2 })] } },
    "nps-nrhp-places": { data: { type: "FeatureCollection", features: [point({ featureId: "nrhp-1", name: "Test", landmark: true, resourceType: "building" })] } },
  };
  context.applyOfficialContextState(map, visibility, opacity, payloads);
  for (const id of FEEDS) {
    const source = context.OFFICIAL_CONTEXT_BY_ID[id];
    assert.equal(sources.get(source.sourceId).promoteId, "featureId");
    for (const layerId of source.layerIds) assert.ok(layers.has(layerId), layerId);
    for (const layerId of source.interactiveLayerIds) assert.ok(source.layerIds.includes(layerId));
  }
  assert.deepEqual(layers.get("external-nps-nrhp-places-halo").filter, ["==", ["get", "landmark"], true]);
  assert.equal(layers.get("external-nps-nrhp-places-labels").minzoom, 11);
  const legend = discovery.discoveryLegend("nws-storm-reports").map(stop => stop.color);
  const paint = JSON.stringify(layers.get("external-nws-storm-reports-points").paint["circle-color"]);
  for (const color of legend) assert.ok(paint.includes(color), `legend chip ${color} matches the map paint`);
});

// MapLibre accepts ["zoom"] only as the input of a top-level interpolate or step.
const containsZoom = value => Array.isArray(value) && (value.length === 1 && value[0] === "zoom" || value.some(containsZoom));
const isTopLevelZoomCurve = value => Array.isArray(value) && (value[0] === "interpolate" || value[0] === "step")
  && JSON.stringify(value[value[0] === "interpolate" ? 2 : 1]) === JSON.stringify(["zoom"]);
const hasNestedZoom = value => isTopLevelZoomCurve(value)
  ? value.slice(value[0] === "interpolate" ? 3 : 2).some(containsZoom)
  : containsZoom(value);
const CIRCLE_SIZE_PROPERTIES = ["circle-radius", "circle-stroke-width"];

test("official circle sizes stay valid zoom curves after globe overview scaling", () => {
  const visibility = Object.fromEntries(context.OFFICIAL_CONTEXT_SOURCES.map(s => [s.id, true]));
  const opacity = Object.fromEntries(context.OFFICIAL_CONTEXT_SOURCES.map(s => [s.id, s.defaultOpacity]));
  const flat = mapHarness("mercator");
  context.applyOfficialContextState(flat.map, visibility, opacity, {});
  let zoomCurves = 0;
  for (const layer of flat.layers.values()) {
    if (layer.type !== "circle") continue;
    for (const property of CIRCLE_SIZE_PROPERTIES) {
      const base = layer.paint?.[property];
      if (!containsZoom(base)) continue;
      zoomCurves += 1;
      assert.ok(isTopLevelZoomCurve(base), `${layer.id} ${property} is a top-level zoom curve`);
      const scaled = globe.globeOverviewPaintSize(base);
      assert.ok(base[3] === 4 || !hasNestedZoom(scaled), `${layer.id} ${property} starts at zoom 4 or survives globe scaling without a nested zoom`);
    }
  }
  assert.ok(zoomCurves >= 3, "the National Register zoom curves are covered");
  const round = mapHarness("globe");
  context.applyOfficialContextState(round.map, visibility, opacity, {});
  for (const layer of round.layers.values()) {
    if (layer.type !== "circle") continue;
    for (const property of CIRCLE_SIZE_PROPERTIES) assert.ok(!hasNestedZoom(layer.paint?.[property]), `${layer.id} ${property} has no nested zoom in globe view`);
  }
});

const route = await import(await moduleUrl("app/api/live-context/route.ts"));
const { NextRequest } = await import(NEXT_SERVER);
async function callFeed(feed, upstream) {
  const original = globalThis.fetch;
  const seen = [];
  globalThis.fetch = async (url) => { seen.push(String(url)); return new Response(JSON.stringify(upstream), { headers: { "Content-Type": "application/json" } }); };
  try {
    const response = await route.GET(new NextRequest(`http://127.0.0.1/api/live-context?feed=${feed}`));
    return { response, body: await response.json(), seen };
  } finally { globalThis.fetch = original; }
}
const pointFeature = (coordinates, properties) => ({ type: "Feature", geometry: { type: "Point", coordinates }, properties });

test("National Register feed keeps only listed Kansas points with safe identifiers and links", async () => {
  const { response, body, seen } = await callFeed("nps-nrhp-places", { type: "FeatureCollection", features: [
    pointFeature([-95.68, 39.05], { NRIS_Refnum: "71000325", RESNAME: "Kansas State Capitol", ResType: "building", City: "Topeka", County: "Shawnee", CertDate: "1971-09-", Is_NHL: null, NARA_URL: "https://catalog.archives.gov/id/123", STATUS: "Listed", Vicinity: "False" }),
    pointFeature([-98.2, 38.3], { NRIS_Refnum: "66000340", RESNAME: "Fort Larned", ResType: "site", City: "Larned", County: "Pawnee", CertDate: "1966-10-15", Is_NHL: "X", NARA_URL: "javascript:alert(1)", STATUS: "Listed", Vicinity: "True" }),
    pointFeature([-97.5, 38.1], { NRIS_Refnum: "80000001", RESNAME: "Demolished Mill", ResType: "building", STATUS: "Removed" }),
    pointFeature([-120, 45], { NRIS_Refnum: "80000002", RESNAME: "Out of state", ResType: "building", STATUS: "Listed" }),
    pointFeature([-97.5, 38.1], { NRIS_Refnum: "bad id!", RESNAME: "Bad", STATUS: "Listed" }),
    pointFeature([-98.21, 38.31], { NRIS_Refnum: "66000340", RESNAME: "Fort Larned", ResType: "site", City: "Larned", County: "Pawnee", Is_NHL: "X", STATUS: "Listed" }),
  ] });
  assert.equal(response.status, 200);
  assert.equal(seen.length, 1);
  const url = new URL(seen[0]);
  assert.equal(url.origin + url.pathname, "https://mapservices.nps.gov/arcgis/rest/services/cultural_resources/nrhp_locations/MapServer/0/query");
  assert.equal(url.searchParams.get("where"), "State='KANSAS'");
  assert.equal(body.feed, "nps-nrhp-places");
  assert.equal(body.state, "partial");
  assert.deepEqual(body.data.features.map(feature => feature.properties.name), ["Kansas State Capitol", "Fort Larned", "Fort Larned"]);
  assert.deepEqual(body.data.features.map(feature => feature.properties.featureId), ["nrhp-71000325", "nrhp-66000340", "nrhp-66000340-2"], "multi-point listings keep unique map identities");
  assert.match(body.limitation, /^2 listed Kansas properties shown at 3 public points \(1 flagged/);
  const [capitol, larned] = body.data.features.map(feature => feature.properties);
  assert.equal(capitol.certified, "1971-09");
  assert.equal(capitol.recordUrl, "https://catalog.archives.gov/id/123");
  assert.equal(capitol.landmark, false);
  assert.equal(larned.landmark, true);
  assert.equal(larned.landmarkLabel, "National Historic Landmark");
  assert.equal(larned.recordUrl, null, "non-NARA links are dropped");
  assert.equal(larned.vicinity, "Approximate (vicinity) location");
  assert.equal(capitol.evidenceRole, "EXTERNAL_CONTEXT_ONLY");
  assert.match(body.limitation, /1 record marked removed/);
  assert.match(body.limitation, /withholds restricted and sensitive locations/);
  assert.match(response.headers.get("Cache-Control"), /s-maxage=86400/);
});

test("storm-report feed categorizes Kansas reports, ranks magnitude and never claims an all-clear", async () => {
  const now = Date.now();
  const { response, body, seen } = await callFeed("nws-storm-reports", { type: "FeatureCollection", features: [
    pointFeature([-97.3, 37.7], { objectid: 1, wfo: "Wichita KS", lsr_validtime: now - 3_600_000, descript: "Hail", loc_desc: "2 N Wichita", magnitude: "1.75", units: "Inch", remarks: "Golf ball hail.", state: "KS" }),
    pointFeature([-99.3, 38.9], { objectid: 2, wfo: "Dodge City KS", lsr_validtime: now - 7_200_000, descript: "Tornado", loc_desc: "Hays", magnitude: null, units: null, remarks: null, state: "KS" }),
    pointFeature([-95.7, 39.0], { objectid: 3, wfo: "Topeka KS", lsr_validtime: now - 9_000_000, descript: "Tstm Wnd Gst", loc_desc: "Topeka", magnitude: "72", units: "MPH", remarks: "", state: "KS" }),
    pointFeature([-97.3, 37.7], { objectid: 4, lsr_validtime: now - 10 * 86_400_000, descript: "Snow", state: "KS" }),
    pointFeature([-93, 44], { objectid: 5, lsr_validtime: now, descript: "Hail", state: "MN" }),
  ] });
  assert.equal(response.status, 200);
  assert.equal(new URL(seen[0]).searchParams.get("where"), "state='KS'");
  assert.equal(body.feed, "nws-storm-reports");
  assert.equal(body.state, "partial");
  const reports = body.data.features.map(feature => feature.properties);
  assert.deepEqual(reports.map(report => report.category), ["Hail", "Tornado", "Wind"]);
  assert.deepEqual(reports.map(report => report.sizeRank), [3, 3, 3]);
  assert.equal(reports[0].magnitudeLabel, "1.75 Inch");
  assert.equal(reports[1].magnitudeLabel, "Not reported");
  assert.equal(reports[0].name, "Hail · 2 N Wichita");
  assert.match(body.limitation, /not an all-clear/);
  assert.equal(body.upstreamUpdatedAt, new Date(now - 3_600_000).toISOString());
});

test("unknown feeds stay rejected and an empty storm window is labeled empty, not safe", async () => {
  const unknown = await route.GET(new NextRequest("http://127.0.0.1/api/live-context?feed=nps-nrhp-sensitive"));
  assert.equal(unknown.status, 400);
  const { body } = await callFeed("nws-storm-reports", { type: "FeatureCollection", features: [] });
  assert.equal(body.state, "empty");
  assert.equal(body.featureCount, 0);
});
