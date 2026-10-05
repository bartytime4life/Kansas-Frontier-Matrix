import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { pathToFileURL } from "node:url";
import test from "node:test";
import ts from "typescript";
async function compile(file) {
  let js = ts.transpileModule(await readFile(file, "utf8"), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
  for (const match of [...js.matchAll(/from "(\.[^"]+)"/g)]) js = js.replace(match[0], `from ${JSON.stringify(await compile(path.resolve(path.dirname(file), match[1]) + ".ts"))}`);
  js = js.replace('from "next/server"', `from ${JSON.stringify(pathToFileURL(path.resolve("node_modules/next/server.js")).href)}`);
  return `data:text/javascript;base64,${Buffer.from(js).toString("base64")}`;
}
const { GET } = await import(await compile("app/api/hydrology/direction/route.ts"));
const { parseDownstreamGuide, readProgressiveDownstreamGuide } = await import(await compile("app/water-flow-context.ts"));
const request = (suffix = "lon=-97.995&lat=38") => ({ nextUrl: new URL(`https://local/api/hydrology/direction?${suffix}`), signal: new AbortController().signal });
const feature = (id, sequence, downstream, coordinates, featuretype = 1) => ({ properties: { id3dhp: id, hydrosequence: sequence, dnhydrosequence: downstream, levelpath: 10, flowdirection: 1, featuretype, gnisidlabel: "Fixture river" }, geometry: { type: "LineString", coordinates } });
const first = feature("A", 30, 20, [[-98, 38], [-97.99, 38]]);
const second = feature("B", 20, null, [[-97.99, 38], [-97.98, 38]], 5);

test("direction route expands the same river and returns derived elevations with connector disclosure", async () => {
  const original = globalThis.fetch; let calls = 0;
  globalThis.fetch = async url => {
    calls++; const u = new URL(url);
    if (u.hostname === "3dhp.nationalmap.gov") return Response.json({ features: u.searchParams.get("distance") === "1200" ? [first] : [first, second] });
    assert.equal(u.hostname, "elevation.nationalmap.gov");
    assert.deepEqual(JSON.parse(u.searchParams.get("renderingRule")), { rasterFunction: "None" });
    const points = JSON.parse(u.searchParams.get("geometry")).points;
    return Response.json({ samples: points.map((p, i) => ({ locationId: i, location: { x: p[0], y: p[1], spatialReference: { wkid: 4326 } }, value: String(500 - i), resolution: 1, attributes: { VerticalDatum: "NAVD88" } })) });
  };
  try {
    const response = await GET(request()); assert.equal(response.status, 200);
    const guide = parseDownstreamGuide(await response.json());
    assert.equal(guide.format, "kfm-3dhp-direction-v2"); assert.equal(calls, 3);
    assert.equal(guide.analysis.segments, 2); assert.equal(guide.analysis.connectors, 1); assert.equal(guide.paths[0].hasConnectors, true);
    assert.equal(guide.analysis.elevation.dropM, 24); assert.equal(guide.analysis.elevation.samples.length, 25);
  } finally { globalThis.fetch = original; }
});

test("elevation failure keeps mapped direction but never invents a terrain value", async () => {
  const original = globalThis.fetch;
  globalThis.fetch = async url => new URL(url).hostname === "3dhp.nationalmap.gov" ? Response.json({ features: [first, second] }) : new Response("unavailable", { status: 503 });
  try {
    const response = await GET(request()); const guide = parseDownstreamGuide(await response.json());
    assert.equal(guide.state, "ready"); assert.equal(guide.analysis.elevation.state, "unavailable");
    assert.equal(guide.analysis.elevation.dropM, null); assert.equal(guide.analysis.elevation.slopePercent, null);
  } finally { globalThis.fetch = original; }
});

test("truncated gauge search remains unavailable, and invalid coordinates do not call upstream", async () => {
  const original = globalThis.fetch; let calls = 0;
  globalThis.fetch = async () => { calls++; return Response.json({ features: [first], exceededTransferLimit: true }); };
  try {
    assert.equal((await GET(request())).status, 503); assert.equal(calls, 1);
    assert.equal((await GET(request("lon=0&lat=0"))).status, 400); assert.equal(calls, 1);
    assert.equal((await GET(request("lon=-98&lon=-97&lat=38"))).status, 400); assert.equal(calls, 1);
  } finally { globalThis.fetch = original; }
});

test("a nearby mapped segment arrives before the slow extension, then the full terrain-backed path replaces it", async () => {
  const original = globalThis.fetch;
  let releaseExtension;
  const extension = new Promise(resolve => { releaseExtension = resolve; });
  globalThis.fetch = async url => {
    const u = new URL(url);
    if (u.hostname === "3dhp.nationalmap.gov") {
      if (u.searchParams.get("distance") === "1200") return Response.json({ features: [first] });
      await extension;
      return Response.json({ features: [first, second] });
    }
    const points = JSON.parse(u.searchParams.get("geometry")).points;
    return Response.json({ samples: points.map((p, i) => ({ locationId: i, location: { x: p[0], y: p[1], spatialReference: { wkid: 4326 } }, value: 500 - i, attributes: { VerticalDatum: "NAVD88" } })) });
  };
  try {
    const response = await GET(request("lon=-97.995&lat=38&stream=1"));
    assert.equal(response.headers.get("content-type"), "application/x-ndjson; charset=utf-8");
    assert.equal(response.headers.get("cache-control"), "no-store");
    let nearby;
    const pending = readProgressiveDownstreamGuide(response, guide => { nearby = guide; releaseExtension(); }, new AbortController().signal);
    const complete = await pending;
    assert.equal(nearby.state, "ready");
    assert.equal(nearby.analysis.segments, 1);
    assert.match(nearby.analysis.stopReason, /Nearby preview/);
    assert.equal(complete.analysis.segments, 2);
    assert.equal(complete.analysis.elevation.state, "ready");
    assert.ok(complete.paths[0].coordinates.length > nearby.paths[0].coordinates.length);
  } finally { globalThis.fetch = original; }
});

test("an incomplete or hostile direction stream cannot become a final path", async () => {
  const response = (lines) => new Response(lines, { headers: { "content-type": "application/x-ndjson" } });
  const signal = new AbortController().signal;
  await assert.rejects(readProgressiveDownstreamGuide(response('{"phase":"error"}\n'), () => {}, signal));
  await assert.rejects(readProgressiveDownstreamGuide(response('{"phase":"nearby","guide":{}}\n'), () => {}, signal));
  await assert.rejects(readProgressiveDownstreamGuide(response('x'.repeat(512 * 1024 + 1)), () => {}, signal));
  assert.equal((await GET(request("lon=-97.995&lat=38&stream=0"))).status, 400);
});
