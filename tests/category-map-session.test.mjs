import test from "node:test";
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import ts from "typescript";

const page = await readFile(process.env.KFM_SETUP_PAGE ?? "app/page.tsx", "utf8");
const ast = ts.createSourceFile("page.tsx", page, ts.ScriptTarget.Latest, true, ts.ScriptKind.TSX);
let opener;
const owners = new Map();
function visit(node) {
  if (ts.isVariableDeclaration(node) && node.name.getText(ast) === "openCategoryMap") opener = node.initializer.getText(ast);
  if (ts.isJsxSelfClosingElement(node)) {
    const key = node.attributes.properties.find(p => p.name?.getText(ast) === "key");
    if (key) owners.set(node.tagName.getText(ast), key.initializer.getText(ast));
  }
  ts.forEachChild(node, visit);
}
visit(ast);
const compile = source => ts.transpileModule(source, { compilerOptions: { target: ts.ScriptTarget.ES2022, module: ts.ModuleKind.CommonJS } }).outputText;
const mapsExports = {};
new Function("exports", compile(await readFile("app/category-maps.ts", "utf8")))(mapsExports);

function session() {
  const values = { setCategoryMapSession: 0, setAviationShowRequest: 7, setCropSelected: true,
    setReviewedWaterSelected: true, setReviewedWeatherSelected: true, setSoilMapState: { visible: true },
    setEarthEngineDisplay: { visible: { "ee-naip": true }, opacity: { "ee-naip": .5 } } };
  const refs = {};
  const calls = [];
  const registry = [{ id: "old-historical-layer" }];
  const official = [...new Set(Object.values(mapsExports.CATEGORY_MAPS).flatMap(look => look.starters))].map(id => ({ id }));
  refs.officialVisibilityRef = { current: Object.fromEntries(official.map(({id}) => [id, true])) };
  const functions = {
    categoryMap: mapsExports.categoryMap, OFFICIAL_CONTEXT_SOURCES: official, LAYER_REGISTRY: registry,
    clearSelectionState() { values.selected = null; values.drawerOpen = false; },
    setOfficialContextVisible(id, on) { refs.officialVisibilityRef.current[id] = on; },
    hideSoilContext: current => ({ ...current, visible: false }),
    FLORA_DEFAULT_YEAR: 2024,
  };
  const scope = new Proxy({}, {
    has: () => true,
    get(_target, name) {
      if (name === Symbol.unscopables) return undefined;
      if (name in functions) return functions[name];
      if (name in globalThis) return globalThis[name];
      if (name.endsWith("Ref")) return refs[name] ??= { current: null };
      if (name.startsWith("set")) return next => { values[name] = typeof next === "function" ? next(values[name]) : next; };
      return (...args) => { calls.push([name, ...args]); };
    },
  });
  // Execute the actual event handler. Map renderer/network behavior is tested
  // separately; these doubles record state ownership at the setup boundary.
  const open = new Function("scope", `with(scope) { ${compile(`const open = ${opener};`)} return open; }`)(scope);
  return { open, values, refs, calls };
}

test("every explicit setup open clears previous layers and evidence, including repeated opens", () => {
  const h = session();
  const sequence = ["agriculture", "government", "aviation", "government", "aviation", "aviation",
    ...Object.keys(mapsExports.CATEGORY_MAPS)];
  for (const [index, topic] of sequence.entries()) {
    h.values.selected = "old-earthquake"; h.values.drawerOpen = true;
    h.values.setPopChangeOn = true; h.values.setPopChangeCounty = "20141";
    h.refs.popChangePrismsRef = { current: true }; h.refs.popChangeHidCountiesRef = { current: true };
    h.open(topic);
    assert.equal(h.values.setCategoryMapSession, index + 1, `${topic}: starts a fresh owner lifecycle`);
    assert.equal(h.values.setAviationShowRequest > 0, topic === "aviation", `${topic}: aviation opens only when requested`);
    assert.equal(h.values.setCropSelected, false); assert.equal(h.values.setReviewedWaterSelected, false);
    assert.equal(h.values.setReviewedWeatherSelected, false); assert.equal(h.values.setSoilMapState.visible, false);
    assert.equal(h.values.setPopChangeOn, false); assert.equal(h.values.setPopChangeCounty, null);
    assert.equal(h.refs.popChangePrismsRef.current, false); assert.equal(h.refs.popChangeHidCountiesRef.current, false);
    assert.equal(h.values.selected, null); assert.equal(h.values.drawerOpen, false);
    assert.equal(h.values.setResearchOpen, false); assert.equal(h.values.setAviationInspect, null);
    assert.deepEqual(h.values.setVisibility, { "old-historical-layer": false });
    assert.deepEqual(h.values.setEarthEngineDisplay.visible, {});
    assert.equal(h.values.setEarthEngineDisplay.opacity["ee-naip"], .5, "hiding imagery preserves slider preferences");
    assert.equal(h.values.setImportPreviewVisible, false);
    assert.equal(h.values.setPlaying, false); assert.equal(h.values.setNoaaRadarPlaying, false);
    assert.deepEqual(Object.entries(h.refs.officialVisibilityRef.current).filter(([,on]) => on).map(([id]) => id).sort(),
      [...mapsExports.CATEGORY_MAPS[topic].starters].sort(), `${topic}: only the requested starter set remains`);
  }
});

test("internally owned layers share the explicit setup lifecycle, independently of catalogue filters", () => {
  for (const name of ["CropCasmaControl", "AviationLayerControl", "GovernedWaterControl", "GovernedWeatherControl", "EarthEngineDisplayControls"])
    assert.equal(owners.get(name), "{categoryMapSession}", `${name}: category change unmounts its old source owner`);
  assert.equal((page.match(/setCategoryMapSession\(/g) ?? []).length, 1, "only opening a setup resets these owners; filtering and 2D/3D controls do not");
});
