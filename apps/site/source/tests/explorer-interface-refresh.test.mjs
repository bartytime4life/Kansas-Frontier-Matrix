import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

const read = (path) => readFile(new URL(`../${path}`, import.meta.url), "utf8");

async function importTs(path) {
  const ts = await import("typescript");
  const source = await read(path);
  const javascript = ts.transpileModule(source, {
    compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
    fileName: path,
  }).outputText;
  return import(`data:text/javascript;base64,${Buffer.from(javascript).toString("base64")}`);
}

test("offline orientation is bundled display geometry inside the Kansas frame", async () => {
  const orientation = await importTs("app/kansas-orientation.ts");
  const features = orientation.KANSAS_ORIENTATION.features;
  const outline = features.find((feature) => feature.properties.role === "outline");
  assert.ok(outline, "Kansas outline present");
  const ring = outline.geometry.coordinates[0];
  assert.deepEqual(ring[0], ring.at(-1), "outline ring is closed");
  for (const [lon, lat] of ring) {
    assert.ok(lon >= -102.06 && lon <= -94.58, `longitude ${lon} inside Kansas`);
    assert.ok(lat >= 36.99 && lat <= 40.01, `latitude ${lat} inside Kansas`);
  }
  assert.ok(features.filter((feature) => feature.properties.role === "river").length >= 4);
  assert.ok(features.some((feature) => feature.properties.role === "graticule"));
  const layers = orientation.orientationLayers({ land: "#000", outline: "#111", river: "#222", graticule: "#333" });
  assert.ok(layers.length >= 3);
  for (const layer of layers) {
    // `kfm-` ids are treated as registry overlays by placement logic.
    assert.doesNotMatch(layer.id, /^kfm-/);
    assert.equal(layer.source, orientation.ORIENTATION_SOURCE_ID);
    assert.notEqual(layer.type, "symbol", "no glyph dependency offline");
  }
  assert.equal(orientation.orientationSource().type, "geojson");
  assert.match(orientation.orientationSource().attribution, /display only/);
});

test("local basemaps carry the orientation layer and stay network-free", async () => {
  const runtime = await read("app/map-runtime.ts");
  for (const name of ["KFM Midnight", "KFM Prairie Dusk"]) {
    const block = runtime.slice(runtime.indexOf(name), runtime.indexOf(name) + 600);
    assert.match(block, /\[ORIENTATION_SOURCE_ID\]: orientationSource\(\)/);
    assert.match(block, /\.\.\.orientationLayers\(/);
    assert.match(block, /id: "kfm-background"/);
    assert.doesNotMatch(block, /tiles:|https?:\/\//);
  }
});

test("the map exposes one zoom control set and no fixed place label", async () => {
  const page = await read("app/page.tsx");
  const css = await read("app/globals.css");
  assert.match(page, /new mapLibre\.NavigationControl\(\{ showCompass: true, showZoom: false, visualizePitch: true \}\)/);
  assert.match(page, /aria-label="Zoom in"/);
  assert.match(page, /aria-label="Zoom out"/);
  assert.match(page, /aria-label="Reset view to Kansas"/);
  assert.doesNotMatch(css, /SMOKY HILLS · KANOPOLIS/);
});

test("quick start routes only to existing controls and tolerates blocked storage", async () => {
  const guide = await read("app/explorer-guide.tsx");
  const page = await read("app/page.tsx");
  assert.match(guide, /EXPLORER_GUIDE_STORAGE_KEY = "kfm\.explorer\.guide\.dismissed\.v1"/);
  assert.equal((guide.match(/try \{/g) ?? []).length, 2, "both storage reads and writes are guarded");
  assert.match(guide, /role="dialog" aria-modal="false"/);
  assert.match(guide, /panelRef\.current\?\.contains\(document\.activeElement\)/, "Escape only closes when focus is inside");
  assert.doesNotMatch(guide, /fetch\(|import\(.*api/);
  assert.match(page, /<ExplorerGuide open=\{guideOpen\}/);
  assert.match(page, /className="guide-trigger" type="button" aria-label="Open the quick start guide"/);
  assert.match(page, /if \(action === "layers"\) openAtlasPanel\("layers"\)/);
  assert.match(page, /else if \(action === "time"\) setTimelineOpen\(true\)/);
  assert.match(page, /else if \(action === "qwen"\) openQwenCompanion\(null\)/);
  assert.match(page, /onMore=\{\(\) => setHelpOpen\(true\)\}/, "reconnects the existing map guide");
  assert.match(page, /aria-pressed=\{undergroundOpen\} onClick=\{toggleUnderground\}/);
});

test("theme loads last, keeps tested geometry in globals and honours reduced motion", async () => {
  const layout = await read("app/layout.tsx");
  const theme = await read("app/explorer-theme.css");
  assert.ok(layout.indexOf('import "./explorer-theme.css"') > layout.indexOf('import "./map-layers.css"'));
  for (const token of ["--bg", "--panel", "--gold", "--water", "--kfm-radius-m", "--kfm-glass"]) assert.match(theme, new RegExp(`${token}:`));
  assert.doesNotMatch(theme, /--topbar:|--global-header-height:|--map-overlay-top:/, "layout tokens stay in globals.css");
  assert.match(theme, /@media \(prefers-reduced-motion: reduce\)[\s\S]*\.explorer-guide \{ animation: none; \}/);
  assert.match(theme, /\.explorer-shell\[data-timeline="false"\] \.timeline-panel \{ transform: translateY\(calc\(100% \+ var\(--status\) \+ 16px\)\)/);
  const banner = theme.match(/\.runtime-degraded-banner \{([^}]+)\}/)?.[1] ?? "";
  assert.doesNotMatch(banner, /(^|[\s;])(pointer-events|top|left|width)\s*:/, "notice geometry is owned by globals.css");
});
