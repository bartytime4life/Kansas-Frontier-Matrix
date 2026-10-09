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
const pageTree = ts.createSourceFile("page.tsx", await read("app/page.tsx"), ts.ScriptTarget.Latest, true, ts.ScriptKind.TSX);
const controlsTree = ts.createSourceFile("controls.tsx", await read("app/scene-effects-controls.tsx"), ts.ScriptTarget.Latest, true, ts.ScriptKind.TSX);
const home = pageTree.statements.find((node) => ts.isFunctionDeclaration(node) && node.name?.text === "Home");
const descendants = (node) => !node || typeof node !== "object" ? [] : [node, ...[node.props?.children].flat(Infinity).flatMap(descendants)];
const textOf = (node) => Array.isArray(node) ? node.map(textOf).join("") : typeof node === "string" || typeof node === "number" ? String(node) : node && typeof node === "object" ? textOf(node.props?.children) : "";
function nodesMatching(root, predicate) {
  const matches = [];
  function visit(node) { if (predicate(node)) matches.push(node); ts.forEachChild(node, visit); }
  visit(root);
  return matches;
}
function evaluate(node, context, tree = pageTree) {
  return new Function(...Object.keys(context), `${transpile(`const result = ${node.getText(tree)};`)} return result;`)(...Object.values(context));
}
const homeDeclaration = (name) => nodesMatching(home.body, (node) => ts.isVariableDeclaration(node) && node.name.getText(pageTree) === name)[0];
const callback = (name, context) => evaluate(homeDeclaration(name).initializer, context);
const configurationEffect = nodesMatching(home.body, (node) => ts.isCallExpression(node) && node.expression.getText(pageTree) === "useEffect" && node.arguments[0].getText(pageTree).includes("const config: TerrainDrawingConfig"))[0];

test("actual surface callbacks preserve independent line choices and cached reading when reselecting the same lens", () => {
  const initial = evaluate(homeDeclaration("terrainDrawingConfigRef").initializer, { useRef: (current) => ({ current }) }).current;
  assert.equal(initial.mode, "off");
  assert.equal(initial.surface, "off");
  assert.equal(initial.surfaceOpacity, .55);
  const sample = { slopeDegrees: 4.65, aspectDegrees: 125, elevationMeters: 251.6, center: [-98, 38], spacingMeters: 80 };
  let reading = sample, cached = sample, centerCalls = 0;
  const configs = [], modes = [], opacities = [];
  const context = {
    terrainDrawingConfigRef: { current: { ...initial, mode: "contours", surface: "slope", enabled: true, provider: "usgs-3dep", light: "dusk", azimuth: 265 } },
    terrainDrawingRef: { current: null }, measureModeRef: { current: null }, clamp: (value, min, max) => Math.max(min, Math.min(max, value)),
    setTerrainSurfaceProbe: (value) => { reading = value; }, setTerrainSurfaceMode: (value) => modes.push(value), setTerrainSurfaceOpacity: (value) => opacities.push(value), setTerrainDrawingMode() {},
  };
  let runtimeConfig = context.terrainDrawingConfigRef.current;
  context.terrainDrawingRef.current = {
    update(config) {
      // The renderer deduplicates a retained cell, and owns invalidation on lens changes.
      if (config.surface !== runtimeConfig.surface) { cached = null; context.setTerrainSurfaceProbe(null); }
      runtimeConfig = config; configs.push(config);
    },
    probeCenter() { centerCalls += 1; if (!cached) { cached = sample; context.setTerrainSurfaceProbe(sample); } },
  };
  const choose = callback("chooseTerrainSurfaceMode", context), center = callback("sampleTerrainSurfaceCenter", context);
  choose("slope"); center();
  assert.equal(reading, sample, "same-lens button does not erase a deduplicated cached reading");
  choose("aspect");
  assert.equal(reading, null);
  center();
  assert.equal(reading, sample, "view-center sample is available immediately after changing lenses");
  callback("chooseTerrainDrawingMode", context)("off");
  assert.equal(configs.at(-1).surface, "aspect", "surface remains on with lines off");
  const opacity = callback("chooseTerrainSurfaceOpacity", context);
  for (const value of [-1, .4, 3, NaN]) opacity(value);
  assert.deepEqual(opacities, [.2, .4, .75, .55]);
  for (const config of configs) {
    assert.equal(config.provider, "usgs-3dep"); assert.equal(config.light, "dusk"); assert.equal(config.azimuth, 265); assert.equal(config.enabled, true);
  }
  context.measureModeRef.current = "distance";
  center();
  assert.equal(centerCalls, 2, "measurement never invokes probing");
  choose("off");
  assert.equal(reading, null);
  assert.deepEqual(modes, ["slope", "aspect", "off"]);
});

