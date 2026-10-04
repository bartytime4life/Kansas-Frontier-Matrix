import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const compile = (source, fileName) => ts.transpileModule(source, {
  compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 }, fileName,
}).outputText;
const globeSource = await readFile(new URL("../app/globe-context.ts", import.meta.url), "utf8");
const globeUrl = `data:text/javascript;base64,${Buffer.from(compile(globeSource, "globe-context.ts")).toString("base64")}`;
const source = await readFile(new URL("../app/water-motion-canvas.ts", import.meta.url), "utf8");
const javascript = compile(source.replace('from "./globe-context";', `from "${globeUrl}";`), "water-motion-canvas.ts");
const { drawWaterMotionCanvas } = await import(`data:text/javascript;base64,${Buffer.from(javascript).toString("base64")}`);

function draw(length, elapsedMs, animateDirection, value = 10, options = {}) {
  const arrows = [];
  const rings = [];
  let strokes = 0;
  const trailLengths = [];
  const context = {
    setTransform() {}, clearRect() {}, save() {}, restore() {}, beginPath() {},
    arc(_x, _y, radius) { rings.push(radius); },
    moveTo(x) { this.startX = x; this.lastX = x; }, lineTo(x) { this.lastX = x; },
    stroke() { strokes += 1; if (this.strokeStyle?.startsWith("rgba(231, 255, 249")) trailLengths.push(this.lastX - this.startX); },
    setLineDash() {}, rotate() {},
    closePath() {}, fill() {}, translate(x, y) { arrows.push([x, y]); },
  };
  const canvas = { width: 0, height: 0, getContext: () => context };
  const map = {
    getCanvas: () => ({ clientWidth: options.width ?? 200, clientHeight: options.height ?? 100 }), project: ([x, y]) => ({ x, y }),
    getProjection: () => ({ type: options.globe ? "globe" : "mercator" }),
    getZoom: () => options.zoom ?? 6,
    getCenter: () => ({ lng: options.center?.[0] ?? 0, lat: options.center?.[1] ?? 40 }),
  };
  const priorWindow = globalThis.window;
  globalThis.window = { devicePixelRatio: 1 };
  try {
    drawWaterMotionCanvas(canvas, map, { features: options.features ?? [] }, "USGS-06864500",
      [{ id: "river", coordinates: options.coordinates ?? [[0, 40], [length, 40]] }],
      { value }, elapsedMs, false, animateDirection);
  } finally {
    globalThis.window = priorWindow;
  }
  return { arrows, rings, strokes, trailLengths };
}

test("mapped downstream arrows move while the observation frame is paused", () => {
  assert.notDeepEqual(draw(100, 0, true).arrows, draw(100, 400, true).arrows);
  assert.deepEqual(draw(100, 0, false).arrows, draw(100, 400, false).arrows);
});

test("a short but visible mapped channel still has a direction arrow", () => {
  assert.deepEqual(draw(20, 0, true).arrows, [[10, 40]]);
  assert.equal(draw(100, 1700, true).arrows.length, 1);
});

test("longer motion trails remain on positive-flow mapped channels", () => {
  assert.ok(draw(100, 400, true).strokes > draw(100, 400, false).strokes);
  assert.equal(draw(100, 400, true, 0).strokes, draw(100, 400, false).strokes);
  const mapped = draw(200, 2200, true);
  assert.ok(mapped.trailLengths.some(length => length > 100 && length <= 200));
});

test("expanded trails reach 240 pixels and follow bends without motion for missing readings", () => {
  const long = draw(400, 4400, true, 10, { width: 500 });
  assert.ok(long.trailLengths.some(length => Math.abs(length - 240) < 0.01));
  const bend = draw(240, 3000, true, 10, { width: 300, height: 200, coordinates: [[0, 40], [120, 40], [120, 160]] });
  assert.deepEqual(bend.arrows, [[120, 88]]);
  assert.equal(draw(400, 4400, true, null, { width: 500 }).trailLengths.length, 0);
});

test("globe overview shrinks and hides pulse rings as Kansas recedes", () => {
  const feature = { geometry: { type: "Point", coordinates: [0, 40] }, properties: { stationId: "USGS-06864500", missing: false, value: 10, trend: "rising" } };
  const flat = draw(100, 400, false, 10, { features: [feature] });
  const regional = draw(100, 400, false, 10, { globe: true, zoom: 5.45, features: [feature] });
  const earth = draw(100, 400, false, 10, { globe: true, zoom: 0.6, features: [feature] });
  assert.ok(flat.rings[0] > regional.rings[0]);
  assert.deepEqual(earth.rings, []);
  assert.deepEqual(draw(100, 400, false, 10, { globe: true, zoom: 5.45, center: [180, 40], features: [feature] }).rings, []);
});

test("zero and missing gauges have stationary marks and no downstream arrows", () => {
  for (const value of [0, null]) {
    const feature = { geometry: { type: "Point", coordinates: [50, 40] }, properties: { stationId: "USGS-06864500", missing: value === null, value, trend: "steady" } };
    const first = draw(100, 0, true, value, { features: [feature] });
    const later = draw(100, 1200, true, value, { features: [feature] });
    assert.equal(first.rings.length, 1);
    assert.deepEqual(first.rings, later.rings);
    assert.deepEqual(first.arrows, []);
    assert.deepEqual(first.trailLengths, []);
  }
});
