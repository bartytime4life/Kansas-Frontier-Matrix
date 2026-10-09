import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { pathToFileURL } from "node:url";
import { createRequire } from "node:module";
import test from "node:test";
import ts from "typescript";

const require = createRequire(import.meta.url);
const read = (path) => readFile(new URL(`../${path}`, import.meta.url), "utf8");
const toUrl = (source) => `data:text/javascript;base64,${Buffer.from(source).toString("base64")}`;
const transpile = (source) => ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022, jsx: ts.JsxEmit.ReactJSX } }).outputText;
const sceneSource = await read("app/scene-effects.ts");
const sceneTree = ts.createSourceFile("effects.ts", sceneSource, ts.ScriptTarget.Latest, true);
const declaration = (tree, statements, name) => statements.find((node) => ts.isVariableStatement(node) && node.declarationList.declarations.some((decl) => decl.name.getText(tree) === name)).declarationList.declarations.find((decl) => decl.name.getText(tree) === name);
const stops = new Function(`${transpile(`const stops = ${declaration(sceneTree, sceneTree.statements, "KANSAS_FLYOVER").initializer.getText(sceneTree)};`)} return stops;`)();
const pageSource = await read("app/page.tsx");
const pageTree = ts.createSourceFile("page.tsx", pageSource, ts.ScriptTarget.Latest, true, ts.ScriptKind.TSX);
const home = pageTree.statements.find((node) => ts.isFunctionDeclaration(node) && node.name?.text === "Home");
function evaluate(initializer, context) {
  return new Function(...Object.keys(context), `${transpile(`const callback = ${initializer};`)} return callback;`)(...Object.values(context));
}
const pageCallback = (name, context) => evaluate(declaration(pageTree, home.body.statements, name).initializer.getText(pageTree), context);
const pageEffect = (needle, context) => {
  const node = home.body.statements.find((node) => ts.isExpressionStatement(node) && ts.isCallExpression(node.expression) && node.expression.expression.getText(pageTree) === "useEffect" && node.expression.arguments[0].getText(pageTree).includes(needle));
  assert.ok(node, `effect containing ${needle}`);
  return evaluate(node.expression.arguments[0].getText(pageTree), context);
};

test("real landscape callback preserves chosen source, scale, look, lens and data while changing only viewpoint/representation", () => {
  for (const reduced of [false, true]) {
    for (const stop of stops.filter((stop) => stop.id !== "return")) {
      const events = [];
      const map = { setMaxPitch: (value) => events.push(["maxPitch", value]), setProjection: (value) => events.push(["mapProjection", value]), easeTo: (value) => events.push(["camera", value]) };
      const context = {
        KANSAS_FLYOVER: stops, mapRef: { current: map }, stopFlyover: () => events.push(["stopFlyover"]), stopSceneOrbit: () => events.push(["stopOrbit"]),
        projectionRef: { current: "globe" }, scenePresetRef: { current: "globe-overview" }, setProjection: (value) => events.push(["projection", value]), setScenePreset: (value) => events.push(["scene", value]),
        replayingCameraHistoryRef: { current: true }, runMapMutation: (_label, callback) => callback(), applyProjectionNavigationLimits: (_map, value) => events.push(["limits", value]),
        styleGenerationReadyRef: { current: true }, setTerrainState: (value) => events.push(["terrain", value]),
        setTerrainPresentation: (_map, enabled, scale) => { events.push(["terrainPresentation", enabled, scale]); return "READY"; },
        verticalExaggerationRef: { current: 1.35 }, topographicOverlayRef: { current: true }, setTerrainHeightOverlay: (_map, value) => events.push(["heightOverlay", value]),
        motionDuration: (duration) => reduced ? 0 : duration, announce() {},
        // Existing presentation/data choices deliberately differ from defaults.
        basemapRef: { current: "imagery" }, terrainProviderRef: { current: "usgs-3dep" }, atmospherePresetRef: { current: "dusk" }, lightAzimuthRef: { current: 265 }, fieldOfViewRef: { current: 29 },
        selectedRef: { current: "feature-1" }, yearRef: { current: 1980 }, visibilityRef: { current: { water: true } },
      };
      const preserved = ["basemapRef", "terrainProviderRef", "atmospherePresetRef", "lightAzimuthRef", "fieldOfViewRef", "selectedRef", "yearRef", "visibilityRef", "verticalExaggerationRef"].map((key) => [key, structuredClone(context[key])]);
      const visit = pageCallback("chooseLandscape", context);
      visit(stop.id);
      for (const [key, before] of preserved) assert.deepEqual(context[key], before, key);
      assert.deepEqual(events.slice(0, 2), [["stopFlyover"], ["stopOrbit"]]);
      assert.ok(events.some(([name, enabled, scale]) => name === "terrainPresentation" && enabled && scale === 1.35));
      assert.deepEqual(events.at(-1), ["camera", { center: [...stop.center], zoom: stop.zoom, pitch: stop.pitch, bearing: stop.bearing, duration: reduced ? 0 : 900, essential: false }]);
      const count = events.length;
      visit("return"); visit("unknown");
      assert.equal(events.length, count, "only the six approved viewpoints run");
    }
  }
});