test("shared renderer config includes surface-only mode and suspends probes without enabling terrain", () => {
  for (const scene of ["overview-2d", "elevation-3d"]) for (const measureMode of [null, "distance"]) {
    const configs = [], readings = [];
    const context = {
      mapRef: { current: {} }, effectiveSceneLight: () => ({ preset: "dusk", azimuth: 265 }), atmospherePreset: "dusk", lightAzimuth: 265, sunClock: 1,
      styleReady: true, styleGenerationReadyRef: { current: true }, scenePreset: scene, projection: "mercator", undergroundOpen: false,
      terrainDrawingMode: "off", terrainSurfaceMode: "slope", terrainSurfaceOpacity: .4, measureMode, terrainProvider: "usgs-3dep", browserRenderBudget: () => ({ efficient: true }), renderQuality: "efficient", terrainDrawingDetail: false,
      terrainDrawingConfigRef: { current: null }, terrainDrawingRef: { current: { update: (value) => configs.push(value) } }, setTerrainSurfaceProbe: (value) => readings.push(value),
    };
    evaluate(configurationEffect.arguments[0], context)();
    assert.equal(configs.length, 1);
    assert.equal(configs[0].enabled, scene === "elevation-3d");
    assert.equal(configs[0].mode, "off"); assert.equal(configs[0].surface, "slope"); assert.equal(configs[0].surfaceOpacity, .4);
    assert.equal(configs[0].probeEnabled, !measureMode);
    assert.deepEqual(readings, measureMode ? [null] : []);
  }
});

test("renderer probe callback ignores disposed/replaced maps and never leaks a reading into measurement", () => {
  const create = nodesMatching(pageTree, (node) => ts.isCallExpression(node) && node.expression.getText(pageTree) === "createTerrainDrawing")[0];
  const map = {}, sample = { slopeDegrees: 8, aspectDegrees: 90, elevationMeters: 450, center: [-98, 38], spacingMeters: 80 };
  for (const disposed of [false, true]) for (const same of [false, true]) for (const measure of [null, "distance"]) {
    const readings = [];
    evaluate(create.arguments[2], { disposed, map, mapRef: { current: same ? map : {} }, measureModeRef: { current: measure }, setTerrainSurfaceProbe: (probe) => readings.push(probe) })(sample);
    assert.deepEqual(readings, !disposed && same ? [measure ? null : sample] : []);
  }
});

test("both real generic hover/click fallbacks exclude scene display sources while retaining evidence and basemap picks", () => {
  const candidates = nodesMatching(pageTree, (node) => ts.isVariableDeclaration(node) && node.name.getText(pageTree) === "externalCandidate" && node.initializer?.getText(pageTree).includes("queryRenderedFeatures"));
  assert.equal(candidates.length, 2);
  const feature = (source) => ({ source, properties: { name: source }, geometry: { type: "Point", coordinates: [-98, 38] } });
  const basemap = feature("openmaptiles"), official = feature("external-usgs-streamflow");
  for (const candidateNode of candidates) {
    let features = [feature("scene-terrain-drawing"), feature("scene-kansas-glow"), feature("kfm-focus"), feature("registered-evidence"), basemap];
    let queries = 0;
    const context = { candidate: undefined, officialCandidate: undefined, map: { queryRenderedFeatures() { queries += 1; return features; } }, event: { point: [1, 2] }, LAYER_REGISTRY: [{ sourceId: "registered-evidence" }] };
    assert.equal(evaluate(candidateNode.initializer, context), basemap);
    features = features.slice(0, -1);
    assert.equal(evaluate(candidateNode.initializer, context), undefined, "display-only hits produce no generic selection or report");
    const before = queries;
    assert.equal(evaluate(candidateNode.initializer, { ...context, officialCandidate: official }), official);
    assert.equal(queries, before, "official evidence retains the higher-priority path");
  }
});

