import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import vm from "node:vm";
import ts from "typescript";
import "./cloudflare-register.mjs";

const proof = JSON.parse(await readFile(new URL("../app/living-waters-proof.json", import.meta.url), "utf8"));
const compile = source => ts.transpileModule(source, { compilerOptions: {
  module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022, jsx: ts.JsxEmit.ReactJSX, esModuleInterop: true,
} }).outputText;
const exports = {};
vm.runInNewContext(compile(await readFile(new URL("../app/living-waters-fixture.ts", import.meta.url), "utf8")), {
  exports, require(name) { assert.equal(name, "./living-waters-proof.json"); return proof; },
  fetch() { throw new Error("No provider I/O permitted"); },
});
const { projectLivingWaters, bindLivingWaters, LIVING_WATERS_SOURCE, LIVING_WATERS_LAYERS } = exports;
const plain = value => JSON.parse(JSON.stringify(value));

for (const [id, state, outcome, count] of [
  ["current", "AVAILABLE", "ANSWER", 4], ["stale", "STALE", "ANSWER", 4],
  ["no-results", "NO_RESULTS", "ABSTAIN", 0], ["unavailable", "UNAVAILABLE", "ERROR", 0],
  ["ambiguous-reach", "ABSTAIN", "ABSTAIN", 0],
]) test(`${id} preserves its finite state, outcome, evidence and withheld presentation`, () => {
  const result = projectLivingWaters(id, 1, "BASELINE");
  assert.equal(result.state, state);
  assert.equal(result.envelope.outcome, outcome);
  assert.equal(result.features.features.length, count);
  assert.equal(result.envelope.evidence_refs[0], proof.evidence_bundle.bundle_id);
  assert.deepEqual(plain(result.envelope), proof.scenarios.find(s => s.id === id).envelope);
  assert.equal(result.point?.value ?? null, count ? 121 : null);
  if (id === "stale") {
    assert.ok(result.envelope.obligations.includes("DISPLAY_STALE_BADGE"));
    assert.ok(result.features.features.every(f => f.properties.stale && f.properties.label.includes("STALE")));
  }
});

test("roles, schematic geometry and sample times do not imply real observations or reach values", () => {
  const before = JSON.stringify(proof);
  for (const index of [0, 1, 2]) {
    const result = projectLivingWaters("current", index, "BASELINE");
    assert.deepEqual(plain(result.point), proof.packet.series.points[index]);
    assert.deepEqual(new Set(result.features.features.map(f => f.properties.role)), new Set(["synthetic_reference", "synthetic_site_metadata"]));
    for (const feature of result.features.features) {
      assert.equal(feature.properties.synthetic, true);
      assert.equal(feature.properties.geometryRole, "schematic_display_only");
      assert.equal(feature.properties.observedAt, result.point.observed_at);
      assert.equal(feature.properties.value, undefined); // No gauge value attributed to a reach.
    }
  }
  for (const index of [-1, 3, 0.5, NaN]) {
    const result = projectLivingWaters("current", index, "BASELINE");
    assert.equal(result.point, null); assert.equal(result.features.features.length, 0);
  }
  assert.equal(projectLivingWaters("live-usgs", 0, "BASELINE").features.features.length, 0);
  assert.equal(JSON.stringify(proof), before);
});

test("correction hold clears values and geometry; restore preserves the pinned baseline", () => {
  const baseline = projectLivingWaters("stale", 2, "BASELINE");
  const held = projectLivingWaters("stale", 2, "CORRECTION_HOLD");
  assert.equal(held.state, "CORRECTION_HOLD");
  assert.equal(held.point, null); assert.equal(held.features.features.length, 0);
  assert.equal(held.envelope, baseline.envelope);
  assert.deepEqual(plain(projectLivingWaters("stale", 2, "BASELINE")), plain(baseline));
});

