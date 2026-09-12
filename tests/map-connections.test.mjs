import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import ts from "typescript";

const modules = new Map();
async function moduleUrl(file) {
  file = path.resolve(file);
  if (modules.has(file)) return modules.get(file);
  let source = await readFile(file, "utf8");
  source = source.replace(/import \{ NextRequest, NextResponse \} from "next\/server";/, "const NextResponse = { json: (body, init) => new Response(JSON.stringify(body), init) };");
  for (const match of [...source.matchAll(/from ["'](\.[^"']+)["']/g)]) {
    const replacement = await moduleUrl(path.resolve(path.dirname(file), match[1]) + ".ts");
    source = source.replace(match[0], `from ${JSON.stringify(replacement)}`);
  }
  const js = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
  const url = `data:text/javascript;base64,${Buffer.from(js).toString("base64")}`;
  modules.set(file, url); return url;
}
const atlas = await import(await moduleUrl("app/event-atlas.ts"));
const coverage = await import(await moduleUrl("app/api/hydrology/coverage/route.ts"));
const counties = await import(await moduleUrl("app/api/event-atlas/counties/route.ts"));
const weather = await import(await moduleUrl("app/api/event-atlas/weather/route.ts"));
const mock = async (response, work) => { const original = globalThis.fetch; globalThis.fetch = async () => Response.json(response); try { await work(); } finally { globalThis.fetch = original; } };

test("24-hour playback preserves empty nineteenth-century days and rejects undefined flow as coverage", () => {
  const manifest = { start: "1880-01-01T00:00:00.000Z", end: "1880-01-02T00:00:00.000Z", radar: { scans: [] }, smoke: { data: { features: [] } } };
  assert.equal(atlas.eventFrames(manifest).length, 24);
  assert.equal(atlas.eventFrames(manifest).at(-1), "1880-01-01T23:00:00.000Z");
  assert.equal(atlas.eventHourAvailability(manifest, [{ observedAt: manifest.start }]).some((hour) => hour.supported), false);
});

test("river coverage separates daily means from instantaneous records and excludes annual peaks", async () => {
  const station = "USGS-06889000";
  const row = (patch) => ({ properties: { monitoring_location_id: station, parameter_code: "00060", begin: "1917-06-12T06:00:00+00:00", end: "2026-01-01T06:00:00+00:00", ...patch } });
  await mock({ type: "FeatureCollection", features: [row({ computation_period_identifier: "Daily", statistic_id: "00003" }), row({ computation_period_identifier: "Water Year", statistic_id: null, begin: "1869-01-01T06:00:00+00:00" })] }, async () => {
    const result = await coverage.GET(new Request(`https://example.test/?station=${station}`));
    const body = await result.json(); assert.equal(result.status, 200); assert.equal(body.daily.start, "1917-06-12T06:00:00.000Z"); assert.equal(body.continuous, null);
  });
  await mock({ type: "FeatureCollection", features: [row({ monitoring_location_id: "USGS-99999999" })] }, async () => assert.equal((await coverage.GET(new Request(`https://example.test/?station=${station}`))).status, 502));
});

test("county baseline requires 105 distinct Kansas counties and preserves missing population", async () => {
  const features = Array.from({ length: 105 }, (_, i) => ({ geometry: { type: "Polygon", coordinates: [[[-99,38],[-98,38],[-98,39],[-99,38]]] }, properties: { GEOID: `20${String(i * 2 + 1).padStart(3,"0")}`, BASENAME: `County ${i}`, POP100: i ? 100 : null, HU100: 40, AREALAND: 2589988.110336, AREAWATER: 0 } }));
  await mock({ type: "FeatureCollection", features }, async () => {
    const result = await counties.GET(new Request("https://example.test/?edition=2010")), data = await result.json();
    assert.equal(result.status, 200); assert.equal(data.data.features[0].properties.population, null); assert.equal(data.data.features[1].properties.landSquareMiles, 1); assert.equal(data.edition, "2010");
  });
  await mock({ type: "FeatureCollection", features: features.slice(1) }, async () => assert.equal((await counties.GET(new Request("https://example.test/?edition=2020"))).status, 502));
  await mock({ type: "FeatureCollection", features: features.map((f) => ({ ...f, properties: { ...f.properties, GEOID: "20001" } })) }, async () => assert.equal((await counties.GET(new Request("https://example.test/?edition=2020"))).status, 502));
});

test("NOAA keeps real zero rain, withholds quality-flagged values, and rejects wrong-day records", async () => {
  const row = { DATE: "1900-05-19", STATION: "USC00143527", LATITUDE: "38.85", LONGITUDE: "-99.3", TMAX: "70", TMAX_ATTRIBUTES: ",X,0", TMIN: "44", PRCP: "0.00", PRCP_ATTRIBUTES: ",,0" };
  await mock([row], async () => {
    const result = await weather.GET(new Request("https://example.test/?day=1900-05-19")), body = await result.json();
    assert.equal(result.status, 200); assert.equal(body.data.features[0].properties.maximumF, null); assert.equal(body.data.features[0].properties.precipitationInches, 0);
  });
  await mock([{ ...row, DATE: "1900-05-20" }], async () => assert.equal((await weather.GET(new Request("https://example.test/?day=1900-05-19"))).status, 502));
  assert.equal((await weather.GET(new Request("https://example.test/?day=1900-02-29"))).status, 400);
});
