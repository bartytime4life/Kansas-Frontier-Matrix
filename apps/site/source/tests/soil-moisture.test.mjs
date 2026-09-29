import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const compile = async (name, imports = {}) => {
  const source = await readFile(new URL(`../app/${name}.ts`, import.meta.url), "utf8");
  const output = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 } }).outputText;
  const mod = { exports: {} };
  new Function("require", "module", "exports", output)((key) => imports[key], mod, mod.exports);
  return mod.exports;
};
const soil = await compile("soil-moisture");
const server = await compile("soil-moisture-server", {
  "./soil-moisture": soil,
  "./bounded-json": { readBoundedText: async response => response.text() },
});
const now = new Date("2026-09-29T13:00:00Z");
const layer = (name, ranges) => `<Layer><ows:Identifier>${name}</ows:Identifier><Dimension><ows:Identifier>Time</ows:Identifier>${ranges.map(range => `<Value>${range}</Value>`).join("")}</Dimension><TileMatrixSetLink><TileMatrixSet>GoogleMapsCompatible_Level6</TileMatrixSet></TileMatrixSetLink></Layer>`;
const capabilities = overrides => `<Capabilities>${Object.entries(soil.SOIL_VIEWS).map(([view, spec]) => layer(spec.layer, overrides?.[view] ?? ["2026-09-25/2026-09-27/P1D"])).join("")}</Capabilities>`;

test("four fixed views share only exact available UTC days and preserve gaps", () => {
  const parsed = soil.parseSoilAvailability(capabilities({ root: ["2026-09-25/2026-09-25/P1D", "2026-09-27/2026-09-27/P1D"] }), now);
  assert.deepEqual(soil.commonSoilDays(parsed), ["2026-09-27", "2026-09-25"]);
  assert.equal(parsed.root.includes("2026-09-26"), false);
  assert.equal(Object.keys(soil.SOIL_VIEWS).length, 4);
  assert.equal(new Set(Object.values(soil.SOIL_VIEWS).map(view => view.layer)).size, 4);
  assert.match(soil.soilLegendUrl("root-uncertainty"), /Uncertainty/);
  assert.match(soil.soilLegendUrl("surface"), /Analyzed_Soil_Moisture_H/);
});

test("malformed provider time and missing layers fail closed", () => {
  assert.throws(() => soil.parseSoilAvailability(capabilities({ root: ["2026-09-25/2026-09-27/P2D"] }), now));
  assert.throws(() => soil.parseSoilAvailability(capabilities({ root: ["2026-02-30/2026-03-02/P1D"] }), now));
  assert.throws(() => soil.parseSoilAvailability("<Capabilities></Capabilities>", now));
  assert.equal(soil.validSoilDay("2026-02-30", now), false);
  assert.equal(soil.validSoilDay("2026-08-01", now), false);
  assert.equal(soil.validSoilDay("2026-09-30", now), false);
});

test("tile address allowlist rejects invalid view, day, duplicate query, and out of range coordinates", () => {
  const good = new URL("https://example.test/api/soil-moisture/tile?view=surface&day=2026-09-27&z=6&x=14&y=24");
  // Request parser uses the actual current 30-day window.
  good.searchParams.set("day", new Date().toISOString().slice(0, 10));
  assert.equal(server.parseTileRequest(good.href).view, "surface");
  for (const [key, value] of [["view", "other"], ["day", "2020-01-01"], ["x", "64"], ["z", "7"], ["y", "-1"]]) {
    const bad = new URL(good); bad.searchParams.set(key, value);
    assert.throws(() => server.parseTileRequest(bad.href), { code: "INVALID_TILE_REQUEST" });
  }
  const duplicate = new URL(good); duplicate.searchParams.append("view", "root");
  assert.throws(() => server.parseTileRequest(duplicate.href));
});

test("provider redirect and oversized responses are rejected before reading", async () => {
  const original = global.fetch;
  try {
    global.fetch = async () => new Response(null, { status: 302, headers: { Location: "https://other.test" } });
    await assert.rejects(server.boundedNasaFetch("https://gibs.earthdata.nasa.gov/test", "image/png", 100), { code: "NASA_REDIRECT_REJECTED" });
    global.fetch = async () => new Response("a", { headers: { "Content-Length": "101" } });
    await assert.rejects(server.boundedNasaFetch("https://gibs.earthdata.nasa.gov/test", "image/png", 100), { code: "NASA_RESPONSE_TOO_LARGE" });
  } finally { global.fetch = original; }
});

test("tile bytes reject false PNG content and oversized streamed body", async () => {
  const original = global.fetch;
  try {
    global.fetch = async () => new Response("not PNG", { headers: { "Content-Type": "image/png" } });
    await assert.rejects(server.soilTileBytes("surface", "2026-09-27", 6, 14, 24), { code: "NASA_INVALID_PNG" });
    const forged = new Uint8Array(33); forged.set([137,80,78,71,13,10,26,10], 0); forged.set([0,0,0,13,73,72,68,82], 8);
    global.fetch = async () => new Response(forged, { headers: { "Content-Type": "image/png" } });
    await assert.rejects(server.soilTileBytes("surface", "2026-09-27", 6, 14, 24), { code: "NASA_INVALID_PNG" });
    global.fetch = async () => new Response(new Uint8Array(1024 * 1024 + 1), { headers: { "Content-Type": "image/png" } });
    await assert.rejects(server.soilTileBytes("surface", "2026-09-27", 6, 14, 24), { code: "NASA_MALFORMED_OR_OVERSIZED" });
  } finally { global.fetch = original; }
});
