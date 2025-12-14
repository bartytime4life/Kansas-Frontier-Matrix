---
title: "🌱 Kansas Frontier Matrix — NASIS & Soil Data Access (SDA) Integration Reference"
path: "docs/data/soils/nasis-sda/README.md"

version: "v11.2.6"
last_updated: "2025-12-13"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Soils & Agronomy Council · FAIR+CARE Oversight"
content_stability: "stable"

status: "Active / In-Repo Canonical"
doc_kind: "Reference Guide"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles: []

intent: "authoritative-soil-metadata-and-lineage"
audience:
  - "Soils & Agronomy"
  - "Data Engineering"
  - "Catalog + Provenance Engineering"
  - "Governance + Stewardship"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

scope:
  domain: "soils"
  applies_to:
    - "docs/data/soils/**"
    - "src/kfm/etl/soils/**"
    - "data/soils/**"
    - "data/stac/soils/**"
    - "data/dcat/soils/**"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
classification: "Public"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
jurisdiction: "Kansas / United States"

indigenous_rights_flag: true
data_steward: "Soils & Agronomy Council · FAIR+CARE Oversight"

commit_sha: "<latest-commit-hash>"
signature_ref: "../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../releases/v11.2.6/sbom.spdx.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

doc_uuid: "urn:kfm:doc:data:soils:nasis-sda:v11.2.6"
semantic_document_id: "kfm-soils-nasis-sda-v11.2.6"
event_source_id: "ledger:kfm:doc:data:soils:nasis-sda:v11.2.6"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "metadata-extraction"
  - "layout-normalization"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "fabricating lineage or dataset relationships"
  - "governance-override"
---

<div align="center">

# 🌱 **NASIS & Soil Data Access (SDA) — KFM Integration Reference**
`docs/data/soils/nasis-sda/README.md`

**Purpose**  
Define how **NRCS NASIS** and **Soil Data Access (SDA)** tabular datasets are **governed, extracted, versioned, and mapped**
into the Kansas Frontier Matrix (KFM). This is the in-repo canonical reference for deterministic soils ETL pipelines, STAC/DCAT
catalogs, and PROV-O lineage graphs.

<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/STAC%2FDCAT%2FPROV-Aligned-brightgreen" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Canonical-brightgreen" />

</div>

---

## 📘 Overview

This document defines **how NRCS NASIS and SDA datasets are governed, extracted, versioned, and mapped** into KFM.

Scope includes:

- NASIS table and column metadata (treated as “schema law” inside KFM)
- SDA SQL-over-HTTP query mechanics (tabular extraction surface)
- Deterministic identifiers and version anchors (reproducibility + safe diffing)
- Provenance and drift-tracking strategies (PROV-O + optional ledgers)
- Mapping patterns into KFM catalog (STAC/DCAT) and graph (Neo4j) layers

---

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 📁 data/
    └── 📁 soils/
        └── 📁 nasis-sda/
            └── 📄 README.md                          — This reference (canonical)

📁 src/
└── 📁 kfm/
    └── 📁 etl/
        └── 📁 soils/
            ├── 📄 README.md                          — Soils ETL module README (implementation-facing)
            └── …                                     — Ingest/normalize/catalog/provenance emitters

📁 data/
└── 📁 soils/
    ├── 📁 raw/
    │   └── 📁 nasis-sda/                              — Raw SDA pulls (JSON/CSV/JSONL; query/window scoped)
    └── 📁 processed/
        ├── 📁 ssurgo/                                — Normalized partitions (Parquet; stable paths)
        └── 📁 gnatsgo/                               — Normalized partitions (Parquet; stable paths)

📁 data/
├── 📁 stac/
│   └── 📁 soils/                                     — STAC collections/items for soils datasets
└── 📁 dcat/
    └── 📁 soils/                                     — DCAT dataset/distributions for soils datasets

📁 reports/
└── 📁 soils/                                         — Validation reports, drift summaries, audit bundles
~~~

---

## 🧭 Context

### Authoritative source systems

#### NRCS NASIS (National Soil Information System)

NASIS is the authoritative soil survey database maintained by NRCS, defining:

- Official soil components, horizons, and interpretations
- Controlled vocabularies, domains, and choice lists
- Internal identifiers used by SDA

KFM treats NASIS metadata references as **schema law**: they are not inferred heuristically.

#### Soil Data Access (SDA)

SDA provides read-only public access to NASIS tabular and spatial data via SQL-over-HTTP:

- REST endpoint: `post.rest`
- SQL-compatible query interface
- JSON/XML outputs with stable column names
- Survey-area–scoped exports and version fields (critical for reproducibility)

KFM uses SDA as the primary extraction surface for tabular soils ETL pipelines.

### Deterministic flow (conceptual)

~~~text
SDA SQL → Structured Extract
→ Schema Validation (NASIS metadata parity)
→ Deterministic Normalization + Partitioning
→ STAC Collections/Items
→ DCAT Dataset/Distributions
→ PROV-O Lineage (and optional OpenLineage)
→ Neo4j soils graph
~~~

---

## 📦 Data & Metadata

### Deterministic identifiers

KFM soils pipelines rely on stable anchors to ensure replayability and safe diffing.

Record-level identifiers (examples):

- `nasiscoiid` — NASIS component internal ID
- `nasischiid` — NASIS horizon internal ID

These SHOULD be persisted into:

