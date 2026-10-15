import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const source = await readFile(new URL("../app/water-flow-context.ts", import.meta.url), "utf8");
const geometrySource = await readFile(new URL("../app/water-flow-motion.ts", import.meta.url), "utf8");
const geometryJs = ts.transpileModule(geometrySource, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const geometryUrl = `data:text/javascript;base64,${Buffer.from(geometryJs).toString("base64")}`;
const javascript = ts.transpileModule(source.replace('"./water-flow-motion"', JSON.stringify(geometryUrl)), {
  compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
  fileName: "water-flow-context.ts",
}).outputText;
const water = await import(`data:text/javascript;base64,${Buffer.from(javascript).toString("base64")}`);

const channel = (flowdirection = 1, featuretype = 1, coordinates = [[-98.23, 38.74], [-98.22, 38.73]]) => ({
  properties: { id3dhp: "AB12", flowdirection, featuretype },
  geometry: { type: "LineString", coordinates },
});

test("direction guide accepts only bounded explicit downstream channel lines", () => {
  const paths = water.boundedDirectionPaths({ features: [
    channel(), channel(0), channel(1, 5), channel(2), channel(1, 1, [[-98.23, 38.74], [Infinity, 38.73]]),
  ] });
  assert.equal(paths.length, 1);
  assert.deepEqual(paths[0].coordinates, [[-98.23, 38.74], [-98.22, 38.73]]);
  assert.throws(() => water.boundedDirectionPaths({ error: { message: "failed" } }));
  assert.throws(() => water.boundedDirectionPaths({ features: Array(101).fill(channel()) }));
});

test("observation cues distinguish zero, missing, rising, and relative loaded range", () => {
  const observations = [0, 20, 100].map((value) => ({ value }));
  const base = { missing: false, value: 20, previousValue: 0 };
  assert.deepEqual(water.waterReadingCue(base, observations), {
    kind: "rising", value: 20, previousValue: 0, change: 20,
    rangePosition: 0.2, rangeMinimum: 0, rangeMaximum: 100,
  });
  assert.equal(water.waterReadingCue({ ...base, value: 0, previousValue: 20 }, observations).kind, "zero");
  const missing = water.waterReadingCue({ ...base, missing: true, value: null }, observations);
  assert.equal(missing.kind, "missing");
  assert.equal(missing.rangePosition, null);
  assert.equal(water.waterReadingCue({ ...base, value: 10, previousValue: 20 }, observations).kind, "falling");
  assert.equal(water.waterReadingCue({ ...base, value: 10, previousValue: null }, observations).kind, "uncompared");
  assert.equal(water.waterReadingCue(base, [{ value: null }]).rangePosition, null);
});


test("legacy bounded directions share the fixed flowline envelope without moving vertices", () => {
  for (const coordinates of [
    [[-102.24, 38], [-102.23, 38]], [[-98, 36.76], [-98, 36.77]], [[-98, 40.23], [-98, 40.24]],
  ]) assert.deepEqual(water.boundedDirectionPaths({features:[channel(1,1,coordinates)]})[0].coordinates, coordinates);
  for (const point of [[-102.26,38],[-94.39,38],[-98,36.74],[-98,40.26]]) {
    assert.deepEqual(water.boundedDirectionPaths({features:[channel(1,1,[point,[-98,38]])]}),[]);
  }
});
