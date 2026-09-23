import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const compileModule = async (name) => {
  const source = await readFile(new URL(`../app/${name}.ts`, import.meta.url), "utf8");
  const output = ts.transpileModule(source, {
    compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
    fileName: `${name}.ts`,
  }).outputText;
  return import(`data:text/javascript;base64,${Buffer.from(output).toString("base64")}`);
};

const radar = await compileModule("noaa-radar");

const capabilities = ({
  times,
  defaultTime = "2026-09-10T12:24:00Z",
  productId = radar.NOAA_RADAR_PRODUCT_ID,
  closeLayer = true,
} = {}) => `<?xml version="1.0" encoding="UTF-8"?>
<WMS_Capabilities version="1.3.0">
  <Capability>
    <Layer>
      <Layer queryable="1">
        <Name>${productId}</Name>
        <Title>CONUS weather radar base reflectivity</Title>
        <Dimension name="time" units="ISO8601" default="${defaultTime}" nearestValue="1">${times}</Dimension>
      ${closeLayer ? "</Layer>" : ""}
    </Layer>
  </Capability>
</WMS_Capabilities>`;

test("capabilities parsing uses only the fixed layer's exact times and sorts and deduplicates them", () => {
  const xml = `<?xml version="1.0"?>
  <WMS_Capabilities>
    <Layer>
      <Layer>
        <Name>unrelated_layer</Name>
        <Dimension name="time" default="1999-01-01T00:00:00Z">1999-01-01T00:00:00Z,1999-01-01T00:04:00Z</Dimension>
      </Layer>
      <Layer>
        <Name>${radar.NOAA_RADAR_PRODUCT_ID}</Name>
        <Dimension units="ISO8601" name='time' nearestValue="1" default='2026-09-10T12:08:00Z'>
          2026-09-10T12:08:00Z,
          2026-09-10T12:00:00.000Z,
          2026-09-10T12:04:00Z,
          2026-09-10T12:04:00.000Z
        </Dimension>
      </Layer>
    </Layer>
  </WMS_Capabilities>`;

  const parsed = radar.parseNoaaRadarCapabilities(xml);

  assert.deepEqual(parsed.frames, [
    "2026-09-10T12:00:00.000Z",
    "2026-09-10T12:04:00.000Z",
    "2026-09-10T12:08:00.000Z",
  ]);
  assert.equal(parsed.upstreamDefaultTime, "2026-09-10T12:08:00.000Z");
  assert.equal(Object.isFrozen(parsed.frames), true);
});

test("capabilities parsing fails closed for a changed, malformed, or ambiguous time contract", () => {
  const cases = [
    {
      label: "wrong layer",
      xml: capabilities({ productId: "different_radar_product", times: "2026-09-10T12:00:00Z,2026-09-10T12:04:00Z" }),
      message: /omitted the fixed CONUS radar layer/i,
    },
    {
      label: "unterminated layer",
      xml: `<WMS_Capabilities><Layer><Name>${radar.NOAA_RADAR_PRODUCT_ID}</Name><Dimension name="time">2026-09-10T12:00:00Z,2026-09-10T12:04:00Z</Dimension>`,
      message: /layer description was incomplete/i,
    },
    {
      label: "interval instead of observations",
      xml: capabilities({ times: "2026-09-10T12:00:00Z/2026-09-10T12:24:00Z/PT4M" }),
      message: /unsupported interval/i,
    },
    {
      label: "invalid timestamp",
      xml: capabilities({ times: "2026-09-10T12:00:00Z,not-a-time" }),
      message: /invalid timestamp/i,
    },
    {
      label: "too few observations",
      xml: capabilities({ times: "2026-09-10T12:00:00Z" }),
      message: /fewer than two usable observation frames/i,
    },
  ];

  for (const fixture of cases) {
    assert.throws(() => radar.parseNoaaRadarCapabilities(fixture.xml), fixture.message, fixture.label);
  }
});

