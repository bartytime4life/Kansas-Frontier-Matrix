import assert from "node:assert/strict";
import { webcrypto } from "node:crypto";
import { readFile } from "node:fs/promises";
import test from "node:test";
import { componentHarness, findNode, settle } from "./component-harness.mjs";

// Use the actual pinned public asset and aviation models. Map/DOM fixtures prove
// event and focus ownership, not rendered charts, provider freshness or clearance.
const imports = {};
for (const name of ["aviation-research", "aviation-profile", "aviation-chart", "aviation-airspace", "aviation-weather", "aviation-traffic", "aviation-drone-data"]) {
  imports[`./${name}`] = (await componentHarness(`app/${name}.ts`, {}, { Error })).exports;
}
const bytes = await readFile("public/data/aviation/kansas-aviation-context.json");
const bounded = (await componentHarness("app/bounded-json.ts", {}, { TextDecoder, Uint8Array })).exports;
const textOf = node => typeof node === "string" || typeof node === "number" ? String(node) : node && typeof node === "object" ? [node.props?.children].flat(Infinity).map(textOf).join(" ").replace(/\s+/g, " ") : "";
const button = (tree, label) => findNode(tree, node => node.type === "button" && textOf(node) === label);
async function setup() {
  const moves = [], timers = new Set(), listeners = new Map(), mapListeners = new Map(), sources = new Map(), layers = new Map();
  const document = { body:{ name:"body" }, activeElement:null }; document.activeElement = document.body;
  const node = name => ({ name, isConnected:true, focus() { document.activeElement = this; moves.push(name); } });
  const inspector = node("inspector"), profile = node("profile"), pointCenter = node("point-center"), sideCenter = node("side-center"), elsewhere = node("elsewhere");
  const canvas = { style:{} }; let center = { lng:-97.65, lat:38.79 };
  const map = {
    getCenter:() => center, getCanvas:() => canvas,
    getSource:id => sources.get(id), addSource(id, value) { sources.set(id, { ...value, setData() {} }); }, removeSource:id => sources.delete(id),
    getLayer:id => layers.get(id), addLayer(layer) { layers.set(layer.id, layer); }, removeLayer:id => layers.delete(id),
    on(event, ...args) { const callback = args.at(-1); const key = `${event}:${args.length > 1 ? args[0] : ""}`; mapListeners.set(key, callback); return map; },
    once(event, callback) { const wrapper = value => { mapListeners.delete(`${event}:`); callback(value); }; wrapper.original = callback; mapListeners.set(`${event}:`, wrapper); return map; },
    off(event, ...args) { const key = `${event}:${args.length > 1 ? args[0] : ""}`, stored = mapListeners.get(key); if (stored === args.at(-1) || stored?.original === args.at(-1)) mapListeners.delete(key); return map; },
  };
  const window = { addEventListener:(name, fn) => listeners.set(name, fn), removeEventListener:(name, fn) => { if (listeners.get(name) === fn) listeners.delete(name); } };
  const h = await componentHarness("app/aviation-control.tsx", { ...imports, "./bounded-json":bounded, "./map-runtime":{ unexaggeratedTerrainElevation:() => null } }, {
    document, window, crypto:webcrypto, TextDecoder, Uint8Array, Error,
    setTimeout:fn => { timers.add(fn); return fn; }, clearTimeout:id => timers.delete(id), setInterval:fn => { timers.add(fn); return fn; }, clearInterval:id => timers.delete(id),
    fetch:async path => {
      if (path === "/data/aviation/kansas-aviation-context.json") return { ok:true, arrayBuffer:async () => bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength) };
      throw new Error("This synthetic fixture supplies no live aviation feeds.");
    },
  });
  let inspectRequest = null; const mapRef = { current:map };
  const render = ({ commit = true } = {}) => {
    const tree = h.render(h.exports.AviationControl, { mapRef, styleReady:true, inspectRequest });
    const point = button(tree, "Inspect map center"), side = findNode(tree, n => n.type === "button" && /^Use map center for [AB]$/.test(textOf(n)));
    for (const [present, target] of [[point, pointCenter], [side, sideCenter]]) {
      target.isConnected = Boolean(present);
      if (!present && document.activeElement === target) document.activeElement = document.body;
    }
    const inspectNode = findNode(tree, n => n.props?.["data-aviation-inspector"] !== undefined);
    if (inspectNode) inspectNode.props.ref.current = inspector;
    const chart = findNode(tree, n => n.props?.className === "aviation-profile-scroll");
    if (chart) chart.props.ref.current = profile;
    const details = findNode(tree, n => n.type === "details"); if (details?.props.ref) details.props.ref.current = { open:true };
    if (commit) h.commit();
    return tree;
  };
  let tree = render();
  findNode(tree, n => n.type === "input" && n.props["aria-label"] === "Show airspace and aviation layers").props.onChange({ target:{ checked:true } });
  render();
  for (let i = 0; i < 20; i++) {
    await new Promise(resolve => setTimeout(resolve, 5)); await settle(); tree = render();
    if (button(tree, "Pick a point on the map")) break;
  }
  assert.ok(button(tree, "Pick a point on the map"), "pinned context must finish verification");
  return { h, render, document, moves, inspector, profile, pointCenter, sideCenter, elsewhere, listeners, mapListeners, timers,
    center:at => { center = at; }, request:value => { inspectRequest = value; },
    choose(label, target, detail = 0) { const tree = render(); document.activeElement = target; button(tree, label).props.onClick({ detail, currentTarget:target }); },
  };
}

