import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const source = await readFile(new URL("../app/streamflow.ts", import.meta.url), "utf8");
const javascript = ts.transpileModule(source, {
  compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
  fileName: "streamflow.ts",
}).outputText;
const streamflow = await import(`data:text/javascript;base64,${Buffer.from(javascript).toString("base64")}`);

const station = (stationId = "USGS-06864500", patch = {}) => ({
  stationId,
  name: "Smoky Hill River at Ellsworth, KS",
  longitude: -98.2306,
  latitude: 38.7306,
  agencyCode: "USGS",
  siteTypeCode: "ST",
  ...patch,
});

const observation = (stationId, observedAt, value, patch = {}) => ({
  stationId,
  observedAt,
  value,
  unit: "ft3/s",
  parameterCode: "00060",
  statisticId: "00000",
  approvalStatus: "Provisional",
  qualifiers: ["P"],
  lastModified: null,
  ...patch,
});

const payload = (patch = {}) => ({
  format: "kfm-usgs-streamflow-v1",
  feed: "usgs-streamflow",
  state: "ready",
  retrievedAt: "2026-09-10T12:30:00Z",
  query: {
    mode: "recent-series",
    start: "2026-09-10T11:00:00Z",
    end: "2026-09-10T12:30:00Z",
    parameterCode: "00060",
  },
  stations: [station()],
  observations: [observation("USGS-06864500", "2026-09-10T12:15:00Z", 120)],
  source: "https://api.waterdata.usgs.gov/ogcapi/v0/",
  limitation: "Provisional external context only.",
  truncated: false,
  interpolation: false,
  evidenceRole: "EXTERNAL_CONTEXT_ONLY",
  ...patch,
});

test("strict payload validation and parsing normalize numeric strings, IDs, and exact UTC times", () => {
  const raw = payload({
    stations: [station("06864500", { name: "  Ellsworth gauge  ", longitude: "-98.2306", latitude: "38.7306" })],
    observations: [observation("06864500", "2026-09-10T12:15:00Z", "120.5", {
      qualifiers: [" P "],
      lastModified: "2026-09-10T12:20:00Z",
    })],
  });

  assert.equal(streamflow.isStreamflowBundlePayload(raw), true);
  assert.equal(streamflow.isStreamflowBundle(raw), false, "numeric strings are wire-valid but not a normalized in-memory bundle");
  const bundle = streamflow.parseStreamflowBundle(raw);
  assert.equal(streamflow.isStreamflowBundle(bundle), true);
  assert.equal(bundle.retrievedAt, "2026-09-10T12:30:00.000Z");
  assert.deepEqual(bundle.stations[0], {
    stationId: "USGS-06864500",
    name: "Ellsworth gauge",
    longitude: -98.2306,
    latitude: 38.7306,
    agencyCode: "USGS",
    siteTypeCode: "ST",
  });
  assert.equal(bundle.observations[0].stationId, "USGS-06864500");
  assert.equal(bundle.observations[0].observedAt, "2026-09-10T12:15:00.000Z");
  assert.equal(bundle.observations[0].value, 120.5);
  assert.equal(bundle.observations[0].qualifiers[0], "P");
  assert.equal(Object.isFrozen(bundle), true);
  assert.equal(Object.isFrozen(bundle.observations), true);
});

test("station and time validators reject ambiguous identifiers, offsets, and calendar rollover", () => {
  assert.equal(streamflow.normalizeUsgsStationId("06864500"), "USGS-06864500");
  assert.equal(streamflow.normalizeUsgsStationId("usgs-06864500"), "USGS-06864500");
  assert.equal(streamflow.isUsgsStationId("USGS-06864500"), true);
  for (const invalid of ["", "USGS-123", "KS-06864500", "USGS-06864500?x=1", "06864500,06864000"]) {
    assert.equal(streamflow.isUsgsStationId(invalid), false, invalid);
  }

  assert.equal(streamflow.normalizeStreamflowIsoTime("2026-09-10T12:15:00Z"), "2026-09-10T12:15:00.000Z");
  assert.equal(streamflow.normalizeStreamflowIsoTime("2026-09-10T12:15:00.2Z"), "2026-09-10T12:15:00.200Z");
  for (const invalid of ["2026-09-10", "2026-09-10T12:15:00", "2026-09-10T12:15:00+00:00", "2026-02-30T12:15:00Z", "latest"]) {
    assert.equal(streamflow.normalizeStreamflowIsoTime(invalid), null, invalid);
  }
});

