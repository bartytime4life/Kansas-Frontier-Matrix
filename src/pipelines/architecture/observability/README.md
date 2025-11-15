---
title: "🛠️ Kansas Frontier Matrix — Unified Reliable Pipeline Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/architecture/reliable-pipelines.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "releases/v10.4.0/sbom.spdx.json"
manifest_ref: "releases/v10.4.0/manifest.zip"
telemetry_ref: "releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/pipelines-reliable-updaters-v1.json"
governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🛠️ **Kansas Frontier Matrix — Unified Reliable Pipeline Architecture**  
`src/pipelines/architecture/reliable-pipelines.md`

**Purpose:**  
Define the **reliability, idempotency, rollback/resume, and blue/green deployment architecture** required for all pipelines and updaters in the Kansas Frontier Matrix (KFM).  
Ensures pipelines are **deterministic, exactly-once at the boundary, debuggable, and fast to roll back** without rewriting history.

</div>

---

## 📘 Overview

Reliable pipelines in KFM follow a **single, enforced pattern**:

1. **Trigger** — cron, event, or manual with a documented envelope  
2. **Light AI (optional)** — schema and mapping hints only, frozen to config  
3. **Deterministic ETL** — pure, stateless transforms with pinned versions  
4. **Validation & QA Gates** — schema, spatial, temporal, domain, drift  
5. **Idempotent Upsert** — natural keys + content hashes, transactional outbox  
6. **Metadata & Versioning** — STAC/DCAT, provenance, semantic versions  
7. **Blue/Green Publish** — immutable artifacts, pointer flips, health checks  
8. **Alerts & Telemetry** — logs, metrics, traces, FAIR+CARE telemetry events  
9. **Rollback & Resume** — pointer-based rollback, checkpoint-based resume  

All patterns MUST comply with:

- **MCP-DL v6.3**  
- **Markdown Rules v10.4**  
- **FAIR+CARE governance**  

---

## 🗂️ Directory Layout

~~~~~text
src/pipelines/architecture/
├── reliable-pipelines.md         # This file
src/pipelines/
├── etl/
│   ├── batch/                    # Batch ETL jobs (files, APIs, backfills)
│   └── streaming/                # Streaming ETL (Kafka, websockets, events)
└── common/
    ├── idempotency/              # Idempotency keys, hashes, outbox utilities
    ├── validation/               # GX / JSONSchema / STAC validation helpers
    ├── observability/            # Logging, metrics, tracing helpers
    ├── versioning/               # Artifact versions, blue/green pointers
    └── governance/               # FAIR+CARE and provenance hooks

data/
├── sources/                      # Source descriptors (contracts)
├── raw/                          # Raw ingested data
├── work/                         # Staging for validation / drift checks
└── processed/
    ├── blue/                     # Currently serving versions
    └── green/                    # Candidate versions
~~~~~

---

## 🧩 Reliable Pipeline Architecture (Indented Mermaid)

~~~~~mermaid
flowchart TD
  T["Trigger<br/>cron · event · manual"] --> AI["Light AI (Optional)<br/>schema · mapping hints"]
  AI --> ETL["Deterministic ETL<br/>pure transforms"]
  ETL --> VAL["Validation & QA Gates<br/>schema · spatial · temporal · drift"]
  VAL -->|pass| UPS["Idempotent Upsert<br/>natural key · content hash · outbox"]
  VAL -->|fail| OBS["Stop · Alert · DLQ"]
  UPS --> META["Metadata & Versioning<br/>STAC · DCAT · provenance"]
  META --> BG["Blue/Green Publish<br/>green → blue pointer flip"]
  BG --> TEL["Alerts & Telemetry<br/>logs · metrics · traces"]
~~~~~

---

## 🧱 1. Triggers & Envelopes

Every run MUST start with a **trigger envelope** capturing intent and idempotency:

### Trigger Types

- **Time-based:** nightly/hourly refreshes, scheduled backfills  
- **Event-based:** webhooks, file drops, STAC updates, message bus events  
- **Manual:** governance-approved replays or hotfixes  

### Envelope Example

