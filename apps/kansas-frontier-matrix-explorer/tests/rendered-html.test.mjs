import assert from "node:assert/strict";
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
  assert.match(html, /synthetic and generalized demonstration layers/i);
  assert.match(html, /Repository briefing/i);
  assert.match(html, /main@(?:<!-- -->)?1ea6593/i);
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
  const temporalComparison = await readFile(new URL("../app/temporal-comparison.ts", import.meta.url), "utf8");
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
  assert.match(temporalComparison, /kfm-temporal-catalog-comparison-v1/);
  assert.match(source, /Catalog availability comparison/);
  assert.match(source, /const matchesReportRecord = useCallback/);
  assert.match(source, /matchesReportRecord\(layer, feature\.properties\)/);
  assert.match(source, /reportScope === "SELECTION"\s*\n\s*\|\| isFeatureAvailableAtTime/);
  assert.match(source, /\[matchesReportRecord, reportLayerIds, reportScope, year\]/);
  assert.match(source, /outsideActiveTime: !isFeatureAvailableAtTime/);
  assert.match(source, /matchedRecords: reportActiveTimeRecordCount/);
  assert.match(source, /retainedSelectionRecords: reportRetainedSelectionCount/);
  assert.match(source, /RETAINED_OUTSIDE_ACTIVE_TIME/);
  assert.match(source, /excluded from the active-time match count/);
  assert.match(source, /const reportIncludedRecordCount = Math\.min\(reportRecords\.length, reportRecordLimit\)/);
  assert.match(source, /reportRecords\.slice\(0, reportRecordLimit\)/);
  assert.match(source, /report copied with \$\{reportIncludedRecordCount\} included records/);
  assert.match(source, /report downloaded with \$\{reportIncludedRecordCount\} included records/);
  assert.doesNotMatch(source, /reportRecords\.length} included records/);
  assert.match(source, /}\n    params\.set\("times",/);
  assert.match(source, /setReportLayerIds\(activeLayers\.map/);
  assert.match(source, /const \[leftOpen, setLeftOpen\] = useState\(false\)/);
  assert.match(about, /Start with a question, finish with a report/);
  assert.match(about, /EVIDENCE STATES/);
  assert.match(css, /\.report-builder-grid/);
  assert.match(css, /\.temporal-compare-lab/);
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

  assert.equal(recipes.ANALYSIS_RECIPES.length, 8);
  assert.equal(recipes.ANALYSIS_RECIPES.every((recipe) => recipe.layerIds.every((id) => id === "county-starter-points" || Boolean(layer(id)))), true);
  assert.equal(layer("water-context").data.features.length, 4);
  assert.equal(layer("agriculture-context").data.features.length, 3);
  assert.equal(layer("communities").data.features.length, 12);
  assert.equal(layer("transport-context").data.features.length, 2);
  assert.match(page, /kfm-map-workspaces-v1/);
  assert.match(page, /saveCurrentWorkspace/);
  assert.match(page, /loadSavedWorkspace/);
  assert.match(page, /temporalComparison/);
  assert.match(page, /locationCameraRedacted\?: boolean/);
  assert.match(page, /locationCameraRedacted: locationCameraRedacted \|\| locationDerivedViewRef\.current/);
  assert.match(page, /snapshot\.locationCameraRedacted !== false/);
  assert.match(page, /locationDerivedViewRef\.current = restoredLocationCameraRedaction/);
  assert.match(page, /setLocationCameraRedacted\(restoredLocationCameraRedaction\)/);
  assert.match(page, /reportEvidenceFilter/);
  assert.match(page, /handleWorkspaceShortcut/);
  assert.match(page, /shortcut R/);
  assert.match(css, /\.analysis-recipes/);
  assert.match(css, /\.saved-workspace-list/);
  assert.match(css, /\.report-active-filters/);
});

