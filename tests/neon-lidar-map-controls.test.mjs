import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";
import { componentHarness, findNode, settle } from "./component-harness.mjs";

const moduleUrl = source => `data:text/javascript;base64,${Buffer.from(ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText).toString("base64")}`;
const previewHelpers = await import(moduleUrl(await readFile("app/neon-lidar-preview.ts", "utf8")));
const inventoryUrl = moduleUrl(await readFile("app/acquisition-inventory.ts", "utf8"));
const acquisition = await import(moduleUrl((await readFile("app/acquisition-client.ts", "utf8")).replace('from "./acquisition-inventory"', `from "${inventoryUrl}"`)));
const SOURCE = "kfm-neon-local-preview", FILL = "external-neon-local-fill";
const boundedUrl = moduleUrl(await readFile("app/bounded-json.ts", "utf8"));
const pilotUrl = moduleUrl((await readFile("app/neon-lidar-pilot-client.ts", "utf8")).replace('"./bounded-json"', JSON.stringify(boundedUrl)).replace('"./neon-lidar-preview"', JSON.stringify(moduleUrl(await readFile("app/neon-lidar-preview.ts", "utf8")))));
const pilotClient = await import(pilotUrl);

function fixture(georeferenced = true) {
  const width = 8, tile = "NEON_D06_KONZ_DP3_666000_4328000";
  const input = { schema_version: "kfm-neon-lidar-preview-v1", data_kind: "synthetic-test", generated_at: "2026-11-23T12:00:00Z",
    source: { site: "KONZ", month: "2024-06", acquisition_run: "2024_KONZ_1", release: "RELEASE-2026", tile,
      attribution: "Synthetic test; no NEON observations", horizontal_crs: 'PROJCRS["Synthetic projected CRS"]', vertical_reference: "Synthetic test", vertical_reference_basis: "Analytic plane", canopy_floor_m: null, canopy_floor_basis: "Unknown for synthetic test",
      files: ["dtm", "dsm", "chm"].map(kind => ({ kind, name: `${tile}_${kind.toUpperCase()}.tif`, product: kind === "chm" ? "DP3.30015.001" : "DP3.30024.001", bytes: 1000, sha256: "a".repeat(64) })) },
    grid: { width, height: width, bounds: [666000, 4328000, 667000, 4329000], source_resolution_m: 1, preview_resolution_m: 125, sampling: "nearest-neighbor", dtm: Array(64).fill(300), dsm: Array(64).fill(312), chm: Array(64).fill(12) },
    lifecycle: "local-preview-only", source_admitted: false, released: false };
  if (georeferenced) input.georeferencing = { method: "rasterio-warp-transform", target_crs: "EPSG:4326", source_crs: input.source.horizontal_crs, coordinate_epoch: null, height_values_transformed: false, horizontal_accuracy_m: null,
    corner_width: 9, corners: Array.from({ length: 81 }, (_, i) => [-97.09 + (i % 9) * .001, 39.09 - Math.floor(i / 9) * .001]) };
  return input;
}
const file = input => ({ size: 10000, text: async () => JSON.stringify(input) });
async function setup(overrides = {}, pilotOverrides = {}) {
  const handlers = new Map(), calls = [], map = {
    overlay: null, hits: [], fail: false,
    on(event, callback) { if (!handlers.has(event)) handlers.set(event, new Set()); handlers.get(event).add(callback); },
    off(event, callback) { handlers.get(event)?.delete(callback); },
    emit(event, payload) { for (const callback of [...handlers.get(event) ?? []]) callback(payload); },
    getLayer(id) { return this.overlay && id === FILL ? { id, source: SOURCE } : undefined; },
    queryRenderedFeatures() { return this.hits; },
    getCanvas() { return { getBoundingClientRect: () => ({ width: 1200, height: 800 }) }; },
    fitBounds(bounds, options) { calls.push({ kind: "fit", bounds, options }); },
  };
  const mapping = {
    NEON_LOCAL_SOURCE: SOURCE, NEON_LOCAL_FILL: FILL,
    buildNeonMapData: value => value.georeferencing ? { type: "FeatureCollection", features: [], tile: value.source.tile } : null,
    neonMapBounds: value => value.georeferencing ? [[-97.09, 39.082], [-97.082, 39.09]] : null,
    applyNeonMapOverlay(target, data, mode, opacity) { if (target.fail) throw new Error("Mutation failed"); target.overlay = opacity === 0 ? null : { data, mode, opacity }; calls.push({ kind: "apply", mode, opacity }); },
    clearNeonMapOverlay(target) { target.overlay = null; calls.push({ kind: "clear" }); },
  };
  const options = { mapRef: { current: map }, styleReady: true, flatMap: true, atPresent: true, reducedMotion: true, ...overrides };
  const harness = await componentHarness("app/neon-lidar-map-controls.tsx", { "next/link": { default: "a" }, "./acquisition-client": acquisition, "./neon-lidar-pilot-client": { ...pilotClient, ...pilotOverrides }, "./neon-lidar-preview": previewHelpers, "./neon-lidar-map": mapping, "./neon-lidar-map-controls.module.css": { default: new Proxy({}, { get: (_, key) => key }) } });
  const render = () => { let c = harness.render(harness.exports.useNeonLidarMap, options); harness.commit(); c = harness.render(harness.exports.useNeonLidarMap, options); harness.commit(); return c; };
  return { harness, map, calls, handlers, options, render };
}