test("manifest reports observed cadence, gaps, retention, age, and freshness without interpolation", () => {
  const xml = capabilities({
    defaultTime: "2026-09-10T12:24:00Z",
    times: [
      "2026-09-10T12:00:00Z",
      "2026-09-10T12:04:00Z",
      "2026-09-10T12:08:00Z",
      "2026-09-10T12:20:00Z",
      "2026-09-10T12:24:00Z",
    ].join(","),
  });

  const current = radar.buildNoaaRadarManifest(xml, "2026-09-10T12:29:00Z");
  assert.equal(current.nominalCadenceSeconds, 240);
  assert.equal(current.gapCount, 1);
  assert.equal(current.retentionMinutes, 24);
  assert.equal(current.latestAgeSeconds, 300);
  assert.equal(current.freshness, "current");
  assert.equal(current.frameCount, 5);
  assert.equal(current.interpolation, false);
  assert.equal(current.evidenceRole, "EXTERNAL_CONTEXT_ONLY");
  assert.equal(current.retrievedAt, "2026-09-10T12:29:00.000Z");

  const delayed = radar.buildNoaaRadarManifest(xml, "2026-09-10T12:40:01Z");
  assert.equal(delayed.latestAgeSeconds, 961);
  assert.equal(delayed.freshness, "delayed");
  assert.equal(radar.noaaRadarManifestIsFresh(current, Date.parse("2026-09-10T12:39:00Z")), true);
  assert.equal(radar.noaaRadarManifestIsFresh(current, Date.parse("2026-09-10T12:39:00.001Z")), false);
  assert.equal(radar.noaaRadarManifestIsFresh(current, Date.parse("2026-09-10T12:19:00Z")), true);
  assert.equal(radar.noaaRadarManifestIsFresh(current, Date.parse("2026-09-10T12:18:59.999Z")), false);
  assert.equal(radar.noaaRadarManifestIsFresh(null, Date.parse("2026-09-10T12:29:00Z")), false);

  const longOutage = radar.buildNoaaRadarManifest(capabilities({
    defaultTime: "2026-09-10T12:48:00Z",
    times: [
      "2026-09-10T12:00:00Z",
      "2026-09-10T12:04:00Z",
      "2026-09-10T12:08:00Z",
      "2026-09-10T12:44:00Z",
      "2026-09-10T12:48:00Z",
    ].join(","),
  }), "2026-09-10T12:53:00Z");
  assert.equal(longOutage.nominalCadenceSeconds, 240);
  assert.equal(longOutage.gapCount, 1);
  assert.throws(() => radar.buildNoaaRadarManifest(xml, "invalid"), /retrieval timestamp was invalid/i);
});

test("loop span selection is inclusive, bounded, sorted, and navigation obeys stop or wrap", () => {
  const frames = [
    "2026-09-10T12:00:00Z",
    "not-a-time",
    "2026-09-10T11:00:00Z",
    "2026-09-10T11:30:00Z",
    "2026-09-10T12:00:00.000Z",
    "2026-09-10T10:30:00Z",
  ];

  assert.deepEqual(radar.selectNoaaRadarLoopFrames(frames, 60), [
    "2026-09-10T11:00:00.000Z",
    "2026-09-10T11:30:00.000Z",
    "2026-09-10T12:00:00.000Z",
  ]);
  assert.deepEqual(radar.selectNoaaRadarLoopFrames(frames, 120, 2), [
    "2026-09-10T11:30:00.000Z",
    "2026-09-10T12:00:00.000Z",
  ]);
  assert.deepEqual(radar.selectNoaaRadarLoopFrames([], 30), []);

  assert.equal(radar.nextNoaaRadarFrameIndex(3, 1, "forward", false), 2);
  assert.equal(radar.nextNoaaRadarFrameIndex(3, 2, "forward", false), null);
  assert.equal(radar.nextNoaaRadarFrameIndex(3, 2, "forward", true), 0);
  assert.equal(radar.nextNoaaRadarFrameIndex(3, 0, "reverse", false), null);
  assert.equal(radar.nextNoaaRadarFrameIndex(3, 0, "reverse", true), 2);
  assert.equal(radar.nextNoaaRadarFrameIndex(0, 0, "forward", true), null);
});

test("tile requests always include one normalized exact TIME and reject untimed input", () => {
  const url = radar.noaaRadarTileUrl("2026-09-10T12:04:00Z");

  assert.equal(url.startsWith(`${radar.NOAA_RADAR_SERVICE_URL}?`), true);
  assert.match(url, /layers=conus_base_reflectivity_mosaic/);
  assert.match(url, /styles=weather_radar_base_reflectivity/);
  assert.match(url, /bbox=\{bbox-epsg-3857\}/);
  assert.match(url, /time=2026-09-10T12%3A04%3A00\.000Z/);
  assert.equal((url.match(/(?:\?|&)time=/g) ?? []).length, 1);
  assert.equal(url.includes("time=undefined"), false);

  for (const value of ["", "latest", "2026-09-10T12:04:00", "2026-09-10T12:04:00+00:00"]) {
    assert.throws(() => radar.noaaRadarTileUrl(value), /requires an exact advertised observation timestamp/i);
  }
});