test("adds bounded renderer-neutral smoke, water, elevation, tile, and scene navigation features", async () => {
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

  assert.equal(explorer.LAYER_REGISTRY.length, 15);
  assert.equal(layer("watershed-context").data.features.length, 3);
  assert.equal(layer("smoke-context").data.features.length, 3);
  assert.equal(layer("elevation-concept").data.features.length, 6);
  assert.equal(layer("tile-matrix-grid").data.features.length, 24);
  assert.equal(layer("water-context").sourceOptions.lineMetrics, true);
  assert.match(explorerSource, /"line-gradient"/);
  assert.match(explorerSource, /type: "fill-extrusion"/);
  assert.match(explorerSource, /not observed smoke, a forecast, an advisory/i);
  assert.match(explorerSource, /not a fetched vector tile, PMTiles archive/i);
  assert.match(runtime, /lngLatToTile/);
  assert.match(runtime, /SCENE_ENVIRONMENTS/);
  assert.doesNotMatch(runtime, /setElevationExaggeration|applySceneEnvironment|setSky|setLight|maplibre-gl|addSource|addLayer/);
  assert.match(page, /SCENE \+ 3D LAB/);
  assert.match(page, /Relative vertical scale/);
  assert.match(page, /Renderer-neutral globe overview/);
  assert.match(page, /reversible 90° renderer-neutral camera turn/);
  assert.match(page, /No PMTiles, MVT, COG, or DEM fetch/);
  assert.match(page, /createNullMapRuntime/);
  assert.doesNotMatch(page, /NavigationControl|FullscreenControl|setVerticalFieldOfView|querySourceFeatures|\bmapRef\.current|from "maplibre-gl"|new maplibregl/);
  assert.match(page, /aria-label="Unified map controls"/);
  assert.match(page, /SOURCE CONNECTIONS/);
  assert.match(page, /Inspect fixture/);
  assert.match(page, /params\.set\("scene"/);
  assert.match(page, /params\.set\("zscale"/);
  assert.match(page, /params\.set\("sky"/);
  assert.match(page, /params\.set\("fov"/);
  assert.match(mapInterface, /Terrain \+ hillshade[\s\S]*HOLD/);
  assert.match(mapInterface, /Offline \/ PMTiles[\s\S]*HOLD/);
  assert.match(css, /\.scene-preset-grid/);
  assert.match(css, /\.scene-tile-ledger/);
  assert.match(css, /\.source-connection-card/);
  assert.match(css, /\.scene-environment-grid/);
});

test("adds a renderer-neutral area-of-interest workflow and browser-local camera history", async () => {
  const page = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
  const runtime = await readFile(new URL("../app/map-runtime.ts", import.meta.url), "utf8");
  const mapInterface = await readFile(new URL("../app/map-interface.ts", import.meta.url), "utf8");
  const css = await readFile(new URL("../app/globals.css", import.meta.url), "utf8");

  assert.doesNotMatch(runtime, /kfm-analysis-area|addSource|addLayer/);
  assert.match(page, /"ANALYSIS_AREA"/);
  assert.match(page, /captureAnalysisArea/);
  assert.match(page, /Locked the current renderer-neutral view bounds as the report area of interest/);
  assert.match(page, /params\.set\("aoi"/);
  assert.match(page, /cameraHistoryRef/);
  assert.match(page, /travelCameraHistory/);
  assert.match(page, /Previous view/);
  assert.match(page, /compatible_record_count/);
  assert.match(page, /startAreaDraw/);
  assert.match(page, /kfm-site-spatial-query-plan-v1/);
  assert.match(page, /FOCUS_POINT_INSIDE_BOUNDS/);
  assert.match(page, /rendererHitsAreEvidence: false/);
  assert.match(css, /\.analysis-area-card/);
  assert.match(css, /\.map-query-surface/);
  assert.match(css, /\.report-map-query/);
  assert.match(mapInterface, /Terrain \+ hillshade[\s\S]*HOLD/);
  assert.match(mapInterface, /Offline \/ PMTiles[\s\S]*HOLD/);
});

test("converts a reversible screen box into a bounded geographic query envelope", async () => {
  const ts = await import("typescript");
  const source = await readFile(new URL("../app/map-runtime.ts", import.meta.url), "utf8");
  const javascript = ts.transpileModule(source, {
    compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
    fileName: "map-runtime.ts",
  }).outputText;
  const runtime = await import(`data:text/javascript;base64,${Buffer.from(javascript).toString("base64")}`);

  assert.deepEqual(runtime.screenRectToBounds(
    { startX: 80, startY: 90, endX: 20, endY: 10 },
    { width: 100, height: 100 },
    { west: -100, south: 30, east: -90, north: 40 },
  ), { west: -98, south: 31, east: -92, north: 39 });
  assert.equal(runtime.screenRectToBounds(
    { startX: 10, startY: 10, endX: 15, endY: 15 },
    { width: 100, height: 100 },
    { west: -100, south: 30, east: -90, north: 40 },
  ), null);
  assert.equal(runtime.screenRectToBounds(
    { startX: 10, startY: 10, endX: 80, endY: 80 },
    { width: 0, height: 100 },
    { west: -100, south: 30, east: -90, north: 40 },
  ), null);
});

test("adds a no-upload KML and GeoJSON inspection preview without admission or renderer effects", async () => {
  const ts = await import("typescript");
  const importSource = await readFile(new URL("../app/import-preview.ts", import.meta.url), "utf8");
  const page = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
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
    inspectedAt: "2026-08-30T18:31:00.000Z",
    supportedBounds: { west: -104.8, south: 34.8, east: -92, north: 42.2 },
    text: JSON.stringify({
      type: "FeatureCollection",
      features: [
        { type: "Feature", properties: {}, geometry: { type: "Point", coordinates: [[-98, 38]] } },
        { type: "Feature", properties: {}, geometry: { type: "LineString", coordinates: [[-98, 38]] } },
        { type: "Feature", properties: {}, geometry: { type: "Polygon", coordinates: [[[-99, 37], [-98, 37], [-98, 38], [-99, 38]]] } },
      ],
    }),
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
    inspectedAt: "2026-08-30T18:32:00.000Z",
    supportedBounds: { west: -104.8, south: 34.8, east: -92, north: 42.2 },
    text: largeText,
  });
  assert.deepEqual(largePreview.bounds, [-98.5, 38.5, -98.4, 38.5]);

  const kmlPreview = imports.buildLocalImportPreview({
    fileName: "local.kml",
    fileSizeBytes: 800,
    inspectedAt: "2026-08-30T18:33:00.000Z",
    supportedBounds: { west: -104.8, south: 34.8, east: -92, north: 42.2 },
    text: `<?xml version="1.0"?><kml xmlns="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom"><Document><atom:author><atom:name>Synthetic fixture</atom:name></atom:author><NetworkLink><Link><href>https://example.invalid/held.kml</href></Link></NetworkLink><Placemark><name>Local point</name><description><![CDATA[<b>not HTML</b>]]></description><ExtendedData><SchemaData><SimpleData name="owner">Synthetic owner</SimpleData></SchemaData></ExtendedData><Point><coordinates>-98.4,38.5</coordinates></Point></Placemark></Document></kml>`,
  });
  assert.equal(kmlPreview.featureCount, 1);
  assert.equal(kmlPreview.unsupportedElementCount, 1);
  assert.equal(kmlPreview.externalReferenceCount, 1);
  assert.equal(kmlPreview.attribution, "Synthetic fixture");
  assert.deepEqual(kmlPreview.sensitivitySignals, ["owner"]);
  assert.match(importSource, /KML/);
  assert.match(importSource, /NetworkLink/);
  assert.doesNotMatch(importSource, /DOMParser|Math\.min\(\.\.\.positions/);
  assert.match(page, /LOCAL IMPORT PREVIEW/);
  assert.match(page, /Temporary Places, KFM-style/);
  assert.match(page, /accept="\.kml,\.geojson,\.json/);
  assert.match(page, /importInspectionGenerationRef/);
  assert.match(page, /inspectionGeneration !== importInspectionGenerationRef\.current/);
  assert.match(page, /No geometry overlay is rendered/);
  assert.match(page, /locationDerivedViewRef\.current = true;\s*setLocationCameraRedacted\(true\);\s*fitRendererNeutralBounds/);
  assert.match(page, /const redactWorkspaceCamera = locationCameraRedacted \|\| locationDerivedViewRef\.current/);
  assert.match(page, /view: redactWorkspaceCamera\s*\?/);
  assert.match(page, /WITHHELD · browser-local geometry/);
  assert.doesNotMatch(page, /Show preview|Hide preview|importPreviewVisible/);
  assert.doesNotMatch(page, /updateImportPreviewSource|from "maplibre-gl"|new maplibregl/);
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

test("builds an explicit Time A and Time B catalog-availability comparison", async () => {
  const ts = await import("typescript");
  const temporalSource = await readFile(new URL("../app/temporal-comparison.ts", import.meta.url), "utf8");
  const explorerSource = await readFile(new URL("../app/explorer-data.ts", import.meta.url), "utf8");
  const inlineTemporalSource = temporalSource.replace(
    'import { isFeatureAvailableAtTime } from "./map-interface";',
    'const isFeatureAvailableAtTime = (layer, featureYear, activeYear) => !layer.temporal || (layer.temporal.mode === "exact" ? featureYear === activeYear : featureYear <= activeYear);',
  );
  const compile = (source, fileName) => ts.transpileModule(source, {
    compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
    fileName,
  }).outputText;
  const temporal = await import(`data:text/javascript;base64,${Buffer.from(compile(inlineTemporalSource, "temporal-comparison.ts")).toString("base64")}`);
  const explorer = await import(`data:text/javascript;base64,${Buffer.from(compile(explorerSource, "explorer-data.ts")).toString("base64")}`);
  const layers = explorer.LAYER_REGISTRY.filter((layer) => ["historical-context", "atmosphere-observations"].includes(layer.id));
  const comparison = temporal.buildTemporalComparison(layers, 1910, 2026);

  assert.equal(comparison.format, "kfm-temporal-catalog-comparison-v1");
  assert.equal(comparison.authority, "SITE_LOCAL_CONTEXT_ONLY");
  assert.equal(comparison.interpretation, "CATALOG_AVAILABILITY_NOT_OBSERVED_CHANGE");
  assert.equal(comparison.timeA, 1910);
  assert.equal(comparison.timeB, 2026);
  assert.equal(comparison.changedLayerCount > 0, true);
  assert.equal(comparison.layers.length, 2);
  assert.match(comparison.limitations.join(" "), /does not detect real-world change/);

  const deniedComparison = temporal.buildTemporalComparison(layers, 1910, 2026, () => false);
  assert.equal(deniedComparison.timeARecordCount, 0);
  assert.equal(deniedComparison.timeBRecordCount, 0);
  assert.equal(deniedComparison.changedLayerCount, 0);
});

test("uses a site-specific social card and request-host metadata", async () => {
  const layout = await readFile(new URL("../app/layout.tsx", import.meta.url), "utf8");
  const socialCard = await readFile(new URL("../public/og-guided.png", import.meta.url));

  assert.match(layout, /x-forwarded-host/);
  assert.match(layout, /new URL\("\/og-guided\.png", metadataBase\)/);
  assert.match(layout, /Synthetic and generalized demonstration data only/);
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
  assert.match(source, /Renderer acquisition is held/);
  assert.match(source, /clamp\(parseNumber\(params\.get\("z"\), KANSAS_VIEW\.zoom\), 4, 16\)/);
  assert.match(source, /value === null \|\| value\.trim\(\) === ""/);
  assert.match(source, /params\.has\("l"\)/);
  assert.match(source, /LAYER_REGISTRY\.map\(\(layer\) => `\$\{layer\.id\}:\$\{\(opacity/);
  assert.match(source, /const params = buildExplorerParams\(\)/);
  assert.doesNotMatch(source, /window\.history\.pushState/);
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

  assert.match(updates, /1ea6593ede80d5ce10f561c7eec72135d6ccf806/);
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

test("keeps the renderer-neutral Workbench complete, bounded, and fail closed", async () => {
  const source = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
  const mapInterface = await readFile(new URL("../app/map-interface.ts", import.meta.url), "utf8");
  const exportCenter = await readFile(new URL("../app/export-center.ts", import.meta.url), "utf8");
  const explorerData = await readFile(new URL("../app/explorer-data.ts", import.meta.url), "utf8");
  const runtime = await readFile(new URL("../app/map-runtime.ts", import.meta.url), "utf8");
  const css = await readFile(new URL("../app/globals.css", import.meta.url), "utf8");
  const packageJson = JSON.parse(await readFile(new URL("../package.json", import.meta.url), "utf8"));
  const buildScript = await readFile(new URL("../scripts/build-verified.sh", import.meta.url), "utf8");
  const installScript = await readFile(new URL("../scripts/install-ci.sh", import.meta.url), "utf8");
  const tsconfig = await readFile(new URL("../tsconfig.json", import.meta.url), "utf8");
  const viteConfig = await readFile(new URL("../vite.config.ts", import.meta.url), "utf8");

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
  assert.match(source, /createNullMapRuntime/);
  assert.match(source, /DIRECT_CONSUMER_MIGRATION_HOLD/);
  assert.match(source, /Renderer HOLD · MapLibre candidate/);
  assert.match(source, /runtime_assets: "NOT_RUN"/);
  assert.match(source, /map_constructed: false/);
  assert.match(source, /MapLibre \{EXPECTED_MAPLIBRE_VERSION\} acquisition boundary/);
  assert.doesNotMatch(source, /from "maplibre-gl"|import\("maplibre-gl"\)|new maplibregl/);
  assert.doesNotMatch(explorerData, /from "maplibre-gl"/);
  assert.doesNotMatch(css, /maplibre-gl\/dist|\.maplibregl-/);
  assert.equal(Object.hasOwn(packageJson.dependencies, "@kfm/maplibre"), false);
  assert.equal(Object.hasOwn(packageJson.dependencies, "maplibre-gl"), false);
  assert.match(runtime, /Renderer-neutral high-contrast preference descriptor/);
  assert.doesNotMatch(runtime, /maplibre-gl|addSource|addLayer|setFilter/);
  assert.match(buildScript, /exec bash "\$\{script_dir\}\/sites-env\.sh"/);
  assert.match(installScript, /exec bash "\$\{script_dir\}\/sites-env\.sh"/);
  assert.match(tsconfig, /"target": "ES2022"/);
  assert.match(tsconfig, /"@kfm\/maplibre": \["\.\.\/\.\.\/packages\/maplibre\/src\/index\.ts"\]/);
  assert.match(viteConfig, /find: "@kfm\/maplibre"/);
  assert.match(viteConfig, /packages\/maplibre\/src\/index\.ts/);
  assert.match(source, /FULL TEMPORAL CAPACITY · 4\.54 GA BP TO 2026/);
  assert.match(source, /Deep-time and intermediate ticks are capacity markers, not claims/);
  assert.match(source, /TIMELINE_JUMPS/);
  assert.match(explorerData, /-4_540_000_000/);
  assert.match(explorerData, /-541_000_000/);
  assert.match(explorerData, /-11_700/);
  assert.match(source, /mapQueryCandidates/);
  assert.match(source, /time_compatible: !selectedTimeMismatch/);
  assert.match(source, /renderer hit testing remains held/);
  assert.match(source, /ACTIVE LAYERS AVAILABLE/);
  assert.match(mapInterface, /Renderer architecture[\s\S]*ACCEPTED/);
  assert.match(mapInterface, /MapRuntimePort \+ Null runtime[\s\S]*VERIFIED SLICE/);
  assert.match(mapInterface, /Dependency admission[\s\S]*EXACT 6\.6\.0/);
  assert.match(mapInterface, /Concrete MapLibre adapter[\s\S]*VERIFIED SLICE/);
  assert.match(mapInterface, /Sites renderer consumer[\s\S]*NULL RUNTIME \/ HOLD/);
  assert.match(mapInterface, /Browser readiness[\s\S]*HOLD/);
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

test("keeps source discovery separate from admission and renderer descriptors inert", async () => {
  const sources = await readFile(new URL("../app/source-intelligence.ts", import.meta.url), "utf8");
  const runtime = await readFile(new URL("../app/map-runtime.ts", import.meta.url), "utf8");

  assert.match(sources, /Source discovery is not source admission/);
  assert.match(sources, /KFM Full Atlas Seed Cards/);
  assert.match(sources, /sourceCount: 12/);
  assert.match(sources, /DEFER DEPENDENCY/);
  assert.match(sources, /National Flood Hazard Layer/);
  assert.match(runtime, /BasemapDescriptor/);
  assert.match(runtime, /Renderer-neutral high-contrast preference descriptor/);
  assert.doesNotMatch(runtime, /addSource|addLayer|setLayerZoomRange/);
});

test("reviews and redacts public-safe exports before download", async () => {
  const ts = await import("typescript");
  const source = await readFile(new URL("../app/export-center.ts", import.meta.url), "utf8");
  const javascript = ts.transpileModule(source, {
    compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
    fileName: "export-center.ts",
  }).outputText;
  const exports = await import(`data:text/javascript;base64,${Buffer.from(javascript).toString("base64")}`);

  const protectedReview = exports.buildPublicSafeExport({
    exportedAt: "2026-08-24T18:30:00.000Z",
    locationCameraRedacted: true,
    view: { center: [-97.5, 38.5], zoom: 7, bearing: 0, pitch: 0 },
    projection: "mercator",
    basemap: "midnight",
    layerOrder: ["planning"],
    activeYear: 2026,
    workspace: "trust",
    layers: [{ id: "planning", title: "Planning", opacity: 1, attribution: "Site fixture", releaseState: "RESTRICTED", generalization: "Generalized", correction: "NONE" }],
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
      releaseState: "RESTRICTED",
      layerReleaseState: "RESTRICTED",
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

  const supportedRestrictedRecordInput = {
    exportedAt: "2026-08-24T18:30:30.000Z",
    locationCameraRedacted: false,
    view: { center: [-97.5, 38.5], zoom: 7, bearing: 0, pitch: 0 },
    projection: "mercator",
    basemap: "midnight",
    layerOrder: ["fauna-sensitive"],
    activeYear: 2026,
    workspace: "trust",
    layers: [{ id: "fauna-sensitive", title: "Sensitive Fauna", opacity: 1, attribution: "Synthetic fixture", releaseState: "DEMONSTRATION", generalization: "None", correction: "NONE" }],
    selection: {
      featureId: "fauna-restricted-record",
      title: "Restricted Fauna record",
      layerId: "fauna-sensitive",
      evidenceState: "ANSWER",
      evidenceReference: "fixture:fauna-restricted-record",
      temporalScope: "2026 fixture",
      sourceYear: 2026,
      temporalMode: "exact",
      sourceTime: "2026",
      releaseTime: "UNRELEASED",
      lastUpdate: "2026-08-24",
      reviewState: "REVIEWED",
      releaseState: "RESTRICTED",
      layerReleaseState: "DEMONSTRATION",
      correctionState: "NONE",
      geometry: { type: "Point", coordinates: [-97.5, 38.5] },
      generalization: "Exact geometry must not travel.",
    },
  };
  const restrictedRecordReview = exports.buildPublicSafeExport(supportedRestrictedRecordInput);
  assert.equal(restrictedRecordReview.payload.selection.geometry, "WITHHELD_BY_POLICY");
  assert.equal(restrictedRecordReview.withheldFeatureCount, 1);
  assert.equal(restrictedRecordReview.checks.find((check) => check.id === "selection").state, "REDACTED");

  const restrictedLayerReview = exports.buildPublicSafeExport({
    ...supportedRestrictedRecordInput,
    layers: [{ ...supportedRestrictedRecordInput.layers[0], releaseState: "RESTRICTED" }],
    selection: {
      ...supportedRestrictedRecordInput.selection,
      featureId: "fauna-restricted-layer",
      evidenceReference: "fixture:fauna-restricted-layer",
      releaseState: "DEMONSTRATION",
      layerReleaseState: "RESTRICTED",
    },
  });
  assert.equal(restrictedLayerReview.payload.selection.geometry, "WITHHELD_BY_POLICY");
  assert.equal(restrictedLayerReview.payload.selection.layerReleaseState, "RESTRICTED");
  assert.equal(restrictedLayerReview.withheldFeatureCount, 1);

  const blockedReview = exports.buildPublicSafeExport({
    ...protectedReview.payload,
    exportedAt: "2026-08-24T18:31:00.000Z",
    locationCameraRedacted: false,
    view: { center: [-97.5, 38.5], zoom: 7, bearing: 0, pitch: 0 },
    projection: "mercator",
    basemap: "midnight",
    layerOrder: ["planning"],
    activeYear: 2026,
    workspace: "trust",
    layers: [{ id: "planning", title: "Planning", opacity: 1, attribution: "", releaseState: "RESTRICTED", generalization: "Generalized", correction: "NONE" }],
    selection: null,
  });
  assert.equal(blockedReview.downloadAllowed, false);
  assert.equal(blockedReview.checks.find((check) => check.id === "attribution").state, "BLOCK");
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
  assert.match(page, /<Link className="about-action" href="\/about">About<\/Link>/);
  assert.match(page, /id="repository-tab-functions"[\s\S]*setRepositoryView\("functions"\)[\s\S]*<span>Functions<\/span>/);
});
