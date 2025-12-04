---
title: "🔁 KFM v11.2.3 — NOAA NODD SNS → SQS Replay & WAL Specification (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Deterministic WAL, DLQ draining, and replay semantics for the NOAA NODD SNS → SQS ingestion pipeline in KFM."
path: "docs/pipelines/atmo/nodd-sns-sqs/replay/README.md"

version: "v11.2.3"
last_updated: "2025-12-04"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Atmospheric Systems · Provenance & Reliability Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x replay-contract compatible"
status: "Active · Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../../../releases/v11.2.3/signature.sig"
attestation_ref: "../../../../../releases/v11.2.3/slsa-attestation.json"
sbom_ref: "../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.3/nodd-sns-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/nodd-sns-sqs-v1.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Replay Specification"
intent: "nodd-sns-sqs-replay-spec"
category: "Pipelines · Atmospheric · Replay · WAL"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
classification: "Public"
jurisdiction: "Kansas / United States"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
immutability_status: "version-pinned"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

ttl_policy: "24 Months"
sunset_policy: "Superseded by next major NODD replay standard"

header_profile: "standard"
footer_profile: "standard"
---

<div align="center">

# 🔁 NOAA NODD SNS → SQS Replay & WAL Specification  

`docs/pipelines/atmo/nodd-sns-sqs/replay/README.md`

**Deterministic WAL, DLQ draining, and replay semantics for the NOAA NODD SNS → SQS ingestion pipeline, ensuring safe reprocessing without duplication or data drift.**

<img src="https://img.shields.io/badge/Docs-MCP--DL_v6.3-blue" />
<img src="https://img.shields.io/badge/Markdown-KFM--MDP_v11.2.3-purple" />
<img src="https://img.shields.io/badge/Pipeline-NODD_SNS_%E2%86%92_SQS-skyblue" />
<img src="https://img.shields.io/badge/Reliability-WAL_replay-green" />
<img src="https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen" />

</div>

---

## 🧭 1. Purpose

This document specifies the **Write-Ahead Log (WAL)**, **replay**, and **DLQ draining** behavior for the NOAA NODD SNS → SQS ingestion pipeline.

Goals:

- Enable **safe reprocessing** of NODD events (bug fixes, backfills, infra incidents) without double-writing STAC Items or corrupting provenance.  
- Guarantee **replay determinism**: for a fixed code + config version, WAL replays produce **identical STAC and PROV-O outputs**.  
- Provide clear **runbooks** for draining DLQs and performing partial or full replays under governance.

This spec is binding for pipeline implementation, CI tests, and operational runbooks.

---

## 🧱 2. Directory Layout (Emoji-Prefix Standard)

Replay documentation and references live under:

    docs/pipelines/atmo/nodd-sns-sqs/replay/
    │
    ├── 📄 README.md                          # This file (WAL & replay spec)
    │
    ├── 📁 wal/                               # WAL formats and invariants (documentation)
    │   ├── 📄 wal-record-spec.md             # Shape and semantics of WAL entries
    │   └── 📄 wal-storage-layout.md          # Logical/physical layout and retention rules
    │
    ├── 📁 replay-engine/                     # Replay logic and CLI interfaces
    │   ├── 📄 replay-engine.md               # High-level replay design
    │   └── 📄 replay-cli-usage.md            # CLI/API usage examples for replays
    │
    └── 📁 runbooks/                          # Human-facing operational runbooks
        ├── 📄 dlq-drain-runbook.md           # DLQ draining, quarantine, and re-injection
        └── 📄 incident-replay-runbook.md     # Replay for incidents, backfills, and bug fixes

Implementation-specific scripts (e.g. `replay_nodd.py`) live in the code tree but MUST conform to the contracts described here.

---

## 📜 3. WAL Record Model

Each ingest attempt that **may mutate state** MUST be preceded by a WAL record.

Conceptual WAL record fields:

- `wal_id`  
  - Stable, unique identifier (UUID or deterministic hash).

- `event_metadata`  
  - Dataset ID, provider, SNS message ID, SQS message ID.

- `object_ref`  
  - URI, bucket provider (AWS/Azure/GCP), etag/hash.

- `intent`  
  - Operation type: `ingest`, `reingest`, `repair`, `backfill`.

- `code_version`  
  - Git SHA or equivalent for the ingestion code.

- `config_version`  
  - Hash or ID of configuration used (e.g., YAML version).

- `timestamp_created`  
  - WAL record creation time (UTC).

- `status`  
  - `pending`, `applied`, `failed`, `rolled_back`.

**Invariants:**

- No STAC or provenance writes may occur **before** a `pending` WAL record exists.  
- `status` transitions:
  - `pending` → `applied` (successful ingest).  
  - `pending` → `failed` (hard failure; may later go to `rolled_back` or replayed).  
  - `applied` entries are immutable except for append-only annotations.

---

## 🔁 4. Replay Semantics

### 4.1 Determinism Requirements

For a given `(event_metadata, object_ref, code_version, config_version)`:

- A **normal ingest** and a **WAL-driven replay** must produce:
  - Identical STAC Items (byte-for-byte or schema-equivalent).  
  - Identical PROV-O lineage (IDs may be stable or deterministically derived).  
  - Equivalent telemetry (within sampling and temporal constraints).

