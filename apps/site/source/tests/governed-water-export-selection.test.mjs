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
const station = "USGS-06892518";
const layers = JSON.parse(await readFile(new URL("./fixtures/governed-water/layers.json", import.meta.url), "utf8"));
const evidence = JSON.parse(await readFile(new URL("./fixtures/governed-water/evidence.json", import.meta.url), "utf8"));
for (const response of [layers, evidence]) response.data.approval_expires_at = "2099-01-01T00:00:00Z";
layers.data.stations = layers.data.stations.filter(s => s.id === station);
layers.data.observations = layers.data.observations.filter(s => s.station_id === station);
evidence.data.entries = evidence.data.entries.filter(s => s.station_id === station);

function harness() {
  const requests = [], downloads = [], statuses = [];
  let stateIndex = 0;
  const hooks = {
    useState(initial) {
      const index = stateIndex++;
      const value = index === 0 ? layers : typeof initial === "function" ? initial() : initial;
      return [value, next => { if (index === 9) statuses.push(next); }];
    },
    useRef: current => ({ current }), useCallback: fn => fn, useEffect() {},
  };
  const jsx = (type, props) => ({ type, props });
  const exports = {};
  vm.runInNewContext(compiled(source), {
    exports,
    require(name) {
      if (name === "react") return hooks;
      if (name === "react/jsx-runtime") return { jsx, jsxs: jsx, Fragment: "fragment" };
      if (name === "./governed-water-availability") return helpers.exports;
      if (name === "./governed-water") return { approvalRemainingMs: expiry => Date.parse(expiry) - Date.now() };
      if (name === "./bounded-json") return { readBoundedJson: async response => response };
      throw new Error(`Unexpected import ${name}`);
    },
    fetch: url => new Promise(resolve => requests.push({ url, resolve })),
    AbortSignal, Blob, Date, setTimeout: () => 0,
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
  return { requests, downloads, statuses,
    choose: id => select.props.onChange({ target: { value: id } }),
    start: () => button.props.onClick(),
  };
}
async function settle() { for (let i = 0; i < 10; i++) await Promise.resolve(); }

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
