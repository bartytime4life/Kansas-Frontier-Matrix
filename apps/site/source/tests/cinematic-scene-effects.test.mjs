import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const read = (path) => readFile(new URL(`../${path}`, import.meta.url), "utf8");
const toUrl = (javascript) => `data:text/javascript;base64,${Buffer.from(javascript).toString("base64")}`;
const transpile = (source) => ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;

async function loadModule(path, replacements = []) {
  let source = await read(path);
  for (const [before, after] of replacements) {
    assert.ok(source.includes(before), `${path} still imports ${before}`);
    source = source.replace(before, after);
  }
  return import(toUrl(transpile(source)));
}

// The NREL solar model lives behind npm packages; a deterministic stand-in
// keeps these tests about the scene-light mapping, not astronomy.
const solarStub = (azimuthDegrees, elevationDegrees) => toUrl(`export const solarPositionAt = () => ({ azimuthDegrees: ${azimuthDegrees}, elevationDegrees: ${elevationDegrees} });`);

async function loadSceneEffects(sun = [210, 35]) {
  const orientationUrl = toUrl(transpile(await read("app/kansas-orientation.ts")));
  const curtainUrl = toUrl(transpile(await read("app/aurora-curtain-layer.ts")));
  const reliefUrl = toUrl(transpile(await read("app/terrain-relief-style.ts")));
  return loadModule("app/scene-effects.ts", [
    ['from "./aurora-curtain-layer";', `from "${curtainUrl}";`],
    ['from "./daylight-layer";', `from "${solarStub(...sun)}";`],
    ['from "./kansas-orientation";', `from "${orientationUrl}";`],
    ['from "./terrain-relief-style";', `from "${reliefUrl}";`],
  ]);
}

test("scene-effect preferences parse defensively and default to the cinematic look", async () => {
  const effects = await loadSceneEffects();
  assert.deepEqual({ ...effects.DEFAULT_SCENE_EFFECTS }, { cinematic: true, curtain: true, sunSync: false, kansasGlow: true, relief2d: false, columns: true, buildings: true });
  assert.equal(effects.DEFAULT_SCENE_EFFECTS.relief2d, false, "defaults add no new network requests");
  assert.deepEqual({ ...effects.parseSceneEffects(null) }, { ...effects.DEFAULT_SCENE_EFFECTS });
  // A preference saved before the new effects existed keeps its choices and gains the defaults.
  assert.deepEqual({ ...effects.parseSceneEffects({ cinematic: false, curtain: "yes", sunSync: true, extra: 1 }) },
    { cinematic: false, curtain: true, sunSync: true, kansasGlow: true, relief2d: false, columns: true, buildings: true });
  assert.ok(Object.isFrozen(effects.parseSceneEffects({})));
});

test("following the sun uses the solar azimuth by day and a labelled night fill after sunset", async () => {
  const day = await loadSceneEffects([214.6, 31.2]);
  const light = day.sunSceneLight(Date.UTC(2026, 9, 9, 20), -98.4, 38.5);
  assert.equal(light.source, "sun");
  assert.equal(light.preset, "clear");
  assert.ok(Math.abs(light.azimuth - 214.6) < 1e-9);
  assert.equal(light.altitude, 31.2);

  const lowSun = await loadSceneEffects([260, 5]);
  assert.equal(lowSun.sunSceneLight(0, -98.4, 38.5).preset, "dusk");

  const night = await loadSceneEffects([300, -25]);
  const moon = night.sunSceneLight(0, -98.4, 38.5);
  assert.equal(moon.source, "moon");
  assert.equal(moon.preset, "night");
  assert.equal(moon.azimuth, 120, "night fill comes from opposite the sun");
});

