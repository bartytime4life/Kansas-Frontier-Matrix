import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { createRequire } from "node:module";
import test from "node:test";
import * as React from "react";
import { renderToStaticMarkup } from "react-dom/server";
import ts from "typescript";

const require = createRequire(import.meta.url);
async function compile(path, imports = {}) {
  const source = await readFile(new URL(path, import.meta.url), "utf8");
  const code = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022, jsx: ts.JsxEmit.ReactJSX } }).outputText;
  const compiled = { exports: {} };
  new Function("require", "module", "exports", code)(id => imports[id] ?? require(id), compiled, compiled.exports);
  return compiled.exports;
}
const context = await compile("../app/earth-engine-context.ts");
const data = await compile("../app/earth-engine-data.ts");
const manifest = (id, year, status = "approved") => {
  const descriptor = context.EARTH_ENGINE_CONTEXT_LAYERS.find(item => item.id === id);
  return {
    schema: "kfm-earth-engine-context/v1", setId: `ks-${year}-synthetic`, boundary: "Kansas · TIGER/2018/States · STATEFP 20",
    approvedAt: "2026-10-06T00:00:00Z", reviewState: "APPROVED_VISUAL_CONTEXT", admission: "NOT_ADMITTED", evidence: "NOT_CLAIM_EVIDENCE",
    layers: [{ ...descriptor, status, period: context.earthEngineLayerPeriod(id, year), resolutionMeters: 30, limits: "Synthetic test only",
      geotiffSha256: "a".repeat(64), reviewSha256: "b".repeat(64), tileIndexes: { 0: { sha256: "c".repeat(64), count: 1, minX: 0, maxX: 0, minY: 0, maxY: 0 } } }],
  };
};

// Exercise the real component's event handlers, rendered markup and display
// projection with deterministic hooks; no browser, tile requests or activation.
async function harness(manifests = [], map = null, initialYearChoice = {}) {
  const states = [{}, false, {}, initialYearChoice, {}];
  let hook = 0, effects = [], display, tree;
  const { EarthEngineDisplayControls } = await compile("../app/earth-engine-display.tsx", {
    react: { ...React, useState: () => {
      const index = hook++;
      return [states[index], next => { states[index] = typeof next === "function" ? next(states[index]) : next; }];
    }, useMemo: fn => fn(), useEffect: fn => effects.push(fn) },
    "next/link": { default: ({ children, ...props }) => React.createElement("a", props, children) },
    "../scripts/earth-engine/cdl_2024_palette.json": { default: { classes: {} } },
    "./earth-engine-context": context, "./earth-engine-data": data,
    "./earth-engine-display.module.css": { default: new Proxy({}, { get: (_target, key) => String(key) }) },
    "./map-layer-composition": { balanceMapRasters() {}, composeMapLayers() {}, requestRasterOpacity() {} },
    "./earth-engine-comparison-panel": { EarthEngineComparisonPanel: () => null },
  });
  const render = () => {
    hook = 0; effects = [];
    tree = EarthEngineDisplayControls({ map, mapYear: 2024, manifests, loading: false, error: null, onReload() {}, onDisplayChange(value) { display = value; }, rendererState: "ready" });
    for (const effect of effects) effect();
    return renderToStaticMarkup(tree);
  };
  function find(element, predicate) {
    if (!React.isValidElement(element)) return null;
    if (predicate(element)) return element;
    for (const child of React.Children.toArray(element.props.children)) {
      const match = find(child, predicate); if (match) return match;
    }
    return null;
  }
  const row = id => {
    const title = context.EARTH_ENGINE_CONTEXT_LAYERS.find(item => item.id === id).title;
    return find(tree, item => item.type === "article" && Boolean(find(item, node => node.type === "select" && node.props["aria-label"] === `${title} image year`)));
  };
  return {
    render, get display() { return display; }, row,
    select: id => find(row(id), item => item.type === "select"),
    checkbox: id => find(row(id), item => item.type === "input" && item.props.type === "checkbox"),
    rowHtml: id => renderToStaticMarkup(row(id)),
  };
}

function mapStub() {
  const sources = new Map(), layers = new Map();
  return { sources, layers, isStyleLoaded: () => true, on() {}, off() {},
    getSource: id => sources.get(id), addSource: (id, source) => sources.set(id, source), removeSource: id => sources.delete(id),
    getLayer: id => layers.get(id), addLayer: layer => layers.set(layer.id, layer), removeLayer: id => layers.delete(id),
    setLayoutProperty(id, name, value) { layers.get(id).layout[name] = value; },
  };
}

