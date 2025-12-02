---
title: "🌩️ KFM v11.2.3 — NOAA SNS → SQS Event-Driven Ingestion Pipeline (GOES · NEXRAD · Public Datasets) — Diamond⁹ Ω / Crown∞Ω Ultimate Certified"
description: "Governed, deterministic ingestion of NOAA public dataset notifications (GOES-16/18, NEXRAD Level II) via SNS → SQS into the KFM atmospheric domain with WAP lineage, STAC previews, and sustainability telemetry."
path: "docs/pipelines/atmo/noaa-sns-sqs/README.md"
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Atmospheric Systems · FAIR+CARE Oversight"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x ingestion-contract compatible"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.3/noaa-sns-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/noaa-sns-sqs-v1.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

fair_category: "F1-A2-I1-R1"
care_label: "Environmental Data Stewardship"
doc_kind: "Pipeline Overview"
intent: "noaa-sns-sqs"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "United States / Kansas"
classification: "Public · Environmental Data Pipeline"
ttl_policy: "Review at each major release"
sunset_policy: "Replaced by future NOAA ingestion architecture revisions"
immutability_status: "version-pinned"

header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "atmospheric-ingestion"
  applies_to:
    - "noaa-sns"
    - "goes-16"
    - "goes-18"
    - "nexrad-level2"
    - "event-ingestion"
    - "wap-lineage"

semantic_intent:
  - "reliability"
  - "governance"
  - "environmental-data"
category: "Pipelines · Atmospheric · Events"

data_steward: "Atmospheric Systems WG · Reliability Engineering"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "governance-override"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "provenance-check"
  - "footer-check"
---

<div align="center">

# 🌩️ NOAA SNS → SQS Event-Driven Ingestion Pipeline  
### **GOES-16 · GOES-18 · NEXRAD Level II · AWS Public Datasets**  
### **Real-Time Atmospheric Ingestion for the Kansas Frontier Matrix**

This subsystem consumes NOAA public-dataset SNS notifications, performs deterministic normalization and validation, applies **WAP** lineage gates, and publishes governed ingestion artifacts into the KFM atmospheric domain.

</div>

---

## 📘 1. Overview

This pipeline implements the **KFM v11 atmospheric ingestion model**, built on:

- 🛰 **GOES-16 & GOES-18 ABI** satellite feeds  
- 📡 **NEXRAD Level II** radar archive notifications  
- 📨 **SNS → SQS** event fan-out  
- 🔧 **Deterministic handlers** (normalization → schema → audit)  
- 🛡 **WAP lineage enforcement**  
- 🗂 **STAC preview + metadata skeletons**  
- 🔁 **Retry, replay & idempotency gates**  
- 📊 **Telemetry, SLO/SLI metrics & sustainability accounting**  

Design mandates:

- **Deterministic** — identical SNS messages produce identical KFM envelopes, WAP signatures, and STAC preview objects.  
- **Governed** — every ingestion action is audit-controlled through PROV-O lineage mapping.  
- **Reproducible** — WAL-style replay and SQS FIFO/dedup keys ensure exactly-once-ish behavior.  
- **Interoperable** — all outputs integrate with STAC v1.x, PROV-O JSON-LD, LangGraph operators, and Focus Mode.

---

## 🗂 2. Directory Structure (Emoji-Prefix Standard)

