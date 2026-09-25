import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const source = await readFile(new URL("../app/source-time.ts", import.meta.url), "utf8");
const javascript = ts.transpileModule(source, {
  compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
  fileName: "source-time.ts",
}).outputText;
const time = await import(`data:text/javascript;base64,${Buffer.from(javascript).toString("base64")}`);

const payload = (feed, features) => ({
  feed,
  state: features.length ? "ready" : "empty",
  retrievedAt: "2026-09-23T12:00:00.000Z",
  upstreamUpdatedAt: null,
  featureCount: features.length,
  data: { type: "FeatureCollection", features },
  source: "https://example.gov/source",
  limitation: "Checked source records only.",
  truncated: false,
});
const feature = (properties) => ({ type: "Feature", geometry: { type: "Point", coordinates: [-97, 38] }, properties });

test("older-day slider conversion preserves UTC leap days and clamps only draft dates", () => {
  const leap = time.utcDayOrdinal("2000-02-29");
  assert.equal(time.utcDayFromOrdinal(leap + 1), "2000-03-01");
  assert.equal(time.utcDayFromOrdinal(leap - 1), "2000-02-28");
  assert.equal(time.utcDayOrdinal("1900-02-29"), null);
  assert.equal(time.utcDayOrdinal("2026-13-01"), null);
  assert.equal(time.boundedUtcDay("2000-02-29", "1995-01-01", "2026-09-23"), "2000-02-29");
  assert.equal(time.boundedUtcDay("1994-12-31", "1995-01-01", "2026-09-23"), "1995-01-01");
  assert.equal(time.boundedUtcDay("2026-09-24", "1995-01-01", "2026-09-23"), "2026-09-23");
  assert.equal(time.boundedUtcDay("", "2005-08-05", "2026-09-23"), "2026-09-23");
  assert.equal(time.boundedUtcDay("2026-09-23", "2026-09-24", "2026-09-23"), null);
});

test("dated source status separates returned day records from selected map frame and visibility", () => {
  const status = (frame, selected, effective, ready) =>
    time.datedSourceDisplayStatus(12, frame, "2026-09-23", selected, effective, ready);
  assert.match(status(3, false, false, true), /12 returned records.*3 at selected frame.*Turn on layer to display/);
  assert.match(status(3, true, false, true), /Held by atlas year/);
  assert.match(status(3, true, true, false), /Waiting for map renderer/);
  assert.match(status(3, true, true, true), /3 at selected frame.*shown on map/);
  assert.match(status(0, true, true, true), /0 at selected frame.*no features to display/);
});

test("earthquake sweep has only checked-day event times and cannot carry yesterday's events", () => {
  const original = payload("usgs-earthquakes", [
    feature({ observedAt: "2026-09-22T23:59:59.000Z", id: "yesterday" }),
    feature({ observedAt: "2026-09-23T00:00:01.000Z", id: "first" }),
    feature({ observedAt: "2026-09-23T00:00:02.000Z", id: "second" }),
  ]);
  assert.deepEqual(time.earthquakeEventTimes(original, "2026-09-23"), ["2026-09-23T00:00:01.000Z", "2026-09-23T00:00:02.000Z"]);
  assert.deepEqual(time.earthquakesThroughEvent(original, "2026-09-23", "2026-09-23T00:00:01.000Z").data.features.map((item) => item.properties.id), ["first"]);
  assert.equal(time.earthquakesThroughEvent(original, "2026-09-21", "2026-09-21T23:59:59.000Z").featureCount, 0);
});

test("smoke sweep changes only at provider validity boundaries", () => {
  const original = payload("noaa-hms-smoke", [
    feature({ start: "2026-09-23T01:00:00.000Z", end: "2026-09-23T02:00:00.000Z", id: "morning" }),
    feature({ start: "2026-09-23T02:00:00.000Z", end: "2026-09-23T03:00:00.000Z", id: "later" }),
  ]);
  assert.deepEqual(time.smokeValidityTimes(original, "2026-09-23"), [
    "2026-09-23T00:00:00.000Z", "2026-09-23T01:00:00.000Z", "2026-09-23T02:00:00.000Z", "2026-09-23T03:00:00.000Z",
  ]);
  assert.equal(time.smokeValidAt(original, "2026-09-23", "2026-09-23T00:00:00.000Z").featureCount, 0);
  assert.deepEqual(time.smokeValidAt(original, "2026-09-23", "2026-09-23T01:00:00.000Z").data.features.map((item) => item.properties.id), ["morning"]);
  assert.deepEqual(time.smokeValidAt(original, "2026-09-23", "2026-09-23T02:00:00.000Z").data.features.map((item) => item.properties.id), ["later"]);
  assert.equal(time.smokeValidAt(original, "2026-09-22", "2026-09-22T02:00:00.000Z").featureCount, 0);
});