test("real map click completes the existing measurement path before any feature/probe selection", () => {
  const click = nodesMatching(pageTree, (node) => ts.isCallExpression(node) && node.expression.getText(pageTree) === "map.on" && node.arguments[0]?.getText(pageTree) === '"click"' && node.arguments[1]?.getText(pageTree).includes("measureCoordinatesRef.current"))[0];
  const updates = [], counts = [], labels = [];
  const context = { undergroundOpenRef: { current: false }, measureModeRef: { current: "distance" }, measureCoordinatesRef: { current: [[-98, 38]] }, measureUnitRef: { current: "metric" }, setMeasureCoordinateCount: (value) => counts.push(value), updateMeasurementSource: (_map, data) => updates.push(data), buildMeasurementData: (coordinates, mode) => ({ coordinates, mode }), setMeasurement: (label) => labels.push(label), measurementLabelFor: (mode, points) => `${mode}:${points.length}`, map: { queryRenderedFeatures() { throw new Error("measurement must not enter feature picking"); } } };
  evaluate(click.arguments[1], context)({ lngLat: { lng: -97, lat: 39 }, point: [5, 6] });
  assert.deepEqual(updates, [{ coordinates: [[-98, 38], [-97, 39]], mode: "distance" }]);
  assert.deepEqual(counts, [2]); assert.deepEqual(labels, ["distance:2"]);
});

const drawingUrl = toUrl(transpile(await read("app/terrain-drawing.ts")));
const surfaceUrl = toUrl(transpile((await read("app/terrain-surface.ts")).replace('"./terrain-drawing"', JSON.stringify(drawingUrl))));
const surfaceModel = await import(surfaceUrl);
const hooks = toUrl("let id=0; export const useId=()=>`surface-${++id}`; export const useState=()=>[false,()=>{}]; export const useEffect=()=>{}; export const useRef=()=>({current:null});");
const scene = toUrl("export const KANSAS_FLYOVER=[]; export const SCENE_EFFECT_OPTIONS=[]; export const SCENE_LOOK_PRESETS={plain:{label:'Plain',settings:{}}}; export const matchingLookPreset=()=>null;");
const studio = toUrl(transpile(await read("app/scene-studio.ts")));
const controlsSource = (await read("app/scene-effects-controls.tsx")).replace('"./terrain-surface"', JSON.stringify(surfaceUrl)).replace('"react"', JSON.stringify(hooks)).replace('"./scene-effects"', JSON.stringify(scene)).replace('"./scene-studio"', JSON.stringify(studio));
const { SceneEffectsControls } = await import(toUrl(transpile(controlsSource).replace('"react/jsx-runtime"', JSON.stringify(pathToFileURL(require.resolve("react/jsx-runtime")).href))));
function props() {
  return {
    settings: { cinematic: true, sunSync: false }, light: null, efficient: false, reducedMotion: false, flyoverActive: false, view: "terrain", presentation: { atmosphere: "dusk", azimuth: 265 }, camera: { pitch: 50, bearing: 0, fieldOfView: 36 }, cameraReady: true,
    onRecipe() {}, onLight() {}, onCamera() {}, onChange() {}, onFlyover() {},
    drawing: { mode: "off", detail: false, status: { state: "ready", message: "90% sampled coverage", intervalMeters: 10, spacingMeters: 120, coverage: .9, validCellCount: 4, totalCellCount: 10 }, source: { organization: "U.S. Geological Survey", title: "USGS source", resolution: "Mixed dates", boundary: "Unknown exact vertical datum", sourceUrl: "https://example.test/dem" }, onMode() {}, onDetail() {} },
    surface: { mode: "slope", opacity: .55, probe: { slopeDegrees: 7.36, aspectDegrees: 132, elevationMeters: 412.7, center: [-98, 38], spacingMeters: 120 }, probeEnabled: true, onMode() {}, onOpacity() {}, onProbeCenter() {} },
  };
}

