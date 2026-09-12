import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import ts from "typescript";
const modules = new Map();
async function moduleUrl(file) {
  file = path.resolve(file); if (modules.has(file)) return modules.get(file);
  let js = ts.transpileModule(await readFile(file, "utf8"), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
  for (const match of [...js.matchAll(/from ["'](\.[^"']+)["']/g)]) js = js.replace(match[0], `from ${JSON.stringify(await moduleUrl(path.resolve(path.dirname(file), match[1]) + ".ts"))}`);
  const url = `data:text/javascript;base64,${Buffer.from(js).toString("base64")}`; modules.set(file, url); return url;
}
const terrain = await import(await moduleUrl("app/terrain-tiles.ts"));
const perf = await import(await moduleUrl("app/map-performance.ts"));
const context = await import(await moduleUrl("app/live-context.ts"));
const tile = (query = "kind=hillshade&z=8&x=58&y=98") => new Request(`https://kfm.test/api/terrain-tile?${query}`);
// A header fixture for dimension validation; actual provider PNGs are checked
// separately. No fixture is ever served in production.
const png = () => { const b = new Uint8Array(33); b.set([137,80,78,71,13,10,26,10]); const v = new DataView(b.buffer); v.setUint32(12,0x49484452); v.setUint32(16,256); v.setUint32(20,256); return b; };

test("terrain tile requests cannot select arbitrary origins, rendering functions, sizes or geography", async () => {
  let calls = 0; const serve = terrain.createTerrainTileService({ fetchBytes: async () => { calls++; return png(); } });
  for (const q of ["kind=hillshade&z=8&x=58&y=98&url=https://other.test", "kind=slope&z=8&x=58&y=98&kind=hillshade", "kind=other&z=8&x=58&y=98", "kind=hillshade&z=17&x=58&y=98", "kind=hillshade&z=8&x=256&y=98", "kind=hillshade&z=8&x=0&y=0", "kind=hillshade&z=8&x=-1&y=98", "kind=hillshade&z=NaN&x=58&y=98"]) assert.equal((await serve(tile(q))).status,400);
  assert.equal(calls,0);
  const request = terrain.terrainTileRequest(new URL(tile("kind=slope&z=8&x=58&y=98").url));
  const upstream = new URL(request.upstream); assert.equal(upstream.hostname,"elevation.nationalmap.gov");
  assert.equal(JSON.parse(upstream.searchParams.get("renderingRule")).rasterFunction,"Slope Map");
  assert.equal(upstream.searchParams.get("size"),"256,256");
  const bbox = upstream.searchParams.get("bbox").split(",").map(Number); assert.ok(bbox[0] < bbox[2] && bbox[1] < bbox[3]);
});
test("concurrent terrain tiles share one upstream fetch and caches expire without extending source freshness", async () => {
  let calls = 0, now = Date.parse("2026-09-12T00:00:00Z");
  const serve = terrain.createTerrainTileService({ now: () => now, fetchBytes: async () => { calls++; await Promise.resolve(); return png(); } });
  const responses = await Promise.all([serve(tile()),serve(tile()),serve(tile())]);
  assert.equal(calls,1); assert.ok(responses.every(r => r.status === 200));
  assert.ok(responses.some(r => r.headers.get("X-KFM-Tile-Cache") === "COALESCED"));
  now += 1000 * (terrain.TERRAIN_TILE_TTL - 10);
  const hit = await serve(tile()); assert.equal(hit.headers.get("X-KFM-Tile-Cache"),"MEMORY");
  assert.match(hit.headers.get("Cache-Control"),/max-age=10, s-maxage=10/);
  now += 11000; await serve(tile()); assert.equal(calls,2);
});
test("edge cache survives service instances, while JSON errors and corrupt dimensions remain retryable", async () => {
  const saved = new Map(); const cache = { match: async r => saved.get(r.url)?.clone(), put: async (r,v) => { saved.set(r.url,v.clone()); } };
  let calls = 0; const options = { edgeCache: () => cache, fetchBytes: async () => { calls++; return png(); } };
  await terrain.createTerrainTileService(options)(tile());
  const hit = await terrain.createTerrainTileService(options)(tile()); assert.equal(hit.headers.get("X-KFM-Tile-Cache"),"EDGE"); assert.equal(calls,1);
  let attempts = 0; const retry = terrain.createTerrainTileService({ fetchBytes: async () => ++attempts === 1 ? new TextEncoder().encode('{"error":"unavailable"}') : png() });
  const bad = await retry(tile()); assert.equal(bad.status,502); assert.equal(bad.headers.get("Cache-Control"),"no-store");
  assert.equal((await retry(tile())).status,200); assert.equal(attempts,2);
  const wrongSize = png(); new DataView(wrongSize.buffer).setUint32(16,8192); assert.throws(() => terrain.validateTerrainPNG(wrongSize));
});
test("render quality caps high-DPI pixel work and respects the browser data-saving preference", () => {
  assert.equal(perf.renderBudget("efficient",3).pixelRatio,1);
  assert.equal(perf.renderBudget("auto",3).pixelRatio,1.5);
  assert.equal(perf.renderBudget("detail",3).pixelRatio,2);
  assert.equal(perf.renderBudget("auto",3,true).imageRequests,6);
  assert.equal(perf.renderBudget("auto",NaN).pixelRatio,1);
});
test("unchanged GeoJSON frames skip worker uploads but changed observations and replaced sources are updated", () => {
  let uploads=0; const source = { setData: () => uploads++ };
  const feature = { type:"Feature",geometry:{type:"Point",coordinates:[-98,38]},properties:{value:1} };
  const data={type:"FeatureCollection",features:[feature]};
  assert.equal(perf.updateGeoJSON(source,data),true);
  assert.equal(perf.updateGeoJSON(source,{...data,features:[feature]}),false);
  assert.equal(perf.updateGeoJSON(source,{...data,features:[{...feature,properties:{value:2}}]}),true);
  assert.equal(uploads,2);
  assert.equal(perf.updateGeoJSON({setData:()=>uploads++},data),true); assert.equal(uploads,3);
});
test("opacity changes do not re-upload provider data or create disabled raster services", () => {
  const sources=new Map(),layers=new Map(); let uploads=0,paintWrites=0,layoutWrites=0;
  const map={
    getSource:id=>sources.get(id),getLayer:id=>layers.get(id),getStyle:()=>({layers:[...layers.values()]}),
    addSource:(id,spec)=>sources.set(id,{...spec,setData:()=>uploads++}),addLayer:layer=>layers.set(layer.id,structuredClone(layer)),
    getLayoutProperty:(id,key)=>layers.get(id)?.layout?.[key],getPaintProperty:(id,key)=>layers.get(id)?.paint?.[key],
    setLayoutProperty:(id,key,value)=>{layoutWrites++;const layer=layers.get(id);layer.layout={...layer.layout,[key]:value};},
    setPaintProperty:(id,key,value)=>{paintWrites++;const layer=layers.get(id);layer.paint={...layer.paint,[key]:value};}
  };
  const visibility=Object.fromEntries(context.OFFICIAL_CONTEXT_SOURCES.map(s=>[s.id,s.id==="census-counties"]));
  const opacity=Object.fromEntries(context.OFFICIAL_CONTEXT_SOURCES.map(s=>[s.id,s.defaultOpacity]));
  const data={type:"FeatureCollection",features:[{type:"Feature",geometry:{type:"Point",coordinates:[-98,38]},properties:{featureId:"test"}}]};
  const payloads={"census-counties":{data}};
  context.applyOfficialContextState(map,visibility,opacity,payloads);
  assert.equal([...sources.values()].filter(s=>s.type==="raster").length,0);
  paintWrites=0;layoutWrites=0;
  context.applyOfficialContextState(map,visibility,opacity,payloads);
  assert.equal(uploads,0);assert.equal(paintWrites,0);assert.equal(layoutWrites,0);
  context.applyOfficialContextState(map,visibility,{...opacity,"census-counties":0.5},payloads);
  assert.equal(uploads,0);assert.equal(paintWrites,2);
  context.applyOfficialContextState(map,{...visibility,"usgs-3dep-hillshade":true},opacity,payloads);
  const source=sources.get("external-usgs-3dep-hillshade");assert.equal(source.maxzoom,14);assert.match(source.tiles[0],/^\/api\/terrain-tile\?/);
});