~~~text
docs/pipelines/atmo/noaa-sns-sqs/
│
├── 📄 README.md                                   # This file
│
├── 📨 sns-topics/                                 # NOAA SNS topic specifications
│   ├── 🌐 goes16.md
│   ├── 🌐 goes18.md
│   └── 🌐 nexrad-level2.md
│
├── 📬 sqs/                                        # Queue policies + redrive model
│   ├── 📜 queue-policy.json
│   ├── 📜 dlq-policy.json
│   └── 📘 fifo-guidelines.md
│
├── 🔧 handlers/                                   # Deterministic event processors
│   ├── 🧾 normalize-message.md
│   ├── ✅ validate-schema.md
│   ├── 📥 enqueue-wap.md
│   └── 🚨 errors.md
│
├── 🧾 schemas/                                    # JSON Schemas (NOAA + KFM)
│   ├── 🛰 noaa-goes-event.json
│   ├── 📡 noaa-nexrad-event.json
│   └── 📦 common-object-metadata.json
│
├── 🔒 iam/                                        # SNS→SQS trust & IAM definitions
│   ├── 🔑 sqs-allow-sns.json
│   └── 🔑 sns-subscription-policy.json
│
├── 🛠️ terraform/                                  # IaC for SNS/SQS/Lambda
│   ├── 📨 sns.tf
│   ├── 📬 sqs.tf
│   ├── 🧩 lambda.tf
│   └── 📤 outputs.tf
│
├── 🪵 lineage/                                    # WAP + PROV-O lineage logic
│   ├── 📃 wap-contract.md
│   ├── 🧬 prov-mapping.json
│   └── 🌱 energy-carbon-metrics.md
│
├── 📑 contracts/                                  # Deterministic ingestion rules
│   ├── 🆔 dedupe-id.md                            # Message key derivation
│   ├── 📦 envelope-contract.md                    # Unified Event Envelope (UEE)
│   └── 🖋️ wap-signature.md                        # WAP audit signatures
│
├── 🔁 retry-replay/                               # WAL-style replay & recovery
│   ├── 📄 replay-strategy.md
│   ├── 📄 replay-contracts.md
│   └── 📄 event-rehydration.md
│
├── 🎯 sli-slo/                                    # SLOs, SLIs, burn budgets
│   ├── 📊 ingestion-latency.md
│   ├── 📊 queue-health.md
│   └── 📊 validation-error-budgets.md
│
├── 🗂️ stac-preview/                               # STAC skeleton generation
│   ├── 🧱 stac-item-skeleton.md
│   └── 🧱 stac-collection-hints.md
│
├── 🔧 transform/                                  # Metadata enrichers & classifiers
│   ├── 🛰 goes-deriver.md
│   ├── 📡 nexrad-deriver.md
│   └── 🧭 spatial-hints.md
│
└── 🧪 tests/                                      # Regression, schema, replay testing
    ├── 🧪 schema-tests.md
    ├── 🧪 golden-messages.json
    └── 🧪 replay-vectors.md
~~~

---

## 🔔 3. Supported NOAA SNS Topics (2025)

| Dataset          | Topic Name               | Notes                               |
|------------------|--------------------------|-------------------------------------|
| GOES-16          | `NewGOES16Object`        | ABI feed, L1b/L2 products           |
| GOES-18          | `NewGOES18Object`        | Contract-identical to GOES-16       |
| NEXRAD Level II  | `NewNEXRADLevel2Archive` | Legacy topic deprecated 2025-09-01  |

All incoming events are rewritten into the **Unified KFM Event Envelope (UEE)** before validation.

---

## 🔄 4. High-Level Event Flow — v11 Deterministic Model

1. SNS publishes an event when a new object appears in NOAA buckets.  
2. SQS FIFO queue receives messages with content-based deduplication.  
3. Normalization handler rewrites the payload into a **KFM Event Envelope (UEE)**.  
4. Schema validation via JSON Schema plus metadata cross-rules.  
5. Transform stage enriches spatial/product metadata and STAC hints.  
6. WAP gates:

   - **Write** — register staging paths.  
   - **Audit** — checksum + STAC preview consistency checks.  
   - **Publish** — lineage events and registry entries.

7. SLI/SLO metrics emitted at each step.  
8. Energy & carbon telemetry computed at job completion using energy/carbon schemas.  
9. Replay engine enables deterministic recovery from WAL-compatible logs.

---

## 🧬 5. Unified Event Envelope (UEE)

Defined in `contracts/envelope-contract.md`.

Core fields:

- `dataset_id` — `goes16`, `goes18`, `nexrad-level2`.  
- `event_time` — ISO-8601 ingestion event time.  
- `object` — `{ bucket, key, size, checksum? }`.  
- `granule_id` — deterministic product of file path + vendor naming rules.  
- `instrument`, `product_level`, `scan_mode`.  
- `spatial_hint` — bounding tile or footprint (when derivable).  
- `source_arn` — authoritative NOAA ARN.

UEE MUST pass:

- Strict schema validation.  
- Cross-field constraints (e.g., product-level ↔ filename consistency).  
- Deterministic derivation rules.

Any failure → DLQ with machine-readable reason codes.

---

## 🛡 6. WAP (Write–Audit–Publish) — v11 Enforcement

Located under `lineage/` and `contracts/`.

**Write**

- Atomic staging of raw objects and metadata.  
- Frozen copy of incoming metadata.  
- Append-only registration into ingestion logs.

**Audit**

- SHA-256 checksum verification.  
- STAC preview alignment checks.  
- NOAA → KFM product mapping validation.  
- Validation signatures (see `wap-signature.md`).

**Publish**

- PROV-O lineage emission (per `lineage/prov-mapping.json`).  
- Registry updates (atmospheric dataset catalogs).  
- SLO timestamp emission (e.g., max-latency).  
- Telemetry packaging (reliability, energy, carbon).

---

## 🔁 7. Retry, Replay & WAL-Style Recovery

