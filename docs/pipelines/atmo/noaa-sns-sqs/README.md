---
title: "🌩️ KFM v11 — NOAA SNS → SQS Event-Driven Ingestion (GOES · NEXRAD · Public Datasets)"
path: "docs/pipelines/atmo/noaa-sns-sqs/README.md"
version: "v11.2.3"
last_updated: "2025-12-01"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Atmospheric Systems · FAIR+CARE Council"
backward_compatibility: "v10.x → v11.x ingestion-contract compatible"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.3/noaa-sns-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/noaa-sns-sqs-v1.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

fair_category: "FAIR: A2 · Interoperable Event Streams"
care_label: "CARE: C1 · Stewardship for Environmental Data"
doc_kind: "Pipeline Overview"
intent: "noaa-sns-sqs"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "United States / Kansas"
classification: "Public · Environmental Data Pipeline"
ttl_policy: "Review each major release"
sunset_policy: "Superseded by next NOAA ingestion architecture revision"
immutability_status: "version-pinned"
---

<div align="center">

# 🌩️ NOAA SNS → SQS Event-Driven Ingestion Pipeline  
**GOES-16 · GOES-18 · NEXRAD Level II**  
**AWS Open Data Notifications**

This service listens to NOAA’s public SNS topics (GOES + NEXRAD) and reliably ingests new granules via an SQS-based fan-out queue, applying Write-Audit-Publish (WAP) controls before they enter the KFM registry, lineage store, and downstream transformation graph.

</div>

---

## 📘 Overview

This ingestion pipeline implements an **event-driven bridge** from NOAA’s AWS Open Data SNS notifications into KFM’s atmospheric data stack:

- 🛰 GOES-16 / GOES-18 ABI + related products  
- 📡 NEXRAD Level II radar data  
- 📨 SNS topics → 📬 SQS queues (fan-out, buffering, redrive)  
- 🧾 JSON schema normalization and validation  
- 🪵 WAP (Write-Audit-Publish) enforcement & lineage capture  
- 📊 Telemetry and energy/carbon metrics for ingestion operations  

The design is:

- **Deterministic** — same messages → same normalized events → same STAC/WAP outputs  
- **Governed** — all writes are WAP-controlled and provenance-tagged  
- **Interoperable** — events can be re-consumed by other KFM pipelines and external tools  

---

## 🗂️ Directory Layout

~~~text
docs/pipelines/atmo/noaa-sns-sqs/
│
├── 📄 README.md                        # This file
│
├── 📨 sns-topics/                      # Topic ARNs, deprecation notes, migration maps
│   ├── 🌐 goes16.md
│   ├── 🌐 goes18.md
│   └── 🌐 nexrad-level2.md
│
├── 📬 sqs/                             # Queue contracts, redrive policies, DLQ
│   ├── 📜 queue-policy.json
│   ├── 📜 dlq-policy.json
│   └── 📘 fifo-guidelines.md
│
├── 🔧 handlers/                        # Lambda / containerized event handlers (design docs)
│   ├── 🧾 normalize-message.md
│   ├── ✅ validate-schema.md
│   ├── 📥 enqueue-wap.md
│   └── 🚨 errors.md
│
├── 🧾 schemas/                         # Event + object-metadata normalization schemas
│   ├── 🛰 noaa-goes-event.json
│   ├── 📡 noaa-nexrad-event.json
│   └── 📦 common-object-metadata.json
│
├── 🔒 iam/                             # IAM policies for SNS → SQS perms
│   ├── 🔑 sqs-allow-sns.json
│   └── 🔑 sns-subscription-policy.json
│
├── 🛠️ terraform/                       # Infrastructure-as-Code definitions
│   ├── 📨 sns.tf
│   ├── 📬 sqs.tf
│   ├── 🧩 lambda.tf
│   └── 📤 outputs.tf
│
└── 🪵 lineage/                         # WAP lineage checks, PROV-O mapping, sustainability
    ├── 📃 wap-contract.md
    ├── 🧬 prov-mapping.json
    └── 🌱 energy-carbon-metrics.md
~~~

---

## 🔔 Supported NOAA AWS SNS Topics (2025)

| Dataset             | Topic Name               | Notes                                                   |
|---------------------|--------------------------|---------------------------------------------------------|
| **GOES-16**         | `NewGOES16Object`        | Real-time ABI/L1b/L2 notifications                      |
| **GOES-18**         | `NewGOES18Object`        | Identical contract to GOES-16                           |
| **NEXRAD Level II** | `NewNEXRADLevel2Archive` | Replaces legacy topic, old one deprecated in 2025-09-01 |

All messages are **normalized** into a unified KFM event envelope before WAP entry.

---

## 🔄 End-to-End Flow (High Level)

1. **SNS publishes** when NOAA uploads a new granule to AWS S3.  
2. **SQS queue receives** the message (fan-out, buffered, retry-safe).  
3. **Handler normalizes** event → unified KFM event schema.  
4. **Schema validation** via JSON Schema + common object-metadata enrichment.  
5. **WAP ingest**:
   - **Write:** stage-area registration  
   - **Audit:** checksum, STAC cross-validation, size checks  
   - **Publish:** KFM registry + lineage store updates  

6. **Telemetry emission** (OpenTelemetry + PROV-O fragments for lineage-aware observability).

---

## 🧰 SNS → SQS Permissions (IAM)

