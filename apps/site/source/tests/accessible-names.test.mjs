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

test("charts and legends with readable values stay groups, not images", async () => {
  // role="img" makes descendants presentational; keep it only where the label
  // already states everything the children show.
  const page = await readFile("app/page.tsx", "utf8");
  const atlas = await readFile("app/local-atlas-control.tsx", "utf8");
  assert.match(page, /<div role="group" className="availability-bars"/, "per-range peak counts stay readable");
  assert.match(atlas, /<div role="group" className="local-atlas-legend"/, "decrease/increase and no-data notes stay readable");
  assert.match(page, /<div role="img" className="terrain-height-ramp" aria-label="Elevation color scale from 200 to 1,250 meters">/);
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

test("the map view keeps one exposed page heading while the layer panel is closed", async () => {
  // The layer panel starts closed and is aria-hidden, so a heading inside it
  // cannot be the page's only h1. The page heading sits directly in <main>.
  const page = await readFile("app/page.tsx", "utf8");
  const ast = ts.createSourceFile("page.tsx", page, ts.ScriptTarget.Latest, true, ts.ScriptKind.TSX);
  const headings = [];
  const visit = (node) => {
    if (ts.isJsxElement(node) && node.openingElement.tagName.getText(ast) === "h1") {
      const parent = ts.isJsxElement(node.parent) ? node.parent.openingElement.tagName.getText(ast) : undefined;
      headings.push({ text: node.getText(ast), parent });
    }
    ts.forEachChild(node, visit);
  };
  visit(ast);
  assert.deepEqual(headings, [{ text: '<h1 className="sr-only">Kansas Frontier Matrix Explorer</h1>', parent: "main" }]);
  assert.match(page, /<p className="panel-kicker">[^\n]*<\/p><h2>\{leftPanelMode === "views"/, "the panel title is a section heading");
  assert.match(page, /\[leftOpen, setLeftOpen\] = useState\(false\)/, "the panel starts closed, which is why the page heading lives outside it");
  // The layer-mode title styles (flex row for the selection badge, larger size)
  // must follow the heading to its new level.
  for (const file of globSync("app/**/*.css")) {
    assert.doesNotMatch(await readFile(file, "utf8"), /data-panel-mode="(?:layers|live)"\] \.panel-heading h1(?![\w-])/, `${file} still styles the layer panel title as an h1`);
  }
  assert.match(await readFile("app/map-layers.css", "utf8"), /\.layer-panel\[data-panel-mode="layers"\] \.panel-heading h2,\n\.layer-panel\[data-panel-mode="live"\] \.panel-heading h2 \{\n  display: flex;/);
});