async function mainClickHandler(scope) {
  const source = await readFile("app/page.tsx", "utf8"), ast = ts.createSourceFile("page.tsx", source, ts.ScriptTarget.Latest, true, ts.ScriptKind.TSX);
  let callback;
  function visit(node) {
    if (ts.isCallExpression(node) && node.expression.getText(ast) === "map.on" && node.arguments[0]?.getText(ast) === '"click"'
      && node.arguments[1]?.getText(ast).includes("measureModeRef.current")) callback = node.arguments[1];
    ts.forEachChild(node, visit);
  }
  visit(ast); assert.ok(callback, "the real page click handler must be found");
  const code = ts.transpileModule(`const handler = ${callback.getText(ast)};`, { compilerOptions: { target: ts.ScriptTarget.ES2022 } }).outputText;
  return new Function(...Object.keys(scope), `${code};return handler;`)(...Object.values(scope));
}

test("map control starts empty, imports locally, waits for explicit Show and retains state across control unmount", async () => {
  const s = await setup(); let c = s.render(); assert.equal(c.preview, null); assert.equal(s.map.overlay, null); assert.equal(c.enabled, false);
  await c.importFile(file(fixture())); c = s.render(); assert.equal(c.canShow, true); assert.equal(c.enabled, false); assert.equal(s.map.overlay, null);
  c.toggle(); c = s.render(); assert.equal(s.map.overlay.mode, "chm"); assert.equal(s.map.overlay.opacity, .8); assert.equal(c.applied, true);
  const clearCount = s.calls.filter(call => call.kind === "clear").length;
  c.setMode("dtm"); c.setOpacity(35); c = s.render(); assert.equal(s.map.overlay.mode, "dtm"); assert.equal(s.map.overlay.opacity, .35); assert.equal(s.calls.filter(call => call.kind === "clear").length, clearCount);
  // Rendering no drawer component does not unmount the page-owned hook.
  c = s.render(); assert.equal(c.mode, "dtm"); assert.equal(c.opacity, 35); assert.equal(c.preview.source.acquisition_run, "2024_KONZ_1");
  c.toggle(); c = s.render(); assert.equal(s.map.overlay, null); assert.equal(c.enabled, false);
  s.harness.dispose(); assert.equal(s.handlers.get("click").size, 0); assert.equal(s.handlers.get("style.load").size, 0);
});

test("zero opacity removes hit-testable display geometry and reports the hidden state", async () => {
  const s = await setup(); let c = s.render(); await c.importFile(file(fixture())); c = s.render(); c.toggle(); c = s.render();
  c.setOpacity(0); c = s.render(); assert.equal(s.map.overlay, null); assert.equal(c.applied, false); assert.match(c.status, /hidden at 0% opacity/);
  c.setOpacity(80); c = s.render(); assert.ok(s.map.overlay); assert.equal(c.applied, true); s.harness.dispose();
});

