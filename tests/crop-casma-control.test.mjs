import assert from "node:assert/strict";
import test from "node:test";
import { componentHarness, findNode, settle } from "./component-harness.mjs";

const sourceId = "external-crop-casma-1km", layerId = `${sourceId}-raster`;
const available = () => ({ state: "available", day: "2026-09-28", validCells: 149102, dataMin: 0, dataMax: .33,
  coverageState: "PARTIAL_AT_CHECKPOINTS", coverageCheckpoints: { "Dodge City": .12, Wichita: 0, Salina: .25, Topeka: null, "Kansas City": null } });
const deferred = () => { let resolve, reject; const promise = new Promise((yes, no) => { resolve = yes; reject = no; }); return { promise, resolve, reject }; };
const checkbox = tree => findNode(tree, node => node.type === "input" && node.props.type === "checkbox");
const recheck = tree => findNode(tree, node => node.type === "button" && node.props.children === "Recheck release");
const badge = tree => findNode(tree, node => node.type === "b");

async function harness(mode = "reviewed") {
  const sources = new Map(), layers = new Map(), events = new Map(), calls = [];
  const map = {
    getSource: id => sources.get(id), removeSource: id => sources.delete(id), addSource: (id, value) => sources.set(id, value),
    getLayer: id => layers.get(id), removeLayer: id => layers.delete(id), addLayer: value => layers.set(value.id, value),
    getProjection: () => ({ type: "mercator" }), getLayoutProperty: (id, name) => layers.get(id)?.layout[name],
    on(name, callback) { if (!events.has(name)) events.set(name, new Set()); events.get(name).add(callback); },
    off(name, callback) { events.get(name)?.delete(callback); },
  };
  const h = await componentHarness("app/crop-casma-control.tsx", {
    "./crop-casma-preview": { loadCropPreview: async () => ({ width: 1024, height: 512 }) },
    "./map-layer-composition": { balanceMapRasters() {}, syncMercatorRaster() {} },
    "./browser-json-request": { browserJsonRequest(url, options) { const request = deferred(); calls.push({ url, options, ...request }); return request.promise; } },
  });
  const props = { mapRef: { current: map }, styleReady: true, projection: "mercator" };
  const render = () => { const tree = h.render(h.exports.CropCasmaControl, props); h.commit(); return tree; };
  const respond = async (body, ok = true) => { calls.at(-1).resolve({ response: { ok }, body }); await settle(); return render(); };
  const loaded = () => { for (const fn of events.get("sourcedata") ?? []) fn({ sourceId, isSourceLoaded: true }); return render(); };
  const first = render();
  if (mode === "reviewed") { findNode(first, n => n.type === "select").props.onChange({target:{value:"reviewed"}}); render(); calls.shift(); }
  return { ...h, render, respond, loaded, props, calls, sources, layers };
}

test("soil release checks have a body budget/deadline and errors permit a retry", async () => {
  const h = await harness();
  assert.equal(h.calls[0].url, "/api/crop-casma/availability");
  assert.equal(h.calls[0].options.maxBytes, 16 * 1024);
  assert.equal(h.calls[0].options.timeoutMs, 15_000);
  assert.equal(recheck(h.render()).props.disabled, true);
  h.calls[0].reject(new DOMException("Request timed out", "TimeoutError"));
  await settle();
  let tree = h.render();
  assert.equal(badge(tree).props.children, "HELD");
  assert.equal(checkbox(tree).props.disabled, true);
  assert.equal(recheck(tree).props.disabled, false);
  recheck(tree).props.onClick(); h.render();
  assert.equal(h.calls.length, 2);
  assert.equal(h.calls[0].options.signal.aborted, true);
  tree = await h.respond(available());
  assert.equal(badge(tree).props.children, "READY");
  assert.equal(checkbox(tree).props.disabled, false);
  h.dispose();
});

test("withdrawn and failed releases remove rendered soil and remain switchable off", async () => {
  for (const [body, ok] of [[{ state: "held", code: "NO_APPROVED_SOIL_PACKAGE" }, true], [{ state: "error" }, false]]) {
    const h = await harness();
    let tree = await h.respond(available());
    checkbox(tree).props.onChange({ target: { checked: true } }); h.render();
    assert.ok(h.sources.has(sourceId)); assert.ok(h.layers.has(layerId));
    tree = h.loaded();
    assert.equal(badge(tree).props.children, "RENDERED"); assert.equal(tree.props["data-visible"], true);
    recheck(tree).props.onClick(); h.render();
    tree = await h.respond(body, ok);
    assert.equal(badge(tree).props.children, "HELD"); assert.equal(tree.props["data-state"], "held");
    assert.equal(tree.props["data-visible"], false); assert.equal(h.sources.size, 0); assert.equal(h.layers.size, 0);
    assert.equal(checkbox(tree).props.disabled, false, "An unavailable selected layer can still be turned off");
    checkbox(tree).props.onChange({ target: { checked: false } }); tree = h.render();
    assert.equal(checkbox(tree).props.checked, false); assert.equal(tree.props["data-state"], "off");
    h.dispose();
  }
});

