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
const studioSource = await read("app/scene-studio.ts");
const studioUrl = toUrl(transpile(studioSource));
const studio = await import(studioUrl);
const curtainUrl = toUrl(transpile(await read("app/aurora-curtain-layer.ts")));
const curtain = await import(curtainUrl);
const solarUrl = toUrl(`export const solarPositionAt = () => ({ azimuthDegrees: 310, elevationDegrees: -20 });`);
const effectsUrl = toUrl(transpile((await read("app/scene-effects.ts"))
  .replace('"./aurora-curtain-layer"', JSON.stringify(curtainUrl))
  .replace('"./daylight-layer"', JSON.stringify(solarUrl))
  .replace('"./kansas-orientation"', JSON.stringify(toUrl(transpile(await read("app/kansas-orientation.ts")))))
  .replace('"./terrain-relief-style"', JSON.stringify(toUrl(transpile(await read("app/terrain-relief-style.ts")))))));
const effects = await import(effectsUrl);

test("recipes coordinate presentation without enabling DEMs, camera changes or provider layers", () => {
  for (const relief2d of [false, true]) {
    const input = { ...effects.DEFAULT_SCENE_EFFECTS, relief2d, columns: false, buildings: false, curtain: false, sunSync: true };
    for (const id of Object.keys(studio.SCENE_RECIPES)) {
      const before = structuredClone(input);
      const next = studio.sceneRecipePresentation(id, input);
      assert.deepEqual(input, before, "no in-place mutations");
      assert.equal(next.settings.relief2d, relief2d, "no additional DEM choice");
      for (const key of ["columns", "buildings", "curtain"]) assert.equal(next.settings[key], false, "opted-out effects remain off");
      assert.deepEqual(Object.keys(next).sort(), ["atmosphere", "azimuth", "settings"], "only existing presentation state changes");
      assert.equal(studio.matchingSceneRecipe(next), id);
      assert.equal(studio.matchingSceneRecipe({ ...next, azimuth: next.azimuth + 1 }), null, "manual light changes produce Custom");
      assert.equal(studio.matchingSceneRecipe({ ...next, settings: { ...next.settings, sunSync: true } }), null, "sun overrides cannot claim a recipe");
      assert.equal(studio.matchingSceneRecipe({ ...next, settings: { ...next.settings, cinematic: !next.settings.cinematic } }), null);
    }
  }
});

function cameraMap() {
  const state = { pitch: 35, bearing: -15, fieldOfView: 36, center: [-98, 38], zoom: 8 };
  const calls = [];
  return { state, calls,
    getPitch: () => state.pitch, getBearing: () => state.bearing,
    getVerticalFieldOfView: () => state.fieldOfView, getMaxPitch: () => 60,
    stop: () => calls.push(["stop"]),
    setVerticalFieldOfView: (value) => { calls.push(["fov", value]); state.fieldOfView = value; },
    easeTo: (value) => { calls.push(["camera", value]); state.pitch = value.pitch; state.bearing = value.bearing; },
  };
}

test("camera callbacks interrupt automation before bounded pose/lens changes and preserve location/zoom", () => {
  const map = cameraMap();
  const options = { view: "tilted", reducedMotion: false, interrupt: () => map.calls.push(["interrupt"]) };
  const changed = studio.applySceneComposition(map, { pitch: 100, bearing: 405, fieldOfView: 90 }, options);
  assert.equal(map.calls[0][0], "interrupt");
  assert.deepEqual(changed, { pitch: 60, bearing: 45, fieldOfView: 60 });
  assert.deepEqual(map.state.center, [-98, 38]);
  assert.equal(map.state.zoom, 8);
  assert.deepEqual(map.calls.at(-1), ["camera", { pitch: 60, bearing: 45, duration: 0, essential: false }]);
  map.calls.length = 0;
  studio.applySceneComposition(map, { fieldOfView: 20 }, options);
  assert.equal(map.calls.some(([kind]) => kind === "camera"), false, "lens does not rewrite pose");
  assert.equal(map.state.pitch, 60);
  assert.equal(map.state.bearing, 45);
  for (const reducedMotion of [false, true]) {
    studio.applySceneComposition(map, studio.compositionDefaults("tilted"), { ...options, reducedMotion, reset: true });
    assert.equal(map.calls.at(-1)[1].duration, reducedMotion ? 0 : 300);
    assert.deepEqual(map.state, { center: [-98, 38], zoom: 8, ...studio.compositionDefaults("tilted") });
  }
});