If this is not achievable (e.g., due to external non-determinism), the pipeline must:

- Explicitly document non-deterministic aspects.  
- Tag those fields in provenance as such.  
- Minimize and isolate non-deterministic behavior.

### 4.2 Replay Types

Supported replay modes:

- **Single-event replay**  
  - Reprocess one WAL entry (identified by `wal_id` or message IDs).

- **Range replay**  
  - Reprocess a time range or WAL ID range for a given dataset or bucket prefix.

- **DLQ replay**  
  - Reprocess messages recovered from DLQ after remediation.

Each replay run MUST:

- Record its own `replay_run_id`.  
- Annotate affected WAL entries and provenance with that `replay_run_id`.  
- Emit telemetry for replay counts and replay mismatches.

---

## 🧪 5. DLQ Draining Model

DLQ handling is governed by **runbooks**, not ad hoc scripts.

High-level DLQ drain steps (documented fully in `runbooks/dlq-drain-runbook.md`):

1. **Classify DLQ messages** by error cause (e.g., schema, connectivity, governance, infra).  
2. **Remediate root cause** (code fix, schema update, configuration, or governance rule change).  
3. **Select DLQ subset** to replay (by time window, dataset, error cause).  
4. **Re-inject** selected messages:
   - Either:
     - Back into primary queue (if safe), or  
     - Into a **quarantine replay queue** tied to a specific `replay_run_id`.  
5. **Monitor replays**:
   - Ensure no duplicate STAC Items or lineage regression.  
   - Check replay telemetry for mismatches.

**Rule:** No DLQ draining may occur without a documented replay plan and reference to an incident or change record.

---

## ⚙️ 6. Replay Engine Behavior

The **replay engine** (documented in `replay-engine/replay-engine.md`) is responsible for:

- Resolving WAL entries or DLQ messages into replay operations.  
- Applying **the same validation, governance, and STAC-write gates** as normal ingestion.  
- Ensuring replay runs do **not** skip validation or governance.  
- Providing a CLI or API with, at minimum:

Conceptual CLI flags:

- `--dataset`  
- `--since` / `--until` (time range).  
- `--wal-id` or `--wal-id-range`.  
- `--replay-run-id` (generated or supplied).  
- `--dry-run` (plan-only, no writes).  
- `--max-events` (safety guard).

Dry-run mode MUST:

- Enumerate candidate WAL entries and actions.  
- Provide “would-do” summaries without modifying any state.

---

## 🧾 7. State & Idempotency Guarantees

Replay reuses the **same idempotency mechanisms** as hot-path ingestion:

- Idempotency keys derived from `(dataset, object_ref, content_hash)` or equivalent.  
- STAC writers that:
  - Compare existing Items before overwriting.  
  - Short-circuit when no effective change is required.

Additional replay guards:

- If an identical `code_version` and `config_version` have already successfully applied to the same WAL entry:
  - The replay engine SHOULD treat the operation as a **no-op** and record a replay hit.  
- Replays that would **downgrade** version or regress schema MUST be blocked unless an explicit override is configured and governance approves.

---

## 📊 8. Telemetry for Replays

Replay-specific telemetry (in addition to base pipeline telemetry):

Required metrics:

- `nodd_sns.replays_total`  
  - Count of replayed WAL entries (labels: `dataset`, `env`, `reason`).

- `nodd_sns.replay_mismatch_total`  
  - Count of replay runs that produced outputs differing from prior ingests.

- `nodd_sns.dlq_reprocessed_total`  
  - DLQ messages successfully reprocessed.

Required span attributes:

- `nodd.replay_run_id`  
- `nodd.replay_mode` (`single`, `range`, `dlq`)  
- `nodd.wal_id`  
- `nodd.replay_original_run` (link to original ingest run ID, if available)

All replay operations must be easily filterable in dashboards and logs using these attributes.

---

## ⚖️ 9. Governance & FAIR+CARE Considerations

Replays interact closely with governance:

- **Sensitive datasets** (e.g., containing sovereign, confidential, or embargoed information) may require:
  - Additional approval before replay.  
  - Restricted replay modes (e.g., no bulk replays without sign-off).

- Governance rules may evolve:
  - Replays may be used to **retrofit** stronger governance to historical ingests (e.g., newly required generalization or redaction).  
  - Such governance-driven replays must:
    - Be clearly documented.  
    - Annotate affected STAC Items and provenance with updated policy references.

Replays must not be used to **erase or hide** provenance; instead, they create **new provenance** linked to the existing history.

---

## 🕰 10. Version History

| Version  | Date       | Notes                                                                                           |
|---------:|------------|-------------------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-04 | Initial NOAA NODD SNS → SQS WAL & replay spec; DLQ drain model, determinism invariants, SLOs.  |

---

<div align="center">

### 🔁 NOAA NODD SNS → SQS Replay & WAL · KFM v11.2.3

Deterministic · WAL-Backed · Provenance-Safe  

MCP-DL v6.3 · KFM-MDP v11.2.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to NODD Pipeline](../README.md) ·  
[📊 Telemetry & SLOs](../telemetry/README.md) ·  
[⚖ Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>