test("surface-only controls expose independent callbacks, fixed model legends and valid-cell coverage", () => {
  const input = props(), changes = [];
  input.surface.onMode = (value) => changes.push(["mode", value]); input.surface.onOpacity = (value) => changes.push(["opacity", value]); input.surface.onProbeCenter = () => changes.push(["center"]);
  const tree = SceneEffectsControls(input), nodes = descendants(tree), text = textOf(tree);
  for (const expected of ["90%", "40% · 4 / 10", "7.4°", "SE", "413 m", "USGS source"]) assert.ok(text.includes(expected), expected);
  assert.ok(!text.includes("Contour interval"));
  const buttons = descendants(nodes.find((node) => node.props?.["aria-label"] === "Surface color")).filter((node) => node.type === "button");
  assert.equal(buttons.length, 3);
  for (const button of buttons) button.props.onClick();
  const strength = nodes.find((node) => node.type === "input" && node.props.id?.endsWith("surface-opacity"));
  strength.props.onChange({ target: { value: "38" } });
  nodes.find((node) => node.type === "button" && textOf(node) === "Sample view center").props.onClick();
  assert.deepEqual(changes, [["mode", "off"], ["mode", "slope"], ["mode", "aspect"], ["opacity", .38], ["center"]]);
  for (const mode of ["slope", "aspect"]) for (const atmosphere of ["dusk", "night", "clear"]) {
    const rendered = descendants(SceneEffectsControls({ ...input, presentation: { atmosphere, azimuth: 60 }, surface: { ...input.surface, mode } }));
    const legend = rendered.find((node) => node.props?.["aria-label"] === (mode === "slope" ? "Slope color legend" : "Facing direction color legend"));
    const entries = descendants(legend).filter((node) => node.type === "li").map((node) => ({ label: textOf(node), color: descendants(node).find((child) => child.type === "i").props.style.backgroundColor }));
    assert.deepEqual(entries, (mode === "slope" ? surfaceModel.TERRAIN_SLOPE_LEGEND : surfaceModel.TERRAIN_ASPECT_LEGEND).map(({ label, color }) => ({ label, color })));
  }
});

test("sample states distinguish flat cells, measurement, unavailable terrain and all Off", () => {
  const input = props();
  const flat = SceneEffectsControls({ ...input, surface: { ...input.surface, probe: { ...input.surface.probe, aspectDegrees: null } } });
  assert.ok(textOf(flat).includes("Flat / no direction"));
  const measuring = SceneEffectsControls({ ...input, surface: { ...input.surface, probeEnabled: false } });
  assert.ok(textOf(measuring).includes("paused while a measurement tool is active"));
  assert.ok(!textOf(measuring).includes("413 m"));
  assert.equal(descendants(measuring).find((node) => node.type === "button" && textOf(node) === "Sample view center").props.disabled, true);
  const unavailable = SceneEffectsControls({ ...input, drawing: { ...input.drawing, status: { state: "unavailable", message: "Choose Terrain 3D", intervalMeters: null, spacingMeters: null, coverage: 0 } }, surface: { ...input.surface, probe: null } });
  assert.ok(textOf(unavailable).includes("Choose Terrain 3D"));
  assert.equal(descendants(unavailable).find((node) => node.type === "button" && textOf(node) === "Sample view center").props.disabled, true);
  const off = textOf(SceneEffectsControls({ ...input, surface: { ...input.surface, mode: "off" } }));
  assert.ok(!off.includes("Surface sample")); assert.ok(!off.includes("Valid samples"));
});

test("map taps keep the active surface reading open without consuming events; outside/Escape still close and clean up", () => {
  const panel = controlsTree.statements.find((node) => ts.isFunctionDeclaration(node) && node.name?.text === "ScenePanel");
  const effect = nodesMatching(panel, (node) => ts.isCallExpression(node) && node.expression.getText(controlsTree) === "useEffect" && node.arguments[0]?.getText(controlsTree).includes("document.addEventListener"))[0];
  class Element { constructor(canvas = false) { this.canvas = canvas; } matches(selector) { assert.equal(selector, "canvas.maplibregl-canvas"); return this.canvas; } }
  for (const mode of ["off", "slope", "aspect"]) for (const probeEnabled of [false, true]) {
    const listeners = new Map(), closed = [], focus = [], inside = new Element(), map = new Element(true);
    const target = { addEventListener(type, fn) { listeners.set(type, fn); }, removeEventListener(type, fn) { assert.equal(listeners.get(type), fn); listeners.delete(type); } };
    const cleanup = evaluate(effect.arguments[0], { open: true, root: { current: { ...target, contains: (value) => value === inside } }, trigger: { current: { focus: () => focus.push(true) } }, setOpen: (value) => closed.push(value), document: target, Element, props: { surface: { mode, probeEnabled } } }, controlsTree)();
    const event = (target) => ({ target, stopPropagation() { throw new Error("outside handler must not consume map/evidence events"); }, preventDefault() { throw new Error("outside handler must not block map input"); } });
    listeners.get("pointerdown")(event(inside)); assert.equal(closed.length, 0);
    listeners.get("pointerdown")(event(map));
    assert.equal(closed.length, mode !== "off" && probeEnabled ? 0 : 1);
    listeners.get("pointerdown")(event(new Element())); assert.equal(closed.at(-1), false);
    listeners.get("keydown")({ key: "Escape", stopPropagation() {} }); assert.deepEqual(focus, [true]);
    cleanup(); assert.equal(listeners.size, 0);
  }
});