test("camera controls tolerate invalid values, retain real restored values and keep globe tilt level", () => {
  const map = cameraMap();
  const options = { view: "terrain", reducedMotion: true, interrupt() {} };
  assert.deepEqual(studio.applySceneComposition(map, { pitch: NaN, fieldOfView: Infinity }, options), { pitch: 35, bearing: -15, fieldOfView: 36 });
  map.state.pitch = 22; map.state.bearing = 280; map.state.fieldOfView = 48;
  assert.deepEqual(studio.readSceneComposition(map), { pitch: 22, bearing: -80, fieldOfView: 48 }, "reads actual drag or snapshot state");
  studio.applySceneComposition(map, { pitch: 50 }, { ...options, view: "globe" });
  assert.equal(map.state.pitch, 0);
});

// Execute the actual renderer environment callback, with real scene-effect
// helpers, without importing unrelated source/network modules from map-runtime.
async function environmentCallback() {
  const source = await read("app/map-runtime.ts");
  const tree = ts.createSourceFile("runtime.ts", source, ts.ScriptTarget.Latest, true);
  const statement = (name) => tree.statements.find((node) => ts.isVariableStatement(node) && node.declarationList.declarations.some((decl) => decl.name.getText(tree) === name)).getText(tree).replace(/^export /, "");
  const code = transpile(`${statement("SCENE_SKIES")}\n${statement("applySceneEnvironment")}`);
  return new Function("effects", `const { effectiveSceneLight, registerCurtainLight, sceneEffectsFor, CINEMATIC_SKIES, GLOBE_ATMOSPHERE_BLEND, CINEMATIC_LIGHT_COLOR, CINEMATIC_LIGHT_INTENSITY } = effects; ${code}; return applySceneEnvironment;`)(effects);
}

function curtainHarness() {
  const counts = { buffers: 0, programs: 0, vaos: 0, uploads: 0, paints: 0, draws: 0, frames: 0 };
  const uniforms = {};
  const gl = new Proxy({}, { get(_target, name) {
    if (name === "createBuffer") return () => { counts.buffers++; return {}; };
    if (name === "createProgram") return () => { counts.programs++; return {}; };
    if (name === "createVertexArray") return () => { counts.vaos++; return {}; };
    if (name === "bufferData" || name === "bufferSubData") return () => { counts.uploads++; };
    if (name === "getUniformLocation") return (_program, uniform) => uniform;
    if (name === "uniform3fv") return (uniform, value) => { uniforms[uniform] = [...value]; };
    if (name === "uniform1f") return (uniform, value) => { uniforms[uniform] = value; };
    if (name === "getShaderParameter" || name === "getProgramParameter") return () => true;
    if (name === "getAttribLocation") return () => 0;
    if (name === "drawArrays") return () => { counts.draws++; };
    return () => ({});
  } });
  let layer;
  let visibility;
  const map = {
    on() {}, off() {}, getTerrain: () => null, getZoom: () => 6, getCenter: () => ({ lng: -98, lat: 38 }),
    getPitch: () => 55, getProjection: () => ({ type: "mercator" }), getStyle: () => ({ layers: [] }),
    getBounds: () => ({ getWest: () => -103, getEast: () => -94, getSouth: () => 36, getNorth: () => 41 }),
    setSky() {}, setLight() {}, triggerRepaint: () => { counts.paints++; },
    getLayer: () => layer,
    addLayer: (next) => { layer = next; layer.onAdd(map, gl); },
    removeLayer: () => { layer.onRemove(map, gl); layer = undefined; },
    getLayoutProperty: () => visibility, setLayoutProperty: (_id, _key, value) => { visibility = value; },
  };
  const frame = { shaderData: { variantName: "mercator" }, modelViewProjectionMatrix: [] };
  return { map, gl, counts, uniforms, render: () => { counts.frames++; layer.render(gl, frame); } };
}

test("real lighting updates replace curtain uniforms in place, including sun sync, with no new GPU work or loop", async (t) => {
  t.mock.method(performance, "now", () => 1000);
  const environment = await environmentCallback();
  const h = curtainHarness();
  effects.setCurtainShimmer(false);
  effects.registerSceneEffects(h.map, effects.DEFAULT_SCENE_EFFECTS);
  environment(h.map, "clear", 210);
  effects.syncBorderCurtain(h.map, false);
  h.render();
  const layer = h.map.getLayer();
  const resources = [h.counts.buffers, h.counts.programs, h.counts.vaos, h.counts.uploads];
  for (const preset of ["dusk", "night", "clear"]) {
    environment(h.map, preset, 210);
    effects.syncBorderCurtain(h.map, false);
    h.render();
    assert.equal(h.map.getLayer(), layer);
    assert.deepEqual(h.uniforms.u_foot, curtain.CURTAIN_PALETTES[preset].foot);
    assert.deepEqual(h.uniforms.u_crest, curtain.CURTAIN_PALETTES[preset].crest);
    assert.equal(h.uniforms.u_time, 0, "paused shimmer stays paused through palette changes");
    assert.deepEqual([h.counts.buffers, h.counts.programs, h.counts.vaos, h.counts.uploads], resources);
  }
  effects.registerSceneEffects(h.map, { ...effects.DEFAULT_SCENE_EFFECTS, sunSync: true });
  environment(h.map, "dusk", 210);
  h.render();
  assert.deepEqual(h.uniforms.u_foot, curtain.CURTAIN_PALETTES.night.foot, "computed night fill overrides manual dusk");
  assert.equal(h.counts.paints, 0, "palette adds no repaint request");
  assert.equal(h.counts.draws, h.counts.frames, "one draw per existing frame");
  effects.syncBorderCurtain(h.map, true);
  assert.equal(h.map.getLayoutProperty(), "none", "Battery saver remains authoritative");
});

