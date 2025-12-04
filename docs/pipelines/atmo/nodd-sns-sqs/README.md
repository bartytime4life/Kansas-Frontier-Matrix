---
title: "🌩️ KFM v11.2.3 — NOAA NODD SNS → SQS Event-Driven Ingestion Pipeline (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Real-time, deterministic, SNS-triggered ingestion of NOAA Open Data Dissemination (NODD) datasets into KFM’s governed ETL spine with WAL-safe replay, STAC integration, and provenance guarantees."
path: "docs/pipelines/atmo/nodd-sns-sqs/README.md"
version: "v11.2.3"
last_updated: "2025-12-04"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Atmospheric Systems · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x ingestion-contract compatible"
status: "Active · Enforced"

commit_sha: ""
previous_version_hash: ""
doc_integrity_checksum: ""

sbom_ref: "../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.3/nodd-sns-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/nodd-sns-sqs-v1.json"
governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Pipeline Specification"
intent: "noaa-nodd-sns-sqs-pipeline"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
sensitivity: "General"
sensitivity_level: "Low"
indigenous_data_flag: false
public_benefit_level: "High"
risk_category: "Low"
redaction_required: false

ontology_alignment:
  schema_org: "DataFeed"
  cidoc: "E29 Design or Procedure"
  prov_o: "prov:Plan"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../schemas/json/pipelines-atmo-nodd-sns-sqs-readme-v1.json"
shape_schema_ref: "../../../../schemas/shacl/pipelines-atmo-nodd-sns-sqs-readme-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "24 Months"
sunset_policy: "Superseded on next major NOAA NODD SNS→SQS standard revision"

header_profile: "standard"
footer_profile: "standard"
---

<div align="center">

# 🌩️ KFM v11.2.3 — NOAA NODD SNS → SQS Event-Driven Ingestion Pipeline  
`docs/pipelines/atmo/nodd-sns-sqs/README.md`

**Purpose:**  
Define the governed, deterministic SNS→SQS ingestion pipeline for NOAA Open Data Dissemination (NODD) datasets (GOES, NEXRAD, model products, etc.) into the KFM ETL spine, with WAL-safe replay, STAC integration, and full provenance.

[Status · Active / Enforced] · [Scope · Atmospheric Systems · Event-Driven ETL] · [Reliability · WAL-Aligned · Idempotent]

</div>

---

## 🧵 1. Overview

This pipeline consumes **NOAA NODD** SNS notifications, pushes them through a **governed SQS queue**, and drives a **deterministic ETL chain** that:

- Fetches new objects from NOAA NODD public cloud buckets (AWS, Azure, GCP mirrors).
- Performs integrity and metadata checks.
- Registers granules as **STAC Items** with dataset-specific extensions.
- Emits **PROV-O** provenance to the KFM ledger.
- Produces OpenTelemetry telemetry for latency, errors, cost, and energy.

The design removes polling, reduces ingestion lag, and ensures that each file’s lineage is provable and reproducible.

---

## 🗂️ 2. Directory Layout (Emoji-Prefix Standard)

    docs/pipelines/atmo/nodd-sns-sqs/
    │
    ├── 📄 README.md
    │
    ├── ⚙️ config/
    │   ├── sns-topics.json                 # SNS topic → dataset map
    │   ├── sqs-queues.json                 # Queue policies, DLQ bindings
    │   └── dataset-contracts/              # Ingestion contracts per dataset
    │
    ├── 🧠 operators/
    │   ├── message-parse.md                # SNS → KFM event translator
    │   ├── integrity-check.md              # Size, checksum, header verification
    │   ├── metadata-extract.md             # Spatial/temporal + product metadata
    │   ├── stac-register.md                # Deterministic STAC Item creation
    │   └── provenance-emit.md              # PROV-O lineage event generator
    │
    ├── 🔁 replay/
    │   ├── wal/                            # Write-Ahead Log for idempotent ingest
    │   ├── replay-engine.md                # Deterministic replay mechanism
    │   └── dlq-drain-runbook.md            # Manual remediation for stuck messages
    │
    └── 📊 telemetry/
        ├── otel-integration.md             # Spans, metrics, logs
        ├── cost-energy.md                  # Energy & cost per-ingest sample
        └── slo-error-budget.md             # Error budgets for queue age & DLQ rate

**Directory contract:**