test("Scene and evidence share a stacking context so the open sample can paint above the drawer", async () => {
  const attribute = (node, name) => node.attributes.properties.find((item) => ts.isJsxAttribute(item) && item.name.getText(pageTree) === name)?.initializer;
  const closestElement = (node) => { let parent = node.parent; while (parent && !ts.isJsxElement(parent)) parent = parent.parent; return parent; };
  const scene = nodesMatching(pageTree, (node) => ts.isJsxSelfClosingElement(node) && node.tagName.getText(pageTree) === "ScenePanel")[0];
  const drawer = nodesMatching(pageTree, (node) => ts.isJsxOpeningElement(node) && attribute(node, "className")?.text === "evidence-drawer")[0];
  const shell = closestElement(scene);
  assert.equal(attribute(shell.openingElement, "className").text, "explorer-shell", "Scene must escape the map-stage stacking context");
  assert.equal(closestElement(drawer.parent), shell, "both floating surfaces have the same stacking parent");
  assert.equal(attribute(scene, "onOpenChange").expression.getText(pageTree), "setScenePanelOpen");
  const sceneCss = await read("app/scene-effects.css"), globalCss = await read("app/globals.css");
  const sceneZ = Number(sceneCss.match(/\.scene-panel\[data-open\]\s*\{[^}]*z-index:\s*(\d+)/)[1]);
  // The final shared drawer rule overrides the earlier responsive declarations.
  const drawerZ = Number([...globalCss.matchAll(/\.layer-panel,\s*\.evidence-drawer\s*\{[^}]*z-index:\s*(\d+)/g)].at(-1)[1]);
  assert.ok(sceneZ > drawerZ, "sample controls stay reachable after a legitimate evidence selection");
  for (const surfaceInspectionOpen of [false, true]) {
    const modal = evaluate(attribute(drawer, "aria-modal").expression, { isCompact: true, rightOpen: true, surfaceInspectionOpen });
    assert.equal(modal, surfaceInspectionOpen ? undefined : true, "covered evidence does not claim modal ownership over the visible sample");
  }
});

test("compact evidence autofocus waits for active surface inspection and preserves Escape focus return", () => {
  const effect = nodesMatching(home.body, (node) => ts.isCallExpression(node) && node.expression.getText(pageTree) === "useEffect" && node.arguments[0]?.getText(pageTree).includes("const returningToScene"))[0];
  class Element { constructor(scene) { this.scene = scene; } closest(selector) { assert.equal(selector, ".scene-panel"); return this.scene ? this : null; } }
  for (const active of [false, true]) for (const surface of ["off", "slope"]) {
    const focus = [], closed = [], listeners = new Map();
    const first = { focus() { focus.push("first"); } }, last = { focus() { focus.push("last"); } };
    const drawer = { addEventListener(type, fn) { listeners.set(type, fn); }, removeEventListener(type, fn) { assert.equal(listeners.get(type), fn); listeners.delete(type); } };
    const context = { isCompact: true, surfaceInspectionOpen: active && surface !== "off", terrainSurfaceMode: surface, mapUtilityOpen: false, rightOpen: true, leftOpen: false, timelineOpen: false, rightPanelRef: { current: drawer }, visibleFocusableElements: () => [first, last], document: { activeElement: new Element(true) }, Element, closeRightPanel() { closed.push(true); } };
    const cleanup = evaluate(effect.arguments[0], context)();
    if (context.surfaceInspectionOpen) {
      assert.equal(listeners.size, 0); assert.deepEqual(focus, [], "tapped evidence does not steal focus behind Scene");
    } else {
      assert.deepEqual(focus, surface === "off" ? ["first"] : [], "surface Escape return stays on Scene trigger; ordinary drawer retains autofocus");
      context.document.activeElement = last;
      let prevented = false;
      listeners.get("keydown")({ key: "Tab", shiftKey: false, preventDefault() { prevented = true; } });
      assert.equal(prevented, true); assert.equal(focus.at(-1), "first", "drawer tab wrapping resumes after Scene closes");
      listeners.get("keydown")({ key: "Escape" }); assert.deepEqual(closed, [true]);
      cleanup(); assert.equal(listeners.size, 0);
    }
  }
  const panel = controlsTree.statements.find((node) => ts.isFunctionDeclaration(node) && node.name?.text === "ScenePanel");
  const reporting = nodesMatching(panel, (node) => ts.isCallExpression(node) && node.expression.getText(controlsTree) === "useEffect" && node.arguments[0]?.getText(controlsTree).includes("onOpenChange?."))[0];
  const opens = [];
  for (const open of [false, true, false]) evaluate(reporting.arguments[0], { open, onOpenChange: (value) => opens.push(value) }, controlsTree)();
  assert.deepEqual(opens, [false, true, false]);
});