function eventTarget() {
  const events = new Map();
  return { events, addEventListener(type, callback) { if (!events.has(type)) events.set(type, new Set()); events.get(type).add(callback); }, removeEventListener(type, callback) { events.get(type)?.delete(callback); }, fire(type) { for (const callback of [...(events.get(type) ?? [])]) callback(); } };
}
function orbitFixture() {
  const container = eventTarget(), document = { ...eventTarget(), hidden: false };
  const mapEvents = eventTarget(), calls = [], timers = new Map();
  let reduced = false, orbiting = false;
  const map = { getContainer: () => container, getBearing: () => 25, getPitch: () => 50, stop: () => calls.push(["stop"]), easeTo: (value) => calls.push(["ease", value]), once: (type, callback) => mapEvents.addEventListener(type, callback), off: (type, callback) => mapEvents.removeEventListener(type, callback) };
  const context = {
    mapRef: { current: map }, document, window: { matchMedia: () => ({ matches: reduced }), setTimeout: (callback) => { timers.set(1, callback); return 1; }, clearTimeout: (key) => timers.delete(key) },
    announce() {}, projectionRef: { current: "mercator" }, scenePresetRef: { current: "elevation-3d" }, basemapRef: { current: "imagery" },
    sceneOrbitTimerRef: { current: null }, sceneOrbitCancelRef: { current: null }, sceneOrbitContextRef: { current: "" }, replayingCameraHistoryRef: { current: false },
    stopFlyover: () => calls.push(["stopFlyover"]), setSceneOrbiting: (value) => { orbiting = value; }, useCallback: (callback) => callback,
  };
  context.stopSceneOrbit = pageCallback("stopSceneOrbit", context);
  const start = pageCallback("startSceneOrbit", context);
  return { start, context, mapEvents, container, document, calls, timers, orbiting: () => orbiting, reduce: () => { reduced = true; } };
}

test("existing orbit mutually excludes flyover and cleans up on every direct input, hidden tab and natural finish", () => {
  for (const reason of ["pointerdown", "wheel", "touchstart", "keydown", "hidden", "finished"]) {
    const f = orbitFixture();
    f.start();
    assert.equal(f.orbiting(), true);
    assert.equal(f.calls[0][0], "stopFlyover");
    assert.equal(f.calls.find(([name]) => name === "ease")[1].bearing, 115);
    if (reason === "hidden") { f.document.hidden = true; f.document.fire("visibilitychange"); }
    else if (reason === "finished") f.mapEvents.fire("moveend");
    else f.container.fire(reason);
    assert.equal(f.orbiting(), false, reason);
    assert.equal(f.context.sceneOrbitCancelRef.current, null);
    assert.equal(f.timers.size, 0);
    for (const target of [f.container, f.document, f.mapEvents]) for (const listeners of target.events.values()) assert.equal(listeners.size, 0, `listener cleanup: ${reason}`);
  }
});