test("style reload reapplies the enabled overlay, while globe, historical frames and unready style withhold it", async () => {
  const s = await setup(); let c = s.render(); await c.importFile(file(fixture())); c = s.render(); c.toggle(); c = s.render();
  s.map.overlay = null; s.map.emit("style.load"); c = s.render(); assert.ok(s.map.overlay); assert.equal(c.enabled, true);
  s.options.flatMap = false; c = s.render(); assert.equal(s.map.overlay, null); assert.match(c.status, /held in globe or Terrain 3D/);
  s.map.emit("style.load"); assert.equal(s.map.overlay, null);
  s.options.flatMap = true; s.options.atPresent = false; c = s.render(); assert.equal(s.map.overlay, null); assert.match(c.status, /held outside Present/);
  s.options.atPresent = true; s.options.styleReady = false; c = s.render(); assert.equal(s.map.overlay, null); assert.match(c.status, /waiting for the map style/);
  s.options.styleReady = true; c = s.render(); assert.ok(s.map.overlay); assert.equal(c.enabled, true); s.harness.dispose(); assert.equal(s.map.overlay, null);
});

test("a legacy numeric preview remains inspectable but cannot invent map georeferencing", async () => {
  const s = await setup(); let c = s.render(); await c.importFile(file(fixture(false))); c = s.render();
  assert.ok(c.preview); assert.equal(c.canShow, false); assert.match(c.status, /Re-prepare/); c.toggle(); c.fit(); s.render(); assert.equal(s.map.overlay, null); assert.equal(s.calls.filter(call => call.kind === "fit").length, 0); s.harness.dispose();
});

test("map cell clicks and editable coordinate drafts share original numeric samples without evidence selection", async () => {
  const s = await setup(); let c = s.render(); const input = fixture(); input.grid.dtm[11] = 301; input.grid.dsm[11] = 299; input.grid.chm[11] = 0;
  await c.importFile(file(input)); c = s.render(); c.toggle(); c = s.render();
  s.map.hits = [{ source: SOURCE, properties: { row: 1, column: 3 } }]; s.map.emit("click", { point: { x: 100, y: 200 } }); c = s.render();
  assert.equal(c.coordinateDraft.row, "2"); assert.equal(c.coordinateDraft.column, "4"); assert.equal(c.probe.dtm, 301); assert.equal(c.probe.surfaceAboveGround, -2); assert.equal(c.probe.differenceIssue, "negative"); assert.equal(c.probe.chm, 0);
  c.selectAxis("row", ""); c = s.render(); assert.equal(c.coordinateDraft.row, ""); assert.equal(c.probe, null);
  c.selectAxis("row", "3"); c = s.render(); assert.equal(c.probe.row, 2); assert.equal(c.probe.column, 3);
  c.selectAxis("column", "9"); c = s.render(); assert.equal(c.coordinateDraft.column, "9"); assert.equal(c.probe, null);
  s.map.hits = [{ source: "official-provider", properties: { row: 1, column: 3 } }]; s.map.emit("click", { point: {} }); c = s.render(); assert.equal(c.probe, null); s.harness.dispose();
});

