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
const flow = await import(await compile("app/water-flow-motion.ts"));
const { GET } = await import(await compile("app/api/hydrology/flowlines/route.ts"));
const request = (suffix) => ({ nextUrl: new URL(`https://local/api/hydrology/flowlines${suffix}`), signal: new AbortController().signal });
const reach = (id, coordinates, extra = {}) => ({ properties: { id3dhp: id, hydrosequence: 30, dnhydrosequence: 20, uphydrosequence: null, levelpath: 10, flowdirection: 1, featuretype: 1, gnisidlabel: "Fixture Creek", ...extra }, geometry: { type: "LineString", coordinates } });
const near = (actual, expected, tolerance, message) => assert.ok(Math.abs(actual - expected) <= tolerance, `${message}: ${actual} vs ${expected}`);

test("flowline cells sit on the 0.25° Kansas grid", () => {
  assert.deepEqual(flow.parseFlowlineCell("-97.25,38.00"), [-97.25, 38]);
  assert.deepEqual(flow.parseFlowlineCell("-102.25,36.75"), [-102.25, 36.75]);
  for (const bad of [null, "", "-97.1,38", "-97.25,38.10", "-120,38", "-94.50,38", "-97.25,40.25", "x,y", "-97.25,38,1", "-97.25, 38"]) {
    assert.equal(flow.parseFlowlineCell(bad), null, String(bad));
  }
  assert.equal(flow.flowlineCellKey([-97.25, 38]), "-97.25,38.00");
});

test("the view asks for nearby cells only at river zoom, nearest first and capped", () => {
  const bounds = { west: -98.2, south: 37.6, east: -96.8, north: 38.4 };
  assert.deepEqual(flow.flowCellsForView(bounds, [-97.5, 38], 8.49), [], "too far out");
  const cells = flow.flowCellsForView(bounds, [-97.5, 38], 11);
  assert.ok(cells.length > 0 && cells.length <= flow.MAX_FLOW_CELLS);
  const first = cells[0];
  assert.ok(Math.abs(first[0] + 0.125 + 97.5) <= 0.126 && Math.abs(first[1] + 0.125 - 38) <= 0.126, "first cell contains the centre");
  for (const cell of cells) assert.ok(flow.parseFlowlineCell(flow.flowlineCellKey(cell)), "every cell is valid");
  assert.deepEqual(flow.flowCellsForView({ west: -110, south: 45, east: -109, north: 46 }, [-109.5, 45.5], 12), [], "outside Kansas");
});

test("the route returns only provider-directed reaches for a valid cell", async () => {
  const original = globalThis.fetch;
  let seen;
  globalThis.fetch = async (url) => {
    seen = new URL(url);
    return Response.json({ features: [reach("A1", [[-97.2, 38.1], [-97.19, 38.1]]), reach("B2", [[-97.19, 38.1], [-97.18, 38.11]], { flowdirection: 0 })], exceededTransferLimit: true });
  };
  try {
    const response = await GET(request("?cell=-97.25,38.00"));
    assert.equal(response.status, 200);
    assert.equal(seen.hostname, "3dhp.nationalmap.gov");
    assert.equal(seen.searchParams.get("where"), "flowdirection=1 AND featuretype IN (1,4,5,6)");
    assert.equal(seen.searchParams.get("geometry"), "-97.25,38.00,-97.00,38.25");
    const payload = flow.parseFlowlinePayload(await response.json());
    assert.equal(payload.reaches.length, 1, "a reach without the downstream flag is never returned");
    assert.equal(payload.reaches[0].id, "A1");
    assert.equal(payload.truncated, true);
    assert.equal(payload.evidenceRole, "EXTERNAL_CONTEXT_ONLY");
  } finally { globalThis.fetch = original; }
});

test("the route refuses bad cells before calling USGS and reports provider failure", async () => {
  const original = globalThis.fetch;
  let calls = 0;
  globalThis.fetch = async () => { calls += 1; return new Response("down", { status: 502 }); };
  try {
    for (const suffix of ["", "?cell=-97.10,38.00", "?cell=-97.25,38.00&extra=1", "?cell=-97.25,38.00&cell=-97.00,38.00"]) {
      assert.equal((await GET(request(suffix))).status, 400, suffix);
    }
    assert.equal(calls, 0);
    assert.equal((await GET(request("?cell=-97.25,38.00"))).status, 503);
  } finally { globalThis.fetch = original; }
});

