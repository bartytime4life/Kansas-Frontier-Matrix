import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import ts from "typescript";
import { componentHarness, findNode, settle } from "./component-harness.mjs";

const compile = source => ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const modules = new Map();
async function moduleUrl(file) {
  file = path.resolve(file);
  if (modules.has(file)) return modules.get(file);
  let js = compile(await readFile(file, "utf8"));
  for (const match of [...js.matchAll(/from ["'](\.[^"']+)["']/g)]) js = js.replace(match[0], `from ${JSON.stringify(await moduleUrl(path.resolve(path.dirname(file), match[1]) + ".ts"))}`);
  const url = `data:text/javascript;base64,${Buffer.from(js).toString("base64")}`;
  modules.set(file, url); return url;
}
const model = await import(await moduleUrl("app/map-starters.ts"));
const context = await import(await moduleUrl("app/live-context.ts"));
const sources = context.OFFICIAL_CONTEXT_SOURCES;
const available = Object.fromEntries(sources.map(source => [source.id, { held: false, unavailable: false }]));
const learning = model.MAP_STARTERS.find(starter => starter.id === "learning-kansas");
const page = await readFile("app/page.tsx", "utf8");
const ast = ts.createSourceFile("page.tsx", page, ts.ScriptTarget.ES2022, true, ts.ScriptKind.TSX);
const declarations = new Map();
function visit(node) {
  if (ts.isVariableDeclaration(node) && ts.isIdentifier(node.name) && node.initializer) declarations.set(node.name.text, node.initializer.getText(ast));
  ts.forEachChild(node, visit);
}
visit(ast);
const run = (expression, bindings) => new Function(...Object.keys(bindings), `${compile(`const result = ${expression};`)}return result;`)(...Object.values(bindings));
const nodes = (tree, type) => {
  const result = [];
  const visit = node => { if (!node || typeof node !== "object") return; if (node.type === type) result.push(node); for (const child of [node.props?.children].flat(Infinity)) visit(child); };
  visit(tree); return result;
};
const memoryStorage = () => {
  const data = new Map(), writes = [];
  return { data, writes, getItem: key => data.get(key) ?? null, setItem: (key, value) => { writes.push([key, value]); data.set(key, value); }, removeItem: key => data.delete(key) };
};

test("six bounded starters use only actual public context, preserve source metadata, and make no admission claims", () => {
  const before = JSON.stringify(sources);
  assert.equal(model.MAP_STARTERS.length, 6);
  assert.equal(new Set(model.MAP_STARTERS.map(starter => starter.id)).size, 6);
  for (const starter of model.MAP_STARTERS) {
    assert.ok(starter.description && starter.limitation);
    assert.ok(starter.ids.length >= 3 && starter.ids.length <= 4);
    for (const id of starter.ids) assert.equal(sources.find(source => source.id === id)?.evidenceRole, "EXTERNAL_CONTEXT_ONLY");
    assert.deepEqual(model.starterPlan(starter.ids, sources, available).selected, [...starter.ids]);
    assert.ok(starter.ids.filter(id => sources.find(source => source.id === id).apiPath).length <= 2, "bound JSON acquisition fanout");
  }
  assert.match(model.MAP_STARTERS.find(starter => starter.id === "historical-landscape").limitation, /do not locate archaeological sites/);
  assert.equal(JSON.stringify(sources), before);
});

test("held, failed, unknown, proposed and private sources never become selectable", () => {
  const blocked = { ...available, "usgs-streamflow": { held: true, unavailable: false }, "usgs-earthquakes": { held: false, unavailable: true } };
  const restricted = { ...sources[0], id: "private-parcels", evidenceRole: "RESTRICTED" };
  const result = model.starterPlan(["usgs-streamflow", "usgs-earthquakes", "atlas-proposed", "private-parcels", "census-counties", "census-counties"], [...sources, restricted], blocked);
  assert.deepEqual(result.selected, ["census-counties"]);
  assert.equal(result.skipped.length, 4);
  assert.match(result.skipped[0].reason, /Held/);
  assert.match(result.skipped[1].reason, /Unavailable/);
  assert.equal(model.starterPlan(learning.ids, sources, {}).selected.length, 0, "missing eligibility fails closed");
});

