import assert from "node:assert/strict";
import "./cloudflare-register.mjs";
import { readFile } from "node:fs/promises";
import { inflateSync } from "node:zlib";
import test from "node:test";
import ts from "typescript";

const modules = new Map();
async function moduleUrl(relative) {
  if (modules.has(relative)) return modules.get(relative);
  let source = await readFile(new URL(relative, import.meta.url), "utf8");
  if (relative.includes("/api/event-atlas/")) {
    const atlas = await moduleUrl("../app/event-atlas.ts");
    const upstream = relative.endsWith("upstream.ts") ? null : await moduleUrl("../app/api/event-atlas/upstream.ts");
    source = source.replaceAll('"../../../event-atlas"', JSON.stringify(atlas));
    if (upstream) source = source.replaceAll('"../upstream"', JSON.stringify(upstream));
  }
  const code = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 }, fileName: relative }).outputText;
  const url = `data:text/javascript;base64,${Buffer.from(code).toString("base64")}`;
  modules.set(relative,url); return url;
}
const atlas = await import(await moduleUrl("../app/event-atlas.ts"));
const kml = (start="2023158 1310",end="2023158 1710",density="Light",coords="-100,38,0 -98,38,0 -98,39,0 -100,38,0") => `<kml><Document><Placemark><description><![CDATA[Start Time: ${start}UTC<br>End Time: ${end}UTC<br>Density: ${density}<br>Satellite: GOES-EAST</div>]]></description><Polygon><outerBoundaryIs><LinearRing><coordinates>${coords}</coordinates></LinearRing></outerBoundaryIs></Polygon></Placemark></Document></kml>`;
const listing = `<a href="n0r_200705050245.png">a</a><a href="n0r_200705050250.png">b</a><a href="n0q_200705050245.png">early Q</a><a href="n0r_200705050246.png">off grid</a>`;
const manifestFixture = () => ({ format: "kfm-event-atlas-v1", start:"2007-05-05T02:00:00.000Z", end:"2007-05-05T03:00:00.000Z", retrievedAt:"2026-09-10T00:00:00.000Z", radar:{ scans:atlas.parseRadarDirectory(listing,"2007-05-05","2007-05-05T02:00:00.000Z","2007-05-05T03:00:00.000Z"),gaps:[] }, smoke:{data:{type:"FeatureCollection",features:[]},gaps:[]},imagery:{dates:[]} });

test("event interval rejects ambiguous/future/rollover dates and unbounded windows", () => {
  assert.equal(atlas.exactUtc("2024-02-29T00:00:00Z"),"2024-02-29T00:00:00.000Z");
  for (const date of ["2023-02-29T00:00:00Z","2024-01-01","2024-01-01T12:00:00+00:00","2024-01-01T24:00:00Z"]) assert.equal(atlas.exactUtc(date),null);
  assert.doesNotThrow(() => atlas.eventInterval("1994-01-01T00:00:00Z",6));
  assert.throws(() => atlas.eventInterval("1799-01-01T00:00:00Z",6));
  assert.throws(() => atlas.eventInterval("2024-01-01T00:00:00Z",48));
  assert.throws(() => atlas.eventInterval("2099-01-01T00:00:00Z",6));
  assert.deepEqual(atlas.intervalDays("2024-01-01T23:00:00Z","2024-01-02T01:00:00Z"),["2024-01-01","2024-01-02"]);
  assert.deepEqual(atlas.intervalDays("2024-01-01T00:00:00Z","2024-01-02T00:00:00Z"),["2024-01-01"]);
});