test("malformed soil availability never enables map rendering or crashes numeric labels", async () => {
  for (const value of [null, [], { state: "available" },
    ...[{ day: "2026-02-30" }, { day: "2026-09-28&z=5" }, { validCells: 0 }, { dataMin: "0.1" }, { dataMin: -.1 }, { dataMax: 1.1 },
      { dataMin: .4, dataMax: .2 }, { coverageCheckpoints: [] }, { coverageState: "SAMPLED_ONLY" },
      { coverageCheckpoints: { ...available().coverageCheckpoints, Wichita: "zero" } }].map(patch => ({ ...available(), ...patch }))]) {
    const h = await harness(), tree = await h.respond(value);
    assert.equal(badge(tree).props.children, "HELD"); assert.equal(checkbox(tree).props.disabled, true);
    assert.equal(h.sources.size, 0); h.dispose();
  }
});

test("cancelled release bodies cannot restore availability, and a lost map style is held", async () => {
  const cancelled = await harness();
  cancelled.dispose(); assert.equal(cancelled.calls[0].options.signal.aborted, true);
  const stale = await cancelled.respond(available());
  assert.equal(checkbox(stale).props.disabled, true); assert.equal(cancelled.sources.size, 0);
  const h = await harness();
  let tree = await h.respond(available());
  checkbox(tree).props.onChange({ target: { checked: true } }); h.render(); tree = h.loaded();
  assert.equal(badge(tree).props.children, "RENDERED");
  h.props.styleReady = false; tree = h.render();
  assert.equal(badge(tree).props.children, "HELD"); assert.equal(tree.props["data-visible"], false);
  assert.equal(h.sources.size, 0); h.dispose();
});

 test("direct provider preview is the default and uses a reprojected canvas without a reviewed package", async () => {
  const h = await harness("preview");
  assert.equal(h.calls[0].url, "/api/crop-casma/preview");
  let tree = await h.respond({state:"available",mode:"preview",role:"EXTERNAL_CONTEXT_ONLY",day:"2026-09-28"});
  assert.equal(checkbox(tree).props.disabled,false);
  checkbox(tree).props.onChange({target:{checked:true}});h.render();await settle();tree=h.render();
  assert.equal(h.sources.get(sourceId).type,"canvas");
  assert.equal(badge(tree).props.children,"RENDERED");
  findNode(tree,n=>n.type==="select").props.onChange({target:{value:"reviewed"}});tree=h.render();
  assert.equal(h.sources.size,0,"source switch removes preview before reviewed check completes");
  assert.equal(h.calls.at(-1).url,"/api/crop-casma/availability");h.dispose();
 });


test("Crop catalog selection survives hidden details, globe and withdrawn release until explicitly hidden", async () => {
  const h = await harness(), selections = [];
  h.props.onSelectionChange = selected => selections.push(selected);
  let tree = await h.respond(available());
  checkbox(tree).props.onChange({ target: { checked: true } }); h.render(); tree = h.loaded();
  assert.equal(selections.at(-1), true);
  const before = h.calls.length;
  assert.equal(findNode(tree, node => node.type === "details").props.open, undefined, "closed disclosure retains mounted owner");
  h.props.projection = "globe"; tree = h.render();
  assert.equal(tree.props["data-state"], "held"); assert.equal(selections.at(-1), true);
  const primary = findNode(tree, node => node.props?.className === "official-context-primary");
  assert.match(findNode(primary, node => node.type === "small").props.children.flat(Infinity).join(""), /globe held/, "selected hold remains visible while source details are closed");
  assert.equal(h.calls.length, before, "display projection causes no release recheck");
  recheck(tree).props.onClick(); h.render(); tree = await h.respond({ state: "held" });
  assert.equal(selections.at(-1), true); assert.equal(checkbox(tree).props.disabled, false);
  checkbox(tree).props.onChange({ target: { checked: false } }); h.render();
  assert.equal(selections.at(-1), false); assert.equal(h.layers.size, 0);
  h.dispose();
});