test("the real page handler claims point completion and other priority clicks before the local probe listener runs", async () => {
  const claimedClicksRef = { current: new WeakSet() }, s = await setup({ claimedClicksRef });
  const measureModeRef = { current: "point" }, aviationPickingRef = { current: false }, undergroundOpenRef = { current: false }, measureCoordinatesRef = { current: [] };
  let geologyActive = false, completed = false;
  const baseLayer = s.map.getLayer.bind(s.map);
  s.map.getLayer = id => id === "geology-marker" ? geologyActive ? { id } : undefined : baseLayer(id);
  s.map.queryRenderedFeatures = (_point, options) => options?.layers?.includes("geology-marker") ? geologyActive ? [{}] : [] : s.map.hits;
  s.map.doubleClickZoom = { enable() { completed = true; } };
  const main = await mainClickHandler({ map: s.map, neonClaimedMapClicksRef: claimedClicksRef, aviationPickingRef, undergroundOpenRef, measureModeRef, measureCoordinatesRef,
    GEOLOGY_POINT_LAYER_IDS: ["geology-marker"], pickKansasSkyAircraft() { return false; }, setMeasureCoordinateCount() {}, updateMeasurementSource() {}, buildMeasurementData() { return {}; }, setMeasurement() {}, measurementLabelFor() { return "point"; }, measureUnitRef: { current: "meters" }, setMeasureMode() {}, announce() {},
    OFFICIAL_CONTEXT_BY_SOURCE_ID: {}, findLayerByRenderer() { return null; }, hasNeonLocalHit: hits => hits.some(hit => hit.source === SOURCE) });
  // Match the page: its click handler is registered when the map is created, before the hook.
  s.map.on("click", main);
  let c = s.render(); await c.importFile(file(fixture())); c = s.render(); c.toggle(); c.selectAxis("row", "1"); c = s.render();
  s.map.hits = [{ source: SOURCE, layer: { id: FILL }, properties: { row: 3, column: 4 } }];
  const event = { point: { x: 100, y: 200 }, lngLat: { lng: -97.085, lat: 39.085 } };
  s.map.emit("click", event); c = s.render();
  assert.equal(completed, true); assert.equal(measureModeRef.current, null); assert.equal(claimedClicksRef.current.has(event), true);
  assert.deepEqual(measureCoordinatesRef.current, [[-97.085, 39.085]]); assert.equal(c.probe.row, 0); assert.equal(c.probe.column, 0);
  // The same cleared mode cannot accidentally authorize a second consumer of that completed event.
  s.map.emit("click", { ...event }); c = s.render(); assert.equal(c.probe.row, 3); assert.equal(c.probe.column, 4);
  s.map.hits = [{ source: SOURCE, layer: { id: FILL }, properties: { row: 0, column: 0 } }];
  for (const priority of ["aviation", "underground", "geology", "draw"]) {
    aviationPickingRef.current = priority === "aviation"; undergroundOpenRef.current = priority === "underground"; geologyActive = priority === "geology"; measureModeRef.current = priority === "draw" ? "distance" : null;
    s.map.emit("click", { ...event }); c = s.render(); assert.equal(c.probe.row, 3, priority); assert.equal(c.probe.column, 4, priority);
  }
  s.harness.dispose();
});

test("new selections immediately remove old overlays/probes; stale reads and cancellation cannot restore them", async () => {
  const s = await setup(); let c = s.render(); await c.importFile(file(fixture())); c = s.render(); c.toggle(); c.selectAxis("row", "2"); c = s.render(); assert.ok(c.probe); assert.ok(s.map.overlay);
  let finish; const old = c.importFile({ size: 1000, text: () => new Promise(resolve => { finish = resolve; }) }); assert.equal(s.map.overlay, null); c = s.render(); assert.equal(c.probe, null); assert.equal(c.preview, null);
  const newer = fixture(); newer.source.month = "2024-07"; await c.importFile(file(newer)); c = s.render(); finish(JSON.stringify(fixture())); await old; await settle(); c = s.render();
  assert.equal(c.preview.source.month, "2024-07"); assert.equal(c.coordinateDraft.row, ""); assert.equal(c.enabled, false);
  let canceled; const pending = c.importFile({ size: 1000, text: () => new Promise(resolve => { canceled = resolve; }) }); c.clear(); canceled(JSON.stringify(fixture())); await pending; c = s.render(); assert.equal(c.preview, null); assert.equal(c.busy, false);
  await c.importFile({ size: 10, text: async () => "{}" }); c = s.render(); assert.ok(c.fileError); assert.equal(s.map.overlay, null); s.harness.dispose();
});

test("fit uses supplied geographic bounds with reduced motion, and a renderer failure holds display", async () => {
  const s = await setup(); let c = s.render(); await c.importFile(file(fixture())); c = s.render(); c.fit();
  const call = s.calls.find(item => item.kind === "fit"); assert.deepEqual(call.bounds, [[-97.09, 39.082], [-97.082, 39.09]]); assert.equal(call.options.duration, 0);
  s.map.fail = true; c.toggle(); c = s.render(); assert.equal(c.applied, false); assert.ok(c.mapError); assert.equal(s.map.overlay, null); s.harness.dispose();
});

