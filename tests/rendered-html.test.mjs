import assert from "node:assert/strict";
import "./cloudflare-register.mjs";
import { readFile } from "node:fs/promises";
import test from "node:test";

test("renders the map-first Kansas explorer shell", async () => {
  const workerUrl = new URL("../dist/server/index.js", import.meta.url);
  workerUrl.searchParams.set("test", `${process.pid}-${Date.now()}`);
  const { default: worker } = await import(workerUrl.href);

  const response = await worker.fetch(
    new Request("http://localhost/", {
      headers: { accept: "text/html" },
    }),
    {
      ASSETS: {
        fetch: async () => new Response("Not found", { status: 404 }),
      },
    },
    {
      waitUntil() {},
      passThroughOnException() {},
    },
  );

  assert.equal(response.status, 200);
  assert.match(
    response.headers.get("content-type") ?? "",
    /^text\/html\b/i,
  );
  const html = await response.text();
  assert.match(html, /Kansas Frontier Matrix Explorer/i);
  assert.match(html, /Layer Catalog/i);
  assert.match(html, /MapLibre/i);
  assert.match(html, /Build report/i);
  assert.match(html, /bounded demonstration data/i);
  assert.match(html, /Repository briefing/i);
  assert.match(html, /main@(?:<!-- -->)?b44494c/i);
  assert.match(html, /Scenario review/i);
  assert.match(html, /Runtime lab/i);
  assert.match(html, /Source observatory/i);
  assert.match(html, /Transition inspector/i);
  assert.match(html, /Readiness gates/i);
  assert.match(html, /county inventory is useful but snapshot-sensitive/i);
});

