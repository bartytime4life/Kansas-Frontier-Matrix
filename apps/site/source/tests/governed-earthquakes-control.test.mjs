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
const helpers = await load("../app/governed-earthquakes-availability.ts");
const source = await read("../app/governed-earthquakes-control.tsx");
const fixture = async name => JSON.parse(await read(`./fixtures/governed-earthquakes/${name}.json`));
const full = await fixture("layers"), allEvidence = await fixture("evidence"), mayLayers = await fixture("layers-may");
const MAY = 5;
const month = (m, layers = mayLayers, evidence = allEvidence) => {
  const l = structuredClone(layers), e = structuredClone(evidence);
  e.data.entries = e.data.entries.filter(x => x.month === m);
  for (const response of [l, e]) response.data.approval_expires_at = "2099-01-01T00:00:00Z";
  return { layers: l, evidence: e };
};

test("evidence binds every part of the selected month to its records in the same release", () => {
  const { layers, evidence } = month(MAY);
  assert.equal(helpers.earthquakeEvidenceMatchesSelection(mayLayers, evidence, MAY), false, "approval expiry differs");
  assert.equal(helpers.earthquakeEvidenceMatchesSelection(layers, evidence, MAY), true);
  assert.equal(helpers.earthquakeExportMatchesSelection(layers, evidence, MAY), true);
  assert.equal(helpers.earthquakeEvidenceMatchesSelection(layers, evidence, 4), false);
  const swapped = structuredClone(evidence); swapped.data.package_id = "sha256:" + "0".repeat(64);
  assert.equal(helpers.earthquakeEvidenceMatchesSelection(layers, swapped, MAY), false);
  const dropped = structuredClone(layers); dropped.data.observations.pop();
  assert.equal(helpers.earthquakeEvidenceMatchesSelection(dropped, evidence, MAY), false);
  const noParts = structuredClone(evidence); noParts.data.entries = [];
  assert.equal(helpers.earthquakeEvidenceMatchesSelection(layers, noParts, MAY), false);
  const relabeled = structuredClone(evidence); relabeled.data.entries[0].part = 2;
  assert.equal(helpers.earthquakeEvidenceMatchesSelection(layers, relabeled, MAY), false);
  const measured = structuredClone(evidence); measured.data.entries[0].bundle.evidence_refs[1].kind = "measurement";
  assert.equal(helpers.earthquakeEvidenceMatchesSelection(layers, measured, MAY), false);
  const otherFamily = structuredClone(evidence); otherFamily.data.entries[0].evidence_ref.ref = "kfm://hazards/storm-events/2025-05/part-1/x";
  assert.equal(helpers.earthquakeEvidenceMatchesSelection(layers, otherFamily, MAY), false);
  const cited = structuredClone(evidence); cited.data.entries[0].bundle.citations[0] = "https://elsewhere.example/";
  assert.equal(helpers.earthquakeEvidenceMatchesSelection(layers, cited, MAY), false);
  // The full-year layer carries other months, so it can never pass as one month's export.
  const year = { ...full, data: { ...full.data, approval_expires_at: "2099-01-01T00:00:00Z" } };
  assert.equal(helpers.earthquakeExportMatchesSelection(year, evidence, MAY), false);
});

test("responses classify without stations, and a missing magnitude is never shown as zero", () => {
  assert.equal(helpers.earthquakeBrowserStateForResponse(full, true), "received");
  assert.equal(helpers.earthquakeBrowserStateForResponse({ envelope: { outcome: "ANSWER" }, data: { months: [5] } }, true), "received");
  assert.equal(helpers.earthquakeBrowserStateForResponse({ envelope: { outcome: "ABSTAIN", reason_code: "NO_APPROVED_SNAPSHOT" } }, true), "no-release");
  assert.equal(helpers.earthquakeBrowserStateForResponse(full, false), "unavailable");
  assert.equal(helpers.earthquakeMagnitudeText(null, null), "Not reported");
  assert.equal(helpers.earthquakeMagnitudeText(2.6, "ml"), "M 2.6 ml");
  assert.equal(helpers.earthquakeMagnitudeText(0, "md"), "M 0 md");
  // Every epicenter is drawn; margin points are marked so the map can draw them hollow.
  const points = helpers.earthquakePoints(full.data.observations);
  assert.equal(points.length, full.data.observations.length);
  assert.deepEqual(points.filter(p => p.properties.margin).map(p => p.properties.eventId), ["ok2025p005"]);
  assert.equal(points.find(p => p.properties.eventId === "us7000p006").properties.magnitude, -1);
});