test("strict bundle validation fails closed for malformed contracts and cross-station ambiguity", () => {
  const invalidCases = [
    payload({ feed: "other-feed" }),
    payload({ source: "http://example.com/data" }),
    payload({ interpolation: true }),
    payload({ evidenceRole: "EVIDENCE" }),
    payload({ state: "empty" }),
    payload({ query: { mode: "recent-series", start: "2026-09-11T00:00:00Z", end: "2026-09-10T00:00:00Z", parameterCode: "00060" } }),
    payload({ stations: [station("USGS-06864500"), station("06864500")] }),
    payload({ observations: [observation("USGS-99999999", "2026-09-10T12:15:00Z", 1)] }),
    payload({ observations: [observation("USGS-06864500", "2026-02-30T12:15:00Z", 1)] }),
    payload({ observations: [observation("USGS-06864500", "2026-09-10T12:15:00Z", "not-a-number")] }),
  ];
  for (const [index, candidate] of invalidCases.entries()) {
    assert.equal(streamflow.isStreamflowBundlePayload(candidate), false, `case ${index}`);
    assert.throws(() => streamflow.parseStreamflowBundle(candidate), /invalid bundle contract/i, `case ${index}`);
  }
});

test("duplicate station-time observations prefer the later explicit lastModified revision", () => {
  const bundle = streamflow.parseStreamflowBundle(payload({
    observations: [
      observation("USGS-06864500", "2026-09-10T12:15:00Z", 100, { lastModified: "2026-09-10T12:16:00Z" }),
      observation("USGS-06864500", "2026-09-10T12:00:00Z", 80, { lastModified: null }),
      observation("06864500", "2026-09-10T12:15:00.000Z", "125", { approvalStatus: "Approved", lastModified: "2026-09-10T12:22:00Z" }),
      observation("USGS-06864500", "2026-09-10T12:15:00Z", 110, { lastModified: "2026-09-10T12:18:00Z" }),
    ],
  }));

  assert.equal(bundle.observations.length, 2);
  assert.deepEqual(bundle.observations.map((item) => item.observedAt), [
    "2026-09-10T12:00:00.000Z",
    "2026-09-10T12:15:00.000Z",
  ]);
  assert.equal(bundle.observations[1].value, 125);
  assert.equal(bundle.observations[1].approvalStatus, "Approved");
  assert.equal(bundle.observations[1].lastModified, "2026-09-10T12:22:00.000Z");
});

test("display frames remain exact and sorted while uniformly bounded to 96 observations", () => {
  const observations = Array.from({ length: 200 }, (_, index) => observation(
    "USGS-06864500",
    new Date(Date.parse("2026-09-01T00:00:00Z") + index * 60_000).toISOString(),
    index,
  ));
  observations.push(observations[50]);
  const bundle = streamflow.parseStreamflowBundle(payload({
    query: { mode: "recent-series", start: "2026-09-01T00:00:00Z", end: "2026-09-01T04:00:00Z", parameterCode: "00060" },
    observations,
  }));

  const frames = streamflow.streamflowDisplayFrames(bundle, 999);
  assert.equal(frames.length, streamflow.STREAMFLOW_MAX_DISPLAY_FRAMES);
  assert.equal(frames[0], "2026-09-01T00:00:00.000Z");
  assert.equal(frames.at(-1), "2026-09-01T03:19:00.000Z");
  assert.equal(frames.every((frame, index) => index === 0 || Date.parse(frame) > Date.parse(frames[index - 1])), true);
  assert.deepEqual(streamflow.buildStreamflowDisplayFrames(bundle, 3), [
    "2026-09-01T00:00:00.000Z",
    "2026-09-01T01:40:00.000Z",
    "2026-09-01T03:19:00.000Z",
  ]);
});

