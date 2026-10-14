import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";
import { componentHarness, findNode, settle } from "./component-harness.mjs";
const compile = source => ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const pure = async file => import(`data:text/javascript;base64,${Buffer.from(compile(await readFile(`app/${file}`, "utf8"))).toString("base64")}`);
const catalog = await pure("layer-workspaces.ts");
const page = await readFile("app/page.tsx", "utf8");
const ast = ts.createSourceFile("page.tsx", page, ts.ScriptTarget.ES2022, true, ts.ScriptKind.TSX);
const declarations = new Map();
function walk(node) { if (ts.isVariableDeclaration(node) && ts.isIdentifier(node.name) && node.initializer) declarations.set(node.name.text, node.initializer.getText(ast)); ts.forEachChild(node, walk); }
walk(ast);
const project = new Function("bindings", compile(`function project(bindings: any) { const { OFFICIAL_CONTEXT_SOURCES, LAYER_WORKSPACES, filterOfficialSources, officialVisibility, daylightEnabled, soilMapState, cropSelected, reviewedWaterSelected, reviewedWeatherSelected, EARTH_ENGINE_CONTEXT_LAYERS, imageryTopics, earthEngineDisplay, LAYER_REGISTRY, visibility, selectedCatalogCount, layerEntryMatches, layerCatalogView, officialWorkspace, officialSourceQuery } = bindings;
const catalogEntries = ${declarations.get("catalogEntries")};
const selectedMapLayerCount = ${declarations.get("selectedMapLayerCount")};
const matchingCatalogEntries = ${declarations.get("matchingCatalogEntries")};
return { catalogEntries, selectedMapLayerCount, matchingCatalogEntries }; }`) + "return project(bindings);");

test("actual page catalog includes every selected family; all tab/topic/search projections preserve state", () => {
  const state = {
    ...catalog, OFFICIAL_CONTEXT_SOURCES: [{ id: "usgs-streamflow", title: "River streamflow", shortTitle: "River Pulse", organization: "USGS", domain: "Living waters", defaultVisibility: true }, { id: "nws-radar", title: "Weather radar", shortTitle: "Radar", organization: "NOAA", domain: "Weather & hazards", defaultVisibility: false }],
    officialVisibility: { "usgs-streamflow": true, "nws-radar": true }, daylightEnabled: true, soilMapState: { visible: true, day: "2026-09-28", opacity: .67 }, cropSelected: true, reviewedWaterSelected: true, reviewedWeatherSelected: true,
    EARTH_ENGINE_CONTEXT_LAYERS: [{ id: "ee-cdl", title: "crop classes", source: "USDA", attribution: "NASS" }], earthEngineDisplay: { visible: { "ee-cdl": true }, years: { "ee-cdl": 1999 } },
    LAYER_REGISTRY: [{ id: "registry", title: "Historical places", domain: "History", description: "Dated anchors" }], visibility: { registry: true },
    layerCatalogView: "selected", officialWorkspace: "all", officialSourceQuery: "",
  };
  const before = JSON.stringify(state), result = project(state);
  assert.equal(result.selectedMapLayerCount, 9, "includes held crop/water/weather, daylight, soil, selected uninstalled imagery, official and registry");
  assert.equal(result.matchingCatalogEntries.length, result.selectedMapLayerCount);
  for (const [query, topic, expected] of [["USGS river", "water", ["usgs-streamflow"]], ["moisture", "water", ["soil", "crop"]], ["solar", "terrain", ["daylight"]], ["GHCN", "disaster", ["reviewed-weather"]], ["nass", "land", ["crop", "ee-cdl"]], ["not present", "all", []]]) {
    const filtered = project({ ...state, officialWorkspace: topic, officialSourceQuery: query });
    assert.deepEqual(filtered.matchingCatalogEntries.map(entry => entry.id), expected);
    assert.equal(filtered.selectedMapLayerCount, 9, "count remains total selection, independent of search");
  }
  assert.deepEqual(project({ ...state, layerCatalogView: "local" }).matchingCatalogEntries.map(entry => entry.id), ["ee-cdl"]);
  assert.equal(project({ ...state, layerCatalogView: "official" }).matchingCatalogEntries.length, 8);
  assert.equal(JSON.stringify(state), before, "filter projections cannot mutate any owner selection, date or opacity");
});