test("main map integration owns hover and click hits before existing evidence selection", async () => {
  const source = await readFile("app/page.tsx", "utf8");
  assert.equal((source.match(/if \(hasNeonLocalHit\(renderedHits\)\)/g) ?? []).length, 2);
  assert.match(source, /hasNeonLocalHit\(renderedHits\)[\s\S]{0,350}clearHoverCandidate\(\);[\s\S]{0,50}return;/);
  assert.match(source, /if \(hasNeonLocalHit\(renderedHits\)\) return;[\s\S]{0,200}const availableLayers/);
  assert.match(source, /const neonLidarMap = useNeonLidarMap\(/); assert.match(source, /<NeonLidarMapControls controller=\{neonLidarMap\}/);
});

test("controls expose the empty local import and all loaded numeric/readout actions", async () => {
  const s = await setup(); let c = s.render();
  const controls = await componentHarness("app/neon-lidar-map-controls.tsx", { "next/link": { default: "a" }, "./acquisition-client": acquisition, "./neon-lidar-pilot-client": pilotClient, "./neon-lidar-preview": previewHelpers, "./neon-lidar-map": {}, "./neon-lidar-map-controls.module.css": { default: new Proxy({}, { get: (_, key) => key }) } });
  let tree = controls.render(controls.exports.NeonLidarMapControls, { controller: c });
  assert.ok(findNode(tree, node => node.type === "input" && node.props.type === "file")); assert.equal(findNode(tree, node => node.props?.children === "Show on map"), undefined);
  await c.importFile(file(fixture())); c = s.render(); tree = controls.render(controls.exports.NeonLidarMapControls, { controller: c });
  for (const label of ["Show on map", "Fit tile", "Clear"]) assert.ok(findNode(tree, node => node.type === "button" && node.props.children === label));
  assert.ok(findNode(tree, node => node.type === "input" && node.props.type === "range")); assert.ok(findNode(tree, node => node.type === "input" && node.props.type === "number"));
  assert.ok(findNode(tree, node => node.type === "strong" && node.props.children === "Synthetic test · not observed terrain."));
  assert.equal(controls.render(controls.exports.NeonLidarMapBadge, { controller: c }), null);
  c.toggle(); c = s.render(); const badge = controls.render(controls.exports.NeonLidarMapBadge, { controller: c });
  assert.ok(findNode(badge, node => node.type === "strong" && node.props.children === "Synthetic local tile · not observed"));
  c.toggle(); c = s.render(); assert.equal(controls.render(controls.exports.NeonLidarMapBadge, { controller: c }), null);
  s.harness.dispose(); controls.dispose();
});

function relayReceipt() {
  const preview = fixture(); preview.data_kind = "provider-files";
  const tile = "NEON_D06_KONZ_DP3_706000_4336000";
  preview.source.month = "2024-09"; preview.source.acquisition_run = "2024_KONZ_10"; preview.source.tile = tile;
  preview.source.files.forEach(item => { item.name = `${tile}_${item.kind.toUpperCase()}.tif`; });
  preview.grid.bounds = [706000, 4336000, 707000, 4337000];
  return { format: "kfm-neon-relay-pilot-v1", preview, generatedAt: "2026-11-23T23:00:00Z", cache: { state: "stale", at: "2026-11-23T22:00:00Z" },
    review: { status: "pending", scientific_accuracy_verified: false, source_admitted: false, canopy_native_max_m: 83.41000366210938,
      canopy_native_cells_above_50m: 5, surface_minus_ground_native_max_m: 32.5,
      notes: ["Native CHM outliers retained; scientific accuracy and vertical reference remain unverified.", "Provider CHM is independent of DSM minus DTM; zero canopy does not establish bare ground."] } };
}

test("pilot receipt validates the pinned provider source, pending science review and cache clock without clamping outliers", () => {
  const receipt = relayReceipt(), parsed = pilotClient.parseNeonPilotReceipt(receipt); assert.ok(parsed);
  assert.equal(parsed.review.canopy_native_max_m, 83.41000366210938); assert.equal(parsed.cache.state, "stale"); assert.equal(parsed.review.scientific_accuracy_verified, false);
  for (const change of [r => r.format = "other", r => r.preview.data_kind = "synthetic-test", r => r.preview.source.month = "2024-08", r => r.review.scientific_accuracy_verified = true,
    r => r.review.source_admitted = true, r => r.review.status = "approved", r => r.review.canopy_native_max_m = Infinity, r => r.review.canopy_native_cells_above_50m = -1,
    r => r.review.notes = [], r => r.cache.state = "unknown", r => r.cache.at = "2026-02-30T12:00:00Z"]) {
    const input = relayReceipt(); change(input); assert.equal(pilotClient.parseNeonPilotReceipt(input), null);
  }
});

test("pilot fetch is an explicit bounded GET and rejects non-2xx before parsing a body", async t => {
  let canceled = false, calls = 0;
  const mocked = t.mock.method(globalThis, "fetch", async (url, init) => { calls++; assert.equal(url, "/api/neon/preview"); assert.equal(init.method, "GET"); assert.equal(init.body, undefined); assert.equal(init.headers, undefined); return { ok: false, body: { cancel: async () => { canceled = true; } }, get headers() { assert.fail("failed response must not enter JSON parsing"); } }; });
  await assert.rejects(pilotClient.readNeonLidarPilot(new AbortController().signal)); assert.equal(calls, 1); assert.equal(canceled, true);
  mocked.mock.mockImplementation(async () => new Response(new Uint8Array(1_000_001)));
  await assert.rejects(pilotClient.readNeonLidarPilot(new AbortController().signal), /limit/);
  mocked.mock.mockImplementation(async () => new Response(JSON.stringify({ ...relayReceipt(), format: "wrong" })));
  await assert.rejects(pilotClient.readNeonLidarPilot(new AbortController().signal), /validation/);
  mocked.mock.mockImplementation(async () => new Response(JSON.stringify(relayReceipt())));
  const result = await pilotClient.readNeonLidarPilot(new AbortController().signal); assert.equal(result.preview.source.acquisition_run, "2024_KONZ_10");
});

test("explicit pilot loading retains source/cache provenance and pending science while leaving Show and Fit separate", async () => {
  let reads = 0;
  const s = await setup({}, { readNeonLidarPilot: async () => { reads++; return relayReceipt(); } }); let c = s.render(); assert.equal(reads, 0);
  await c.loadPilot(); c = s.render(); assert.equal(reads, 1); assert.equal(c.enabled, false); assert.equal(s.map.overlay, null); assert.match(c.status, /Dev-processed provider pilot ready/);
  assert.equal(c.pilotReceipt.cache.state, "stale"); assert.equal(c.preview.data_kind, "provider-files");
  const controls = await componentHarness("app/neon-lidar-map-controls.tsx", { "next/link": { default: "a" }, "./acquisition-client": acquisition, "./neon-lidar-pilot-client": pilotClient, "./neon-lidar-preview": previewHelpers, "./neon-lidar-map": {}, "./neon-lidar-map-controls.module.css": { default: new Proxy({}, { get: (_, key) => key }) } });
  const tree = controls.render(controls.exports.NeonLidarMapControls, { controller: c });
  assert.ok(findNode(tree, node => node.type === "time" && node.props.dateTime === "2026-11-23T22:00:00Z"));
  assert.ok(findNode(tree, node => node.type === "p" && Array.isArray(node.props.children) && node.props.children.some(text => typeof text === "string" && /independent accuracy and vertical reference are unverified/.test(text))));
  assert.ok(findNode(tree, node => node.type === "p" && Array.isArray(node.props.children) && node.props.children.some(text => typeof text === "string" && /cached preview is stale/.test(text))));
  c.toggle(); c = s.render(); assert.ok(s.map.overlay); const badge = controls.render(controls.exports.NeonLidarMapBadge, { controller: c });
  assert.ok(findNode(badge, node => node.type === "strong" && node.props.children === "Dev-processed NEON pilot · review pending"));
  s.harness.dispose(); controls.dispose();
});

test("replaced or canceled pilot reads cannot restore old map data or probes", async () => {
  let finish, observedSignal;
  const s = await setup({}, { readNeonLidarPilot: signal => { observedSignal = signal; return new Promise(resolve => { finish = resolve; }); } }); let c = s.render();
  const pending = c.loadPilot(); c = s.render(); await c.importFile(file(fixture())); c = s.render(); finish(relayReceipt()); await pending; c = s.render();
  assert.equal(observedSignal.aborted, true); assert.equal(c.pilotReceipt, null); assert.equal(c.preview.data_kind, "synthetic-test"); assert.equal(c.enabled, false);
  const canceled = c.loadPilot(); c.clear(); finish(relayReceipt()); await canceled; c = s.render(); assert.equal(c.preview, null); assert.equal(c.pilotReceipt, null); assert.equal(c.busy, false);
  s.harness.dispose();
});
