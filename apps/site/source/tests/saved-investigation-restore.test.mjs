import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import ts from "typescript";
import { componentHarness, findNode } from "./component-harness.mjs";

const modules = new Map();
async function moduleUrl(file) {
  const resolved = path.resolve(file); if (modules.has(resolved)) return modules.get(resolved);
  let js = ts.transpileModule(await readFile(resolved, "utf8"), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
  for (const match of [...js.matchAll(/from ["'](\.[^"']+)["']/g)]) js = js.replace(match[0], `from ${JSON.stringify(await moduleUrl(path.resolve(path.dirname(resolved), match[1]) + ".ts"))}`);
  const url = `data:text/javascript;base64,${Buffer.from(js).toString("base64")}`; modules.set(resolved, url); return url;
}
const saved = await import(await moduleUrl("app/saved-workspaces.ts"));
const trail = await import(await moduleUrl("app/places-trail.ts"));
const research = await import(await moduleUrl("app/research-context.ts"));
const subsurface = await import(await moduleUrl("app/subsurface-model.ts"));
const history = await import(await moduleUrl("app/explorer-layer-history.ts"));
const context = await import(await moduleUrl("app/live-context.ts"));
const smoke = await import(await moduleUrl("app/hms-smoke-playback.ts"));
const source = await readFile("app/page.tsx", "utf8");
const ast = ts.createSourceFile("page.tsx", source, ts.ScriptTarget.ES2022, true, ts.ScriptKind.TSX), callbacks = new Map();
let placesMarkup, initialView, constructorPitchLimit;
function visit(node) {
  if (ts.isVariableDeclaration(node) && node.initializer) {
    const init = node.initializer;
    if (ts.isArrowFunction(init)) callbacks.set(node.name.getText(ast), init.getText(ast));
    else if (ts.isCallExpression(init) && init.expression.getText(ast) === "useCallback") callbacks.set(node.name.getText(ast), init.arguments[0].getText(ast));
    if (node.name.getText(ast) === "initialView") initialView = init.getText(ast);
  }
  if (ts.isJsxElement(node) && node.openingElement.attributes.properties.some(p => ts.isJsxAttribute(p) && p.name.getText(ast) === "className" && p.initializer?.text?.includes("places-trail-section"))) placesMarkup = node.getText(ast);
  if (ts.isPropertyAssignment(node) && node.name.getText(ast) === "maxPitch" && node.initializer.getText(ast).includes("scenePresetRef.current")) constructorPitchLimit = node.initializer.getText(ast);
  ts.forEachChild(node, visit);
}
visit(ast);
const KEY = "kfm-map-workspaces-v1", A = "2026-09-20", B = "2026-09-21", QUAKE = "usgs-earthquakes", ALERT = "nws-alerts", SMOKE = "noaa-hms-smoke";
const KANSAS = { center: [-98.38, 38.48], zoom: 5.45, bearing: 0, pitch: 0 };
const capture = { center: [-99.3, 37.8], zoom: 10, bearing: 10, pitch: 70 };
const payload = (feed, day) => ({ feed, state: "empty", featureCount: 0, data: { type: "FeatureCollection", features: [] }, retrievedAt: "2026-11-09T12:00:00Z", sourceDay: day, ...(feed === SMOKE ? { smokeCoverage: { day } } : {}) });
const settle = async () => { for (let i = 0; i < 24; i++) await Promise.resolve(); };
const textOf = node => typeof node === "string" || typeof node === "number" ? String(node) : node && typeof node === "object" ? [node.props?.children].flat(Infinity).map(textOf).join(" ").replace(/\s+/g, " ") : "";
const find = (node, predicate) => { if (!node || typeof node !== "object") return; if (predicate(node)) return node; for (const child of [node.props?.children].flat(Infinity)) { const hit = find(child, predicate); if (hit) return hit; } };

// Execute the actual page handlers and actual strict models. The only acquisition
// seam returns synthetic allowlisted adapter responses; no network or real storage.
function fixture({ map = false, deferReads = false } = {}) {
  const values = new Map(), messages = [], requests = [], moves = [], visibilityCalls = [], opacityCalls = [];
  let denied = false;
  const state = {
    view: structuredClone(capture), workspaceName: "Synthetic archived investigation A", savedWorkspaces: [], activePlaceId: null,
    locationCameraRedacted: false, researchLocationRedacted: false, subsurfacePrivate: false, researchOpen: false, researchAnchor: null, researchContext: null, subsurfaceContext: null,
    visibility: {}, opacity: {}, layerOrder: [], year: 2026, mapEvidenceFilter: "ALL", basemap: "standard", projection: "mercator", scenePreset: "elevation-3d",
    verticalExaggeration: 1, atmospherePreset: "clear", lightAzimuth: 210, fieldOfView: 36, terrainProvider: "usgs-3dep",
    measurementGeometryMode: null, measureUnit: "imperial", measurement: "Select a measurement tool", analysisArea: null,
    compareTimeA: 1910, compareTimeB: 2026, temporalMode: "snapshot", temporalStepRule: "available-events", sweepRangeStart: 1910, sweepRangeEnd: 2026, movingWindowFrames: 3, playbackDirection: "forward", playbackLoopMode: "stop",
    reportTitle: "Synthetic investigation", reportScope: "VIEWPORT", reportDetail: "STANDARD", reportLayerIds: [], reportSections: { summary: true }, reportQuery: "", reportEvidenceFilter: "ALL", selected: null,
    officialVisibility: Object.fromEntries(context.OFFICIAL_CONTEXT_SOURCES.map(s => [s.id, s.id === QUAKE])),
    officialOpacity: Object.fromEntries(context.OFFICIAL_CONTEXT_SOURCES.map(s => [s.id, s.id === QUAKE ? .7 : s.defaultOpacity])),
    officialArchiveDays: { [QUAKE]: A }, officialPayloads: { [QUAKE]: payload(QUAKE, A) }, officialStates: {}, officialErrors: {},
    leftPanelMode: "places", visibleCount: 0, temporalScopeLabel: "Operational present", placeTourPlaying: false,
  };
  const mapStub = { isStyleLoaded: () => false, setMaxPitch: value => moves.push({ maxPitch: value }), easeTo: value => moves.push(value) };
  const bindings = {
    ...saved, ...trail, ...research, ...subsurface, ...history, ...context,
    Object, Array, Set, Map, Math, Number, Boolean, String, Error, Date, Promise, AbortController, URL, encodeURIComponent, undefined,
    LAYER_REGISTRY: [], defaultOrder: [], defaultReportSections: { summary: true }, KNOWN_TEMPORAL_FRAMES: new Set([1910, 2026]), OFFICIAL_CONTEXT_PRESENT_FRAME: 2026,
    TIME_STEPS: [1910, 2026], DEFAULT_TERRAIN_DEPTH: 1, KANSAS_VIEW: KANSAS, REGIONAL_NAVIGATION_BOUNDS: [[-104.8, 34.8], [-92, 42.2]], evidenceLabels: {}, WORKSPACE_STORAGE_KEY: KEY,
    window: { localStorage: { getItem: key => values.get(key) ?? null, setItem(key, raw) { if (denied) throw new Error("quota denied"); values.set(key, raw); } } },
    locationDerivedViewRef: { current: false }, pendingViewRef: { current: null }, mapRef: { current: map ? mapStub : null },
    officialVisibilityRef: { current: state.officialVisibility }, officialOpacityRef: { current: state.officialOpacity }, officialArchiveDaysRef: { current: { [QUAKE]: A } },
    officialArchivePayloadsRef: { current: { [QUAKE]: payload(QUAKE, A) } }, officialPayloadsRef: { current: state.officialPayloads }, officialRequestsRef: { current: new Map() },
    terrainProviderRef: { current: "usgs-3dep" }, scenePresetRef: { current: "overview-2d" }, buildYearCurrentRef: { current: true }, temporalQueryRef: { current: { frame: 2026 } },
    layerJsonReadsRef: { current: { read(url, options) {
      assert.ok(context.OFFICIAL_CONTEXT_SOURCES.some(s => s.apiPath && (url === s.apiPath || url.startsWith(`${s.apiPath}&day=`))), "only the existing fixed source adapter path may be read");
      const item = { url, options }; requests.push(item);
      const feed = context.OFFICIAL_CONTEXT_SOURCES.find(s => s.apiPath && (url === s.apiPath || url.startsWith(`${s.apiPath}&day=`))).id;
      const body = payload(feed, new URL(url, "https://synthetic.test").searchParams.get("day") ?? undefined);
      if (deferReads) return new Promise(resolve => { item.resolve = value => resolve({ response: Response.json(value ?? body), body: value ?? body }); });
      return Promise.resolve({ response: Response.json(body), body });
    } } },
    clamp: (v, low, high) => Math.max(low, Math.min(high, v)), terrainDepth: v => v, motionDuration: v => v, currentUtcDay: () => "2026-11-09",
    stopSceneOrbit() {}, applyProjectionNavigationLimits() {}, announce: message => messages.push(message), isCompact: false,
    earthquakeEventTimes: () => [], readFireDay: async () => null, formatTimelineStep: String,
    jsx: (type, props, ...children) => ({ type, props: { ...props, children } }),
  };
  const scope = new Proxy(bindings, { has: () => true, get(target, key) {
    if (key === Symbol.unscopables) return undefined;
    if (key === "visibleOfficialSources") return context.OFFICIAL_CONTEXT_SOURCES.filter(s => state.officialVisibility[s.id]);
    if (key in target) return target[key]; if (key in state) return state[key];
    if (/^set[A-Z]/.test(key)) return target[key] = value => { const name = key[3].toLowerCase() + key.slice(4); state[name] = typeof value === "function" ? value(state[name]) : value; };
    if (key.endsWith("Ref")) return target[key] = { current: null };
    throw new Error(`Missing investigation fixture binding ${String(key)}`);
  } });
  const evaluate = code => new Function("scope", `with(scope){${ts.transpileModule(`return (${code});`, { compilerOptions: { target: ts.ScriptTarget.ES2022, jsx: ts.JsxEmit.React, jsxFactory: "jsx" } }).outputText}}`)(scope);
  for (const name of ["validLayerPayload", "refreshOfficialContext", "loadOfficialArchiveDay", "setOfficialContextVisible", "setOfficialContextOpacity", "chooseTerrainProvider", "persistSavedWorkspaces", "saveCurrentWorkspace", "loadSavedWorkspace", "stopPlaceTour", "reorderSavedWorkspace", "deleteSavedWorkspace"]) {
    assert.ok(callbacks.has(name), name); bindings[name] = evaluate(callbacks.get(name));
  }
  const visible = bindings.setOfficialContextVisible, opacity = bindings.setOfficialContextOpacity;
  bindings.setOfficialContextVisible = (id, selected) => { visibilityCalls.push({ id, selected, day: bindings.officialArchiveDaysRef.current[id] }); visible(id, selected); };
  bindings.setOfficialContextOpacity = (id, value) => { opacityCalls.push({ id, value }); opacity(id, value); };
  return { state, bindings, values, messages, requests, moves, visibilityCalls, opacityCalls, evaluate,
    save() { bindings.saveCurrentWorkspace(); return state.savedWorkspaces[0]; },
    load(snapshot) { bindings.loadSavedWorkspace(snapshot); },
    render() { assert.ok(placesMarkup); return evaluate(placesMarkup); },
    deny() { denied = true; },
    changeToB() {
      state.officialVisibility = { ...state.officialVisibility, [QUAKE]: false, [ALERT]: true }; bindings.officialVisibilityRef.current = state.officialVisibility;
      state.officialOpacity = { ...state.officialOpacity, [QUAKE]: .2 }; bindings.officialOpacityRef.current = state.officialOpacity;
      state.officialArchiveDays = { [QUAKE]: B }; bindings.officialArchiveDaysRef.current = state.officialArchiveDays;
      state.officialPayloads = { [QUAKE]: payload(QUAKE, B) }; bindings.officialPayloadsRef.current = state.officialPayloads; bindings.officialArchivePayloadsRef.current = { [QUAKE]: payload(QUAKE, B) };
      state.terrainProvider = "mapzen"; bindings.terrainProviderRef.current = "mapzen";
      state.view = { center: [-96, 39], zoom: 7, bearing: 40, pitch: 10 };
    },
  };
}

test("actual Place save and library restore recover public layers, opacity, committed day and DEM after A to B", async () => {
  const f = fixture(), snapshot = f.save();
  assert.equal(saved.validSavedWorkspaceRecord(snapshot), true); assert.equal(snapshot.sourceSettings.visibility[QUAKE], true);
  assert.equal(snapshot.sourceSettings.archiveDays[QUAKE], A); assert.equal(snapshot.sourceSettings.terrainProvider, "usgs-3dep");
  f.changeToB();
  const row = find(f.render(), node => node.props?.className === "place-stop-main"); row.props.onClick(); await settle();
  assert.equal(f.state.officialVisibility[QUAKE], true); assert.equal(f.state.officialVisibility[ALERT], false); assert.equal(f.state.officialOpacity[QUAKE], .7);
  assert.equal(f.state.officialArchiveDays[QUAKE], A); assert.equal(f.state.terrainProvider, "usgs-3dep");
  assert.equal(f.requests.length, 1); assert.match(f.requests[0].url, /day=2026-09-20$/);
  assert.equal(f.bindings.officialPayloadsRef.current[QUAKE].sourceDay, A);
  assert.deepEqual(f.state.view, capture); assert.deepEqual(f.bindings.pendingViewRef.current, capture);
  assert.match(f.messages.at(-1), /saved source settings restored|dated source records|no mapped records returned/);
  assert.equal(JSON.parse(f.values.get(KEY))[0].sourceSettings.archiveDays[QUAKE], A);
});

test("a superseded dated request cannot overwrite the reopened Place", async () => {
  const f = fixture({ deferReads: true }), snapshot = f.save(); f.changeToB();
  const old = f.bindings.loadOfficialArchiveDay(QUAKE, B, true); await settle();
  assert.equal(f.requests.length, 1); f.load(snapshot); await settle(); assert.equal(f.requests.length, 2);
  assert.equal(f.requests[0].options.signal.aborted, true);
  f.requests[1].resolve(); await settle(); f.requests[0].resolve(); await old; await settle();
  assert.equal(f.bindings.officialPayloadsRef.current[QUAKE].sourceDay, A); assert.equal(f.state.officialArchiveDays[QUAKE], A);
});

test("pending, failed, wrong-day and uncommitted smoke targets cannot become a saved archive date", () => {
  for (const bad of [undefined, { ...payload(QUAKE, A), state: "error" }, payload(QUAKE, B)]) {
    const f = fixture(); f.bindings.officialArchivePayloadsRef.current[QUAKE] = bad;
    assert.equal(f.save(), undefined); assert.equal(f.values.size, 0); assert.equal(f.state.activePlaceId, null); assert.match(f.messages.at(-1), /has not finished loading/);
  }
  const f = fixture(); f.state.officialVisibility[SMOKE] = true; f.state.officialArchiveDays[SMOKE] = A;
  f.bindings.officialArchivePayloadsRef.current[SMOKE] = payload(SMOKE, A);
  f.bindings.officialArchiveDaysRef.current[SMOKE] = B;
  const snapshot = f.save(); assert.equal(snapshot.sourceSettings.archiveDays[SMOKE], A, "the displayed committed day wins over a merely reserved playback request");
});

test("camera is queued before acquisition and survives initialization, including bounded globe and regional views", async () => {
  const f = fixture(), snapshot = f.save(); f.changeToB(); f.load(snapshot);
  assert.deepEqual(f.evaluate(initialView), capture, "run the constructor's actual initial-view expression after early restore");
  assert.ok(constructorPitchLimit); assert.equal(f.evaluate(constructorPitchLimit), 72, "the constructor must use the restored terrain limit before any React effects run");
  assert.equal(f.bindings.projectionRef.current, "mercator"); assert.equal(f.bindings.basemapRef.current, "standard");
  assert.equal(f.bindings.terrainProviderRef.current, "usgs-3dep");
  assert.deepEqual(f.state.view, capture); assert.deepEqual(f.bindings.cameraHistoryRef.current, [capture]);
  const global = { ...snapshot, projection: "globe", view: { center: [250, 95], zoom: -4, bearing: 400, pitch: 100 } };
  f.load(global); assert.deepEqual(f.state.view, { center: [180, 85], zoom: 0, bearing: 180, pitch: 72 });
  f.load({ ...global, projection: "mercator", scene: { ...snapshot.scene, preset: "overview-2d" } });
  assert.deepEqual(f.state.view, { center: [-92, 42.2], zoom: 4, bearing: 180, pitch: 60 });
  assert.equal(f.evaluate(constructorPitchLimit), 60);
  await settle();
});

test("a ready map receives the same safe queued camera and full terrain pitch", async () => {
  const f = fixture({ map: true }), snapshot = f.save(); f.changeToB(); f.load(snapshot);
  assert.ok(f.moves.some(item => item.maxPitch === 72));
  assert.deepEqual(f.moves.at(-1), { ...capture, duration: 650 }); assert.deepEqual(f.bindings.pendingViewRef.current, capture);
  await settle();
});

test("legacy saves retain their sources with an explicit notice and no invented exact replay", () => {
  const f = fixture(), snapshot = f.save(), legacy = { ...snapshot }; delete legacy.sourceSettings;
  f.state.savedWorkspaces = [legacy]; f.changeToB(); f.load(legacy);
  assert.equal(f.state.officialVisibility[QUAKE], false); assert.equal(f.state.officialVisibility[ALERT], true);
  assert.equal(f.state.officialArchiveDays[QUAKE], B); assert.equal(f.state.terrainProvider, "mapzen");
  assert.equal(f.requests.length, 0); assert.match(f.messages.at(-1), /legacy save.*not recorded; current settings retained/);
  assert.match(textOf(f.render()), /public source\/date\/DEM settings not recorded/);
  assert.equal(saved.parseSavedWorkspaceList(JSON.stringify([legacy]), 12).records.length, 1);
});

test("location-derived or legacy cameras and AOIs stay generalized; no provider rows or private contexts are serialized", () => {
  const f = fixture(); f.state.locationCameraRedacted = true;
  f.state.analysisArea = { west: -99.31, east: -99.29, south: 37.79, north: 37.81 };
  f.bindings.officialArchivePayloadsRef.current[QUAKE] = { ...payload(QUAKE, A), featureCount: 1, data: { type: "FeatureCollection", features: [{ id: "SYNTHETIC-MEASUREMENT-DO-NOT-CACHE" }] } };
  const snapshot = f.save(), raw = f.values.get(KEY);
  assert.deepEqual(snapshot.view, KANSAS); assert.equal(snapshot.analysisArea, null); assert.equal(snapshot.measurement, null);
  assert.equal(JSON.parse(raw)[0].researchContext, undefined); assert.equal(JSON.parse(raw)[0].subsurfaceContext, undefined); assert.doesNotMatch(raw, /SYNTHETIC-MEASUREMENT-DO-NOT-CACHE/);
  const legacy = { ...snapshot, view: capture, analysisArea: f.state.analysisArea }; delete legacy.locationCameraRedacted; delete legacy.sourceSettings;
  f.load(legacy); assert.deepEqual(f.state.view, KANSAS); assert.equal(f.state.analysisArea, null); assert.equal(f.state.locationCameraRedacted, true);
});

test("removed public source identities never activate unknown providers and current selection counts include public sources", () => {
  const f = fixture(), snapshot = f.save();
  assert.match(textOf(f.render()), /1 selected public \/ registry layers/); assert.match(textOf(f.render()), /does not confirm loaded or verified/);
  assert.match(textOf(f.render()), /1 selected layers/);
  const unavailable = { ...snapshot, sourceSettings: { ...snapshot.sourceSettings, visibility: { "retired-public-source": true } } };
  assert.equal(saved.validSavedWorkspaceRecord(unavailable), true); f.changeToB(); f.load(unavailable);
  assert.equal(f.visibilityCalls.some(call => call.id === "retired-public-source"), false); assert.equal(f.requests.length, 0);
  assert.match(f.messages.at(-1), /saved sources or archive dates are unavailable/);
});

test("storage failure preserves the library and current investigation instead of reporting a save", () => {
  const f = fixture(), first = f.save(), bytes = f.values.get(KEY); f.deny(); f.state.workspaceName = "Unsaved second Place";
  f.save(); assert.equal(f.values.get(KEY), bytes); assert.equal(f.state.savedWorkspaces.length, 1); assert.equal(f.state.savedWorkspaces[0], first);
  assert.match(f.messages.at(-1), /could not be saved/);
});

const deferred = () => { let resolve; const promise = new Promise(done => { resolve = done; }); return { promise, resolve }; };
const smokePayload = (day, marker) => ({ ...payload(SMOKE, day), marker, smokeCoverage:{ day, availableDays:[day], missingDays:[] } });
async function playbackFixture({ upload = false } = {}) {
  const f = fixture({ map:true, deferReads:true }), b = f.bindings, s = f.state;
  const source = { type:"geojson" }, reads = [], frames = [], paints = [], advanceTimers = [], uploadWait = deferred(); let uploaded;
  b.smokePlaybackGenerationRef = { current:0 }; b.smokePlaybackCancelRef = { current:null };
  b.smokeTransitionsRef = { current:new smoke.HmsFrameTransitions() };
  b.mapRef.current.getSource = () => source; b.styleGenerationReadyRef = { current:true };
  b.runMapMutation = (_label, mutate) => { mutate(); return true; };
  b.runtimeOfficialVisibility = visibility => visibility; b.applyOfficialContextState = () => {};
  b.noaaRadarReadyRef = { current:false }; b.noaaRadarFrameTimeRef = { current:null };
  b.smokeValidityTimes = () => []; b.smokeInitialFrameIndex = () => -1;
  b.geoJSONHasData = () => true; b.hmsFade = async () => {};
  b.resetHmsSmokeFade = () => paints.push("reset"); b.setHmsSmokeFade = (_map, factor) => paints.push(factor);
  b.waitForGeoJSON = (_source, signal) => { uploaded = signal; return upload ? uploadWait.promise : Promise.resolve(); };
  function committed(day) {
    const value = smokePayload(day, `committed-${day}`);
    s.officialVisibility[SMOKE] = true; s.officialArchiveDays[SMOKE] = day; s.officialPayloads = { ...s.officialPayloads, [SMOKE]:value };
    b.officialVisibilityRef.current = s.officialVisibility; b.officialArchiveDaysRef.current = { ...b.officialArchiveDaysRef.current, [SMOKE]:day };
    b.officialPayloadsRef.current = s.officialPayloads; b.officialArchivePayloadsRef.current[SMOKE] = value;
  }
  committed(A); const savedA = f.save(), savedB = { ...savedA, id:"synthetic-b", sourceSettings:{ ...savedA.sourceSettings, archiveDays:{ ...savedA.sourceSettings.archiveDays, [SMOKE]:B } } };
  const reserve = f.evaluate(callbacks.get("reserveSmokePlayback")), commit = f.evaluate(callbacks.get("commitSmokePlayback"));
  const h = await componentHarness("app/hms-smoke-playback-control.tsx", {
    "./hms-smoke-playback":{ ...smoke, HmsFrameCache:class extends smoke.HmsFrameCache {
      constructor() { super((url, options) => { const request = { url, signal:options.signal, ...deferred() }; reads.push(request); return request.promise; }); }
    } },
  }, {
    document:{ hidden:false, addEventListener() {}, removeEventListener() {} },
    setTimeout:(fn, delay) => { const timer = { fn, delay, canceled:false }; advanceTimers.push(timer); return timer; }, clearTimeout:timer => { timer.canceled = true; }, setInterval:() => 1, clearInterval() {},
  });
  const render = () => { const tree = h.render(h.exports.HmsSmokePlayback, {
    enabled:true, reducedMotion:false, displayedDay:s.officialArchiveDays[SMOKE], payload:s.officialPayloads[SMOKE], cancelRef:b.smokePlaybackCancelRef,
    onReserve:reserve, onFrame:(...args) => { frames.push(args); return commit(...args); }, onCurrent() {},
  }); h.commit(); return tree; };
  render();
  return { ...f, reads, frames, paints, advanceTimers, savedA, savedB, committed, render, uploaded:() => uploaded,
    async start(day) {
      let tree = render(); findNode(tree, n => n.props?.["aria-label"] === "HMS from date").props.onChange({ target:{ value:day } });
      findNode(tree, n => n.props?.["aria-label"] === "HMS through date").props.onChange({ target:{ value:day } }); tree = render();
      findNode(tree, n => n.type === "button" && n.props.children === "Check / retry day").props.onClick(); await settle();
    },
    async play(from, through) {
      let tree = render(); findNode(tree, n => n.props?.["aria-label"] === "HMS from date").props.onChange({ target:{ value:from } });
      findNode(tree, n => n.props?.["aria-label"] === "HMS through date").props.onChange({ target:{ value:through } }); tree = render();
      findNode(tree, n => n.type === "button" && n.props.children === "Play").props.onClick(); await settle();
    },
    async respond(index = 0, marker = "old-playback") { const read = reads[index], day = new URL(read.url, "https://synthetic.test").searchParams.get("day"); read.resolve(Response.json(smokePayload(day, marker))); await settle(); await settle(); },
    async settleRestore(marker = "fresh-restored") {
      for (const request of f.requests) request.resolve(smokePayload(new URL(request.url, "https://synthetic.test").searchParams.get("day"), marker));
      await settle(); await settle();
    },
    async finishUpload() { uploadWait.resolve(); await settle(); await settle(); },
    dispose() { h.dispose(); assert.equal(b.smokePlaybackCancelRef.current, null); },
  };
}

test("Place restore synchronously cancels pending smoke reads before passive cleanup, including same-day and A→B→A", async () => {
  for (const requestDay of [A, B]) {
    const f = await playbackFixture();
    try {
      await f.start(requestDay); assert.equal(f.reads.length, 1); assert.equal(f.reads[0].signal.aborted, false);
      f.load(f.savedB); f.load(f.savedA);
      // Deliberately do not render the child: cancellation must happen in the restore event.
      assert.equal(f.reads[0].signal.aborted, true); assert.equal(f.bindings.smokePlaybackGenerationRef.current, 2);
      await f.settleRestore(); await f.respond();
      assert.equal(f.frames.length, 0); assert.equal(f.state.officialArchiveDays[SMOKE], A); assert.equal(f.bindings.officialPayloadsRef.current[SMOKE].marker, "fresh-restored");
      assert.match(textOf(f.render()), /Check \/ retry day/);
    } finally { f.dispose(); }
  }
});

test("same-day Place restore clears a tentative upload, aborts its transition, and prevents late rollback", async () => {
  const f = await playbackFixture({ upload:true });
  try {
    await f.start(A); await f.respond(); assert.ok(f.uploaded()); assert.equal(f.bindings.officialPayloadsRef.current[SMOKE].marker, "old-playback");
    f.load(f.savedA);
    assert.equal(f.frames[0][2].aborted, true); assert.equal(f.uploaded().aborted, true);
    assert.equal(f.bindings.officialPayloadsRef.current[SMOKE], undefined, "same-day takeover must not retain uncommitted geometry");
    assert.equal(f.requests.filter(request => request.url.includes(`day=${A}`)).length, 1);
    await f.settleRestore(); const fresh = f.bindings.officialPayloadsRef.current[SMOKE], paints = f.paints.length;
    await f.finishUpload(); assert.equal(f.bindings.officialPayloadsRef.current[SMOKE], fresh); assert.equal(fresh.marker, "fresh-restored"); assert.equal(f.paints.length, paints, "old finally cannot change the restored frame's presentation");
    assert.equal(f.state.officialArchiveDays[SMOKE], A); assert.equal(f.bindings.officialArchivePayloadsRef.current[SMOKE], fresh);
  } finally { f.dispose(); }
});

test("an active smoke A upload cannot overwrite fresh A after Place A→B→A handoff", async () => {
  const f = await playbackFixture({ upload:true });
  try {
    f.committed(B); f.render(); await f.start(A); await f.respond(); assert.ok(f.uploaded());
    f.load(f.savedB); f.load(f.savedA); assert.equal(f.uploaded().aborted, true); assert.equal(f.bindings.smokePlaybackGenerationRef.current, 2);
    await f.settleRestore(); const fresh = f.bindings.officialPayloadsRef.current[SMOKE]; await f.finishUpload();
    assert.equal(fresh.marker, "fresh-restored"); assert.equal(f.bindings.officialPayloadsRef.current[SMOKE], fresh); assert.equal(f.state.officialArchiveDays[SMOKE], A);
    assert.equal(f.requests[0].options.signal.aborted, true, "superseded fresh B read is canceled too");
  } finally { f.dispose(); }
});

test("legacy Place takeover restores only the last committed smoke frame while canceling an upload", async () => {
  const f = await playbackFixture({ upload:true });
  try {
    await f.start(B); await f.respond(); const legacy = { ...f.savedA }; delete legacy.sourceSettings;
    f.load(legacy); assert.equal(f.uploaded().aborted, true); assert.equal(f.bindings.officialPayloadsRef.current[SMOKE].marker, `committed-${A}`);
    assert.equal(f.bindings.officialArchiveDaysRef.current[SMOKE], A); assert.equal(f.requests.length, 0);
    const committed = f.bindings.officialPayloadsRef.current[SMOKE]; await f.finishUpload(); assert.equal(f.bindings.officialPayloadsRef.current[SMOKE], committed); assert.equal(f.state.officialArchiveDays[SMOKE], A);
    assert.match(f.messages.at(-1), /legacy save/);
  } finally { f.dispose(); }
});

test("restore cancels prefetch and invalidates an already-queued advance callback before child effects run", async () => {
  const f = await playbackFixture();
  try {
    await f.play(A, B); await f.respond(); f.render();
    assert.equal(f.reads.length, 2, "successful A starts the bounded B prefetch");
    const advance = f.advanceTimers.find(timer => timer.delay === 1500 && !timer.canceled); assert.ok(advance);
    f.load(f.savedA); assert.equal(f.reads[1].signal.aborted, true);
    const count = f.reads.length, generation = f.bindings.smokePlaybackGenerationRef.current;
    advance.fn(); await settle();
    assert.equal(f.reads.length, count, "a callback queued before restore cannot reserve or request another day");
    assert.equal(f.bindings.officialArchiveDaysRef.current[SMOKE], A); assert.equal(f.bindings.smokePlaybackGenerationRef.current, generation);
    await f.settleRestore(); await f.respond(1, "late-prefetch"); assert.equal(f.frames.length, 1); assert.equal(f.state.officialArchiveDays[SMOKE], A); assert.equal(f.bindings.officialPayloadsRef.current[SMOKE].marker, "fresh-restored");
  } finally { f.dispose(); }
});