test("specialty owners are mounted once in persistent hidden wrappers; official playback rows use unfiltered inventory", () => {
  const owners = new Map();
  function visit(node, ancestors = []) {
    if (ts.isJsxSelfClosingElement(node)) {
      const name = node.tagName.getText(ast);
      if (["GovernedWaterControl", "GovernedWeatherControl", "SoilMoistureControl", "CropCasmaControl", "EarthEngineDisplayControls"].includes(name)) {
        owners.set(name, (owners.get(name) ?? 0) + 1);
        assert.ok(!ancestors.some(parent => ts.isConditionalExpression(parent) || ts.isBinaryExpression(parent) && parent.operatorToken.kind === ts.SyntaxKind.AmpersandAmpersandToken), `${name} must not unmount with catalog filters`);
        assert.ok(ancestors.some(parent => ts.isJsxElement(parent) && parent.openingElement.attributes.properties.some(prop => prop.name?.getText(ast) === "hidden")), `${name} uses a persistent hidden ancestor`);
      }
    }
    ts.forEachChild(node, child => visit(child, [...ancestors, node]));
  }
  visit(ast);
  assert.equal(owners.size, 5); assert.ok([...owners.values()].every(count => count === 1));
  assert.match(page, /filterOfficialSources\(OFFICIAL_CONTEXT_SOURCES, "all", ""\)\.map\(\(source\)/);
  assert.match(page, /hidden=\{!listedOfficialSources\.some\(item => item\.id === source\.id\)\}/);
});

test("Appearance and Measure are primary; every advanced view invokes the existing route key", async () => {
  const h = await componentHarness("app/explorer-controls-navigation.tsx", {}), changes = [];
  for (const [id, title] of [...h.exports.EXPLORER_CONTROL_SECTIONS, ...h.exports.ADVANCED_CONTROL_SECTIONS]) {
    const tree = h.render(h.exports.ExplorerControlsNavigation, { value: id, onChange: next => changes.push(next) });
    const button = findNode(tree, node => node.type === "button" && node.props.children === title);
    assert.equal(button.props["aria-pressed"], true);
    let focusedSummary = false;
    const details = { open: true, querySelector: selector => { assert.equal(selector, "summary"); return { focus: () => { focusedSummary = true; } }; } };
    button.props.onClick({ currentTarget: { closest: () => details } });
    assert.equal(changes.at(-1), id);
    if (h.exports.ADVANCED_CONTROL_SECTIONS.some(([advanced]) => advanced === id)) {
      assert.equal(details.open, false);
      assert.equal(focusedSummary, true, "closing the disclosure returns keyboard focus to a visible control");
    }
  }
  assert.deepEqual(Array.from(h.exports.EXPLORER_CONTROL_SECTIONS, ([id]) => id), ["scene", "measure"]);
  assert.equal(new Set(changes).size, 11, "all retained control views remain reachable without an Explore panel");
  h.dispose();
});
test("focus boundaries ignore closed disclosure contents even when the browser retains their layout boxes", () => {
  class Details {
    constructor(parentElement, open) { this.parentElement = parentElement; this.open = open; }
    querySelector(selector) { assert.equal(selector, ":scope > summary"); return this.summary; }
  }
  const container = { parentElement: null, contains(node) { while (node) { if (node === this) return true; node = node.parentElement; } return false; } };
  const element = (parentElement, blocked = false, tabIndex = 0, rects = 1) => ({ parentElement, tabIndex, closest: () => blocked ? {} : null, getClientRects: () => Array(rects).fill({ width: 40, height: 44 }) });
  const close = element(container), disclosure = new Details(container, false);
  disclosure.summary = element(disclosure);
  const closedButton = element(disclosure), nested = new Details(disclosure, true);
  nested.summary = element(nested);
  const nestedButton = element(nested), hidden = element(container, true), negative = element(container, false, -1), unrendered = element(container, false, 0, 0);
  container.querySelectorAll = () => [close, disclosure.summary, closedButton, nested.summary, nestedButton, hidden, negative, unrendered];
  const list = new Function("HTMLDetailsElement", compile(`const FOCUSABLE_SELECTOR = ${declarations.get("FOCUSABLE_SELECTOR")}; const list = ${declarations.get("visibleFocusableElements")}; return list;`))(Details);
  assert.deepEqual(list(container), [close, disclosure.summary], "closed bodies cannot become the final focus target");
  disclosure.open = true;
  assert.deepEqual(list(container), [close, disclosure.summary, closedButton, nested.summary, nestedButton], "opening the disclosure restores its controls");
  nested.open = false;
  assert.deepEqual(list(container), [close, disclosure.summary, closedButton, nested.summary], "a nested closed summary remains reachable but its body does not");
});

test("reviewed water remains selected and hideable when a refresh withholds its package", async () => {
  const availability = await pure("governed-water-availability.ts");
  const layers = JSON.parse(await readFile("tests/fixtures/governed-water/layers.json", "utf8"));
  layers.data.approval_expires_at = "2099-01-01T00:00:00Z";
  const requests = [], timers = [], selections = [];
  const h = await componentHarness("app/governed-water-control.tsx", {
    "./bounded-json": { readBoundedJson: async response => response.body },
    "./governed-water": { approvalRemainingMs: (expiry, now) => Date.parse(expiry) - now },
    "./governed-water-availability": availability,
  }, {
    fetch: url => new Promise(resolve => requests.push({ url, resolve })),
    setTimeout: (fn, ms) => { timers.push({ fn, ms }); return timers.length; }, clearTimeout() {}, setInterval: () => 1, clearInterval() {},
  });
  const props = { mapRef: { current: null }, styleReady: false, onSelectionChange: value => selections.push(value) };
  const render = () => { const tree = h.render(h.exports.GovernedWaterControl, props); h.commit(); return tree; };
  render(); timers.find(timer => timer.ms === 0).fn();
  requests[0].resolve({ ok: true, body: layers }); await settle(); let tree = render();
  const checkbox = node => findNode(node, item => item.type === "input" && item.props.type === "checkbox");
  checkbox(tree).props.onChange({ target: { checked: true } }); tree = render();
  assert.equal(selections.at(-1), true);
  const refresh = findNode(tree, item => item.type === "button" && item.props.children === "Check connection");
  refresh.props.onClick(); tree = render();
  assert.equal(checkbox(tree).props.checked, true); assert.equal(checkbox(tree).props.disabled, false);
  requests.at(-1).resolve({ ok: true, body: { envelope: { reason_code: "NO_APPROVED_SNAPSHOT" } } }); await settle(); tree = render();
  assert.equal(selections.at(-1), true); assert.equal(checkbox(tree).props.disabled, false);
  checkbox(tree).props.onChange({ target: { checked: false } }); render();
  assert.equal(selections.at(-1), false);
  h.dispose();
});