test("manual light is used unless the map opted into following the sun", async () => {
  const effects = await loadSceneEffects([100, 40]);
  const map = { getCenter: () => ({ lng: -98.4, lat: 38.5 }) };
  assert.deepEqual({ ...effects.effectiveSceneLight(map, "dusk", 400) }, { preset: "dusk", azimuth: 40, altitude: effects.DEFAULT_LIGHT_ALTITUDE.dusk, source: "manual" });
  effects.registerSceneEffects(map, { cinematic: true, curtain: true, sunSync: true });
  const synced = effects.effectiveSceneLight(map, "night", 210);
  assert.equal(synced.source, "sun");
  assert.equal(synced.azimuth, 100);
});

test("cinematic relief keeps the standard method so array-free paint stays valid", async () => {
  const effects = await loadSceneEffects();
  const paint = effects.cinematicHillshadePaint("general", "dusk", -125);
  assert.equal(paint["hillshade-method"], "standard");
  assert.equal(paint["hillshade-illumination-direction"], 235);
  assert.equal(paint["hillshade-exaggeration"], 1);
  for (const preset of ["night", "dusk", "clear"]) {
    for (const value of Object.values(effects.cinematicHillshadePaint("topographic", preset, 90))) assert.ok(!Array.isArray(value));
  }
});

test("relief paint follows the effect switch and only writes changed properties", async () => {
  const effects = await loadSceneEffects();
  const paint = new Map();
  let writes = 0;
  const map = {
    getCenter: () => ({ lng: -98.4, lat: 38.5 }),
    getLayer: () => ({ type: "hillshade" }),
    getPaintProperty: (_layer, property) => paint.get(property),
    setPaintProperty: (_layer, property, value) => { writes += 1; paint.set(property, value); },
  };
  effects.registerSceneEffects(map, { cinematic: true, curtain: true, sunSync: false });
  effects.applyTerrainReliefStyle(map, "general", "dusk", 235);
  assert.equal(paint.get("hillshade-highlight-color"), "#ffcf94");
  const firstWrites = writes;
  effects.applyTerrainReliefStyle(map, "general", "dusk", 235);
  assert.equal(writes, firstWrites, "an unchanged view does not repaint tiles");
  effects.registerSceneEffects(map, { cinematic: false, curtain: true, sunSync: false });
  effects.applyTerrainReliefStyle(map, "general", "dusk", 235);
  assert.equal(paint.get("hillshade-highlight-color"), "#ecd6b5", "effects off restores the legacy palette");
  assert.equal(paint.get("hillshade-exaggeration"), 0.66);
});

test("the curtain shows in tilted and globe views and never in Battery saver", async () => {
  const effects = await loadSceneEffects();
  const on = { ...effects.DEFAULT_SCENE_EFFECTS };
  assert.equal(effects.curtainShouldShow(on, 45, false, "mercator"), true);
  assert.equal(effects.curtainShouldShow(on, effects.CURTAIN_MIN_PITCH - 1, false, "mercator"), false);
  assert.equal(effects.curtainShouldShow(on, 45, true, "mercator"), false);
  assert.equal(effects.curtainShouldShow(on, 0, false, "globe"), true, "the globe shows the wall at any tilt");
  assert.equal(effects.curtainShouldShow(on, 0, true, "globe"), false);
  assert.equal(effects.curtainShouldShow({ ...on, curtain: false }, 45, false, "mercator"), false);
  assert.equal(effects.curtainShouldShow(on, Number.NaN, false, "mercator"), false);
});

test("a curtain that cannot be created is removed without failing the style sync", async () => {
  const effects = await loadSceneEffects();
  const layers = new Map();
  const map = {
    getLayer: (id) => layers.get(id),
    getStyle: () => ({ layers: [] }),
    addLayer: (layer) => { layers.set(layer.id, layer); throw new Error("shader failed"); },
    removeLayer: (id) => layers.delete(id),
    setLayoutProperty: () => {},
  };
  effects.registerSceneEffects(map, { cinematic: true, curtain: true, sunSync: false });
  assert.equal(effects.syncBorderCurtain(map, false), false);
  assert.equal(layers.size, 0);
  effects.registerSceneEffects(map, { cinematic: true, curtain: false, sunSync: false });
  assert.equal(effects.syncBorderCurtain(map, false), true);
});

