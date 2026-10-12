import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const source = await readFile(new URL("../app/fire-report-analysis.ts", import.meta.url), "utf8");
const javascript = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const { buildFireReportContext, nearbyFireContext, validFireReportContext } = await import(`data:text/javascript;base64,${Buffer.from(javascript).toString("base64")}`);
const fire = (longitude, latitude, name, acquiredAt) => ({ type: "Feature", geometry: { type: "Point", coordinates: [longitude, latitude] }, properties: { name, acquiredAt } });

test("nearby comparison retains distance and source time without asserting an incident match", () => {
  const neighbors = nearbyFireContext(fire(-96, 38, "Report", null), [fire(-96.02, 38, "Thermal pixel", "2026-09-23T16:00:00Z"), fire(-97, 38, "Far pixel", null)], "acquiredAt");
  assert.equal(neighbors.length, 1);
  assert.equal(neighbors[0].name, "Thermal pixel");
  assert.ok(neighbors[0].distanceKm > 1 && neighbors[0].distanceKm < 2);
  assert.equal(neighbors[0].eventTime, "2026-09-23T16:00:00Z");
});

test("invalid coordinates and missing candidates do not produce a false corroboration", () => {
  assert.deepEqual(nearbyFireContext(fire(-96, 38, "Report", null), [fire(NaN, 38, "Bad", null)], "acquiredAt"), []);
  assert.deepEqual(nearbyFireContext(null, [fire(-96, 38, "Pixel", null)], "acquiredAt"), []);
});

test("fire report seed retains distinct provider and retrieval times with bounded comparison", () => {
  const selected = { ...fire(-96, 38, "Kansas report", null), properties: { name: "Kansas report", featureId: "nifc-1", discoveryAt: "2026-09-23T12:00:00Z" } };
  const context = buildFireReportContext("nifc-fire-reports", selected, "2026-09-24T14:00:00Z", "partial", "error", [
    { name: "Thermal pixel", distanceKm: 2.5, eventTime: "2026-09-23T15:00:00Z" },
    { name: "Invalid far point", distanceKm: 20, eventTime: null },
  ]);
  assert.equal(context.observedAt, "2026-09-23T12:00:00Z");
  assert.equal(context.retrievedAt, "2026-09-24T14:00:00Z");
  assert.equal(context.feedState, "partial");
  assert.equal(context.comparisonState, "unavailable");
  assert.equal(context.nearby.length, 1);
  assert.equal(validFireReportContext(context), true);
  assert.equal(validFireReportContext({ ...context, sourceUrl: "https://example.com/" }), false);
});
