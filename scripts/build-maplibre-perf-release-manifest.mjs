#!/usr/bin/env node

import crypto from "node:crypto";
import fs from "node:fs/promises";

const outPath =
  "artifacts/perf/release-manifest.maplibre-perf.json";

const artifacts = [
  {
    name: "run-receipt",
    path: "artifacts/perf/run-receipt.json",
    role: "run_receipt"
  },
  {
    name: "perf-results",
    path: "artifacts/perf/perf-results.json",
    role: "perf_results"
  },
  {
    name: "run-receipt-dsse",
    path: "artifacts/perf/run-receipt.dsse.json",
    role: "attestation"
  },
  {
    name: "run-receipt-sha256",
    path: "artifacts/perf/run-receipt.sha256",
    role: "checksum"
  },
  {
    name: "perf-envelope",
    path: "configs/maplibre/perf-envelope.v1.json",
    role: "perf_envelope"
  },
  {
    name: "render-diff-report",
    path: "artifacts/perf/render-diff/render-diff-report.json",
    role: "render_diff"
  }
];

function sha256(bytes) {
  return (
    "sha256:" +
    crypto.createHash("sha256").update(bytes).digest("hex")
  );
}

async function maybeAdd(path, name, role) {
  try {
    await fs.access(path);
    artifacts.push({ name, path, role });
  } catch {
    // Optional artifact not present.
  }
}

const results = JSON.parse(
  await fs.readFile("artifacts/perf/perf-results.json", "utf8")
);

for (const row of results) {
  if (row.frameTimesPath) {
    artifacts.push({
      name: `frame-times-${row.scenario}`,
      path: row.frameTimesPath,
      role: "frame_times"
    });
  }

  if (row.screenshotPath) {
    artifacts.push({
      name: `screenshot-${row.scenario}`,
      path: row.screenshotPath,
      role: "screenshot"
    });
  }
}

await maybeAdd(
  "artifacts/perf/proof-pack.maplibre-perf.json",
  "proof-pack-maplibre-perf",
  "proof_pack"
);

await maybeAdd(
  "artifacts/perf/correction-notice.maplibre-perf.json",
  "correction-notice-maplibre-perf",
  "correction_notice"
);

await maybeAdd(
  "artifacts/perf/rollback-plan.maplibre-perf.json",
  "rollback-plan-maplibre-perf",
  "rollback_plan"
);

await maybeAdd(
  "artifacts/perf/failure-bundle.maplibre-perf.json",
  "failure-bundle-maplibre-perf",
  "failure_bundle"
);

const included = [];

for (const artifact of artifacts) {
  const bytes = await fs.readFile(artifact.path);

  included.push({
    ...artifact,
    sha256: sha256(bytes)
  });
}

const receipt = JSON.parse(
  await fs.readFile("artifacts/perf/run-receipt.json", "utf8")
);

const now = new Date().toISOString();

const manifest = {
  object_type: "ReleaseManifest",
  schema_version: "v1",
  release_id: `maplibre-perf-release-${now.replaceAll(":", "-")}`,
  created_utc: now,
  domain: "maplibre",
  status: receipt.status === "completed" ? "candidate" : "rejected",
  policy_posture: receipt.policy_posture ?? "review_required",
  artifacts: included
};

await fs.mkdir("artifacts/perf", { recursive: true });

await fs.writeFile(outPath, JSON.stringify(manifest, null, 2));

console.log("ANSWER: wrote MapLibre perf release manifest");
console.log(`- ${outPath}`);
