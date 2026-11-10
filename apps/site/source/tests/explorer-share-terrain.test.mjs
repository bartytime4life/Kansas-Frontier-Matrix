import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";
import { componentHarness } from "./component-harness.mjs";

// Actual complete page callbacks with public synthetic state, real URL/soil/DEM
// models, an in-memory clipboard/history and a renderer seam. No provider I/O.
const soil = (await componentHarness("app/soil-moisture.ts", {})).exports;
const external = (await componentHarness("app/external-context-sources.ts", {})).exports;
const terrain = (await componentHarness("app/terrain-sources.ts", { "./external-context-sources":external })).exports;
const history = (await componentHarness("app/explorer-layer-history.ts", { "./embed-runtime": { isEmbeddedSiteRuntime:() => false } }, { URLSearchParams })).exports;
const source = await readFile("app/page.tsx", "utf8");
const ast = ts.createSourceFile("page.tsx", source, ts.ScriptTarget.ES2022, true, ts.ScriptKind.TSX);
const callbacks = new Map(); let serializerDependencies;
function visit(node) {
  if (ts.isVariableDeclaration(node) && node.initializer) {
    const name = node.name.getText(ast), init = node.initializer;
    if (ts.isArrowFunction(init)) callbacks.set(name, init.getText(ast));
    if (ts.isCallExpression(init) && init.expression.getText(ast) === "useCallback") {
      callbacks.set(name, init.arguments[0].getText(ast));
      if (name === "buildExplorerParams") serializerDependencies = init.arguments[1].getText(ast);
    }
  }
  ts.forEachChild(node, visit);
}
visit(ast);
const compile = (code, scope) => new Function("scope", `with(scope){${ts.transpileModule(`return (${code});`, { compilerOptions:{ target:ts.ScriptTarget.ES2022 } }).outputText}}`)(scope);
const KANSAS = { center:[-98.38, 38.48], zoom:5.45, bearing:0, pitch:0 };
const camera = { center:[-99.3, 37.8], zoom:10, bearing:15, pitch:60 };
const ref = current => ({ current });
function fixture({ provider = "mapzen", redacted = false, map = false } = {}) {
  const state = {
    terrainProvider:provider, scenePreset:"elevation-3d", verticalExaggeration:1.5, terrainState:"READY",
    terrainElevationReading:{ provider, meters:500 }, terrainElevationUnavailable:"old sample state",
    view:structuredClone(camera), locationCameraRedacted:redacted, analysisArea:{ west:-100, south:37, east:-99, north:38 },
    activeLayers:[{ id:"synthetic-layer", defaultOpacity:1 }], opacity:{ "synthetic-layer":.7 }, layerOrder:["synthetic-layer"],
    visibleOfficialSources:[], officialArchiveDays:{}, officialOpacity:{}, officialVisibility:{},
    soilMapState:{ visible:false, view:"surface", day:"", opacity:.65 },
    daylightDay:"2026-11-09", daylightThroughDay:"2026-11-09", daylightInstant:Date.parse("2026-11-09T18:00:00Z"), daylightEnabled:false,
    streamflowRange:"24h", streamflowPlaybackSpeed:1, streamflowFrameTime:null, streamflowSelectedStationId:null, streamflowArchiveDay:null,
    liveInstrument:"river", noaaRadarFollowLatest:true, noaaRadarFrameTime:null, noaaRadarLoopSpan:60, noaaRadarPlaybackSpeed:1,
    officialWorkspace:"all", layerCatalogView:"official", year:2026, temporalMode:"snapshot", temporalStepRule:"regular-calendar",
    sweepRangeStart:1910, sweepRangeEnd:2026, movingWindowFrames:3, playbackDirection:"forward", playbackLoopMode:"stop", dynamicEffects:false,
    mapEvidenceFilter:"ALL", basemap:"midnight", projection:"mercator", atmospherePreset:"clear", lightAzimuth:235, fieldOfView:36,
    gestureMode:"cooperative", measureUnit:"imperial", currentWorkspace:"explore", mapUtilityOpen:false, mapUtilityView:"scene",
    compareTimeA:1910, compareTimeB:2026, selected:null, drawerView:"evidence", rightOpen:false, focusStage:"outcome", focusIntent:"explain",
  };
  const copied = [], messages = [], carriers = [], moves = [], stateWrites = [];
  const mapStub = { jumpTo:value => moves.push(value), setMaxPitch:value => moves.push({ maxPitch:value }), isStyleLoaded:() => false, getSource:() => ({}), isSourceLoaded:() => false };
  const browserHistory = { state:{ router:"retained" }, replaceState(value) { this.state = value; } };
  const bindings = {
    ...soil, ...terrain, ...history, URLSearchParams, URL, Date, Number, String, Boolean, Object, Array, Set, Map, Math,
    KANSAS_VIEW:KANSAS, LAYER_REGISTRY:[{ id:"synthetic-layer", defaultOpacity:1 }], OFFICIAL_CONTEXT_SOURCES:[],
    defaultVisibility:{ "synthetic-layer":true }, defaultOpacity:{ "synthetic-layer":1 }, defaultOrder:["synthetic-layer"], defaultOfficialVisibility:{}, defaultOfficialOpacity:{},
    KNOWN_TEMPORAL_FRAMES:new Set([1910, 2026]), TIME_STEPS:[1910, 2026], OFFICIAL_CONTEXT_PRESENT_FRAME:2026, evidenceLabels:{}, DEFAULT_TERRAIN_DEPTH:1,
    SUPPORTED_CONTEXT_BOUNDS:{ west:-104.8, south:34.8, east:-92, north:42.2 },
    window:{ location:{ origin:"https://synthetic.invalid", pathname:"/", search:"" }, history:browserHistory, setTimeout() {} },
    navigator:{ clipboard:{ writeText:async value => copied.push(value) } },
    mapRef:ref(map ? mapStub : null), compactRef:ref(false), styleGenerationReadyRef:ref(false),
    locationDerivedViewRef:ref(redacted), terrainProviderRef:ref(provider), attachedTerrainProviderRef:ref(provider),
    officialArchiveDaysRef:ref({}), officialPayloadsRef:ref({}), officialArchivePayloadsRef:ref({}), officialRequestsRef:ref(new Map()),
    basemapRef:ref(state.basemap), atmospherePresetRef:ref(state.atmospherePreset), lightAzimuthRef:ref(state.lightAzimuth),
    clamp:(value, low, high) => Math.max(low, Math.min(high, value)),
    parseNumber:(value, fallback) => value !== null && value.trim() !== "" && Number.isFinite(Number(value)) ? Number(value) : fallback,
    restoreTopic:() => "all", currentKansasCalendarDay:() => "2026-11-09", currentUtcDay:() => "2026-11-09",
    restoreDaylightView:() => ({ day:"2026-11-09", throughDay:"2026-11-09", instantMs:Date.parse("2026-11-09T18:00:00Z"), enabled:false, playing:false }),
    readContextPreference:() => null, preferredContextIds:params => params.has("ctx") ? params.get("ctx").split(",").filter(Boolean) : null,
    normalizeUsgsStationId:() => null, restoreStreamflowArchiveDay:() => null, terrainDepth:value => value, compositionDefaults:() => ({ fieldOfView:36 }),
    findFeature:() => null, applyProjectionNavigationLimits() {},
    refreshOfficialContext() { assert.fail("fixture must not activate a provider"); }, loadOfficialArchiveDay() { assert.fail("fixture must not load archives"); },
    refreshNoaaRadarManifest() { assert.fail("fixture must not load radar"); }, refreshStreamflow() { assert.fail("fixture must not load river data"); }, refreshNoaaHydrologyNetwork() { assert.fail("fixture must not load gauges"); },
    announce:value => messages.push(value), replaceExplorerHistory:path => { browserHistory.path = path; return true; },
    applyTerrainPresentation(_map, enabled, scale, carrier) { carriers.push({ enabled, scale, carrier }); return "LOADING"; },
    terrainPresentationSourceMatches:() => true, applyTerrainReliefStyle() {}, applyTopographicRasterDepth() {}, TERRAIN_SOURCE_ID:"synthetic-dem",
  };
  const scopeFor = captured => new Proxy(bindings, { has:() => true, get(target, key) {
    if (key === Symbol.unscopables) return undefined;
    if (key in target) return target[key];
    if (key in captured) return captured[key];
    if (/^set[A-Z]/.test(key)) return target[key] = value => { const name = key[3].toLowerCase() + key.slice(4); state[name] = typeof value === "function" ? value(state[name]) : value; stateWrites.push({ name, value:state[name] }); };
    if (key.endsWith("Ref")) return target[key] = ref(null);
    throw new Error(`Missing share fixture binding ${String(key)}`);
  } });
  const evaluate = code => compile(code, scopeFor(state));
  let lastDependencies, serializer;
  const serialize = () => {
    const dependencies = evaluate(serializerDependencies);
    if (!lastDependencies || dependencies.some((value, index) => !Object.is(value, lastDependencies[index]))) {
      lastDependencies = dependencies;
      serializer = compile(callbacks.get("buildExplorerParams"), scopeFor({ ...state }));
    }
    return serializer();
  };
  bindings.buildExplorerParams = serialize;
  return { state, bindings, copied, messages, carriers, moves, stateWrites, serialize,
    share:() => evaluate(callbacks.get("shareView"))(),
    restore(value) { bindings.window.location.search = typeof value === "string" ? value : `?${value}`; evaluate(callbacks.get("restoreExplorerFromUrl"))(); },
    present() { bindings.mapRef.current = mapStub; return evaluate(callbacks.get("setTerrainPresentation"))(mapStub, true, state.verticalExaggeration); },
  };
}