Located in `retry-replay/`.

Components:

- **Replay Strategy** — deterministic ordering + idempotent dedupe keys.  
- **Replay Contracts** — UEE rehydration + WAP gating rules.  
- **Golden Replay Vectors** — stored under `tests/` for regression testing.

Replay is:

- **Lossless** — events are never silently dropped.  
- **Idempotent** — repeated replays converge on the same state.  
- **Audit-locked** — all replay actions generate lineage & telemetry traces.

---

## 🎯 8. SLO / SLI Error Budgets

Located in `sli-slo/`.

Tracked indicators:

- Ingestion latency (P50/P95/P99).  
- Queue backlog depth and age.  
- Schema validation error rates.  
- DLQ utilization and error classes.  
- WAP audit failure rates.

Burn alerts:

- Feed atmospheric reliability dashboards.  
- Are reviewed by the FAIR+CARE Council and Atmospheric Systems WG.

---

## 🗂️ 9. STAC Preview Skeletons

Located in `stac-preview/`.

Each UEE produces:

- A **STAC Item skeleton** (no assets yet).  
- **STAC Collection hints** for automatic collection updates.  
- Consistency checks for filename ↔ product-level ↔ collection mapping.

This enables shallow provenance and discoverability **before** full product hydration.

---

## 🔧 10. Transformation Layer

Located in `transform/`.

Responsibilities:

- Product classification (e.g., ABI L1b vs L2).  
- Spatial derivation (tile ID, bounding box, region hints).  
- Instrument metadata population.  
- NEXRAD scan-time hydration (radar ID, volume scan time).  
- GOES ABI band and channel inference.

All transforms MUST be:

- Deterministic.  
- Version-pinned with change logs.  
- Tested against **golden messages** in `tests/golden-messages.json`.

---

## 📊 11. Telemetry, Energy & Carbon Metrics

Telemetry is emitted at:

- UEE creation.  
- Schema validation completion.  
- WAP write/audit/publish transitions.  
- Replay and DLQ handling steps.

Outputs MUST follow:

- `telemetry_schema` — `noaa-sns-sqs-v1.json`.  
- `energy_schema` — `energy-v2.json`.  
- `carbon_schema` — `carbon-v2.json`.

Representative metrics:

- Queue lag (per topic/region).  
- Event processing duration.  
- CPU-seconds converted to kWh estimates.  
- Carbon conversion via regional grid factors.

These metrics power:

- Reliability SLI/SLO dashboards.  
- Sustainability and carbon reports.  
- Governance and FAIR+CARE compliance checks.

---

## ⚖️ 12. Governance, FAIR, CARE

Obligations:

- **NOAA** remains the authoritative upstream provider; KFM does not alter source truth.  
- No destructive metadata rewriting; original NOAA metadata is preserved.  
- PROV-O lineage MUST remain intact and replayable across versions.  
- **FAIR+CARE** principles applied to:
  - Hazard communication (e.g., severe storms).  
  - Community and infrastructure-related products.  

Sustainability telemetry is required and reviewed regularly.

---

## 🧪 13. CI/CD Validation

Required workflows (names may map to CI jobs):

- `schema-val` — NOAA and UEE schema validations.  
- `terraform-sec` — security checks for IaC.  
- `lineage-consistency` — PROV-O mapping checks.  
- `mdp-compliance` — Markdown protocol compliance (KFM-MDP v11.2.2).  
- `telemetry-schema-tests` — telemetry payload validation.  
- `replay-regression` — replay vectors and WAL behavior tests.

All MUST pass prior to:

- New pipeline releases.  
- Substantial configuration changes (topics, queues, IAM, WAP rules).

---

## 🕰 14. Version History

| Version  | Date       | Notes                                                                 |
|----------|------------|-----------------------------------------------------------------------|
| v11.2.3  | 2025-12-02 | Full Ultimate rewrite; expanded dirs; SLO/SLI; replay engine; STAC preview integration. |
| v11.1.x  | 2025-10    | PROV-O lineage upgrade and WAP enforcement.                           |
| v10.x    | 2024–2025  | Original SNS→SQS ingestion pipeline implementation.                  |

---

<div align="center">

🌩️ **Kansas Frontier Matrix — NOAA SNS → SQS Event-Driven Ingestion**  
Real-Time NOAA Feeds · 🛰 GOES/NEXRAD · 🛡 WAP-Governed · 🌱 Energy/Carbon Telemetry  

[📚 Docs Root](../../../README.md) ·
[🧱 Pipelines Index](../../README.md) ·
[🛡 Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md)  

© 2025 Kansas Frontier Matrix — MIT License

</div>