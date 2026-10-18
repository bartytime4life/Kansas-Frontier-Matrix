import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";
import { componentHarness, findNode, settle } from "./component-harness.mjs";
import { PRIVATE_PROFILE_TEST_ONLY } from "./private-profile-test-only.mjs";

const read = file => readFile(new URL(`../${file}`, import.meta.url), "utf8");
const page = ts.createSourceFile("page.tsx", await read("app/page.tsx"), ts.ScriptTarget.Latest, true, ts.ScriptKind.TSX);
const nodes = [];
function visit(node) { nodes.push(node); ts.forEachChild(node, visit); }
visit(page);
const attr = (node, name) => node.attributes.properties.find(a => a.name?.getText(page) === name)?.initializer;
const declaration = name => nodes.find(n => ts.isVariableDeclaration(n) && n.name.getText(page) === name).initializer;
const evaluate = (node, scope) => new Function(...Object.keys(scope), ts.transpileModule(`const result = ${node.getText(page)};`, { compilerOptions: { target: ts.ScriptTarget.ES2022 } }).outputText + "; return result;")(...Object.values(scope));

test("Map identifies one foreground mode and switching out of Underground/Compare reveals the chosen map", () => {
  const group = declaration("mapRepresentationControls");
  const buttons = nodes.filter(n => ts.isJsxOpeningElement(n) && n.tagName.getText(page) === "button" && n.pos >= group.pos && n.end <= group.end && attr(n, "aria-pressed"));
  assert.equal(buttons.length, 5);
  for (const mode of ["underground", "2d", "terrain", "globe", "compare"]) {
    const scope = { undergroundOpen: mode === "underground", mapUtilityOpen: mode === "compare", mapUtilityView: "compare", projection: mode === "globe" ? "globe" : "mercator", scenePreset: mode === "terrain" ? "elevation-3d" : "overview-2d" };
    const active = buttons.map(n => evaluate(attr(n, "aria-pressed").expression, scope));
    assert.equal(active.filter(Boolean).length, 1, mode);
    assert.equal(active[["underground", "2d", "terrain", "globe", "compare"].indexOf(mode)], true);
  }
  for (const from of ["compare", "scene", "localAtlas"]) for (const target of ["2d", "terrain", "globe"]) {
    const calls = [];
    evaluate(declaration("chooseMapMenuRepresentation"), { mapUtilityView: from, setUndergroundOpen: v => calls.push(["underground", v]), setMapUtilityOpen: v => calls.push(["utility", v]), activateMapRepresentation: v => calls.push(["view", v]) })(target);
    assert.deepEqual(calls, [["underground", false], ...(from === "compare" ? [["utility", false]] : []), ["view", target]]);
  }
});

test("Effects returns to the map from private draft workspaces and closes competing mobile panels", () => {
  for (const isCompact of [false, true]) for (const open of [false, true]) {
    const state = { workspace: "reports", effects: false, guide: true, utility: true, sources: true, left: true, right: true, qwen: true };
    const draft = { title: "Owner report", sections: ["evidence"] };
    evaluate(declaration("changeScenePanelOpen"), {
      useCallback: fn => fn, isCompact, draft,
      setScenePanelOpen: v => state.effects = v, setPrimaryWorkspace: v => state.workspace = v,
      setGuideOpen: v => state.guide = v, dismissMapUtilityWithoutFocus: () => state.utility = false,
      setSourceStatusOpen: v => state.sources = v, setLeftOpen: v => state.left = v,
      setRightOpen: v => state.right = v, setQwenOpen: v => state.qwen = v,
    })(open);
    assert.equal(state.effects, open);
    assert.equal(state.workspace, open ? "map" : "reports");
    assert.equal(state.utility, !open);
    for (const key of ["sources", "left", "right", "qwen"]) assert.equal(state[key], !(open && isCompact), key);
    assert.deepEqual(draft, { title: "Owner report", sections: ["evidence"] });
  }
});

test("Source status stays inside Layers, filters selected/all without changing visibility, and retains private downloads", () => {
  const source = nodes.find(n => ts.isJsxOpeningElement(n) && attr(n, "id")?.text === "map-source-status");
  let parent = source.parent;
  while (parent && !(ts.isJsxElement(parent) && attr(parent.openingElement, "className")?.text === "layer-panel")) parent = parent.parent;
  assert.ok(parent, "source recovery belongs to the layer drawer");
  const filter = nodes.find(n => ts.isCallExpression(n) && n.expression.getText(page) === "OFFICIAL_CONTEXT_SOURCES.filter" && n.arguments[0].getText(page).includes("sourceStatusScope"));
  const officialVisibility = { census: true, river: false }, sources = [{ id: "census" }, { id: "river" }];
  for (const sourceStatusScope of ["selected", "all"]) {
    assert.deepEqual(evaluate(filter, { sourceStatusScope, OFFICIAL_CONTEXT_SOURCES: sources, officialVisibility }), sourceStatusScope === "all" ? sources : [sources[0]]);
    assert.deepEqual(officialVisibility, { census: true, river: false });
  }
  const data = nodes.filter(n => ts.isJsxSelfClosingElement(n) && n.tagName.getText(page) === "DataNotices");
  assert.equal(data.length, 1);
  assert.ok(data[0].attributes.properties.some(a => a.name?.getText(page) === "embedded"));
  assert.ok(data[0].pos > source.pos && data[0].end < source.parent.end);
});

