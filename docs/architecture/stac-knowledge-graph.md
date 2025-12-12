---
title: "🧭 Kansas Frontier Matrix — STAC to Knowledge-Graph Architecture & Provenance Model"
path: "docs/architecture/stac-knowledge-graph.md"
version: "v11.2.6"
last_updated: "2025-12-12"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Architecture Review Board · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Architecture Standard"
header_profile: "standard"
footer_profile: "standard"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

scope:
  domain: "architecture"
  applies_to:
    - "data/stac/**"
    - "data/sources/**"
    - "data/processed/**"
    - "schemas/**"
    - "src/**"
    - "docs/architecture/**"

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

signature_ref: "././releases/v11.2.6/signature.sig"
attestation_ref: "././releases/v11.2.6/slsa-attestation.json"
sbom_ref: "././releases/v11.2.6/sbom.spdx.json"
manifest_ref: "././releases/v11.2.6/manifest.zip"

story_node_refs: []
immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:architecture:stac-knowledge-graph:v11.2.6"
semantic_document_id: "kfm-architecture-stac-knowledge-graph-v11.2.6"
event_source_id: "ledger:kfm:doc:architecture:stac-knowledge-graph:v11.2.6"
doc_integrity_checksum: "<sha256>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "diagram-extraction"
  - "metadata-extraction"
  - "layout-normalization"

ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

transform_registry:
  allowed:
    - "summary"
    - "semantic-highlighting"
    - "diagram-extraction"
    - "metadata-extraction"
    - "layout-normalization"
  prohibited:
    - "content-alteration"
    - "speculative-additions"
    - "unverified-architectural-claims"
    - "narrative-fabrication"
    - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

fencing_profile: "outer-backticks-inner-tildes-v1"
layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "footer-check"
  - "accessibility-check"
  - "metadata-check"
  - "provenance-check"
  - "secret-scan"
  - "pii-scan"

governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
---

<div align="center">

# 🧭 **Kansas Frontier Matrix — STAC to Knowledge-Graph Architecture & Provenance Model**
`docs/architecture/stac-knowledge-graph.md`

**Purpose**   
Define the canonical architecture pattern for ingesting STAC catalogs into the Kansas Frontier Matrix Neo4j knowledge graph while preserving full PROV-O lineage, enabling fast spatiotemporal queries, and supporting Story Nodes / Focus Mode without data drift.

<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/STAC-KFM--STAC_v11-005eb8" />
<img src="https://img.shields.io/badge/PROV-KFM--PROV_v11-6f42c1" />
<img src="https://img.shields.io/badge/Graph-Neo4j-008cc1" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

</div>

---

## 📘 Overview

This document defines the **canonical architecture pattern** for ingesting **STAC catalogs** into the Kansas Frontier Matrix **Neo4j knowledge graph**, preserving **full PROV-O lineage**, enabling **fast spatiotemporal queries**, and supporting **Story Nodes and Focus Mode** without data drift.

### 1. Architectural Intent

The STAC → Graph pattern serves four core objectives:

1. **Deterministic ingestion** of external and internal STAC catalogs
2. **First-class provenance** for every transformation and derivative
3. **Fast temporal and spatial traversal** for narrative and analysis layers
4. **Governance-ready lineage** aligned with FAIR+CARE and Indigenous data protections

This pattern is **mandatory** for all geospatial raster, vector, and derived analytical products in KFM v11.

---

## 🗂️ Directory Layout

~~~text
📁 KansasFrontierMatrix/                          — KFM monorepo root
├── 📁 docs/                                      — Documentation layer
│   ├── 📁 architecture/                          — Architecture standards and diagrams
│   │   └── 📄 stac-knowledge-graph.md             — ← This standard
│   └── 📁 standards/                             — Governance / FAIR+CARE / sovereignty
│       ├── 📁 governance/                        — Governance charter and standards
│       ├── 📁 faircare/                          — FAIR+CARE guidance
│       └── 📁 sovereignty/                       — Indigenous data protection policy
├── 📁 data/                                      — Data layer (raw → processed → catalogs)
│   ├── 📁 sources/                               — Source manifests (license, checksums, access)
│   ├── 📁 processed/                             — Deterministic pipeline outputs
│   └── 📁 stac/                                  — STAC Collections/Items (publishable catalog)
├── 📁 schemas/                                   — Machine-validated schemas (STAC/DCAT/PROV)
│   ├── 📁 stac/                                  — KFM-STAC v11 profile schemas
│   ├── 📁 dcat/                                  — KFM-DCAT v11 mappings/shapes
│   └── 📁 prov/                                  — KFM-PROV v11 mappings/shapes
├── 📁 src/                                       — Runtime code
│   ├── 📁 etl/                                   — Deterministic ingestion + transforms
│   └── 📁 graph/                                 — Neo4j ingestion, constraints, idempotent merges
└── 📁 mcp/                                       — Runs, experiments, model cards, logs
    └── 📁 runs/                                  — Reproducible run records (config snapshots, seeds)
~~~

---

## 🧱 Architecture

### 2. Core Graph Entities

#### 2.1 Collection (`:Collection`)
Represents a STAC Collection.

**Required properties**
- `collection_id` (stable identifier)
- `title`
- `license`
- `stac_version`
- `created_at`

#### 2.2 Item (`:Item`)
Represents a STAC Item (acquisition-time atomic unit).

**Required properties**
- `item_id` (globally unique)
- `collection_id`
- `acquisition_time` (ISO-8601 UTC)
- `geometry` (WKB or GeoJSON)
- `bbox`
- `platform`
- `constellation`

**Optional properties**
- `gsd`
- `cloud_cover`
- `eo_bands`
- `created_at`
- `updated_at`

