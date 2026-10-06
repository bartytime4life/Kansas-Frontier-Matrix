import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

test("mobile map keeps primary actions reachable while the desktop dock actions stay hidden", async () => {
  const [page, css, toolbar, dataWorkspace] = await Promise.all([
    readFile(new URL("../app/page.tsx", import.meta.url), "utf8"),
    readFile(new URL("../app/globals.css", import.meta.url), "utf8"),
    readFile(new URL("../app/map-toolbar.tsx", import.meta.url), "utf8"),
    readFile(new URL("../app/data/workspace.module.css", import.meta.url), "utf8"),
  ]);

  assert.match(page, /<nav className="map-chrome-dock" aria-label="Map view and controls">/);
  assert.match(page, /<div className="map-dock-representations" role="group" aria-label="Map representation">/);
  assert.match(page, /<nav className="map-mobile-actions" aria-label="Mobile map actions">/);
  for (const label of ["Map layers", "Places", "Sources", "Time", "Style"]) assert.match(page, new RegExp(`>${label}(?:\\s|<)`));
  assert.match(page, /onClick=\{openMapSettings\}>Style<\/button>/);
  assert.match(page, /id="map-settings"/);
  assert.match(page, /<RenderQualityControl value=\{renderQuality\} onChange=\{chooseRenderQuality\} \/>/);
  assert.match(toolbar, /aria-label="Open data and download notices"/);
  assert.match(css, /safe-area-inset-bottom/);
  assert.match(css, /:root \{[\s\S]*?--global-header-height:\s*54px;[\s\S]*?--mobile-header-height:\s*96px;[\s\S]*?--topbar:\s*var\(--global-header-height\);/);
  assert.match(css, /@media \(min-width: 761px\) and \(max-width: 1100px\) \{[\s\S]*?\.mobile-primary-tabs \{ display: none; \}/);
  assert.match(css, /@media \(max-width: 760px\) \{\s*:root \{ --topbar: var\(--mobile-header-height\); \}[\s\S]*?\.mobile-primary-tabs \{ display: flex; grid-area: mobile; \}/);
  assert.match(css, /@media \(max-width: 760px\)[\s\S]*?\.brand-lockup \.mark \{ display: grid;/);
  assert.match(css, /@media \(max-width: 760px\)[\s\S]*?\.map-dock-actions \{ display: flex; flex: none;/);
  assert.match(css, /\.map-dock-actions > \.map-dock-menu:not\(\.map-dock-map-menu\) \{ display: none; \}/);
  assert.match(css, /\.map-stage\[data-live-dock="false"\] \.qwen-map-launch \{ bottom: calc\(74px \+ env\(safe-area-inset-bottom\)\); \}/);
  assert.match(css, /\.map-mobile-actions button, \.map-mobile-actions a \{ min-height: 48px;/);
  assert.match(css, /\.data-notices-trigger \{ min-width: 44px !important; width: 44px;/);
  assert.match(css, /\.map-source-status \{[\s\S]*border-radius: 20px 20px 0 0/);
  assert.match(css, /\.event-workspace \.event-calendar-cell \{ min-height: 32px/);
  assert.match(dataWorkspace, /\.page input,\.page select,\.page textarea\{min-height:48px;font-size:16px\}/);

  const finalToolSheetOverride = css.lastIndexOf(".map-utility-panel[data-view]");
  assert.ok(finalToolSheetOverride > css.lastIndexOf(".map-utility-panel { top: var(--map-overlay-top); right: 68px; }"));
  assert.match(css.slice(finalToolSheetOverride), /\.map-utility-panel\[data-view\] \{\s*inset: auto 0 0;\s*width: 100%;\s*height: min\(86dvh, 820px, 100%\);/);

  assert.match(page, /const visibleFocusableElements = \(container: HTMLElement\) =>/);
  assert.match(page, /textarea:not\(\[disabled\]\), summary/);
  assert.match(page, /element\.tabIndex >= 0/);
  assert.match(page, /!element\.closest\("\[hidden\], \[inert\]"\)/);
  assert.match(page, /element\.getClientRects\(\)\.length > 0/);
  assert.ok((page.match(/visibleFocusableElements\(/g) ?? []).length >= 4);
  assert.doesNotMatch(page, /filter\(\(element\) => !element\.hasAttribute\("hidden"\)\)/);

});

test("compact Qwen is a scrollable modal with contained keyboard focus", async () => {
  const [page, css] = await Promise.all([
    readFile(new URL("../app/page.tsx", import.meta.url), "utf8"),
    readFile(new URL("../app/globals.css", import.meta.url), "utf8"),
  ]);

  assert.match(page, /className="qwen-panel" role="dialog" aria-modal=\{isCompact\}/);
  const effectStart = page.indexOf("if (!qwenOpen || !isCompact) return;");
  const effectEnd = page.indexOf("}, [closeQwenCompanion, isCompact, qwenOpen]);", effectStart);
  assert.ok(effectStart >= 0 && effectEnd > effectStart, "compact Qwen focus effect must be present");
  const focusEffect = page.slice(effectStart, effectEnd);
  assert.match(focusEffect, /const panel = qwenPanelRef\.current;/);
  assert.match(focusEffect, /panel\.contains\(document\.activeElement\)[\s\S]*?focus\(\{ preventScroll: true \}\)/);
  assert.match(focusEffect, /event\.key === "Escape"[\s\S]*?event\.stopPropagation\(\);[\s\S]*?closeQwenCompanion\(\)/);
  assert.match(focusEffect, /event\.key !== "Tab"[\s\S]*?document\.activeElement === first[\s\S]*?last\.focus\(\)[\s\S]*?document\.activeElement === last[\s\S]*?first\.focus\(\)/);

  assert.match(css, /@media \(max-width: 760px\)[\s\S]*?\.qwen-panel\[aria-modal="true"\] \{[^}]*overflow-x: hidden;[^}]*overflow-y: auto;[^}]*overscroll-behavior: contain;[^}]*-webkit-overflow-scrolling: touch;/);
  assert.match(css, /@media \(max-width: 760px\)[\s\S]*?\.qwen-panel\[aria-modal="true"\] \.qwen-messages \{[^}]*flex: 0 0 auto;[^}]*max-height: min\(40dvh, 260px\);/);
});
