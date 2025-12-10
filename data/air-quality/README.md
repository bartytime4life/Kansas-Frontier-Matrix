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

# 🌫️ KFM v11.2.6 — Air Quality Sources & API Governance  

Authoritative governance, validation, provenance, and STAC/DCAT metadata rules for all **KFM air-quality ingestion pipelines**:

- **OpenAQ v3**  
- **AirNow**  
- **CAMS NRT**

This file defines **freshness gates**, **schema-drift detection**, **API lifecycle management**, **source-version provenance**, and **ingestion guardrails** for the KFM pipeline:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j graph → API → Story Nodes → Focus Mode

---

## 🗂️ Directory Layout

~~~text
docs/
└── 📁 data/
    └── 📁 air-quality/
        ├── 📄 README.md                          # 🌫️ This file — air-quality sources & API governance
        │
        ├── 📁 sources/                           # Per-source governance and integration docs
        │   ├── 📄 openaq-v3.md                   # OpenAQ v3 migration + ingestion rules
        │   ├── 📄 airnow.md                      # AirNow preliminary/official data governance
        │   └── 📄 cams-nrt.md                    # CAMS NRT validation-window and cadence policies
        │
        ├── 📁 stac/                              # STAC metadata templates (docs side)
        │   ├── 📁 collections/
        │   │   ├── 📄 openaq.json                # STAC Collection template: OpenAQ v3
        │   │   ├── 📄 airnow.json                # STAC Collection template: AirNow
        │   │   └── 📄 cams-nrt.json              # STAC Collection template: CAMS NRT
        │   └── 📁 items/
        │       └── 📄 template-item.json         # Version-tagged STAC Item template
        │
        ├── 📁 ingestion/                         # Ingestion configuration & policy examples
        │   ├── 📄 openaq-v3-config.yaml          # OpenAQ v3 ingestion & freshness policies
        │   ├── 📄 airnow-config.yaml             # AirNow freshness-gate & mode rules
        │   └── 📄 cams-nrt-config.yaml           # CAMS NRT cadence-aware ingest rules
        │
        └── 📁 governance/                        # Data governance assets for air-quality
            ├── 📄 freshness-gates.md             # Freshness gating per provider
            ├── 📄 api-lifecycle-tracking.md      # API retirement & version-control policies
            └── 📄 provenance-schema.json         # PROV-O / DCAT extensions for air-quality
~~~

Related implementation paths (documented in their own READMEs):

- `src/pipelines/atmo/air_quality/` — ingestion and harmonization ETL  
- `data/raw/air_quality/` — immutable raw source pulls  
- `data/work/air_quality/` — normalized intermediate tables  
- `data/processed/air_quality/` — harmonized & unit-converted datasets  
- `data/stac/air_quality/` — STAC Collections & Items for air-quality assets  
- `data/catalogs/air_quality/` — DCAT datasets and distributions  
- `data/provenance/air_quality/` — PROV bundles for ingestion and harmonization runs  

---

## 📘 Overview

Air-quality sources differ significantly in:

- **reliability & uptime**  
- **update cadence & latency**  
- **validation / preliminary status semantics**  
- **schema stability and API lifecycle**  

This directory provides **unified governance** so downstream KFM pipelines remain:

- **Deterministic** — idempotent ETL, contract-driven schemas  
- **Reliable** — robust to API/schema changes, with drift detection and fallbacks  
- **FAIR+CARE aligned** — explicit licenses, usage constraints, and sovereignty-aware rules  
- **STAC/DCAT-compatible** — uniform metadata for sources and harmonized products  
- **Focus Mode-aware** — Story Nodes and UI can explain status, freshness, and provenance  
- **Provenance-complete** — full PROV and OpenLineage coverage

Primary supported sources:

- **OpenAQ v3** — globally standardized community air-quality platform  
- **AirNow** — US EPA preliminary & official AQI/observational feeds  
- **CAMS NRT** — Copernicus real-time atmospheric composition forecasts  

All ingestion must validate **freshness windows**, **source versions**, **cadence patterns**, and **licensing/usage constraints**.

---

## 📦 Scope of This Directory

This directory governs **all air-quality sources and harmonized products** flowing through the KFM pipeline:

- **API lifecycle tracking**
  - breaking changes, forced migrations, deprecations
- **Versioned provenance**
  - source-version IDs in STAC Collections & Items and DCAT datasets
- **Freshness gating**
  - per-provider thresholds and SLOs
- **Schema-drift detection**
  - WAL-safe ingestion fallback and drift telemetry
- **Latency thresholds**
  - for “real-time” and near-real-time ingestion
- **Harmonized STAC/DCAT baselines**
  - common properties and extensions across sources
