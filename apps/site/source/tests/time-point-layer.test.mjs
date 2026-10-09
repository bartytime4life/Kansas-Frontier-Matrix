import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const source = ts.transpileModule(await readFile(new URL("../app/time-point-layer.ts", import.meta.url), "utf8"), {
  compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
}).outputText;
const { createTimePointLayer, rgb, translateMatrix } = await import(`data:text/javascript;base64,${Buffer.from(source).toString("base64")}`);

const colors = { halo: "#a883ff", core: "#f6edff", stroke: "#a47dff" };
const mercatorX = (lng) => (180 + lng) / 360;

// Records the WebGL2 calls the layer makes; shaders compile unless told otherwise.
function fakeGl({ failGlobe = false, failAll = false } = {}) {
  const calls = [], uniforms = new Map(), uploads = [];
  let current = null, shaderText = new Map(), objectId = 0;
  const gl = {
    VERTEX_SHADER: 1, FRAGMENT_SHADER: 2, COMPILE_STATUS: 3, LINK_STATUS: 4, ARRAY_BUFFER: 5, DYNAMIC_DRAW: 6, FLOAT: 7,
    BLEND: 8, ONE: 9, ONE_MINUS_SRC_ALPHA: 10, DEPTH_TEST: 11, CULL_FACE: 12, TRIANGLE_STRIP: 13,
    drawingBufferWidth: 1600, drawingBufferHeight: 1000,
    createShader: () => ({ id: ++objectId }), shaderSource: (shader, text) => shaderText.set(shader, text), compileShader() {},
    getShaderParameter: (shader) => !failAll && !(failGlobe && shaderText.get(shader).includes("projectTileWithElevation")),
    createProgram: () => ({ id: ++objectId }), attachShader() {}, linkProgram() {}, deleteShader() {}, getProgramParameter: () => true,
    createVertexArray: () => ({ vao: ++objectId }), bindVertexArray() {}, createBuffer: () => ({ buffer: ++objectId }), bindBuffer() {},
    bufferData: (_target, data) => uploads.push(["data", Float32Array.from(data)]), bufferSubData: (_target, _offset, data) => uploads.push(["sub", Float32Array.from(data)]),
    getAttribLocation: (_program, name) => ["a_offset", "a_time", "a_ground"].indexOf(name), enableVertexAttribArray() {}, vertexAttribPointer() {}, vertexAttribDivisor() {},
    getUniformLocation: (program, name) => ({ program, name }), useProgram: (program) => { current = program; },
    deleteVertexArray: (vao) => calls.push(["deleteVertexArray", vao]), deleteProgram: (program) => calls.push(["deleteProgram", program]), deleteBuffer: (buffer) => calls.push(["deleteBuffer", buffer]),
    enable() {}, disable() {}, blendFunc() {},
    drawArraysInstanced: (mode, first, count, instances) => calls.push(["draw", uniforms.get("u_pass"), instances, mode, count]),
  };
  for (const setter of ["uniform1f", "uniform1i", "uniform2f", "uniform3f", "uniform4f"]) gl[setter] = (location, ...values) => uniforms.set(location.name, values.length === 1 ? values[0] : values);
  gl.uniformMatrix4fv = (location, _transpose, value) => uniforms.set(location.name, value);
  gl.uniform3fv = (location, value) => uniforms.set(location.name, value);
  return { gl, calls, uniforms, uploads, get current() { return current; } };
}

function fakeMap() {
  const handlers = new Map(); let repaints = 0;
  return {
    handlers, get repaints() { return repaints; },
    on: (event, fn) => handlers.set(event, fn), off: (event, fn) => { if (handlers.get(event) === fn) handlers.delete(event); },
    triggerRepaint: () => { repaints += 1; }, getTerrain: () => null, getZoom: () => 6, getPixelRatio: () => 2,
    getBounds: () => ({ getWest: () => -103, getEast: () => -94, getSouth: () => 36, getNorth: () => 41 }),
    queryTerrainElevation: () => 0, transform: { cameraToCenterDistance: 750 },
  };
}

const mercatorInput = { shaderData: { variantName: "mercator" }, modelViewProjectionMatrix: Array.from({ length: 16 }, (_, i) => (i % 5 === 0 ? 1 : 0)) };
const flashes = [
  { longitude: -98.5, latitude: 38.5, timeMs: 1_000_000 },
  { longitude: -97.25, latitude: 39.1, timeMs: 1_060_000 },
  { longitude: -100.0, latitude: 37.4, timeMs: 1_900_000 },
];