test("centers the primary workflow on map-scoped custom reports", async () => {
  const source = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
  const mapInterface = await readFile(new URL("../app/map-interface.ts", import.meta.url), "utf8");
  const about = await readFile(new URL("../app/about/page.tsx", import.meta.url), "utf8");
  const css = await readFile(new URL("../app/globals.css", import.meta.url), "utf8");

  assert.match(mapInterface, /"report"/);
  assert.match(source, /kfm-custom-map-report-v1/);
  assert.match(source, /Custom report builder/);
  assert.match(source, /Build from the map you are using/);
  assert.match(source, /Map extent/);
  assert.match(source, /Visible layers/);
  assert.match(source, /Report \.html/);
  assert.match(source, /Data \.json/);
  assert.match(source, /setReportLayerIds\(activeLayers\.map/);
  assert.match(source, /const \[leftOpen, setLeftOpen\] = useState\(false\)/);
  assert.match(source, /const \[leftPanelMode, setLeftPanelMode\] = useState<LeftPanelMode>\("layers"\)/);
  assert.match(source, /const KANSAS_VIEW: ViewState = \{ center: \[-98\.38, 38\.48\], zoom: 5\.45, bearing: 0, pitch: 0 \}/);
  assert.match(source, /const \[scenePreset, setScenePreset\] = useState<ScenePresetId>\("overview-2d"\)/);
  assert.match(source, /restoredScene[^\n]+\? restoredScene : "overview-2d"/);
  assert.match(source, /const defaultReportLayerIds = LAYER_REGISTRY\.filter\(\(layer\) => defaultVisibility\[layer\.id\]\)/);
  assert.match(mapInterface, /id: "overview"[\s\S]+transport-context/);
  assert.match(about, /Start with a question, finish with a report/);
  assert.match(about, /EVIDENCE STATES/);
  assert.match(css, /\.report-builder-grid/);
  assert.match(css, /\.about-page/);
});

test("adds reusable analysis recipes, device-local workspaces, report filters, and richer fixtures", async () => {
  const ts = await import("typescript");
  const recipeSource = await readFile(new URL("../app/analysis-recipes.ts", import.meta.url), "utf8");
  const explorerSource = await readFile(new URL("../app/explorer-data.ts", import.meta.url), "utf8");
  const page = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
  const css = await readFile(new URL("../app/globals.css", import.meta.url), "utf8");
  const compile = (source, fileName) => ts.transpileModule(source, {
    compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
    fileName,
  }).outputText;
  const recipes = await import(`data:text/javascript;base64,${Buffer.from(compile(recipeSource, "analysis-recipes.ts")).toString("base64")}`);
  const explorer = await import(`data:text/javascript;base64,${Buffer.from(compile(explorerSource, "explorer-data.ts")).toString("base64")}`);
  const layer = (id) => explorer.LAYER_REGISTRY.find((candidate) => candidate.id === id);

  assert.equal(recipes.ANALYSIS_RECIPES.length, 11);
  assert.equal(recipes.ANALYSIS_RECIPES.every((recipe) => recipe.layerIds.every((id) => id === "county-starter-points" || Boolean(layer(id)))), true);
  assert.equal(layer("water-context").data.features.length, 4);
  assert.equal(layer("agriculture-context").data.features.length, 3);
  assert.equal(layer("communities").data.features.length, 12);
  assert.equal(layer("transport-context").data.features.length, 3);
  assert.equal(["kansas-extent", "water-context", "watershed-context", "prairie-context", "atmosphere-observations", "communities", "transport-context"].every((id) => layer(id).defaultVisibility), true);
  assert.match(page, /kfm-map-workspaces-v1/);
  assert.match(page, /saveCurrentWorkspace/);
  assert.match(page, /loadSavedWorkspace/);
  assert.match(page, /reportEvidenceFilter/);
  assert.match(page, /handleWorkspaceShortcut/);
  assert.match(page, /shortcut R/);
  assert.match(css, /\.analysis-recipes/);
  assert.match(css, /\.saved-workspace-list/);
  assert.match(css, /\.report-active-filters/);
});

test("adds bounded smoke, water, elevation, tile, and scene navigation features", async () => {
  const ts = await import("typescript");
  const explorerSource = await readFile(new URL("../app/explorer-data.ts", import.meta.url), "utf8");
  const page = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
  const runtime = await readFile(new URL("../app/map-runtime.ts", import.meta.url), "utf8");
  const mapInterface = await readFile(new URL("../app/map-interface.ts", import.meta.url), "utf8");
  const css = await readFile(new URL("../app/globals.css", import.meta.url), "utf8");
  const compiled = ts.transpileModule(explorerSource, {
    compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
    fileName: "explorer-data.ts",
  }).outputText;
  const explorer = await import(`data:text/javascript;base64,${Buffer.from(compiled).toString("base64")}`);
  const layer = (id) => explorer.LAYER_REGISTRY.find((candidate) => candidate.id === id);

  assert.equal(explorer.LAYER_REGISTRY.length, 21);
  assert.equal(layer("watershed-context").data.features.length, 3);
  assert.equal(layer("smoke-context").data.features.length, 3);
  assert.equal(layer("elevation-concept").data.features.length, 6);
  assert.equal(layer("tile-matrix-grid").data.features.length, 24);
  assert.equal(layer("water-context").sourceOptions.lineMetrics, true);
  assert.match(explorerSource, /"line-gradient"/);
  assert.match(explorerSource, /type: "fill-extrusion"/);
  assert.match(explorerSource, /not observed smoke, a forecast, an advisory/i);
  assert.match(explorerSource, /not a fetched vector tile, PMTiles archive/i);
  assert.match(runtime, /setElevationExaggeration/);
  assert.match(runtime, /type: "color-relief"/);
  assert.match(runtime, /"color-relief-color"/);
  assert.match(runtime, /applySceneEnvironment/);
  assert.match(runtime, /setSky/);
  assert.match(runtime, /setLight/);
  assert.match(runtime, /lngLatToTile/);
  assert.match(page, /MAP REPRESENTATION/);
  assert.match(page, /Verified renderer controls/);
  assert.match(page, /HMS smoke · Shake stations · hazard overlays/);
  assert.match(page, /setVerticalFieldOfView/);
  assert.match(page, /Started a reversible 90° MapLibre camera orbit/);
  assert.match(page, /External DEM; not KFM evidence/);
  assert.match(page, /new maplibregl\.NavigationControl/);
  assert.match(page, /new maplibregl\.FullscreenControl/);
  assert.match(page, /aria-label="Unified map controls"/);
  assert.match(page, /SOURCE CONNECTIONS/);
  assert.match(page, /querySourceFeatures/);
  assert.match(page, /params\.set\("scene"/);
  assert.match(page, /params\.set\("zscale"/);
  assert.match(page, /params\.set\("sky"/);
  assert.match(page, /params\.set\("fov"/);
  assert.match(mapInterface, /Terrain \+ hillshade[\s\S]*CONTEXT ONLY/);
  assert.match(page, /3D SOURCE LEDGER/);
  assert.match(page, /TERRAIN INVESTIGATION/);
  assert.match(page, /queryTerrainElevation\(coordinate, \{ exaggerated: false \}\)/);
  assert.match(page, /Renderer preview only—not analytical elevation or report evidence/);
  assert.match(css, /\.terrain-profile-preview/);
  assert.match(page, /TERRAIN SCENE PASSPORT/);
  assert.match(page, /TOPOGRAPHIC HEIGHT/);
  assert.match(page, /PRIORITY_CONTEXT_GROUPS/);
  assert.match(page, /Provider heights only/);
  assert.match(page, /role="switch" aria-checked=\{structures3DEnabled\}/);
  assert.match(page, /Earthquakes, water \+ smoke/);
  assert.match(page, /setPriorityContextGroupVisible/);
  assert.match(page, /priority-context-source/);
  assert.match(css, /\.priority-context-deck/);
  assert.match(css, /\.priority-context-source-list/);
  assert.match(page, /Hide controls/);
  assert.match(page, /Lock for report/);
  assert.match(page, /queryTerrainElevation\(\[event\.lngLat\.lng, event\.lngLat\.lat\], \{ exaggerated: false \}\)/);
  assert.match(page, /colorRampMeters/);
  assert.match(page, /Vertical datum, analytical spacing, and KFM source admission are not asserted/);
  assert.match(css, /\.terrain-scene-passport/);
  assert.match(css, /\.scene-structures-control/);
  assert.match(page, /STRUCTURE_3D_SOURCE/);
  assert.match(runtime, /ACTIVE_TERRAIN_SOURCE/);
  assert.match(runtime, /LIBERTY_STRUCTURES_3D_LAYER_ID = "building-3d"/);
  assert.match(runtime, /layer\?\.type !== "fill-extrusion"/);
  assert.match(runtime, /neither duplicates the layer nor invents a client-side height/);
  assert.match(mapInterface, /Offline \/ PMTiles[\s\S]*HOLD/);
  assert.match(css, /\.scene-preset-grid/);
  assert.match(css, /\.renderer-capability-list/);
  assert.match(css, /\.source-connection-card/);
});

test("keeps representation switching atomic across 2D, terrain, and globe", async () => {
  const source = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
  assert.match(source, /map\?\.stop\(\)/);
  assert.match(source, /scenePresetRef\.current = nextScenePreset/);
  assert.match(source, /setTerrainPresentation\(map, false, 1\)[\s\S]+map\.setProjection[\s\S]+setTerrainPresentation\(map, true, 1\)/);
  assert.match(source, /map\.triggerRepaint\(\)/);
});

test("adds governed living systems, hazards, people, transport, settlement, and dynamic MapLibre layers", async () => {
  const ts = await import("typescript");
  const explorerSource = await readFile(new URL("../app/explorer-data.ts", import.meta.url), "utf8");
  const runtime = await readFile(new URL("../app/map-runtime.ts", import.meta.url), "utf8");
  const mapInterface = await readFile(new URL("../app/map-interface.ts", import.meta.url), "utf8");
  const page = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
  const about = await readFile(new URL("../app/about/page.tsx", import.meta.url), "utf8");
  const compiled = ts.transpileModule(explorerSource, {
    compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
    fileName: "explorer-data.ts",
  }).outputText;
  const explorer = await import(`data:text/javascript;base64,${Buffer.from(compiled).toString("base64")}`);
  const layer = (id) => explorer.LAYER_REGISTRY.find((candidate) => candidate.id === id);
  const requiredLayers = [
    "water-context", "smoke-context", "fire-context", "habitat-connectivity",
    "fauna-range-context", "flora-communities", "people-dna-context",
    "hazards-context", "transport-context", "communities",
  ];

  assert.deepEqual(requiredLayers.filter((id) => !layer(id)), []);
  assert.equal(layer("fire-context").data.features.length, 3);
  assert.equal(layer("hazards-context").data.features.length, 3);
  assert.equal(layer("habitat-connectivity").data.features.length, 3);
  assert.equal(layer("fauna-range-context").data.features.length, 2);
  assert.equal(layer("flora-communities").data.features.length, 3);
  assert.equal(layer("people-dna-context").data.features.length, 3);
  assert.equal(layer("people-dna-context").publicStatus, "RESTRICTED");
  assert.equal(layer("people-dna-context").releaseState, "RESTRICTED");
  assert.deepEqual(layer("fire-context").temporal.years, [2022, 2024, 2026]);
  assert.deepEqual(new Set(layer("transport-context").data.features.map((feature) => feature.properties.transportMode)), new Set(["ROAD", "RAIL"]));
  assert.deepEqual(new Set(layer("communities").data.features.map((feature) => feature.properties.settlementClass)), new Set(["METRO", "REGIONAL", "LOCAL"]));
  assert.equal(explorer.LAYER_REGISTRY.flatMap((record) => record.data.features).every((feature) => feature.id === feature.properties.fid), true);
  assert.equal(new Set(explorer.LAYER_REGISTRY.map((record) => record.sourceId)).size, explorer.LAYER_REGISTRY.length);
  assert.match(explorerSource, /No species occurrence, population, nest, migration track/i);
  assert.match(explorerSource, /Contains no individual, household, tribal affiliation/i);
  assert.match(explorerSource, /Not an active fire, ignition, burn severity product/i);
  assert.match(runtime, /applyDynamicMapEffects/);
  assert.match(runtime, /water-context-flow/);
  assert.match(runtime, /transport-context-rail/);
  assert.doesNotMatch(page, /<strong id="scene-motion-title">Dynamic map effects/);
  assert.match(page, /prefers-reduced-motion: reduce/);
  assert.match(page, /requestAnimationFrame\(renderEffects\)/);
  assert.match(mapInterface, /Habitat \+ living systems/);
  assert.match(mapInterface, /People, movement \+ places/);
  assert.match(about, /Broad relationships, bounded claims/);
});

test("makes the Explorer faster to compose, filter, and investigate across domains", async () => {
  const page = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
  const runtime = await readFile(new URL("../app/map-runtime.ts", import.meta.url), "utf8");
  const about = await readFile(new URL("../app/about/page.tsx", import.meta.url), "utf8");
  const css = await readFile(new URL("../app/globals.css", import.meta.url), "utf8");

  assert.match(page, /Quick lenses/);
  assert.match(page, /All layer domains/);
  assert.match(page, /Reset defaults/);
  assert.match(page, /catalogCategorySlug/);
  assert.match(page, /MAP_VIEW_PROFILES\.map/);
  assert.match(page, /Map evidence filter/);
  assert.match(page, /mapCompatibleFeatureCount/);
  assert.match(page, /params\.set\("ef", mapEvidenceFilter\)/);
  assert.match(page, /mapEvidenceFilter\?: RegistryEvidenceFilter/);
  assert.match(page, /mapEvidenceState: mapEvidenceFilter/);
  assert.match(page, /Nearby context/);
  assert.match(page, /anchorDistanceMiles/);
  assert.match(page, /showNearbyContextLayers/);
  assert.match(page, /fitNearbyContext/);
  assert.match(page, /Distances use generalized feature anchors/);
  assert.match(runtime, /RegistryEvidenceFilter/);
  assert.match(runtime, /evidenceFilterForRecord/);
  assert.match(runtime, /map\.setFilter\(renderer\.id, filter \?\? null\)/);
  assert.match(about, /discover nearby cross-domain records/i);
  assert.match(css, /\.catalog-quick-lenses/);
  assert.match(css, /\.catalog-domain-index/);
  assert.match(css, /catalog-groups \{ flex: none/);
  assert.match(css, /\.catalog-evidence-filter/);
  assert.match(css, /\.nearby-context-card/);
});

test("adds a MapLibre area-of-interest workflow and browser-local camera history", async () => {
  const page = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
  const runtime = await readFile(new URL("../app/map-runtime.ts", import.meta.url), "utf8");
  const mapInterface = await readFile(new URL("../app/map-interface.ts", import.meta.url), "utf8");
  const css = await readFile(new URL("../app/globals.css", import.meta.url), "utf8");

  assert.match(runtime, /kfm-analysis-area/);
  assert.match(runtime, /buildAnalysisAreaData/);
  assert.match(runtime, /updateAnalysisAreaSource/);
  assert.match(page, /"ANALYSIS_AREA"/);
  assert.match(page, /captureAnalysisArea/);
  assert.match(page, /Locked the current MapLibre viewport as the report area of interest/);
  assert.match(page, /params\.set\("aoi"/);
  assert.match(page, /cameraHistoryRef/);
  assert.match(page, /travelCameraHistory/);
  assert.match(page, /Previous view/);
  assert.match(page, /boxZoomEnd/);
  assert.match(page, /Capture report area/);
  assert.match(page, /Shift-drag locked a browser-local MapLibre report area/);
  assert.match(page, /compatible_record_count/);
  assert.match(css, /\.analysis-area-card/);
  assert.match(mapInterface, /Terrain \+ hillshade[\s\S]*CONTEXT ONLY/);
  assert.match(mapInterface, /Offline \/ PMTiles[\s\S]*HOLD/);
});

test("adds a no-upload KML and GeoJSON inspection preview without admission effects", async () => {
  const ts = await import("typescript");
  const importSource = await readFile(new URL("../app/import-preview.ts", import.meta.url), "utf8");
  const page = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
  const runtime = await readFile(new URL("../app/map-runtime.ts", import.meta.url), "utf8");
  const mapInterface = await readFile(new URL("../app/map-interface.ts", import.meta.url), "utf8");
  const css = await readFile(new URL("../app/globals.css", import.meta.url), "utf8");
  const javascript = ts.transpileModule(importSource, {
    compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
    fileName: "import-preview.ts",
  }).outputText;
  const imports = await import(`data:text/javascript;base64,${Buffer.from(javascript).toString("base64")}`);
  const preview = imports.buildLocalImportPreview({
    fileName: "test.geojson",
    fileSizeBytes: 480,
    inspectedAt: "2026-08-30T18:30:00.000Z",
    supportedBounds: { west: -104.8, south: 34.8, east: -92, north: 42.2 },
    text: JSON.stringify({
      type: "FeatureCollection",
      attribution: "Synthetic test fixture",
      features: [{
        type: "Feature",
        id: "preview-1",
        properties: { name: "Preview point", observed_time: "2026-08-30" },
        geometry: { type: "Point", coordinates: [-98.4, 38.5] },
      }],
    }),
  });

  assert.equal(preview.featureCount, 1);
  assert.equal(preview.coverage, "WITHIN_KANSAS_CONTEXT");
  assert.equal(preview.renderAllowed, true);
  assert.deepEqual(preview.temporalFields, ["observed_time"]);
  const previewAudit = imports.importPreviewAudit(preview);
  assert.equal(previewAudit.bounds, "WITHHELD_LOCAL_GEOMETRY");
  assert.doesNotMatch(JSON.stringify(previewAudit), /-98\.4|38\.5/);
  assert.equal(previewAudit.effects, "NO_UPLOAD_NO_EXACT_BOUNDS_NO_SOURCE_ADMISSION_NO_REPORT_DATA_NO_PUBLICATION");

  const invalidPreview = imports.buildLocalImportPreview({
    fileName: "invalid-structures.geojson",
    fileSizeBytes: 600,
    inspectedAt: "2026-08-31T05:30:00.000Z",
    supportedBounds: { west: -104.8, south: 34.8, east: -92, north: 42.2 },
    text: JSON.stringify({ type: "FeatureCollection", features: [
      { type: "Feature", properties: {}, geometry: { type: "Point", coordinates: [[-98, 38]] } },
      { type: "Feature", properties: {}, geometry: { type: "LineString", coordinates: [[-98, 38]] } },
      { type: "Feature", properties: {}, geometry: { type: "Polygon", coordinates: [[[-99, 37], [-98, 37], [-98, 38], [-99, 38]]] } },
    ] }),
  });
  assert.equal(invalidPreview.featureCount, 0);
  assert.equal(invalidPreview.invalidFeatureCount, 3);
  assert.equal(invalidPreview.renderAllowed, false);

  const largeCoordinates = Array.from({ length: 150_000 }, (_, index) => [-98.5 + (index % 2) * 0.1, 38.5]);
  const largeText = JSON.stringify({ type: "MultiPoint", coordinates: largeCoordinates });
  assert.ok(Buffer.byteLength(largeText) < imports.IMPORT_PREVIEW_MAX_BYTES);
  const largePreview = imports.buildLocalImportPreview({
    fileName: "large.geojson",
    fileSizeBytes: Buffer.byteLength(largeText),
    inspectedAt: "2026-08-31T05:31:00.000Z",
    supportedBounds: { west: -104.8, south: 34.8, east: -92, north: 42.2 },
    text: largeText,
  });
  assert.deepEqual(largePreview.bounds, [-98.5, 38.5, -98.4, 38.5]);

  const kmlPreview = imports.buildLocalImportPreview({
    fileName: "local.kml",
    fileSizeBytes: 800,
    inspectedAt: "2026-08-31T05:32:00.000Z",
    supportedBounds: { west: -104.8, south: 34.8, east: -92, north: 42.2 },
    text: `<?xml version="1.0"?><kml xmlns="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom"><Document><atom:author><atom:name>Synthetic fixture</atom:name></atom:author><NetworkLink><Link><href>https://example.invalid/held.kml</href></Link></NetworkLink><Placemark><name>Local point</name><description><![CDATA[<b>not HTML</b>]]></description><ExtendedData><SchemaData><SimpleData name="owner">Synthetic owner</SimpleData></SchemaData></ExtendedData><Point><coordinates>-98.4,38.5</coordinates></Point></Placemark></Document></kml>`,
  });
  assert.equal(kmlPreview.featureCount, 1);
  assert.equal(kmlPreview.unsupportedElementCount, 1);
  assert.equal(kmlPreview.externalReferenceCount, 1);
  assert.equal(kmlPreview.attribution, "Synthetic fixture");
  assert.deepEqual(kmlPreview.sensitivitySignals, ["owner"]);

  const disguisedGeometryPreview = imports.buildLocalImportPreview({
    fileName: "disguised-geometry.kml",
    fileSizeBytes: 700,
    inspectedAt: "2026-08-31T05:33:00.000Z",
    supportedBounds: { west: -104.8, south: 34.8, east: -92, north: 42.2 },
    text: `<?xml version="1.0"?><kml><Document><Placemark><name>No geometry</name><description><![CDATA[<Point><coordinates>-98.4,38.5</coordinates></Point>]]></description><!-- <LineString><coordinates>-99,38 -98,39</coordinates></LineString> --></Placemark></Document></kml>`,
  });
  assert.equal(disguisedGeometryPreview.featureCount, 0);
  assert.equal(disguisedGeometryPreview.bounds, null);
  assert.equal(disguisedGeometryPreview.renderAllowed, false);

  const malformedCoordinatePreview = imports.buildLocalImportPreview({
    fileName: "malformed-coordinates.kml",
    fileSizeBytes: 500,
    inspectedAt: "2026-08-31T05:34:00.000Z",
    supportedBounds: { west: -104.8, south: 34.8, east: -92, north: 42.2 },
    text: `<?xml version="1.0"?><kml><Document><Placemark><name>Broken line</name><LineString><coordinates>-99,38 malformed -98,39</coordinates></LineString></Placemark></Document></kml>`,
  });
  assert.equal(malformedCoordinatePreview.featureCount, 0);
  assert.equal(malformedCoordinatePreview.renderAllowed, false);

  assert.throws(() => imports.buildLocalImportPreview({
    fileName: "comment-spliced-tag.kml",
    fileSizeBytes: 420,
    inspectedAt: "2026-08-31T05:35:00.000Z",
    supportedBounds: { west: -104.8, south: 34.8, east: -92, north: 42.2 },
    text: `<?xml version="1.0"?><kml><Document><Placemark><name>Broken point</name><Poi<!-- synthetic separator -->nt><coordinates>-98.4,38.5</coordinates></Point></Placemark></Document></kml>`,
  }), /outside tag markup/);

  assert.match(importSource, /kmlMarkupForInspection/);
  assert.match(importSource, /positions\.some\(\(position\) => position === null\)/);
  assert.match(importSource, /KML/);
  assert.match(importSource, /NetworkLink/);
  assert.doesNotMatch(importSource, /DOMParser|Math\.min\(\.\.\.positions/);
  assert.match(page, /LOCAL IMPORT PREVIEW/);
  assert.match(page, /Temporary Places, KFM-style/);
  assert.match(page, /accept="\.kml,\.geojson,\.json/);
  assert.match(page, /importInspectionGenerationRef/);
  assert.match(page, /inspectionGeneration !== importInspectionGenerationRef\.current/);
  assert.match(page, /locationDerivedViewRef\.current = true;\s*setLocationCameraRedacted\(true\)/);
  assert.match(page, /const redactWorkspaceCamera = locationCameraRedacted \|\| locationDerivedViewRef\.current/);
  assert.match(page, /updateImportPreviewSource/);
  assert.match(runtime, /kfm-import-preview/);
  assert.match(mapInterface, /External data admission[\s\S]*HOLD/);
  assert.match(css, /\.import-dropzone/);
  assert.match(css, /\.import-check-list/);
});

test("keeps optional guided examples while moving explanatory copy to About", async () => {
  const source = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
  const about = await readFile(new URL("../app/about/page.tsx", import.meta.url), "utf8");
  const css = await readFile(new URL("../app/globals.css", import.meta.url), "utf8");

  assert.match(source, /GUIDED_EXAMPLES/);
  assert.match(source, /atmo-topeka-2026/);
  assert.match(source, /atmo-hays-2024/);
  assert.match(source, /planning-generalized-envelope/);
  assert.match(source, /Every current map layer is synthetic or generalized/);
  assert.match(source, /Guided material remains available from About/);
  assert.match(about, /site-local synthetic and generalized demonstration records/);
  assert.match(source, /kfm-guided-start-dismissed-v1/);
  assert.match(source, /openGuidedExample/);
  assert.match(css, /\.guided-start/);
  assert.match(css, /\.guided-example-list button/);
});

test("adds a bounded guided story and read-only layer comparison", async () => {
  const source = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
  const mapInterface = await readFile(new URL("../app/map-interface.ts", import.meta.url), "utf8");
  const css = await readFile(new URL("../app/globals.css", import.meta.url), "utf8");

  assert.match(source, /KFM_STORY_TRAIL/);
  assert.match(source, /A correction stays attached to the record/);
  assert.match(source, /Fixture-first 2D guidance only/);
  assert.match(source, /no live StoryManifest playback/);
  assert.match(source, /kfm-site-layer-comparison-v1/);
  assert.match(source, /Comparison is a read-only projection/);
  assert.match(source, /params\.set\("compare"/);
  assert.match(mapInterface, /"compare"/);
  assert.match(css, /\.story-trail/);
  assert.match(css, /\.layer-compare-grid/);
});

test("adds a complete county starter slice and scoped temporal catalog comparison", async () => {
  const countySource = await readFile(new URL("../app/county-starter-slice.ts", import.meta.url), "utf8");
  const countyData = JSON.parse(await readFile(new URL("../app/county-starter-points.json", import.meta.url), "utf8"));
  const temporalSource = await readFile(new URL("../app/temporal-comparison.ts", import.meta.url), "utf8");
  const page = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
  const mapInterface = await readFile(new URL("../app/map-interface.ts", import.meta.url), "utf8");
  const css = await readFile(new URL("../app/globals.css", import.meta.url), "utf8");

  assert.equal(countyData.counties.length, 105);
  assert.equal(new Set(countyData.counties.map((county) => county.geoid)).size, 105);
  assert.equal(countyData.counties.every((county) => Number.isFinite(county.latitude) && Number.isFinite(county.longitude)), true);
  assert.match(countySource, /GENERALIZED_GEOMETRY/);
  assert.match(countySource, /not a county boundary, centroid, address, county seat, parcel location/i);
  assert.match(page, /COUNTY_STARTER_LAYER/);
  assert.match(page, /TIME A \/ TIME B CATALOG AVAILABILITY/);
  assert.match(page, /matchesReportRecord/);
  assert.match(page, /params\.set\("times"/);
  assert.match(temporalSource, /CATALOG_AVAILABILITY_NOT_OBSERVED_CHANGE/);
  assert.match(temporalSource, /recordFilter/);
  assert.match(mapInterface, /Repository Sites consumer[\s\S]*NULL RUNTIME \/ HOLD/);
  assert.match(css, /\.temporal-compare-lab/);
});

test("uses a site-specific social card and request-host metadata", async () => {
  const layout = await readFile(new URL("../app/layout.tsx", import.meta.url), "utf8");
  const socialCard = await readFile(new URL("../public/og-guided.png", import.meta.url));

  assert.match(layout, /x-forwarded-host/);
  assert.match(layout, /new URL\("\/og-guided\.png", metadataBase\)/);
  assert.match(layout, /real MapLibre Kansas vector context/);
  assert.ok(socialCard.byteLength > 100_000);
});

test("keeps Focus Mode fail closed and share state complete", async () => {
  const source = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
  const focus = await readFile(new URL("../app/focus-mode.ts", import.meta.url), "utf8");

  assert.match(source, /focusResultForState/);
  assert.match(focus, /GEOMETRY_IS_NOT_EVIDENCE/);
  assert.match(focus, /TIME_SCOPE_MISMATCH/);
  assert.match(source, /Outcomes cannot be manually overridden/);
  assert.match(source, /kfm-focus-session-receipt-v1/);
  assert.match(source, /Apply explicit change/);
  assert.match(source, /context_is_evidence: false/);
  assert.match(source, /aria-controls={`drawer-panel-/);
  assert.doesNotMatch(source, /setFocusScenario|className="focus-scenarios"/);
  assert.match(source, /params\.set\("proj", projection\)/);
  assert.match(source, /params\.set\("order", layerOrder\.join\(","\)\)/);
  assert.match(source, /params\.set\("focusStage", focusStage\)/);
  assert.match(source, /params\.set\("focusIntent", focusIntent\)/);
  assert.match(source, /params\.set\("ws", currentWorkspace\)/);
  assert.match(source, /params\.get\("privacy"\) === "location-camera-redacted"/);
  assert.match(source, /window\.addEventListener\("popstate", handlePopState\)/);
  assert.match(source, /WebGL2 is unavailable in this browser/);
  assert.match(source, /clamp\(parseNumber\(params\.get\("z"\), KANSAS_VIEW\.zoom\), 4, 16\)/);
  assert.match(source, /value === null \|\| value\.trim\(\) === ""/);
  assert.match(source, /params\.has\("l"\)/);
  assert.match(source, /LAYER_REGISTRY\.map\(\(layer\) => `\$\{layer\.id\}:\$\{\(opacity/);
  assert.match(source, /const params = buildExplorerParams\(\)/);
  assert.doesNotMatch(source, /window\.history\.pushState/);
});

test("adds device-local Places trails and faster layer isolation controls", async () => {
  const ts = await import("typescript");
  const page = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
  const mapInterface = await readFile(new URL("../app/map-interface.ts", import.meta.url), "utf8");
  const placesSource = await readFile(new URL("../app/places-trail.ts", import.meta.url), "utf8");
  const css = await readFile(new URL("../app/globals.css", import.meta.url), "utf8");
  const javascript = ts.transpileModule(placesSource, {
    compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
    fileName: "places-trail.ts",
  }).outputText;
  const places = await import(`data:text/javascript;base64,${Buffer.from(javascript).toString("base64")}`);

  assert.match(mapInterface, /"places"/);
  assert.match(page, /Places \+ investigation trails/);
  assert.match(page, /Google Earth–inspired, KFM-governed/);
  assert.match(page, /locationCameraRedacted \|\| locationDerivedViewRef\.current/);
  assert.match(page, /setLayerGroupVisibility/);
  assert.match(page, /isolateLayer/);
  assert.match(page, />Show all</);
  assert.match(page, />Solo</);
  assert.match(css, /\.place-trail-list/);
  assert.match(css, /\.catalog-group-heading/);

  const stops = [{ id: "a" }, { id: "b" }, { id: "c" }];
  assert.deepEqual(places.reorderPlaceStops(stops, "b", -1).map((stop) => stop.id), ["b", "a", "c"]);
  assert.deepEqual(places.reorderPlaceStops(stops, "a", -1).map((stop) => stop.id), ["a", "b", "c"]);
  assert.equal(places.nextPlaceStopIndex(3, 2, 1), 0);
  assert.equal(places.nextPlaceStopIndex(3, 0, -1), 2);
  assert.equal(places.normalizePlaceStopName("  Flint   Hills  ", 1), "Flint Hills");
  assert.equal(places.normalizePlaceStopName("", 2), "Kansas place 2");
});

test("resolves Focus outcomes and temporal scope with fail-closed precedence", async () => {
  const ts = await import("typescript");
  const source = await readFile(new URL("../app/focus-mode.ts", import.meta.url), "utf8");
  const javascript = ts.transpileModule(source, {
    compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
    fileName: "focus-mode.ts",
  }).outputText;
  const focus = await import(`data:text/javascript;base64,${Buffer.from(javascript).toString("base64")}`);

  const expected = {
    ANSWER: "ANSWER",
    CORRECTED: "ANSWER",
    MISSING_EVIDENCE: "ABSTAIN",
    SOURCE_STALE: "ABSTAIN",
    GENERALIZED_GEOMETRY: "ABSTAIN",
    SUPERSEDED: "ABSTAIN",
    DENIED_BY_POLICY: "DENY",
    RESTRICTED_ACCESS: "DENY",
    ERROR: "ERROR",
  };
  for (const [state, outcome] of Object.entries(expected)) {
    assert.equal(focus.focusResultForState(state, false).outcome, outcome, state);
  }

  assert.equal(focus.focusResultForState("ANSWER", true).code, "TIME_SCOPE_MISMATCH");
  assert.equal(focus.focusResultForState("DENIED_BY_POLICY", true).outcome, "DENY");
  assert.equal(focus.focusResultForState("ERROR", true).outcome, "ERROR");
  assert.equal(focus.isFeatureTimeMismatch({ mode: "exact" }, 2026, 2024), true);
  assert.equal(focus.isFeatureTimeMismatch({ mode: "exact" }, 2026, 2026), false);
  assert.equal(focus.isFeatureTimeMismatch({ mode: "through" }, 1910, 1885), true);
  assert.equal(focus.isFeatureTimeMismatch({ mode: "through" }, 1885, 1910), false);
  assert.equal(focus.isFeatureTimeMismatch(undefined, 2026, 1885), false);

  const mismatchActions = focus.buildFocusActionProposals({
    state: "ANSWER",
    timeMismatch: true,
    activeYear: 2024,
    featureYear: 2026,
    currentCenter: [-98.4, 38.5],
    focusCenter: [-95.7, 39.0],
  });
  assert.equal(mismatchActions[0].kind, "SET_TIME");
  assert.equal(mismatchActions[0].targetYear, 2026);
  const deniedActions = focus.buildFocusActionProposals({
    state: "DENIED_BY_POLICY",
    timeMismatch: true,
    activeYear: 2024,
    featureYear: 2026,
    currentCenter: [-98.4, 38.5],
    focusCenter: [-95.7, 39.0],
  });
  assert.equal(deniedActions.some((action) => action.kind === "SET_TIME"), false);
});

test("keeps repository updates pinned and boundary-labeled", async () => {
  const updates = await readFile(new URL("../app/repository-updates.ts", import.meta.url), "utf8");
  const identity = await readFile(new URL("../app/site-identity.ts", import.meta.url), "utf8");

  assert.match(identity, /b44494c1cf0807ed28b606e8a41b255bebdf4ad7/);
  assert.match(updates, /SITE_IDENTITY\.repositoryCommit/);
  assert.match(updates, /separate source histories/);
  assert.match(updates, /Local geodata inspection now fails closed on malformed or stale input/);
  assert.match(updates, /All 105 Kansas counties now have public locator starters/);
  assert.match(updates, /Time A \/ Time B comparison preserves report scope/);
  assert.match(updates, /exact maplibre-gl 6\.6\.0 lock closure/);
  assert.match(updates, /521 commits after the prior Site evidence pin/);
  assert.match(updates, /Planning scenarios now have a strict review projection/);
  assert.match(updates, /Accessibility guidance now separates targets from proof/);
  assert.match(updates, /The executable API checkpoint is intentionally negative-only/);
  assert.match(updates, /Consent metadata is normalized; the fixture-first boundary remains/);
  assert.match(updates, /Hydrology dashboard boundary is now repository-grounded/);
  assert.match(updates, /The retained GeoParquet 1\.1 CRS fixture was corrected/);
  assert.match(updates, /This Site remains a separate synthetic demonstration and is not KFM runtime-readiness evidence/);
  assert.match(updates, /no county lifecycle readiness, release, or publication state/);
  assert.match(updates, /HOLD is not a fifth client-facing runtime outcome/);
  assert.match(updates, /PUBLISHED → PUBLISHED_SUPERSEDED/);
  assert.match(updates, /HOLD_CURRENT_RELEASE/);
});

test("replays the strict planning-scenario fixture and finite negative states", async () => {
  const ts = await import("typescript");
  const source = await readFile(new URL("../app/planning-scenario.ts", import.meta.url), "utf8");
  const page = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
  const css = await readFile(new URL("../app/globals.css", import.meta.url), "utf8");
  const compiled = ts.transpileModule(source, {
    compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
    fileName: "planning-scenario.ts",
  }).outputText;
  const scenario = await import(`data:text/javascript;base64,${Buffer.from(compiled).toString("base64")}`);

  assert.deepEqual(Object.keys(scenario.PLANNING_SCENARIO_REVIEWS), ["held", "missing", "denied", "error"]);
  assert.equal(scenario.PLANNING_SCENARIO_REVIEWS.held.outcome, "ABSTAIN");
  assert.equal(scenario.PLANNING_SCENARIO_REVIEWS.held.inputs.length, 3);
  assert.equal(scenario.PLANNING_SCENARIO_REVIEWS.held.assumptions.length, 3);
  assert.equal(scenario.PLANNING_SCENARIO_REVIEWS.held.equityQuestions.length, 2);
  assert.equal(scenario.PLANNING_SCENARIO_REVIEWS.denied.evidenceRefs.length, 0);
  assert.equal(scenario.PLANNING_SCENARIO_REVIEWS.error.scenarioStatus, null);
  assert.match(page, /FIXTURE-ONLY · TEXT-FIRST REVIEW/);
  assert.match(page, /Evidence resolved <b>FALSE/);
  assert.match(page, /performs no transport, source retrieval, scenario computation/);
  assert.match(css, /\.planning-scenario-review/);
  assert.doesNotMatch(source, /\bfetch\s*\(/);
  assert.doesNotMatch(source, /localStorage|sessionStorage/);
});

test("imports the complete repository feature catalog without maturity inflation", async () => {
  const ts = await import("typescript");
  const featureSource = await readFile(new URL("../app/feature-catalog.ts", import.meta.url), "utf8");
  const compiled = ts.transpileModule(featureSource, {
    compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
    fileName: "feature-catalog.ts",
  }).outputText;
  const catalog = await import(`data:text/javascript;base64,${Buffer.from(compiled).toString("base64")}`);

  assert.equal(catalog.FEATURE_CATALOG.length, 38);
  assert.equal(new Set(catalog.FEATURE_CATALOG.map((feature) => feature.id)).size, 38);
  assert.equal(new Set(catalog.FEATURE_CATALOG.map((feature) => feature.area)).size, 6);
  assert.deepEqual(
    Object.fromEntries(["VERIFIED_SLICE", "FIXTURE_FIRST", "DOCUMENTED", "HOLD"].map((maturity) => [maturity, catalog.FEATURE_CATALOG.filter((feature) => feature.maturity === maturity).length])),
    { VERIFIED_SLICE: 4, FIXTURE_FIRST: 26, DOCUMENTED: 7, HOLD: 1 },
  );
  assert.equal(catalog.FEATURE_CATALOG.some((feature) => feature.id === "story-player" && feature.maturity === "FIXTURE_FIRST"), true);
  assert.equal(catalog.FEATURE_CATALOG.every((feature) => feature.path && feature.summary), true);
});

test("keeps the MapLibre Workbench complete, bounded, and responsive", async () => {
  const source = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
  const mapInterface = await readFile(new URL("../app/map-interface.ts", import.meta.url), "utf8");
  const exportCenter = await readFile(new URL("../app/export-center.ts", import.meta.url), "utf8");
  const explorerData = await readFile(new URL("../app/explorer-data.ts", import.meta.url), "utf8");
  const css = await readFile(new URL("../app/globals.css", import.meta.url), "utf8");
  const prepareMapLibreAssets = await readFile(new URL("../scripts/prepare-maplibre-assets.mjs", import.meta.url), "utf8");
  const buildScript = await readFile(new URL("../scripts/build-verified.sh", import.meta.url), "utf8");
  const installScript = await readFile(new URL("../scripts/install-ci.sh", import.meta.url), "utf8");
  const tsconfig = await readFile(new URL("../tsconfig.json", import.meta.url), "utf8");

  assert.match(source, /id="map-utility-panel"/);
  for (const view of ["Navigate", "Inspect", "Import", "Compare", "Display", "Measure", "Export", "Diagnostics"]) assert.match(source, new RegExp(`${view}`));
  assert.match(source, /kfm-map-context-receipt-v1/);
  assert.match(source, /kfm-map-diagnostics-v1/);
  assert.match(exportCenter, /kfm-public-safe-map-export-v2/);
  assert.match(source, /Preview trust before download/);
  assert.match(source, /Renderer-neutral runtime seam/);
  assert.match(source, /location-camera-redacted/);
  assert.match(source, /WITHHELD_BROWSER_LOCATION/);
  assert.match(source, /Screen measurement — not survey, cadastral, legal, or evidence/);
  assert.match(source, /Go to coordinates/);
  assert.match(source, /Current viewport only/);
  assert.match(source, /Visible layers only/);
  assert.match(source, /copyMapCenter/);
  assert.match(source, /fitIndexedFeatures/);
  assert.match(source, /SUPPORTED_CONTEXT_BOUNDS/);
  assert.match(source, /site_package: "6\.6\.0"/);
  assert.match(source, /setWorkerUrl\(MAPLIBRE_WORKER_URL\)/);
  assert.match(source, /getWorkerUrl\(\) !== MAPLIBRE_WORKER_URL/);
  assert.match(source, /getVersion\(\)/);
  assert.match(source, /MAPLIBRE_RUNTIME_ASSET_URLS/);
  assert.match(source, /if \(!response\.ok\) throw new Error/);
  assert.match(source, /map\.on\("idle"/);
  assert.match(source, /map\.areTilesLoaded\(\)/);
  assert.match(source, /map\.isSourceLoaded\(layer\.sourceId\)/);
  assert.match(source, /MapLibre \{EXPECTED_MAPLIBRE_VERSION\} runtime proof/);
  assert.match(source, /SAME_ORIGIN_CONFIGURED/);
  assert.match(prepareMapLibreAssets, /maplibre-gl-worker\.mjs/);
  assert.match(prepareMapLibreAssets, /maplibre-gl-shared\.mjs/);
  assert.match(buildScript, /exec bash "\$\{script_dir\}\/sites-env\.sh"/);
  assert.match(installScript, /exec bash "\$\{script_dir\}\/sites-env\.sh"/);
  assert.match(tsconfig, /"target": "ES2022"/);
  assert.match(source, /FULL TEMPORAL CAPACITY · 4\.54 GA BP TO 2026/);
  assert.match(source, /Deep-time and intermediate ticks are capacity markers, not claims/);
  assert.match(source, /TIMELINE_JUMPS/);
  assert.match(explorerData, /-4_540_000_000/);
  assert.match(explorerData, /-541_000_000/);
  assert.match(explorerData, /-11_700/);
  assert.match(source, /mapQueryCandidates/);
  assert.match(source, /selected && !selectedTimeMismatch && !selectedLayerHidden/);
  assert.match(source, /VISIBLE LAYERS/);
  assert.match(mapInterface, /Renderer architecture[\s\S]*ACCEPTED/);
  assert.match(mapInterface, /MapRuntimePort \+ Null runtime[\s\S]*VERIFIED SLICE/);
  assert.match(mapInterface, /Dependency admission[\s\S]*EXACT 6\.6\.0/);
  assert.match(mapInterface, /Concrete MapLibre adapter[\s\S]*VERIFIED SLICE/);
  assert.match(mapInterface, /Browser readiness[\s\S]*BOUNDED FIXTURE/);
  assert.match(explorerData, /"fill-outline-color": \["case", \["boolean", \["feature-state", "hover"\]/);
  assert.match(css, /\.map-utility-panel\[data-open="true"\]/);
  assert.match(css, /\.mobile-hidden-control/);
  assert.match(css, /grid-template-columns: repeat\(5,1fr\)/);
  assert.doesNotMatch(css, /\.map-tool-rail > button:nth-child/);
});

test("resolves exact, through-time, and untimed Map Workbench availability", async () => {
  const ts = await import("typescript");
  const source = await readFile(new URL("../app/map-interface.ts", import.meta.url), "utf8");
  const javascript = ts.transpileModule(source, {
    compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
    fileName: "map-interface.ts",
  }).outputText;
  const mapInterface = await import(`data:text/javascript;base64,${Buffer.from(javascript).toString("base64")}`);

  const exact = { temporal: { mode: "exact", years: [2024, 2026] } };
  const through = { temporal: { mode: "through", years: [1885, 1910] } };
  assert.equal(mapInterface.isLayerAvailableAtTime(exact, 2024), true);
  assert.equal(mapInterface.isLayerAvailableAtTime(exact, 2025), false);
  assert.equal(mapInterface.isLayerAvailableAtTime(through, 1880), false);
  assert.equal(mapInterface.isLayerAvailableAtTime(through, 1900), true);
  assert.equal(mapInterface.isLayerAvailableAtTime({}, 1880), true);

  const layer = {
    temporal: { mode: "through", years: [1885, 1910] },
    data: { features: [
      { properties: { fid: "vintage-1885", year: 1885 } },
      { properties: { fid: "vintage-1910", year: 1910 } },
    ] },
  };
  assert.equal(mapInterface.inspectableFeatureId(layer, 1880), null);
  assert.equal(mapInterface.inspectableFeatureId(layer, 1900), "vintage-1885");
  assert.equal(mapInterface.inspectableFeatureId(layer, 2026), "vintage-1910");
});

test("keeps source discovery separate from admission and map ranges explicit", async () => {
  const sources = await readFile(new URL("../app/source-intelligence.ts", import.meta.url), "utf8");
  const runtime = await readFile(new URL("../app/map-runtime.ts", import.meta.url), "utf8");

  assert.match(sources, /Source discovery is not source admission/);
  assert.match(sources, /KFM Full Atlas Seed Cards/);
  assert.match(sources, /sourceCount: 12/);
  assert.match(sources, /DEFER DEPENDENCY/);
  assert.match(sources, /National Flood Hazard Layer/);
  assert.match(runtime, /attribution: record\.attribution/);
  assert.match(runtime, /setLayerZoomRange\(renderer\.id, record\.minZoom, record\.maxZoom\)/);
});

test("keeps every top-level external map carrier in a display-only disclosure registry", async () => {
  const ts = await import("typescript");
  const source = await readFile(new URL("../app/external-context-sources.ts", import.meta.url), "utf8");
  const page = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
  const runtime = await readFile(new URL("../app/map-runtime.ts", import.meta.url), "utf8");
  const terrain = await readFile(new URL("../app/terrain-sources.ts", import.meta.url), "utf8");
  const javascript = ts.transpileModule(source, {
    compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
    fileName: "external-context-sources.ts",
  }).outputText;
  const registry = await import(`data:text/javascript;base64,${Buffer.from(javascript).toString("base64")}`);

  assert.equal(registry.EXTERNAL_CONTEXT_SOURCES.length, 5);
  assert.equal(new Set(registry.EXTERNAL_CONTEXT_SOURCES.map((record) => record.id)).size, 5);
  assert.equal(registry.EXTERNAL_CONTEXT_SOURCES.every((record) => record.requestUrl.startsWith("https://")), true);
  assert.equal(registry.EXTERNAL_CONTEXT_SOURCES.every((record) => record.sourceUrl.startsWith("https://")), true);
  assert.equal(registry.EXTERNAL_CONTEXT_SOURCES.every((record) => record.attribution.length > 0 && record.fallback.length > 0), true);
  assert.equal(registry.EXTERNAL_CONTEXT_SOURCES.every((record) => record.evidenceRole === "DISPLAY_CONTEXT_ONLY"), true);
  assert.equal(registry.EXTERNAL_CONTEXT_SOURCES.every((record) => record.exportEffect === "ATTRIBUTION_ONLY"), true);
  assert.match(runtime, /externalContextSource\("openfreemap-liberty"\)/);
  assert.match(runtime, /externalContextSource\("esri-world-imagery"\)/);
  assert.match(runtime, /externalContextSource\("openstreetmap-standard"\)/);
  assert.match(runtime, /externalContextSource\("usgs-national-map-topo"\)/);
  assert.match(terrain, /externalContextSource\("aws-mapzen-terrarium"\)/);
  assert.match(terrain, /TERRARIUM_RENDER_MAX_ZOOM = 11/);
  assert.match(terrain, /deeper map zooms deliberately overzoom the clean z11 DEM/);
  assert.match(terrain, /maxZoom: TERRARIUM_RENDER_MAX_ZOOM/);
  assert.match(page, /Browser-requested display carriers/);
  assert.match(page, /NO REQUEST FROM CURRENT VIEW/);
});

test("connects fourteen bounded official Kansas context sources without admitting evidence", async () => {
  const ts = await import("typescript");
  const registrySource = await readFile(new URL("../app/live-context.ts", import.meta.url), "utf8");
  const radarSource = await readFile(new URL("../app/noaa-radar.ts", import.meta.url), "utf8");
  const route = await readFile(new URL("../app/api/live-context/route.ts", import.meta.url), "utf8");
  const page = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
  const css = await readFile(new URL("../app/globals.css", import.meta.url), "utf8");
  const compile = (source, fileName) => ts.transpileModule(source, {
    compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
    fileName,
  }).outputText;
  const radarUrl = `data:text/javascript;base64,${Buffer.from(compile(radarSource, "noaa-radar.ts")).toString("base64")}`;
  const performanceSource = await readFile(new URL("../app/map-performance.ts", import.meta.url), "utf8");
  const performanceUrl = `data:text/javascript;base64,${Buffer.from(compile(performanceSource, "map-performance.ts")).toString("base64")}`;
  const javascript = compile(registrySource.replace('from "./noaa-radar";', `from "${radarUrl}";`).replace('from "./map-performance";', `from "${performanceUrl}";`), "live-context.ts");
  const registry = await import(`data:text/javascript;base64,${Buffer.from(javascript).toString("base64")}`);

  assert.deepEqual(registry.OFFICIAL_CONTEXT_SOURCES.map((record) => record.id), [
    "census-counties",
    "usgs-streamflow",
    "noaa-nwps-gauges",
    "usgs-3dhp-hydrography",
    "usgs-wbd-watersheds",
    "noaa-nwm-analysis",
    "noaa-nwm-short-range",
    "usgs-earthquakes",
    "noaa-hms-smoke",
    "raspberry-shake-stations",
    "usgs-3dep-hillshade",
    "usgs-3dep-slope",
    "nws-alerts",
    "nws-radar",
  ]);
  assert.deepEqual(registry.OFFICIAL_CONTEXT_SOURCES.filter((record) => record.defaultVisibility).map((record) => record.id), ["census-counties", "usgs-streamflow", "usgs-3dhp-hydrography"]);
  assert.equal(registry.OFFICIAL_CONTEXT_SOURCES.every((record) => record.evidenceRole === "EXTERNAL_CONTEXT_ONLY"), true);
  assert.equal(registry.OFFICIAL_CONTEXT_SOURCES.filter((record) => record.domain === "Living waters").length, 6);
  assert.match(registry.OFFICIAL_CONTEXT_BY_ID["usgs-streamflow"].serviceUrl, /^https:\/\/api\.waterdata\.usgs\.gov\/ogcapi\/v1\//);
  assert.match(registry.OFFICIAL_CONTEXT_BY_ID["usgs-3dhp-hydrography"].mapUrl, /^https:\/\/3dhp\.nationalmap\.gov\/[\s\S]*usgs_3dhp_all\/MapServer\/export/);
  assert.match(registry.OFFICIAL_CONTEXT_BY_ID["usgs-wbd-watersheds"].mapUrl, /wbd\/MapServer\/export/);
  assert.match(registry.OFFICIAL_CONTEXT_BY_ID["noaa-nwm-analysis"].boundary, /does not advertise a selectable time axis/i);
  assert.match(registry.OFFICIAL_CONTEXT_BY_ID["noaa-nwm-short-range"].boundary, /modeled maximum over a forecast window/i);
  assert.match(registry.OFFICIAL_CONTEXT_BY_ID["noaa-hms-smoke"].apiPath, /feed=noaa-hms-smoke/);
  assert.match(registry.OFFICIAL_CONTEXT_BY_ID["noaa-hms-smoke"].boundary, /fire perimeter[\s\S]*surface PM2\.5/i);
  assert.match(registry.OFFICIAL_CONTEXT_BY_ID["raspberry-shake-stations"].serviceUrl, /stationview\.raspberryshake\.org/);
  assert.match(registry.OFFICIAL_CONTEXT_BY_ID["raspberry-shake-stations"].boundary, /not realtime/i);
  assert.match(registry.OFFICIAL_CONTEXT_BY_ID["usgs-3dep-slope"].mapUrl, /^\/api\/terrain-tile\?kind=slope&z=\{z\}&x=\{x\}&y=\{y\}$/);
  assert.match(page, /OFFICIAL OPERATIONAL CONTEXT/);
  assert.match(page, /Real Kansas source connections/);
  assert.match(page, /Refresh visible/);
  assert.match(page, /Search places, layers, official data/);
  assert.match(page, /params\.set\("ctx"/);
  assert.match(page, /params\.set\("ctxo"/);
  assert.match(page, /zero mapped features[\s\S]*not an all-clear/i);
  assert.match(page, /governance issue #3393/);
  const countySource = await readFile(new URL("../app/county-baseline.ts", import.meta.url), "utf8");
  assert.match(route, /countyBaseline\("2020"\)/);
  assert.match(countySource, /STATE='20'/);
  assert.match(countySource, /POP100,HU100/);
  assert.match(route, /state_code/);
  assert.match(route, /datetime/);
  assert.match(route, /earthquake\.usgs\.gov\/fdsnws\/event\/1\/query/);
  assert.match(route, /NOAA HMS smoke publications/);
  assert.match(route, /data\.raspberryshake\.org\/fdsnws\/station\/1\/query/);
  assert.match(route, /MAX_RASPBERRY_SHAKE_STATIONS = 250/);
  assert.match(route, /normalizedFdsnHeader/);
  assert.match(route, /FDSN archive is delayed by at least 30 minutes/);
  assert.match(route, /minlatitude/);
  assert.match(route, /maxlongitude/);
  assert.match(route, /KansasFrontierMatrixExplorer\/1\.0/);
  assert.match(route, /MAX_NWS_ZONE_REQUESTS = 36/);
  assert.match(route, /forecast\|county\|fire/);
  assert.match(route, /KSZ\|KSC/);
  assert.match(route, /Unknown live-context feed/);
  assert.doesNotMatch(route, /searchParams\.get\("url"\)/);
  assert.match(css, /\.official-context-catalog/);
  assert.match(css, /\.official-connection-ledger/);
});

test("adds bounded exact-time streamflow, NOAA hydrology roles, and a gap-aware River Pulse workbench", async () => {
  const streamflow = await readFile(new URL("../app/streamflow.ts", import.meta.url), "utf8");
  const usgsRoute = await readFile(new URL("../app/api/hydrology/streamflow/route.ts", import.meta.url), "utf8");
  const noaaHydrology = await readFile(new URL("../app/noaa-hydrology.ts", import.meta.url), "utf8");
  const noaaRoute = await readFile(new URL("../app/api/hydrology/noaa/route.ts", import.meta.url), "utf8");
  const observatory = await readFile(new URL("../app/hydrology-observatory.tsx", import.meta.url), "utf8");
  const livingAtlas = await readFile(new URL("../app/living-atlas.ts", import.meta.url), "utf8");
  const page = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
  const css = await readFile(new URL("../app/globals.css", import.meta.url), "utf8");

  assert.match(usgsRoute, /USGS_API_ORIGIN = "https:\/\/api\.waterdata\.usgs\.gov"/);
  assert.match(usgsRoute, /OGC_ROOT = "\/ogcapi\/v1\/collections"/);
  assert.match(usgsRoute, /latest-continuous\/items/);
  assert.match(usgsRoute, /continuous\/items/);
  assert.match(usgsRoute, /daily\/items/);
  assert.match(usgsRoute, /monitoring-locations\/items/);
  assert.match(usgsRoute, /ALLOWED_UPSTREAM_PATHS/);
  assert.match(usgsRoute, /NETWORK_STATION_CAP = 72/);
  assert.match(usgsRoute, /geographicallySpread/);
  assert.match(usgsRoute, /Network mode supports only range=24h and parameter 00060/);
  assert.match(usgsRoute, /const statisticId = daily \? "00003" : null/);
  assert.match(usgsRoute, /view uses USGS daily values with statistic 00003 \(daily mean\)/i);
  assert.doesNotMatch(usgsRoute, /searchParams\.get\("url"\)/);

  assert.match(streamflow, /STREAMFLOW_MAX_DISPLAY_FRAMES = 96/);
  assert.match(streamflow, /Returns a bounded sample of actual observation times; no synthetic timestamps are inserted/);
  assert.match(streamflow, /held only within the caller-declared tolerance and are never interpolated/);
  assert.match(streamflow, /Null values and time deltas larger[\s\S]*terminate a fragment instead of visually bridging missing data/);
  assert.match(streamflow, /interpolation: false/);

  assert.match(noaaRoute, /KANSAS_GAUGES_URL = `\$\{NWPS_BASE\}\/gauges\?bbox\.xmin=-102\.0517/);
  assert.match(noaaRoute, /type HydrologyMode = "network" \| "gauge" \| "reach"/);
  assert.match(noaaRoute, /OFFICIAL_NWS_OBSERVATION/);
  assert.match(noaaRoute, /OFFICIAL_NWS_FORECAST/);
  assert.match(noaaRoute, /analysis_assimilation/);
  assert.match(noaaRoute, /short_range/);
  assert.match(noaaRoute, /analysis\/assimilation is not a gauge observation/i);
  assert.match(noaaRoute, /short-range NWM output is not an official River Forecast Center forecast/i);
  assert.match(noaaRoute, /candidate === -999 \|\| candidate === -9999/);
  assert.doesNotMatch(noaaRoute, /searchParams\.get\("url"\)/);
  assert.match(noaaHydrology, /sourceRole: "OFFICIAL_NWS_OBSERVATION" \| "OFFICIAL_NWS_FORECAST"/);
  assert.match(noaaHydrology, /floodCategory: gauge\.observed\.floodCategory \?\? gauge\.forecast\.floodCategory/);

  assert.match(observatory, /aria-label="River Pulse streamflow observation controls"/);
  assert.match(observatory, /aria-label="Select an exact streamflow observation frame"/);
  assert.match(observatory, /Marker area uses a logarithmic ft³\/s scale/);
  assert.match(observatory, /Raw discharge is not a flood category/);
  assert.match(observatory, /Exact values · gaps break the path/);
  assert.match(observatory, /no value interpolation/);
  assert.match(page, /<HydrologyObservatory/);
  assert.match(page, /mode=station&range=\$\{requestedRange\}&station=\$\{encodeURIComponent\(stationId!\)\}&parameter=00060/);
  assert.match(page, /params\.set\("hydroRange"/);
  assert.match(page, /params\.set\("hydroStation"/);
  assert.match(css, /\.hydrology-observatory/);
  assert.match(css, /\.hydrology-chart-segment/);
  assert.match(livingAtlas, /Exact USGS samples \+ provider-current GIS/);
  assert.match(livingAtlas, /No gauge value is generalized to a reach or basin/);
});

test("the built hydrology adapters reject invalid query shapes before any upstream request", async () => {
  const workerUrl = new URL("../dist/server/index.js", import.meta.url);
  workerUrl.searchParams.set("test", `hydrology-invalid-${process.pid}-${Date.now()}`);
  const { default: worker } = await import(workerUrl.href);
  const originalFetch = globalThis.fetch;
  let upstreamCalls = 0;
  try {
    globalThis.fetch = async () => {
      upstreamCalls += 1;
      throw new Error("Invalid hydrology queries must not reach an upstream service.");
    };

    const usgsResponse = await worker.fetch(
      new Request("http://localhost/api/hydrology/streamflow?mode=network&range=1y&url=https://example.invalid"),
      {},
      { waitUntil() {}, passThroughOnException() {} },
    );
    assert.equal(usgsResponse.status, 400);
    const usgsError = await usgsResponse.json();
    assert.equal(usgsError.code, "USGS_STREAMFLOW_INVALID_QUERY");
    assert.equal(usgsError.interpolation, false);
    assert.equal(usgsError.evidenceRole, "EXTERNAL_CONTEXT_ONLY");

    const noaaResponse = await worker.fetch(
      new Request("http://localhost/api/hydrology/noaa?mode=gauge&lid=bad&url=https://example.invalid"),
      {},
      { waitUntil() {}, passThroughOnException() {} },
    );
    assert.equal(noaaResponse.status, 400);
    const noaaError = await noaaResponse.json();
    assert.equal(noaaError.error.code, "INVALID_LID");
    assert.equal(noaaError.recordCount, 0);
    assert.match(noaaError.limitation, /No synthetic, cached-stale, cross-source, or untimed fallback was used/);
    assert.equal(upstreamCalls, 0);
  } finally {
    globalThis.fetch = originalFetch;
  }
});

test("adds an exact-time NOAA nowCOAST radar loop and a fail-closed control surface", async () => {
  const radar = await readFile(new URL("../app/noaa-radar.ts", import.meta.url), "utf8");
  const route = await readFile(new URL("../app/api/noaa-radar/frames/route.ts", import.meta.url), "utf8");
  const liveContext = await readFile(new URL("../app/live-context.ts", import.meta.url), "utf8");
  const page = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
  const css = await readFile(new URL("../app/globals.css", import.meta.url), "utf8");

  assert.match(radar, /NOAA_RADAR_PRODUCT_ID = "conus_base_reflectivity_mosaic"/);
  assert.match(radar, /nowcoast\.noaa\.gov\/geoserver\/weather_radar\/wms\?service=WMS&version=1\.3\.0&request=GetCapabilities/);
  assert.match(radar, /rawTokens\.some\(\(value\) => value\.includes\("\/"\)\)/);
  assert.match(radar, /unsupported interval/);
  assert.match(radar, /requires an exact advertised observation timestamp/);
  assert.match(radar, /parameters\.push\(`time=\$\{encodeURIComponent\(normalized\)\}`\)/);
  assert.match(radar, /interpolation: false/);
  assert.match(route, /MAX_CAPABILITIES_BYTES = 512 \* 1024/);
  assert.match(route, /REQUEST_TIMEOUT_MS = 12_000/);
  assert.match(route, /did not match the fixed WMS contract/);
  assert.match(route, /No synthetic or untimed fallback was used/);
  assert.match(route, /"Cache-Control": "no-store"/);
  assert.doesNotMatch(route, /searchParams\.get\(|new URL\(request\.url\)/);
  assert.match(liveContext, /axis: "provider-observation-loop"/);
  assert.match(liveContext, /setNoaaRadarObservationTime/);
  assert.match(liveContext, /noaaRadarTileUrl\(observedAt\)/);
  assert.doesNotMatch([radar, route, liveContext].join("\n"), /opengeo\.ncep\.noaa\.gov|conus_bref_qcd/);

  assert.match(page, /aria-label="NOAA observed radar loop controls"/);
  assert.match(page, /aria-label="Previous NOAA radar observation"/);
  assert.match(page, /aria-label="Next NOAA radar observation"/);
  assert.match(page, /aria-label="Select an exact NOAA radar observation"/);
  assert.match(page, /<option value=\{30\}>30 min<\/option><option value=\{60\}>1 hour<\/option><option value=\{120\}>2 hours<\/option>/);
  assert.match(page, /<option value=\{0\.5\}>0\.5×<\/option><option value=\{1\}>1×<\/option><option value=\{2\}>2×<\/option>/);
  assert.match(page, /Reflectivity legend \+ source/);
  assert.match(page, /noaaRadarManifestIsFresh/);
  assert.match(page, /newest NOAA radar observation is more than 15 minutes old/i);
  assert.match(page, /Each source keeps its own observation or retrieval clock; visual overlap does not establish correlation, lag, direction, or causation/);
  assert.match(page, /A settled request means MapLibre reported no source error; it does not prove complete radar coverage/);
  assert.match(page, /noaaRadarPendingFrameTimeRef/);
  assert.match(page, /noaaRadarFrameFailureRef/);
  assert.match(page, /temporalQueryRef\.current\.frame !== OFFICIAL_CONTEXT_PRESENT_FRAME[\s\S]*NOAA radar remains held outside/);
  assert.match(page, /event\.sourceId !== OFFICIAL_CONTEXT_BY_ID\["nws-radar"\]\.sourceId \|\| !event\.tile \|\| !event\.isSourceLoaded/);
  assert.match(page, /if \(!noaaRadarObservationTimeIsApplied\(map, observedAt\)\) return/);
  assert.match(page, /pendingRadarFrame[\s\S]*noaaRadarFrameLoadCleanupRef\.current\?\.\(\)[\s\S]*setNoaaRadarFrameLoadState\("idle"\)[\s\S]*map\.setStyle/);
  assert.match(page, /Reduced motion is active\. Automatic looping is off/);
  assert.match(page, /times remain separate from the atlas year/);
  assert.match(css, /\.noaa-radar-loop/);
  assert.match(css, /\.noaa-radar-transport/);
  assert.match(css, /\.noaa-radar-legend/);
  assert.match(css, /@media \(max-width: 760px\)[\s\S]*\.noaa-radar-loop/);
});

test("checks current GitHub main through one fixed read-only backend route", async () => {
  const route = await readFile(new URL("../app/api/repository-status/route.ts", import.meta.url), "utf8");
  const page = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
  const layout = await readFile(new URL("../app/layout.tsx", import.meta.url), "utf8");
  const favicon = await readFile(new URL("../app/favicon.ico/route.ts", import.meta.url), "utf8");

  assert.match(route, /api\.github\.com\/repos\/\$\{REPOSITORY\}\/branches\/\$\{REF\}/);
  assert.match(route, /READ_ONLY_PUBLIC_METADATA/);
  assert.match(route, /SITE_SOURCE_SEPARATE/);
  assert.match(route, /MAX_RESPONSE_BYTES/);
  assert.doesNotMatch(route, /searchParams\.get\("url"\)/);
  assert.match(page, /LIVE READ-ONLY GITHUB CHECK/);
  assert.match(page, /no automatic code sync or mutation/i);
  assert.match(layout, /shortcut: "\/favicon\.ico"/);
  assert.match(favicon, /content-type.*image\/svg\+xml/i);
});

test("the built official-context adapter rejects unknown feeds without network access", async () => {
  const workerUrl = new URL("../dist/server/index.js", import.meta.url);
  workerUrl.searchParams.set("test", `official-${process.pid}-${Date.now()}`);
  const { default: worker } = await import(workerUrl.href);
  const response = await worker.fetch(new Request("http://localhost/api/live-context?feed=arbitrary"), {}, { waitUntil() {}, passThroughOnException() {} });
  assert.equal(response.status, 400);
  assert.match(await response.text(), /fixed allowlist/i);
});

test("the built NOAA radar adapter returns explicit observations and fails closed", async () => {
  const workerUrl = new URL("../dist/server/index.js", import.meta.url);
  workerUrl.searchParams.set("test", `radar-${process.pid}-${Date.now()}`);
  const { default: worker } = await import(workerUrl.href);
  const originalFetch = globalThis.fetch;
  const upstreamCalls = [];
  const capabilitiesUrl = "https://nowcoast.noaa.gov/geoserver/weather_radar/wms?service=WMS&version=1.3.0&request=GetCapabilities";
  const baseTime = Math.floor(Date.now() / 240_000) * 240_000;
  const expectedFrames = [-2, -1, 0].map((offset) => new Date(baseTime + offset * 240_000).toISOString());
  const xml = `<?xml version="1.0"?><WMS_Capabilities><Capability><Layer><Layer><Name>conus_base_reflectivity_mosaic</Name><Dimension name="time" default="${expectedFrames[2]}">${expectedFrames[2]},${expectedFrames[0]},${expectedFrames[1]}</Dimension></Layer></Layer></Capability></WMS_Capabilities>`;
  try {
    globalThis.fetch = async (input) => {
      upstreamCalls.push(String(input));
      return new Response(xml, { headers: { "content-type": "application/xml" } });
    };
    const readyResponse = await worker.fetch(new Request("http://localhost/api/noaa-radar/frames?url=https://example.invalid/untimed"), {}, { waitUntil() {}, passThroughOnException() {} });
    assert.equal(readyResponse.status, 200);
    const manifest = await readyResponse.json();
    assert.deepEqual(manifest.frames, expectedFrames);
    assert.equal(manifest.interpolation, false);
    assert.equal(manifest.evidenceRole, "EXTERNAL_CONTEXT_ONLY");
    assert.deepEqual(upstreamCalls, [capabilitiesUrl]);

    globalThis.fetch = async () => new Response("Unavailable", { status: 503, headers: { "content-type": "text/plain" } });
    const errorResponse = await worker.fetch(new Request("http://localhost/api/noaa-radar/frames?case=upstream-error"), {}, { waitUntil() {}, passThroughOnException() {} });
    assert.equal(errorResponse.status, 502);
    assert.equal(errorResponse.headers.get("cache-control"), "no-store");
    const error = await errorResponse.json();
    assert.equal(error.state, "error");
    assert.equal(error.code, "NOAA_RADAR_UNAVAILABLE");
    assert.equal(error.message, "NOAA radar frames are temporarily unavailable. No synthetic or untimed fallback was used.");
    assert.equal("frames" in error, false);
  } finally {
    globalThis.fetch = originalFetch;
  }
});

test("the built official-context adapter joins dated Census population and bounds USGS earthquakes", async () => {
  const workerUrl = new URL("../dist/server/index.js", import.meta.url);
  workerUrl.searchParams.set("test", `official-data-${process.pid}-${Date.now()}`);
  const { default: worker } = await import(workerUrl.href);
  const originalFetch = globalThis.fetch;
  const upstreamCalls = [];
  globalThis.fetch = async (input) => {
    const url = String(input);
    upstreamCalls.push(url);
    if (url.includes("tigerweb.geo.census.gov")) return new Response(JSON.stringify({
      type: "FeatureCollection",
      features: Array.from({ length: 105 }, (_, i) => ({ type: "Feature", geometry: { type: "Polygon", coordinates: [[[-98, 38], [-97, 38], [-97, 39], [-98, 39], [-98, 38]]] }, properties: { GEOID: `20${String(i * 2 + 1).padStart(3, "0")}`, BASENAME: `Fixture county ${i}`, STATE: "20", POP100: 6118, HU100: 2400, AREALAND: 2589988.110336, AREAWATER: 0 } })),
    }), { headers: { "content-type": "application/json" } });
    if (url.includes("api.census.gov")) return new Response(JSON.stringify([
      ["NAME", "DP05_0001E", "state", "county"],
      ["Ellsworth County, Kansas", "6118", "20", "053"],
    ]), { headers: { "content-type": "application/json" } });
    if (url.includes("earthquake.usgs.gov")) return new Response(JSON.stringify({
      type: "FeatureCollection",
      metadata: { count: 1 },
      features: [{ type: "Feature", id: "us-test", geometry: { type: "Point", coordinates: [-98.1, 38.7, 5.4] }, properties: { title: "M 2.1 - central Kansas", place: "central Kansas", mag: 2.1, magType: "ml", time: 1789000000000, updated: 1789000300000, status: "reviewed", type: "earthquake", url: "https://earthquake.usgs.gov/earthquakes/eventpage/us-test" } }],
    }), { headers: { "content-type": "application/json" } });
    throw new Error(`Unexpected upstream request: ${url}`);
  };
  try {
    const countyResponse = await worker.fetch(new Request("http://localhost/api/live-context?feed=census-counties"), {}, { waitUntil() {}, passThroughOnException() {} });
    assert.equal(countyResponse.status, 200);
    const countyPayload = await countyResponse.json();
    assert.equal(countyPayload.state, "ready");
    assert.equal(countyPayload.data.features[0].properties.populationEstimate, 6118);
    assert.equal(countyPayload.data.features[0].properties.populationEstimateYear, 2020);
    assert.equal(countyPayload.data.features.length, 105);
    assert.equal(countyPayload.data.features[0].properties.housingUnits, 2400);
    assert.equal(upstreamCalls.some((url) => url.includes("api.census.gov")), false);

    const earthquakeResponse = await worker.fetch(new Request("http://localhost/api/live-context?feed=usgs-earthquakes"), {}, { waitUntil() {}, passThroughOnException() {} });
    assert.equal(earthquakeResponse.status, 200);
    const earthquakePayload = await earthquakeResponse.json();
    assert.equal(earthquakePayload.featureCount, 1);
    assert.equal(earthquakePayload.data.features[0].properties.magnitude, 2.1);
    assert.equal(earthquakePayload.data.features[0].properties.depthKilometers, 5.4);
    assert.equal(upstreamCalls.some((url) => url.includes("eventtype=earthquake")), true);
    assert.equal(upstreamCalls.some((url) => url.includes("minlatitude=36.9") && url.includes("maxlongitude=-94.5")), true);
  } finally {
    globalThis.fetch = originalFetch;
  }
});

test("reviews and redacts public-safe exports before download", async () => {
  const ts = await import("typescript");
  const source = await readFile(new URL("../app/export-center.ts", import.meta.url), "utf8");
  const javascript = ts.transpileModule(source, {
    compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
    fileName: "export-center.ts",
  }).outputText;
  const exports = await import(`data:text/javascript;base64,${Buffer.from(javascript).toString("base64")}`);
  const temporalSweep = { mode: "snapshot", frame: 2026, rangeStart: 1885, rangeEnd: 2026, windowStart: 2026, stepRule: "available-events", interpolation: false };

  const protectedReview = exports.buildPublicSafeExport({
    exportedAt: "2026-08-24T18:30:00.000Z",
    locationCameraRedacted: true,
    view: { center: [-97.5, 38.5], zoom: 7, bearing: 0, pitch: 0 },
    projection: "mercator",
    basemap: "midnight",
    layerOrder: ["planning"],
    temporalSweep,
    workspace: "trust",
    layers: [{ id: "planning", title: "Planning", opacity: 1, attribution: "Site fixture", releaseState: "HELD", generalization: "Generalized", correction: "NONE" }],
    selection: {
      featureId: "protected-1",
      title: "Protected fixture",
      layerId: "planning",
      evidenceState: "DENIED_BY_POLICY",
      evidenceReference: "fixture:protected-1",
      temporalScope: "2026 fixture",
      sourceYear: 2026,
      temporalMode: "exact",
      sourceTime: "2026",
      releaseTime: "UNRELEASED",
      lastUpdate: "2026-08-24",
      reviewState: "HELD",
      releaseState: "HELD",
      correctionState: "NONE",
      geometry: { type: "Point", coordinates: [-97.5, 38.5] },
      generalization: "Generalized",
    },
  });

  assert.equal(protectedReview.payload.format, "kfm-public-safe-map-export-v2");
  assert.equal(protectedReview.payload.map.center, "WITHHELD_BROWSER_LOCATION");
  assert.equal(protectedReview.payload.selection.geometry, "WITHHELD_BY_POLICY");
  assert.equal(protectedReview.withheldFeatureCount, 1);
  assert.equal(protectedReview.downloadAllowed, true);

  const blockedReview = exports.buildPublicSafeExport({
    ...protectedReview.payload,
    exportedAt: "2026-08-24T18:31:00.000Z",
    locationCameraRedacted: false,
    view: { center: [-97.5, 38.5], zoom: 7, bearing: 0, pitch: 0 },
    projection: "mercator",
    basemap: "midnight",
    layerOrder: ["planning"],
    temporalSweep,
    workspace: "trust",
    layers: [{ id: "planning", title: "Planning", opacity: 1, attribution: "", releaseState: "HELD", generalization: "Generalized", correction: "NONE" }],
    selection: null,
  });
  assert.equal(blockedReview.downloadAllowed, false);
  assert.equal(blockedReview.checks.find((check) => check.id === "attribution").state, "BLOCK");
});

test("binds a governed temporal sweep to map filters, live-source holds, comparison, stories, and exports", async () => {
  const page = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
  const runtime = await readFile(new URL("../app/map-runtime.ts", import.meta.url), "utf8");
  const liveContext = await readFile(new URL("../app/live-context.ts", import.meta.url), "utf8");
  const exportCenter = await readFile(new URL("../app/export-center.ts", import.meta.url), "utf8");
  const workspaceModel = await readFile(new URL("../app/workspace-model.ts", import.meta.url), "utf8");
  const snapshotMap = await readFile(new URL("../app/snapshot-map.tsx", import.meta.url), "utf8");
  const css = await readFile(new URL("../app/globals.css", import.meta.url), "utf8");

  assert.match(page, /SEMANTIC TIME SWEEP/);
  assert.match(page, /applyTemporalRegistryFilters/);
  assert.match(page, /setTemporalMode\("snapshot"\)[\s\S]+selectStoredFeature\(example\.layerId/);
  assert.match(page, /selection\.kind !== "registry"[\s\S]+filter === "ALL"/);
  assert.match(page, /officialContextIdForSelection/);
  assert.match(page, /aria-current=\{step === temporalQuery\.frame \? "step" : undefined\}/);
  assert.match(runtime, /map\.setFilter\(renderer\.id, filter \?\? null\)/);
  assert.match(liveContext, /OFFICIAL_CONTEXT_TEMPORAL_SUPPORT/);
  assert.match(liveContext, /supportedFrames\.includes\(frame\)/);
  assert.match(exportCenter, /sweepMode: input\.temporalSweep\.mode/);
  assert.match(exportCenter, /interpolation: input\.temporalSweep\.interpolation/);
  assert.match(workspaceModel, /temporalSweep\?: Readonly/);
  assert.match(snapshotMap, /temporalQueryForSnapshot/);
  assert.match(snapshotMap, /applyRegistryState\([\s\S]+query\.frame[\s\S]+query\)/);
  assert.match(css, /\.timeline-sweep-setup/);
});

test("keeps the complete function inventory three-axis and runtime seam fail closed", async () => {
  const ts = await import("typescript");
  const registrySource = await readFile(new URL("../app/function-registry.ts", import.meta.url), "utf8");
  const seamSource = await readFile(new URL("../app/runtime-seam.ts", import.meta.url), "utf8");
  const page = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
  const compile = (source, fileName) => ts.transpileModule(source, {
    compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
    fileName,
  }).outputText;
  const registry = await import(`data:text/javascript;base64,${Buffer.from(compile(registrySource, "function-registry.ts")).toString("base64")}`);
  const seam = await import(`data:text/javascript;base64,${Buffer.from(compile(seamSource, "runtime-seam.ts")).toString("base64")}`);

  assert.equal(registry.FUNCTION_REGISTRY.some((record) => record.title === "Export" && record.maturity === "IMPLEMENTED"), true);
  assert.equal(registry.FUNCTION_REGISTRY.some((record) => record.title === "Compare" && record.state === "GATED"), true);
  assert.equal(registry.MAP_FUNCTIONS.length, 20);
  assert.equal(registry.SITE_EXTENSION_FUNCTIONS.length, 9);
  assert.equal(registry.OPERATIONAL_HANDOFFS.length, 6);
  assert.equal(registry.FUNCTION_REGISTRY.length, 35);
  assert.equal(new Set(registry.FUNCTION_REGISTRY.map((record) => record.id)).size, 35);
  assert.equal(registry.MAP_FUNCTIONS.every((record) => record.inventory === "MAP FUNCTION MATRIX"), true);
  assert.equal(registry.MAP_FUNCTIONS.some((record) => record.id === "hover-summary" && record.maturity === "NOT IMPLEMENTED"), true);
  assert.equal(registry.MAP_FUNCTIONS.some((record) => record.id === "story-node" && record.state === "BOUNDED"), true);
  assert.equal(registry.functionsForGroup("OPERATIONAL_HANDOFF").every((record) => record.action === "COPY_HANDOFF"), true);
  assert.equal(seam.runtimeSeamStepForSelection(null).state, "ABSTAINED");
  assert.equal(seam.runtimeSeamStepForSelection("DENIED_BY_POLICY").state, "DENIED");
  assert.equal(seam.runtimeSeamStepForSelection("SOURCE_STALE").state, "STALE");
  assert.equal(seam.runtimeSeamStepForSelection("ERROR").state, "ERROR");
  assert.equal(seam.runtimeSeamStepForSelection("ANSWER").state, "READY");
  assert.match(page, /Function and interface navigator/);
  assert.match(page, /record\.action === "OPEN_TIMELINE"/);
  assert.match(page, /All 38 repository feature families/);
  assert.match(page, /Compose/);
  assert.match(page, /<Link className="about-action"/);
  assert.match(page, /ANALYSIS_RECIPES/);
});

test("keeps the feature, connection, action, and coding registries aligned", async () => {
  const features = await readFile(new URL("../app/site-features.ts", import.meta.url), "utf8");
  const connections = await readFile(new URL("../app/site-connections.ts", import.meta.url), "utf8");
  const actions = await readFile(new URL("../app/site-actions.ts", import.meta.url), "utf8");
  const architecture = await readFile(new URL("../app/site-architecture.ts", import.meta.url), "utf8");
  const registry = await readFile(new URL("../app/site-registry.ts", import.meta.url), "utf8");
  const page = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
  const docs = await readFile(new URL("../docs/SITE_FEATURE_CONNECTION_ACTION_MAP.md", import.meta.url), "utf8");

  assert.match(features, /id: "earthquake-seismic-context"/);
  assert.match(features, /id: "hydrology-river-pulse"/);
  assert.match(features, /id: "smoke-weather-context"/);
  assert.match(features, /id: "held-raspberry-waveform-bridge"/);
  assert.match(connections, /CONNECTION_CODE_PATHS/);
  assert.match(connections, /"usgs-earthquakes"/);
  assert.match(connections, /"usgs-streamflow"/);
  assert.match(connections, /"noaa-hms-smoke"/);
  assert.match(connections, /"raspberry-shake-stations"/);
  assert.match(actions, /id: "toggle-context-group"/);
  assert.match(actions, /id: "refresh-streamflow"/);
  assert.match(actions, /id: "refresh-radar-frames"/);
  assert.match(actions, /id: "open-provider-source"/);
  assert.match(architecture, /id: "registry-and-alignment"/);
  assert.match(architecture, /route: "\/api\/live-context"/);
  assert.match(registry, /SITE_REGISTRY_VERSION = "kfm-site-registry-v1"/);
  assert.match(registry, /validateSiteRegistry/);
  assert.match(page, /SITE_REGISTRY_COUNTS.features/);
  assert.match(page, /SITE_REGISTRY_COUNTS.connections/);
  assert.match(page, /SITE_REGISTRY_COUNTS.actions/);
  assert.match(docs, /Alignment contract/);
  assert.match(docs, /Held ideas intentionally scaffolded/);
});

test("keeps the complete Layer Catalog reachable in one scroll surface", async () => {
  const page = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
  const css = await readFile(new URL("../app/globals.css", import.meta.url), "utf8");

  assert.match(page, /Layers <b>\{visibleOfficialCount\}\/\{OFFICIAL_CONTEXT_SOURCES\.length\}<\/b>/);
  assert.match(page, /className="catalog-section-jump"/);
  assert.match(page, /href="#catalog-layer-stack"/);
  assert.match(page, /href="#priority-context-title"/);
  assert.match(page, /Earthquake · water · smoke/);
  assert.match(page, /id="catalog-layer-stack"/);
  assert.match(page, /Registered layers <span>\{filteredLayerIds\.size\}\/\{LAYER_REGISTRY\.length\}<\/span>/);
  assert.match(css, /\.layer-catalog-body \{[^}]*overflow-y: auto/);
  assert.match(css, /\.catalog-groups \{ flex: none; min-height: auto; overflow: visible;/);
  assert.match(css, /\.official-context-catalog \{ flex: none; min-height: 0; overflow: hidden;/);
  assert.match(css, /\.catalog-layer-stack-actions/);
});

test("carries governed map context into creation workflows and checked source portals", async () => {
  const page = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
  const sources = await readFile(new URL("../app/source-intelligence.ts", import.meta.url), "utf8");
  const workspaceModel = await readFile(new URL("../app/workspace-model.ts", import.meta.url), "utf8");
  const workspaces = await readFile(new URL("../app/report-story-workspaces.tsx", import.meta.url), "utf8");
  const css = await readFile(new URL("../app/globals.css", import.meta.url), "utf8");

  assert.match(page, /Map context ready/);
  assert.match(page, /Create evidence report/);
  assert.match(page, /Create guided story/);
  assert.match(page, /Inspect connected sources/);
  assert.match(page, /DRAFT · NOT PUBLISHED/);
  assert.match(page, /setReportLayerIds\(activeLayers\.map/);
  assert.match(sources, /sourceUrl: string/);
  assert.match(sources, /checkedAt: string/);
  assert.match(sources, /SourceAdmissionState/);
  for (const state of ["candidate", "context-only", "admitted", "held", "quarantined", "denied"]) {
    assert.match(sources, new RegExp(`"${state}"`));
  }
  assert.match(sources, /https:\/\/kgs\.ku\.edu\/data-and-maps/);
  assert.match(sources, /https:\/\/www\.ksdot\.gov\/about\/our-organization\/divisions\/planning-and-development\/kansas-maps-and-gis-resources/);
  for (const type of ["SourceDescriptor", "EvidenceRecord", "TemporalExtent", "MapSnapshot", "ReportDraft", "StoryScene", "PolicyDecision", "TrustState"]) {
    assert.match(workspaceModel, new RegExp(`(?:interface|type) ${type}`));
  }
  assert.match(workspaceModel, /Trust in the map/);
  assert.match(workspaceModel, /Protected detail fails closed/);
  assert.match(workspaces, /Export Markdown/);
  assert.match(workspaces, /Export JSON/);
  assert.match(workspaces, /DRAFT · NOT PUBLISHED/);
  assert.match(workspaces, /localStorage/);
  assert.match(css, /\.map-context-card/);
  assert.match(css, /\.source-admission-legend/);
  assert.match(css, /\.source-candidate-card footer a/);
});
