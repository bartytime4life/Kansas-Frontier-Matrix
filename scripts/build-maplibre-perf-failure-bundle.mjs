#!/usr/bin/env node

import crypto from "node:crypto";
import fs from "node:fs/promises";

const outPath =
  "artifacts/perf/failure-bundle.maplibre-perf.json";

const candidatePaths = [
  "artifacts/perf/run-receipt.json",
  "artifacts/perf/perf-results.json",
  "artifacts/perf/release-manifest.maplibre-perf.json",
  "artifacts/perf/render-diff/render-diff-report.json",
  "artifacts/perf/correction-notice.maplibre-perf.json",
  "artifacts/perf/rollback-plan.maplibre-perf.json"
];

function sha256(bytes) {
  return (
    "sha256:" +
    crypto.createHash("sha256").update(bytes).digest("hex")
  );
}

const artifacts = [];

for (const path of candidatePaths) {
  try {
    const bytes = await fs.readFile(path);

    artifacts.push({
      path,
      sha256: sha256(bytes)
    });
  } catch {
    // Artifact may not exist depending on failure point.
  }
}

const now = new Date().toISOString();

const bundle = {
  object_type: "FailureBundle",
  schema_version: "v1",
  domain: "maplibre",
  bundle_id: `maplibre-perf-failure-${now.replaceAll(":", "-")}`,
  created_utc: now,
  trigger: "perf_or_render_governance_failure",
  status: "captured",
  artifacts
};

await fs.mkdir("artifacts/perf", { recursive: true });

await fs.writeFile(outPath, JSON.stringify(bundle, null, 2));

console.log("ANSWER: wrote MapLibre perf FailureBundle");
console.log(`- ${outPath}`);
