```markdown
---
title: "🌫️ KFM v11.2.6 — Air Quality Sources & API Governance (OpenAQ v3 · AirNow · CAMS NRT · Diamond⁹ Ω / Crown∞Ω Certified)"
path: "docs/data/air-quality/README.md"
version: "v11.2.6"
last_updated: "2025-12-10"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council & Reliability Engineering"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
signature_ref: "../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../releases/v11.2.6/slsa-attestation.json"

sbom_ref: "../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../../releases/v11.2.6/air-quality-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/air-quality-sources-v11.2.6.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Data Governance"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "air-quality"
  applies_to:
    - "openaq-v3"
    - "airnow"
    - "cams-nrt"
    - "stac"
    - "governance"
    - "drift-detection"

semantic_intent:
  - "air-quality-data"
  - "api-governance"
  - "versioned-ingestion"
  - "metadata-standardization"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "Environmental (non-sensitive)"
sensitivity_level: "None"
public_exposure_risk: "Low"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:data:air-quality:index:v11.2.6"
semantic_document_id: "kfm-data-air-quality-index-v11.2.6"
event_source_id: "ledger:data-air-quality-index-v11.2.6"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true
diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"
---

<div align="center">

# 🌫️ **KFM v11.2.6 — Air Quality Sources & API Governance**  
`docs/data/air-quality/README.md`

**Purpose:**  
Provide the authoritative governance, validation, provenance, and STAC/DCAT metadata rules for all KFM air-quality ingestion pipelines:  
**OpenAQ v3**, **AirNow**, and **CAMS NRT**.  
Defines freshness gates, schema-drift detection, API lifecycle management, source-version provenance, and ingestion guardrails across the full pipeline:  
**Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j → API → React/MapLibre/Cesium → Story Nodes → Focus Mode.**

</div>

---

## 📘 Overview

Air-quality data sources vary widely in reliability, stability, latency, and validation guarantees.  
This directory provides **unified governance** so downstream pipelines remain:

- Deterministic  
- Reliable under schema/API changes  
- FAIR+CARE aligned  
- STAC/DCAT-compatible  
- Focus Mode-aware  
- Provenance-complete  

Primary supported sources:

- **OpenAQ v3** — globally standardized community air-quality platform  
- **AirNow** — US EPA preliminary & official AQI/observational feeds  
- **CAMS NRT** — Copernicus real-time atmospheric composition forecasts  

All ingestion must validate freshness windows, source versions, cadence patterns, and licensing/usage constraints.

---

## 🗂️ Directory Layout

~~~text
docs/data/air-quality/
├── 📄 README.md                               # This file
│
├── 📁 sources/                                # Per-source governance docs
│   ├── 📄 openaq-v3.md                        # OpenAQ v3 migration + ingestion
│   ├── 📄 airnow.md                           # AirNow preliminary-data governance
│   └── 📄 cams-nrt.md                         # CAMS NRT validation-window policy
│
├── 📁 stac/                                   # STAC metadata templates
│   ├── 📁 collections/
│   │   ├── 🌐 openaq.json                     # STAC Collection: OpenAQ v3
│   │   ├── 🌐 airnow.json                     # STAC Collection: AirNow
│   │   └── 🌐 cams-nrt.json                   # STAC Collection: CAMS NRT
│   └── 📂 items/
│       └── 📄 template-item.json              # STAC Item template (version-tagged)
│
├── 📁 ingestion/                              # Ingestion configuration files
│   ├── 🧾 openaq-v3-config.yaml               # OpenAQ v3 ingestion policy
│   ├── 🧾 airnow-config.yaml                  # AirNow freshness-gate rules
│   └── 🧾 cams-nrt-config.yaml                # CAMS cadence-aware rules
│
└── 📁 governance/                             # Data governance assets
    ├── 📄 freshness-gates.md                  # Freshness gating per provider
    ├── 📄 api-lifecycle-tracking.md           # API retirement & version-control
    └── 📄 provenance-schema.json              # PROV-O / DCAT extensions
~~~

---

## 📦 Scope of This Directory

This directory governs:

- **API lifecycle tracking** (breaking changes, forced migrations, deprecations)  
- **Versioned provenance** in all STAC Collections & Items  
- **Freshness gating rules** per provider  
- **Schema-drift detection** and WAL-safe ingestion fallback  
- **Latency thresholds** for real-time ingestion  
- Harmonized **STAC/DCAT metadata baselines**  
- Example ingestion configs (OpenAQ v3, AirNow, CAMS NRT)  
- Error handling + decision trees for reliability engineering  
- Integration hooks for:
  - OpenTelemetry  
  - OpenLineage  
  - Error-budget enforcement  

Each rule here informs all dependent pipelines under `src/pipelines/atmo/air-quality/`.

---

## 🧭 Responsibilities

This directory is responsible for:

- Maintaining **API lifecycle policies**  
- Ensuring all datasets embed **source-version IDs**  
- Defining:
  - freshness expectations  
  - polling cadence  
  - fallback logic  
  - status marking (“unverified”, “preliminary”, “validated”)  
- Publishing ingestion guardrails  
- Writing metadata templates for:
  - STAC Collections  
  - STAC Items  
  - PROV-O lineage  
  - DCAT dataset registrations  

All content must pass **KFM-MDP v11.2.6** CI enforcement.

---

## 🌍 Source Governance Summary

### 🟦 OpenAQ v3 — Mandatory Migration

- v1/v2 retired: **2025-01-31**  
- All ingestion MUST use:
  - `/v3/locations`
  - `/v3/latest`
  - `/v3/measurements`
- STAC Items require:
  - `properties.source_version: "OpenAQ-v3"`
  - API metadata snapshot embedded in lineage

### 🟧 AirNow — Preliminary + Verified Modes

- All data considered **preliminary** unless explicitly official  
- Freshness gating mandatory  
- Must embed **Fact Sheet last-updated timestamp**  
- Missing data ≠ outage → mark as **unverified interval**

### 🟩 CAMS NRT — Cadence-Aware Forecasting

- Last public validation checkpoint: **2025-06-01**  
- Polling must respect **cadence**, not fixed frequency  
- STAC Items require:
  - `properties.validation_window`
  - `properties.source_version`
  - forecast cycle metadata

---

## 🧩 Integration With KFM Pipelines

All air-quality ingestion flows must align with the core KFM pipeline:

> **Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j → API → React/MapLibre/Cesium → Story Nodes → Focus Mode**

Specifically, they integrate with:

- **LangGraph DAG orchestrator** for deterministic ETL and replay  
- **OpenTelemetry** for metrics and traces  
- **OpenLineage** for job- and dataset-level lineage  
- **Neo4j ingestion** via governed graph mappers  
- **Energy + carbon telemetry schemas** for sustainability reporting  
- **Pipeline contract enforcement** (`KFM-PDC v11`) to guarantee API and schema stability  

Operational compliance:

- WAL-safe writes  
- Idempotent upserts  
- Rollback hooks  
- Canary testing for structure/API changes  
- Schema drift detection and auto-quarantine of suspect batches  

---

## 🧪 QA, Testing & Drift Monitoring

Daily test suite:

- API link checks  
- Schema-diff detection  
- Freshness thresholds  
- Latency checks  
- Proactive fallback to previous stable datasets  

Failures are logged in:

- `releases/*/air-quality-telemetry.json`

These telemetry artifacts are validated against  
`schemas/telemetry/air-quality-sources-v11.2.6.json`.

---

## 🕰️ Version History

| Version  | Date       | Notes                                                                                           |
|----------|------------|-------------------------------------------------------------------------------------------------|
| v11.2.6  | 2025-12-10 | Aligned with KFM-MDP v11.2.6; restored emoji directory layout; updated release & telemetry refs |
| v11.2.2  | 2025-11-28 | Upgraded to v11.2.2; emoji directory tree; full STAC/DCAT/PROV-O alignment                     |
| v11.1.0  | 2025-11-10 | Initial air-quality governance directory established                                            |

---

<div align="center">

### 🔗 Footer  

[🌐 KFM Home](../../README.md) · [📚 Standards](../../standards/README.md) · [📦 STAC Catalog](../../data/stac/)

</div>
```
