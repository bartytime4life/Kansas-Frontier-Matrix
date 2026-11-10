import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import { pathToFileURL } from "node:url";
import ts from "typescript";
import { componentHarness, findNode } from "./component-harness.mjs";

const compile = source => ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const pure = async file => "data:text/javascript;base64," + Buffer.from(compile(await readFile(file, "utf8"))).toString("base64");
const flow = await import(await pure("app/streamflow.ts")), water = await import(await pure("app/water-flow-context.ts"));
const routeSource = compile(await readFile("app/api/hydrology/streamflow/route.ts", "utf8"))
  .replace('import { env } from "cloudflare:workers";', 'const env = { USGS_WATER_API_KEY: "synthetic-test-key" };')
  .replace('from "../../../streamflow-transport"', `from ${JSON.stringify(await pure("app/streamflow-transport.ts"))}`)
  .replace('from "../../../bounded-json"', `from ${JSON.stringify(await pure("app/bounded-json.ts"))}`)
  .replace('from "next/server"', `from ${JSON.stringify(pathToFileURL(path.resolve("node_modules/next/server.js")).href)}`);
const NOW = "2026-11-10T04:00:00.000Z", EARLIER = "2026-11-10T03:30:00.000Z", LATER = "2026-11-10T03:45:00.000Z", ID = "USGS-06864500";
const clock = `const Date = class extends globalThis.Date { constructor(...args) { super(...(args.length ? args : [${JSON.stringify(NOW)}])); } static now() { return globalThis.Date.parse(${JSON.stringify(NOW)}); } };\n`;
let serial = 0;
const textOf = node => typeof node === "string" || typeof node === "number" ? String(node) : node && typeof node === "object" ? [node.props?.children].flat(Infinity).map(textOf).join(" ").replace(/\s+/g, " ") : "";

async function fixture(rows) {
  const originalFetch = globalThis.fetch, requests = [];
  // Deny all transport during framework bootstrap and every unexpected fixture request.
  globalThis.fetch = async () => { throw new Error("No transport during fixture import"); };
  let body;
  try {
    const { GET } = await import("data:text/javascript;base64," + Buffer.from(clock + routeSource + `\n// unit fixture ${++serial}`).toString("base64"));
    globalThis.fetch = async input => {
      const url = new URL(input); requests.push(url.pathname);
      assert.equal(url.origin, "https://api.waterdata.usgs.gov");
      const collection = features => Response.json({ type: "FeatureCollection", features, numberReturned: features.length, links: [], timeStamp: NOW });
      if (url.pathname.endsWith("/monitoring-locations/items")) return collection([{ type: "Feature", id: ID, geometry: { type: "Point", coordinates: [-98, 38] }, properties: {
        id: ID, agency_code: "USGS", monitoring_location_number: ID.slice(5), monitoring_location_name: "SYNTHETIC UNIT CHECK", site_type_code: "ST", hydrologic_unit_code: null, county_name: null, drainage_area: null, contributing_drainage_area: null,
      } }]);
      if (url.pathname.endsWith("/continuous/items")) return collection(rows.map((row, index) => ({ type: "Feature", id: String(index), geometry: { type: "Point", coordinates: [-98, 38] }, properties: {
        time_series_id: "synthetic-unit-series", monitoring_location_id: ID, parameter_code: "00060", statistic_id: "00011", approval_status: "Provisional", qualifier: null, last_modified: row.time, ...row,
      } })));
      throw new Error(`Unexpected fixture request ${url}`);
    };
    const response = await GET({ nextUrl: new URL(`https://synthetic.test/api/hydrology/streamflow?mode=station&station=${ID}&range=24h&parameter=00060`) });
    assert.equal(response.status, 200); body = await response.json(); assert.equal(requests.length, 2);
  } finally { globalThis.fetch = originalFetch; }
  const bundle = flow.parseStreamflowBundle(body);
  assert.equal(bundle.observations.length, rows.length, "the adapter and parser retain every raw fixture row");
  const h = await componentHarness("app/hydrology-observatory.tsx", {
    "./streamflow": flow, "./water-flow-context": water,
    "./river-network-signal": { RiverNetworkSignal: () => null }, "./river-pulse-visuals": { nearestRiverSample: () => 0 }, "./water-terrain-profile": { WaterTerrainProfile: () => null },
  });
  const noop = () => {};
  let cursor = EARLIER;
  const render = next => {
    cursor = next ?? cursor;
    const frame = flow.buildStreamflowFrame(bundle, cursor, 60);
    const tree = h.render(h.exports.HydrologyObservatory, { bundle, state: "ready", error: null, frame, frameIndex: cursor === EARLIER ? 0 : 1, selectedStationId: ID,
      playing: false, speed: 1, range: "24h", reducedMotion: true, downstreamState: "idle", downstreamPathCount: 0,
      onClose: noop, onRefresh: noop, onTogglePlay: noop, onStep: noop, onSeek: noop, onJumpLatest: noop, onSpeed: noop, onRange: noop, onSelectStation: noop, onShowDirection: noop,
    });
    return tree;
  };
  return { bundle, h, render, card: tree => textOf(findNode(tree, node => node.props?.className === "hydrology-water-reading-head")), probe: tree => findNode(tree, node => node.props?.className === "river-sample-probe") };
}

