import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

function undergroundImports(source) {
  const imports = new Set();
  const sourceFile = ts.createSourceFile("map.js", source, ts.ScriptTarget.Latest, true, ts.ScriptKind.JS);
  function visit(node) {
    if (ts.isCallExpression(node) && node.expression.kind === ts.SyntaxKind.ImportKeyword) {
      const target = node.arguments[0];
      if (target && (ts.isStringLiteral(target) || ts.isNoSubstitutionTemplateLiteral(target))
        && /^\.\/underground-panel-[A-Za-z0-9_-]+\.js$/.test(target.text)) imports.add(target.text);
    }
    ts.forEachChild(node, visit);
  }
  visit(sourceFile);
  return [...imports];
}

test("Underground chunk selection follows dynamic imports, excluding retained filenames and static imports", () => {
  const source = [
    'const retainedAssets = ["./underground-panel-Old.js"];',
    '// import("./underground-panel-Comment.js")',
    'import "./underground-panel-Eager.js";',
    'const load = () => import(`./underground-panel-Current.js`);',
  ].join("\n");
  assert.deepEqual(undergroundImports(source), ["./underground-panel-Current.js"]);
  assert.deepEqual(undergroundImports('import "./underground-panel-Eager.js";'), []);
});

test("the built main-map dependency list excludes the on-demand Underground implementation", async () => {
  const { default: manifest } = await import("../dist/server/__vite_rsc_assets_manifest.js");
  const readAsset = file => readFile(new URL(`../dist/client${file}`, import.meta.url), "utf8");
  const entries = Object.values(manifest.clientReferenceDeps);
  const mapEntries = new Map();
  for (const entry of entries) for (const file of entry.js) {
    if (/\/page-[^/]+\.js$/.test(file)) {
      const source = await readAsset(file);
      if (source.includes("Preparing spatial explorer")) mapEntries.set(file, { entry, source });
    }
  }
  assert.equal(mapEntries.size, 1, "identify one current main-map entry from the manifest and rendered loading surface");
  const [mapFile, { entry: mapEntry, source }] = [...mapEntries][0];
  // Immutable historical chunks are deliberately retained for open tabs. Only
  // actual imports from the current manifest's map module establish this build.
  const underground = undergroundImports(source);
  assert.equal(underground.length, 1, "the current map dynamically imports one separate Underground implementation chunk");
  const undergroundFile = new URL(underground[0], `https://build.invalid${mapFile}`).pathname;
  assert.ok(!mapEntry.js.includes(undergroundFile), "do not statically preload the optional panel");
  assert.ok(!mapEntry.js.some(file => /\/underground-panel-[^/]+\.js$/.test(file)), "no Underground implementation belongs to the initial dependency list");
  const initial = (await Promise.all(mapEntry.js.map(readAsset))).join("\n");
  assert.doesNotMatch(initial, /Source assets are loading\./, "the Underground worker state remains outside the initial code");
  assert.match(await readAsset(undergroundFile), /Source assets are loading\./);
});