~~~~~json
{
  "trigger_id": "cron-2025-11-15T00:00Z-kgs-wells",
  "trigger_kind": "cron",
  "dataset_id": "kgs_wells",
  "source_uri": "https://example.org/kgs/wells",
  "requested_range": {
    "start": "1900-01-01",
    "end": "2025-11-01"
  },
  "idempotency_key": "sha256(dataset_id|requested_range|source_uri)"
}
~~~~~

The `idempotency_key` is used to ensure **we do not re-run the same envelope twice** once it has succeeded.

---

## 🎯 2. Idempotency Requirements

### Trigger-Level Idempotency Key

~~~~~text
sha256(dataset_id + "|" + version_or_range + "|" + source_uri)
~~~~~

### Record-Level Natural Key & Hash

- **Natural key:** minimal stable identity for each record (e.g. `(station_id, date)`).
- **Content hash:** hash of **normalized record without runtime fields** (no timestamps, no ephemeral IDs).

~~~~~text
content_hash = sha256(normalized_record_without_runtime_fields)
~~~~~

### Transactional Outbox

Any pipeline that writes to the graph and also:

- Sends events to Kafka / queues  
- Writes to STAC / DCAT endpoints  
- Triggers downstream services  

MUST use a **transactional outbox** to ensure:

- Internal DB writes and outbox entries are committed in a **single transaction**.  
- A separate worker delivers outbox messages with retries and backoff.  

---

## 🧪 3. Validation & QA Gates

No data is promoted to `data/processed/` or Neo4j until it passes **all required gates**.

### Validation Matrix

| Gate     | Check Type                             | Tooling                          | Action      |
|----------|----------------------------------------|----------------------------------|------------|
| Schema   | JSON Schema / Pydantic / STAC          | GX, `jsonschema`, STAC validator | Fail        |
| Spatial  | CRS validity, geometry sanity          | GDAL/OGR, Shapely                | Fail        |
| Temporal | Range, monotonicity                    | Custom checks                    | Warn/Fail   |
| Domain   | Enums, ranges, controlled vocabularies | Lookup tables, GX                | Fail        |
| Drift    | Statistical differences vs last good   | Custom metrics                   | Warn/Review |

On **any failure**:

- Outputs remain in `data/work/**` only.  
- `qa_gate_failed` events are emitted.  
- Pipelines MUST NOT publish or update pointers.

---

## 🧱 4. Versioning & Blue/Green Pipeline

### Immutable Artifacts

All artifacts generated by a run MUST be **immutable** and versioned, e.g.:

~~~~~text
s3://kfm/artifacts/{dataset}/{version}/...
data/processed-green/{dataset}/...
data/processed-blue/{dataset}/...
~~~~~

### Promotion Sequence

1. Write candidate dataset to `processed-green/**`.  
2. Run post-publish health checks (can the UI/API query the candidate successfully?).  
3. Flip pointer to `processed-blue/**` atomically.  
4. Emit `publish_promoted` telemetry and update metadata (STAC/DCAT).

Blue/green patterns guarantee that **rollback is a pointer flip**, not a destructive rewrite.

---

## 📡 5. Observability & Telemetry

Pipelines MUST integrate with the observability architecture defined in:

- `src/pipelines/architecture/observability/README.md`

### Required Log Fields

- `dataset_id`  
- `run_id`  
- `trigger_id`  
- `stage` (`extract`, `transform`, `validate`, `load`, `publish`)  
- `status`  
- `idempotency_key`  
- `duration_ms`  
- `error_class`, `error_message` (if any)  

### Example Telemetry Events

~~~~~json
{"event":"stage_started","stage":"etl","run_id":"2025-11-15-abc","dataset":"kgs_wells"}
{"event":"qa_gate_failed","gate":"schema","errors":3,"run_id":"2025-11-15-abc","dataset":"kgs_wells"}
{"event":"upsert_summary","inserted":1240,"updated":311,"skipped":9123,"run_id":"2025-11-15-abc","dataset":"kgs_wells"}
{"event":"publish_promoted","from":"green","to":"blue","version":"v10.4.2","run_id":"2025-11-15-abc","dataset":"kgs_wells"}
~~~~~

Metrics, traces, and telemetry output locations are defined in the observability spec; pipelines must comply.

---

## 🔁 6. Retries, Backoff & DLQ

### Retry Policy