function mapHarness(failLayer = null) {
  const sources = new Map(), layers = new Map(), listeners = new Map();
  const map = {
    getSource: id => sources.get(id), getLayer: id => layers.get(id),
    addSource: (id, source) => sources.set(id, source), removeSource: id => sources.delete(id),
    addLayer(layer) { if (layer.id === failLayer) throw new Error("renderer unavailable"); layers.set(layer.id, layer); },
    removeLayer: id => layers.delete(id),
    on(event, id, fn) { listeners.set(fn ? `${event}:${id}` : event, fn ?? id); },
    once(event, fn) { listeners.set(event, fn); },
    off(event, id, fn) { const key = fn ? `${event}:${id}` : event; if (listeners.get(key) === (fn ?? id)) listeners.delete(key); },
    fitBounds() {},
  };
  return { map, sources, layers, listeners };
}

test("renderer binds inline fixture only and cleans callbacks, partial installs and style reloads", () => {
  const h = mapHarness(), inspections = [], frames = [];
  const data = projectLivingWaters("current", 0, "BASELINE").features;
  const dispose = bindLivingWaters(h.map, data, 0.4, id => inspections.push(id), () => frames.push(true));
  assert.equal(h.sources.get(LIVING_WATERS_SOURCE).data, data);
  assert.equal(h.layers.get(LIVING_WATERS_LAYERS[1]).paint["line-opacity"], 0.4);
  const click = h.listeners.get(`click:${LIVING_WATERS_LAYERS[2]}`), idle = h.listeners.get("idle");
  click({ features: [{ properties: { id: "USGS-live-or-restricted" } }] });
  assert.deepEqual(inspections, []);
  click({ features: [{ properties: { id: proof.packet.gauge.site_id } }] });
  assert.deepEqual(inspections, [proof.packet.gauge.site_id]);
  dispose(); idle(); click({ features: [{ properties: { id: proof.packet.gauge.site_id } }] });
  assert.equal(h.sources.size + h.layers.size + h.listeners.size, 0);
  assert.deepEqual(frames, []); assert.equal(inspections.length, 1);
  const reload = bindLivingWaters(h.map, data, 1, () => {}, () => {});
  assert.equal(h.layers.size, 3); reload();
  for (const id of LIVING_WATERS_LAYERS) {
    const broken = mapHarness(id);
    assert.throws(() => bindLivingWaters(broken.map, data, 1, () => {}, () => {}));
    assert.equal(broken.sources.size + broken.layers.size + broken.listeners.size, 0);
  }
  const asyncFailure = mapHarness(), failed = [];
  bindLivingWaters(asyncFailure.map, data, 1, () => {}, () => {}, () => failed.push(true));
  const error = asyncFailure.listeners.get("error");
  error({ sourceId: "unrelated-provider" }); assert.equal(asyncFailure.sources.size, 1);
  error({ sourceId: LIVING_WATERS_SOURCE }); assert.deepEqual(failed, [true]);
  assert.equal(asyncFailure.sources.size + asyncFailure.layers.size + asyncFailure.listeners.size, 0);
});