test("actual Share current view round-trips both allowlisted DEMs into the first terrain carrier", async () => {
  for (const provider of ["mapzen", "usgs-3dep"]) {
    const sender = fixture({ provider }); await sender.share();
    const url = new URL(sender.copied[0]); assert.equal(url.searchParams.get("dem"), provider);
    assert.equal(url.searchParams.get("scene"), "elevation-3d"); assert.equal(url.searchParams.get("zscale"), "1.5");
    const receiver = fixture({ provider:provider === "mapzen" ? "usgs-3dep" : "mapzen" }); receiver.restore(url.search);
    assert.equal(receiver.state.terrainProvider, provider); assert.equal(receiver.bindings.terrainProviderRef.current, provider);
    assert.equal(receiver.state.scenePreset, "elevation-3d"); assert.equal(receiver.state.verticalExaggeration, 1.5);
    assert.deepEqual(receiver.state.view, camera); assert.deepEqual(receiver.state.analysisArea, sender.state.analysisArea);
    assert.equal(receiver.bindings.explorerRestoredRef.current, true);
    receiver.present(); assert.equal(receiver.carriers[0].carrier.id, terrain.terrainSourceFor(provider).id);
    assert.equal(receiver.carriers[0].scale, 1.5); assert.match(receiver.carriers[0].carrier.boundary, /not|does not/i);
  }
});

