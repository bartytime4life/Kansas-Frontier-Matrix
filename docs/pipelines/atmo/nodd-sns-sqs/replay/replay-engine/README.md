---
title: "♻️ KFM v11.2.3 — NODD Replay Engine (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Deterministic WAL-driven replay engine for the NOAA NODD SNS → SQS ingestion pipeline, providing governed tools to reprocess failed or scoped ingest units safely."
path: "docs/pipelines/atmo/nodd-sns-sqs/replay/replay-engine/README.md"

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

signature_ref: "../../../../../../releases/v11.2.3/signature.sig"
attestation_ref: "../../../../../../releases/v11.2.3/slsa-attestation.json"
sbom_ref: "../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.3/nodd-sns-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/nodd-sns-sqs-v1.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Replay Engine Specification"
intent: "nodd-sns-sqs-replay-engine-readme"
category: "Pipelines · Atmospheric · Replay · Engine"

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
sunset_policy: "Superseded by next major NODD replay engine standard"

header_profile: "standard"
footer_profile: "standard"
---

# ♻️ NODD Replay Engine  

`docs/pipelines/atmo/nodd-sns-sqs/replay/replay-engine/README.md`

Deterministic **WAL-driven replay engine** for the NOAA NODD SNS → SQS ingestion pipeline.

The replay engine provides:

- A governed mechanism to **reprocess failed ingest units**.  
- **Scoped, WAL-centric selection** for incident and DLQ replays.  
- **Idempotent orchestration** that reuses the same operators as the hot path.  
- Tight integration with **runbooks, telemetry, and governance gates**.

It is the only approved way to perform bulk or targeted replays for NODD ingestion.

⸻

## 🗂 1. Directory Layout (Replay Engine)

~~~text
docs/pipelines/atmo/nodd-sns-sqs/replay/replay-engine/
│
├── 📄 README.md                  # This file — replay engine contract & behavior
│
├── 📄 cli-spec.md                # CLI/API interface, flags, and usage patterns
├── 📄 selection-spec.md          # Query model for selecting WAL records to replay
├── 📄 safety-guards.md           # Limits, backpressure controls, and guardrails
└── 📄 integration-notes.md       # Integration with schedulers, CI, and runbooks
~~~

Related replay documentation:

- WAL core spec: `../wal/README.md`  
- WAL record model: `../wal/wal-record-model.md`  
- WAL state machine: `../wal/wal-state-machine.md`  
- Runbooks: `../runbooks/README.md`  

⸻

## 🧭 2. Purpose & Scope

The NODD replay engine exists to:

- Provide a **single, governed mechanism** for all NODD replays.  
- Ensure that every replay:
  - Uses **WAL as the source of truth**, not ad hoc SQS manipulation.  
  - Respects the **WAL state machine** and record model.  
  - Remains **deterministic and idempotent** with respect to STAC and provenance.  
- Integrate seamlessly with:
  - DLQ drains  
  - Incident replays  
  - Backfills and targeted window reprocessing  

Out of scope:

- Ad hoc scripts that bypass WAL.  
- Direct SQS → worker injections without WAL record correlation.  
- Replays that attempt to alter WAL semantics or bypass governance.

⸻

## 🧱 3. High-Level Architecture

The replay engine sits alongside the hot-path ingestion workers and interacts with:

- **WAL backend**  
- **SQS queues** (primary and DLQ)  
- **STAC and provenance operators**  
- **Telemetry & alerts**

Conceptual flow:

1. **Selection**  
   - Query WAL for records eligible for replay, based on:
     - `dataset`  
     - Time window  
     - `status` (`failed`, optionally `succeeded` for repair-and-replace)  
     - `last_error_code`  
     - `attempts` count and replay limits  

