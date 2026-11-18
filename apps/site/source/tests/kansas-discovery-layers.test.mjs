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
const clusters = await import(await moduleUrl("app/context-clusters.ts"));
const downloads = await import(await moduleUrl("app/source-downloads.ts"));
const drawer = await import(await moduleUrl("app/evidence-drawer-data.ts"));
const registry = await import(await moduleUrl("app/site-registry.ts"));
const globe = await import(await moduleUrl("app/globe-context.ts"));

const ALLOWED_TILE_HOSTS = new Set(["mapservices.weather.noaa.gov", "www.mrlc.gov", "edits.nationalmap.gov", "sdmdataaccess.sc.egov.usda.gov"]);
const FEEDS = ["nws-storm-reports", "nps-nrhp-places"];

test("discovery layers are fixed, provider-rendered, off by default and never admitted as evidence", () => {
  assert.equal(discovery.KANSAS_DISCOVERY_SOURCES.length, 8);
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
  // Single markers keep their styling; nearby markers are counted in a numbered circle that splits on zoom.
  const one = ["!", ["has", "point_count"]], many = ["has", "point_count"];
  assert.deepEqual(layers.get("external-nps-nrhp-places-halo").filter, ["all", one, ["==", ["get", "landmark"], true]]);
  assert.deepEqual(layers.get("external-nps-nrhp-places-points").filter, one);
  assert.deepEqual(layers.get("external-nps-nrhp-places-labels").filter, one);
  assert.equal(layers.get("external-nps-nrhp-places-labels").minzoom, 11);
  assert.deepEqual(layers.get("external-nps-nrhp-places-clusters").filter, many);
  assert.deepEqual(layers.get("external-nps-nrhp-places-cluster-count").layout["text-field"], ["get", "point_count_abbreviated"]);
  const added = sources.get(context.OFFICIAL_CONTEXT_BY_ID["nps-nrhp-places"].sourceId);
  assert.equal(added.cluster, true); assert.equal(added.clusterMaxZoom, clusters.HISTORIC_PLACE_CLUSTER_MAX_ZOOM); assert.equal(added.clusterRadius, clusters.HISTORIC_PLACE_CLUSTER_RADIUS);
  assert.deepEqual(Object.keys(added.clusterProperties).sort(), ["buildings", "districts", "landmarks", "objects", "sites", "structures"]);
  assert.deepEqual(context.OFFICIAL_CONTEXT_BY_ID["nps-nrhp-places"].interactiveLayerIds, ["external-nps-nrhp-places-clusters", "external-nps-nrhp-places-points"]);
  assert.equal(JSON.stringify(layers.get("external-nps-nrhp-places-clusters").paint["circle-stroke-color"]).includes("landmarks"), true, "a circle holding a landmark gets the light ring");
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

test("KDWP outdoor-access feeds page the provider, keep valid Kansas polygons and never request contract identifiers", async () => {
  const square = (lon, lat) => ({ type: "Polygon", coordinates: [[[lon, lat], [lon + 0.05, lat], [lon + 0.05, lat + 0.05], [lon, lat + 0.05], [lon, lat]]] });
  const original = globalThis.fetch, seen = [];
  globalThis.fetch = async url => {
    const u = new URL(String(url)); seen.push(u);
    const offset = Number(u.searchParams.get("resultOffset"));
    const page = offset === 0
      ? { type: "FeatureCollection", exceededTransferLimit: true, features: [
        { type: "Feature", geometry: square(-97, 38), properties: { FID: 1, AREAID: 1386, ACRES: 1121.6, COUNTY: "Dickinson", ISARCHERYS: 1, NOTES: "SIP payments are $10 per acre. Contract number 11004", CONTRACTID: "11004" } },
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
      assert.doesNotMatch(u.searchParams.get("outFields"), /CONTRACT|NOTES/i, "landowner contract identifiers and administrative notes are never requested");
      assert.equal(u.searchParams.get("maxAllowableOffset"), "0.0005");
    }
    assert.deepEqual(body.data.features.map(f => f.properties.featureId), ["kdwp-wiha-1", "kdwp-wiha-4"]);
    const [first, second] = body.data.features.map(f => f.properties);
    assert.equal(first.name, "WIHA tract 1386 · Dickinson County");
    assert.equal(first.acres, 1122);
    assert.equal(first.archeryOnly, "Archery only");
    assert.equal("notes" in first, false, "administrative notes never reach the public payload");
    assert.doesNotMatch(JSON.stringify(body.data), /11004|SIP payments|CONTRACTID/, "provider-side contract and payment text is dropped even if returned");
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

test("frontier trails query fixed NPS layers for public rows only, keep Kansas line parts and stay partial when a trail fails", async () => {
  const line = (...points) => points;
  const original = globalThis.fetch, seen = [];
  globalThis.fetch = async url => {
    const u = new URL(String(url)); seen.push(u);
    const service = u.pathname.split("/")[5];
    if (service === "CALI_NHT") return new Response("unavailable", { status: 503 });
    const pages = {
      SAFE_NHT: [{ type: "Feature", geometry: { type: "LineString", coordinates: line([-97.5, 38.3], [-97.4, 38.35]) }, properties: { OBJECTID: 7, TRNAME: "SANTA FE NATIONAL HISTORIC TRAIL", XYACCURACY: ">=14m" } }],
      // A national line: one part in Kansas, one far away in Wyoming.
      OREG_NHT: [{ type: "Feature", geometry: { type: "MultiLineString", coordinates: [line([-96.6, 39.7], [-96.9, 39.9]), line([-105.3, 42.55], [-105.4, 42.6])] }, properties: { OBJECTID: 2 } }],
      POEX_NHT: [{ type: "Feature", geometry: { type: "LineString", coordinates: line([-110, 41], [-111, 41.2]) }, properties: { OBJECTID: 1 } }],
      NTIR_OTHER_ChisholmGreatWesternNHTFSEA_ln: [
        { type: "Feature", geometry: { type: "LineString", coordinates: line([-97.3, 37.7], [-97.6, 38.6]) }, properties: { OBJECTID: 11, TRNAME: "CHISHOLM TRAIL - ELLSWORTH TRAIL" } },
        { type: "Feature", geometry: { type: "Point", coordinates: [-97.3, 37.7] }, properties: { OBJECTID: 12 } },
      ],
    };
    return new Response(JSON.stringify({ type: "FeatureCollection", features: pages[service] ?? [] }), { headers: { "Content-Type": "application/json" } });
  };
  try {
    const response = await route.GET(new NextRequest("http://127.0.0.1/api/live-context?feed=nps-historic-trails"));
    const body = await response.json();
    assert.equal(response.status, 200);
    assert.equal(seen.length, 5);
    for (const u of seen) {
      assert.equal(u.origin, "https://services1.arcgis.com");
      assert.match(u.pathname, /^\/fBc8EJBxQRMcHlei\/arcgis\/rest\/services\/(SAFE_NHT|OREG_NHT|CALI_NHT|POEX_NHT|NTIR_OTHER_ChisholmGreatWesternNHTFSEA_ln)\/FeatureServer\/0\/query$/);
      assert.doesNotMatch(u.searchParams.get("outFields"), /NOTES|USER|CREATOR|EDITOR|GlobalID|\*/i, "no free-text or editor fields are requested");
      if (/SAFE|Chisholm/.test(u.pathname)) assert.match(u.searchParams.get("where"), /PUBLICDISPLAY='Public Map Display' AND DATAACCESS='Unrestricted'/);
    }
    const byId = Object.fromEntries(body.data.features.map(f => [f.properties.featureId, f]));
    assert.deepEqual(Object.keys(byId).sort(), ["trail-cattle-11", "trail-oreg-2", "trail-safe-7"]);
    assert.equal(byId["trail-oreg-2"].geometry.coordinates.length, 1, "the out-of-Kansas part is dropped");
    assert.equal(byId["trail-safe-7"].properties.name, "Santa Fe National Historic Trail");
    assert.equal(byId["trail-safe-7"].properties.mapAccuracy, ">=14m");
    assert.equal(byId["trail-cattle-11"].properties.name, "Chisholm Trail - Ellsworth Trail");
    assert.match(byId["trail-cattle-11"].properties.designation, /not a designated trail/);
    assert.equal(byId["trail-cattle-11"].properties.trailGroup, "cattle");
    assert.equal(body.state, "partial");
    assert.match(body.limitation, /unavailable this time: California National Historic Trail/);
    assert.match(body.limitation, /not public access/);
  } finally { globalThis.fetch = original; }
});

test("frontier trails draw designated trails solid and study routes dashed, with legend colors matching paint", () => {
  const { map, layers } = mapHarness();
  const visibility = Object.fromEntries(context.OFFICIAL_CONTEXT_SOURCES.map(s => [s.id, s.id === "nps-historic-trails"]));
  const opacity = Object.fromEntries(context.OFFICIAL_CONTEXT_SOURCES.map(s => [s.id, s.defaultOpacity]));
  context.applyOfficialContextState(map, visibility, opacity, { "nps-historic-trails": { data: { type: "FeatureCollection", features: [] } } });
  assert.deepEqual(layers.get("external-nps-historic-trails-line").filter, ["!=", ["get", "trailGroup"], "cattle"]);
  assert.deepEqual(layers.get("external-nps-historic-trails-cattle").filter, ["==", ["get", "trailGroup"], "cattle"]);
  assert.ok(layers.get("external-nps-historic-trails-cattle").paint["line-dasharray"]);
  // Shared Oregon/California/Pony Express ruts draw side by side, casing and line together.
  const offset = layers.get("external-nps-historic-trails-line").paint["line-offset"];
  assert.deepEqual(layers.get("external-nps-historic-trails-casing").paint["line-offset"], offset);
  const offsetFor = group => { const i = offset.indexOf(group); return i < 0 ? offset.at(-1) : offset[i + 1]; };
  assert.equal(new Set(["oregon", "california", "pony-express"].map(offsetFor)).size, 3, "each shared-route trail has its own offset");
  assert.equal(offsetFor("santa-fe"), 0);
  assert.equal(layers.get("external-nps-historic-trails-labels").minzoom, 7);
  const paint = JSON.stringify(layers.get("external-nps-historic-trails-line").paint["line-color"]);
  for (const stop of discovery.discoveryLegend("nps-historic-trails")) assert.ok(paint.includes(stop.color), stop.label);
  assert.ok(discovery.NEW_LAYER_IDS.has("nps-historic-trails"));
  assert.deepEqual(topics.officialSourceTopics("nps-historic-trails"), ["history", "places", "transport"]);
});

test("trail sites keep public Kansas points, drop private sites and never request contact or editor fields", async () => {
  const pt = (x, y, properties) => ({ type: "Feature", geometry: { type: "Point", coordinates: [x, y] }, properties });
  const { response, body, seen } = await callFeed("nps-trail-places", { type: "FeatureCollection", features: [
    pt(-96.49, 38.66, { OBJECTID: 5, name: "Neosho Crossing", city: "Council Grove", county: "Morris", safe: 1, oreg: 0, certified_site: 1,
      url: "https://www.nps.gov/places/neosho-crossing.htm", histsig: "  A natural rockbed crossing on the Santa Fe Trail. ", access_: "unrestricted" }),
    pt(-101.7, 37.1, { OBJECTID: 6, name: "Davis Ruts", access_: "This half-mile stretch is on a private ranch and is not accessible to the visiting public. (620) 555-0100" }),
    pt(-98.2, 38.2, { OBJECTID: 7, name: "Old Store", access_: "Private" }),
    pt(-98.3, 38.3, { OBJECTID: 11, name: "Closed House", access_: "Access is restricted." }),
    pt(-96.7, 39.0, { OBJECTID: 8, name: "Unlinked Site", url: "javascript:alert(1)", cali: 1, poex: 1 }),
    pt(-94.8, 37.1, { OBJECTID: 12, name: "Route 66 Station" }),
    pt(-120, 45, { OBJECTID: 9, name: "Far Away", safe: 1 }),
    pt(-97, 38, { OBJECTID: 10, name: "", safe: 1 }),
  ] });
  assert.equal(response.status, 200);
  const u = new URL(seen[0]);
  assert.equal(u.origin + u.pathname, "https://services1.arcgis.com/fBc8EJBxQRMcHlei/arcgis/rest/services/SAFE_SantaFeNHTPointsofInterest_pt/FeatureServer/0/query");
  assert.doesNotMatch(u.searchParams.get("outFields"), /telephone|email|address|Notes|user|GlobalID|\*/i, "contact, notes and editor fields are never requested");
  assert.deepEqual(body.data.features.map(f => f.properties.featureId), ["trail-place-5", "trail-place-8"]);
  const [crossing, unlinked] = body.data.features.map(f => f.properties);
  assert.equal(crossing.place, "Council Grove, Morris County");
  assert.equal(crossing.trails, "Santa Fe");
  assert.equal(crossing.certified, "NPS-certified trail site");
  assert.equal(crossing.history, "A natural rockbed crossing on the Santa Fe Trail.");
  assert.equal(crossing.recordUrl, "https://www.nps.gov/places/neosho-crossing.htm");
  assert.equal(unlinked.recordUrl, null);
  assert.equal(unlinked.trails, "California, Pony Express");
  assert.doesNotMatch(JSON.stringify(body), /access_|620\) 555|Davis Ruts|Old Store|Closed House/, "private sites and the access field are not published");
  assert.match(body.limitation, /3 sites NPS describes as private or not open to visitors are left out/);
  assert.match(body.limitation, /1 on other corridors are not shown/);
  assert.doesNotMatch(JSON.stringify(body.data), /Route 66/);
  assert.equal(body.state, "partial");
});

test("every official source has exactly one catalog category, and the download route serves exactly the on-site downloads", async () => {
  const categories = new Set(["Reference boundaries & locators", "Hydrology & water", "Geology & landforms", "Habitat, fauna & flora", "Agriculture", "Weather & hazards", "Fire, smoke & hazards", "People & DNA", "Roads, rail & movement", "Settlements & cities", "Historical geography", "Public-safe planning", "Review & diagnostics"]);
  const ids = context.OFFICIAL_CONTEXT_SOURCES.map(source => source.id).sort();
  assert.deepEqual(Object.keys(topics.OFFICIAL_SOURCE_CATEGORY).sort(), ids);
  for (const [id, category] of Object.entries(topics.OFFICIAL_SOURCE_CATEGORY)) assert.ok(categories.has(category), `${id}: ${category}`);
  // Sources that an old if-chain sent to "Weather & hazards" by default.
  assert.equal(topics.OFFICIAL_SOURCE_CATEGORY["kdot-roads"], "Roads, rail & movement");
  assert.equal(topics.OFFICIAL_SOURCE_CATEGORY["blm-plss-sections"], "Reference boundaries & locators");
  assert.equal(topics.OFFICIAL_SOURCE_CATEGORY["usgs-3dep-slope"], "Geology & landforms");
  assert.equal(topics.OFFICIAL_SOURCE_CATEGORY["kgs-aquifer-dakota"], "Hydrology & water");
  assert.equal(topics.OFFICIAL_SOURCE_CATEGORY["nasa-gibs-fire-points"], "Fire, smoke & hazards");
  assert.equal(topics.OFFICIAL_SOURCE_CATEGORY["nrcs-ssurgo-soils"], "Agriculture");
  assert.match(await readFile("app/page.tsx", "utf8"), /category: OFFICIAL_SOURCE_CATEGORY\[officialSource\.id\],/);

  const download = await import(await moduleUrl("app/api/source-download/route.ts"));
  const onSite = Object.entries(downloads.SOURCE_DOWNLOADS).filter(([, { href }]) => href.startsWith("/api/source-download?")).map(([id]) => id);
  assert.ok(onSite.length >= 14 && onSite.includes("nps-trail-places") && onSite.includes("nws-storm-reports"));
  const original = globalThis.fetch;
  globalThis.fetch = async () => { throw new Error("provider unavailable in test"); };
  try {
    for (const id of onSite) {
      assert.equal(downloads.SOURCE_DOWNLOADS[id].href, `/api/source-download?source=${id}`);
      const response = await download.GET(new Request(`http://127.0.0.1/api/source-download?source=${id}`));
      assert.notEqual(response.status, 400, id);
    }
    for (const id of [...ids.filter(id => !onSite.includes(id)), "not-a-source", ""]) {
      const response = await download.GET(new Request(`http://127.0.0.1/api/source-download?source=${encodeURIComponent(id)}`));
      assert.equal(response.status, 400, id);
    }
  } finally { globalThis.fetch = original; }
});

test("a numbered circle is summarised for its own source and is never read as one record", () => {
  const cluster = { cluster: true, cluster_id: 9, point_count: 128, landmarks: 2, buildings: 90, districts: 20, structures: 10, sites: 5, objects: 1 };
  assert.deepEqual(clusters.officialClusterSummary("nps-nrhp-places", cluster), { title: "128 National Register markers in this area",
    detail: "2 National Historic Landmarks · 90 buildings · 20 districts · 5 sites · 10 structures · 1 object" });
  assert.deepEqual(clusters.officialClusterSummary("nps-nrhp-places", { cluster: true, point_count: 2 }), { title: "2 National Register markers in this area", detail: "Select to zoom in" });
  assert.equal(clusters.officialClusterSummary("nps-nrhp-places", { featureId: "nrhp-1", name: "Test", landmark: true }), null, "one marker is a record, not a count");
  // Bridges keep their own wording, and a source without clusters is never summarised.
  assert.match(clusters.officialClusterSummary("kdot-bridges-local", { cluster: true, point_count: 40, earliest: 1920, longestFt: 300, closed: 1, posted: 2 }).title, /^40 bridges in this area$/);
  assert.equal(clusters.officialClusterSummary("usgs-earthquakes", cluster), null);
  assert.equal(clusters.officialClusterSummary(undefined, cluster), null);
});

test("KDWP layers carry NEW markers and legend chips that share the map paint colours; NEW markers expire", async () => {
  const { readFile: read } = await import("node:fs/promises");
  const ts = (await import("typescript")).default;
  const source = ts.transpileModule(await read("app/kansas-discovery-layers.ts", "utf8"), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText
    .replace(/from "\.\/kdot-bridges"/, `from ${JSON.stringify("data:text/javascript;base64," + Buffer.from(ts.transpileModule(await read("app/kdot-bridges.ts", "utf8"), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText).toString("base64"))}`);
  const layers = await import(`data:text/javascript;base64,${Buffer.from(source).toString("base64")}`);
  for (const id of ["kdwp-wildlife-areas", "kdwp-wiha-access"]) {
    assert.ok(layers.NEW_LAYER_IDS.has(id));
    assert.deepEqual(layers.discoveryLegend(id).map(stop => stop.color), [layers.KDWP_AREA_COLORS[id].fill]);
  }
  assert.equal(layers.isNewLayer("kdwp-wiha-access", Date.parse("2026-11-18T00:00:00Z")), true);
  assert.equal(layers.isNewLayer("kdwp-wiha-access", Date.parse("2027-01-01T00:00:00Z")), false);
  assert.equal(layers.isNewLayer("census-counties", Date.parse("2026-11-18T00:00:00Z")), false);
  const context = await read("app/live-context.ts", "utf8");
  assert.doesNotMatch(context, /\["kdwp-wildlife-areas", "#7fbf6a"/, "map paint reads the shared KDWP colours");
  assert.match(context, /const \{ fill: color, line \} = KDWP_AREA_COLORS\[id\];/);
  const page = await read("app/page.tsx", "utf8");
  assert.match(page, /isNewLayer\(source\.id\) && <> <span className="new-layer-badge" aria-hidden="true"/);
  assert.match(page, /aria-label=\{`Show \$\{source\.title\}`\}/);
  assert.match(page, /const goesSelected = Boolean\(officialVisibility\["noaa-goes-geocolor"\]\);/);
  assert.match(page, /\}, \[buildYearCurrent, goesSelected, refreshNoaaSatelliteFrames, temporalQuery\.frame\]\);/);
});

test("KDWP keeps completed pages when the shared budget shortens a later page, and still fails on other errors", async () => {
  const square = (lon, lat) => ({ type: "Polygon", coordinates: [[[lon, lat], [lon + 0.05, lat], [lon + 0.05, lat + 0.05], [lon, lat + 0.05], [lon, lat]]] });
  const firstPage = { type: "FeatureCollection", exceededTransferLimit: true, features: [
    { type: "Feature", geometry: square(-98, 38), properties: { FID: 1, NAME: "Cheyenne Bottoms Wildlife Area" } }] };
  const realNow = Date.now, realSetTimeout = globalThis.setTimeout, originalFetch = globalThis.fetch;
  const run = async (laterPage, { slowFirstPage = false } = {}) => {
    let clock = realNow();
    Date.now = () => clock;
    // Compress timers so a provider timeout costs milliseconds; abort timing keeps its order.
    globalThis.setTimeout = (fn, ms, ...args) => realSetTimeout(fn, Math.min(ms ?? 0, 50) / 10, ...args);
    const hang = signal => new Promise((_, reject) => signal.addEventListener("abort", () => reject(Object.assign(new Error("aborted"), { name: "AbortError" })), { once: true }));
    globalThis.fetch = async (url, init) => {
      const offset = Number(new URL(String(url)).searchParams.get("resultOffset"));
      if (offset === 0) {
        if (slowFirstPage) return hang(init.signal);
        clock += 18_000; // the first page used 18 s of the 25 s budget
        return new Response(JSON.stringify(firstPage), { headers: { "Content-Type": "application/json" } });
      }
      return laterPage(init.signal, hang);
    };
    try {
      const response = await route.GET(new NextRequest("http://127.0.0.1/api/live-context?feed=kdwp-wildlife-areas"));
      return { response, body: await response.json() };
    } finally {
      Date.now = realNow; globalThis.setTimeout = realSetTimeout; globalThis.fetch = originalFetch;
    }
  };

  const shortened = await run((signal, hang) => hang(signal));
  assert.equal(shortened.response.status, 200, "a budget-shortened later page does not discard completed pages");
  assert.equal(shortened.body.state, "partial");
  assert.equal(shortened.body.truncated, true);
  assert.deepEqual(shortened.body.data.features.map(f => f.properties.featureId), ["kdwp-area-1"]);
  assert.match(shortened.body.limitation, /capped/);

  const upstreamError = await run(async () => new Response("unavailable", { status: 500 }));
  assert.equal(upstreamError.response.status, 503, "a non-timeout upstream error on a later page still fails the feed");

  const firstPageTimeout = await run(async () => { throw new Error("unreachable"); }, { slowFirstPage: true });
  assert.equal(firstPageTimeout.response.status, 503, "a first-page timeout still fails the feed");
});

test("the selected bridge record read is size-bounded and abortable", async () => {
  const { readFile: read } = await import("node:fs/promises");
  const page = await read("app/page.tsx", "utf8");
  assert.match(page, /fetch\(`\/api\/bridge-detail\?id=\$\{encodeURIComponent\(selectedBridgeId\)\}`[\s\S]{0,400}readBoundedJson\(response, 256 \* 1024, controller\.signal\)/);
  assert.doesNotMatch(await read("app/api/live-context/route.ts", "utf8"), /fetchBoundedJsonArray/, "the unused array reader is removed");
});

test("trail sites are counted in numbered circles that split on zoom, and single sites keep their marker and label", () => {
  const id = "nps-trail-places", source = context.OFFICIAL_CONTEXT_BY_ID[id];
  const { map, sources, layers } = mapHarness();
  const visibility = Object.fromEntries(context.OFFICIAL_CONTEXT_SOURCES.map(item => [item.id, false]));
  const opacity = Object.fromEntries(context.OFFICIAL_CONTEXT_SOURCES.map(item => [item.id, item.defaultOpacity]));
  const data = { type: "FeatureCollection", features: [pointFeature([-97, 38], { featureId: "trail-place-42", name: "Synthetic crossing" })] };
  context.applyOfficialContextState(map, { ...visibility, [id]: true }, { ...opacity, [id]: 0.6 }, { [id]: { data } });
  assert.deepEqual(source.layerIds, ["external-nps-trail-places-points", "external-nps-trail-places-labels", "external-nps-trail-places-clusters", "external-nps-trail-places-cluster-count"]);
  assert.deepEqual(source.interactiveLayerIds, ["external-nps-trail-places-clusters", "external-nps-trail-places-points"]);
  const one = ["!", ["has", "point_count"]], many = ["has", "point_count"], added = sources.get(source.sourceId);
  assert.equal(added.cluster, true); assert.equal(added.clusterMaxZoom, clusters.TRAIL_PLACE_CLUSTER_MAX_ZOOM); assert.equal(added.clusterRadius, clusters.TRAIL_PLACE_CLUSTER_RADIUS);
  assert.deepEqual(Object.keys(added.clusterProperties).sort(), ["california", "certified", "oregon", "ponyExpress", "santaFe"]);
  assert.deepEqual(layers.get(source.layerIds[0]).filter, one); assert.deepEqual(layers.get(source.layerIds[1]).filter, one);
  assert.equal(layers.get(source.layerIds[1]).minzoom, 8);
  assert.deepEqual(layers.get(source.layerIds[2]).filter, many); assert.equal(layers.get(source.layerIds[2]).type, "circle");
  assert.deepEqual(layers.get(source.layerIds[3]).layout["text-field"], ["get", "point_count_abbreviated"]);
  assert.match(source.legend, /^Numbered circles count sites and split as you zoom in\./);
});

test("a trail-site circle says how many sites it holds, how many are certified and which trails they are on", () => {
  const cluster = { cluster: true, cluster_id: 4, point_count: 31, certified: 18, santaFe: 22, oregon: 14, california: 14, ponyExpress: 0 };
  assert.deepEqual(clusters.officialClusterSummary("nps-trail-places", cluster), { title: "31 trail sites in this area",
    detail: "18 NPS-certified · Santa Fe 22 · Oregon 14 · California 14" });
  assert.deepEqual(clusters.officialClusterSummary("nps-trail-places", { cluster: true, point_count: 2 }), { title: "2 trail sites in this area", detail: "Select to zoom in" });
  assert.equal(clusters.officialClusterSummary("nps-trail-places", { featureId: "trail-place-1", name: "Council Grove", trails: "Santa Fe" }), null, "one site is a record, not a count");
  // The totals are counted from each site's own fields: a site on a shared corridor counts toward every trail it names.
  const totals = clusters.TRAIL_PLACE_CLUSTER_PROPERTIES;
  assert.deepEqual(totals.certified, ["+", ["case", ["==", ["get", "certified"], "NPS-certified trail site"], 1, 0]]);
  assert.deepEqual(totals.ponyExpress, ["+", ["case", ["in", "Pony Express", ["to-string", ["coalesce", ["get", "trails"], ""]]], 1, 0]]);
});
