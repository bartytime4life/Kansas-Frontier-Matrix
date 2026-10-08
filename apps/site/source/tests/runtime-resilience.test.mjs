import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import ts from "typescript";

const modules = new Map();
const moduleUrl = async (file) => {
  const resolved = path.resolve(file);
  if (modules.has(resolved)) return modules.get(resolved);
  let js = ts.transpileModule(await readFile(resolved, "utf8"), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
  for (const match of [...js.matchAll(/from ["'](\.[^"']+)["']/g)]) {
    js = js.replace(match[0], `from ${JSON.stringify(await moduleUrl(path.resolve(path.dirname(resolved), match[1]) + ".ts"))}`);
  }
  const url = `data:text/javascript;base64,${Buffer.from(js).toString("base64")}`;
  modules.set(resolved, url);
  return url;
};

const saved = await import(await moduleUrl("app/saved-workspaces.ts"));
const embedded = await import(await moduleUrl("app/embed-runtime.ts"));
const perf = await import(await moduleUrl("app/map-performance.ts"));
const registry = await import(await moduleUrl("app/site-registry.ts"));

const workspace = {
  id: "workspace-1", name: "Kansas view", savedAt: "2026-09-15T16:00:00Z",
  view: { center: [-98.38, 38.48], zoom: 5.45, bearing: 0, pitch: 0 },
  visibility: { "water-context": true }, opacity: { "water-context": 0.5 }, layerOrder: ["water-context"], year: 2026,
  basemap: "standard", projection: "mercator",
  report: { title: "Kansas report", scope: "VIEWPORT", detail: "STANDARD", layerIds: ["water-context"], sections: {}, query: "" },
  selection: null,
};

test("corrupt device-local workspaces cannot replace the Explorer with a blank root", () => {
  assert.deepEqual(saved.parseSavedWorkspaceList(JSON.stringify([null]), 24), { records: [], rejected: true });
  assert.deepEqual(saved.parseSavedWorkspaceList("not-json", 24), { records: [], rejected: true });
  assert.deepEqual(saved.parseSavedWorkspaceList("x".repeat(101), 24, 100), { records: [], rejected: true });
  const mixed = saved.parseSavedWorkspaceList(JSON.stringify([workspace, { ...workspace, id: "" }]), 24);
  assert.equal(mixed.records.length, 1);
  assert.equal(mixed.records[0].id, "workspace-1");
  assert.equal(mixed.rejected, true);
});

test("embedded panels do not rewrite host-controlled history and history failures stay contained", () => {
  let writes = 0;
  const history = { replaceState: () => { writes++; } };
  assert.equal(embedded.replaceExplorerHistory("/?t=2026", true, history), false);
  assert.equal(writes, 0);
  assert.equal(embedded.replaceExplorerHistory("/?t=2026", false, history), true);
  assert.equal(writes, 1);
  assert.equal(embedded.replaceExplorerHistory("/?t=2026", false, { replaceState: () => { throw new Error("denied"); } }), false);
});

test("automatic embedded rendering uses the smallest bounded GPU budget", () => {
  const budget = perf.renderBudget("auto", 3, false, false, true);
  assert.equal(budget.pixelRatio, 1);
  assert.equal(budget.imageRequests, 6);
  assert.equal(budget.tileCache, 48);
  assert.equal(budget.workerCount, 1);
  assert.equal(budget.efficient, true);
  assert.equal(perf.renderBudget("detail", 3, false, false, true).pixelRatio, 2);
});

test("map health keeps a rendering failure finite and excludes sensitive exception text", () => {
  const enabled = { isEnabled: () => true };
  let legacySourceChecks = 0;
  const map = {
    isStyleLoaded: () => true,
    getSource: () => ({ loaded: () => { throw new Error("https://private.example/?token=secret"); } }),
    isSourceLoaded: () => { legacySourceChecks++; throw new Error("missing tile manager"); },
    getCanvas: () => ({ width: 400, height: 300, getBoundingClientRect: () => ({ width: 400, height: 300 }) }),
    getProjection: () => ({ type: "mercator" }),
    loaded: () => true,
    areTilesLoaded: () => true,
    dragPan: enabled, scrollZoom: enabled, keyboard: enabled, touchZoomRotate: enabled,
  };
  const health = perf.sampleMapRuntimeHealth(map, ["local-fixture"], true, true);
  assert.equal(health.sourceReadyById["local-fixture"], false);
  assert.deepEqual(health.failedChecks, ["SOURCE_CHECK_FAILED"]);
  assert.equal(health.canvasReady, true);
  assert.equal(health.tilesLoaded, true);
  assert.equal(legacySourceChecks, 0);
  assert.doesNotMatch(JSON.stringify(health), /private\.example|secret/);
});

test("MapLibre event and startup telemetry uses finite classes without reading provider errors", async () => {
  assert.equal(perf.mapRuntimeErrorCode("event", "private-token-source"), "MAP_SOURCE_FAILED");
  assert.equal(perf.mapRuntimeErrorCode("event"), "MAP_RENDER_FAILED");
  assert.equal(perf.mapRuntimeErrorCode("start"), "MAP_START_FAILED");
  assert.equal(perf.mapRuntimeErrorCode("load"), "MAP_LOAD_FAILED");
  const page = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
  const eventHandler = page.slice(page.indexOf('map.on("error", (event) => {'));
  assert.ok(eventHandler.startsWith('map.on("error", (event) => {'));
  assert.doesNotMatch(eventHandler.slice(0, 1200), /event\.error|\.message/);
  assert.match(page, /catch \{\s*const message = mapRuntimeErrorCode\("start"\)/);
  assert.match(page, /catch\(\(\) => \{\s*const message = mapRuntimeErrorCode\("load"\)/);
  const snapshot = await readFile(new URL("../app/snapshot-map.tsx", import.meta.url), "utf8");
  assert.doesNotMatch(snapshot, /error\.message|unknown renderer failure/);
  assert.match(snapshot, /MAP_RENDER_FAILED/);
});

test("control-owned and buffered radar source failures never become a fatal map runtime error", async () => {
  // Read each control's actual source IDs so a renamed source cannot silently
  // fall through to "Map runtime error: MAP_SOURCE_FAILED" again.
  const read = (file) => readFile(new URL(`../app/${file}`, import.meta.url), "utf8");
  const [soil, crop, earthEngine, geopdf] = await Promise.all([
    read("soil-moisture-control.tsx"), read("crop-casma-control.tsx"), read("earth-engine-display.tsx"), read("local-geopdf-map.ts"),
  ]);
  const soilSources = JSON.parse(soil.match(/const SOURCES = (\[[^\]]+\]) as const;/)[1]);
  const cropSource = crop.match(/const SOURCE = "([^"]+)";/)[1];
  const earthEnginePrefix = earthEngine.match(/const sourceId = \(id: string\) => `([^$`]+)\$\{id\}`;/)[1];
  const geopdfSource = geopdf.match(/export const LOCAL_REVIEW_SOURCE = "([^"]+)";/)[1];
  assert.equal(soilSources.length, 2);
  for (const sourceId of [...soilSources, cropSource, `${earthEnginePrefix}ee-cdl`, geopdfSource, `${geopdfSource}-5-7-12`]) {
    assert.equal(perf.controlOwnsMapSourceErrors(sourceId), true, sourceId);
  }
  for (const sourceId of [undefined, "", "openmaptiles", "osm-context", "kfm-terrain-dem", "external-nws-radar", "private-token-source"]) {
    assert.equal(perf.controlOwnsMapSourceErrors(sourceId), false, String(sourceId));
  }

  const context = await import(await moduleUrl("app/live-context.ts"));
  const radar = context.OFFICIAL_CONTEXT_BY_ID["nws-radar"];
  assert.equal(context.officialContextForMapSource(radar.sourceId), radar);
  assert.equal(context.officialContextForMapSource(`${radar.sourceId}-buffer`), radar);
  assert.equal(context.officialContextForMapSource("external-usgs-earthquakes")?.id, "usgs-earthquakes");
  assert.equal(context.officialContextForMapSource("osm-context"), undefined);
  assert.equal(context.officialContextForMapSource(undefined), undefined);

  // The page skips these sources, so each control must report its own late failures.
  const soilError = soil.slice(soil.indexOf("const onError = (event: unknown) => {"), soil.indexOf("const onRender = () => {"));
  assert.doesNotMatch(soilError, /\|\| settled\) return;/);
  assert.match(soilError, /if \(settled\) \{[\s\S]*state: "partial"/);
  assert.match(soil, /setMapState\(\{ state: failed \? "partial" : "rendered", loaded, failed,/);

  const page = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
  const eventHandler = page.slice(page.indexOf('map.on("error", (event) => {'));
  const fatal = eventHandler.indexOf("Map runtime error:");
  assert.ok(eventHandler.indexOf("if (controlOwnsMapSourceErrors(sourceId)) return;") > 0);
  assert.ok(eventHandler.indexOf("if (controlOwnsMapSourceErrors(sourceId)) return;") < fatal);
  assert.match(eventHandler.slice(0, fatal), /const affectedOfficialContext = officialContextForMapSource\(sourceId\);/);
});

test("map health treats a local source awaiting style installation as pending", () => {
  const enabled = { isEnabled: () => true };
  const map = {
    isStyleLoaded: () => false,
    getSource: () => { throw new Error("source should not be read before style load"); },
    getCanvas: () => ({ width: 400, height: 300, getBoundingClientRect: () => ({ width: 400, height: 300 }) }),
    getProjection: () => ({ type: "mercator" }),
    loaded: () => false,
    areTilesLoaded: () => false,
    dragPan: enabled, scrollZoom: enabled, keyboard: enabled, touchZoomRotate: enabled,
  };
  const health = perf.sampleMapRuntimeHealth(map, ["local-fixture"], true, true);
  assert.equal(health.sourceReadyById["local-fixture"], false);
  assert.deepEqual(health.failedChecks, []);
});

test("map health accepts an implicit Mercator projection and recognizes globe", () => {
  const enabled = { isEnabled: () => true };
  let explicitProjection;
  const map = {
    isStyleLoaded: () => true,
    getSource: () => ({ loaded: () => true }),
    getCanvas: () => ({ width: 400, height: 300, getBoundingClientRect: () => ({ width: 400, height: 300 }) }),
    getProjection: () => explicitProjection,
    loaded: () => true,
    areTilesLoaded: () => true,
    dragPan: enabled, scrollZoom: enabled, keyboard: enabled, touchZoomRotate: enabled,
  };
  const defaultHealth = perf.sampleMapRuntimeHealth(map, ["local-fixture"], true, true);
  assert.equal(defaultHealth.projection, "mercator");
  assert.deepEqual(defaultHealth.failedChecks, []);
  explicitProjection = { type: "globe" };
  const globeHealth = perf.sampleMapRuntimeHealth(map, ["local-fixture"], true, true);
  assert.equal(globeHealth.projection, "globe");
  assert.deepEqual(globeHealth.failedChecks, []);
});

test("route and global error surfaces keep client failures visible", async () => {
  const [routeError, globalError, page, snapshot] = await Promise.all([
    readFile(new URL("../app/error.tsx", import.meta.url), "utf8"),
    readFile(new URL("../app/global-error.tsx", import.meta.url), "utf8"),
    readFile(new URL("../app/page.tsx", import.meta.url), "utf8"),
    readFile(new URL("../app/snapshot-map.tsx", import.meta.url), "utf8"),
  ]);
  assert.match(routeError, /Retry in battery saver/);
  assert.match(globalError, /The Explorer could not finish loading/);
  assert.match(routeError, /window\.location\.reload/);
  assert.match(globalError, /window\.location\.reload/);
  assert.doesNotMatch(page, /\.loseContext\(/);
  assert.doesNotMatch(snapshot, /\.loseContext\(/);
  assert.match(page, /Map style synchronization/);
  assert.match(page, /mapMutationErrorRef/);
});

test("embedded shells use parent-relative height and explicit shares stay guarded", async () => {
  const [css, observatory] = await Promise.all([
    readFile(new URL("../app/globals.css", import.meta.url), "utf8"),
    readFile(new URL("../app/observatory/workspace.tsx", import.meta.url), "utf8"),
  ]);
  assert.match(css, /\.site-root\s*\{[^}]*height:\s*100%/s);
  assert.match(css, /\.explorer-shell\s*\{[^}]*height:\s*calc\(100% - var\(--topbar\)\)/s);
  assert.doesNotMatch(observatory, /window\.history\.replaceState/);
  assert.match(observatory, /replaceExplorerHistory/);
});

test("compact map chrome shares one overlay clearance with degraded and utility surfaces", async () => {
  const css = await readFile(new URL("../app/globals.css", import.meta.url), "utf8");
  const root = css.match(/:root\s*\{([^}]+)\}/)?.[1] ?? "";
  const banner = css.match(/\.runtime-degraded-banner\s*\{([^}]+)\}/)?.[1] ?? "";
  assert.match(root, /--map-dock-height:\s*0px/);
  assert.match(root, /--map-overlay-top:\s*calc\(var\(--map-dock-height\) \+ var\(--map-overlay-gap\)\)/);
  assert.match(css, /\.map-chrome-dock\s*\{[^}]*height:\s*44px/s);
  assert.match(banner, /top:\s*var\(--map-overlay-top\)/);
  assert.match(banner, /left:\s*72px/);
  assert.match(banner, /width:\s*min\(460px, calc\(100% - 144px\)\)/);
  assert.match(banner, /pointer-events:\s*none/);
  assert.doesNotMatch(banner, /translateX/);
  assert.match(css, /\.map-source-status\s*\{[^}]*top:\s*var\(--map-overlay-top\)/s);
  assert.match(css, /\.map-tool-rail\s*\{[^}]*top:\s*var\(--map-overlay-top\)/s);
  assert.match(root, /--global-header-height:\s*54px/);
  assert.match(root, /--mobile-header-height:\s*54px/);
  assert.match(root, /--topbar:\s*var\(--global-header-height\)/);
  assert.match(css, /@media \(max-width: 760px\) \{\s*:root \{ --topbar: var\(--mobile-header-height\); \}/);
  assert.doesNotMatch(css, /map-command-bar|map-view-mode-strip|map-control-strip/);
});

test("every official connection has feature-level traceability", () => {
  assert.equal(registry.SITE_REGISTRY_COUNTS.connections, 48);
  assert.deepEqual(registry.SITE_REGISTRY_VALIDATION, { ok: true, errors: [] });
});
