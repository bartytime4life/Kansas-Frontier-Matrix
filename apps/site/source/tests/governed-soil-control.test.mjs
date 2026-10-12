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
const helpers = await load("../app/governed-soil-availability.ts");
const source = await read("../app/governed-soil-control.tsx");
const station = "53974", other = "03067";
const fixture = async name => JSON.parse(await read(`./fixtures/governed-soil/${name}.json`));
const full = await fixture("layers"), allEvidence = await fixture("evidence");
const only = (id, layers = full, evidence = allEvidence) => {
  const l = structuredClone(layers), e = structuredClone(evidence);
  l.data.stations = l.data.stations.filter(s => s.id === id);
  l.data.observations = l.data.observations.filter(o => o.station_id === id);
  e.data.entries = e.data.entries.filter(x => x.station_id === id);
  for (const response of [l, e]) response.data.approval_expires_at = "2099-01-01T00:00:00Z";
  return { layers: l, evidence: e };
};

test("evidence binds the selected station's five depth bundles to its observations in the same release", () => {
  const { layers, evidence } = only(station);
  assert.equal(helpers.soilEvidenceMatchesSelection(full, evidence, station), false, "approval expiry differs");
  assert.equal(helpers.soilEvidenceMatchesSelection(layers, evidence, station), true);
  assert.equal(helpers.soilExportMatchesSelection(layers, evidence, station), true);
  assert.equal(helpers.soilEvidenceMatchesSelection(layers, evidence, other), false);
  const swapped = structuredClone(evidence); swapped.data.package_id = "sha256:" + "0".repeat(64);
  assert.equal(helpers.soilEvidenceMatchesSelection(layers, swapped, station), false);
  const dropped = structuredClone(layers); dropped.data.observations.pop();
  assert.equal(helpers.soilEvidenceMatchesSelection(dropped, evidence, station), false);
  const missingDepth = structuredClone(evidence); missingDepth.data.entries.pop();
  assert.equal(helpers.soilEvidenceMatchesSelection(layers, missingDepth, station), false);
  const reordered = structuredClone(evidence); reordered.data.entries.reverse();
  assert.equal(helpers.soilEvidenceMatchesSelection(layers, reordered, station), false);
  const weather = structuredClone(evidence); weather.data.entries[0].evidence_ref.ref = `kfm://weather/station/${station}/x`;
  assert.equal(helpers.soilEvidenceMatchesSelection(layers, weather, station), false);
  // The full layer carries both stations, so it can never pass as one station's export.
  assert.equal(helpers.soilExportMatchesSelection({ ...full, data: { ...full.data, approval_expires_at: "2099-01-01T00:00:00Z" } }, evidence, station), false);
});

test("the latest day shows withheld values as withheld, never as zero", () => {
  const day = helpers.latestSoilDay(full.data.observations, station);
  assert.equal(day.date, "2026-10-10");
  const oakley = helpers.latestSoilDay(full.data.observations, other);
  assert.equal(oakley.date, "2026-10-10");
  assert.equal(helpers.soilValueText(oakley.moisture[5]), "Withheld (missing)");
  assert.match(helpers.soilValueText(oakley.temperature[5]), /^-?\d+\.\d °C$/);
  assert.equal(helpers.soilValueText({ withheld: "OUT_OF_RANGE", value: null }), "Withheld (outside the physical range)");
  assert.equal(helpers.soilValueText({ withheld: null, value: 0.28, unit: "m3/m3" }), "0.280 m³/m³");
  assert.equal(helpers.soilValueText({ withheld: null, value: 21, unit: "degC" }), "21.0 °C");
  assert.equal(helpers.soilValueText(undefined), "Not reported");
  assert.equal(helpers.latestSoilDay(full.data.observations, "99999"), null);
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
      if (name === "./governed-soil-availability") return helpers;
      if (name === "./governed-water") return { approvalRemainingMs: expiry => Date.parse(expiry) - Date.now() };
      if (name === "./bounded-json") return { readBoundedJson: async response => response };
      throw new Error(`Unexpected import ${name}`);
    },
    fetch: url => new Promise(resolve => requests.push({ url, resolve })),
    AbortSignal, Blob, Date, setTimeout: () => 0,
    URL: { createObjectURL: () => "blob:test", revokeObjectURL() {} },
    document: { createElement: () => ({ click() { downloads.push(this.download); } }) },
  });
  const tree = exports.GovernedSoilControl({ mapRef: { current: null }, styleReady: false });
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


test("the control renders depth values and exports one station's evidence from the soil routes", async () => {
  const { layers, evidence } = only(station);
  const h = harness(layers);
  assert.match(h.text, /2026-10-10/);
  assert.match(h.text, /values may be revised/);
  assert.match(h.text, /Depth Soil moisture Soil temperature/);
  assert.match(h.text, /\d\.\d{3} m³\/m³/);
  h.start();
  assert.match(h.requests[0].url, /^\/api\/governed\/soil\/v1\/layers\?station_id=53974$/);
  h.requests[0].resolve(layers); await settle();
  assert.match(h.requests[1].url, /^\/api\/governed\/soil\/v1\/evidence\?station_id=53974$/);
  h.requests[1].resolve(evidence); await settle();
  assert.deepEqual(h.downloads, [`kfm-reviewed-soil-${station}.json`]);
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