test("keyboard Inspect map center focuses the matching inspector at the current center", async () => {
  const f = await setup(); button(f.render(), "Pick a point on the map").props.onClick(); f.render(); f.center({ lng:-96.5, lat:38.5 });
  f.choose("Inspect map center", f.pointCenter); const tree = f.render();
  assert.equal(button(tree, "Inspect map center"), undefined); assert.equal(f.document.activeElement, f.inspector); assert.deepEqual(f.moves, ["inspector"]); assert.match(textOf(tree), /38.5000, -96.5000/);
  f.h.dispose(); assert.equal(f.timers.size, 0); assert.equal(f.listeners.size, 0); assert.equal(f.mapListeners.size, 0);
});

test("pointer center and map picks keep their existing focus, and newer focus wins before commit", async () => {
  for (const kind of ["pointer-center", "map", "newer-focus"]) {
    const f = await setup(); button(f.render(), "Pick a point on the map").props.onClick(); f.render();
    if (kind === "map") { f.document.activeElement = f.elsewhere; f.mapListeners.get("click:")({ lngLat:{ lng:-97, lat:38 } }); }
    else { f.choose("Inspect map center", f.pointCenter, kind === "pointer-center" ? 1 : 0); if (kind === "newer-focus") f.document.activeElement = f.elsewhere; }
    f.render(); assert.equal(f.moves.length, 0, kind); assert.notEqual(f.document.activeElement, f.inspector, kind); f.h.dispose();
  }
});

test("keyboard A keeps its control and keyboard B focuses the matching cross-section", async () => {
  const f = await setup(); button(f.render(), "Draw a side view (A to B)").props.onClick(); f.render();
  f.choose("Use map center for A", f.sideCenter); let tree = f.render(); assert.ok(button(tree, "Use map center for B")); assert.equal(f.document.activeElement, f.sideCenter); assert.equal(f.moves.length, 0);
  f.center({ lng:-97.2, lat:38.9 }); f.choose("Use map center for B", f.sideCenter); tree = f.render(); assert.equal(button(tree, "Use map center for B"), undefined);
  assert.ok(findNode(tree, n => n.props?.["aria-label"] === "Scrollable aviation cross-section chart")); assert.equal(f.document.activeElement, f.profile); assert.deepEqual(f.moves, ["profile"]); f.h.dispose();
});

