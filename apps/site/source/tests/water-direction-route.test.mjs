import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { pathToFileURL } from "node:url";
import { createContext, runInContext } from "node:vm";
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

async function pageDirectionCallbacks(context) {
  const source = ts.createSourceFile("app/page.tsx", await readFile("app/page.tsx", "utf8"), ts.ScriptTarget.Latest, true, ts.ScriptKind.TSX);
  let click, readyEffect;
  const visit = node => {
    if (ts.isVariableDeclaration(node) && node.name.getText(source) === "showStreamflowDirection") click = node.initializer?.arguments[0];
    if (ts.isCallExpression(node) && node.expression.getText(source) === "useEffect" && node.arguments[0]?.getText(source).includes("riverPathFocusRef.current !== downstreamStationId")) readyEffect = node.arguments[0];
    ts.forEachChild(node, visit);
  };
  visit(source);
  assert.ok(click && readyEffect, "page click handler and final-path effect must both exist");
  const runnable = arrow => runInContext(ts.transpileModule(`(${arrow.getText(source)})`, {
    compilerOptions: { module: ts.ModuleKind.None, target: ts.ScriptTarget.ES2022 },
  }).outputText, context);
  return { click: runnable(click), fitReady: runnable(readyEffect) };
}

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
    assert.equal(guide.format, "kfm-3dhp-direction-v3"); assert.equal(calls, 3);
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

test("clicking Zoom to flow direction after the nearby event still refits the final route", async () => {
  const original = globalThis.fetch;
  let releaseExtension, releaseTerrain;
  const extension = new Promise(resolve => { releaseExtension = resolve; });
  const terrain = new Promise(resolve => { releaseTerrain = resolve; });
  const station = { stationId: "06864500", name: "Fixture gauge", longitude: -97.995, latitude: 38 };
  const fits = [];
  const context = createContext({
    mapRef: { current: { getCenter: () => ({ lng: station.longitude, lat: station.latitude }), getCanvas: () => ({ clientHeight: 800 }), fitBounds: bounds => fits.push(JSON.parse(JSON.stringify(bounds))) } },
    streamflowBundle: { stations: [station] }, streamflowSelectedAtPresent: true,
    streamflowFrame: { features: [{ properties: { stationId: station.stationId, missing: false, value: 10 } }] },
    streamflowSelectedStation: station, streamflowSelectedStationId: station.stationId,
    selectStreamflowStation: () => assert.fail("station is already selected"),
    downstreamPaths: [], downstreamAnalysis: null, downstreamState: "loading", downstreamStationId: station.stationId,
    riverPathFocusRef: { current: null }, reducedMotion: true, announce: () => {},
  });
  const { click, fitReady } = await pageDirectionCallbacks(context);
  globalThis.fetch = async url => {
    const u = new URL(url);
    if (u.hostname === "3dhp.nationalmap.gov") {
      if (u.searchParams.get("distance") === "1200") return Response.json({ features: [first] });
      await extension;
      return Response.json({ features: [first, second] });
    }
    await terrain;
    const points = JSON.parse(u.searchParams.get("geometry")).points;
    return Response.json({ samples: points.map((p, i) => ({ locationId: i, location: { x: p[0], y: p[1], spatialReference: { wkid: 4326 } }, value: 500 - i, attributes: { VerticalDatum: "NAVD88" } })) });
  };
  try {
    const response = await GET(request("lon=-97.995&lat=38&stream=1"));
    assert.equal(response.headers.get("content-type"), "application/x-ndjson; charset=utf-8");
    assert.equal(response.headers.get("cache-control"), "no-store");
    let nearby, network;
    const pending = readProgressiveDownstreamGuide(response, guide => {
      context.downstreamPaths = guide.paths;
      context.downstreamAnalysis = guide.analysis ?? null;
      if (guide.format === "kfm-3dhp-direction-v2") {
        nearby = guide;
        click(); // Zoom to flow direction after the nearby event, before the network and terrain.
        releaseExtension();
        assert.equal(context.riverPathFocusRef.current, station.stationId);
        assert.equal(fits.length, 1, "the nearby preview is fitted immediately");
        fitReady();
        assert.equal(fits.length, 1, "the nearby preview cannot consume the pending focus");
      } else {
        network = guide;
        fitReady();
        releaseTerrain();
        assert.equal(fits.length, 2, "the full network fits while terrain is loading");
        assert.equal(context.riverPathFocusRef.current, station.stationId, "network preview retains focus for ready");
      }
    }, new AbortController().signal);
    const complete = await pending;
    assert.equal(nearby.state, "ready");
    assert.equal(nearby.analysis.segments, 1);
    assert.match(nearby.analysis.stopReason, /Nearby preview/);
    assert.equal(complete.analysis.segments, 2);
    assert.equal(complete.analysis.elevation.state, "ready");
    assert.ok(complete.paths[0].coordinates.length > nearby.paths[0].coordinates.length);
    assert.equal(network.format, "kfm-3dhp-direction-v3");
    context.downstreamPaths = complete.paths;
    context.downstreamAnalysis = complete.analysis;
    context.downstreamState = complete.state;
    fitReady();
    const points = complete.paths.flatMap(path => path.coordinates);
    assert.equal(fits.length, 3, "the final ready route must refit after both previews");
    assert.deepEqual(fits[2], [[Math.min(...points.map(point => point[0])), Math.min(...points.map(point => point[1]))], [Math.max(...points.map(point => point[0])), Math.max(...points.map(point => point[1]))]]);
    assert.notDeepEqual(fits[2], fits[0]);
    assert.equal(context.riverPathFocusRef.current, null);
  } finally { releaseExtension(); releaseTerrain(); globalThis.fetch = original; }
});

test("an incomplete or hostile direction stream cannot become a final path", async () => {
  const response = (lines) => new Response(lines, { headers: { "content-type": "application/x-ndjson" } });
  const signal = new AbortController().signal;
  await assert.rejects(readProgressiveDownstreamGuide(response('{"phase":"error"}\n'), () => {}, signal));
  await assert.rejects(readProgressiveDownstreamGuide(response('{"phase":"nearby","guide":{}}\n'), () => {}, signal));
  await assert.rejects(readProgressiveDownstreamGuide(response('x'.repeat(512 * 1024 + 1)), () => {}, signal));
  assert.equal((await GET(request("lon=-97.995&lat=38&stream=0"))).status, 400);
});


test("the extended network becomes drawable before delayed terrain samples", async () => {
  const original=globalThis.fetch; let releaseTerrain;
  const wait=new Promise(resolve=>{releaseTerrain=resolve;});let sawNetwork=false;
  globalThis.fetch=async url=>{
    if(new URL(url).hostname==="3dhp.nationalmap.gov") return Response.json({features:[first,second]});
    await wait;return new Response("unavailable",{status:503});
  };
  try {
    const response=await GET(request("lon=-97.995&lat=38&stream=1"));
    const complete=await readProgressiveDownstreamGuide(response,guide=>{
      if(guide.format==="kfm-3dhp-direction-v3") {sawNetwork=true;assert.ok(guide.analysis.upstreamM>0);releaseTerrain();}
    },new AbortController().signal);
    assert.equal(sawNetwork,true);assert.equal(complete.state,"ready");assert.equal(complete.analysis.elevation.state,"unavailable");
    const forged=structuredClone(complete);forged.analysis.upstreamM=200000;assert.throws(()=>parseDownstreamGuide(forged));
  } finally {releaseTerrain();globalThis.fetch=original;}
});
