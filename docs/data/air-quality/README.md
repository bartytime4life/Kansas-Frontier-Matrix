---
title: "🌫️ KFM v11.2.2 — Air Quality Sources & API Governance (OpenAQ v3 · AirNow · CAMS NRT · Diamond⁹ Ω / Crown∞Ω Certified)"
path: "docs/data/air-quality/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council & Reliability Engineering"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
signature_ref: "../../../releases/v11.2.2/signature.sig"
attestation_ref: "../../../releases/v11.2.2/slsa-attestation.json"

sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../releases/v11.2.2/air-quality-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/air-quality-sources-v11.2.2.json"
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
doc_uuid: "urn:kfm:doc:data:air-quality:index:v11.2.2"
semantic_document_id: "kfm-data-air-quality-index-v11.2.2"
event_source_id: "ledger:data-air-quality-index-v11.2.2"

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

# 🌫️ **KFM v11.2.2 — Air Quality Sources & API Governance**  
`docs/data/air-quality/README.md`

**Purpose**  
Provide the authoritative governance, validation, provenance, and STAC/DCAT metadata rules for all KFM air‑quality ingestion pipelines (OpenAQ v3, AirNow, CAMS NRT) across the full KFM pipeline:

**Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j graph → API → React/MapLibre/Cesium → Story Nodes → Focus Mode.** :contentReference[oaicite:0]{index=0}  

This document defines:

- Freshness gates and latency budgets  
- Schema‑drift and API‑lifecycle detection  
- Source‑version and run‑level provenance  
- STAC/DCAT/PROV alignment for air‑quality datasets  
- Reliability guardrails required for Diamond⁹ Ω / Crown∞Ω certification

