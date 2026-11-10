import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import vm from "node:vm";
import ts from "typescript";

const source = await readFile(new URL("../app/governed-water-control.tsx", import.meta.url), "utf8");
const availability = await readFile(new URL("../app/governed-water-availability.ts", import.meta.url), "utf8");
const compiled = text => ts.transpileModule(text, { compilerOptions: {
  module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022, jsx: ts.JsxEmit.ReactJSX,
} }).outputText;
const helpers = { exports: {} };
vm.runInNewContext(compiled(availability), { exports: helpers.exports });
const water = { exports: {} };
vm.runInNewContext(compiled(await readFile(new URL("../app/governed-water.ts", import.meta.url), "utf8")), { exports: water.exports });
const bounded = { exports: {} };
vm.runInNewContext(compiled(await readFile(new URL("../app/bounded-json.ts", import.meta.url), "utf8")), { exports: bounded.exports, TextDecoder });
const station = "USGS-06892518";
const layers = JSON.parse(await readFile(new URL("./fixtures/governed-water/layers.json", import.meta.url), "utf8"));
const evidence = JSON.parse(await readFile(new URL("./fixtures/governed-water/evidence.json", import.meta.url), "utf8"));
for (const response of [layers, evidence]) response.data.approval_expires_at = "2099-01-01T00:00:00Z";
layers.data.stations = layers.data.stations.filter(s => s.id === station);
layers.data.observations = layers.data.observations.filter(s => s.station_id === station);
evidence.data.entries = evidence.data.entries.filter(s => s.station_id === station);

function harness() {
  const requests = [], downloads = [], statuses = [], effects = [], updates = [], reads = [];
  let stateIndex = 0;
  const hooks = {
    useState(initial) {
      const index = stateIndex++;
      const value = index === 0 ? layers : typeof initial === "function" ? initial() : initial;
      return [value, next => { updates.push({ index, value: next }); if (index === 9) statuses.push(next); }];
    },
    useRef: current => ({ current }), useCallback: fn => fn, useEffect: fn => effects.push(fn),
  };
  const jsx = (type, props) => ({ type, props });
  const exports = {};
  vm.runInNewContext(compiled(source), {
    exports,
    require(name) {
      if (name === "react") return hooks;
      if (name === "react/jsx-runtime") return { jsx, jsxs: jsx, Fragment: "fragment" };
      if (name === "./governed-water-availability") return helpers.exports;
      if (name === "./governed-water") return water.exports;
      if (name === "./bounded-json") return { readBoundedJson: (response, limit) => { reads.push(response); return bounded.exports.readBoundedJson(response, limit); } };
      throw new Error(`Unexpected import ${name}`);
    },
    fetch: url => new Promise(resolve => requests.push({ url, resolve: (value, status = 200) => resolve(value instanceof Response ? value : Response.json(value, { status })) })),
    AbortController, AbortSignal, Blob, Date, setTimeout: () => 0, clearTimeout() {},
    URL: { createObjectURL: () => "blob:test", revokeObjectURL() {} },
    document: { createElement: () => ({ click() { downloads.push(this.download); } }) },
  });
  const tree = exports.GovernedWaterControl({ mapRef: { current: null }, styleReady: false });
  function find(node, predicate) {
    if (!node || typeof node !== "object") return;
    if (predicate(node)) return node;
    for (const child of [node.props?.children].flat(Infinity)) {
      const result = find(child, predicate); if (result) return result;
    }
  }
  const select = find(tree, node => node.type === "select");
  const button = find(tree, node => node.type === "button" && node.props.children === "Export selected station with evidence");
  return { requests, downloads, statuses, reads, updates,
    checkEvidence: () => effects.at(-1)(),
    choose: id => select.props.onChange({ target: { value: id } }),
    start: () => button.props.onClick(),
  };
}
async function settle() { for (let i = 0; i < 40; i++) await Promise.resolve(); }

for (const stage of [0, 1]) test(`A→B→A during export request ${stage + 1} withholds the download`, async () => {
  const h = harness(); h.start();
  assert.equal(h.requests.length, 1);
  if (stage === 1) { h.requests[0].resolve(layers); await settle(); }
  h.choose("USGS-07156900"); h.choose(station);
  if (stage === 0) { h.requests[0].resolve(layers); await settle(); }
  assert.equal(h.requests.length, 2);
  assert.match(h.requests[0].url, /layers\?station_id=USGS-06892518$/);
  assert.match(h.requests[1].url, /evidence\?station_id=USGS-06892518$/);
  h.requests[1].resolve(evidence); await settle();
  assert.deepEqual(h.downloads, []);
  assert.match(h.statuses.at(-1), /^Export withheld:/);
});

test("unchanged selection, including reselecting A, permits a valid export", async () => {
  const h = harness(); h.start(); h.choose(station);
  h.requests[0].resolve(layers); await settle();
  h.requests[1].resolve(evidence); await settle();
  assert.deepEqual(h.downloads, [`kfm-reviewed-water-${station}.json`]);
  assert.match(h.statuses.at(-1), /^Export includes/);
});

for (const status of [302, 401, 403, 404, 409, 429, 500, 503]) for (const stage of [0, 1]) test(`water export withholds HTTP ${status} from ${stage ? "evidence" : "layers"} despite matching JSON`, async () => {
  const h = harness(); h.start();
  if (stage) { h.requests[0].resolve(layers); await settle(); }
  const response = Response.json(stage ? evidence : layers, { status });
  h.requests[stage].resolve(response); await settle();
  assert.equal(h.requests.length, stage + 1, "no further request follows a failed response");
  assert.equal(h.reads.length, stage, "the failed response body is never parsed as reviewed data");
  assert.equal(response.bodyUsed, true, "unused failed response is canceled");
  assert.equal(response.body.locked, false);
  assert.deepEqual(h.downloads, []);
  assert.match(h.statuses.at(-1), /^Export withheld:/);
});

test("water station evidence accepts HTTP 200 but withholds every failed HTTP response", async () => {
  for (const status of [200, 302, 401, 403, 404, 409, 429, 500, 503]) {
    const h = harness(), cleanup = h.checkEvidence();
    assert.equal(h.requests.length, 1); assert.match(h.requests[0].url, /evidence\?station_id=USGS-06892518$/);
    const response = Response.json(evidence, { status }); h.requests[0].resolve(response); await settle();
    const records = h.updates.filter(update => update.index === 8);
    if (status === 200) {
      assert.equal(h.reads.length, 1); assert.equal(records.at(-1).value.stationId, station);
      assert.equal(records.at(-1).value.value.data.package_id, evidence.data.package_id);
    } else {
      assert.equal(h.reads.length, 0); assert.ok(records.every(update => update.value === null));
      assert.equal(h.updates.findLast(update => update.index === 0).value, null);
      assert.equal(h.updates.findLast(update => update.index === 4).value, "unavailable");
      assert.match(h.updates.findLast(update => update.index === 1).value, /Evidence request unavailable/);
      assert.equal(response.bodyUsed, true); assert.equal(response.body.locked, false);
    }
    assert.deepEqual(h.downloads, []); cleanup();
  }
});