test("header Effects uses the parent's open state, shares settings, and keeps water controls first", async () => {
  let open = false, settings = { waterFlow: false, stars: true };
  const changes = [], listeners = new Map();
  const scene = {
    SCENE_EFFECT_OPTIONS: [{ key: "stars", label: "Stars", views: ["globe"], detail: "Catalog stars" }, { key: "waterFlow", label: "Flowing water", views: ["2d"], detail: "Direction only", network: true }],
    SCENE_LOOK_PRESETS: { plain: { label: "Plain", settings: { waterFlow: false, stars: false } } }, matchingLookPreset: () => null,
  };
  const h = await componentHarness(new URL("../app/scene-effects-controls.tsx", import.meta.url), {
    "./scene-effects": scene, "./scene-studio": { matchingSceneRecipe: () => null }, "./terrain-surface": {},
  }, { document: { addEventListener: (type, fn) => listeners.set(type, fn), removeEventListener: type => listeners.delete(type) } }, "\nexport { SceneEffectSwitches };\n");
  const props = () => ({ toolbar: true, open, settings, view: "2d", presentation: {}, onOpenChange: v => { open = v; }, onChange: v => { settings = v; changes.push(v); } });
  const render = () => { const tree = h.render(h.exports.ScenePanel, props()); h.commit(); return tree; };
  let tree = render();
  const trigger = findNode(tree, n => n.type === "button");
  assert.equal(trigger.props["aria-label"], "Effects & rendering");
  trigger.props.onClick(); tree = render();
  assert.ok(findNode(tree, n => n.props?.role === "dialog"));
  open = false; tree = render();
  assert.equal(findNode(tree, n => n.props?.role === "dialog"), undefined, "opening another tool closes Effects immediately");
  assert.equal(listeners.size, 0);
  const switches = h.render(h.exports.SceneEffectSwitches, { ...props(), cameraReady: true, efficient: false, reducedMotion: false });
  const first = findNode(switches, n => n.type === "input");
  assert.equal(first.props["aria-label"], "Flowing water"); first.props.onChange();
  assert.deepEqual({ ...changes.at(-1) }, { waterFlow: true, stars: true });
  h.dispose();
});

test("embedded dated downloads still save exact-day context locally through the bounded reader", async () => {
  const calls = [], saved = [], payload = { featureCount: 3 };
  const h = await componentHarness(new URL("../app/map-toolbar.tsx", import.meta.url), {
    "./public-profile": PRIVATE_PROFILE_TEST_ONLY,
    "next/link": { default: "a" }, "./source-downloads": { SOURCE_DOWNLOADS: {} }, "./map-performance": { QUALITY_LABELS: {} },
    "./daily-baseline": { currentUtcDay: () => "2026-10-16" }, "./event-atlas": { eventDay: value => /^\d{4}-\d{2}-\d{2}$/.test(value) },
    "./bounded-json": { readBoundedJson: async (_response, limit) => { assert.equal(limit, 8 * 1024 * 1024); return payload; } },
    "./map-context-cache": { mapCachePath: (_kind, day) => day, saveFireDay: async (day, value) => { saved.push([day, value]); return 512; } },
  }, { fetch: async (url, options) => { calls.push([url, options]); return { ok: true }; } });
  const dates = [], render = () => h.render(h.exports.DataNotices, { embedded: true, onFireSaved: day => dates.push(day) });
  let tree = render();
  assert.equal(tree.props.className, "data-notices data-notices-inline");
  findNode(tree, n => n.props?.className === "data-notices-trigger").props.onClick(); tree = render();
  assert.ok(findNode(tree, n => n.props?.href === "/downloads"));
  assert.ok(findNode(tree, n => n.props?.href === "/stewards"));
  assert.ok(findNode(tree, n => n.props?.href === "/data"));
  const choice = findNode(tree, n => n.type === "div" && n.props?.className === "map-download-choice" && findNode(n, child => child.type === "button"));
  findNode(choice, n => n.type === "input").props.onChange({ currentTarget: { value: "2026-10-15" } }); tree = render();
  findNode(tree, n => n.type === "button" && n.props.children === "Save day for map").props.onClick(); await settle();
  assert.equal(calls[0][0], "/api/live-context?feed=nasa-gibs-fire-points&day=2026-10-15");
  assert.equal(calls[0][1].cache, "no-store");
  assert.deepEqual(saved, [["2026-10-15", payload]]); assert.deepEqual(dates, ["2026-10-15"]);
});

test("public hosted chat opens a fixed live destination without transferring staging context", async () => {
  const identity = await import(`data:text/javascript;base64,${Buffer.from(ts.transpileModule(await read("app/site-identity.ts"), { compilerOptions: { module: ts.ModuleKind.ESNext } }).outputText).toString("base64")}`);
  const link = nodes.find(n => ts.isJsxOpeningElement(n) && n.tagName.getText(page) === "a" && attr(n, "className")?.text === "qwen-map-launch hosted-chat-launch");
  assert.ok(link);
  const href = evaluate(attr(link, "href").expression, { SITE_IDENTITY: identity.SITE_IDENTITY });
  assert.equal(href, "https://kansasfrontiermatrix.com/?kfm-chat=1");
  assert.equal(attr(link, "target").text, "_blank");
  assert.equal(attr(link, "rel").text, "noopener noreferrer");
  assert.equal(attr(link, "onClick"), undefined, "opening chat never sends records, draft text or camera coordinates");
});