test("calendar weeks retain all 24 UTC hours when a checked day has gaps", () => {
  assert.equal(atlas.eventDay("2007-05-05"), "2007-05-05");
  assert.equal(atlas.eventDay("2007-02-29"), null);
  assert.deepEqual(atlas.eventWeekDays("2007-05-05"), ["2007-04-29", "2007-04-30", "2007-05-01", "2007-05-02", "2007-05-03", "2007-05-04", "2007-05-05"]);
  const slots = atlas.eventDayHours("2007-05-05");
  assert.equal(slots.length, 24);
  assert.deepEqual(slots.map((slot) => slot.hour), Array.from({ length: 24 }, (_, hour) => hour));
  assert.equal(slots[0].start, "2007-05-05T00:00:00.000Z");
  assert.equal(slots.at(-1).end, "2007-05-06T00:00:00.000Z");
  const empty = atlas.eventHourAvailability({
    format: "kfm-event-atlas-v1", start: "2007-05-05T00:00:00.000Z", end: "2007-05-06T00:00:00.000Z", retrievedAt: "2026-09-10T00:00:00.000Z",
    radar: { scans: [], gaps: [], message: "" }, smoke: { data: { type: "FeatureCollection", features: [] }, gaps: [], message: "" }, imagery: { dates: [], message: "" }, evidenceRole: "EXTERNAL_CONTEXT_ONLY",
  }, [], "2007-05-05");
  assert.equal(empty.length, 24);
  assert.equal(empty.every((slot) => slot.supported === false), true);
  const supported = atlas.eventHourAvailability({
    ...manifestFixture(), start: "2007-05-05T00:00:00.000Z", end: "2007-05-06T00:00:00.000Z",
  }, [], "2007-05-05");
  assert.equal(supported.find((slot) => slot.hour === 2)?.radar, true);
  assert.equal(supported.find((slot) => slot.hour === 1)?.supported, false);
});

test("radar admits actual files only, on-grid, in the requested half-open interval and product era", () => {
  const scans=atlas.parseRadarDirectory(listing,"2007-05-05","2007-05-05T02:45:00.000Z","2007-05-05T02:50:00.000Z");
  assert.equal(scans.length,1); assert.equal(scans[0].product,"n0r");
  assert.equal(scans[0].time,"2007-05-05T02:45:00.000Z");
  assert.equal(atlas.radarAt(scans,"2007-05-05T02:49:59Z")?.time,scans[0].time);
  assert.equal(atlas.radarAt(scans,"2007-05-05T02:50:00Z"),null);
  assert.equal(atlas.radarAt(scans,"2007-05-05T02:44:59Z"),null);
  assert.equal(atlas.radarProduct("2011-02-15T23:55:00Z"),"n0r"); assert.equal(atlas.radarProduct("2011-02-16T00:00:00Z"),"n0q");
});

test("HMS ordinal timestamps preserve leap years and reject invalid clock fields", () => {
  assert.equal(atlas.hmsTime("2023158 1310UTC"),"2023-06-07T13:10:00.000Z");
  assert.equal(atlas.hmsTime("2020366 2359"),"2020-12-31T23:59:00.000Z");
  for(const t of ["2023366 1310","2023000 1310","2023158 2400","2023158 1260","2023-06-07"]) assert.equal(atlas.hmsTime(t),null);
});

test("HMS polygons use their exact intervals and preserve unknown historical density", () => {
  const data=atlas.parseSmokeKml(kml(),"https://source.test/date.kml");
  assert.equal(data.features.length,1);
  assert.equal(data.features[0].properties.satellite,"GOES-EAST");
  assert.equal(atlas.smokeAt(data,"2023-06-07T13:09:59Z").features.length,0);
  assert.equal(atlas.smokeAt(data,"2023-06-07T13:10:00Z").features.length,1);
  assert.equal(atlas.smokeAt(data,"2023-06-07T17:10:00Z").features.length,0);
  assert.equal(atlas.parseSmokeKml(kml("2005217 1310","2005217 1710","NA"),"x").features[0].properties.density,"NA");
  assert.equal(atlas.parseSmokeKml(kml(undefined,undefined,undefined,"0,1,0 1,1,0 1,2,0 0,1,0"),"x").features.length,0);
});

test("HMS parser fails closed on XML entities, missing dates, bad rings and unknown categories", () => {
  assert.throws(() => atlas.parseSmokeKml("<!DOCTYPE kml>"+kml(),"x"));
  assert.throws(() => atlas.parseSmokeKml(kml("",""),"x"));
  assert.throws(() => atlas.parseSmokeKml(kml(undefined,undefined,"invented"),"x"));
  assert.throws(() => atlas.parseSmokeKml(kml(undefined,undefined,undefined,"-100,38,0 -98,38,0 -98,39,0 -101,38,0"),"x"));
  assert.throws(() => atlas.parseSmokeKml(kml("2023158 1710","2023158 1310"),"x"));
});

