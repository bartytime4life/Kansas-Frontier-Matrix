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

const ALLOWED_TILE_HOSTS = new Set(["mapservices.weather.noaa.gov", "edits.nationalmap.gov", "sdmdataaccess.sc.egov.usda.gov"]);
const FEEDS = ["nps-nrhp-places"];

test("discovery layers are fixed, provider-rendered, off by default and never admitted as evidence", () => {
  assert.equal(discovery.KANSAS_DISCOVERY_SOURCES.length, 4);
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
    assert.ok(discovery.discoveryLegend(source.id)?.length >= 1, `${source.id} has legend chips`);
    for (const stop of discovery.discoveryLegend(source.id)) assert.match(stop.color, /^#[0-9a-f]{6}$/);
    assert.ok(context.OFFICIAL_CONTEXT_TEMPORAL_SUPPORT[source.id], `${source.id} declares its clock`);
    assert.ok(topics.officialSourceTopics(source.id).length >= 2, `${source.id} is reachable from topics`);
    assert.match(downloads.SOURCE_DOWNLOADS[source.id].href, /^https:\/\//);
    assert.deepEqual(drawer.drawerArtifactAttributes(source.id, { anything: "x" }), []);
  }
  assert.match(context.OFFICIAL_CONTEXT_BY_ID["noaa-spc-fire-weather"].boundary, /not burn bans, red-flag warnings/);
  assert.match(context.OFFICIAL_CONTEXT_BY_ID["usgs-padus-lands"].boundary, /does not grant public access/);
  assert.equal(context.OFFICIAL_CONTEXT_TEMPORAL_SUPPORT["noaa-cpc-drought-outlook"].axis, "provider-forecast-series");
  for (const id of ["noaa-spc-convective-outlook", "noaa-mrms-qpe-24h", "noaa-wpc-qpf-5day", "mrlc-nlcd-land-cover", "nws-storm-reports"]) {
    assert.equal(context.OFFICIAL_CONTEXT_BY_ID[id], undefined, `${id} stays with its existing richer Explorer feature`);
  }
});

test("new topics reach weather, hazards, ecology, land and history without changing population topics", () => {
  const ids = topic => topics.filterOfficialSources(context.OFFICIAL_CONTEXT_SOURCES, topic, "").map(source => source.id);
  for (const id of ["noaa-spc-fire-weather", "noaa-cpc-drought-outlook"]) { assert.ok(ids("weather").includes(id), id); assert.ok(ids("disaster").includes(id), id); }
  assert.ok(ids("agriculture").includes("noaa-cpc-drought-outlook"));
  assert.ok(ids("ecology").includes("usgs-padus-lands"));
  assert.ok(ids("land").includes("usgs-padus-lands"));
  assert.ok(ids("history").includes("nps-nrhp-places"));
  assert.ok(!ids("people").includes("nps-nrhp-places"));
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
  context.applyOfficialContextState(map, visibility(ids.filter(id => id !== "noaa-cpc-drought-outlook")), opacity, {});
  assert.equal(layers.get("external-noaa-cpc-drought-outlook-raster").layout.visibility, "none");
  // One selected raster keeps the opacity chosen on its own slider.
  const single = mapHarness();
  context.applyOfficialContextState(single.map, visibility(["usgs-padus-lands"]), { ...opacity, "usgs-padus-lands": 0.81 }, {});
  assert.equal(single.layers.get("external-usgs-padus-lands-raster").paint["raster-opacity"], 0.81);
  assert.equal(single.sources.has(context.OFFICIAL_CONTEXT_BY_ID["noaa-cpc-drought-outlook"].sourceId), false);
});

test("the National Register feed draws typed places and landmark rings from its payload", () => {
  const { map, sources, layers } = mapHarness();
  const visibility = Object.fromEntries(context.OFFICIAL_CONTEXT_SOURCES.map(s => [s.id, FEEDS.includes(s.id)]));
  const opacity = Object.fromEntries(context.OFFICIAL_CONTEXT_SOURCES.map(s => [s.id, s.defaultOpacity]));
  const point = (properties) => ({ type: "Feature", geometry: { type: "Point", coordinates: [-97, 38.5] }, properties });
  const payloads = {
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
  const legend = discovery.discoveryLegend("nps-nrhp-places").map(stop => stop.color);
  const paint = JSON.stringify(layers.get("external-nps-nrhp-places-points").paint["circle-color"]);
  for (const color of legend.slice(0, 5)) assert.ok(paint.includes(color), `legend chip ${color} matches the map paint`);
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

test("unknown feeds stay rejected and an empty listing response is labeled empty", async () => {
  for (const feed of ["nps-nrhp-sensitive", "nws-storm-reports"]) {
    const unknown = await route.GET(new NextRequest(`http://127.0.0.1/api/live-context?feed=${feed}`));
    assert.equal(unknown.status, 400);
  }
  const { body } = await callFeed("nps-nrhp-places", { type: "FeatureCollection", features: [] });
  assert.equal(body.state, "empty");
  assert.equal(body.featureCount, 0);
});

test("KDWP outdoor-access feeds page the provider, keep valid Kansas polygons and never request contract identifiers", async () => {
  const square = (lon, lat) => ({ type: "Polygon", coordinates: [[[lon, lat], [lon + 0.05, lat], [lon + 0.05, lat + 0.05], [lon, lat + 0.05], [lon, lat]]] });
  const original = globalThis.fetch, seen = [];
  globalThis.fetch = async url => {
    const u = new URL(String(url)); seen.push(u);
    const offset = Number(u.searchParams.get("resultOffset"));
    const page = offset === 0
      ? { type: "FeatureCollection", exceededTransferLimit: true, features: [
        { type: "Feature", geometry: square(-97, 38), properties: { FID: 1, AREAID: 1386, ACRES: 1121.6, COUNTY: "Dickinson", ISARCHERYS: 1, NOTES: "  05s18w20 " } },
        { type: "Feature", geometry: square(-120, 45), properties: { FID: 2, AREAID: 9 } },
        { type: "Feature", geometry: { type: "Point", coordinates: [-97, 38] }, properties: { FID: 3 } } ] }
      : { type: "FeatureCollection", features: [{ type: "Feature", geometry: square(-99, 39), properties: { FID: 4, AREAID: 7, ISARCHERYS: 0 } }] };
    return new Response(JSON.stringify(page), { headers: { "Content-Type": "application/json" } });
  };
  try {
    const response = await route.GET(new NextRequest("http://127.0.0.1/api/live-context?feed=kdwp-wiha-access"));
    const body = await response.json();
    assert.equal(response.status, 200);
    assert.equal(seen.length, 2, "the provider transfer limit pages to a second request");
    assert.deepEqual(seen.map(u => u.searchParams.get("resultOffset")), ["0", "2000"]);
    for (const u of seen) {
      assert.equal(u.origin + u.pathname, "https://services1.arcgis.com/q2CglofYX6ACNEeu/arcgis/rest/services/24_25_7_29/FeatureServer/0/query");
      assert.doesNotMatch(u.searchParams.get("outFields"), /CONTRACT/i, "landowner contract identifiers are never requested");
      assert.equal(u.searchParams.get("maxAllowableOffset"), "0.0005");
    }
    assert.deepEqual(body.data.features.map(f => f.properties.featureId), ["kdwp-wiha-1", "kdwp-wiha-4"]);
    const [first, second] = body.data.features.map(f => f.properties);
    assert.equal(first.name, "WIHA tract 1386 · Dickinson County");
    assert.equal(first.acres, 1122);
    assert.equal(first.archeryOnly, "Archery only");
    assert.equal(first.notes, "05s18w20");
    assert.equal(second.archeryOnly, "Not archery-only");
    assert.equal(body.state, "partial");
    assert.match(body.limitation, /2 withheld/);
    assert.match(body.limitation, /not general public access|Not legal access/i);
  } finally { globalThis.fetch = original; }
});

test("KDWP wildlife areas keep unnamed polygons and accept only ksoutdoors links from the HTML snippet", async () => {
  const square = { type: "Polygon", coordinates: [[[-98, 38], [-97.9, 38], [-97.9, 38.1], [-98, 38.1], [-98, 38]]] };
  const { body } = await callFeed("kdwp-wildlife-areas", { type: "FeatureCollection", features: [
    { type: "Feature", geometry: square, properties: { FID: 1, NAME: "Hamilton State Fishing Lake and Wildlife Area", Label_Name: "Hamilton SFL and Wildlife Area", Hunt_Acc: "Yes", Access_Res: "No",
      Hyperlink: 'Click <a href="https://ksoutdoors.com/KDWPT-Info/Locations/Wildlife-Areas" target="_top">HERE</a> to view.' } },
    { type: "Feature", geometry: square, properties: { FID: 214, NAME: null, Label_Name: null, Hyperlink: '<a href="javascript:alert(1)">x</a>' } },
  ] });
  const [named, unnamed] = body.data.features.map(f => f.properties);
  assert.equal(named.name, "Hamilton SFL and Wildlife Area");
  assert.equal(named.recordUrl, "https://ksoutdoors.com/KDWPT-Info/Locations/Wildlife-Areas");
  assert.equal(unnamed.name, "KDWP wildlife area (unnamed in source)");
  assert.equal(unnamed.recordUrl, null);
  assert.equal(body.state, "ready");
});