test("changing only the selected DEM refreshes the memoized serializer and tab history", () => {
  const f = fixture(); const first = f.serialize();
  f.state.terrainProvider = "usgs-3dep"; const second = f.serialize();
  assert.equal(first.get("dem"), "mapzen"); assert.equal(second.get("dem"), "usgs-3dep");
  assert.notEqual(first.toString(), second.toString());
  history.saveExplorerHistoryView(second, f.bindings.window.history);
  f.state.terrainProvider = "mapzen"; f.restore("?dem=mapzen");
  assert.equal(f.state.terrainProvider, "usgs-3dep", "existing tab-history semantics use the saved view");
  assert.equal(f.bindings.window.history.state.router, "retained");
});

test("legacy, blank and unrecognized DEM parameters select Mapzen without retaining a previous carrier", () => {
  for (const value of [null, "", "MAPZEN", "USGS-3DEP", "other", "https://untrusted.invalid/dem", "__proto__"]) {
    const f = fixture({ provider:"usgs-3dep", map:true }), params = f.serialize();
    if (value === null) params.delete("dem"); else params.set("dem", value);
    f.restore(params);
    assert.equal(f.state.terrainProvider, "mapzen", String(value)); assert.equal(f.bindings.terrainProviderRef.current, "mapzen");
    assert.equal(f.bindings.attachedTerrainProviderRef.current, null); assert.equal(f.state.terrainElevationReading, null); assert.equal(f.state.terrainElevationUnavailable, null); assert.equal(f.state.terrainState, "LOADING");
    assert.equal(f.state.scenePreset, "elevation-3d"); assert.deepEqual(f.state.view, camera); assert.equal(f.state.layerPreferencesReady, true);
    f.present(); assert.equal(f.carriers[0].carrier.id, terrain.terrainSourceFor("mapzen").id);
  }
});

