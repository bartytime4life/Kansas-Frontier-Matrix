import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import ts from "typescript";
import test from "node:test";
const cache = new Map();
async function moduleUrl(file) {
  file = path.resolve(file); if (cache.has(file)) return cache.get(file);
  let js = ts.transpileModule(await readFile(file, "utf8"), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
  for (const match of [...js.matchAll(/from ["'](\.[^"']+)["']/g)]) js = js.replace(match[0], `from ${JSON.stringify(await moduleUrl(path.resolve(path.dirname(file), match[1]) + ".ts"))}`);
  const url = `data:text/javascript;base64,${Buffer.from(js).toString("base64")}`; cache.set(file,url); return url;
}
const intake = await import(await moduleUrl("app/data-intake.ts"));
const daily = await import(await moduleUrl("app/daily-baseline.ts"));
const upstream = await import(await moduleUrl("app/api/event-atlas/upstream.ts"));
const eventAtlas = await import(await moduleUrl("app/event-atlas.ts"));
test("intake rejects malformed dates, credential URLs, duplicate file paths and unsupported payloads", () => {
  const fields = { title: "A real source", sourceId: "general", sourceUrl: "https://example.gov/data", description: "Historical public county records", license: "Unknown", sensitivity: "unknown", startDate: "1900-01-01", endDate: "1900-12-31" };
  assert.equal(intake.validateSubmission(fields).startDate, "1900-01-01");
  assert.throws(() => intake.validateSubmission({...fields,startDate:"1900-02-29"}));
  assert.throws(() => intake.validateSubmission({...fields,sourceUrl:"https://user:secret@example.gov"}));
  assert.throws(() => intake.validateUpload("../../data.csv",50));
  assert.throws(() => intake.validateUpload("script.js",50));
  assert.throws(() => intake.validateUpload("data.csv",intake.MAX_UPLOAD_BYTES+1));
  assert.throws(() => intake.validateReview({...fields,status:"submitted"},"accepted","Checked provider terms and data structure."));
});
test("daily baseline advances across midnight and year boundaries without replacing historical stacks", () => {
  assert.equal(daily.currentDayStart(new Date("2026-12-31T23:59:00Z")),"2026-12-31T00:00");
  assert.equal(daily.currentDayStart(new Date("2027-01-01T00:01:00Z")),"2027-01-01T00:00");
  assert.deepEqual(daily.BASELINE_STACKS.overview,["census-counties","usgs-streamflow","usgs-3dhp-hydrography"]);
  assert.equal(daily.BASELINE_STACKS.history,undefined);
});
test("provider redirects are rejected without using the redirect mode unsupported by Workers", async () => {
  const original = globalThis.fetch; let calls = 0;
  globalThis.fetch = async (_url, init) => { calls++; assert.equal(init.redirect,"manual"); return new Response(null,{status:302,headers:{Location:"https://untrusted.test/data"}}); };
  try { await assert.rejects(upstream.boundedFetch("https://tigerweb.geo.census.gov/query",1000),/HTTP 302/); assert.equal(calls,1); }
  finally { globalThis.fetch = original; }
});

test("bounded upstream requests use only approved HTTPS origins and the validated URL", async () => {
  const original = globalThis.fetch;
  const calls = [];
  globalThis.fetch = async (input, init) => {
    calls.push(String(input));
    assert.equal(init.redirect, "manual");
    return new Response("ok");
  };
  try {
    for (const url of [
      "http://tigerweb.geo.census.gov/query",
      "https://tigerweb.geo.census.gov:8443/query",
      "https://user@tigerweb.geo.census.gov/query",
      "https://tigerweb.geo.census.gov.evil.test/query",
      "https://tigerweb.geo.census.gov/query#fragment",
    ]) await assert.rejects(upstream.boundedFetch(url, 1000), /Non-allowlisted source/);
    assert.equal(calls.length, 0);
    const result = await upstream.boundedFetch("https://tigerweb.geo.census.gov/query?state=20", 1000);
    assert.equal(result.text(), "ok");
    assert.deepEqual(calls, ["https://tigerweb.geo.census.gov/query?state=20"]);
  } finally { globalThis.fetch = original; }
});

test("bounded upstream responses preserve empty tiles and reject oversized bodies", async () => {
  const original = globalThis.fetch;
  try {
    globalThis.fetch = async () => new Response(null, { status: 204 });
    const empty = await upstream.boundedFetch("https://gibs.earthdata.nasa.gov/tile", 1000);
    assert.equal(empty.bytes.length, 0);
    globalThis.fetch = async () => new Response("too large", { headers: { "content-length": "1001" } });
    await assert.rejects(upstream.boundedFetch("https://gibs.earthdata.nasa.gov/tile", 1000), /response budget/);
  } finally { globalThis.fetch = original; }
});

test("rejected upstream responses cancel their unread bodies", async () => {
  const original = globalThis.fetch;
  try {
    for (const init of [
      { status: 302, headers: { Location: "https://untrusted.test/data" } },
      { headers: { "Content-Length": "1001" } },
    ]) {
      let canceled = false;
      const response = new Response(new ReadableStream({ cancel() { canceled = true; } }), init);
      globalThis.fetch = async () => response;
      await assert.rejects(upstream.boundedFetch("https://tigerweb.geo.census.gov/query", 1000), /HTTP 302|response budget/);
      assert.equal(canceled, true);
      assert.equal(response.body.locked, false);
    }
  } finally { globalThis.fetch = original; }
});

test("streamed upstream bodies cancel at the byte cap and release their reader", async () => {
  const original = globalThis.fetch;
  let canceled = false;
  let pulls = 0;
  const response = new Response(new ReadableStream({
    pull(controller) { pulls++; controller.enqueue(new Uint8Array(600)); },
    cancel() { canceled = true; },
  }));
  globalThis.fetch = async () => response;
  try {
    await assert.rejects(upstream.boundedFetch("https://tigerweb.geo.census.gov/query", 1000), /response budget/);
    assert.equal(canceled, true);
    assert.ok(pulls <= 3);
    assert.equal(response.body.locked, false);
  } finally { globalThis.fetch = original; }
});

test("caller abort after upstream headers cancels a stalled body without returning partial bytes", { timeout: 1000 }, async () => {
  const original = globalThis.fetch;
  const controller = new AbortController();
  const reason = new DOMException("The viewer canceled the request.", "AbortError");
  let reading;
  const started = new Promise(resolve => { reading = resolve; });
  let cancelReason;
  let pulls = 0;
  const response = new Response(new ReadableStream({
    pull(stream) {
      if (pulls++ === 0) stream.enqueue(new TextEncoder().encode("incomplete payload"));
      else reading();
    },
    cancel(value) { cancelReason = value; },
  }));
  globalThis.fetch = async () => response;
  try {
    const pending = upstream.boundedFetch("https://tigerweb.geo.census.gov/query", 1000, { signal: controller.signal });
    await started;
    assert.equal(response.body.locked, true);
    controller.abort(reason);
    await assert.rejects(pending, error => error === reason);
    assert.equal(cancelReason, reason);
    assert.equal(response.body.locked, false);
  } finally { globalThis.fetch = original; }
});

test("upstream timeout after headers cancels a stalled body", { timeout: 1000 }, async () => {
  const original = globalThis.fetch;
  let canceled = false;
  const response = new Response(new ReadableStream({ cancel() { canceled = true; } }));
  globalThis.fetch = async () => response;
  try {
    await assert.rejects(upstream.boundedFetch("https://tigerweb.geo.census.gov/query", 1000, { timeoutMs: 15 }), { name: "AbortError" });
    assert.equal(canceled, true);
    assert.equal(response.body.locked, false);
  } finally { globalThis.fetch = original; }
});

test("successful upstream reads preserve their bytes and release their reader", async () => {
  const original = globalThis.fetch;
  const response = new Response("Kansas · 水", { headers: { "X-Source": "fixture" } });
  globalThis.fetch = async () => response;
  try {
    const result = await upstream.boundedFetch("https://tigerweb.geo.census.gov/query", 1000);
    assert.deepEqual(result.bytes, new TextEncoder().encode("Kansas · 水"));
    assert.equal(result.text(), "Kansas · 水");
    assert.equal(result.headers.get("X-Source"), "fixture");
    assert.equal(response.body.locked, false);
  } finally { globalThis.fetch = original; }
});

test("NOAA smoke archive paths accept only exact calendar days", () => {
  assert.equal(eventAtlas.smokeUrl("2026-09-26"), "https://satepsanone.nesdis.noaa.gov/pub/FIRE/web/HMS/Smoke_Polygons/KML/2026/09/hms_smoke20260926.kml");
  for (const day of ["2026-02-30", "2026-09-26/../../private", "2026-09-26%2Fprivate", "//other.test"]) {
    assert.throws(() => eventAtlas.smokeUrl(day), /exact calendar date/);
  }
});
