import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import vm from "node:vm";
import ts from "typescript";

const read = path => readFile(new URL(path, import.meta.url), "utf8");
const compiled = text => ts.transpileModule(text, { compilerOptions: {
  module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022, jsx: ts.JsxEmit.ReactJSX,
} }).outputText;
const load = async path => { const exports = {}; vm.runInNewContext(compiled(await read(path)), { exports }); return exports; };
const waterHelpers = await load("../app/governed-water-availability.ts");
const helpers = await load("../app/governed-weather-availability.ts");
const source = await read("../app/governed-weather-control.tsx");
const station = "USW00003928", other = "USW00013996";
const fixture = async name => JSON.parse(await read(`./fixtures/governed-weather/${name}.json`));
const full = await fixture("layers"), allEvidence = await fixture("evidence");
const only = (id, layers = full, evidence = allEvidence) => {
  const l = structuredClone(layers), e = structuredClone(evidence);
  l.data.stations = l.data.stations.filter(s => s.id === id);
  l.data.observations = l.data.observations.filter(o => o.station_id === id);
  e.data.entries = e.data.entries.filter(x => x.station_id === id);
  for (const response of [l, e]) response.data.approval_expires_at = "2099-01-01T00:00:00Z";
  return { layers: l, evidence: e };
};

test("evidence binds to the selected station's observations in the same release", () => {
  const { layers, evidence } = only(station, full, allEvidence);
  assert.equal(helpers.weatherEvidenceMatchesSelection(full, only(station, full, allEvidence).evidence, station), false, "approval expiry differs");
  assert.equal(helpers.weatherEvidenceMatchesSelection(layers, evidence, station), true);
  assert.equal(helpers.weatherExportMatchesSelection(layers, evidence, station), true);
  assert.equal(helpers.weatherEvidenceMatchesSelection(layers, evidence, other), false);
  const swapped = structuredClone(evidence); swapped.data.package_id = "sha256:" + "0".repeat(64);
  assert.equal(helpers.weatherEvidenceMatchesSelection(layers, swapped, station), false);
  const dropped = structuredClone(layers); dropped.data.observations.pop();
  assert.equal(helpers.weatherEvidenceMatchesSelection(dropped, evidence, station), false);
  const water = structuredClone(evidence); water.data.entries[0].evidence_ref.ref = `kfm://water/station/${station}/x`;
  assert.equal(helpers.weatherEvidenceMatchesSelection(layers, water, station), false);
  // The full layer carries every station, so it can never pass as one station's export.
  assert.equal(helpers.weatherExportMatchesSelection({ ...full, data: { ...full.data, approval_expires_at: "2099-01-01T00:00:00Z" } }, evidence, station), false);
});

test("the latest station-local day shows withheld values as withheld, never as zero", () => {
  const day = helpers.latestWeatherDay(full.data.observations, station);
  assert.equal(day.date, "2026-10-10");
  assert.equal(day.values.TMAX.withheld, "QUALITY_FLAG");
  assert.equal(helpers.weatherValueText(day.values.TMAX), "Withheld (failed provider quality check)");
  assert.equal(day.withheld, 1);
  assert.equal(helpers.weatherValueText({ withheld: "MISSING", value: null }), "Withheld (missing)");
  assert.equal(helpers.weatherValueText({ withheld: null, value: 0, trace: true, unit: "mm" }), "Trace");
  assert.equal(helpers.weatherValueText({ withheld: null, value: 21.7, trace: false, unit: "degC" }), "21.7 °C");
  assert.equal(helpers.weatherValueText(undefined), "Not reported");
  assert.equal(helpers.latestWeatherDay(full.data.observations, "USW99999999"), null);
});

function harness(initial) {
  const requests = [], downloads = [], statuses = [];
  let stateIndex = 0;
  const hooks = {
    useState(value) {
      const index = stateIndex++;
      return [index === 0 ? initial : typeof value === "function" ? value() : value, next => { if (index === 9) statuses.push(next); }];
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
      if (name === "./governed-water-availability") return waterHelpers;
      if (name === "./governed-weather-availability") return helpers;
      if (name === "./governed-water") return { approvalRemainingMs: expiry => Date.parse(expiry) - Date.now() };
      if (name === "./bounded-json") return { readBoundedJson: async response => response };
      throw new Error(`Unexpected import ${name}`);
    },
    fetch: url => new Promise(resolve => requests.push({ url, resolve })),
    AbortSignal, Blob, Date, setTimeout: () => 0,
    URL: { createObjectURL: () => "blob:test", revokeObjectURL() {} },
    document: { createElement: () => ({ click() { downloads.push(this.download); } }) },
  });
  const tree = exports.GovernedWeatherControl({ mapRef: { current: null }, styleReady: false });
  const text = [];
  function find(node, predicate) {
    if (typeof node === "string") text.push(node);
    if (!node || typeof node !== "object") return;
    if (predicate(node)) return node;
    for (const child of [node.props?.children].flat(Infinity)) { const result = find(child, predicate); if (result) return result; }
  }
  const select = find(tree, node => node.type === "select");
  const button = find(tree, node => node.type === "button" && node.props.children === "Export selected station with evidence");
  find(tree, () => false);
  return { requests, downloads, statuses, text: text.join(" "),
    choose: id => select.props.onChange({ target: { value: id } }), start: () => button.props.onClick() };
}
const settle = async () => { for (let i = 0; i < 10; i++) await Promise.resolve(); };

test("the control renders withheld values and exports one station's evidence from the weather routes", async () => {
  const { layers, evidence } = only(station);
  const h = harness(layers);
  assert.match(h.text, /Withheld \(failed provider quality check\)/);
  assert.match(h.text, /Preliminary provider data/);
  h.start();
  assert.match(h.requests[0].url, /^\/api\/governed\/weather\/v1\/layers\?station_id=USW00003928$/);
  h.requests[0].resolve(layers); await settle();
  assert.match(h.requests[1].url, /^\/api\/governed\/weather\/v1\/evidence\?station_id=USW00003928$/);
  h.requests[1].resolve(evidence); await settle();
  assert.deepEqual(h.downloads, [`kfm-reviewed-weather-${station}.json`]);
  assert.match(h.statuses.at(-1), /^Export includes/);
});

test("changing station during an export withholds the download", async () => {
  const { layers, evidence } = only(station);
  const h = harness(layers); h.start();
  h.choose(other); h.choose(station);
  h.requests[0].resolve(layers); await settle();
  h.requests[1].resolve(evidence); await settle();
  assert.deepEqual(h.downloads, []);
  assert.match(h.statuses.at(-1), /^Export withheld:/);
});
