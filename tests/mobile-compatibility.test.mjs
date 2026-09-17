import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

test("mobile map keeps layers, live data, sources, time, and style reachable without a desktop rail", async () => {
  const [page, css, toolbar, dataWorkspace] = await Promise.all([
    readFile(new URL("../app/page.tsx", import.meta.url), "utf8"),
    readFile(new URL("../app/globals.css", import.meta.url), "utf8"),
    readFile(new URL("../app/map-toolbar.tsx", import.meta.url), "utf8"),
    readFile(new URL("../app/data/workspace.module.css", import.meta.url), "utf8"),
  ]);

  assert.match(page, /<nav className="map-mobile-actions" aria-label="Mobile map actions">/);
  for (const label of ["Layers", "Live", "Sources", "Time", "Style"]) assert.match(page, new RegExp(`>${label}(?:\\s|<)`));
  assert.match(page, /openMapUtility\("display"\)/);
  assert.match(page, /map-render-quality-choice/);
  assert.match(toolbar, /aria-label="Open data and download notices"/);
  assert.match(css, /safe-area-inset-bottom/);
  assert.match(css, /\.map-control-strip \{ display: none; \}/);
  assert.match(css, /\.map-source-status \{[\s\S]*border-radius: 20px 20px 0 0/);
  assert.match(css, /\.event-workspace \.event-calendar-cell \{ min-height: 32px/);
  assert.match(dataWorkspace, /\.page input,\.page select,\.page textarea\{min-height:48px;font-size:16px\}/);

  const finalWorkbenchOverride = css.lastIndexOf(".map-utility-panel[data-view]");
  assert.ok(finalWorkbenchOverride > css.lastIndexOf(".map-utility-panel { top: 62px; right: 68px; }"));
  assert.match(css.slice(finalWorkbenchOverride), /\.map-utility-panel\[data-view\] \{\s*inset: auto 0 0;\s*width: 100%;\s*height: min\(86dvh, 820px, 100%\);/);

  assert.match(page, /const visibleFocusableElements = \(container: HTMLElement\) =>/);
  assert.match(page, /textarea:not\(\[disabled\]\), summary/);
  assert.match(page, /element\.tabIndex >= 0/);
  assert.match(page, /!element\.closest\("\[hidden\], \[inert\]"\)/);
  assert.match(page, /element\.getClientRects\(\)\.length > 0/);
  assert.ok((page.match(/visibleFocusableElements\(/g) ?? []).length >= 4);
  assert.doesNotMatch(page, /filter\(\(element\) => !element\.hasAttribute\("hidden"\)\)/);

  assert.match(page, /selectStoredFeature\(step\.layerId, step\.featureId\);\s*if \(isCompact\) setRightOpen\(false\);/);
  assert.match(page, /\[announce, commitTemporalFrame, isCompact, selectStoredFeature\]/);
});
