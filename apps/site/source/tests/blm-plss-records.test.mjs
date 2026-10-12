import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import ts from "typescript";

const modules = new Map();
async function load(file) {
  file = path.resolve(file); if (modules.has(file)) return modules.get(file);
  let js = ts.transpileModule(await readFile(file, "utf8"), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
  for (const match of [...js.matchAll(/from ["'](\.[^"']+)["']/g)]) js = js.replace(match[0], `from ${JSON.stringify(await load(path.resolve(path.dirname(file), match[1]) + ".ts"))}`);
  const url = `data:text/javascript;base64,${Buffer.from(js).toString("base64")}`; modules.set(file, url); return url;
}
const blm = await import(await load("app/blm-plss-records.ts"));
const route = await import(await load("app/api/blm-plss-records/route.ts"));
const query = { layer: "blm-plss-sections", longitude: -97.3361, latitude: 37.6922 };
const request = params => new Request(`http://localhost/api/blm-plss-records?${new URLSearchParams(params)}`);
const feature = (attributes = {}) => ({ attributes: { OBJECTID: 1443392, PLSSID: "KS060270S0010E0", FRSTDIVID: "KS060270S0010E0SN20", FRSTDIVTXT: "Section", FRSTDIVLAB: "20", SOURCEDATE: Date.UTC(1908, 0, 1), ...attributes } });
const body = (features = [feature()], extra = {}) => ({ features, geometryType: "esriGeometryPolygon", ...extra });

test("BLM point inspection uses only the displayed Kansas layer filters and fixed provider fields", async () => {
  const displayed = await readFile("app/live-context.ts", "utf8");
  for (const [id, profile] of Object.entries(blm.BLM_PLSS_LAYERS)) {
    const url = new URL(blm.blmPlssProviderUrl({ ...query, layer: id }));
    assert.equal(url.origin, "https://gis.blm.gov");
    assert.equal(url.pathname.endsWith(`/${profile.layer}/query`), true);
    assert.equal(url.searchParams.get("where"), profile.where);
    assert.equal(url.searchParams.get("outFields"), profile.fields);
    assert.equal(url.searchParams.get("returnGeometry"), "false");
    assert.equal(url.searchParams.get("resultRecordCount"), "10");
    assert.equal(url.searchParams.get("orderByFields"), "OBJECTID");
    assert.ok(displayed.includes(`blmPlssImageUrl(${profile.layer}, "${profile.where}")`));
    const count = new URL(blm.blmPlssProviderUrl({ ...query, layer: id }, true));
    assert.equal(count.searchParams.get("where"), profile.where);
    assert.equal(count.searchParams.get("returnCountOnly"), "true");
    assert.equal(count.searchParams.get("outFields"), null);
  }
});
test("PLSS query rejects out-of-state points, arbitrary provider inputs and duplicate parameters", async () => {
  assert.deepEqual(blm.parseBlmPlssQuery(request(query).url), query);
  for (const params of [{ ...query, latitude: 36 }, { ...query, layer: "__proto__" }, { ...query, url: "http://127.0.0.1/" }, { ...query, where: "1=1" }, { ...query, longitude: "Infinity" }]) {
    assert.throws(() => blm.parseBlmPlssQuery(request(params).url));
    assert.equal((await route.GET(request(params))).status, 400);
  }
  assert.throws(() => blm.parseBlmPlssQuery(request(query).url + "&layer=blm-plss-townships"));
});
test("PLSS records preserve separate identifiers and source dates without implying title", () => {
  const section = blm.parseBlmPlssRecords(body(), query, 1);
  assert.equal(section.state, "ready"); assert.equal(section.role, "EXTERNAL_CONTEXT_ONLY");
  assert.equal(section.records[0].plssId, "KS060270S0010E0");
  assert.equal(section.records[0].firstDivisionId, "KS060270S0010E0SN20");
  assert.equal(section.records[0].sourceDocumentDate, "1908-01-01");
  assert.equal(section.records[0].revisedDate, null);
  assert.match(section.records[0].officialRecordUrl, /objectIds=1443392&/);
  const township = blm.parseBlmPlssRecords(body([feature({ STATEABBR: "KS", TWNSHPLAB: "T27S R1E", PRINMER: "6th Meridian" })]), { ...query, layer: "blm-plss-townships" }, 1);
  assert.equal(township.records[0].townshipLabel, "T27S R1E");
  const intersected = blm.parseBlmPlssRecords(body([feature({ STATEABBR: "KS", SECDIVID: "KS-SECOND", SECDIVTXT: "Government lot", SECDIVLAB: "Lot 1", REVISEDDATE: Date.UTC(2020, 0, 2) })]), { ...query, layer: "blm-plss-intersected" }, 1);
  assert.equal(intersected.records[0].secondDivisionLabel, "Lot 1");
  assert.equal(intersected.records[0].revisedDate, "2020-01-02");
  assert.equal(blm.parseBlmPlssRecords({ features: [] }, query, 0).state, "empty");
});
test("GLO handoff copies bounded survey search context without claiming a document match", async () => {
  const section = blm.parseBlmPlssRecords(body(), query, 1).records[0];
  assert.equal(blm.gloSearchReference(section, query),
    "Kansas | BLM PLSS township ID: KS060270S0010E0 | BLM section: 20 | Map center: 37.69220, -97.33610");
  const township = blm.parseBlmPlssRecords(body([feature({ STATEABBR: "KS", TWNSHPLAB: "T27S R1E", PRINMER: "6th Meridian" })]), { ...query, layer: "blm-plss-townships" }, 1).records[0];
  assert.match(blm.gloSearchReference(township, query), /BLM township label: T27S R1E \| Principal meridian: 6th Meridian/);
  assert.equal(blm.gloSearchReference({ ...section, plssId: "OK060270S0010E0" }, query), null);
  assert.equal(blm.gloSearchReference(section, { ...query, longitude: -103 }), null);
  assert.doesNotMatch(blm.gloSearchReference({ ...section, firstDivisionLabel: "20\nMatched patent" }, query), /Matched patent|BLM section/);
  assert.doesNotMatch(blm.gloSearchReference({ ...section, firstDivisionType: "Tract" }, query), /BLM section/);
  const inspector = await readFile("app/blm-plss-inspector.tsx", "utf8");
  assert.match(inspector, /BLM survey feature attributes/);
  assert.match(inspector, /no GLO document has been matched or reviewed/i);
  assert.doesNotMatch(inspector, /Official BLM record/);
});
test("BLM malformed counts, duplicate identities and inconsistent responses fail closed or disclose partial", () => {
  for (const invalid of [{ error: { code: 500 } }, { count: -1 }, { count: "1" }, { count: 1.5 }]) assert.throws(() => blm.parseBlmPlssCount(invalid));
  assert.equal(blm.parseBlmPlssCount({ count: 2 }), 2);
  assert.equal(blm.parseBlmPlssRecords(body([feature({ PLSSID: "OK123" })]), query, 1).state, "partial");
  assert.equal(blm.parseBlmPlssRecords(body([feature()]), query, 2).state, "partial");
  assert.equal(blm.parseBlmPlssRecords(body(Array.from({ length: 10 }, (_, i) => feature({ OBJECTID: i + 1 }))), query, 11).state, "partial");
  for (const invalid of [{ error: { code: 400 } }, {}, body([feature(), feature()]), body([feature({ PLSSID: "OK123", STATEABBR: "OK" })], { exceededTransferLimit: true }), body([feature()], { geometryType: "esriGeometryPoint" }), body([feature()], { exceededTransferLimit: "false" })]) assert.throws(() => blm.parseBlmPlssRecords(invalid, query, 1));
  assert.throws(() => blm.parseBlmPlssRecords(body([feature()]), query, 0));
});
test("BLM route keeps a bounded count and record read and withholds upstream failures", async () => {
  const original = globalThis.fetch;
  try {
    const calls = [];
    globalThis.fetch = async (url, options) => {
      assert.equal(options.redirect, "manual");
      const params = new URL(url).searchParams; calls.push(params.has("returnCountOnly") ? "count" : "features");
      return Response.json(params.has("returnCountOnly") ? { count: 1 } : body());
    };
    const response = await route.GET(request(query)), result = await response.json();
    assert.equal(response.status, 200); assert.deepEqual(calls, ["count", "features"]);
    assert.equal(response.headers.get("cache-control"), "no-store");
    assert.equal(result.records.length, 1); assert.equal(result.partial, false);
    globalThis.fetch = async url => new URL(url).searchParams.has("returnCountOnly") ? Response.json({ count: 0 }) : assert.fail("empty count requested records");
    assert.equal((await (await route.GET(request(query))).json()).state, "empty");
    for (const bad of [Response.json({ error: { message: "provider secret" } }), new Response(null, { status: 302, headers: { Location: "http://127.0.0.1/" } }), new Response("x".repeat(4097))]) {
      globalThis.fetch = async () => bad;
      const result = await route.GET(request(query)); assert.equal(result.status, 502);
      assert.equal((await result.text()).includes("provider secret"), false);
    }
    const controller = new AbortController(); controller.abort(); globalThis.fetch = () => assert.fail("aborted request reached BLM");
    assert.equal((await route.GET(new Request(request(query), { signal: controller.signal }))).status, 502);
  } finally { globalThis.fetch = original; }
});