test("actual page eligibility preserves the existing frame/build and Globe restrictions without changing zoom or dates", () => {
  const useMemo = fn => fn();
  for (const [frame, projection, buildYearCurrent] of [[context.OFFICIAL_CONTEXT_PRESENT_FRAME, "mercator", true], [1900, "mercator", true], [context.OFFICIAL_CONTEXT_PRESENT_FRAME, "globe", true], [context.OFFICIAL_CONTEXT_PRESENT_FRAME, "mercator", false]]) {
    const access = run(declarations.get("starterAccess"), { useMemo, OFFICIAL_CONTEXT_SOURCES: sources, officialContextVisibilityForFrame: context.officialContextVisibilityForFrame,
      temporalQuery: { frame }, buildYearCurrent, projection, officialStates: {}, view: { zoom: 5 }, sourceMinimumZoom: source => source.minDisplayZoom ?? (source.id === "usgs-3dep-hillshade" ? 7 : 0) });
    const plan = model.starterPlan(learning.ids, sources, access);
    if (frame === 1900 || !buildYearCurrent) assert.equal(plan.selected.length, 0);
    else if (projection === "globe") assert.ok(!plan.selected.includes("usgs-3dep-hillshade"));
    else { assert.equal(plan.selected.length, 3); assert.match(access["usgs-3dep-hillshade"].guidance, /zoom 7/); }
  }
});

test("actual apply handler changes only public context owners, avoids repeat work, preserves customization, and resets safely", () => {
  const calls = [], announcements = [], ref = { current: { "nws-radar": true, "census-counties": true } };
  const preserved = { camera: [-98, 38], zoom: 9, sourceDays: { "noaa-hms-smoke": "2025-01-01" }, opacity: .37, reviewed: true, imagery: true };
  const before = JSON.stringify(preserved);
  const apply = run(declarations.get("applyStarterContext"), { ...model, OFFICIAL_CONTEXT_SOURCES: sources, starterAccess: available, officialVisibilityRef: ref,
    setOfficialContextVisible(id, visible) { calls.push([id, visible]); ref.current = { ...ref.current, [id]: visible }; },
    setOfficialSourceQuery() {}, setOfficialWorkspace() {}, setOfficialCatalogFilter() {}, setLayerCatalogView() {}, announce: value => announcements.push(value) });
  apply(learning.ids, learning.title);
  assert.deepEqual(calls[0], ["nws-radar", false], "remove unused live source first");
  assert.equal(calls.length, 3, "already selected Census does not refetch");
  apply(learning.ids, learning.title); assert.equal(calls.length, 3, "reapplying makes no owner calls");
  ref.current = { ...ref.current, "usgs-streamflow": true };
  assert.ok(model.contextSelectionChanges(learning.ids, sources, ref.current).length, "individual toggles remain custom selections");
  apply([], "Clear starter layers"); assert.ok(Object.values(ref.current).every(value => value === false));
  const count = calls.length; apply([], "Clear starter layers"); assert.equal(calls.length, count);
  apply(["private-parcels"], "Invalid"); assert.equal(calls.length, count); assert.match(announcements.at(-1), /remain selected/);
  assert.equal(JSON.stringify(preserved), before);
});

test("preferences are bounded public IDs only; empty selections, upgrades and explicit links restore correctly", () => {
  const valid = ids => JSON.stringify({ version: 1, ids });
  assert.deepEqual(model.parseContextPreference(valid([...learning.ids, "removed-layer", "private-record"]), sources), [...learning.ids]);
  assert.deepEqual(model.parseContextPreference(valid([]), sources), []);
  for (const raw of [null, "{", "[]", "x".repeat(8001), valid(["census-counties", "census-counties"]), valid([1]), JSON.stringify({ version: 2, ids: [] }), JSON.stringify({ version: 1, ids: [], camera: [1, 2] })]) assert.equal(model.parseContextPreference(raw, sources), null);
  assert.deepEqual(model.preferredContextIds(new URLSearchParams("ctx="), learning.ids), [""]);
  assert.deepEqual(model.preferredContextIds(new URLSearchParams("ctx=kdot-roads&c=1,2"), learning.ids), ["kdot-roads"]);
  assert.deepEqual(model.preferredContextIds(new URLSearchParams("topic=water"), learning.ids), learning.ids);
  assert.equal(model.preferredContextIds(new URLSearchParams(), null), null);
});

test("device storage writes exclude personal state and restricted IDs; failure is safe and forgetting is explicit", () => {
  const storage = memoryStorage(); globalThis.window = { localStorage: storage };
  assert.equal(model.writeContextPreference([...learning.ids, "private-record"], sources), true);
  assert.deepEqual(JSON.parse(storage.data.get(model.CONTEXT_PREFERENCE_KEY)), { version: 1, ids: [...learning.ids] });
  assert.deepEqual(model.readContextPreference(sources), [...learning.ids]);
  assert.equal(model.writeContextPreference(null, sources), true); assert.equal(storage.data.size, 0);
  globalThis.window = { get localStorage() { throw new Error("blocked"); } };
  assert.equal(model.readContextPreference(sources), null); assert.equal(model.writeContextPreference([], sources), false); assert.equal(model.writeContextPreference(null, sources), false);
  delete globalThis.window;
});

