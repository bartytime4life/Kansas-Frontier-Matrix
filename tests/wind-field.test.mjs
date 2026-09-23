import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const source = await readFile(new URL("../app/wind-field.ts", import.meta.url), "utf8");
const javascript = ts.transpileModule(source, {
  compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
  fileName: "wind-field.ts",
}).outputText;
const { WIND_GRID, parseWindForecast, windVector, interpolateWind, isWindField } = await import(`data:text/javascript;base64,${Buffer.from(javascript).toString("base64")}`);
const fixture = () => WIND_GRID.map(([longitude, latitude]) => ({
  longitude, latitude, utc_offset_seconds: 0,
  hourly_units: { wind_speed_10m: "km/h", wind_direction_10m: "°" },
  hourly: { time: ["2026-09-23T22:00", "2026-09-23T23:00"], wind_speed_10m: [20, 30], wind_direction_10m: [270, 270] },
}));

test("complete bounded wind grid keeps two model forecast hours", () => {
  const field = parseWindForecast(fixture(), "2026-09-23T22:10:00Z");
  assert.equal(field.role, "EXTERNAL_MODEL_DISPLAY_ONLY");
  assert.equal(field.frames.length, 2);
  assert.equal(field.frames[0].samples.length, 9);
  assert.equal(field.frames[0].validAt, "2026-09-23T22:00:00.000Z");
  assert.equal(isWindField(field), true);
  const [east, north] = windVector(field.frames[0].samples[0]);
  assert.ok(east > 19.9 && Math.abs(north) < 0.001);
  const middle = interpolateWind(field.frames[0].samples, -98.4, 38.5);
  assert.ok(middle && middle[0] > 19.9);
});

test("missing locations, inconsistent clocks, and invalid vectors fail closed", () => {
  assert.throws(() => parseWindForecast(fixture().slice(1), "2026-09-23T22:10:00Z"));
  const clocks = fixture(); clocks[4].hourly.time[0] = "2026-09-23T21:00";
  assert.throws(() => parseWindForecast(clocks, "2026-09-23T22:10:00Z"));
  const values = fixture(); values[0].hourly.wind_speed_10m[0] = Number.NaN;
  assert.throws(() => parseWindForecast(values, "2026-09-23T22:10:00Z"));
});
