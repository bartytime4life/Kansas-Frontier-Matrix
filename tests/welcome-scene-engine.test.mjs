import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';

// The real engine with stand-ins for three.js, the scene catalog and loaders:
// these tests are about when a scene is compiled and swapped, not rendering.
const toUrl = source => `data:text/javascript;base64,${Buffer.from(source).toString('base64')}`;
const three = toUrl(`
export const SRGBColorSpace = 'srgb', ACESFilmicToneMapping = 4;
export const MathUtils = { radToDeg: r => r * 180 / Math.PI, degToRad: d => d * Math.PI / 180 };
export class WebGLRenderer {
  constructor() { globalThis.__engine.renderer = this; this.extensions = { has: name => name === 'KHR_parallel_shader_compile' && globalThis.__engine.parallel }; if (globalThis.__engine.parallel !== undefined) this.compileAsync = (scene, camera) => { globalThis.__engine.log.push(['compile', scene.name]); return new Promise(resolve => { globalThis.__engine.finishCompile = resolve; }); }; }
  setPixelRatio() {} setSize() {} dispose() {} forceContextLoss() {} getContext() { return {}; }
  render(scene) { globalThis.__engine.log.push(['render', scene.name]); }
}`);
const catalog = toUrl(`export const SCENE_CATALOG = { a: { duration: 10 }, b: { duration: 10 } }; export const beatIndex = () => 0;`);
const loaders = toUrl(`const scene = name => async () => ({ create: () => ({ scene: { name }, camera: {}, update() {}, dispose() { globalThis.__engine.log.push(['dispose', name]); } }) });
export const SCENE_LOADERS = { a: scene('a'), b: scene('b') };`);
const kit = toUrl(`export const disposeTree = scene => globalThis.__engine.log.push(['disposeTree', scene.name]); export const clamp = (v, lo = 0, hi = 1) => Math.min(hi, Math.max(lo, v)); export const POINT_SCALE = { value: 1 };`);

let source = await readFile('app/living-welcome/scenes/engine.mjs', 'utf8');
for (const [from, to] of [["from 'three';", `from '${three}';`], ["from './catalog.mjs';", `from '${catalog}';`], ["from './index.mjs';", `from '${loaders}';`], ["from './kit.mjs';", `from '${kit}';`]]) {
  assert.ok(source.includes(from), `engine still imports ${from}`);
  source = source.replace(from, to);
}
const { createSceneEngine } = await import(toUrl(source));

Object.assign(globalThis, {
  window: { devicePixelRatio: 1 },
  document: { hidden: false, addEventListener() {}, removeEventListener() {} },
  ResizeObserver: class { observe() {} disconnect() {} },
  requestAnimationFrame: () => 1,
  cancelAnimationFrame: () => {},
});
const canvas = () => ({ clientWidth: 800, clientHeight: 450, dataset: {}, isConnected: true, addEventListener() {}, removeEventListener() {} });
const settle = () => new Promise(resolve => setTimeout(resolve, 200));
const start = parallel => { globalThis.__engine = { parallel, log: [] }; return createSceneEngine(canvas(), {}); };
// A paused engine may draw its still frame more than once; only the order matters.
const renders = () => [...new Set(globalThis.__engine.log.filter(([kind]) => kind === 'render').map(([, name]) => name))];
const at = (kind, name) => globalThis.__engine.log.findIndex(([k, n]) => k === kind && n === name);

test('with parallel shader compile, a scene is compiled before it replaces the one on screen', async () => {
  const engine = start(true);
  engine.show('a'); await settle();
  assert.deepEqual(globalThis.__engine.log, [['compile', 'a']], 'nothing draws while the first scene compiles');
  globalThis.__engine.finishCompile(); await settle();
  assert.deepEqual(renders(), ['a']);
  assert.equal(engine.sceneId, 'a');
  engine.show('b'); await settle();
  assert.equal(engine.sceneId, 'a', 'the current scene stays while the next one compiles');
  assert.deepEqual(globalThis.__engine.log.at(-1), ['compile', 'b']);
  globalThis.__engine.finishCompile(); await settle();
  assert.equal(engine.sceneId, 'b');
  assert.ok(at('compile', 'b') < at('dispose', 'a') && at('dispose', 'a') < at('disposeTree', 'a') && at('disposeTree', 'a') < at('render', 'b'), 'the previous scene is released only after the next one compiled, then the next one draws');
  engine.dispose();
});

test('a scene superseded while it compiles is disposed and never drawn', async () => {
  const engine = start(true);
  engine.show('a'); await settle(); globalThis.__engine.finishCompile(); await settle();
  engine.show('b'); await settle();
  engine.show('a'); // back to the scene on screen while b compiles
  globalThis.__engine.finishCompile(); await settle();
  assert.equal(engine.sceneId, 'a');
  assert.ok(!renders().includes('b'), 'b never reaches the screen');
  assert.deepEqual(globalThis.__engine.log.slice(-2), [['dispose', 'b'], ['disposeTree', 'b']]);
  engine.dispose();
});

test('without parallel shader compile, the first draw compiles as before', async () => {
  for (const parallel of [false, undefined]) {
    const engine = start(parallel);
    engine.show('a'); await settle();
    assert.equal(engine.sceneId, 'a');
    assert.ok(!globalThis.__engine.log.some(([kind]) => kind === 'compile'), `no compileAsync wait (${parallel})`);
    assert.deepEqual(renders(), ['a']);
    engine.dispose();
  }
});