- `config/` describes external dependencies (SNS topics, SQS queues, dataset ingestion contracts).
- `operators/` documents each logical operator in the ETL chain.
- `replay/` defines WAL, DLQ, and replay semantics.
- `telemetry/` specifies spans, metrics, and SLO/error-budget definitions.

---

## 🚀 3. Pipeline Flow

High-level flow:

1. **SNS publish**  
   NOAA NODD SNS topics publish a notification when a new object is written to a public bucket.

2. **SQS receive**  
   An SQS queue subscribed to the SNS topic receives messages with at-least-once delivery guarantees.

3. **Message parse**  
   The ingestion spine reads SQS messages and normalizes SNS payloads into a canonical KFM event envelope.

4. **Object fetch**  
   The pipeline fetches the referenced object from the appropriate NODD bucket (AWS, Azure, or GCP mirror).

5. **Deterministic QC**  
   The pipeline performs deterministic quality checks:
   - File completeness.
   - Header validation.
   - Timestamp range.
   - Expected geospatial coverage and product identifiers.

6. **WAL commit**  
   The event and its metadata are recorded in a **Write-Ahead Log** (WAL) to ensure idempotent processing.

7. **STAC registration**  
   A STAC Item is created with deterministic IDs and dataset-specific extensions; checksums and metadata are attached.

8. **Provenance emit**  
   A PROV-O Entity and Activity chain is emitted to the KFM provenance ledger, linking SNS → SQS → operators → STAC.

9. **Telemetry emit**  
   OpenTelemetry spans and metrics are emitted for queue age, ingest duration, failures, cost, and energy.

10. **Retry / DLQ**  
    Non-transient failures are retried according to policy; persistent issues send messages to a DLQ, with runbooks in `replay/dlq-drain-runbook.md`.

---

## 🛰️ 4. Supported NOAA NODD Datasets

Initial governed scope (expandable):

- GOES-East / GOES-West ABI Level 1b / Level 2 scenes.
- NEXRAD Level II and Level III radar products.
- GFS (Global Forecast System) model outputs.
- HRRR (High-Resolution Rapid Refresh) model outputs.
- Surface observations.
- Ocean data (e.g., NDBC buoy observations).

Each dataset has a dedicated ingestion contract under:

- `config/dataset-contracts/`

Dataset contracts define:

- SNS topic ARNs and message formats.
- Expected bucket prefixes and object naming conventions.
- Metadata extraction logic (time, space, product type).
- STAC collection mapping and extension usage.

---

## 🔧 5. Deterministic Ingestion Semantics

**Idempotent by design**

- No ingest side-effects are performed without a successful **WAL commit**.
- Downstream writes are keyed by:
  - `(dataset_id, nominal_time, sha256)` or equivalent canonical key.
- STAC registration uses deterministic identifiers (e.g., UUIDv5 or deterministic slugs).
- Multiple deliveries from SQS (retries, duplicates) cannot produce duplicate STAC Items or data rows when contracts are followed.

**Replay model**

- The WAL supports:
  - Rewind (selecting a time or offset range).
  - Reapply (replaying events with identical semantics).
  - Resume after failure (continuing from last committed offset).
- `replay/replay-engine.md` defines:
  - How WAL entries map to ETL steps.
  - Required invariants to ensure replay equivalence.
- `replay/dlq-drain-runbook.md` provides:
  - Manual remediation steps for DLQ events.
  - Validation rules for re-injecting messages safely.

---

## 📦 6. STAC Integration

Each valid granule becomes a **STAC Item** in a dataset-specific STAC Collection.

**STAC Item content:**

- `id`  
  - Deterministic, derived from dataset identifiers and acquisition time.
- `datetime`  
  - Taken from authoritative NOAA metadata (observation, scene, or model time).
- Extensions (dataset-dependent), e.g.:
  - `proj:*` for projection metadata.
  - `eo:*` for Earth Observation scenes.
  - `sat:*` for satellite platform and orbit details.
- `geometry` / `bbox`  
  - Derived from product spatial coverage.
- `assets`  
  - Links to the primary data file and relevant sidecars (e.g., QA flags, cloud masks).
- Checksums and sizes for each asset.
- Links to provenance and related items.

**Storage layout:**

    data/stac/nodd/<dataset>/<year>/<day>/<item-id>.json

Where:

- `<dataset>` corresponds to the KFM dataset identifier (e.g., `goes-abi`, `nexrad-l2`, `hrrr`).
- `<year>` / `<day>` follow acquisition time (UTC).
- `<item-id>` is the deterministic STAC Item ID.