test("exact imagery availability rejects absent dates and unsupported temporal cadence", () => {
  assert.equal(atlas.domainIncludes("<Domain>2023-06-01/2023-06-08/P1D</Domain>","2023-06-07"),true);
  assert.equal(atlas.domainIncludes("<Domain>2023-06-01/2023-06-08/P1D</Domain>","2023-06-09"),false);
  assert.equal(atlas.domainIncludes("<Domain>2023-06-01,2023-06-08</Domain>","2023-06-07"),false);
  assert.equal(atlas.domainIncludes("<Domain>2023-06-01/2023-06-08/P2D</Domain>","2023-06-07"),false);
});

test("event sequence includes gap boundaries and excludes the query end", () => {
  const m=manifestFixture(); const frames=atlas.eventFrames(m,[{observedAt:"2007-05-05T02:01:00.000Z"}]);
  assert.ok(frames.includes("2007-05-05T02:55:00.000Z"));
  assert.ok(frames.includes("2007-05-05T02:31:01.000Z"));
  assert.ok(!frames.includes(m.end)); assert.equal(new Set(frames).size,frames.length);
  assert.deepEqual(frames,[...frames].sort());
});

test("manifest marks upstream gaps rather than substituting current data", async () => {
  const {GET}=await import(await moduleUrl("../app/api/event-atlas/manifest/route.ts"));
  const previous=globalThis.fetch;
  globalThis.fetch=async (url) => {
    const u=new URL(url);
    if(u.hostname==="mesonet.agron.iastate.edu") return new Response(listing);
    if(u.hostname==="satepsanone.nesdis.noaa.gov") return new Response("missing",{status:404});
    return new Response("<Domain>2007-05-05</Domain>");
  };
  try {
    const response=await GET(new Request("https://app.test/api/event-atlas/manifest?start=2007-05-05T02%3A00%3A00Z&hours=1"));
    assert.equal(response.status,200); const body=await response.json();
    assert.equal(body.radar.scans.length,2); assert.equal(body.smoke.state,"partial");
    assert.equal(body.smoke.data.features.length,0); assert.equal(body.smoke.gaps.length,2);
    assert.deepEqual(body.imagery.dates,["2007-05-05"]);
    assert.equal(body.evidenceRole,"EXTERNAL_CONTEXT_ONLY");
    const invalid=await GET(new Request("https://app.test/api/event-atlas/manifest?start=latest&hours=999&url=https://evil.test")); assert.equal(invalid.status,400);
  } finally {globalThis.fetch=previous;}
});

test("radar image adapter rejects absent frames before any WMS request", async () => {
  const {GET}=await import(await moduleUrl("../app/api/event-atlas/radar-frame/route.ts"));
  const previous=globalThis.fetch; const seen=[];
  globalThis.fetch=async (url) => {seen.push(String(url));return new Response(listing);};
  try {
    const response=await GET(new Request("https://app.test/api/event-atlas/radar-frame?time=2007-05-05T02%3A40%3A00Z"));
    assert.equal(response.status,404);assert.ok(seen.every((url)=>!url.includes("GetMap")));
    const invalid=await GET(new Request("https://app.test/api/event-atlas/radar-frame?time=1994-01-01T00%3A00%3A00Z"));assert.equal(invalid.status,502);
  } finally {globalThis.fetch=previous;}
});

test("tile adapter rejects time snapping and converts 204 into truly transparent pixels", async () => {
  const {GET}=await import(await moduleUrl("../app/api/event-atlas/tile/route.ts"));
  const previous=globalThis.fetch;
  globalThis.fetch=async () => new Response("wrong day",{headers:{"content-type":"image/jpeg","layer-time-actual":"2023-06-06T00:00:00Z"}});
  try {
    const snapped=await GET(new Request("https://app.test/api/event-atlas/tile?kind=satellite&date=2023-06-07&z=6&x=14&y=24"));assert.equal(snapped.status,502);
    globalThis.fetch=async () => new Response(null,{status:204});
    const empty=await GET(new Request("https://app.test/api/event-atlas/tile?kind=flora&date=2023-06-07&z=6&x=14&y=24"));
    assert.equal(empty.status,200);assert.equal(empty.headers.get("x-aggregate-state"),"no-records");
    const png=Buffer.from(await empty.arrayBuffer());const length=png.readUInt32BE(33);
    assert.deepEqual([...inflateSync(png.subarray(41,41+length))],[0,0,0,0,0]);
    const precise=await GET(new Request("https://app.test/api/event-atlas/tile?kind=fauna&date=2023-06-07&z=12&x=900&y=1500"));assert.equal(precise.status,502);
  } finally {globalThis.fetch=previous;}
});

