#!/usr/bin/env node

import crypto from "node:crypto";
import fs from "node:fs/promises";
import { chromium } from "playwright";

const ARTIFACT_DIR = "artifacts/perf";
const ENVELOPE_PATH = "configs/maplibre/perf-envelope.v1.json";
const RENDER_DIFF_REPORT_PATH =
  "artifacts/perf/render-diff/render-diff-report.json";

const scenarios = [
  {
    name: "cache-heavy-layout-slim",
    cache: { maxTileCacheSize: 200, maxTileCacheZoomLevels: 3 },
    styleMode: "layout-first",
    tiles: "slim"
  },
  {
    name: "cache-light-heavy-paint-heavy",
    cache: { maxTileCacheSize: 50, maxTileCacheZoomLevels: 1 },
    styleMode: "heavy-paint",
    tiles: "heavy"
  }
];

function sha256Json(value) {
  return (
    "sha256:" +
    crypto
      .createHash("sha256")
      .update(JSON.stringify(value, Object.keys(value).sort()))
      .digest("hex")
  );
}

function p95(values) {
  if (!values.length) return 0;
  const sorted = [...values].sort((a, b) => a - b);
  return sorted[Math.floor(sorted.length * 0.95)] ?? 0;
}

function buildStyle({ styleMode, tiles }) {
  const sourceUrl =
    tiles === "slim"
      ? "http://localhost:8080/fixtures/slim/style.json"
      : "http://localhost:8080/fixtures/heavy/style.json";

  return {
    version: 8,
    glyphs: "https://demotiles.maplibre.org/font/{fontstack}/{range}.pbf",
    sources: {
      demo: {
        type: "vector",
        url: sourceUrl
      }
    },
    layers:
      styleMode === "layout-first"
        ? [
            {
              id: "roads",
              type: "line",
              source: "demo",
              "source-layer": "roads",
              layout: {
                visibility: "visible",
                "line-cap": "round"
              },
              paint: {
                "line-width": [
                  "interpolate",
                  ["linear"],
                  ["zoom"],
                  5,
                  0.5,
                  12,
                  2
                ],
                "line-color": "#888"
              }
            }
          ]
        : [
            {
              id: "roads",
              type: "line",
              source: "demo",
              "source-layer": "roads",
              paint: {
                "line-width": ["case", [">", ["zoom"], 10], 4, 1],
                "line-opacity": [
                  "interpolate",
                  ["linear"],
                  ["zoom"],
                  5,
                  0.2,
                  14,
                  1
                ],
                "line-color": [
                  "match",
                  ["get", "class"],
                  "primary",
                  "#ff0000",
                  "secondary",
                  "#00ff00",
                  "#888"
                ]
              }
            }
          ]
  };
}