- **Ingestion configs**
  - reference configs for OpenAQ v3, AirNow, CAMS NRT
- **Error handling & decision trees**
  - guidance for Reliability Engineering
- **Integration hooks**
  - OpenTelemetry, OpenLineage, energy/carbon telemetry, pipeline contracts

These rules apply to all dependent pipelines under:

- `src/pipelines/atmo/air_quality/**`

and must be reflected in both **catalogs** and the **Neo4j graph**.

---

## 🧭 Responsibilities

The air-quality governance index is responsible for:

- Maintaining **API lifecycle policies** per source  
- Ensuring all datasets embed **source-version identifiers**, including:
  - API version  
  - endpoint families  
  - relevant changelog references  
- Defining:
  - freshness expectations (per source & product)  
  - polling cadence and allowed jitter  
  - fallback logic on outage / schema change  
  - status markers (`unverified`, `preliminary`, `validated`)  
- Publishing ingestion guardrails:
  - rate-limit considerations  
  - backoff and retry policies  
- Providing metadata templates for:
  - STAC Collections & Items (KFM-STAC v11 profile)  
  - DCAT Datasets & Distributions (KFM-DCAT v11 profile)  
  - PROV-O lineage and OpenLineage integration

All content is enforced via **KFM-MDP v11.2.6** markdown checks and schema validation.

---

## 🌐 Pipeline Fit (ETL → Catalogs → Graph → UI)

Air-quality ingestion follows the core KFM pipeline:

1. **Deterministic ETL**
   - API → raw pulls → normalized tables  
   - unit-safe handling (native units preserved; unit conversion in harmonization steps)  

2. **STAC / DCAT / PROV Catalogs**
   - STAC Collections & Items for:
     - per-source streams (OpenAQ, AirNow, CAMS NRT)
     - harmonized products  
   - DCAT datasets describing:
     - coverage, licensing, and usage constraints  
   - PROV/OpenLineage for:
     - ingestion runs
     - harmonization and unit conversion

3. **Neo4j Graph**
   - Nodes: `AirQualityObservation`, `Station`, `ForecastGrid`, `Dataset`, `DatasetVersion`, `SourceAPI`  
   - Relationships: `OBSERVED_AT`, `DERIVED_FROM`, `HAS_VERSION`, `USES_API_VERSION`  

4. **API Layer**
   - Stable endpoints for:
     - harmonized air-quality time series  
     - per-station/per-region products  
     - lineages and quality flags  

5. **Story Nodes & Focus Mode**
   - Narrative nodes summarizing:
     - AQ events (e.g., smoke episodes, dust, ozone spikes)  
     - source reliability incidents  
     - SLO / freshness issues  
   - Focus Mode exposes:
     - STAC/DCAT-backed views
     - telemetry and provenance details  

---

## 🌍 Source Governance Summary

### 🟦 OpenAQ v3 — Mandatory Migration

- Legacy v1/v2 retired: **2025-01-31** (no further ingestion from v1/v2).  
- All ingestion MUST use:
  - `/v3/locations`  
  - `/v3/latest`  
  - `/v3/measurements`  
- STAC Items and DCAT datasets MUST include:
  - `properties.kfm:source_id = "openaq"`  
  - `properties.kfm:source_version = "openaq-v3"`  
  - API metadata snapshot (base URL, version, changelog URL) in provenance.  
- Governance requirements:
  - new endpoints or query params require governance review  
  - license and terms-of-use recorded in DCAT and STAC properties

### 🟧 AirNow — Preliminary + Verified Modes

- All data considered **preliminary** unless explicitly flagged as official / verified.  
- Freshness gating is **mandatory**:
  - if data older than SLO threshold → mark as **stale** and route to degraded path.  
- STAC metadata MUST:
  - distinguish `preliminary` vs `official` modes  
  - embed **Fact Sheet “last-updated” timestamp** when available  
- Missing data ≠ outage:
  - treat as **unverified interval**, not as source failure  
  - mark via:
    - STAC properties (`kfm:aq_status = "unverified"`)  
    - graph attributes on `AirQualityObservation` nodes  

### 🟩 CAMS NRT — Cadence-Aware Forecasting

- Last public validation checkpoint: **2025-06-01** (reference for “known good” behavior).  
- Polling must respect **product cadence**, not naive fixed frequency:
  - e.g., per forecast cycle + distribution delay windows.  
- STAC Items MUST include:
  - `properties.kfm:validation_window`  
  - `properties.kfm:source_version = "cams-nrt-vX.Y"`  
  - forecast cycle metadata (run time, lead time, horizon).  