test("the payload check rejects foreign sources, bad reaches and inconsistent state", () => {
  const good = { format: "kfm-3dhp-flowlines-v1", cell: [-97.25, 38], state: "ready", truncated: false, reaches: [{ id: "A1", sequence: 3, downstream: null, levelpath: 9, name: null, featureType: 1, coordinates: [[-97.2, 38.1], [-97.19, 38.1]] }], source: flow.FLOWLINE_SERVICE, retrievedAt: "2026-10-10T00:00:00Z", evidenceRole: "EXTERNAL_CONTEXT_ONLY", limitation: "x" };
  assert.equal(flow.parseFlowlinePayload(good).reaches.length, 1);
  for (const broken of [
    { ...good, source: "https://example.com/" },
    { ...good, state: "empty" },
    { ...good, reaches: [{ ...good.reaches[0], featureType: 2 }] },
    { ...good, reaches: [{ ...good.reaches[0], coordinates: [[-97.2, 38.1]] }] },
    { ...good, reaches: [{ ...good.reaches[0], coordinates: [[-80, 38.1], [-97.19, 38.1]] }] },
    { ...good, cell: [-97.1, 38] },
  ]) assert.throws(() => flow.parseFlowlinePayload(broken));
});

test("gauge cues come from current measured or zero readings only", () => {
  const at = [-97.2, 38.1];
  assert.equal(flow.gaugeCue({ value: null, missing: true }, at), null, "missing");
  assert.equal(flow.gaugeCue({ value: 40, readingState: "stale", trend: "rising" }, at), null, "stale");
  assert.equal(flow.gaugeCue({ value: 40, readingState: "measured" }, [-80, 38]), null, "outside Kansas");
  const zero = flow.gaugeCue({ value: 0, readingState: "zero" }, at);
  assert.equal(zero.moving, false, "measured zero stills the water");
  const rising = flow.gaugeCue({ value: 900, readingState: "measured", trend: "rising", visualMagnitude: 2.95 }, at);
  assert.equal(rising.tint, "rising");
  assert.equal(rising.moving, true);
  near(rising.intensity, 0.59, 1e-9, "intensity follows the column scale");
  assert.equal(flow.gaugeCue({ value: 5, readingState: "measured", trend: "odd" }, at).tint, "unknown");
});

test("geometry runs downstream, and gauge styling stays on the gauged reach", () => {
  const reaches = [
    { id: "MAIN", sequence: 2, downstream: null, levelpath: 1, name: "Fixture River", featureType: 1, coordinates: [[-97.3, 38.1], [-97.25, 38.1], [-97.2, 38.1], [-97.1, 38.1]] },
    { id: "TRIB", sequence: 5, downstream: 2, levelpath: 2, name: null, featureType: 1, coordinates: [[-97.25, 38.2], [-97.25, 38.1]] },
  ];
  const gauge = flow.gaugeCue({ value: 120, readingState: "measured", trend: "falling", visualMagnitude: 2 }, [-97.2495, 38.0998]);
  const geometry = flow.buildFlowGeometry(reaches, [gauge]);
  assert.equal(geometry.count, 4);
  assert.equal(geometry.reaches, 2);
  assert.equal(geometry.gauged, 1);
  const segment = (index) => Array.from(geometry.segments.slice(index * flow.FLOW_SEGMENT_FLOATS, (index + 1) * flow.FLOW_SEGMENT_FLOATS));
  // Distance grows along digitized (downstream) order, segment to segment.
  const main = [0, 1, 2].map(segment);
  assert.equal(main[0][6], 0);
  for (let i = 0; i < 3; i += 1) assert.ok(main[i][7] > main[i][6], "distance increases downstream");
  near(main[1][6], main[0][7], 1e-3, "segments chain");
  // The gauge sits at the first junction of MAIN: emphasis there, none far away.
  assert.ok(main[0][8] > 0 && main[1][8] > 0, "segments near the gauge are emphasised");
  assert.equal(main[2][8], 0, "a segment beyond the window keeps the direction-only look");
  assert.equal(main[0][10], flow.FLOW_TINT_INDEX.falling);
  assert.equal(main[2][10], flow.FLOW_TINT_INDEX.direction);
  // The tributary joins 50 m from the gauge, but the gauge snapped to MAIN only.
  assert.equal(segment(3)[8], 0, "values are not painted onto a neighbouring reach");
  for (const vertex of geometry.vertices) for (const slot of vertex.slots) assert.ok(slot % flow.FLOW_SEGMENT_FLOATS === 2 || slot % flow.FLOW_SEGMENT_FLOATS === 5);
});

