#!/usr/bin/env node

import crypto from "node:crypto";
import fs from "node:fs/promises";

const manifestPath =
  "artifacts/perf/release-manifest.maplibre-perf.json";
const receiptPath =
  "artifacts/perf/run-receipt.json";
const envelopePath =
  "configs/maplibre/perf-envelope.v1.json";
const outPath =
  "artifacts/perf/proof-pack.maplibre-perf.json";

function sha256(bytes) {
  return (
    "sha256:" +
    crypto.createHash("sha256").update(bytes).digest("hex")
  );
}

async function sha256File(path) {
  return sha256(await fs.readFile(path));
}

const manifest = JSON.parse(await fs.readFile(manifestPath, "utf8"));
const now = new Date().toISOString();

const proofPack = {
  object_type: "ProofPack",
  schema_version: "v1",
  domain: "maplibre",
  proof_id: `maplibre-perf-proof-${now.replaceAll(":", "-")}`,
  created_utc: now,
  release_manifest_path: manifestPath,
  run_receipt_path: receiptPath,
  perf_envelope_path: envelopePath,
  validation_command:
    "python3 tools/validators/maplibre/validate_perf_governance.py",
  validation_outcome: "ANSWER",
  artifact_count: manifest.artifacts.length,
  release_manifest_sha256: await sha256File(manifestPath),
  run_receipt_sha256: await sha256File(receiptPath),
  perf_envelope_sha256: await sha256File(envelopePath)
};

await fs.mkdir("artifacts/perf", { recursive: true });

await fs.writeFile(outPath, JSON.stringify(proofPack, null, 2));

console.log("ANSWER: wrote MapLibre perf ProofPack");
console.log(`- ${outPath}`);
