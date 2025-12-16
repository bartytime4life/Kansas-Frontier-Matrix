---
title: "🌐 KFM — Air Quality STAC Folder"
path: "data/air-quality/stac/README.md"

version: "v11.2.6"
last_updated: "2025-12-16"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Data Architecture Board · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Canonical"
doc_kind: "Folder README"
header_profile: "standard"
footer_profile: "standard"
intent: "air-quality-stac-folder-overview"

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
    - "data/air-quality/stac/**"
    - "data/air-quality/**"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"

indigenous_rights_flag: true
owner: "KFM Core · Data Engineering"
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by a later governed revision"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"

immutability_status: "mutable-plan"
doc_uuid: "urn:kfm:doc:data:air-quality:stac:readme:v11.2.6"
semantic_document_id: "kfm-air-quality-stac-readme"
event_source_id: "ledger:kfm:doc:data:air-quality:stac:readme:v11.2.6"
doc_integrity_checksum: "<sha256>"

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
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

provenance_chain:
  - "docs/standards/kfm_markdown_protocol_v11.2.6.md@v11.2.6"
---

# 🌐 KFM — Air Quality STAC Folder

> **Purpose**  
> Store **STAC Catalog / Collection / Item** JSON for Air Quality datasets so they can be validated, versioned, and discovered consistently across KFM’s ETL → catalog → graph → API → UI workflow.

## 📘 Overview

This folder contains **metadata-first** STAC artifacts for the Air Quality domain.

What belongs here:

- STAC JSON objects (Catalogs, Collections, Items)
- Optional run artifacts referenced by STAC assets (e.g., QA reports, telemetry PROV JSON‑LD)

What does **not** belong here:

- raw data payloads (place those under `data/raw/**` or `data/processed/**`)
- secrets or credentials
- ungoverned “scratch” catalogs without validation and provenance notes

## 🗂️ Directory Layout

~~~text
📁 data/air-quality/stac/                       — Domain STAC (air-quality)
├── 📄 README.md                                — This file
├── 🧾 catalog.json                             — (optional) domain root Catalog
├── 📁 collections/                             — STAC Collections (group related items)
│   └── 📁 <collection_id>/                     — One folder per collection
│       └── 🧾 collection.json                  — Collection metadata (extent, license, summaries)
├── 📁 items/                                   — STAC Items (dataset granules / stations / products)
│   └── 📁 <collection_id>/                     — Items organized by collection
│       └── 🧾 <item_id>.json                   — Item (GeoJSON Feature + assets + properties)
└── 📁 assets/                                  — (optional) local assets referenced by Items
    └── 📁 telemetry/                           — (optional) run telemetry + PROV JSON‑LD
~~~

## 🧭 Context

KFM treats STAC as a **primary schema** for spatio‑temporal asset discovery and validation, while DCAT and PROV‑O provide broader catalog interoperability and lineage.

In the pipeline:

- ETL jobs write or update STAC Items/Collections here (or to an artifact store)
- Validators ensure conformance before promotion/publishing
- Catalog + provenance metadata becomes ingestible into the knowledge graph and API layers

## 🧪 Validation & CI/CD

Minimum expectations for Air Quality STAC artifacts:

- STAC JSON must be valid and stable (no non-deterministic fields without explicit versioning)
- Item identifiers are stable and do not change across runs unless versioned
- Any geometry/footprint for sensitive locations follows governance decisions

Recommended checks:

- STAC schema validation (offline-capable if extensions are referenced by URL)
- Minimal QA: bbox/geometry consistency; datetime coverage sanity
- Governance alignment: license/constraints consistent with `data/air-quality/governance/**`

## 📦 Data & Metadata

### Minimum STAC Item expectations (practical)

A STAC Item should include (at minimum):

- `stac_version`
- `id`
- `type: "Feature"`
- `geometry` + `bbox` (or `geometry: null` for non-spatial doc-only items)
- `properties.datetime` **or** `properties.start_datetime` + `properties.end_datetime`
- `assets` with stable `href` links

If the air-quality asset is a time series or station-based product, ensure the Item’s temporal properties reflect the covered period (not merely the ingest time).

### Naming and stability

Recommended stability rules:

- `collection_id` reflects the upstream dataset family (stable over time)
- `item_id` reflects a stable upstream identifier (station id, product id, or a versioned id)
- Any breaking change to Item semantics should create a new versioned Item and link via versioning metadata (per KFM versioning practice)

## 🌐 STAC, DCAT & PROV Alignment

### STAC ↔ DCAT

Recommended mapping approach:

- Collection ↔ DCAT Dataset (title, description, license, keywords, publisher)
- Item ↔ distribution record(s) or dataset granules (asset-level links)

### STAC ↔ PROV‑O

Recommended linkage approach:

- Each ETL run is a `prov:Activity`
- Each produced Item/asset is a `prov:Entity`
- Items link to provenance via an asset (e.g., `telemetry-prov`) or a consistent `properties.*` reference that points to a PROV document

### Governance linkage

Air Quality STAC must reference domain governance decisions:

- prefer linking in metadata (or by convention) to `data/air-quality/governance/**`
- ensure license/constraints appear in Collection metadata where appropriate

## ⚖ FAIR+CARE & Governance

- Follow the Air Quality governance folder for source-specific constraints.
- If station coordinates or sensor placements have sensitivity concerns, apply:
  - geometry generalization, bounding regions, or access controls as required,
  - documented review/approval notes before publishing.

## 🕰️ Version History

| Version | Date | Notes |
|---|---:|---|
| v11.2.6 | 2025-12-16 | Initial governed README for air-quality STAC folder layout + expectations. |

<div align="center">

**KFM — Air Quality STAC Folder**  
`data/air-quality/stac/README.md`

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Domain-Air%20Quality-blue" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Canonical-brightgreen" />

**Navigation**  
[Air Quality Governance](../governance/README.md) · [Data Index](../../README.md) · [Standards Index](../../../docs/standards/README.md) · [Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md) · [FAIR+CARE Guide](../../../docs/standards/faircare/FAIRCARE-GUIDE.md) · [Indigenous Data Protection](../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© Kansas Frontier Matrix · v11.2.6 · CC-BY 4.0

</div>
