---
title: "🌫️ Kansas Frontier Matrix — Harmonized Air Quality Ingestion & Correction Pipeline"
path: "docs/data/air-quality/harmonized-ingestion.md"
version: "v11.2.6"
last_updated: "2025-12-12"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council · Reliability Engineering"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Pipeline Design & Governance Standard"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

intent: "air-quality-harmonization"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

scope:
  domain: "air-quality"
  applies_to:
    - "docs/data/air-quality/**"
    - "data/sources/air-quality/**"
    - "data/processed/air-quality/**"
    - "data/stac/air-quality/**"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"

indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

commit_sha: "<latest-commit-hash>"
provenance_chain:
  - "docs/data/air-quality/harmonized-ingestion.md@v11.2.6"

doc_uuid: "urn:kfm:doc:data:air-quality:harmonized-ingestion:v11.2.6"
semantic_document_id: "kfm-air-quality-harmonized-ingestion-v11.2.6"
event_source_id: "ledger:kfm:doc:data:air-quality:harmonized-ingestion:v11.2.6"
doc_integrity_checksum: "<sha256>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
  - "layout-normalization"

ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
---

# 🌫️ Harmonized Air Quality Ingestion & Correction Pipeline

**Purpose**  
Define the canonical KFM pipeline for ingesting, correcting, aggregating, and publishing daily-standardized air quality observations from authoritative regulatory sources and dense low-cost sensor networks.

---

## 📘 Overview

This standard defines a **deterministic, version-pinned, provenance-complete** workflow for producing harmonized daily air quality datasets suitable for:

- regulatory-aligned analysis and baselines
- high-resolution spatial modeling
- Story Nodes and Focus Mode narratives
- long-term climate, health, and equity studies

### Normative guarantees

- **Raw data is preserved** (never overwritten).
- **Corrections are versioned** (algorithm + version + parameters are explicit).
- **Daily harmonization is reproducible** (config-driven; deterministic replay).
- **Every published daily product is lineage-complete** (PROV-O chain from raw → corrected → aggregated → published).

---

## 🗂️ Directory Layout

~~~text
docs/
├── 📁 data/
│   └── 📁 air-quality/
│       ├── 📄 harmonized-ingestion.md                 — This pipeline standard
│       └── 📄 README.md                               — Air quality domain index (recommended)
data/
├── 📁 sources/
│   └── 📁 air-quality/
│       ├── 📁 aqs/                                    — Raw AQS pulls + source manifests
│       └── 📁 purpleair/                               — Raw PurpleAir pulls + source manifests
├── 📁 processed/
│   └── 📁 air-quality/
│       ├── 📁 corrected/                               — Corrected sensor outputs (daily)
│       └── 📁 harmonized/                              — Harmonized daily products (multi-source)
└── 📁 stac/
    └── 📁 air-quality/
        ├── 📄 collection.json                          — STAC Collection (air quality)
        └── 📁 items/                                   — Daily STAC Items (one per day)
mcp/
└── 📁 runs/
    └── 📁 air-quality/
        └── 📁 <run-id>/                                — Config snapshot + logs + telemetry
src/
└── 📁 pipelines/
    └── 📁 air-quality/
        ├── 📁 configs/                                 — Version-pinned pipeline configs
        ├── 📁 corrections/                              — Correction specs + algorithm IDs
        └── 📄 pipeline.py                               — Deterministic orchestrator
schemas/
└── 📁 air-quality/
    ├── 📄 observations.schema.json                     — Harmonized observation schema
    └── 📄 telemetry.schema.json                         — Completeness/dropout/variance telemetry
tests/
└── 📁 air-quality/
    └── 📄 test_harmonized_ingestion.py                 — Unit + contract tests
~~~


## 🧭 Context

This pipeline harmonizes measurements from two classes of sources:

### 🏛️ Regulatory monitors (authoritative)

- **EPA Air Quality System (AQS)**
  - regulatory-grade instruments
  - daily summary statistics (baseline for compliance and trend analysis)
  - authoritative site metadata (e.g., monitor type, method codes, QA context)

### 🧭 Dense sensor networks (high-density, bias-prone)

- **PurpleAir** (low-cost PM sensors)
  - high spatial density and high temporal resolution
  - known biases requiring correction and explicit uncertainty handling

### Optional augmentation (context, not authority)

- **AirNow** (near-real-time indices for situational awareness)
- **CAMS NRT** (regional atmospheric context)

---

## 🧱 Architecture

### Deterministic processing stages

1. **Raw ingest**
   - ingest AQS daily summaries
   - ingest PurpleAir high-frequency feeds (as published)
   - store raw artifacts and record a source manifest (license/rights, retrieval date, checksums)

2. **Sensor correction (post-ingest)**
   - apply versioned correction logic to low-cost sensor fields
   - write corrected outputs as new derived artifacts (raw remains immutable)

3. **Temporal harmonization**
   - aggregate corrected sensor observations into **daily values**
   - generate completeness + confidence telemetry for each daily aggregate

4. **Daily harmonized product assembly**
   - produce a multi-source daily dataset (regulatory + corrected sensor)
   - maintain explicit source attribution per measurement

5. **Catalog publish**
   - publish a **single STAC Item per day** with multi-asset packaging
   - mirror required catalog metadata as DCAT-compatible records

