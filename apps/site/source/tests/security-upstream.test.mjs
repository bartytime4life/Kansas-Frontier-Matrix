import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import "./cloudflare-register.mjs";
import test from "node:test";
import ts from "typescript";

const noaaSource = await readFile(new URL("../app/api/hydrology/noaa/route.ts", import.meta.url), "utf8");
const shim = "data:text/javascript,export const NextResponse={json:(body,init)=>Response.json(body,init)}";
const noaaJavaScript = ts.transpileModule(noaaSource.replace('from "next/server"', `from "${shim}"`), {
  compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
}).outputText;
const { GET: noaaGet } = await import(`data:text/javascript;base64,${Buffer.from(noaaJavaScript).toString("base64")}`);

test("NOAA hydrology refuses redirects and retains the Kansas network response", async () => {
  const originalFetch = globalThis.fetch;
  const calls = [];
  const request = { nextUrl: new URL("http://localhost/api/hydrology/noaa?mode=network") };
  try {
    globalThis.fetch = async (input, init) => {
      calls.push(String(input));
      assert.equal(init.redirect, "manual");
      return new Response(null, { status: 302, headers: { location: "http://127.0.0.1/private" } });
    };
    const rejected = await noaaGet(request);
    assert.equal(rejected.status, 502);
    assert.equal((await rejected.json()).error.code, "NOAA_UPSTREAM_STATUS");
    assert.equal(calls.length, 1);

    globalThis.fetch = async (input, init) => {
      calls.push(String(input));
      assert.equal(init.redirect, "manual");
      return Response.json({ gauges: [] });
    };
    const accepted = await noaaGet(request);
    assert.equal(accepted.status, 200);
    const payload = await accepted.json();
    assert.equal(payload.mode, "network");
    assert.deepEqual(payload.records, []);
    assert.equal(calls.length, 2);
  } finally { globalThis.fetch = originalFetch; }
});

test("malformed NASA fire dates cannot reach an upstream", async () => {
  const workerUrl = new URL("../dist/server/index.js", import.meta.url);
  workerUrl.searchParams.set("test", `gibs-security-${process.pid}-${Date.now()}`);
  const { default: worker } = await import(workerUrl.href);
  const originalFetch = globalThis.fetch;
  let calls = 0;
  try {
    globalThis.fetch = async () => { calls++; throw new Error("Unexpected upstream request"); };
    const response = await worker.fetch(new Request("http://localhost/api/live-context?feed=nasa-gibs-fire-points&day=2026-09-26%2F..%2Fprivate"), {}, { waitUntil() {}, passThroughOnException() {} });
    assert.equal(response.status, 400);
    assert.equal(calls, 0);
  } finally { globalThis.fetch = originalFetch; }
});