test("both real drawer resize callbacks preserve the first tap at unchanged size and invalidate it on actual resizing", async () => {
  const { resizeMapAfterLayout } = await import(toUrl(transpile(await read("app/cutaway-locator.ts"))));
  const effect = nodesMatching(home.body, (node) => ts.isCallExpression(node) && node.expression.getText(pageTree) === "useEffect" && node.arguments[0]?.getText(pageTree).includes("resizeMapAfterLayout"))[0];
  const runtimeTree = ts.createSourceFile("runtime.ts", await read("app/terrain-drawing-runtime.ts"), ts.ScriptTarget.Latest, true);
  const movement = nodesMatching(runtimeTree, (node) => ts.isVariableDeclaration(node) && node.name.getText(runtimeTree) === "onMoveStart")[0];
  function fixture(config) {
    const tasks = new Map(), sample = { slopeDegrees: .6, aspectDegrees: 0, elevationMeters: 613 }, container = { clientWidth: 1440, clientHeight: 856, closest: () => null }, canvas = { style: { width: "1440px", height: "856px" } };
    let reading = sample, resizes = 0;
    const move = evaluate(movement.initializer, { moving: false, cancel() {}, clearProbe() { reading = null; }, active: () => true, cache: {}, waiting() {} }, runtimeTree);
    const map = { getContainer: () => container, getCanvas: () => canvas, resize() { resizes += 1; move(); canvas.style.width = `${container.clientWidth}px`; canvas.style.height = `${container.clientHeight}px`; } };
    const context = { mapRef: { current: map }, terrainDrawingConfigRef: { current: config }, resizeMapAfterLayout, runMapMutation: (_label, callback) => callback(), window: {
      requestAnimationFrame(callback) { tasks.set("raf", callback); return "raf"; }, setTimeout(callback, delay) { assert.equal(delay, 260); tasks.set("delayed", callback); return "delayed"; }, cancelAnimationFrame: (id) => tasks.delete(id), clearTimeout: (id) => tasks.delete(id),
    } };
    const cleanup = evaluate(effect.arguments[0], context)();
    return { context, tasks, sample, container, move, cleanup, reading: () => reading, resizes: () => resizes };
  }
  for (const surface of ["slope", "aspect", "off", undefined]) for (const enabled of [false, true]) {
    const f = fixture({ enabled, surface });
    for (const phase of ["raf", "delayed"]) f.tasks.get(phase)();
    const protectedSurface = enabled && (surface === "slope" || surface === "aspect");
    assert.equal(f.resizes(), protectedSurface ? 0 : 2, `enabled=${enabled}, surface=${surface}`);
    assert.equal(f.reading(), protectedSurface ? f.sample : null, "both drawer-settling callbacks leave a valid first-tap reading alone");
    f.move(); assert.equal(f.reading(), null, "real movement retains renderer invalidation");
    f.cleanup(); assert.equal(f.tasks.size, 0);
  }
  for (const changedPhase of ["raf", "delayed"]) {
    const f = fixture({ enabled: true, surface: "slope" });
    for (const phase of ["raf", "delayed"]) {
      if (phase === changedPhase) f.container.clientHeight = 700;
      f.tasks.get(phase)();
    }
    assert.equal(f.resizes(), 1); assert.equal(f.reading(), null, `${changedPhase} must honor actual dimension changes`);
    f.cleanup();
  }
  const switched = fixture({ enabled: true, surface: "slope" });
  switched.tasks.get("raf")();
  switched.context.terrainDrawingConfigRef.current = { enabled: true, surface: "off" };
  switched.tasks.get("delayed")();
  assert.equal(switched.resizes(), 1, "deferred callbacks read the current lens choice, not stale render state");
  switched.cleanup();
});
