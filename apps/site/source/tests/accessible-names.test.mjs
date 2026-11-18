import assert from "node:assert/strict";
import { globSync } from "node:fs";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

// aria-label and aria-labelledby are ignored on elements with no role (a div,
// span, footer outside a landmark, b, and similar). A screen reader then never
// hears names such as "Radar playback" or "Map status". Every labelled generic
// element must declare the role that makes its name count: usually "group" for
// related controls or readouts, "img" for a purely visual scale whose label
// states its values, or "region" for a map container.
const GENERIC = new Set(["div", "span", "footer", "header", "p", "b", "strong", "em", "small", "i", "label"]);

function unnamedLabels(file, source) {
  const ast = ts.createSourceFile(file, source, ts.ScriptTarget.Latest, true, ts.ScriptKind.TSX);
  const found = [];
  const visit = (node) => {
    if (ts.isJsxOpeningElement(node) || ts.isJsxSelfClosingElement(node)) {
      const tag = node.tagName.getText(ast);
      const names = node.attributes.properties.filter(ts.isJsxAttribute).map((attribute) => attribute.name.getText(ast));
      if (GENERIC.has(tag) && (names.includes("aria-label") || names.includes("aria-labelledby")) && !names.includes("role")) {
        found.push(`${file}:${ast.getLineAndCharacterOfPosition(node.getStart()).line + 1} <${tag}>`);
      }
    }
    ts.forEachChild(node, visit);
  };
  visit(ast);
  return found;
}

test("labelled generic elements declare a role so their accessible name is announced", async () => {
  const files = globSync("app/**/*.tsx");
  assert.ok(files.length > 50, "scans the Explorer components");
  const found = [];
  for (const file of files) found.push(...unnamedLabels(file, await readFile(file, "utf8")));
  assert.deepEqual(found, []);
});

test("the scan flags a roleless label and accepts each allowed form", () => {
  assert.deepEqual(unnamedLabels("x.tsx", '<div aria-label="Radar playback"><button /></div>'), ["x.tsx:1 <div>"]);
  assert.deepEqual(unnamedLabels("x.tsx", '<footer className="status-bar" aria-label="Map status" />'), ["x.tsx:1 <footer>"]);
  assert.deepEqual(unnamedLabels("x.tsx", '<div role="group" aria-label="Radar playback" />'), []);
  assert.deepEqual(unnamedLabels("x.tsx", '<nav aria-label="Map tools" />'), [], "elements with an implicit role are left alone");
  assert.deepEqual(unnamedLabels("x.tsx", '<b aria-hidden="true">3</b>'), []);
});

test("the data notices button names its counts and hides the badge digits", async () => {
  const toolbar = await readFile("app/map-toolbar.tsx", "utf8");
  assert.match(toolbar, /aria-label=\{`Open data and download notices: \$\{issues\.length\} source issue/);
  assert.match(toolbar, /<b aria-hidden="true">\{issues\.length \|\| DOWNLOAD_NOTICES\.length\}<\/b>/);
});

test("the Observatory storm key is a labelled section, not a nested complementary landmark", async () => {
  const panel = await readFile("app/observatory/storm-panel.tsx", "utf8");
  assert.match(panel, /<section className="event-storm-key" aria-label="Storm cell map key">/);
  assert.doesNotMatch(panel, /<aside className="event-storm-key"/);
});
