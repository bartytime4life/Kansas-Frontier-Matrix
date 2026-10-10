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
  assert.deepEqual(flow.flowCellsForView(bounds, [-97.5, 38], 9.5), [], "too far out");
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
  assert.ok(layerModule.flowHalfWidth(20) <= 6 && layerModule.flowHalfWidth(5) >= 1.4);
  near(layerModule.metersPerPixel(0, 0), 2 * Math.PI * 6378137 / 512, 1e-6, "metres per pixel at the equator, zoom 0");
  const layer = layerModule.createWaterFlowLayer({ id: "w", clock: () => null, palette: () => layerModule.WATER_FLOW_PALETTES.night });
  assert.equal(layer.type, "custom");
  assert.equal(layer.renderingMode, "3d", "depth-tested so hills hide the water behind them");
  assert.equal(layer.segmentCount, 0);
  assert.doesNotThrow(() => layer.render({}, {}), "render before onAdd is a no-op");
});