function harness(initial) {
  const requests = [], downloads = [], statuses = [];
  let stateIndex = 0;
  const hooks = {
    useState(value) {
      const index = stateIndex++;
      const preset = { 0: initial, 6: MAY, 10: [1, 2, 5] };
      return [index in preset ? preset[index] : typeof value === "function" ? value() : value, next => { if (index === 9) statuses.push(next); }];
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
      if (name === "./governed-earthquakes-availability") return helpers;
      if (name === "./governed-water") return { approvalRemainingMs: expiry => Date.parse(expiry) - Date.now() };
      if (name === "./bounded-json") return { readBoundedJson: async response => response };
      throw new Error(`Unexpected import ${name}`);
    },
    fetch: url => new Promise(resolve => requests.push({ url, resolve })),
    AbortController, AbortSignal, Blob, Date, setTimeout: () => 0, clearTimeout() {},
    URL: { createObjectURL: () => "blob:test", revokeObjectURL() {} },
    document: { createElement: () => ({ click() { downloads.push(this.download); } }) },
  });
  const tree = exports.GovernedEarthquakesControl({ mapRef: { current: null }, styleReady: false });
  const text = [];
  function find(node, predicate) {
    if (typeof node === "string" || typeof node === "number") text.push(String(node));
    if (!node || typeof node !== "object") return;
    if (predicate(node)) return node;
    for (const child of [node.props?.children].flat(Infinity)) { const result = find(child, predicate); if (result) return result; }
  }
  const select = find(tree, node => node.type === "select");
  const button = find(tree, node => node.type === "button" && node.props.children === "Export selected month with evidence");
  find(tree, () => false);
  const request = pattern => requests.find(r => pattern.test(r.url));
  return { requests, request, downloads, statuses, text: text.join(" "),
    choose: m => select.props.onChange({ target: { value: String(m) } }), start: () => button.props.onClick() };
}
const settle = async () => { for (let i = 0; i < 10; i++) await Promise.resolve(); };

test("the control lists the month's earthquakes as catalog solutions, and exports one month's evidence from the earthquake routes", async () => {
  const { layers, evidence } = month(MAY);
  const h = harness(layers);
  assert.match(h.text, /Catalog solutions, not shaking estimates or alerts/);
  assert.match(h.text, /not the state boundary/);
  assert.match(h.text, /M 2\.8 ml/);
  assert.match(h.text, /outside Kansas rectangle/);
  assert.match(h.text, /Not reported/, "a missing depth or magnitude is unreported");
  h.start();
  assert.match(h.requests[0].url, /^\/api\/governed\/earthquakes\/v1\/layers\?month=5$/);
  h.requests[0].resolve(layers); await settle();
  assert.match(h.requests[1].url, /^\/api\/governed\/earthquakes\/v1\/evidence\?month=5$/);
  h.requests[1].resolve(evidence); await settle();
  assert.deepEqual(h.downloads, ["kfm-reviewed-earthquakes-2025-05.json"]);
  assert.match(h.statuses.at(-1), /^Export includes/);
});

test("changing month during an export withholds the download", async () => {
  const { layers, evidence } = month(MAY);
  const h = harness(layers); h.start();
  h.choose(2); h.choose(MAY);
  h.request(/layers\?month=5$/).resolve(layers); await settle();
  h.request(/evidence\?month=5$/).resolve(evidence); await settle();
  assert.deepEqual(h.downloads, []);
  assert.match(h.statuses.at(-1), /^Export withheld:/);
});

test("a full-year response cannot be exported as one month", async () => {
  const { evidence } = month(MAY);
  const year = { ...full, data: { ...full.data, approval_expires_at: "2099-01-01T00:00:00Z" } };
  const h = harness(year); h.start();
  h.requests[0].resolve(year); await settle();
  h.requests[1].resolve(evidence); await settle();
  assert.deepEqual(h.downloads, []);
  assert.match(h.statuses.at(-1), /^Export withheld:/);
});