test("a measured zero stills only its own stretch, and duplicates across cells draw once", () => {
  const coordinates = [[-97.3, 38.1], [-97.29, 38.1], [-97.2, 38.1], [-97.1, 38.1]];
  const reaches = [{ id: "R", sequence: 1, downstream: null, levelpath: 1, name: null, featureType: 1, coordinates }];
  const geometry = flow.buildFlowGeometry([...reaches, ...reaches], [flow.gaugeCue({ value: 0, readingState: "zero" }, [-97.295, 38.1])]);
  assert.equal(geometry.count, 3, "a reach returned by two cells is drawn once");
  const motion = (index) => geometry.segments[index * flow.FLOW_SEGMENT_FLOATS + 9];
  assert.ok(motion(0) < 0.05, "still water at the zero gauge");
  assert.equal(motion(2), 1, "water keeps its direction cue beyond the window");
  near(flow.gaugeFalloff(0), 1, 1e-12, "full at the gauge");
  near(flow.gaugeFalloff(flow.GAUGE_REACH_WINDOW_M), 0, 1e-12, "gone at the window edge");
});

test("the flow layer has a globe shader path, bounded widths and palettes for every light", async () => {
  const layerModule = await import(await compile("app/water-flow-layer.ts"));
  const source = await readFile("app/water-flow-layer.ts", "utf8");
  assert.match(source, /projectTileWithElevation\(p\.xy/);
  assert.match(source, /variantName === "globe"/);
  assert.match(source, /drawArraysInstanced/);
  for (const preset of ["night", "dusk", "clear"]) {
    const palette = layerModule.WATER_FLOW_PALETTES[preset];
    assert.equal(palette.tints.length, 5, `${preset} has a tint per trend`);
    for (const channel of [...palette.base, ...palette.streak, ...palette.tints.flat()]) assert.ok(channel >= 0 && channel <= 1);
  }
  assert.equal(layerModule.flowHalfWidth(10), 1.6);
  assert.ok(layerModule.flowHalfWidth(20) <= 6 && layerModule.flowHalfWidth(5) >= 0.8);
  near(layerModule.metersPerPixel(0, 0), 2 * Math.PI * 6378137 / 512, 1e-6, "metres per pixel at the equator, zoom 0");
  const layer = layerModule.createWaterFlowLayer({ id: "w", clock: () => null, palette: () => layerModule.WATER_FLOW_PALETTES.night });
  assert.equal(layer.type, "custom");
  assert.equal(layer.renderingMode, "3d", "depth-tested so hills hide the water behind them");
  assert.equal(layer.segmentCount, 0);
  assert.doesNotThrow(() => layer.render({}, {}), "render before onAdd is a no-op");
});

test("drawing budget reports only represented reaches and gauge cues, with omitted geometry explicit", () => {
  const reaches = Array.from({length: 400}, (_, i) => ({ id: `C${i}`, coordinates: Array.from({length: 501}, (_, j) => [-97 + i * .0001 + j * .000001, 38]), sequence: null, downstream: null, levelpath: null, name: null, featureType: 1 }));
  const omittedGauge = flow.gaugeCue({ value: 100, readingState: "measured" }, reaches[399].coordinates[0]);
  const geometry = flow.buildFlowGeometry(reaches, [omittedGauge]);
  assert.equal(geometry.count, flow.MAX_FLOW_SEGMENTS);
  assert.equal(geometry.reaches, 120, "only 120 reaches have any drawn segments");
  assert.equal(geometry.availableReaches, 400);
  assert.equal(geometry.gauged, 0, "a gauge on omitted geometry is not reported as drawn");
  assert.equal(geometry.truncated, true);
});

test("nearest-first terrain queue preserves exact order while calculating each distance once", async t => {
  const layer = await import(await compile("app/water-flow-layer.ts"));
  const vertices = Array.from({length: 60000}, (_, i) => ({lng: -97 + Math.sin(i * 17.1) * .3, lat: 38 + Math.cos(i * 13.7) * .2, slots: []}));
  const center = {lng: -97.15, lat: 38.1};
  let beforeCalls = 0;
  const before = () => vertices.map((_, i) => i).sort((a, b) => {
    beforeCalls += 2;
    return Math.hypot(vertices[a].lng - center.lng, vertices[a].lat - center.lat) - Math.hypot(vertices[b].lng - center.lng, vertices[b].lat - center.lat);
  });
  const expected = before();
  assert.deepEqual(layer.orderedFlowVertices(vertices, center), expected);
  const times = {before: [], after: []};
  for (let i = 0; i < 7; i++) for (const kind of i % 2 ? ["after", "before"] : ["before", "after"]) {
    const start = performance.now();
    (kind === "before" ? before : () => layer.orderedFlowVertices(vertices, center))();
    times[kind].push(performance.now() - start);
  }
  const median = values => values.sort((a,b) => a-b)[3];
  t.diagnostic(JSON.stringify({scenario: "synthetic-60000-vertex-order", runs: 7, beforeMedianMs: median(times.before), afterMedianMs: median(times.after), beforeDistanceCalls: beforeCalls / 8, afterDistanceCalls: vertices.length, exactOrder: true}));
});


test("fixed overview grids cover Kansas and source order drives bounded zoom detail", () => {
  const bounds = flow.FLOWLINE_EXTENT;
  const overview = flow.flowRequestsForView(bounds, [-98.4, 38.5], 5);
  assert.equal(overview.length, 8);
  const area = overview.map(flow.parseFlowRequest).reduce((sum, cell) => sum + (cell.east - cell.cell[0]) * (cell.north - cell.cell[1]), 0);
  near(area, (bounds.east-bounds.west)*(bounds.north-bounds.south), 1e-10, "full envelope, no centre-only coverage");
  for (const key of overview) assert.equal(flow.parseFlowRequest(key).minimumOrder, 5);
  for (const zoom of [7, 8, 9, 10, 15]) assert.ok(flow.flowRequestsForView(bounds, [-98.4, 38.5], zoom).length <= 26);
  assert.ok(flow.flowRequestsForView(bounds, [-98.4, 38.5], 7).some(key => key.startsWith("regional:")));
  for (const bad of ["overview:-97.25,38.00", "regional:-97.00,38.00", "overview:-104.25,36.75", "overview:0,0", "overview:-98.25,38.75&where=1=1"]) assert.equal(flow.parseFlowRequest(bad), null);
  assert.equal(flow.flowReachMinZoom(null), 9);
  assert.equal(flow.flowReachMinZoom(5), 4);
  assert.equal(flow.flowReachMinZoom(3), 7);
  for (const minimum of [4,7,9]) {
    assert.equal(flow.flowZoomOpacity(minimum, minimum), 0);
    assert.equal(flow.flowZoomOpacity(minimum + .5, minimum), .5);
    assert.equal(flow.flowZoomOpacity(minimum + 1, minimum), 1);
    let prior = 0;
    for (let zoom = minimum; zoom < minimum+1; zoom += .01) {
      const opacity = flow.flowZoomOpacity(zoom, minimum);
      assert.ok(opacity >= prior && opacity - prior < .016);
      prior = opacity;
    }
  }
});

test("overview route enforces order and direction independently of provider filtering", async () => {
  const original = globalThis.fetch;
  let seen;
  globalThis.fetch = async url => {
    seen = new URL(url);
    return Response.json({ features: [
      reach("MAJOR", [[-98,38],[-97.99,38]], {streamorder:5}),
      reach("SMALL", [[-98,38],[-97.99,38]], {streamorder:2}),
      reach("UNKNOWN", [[-98,38],[-97.99,38]]),
      reach("REVERSE", [[-98,38],[-97.99,38]], {streamorder:5,flowdirection:0}),
    ] });
  };
  try {
    const response = await GET(request("?cell=overview:-98.25,38.75"));
    assert.equal(response.status,200);
    assert.equal(seen.searchParams.get("geometry"), "-98.25,38.75,-96.25,40.25");
    assert.equal(seen.searchParams.get("maxAllowableOffset"), "0.001");
    assert.match(seen.searchParams.get("where"), /streamorder>=5/);
    assert.match(seen.searchParams.get("outFields"), /streamorder/);
    const payload = flow.parseFlowlinePayload(await response.json());
    assert.deepEqual(payload.reaches.map(r=>r.id), ["MAJOR"]);
    assert.equal(payload.reaches[0].streamOrder,5);
    assert.throws(()=>flow.parseFlowlinePayload({...payload,requestKey:"regional:-98.25,37.75"}));
    assert.throws(()=>flow.parseFlowlinePayload({...payload,reaches:[{...payload.reaches[0],streamOrder:null}]}));
  } finally {globalThis.fetch=original;}
});

test("source order is encoded per reach without changing direction or inventing connectors", () => {
  const base = {sequence:null,downstream:null,levelpath:null,name:null,featureType:1};
  const reaches = [5,3,null].map((streamOrder,i)=>({...base,id:`LOD${i}`,streamOrder,coordinates:[[-98+i*.1,38],[-97.99+i*.1,38]]}));
  const geometry=flow.buildFlowGeometry(reaches,[]);
  assert.equal(geometry.count,3);
  assert.deepEqual([0,1,2].map(i=>geometry.segments[i*flow.FLOW_SEGMENT_FLOATS+12]), [4,7,9]);
  for(let i=0;i<3;i++) {
    const segment=geometry.segments.subarray(i*flow.FLOW_SEGMENT_FLOATS,(i+1)*flow.FLOW_SEGMENT_FLOATS);
    assert.ok(segment[3]>segment[0], "provider eastward order is preserved");
    assert.equal(segment[6],0, "no invented connection across reaches");
    assert.ok(segment[7]>0);
  }
});


test("fractional zoom and reduced motion update uniforms without re-uploading flat geometry", async () => {
  const renderer = await import(await compile("app/water-flow-layer.ts"));
  let uploads=0, draws=0;
  const uniforms={};
  const gl=new Proxy({drawingBufferWidth:1440,drawingBufferHeight:900},{get(target,name){
    if(name in target)return target[name];
    if(name==="bufferData")return ()=>{uploads++;};
    if(name==="getUniformLocation")return (_p,name)=>name;
    if(name==="uniform1f")return (name,value)=>{uniforms[name]=value;};
    if(name==="getShaderParameter"||name==="getProgramParameter")return ()=>true;
    if(name==="getAttribLocation")return ()=>0;
    if(name==="drawArraysInstanced")return ()=>{draws++;};
    return ()=>({});
  }});
  let zoom=5;
  const map={getZoom:()=>zoom,getCenter:()=>({lng:-98,lat:38}),getTerrain:()=>null,on(){},off(){},triggerRepaint(){}};
  const layer=renderer.createWaterFlowLayer({id:"test",clock:()=>null,palette:()=>renderer.WATER_FLOW_PALETTES.clear});
  layer.onAdd(map,gl);
  layer.setGeometry(flow.buildFlowGeometry([{id:"A",sequence:null,downstream:null,levelpath:null,name:null,featureType:1,streamOrder:5,coordinates:[[-98,38],[-97.99,38]]}],[]));
  const afterCornerUpload=uploads;
  for(let i=0;i<60;i++){zoom=5+i*.02;layer.render(gl,{modelViewProjectionMatrix:new Float32Array(16)});}
  assert.equal(uploads-afterCornerUpload,1,"one instance upload across 60 zoom frames");
  assert.equal(draws,60);
  near(uniforms.u_zoom,6.18,1e-10,"current fractional zoom");
  assert.equal(uniforms.u_time,0,"reduced-motion clock remains still");
  assert.equal(layer.segmentCount,1);
  layer.onRemove(map,gl);
});

test("statewide gauge snapping skips distant geometry while retaining the exact nearest-reach rule", t=>{
  const reaches=Array.from({length:200},(_,i)=>({id:`B${i}`,sequence:null,downstream:null,levelpath:null,name:null,featureType:1,streamOrder:5,coordinates:Array.from({length:11},(_,j)=>[-101+i*.03+j*.00001,38])}));
  const cues=Array.from({length:10},(_,i)=>flow.gaugeCue({value:100,readingState:"measured"},reaches[i*15].coordinates[4]));
  const original=Math.sin;
  let calls=0;
  t.mock.method(Math,"sin",value=>{calls++;return original(value);});
  flow.buildFlowGeometry(reaches,[]);const constructionCalls=calls;calls=0;
  const geometry=flow.buildFlowGeometry(reaches,cues);
  assert.equal(geometry.gauged,10);
  assert.ok(calls-constructionCalls<1000,"exact snaps visit nearby segments, not every segment for every gauge");
  for(let i=0;i<cues.length;i++)assert.equal(flow.snapGauge(reaches,cues[i].coordinate).reach,i*15);
});
