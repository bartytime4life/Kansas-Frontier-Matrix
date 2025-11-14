---
title: "🔑 Kansas Frontier Matrix — Idempotency Key Specification (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/architecture/idempotency/key_spec.md"
version: "v10.3.1"
last_updated: "2025-11-13"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/pipelines-idempotency-key-spec-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🔑 **Kansas Frontier Matrix — Idempotency Key Specification**  
`src/pipelines/architecture/idempotency/key_spec.md`

**Purpose:**  
Define the **canonical idempotency key design** for all Kansas Frontier Matrix (KFM) pipelines.  
These rules ensure every pipeline execution is **replay-safe, duplicate-resistant, deterministic**, and **FAIR+CARE governed**, even in the presence of at-least-once delivery and repeated events.

</div>

---

## 📘 Overview

Idempotency keys in KFM:

- Uniquely identify a **logical pipeline run** for a given dataset + version + source  
- Allow safe re-execution (1× or 10,000×) without changing the final state  
- Are used by:
  - Durable KV stores  
  - Transactional outbox consumers  
  - Observability and governance systems  
  - Replay engines  

This document defines:

- The **key formula**  
- Required input fields  
- Storage requirements  
- Validation rules  
- Telemetry expectations  

---

## 🗂️ Directory Context

~~~~~text
src/pipelines/architecture/idempotency/
├── README.md
├── key_spec.md                 # This file
├── outbox.md
├── state_store.md
├── replay_engine.md
└── examples/
~~~~~

---

## 🧩 Idempotency Key Definition

### Canonical Formula (v10.3.1)

The idempotency key MUST be computed as:

~~~~~text
sha256(dataset_id + "|" + version + "|" + source_uri)
~~~~~

**Requirements:**

- Pure, deterministic function  
- Input strings MUST be normalized (trim, lowercase where appropriate)  
- MUST NOT depend on timestamps, random values, or mutable state  

### Required Components

| Field        | Description                                |
|--------------|--------------------------------------------|
| `dataset_id` | Stable dataset identifier (e.g. STAC/contract ID) |
| `version`    | Semantic version (x.y.z) of pipeline or artifact   |
| `source_uri` | Canonical URI for primary input asset      |

Example inputs:

- `dataset_id = "noaa_storm_events_1950_2025"`  
- `version = "v10.3.1"`  
- `source_uri = "https://www.ncei.noaa.gov/storm-events/file_1950_2025.csv"`  

---

## 🧱 Normalization Rules

Before hashing:

1. **dataset_id**  
   - MUST match the dataset ID used in STAC/DCAT and data contracts.  

2. **version**  
   - MUST be semantic (`v10.3.1`) and stable for a given release.  

3. **source_uri**  
   - MUST be a fully-qualified URL or canonical storage path.  
   - No querystring noise; normalized form only.  

If any field changes → the idempotency key must also change.

---

## 🧬 Key Shape & Storage

### Key Shape

All keys MUST be stored as:

~~~~~text
sha256:<hex-64>
~~~~~

Example:

~~~~~text
sha256:31b1ee2f4dd9030c95f84a78047bcdfd7b8a38ef9c7f0c31bde1dca55ed9012
~~~~~

### Storage Requirements

- Stored in a **durable KV store**:
  - S3, DynamoDB, Firestore, or equivalent  
- Keys MUST be **append-only** (no deletions, no in-place overwrites)  
- Each record MUST track:
  - `idempotency_key`  
  - `dataset_id`  
  - `version`  
  - `artifact_checksum` (if available)  
  - `replay_safe` flag  
  - `timestamp`  

---

## 🧪 Example Key Record

~~~~~json
{
  "dataset_id": "noaa_storm_events_1950_2025",
  "version": "v10.3.1",
  "source_uri": "https://www.ncei.noaa.gov/storm-events/file_1950_2025.csv",
  "idempotency_key": "sha256:31b1ee2f4dd9030c95f84a78047bcdfd7b8a38ef9c7f0c31bde1dca55ed9012",
  "artifact_checksum": "sha256:88bedf22ee...",
  "timestamp": "2025-11-13T17:44:00Z",
  "replay_safe": true
}
~~~~~

---

## ♻️ Integration With Event Envelopes

Every event envelope MUST carry the computed key:

~~~~~json
{
  "event_id": "9b7439e1-2c8a-4d9c-bc66-c9bcdf06e4b2",
  "event_type": "etl",
  "dataset_id": "noaa_storm_events_1950_2025",
  "version": "v10.3.1",
  "source_uri": "https://www.ncei.noaa.gov/storm-events/file_1950_2025.csv",
  "idempotency_key": "sha256:31b1ee2f4dd9030c95f84a78047bcdfd7b8a38ef9c7f0c31bde1dca55ed9012"
}
~~~~~

The **idempotency validator** recomputes the key and:

- Compares against the supplied key  
- Checks the KV store (seen / unseen)  
- Decides whether to:
  - Proceed with execution, or  
  - Treat as a **no-op duplicate**  

---

## ⚖️ Governance & FAIR+CARE Considerations

Idempotency keys MUST respect governance:

- Keys are considered **non-sensitive**, but linked artifacts may be sensitive.  
- Governance ledgers MUST record:
  - Keys used for sensitive or restricted datasets  
  - Whether masking/CARE enforcement was applied under a given key  

Ledger reference (idempotency-related):

~~~~~text
docs/reports/audit/pipeline_idempotency_ledger.json
~~~~~

---

## 📡 Telemetry Requirements

Telemetry for idempotency keys MUST include:

- `idempotency_key`  
- `duplicate_detected` (boolean)  
- `replay_triggered` (boolean)  
- `artifact_checksum`  
- `care_label`  
- `dataset_id`  
- `version`  

Telemetry entries are appended to:

~~~~~text
../../../../../releases/v10.3.0/focus-telemetry.json
~~~~~

---

## 🚫 Anti-Patterns (Forbidden)

- Keys including timestamps or random numbers  
- Keys changing across retries for the same logical work  
- Keys derived from mutable job IDs or message offsets  
- Keys omitting `source_uri` (causes ambiguity for multi-source datasets)  
- Deleting/rewriting keys in the KV store  

Any anti-pattern detected must be corrected before pipeline can be certified.

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|--------|--------|---------|
| v10.3.1 | 2025-11-13 | Pipeline Architecture Team | Established canonical idempotency key formula, normalization rules, and telemetry bindings for KFM v10.3. |

---

<div align="center">

**Kansas Frontier Matrix — Idempotency Key Specification**  
Deterministic Keys × Zero Duplication × Immutable Governance  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  

[Back to Idempotency Architecture](../README.md)

</div>