2. **Preparation**  
   - Validate selection against:
     - Safety guards and batch limits  
     - Runbook-defined scopes (DLQ drain, incident replay, etc.).  
   - Transition selected records:
     - `status: "failed" → "pending"`  
     - Set `replay_reason` (for example, `"dlq-drain"`, `"incident"`, `"backfill"`)

3. **Re-enqueue / Execution**  
   - Reconstruct ingestion work from WAL fields (equivalent to original SNS/SQS messages).  
   - Feed work into:
     - Standard ingestion workers, or  
     - A dedicated replay worker pool that uses the same operators.

4. **Completion & Telemetry**  
   - As ingest completes:
     - WAL records update to terminal statuses (`succeeded` / `quarantined`).  
     - Telemetry increments replay and mismatch metrics.  
   - Alerts and dashboards show replay progress and outcomes.

⸻

## 🔍 4. Core Contracts

The replay engine MUST honor the following core contracts:

- **WAL-first**  
  - No replay occurs without a corresponding WAL record.  
  - WAL is the **canonical selector** and state holder for all replays.

- **State-machine compliance**  
  - Legal transitions only, as defined in `wal-state-machine.md`.  
  - For failed-only replays:
    - `status = "failed" → "pending" → "in_progress" → "succeeded"/"failed"/"quarantined"`  

- **Idempotent behavior**  
  - Replaying a WAL record:
    - MUST NOT create duplicate STAC Items or duplicated provenance edges.  
    - MUST be safe to re-run if a replay job is itself retried.

- **Governed selection**  
  - Selection logic MUST be expressible as:
    - Dataset filters  
    - Time windows  
    - Error-code filters  
    - Status and attempts filters  
  - Ad hoc “select everything” replays in prod are forbidden without Council approval.

- **Runbook alignment**  
  - For high-level flows (DLQ drains, delayed queues, incident replays, validation error remediation), the replay engine MUST be used according to the corresponding runbooks in `../runbooks/`.

⸻

## 🔁 5. Replay Modes

The engine supports three governed replay modes; implementations MUST treat them explicitly.

### 5.1 Failed-Only Replay (Default)

- Scope:
  - WAL records with `status = "failed"` and:
    - `attempts < max_attempts`, and  
    - `last_error_code` in a replayable set (e.g., errors now fixed).  
- Usage:
  - DLQ drain operations.  
  - Transient error remediation after infra fixes.  
- Behavior:
  - `failed → pending` with `replay_reason = "dlq-drain"` or `"incident"`.

### 5.2 Repair-and-Replace Replay (Advanced)

- Scope:
  - WAL records with `status = "succeeded"` where outputs are known to be incorrect.  
- Usage:
  - Post-incident corrections after buggy deploys.  
- Requirements:
  - Additional logic to:
    - Safely update or replace existing STAC Items and provenance.  
  - Additional governance approval for `prod`.

### 5.3 Backfill / Fill-Missing Replay

- Scope:
  - Logical “replay” of historical windows that may include:
    - Missing WAL records (fresh ingest).  
    - Existing failed records (standard replay).  
- Usage:
  - Managed via incident or backfill pipelines, but MUST still:
    - Populate or use WAL records.  
    - Obey the same engine and WAL semantics.

⸻

## 🧮 6. Selection Model (Summary)

Detailed selection model is in `selection-spec.md`. At a minimum, the replay engine MUST support selecting WAL records by:

- `dataset` (single or list)  
- `status` (at least `failed`, optionally `succeeded` for advanced modes)  
- `last_error_code` (one or more error classes)  
- Time filters:
  - `event_time` range  
  - `time_range_start` / `time_range_end` overlap  
  - `created_at` range  
- Attempt limit:
  - `attempts < max_attempts`  
- Optional additional constraints:
  - `replay_reason` (for filtering previous replay attempts)  
  - Custom governed tags (if defined in WAL extensions)

The engine MUST:

- Represent selections declaratively (e.g., as JSON or YAML selection specs).  
- Surface these specs in logs and incident records for provenance and reproducibility.