- Maximum attempts: **5**  
- Strategy: **exponential backoff with jitter**  
- Only applied to **I/O operations** (remote APIs, storage, DB connections)  
- All retries MUST honor:
  - Timeouts  
  - Circuit breakers  

### DLQ (Dead Letter Queue)

Any work item that exceeds retry limits MUST:

- Be written to a DLQ with:
  - Payload  
  - Error class and message  
  - Stack trace (if available)  
  - `first_seen_at`, `last_seen_at`, and `retry_count`  
- Trigger an alert route (SRE, governance, or data engineering).

---

## 🧯 7. Rollback & Resume

### Rollback

Rollback is always:

- **Pointer-based** (blue/green), not a destructive deletion.  
- Documented in governance ledger (who, why, when).  

Rules:

- Never mutate or delete previously published artifacts in place.  
- Use the previous `blue` version as the rollback target.  
- For graph data, use snapshots or replay from last known-good artifacts.

### Resume

Resume MUST use **checkpoints**:

- Cursor types:
  - Date/time range
  - Page/token
  - Offset/sequence ID  
- Checkpoints persisted in durable storage.  
- Resume logic must rely on:
  - Idempotent reads  
  - Idempotent upserts  
  - Idempotent side-effects (outbox pattern)  

This ensures safe re-runs without duplication or data loss.

---

## 📜 8. Data-Level Requirements

Any dataset managed by a reliable pipeline MUST have:

- A `data/sources/<dataset>.json` descriptor with:
  - Source endpoints and schemas  
  - Temporal and spatial coverage  
  - License and CARE tags  
  - Expected outputs (tables, COGs, STAC collections, graph updates)  

Directory expectations:

~~~~~text
data/
  sources/<dataset>.json
  raw/<dataset>/...
  work/<dataset>/...
  processed/
    blue/<dataset>/...
    green/<dataset>/...
  stac/
    collections/...
    items/...
~~~~~

---

## 🧮 9. Idempotent Upsert Pseudocode

~~~~~python
def upsert(records, store, run_id):
    for r in records:
        nk = natural_key(r)
        h = content_hash(normalize(r))
        prev = store.get_meta(nk)

        if prev and prev.hash == h:
            mark_skipped(nk, run_id)
            continue

        store.transactional_upsert(
            natural_key=nk,
            record=r,
            hash=h,
            prev_hash=prev.hash if prev else None,
            run_id=run_id,
        )
~~~~~

This pattern MUST be applied to all updaters: graph upserts, tabular sinks, and external-facing indices.

---

## 🧑‍🏭 10. Operator Runbook

Operators MUST follow these steps:

1. **Trigger**  
   - Confirm correct dataset + mode (cron/event/manual).  
   - For manual runs, document justification in governance ledger.  
2. **Monitor**  
   - Watch logs for `stage_started`, `qa_gate_failed`, `stage_failed`.  
   - Check dashboards for retries, DLQ entries, and performance anomalies.  
3. **On Validation Failure**  
   - Inspect gate reports and sample failing records.  
   - Fix schema, transform, or contracts.  
   - Perform a small **dry-run** on a subset.  
   - Re-run full pipeline once verified.  
4. **On Publish Issues**  
   - If candidate green data is unhealthy:
     - Flip pointer back to previous blue.  
     - Open an incident with `run_id`, scope, and impact.  
   - Fix underlying cause, then re-run.  
5. **Resume**  
   - Use checkpoints; do not restart from scratch unless necessary.  
   - Confirm idempotency guarantees before resume.  
6. **Close Out**  
   - Confirm telemetry and governance entries are written.  
   - Update release notes if pointer flips or schema changes occurred.  

---

## 🕰️ Version History

| Version | Date       | Author / Team              | Summary                                                                        |
|--------:|------------|----------------------------|--------------------------------------------------------------------------------|
| v10.4.0 | 2025-11-15 | Pipeline Architecture Team | Unified reliable pipeline architecture; aligned with observability spec format. |
| v10.3.1 | 2025-11-13 | Pipeline Architecture Team | Previous “Reliable Pipeline Architecture Guide”.                               |
| v1.0.0  | 2025-11-15 | ETL/Updaters Working Group | Initial “Reliable Updaters” pattern.                                           |