- STAC Item properties (as identifiers or in `properties.kfm:*`)
- DCAT distributions (as part of provenance/identifier metadata)
- Neo4j node IDs (stable `urn:kfm:*` identifiers)

### Survey/export version anchors

Fields commonly used as “snapshot boundaries” (availability varies by extract/table):

- `tabnasisexportdate`
- `satabularver`

These anchors MUST be carried in:

- provenance metadata (PROV-O entity attributes)
- drift and reconciliation reports
- incremental update detection logic (CDC windows + export versions)

### Governance classification

This reference is classified as:

- `classification: Public`
- `sensitivity: General (non-sensitive; auto-mask rules apply)`
- `care_label: Public · Low-Risk`

Interpretation layers or sensitive overlays (if any) require additional governance and may change downstream handling.

---

## 🧱 Architecture

### SDA query mechanics (integration expectations)

- Queries are issued to SDA using SQL-over-HTTP (SDA `post.rest`).
- Queries SHOULD be parameterized and recorded (query text hash + window bounds).
- Responses MUST be treated as raw source entities in provenance.

Recommended extraction practice:

- query-by-window for incremental pulls (CDC-like semantics),
- deterministic paging and stable ordering,
- raw snapshot persistence before any normalization.

### Drift tracking strategy (minimum viable)

- Persist raw extracts per window (or per export version).
- Normalize deterministically and compute checksums per partition.
- Compare checksums and/or row-level keys between runs.
- Emit a drift summary report to `reports/soils/` and link it from provenance.

### Neo4j mapping (reference-level)

Recommended entity types:

- `:SoilComponent` (keyed by stable NASIS component ID)
- `:SoilHorizon` (keyed by stable NASIS horizon ID)
- `:SurveyArea` (areasymbol + export anchors)
- `:DatasetSnapshot` (tabular export version anchors)
- `:ExtractionActivity` (SDA extraction job)

Recommended relations:

- `(:DatasetSnapshot)-[:WAS_DERIVED_FROM]->(:DatasetSnapshot)` (export lineage)
- `(:ExtractionActivity)-[:USED]->(:DatasetSnapshot|:SchemaReference)`
- `(:SoilHorizon)-[:PART_OF]->(:SoilComponent)`
- `(:SoilComponent)-[:IN_SURVEY_AREA]->(:SurveyArea)`

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC alignment (reference)

- Collections represent dataset families and/or survey-area-scoped products (e.g., SSURGO, gNATSGO).
- Items represent extract units (by table/window, by export version, or by partition policy).
- Properties SHOULD include:
  - stable NASIS identifiers (where relevant)
  - export version anchors (`tabnasisexportdate`, `satabularver` where available)
  - deterministic pipeline version metadata (`kfm:algorithm_version`, `kfm:code_commit_sha`)

### DCAT alignment (reference)

- `dcat:Dataset` represents a soils dataset family or product (SSURGO, gNATSGO).
- `dcat:distribution` entries represent extract artifacts (raw snapshots, normalized Parquet, GeoPackage, etc.).
- `dct:provenance` MUST reference provenance summaries for extraction + normalization activities.

### PROV-O alignment (minimum)

- `prov:Activity`: SDA extraction job (and any normalization/partitioning job)
- `prov:Entity`: raw extract snapshot; processed normalized partitions; catalog records
- `prov:used`: activity used SDA query + schema reference + upstream snapshot
- `prov:wasGeneratedBy`: artifacts generated by extraction/transform activities
- `prov:wasDerivedFrom`: processed artifacts derived from raw extracts (and prior export versions when applicable)

---

## 🧠 Story Node & Focus Mode Integration

This reference supports Story Nodes by providing:

- stable identifiers and version anchors for traceable soil narratives,
- explicit provenance expectations (no “mystery joins”),
- governance constraints on interpretation layers.

Focus Mode MAY summarize this document and extract metadata fields, but MUST NOT invent schema fields, lineage, or policy.

---

## 🧪 Validation & CI/CD

Automated checks expected for governed soils pipelines and catalog outputs include:

- NASIS schema parity validation (required columns, types, domains where applicable)
- SDA column completeness checks
- Domain/choice-list preservation (no lossy remapping)
- PROV-O integrity (required fields present; correct linkage)
- STAC validation (collection + item validity; required KFM properties)
- Drift detection (checksum/key deltas; flagged thresholds)

All checks are enforced by KFM CI pipelines prior to merge.

---

## ⚖ FAIR+CARE & Governance

Soils data is governed under:

- FAIR principles (Findable, Accessible, Interoperable, Reusable)
- CARE principles where Indigenous lands or culturally sensitive contexts intersect with interpretation layers

Enforcement posture:

- No speculative soil interpretations in governed outputs
- No reinterpretation of NRCS taxonomic meaning
- Respect land-use sensitivity flags and Indigenous sovereignty policies when applicable

---

## 🕰️ Version History

| Version | Date       | Notes |
|-------:|------------|------|
| v11.2.6 | 2025-12-13 | Initial governed NASIS/SDA integration reference (canonical in-repo) |

---

<div align="center">

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Canonical-brightgreen" />

[📚 Data Documentation Index](../../README.md) ·
[🌱 Soils Data Docs](../README.md) ·
[🏗️ Data Architecture](../../../architecture/data/README.md) ·
[🏛️ Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC‑BY 4.0

</div>
