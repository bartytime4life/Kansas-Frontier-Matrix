#!/usr/bin/env node

import fs from "node:fs/promises";

const manifestPath =
  "artifacts/perf/release-manifest.maplibre-perf.json";

const correctionPath =
  "artifacts/perf/correction-notice.maplibre-perf.json";

const rollbackPath =
  "artifacts/perf/rollback-plan.maplibre-perf.json";

const manifest = JSON.parse(await fs.readFile(manifestPath, "utf8"));
const now = new Date().toISOString();

const needsCorrection = manifest.status !== "candidate";

if (!needsCorrection) {
  console.log("ANSWER: no correction or rollback needed");
  process.exit(0);
}

const correctionNotice = {
  object_type: "CorrectionNotice",
  schema_version: "v1",
  domain: "maplibre",
  notice_id: `maplibre-perf-correction-${now.replaceAll(":", "-")}`,
  created_utc: now,
  trigger: "perf_or_render_governance_failure",
  status: "draft",
  affected_release_manifest_path: manifestPath,
  reason: `Release manifest status is ${manifest.status}`,
  required_action:
    "Block publication until perf governance returns ANSWER.",
  policy_posture: "review_required"
};

const rollbackPlan = {
  object_type: "RollbackPlan",
  schema_version: "v1",
  domain: "maplibre",
  rollback_id: `maplibre-perf-rollback-${now.replaceAll(":", "-")}`,
  created_utc: now,
  status: "draft",
  affected_release_manifest_path: manifestPath,
  rollback_strategy:
    "Retain prior released renderer/tile artifacts; do not promote failed candidate.",
  verification_command:
    "python3 tools/validators/maplibre/validate_perf_governance.py",
  policy_posture: "review_required"
};

await fs.mkdir("artifacts/perf", { recursive: true });

await fs.writeFile(
  correctionPath,
  JSON.stringify(correctionNotice, null, 2)
);

await fs.writeFile(
  rollbackPath,
  JSON.stringify(rollbackPlan, null, 2)
);

console.log("DENY: correction and rollback artifacts generated");
console.log(`- ${correctionPath}`);
console.log(`- ${rollbackPath}`);