---

##🧱 7. Provenance & Lineage (PROV-O)

The pipeline treats each ingest as a **PROV-O Activity** that:

- `prov:used`
  - The SNS notification Entity.
  - The SQS message Entity.
  - The remote object Entity (NODD bucket object).
- `prov:generated`
  - One or more STAC Item Entities.
  - Derived metadata Entities (e.g., QC reports).
- `prov:wasAssociatedWith`
  - A KFM pipeline Agent (service identity, operator, or automated workflow).

Provenance objects must:

- Be emitted in a machine-readable format.
- Link back to STAC Items and KFM dataset records.
- Be discoverable in the KFM provenance ledger and graph.

---

## 🛡️ 8. Governance, FAIR+CARE, & Ethics

This pipeline is **governed**, meaning:

- All operators must be deterministic and documented under `operators/`.
- Metadata transformations may not alter the scientific meaning of measurements.
- Any derived fields (e.g., flags, summary statistics) must:
  - Indicate derivation.
  - Include references to source metadata and algorithms.

**FAIR**

- Findable: STAC and provenance records are indexed and discoverable.
- Accessible: Public datasets remain public; internal processing logs follow access control.
- Interoperable: STAC and PROV-O models use established standards and KFM profiles.
- Reusable: Ingestion contracts and transformations are documented and versioned.

**CARE**

- Collective benefit: Atmospheric data is used to support hazard awareness, research, and resilience.
- Authority to control: If future datasets intersect Indigenous or sovereign concerns, dataset contracts must:
  - Respect access policies.
  - Apply generalization or redaction as required.
- Responsibility and Ethics: Energy and cost telemetry is collected to monitor sustainability and cloud usage.

Governance checks:

- Implemented via LangGraph governance gates before STAC registration and ledger commit.
- Runbook references are included in `replay/dlq-drain-runbook.md` and telemetry docs.

---

## 📊 9. Telemetry & Reliability Standards

**Metrics collected (minimum set):**

- Queue depth (SQS approximate number of messages).
- Queue age:
  - P50, P90, P99 message age.
- Retry count:
  - Per-dataset, per-operator.
- DLQ rate:
  - Fraction of messages routed to DLQ.
- Ingest duration:
  - End-to-end latency for each granule.
- Throughput and volume:
  - Messages per second.
  - Bytes ingested per unit time.
- Resource use (estimated):
  - Energy (kWh equivalent).
  - Cloud cost (currency).
  - Carbon intensity (gCO₂e) where available.

**SLO examples:**

- Queue age SLO:
  - P90 message age < 90 seconds.
- DLQ SLO:
  - < 0.05% of messages per rolling window.
- Replay determinism SLO:
  - 100% equivalence for WAL replays within defined windows.

Telemetry is defined in:

- `telemetry/otel-integration.md`
- `telemetry/cost-energy.md`
- `telemetry/slo-error-budget.md`

OpenTelemetry exports are summarized at `telemetry_ref`.

---

## 🧪 10. Validation & Testing

Before activation (and on every change), the following test families are required:

- **SNS message schema validation**
  - Confirms SNS payloads conform to expected structure per dataset contract.
- **SQS delivery simulation**
  - Exercises at-least-once semantics and duplicate deliveries.
- **Corrupt file detection**
  - Ensures that truncation, checksum mismatches, or header corruption are detected and handled.
- **Replay equivalence test**
  - Verifies that WAL-driven replays produce identical STAC Items and provenance.
- **STAC compliance test**
  - Validates Items against KFM’s STAC profiles and schemas.
- **Provenance completeness**
  - Confirms that each ingest has a complete PROV-O chain from SNS to STAC.

All tests must:

- Be wired into CI/CD.
- Block promotion when failing.
- Be documented under `operators/` and `replay/` as appropriate.

---

## 📚 11. Version History

| Version  | Date       | Notes                                                       |
|----------|------------|-------------------------------------------------------------|
| v11.2.3  | 2025-12-04 | Initial full governance-aligned release.                   |
| v11.2.2  | 2025-11-12 | Added HRRR and NEXRAD Level II metadata validators.        |
| v11.2.1  | 2025-10-28 | Added WAL v3 and deterministic UUIDv5 STAC ID strategy.    |
| v11.2.0  | 2025-10-10 | Migration to LangGraph governance gates for this pipeline. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

⬅ Back to Atmospheric Pipelines · ⬅ Back to Pipelines Index · 📜 Governance Charter

</div>