test("pointer B completion and newer focus do not transfer keyboard focus to the chart", async () => {
  for (const kind of ["pointer", "newer-focus"]) {
    const f = await setup(); button(f.render(), "Draw a side view (A to B)").props.onClick(); f.render();
    f.choose("Use map center for A", f.sideCenter); f.render(); f.center({ lng:-97.2, lat:38.9 });
    f.choose("Use map center for B", f.sideCenter, kind === "pointer" ? 1 : 0); if (kind === "newer-focus") f.document.activeElement = f.elsewhere;
    f.render(); assert.equal(f.moves.length, 0, kind); assert.notEqual(f.document.activeElement, f.profile); f.h.dispose();
  }
});

test("invalid keyboard B retains its control and A, then corrects without focusing an old chart", async () => {
  for (const kind of ["same-point", "too-far", "newer-focus"]) {
    const f = await setup();
    // First create a chart: a subsequent invalid attempt must not focus it.
    button(f.render(), "Draw a side view (A to B)").props.onClick(); f.render();
    f.choose("Use map center for A", f.sideCenter); f.render(); f.center({ lng:-97.2, lat:38.9 });
    f.choose("Use map center for B", f.sideCenter); f.render(); f.moves.length = 0;
    button(f.render(), "Draw a side view (A to B)").props.onClick(); f.render();
    f.choose("Use map center for A", f.sideCenter); f.render();
    if (kind === "too-far") f.center({ lng:-85, lat:38.9 });
    f.choose("Use map center for B", f.sideCenter);
    if (kind === "newer-focus") f.document.activeElement = f.elsewhere;
    let tree = f.render(); assert.match(textOf(tree), kind === "too-far" ? /320 NM/ : /two distinct points/); assert.ok(button(tree, "Use map center for B"));
    assert.equal(f.document.activeElement, kind === "newer-focus" ? f.elsewhere : f.sideCenter); assert.equal(f.moves.length, 0); assert.ok(f.mapListeners.has("click:"));
    f.center({ lng:-96.9, lat:39 }); f.choose("Use map center for B", f.sideCenter); tree = f.render();
    assert.equal(button(tree, "Use map center for B"), undefined); assert.doesNotMatch(textOf(tree), /two distinct points|320 NM/); assert.equal(f.document.activeElement, f.profile); assert.deepEqual(f.moves, ["profile"]); f.h.dispose();
  }
});

test("an invalid map B leaves its listener active for a corrected pointer selection", async () => {
  const f = await setup(); button(f.render(), "Draw a side view (A to B)").props.onClick(); f.render();
  f.mapListeners.get("click:")({ lngLat:{ lng:-97.65, lat:38.79 } }); f.render();
  f.document.activeElement = f.elsewhere; f.mapListeners.get("click:")({ lngLat:{ lng:-97.65, lat:38.79 } });
  let tree = f.render(); assert.match(textOf(tree), /two distinct points/); assert.ok(button(tree, "Use map center for B")); assert.ok(f.mapListeners.has("click:"));
  f.mapListeners.get("click:")({ lngLat:{ lng:-97.2, lat:38.9 } }); tree = f.render();
  assert.equal(button(tree, "Use map center for B"), undefined); assert.ok(findNode(tree, n => n.props?.className === "aviation-profile-scroll")); assert.equal(f.document.activeElement, f.elsewhere); assert.equal(f.moves.length, 0); assert.equal(f.mapListeners.has("click:"), false); f.h.dispose();
});

test("the existing dossier Inspect request still expands and focuses its point inspector", async () => {
  const f = await setup(); f.request({ lon:-96.8, lat:38.7, label:"SYNTHETIC dossier target", nonce:1 }); f.render(); const tree = f.render();
  assert.match(textOf(tree), /SYNTHETIC dossier target/); assert.equal(f.document.activeElement, f.inspector); f.h.dispose();
});
