---
title: "🌩️ KFM v11 — NOAA SNS → SQS Event-Driven Ingestion (GOES · NEXRAD · Public Datasets)"
path: "docs/pipelines/atmo/noaa-sns-sqs/README.md"
version: "v11.2.3"
last_updated: "2025-12-01"

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
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

fair_category: "FAIR: F1-A2 · Interoperable Event Streams"
care_label: "CARE: C1 · Environmental Data Stewardship"
doc_kind: "Pipeline Overview"
intent: "noaa-sns-sqs"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "United States / Kansas"
classification: "Public · Environmental Data Pipeline"
ttl_policy: "Review at each major release"
sunset_policy: "Replaced by future NOAA ingestion architecture revisions"
immutability_status: "version-pinned"
---

<div align="center">

# 🌩️ NOAA SNS → SQS Event-Driven Ingestion Pipeline  
### **GOES-16 · GOES-18 · NEXRAD Level II**  
### **AWS Public Dataset Notifications → KFM WAP**

This pipeline consumes NOAA’s real-time SNS notifications, normalizes messages, enforces WAP lineage gates, and publishes deterministic ingestion events into the KFM atmospheric stack.

</div>

---

## 📘 1. Overview

This subsystem handles NOAA’s event-driven ingest path:

- 🛰 **GOES-16 / GOES-18 ABI** products  
- 📡 **NEXRAD Level II** radar archive  
- 📨 **SNS → SQS fan-out** ingestion  
- 🧾 **Normalization + schema validation**  
- 🛡 **WAP** (Write-Audit-Publish) lineage enforcement  
- 📊 **Telemetry + sustainability metrics**  

Core design principles:

- **Deterministic:** identical SNS messages always yield identical WAP and STAC output.  
- **Governed:** every event is provenance-tracked and audit-gated.  
- **Interoperable:** outputs seamlessly integrate with KFM STAC, PROV-O, and LangGraph operators.

---

## 🗂 2. Directory Structure (Emoji-Prefix Standard)

~~~text
docs/pipelines/atmo/noaa-sns-sqs/
│
├── 📄 README.md                               # This file
│
├── 📨 sns-topics/                             # NOAA SNS topic definitions
│   ├── 🌐 goes16.md
│   ├── 🌐 goes18.md
│   └── 🌐 nexrad-level2.md
│
├── 📬 sqs/                                     # Queue policies + redrive design
│   ├── 📜 queue-policy.json
│   ├── 📜 dlq-policy.json
│   └── 📘 fifo-guidelines.md
│
├── 🔧 handlers/                                # Event handler specifications
│   ├── 🧾 normalize-message.md
│   ├── ✅ validate-schema.md
│   ├── 📥 enqueue-wap.md
│   └── 🚨 errors.md
│
├── 🧾 schemas/                                 # JSON Schema validation contracts
│   ├── 🛰 noaa-goes-event.json
│   ├── 📡 noaa-nexrad-event.json
│   └── 📦 common-object-metadata.json
│
├── 🔒 iam/                                     # IAM bindings + SNS→SQS trust
│   ├── 🔑 sqs-allow-sns.json
│   └── 🔑 sns-subscription-policy.json
│
├── 🛠️ terraform/                               # IaC: SNS, SQS, handlers, outputs
│   ├── 📨 sns.tf
│   ├── 📬 sqs.tf
│   ├── 🧩 lambda.tf
│   └── 📤 outputs.tf
│
└── 🪵 lineage/                                 # WAP + PROV-O lineage contracts
    ├── 📃 wap-contract.md
    ├── 🧬 prov-mapping.json
    └── 🌱 energy-carbon-metrics.md
~~~

---

## 🔔 3. Supported NOAA SNS Topics (2025)

| Dataset | Topic Name | Notes |
|--------|-------------|-------|
| **GOES-16** | `NewGOES16Object` | ABI + L1b/L2 feed |
| **GOES-18** | `NewGOES18Object` | Contract-identical to GOES-16 |
| **NEXRAD Level II** | `NewNEXRADLevel2Archive` | Legacy topic deprecated 2025-09-01 |

All inputs are transformed into a **Unified KFM Event Envelope** before entering WAP.

