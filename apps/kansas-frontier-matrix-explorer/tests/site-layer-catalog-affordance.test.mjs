import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

const appRoot = new URL("../app/", import.meta.url);
const source = await readFile(new URL("site-layer-library.tsx", appRoot), "utf8");
const css = await readFile(new URL("site-layer-library.css", appRoot), "utf8");

const enhancementStart = source.indexOf("function enhanceCatalogScrollRegion");
const enhancementEnd = source.indexOf("/** A failed owner read");
const enhancement = source.slice(enhancementStart, enhancementEnd);

test("full Layer Catalog gets one bounded keyboard-scroll affordance", () => {
  assert.ok(enhancementStart >= 0 && enhancementEnd > enhancementStart);
  assert.match(source, /const CATALOG_SCROLL_SELECTOR = "\.layer-panel \.catalog-groups"/);
  assert.match(enhancement, /region\.tabIndex = 0/);
  assert.match(enhancement, /region\.setAttribute\("role", "region"\)/);
  assert.match(enhancement, /ResizeObserver/);
  assert.match(enhancement, /MutationObserver/);
  assert.match(source, /dataset\.scrollable/);
  assert.match(source, /dataset\.atStart/);
  assert.match(source, /dataset\.atEnd/);
});

test("filtered catalog counts and labels remain truthful", () => {
  assert.match(source, /currentControlCount/);
  assert.match(source, /data-current-control-count/);
  assert.match(source, /from \$\{layerCount\} registered layers/);
  assert.match(source, /Scroll to reach all current matches/);
  assert.doesNotMatch(source, /Scroll to reach every layer/);
});

test("catalog enhancement remains presentational and local-only", () => {
  assert.doesNotMatch(enhancement, /\.click\s*\(/);
  assert.doesNotMatch(enhancement, /dispatchEvent|fetch\s*\(|XMLHttpRequest|WebSocket/);
  assert.doesNotMatch(enhancement, /localStorage|sessionStorage|history\./);
  assert.doesNotMatch(enhancement, /onChange|setVisibility|setOpacity/);
});

test("summary distinguishes requested visibility from time compatibility", () => {
  assert.match(source, /requestedCount/);
  assert.match(source, /timeCompatibleCount/);
  assert.match(source, /requested visible/);
  assert.match(source, /time-compatible/);
  assert.match(source, /renderer delivery remains held/);
  assert.match(source, /className="site-layer-library-divider"/);
  assert.match(css, /\.site-layer-library-divider/);
  assert.doesNotMatch(css, /site-layer-library-summary i/);
});

test("CSS preserves a single visible catalog scroller across viewports", () => {
  assert.match(css, /\.layer-panel \.catalog-groups\s*\{/);
  assert.match(css, /overflow-y:\s*auto/);
  assert.match(css, /scrollbar-gutter:\s*stable/);
  assert.match(css, /overscroll-behavior-y:\s*contain/);
  assert.match(css, /data-at-start="false"/);
  assert.match(css, /data-at-end="false"/);
  assert.match(css, /:focus-visible/);
  assert.match(css, /@media \(max-width: 720px\)/);
  assert.match(css, /@media \(prefers-reduced-motion: reduce\)/);
  assert.doesNotMatch(css, /\.layer-panel \.catalog-groups[^}]*display:\s*none/s);
});