[![KFM-MDP v11.2.6](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.6-informational)]() ·
[![STAC 1.0.0 · DCAT 3.0 · PROV-O](https://img.shields.io/badge/Metadata-STAC_1.0.0_%7C_DCAT_3.0_%7C_PROV--O-blue)]() ·
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold)]() ·
[![Status: Stable](https://img.shields.io/badge/Status-Stable_%2F_Governed-brightgreen)]()

</div>

---

## 📘 Overview

KFM is an open geospatial hub combining Kansas environmental, cultural, and historical data into an interactive map, timeline, and semantic graph with Focus Mode narratives.:contentReference[oaicite:1]{index=1}  Air‑quality data is a core environmental stream that must remain reliable under changing APIs, evolving scientific standards, and long‑term climate context.

This document governs all air‑quality ingestion and modeling that lands in:

- **data/sources/** manifests (source‑level metadata)  
- **data/stac/** Collections & Items for air‑quality assets (STAC 1.0.0):contentReference[oaicite:2]{index=2}  
- **data/catalog/** DCAT 3.0 dataset entries for API and file access:contentReference[oaicite:3]{index=3}  
- **src/graph/** Neo4j ingestion of air‑quality observables and forecasts (GeoSPARQL/OWL‑Time aligned):contentReference[oaicite:4]{index=4}  
- **src/api/** air‑quality query endpoints  
- **src/web/** air‑quality visualizations (MapLibre / Cesium) and Focus Mode story nodes:contentReference[oaicite:5]{index=5}  

All rules here are binding for:

- **OpenAQ v3** — community air‑quality observations  
- **AirNow** — US EPA preliminary & official observations  
- **CAMS NRT** — Copernicus Near‑Real‑Time atmospheric composition forecasts  

and any derived, fused, or regridded datasets referencing these sources.

---

## 🗂️ Directory Layout

This section describes only the governance subtree under `docs/data/air-quality/`. Runtime configs and code paths are referenced in later sections.

~~~text
docs/data/air-quality/
├── README.md                              # This governance & alignment document (you are here)
│
├── sources/                               # Per-source governance specs (human-readable)
│   ├── openaq-v3.md                       # OpenAQ v3 migration, fields, backfill rules
│   ├── airnow.md                          # AirNow prelim/official flags, status semantics
│   └── cams-nrt.md                        # CAMS NRT forecast cycles and validation windows
│
├── stac/                                  # STAC metadata templates for air-quality datasets
│   ├── collections/
│   │   ├── openaq.json                    # STAC Collection: OpenAQ v3 (observations)
│   │   ├── airnow.json                    # STAC Collection: AirNow (US EPA)
│   │   └── cams-nrt.json                  # STAC Collection: CAMS NRT (forecasts)
│   └── items/
│       └── template-item.json             # STAC Item template (source_version-tagged)
│
├── ingestion/                             # Normative ingestion configuration examples
│   ├── openaq-v3-config.yaml              # OpenAQ v3 ingestion/freshness policy template
│   ├── airnow-config.yaml                 # AirNow freshness-gate & status-mapping rules
│   └── cams-nrt-config.yaml               # CAMS cadence-aware polling & backfill rules
│
└── governance/                            # Cross-source governance primitives
    ├── freshness-gates.md                 # Freshness & latency budgets per provider
    ├── api-lifecycle-tracking.md          # API versioning & retirement policy
    └── provenance-schema.json             # PROV-O/DCAT extensions for air-quality workflows
~~~

> **Runtime code & configs (design requirement)**  
> - ETL code for air‑quality **MUST** live under: `src/pipelines/atmo/air-quality/` (per‑source modules).  
> - Machine‑readable ingestion configs **SHOULD** be stored under: `src/pipelines/atmo/air-quality/config/`.  
> - The files under `docs/data/air-quality/ingestion/` are the **governed templates** that CI validates against and that configs must conform to (via schema checks and golden‑file tests).:contentReference[oaicite:6]{index=6}  

---

## 🧭 Context

### Scope of This Directory

This directory governs:

- **API lifecycle tracking** for OpenAQ v3, AirNow, CAMS NRT (new versions, deprecations, retires)  
- **Freshness & latency gates** for all air‑quality pipelines  
- **Schema‑drift detection** and WAL‑safe ingestion fallbacks:contentReference[oaicite:7]{index=7}  
- **Status semantics and quality tiers** (“preliminary”, “unverified”, “validated”, “forecast”)  
- **STAC/DCAT/PROV baselines** for all air‑quality datasets  
- **Drift & outage labeling** that flows into the Neo4j graph and Focus Mode narratives:contentReference[oaicite:8]{index=8}  

It does **not** define implementation details of the ETL code itself; instead it constrains what that code is allowed to do and how it must expose metadata and telemetry.

### Responsibilities

This directory is responsible for:

- Publishing **source‑specific governance docs** (`sources/*.md`)  
- Maintaining **STAC Collection & Item templates** for each provider  
- Defining **canonical DCAT 3.0 mappings** for each API / dataset pair:contentReference[oaicite:9]{index=9}  
- Defining **PROV‑O patterns** for air‑quality ETL and fusion steps (Entities, Activities, Agents):contentReference[oaicite:10]{index=10}  
- Documenting **freshness, cadence, and fallback policies**  

All downstream code (ETL, graph, API, web) is expected to treat these files as **contracts**; CI enforces that expectation.

---

## 📦 Data & Metadata

### Source Governance Summary

#### 🟦 OpenAQ v3 — Mandatory v3 Migration

- Legacy OpenAQ v1/v2 endpoints are considered **retired** as of **2025‑01‑31**; ingestion MUST use v3 only.  
- Allowed endpoints (configurable per pipeline, but default set):  
  - `/v3/locations` — station metadata, instruments, coordinates  
  - `/v3/latest` — latest per‑station readings  
  - `/v3/measurements` — full historical measurements  
- Each STAC Item **MUST** include:  
  - `properties.source_id` — stable OpenAQ location/measurement identifier  
  - `properties.source_version = "OpenAQ-v3"`  
  - `properties.api_base_url` — base path used during extract  
- DCAT Dataset for OpenAQ is modeled as a **dataset series** of daily materialized snapshots (one DCAT Dataset per snapshot, linked via `dcat:inSeries`).:contentReference[oaicite:11]{index=11}  

#### 🟧 AirNow — Preliminary vs Official Modes

- All AirNow data is treated as **preliminary** unless provider metadata marks it as official/validated.  
- Freshness gating is mandatory: ingestion MUST enforce maximum age windows for “near‑real‑time” products; older data is still ingested but flagged as **stale**.  
- Public AirNow fact‑sheet timestamps (last updated / methodology) MUST be recorded in provenance as a PROV Entity linked via `prov:hadPrimarySource`.:contentReference[oaicite:12]{index=12}  
- Missing data in a time window MUST be modeled as **“unverified interval”**, not as an outage, unless explicit outage signals are present from the provider.

#### 🟩 CAMS NRT — Cadence‑Aware Forecasts

- CAMS NRT ingestion is **cadence‑driven**, not fixed‑interval polling. Pipelines must respect documented forecast cycles.  
- Each STAC Item for CAMS NRT MUST include:  
  - `properties.forecast_cycle` — e.g. `"2025-06-01T00:00Z"`  
  - `properties.validation_window` — time interval where the forecast is considered valid  
  - `properties.source_version` — e.g. `"CAMS-NRT-vX.Y"`  
- DCAT Dataset entries are modeled as a **DatasetSeries** of forecast cycles, with each cycle a Dataset that has Distributions for NetCDF/GRIB/GeoTIFF slices.:contentReference[oaicite:13]{index=13}  

### STAC / DCAT Baseline (All Sources)

For every air‑quality dataset:

- **STAC**  
  - One **Collection** per provider (`openaq`, `airnow`, `cams-nrt`).:contentReference[oaicite:14]{index=14}  
  - Items must be valid STAC 1.0.0 GeoJSON Features with `geometry`, `bbox`, `datetime`, and `properties` including:  
    - `properties.kfm:run_id` — stable ETL run identifier (for PROV linkage)  
    - `properties.kfm:quality_tier` — one of `preliminary|unverified|validated|forecast`  
    - `properties.kfm:source_handle` — `openaq-v3|airnow|cams-nrt`  

- **DCAT 3.0**  
  - One **Dataset** per materialized logical product (e.g. “OpenAQ Observations — Daily Snapshot YYYY‑MM‑DD”).  
  - `dcat:DataService` entries for each upstream API (`openaq-api`, `airnow-api`, `cams-api`) with `dcat:servesDataset` relations.:contentReference[oaicite:15]{index=15}  
  - Each Distribution must include:  
    - `dcat:downloadURL` or `dcat:accessURL`  
    - `dcat:mediaType` (e.g. `application/json`, `application/x-netcdf`)  
    - `spdx:checksum` using SHA‑256, aligning with KFM SBOM and integrity policy.:contentReference[oaicite:16]{index=16}  

---

## 🧱 Architecture

This section ties the air‑quality governance to the KFM end‑to‑end pipeline.:contentReference[oaicite:17]{index=17}  

### ETL → STAC/DCAT/PROV

Design requirements:

- **ETL location**  
  - OpenAQ v3 pipeline module: `src/pipelines/atmo/air-quality/openaq_v3.py` (name illustrative but MUST live under this directory).  
  - AirNow pipeline module: `src/pipelines/atmo/air-quality/airnow.py`  
  - CAMS NRT pipeline module: `src/pipelines/atmo/air-quality/cams_nrt.py`  

- **Config‑driven & deterministic**  
  - Each pipeline reads from a YAML config in `src/pipelines/atmo/air-quality/config/` that mirrors the governed template in `docs/data/air-quality/ingestion/`.  
  - All randomness (sampling, backoff jitter) MUST use seeded RNGs recorded in run‑level PROV metadata, consistent with MCP’s deterministic‑pipeline guidance.  

- **Provenance modeling (PROV‑O)**:contentReference[oaicite:19]{index=19}  
  - Source API calls are modeled as `prov:Activity` instances (e.g. `openaq_v3_pull_2025-06-01T00Z`).  
  - Raw responses are `prov:Entity` objects, linked via `prov:wasGeneratedBy` to the pull Activity and `prov:wasAttributedTo` the remote provider Agent.  
  - Transform + load steps are separate Activities; derived STAC Items are Entities with explicit `prov:wasDerivedFrom` links to raw Entities.  
  - The ETL runner (e.g. `kfm-air-quality-etl` service) is a `prov:SoftwareAgent`; human maintainers are `prov:Person` Agents.

- **Catalog integration**  
  - STAC JSON is written under `data/stac/atmo/air-quality/` and must pass KFM’s STAC validation pipeline.:contentReference[oaicite:20]{index=20}  
  - DCAT metadata is generated or updated under `data/catalog/atmo/air-quality/` according to the DCAT guide.:contentReference[oaicite:21]{index=21}  

### Graph → API → UI

- **Neo4j graph**  
  - Air‑quality observations are modeled as time‑indexed nodes (e.g. `:AirQualityObservation`) linked to `:Location` nodes with GeoSPARQL geometries (point, polygon).:contentReference[oaicite:22]{index=22}  
  - Forecast grid cells can use either explicit geometries or DGGS identifiers (H3) for efficient querying.  

- **API layer**  
  - Read‑only APIs under `src/api/air-quality/` expose:  
    - Observation queries (by location, time, pollutant, source).  
    - Forecast queries (by horizon, pollutant, scenario).  
    - Metadata endpoints for freshness and status.  

- **Frontend**  
  - `src/web/` uses MapLibre / Cesium to visualize air‑quality layers on KFM’s map/timeline, reusing existing historical and environmental context layers.  

---

## 🧠 Story Node & Focus Mode Integration

KFM’s Focus Mode and Story Nodes are built on the knowledge graph and source metadata, not directly on raw API responses.:contentReference[oaicite:24]{index=24}  

Design constraints:

- Story Nodes summarizing air‑quality events (e.g. “Smoke episode over northeast Kansas, July 2035”) MUST:  
  - Reference underlying STAC Items and DCAT Datasets as **facts**.  
  - Use provenance to distinguish observed vs forecast vs preliminary data.  
  - Explicitly label uncertainty when forecasts and observations disagree (interpretation, not fact).  

- Narrative generation **MUST NOT**:  
  - Infer health outcomes or policy recommendations beyond the data.  
  - Attribute causes of poor air quality (e.g. “caused by specific facility”) unless backed by explicit data and governance‑approved models.  

- For Indigenous and local communities, Focus Mode must avoid tying air‑quality narratives to sensitive cultural sites or sacred locations except at generalized spatial scales (e.g. county or H3 grid), honoring CARE and KFM sovereignty policies.  

---

## 🧪 Validation & CI/CD

Air‑quality pipelines participate fully in KFM’s CI/CD architecture.  

### CI Checks

GitHub Actions (see `.github/workflows/kfm-ci.yml`) must include, for every change touching air‑quality code or governance:

- **Schema validation**  
  - YAML configs: JSON Schema + semantic checks (e.g. source handles, quality tiers).  
  - STAC JSON templates: STAC 1.0.0 validation.:contentReference[oaicite:27]{index=27}  
  - DCAT JSON: SHACL shapes for DCAT 3.0 profiles.:contentReference[oaicite:28]{index=28}  

- **Static analysis & tests**  
  - Unit tests for extraction, transformation, and status mapping logic.  
  - Integration tests against mocked API responses (contract tests).  
  - Golden‑file tests: sample runs must emit STAC & DCAT artifacts that match governance templates.

- **Security & supply‑chain checks**  
  - Dependency scanning and SBOM validation for ETL and API code.  
  - No secrets or API keys committed to configs or docs (enforced by secret scanners).

### Drift & Freshness Monitoring

Daily scheduled jobs (implemented as CI workflows plus runtime monitors):

- **API health & schema drift**  
  - Check for response shape changes vs expected JSON Schema; raise alerts on drift.  
  - Track HTTP status codes and latency distributions; log to OpenTelemetry.:contentReference[oaicite:30]{index=30}  

- **Freshness & latency gates**  
  - For each provider, compute lag between “expected latest” and “last successful observation” and classify into: `ok | warning | critical`.  
  - Emit results into `air-quality-telemetry.json` (referenced in front‑matter) and the KFM telemetry schema.  

- **Fallback behavior**  
  - When gates fail, pipelines MUST:  
    - Switch to most recent stable historical data where appropriate.  
    - Flag derived datasets as “degraded” in STAC/DCAT metadata.  
    - Avoid silently dropping data; gaps must be explicitly modeled.  

---

## 🌐 STAC, DCAT & PROV Alignment

This section summarizes how the STAC, DCAT, and PROV standards are combined for air‑quality in KFM.  

- **STAC**  
  - STAC Collections describe each provider’s dataset, including spatial/temporal extents and licenses.  
  - STAC Items represent individual observation or forecast “tiles” in space‑time.  
  - `links` arrays connect Items → Collections and to associated DCAT / PROV resources.

- **DCAT 3.0**  
  - DCAT Datasets describe logical datasets (daily snapshots, forecast cycles).  
  - DCAT Distributions describe accessible forms (files, APIs, tiles).  
  - `dcat:DataService` entries point to upstream APIs and internal KFM APIs.:contentReference[oaicite:32]{index=32}  

- **PROV‑O**  
  - PROV Entities are mapped to:  
    - Raw API payloads  
    - Processed STAC Items  
    - DCAT Distributions  
  - PROV Activities capture ETL runs, resampling, aggregation, and fusion steps.  
  - PROV Agents capture providers (OpenAQ, EPA / AirNow, CAMS), KFM ETL services, and maintainers.:contentReference[oaicite:33]{index=33}  

Together, these standards allow external tools and internal Focus Mode to trace **where air‑quality data came from, how it was processed, and how trustworthy it is**.

---

## ⚖ FAIR+CARE & Governance

While air‑quality data is marked as **Public · Low‑Risk**, KFM still applies FAIR+CARE and sovereignty principles.  

- **FAIR**  
  - **Findable** — All STAC and DCAT records must have stable URIs, descriptive titles, and keywords.  
  - **Accessible** — Public endpoints documented with rate‑limit and usage notes.  
  - **Interoperable** — STAC 1.0.0, DCAT 3.0, PROV‑O, GeoSPARQL, OWL‑Time.  
  - **Reusable** — License fields recorded at both Collection/Dataset level and Distribution level (typically CC‑BY or public domain, depending on provider terms).

- **CARE & Sovereignty**  
  - Even though air‑quality is non‑sensitive, overlays with Indigenous lands or sensitive ecological sites must honor the **Indigenous Data Protection** standard (e.g. generalizing exact boundaries when displayed).  
  - Any cross‑linking between air‑quality datasets and explicitly Indigenous datasets must be reviewed by the FAIR+CARE Council.

- **Energy & Carbon Telemetry**  
  - ETL and heavy processing workloads MUST record energy and carbon metrics into the referenced telemetry schemas (`energy-v2`, `carbon-v2`) to support sustainable operations.  

---

## 🕰️ Version History

| Version | Date       | Notes                                                                                              |
|---------|------------|----------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025‑11‑28 | Air‑quality governance stabilized; STAC/DCAT/PROV alignment; OpenAQ v3 mandatory; this doc aligned to KFM‑MDP v11.2.6 layout and heading profiles. |
| v11.1.0 | 2025‑11‑10 | Initial air‑quality governance directory established (OpenAQ, AirNow, CAMS NRT) with basic freshness and API lifecycle tracking. |

---

<div align="center">

### 🔗 Footer  

[🏠 KFM Home](../../README.md) ·  
[📚 Standards Index](../../standards/README.md) ·  
[⚖ ROOT Governance](../../standards/governance/ROOT-GOVERNANCE.md) ·  
[🤝 FAIR+CARE Guide](../../standards/faircare/FAIRCARE-GUIDE.md) ·  
[🪶 Indigenous Data Protection](../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·  
[🔐 Security Policy](../../security/SECURITY.md) ·  
[📝 Markdown Protocol v11.2.6](../../standards/kfm_markdown_protocol_v11.2.6.md) ·  
[📦 STAC Catalog Root](../../data/stac/)

</div>