### SQS Queue Policy (Minimum)

- MUST allow `sns:Publish` / `sqs:SendMessage` *only* from the correct SNS topics.  
- MUST restrict `SourceArn` to NOAA SNS topic ARNs.  
- MUST deny unknown publishers (defense-in-depth).  

### SNS Subscription Confirmation

Handler design assumptions:

- Messages comply with AWS SNS message format or the subscription is rejected.  
- Only trusted topic ARNs are allowed; no “S3 event proxy” or ad-hoc event sources.  

IAM guidance is detailed in:

- `iam/sqs-allow-sns.json`  
- `iam/sns-subscription-policy.json`

---

## 🧬 Event Schema & Validation Strategy

Each NOAA message is transformed into a **Normalized Event Envelope**.

**Core fields (required or strongly recommended):**

- `bucket` — S3 bucket name (string)  
- `key` — object key (string)  
- `timestamp` — event time (ISO 8601)  
- `dataset_id` — e.g., `goes16`, `goes18`, `nexrad-level2`  
- `instrument` — ABI, Radar, etc.  
- `product_level` — L1b, L2, etc.  
- `granule_id` — derived from key naming convention  
- `expected_size` — size estimate (bytes)  
- `checksum` — sha256 or similar when provided  

All event types cross-map into **PROV-O** + a minimal **STAC Item skeleton** compatible with `KFM-STAC v11`.

Validation:

- JSON Schema validation using `schemas/noaa-goes-event.json`, `noaa-nexrad-event.json`, and `common-object-metadata.json`.  
- Any schema failure results in:
  - event sent to DLQ (Dead Letter Queue)  
  - telemetry event (`schema_error`)  
  - no WAP Write step executed.

---

## 🪵 WAP (Write-Audit-Publish) Hook Integration

WAP contracts enforce:

- **Deterministic writes** to staging.  
- **Checksums** (sha256) required for publish to KFM registry.  
- **STAC Item generation** from normalized metadata:
  - geometry/extent derived by downstream geospatial pipeline.  
- **Lineage** stored as JSON-LD/PROV fragments, linking:
  - SNS event → S3 object → staging asset → STAC Item → KFM dataset.  
- **Publish-gates** for:
  - incomplete events  
  - missing checksum or size  
  - invalid or deprecated products  

WAP details are specified in:

- `lineage/wap-contract.md`  
- `lineage/prov-mapping.json`

---

## 📊 Telemetry (OpenTelemetry + KFM Telemetry)

Emits (non-exhaustive):

- **Ingestion latency** per message (SNS notification → WAP write).  
- **Queue lag** + backlog size metrics for SQS.  
- **Success/fail counts** per dataset_id (GOES-16, GOES-18, NEXRAD).  
- **Schema errors** and normalization failures.  
- **DLQ events** (with minimal, non-sensitive diagnostics).  
- **Energy + carbon metrics** for the ingestion compute path, derived from infra metrics.

Telemetry is aggregated in:

~~~text
../../../../releases/v11.2.3/noaa-sns-telemetry.json
~~~

Telemetry MUST:

- Conform to `telemetry_schema`.  
- Avoid sensitive information (no raw object URLs in logs; use hashed/short IDs if needed).  

---

## ⚖ FAIR+CARE & Governance

Even though NOAA datasets are **public environmental data**, the pipeline must:

- Respect any **downstream CARE constraints** applied within KFM (e.g., sensitive derived products).  
- Maintain accurate provenance (no editing of NOAA’s metadata beyond normalization).  
- Avoid re-labelling or misrepresenting NOAA’s data quality or license terms.  

Governance aspects covered:

- PROV-O mapping ensures that NOAA remains correctly cited as the data producer.  
- Energy/carbon metrics are captured to inform sustainability reporting.  
- Operational logs are used for reliability + reproducibility audits.

---

## 🧪 Validation & CI/CD

Key CI checks include:

- **Schema validation** against `schemas/noaa-*.json`.  
- **Terraform validation** and security scanning.  
- **IAM policy linting** for overly broad grants.  
- **Telemetry schema validation** (matching `noaa-sns-sqs-v1.json`).  
- **Documentation lint** ensuring this README stays in sync with code & infra.

CI workflows:

- `noaa-sns-sqs-schema.yml`  
- `noaa-sns-sqs-terraform.yml`  
- `noaa-sns-sqs-telemetry.yml`  

---

## 🕰 Version History

| Version   | Date       | Notes                                                     |
|-----------|------------|-----------------------------------------------------------|
| **v11.2.3** | 2025-12-01 | Full KFM v11 alignment, stable schemas, telemetry v1      |
| v11.1.x   | 2025-10    | Added WAP lineage mapping and PROV-O fragment generation |
| v10.x     | 2024–2025  | Initial pipeline, basic SNS → SQS ingest and staging     |

---

## ⚖️ Footer

<div align="center">

**Kansas Frontier Matrix — NOAA SNS → SQS Ingestion Pipeline**  
🌩️ Event-Driven Ingest · 🛰 GOES/NEXRAD · 🛡 FAIR+CARE-Aligned · 🌱 Sustainability-Aware  

[📚 Docs Root](../../../README.md) •  
[🧱 Pipelines Index](../../README.md) •  
[🛡 Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md)

© 2025 Kansas Frontier Matrix — MIT License  

**End of Document**

</div>
