import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const compileModuleUrl = async (name, transform = (source) => source) => {
  const source = await readFile(new URL(`../app/${name}.ts`, import.meta.url), "utf8");
  const output = ts.transpileModule(transform(source), {
    compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
    fileName: `${name}.ts`,
  }).outputText;
  return `data:text/javascript;base64,${Buffer.from(output).toString("base64")}`;
};

const temporal = await import(await compileModuleUrl("temporal-sweep"));
const radarModuleUrl = await compileModuleUrl("noaa-radar");
const official = await import(await compileModuleUrl("live-context", (source) => source.replace(
  'from "./noaa-radar";',
  `from "${radarModuleUrl}";`,
)));

const feature = (fid, title, year) => ({
  type: "Feature",
  id: fid,
  properties: { fid, title, year },
  geometry: { type: "Point", coordinates: [-98, 38] },
});

const layer = (id, domain, mode, years) => ({
  id,
  title: id,
  domain,
  temporal: { field: "year", mode, years, label: `${id} time` },
  data: { type: "FeatureCollection", features: years.map((year) => feature(`${id}-${year}`, `${id} ${year}`, year)) },
});

const exactA = layer("weather", "Atmosphere", "exact", [2022, 2024, 2026]);
const exactB = layer("fire", "Fire", "exact", [2024, 2026]);
const through = layer("history", "History", "through", [1885, 1910]);
const layers = [exactA, exactB, through];
const atlas = [1885, 1910, 1950, 2022, 2024, 2026];

test("event stepping uses only bounded layer event dates plus bounded endpoints", () => {
  assert.deepEqual(
    temporal.buildTemporalSequence(layers, atlas, 1900, 2025, "available-events"),
    [1900, 1910, 2022, 2024, 2025],
  );
  assert.deepEqual(
    temporal.buildTemporalSequence(layers, atlas, 1900, 2025, "regular-calendar"),
    [1910, 1950, 2022, 2024],
  );
  assert.deepEqual(
    temporal.buildTemporalSequence([layer("new-feed", "Water", "exact", [2023])], atlas, 2022, 2024, "available-events"),
    [2022, 2023, 2024],
  );
  assert.deepEqual(
    temporal.buildTemporalSequence(layers, atlas, 2000, 2000, "regular-calendar"),
    [2000],
  );
});

test("moving windows and accumulation use explicit intervals without interpolation", () => {
  const sequence = [2022, 2024, 2026];
  const windowQuery = temporal.buildTemporalQuery("moving-window", 2026, 2022, 2026, sequence, 2);
  assert.equal(windowQuery.windowStart, 2024);
  assert.deepEqual(
    temporal.temporalRecordsForQuery([exactA], windowQuery, true).map((record) => record.year),
    [2024, 2026],
  );

  const offSequenceQuery = temporal.buildTemporalQuery("moving-window", 2025, 2022, 2026, sequence, 2);
  assert.equal(offSequenceQuery.windowStart, 2022);
  assert.equal(offSequenceQuery.frame, 2025);

  const outsideRangeQuery = temporal.buildTemporalQuery("snapshot", 2026, 1885, 1910, [1885, 1910]);
  assert.equal(outsideRangeQuery.frame, 2026);
  assert.equal(outsideRangeQuery.rangeEnd, 2026);

  const accumulationQuery = temporal.buildTemporalQuery("accumulation", 2026, 2024, 2026, sequence, 3);
  assert.deepEqual(
    temporal.temporalRecordsForQuery(layers, accumulationQuery, true).map((record) => record.year).sort(),
    [2024, 2024, 2026, 2026],
  );
});

test("frame summaries expose entered, exited, and cross-domain co-presence", () => {
  const prior = temporal.buildTemporalQuery("snapshot", 2022, 2022, 2026, [2022, 2024, 2026]);
  const current = temporal.buildTemporalQuery("snapshot", 2024, 2022, 2026, [2022, 2024, 2026]);
  const summary = temporal.buildTemporalFrameSummary(layers, current, prior);

  assert.equal(summary.entered.length, 2);
  assert.equal(summary.exited.length, 1);
  assert.equal(summary.activeDomainCount, 3);
  assert.equal(summary.domainPairs.some((pair) => pair.id === "Atmosphere::Fire"), true);
});

test("playback obeys direction and explicit stop or loop boundaries", () => {
  const sequence = [1910, 2022, 2024];
  assert.equal(temporal.nextTemporalFrame(sequence, 1910, "forward", "stop"), 2022);
  assert.equal(temporal.nextTemporalFrame(sequence, 2024, "forward", "stop"), null);
  assert.equal(temporal.nextTemporalFrame(sequence, 2024, "forward", "loop"), 1910);
  assert.equal(temporal.nextTemporalFrame(sequence, 1910, "reverse", "loop"), 2024);
  assert.equal(temporal.nextTemporalFrame(sequence, 2023, "forward", "stop"), 2024);
  assert.equal(temporal.nextTemporalFrame(sequence, 2023, "reverse", "stop"), 2022);
  assert.equal(temporal.nearestTemporalFrame(sequence, 2023), 2022);
});

test("current official sources fail closed outside the operational-present frame", () => {
  const selected = Object.fromEntries(official.OFFICIAL_CONTEXT_SOURCES.map((source) => [source.id, true]));
  assert.equal(Object.values(official.officialContextVisibilityForFrame(selected, 1910)).every((value) => value === false), true);
  assert.equal(Object.values(official.officialContextVisibilityForFrame(selected, official.OFFICIAL_CONTEXT_PRESENT_FRAME)).every((value) => value === true), true);
});
