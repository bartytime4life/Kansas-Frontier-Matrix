import "./cloudflare-register.mjs";
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { pathToFileURL } from "node:url";
import test from "node:test";
import ts from "typescript";

// Compile the real route and its module graph to data URLs, as tests/kansas-discovery-layers.test.mjs does.
const dataModule = source => `data:text/javascript;base64,${Buffer.from(source).toString("base64")}`;
const NEXT_SERVER = dataModule(`export class NextRequest extends Request { get nextUrl() { return new URL(this.url); } }
export const NextResponse = { json: (body, init = {}) => Response.json(body, init) };`);
const modules = new Map();
async function moduleUrl(file) {
  file = path.resolve(file);
  if (modules.has(file)) return modules.get(file);
  let js = ts.transpileModule(await readFile(file, "utf8"), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
  for (const match of [...js.matchAll(/from ["']([^"']+)["']/g)]) {
    const specifier = match[1];
    const resolved = specifier.startsWith(".") ? await moduleUrl(path.resolve(path.dirname(file), specifier) + ".ts")
      : specifier.startsWith("cloudflare:") ? specifier : specifier === "next/server" ? NEXT_SERVER : import.meta.resolve(specifier, pathToFileURL(file).href);
    js = js.replace(match[0], `from ${JSON.stringify(resolved)}`);
  }
  const url = dataModule(js);
  modules.set(file, url); return url;
}
const route = await import(await moduleUrl("app/api/live-context/route.ts"));
const { NextRequest } = await import(NEXT_SERVER);
const bindings = globalThis.__KFM_TEST_BINDINGS ??= {};

const DAY = 86_400_000;
// One clock for the whole file, always moving forward, so each test starts past every earlier kept answer.
let clock = Date.parse("2026-11-22T12:00:00Z");
const realNow = Date.now;
test.before(() => { Date.now = () => clock; });
test.after(() => { Date.now = realNow; });

const place = (refnum, name, extra = {}) => ({ type: "Feature", geometry: { type: "Point", coordinates: [-95.68, 39.05] },
  properties: { NRIS_Refnum: refnum, RESNAME: name, ResType: "building", City: "Topeka", County: "Shawnee", CertDate: "1971-09-01", Is_NHL: null, NARA_URL: null, STATUS: "Listed", Vicinity: "False", ...extra } });
const places = (...features) => ({ type: "FeatureCollection", features });
/** Calls the feed with a stand-in provider: `upstream` is a body to answer with, or an HTTP status to fail with. */
async function call(query, upstream) {
  const original = globalThis.fetch;
  let reads = 0;
  globalThis.fetch = async () => { reads++; return typeof upstream === "number" ? new Response("unavailable", { status: upstream }) : new Response(JSON.stringify(upstream), { headers: { "Content-Type": "application/json" } }); };
  try {
    const response = await route.GET(new NextRequest(`http://127.0.0.1/api/live-context?${query}`));
    return { status: response.status, body: await response.json(), reads };
  } finally { globalThis.fetch = original; }
}
const names = body => body.data.features.map(feature => feature.properties.name);

test("a complete answer is kept for the lifetime the feed declares, with its original retrieval time", async () => {
  clock += 10 * DAY;
  const first = await call("feed=nps-nrhp-places", places(place("71000325", "Kansas State Capitol")));
  assert.equal(first.status, 200); assert.equal(first.body.state, "ready"); assert.ok(first.reads > 0);
  clock += DAY - 1;
  // The provider now says something else, but the day is not up: no read, same answer.
  const kept = await call("feed=nps-nrhp-places", places(place("66000340", "Fort Larned")));
  assert.equal(kept.reads, 0);
  assert.deepEqual(names(kept.body), ["Kansas State Capitol"]);
  assert.equal(kept.body.retrievedAt, first.body.retrievedAt);
  clock += 1;
  const fresh = await call("feed=nps-nrhp-places", places(place("66000340", "Fort Larned")));
  assert.ok(fresh.reads > 0, "after the declared day it is read again");
  assert.deepEqual(names(fresh.body), ["Fort Larned"]);
});

test("when the lifetime is up and the provider is down, the kept answer serves for the declared stale window, then the failure shows", async () => {
  clock += 10 * DAY;
  await call("feed=nps-nrhp-places", places(place("71000325", "Kansas State Capitol")));
  clock += DAY + 5;
  const stale = await call("feed=nps-nrhp-places", 503);
  assert.ok(stale.reads > 0, "the provider was asked");
  assert.equal(stale.status, 200);
  assert.deepEqual(names(stale.body), ["Kansas State Capitol"]);
  clock += DAY;
  const failed = await call("feed=nps-nrhp-places", 503);
  assert.equal(failed.status, 503);
  assert.equal(failed.body.state, "error");
  assert.equal(failed.body.fallback, "No fallback inference or substitute dataset was produced.");
});

test("a failure is never kept, and a feed with no answer yet fails as before", async () => {
  clock += 10 * DAY;
  const failed = await call("feed=nps-nrhp-places", 503);
  assert.equal(failed.status, 503);
  const recovered = await call("feed=nps-nrhp-places", places(place("71000325", "Kansas State Capitol")));
  assert.ok(recovered.reads > 0); assert.equal(recovered.status, 200);
  assert.deepEqual(names(recovered.body), ["Kansas State Capitol"]);
});

test("a partial answer is read again within five minutes rather than standing for a day", async () => {
  clock += 10 * DAY;
  // One record without a usable identifier is withheld, so the answer is partial.
  const partial = await call("feed=nps-nrhp-places", places(place("71000325", "Kansas State Capitol"), place("", "No identifier")));
  assert.equal(partial.body.state, "partial");
  clock += 299_000;
  assert.equal((await call("feed=nps-nrhp-places", places(place("66000340", "Fort Larned")))).reads, 0);
  clock += 1_000;
  const again = await call("feed=nps-nrhp-places", places(place("66000340", "Fort Larned")));
  assert.ok(again.reads > 0);
  assert.deepEqual(names(again.body), ["Fort Larned"]);
});

test("requests that arrive together share one provider read", async () => {
  clock += 10 * DAY;
  const original = globalThis.fetch;
  let reads = 0, release;
  const gate = new Promise(resolve => { release = resolve; });
  globalThis.fetch = async () => { reads++; await gate; return new Response(JSON.stringify(places(place("71000325", "Kansas State Capitol"))), { headers: { "Content-Type": "application/json" } }); };
  try {
    const both = [route.GET(new NextRequest("http://127.0.0.1/api/live-context?feed=nps-nrhp-places")), route.GET(new NextRequest("http://127.0.0.1/api/live-context?feed=nps-nrhp-places"))];
    await new Promise(resolve => setTimeout(resolve, 20));
    const during = reads;
    release();
    const [a, b] = await Promise.all(both);
    assert.equal(reads, during, "no further read after the first answered");
    const [one, two] = [await a.json(), await b.json()];
    assert.equal(one.retrievedAt, two.retrievedAt);
    // A single visitor's read of this feed makes this many provider requests; two visitors together made no more.
    clock += 10 * DAY;
    const alone = await call("feed=nps-nrhp-places", places(place("71000325", "Kansas State Capitol")));
    assert.equal(during, alone.reads);
  } finally { globalThis.fetch = original; }
});

test("dated archive requests, no-store feeds and the off switch read the provider every time", async () => {
  clock += 10 * DAY;
  const quakes = { type: "FeatureCollection", features: [] };
  assert.ok((await call("feed=usgs-earthquakes&day=2026-11-01", quakes)).reads > 0);
  assert.ok((await call("feed=usgs-earthquakes&day=2026-11-01", quakes)).reads > 0, "an archive day is not kept");
  assert.ok((await call("feed=usgs-earthquakes", quakes)).reads > 0);
  assert.equal((await call("feed=usgs-earthquakes", quakes)).reads, 0, "the present-day answer is kept for its five minutes");
  clock += 300_000;
  assert.ok((await call("feed=usgs-earthquakes", quakes)).reads > 0);
  bindings.KFM_LIVE_CONTEXT_KEEP = "off";
  try {
    assert.ok((await call("feed=usgs-earthquakes", quakes)).reads > 0, "with the switch off every request reads the provider");
    assert.ok((await call("feed=usgs-earthquakes", quakes)).reads > 0);
  } finally { delete bindings.KFM_LIVE_CONTEXT_KEEP; }
  const source = await readFile("app/api/live-context/route.ts", "utf8");
  assert.match(source, /"census-congress-119": 0, "deflock-alpr": 0/, "the two no-store feeds declare no lifetime, so they are never kept");
  assert.match(source, /cacheSeconds\[feed\] > 0 && feed !== "census-counties" && !isBridgeFeed\(feed\)/, "feeds that keep their own answers are left to do so");
});

test("the headers a kept answer goes out with are the ones the feed always declared", async () => {
  clock += 10 * DAY;
  const original = globalThis.fetch;
  globalThis.fetch = async () => new Response(JSON.stringify(places(place("71000325", "Kansas State Capitol"))), { headers: { "Content-Type": "application/json" } });
  try {
    const read = await route.GET(new NextRequest("http://127.0.0.1/api/live-context?feed=nps-nrhp-places"));
    const kept = await route.GET(new NextRequest("http://127.0.0.1/api/live-context?feed=nps-nrhp-places"));
    for (const header of ["Cache-Control", "X-KFM-Context-State", "X-Content-Type-Options"]) assert.equal(kept.headers.get(header), read.headers.get(header), header);
    assert.equal(kept.headers.get("Cache-Control"), "public, max-age=0, s-maxage=86400, stale-while-revalidate=86400");
  } finally { globalThis.fetch = original; }
});