6. **Lineage encoding**
   - emit a PROV graph linking raw → corrected → aggregated → published
   - no published product is valid without a resolvable lineage chain

### Sensor correction governance (PM2.5)

- Correction formulas are **applied post-ingest**.
- Raw values are **never overwritten**.
- Corrected fields are explicitly versioned and attributable.

Required correction metadata (minimum):

~~~yaml
pm25_raw: <number>
pm25_corrected_<algorithm_id>_<version>: <number>
relative_humidity: <number>
correction_algorithm_id: <string>
correction_model_version: <string>
correction_parameters_hash: <string>
qc_flags: <array>
source_system: <string>
~~~


### Bias transparency (normative)

- Correction model version MUST be present for every corrected record.
- Known limitations (e.g., aerosol-type sensitivity: dust vs smoke) MUST be documented in metadata.
- Regional deviations SHOULD be tracked via telemetry annotations and retained with the daily product.

### Authority precedence (normative)

- Regulatory observations remain the **baseline reference** for compliance/trend.
- Dense sensors provide **supplemental spatial detail**, not regulatory authority.
- Where products combine sources, the harmonized record MUST preserve per-source identity and flags.

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Raw ingest: EPA AQS daily summary"] --> H["Daily harmonized product"]
  B["Raw ingest: PurpleAir high-frequency"] --> C["Sensor correction (versioned)"]
  C --> D["Daily aggregation (corrected sensors)"]
  D --> H
  H --> S["STAC Item (per day) + DCAT mirror"]
  S --> P["PROV lineage graph"]
~~~

This diagram shows the required stage ordering: raw ingestion is preserved, correction produces derived artifacts, daily aggregation harmonizes time, and publication emits STAC/DCAT outputs plus a PROV lineage chain.

---

## 📦 Data & Metadata

### Daily product expectations

Each daily harmonized product SHOULD provide:

- pollutant measurements (e.g., PM2.5) with units and method metadata
- per-source attribution (AQS vs corrected sensor)
- daily completeness metrics
- correction variance metrics (corrected vs raw deltas)
- QC flags (dropout, suspect values, missing RH, etc.)

### Required telemetry (minimum)

- data completeness (per day, per site/sensor)
- sensor dropout rate
- correction delta statistics (raw → corrected)
- daily aggregation confidence flags

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC (daily Item)

Each daily air quality product is published as a single STAC Item with:

- unified temporal extent (daily)
- spatial geometry aligned to the monitoring footprint (or the chosen representation policy)
- explicit processing indicators (e.g., processing level; correction algorithm identifiers)
- multiple assets, at minimum:

~~~yaml
assets:
  aqs_daily_summary: {}
  purpleair_raw_timeseries: {}
  purpleair_corrected_daily: {}
  harmonized_daily_product: {}
  prov_lineage: {}
~~~


### DCAT (mirror)

- The daily product MUST be representable as a DCAT dataset/distribution record.
- Dataset-level fields MUST include title, description, license, publisher/creator, temporal/spatial coverage, and access distribution links.

### PROV-O (lineage)

Every published daily Item MUST include a PROV graph encoding:

- raw ingestion activities
- correction algorithm execution
- temporal aggregation
- publishing/signing activity (when applicable)

Minimum PROV roles:

- **prov:Entity** — raw sensor feed, corrected dataset, aggregated daily dataset, published STAC Item
- **prov:Activity** — ingest, correction, aggregation, publish
- **prov:Agent** — pipeline runner, guidance/standard source, and responsible stewarding body

---

## 🧪 Validation & CI/CD

### Validation requirements

- schema validation for raw and processed records
- correction metadata completeness checks
- STAC Item validation for every published day
- PROV graph validation (required fields and resolvable chain)

### Failure handling (normative)

- partial days are **flagged, not dropped**
- deterministic replay is supported via stored raw feeds, config snapshots, and run logs
- regulatory baselines are never replaced by sensor inference

---

## ⚖ FAIR+CARE & Governance

- No individual-level exposure inference is permitted from these datasets.
- Indigenous and vulnerable community overlays are governed separately and MUST follow sovereignty policy constraints.
- Sensor density does not imply authority; all derived products MUST disclose source class and correction status.
- Corrections MUST be auditable, reversible, and transparently disclosed in metadata and lineage.

---

## 🧠 Story Node & Focus Mode Integration

This pipeline directly supports Story Nodes such as:

- wildfire smoke narratives and impacts
- urban vs rural exposure comparisons
- long-term particulate trends
- environmental justice Story Nodes

Narrative layers MUST reference cataloged STAC Items (and their provenance), not ad-hoc datasets.

---

## 🕰️ Version History

| Version | Date | Notes |
|---|---|---|
| v11.2.6 | 2025-12-12 | Governance alignment; deterministic stage ordering; versioned correction metadata; STAC/DCAT/PROV hard requirements; footer governance links. |

---

<div align="center">

🌫️ **Harmonized Air Quality Ingestion & Correction Pipeline**  
Deterministic Pipelines · Open Provenance · FAIR+CARE Governance

[📘 Docs Root](../../README.md) ·
[🌫️ Air Quality Domain Index](./README.md) ·
[🏛️ Governance Charter](../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC‑BY 4.0

</div>