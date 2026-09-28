import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const source = await readFile(new URL("../app/lightning-data.ts", import.meta.url), "utf8");
const js = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const lightning = await import(`data:text/javascript;base64,${Buffer.from(js).toString("base64")}`);
const xml = (times, layer = lightning.NOAA_LIGHTNING_LAYER) => `<WMS_Capabilities><Layer><Name>other_layer</Name><Dimension name="time">1990-01-01T00:00:00Z</Dimension></Layer><Layer><Name>${layer}</Name><Dimension name="time" units="ISO8601">${times}</Dimension></Layer></WMS_Capabilities>`;

test("fixed NOAA layer admits only exact UTC quarter-hour frames", () => {
  const result = lightning.parseLightningCapabilities(xml("2026-09-28T13:30:00Z,2026-09-28T13:15:00.000Z,2026-09-28T13:30:00.000Z"), "2026-09-28T13:34:00.000Z");
  assert.deepEqual(result.frames, ["2026-09-28T13:15:00.000Z", "2026-09-28T13:30:00.000Z"]);
  assert.equal(result.latest, "2026-09-28T13:30:00.000Z");
  assert.equal(result.intervalMinutes, 15);
  assert.equal(result.evidenceRole, "EXTERNAL_CONTEXT_ONLY");
  assert.throws(() => lightning.parseLightningCapabilities(xml("2026-09-28T13:30:00Z", "different")), /fixed NOAA/i);
  assert.throws(() => lightning.parseLightningCapabilities(xml("2026-09-28T13:00:00Z/2026-09-28T13:30:00Z/PT15M")), /unsupported/i);
  assert.throws(() => lightning.parseLightningCapabilities(xml("2026-09-28T13:07:00Z")), /15-minute clock/i);
  assert.throws(() => lightning.parseLightningCapabilities(xml("2026-02-31T13:15:00Z")), /invalid UTC/i);
});

test("WMS requests are fixed to EPSG:3857 tile bounds and a named time", () => {
  const frame = "2026-09-28T13:30:00.000Z";
  const url = new URL(lightning.lightningWmsUrl(frame, 5, 7, 12));
  assert.equal(url.origin, "https://nowcoast.noaa.gov");
  assert.equal(url.searchParams.get("LAYERS"), lightning.NOAA_LIGHTNING_LAYER);
  assert.equal(url.searchParams.get("STYLES"), lightning.NOAA_LIGHTNING_STYLE);
  assert.equal(url.searchParams.get("SRS"), "EPSG:3857");
  assert.equal(url.searchParams.get("VERSION"), "1.1.1");
  assert.equal(url.searchParams.get("TIME"), "2026-09-28T13:30:00.000Z");
  assert.equal(url.searchParams.get("TRANSPARENT"), "TRUE");
  assert.equal(url.searchParams.get("BBOX")?.split(",").length, 4);
  assert.throws(() => lightning.lightningWmsUrl(frame, 14, 7, 12), /coordinates/i);
  assert.throws(() => lightning.lightningWmsUrl(frame, 5, -1, 12), /coordinates/i);
  assert.throws(() => lightning.lightningWmsUrl("2026-09-28T13:30:00Z", 5, 7, 12), /advertised UTC/i);
});

test("NASA GIBS carrier is fixed historical climatology, separate from NOAA", () => {
  assert.match(lightning.NASA_LIGHTNING_METADATA_URL, /LIS_High_Resolution_Full_Climatology/);
  assert.match(lightning.NASA_LIGHTNING_TILES, /GoogleMapsCompatible_Level6/);
  assert.doesNotMatch(lightning.NASA_LIGHTNING_TILES, /nowcoast/);
});

test("lightning density legend is the fixed NOAA image for the displayed layer", () => {
  const url = new URL(lightning.NOAA_LIGHTNING_LEGEND_URL);
  assert.equal(url.origin, "https://nowcoast.noaa.gov");
  assert.equal(url.searchParams.get("request"), "GetLegendGraphic");
  assert.equal(url.searchParams.get("layer"), lightning.NOAA_LIGHTNING_LAYER);
  assert.equal(url.searchParams.get("format"), "image/png");
});

test("lightning controls display the provider legend and do not infer interval boundaries", async () => {
  const [page, css, quality, legendRoute, registry] = await Promise.all([
    readFile(new URL("../app/page.tsx", import.meta.url), "utf8"),
    readFile(new URL("../app/globals.css", import.meta.url), "utf8"),
    readFile(new URL("../app/source-quality-row.tsx", import.meta.url), "utf8"),
    readFile(new URL("../app/api/lightning/legend/route.ts", import.meta.url), "utf8"),
    readFile(new URL("../app/live-context.ts", import.meta.url), "utf8"),
  ]);
  assert.match(page, /src="\/api\/lightning\/legend"/);
  assert.match(legendRoute, /fetchLightningPng\(NOAA_LIGHTNING_LEGEND_URL\)/);
  assert.doesNotMatch(css, /\.lightning-density-key i \{[^}]*linear-gradient/);
  assert.doesNotMatch(page, /Frame interval:/);
  assert.doesNotMatch(quality, /interval ends/);
  assert.match(registry, /defaultOpacity: 0\.27, color: "#8779c9"/);
});