---

## 🔄 4. Event Flow (High-Level)

1. **SNS publishes** on new NOAA granule arrival.  
2. **SQS fan-out queue** receives and buffers messages.  
3. **Handler normalization:**
   - dataset classification  
   - metadata extraction  
   - envelope unification  
4. **Schema validation:** JSON Schema + common metadata enrichment.  
5. **WAP pipeline:**
   - **Write:** staging registration  
   - **Audit:** checksum validation + STAC hints  
   - **Publish:** registry + lineage  
6. **Telemetry:** ingestion latency, queue lag, error patterns, energy/carbon metrics.

---

## 🧬 5. Event Schema & Validation

The **Unified Event Envelope** includes:

- `dataset_id` (`goes16`, `goes18`, `nexrad-level2`)  
- `bucket` and `key`  
- `timestamp` (ISO-8601 event time)  
- `instrument` / `product_level`  
- `granule_id` (derived)  
- `expected_size` and `checksum` when provided  

Schemas live under `schemas/` and must pass:

- **strict JSON Schema** validation  
- **cross-field rules** (e.g., product naming conventions)  
- **metadata enrichment** (instrument, spatial hints)  

Failures trigger:

- DLQ routing  
- structured telemetry error events  
- no WAP write allowed  

---

## 🛡 6. WAP (Write-Audit-Publish)

WAP gating enforces:

### **Write**
- deterministic staging path  
- atomic object registration  

### **Audit**
- sha256 checksum match  
- STAC skeleton consistency  
- NOAA → KFM mapping accuracy  
- validation signatures  

### **Publish**
- registry entry  
- lineage event generation  
- telemetry emission  

Lineage uses **PROV-O JSON-LD** mapped via `lineage/prov-mapping.json`.

---

## 📬 7. SNS → SQS IAM Controls

Minimum required guarantees:

- SQS must **only** accept messages from official NOAA SNS ARNs.  
- SNS subscription policies must enforce **SourceArn** and **Sender** validation.  
- No wildcard publishers allowed.  
- Subscription confirmation failures must be logged and blocked.  

IAM definitions live under `iam/`.

---

## 📊 8. Telemetry (OTel · Sustainability)

Metrics exported:

- ingestion latency  
- queue backlog  
- schema error counts  
- DLQ depth + reason codes  
- WAP audit failure types  
- compute duration → energy estimation  
- carbon factors via `carbon_schema`  

Telemetry file stored at:

```
../../../../releases/v11.2.3/noaa-sns-telemetry.json
```

---

## ⚖️ 9. Governance, FAIR, CARE

Governance obligations:

- NOAA remains recorded as the **source authority**.  
- No metadata rewriting beyond normalization.  
- CARE rules respected for downstream derived products.  
- Sustainability telemetry required (energy + carbon).  
- Provenance must remain **immutable** and **replayable**.

---

## 🧪 10. CI/CD Validation

Required checks:

- JSON Schema validation  
- IaC validation + security scanning  
- WAP contract consistency  
- Telemetry schema validation  
- Markdown/MDP compliance  

Workflows:

- `noaa-sns-sqs-schema.yml`  
- `noaa-sns-sqs-terraform.yml`  
- `noaa-sns-sqs-telemetry.yml`

---

## 🕰 11. Version History

| Version | Date | Notes |
|--------|-------|-------|
| **v11.2.3** | 2025-12-01 | Full KFM-v11 rework, WAP integration, telemetry v1 |
| v11.1.x | 2025-10 | PROV-O lineage mapping added |
| v10.x | 2024–2025 | Original SNS→SQS ingestion pipeline |

---

## ⚖️ 12. Footer

<div align="center">

**Kansas Frontier Matrix — NOAA Event-Driven Ingestion Subsystem**  
🌩️ Real-Time NOAA Feeds · 🛰 GOES/NEXRAD · 🛡 WAP-Governed · 🌱 Sustainability-Aware  

[📚 Docs Root](../../../README.md) •  
[🧱 Pipelines Index](../../README.md) •  
[🛡 Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md)

© 2025 Kansas Frontier Matrix — MIT License  

**End of Document**

</div>