test("accessible native controls choose every starter, announce partial coverage, customize, and clear on the same desktop/mobile owner", async () => {
  for (const compact of [false, true]) {
    const h = await componentHarness("app/map-starters-control.tsx", { "./map-starters": model });
    const calls = [], props = { sources, access: available, visibility: {}, selectionReady: true, sourceStatus: () => "Available to request", onApply: (ids, title) => calls.push({ ids, title }), compact };
    const render = () => { const tree = h.render(h.exports.MapStartersControl, props); h.commit(); return tree; };
    let tree = render(); await settle(); tree = render();
    const select = findNode(tree, node => node.type === "select");
    assert.ok(select.props["aria-describedby"].includes("map-starters-description"));
    assert.equal(nodes(tree, "option").length, 6);
    for (const starter of model.MAP_STARTERS) {
      select.props.onChange({ target: { value: starter.id } }); tree = render();
      const button = findNode(tree, node => node.type === "button" && node.props.children === "Use starter");
      assert.equal(button.props.type, "button"); assert.equal(button.props.disabled, false); button.props.onClick();
      assert.deepEqual(calls.at(-1).ids, [...starter.ids]);
    }
    props.access = { ...available, "fema-flood-zones": { held: true, unavailable: false } }; tree = render();
    assert.ok(nodes(tree, "span").some(node => String(node.props.children).includes("Held")));
    findNode(tree, node => node.type === "button" && node.props.children === "Use starter").props.onClick(); tree = render();
    assert.match(findNode(tree, node => node.props?.role === "status").props.children, /skipped/);
    props.access = {}; tree = render(); assert.equal(findNode(tree, node => node.type === "button" && node.props.children === "Use starter").props.disabled, true);
    findNode(tree, node => node.type === "button" && node.props.children === "Clear context layers").props.onClick(); tree = render();
    assert.deepEqual(Array.from(calls.at(-1).ids), []);
    assert.equal(findNode(tree, node => node.props?.role === "status").props["aria-live"], "polite");
    assert.equal(nodes(tree, "select").length, 1); h.dispose();
  }
});

test("remember is opt-in, waits for restored selection, tracks custom selections and empty reset, and can be removed", async () => {
  const storage = memoryStorage(); globalThis.window = { localStorage: storage };
  const h = await componentHarness("app/map-starters-control.tsx", { "./map-starters": model });
  const props = { sources, access: available, visibility: { "census-counties": true }, selectionReady: false, sourceStatus: () => "Selected", onApply() {} };
  const render = () => { const tree = h.render(h.exports.MapStartersControl, props); h.commit(); return tree; };
  render(); await settle(); let tree = render(); assert.equal(storage.writes.length, 0);
  const checkbox = () => findNode(tree, node => node.type === "input" && node.props.type === "checkbox");
  assert.equal(checkbox().props.checked, false); assert.equal(checkbox().props.disabled, true);
  props.selectionReady = true; tree = render(); checkbox().props.onChange({ target: { checked: true } }); tree = render(); await settle();
  assert.deepEqual(model.readContextPreference(sources), ["census-counties"]);
  props.visibility = { "kdot-roads": true, "private-record": true }; tree = render(); await settle(); assert.deepEqual(model.readContextPreference(sources), ["kdot-roads"]);
  props.visibility = {}; tree = render(); await settle(); assert.deepEqual(model.readContextPreference(sources), []);
  checkbox().props.onChange({ target: { checked: false } }); tree = render(); assert.equal(model.readContextPreference(sources), null);
  assert.equal(checkbox().props.checked, false); h.dispose(); delete globalThis.window;
});

test("remembered preference cannot overwrite pending URL restoration; storage failure is announced", async () => {
  const storage = memoryStorage(); globalThis.window = { localStorage: storage };
  model.writeContextPreference(learning.ids, sources); storage.writes.length = 0;
  const h = await componentHarness("app/map-starters-control.tsx", { "./map-starters": model });
  const props = { sources, access: available, visibility: {}, selectionReady: false, sourceStatus: () => "Selected", onApply() {} };
  const render = () => { const tree = h.render(h.exports.MapStartersControl, props); h.commit(); return tree; };
  render(); await settle(); render(); assert.equal(storage.writes.length, 0);
  props.selectionReady = true; props.visibility = { "kdot-roads": true }; render(); await settle(); assert.deepEqual(model.readContextPreference(sources), ["kdot-roads"]);
  globalThis.window = { get localStorage() { throw new Error("blocked"); } };
  props.visibility = {}; render(); await settle(); const tree = render();
  assert.match(findNode(tree, node => node.props?.role === "status").props.children, /unavailable/);
  assert.equal(findNode(tree, node => node.type === "input").props.checked, false);
  h.dispose(); delete globalThis.window;
});