test("the curtain ring is a closed, densified display outline inside the Kansas frame", async () => {
  const orientation = await import(toUrl(transpile(await read("app/kansas-orientation.ts"))));
  const curtain = await import(toUrl(transpile(await read("app/aurora-curtain-layer.ts"))));
  const points = curtain.densifyRing(orientation.KANSAS_OUTLINE, 2.5);
  assert.ok(points.length > 500, "border is densified so wall feet can follow terrain");
  assert.equal(points[0].lng, points.at(-1).lng);
  assert.equal(points[0].lat, points.at(-1).lat);
  assert.equal(points[0].t, 0);
  assert.equal(points.at(-1).t, 1);
  for (let index = 1; index < points.length; index += 1) assert.ok(points[index].t >= points[index - 1].t, "perimeter parameter increases");
  for (const point of points) {
    assert.ok(point.lng >= -102.06 && point.lng <= -94.58);
    assert.ok(point.lat >= 36.99 && point.lat <= 40.01);
  }
  assert.equal(curtain.curtainHeightMeters(0), curtain.CURTAIN_HEIGHT_STOPS[0][1]);
  assert.ok(curtain.curtainHeightMeters(2) > curtain.curtainHeightMeters(4), "taller from orbit");
  assert.ok(curtain.curtainHeightMeters(7) < curtain.curtainHeightMeters(6));
  assert.ok(curtain.curtainHeightMeters(20) > 0);
});

test("the selection ping runs two expanding rings and then stops", async () => {
  const effects = await loadSceneEffects();
  const start = effects.selectionPulseFrame(0);
  const middle = effects.selectionPulseFrame(effects.SELECTION_PULSE_PERIOD_MS / 2);
  assert.equal(start.running, true);
  assert.ok(middle.radius > start.radius);
  assert.ok(middle.opacity < start.opacity);
  assert.deepEqual(effects.selectionPulseFrame(effects.SELECTION_PULSE_DURATION_MS), { radius: 12, opacity: 0, running: false });
  assert.equal(effects.selectionPulseFrame(Number.POSITIVE_INFINITY).running, false);
});

test("flyover stops are bounded camera targets that end back over Kansas", async () => {
  const effects = await loadSceneEffects();
  assert.ok(effects.KANSAS_FLYOVER.length >= 5);
  assert.equal(new Set(effects.KANSAS_FLYOVER.map((stop) => stop.id)).size, effects.KANSAS_FLYOVER.length);
  for (const stop of effects.KANSAS_FLYOVER) {
    const [lng, lat] = stop.center;
    assert.ok(lng >= -102.06 && lng <= -94.58 && lat >= 36.99 && lat <= 40.01, `${stop.id} looks at Kansas`);
    assert.ok(stop.pitch <= 72, `${stop.id} respects the Terrain 3D pitch limit`);
    assert.ok(stop.flightMs > 0 && stop.dwellMs >= 0);
  }
  assert.equal(effects.KANSAS_FLYOVER.at(-1).id, "return");
});

test("selection glow and ping layers are drawn with the other selection system layers", async () => {
  const runtime = await read("app/map-runtime.ts");
  for (const id of ["kfm-selection-glow", "kfm-selection-halo", "SELECTION_PULSE_LAYER_ID"]) assert.match(runtime, new RegExp(id));
  const composition = await read("app/map-layer-composition.ts");
  for (const id of ["kfm-selection-glow", "kfm-selection-halo", "kfm-selection-pulse"]) assert.match(composition, new RegExp(`"${id}"`));
});

test("globe backdrop, vignette and effect styles load after the theme", async () => {
  const layout = await read("app/layout.tsx");
  assert.ok(layout.indexOf('import "./scene-effects.css";') > layout.indexOf('import "./explorer-theme.css";'));
  const css = await read("app/scene-effects.css");
  assert.match(css, /\.map-canvas\[data-projection="globe"\]/);
  assert.match(css, /prefers-reduced-motion/);
  const page = await read("app/page.tsx");
  assert.match(page, /data-projection=\{projection\}/);
  assert.match(page, /registerSceneEffects\(map, sceneEffectsRef\.current\)/);
});

