#!/usr/bin/env node

import crypto from "node:crypto";
import fs from "node:fs/promises";

const receiptPath =
  process.argv[2] ?? "artifacts/perf/run-receipt.json";

const outPath =
  process.argv[3] ?? "artifacts/perf/run-receipt.dsse.json";

function sha256(bytes) {
  return crypto
    .createHash("sha256")
    .update(bytes)
    .digest("hex");
}

function b64(bytes) {
  return Buffer.from(bytes).toString("base64");
}

const receiptBytes = await fs.readFile(receiptPath);
const receipt = JSON.parse(receiptBytes.toString("utf8"));

const payloadType =
  "application/vnd.kfm.maplibre.perf.run-receipt.v1+json";

const envelope = {
  payloadType,
  payload: b64(receiptBytes),
  signatures: [],
  kfm_attestation: {
    object_type: "AttestationEnvelope",
    schema_version: "v1",
    subject_type: "RunReceipt",
    subject_path: receiptPath,
    subject_sha256: `sha256:${sha256(receiptBytes)}`,
    domain: "maplibre",
    policy_posture: receipt.policy_posture ?? "review_required",
    created_utc: new Date().toISOString(),
    signing_status: "unsigned",
    notes: [
      "DSSE-shaped unsigned envelope for CI review.",
      "Cosign signing may be applied in release-capable environments."
    ]
  }
};

await fs.mkdir("artifacts/perf", { recursive: true });

await fs.writeFile(outPath, JSON.stringify(envelope, null, 2));

await fs.writeFile(
  "artifacts/perf/run-receipt.sha256",
  `${sha256(receiptBytes)}  ${receiptPath}\n`
);

console.log("ANSWER: wrote unsigned DSSE-shaped envelope");
console.log(`- ${outPath}`);
console.log("- artifacts/perf/run-receipt.sha256");