test("orbit cannot start under reduced motion/hidden/globe and mode changes interrupt existing automation", () => {
  for (const mode of ["reduce", "hidden", "globe"]) {
    const f = orbitFixture();
    if (mode === "reduce") f.reduce();
    if (mode === "hidden") f.document.hidden = true;
    if (mode === "globe") f.context.projectionRef.current = "globe";
    f.start();
    assert.equal(f.calls.length, 0);
    assert.equal(f.orbiting(), false);
  }
  const calls = [];
  const context = { sceneOrbitCancelRef: { current() {} }, sceneOrbitContextRef: { current: "mercator/elevation-3d/imagery" }, flyoverCancelRef: { current() {} }, reducedMotion: false, undergroundOpen: false, projection: "globe", scenePreset: "globe-overview", basemap: "standard", stopSceneOrbit: () => calls.push("orbit"), stopFlyover: () => calls.push("flyover") };
  pageEffect("sceneOrbitContextRef.current !==", context)();
  assert.deepEqual(calls, ["orbit", "flyover"]);
});

test("drawing configuration updates one existing renderer and is enabled only for ready regional terrain", () => {
  for (const ready of [false, true]) for (const scene of ["overview-2d", "elevation-3d"]) for (const projection of ["mercator", "globe"]) {
    const updates = [];
    const context = {
      mapRef: { current: {} }, effectiveSceneLight: () => ({ preset: "dusk", azimuth: 265 }), atmospherePreset: "night", lightAzimuth: 210, sunClock: 1,
      styleReady: ready, styleGenerationReadyRef: { current: ready }, scenePreset: scene, projection, undergroundOpen: false,
      terrainDrawingMode: "both", terrainSurfaceMode: "off", terrainSurfaceOpacity: 0.55, measureMode: null, terrainProvider: "usgs-3dep", browserRenderBudget: () => ({ efficient: true }), renderQuality: "efficient", terrainDrawingDetail: true,
      terrainDrawingConfigRef: { current: null }, terrainDrawingRef: { current: { update: (config) => updates.push(config) } },
    };
    const update = pageEffect("const config: TerrainDrawingConfig", context);
    update(); update();
    assert.equal(updates.length, 2);
    assert.equal(updates[0].enabled, ready && scene === "elevation-3d" && projection === "mercator");
    assert.equal(updates[0].provider, "usgs-3dep");
    assert.equal(updates[0].light, "dusk");
    assert.equal(updates[0].efficient, true);
    const off = pageCallback("chooseTerrainDrawingMode", { ...context, setTerrainDrawingMode: () => {} });
    off("off");
    assert.equal(updates.at(-1).mode, "off", "Off reaches runtime synchronously before React effects");
  }
});

async function controlsModule() {
  const drawingUrl = toUrl(transpile(await read("app/terrain-drawing.ts")));
  const surfaceUrl = toUrl(transpile((await read("app/terrain-surface.ts")).replace('"./terrain-drawing"', JSON.stringify(drawingUrl))));
  const hooks = toUrl("let id = 0; export const useId = () => `terrain-${++id}`; export const useState = () => [false, () => {}]; export const useEffect = () => {}; export const useRef = () => ({current:null});");
  const scene = toUrl(`export const KANSAS_FLYOVER = ${JSON.stringify(stops)}; export const SCENE_EFFECT_OPTIONS = []; export const SCENE_LOOK_PRESETS = {plain:{label:'Plain',settings:{}}}; export const matchingLookPreset = () => null;`);
  const studio = toUrl(transpile(await read("app/scene-studio.ts")));
  const source = (await read("app/scene-effects-controls.tsx")).replace('"./terrain-surface"', JSON.stringify(surfaceUrl)).replace('"react"', JSON.stringify(hooks)).replace('"./scene-effects"', JSON.stringify(scene)).replace('"./scene-studio"', JSON.stringify(studio));
  return import(toUrl(transpile(source).replace('"react/jsx-runtime"', JSON.stringify(pathToFileURL(require.resolve("react/jsx-runtime")).href))));
}
const descendants = (node) => !node || typeof node !== "object" ? [] : [node, ...[node.props?.children].flat(Infinity).flatMap(descendants)];
const textOf = (node) => Array.isArray(node) ? node.map(textOf).join("") : typeof node === "string" || typeof node === "number" ? String(node) : node && typeof node === "object" ? textOf(node.props?.children) : "";

