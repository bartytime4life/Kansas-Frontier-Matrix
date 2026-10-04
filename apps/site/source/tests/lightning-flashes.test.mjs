import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const source = await readFile(new URL("../app/lightning-flashes.ts", import.meta.url), "utf8");
const js = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const glm = await import(`data:text/javascript;base64,${Buffer.from(js).toString("base64")}`);
const generatedAt = "2026-10-01T02:00:00.000000+00:00";
const requestedAt = "2026-10-01T02:00:10.000Z";
const feature = (id, time = "2026-10-01T01:59:30.000000+00:00", coordinates = [-97.974365234, 39.491146088]) => ({
  type: "Feature", geometry: { type: "Point", coordinates },
  properties: { id, flash_time: time, energy_fj: 5.2, area_km2: 74.16 },
});
const feed = (features, metadata = {}) => ({ type: "FeatureCollection", features, metadata: { source: "goes19_glm", window_minutes: 15, count: features.length, generated_at: generatedAt, ...metadata } });

test("observed flash times and centroids are preserved and sorted; no synthetic event is added", () => {
  const x = glm.parseGlmFlashSnapshot(feed([
    feature(2, "2026-10-01T01:59:45.000000+00:00"), feature(1),
  ]), 15, requestedAt);
  assert.equal(x.evidenceRole, "EXTERNAL_CONTEXT_ONLY");
  assert.equal(x.source, "NOAA_GOES19_GLM_VIA_ATMOSTORM");
  assert.equal(x.state, "ready");
  assert.equal(x.flashes.length, 2);
  assert.equal(x.flashes[0].observedAt, "2026-10-01T01:59:30.000000+00:00");
  assert.deepEqual([x.flashes[0].longitude, x.flashes[0].latitude], [-97.974365234, 39.491146088]);
  assert.deepEqual(glm.glmFlashPlaybackBounds(x), { start: Date.parse(generatedAt) - 15 * 60_000, end: Date.parse(generatedAt) });
});

test("changed source, wrong window, duplicate flashes, bad coordinates and future times fail closed", () => {
  assert.throws(() => glm.parseGlmFlashSnapshot(feed([feature(1)], { source: "different" }), 15, requestedAt), /source, window/i);
  assert.throws(() => glm.parseGlmFlashSnapshot(feed([feature(1)], { window_minutes: 5 }), 15, requestedAt), /source, window/i);
  assert.throws(() => glm.parseGlmFlashSnapshot(feed([feature(1), feature(1)]), 15, requestedAt), /duplicate/i);
  assert.throws(() => glm.parseGlmFlashSnapshot(feed([feature(1, undefined, [-70, 39])]), 15, requestedAt), /position/i);
  assert.throws(() => glm.parseGlmFlashSnapshot(feed([feature(1, "2026-10-01T02:03:00.000000+00:00")]), 15, requestedAt), /time/i);
  assert.throws(() => glm.parseGlmFlashSnapshot(feed([feature(1)], { count: 5000 }), 15, requestedAt), /count/i);
});

test("empty, stale, border and capped responses disclose their limits", () => {
  assert.equal(glm.parseGlmFlashSnapshot(feed([]), 15, requestedAt).state, "empty");
  assert.equal(glm.parseGlmFlashSnapshot(feed([feature(1)]), 15, "2026-10-01T02:10:00.000Z").state, "stale");
  assert.equal(glm.parseGlmFlashSnapshot(feed([feature(1, undefined, [-94.5, 39])]), 15, requestedAt).nearBorderCount, 1);
  const capped = glm.parseGlmFlashSnapshot(feed(Array.from({ length: 5000 }, (_, i) => feature(i))), 15, requestedAt);
  assert.equal(capped.state, "partial");
  assert.match(capped.partialReason, /older flashes may be missing/i);
  assert.throws(() => glm.parseGlmFlashSnapshot(feed(Array.from({ length: 5001 }, (_, i) => feature(i))), 15, requestedAt), /count/i);
});

test("three-hour source window is supported and slices partition observed timestamps", () => {
  const x = glm.parseGlmFlashSnapshot(feed([
    feature(1, "2026-09-30T23:00:00Z"),
    feature(2, "2026-09-30T23:15:00Z"),
    feature(3, "2026-10-01T02:00:00Z"),
  ], { window_minutes: 180 }), 180, requestedAt);
  for (const minutes of [15, 30, 60]) {
    const bins = glm.glmFlashBins(x, minutes);
    assert.equal(bins.length, 180 / minutes);
    assert.equal(bins.reduce((sum, bin) => sum + bin.count, 0), 3);
    assert.equal(bins.at(-1).count, 1);
    assert.equal(bins[0].start, Date.parse("2026-09-30T23:00:00Z"));
    assert.equal(bins.at(-1).end, Date.parse(generatedAt));
  }
  assert.equal(glm.glmFlashBins(x, 15)[0].count, 1);
  assert.equal(glm.glmFlashBins(x, 15)[1].count, 1);
  assert.equal(glm.glmFlashBins(x, 15)[2].count, 0);
  assert.throws(() => glm.parseGlmFlashSnapshot(feed([], { window_minutes: 1440 }), 1440, requestedAt));
});