async function controlsModule() {
  const drawingUrl = toUrl(transpile(await read("app/terrain-drawing.ts")));
  const surfaceUrl = toUrl(transpile((await read("app/terrain-surface.ts")).replace('"./terrain-drawing"', JSON.stringify(drawingUrl))));
  // Element-tree tests execute the real component callbacks; only React's
  // render lifecycle hook is replaced to avoid bringing a DOM into Node tests.
  const hooks = toUrl("let next = 0; export const useId = () => `studio-${++next}`; export const useState = () => [false, () => {}]; export const useEffect = () => {}; export const useRef = () => ({current:null});");
  const source = (await read("app/scene-effects-controls.tsx")).replace('"./terrain-surface"', JSON.stringify(surfaceUrl))
    .replace('"react"', JSON.stringify(hooks)).replace('"./scene-effects"', JSON.stringify(effectsUrl)).replace('"./scene-studio"', JSON.stringify(studioUrl));
  return import(toUrl(transpile(source).replace('"react/jsx-runtime"', JSON.stringify(pathToFileURL(require.resolve("react/jsx-runtime")).href))));
}
const descendants = (node) => !node || typeof node !== "object" ? [] : [node, ...[node.props?.children].flat(Infinity).flatMap(descendants)];

test("real controls dispatch recipe, light and camera changes; repeated panels have unique labels", async () => {
  const { SceneEffectsControls } = await controlsModule();
  const changes = [];
  const props = { settings: effects.DEFAULT_SCENE_EFFECTS, light: null, efficient: false, reducedMotion: false, flyoverActive: false, view: "tilted", presentation: { atmosphere: "night", azimuth: 210 }, camera: { pitch: 25, bearing: -22, fieldOfView: 44 }, cameraReady: true,
    onRecipe: (value) => changes.push(["recipe", value]), onLight: (value) => changes.push(["light", value]), onCamera: (...value) => changes.push(["camera", ...value]), onChange: (value) => changes.push(["effects", value]), onFlyover() {} };
  const first = descendants(SceneEffectsControls(props));
  first.find((node) => node.props?.["data-look"] === "golden").props.onClick();
  first.find((node) => node.props?.id?.endsWith("-light")).props.onChange({ target: { value: "260" } });
  for (const [id, value] of [["tilt", "50"], ["lens", "25"], ["bearing", "90"]]) first.find((node) => node.props?.id?.endsWith(`-${id}`)).props.onChange({ target: { value } });
  first.find((node) => node.type === "button" && node.props?.title?.includes("Keeps location")).props.onClick();
  assert.deepEqual(changes, [["recipe", "golden"], ["light", { atmosphere: "night", azimuth: 260 }], ["camera", { pitch: 50 }], ["camera", { fieldOfView: 25 }], ["camera", { bearing: 90 }], ["camera", studio.compositionDefaults("tilted"), true]]);
  const second = descendants(SceneEffectsControls(props));
  const ids = [...first, ...second].map((node) => node.props?.id).filter(Boolean);
  assert.equal(ids.length, new Set(ids).size, "all repeated controls use unique IDs");
  for (const node of first.filter((node) => node.props?.htmlFor)) assert.ok(ids.includes(node.props.htmlFor));
  assert.equal(first.find((node) => node.props?.id?.endsWith("-tilt")).props.max, 60);
  const globe = descendants(SceneEffectsControls({ ...props, view: "globe", reducedMotion: true, settings: { ...props.settings, sunSync: true } }));
  assert.equal(globe.find((node) => node.props?.id?.endsWith("-tilt")).props.disabled, true);
  assert.equal(globe.find((node) => node.props?.id?.endsWith("-light")).props.disabled, true);
  assert.equal(globe.find((node) => node.props?.className === "scene-effects-flyover").props.disabled, true);
  let stopped = 0;
  first[0].props.onPointerDown({ stopPropagation() { stopped++; } });
  first[0].props.onClick({ stopPropagation() { stopped++; } });
  assert.equal(stopped, 2, "controls do not leak pointer/click actions onto map features");
});
