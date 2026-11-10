import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const source = await readFile(new URL("../app/water-flow-context.ts", import.meta.url), "utf8");
const javascript = ts.transpileModule(source, {
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
  const basis = { stationId: "USGS-06864500", parameterCode: "00060", statisticId: "00011", unit: "ft^3/s" };
  const observations = [0, 20, 100].map((value) => ({ ...basis, value }));
  const base = { ...basis, missing: false, value: 20, previousValue: 0 };
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

test("comparison cues never combine different stations, parameters, statistics or units", () => {
  const basis = { stationId: "USGS-06864500", parameterCode: "00060", statisticId: "00011", unit: "ft^3/s" };
  const frame = { ...basis, missing: false, value: 100, previousValue: 5 };
  for (const changed of [{ unit: "m^3/s" }, { statisticId: "00003" }, { parameterCode: "00065" }, { stationId: "USGS-06864501" }]) {
    const rows = [{ ...basis, value: 100 }, { ...basis, ...changed, value: 5 }];
    assert.equal(water.waterComparisonState(rows, frame), "mixed");
    const cue = water.waterReadingCue(frame, rows);
    assert.deepEqual(cue, { kind: "uncompared", value: 100, previousValue: null, change: null, rangePosition: null, rangeMinimum: null, rangeMaximum: null });
    assert.equal(water.waterReadingCue({ ...frame, value: 0 }, rows).kind, "zero");
    assert.equal(water.waterReadingCue({ ...frame, missing: true, value: null }, rows).kind, "missing");
  }
});

test("unqualified measurement bases withhold comparisons without withholding the raw reading", () => {
  const basis = { stationId: "USGS-06864500", parameterCode: "00060", statisticId: "00011", unit: "ft^3/s" };
  for (const missing of [{ unit: null }, { unit: "" }, { statisticId: null }, { statisticId: undefined }, { parameterCode: undefined }]) {
    const frame = { ...basis, ...missing, missing: false, value: 10, previousValue: 5 };
    const rows = [{ ...basis, ...missing, value: 5 }, { ...basis, ...missing, value: 10 }];
    assert.equal(water.waterComparisonState(rows, frame), "unqualified");
    const cue = water.waterReadingCue(frame, rows);
    assert.equal(cue.value, 10); assert.equal(cue.change, null); assert.equal(cue.rangePosition, null);
  }
  assert.equal(water.waterComparisonState([]), "empty");
});