test("same-page A→B→A DEM restoration clears prior-carrier readiness and readings before effects", () => {
  const f = fixture({ map:true }); const a = f.serialize();
  const b = new URLSearchParams(a); b.set("dem", "usgs-3dep");
  for (const [params, provider] of [[b, "usgs-3dep"], [a, "mapzen"], [b, "usgs-3dep"]]) {
    f.restore(params);
    assert.equal(f.state.terrainProvider, provider); assert.equal(f.bindings.terrainProviderRef.current, provider);
    assert.equal(f.state.terrainElevationReading, null); assert.equal(f.state.terrainElevationUnavailable, null);
    assert.equal(f.state.terrainState, "LOADING"); assert.equal(f.bindings.attachedTerrainProviderRef.current, null);
    f.present(); assert.equal(f.carriers.at(-1).carrier.id, terrain.terrainSourceFor(provider).id);
    f.state.terrainState = "READY"; f.state.terrainElevationReading = { provider, meters:500 };
  }
});

test("DEM sharing preserves camera and AOI redaction while unrelated public view parameters survive", async () => {
  for (const redaction of ["state", "ref"]) {
    const f = fixture({ provider:"usgs-3dep" });
    if (redaction === "state") f.state.locationCameraRedacted = true; else f.bindings.locationDerivedViewRef.current = true;
    await f.share(); const params = new URL(f.copied[0]).searchParams;
    assert.equal(params.get("dem"), "usgs-3dep"); assert.equal(params.get("privacy"), "location-camera-redacted"); assert.equal(params.has("aoi"), false);
    assert.equal(params.get("c"), "-98.38000,38.48000"); assert.equal(params.get("z"), "5.45"); assert.equal(params.has("p"), false);
    const receiver = fixture(); receiver.restore(params);
    assert.deepEqual(receiver.state.view, KANSAS); assert.equal(receiver.state.analysisArea, null); assert.equal(receiver.state.locationCameraRedacted, true);
    assert.equal(receiver.state.terrainProvider, "usgs-3dep"); assert.equal(receiver.state.basemap, "midnight");
    assert.equal(receiver.state.opacity["synthetic-layer"], .7); assert.deepEqual(receiver.state.layerOrder, ["synthetic-layer"]);
    assert.equal(receiver.state.year, 2026); assert.equal(receiver.state.atmospherePreset, "clear"); assert.equal(receiver.state.lightAzimuth, 235); assert.equal(receiver.state.fieldOfView, 36);
  }
});