test("look presets are complete and recognised; Plain turns every effect off", async () => {
  const effects = await loadSceneEffects();
  for (const [id, preset] of Object.entries(effects.SCENE_LOOK_PRESETS)) {
    assert.deepEqual(Object.keys(preset.settings).sort(), [...effects.SCENE_EFFECT_KEYS].sort(), `${id} sets every effect`);
    assert.equal(effects.matchingLookPreset(preset.settings), id);
  }
  assert.ok(effects.SCENE_EFFECT_KEYS.every((key) => effects.SCENE_LOOK_PRESETS.plain.settings[key] === false));
  assert.equal(effects.matchingLookPreset({ ...effects.SCENE_LOOK_PRESETS.plain.settings, columns: true }), null, "a mixed choice is Custom");
  assert.deepEqual(effects.SCENE_EFFECT_OPTIONS.map((option) => option.key).sort(), [...effects.SCENE_EFFECT_KEYS].sort(), "every effect has a GUI row");
  assert.deepEqual(effects.SCENE_EFFECT_OPTIONS.filter((option) => option.network).map((option) => option.key), ["relief2d"], "only 2D relief is labelled as making requests");
});

test("the curtain has a globe shader path that uses MapLibre's projection prelude", async () => {
  const layer = await read("app/aurora-curtain-layer.ts");
  assert.match(layer, /projectTileWithElevation\(a_pos/);
  assert.match(layer, /variantName === "globe"/);
  for (const uniform of ["u_projection_matrix", "u_projection_fallback_matrix", "u_projection_tile_mercator_coords", "u_projection_clipping_plane", "u_projection_transition"]) assert.match(layer, new RegExp(uniform));
});

test("a globe shader that fails to compile disables only the globe curtain, once", async () => {
  const curtain = await import(toUrl(transpile(await read("app/aurora-curtain-layer.ts"))));
  let compileAttempts = 0, globeCompiles = 0, draws = 0;
  const gl = new Proxy({}, {
    get(_target, name) {
      if (name === "VERTEX_SHADER") return 1;
      if (name === "FRAGMENT_SHADER") return 2;
      if (name === "getShaderParameter") return () => { compileAttempts += 1; return !(globeCompiles > 0 && compileAttempts > 2); };
      if (name === "shaderSource") return (_shader, source) => { if (source.includes("projectTileWithElevation")) globeCompiles += 1; };
      if (name === "getProgramParameter") return () => true;
      if (name === "getAttribLocation") return () => 0;
      if (name === "drawArrays") return () => { draws += 1; };
      return () => ({});
    },
  });
  const map = { on() {}, off() {}, getTerrain: () => null, getZoom: () => 3, getBounds: () => ({ getWest: () => -110, getEast: () => -90, getSouth: () => 30, getNorth: () => 45 }) };
  const layer = curtain.createAuroraCurtainLayer({ id: "test", ring: [[-100, 37], [-95, 37], [-95, 40], [-100, 37]], clock: () => null });
  layer.onAdd(map, gl);
  const globeFrame = { shaderData: { variantName: "globe", vertexShaderPrelude: "", define: "" }, defaultProjectionData: { mainMatrix: [], fallbackMatrix: [], tileMercatorCoords: [0, 0, 1, 1], clippingPlane: [0, 0, 0, 0], projectionTransition: 1 } };
  assert.doesNotThrow(() => layer.render(gl, globeFrame));
  assert.doesNotThrow(() => layer.render(gl, globeFrame));
  assert.equal(globeCompiles, 1, "a failed globe shader is not recompiled every frame");
  assert.equal(draws, 0);
  layer.render(gl, { shaderData: { variantName: "mercator" }, modelViewProjectionMatrix: [] });
  assert.equal(draws, 1, "the flat-map curtain still draws");
});
