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
});