const controlSource = await readFile(new URL("../app/living-waters-control.tsx", import.meta.url), "utf8");
function controlHarness() {
  const h = mapHarness(), slots = [], effects = [];
  let stateIndex = 0, effectIndex = 0, pending = [], tree;
  const hooks = {
    useState(initial) { const i = stateIndex++; if (!(i in slots)) slots[i] = initial; return [slots[i], next => { slots[i] = next; }]; },
    useLayoutEffect(fn, deps) { const i = effectIndex++; const old = effects[i];
      if (!old || deps.some((dep, j) => dep !== old.deps[j])) pending.push(() => { old?.dispose?.(); effects[i] = { deps, dispose: fn() }; }); },
  };
  const jsx = (type, props) => ({ type, props });
  const control = {};
  vm.runInNewContext(compile(controlSource), { exports: control, document: { body: {} },
    require(name) {
      if (name === "react") return hooks;
      if (name === "react-dom") return { createPortal: node => node };
      if (name === "react/jsx-runtime") return { jsx, jsxs: jsx };
      if (name === "./living-waters-fixture") return exports;
      throw new Error(`Unexpected runtime import ${name}`);
    }, fetch() { throw new Error("No provider I/O permitted"); },
  });
  const props = { mapRef: { current: h.map }, styleReady: true, flatMap: true, onFlatMap() {} };
  const render = () => { stateIndex = 0; effectIndex = 0; pending = []; tree = control.LivingWatersControl(props); pending.forEach(fn => fn()); return tree; };
  function find(node, predicate) {
    if (!node || typeof node !== "object") return;
    if (predicate(node)) return node;
    for (const child of [node.props?.children].flat(Infinity)) { const found = find(child, predicate); if (found) return found; }
  }
  const button = label => find(tree, n => n.type === "button" && n.props.children === label);
  const input = label => find(find(tree, n => n.type === "label" && [n.props.children].flat()[0] === label), n => n.type === "select" || n.type === "input");
  const click = label => { button(label).props.onClick(); render(); };
  const choose = (label, value) => { input(label).props.onChange({ target: { value, checked: value } }); render(); };
  render();
  return { ...h, props, render, click, choose, tree: () => tree };
}

test("control opts in, distinguishes all five outcomes, and keeps the map label visible", () => {
  const h = controlHarness();
  assert.equal(h.sources.size, 0);
  h.click("Inspect synthetic proof"); h.choose("Show synthetic schematic", true);
  for (const scenario of proof.packet.scenarios) {
    h.choose("Fixture scenario", scenario.id);
    const text = JSON.stringify(h.tree());
    assert.ok(text.includes(scenario.state)); assert.ok(text.includes(scenario.display_message));
    assert.equal(h.sources.size, ["AVAILABLE", "STALE"].includes(scenario.state) ? 1 : 0);
    if (h.sources.size) { assert.ok(text.includes("Synthetic map presentation")); assert.ok(text.includes("SYNTHETIC LIVING WATERS")); }
    else assert.ok(!text.includes("Synthetic map presentation"));
  }
});

test("control correction, projection changes, style readiness and close release only fixture state", () => {
  const h = controlHarness(); h.click("Inspect synthetic proof"); h.choose("Show synthetic schematic", true);
  h.click("Rehearse correction hold"); assert.equal(h.sources.size, 0);
  assert.ok(JSON.stringify(h.tree()).includes("CORRECTION_HOLD"));
  h.click("Restore pinned fixture"); assert.equal(h.sources.size, 1);
  h.props.flatMap = false; h.render(); assert.equal(h.sources.size, 0);
  h.props.flatMap = true; h.render(); assert.equal(h.sources.size, 1);
  h.props.styleReady = false; h.render(); assert.equal(h.sources.size, 0);
  h.props.styleReady = true; h.render(); assert.equal(h.sources.size, 1);
  h.click("Close proof"); assert.equal(h.sources.size + h.layers.size + h.listeners.size, 0);
});

test("production Site catalog discovers the opt-in proof without rendering observations by default", async () => {
  const { default: worker } = await import("../dist/server/index.js");
  const response = await worker.fetch(new Request("http://localhost/", { headers: { accept: "text/html" } }),
    { ASSETS: { fetch: async () => new Response("Not found", { status: 404 }) } },
    { waitUntil() {}, passThroughOnException() {} });
  assert.equal(response.status, 200);
  const html = await response.text();
  assert.match(html, /Living Waters · SYNTHETIC PROOF/);
  assert.match(html, /Inspect synthetic proof/);
  assert.match(html, /illustrative geometry · no real observations/);
  assert.doesNotMatch(html, /aria-label="Synthetic map presentation"/);
  assert.doesNotMatch(html, /121(?:<!-- -->)? ft3\/s/);
});