test("frame construction uses the latest prior sample only inside tolerance and never interpolates", () => {
  const raw = payload({
    stations: [
      station("USGS-06864500"),
      station("USGS-06864000", { name: "Smoky Hill River near Russell", longitude: -98.86, latitude: 38.78 }),
      station("USGS-06861000", { name: "Saline River at Tescott", longitude: -97.88, latitude: 39.0 }),
    ],
    observations: [
      observation("USGS-06864500", "2026-09-10T12:00:00Z", 100),
      observation("USGS-06864500", "2026-09-10T12:15:00Z", 120),
      observation("USGS-06864500", "2026-09-10T12:45:00Z", 999),
      observation("USGS-06864000", "2026-09-10T12:20:00Z", null),
    ],
  });
  const bundle = streamflow.parseStreamflowBundle(raw);
  const frame = streamflow.buildStreamflowFrame(bundle, "2026-09-10T12:30:00Z", 20);

  assert.equal(frame.type, "FeatureCollection");
  assert.equal(frame.features.length, 3);
  const ellsworth = frame.features.find((feature) => feature.properties.stationId === "USGS-06864500").properties;
  assert.equal(ellsworth.featureId, "usgs-streamflow-06864500");
  assert.equal(ellsworth.frameCursor, "2026-09-10T12:30:00.000Z");
  assert.equal(ellsworth.observedAt, "2026-09-10T12:15:00.000Z");
  assert.equal(ellsworth.value, 120);
  assert.equal(ellsworth.previousValue, 100);
  assert.equal(ellsworth.changePercent, 20);
  assert.equal(ellsworth.trend, "rising");
  assert.equal(ellsworth.ageMinutes, 15);
  assert.equal(ellsworth.missing, false);
  assert.equal(ellsworth.interpolation, false);

  const nullValue = frame.features.find((feature) => feature.properties.stationId === "USGS-06864000").properties;
  assert.equal(nullValue.observedAt, "2026-09-10T12:20:00.000Z");
  assert.equal(nullValue.ageMinutes, 10);
  assert.equal(nullValue.value, null);
  assert.equal(nullValue.displayValue, "Value not reported");
  assert.equal(nullValue.trend, "missing");
  assert.equal(nullValue.missing, true);

  const absent = frame.features.find((feature) => feature.properties.stationId === "USGS-06861000").properties;
  assert.equal(absent.observedAt, null);
  assert.equal(absent.ageMinutes, null);
  assert.equal(absent.displayValue, "No observation in tolerance");
  assert.equal(absent.missing, true);
  assert.equal(frame.features.some((feature) => feature.properties.value === 999), false, "future observations are never selected");
  assert.throws(() => streamflow.buildStreamflowFrame(bundle, "latest", 20), /explicit UTC ISO cursor/i);
  assert.throws(() => streamflow.buildStreamflowFrame(bundle, "2026-09-10T12:30:00Z", -1), /non-negative tolerance/i);
});

test("large observation gaps suppress change claims even when the current value is displayable", () => {
  const bundle = streamflow.parseStreamflowBundle(payload({
    query: { mode: "historical-series", start: "2026-09-01T00:00:00Z", end: "2026-09-10T12:30:00Z", parameterCode: "00060" },
    observations: [
      observation("USGS-06864500", "2026-09-01T00:00:00Z", 100),
      observation("USGS-06864500", "2026-09-10T12:15:00Z", 150),
    ],
  }));
  const frame = streamflow.buildStreamflowFrame(bundle, "2026-09-10T12:20:00Z", 30);
  assert.equal(frame.features[0].properties.value, 150);
  assert.equal(frame.features[0].properties.changePercent, null);
  assert.equal(frame.features[0].properties.previousObservedAt, null);
  assert.equal(frame.features[0].properties.trend, "unknown");
});

test("selected station series is canonical and hydrograph paths break at nulls and declared gaps", () => {
  const series = [
    observation("USGS-06864500", "2026-09-10T00:00:00Z", 10),
    observation("USGS-06864500", "2026-09-10T00:05:00Z", 20),
    observation("USGS-06864500", "2026-09-10T00:10:00Z", null),
    observation("USGS-06864500", "2026-09-10T00:15:00Z", 30),
    observation("USGS-06864500", "2026-09-10T00:20:00Z", 40),
    observation("USGS-06864500", "2026-09-10T01:00:00Z", 50),
    observation("USGS-06864500", "2026-09-10T01:05:00Z", 60),
  ];
  const bundle = streamflow.parseStreamflowBundle(payload({
    query: { mode: "recent-series", start: "2026-09-10T00:00:00Z", end: "2026-09-10T02:00:00Z", parameterCode: "00060" },
    observations: series,
  }));
  const selected = streamflow.stationObservations(bundle, "06864500");
  assert.equal(selected.length, 7);
  assert.equal(selected.every((item) => item.stationId === "USGS-06864500"), true);
  assert.throws(() => streamflow.stationObservations(bundle, "not-a-site"), /valid USGS/i);

  const segments = streamflow.buildHydrographSegments(selected, { width: 300, height: 100, padding: 10, gapMinutes: 20 });
  assert.deepEqual(segments.map((segment) => segment.pointCount), [2, 2, 2]);
  assert.deepEqual(segments.map((segment) => [segment.startTime, segment.endTime]), [
    ["2026-09-10T00:00:00.000Z", "2026-09-10T00:05:00.000Z"],
    ["2026-09-10T00:15:00.000Z", "2026-09-10T00:20:00.000Z"],
    ["2026-09-10T01:00:00.000Z", "2026-09-10T01:05:00.000Z"],
  ]);
  assert.equal(segments.every((segment) => /^M\d+\.\d{2},\d+\.\d{2} L\d+\.\d{2},\d+\.\d{2}$/.test(segment.path)), true);
  assert.throws(() => streamflow.buildHydrographSegments(selected, { width: 300, height: 100, gapMinutes: 0 }), /positive finite duration/i);
  assert.throws(() => streamflow.buildHydrographSegments([
    ...selected,
    { ...selected[0], stationId: "USGS-06864000" },
  ], { width: 300, height: 100, gapMinutes: 20 }), /one selected station/i);
});