test("real Scene controls expose four shared drawing modes, source readings and six keyboard-ready viewpoints", async () => {
  const { SceneEffectsControls } = await controlsModule();
  const changes = [];
  const props = {
    settings: { cinematic: true, sunSync: false }, light: null, efficient: false, reducedMotion: false, flyoverActive: false, view: "terrain", presentation: { atmosphere: "dusk", azimuth: 265 }, camera: { pitch: 50, bearing: 0, fieldOfView: 36 }, cameraReady: true,
    onRecipe() {}, onLight() {}, onCamera() {}, onChange() {}, onFlyover() {},
    drawing: { mode: "both", detail: false, status: { state: "ready", message: "80% sampled coverage · centered patch", intervalMeters: 10, spacingMeters: 120, coverage: .8 }, source: { organization: "U.S. Geological Survey", title: "USGS source", resolution: "Mixed source resolutions and dates", boundary: "Unknown exact vertical datum", sourceUrl: "https://example.test/dem" }, onMode: (mode) => changes.push(["mode", mode]), onDetail: (detail) => changes.push(["detail", detail]) },
    exploration: { orbiting: false, onOrbit: () => changes.push(["orbit"]), onLandscape: (id) => changes.push(["landscape", id]) },
  };
  const nodes = descendants(SceneEffectsControls(props));
  const modes = descendants(nodes.find((node) => node.props?.["aria-label"] === "Terrain drawing mode")).filter((node) => node.type === "button");
  assert.equal(modes.length, 4);
  for (const node of modes) node.props.onClick();
  const shortcuts = descendants(nodes.find((node) => node.props?.["aria-label"] === "Kansas landscape viewpoints")).filter((node) => node.type === "button");
  assert.equal(shortcuts.length, 6);
  for (const node of shortcuts) node.props.onClick();
  nodes.find((node) => node.props?.className === "scene-orbit-action").props.onClick();
  assert.deepEqual(changes, ["off", "contours", "grid", "both"].map((mode) => ["mode", mode]).concat(stops.filter((stop) => stop.id !== "return").map((stop) => ["landscape", stop.id]), [["orbit"]]));
  const rendered = textOf(nodes[0]);
  for (const value of ["USGS 3DEP", "10 m", "120 m", "80%", "Spacing is sampling density, not source accuracy", "Unknown exact vertical datum"]) assert.ok(rendered.includes(value), value);
  const gridOnly = textOf(SceneEffectsControls({ ...props, drawing: { ...props.drawing, mode: "grid" } }));
  assert.ok(!gridOnly.includes("Contour interval"), "hidden contours do not claim a visible interval");
  for (const value of ["Sample spacing", "120 m", "Valid samples", "80%"]) assert.ok(gridOnly.includes(value), value);
  const constrained = descendants(SceneEffectsControls({ ...props, reducedMotion: true, efficient: true }));
  assert.equal(constrained.find((node) => node.props?.className === "scene-orbit-action").props.disabled, true);
  const finer = descendants(constrained.find((node) => node.props?.className === "scene-drawing-detail")).find((node) => node.type === "input");
  assert.equal(finer.props.disabled, true);
});
