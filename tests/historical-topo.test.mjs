import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

async function compile(path, imports = {}) {
  const source = await readFile(new URL(`../app/${path}.ts`, import.meta.url), "utf8");
  const code = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 } }).outputText;
  const compiledModule = { exports: {} };
  new Function("require", "module", "exports", code)((key) => imports[key], compiledModule, compiledModule.exports);
  return compiledModule.exports;
}

const topo = await compile("historical-topo");
const request = "https://site.example/api/historical-topo?lng=-95.68&lat=39.05&from=1880&through=1960&scale=125000&name=Topeka&offset=0";
const record = { attributes: { OBJECTID: 4628, map_scale: 125000, map_name: "Topeka", primary_state: "KS", date_on_map: 1889, imprint_year: 1891, scan_id: 122705, series: "HTMC", datum: "NAD27" }, geometry: { rings: [[[-95.8, 39], [-95.8, 39.2], [-95.6, 39.2], [-95.6, 39], [-95.8, 39]]] } };

test("historical sheet search binds the official catalog to a bounded place, edition range, and scale", () => {
  const search = topo.parseTopoSearch(request);
  const url = new URL(topo.topoProviderUrl(search));
  assert.equal(url.origin, "https://ngmdb.usgs.gov");
  assert.equal(url.searchParams.get("resultRecordCount"), "24");
  assert.equal(url.searchParams.get("returnGeometry"), "true");
  assert.match(url.searchParams.get("where"), /^primary_state = 'KS' AND date_on_map >= 1880 AND date_on_map <= 1960 AND map_scale = 125000 AND map_name LIKE '%Topeka%'$/);
  const bounds = url.searchParams.get("geometry").split(",").map(Number);
  assert.deepEqual(bounds.map(value => Number(value.toFixed(2))), [-96.33, 38.6, -95.03, 39.5]);
});

test("historical sheet query rejects extra keys, unsafe names, and out-of-region searches", () => {
  assert.throws(() => topo.parseTopoSearch(`${request}&server=https://evil.example`));
  assert.throws(() => topo.parseTopoSearch(request.replace("Topeka", "Topeka%25")));
  assert.throws(() => topo.parseTopoSearch(request.replace("lng=-95.68", "lng=0")));
  assert.throws(() => topo.parseTopoSearch(request.replace("from=1880", "from=1970")));
});

test("catalog parsing preserves actual footprint, scan identity, and distinct edition and imprint years", () => {
  const parsed = topo.parseTopoCatalog({ features: [record], exceededTransferLimit: false });
  assert.equal(parsed.more, false);
  assert.equal(parsed.sheets[0].year, 1889);
  assert.equal(parsed.sheets[0].imprintYear, 1891);
  assert.equal(parsed.sheets[0].scanId, 122705);
  assert.deepEqual(parsed.sheets[0].footprint.geometry.coordinates, record.geometry.rings);
  assert.equal(parsed.sheets[0].viewerHref, "https://ngmdb.usgs.gov/topoview/viewer/#12/39.10000/-95.70000");
  assert.deepEqual(topo.parseTopoCatalog({ features: [{ ...record, geometry: { rings: [[[999, 0], [1, 1], [2, 2], [999, 0]]] } }] }).sheets, []);
});

test("Oklahoma and unlabeled sheets cannot enter Kansas results even if the provider ignores its state filter", () => {
  const oklahoma = { ...record, attributes: { ...record.attributes, OBJECTID: 4629, map_name: "Enid", primary_state: "OK" } };
  const unlabeled = { ...record, attributes: { ...record.attributes, OBJECTID: 4630, primary_state: null } };
  const mixed = topo.parseTopoCatalog({ features: [oklahoma, record, unlabeled], exceededTransferLimit: false });
  assert.deepEqual(mixed.sheets.map(sheet => [sheet.name, sheet.state]), [["Topeka", "KS"]]);
  assert.deepEqual(topo.parseTopoCatalog({ features: [oklahoma], exceededTransferLimit: false }).sheets, []);
});

test("the route returns external context and fails closed when USGS is unavailable", async () => {
  const foreign = { ...record, attributes: { ...record.attributes, OBJECTID: 4629, map_name: "Enid", primary_state: "OK" } };
  let providerUrl = "";
  const route = await compile("api/historical-topo/route", {
    "../event-atlas/upstream": { boundedFetch: async (url) => { providerUrl = url; return { text: () => JSON.stringify({ features: [foreign, record], exceededTransferLimit: false }) }; } },
    "../../historical-topo": topo,
  });
  const response = await route.GET(new Request(request));
  const body = await response.json();
  assert.equal(response.status, 200);
  assert.equal(body.role, "EXTERNAL_CONTEXT_ONLY");
  assert.equal(body.sheets.length, 1);
  assert.equal(body.sheets[0].state, "KS");
  assert.match(new URL(providerUrl).searchParams.get("where"), /primary_state = 'KS'/);
  assert.match(body.note, /No scanned raster/);
  const invalid = await route.GET(new Request(`${request}&bad=1`));
  assert.equal(invalid.status, 400);

  const unavailable = await compile("api/historical-topo/route", {
    "../event-atlas/upstream": { boundedFetch: async () => { throw new Error("provider down"); } },
    "../../historical-topo": topo,
  });
  const failure = await unavailable.GET(new Request(request));
  assert.equal(failure.status, 502);
  assert.deepEqual((await failure.json()).sheets, []);
});