test("empty inventory uses each product's supported default consistently in control, text, link and display state", async () => {
  const ui = await harness(); ui.render();
  for (const [id, expected] of [["ee-landsat4", 1993], ["ee-landsat5", 2012]]) {
    assert.equal(ui.select(id).props.value, expected);
    assert.match(ui.rowHtml(id), new RegExp(`value="${expected}" selected=""`));
    assert.match(ui.rowHtml(id), new RegExp(`${expected} source year · imagery not prepared`));
    assert.match(ui.rowHtml(id), new RegExp(`/earth-engine\\?dataset=${id}&amp;year=${expected}`));
    assert.doesNotMatch(ui.rowHtml(id), /2024 source year|year=2024/);
    assert.equal(ui.checkbox(id).props.disabled, true); assert.equal(ui.checkbox(id).props.checked, false);
    assert.equal(ui.display.years[id], expected);
  }
  for (const [id, bounds] of Object.entries(context.EARTH_ENGINE_SOURCE_YEARS)) {
    const year = ui.display.years[id]; assert.ok(Number.isInteger(year) && year >= bounds[0] && year <= bounds[1], id);
  }
  assert.equal(ui.display.years["ee-3dep"], undefined); assert.deepEqual(ui.display.visible, {});
});

test("default prefers the latest approved installed year of the same product inside its source bounds", async () => {
  const valid = [manifest("ee-landsat4", 1989), manifest("ee-landsat4", 1991), manifest("ee-landsat4", 1993, "held"), manifest("ee-landsat5", 2010)];
  for (const item of valid) assert.ok(context.parseEarthEngineManifest(item));
  const ui = await harness([...valid, manifest("ee-landsat4", 2024)]); ui.render();
  assert.equal(ui.select("ee-landsat4").props.value, 1991); assert.equal(ui.select("ee-landsat5").props.value, 2010);
  assert.match(ui.rowHtml("ee-landsat4"), /1991 calendar year/);
  assert.doesNotMatch(ui.rowHtml("ee-landsat4"), /Prepare 1991/);
  assert.equal(ui.checkbox("ee-landsat4").props.disabled, false);
  assert.equal(ui.checkbox("ee-landsat4").props.checked, false); assert.deepEqual(ui.display.visible, {});
});

test("an explicit supported but uninstalled year remains unavailable and removes prior imagery instead of substituting it", async () => {
  const map = mapStub(), ui = await harness([manifest("ee-landsat4", 1990)], map); ui.render();
  const source = "kfm-ee-context-source-ee-landsat4", layer = "kfm-ee-context-layer-ee-landsat4";
  assert.match(map.sources.get(source).tiles[0], /ks-1990-synthetic/);
  assert.equal(map.layers.get(layer).layout.visibility, "none");
  ui.select("ee-landsat4").props.onChange({ target: { value: "1991" } }); ui.render();
  assert.equal(ui.select("ee-landsat4").props.value, 1991); assert.equal(ui.display.years["ee-landsat4"], 1991);
  assert.match(ui.rowHtml("ee-landsat4"), /1991 source year · imagery not prepared/);
  assert.match(ui.rowHtml("ee-landsat4"), /dataset=ee-landsat4&amp;year=1991/);
  assert.equal(ui.checkbox("ee-landsat4").props.disabled, true);
  assert.equal(map.sources.has(source), false); assert.equal(map.layers.has(layer), false); assert.deepEqual(ui.display.visible, {});
});

test("out-of-range, fractional and malformed year events preserve the user's last valid selection", async () => {
  for (const [id, valid] of [["ee-landsat4", 1991], ["ee-landsat5", 2009]]) {
    const ui = await harness(); ui.render();
    ui.select(id).props.onChange({ target: { value: String(valid) } }); ui.render();
    const before = ui.rowHtml(id);
    for (const invalid of ["2024", "1895", "1991.5", "NaN", "Infinity", "", "not-a-year"]) {
      ui.select(id).props.onChange({ target: { value: invalid } }); ui.render();
      assert.equal(ui.select(id).props.value, valid, `${id}: ${invalid}`);
      assert.equal(ui.rowHtml(id), before); assert.equal(ui.display.years[id], valid);
    }
  }
});

test("invalid in-memory year choices cannot create unsupported preparation links or renderer years", async () => {
  const ui = await harness([], null, { "ee-landsat4": 2024, "ee-landsat5": Number.NaN }); ui.render();
  assert.equal(ui.display.years["ee-landsat4"], 1993); assert.equal(ui.display.years["ee-landsat5"], 2012);
  assert.match(ui.rowHtml("ee-landsat4"), /dataset=ee-landsat4&amp;year=1993/);
  assert.match(ui.rowHtml("ee-landsat5"), /dataset=ee-landsat5&amp;year=2012/);
  assert.deepEqual(ui.display.visible, {});
});
