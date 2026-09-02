#!/usr/bin/env node

import fs from "node:fs/promises";
import path from "node:path";
import pixelmatch from "pixelmatch";
import { PNG } from "pngjs";

const screenshotsDir = "artifacts/perf/screenshots";
const baselineDir = "tests/fixtures/maplibre/baselines";
const diffDir = "artifacts/perf/render-diff";

const envelope = JSON.parse(
  await fs.readFile("configs/maplibre/perf-envelope.v1.json", "utf8")
);

const threshold = envelope.thresholds.render_pixel_delta_ratio;

await fs.mkdir(diffDir, { recursive: true });

const screenshots = await fs.readdir(screenshotsDir);
const reports = [];

for (const file of screenshots.filter((f) => f.endsWith(".png"))) {
  const screenshotPath = path.join(screenshotsDir, file);
  const baselinePath = path.join(baselineDir, file);
  const diffPath = path.join(diffDir, file.replace(".png", ".diff.png"));

  let status = "compared";
  let passed = true;
  let pixelDeltaRatio = 0;
  const notes = [];

  try {
    const actual = PNG.sync.read(await fs.readFile(screenshotPath));
    const baseline = PNG.sync.read(await fs.readFile(baselinePath));

    if (actual.width !== baseline.width || actual.height !== baseline.height) {
      status = "dimension_mismatch";
      passed = false;
      notes.push("Screenshot dimensions do not match baseline.");
    } else {
      const diff = new PNG({
        width: actual.width,
        height: actual.height
      });

      const changedPixels = pixelmatch(
        actual.data,
        baseline.data,
        diff.data,
        actual.width,
        actual.height,
        { threshold: 0.1 }
      );

      pixelDeltaRatio = changedPixels / (actual.width * actual.height);
      passed = pixelDeltaRatio <= threshold;

      await fs.writeFile(diffPath, PNG.sync.write(diff));
    }
  } catch (err) {
    status = "missing_baseline";
    passed = false;
    notes.push(String(err.message ?? err));
  }

  reports.push({
    scenario: file.replace(".png", ""),
    screenshot_path: screenshotPath,
    baseline_path: baselinePath,
    diff_path: diffPath,
    status,
    pixel_delta_ratio: Number(pixelDeltaRatio.toFixed(6)),
    threshold,
    passed,
    notes
  });
}

const report = {
  object_type: "RenderDiffReport",
  schema_version: "v1",
  domain: "maplibre",
  created_utc: new Date().toISOString(),
  status: reports.every((r) => r.passed) ? "passed" : "failed",
  threshold,
  scenarios: reports
};

await fs.writeFile(
  path.join(diffDir, "render-diff-report.json"),
  JSON.stringify(report, null, 2)
);

if (report.status !== "passed") {
  console.error("DENY: render diff failed");
  console.error(JSON.stringify(report, null, 2));
  process.exit(1);
}

console.log("ANSWER: render diff passed");