test("current NASA fire points use only a labeled previous UTC day when new-day tiles are missing", async () => {
  const workerUrl = new URL("../dist/server/index.js", import.meta.url);
  workerUrl.searchParams.set("test", `gibs-day-boundary-${process.pid}-${Date.now()}`);
  const { default: worker } = await import(workerUrl.href);
  const originalFetch = globalThis.fetch;
  const today = new Date().toISOString().slice(0, 10);
  const yesterday = new Date(Date.parse(`${today}T00:00:00Z`) - 86_400_000).toISOString().slice(0, 10);
  const calls = [];
  const context = { waitUntil() {}, passThroughOnException() {} };
  try {
    globalThis.fetch = async (input) => {
      const url = String(input);
      calls.push(url);
      assert.match(url, /^https:\/\/gibs\.earthdata\.nasa\.gov\/wmts\/epsg4326\/best\//);
      if (url.includes(`/default/${today}/`)) return new Response("Not published", { status: 404 });
      if (url.includes(`/default/${yesterday}/`)) return new Response(new Uint8Array([0]), { headers: { "Content-Type": "application/octet-stream" } });
      throw new Error(`Unexpected NASA day in ${url}`);
    };
    const current = await worker.fetch(new Request("http://localhost/api/live-context?feed=nasa-gibs-fire-points"), {}, context);
    assert.equal(current.status, 200);
    const payload = await current.json();
    assert.equal(payload.state, "partial");
    assert.equal(payload.sourceDay, yesterday);
    assert.equal(payload.featureCount, 0);
    assert.match(payload.limitation, new RegExp(`current UTC day ${today} returned a missing tile`));
    assert.ok(calls.some((url) => url.includes(`/default/${today}/`)));
    assert.ok(calls.some((url) => url.includes(`/default/${yesterday}/`)));

    calls.length = 0;
    const download = await worker.fetch(new Request("http://localhost/api/source-download?source=nasa-gibs-fire-points"), {}, context);
    assert.equal(download.status, 200);
    assert.equal(download.headers.get("content-disposition"), `attachment; filename="kfm-nasa-gibs-fire-points-${yesterday}.geojson"`);
    const geojson = await download.json();
    assert.equal(geojson.kfm.sourceDay, yesterday);
    assert.equal(geojson.kfm.state, "partial");
    assert.equal(geojson.features.length, 0);

    calls.length = 0;
    const archivedDownload = await worker.fetch(new Request(`http://localhost/api/source-download?source=nasa-gibs-fire-points&day=${yesterday}`), {}, context);
    assert.equal(archivedDownload.status, 200);
    assert.equal(archivedDownload.headers.get("content-disposition"), `attachment; filename="kfm-nasa-gibs-fire-points-${yesterday}.geojson"`);
    const archiveGeojson = await archivedDownload.json();
    assert.equal(archiveGeojson.kfm.requestedDay, yesterday);
    assert.equal(archiveGeojson.kfm.sourceDay, yesterday);
    assert.equal(archiveGeojson.kfm.state, "empty");
    assert.ok(calls.length > 0 && calls.every((url) => url.includes(`/default/${yesterday}/`)));

    calls.length = 0;
    for (const query of [`source=census-counties&day=${yesterday}`, "source=nasa-gibs-fire-points&day=2026-02-30", `source=nasa-gibs-fire-points&day=${yesterday}&day=${today}`, "source=nasa-gibs-fire-points&day=9999-01-01"]) {
      const rejected = await worker.fetch(new Request(`http://localhost/api/source-download?${query}`), {}, context);
      assert.equal(rejected.status, 400, query);
    }
    assert.deepEqual(calls, []);

    calls.length = 0;
    const exact = await worker.fetch(new Request(`http://localhost/api/live-context?feed=nasa-gibs-fire-points&day=${today}`), {}, context);
    assert.equal(exact.status, 502);
    assert.ok(calls.length > 0 && calls.every((url) => url.includes(`/default/${today}/`)));
  } finally { globalThis.fetch = originalFetch; }
});

test("NOAA hydrology resolves only named endpoints from validated identifiers", async () => {
  const originalFetch = globalThis.fetch;
  const calls = [];
  globalThis.fetch = async (input, init) => {
    calls.push(String(input));
    assert.equal(init.redirect, "manual");
    return Response.json({});
  };
  const request = (query) => ({ nextUrl: new URL(`http://localhost/api/hydrology/noaa?${query}`) });
  try {
    for (const query of ["mode=gauge&lid=ABC%2F..%2Fprivate", "mode=gauge&lid=ABC%40evil.test", "mode=reach&reach=12%2F..%2Fprivate"]) {
      assert.equal((await noaaGet(request(query))).status, 400);
    }
    assert.deepEqual(calls, []);
    await noaaGet(request("mode=gauge&lid=ABCD"));
    assert.deepEqual(calls.splice(0), [
      "https://api.water.noaa.gov/nwps/v1/gauges/ABCD",
      "https://api.water.noaa.gov/nwps/v1/gauges/ABCD/stageflow/observed",
      "https://api.water.noaa.gov/nwps/v1/gauges/ABCD/stageflow/forecast",
    ]);
    await noaaGet(request("mode=reach&reach=12345"));
    assert.deepEqual(calls, [
      "https://api.water.noaa.gov/nwps/v1/reaches/12345/streamflow?series=analysis_assimilation",
      "https://api.water.noaa.gov/nwps/v1/reaches/12345/streamflow?series=short_range",
    ]);
  } finally { globalThis.fetch = originalFetch; }
});