#### 2.3 Asset (`:Asset`)
Represents a STAC Asset or derivative file.

**Required properties**
- `asset_id` (`item_id::asset_key`)
- `href`
- `type` (MIME)
- `roles` (array)
- `checksum`
- `size_bytes`

#### 2.4 Process (`:Process`)
Represents a PROV Activity (ingest, transform, derive).

**Required properties**
- `process_id`
- `name`
- `kind` (`ingest | transform | derive | subset | reproject`)
- `started_at`
- `ended_at`
- `params_json`
- `code_ref` (git SHA)
- `container_digest`
- `attestation_ref`

#### 2.5 Dataset (`:Dataset`) *(optional materialization)*
Used for mosaics, composites, or analytical outputs.

**Required properties**
- `dataset_id`
- `title`
- `spatial_ref`
- `temporal_extent`
- `checksum`
- `size_bytes`
- `location`

---

### 3. Canonical Relationships

~~~text
(:Collection)-[:HAS_ITEM]->(:Item)
(:Item)-[:HAS_ASSET]->(:Asset)
(:Item)-[:IN_COLLECTION]->(:Collection)

(:Process)-[:USED]->(:Item|:Asset)
(:Process)-[:GENERATED]->(:Item|:Asset|:Dataset)

(:Asset)-[:DERIVED_FROM]->(:Asset|:Item)
~~~

This structure directly mirrors PROV-O:

| PROV Concept | KFM Node |
|---|---|
| Entity | Item, Asset, Dataset |
| Activity | Process |
| Agent | Tool / User (optional extension) |

---

### 4. Indexing & Performance Guarantees

#### 4.1 Identity & Integrity
- Unique constraints on:
  - `:Item(item_id)`
  - `:Collection(collection_id)`
  - `:Asset(asset_id)`
  - `:Process(process_id)`

#### 4.2 Temporal Access
- Composite index:
  - `:Item(item_id, acquisition_time)`
- Range index:
  - `:Item(acquisition_time)`

#### 4.3 Spatial Acceleration
Each Item must include at least one tiling key:
- `s2_cell_level_12` **or**
- `quadkey_z14`

Used for coarse filtering prior to exact geometry tests.

---

### 5. Deterministic Ingestion Contract

Each ingested STAC Item must supply (at minimum) the following shape (KFM foreign-members allowed):

~~~json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "collection": "string",
  "id": "string",
  "bbox": [-102.05, 37.0, -94.6, 40.0],
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [-102.05, 37.0],
        [-102.05, 40.0],
        [-94.6, 40.0],
        [-94.6, 37.0],
        [-102.05, 37.0]
      ]
    ]
  },
  "properties": {
    "datetime": "2025-01-01T00:00:00Z",
    "platform": "string",
    "constellation": "string"
  },
  "assets": {
    "data": {
      "href": "uri",
      "type": "mime",
      "roles": ["data"],
      "checksum": "sha256:<hex>",
      "size_bytes": 123456
    }
  },
  "provenance": {
    "process": {
      "id": "proc-id",
      "name": "ingest_stac@vX",
      "kind": "ingest",
      "code_ref": "git-sha",
      "container_digest": "sha256:<hex>",
      "attestation_ref": "slsa.json"
    },
    "inputs": ["asset-id-1"]
  }
}
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

### DCAT
- STAC Collections and derived `:Dataset` materializations MAY be expressed as `dcat:Dataset`.
- STAC Assets and file-level outputs MAY be expressed as `dcat:Distribution` (media type, checksum, size).

### STAC
- STAC `Collection` ↔ `:Collection`
- STAC `Item` ↔ `:Item`
- STAC `assets.{key}` ↔ `:Asset` (`asset_id = item_id::asset_key`)

### PROV-O
- `:Item`, `:Asset`, `:Dataset` ↔ `prov:Entity`
- `:Process` ↔ `prov:Activity`
- `:Agent` (reserved) ↔ `prov:Agent`

---

## 🧠 Story Node & Focus Mode Integration

- Story Nodes anchor on `:Item` or `:Dataset`.
- Lineage panels traverse:
  - `:DERIVED_FROM`
  - `:USED`
  - `:GENERATED`
- Focus Mode queries rely on:
  - `acquisition_time`
  - tiling keys
  - optional gazetteer joins

This guarantees narrative traceability without recomputation.

---

## ⚖ FAIR+CARE & Governance

- All Assets and Datasets must carry:
  - cryptographic checksums
  - provenance activities
- Sensitive data may include:
  - `care_label`
  - `access_label`
- SBOM and SLSA attestations are mandatory for derived products.
- NHPA §304 and Indigenous data flags propagate through lineage edges.

---

## 🧪 Validation & CI/CD

Markdown and ingestion compliance are CI-enforced.

### 8. Non-Negotiable Rules
- No Item without provenance.
- No Asset without checksum.
- No Dataset without lineage.
- No Story Node without graph anchoring.

Violations block CI ingestion.

### 9. Future Extensions (Reserved)
- Agent attribution (`:Agent`)
- Uncertainty propagation nodes
- Energy / carbon telemetry linkage
- Automated provenance diffing

---

## 🕰️ Version History

| Version | Date | Notes |
|---:|---:|---|
| **v11.2.6** | 2025-12-12 | Initial governed architecture release |

<div align="center">

Designed for Longevity · Governed for Integrity

[← Architecture Index](./README.md) ·
[↔ Data Pipeline Contracts](../standards/pipeline/README.md) ·
[⚖ Governance Charter](../standards/governance/ROOT-GOVERNANCE.md) ·
[FAIR+CARE Guide](../standards/faircare/FAIRCARE-GUIDE.md) ·
[Indigenous Data Protection](../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

</div>