test("points upload once, relative to a local origin and the earliest time", () => {
  const layer = createTimePointLayer({ id: "flashes", colors });
  const { gl, uploads } = fakeGl(); const map = fakeMap();
  layer.setPoints(flashes);
  layer.onAdd(map, gl);
  assert.equal(uploads.length, 1);
  const [, data] = uploads[0];
  assert.equal(data.length, flashes.length * 4);
  assert.deepEqual([data[0], data[1], data[2]], [0, 0, 0]);
  assert.ok(Math.abs(data[4] - (mercatorX(-97.25) - mercatorX(-98.5))) < 1e-7);
  assert.equal(data[6], 60_000);
  assert.equal(data[10], 900_000);
  for (const event of ["moveend", "terrain", "sourcedata"]) assert.ok(map.handlers.has(event));
  // Moving the time window only changes uniforms: no further upload.
  layer.setWindow({ visible: true, halo: true, opacity: 0.9, mode: "pulse", cursor: 1_070_000, trailMs: 60_000 });
  layer.setWindow({ visible: true, halo: true, opacity: 0.9, mode: "pulse", cursor: 1_080_000, trailMs: 60_000 });
  assert.equal(uploads.filter(([kind]) => kind === "data").length, 1);
  assert.equal(map.repaints, 2);
});

test("slice and pulse windows reach the shader relative to the base time; halo and core draw in order", () => {
  const layer = createTimePointLayer({ id: "flashes", colors });
  const fake = fakeGl(); const map = fakeMap();
  layer.setPoints(flashes); layer.onAdd(map, fake.gl);

  layer.setWindow({ visible: true, halo: true, opacity: 0.8, mode: "slice", start: 1_000_000, end: 1_900_000, endInclusive: true });
  layer.render(fake.gl, mercatorInput);
  assert.equal(fake.uniforms.get("u_mode"), 0);
  assert.deepEqual(fake.uniforms.get("u_window"), [0, 900_000, 1, 0]);
  assert.equal(fake.uniforms.get("u_opacity"), 0.8);
  assert.deepEqual(fake.uniforms.get("u_extrude"), [2 / 800, 2 / 500]);
  assert.equal(fake.uniforms.get("u_extrude_w"), 750);
  assert.equal(fake.uniforms.get("u_device_ratio"), 2);
  assert.deepEqual(fake.calls.filter(([name]) => name === "draw").map(([, pass, instances, mode, count]) => [pass, instances, mode, count]),
    [[0, 3, fake.gl.TRIANGLE_STRIP, 4], [1, 3, fake.gl.TRIANGLE_STRIP, 4]]);
  assert.deepEqual(fake.uniforms.get("u_fill"), rgb(colors.core));

  fake.calls.length = 0;
  layer.setWindow({ visible: true, halo: false, opacity: 0.5, mode: "pulse", cursor: 1_070_000, trailMs: 120_000 });
  layer.render(fake.gl, mercatorInput);
  assert.equal(fake.uniforms.get("u_mode"), 1);
  assert.deepEqual(fake.uniforms.get("u_window"), [70_000, 120_000, 0, 0]);
  assert.deepEqual(fake.calls.filter(([name]) => name === "draw").map(([, pass]) => pass), [1], "reduced motion draws no halo pass");

  fake.calls.length = 0;
  layer.setWindow({ visible: false, halo: false, opacity: 0, mode: "slice", start: 0, end: 0, endInclusive: false });
  layer.render(fake.gl, mercatorInput);
  assert.equal(fake.calls.length, 0, "a hidden window draws nothing");
});

test("a globe shader failure disables only the globe variant and never throws", () => {
  const layer = createTimePointLayer({ id: "flashes", colors });
  const fake = fakeGl({ failGlobe: true }); const map = fakeMap();
  layer.setPoints(flashes); layer.onAdd(map, fake.gl);
  layer.setWindow({ visible: true, halo: true, opacity: 1, mode: "slice", start: 0, end: 2_000_000, endInclusive: true });
  const globe = { shaderData: { variantName: "globe", vertexShaderPrelude: "/* prelude: projectTileWithElevation */", define: "#define GLOBE" },
    defaultProjectionData: { mainMatrix: new Float32Array(16), fallbackMatrix: new Float32Array(16), tileMercatorCoords: [0, 0, 1, 1], clippingPlane: [0, 0, 0, 0], projectionTransition: 1 } };
  assert.doesNotThrow(() => layer.render(fake.gl, globe));
  assert.doesNotThrow(() => layer.render(fake.gl, globe));
  assert.equal(fake.calls.filter(([name]) => name === "draw").length, 0);
  layer.render(fake.gl, mercatorInput);
  assert.equal(fake.calls.filter(([name]) => name === "draw").length, 2, "mercator still draws");
});