async function main() {
  await fs.mkdir(`${ARTIFACT_DIR}/frame-times`, { recursive: true });
  await fs.mkdir(`${ARTIFACT_DIR}/screenshots`, { recursive: true });
  await fs.mkdir(`${ARTIFACT_DIR}/render-diff`, { recursive: true });

  const perfEnvelope = JSON.parse(
    await fs.readFile(ENVELOPE_PATH, "utf8")
  );

  const thresholds = perfEnvelope.thresholds;
  const results = [];

  const browser = await chromium.launch({ headless: true });

  for (const scenario of scenarios) {
    const page = await browser.newPage({
      viewport: { width: 1280, height: 720 }
    });

    await page.setContent(`
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8"/>
  <title>MapLibre Perf Smoke</title>
  <style>
    html, body, #map {
      margin: 0;
      width: 100%;
      height: 100%;
    }
  </style>
  <link
    href="https://unpkg.com/maplibre-gl@5.5.0/dist/maplibre-gl.css"
    rel="stylesheet"
  />
  <script src="https://unpkg.com/maplibre-gl@5.5.0/dist/maplibre-gl.js"></script>
</head>
<body>
  <div id="map"></div>
</body>
</html>
`);

    const style = buildStyle(scenario);

    const metrics = await page.evaluate(async ({ scenario, style }) => {

      const frameTimes = [];
      let lastFrame = performance.now();

      function rafLoop() {
        const now = performance.now();
        frameTimes.push(now - lastFrame);
        lastFrame = now;

        if (frameTimes.length < 300) {
          requestAnimationFrame(rafLoop);
        }
      }

      requestAnimationFrame(rafLoop);

      const loadStart = performance.now();

      const map = new maplibregl.Map({
        container: "map",
        style,
        center: [-98.6, 39.8],
        zoom: 6,
        attributionControl: false,
        maxTileCacheSize: scenario.cache.maxTileCacheSize,
        maxTileCacheZoomLevels: scenario.cache.maxTileCacheZoomLevels
      });

      const loadMs = await new Promise((resolve) => {
        map.on("load", () => resolve(performance.now() - loadStart));
        map.on("error", () => resolve(performance.now() - loadStart));
      });

      const idleStart = performance.now();

      map.easeTo({
        center: [-97.2, 38.9],
        zoom: 8,
        duration: 2500
      });

      const idleMs = await new Promise((resolve) => {
        map.on("idle", () => resolve(performance.now() - idleStart));
        setTimeout(() => resolve(performance.now() - idleStart), 5000);
      });

      const avgFrameMs =
        frameTimes.reduce((a, b) => a + b, 0) / frameTimes.length;

      const sortedFrames = [...frameTimes].sort((a, b) => a - b);
      const p95FrameMs =
        sortedFrames[Math.floor(sortedFrames.length * 0.95)] ?? 0;

      map.remove();

      return {
        loadMs: Math.round(loadMs),
        idleMs: Math.round(idleMs),
        frames: frameTimes.length,
        avgFrameMs: Number(avgFrameMs.toFixed(2)),
        p95FrameMs: Number(p95FrameMs.toFixed(2)),
        frameTimes: frameTimes.map((v) => Number(v.toFixed(4)))
      };
    }, { scenario, style });

    const frameTimesPath =
      `${ARTIFACT_DIR}/frame-times/${scenario.name}.csv`;

    const frameCsv =
      "frame_index,frame_ms\n" +
      metrics.frameTimes.map((v, i) => `${i},${v}`).join("\n") +
      "\n";

    await fs.writeFile(frameTimesPath, frameCsv);

    const screenshotPath =
      `${ARTIFACT_DIR}/screenshots/${scenario.name}.png`;

    await page.screenshot({
      path: screenshotPath,
      fullPage: true
    });

    const row = {
      scenario: scenario.name,
      styleMode: scenario.styleMode,
      tiles: scenario.tiles,
      loadMs: metrics.loadMs,
      idleMs: metrics.idleMs,
      frames: metrics.frames,
      avgFrameMs: metrics.avgFrameMs,
      p95FrameMs: metrics.p95FrameMs,
      frameTimesPath,
      screenshotPath,
      renderDiffReportPath: RENDER_DIFF_REPORT_PATH
    };

    results.push(row);

    await page.close();
  }

  await browser.close();

  const receiptScenarios = results.map((row) => {
    const passed =
      row.avgFrameMs <= thresholds.avg_frame_ms &&
      row.p95FrameMs <= thresholds.p95_frame_ms &&
      row.idleMs <= thresholds.idle_ms &&
      row.loadMs <= thresholds.load_ms;

    return {
      name: row.scenario,
      style_mode: row.styleMode,
      tile_set: row.tiles,
      avg_frame_ms: row.avgFrameMs,
      p95_frame_ms: row.p95FrameMs,
      idle_ms: row.idleMs,
      load_ms: row.loadMs,
      frame_times_path: row.frameTimesPath,
      screenshot_path: row.screenshotPath,
      render_diff_report_path: row.renderDiffReportPath,
      passed
    };
  });

  const now = new Date().toISOString();

  const runReceipt = {
    object_type: "RunReceipt",
    schema_version: "v1",
    run_id: `maplibre-perf-${now.replaceAll(":", "-")}`,
    created_utc: now,
    domain: "maplibre",
    status: receiptScenarios.every((s) => s.passed)
      ? "completed"
      : "failed",
    policy_posture: "public_safe",
    spec_hash: sha256Json({ scenarios, thresholds }),
    perf_envelope_path: ENVELOPE_PATH,
    perf_envelope_hash: sha256Json(perfEnvelope),
    scenarios: receiptScenarios
  };

  await fs.writeFile(
    `${ARTIFACT_DIR}/perf-results.json`,
    JSON.stringify(results, null, 2)
  );

  await fs.writeFile(
    `${ARTIFACT_DIR}/run-receipt.json`,
    JSON.stringify(runReceipt, null, 2)
  );

  console.table(results);

  console.log("\nANSWER: MapLibre smoke perf completed");
  console.log(`- ${ARTIFACT_DIR}/perf-results.json`);
  console.log(`- ${ARTIFACT_DIR}/run-receipt.json`);
}

main().catch((err) => {
  console.error("ERROR: MapLibre smoke perf failed");
  console.error(err);
  process.exit(1);
});