test("county resources never request precise source geometry and reject unmatched counties", async () => {
  const {GET}=await import(await moduleUrl("../app/api/event-atlas/resources/route.ts"));
  const previous=globalThis.fetch;const seen=[];
  globalThis.fetch=async (url) => {
    seen.push(String(url));
    if(String(url).includes("Mine_Symbols")) return Response.json({features:[{attributes:{County:"Unknown County",symbol_count:2}}]});
    return Response.json({type:"FeatureCollection",features:Array.from({length:105},(_,i)=>({geometry:{type:"Polygon",coordinates:[]},properties:{BASENAME:`County ${i}`,GEOID:`20${i}`}}))});
  };
  try {
    const response=await GET(new Request("https://app.test/api/event-atlas/resources?edition=1984"));assert.equal(response.status,502);
    const query=new URL(seen.find((url)=>url.includes("Mine_Symbols")));
    assert.equal(query.searchParams.get("returnGeometry"),"false");assert.equal(query.searchParams.get("groupByFieldsForStatistics"),"County");
    const invalid=await GET(new Request("https://app.test/api/event-atlas/resources?edition=1984%27%20OR%201%3D1"));assert.equal(invalid.status,400);
  } finally {globalThis.fetch=previous;}
});

test("admitted radar renders only exact TIME in Mercator with fixed dimensions", async () => {
  const {GET}=await import(await moduleUrl("../app/api/event-atlas/radar-frame/route.ts"));
  const previous=globalThis.fetch;let wms=null;
  const png=new Uint8Array(24);png.set([137,80,78,71,13,10,26,10]);new DataView(png.buffer).setUint32(16,1024);new DataView(png.buffer).setUint32(20,600);
  globalThis.fetch=async (url)=>{const u=new URL(url);if(u.pathname.includes("cgi-bin")){wms=u;return new Response(png,{headers:{"content-type":"image/png"}});}return new Response(listing);};
  try {
    const response=await GET(new Request("https://app.test/api/event-atlas/radar-frame?time=2007-05-05T02%3A45%3A00Z"));
    assert.equal(response.status,200);assert.equal(response.headers.get("x-radar-mosaic-time"),"2007-05-05T02:45:00.000Z");
    assert.equal(wms.searchParams.get("time"),"2007-05-05T02:45:00Z");assert.equal(wms.searchParams.get("srs"),"EPSG:3857");assert.equal(wms.searchParams.get("width"),"1024");
    assert.equal(wms.searchParams.get("layers"),"nexrad-n0r-wmst");assert.match(response.headers.get("x-source-artifact"),/n0r_200705050245\.png$/);
  } finally {globalThis.fetch=previous;}
});

test("saved Worker serves the event mixer and navigable cited research without browser globals", async () => {
  const {default:worker}=await import(new URL("../dist/server/index.js",import.meta.url));
  const env={ASSETS:{fetch:async()=>new Response("not found",{status:404})}},ctx={waitUntil(){},passThroughOnException(){}};
  const response=await worker.fetch(new Request("http://localhost/observatory"),env,ctx);assert.equal(response.status,200);
  const html=await response.text();
  for(const label of ["Event Observatory","Layer an event","Show Radar reflectivity","Show Smoke footprint","Show Fauna occurrences","Resource-map symbols","Shared event clock"]) assert.match(html,new RegExp(label,"i"));
  assert.ok(!/checked=""[^>]*aria-label="Loop"/.test(html));
  const sources=await worker.fetch(new Request("http://localhost/observatory/sources"),env,ctx);assert.equal(sources.status,200);const report=await sources.text();
  assert.match(report,/Sources and references/);assert.match(report,/b44494c1cf0807ed28b606e8a41b255bebdf4ad7/);assert.match(report,/HRRR flow is therefore researched but not activated/);
});