test("a GPU that cannot compile the layer reports failure instead of throwing inside addLayer", () => {
  const layer = createTimePointLayer({ id: "flashes", colors });
  const fake = fakeGl({ failAll: true }); const map = fakeMap();
  layer.setPoints(flashes);
  assert.equal(layer.failed, false);
  assert.doesNotThrow(() => layer.onAdd(map, fake.gl));
  assert.equal(layer.failed, true);
  layer.setWindow({ visible: true, halo: true, opacity: 1, mode: "slice", start: 0, end: 2_000_000, endInclusive: true });
  assert.doesNotThrow(() => layer.render(fake.gl, mercatorInput));
  assert.equal(fake.calls.filter(([name]) => name === "draw").length, 0);
  assert.doesNotThrow(() => layer.onRemove(map, fake.gl));
});

test("removal frees the program, vertex array and buffer and unsubscribes", () => {
  const layer = createTimePointLayer({ id: "flashes", colors });
  const fake = fakeGl(); const map = fakeMap();
  layer.setPoints(flashes); layer.onAdd(map, fake.gl);
  layer.onRemove(map, fake.gl);
  for (const name of ["deleteVertexArray", "deleteProgram", "deleteBuffer"]) assert.ok(fake.calls.some(([call]) => call === name), name);
  assert.equal(map.handlers.size, 0);
  fake.calls.length = 0;
  layer.setWindow({ visible: true, halo: true, opacity: 1, mode: "slice", start: 0, end: 2_000_000, endInclusive: true });
  layer.render(fake.gl, mercatorInput);
  assert.equal(fake.calls.length, 0);
});

test("float32 time offsets select exactly the flashes the CPU filter selected", () => {
  // Worst case: a full 180-minute GLM window plus the provider's 2-minute lead, ms timestamps.
  let seed = 11; const rand = () => (seed = (seed * 1664525 + 1013904223) % 4294967296) / 4294967296;
  const end = Date.UTC(2026, 6, 4, 3), start = end - 182 * 60_000;
  const times = Array.from({ length: 5000 }, () => Math.round(start + rand() * (end - start)));
  // Put flashes exactly on, and one millisecond either side of, every 15-minute edge.
  for (let edge = start; edge <= end; edge += 900_000) times.push(edge - 1, edge, edge + 1);
  const base = Math.min(...times), f = Math.fround;
  for (let binStart = start; binStart < end; binStart += 900_000) {
    const binEnd = Math.min(end, binStart + 900_000), inclusive = binEnd === end;
    for (const t of times) {
      const cpu = t >= binStart && (inclusive ? t <= binEnd : t < binEnd);
      const gpu = f(t - base) >= f(binStart - base) && (f(t - base) < f(binEnd - base) || (inclusive && f(t - base) <= f(binEnd - base)));
      assert.equal(gpu, cpu, `flash at ${t} in bin ${binStart}`);
    }
  }
  for (const cursor of [start + 60_000, start + 5_400_000, end]) {
    for (const t of times) {
      const cpu = t <= cursor && t >= cursor - 60_000;
      const age = f(f(cursor - base) - f(t - base));
      assert.equal(age >= 0 && age <= 60_000, cpu, `pulse flash at ${t}`);
    }
  }
});

test("the Mercator matrix folds in the data origin in float64", () => {
  const matrix = Array.from({ length: 16 }, (_, i) => i + 1);
  const out = translateMatrix(matrix, 3, 5);
  for (let row = 0; row < 4; row += 1) assert.equal(out[12 + row], Math.fround(matrix[row] * 3 + matrix[4 + row] * 5 + matrix[12 + row]));
  assert.deepEqual(Array.from(out.slice(0, 12)), matrix.slice(0, 12));
  assert.deepEqual(rgb("#a47dff"), [0xa4 / 255, 0x7d / 255, 1]);
  assert.throws(() => rgb("purple"));
});