⸻

## 🛡 7. Safety & Guardrails

Safety mechanisms are further detailed in `safety-guards.md`. Key requirements:

- **Batch size limits**  
  - Each replay batch MUST have:
    - Max record count.  
    - Max estimated data volume.  

- **Rate limiting**  
  - Replay throughput MUST be bounded so it does not:
    - Overwhelm workers.  
    - Violate queue-age or latency SLOs.

- **Kill-switch integration**  
  - Respect environment- and dataset-level kill-switch flags:
    - If a dataset is paused, replay engine MUST NOT initiate new work for it.

- **Max attempts enforcement**  
  - Honor `max_attempts` per WAL record to avoid infinite retry loops.

- **Dry-run capabilities**  
  - Provide a non-mutating mode that:
    - Lists candidate WAL records.  
    - Estimates replay impact.  
    - Produces a selection report for review.

- **Audit trails**  
  - Every replay invocation MUST be traceable to:
    - Who/what initiated it.  
    - Which selection spec was used.  
    - Which WAL records were touched.

⸻

## 📡 8. Telemetry & Metrics

The replay engine MUST emit telemetry compatible with `telemetry_schema`:

Key metrics (incremented or updated as appropriate):

- `nodd_sns.replays_total{dataset,env,replay_reason}`  
- `nodd_sns.replay_batches_total{env,replay_reason}`  
- `nodd_sns.replay_batch_size{env}` (distribution)  
- `nodd_sns.replay_mismatch_total{dataset,env}`  
- `nodd_sns.wal_records_total{status,env}` (with transitions visible during replays)

Spans:

- Each replay batch SHOULD have a top-level span that includes:
  - Selection spec hash or ID.  
  - Number of WAL records in the batch.  
  - Replay mode (`failed-only`, `repair-and-replace`, `backfill`).  

Logging:

- Replay actions MUST log in structured form:
  - Selection spec.  
  - Batch identifiers.  
  - Aggregated outcomes (succeeded/failed/quarantined counts).

⸻

## 🧪 9. Testing & CI Requirements

CI MUST validate replay engine behavior along these axes:

- **Selection correctness**  
  - Unit tests with synthetic WAL records verifying that:
    - Selection filters pick the correct subset.  
    - Boundary conditions (time ranges, attempt limits) are correct.

- **State machine compliance**  
  - Tests that:
    - Legal transitions succeed.  
    - Illegal transitions (e.g., `succeeded → pending` without special mode) are rejected.

- **Idempotency**  
  - Replaying the same selection twice:
    - Does not duplicate STAC Items or provenance edges.  
    - Leaves WAL in a consistent terminal state.

- **Guardrail enforcement**  
  - Tests that:
    - Batch size and rate limits are respected.  
    - Kill-switch flags are honored.  
    - `max_attempts` is enforced.

- **Dry-run vs live-run**  
  - Dry-run produces:
    - Correct statistics and sample records.  
  - Live-run:
    - Modifies WAL and queues exactly as predicted.

Any functional change to replay behavior MUST:

- Update this file and related specs (`cli-spec.md`, `selection-spec.md`, `safety-guards.md`).  
- Update CI tests to reflect new intended behavior.

⸻

## 📘 10. Version History

| Version  | Date       | Notes                                                                                                            |
|---------:|------------|------------------------------------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-04 | Initial NODD replay engine spec; defined architecture, replay modes, selection model, guardrails, and CI rules. |

---

<div align="center">

♻️ NODD Replay Engine · KFM v11.2.3  

WAL-First · Deterministic · Governance-Enforced  

MCP-DL v6.3 · KFM-MDP v11.2.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to Replay Overview](../README.md) ·  
[📓 WAL Spec](../wal/README.md) ·  
[🧰 Runbooks](../runbooks/README.md) ·  
[📊 Telemetry Dashboards](../../telemetry/dashboards/README.md) ·  
[⚖ Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