for (const [name, patch] of [["different units", { unit_of_measure: "m^3/s" }], ["different statistics", { statistic_id: "00003" }], ["unqualified statistic", { statistic_id: null }]]) test(`route → parser → River UI withholds ${name} comparisons and preserves raw inspection`, async () => {
  const f = await fixture([{ time: EARLIER, value: 100, unit_of_measure: "ft^3/s" }, { time: LATER, value: 5, unit_of_measure: "ft^3/s", ...patch }]);
  try {
    const untouched = JSON.stringify(f.bundle);
    let tree = f.render(); assert.match(f.card(tree), /100 ft³\/s/); assert.doesNotMatch(f.card(tree), /100 m\^3\/s/);
    assert.match(textOf(tree), /Comparison withheld.*Raw observations remain available/);
    assert.equal(findNode(tree, node => node.props?.className === "hydrology-chart"), undefined);
    assert.equal(findNode(tree, node => node.props?.role === "meter"), undefined);
    assert.match(textOf(f.probe(tree)), /100 ft³\/s/);
    findNode(tree, node => node.props?.["aria-label"] === "Inspect exact station sample").props.onChange({ target: { value: "1" } });
    tree = f.render(); assert.match(textOf(f.probe(tree)), patch.unit_of_measure ? /5 m\^3\/s/ : /5 ft³\/s/);
    tree = f.render(LATER); assert.match(f.card(tree), patch.unit_of_measure ? /5 m\^3\/s/ : /5 ft³\/s/);
    assert.equal(JSON.stringify(f.bundle), untouched, "rendering never converts or drops the source observations");
  } finally { f.h.dispose(); }
});

test("a fully compatible route series keeps its chart, range and exact zero", async () => {
  const f = await fixture([{ time: EARLIER, value: 0, unit_of_measure: "ft^3/s" }, { time: LATER, value: 100, unit_of_measure: "ft^3/s" }]);
  try {
    let tree = f.render(); assert.match(f.card(tree), /0 ft³\/s/); assert.match(textOf(tree), /MEASURED ZERO/);
    assert.ok(findNode(tree, node => node.props?.className === "hydrology-chart")); assert.ok(findNode(tree, node => node.props?.role === "meter"));
    assert.doesNotMatch(textOf(tree), /Comparison withheld/);
    tree = f.render(LATER); assert.match(f.card(tree), /100 ft³\/s/); assert.match(textOf(tree), /Rising by 100 ft³\/s/);
  } finally { f.h.dispose(); }
});

test("null and zero rows remain distinct and inspectable while mixed comparisons are withheld", async () => {
  const f = await fixture([{ time: EARLIER, value: 0, unit_of_measure: "ft^3/s" }, { time: LATER, value: null, unit_of_measure: "m^3/s" }]);
  try {
    let tree = f.render(); assert.match(f.card(tree), /0 ft³\/s/); assert.match(textOf(tree), /MEASURED ZERO/);
    tree = f.render(LATER); assert.match(f.card(tree), /No reading at this frame/);
    findNode(tree, node => node.props?.["aria-label"] === "Inspect exact station sample").props.onChange({ target: { value: "1" } });
    tree = f.render(); assert.match(textOf(f.probe(tree)), /not reported.*Missing value/);
    assert.deepEqual(f.bundle.observations.map(row => row.value), [0, null]);
  } finally { f.h.dispose(); }
});
