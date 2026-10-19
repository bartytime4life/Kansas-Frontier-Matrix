import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import ts from 'typescript';
// Staging retains its existing minimum-zoom field in the 13-float layout.
const STRIDE = 13;

async function loadLayer(directory = '.') {
  const compile = async file => {
    let code = ts.transpileModule(await readFile(`${directory}/app/${file}.ts`, 'utf8'), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
    for (const match of [...code.matchAll(/from "\.\/([^\"]+)"/g)]) code = code.replace(match[0], `from ${JSON.stringify(await compile(match[1]))}`);
    return `data:text/javascript;base64,${Buffer.from(code).toString('base64')}`;
  };
  return import(await compile('water-flow-layer'));
}
function renderer(createWaterFlowLayer, vertices = 3001, initialHeight = 0) {
  const uploads = [], draws = [], events = new Map();
  let calls = 0, repaints = 0, terrain = { source: 'dem', exaggeration: 1 }, height = 0;
  const segments = new Float32Array(vertices * STRIDE);
  const geometry = { segments, count: vertices, vertices: Array.from({ length: vertices }, (_, i) => ({ lng: -98 + i * .000001, lat: 38, slots: [i * STRIDE + 2, i * STRIDE + 5] })) };
  for (const vertex of geometry.vertices) for (const slot of vertex.slots) segments[slot] = initialHeight;
  const gl = new Proxy({ drawingBufferWidth: 1600, drawingBufferHeight: 720,
    bufferData(_target, data) { uploads.push(data.slice()); },
    drawArraysInstanced(_mode, _start, _corners, count) { draws.push(count); },
    getShaderParameter: () => true, getProgramParameter: () => true, getAttribLocation: () => 0,
    createBuffer: () => ({}), createShader: () => ({}), createProgram: () => ({}), createVertexArray: () => ({}),
  }, { get: (target, key) => key in target ? target[key] : /^[A-Z_]+$/.test(key) ? 1 : () => {} });
  const map = { getTerrain: () => terrain, getCenter: () => ({ lng: -98, lat: 38 }), isMoving: () => false,
    queryTerrainElevation() { calls++; return typeof height === 'function' ? height(calls) : height; },
    getZoom: () => 11, triggerRepaint() { repaints++; }, on: (name, fn) => events.set(name, fn), off() {} };
  const layer = createWaterFlowLayer({ id: 'test-water', clock: () => 7, palette: () => ({ base: [0,0,1], streak: [1,1,1], tints: Array(5).fill([1,1,1]), opacity: .86 }) });
  layer.onAdd(map, gl); uploads.length = 0; layer.setGeometry(geometry);
  const input = { shaderData: { variantName: 'mercator' }, modelViewProjectionMatrix: Array(16).fill(0) };
  return { layer, map, geometry, uploads, draws, events, gl,
    render: () => layer.render(gl, input), set height(value) { height = value; }, set terrain(value) { terrain = value; },
    get calls() { return calls; }, get repaints() { return repaints; } };
}

test('unchanged and unavailable terrain completes sampling with one upload and identical draws', async t => {
  const { createWaterFlowLayer } = await loadLayer();
  for (const height of [0, null, NaN]) {
    const r = renderer(createWaterFlowLayer, 60000); r.height = height;
    for (let frame = 0; frame < 41; frame++) r.render();
    assert.equal(r.calls, 60000, 'no vertex or terrain query was dropped');
    assert.equal(r.uploads.length, 1);
    assert.ok(r.uploads.every(bytes => bytes.length === 60000 * STRIDE));
    assert.deepEqual(r.geometry.segments, new Float32Array(60000 * STRIDE));
    assert.deepEqual(r.draws, Array(41).fill(60000), 'every segment remains in every frame');
    assert.ok(r.repaints >= 40, 'unchanged batches still progress to completion');
  }
  t.diagnostic(JSON.stringify({ workload: 'synthetic-60000-segment-unchanged-terrain', baselineUploadBytes: 40 * 60000 * STRIDE * 4, candidateUploadBytes: 60000 * STRIDE * 4, terrainQueries: 60000, frames: 41, fpsClaim: false }));
});

test('late heights, Float32 rounding, source resampling and terrain removal preserve exact bytes', async () => {
  const { createWaterFlowLayer } = await loadLayer();
  const r = renderer(createWaterFlowLayer); r.height = call => call > 3000 ? 123.456789 : null;
  r.render(); r.render(); r.render();
  assert.equal(r.calls, 3001); assert.equal(r.uploads.length, 2);
  assert.equal(r.geometry.segments[3000 * STRIDE + 2], Math.fround(123.456789));
  r.height = 123.456789; r.events.get('sourcedata')({ sourceId: 'dem' });
  r.render(); r.render(); r.render();
  const uploads = r.uploads.length;
  r.events.get('sourcedata')({ sourceId: 'dem' }); r.render(); r.render(); r.render();
  assert.equal(r.uploads.length, uploads, 'Float64-to-Float32 rounding does not cause repeated uploads');
  assert.ok(r.geometry.vertices.every(v => v.slots.every(slot => r.geometry.segments[slot] === Math.fround(123.456789))));
  r.terrain = null; r.render();
  assert.equal(r.uploads.length, uploads + 1);
  assert.ok(r.geometry.vertices.every(v => v.slots.every(slot => r.geometry.segments[slot] === 0)));
  r.render(); assert.equal(r.uploads.length, uploads + 1);
  assert.equal(r.layer.terrainSamplingPending, false);
  const early = renderer(createWaterFlowLayer); early.height = 17; early.render();
  early.terrain = null; early.render(); assert.equal(early.layer.terrainSamplingPending, false);
  assert.ok(early.geometry.vertices.every(v => v.slots.every(slot => early.geometry.segments[slot] === 0)));
  const repaintCount = early.repaints; early.render(); assert.equal(early.repaints, repaintCount, 'no obsolete terrain queue keeps 2D redrawing');
  const signed = renderer(createWaterFlowLayer, 1); signed.height = -0; signed.render();
  assert.ok(Object.is(signed.geometry.segments[2], -0), 'stored signed zero preserves provider Float32 bytes');
  signed.terrain = null; signed.render(); assert.ok(Object.is(signed.geometry.segments[2], 0));
  r.layer.onRemove(r.map, r.gl);
});

if (process.env.KFM_FLOW_BASELINE) test('exact baseline and candidate render the same geometry and segment counts', async t => {
  const before = renderer((await loadLayer(process.env.KFM_FLOW_BASELINE)).createWaterFlowLayer, 60000);
  const after = renderer((await loadLayer()).createWaterFlowLayer, 60000);
  for (let frame = 0; frame < 41; frame++) { before.render(); after.render(); }
  assert.deepEqual(after.geometry.segments, before.geometry.segments);
  assert.deepEqual(after.draws, before.draws);
  assert.equal(before.calls, after.calls);
  t.diagnostic(JSON.stringify({ baselineUploads: before.uploads.length, candidateUploads: after.uploads.length, baselineBytes: before.uploads.reduce((sum, data) => sum + data.byteLength, 0), candidateBytes: after.uploads.reduce((sum, data) => sum + data.byteLength, 0), equalGeometryAndDrawCounts: true, realGPU: false }));
});