- Latency and forecast-verification data SHOULD feed:
  - `air-quality-telemetry.json`  
  - Story Nodes describing forecast reliability and bias patterns.

---

## 📏 Governance Rules — Freshness, Drift & Latency

### Freshness Gates

- Per-source thresholds for:
  - maximum allowed age since observation/forecast time  
  - allowable missing intervals before marking as **stale** or **degraded**.  
- Documented in `docs/data/air-quality/governance/freshness-gates.md`.  
- Enforced via:
  - ingestion configs in `docs/data/air-quality/ingestion/*.yaml`  
  - telemetry checks in `air-quality-telemetry.json`.

### Schema-Drift Detection

- Daily checks compare:
  - current API response shape vs last known baseline  
  - STAC/DCAT fields vs schemas (`KFM-STAC v11`, `KFM-DCAT v11`).  
- Drift outcomes:
  - **benign drift** → updated templates and configs  
  - **breaking drift** → WAL-safe fallback to previous stable dataset, plus Story Node incident.

### Latency & SLOs

- Source-specific latency SLOs tracked via:
  - `telemetry_ref` (air-quality telemetry)  
  - latency histograms in observability stack.  
- Violations should:
  - annotate STAC Items with SLO state (e.g. `kfm:slo_state`)  
  - trigger reliability incident workflows.

---

## 🌱 FAIR+CARE, Ethics & Sovereignty

Air-quality data are generally **public, low-risk environmental** measurements, but KFM still enforces:

- **FAIR+CARE**:
  - clear licensing & attribution (OpenAQ, AirNow, CAMS policies)  
  - transparent provenance and data quality statements  
- **Sovereignty-aware usage**:
  - integration with Indigenous communities or localized projects must honor:
    - `INDIGENOUS-DATA-PROTECTION.md`  
    - local data-sharing agreements and context of use  
  - avoid misinterpretation in sensitive cultural or land-management contexts.

Ethics and sovereignty policies are referenced from:

- `ethics_ref` and `sovereignty_policy` fields in the front-matter.

---

## 🧪 QA, Testing & Drift Monitoring

Daily and release-time QA includes:

- **API link checks**
  - ensure endpoints are reachable and returning valid data.  
- **Schema-diff detection**
  - compare JSON shapes against golden snapshots and JSON Schemas.  
- **Freshness thresholds**
  - verify all ingested records satisfy per-source freshness SLOs.  
- **Latency checks**
  - measure ingestion lag; alert on sustained breaches.  
- **Fallback verification**
  - confirm WAL-safe fallback to previous stable datasets on failure.  

Results are written to:

- `releases/*/air-quality-telemetry.json` (path referenced via `telemetry_ref`).

These telemetry outputs are ingested into:

- Neo4j (for reliability Story Nodes)  
- dashboards used by Reliability Engineering and FAIR+CARE Council.

---

## 🕰️ Version History

| Version  | Date       | Notes                                                                                 |
|----------|------------|---------------------------------------------------------------------------------------|
| v11.2.6  | 2025-12-10 | Aligned with KFM-MDP v11.2.6; updated references to v11.2.6 releases and schemas; clarified pipeline fit and governance rules. |
| v11.2.2  | 2025-11-28 | Upgraded to v11.2.2; emoji directory tree; full STAC/DCAT/PROV-O alignment.          |
| v11.1.0  | 2025-11-10 | Initial air-quality governance directory established.                                |

---

### ⚖ FAIR+CARE & Governance Footer

This document:

- complies with **KFM-MDP v11.2.6**, **KFM-STAC v11**, **KFM-DCAT v11**, and **KFM-PROV v11**  
- is governed by the **FAIR+CARE Council** and **Reliability Engineering**, with co-review by the Governance Council  
- must be updated when:
  - new air-quality sources are added  
  - API versions change materially  
  - governance, telemetry, or provenance rules are updated

Edits require approval from the FAIR+CARE Council and Reliability Engineering and must pass
`markdown-lint`, `schema-lint`, `footer-check`, air-quality ETL tests, and telemetry validation workflows.

<br/>

<sub>© Kansas Frontier Matrix · CC-BY 4.0 · Diamond⁹ Ω / Crown∞Ω · Aligned with KFM‑MDP v11.2.6</sub>

<br/>

<div align="center">

🌫️ **Kansas Frontier Matrix — Air Quality Sources & API Governance v11.2.6**  
Deterministic Ingestion · STAC/DCAT/PROV Aligned · FAIR+CARE Stewardship  

[📘 Docs Root](../../README.md) · [📊 Data Docs Index](../README.md) · [🌫 Air-Quality Index](./README.md) · [⚖ Governance Charter](../../standards/governance/ROOT-GOVERNANCE.md)

</div>