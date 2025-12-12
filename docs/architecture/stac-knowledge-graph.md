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
diagram_profiles:
  - "mermaid-flowchart-v1"

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
    - "docs/architecture/**"
    - "data/stac/**"
    - "data/processed/**"
    - "src/**"
    - "mcp/**"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"

indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by KFM-STAC v12"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"

signature_ref: "././releases/v11.2.6/signature.sig"
attestation_ref: "././releases/v11.2.6/slsa-attestation.json"
sbom_ref: "././releases/v11.2.6/sbom.spdx.json"
manifest_ref: "././releases/v11.2.6/manifest.zip"

governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

provenance_chain: []
provenance_requirements:
  versions_required: false
  newest_first: true
  must_reference_superseded: false
  must_reference_origin_root: false

story_node_refs: []
immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:architecture:stac-knowledge-graph:v11.2.6"
semantic_document_id: "kfm-stac-knowledge-graph-v11.2.6"
event_source_id: "ledger:kfm:doc:architecture:stac-knowledge-graph:v11.2.6"
doc_integrity_checksum: "<sha256>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

ai_transform_permissions:
  - "summary"
  - "timeline-generation"
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

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# 🧭 **Kansas Frontier Matrix — STAC → Knowledge‑Graph Architecture & Provenance Model**
`docs/architecture/stac-knowledge-graph.md`

**Purpose**  
Define the **canonical, governed architecture** for ingesting **STAC catalogs** into the Kansas Frontier Matrix **Neo4j knowledge graph**, preserving **PROV‑O lineage**, enabling **fast spatiotemporal queries**, and supporting **Story Nodes / Focus Mode** without data drift.

<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img src="https://img.shields.io/badge/KFM--STAC-v11-purple" />
<img src="https://img.shields.io/badge/KFM--PROV-v11-blueviolet" />
<img src="https://img.shields.io/badge/Graph-Neo4j-black" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />

</div>

---

## 📘 Overview

### 1. Architectural intent (normative)

The STAC → Graph pattern serves four objectives:

1. **Deterministic ingestion** of external and internal STAC catalogs
2. **First‑class provenance** for every transformation and derivative (PROV‑O compatible)
3. **Fast temporal and spatial traversal** for narrative and analysis layers
4. **Governance‑ready lineage** aligned with FAIR+CARE and Indigenous data protections

This pattern is **mandatory** for all governed geospatial raster, vector, and derived analytical products in KFM v11.

### 2. Concept mapping (STAC ↔ Graph ↔ PROV‑O)

| Concept | STAC | Graph | PROV‑O |
|---|---|---|---|
| Dataset grouping | Collection | `:Collection` | `prov:Entity` (optional) |
| Atomic acquisition | Item | `:Item` | `prov:Entity` |
| File / distribution | Asset | `:Asset` | `prov:Entity` |
| Ingest / transform | — | `:Process` | `prov:Activity` |
| Person/tool attribution | — | `:Agent` (reserved) | `prov:Agent` |

---

## 🗂️ Directory Layout

The following layout is the **required contract** for pipelines implementing this standard (names may vary; **artifact placement MUST NOT**).

~~~text
📁 docs/
├── 📁 architecture/
│   └── 📄 stac-knowledge-graph.md — this standard
│
├── 📁 standards/
│   ├── 📁 governance/
│   │   └── 📄 ROOT-GOVERNANCE.md
│   ├── 📁 faircare/
│   │   └── 📄 FAIRCARE-GUIDE.md
│   └── 📁 sovereignty/
│       └── 📄 INDIGENOUS-DATA-PROTECTION.md
│
📁 data/
├── 📁 sources/
│   └── 📄 <source>.yml — source manifests (license, retrieval date, checksums, restrictions)
├── 📁 stac/
│   ├── 📁 collections/
│   └── 📁 items/
├── 📁 processed/
│   └── 📁 <dataset_id>/
└── 📁 prov/
    └── 📁 <run_id>/
│
📁 mcp/
└── 📁 runs/
    └── 📁 <run_id>/
        ├── 📄 run-config.snapshot.yml
        └── 📄 run.log
~~~

---

## 🧭 Context

### 1. Pipeline position (normative)

~~~text
Deterministic ETL
↓
STAC / DCAT / PROV catalogs emitted (pass even on partial failures where safe)
↓
Neo4j knowledge graph ingest (idempotent, incremental)
↓
API boundary (only supported boundary for UI)
↓
Frontend (Map + Narrative)
↓
Story Nodes → Focus Mode
~~~

### 2. Key principle (normative)

> Provenance is **part of the data model**, not an optional audit log.

---

## 🗺️ Diagrams

### 1. End‑to‑end flow (reference)

~~~mermaid
flowchart LR
  A[STAC Catalog or Collection] --> B[Validate STAC + KFM extensions]
  B --> C[Normalize identifiers + geometry + timestamps]
  C --> D[Write STAC to data/stac]
  C --> E[Emit PROV bundle to data/prov]
  D --> F[Neo4j ingest job]
  E --> F
  F --> G[API]
  G --> H[UI]
  H --> I[Story Nodes]
  H --> J[Focus Mode]
~~~

### 2. Canonical graph shape (reference)

~~~mermaid
flowchart TB
  COL[Collection] -->|HAS_ITEM| ITM[Item]
  ITM -->|HAS_ASSET| ASO[Asset]
  ITM -->|IN_COLLECTION| COL

  PRC[Process] -->|USED| ITM
  PRC -->|USED| ASI[Asset]
  PRC -->|GENERATED| ASO
  PRC -->|GENERATED| DST[Dataset]
  ASO -->|DERIVED_FROM| ASI
~~~

---

## 🧱 Architecture

### 1. Core graph entities (nodes) (normative)

#### 1.1 Collection (`:Collection`)

**Required properties**

- `collection_id` (stable identifier)
- `title`
- `license`
- `stac_version`
- `created_at`

#### 1.2 Item (`:Item`)

**Required properties**

- `item_id` (globally unique)
- `collection_id`
- `acquisition_time` (ISO‑8601 UTC)
- `geometry` (WKB or GeoJSON)
- `bbox`
- `platform`
- `constellation`

**Required acceleration keys (one of the following)**

- `s2_cell_level_12` **OR**
- `quadkey_z14`

**Optional properties**

- `gsd`
- `cloud_cover`
- `eo_bands`
- `created_at`
- `updated_at`

#### 1.3 Asset (`:Asset`)

**Required properties**

- `asset_id` (`item_id::asset_key`)
- `href`
- `type` (MIME)
- `roles` (array of strings)
- `checksum` (sha256)
- `size_bytes`

#### 1.4 Process (`:Process`)

Represents a PROV Activity (ingest, transform, derive).

**Required properties**

- `process_id`
- `name`
- `kind` (`ingest | transform | derive | subset | reproject`)
- `started_at`
- `ended_at`
- `params_json` (deterministic JSON string)
- `code_ref` (git SHA)
- `container_digest`
- `attestation_ref`

#### 1.5 Dataset (`:Dataset`) (optional materialization)

Used for mosaics, composites, or analytical outputs.

**Required properties**

- `dataset_id`
- `title`
- `spatial_ref`
- `temporal_extent`
- `checksum`
- `size_bytes`
- `location`

### 2. Canonical relationships (normative)

~~~text
(:Collection)-[:HAS_ITEM]->(:Item)
(:Item)-[:HAS_ASSET]->(:Asset)
(:Item)-[:IN_COLLECTION]->(:Collection)

(:Process)-[:USED]->(:Item|:Asset)
(:Process)-[:GENERATED]->(:Item|:Asset|:Dataset)

(:Asset)-[:DERIVED_FROM]->(:Asset|:Item)
~~~

This structure directly mirrors PROV‑O:

| PROV concept | KFM node |
|---|---|
| Entity | `:Item`, `:Asset`, `:Dataset` |
| Activity | `:Process` |
| Agent | `:Agent` (reserved extension) |

### 3. Indexing & performance guarantees (normative)

#### 3.1 Identity & integrity

Unique constraints MUST exist on:

- `:Item(item_id)`
- `:Collection(collection_id)`
- `:Asset(asset_id)`
- `:Process(process_id)`

#### 3.2 Temporal access

- Composite index: `:Item(item_id, acquisition_time)`
- Range index: `:Item(acquisition_time)`

#### 3.3 Spatial acceleration

Each `:Item` MUST carry **at least one tiling key** (`s2_cell_level_12` or `quadkey_z14`) for coarse filtering prior to exact geometry tests.

### 4. Deterministic ingestion contract (normative)

Each ingested STAC Item MUST supply:

- a valid STAC `collection`, `id`, `geometry`, `bbox`
- `properties.datetime` in ISO‑8601 UTC
- deterministic, complete asset objects with checksums
- process provenance sufficient to reconstruct lineage

Example (illustrative):

~~~json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "collection": "string",
  "id": "string",
  "bbox": [-101.0, 37.0, -95.0, 40.0],
  "geometry": { "type": "Polygon", "coordinates": [] },
  "properties": {
    "datetime": "2025-01-01T00:00:00Z",
    "platform": "string",
    "constellation": "string",
    "s2_cell_level_12": "string"
  },
  "assets": {
    "data": {
      "href": "uri",
      "type": "mime",
      "roles": ["data"],
      "checksum:sha256": "hex",
      "size": 123456
    }
  },
  "kfm:provenance": {
    "process": {
      "id": "proc-id",
      "name": "ingest_stac@vX",
      "kind": "ingest",
      "code_ref": "git-sha",
      "container_digest": "sha256:...",
      "attestation_ref": "slsa.json"
    },
    "inputs": ["asset-id-1"]
  }
}
~~~

Notes:

- `assets` MUST be an object keyed by `asset_key` (STAC‑compliant), not an array.
- Checksums MUST be cryptographically strong (`sha256`).
- `params_json` MUST be deterministically serialized (stable key order, stable whitespace rules in implementation).

### 5. Reserved extensions (non‑breaking)

- Agent attribution (`:Agent`, `prov:wasAssociatedWith`)
- Uncertainty propagation nodes
- Energy / carbon telemetry linkage
- Automated provenance diffing

---

## 🧠 Story Node & Focus Mode Integration

### 1. Anchoring (normative)

- Story Nodes MUST anchor to `:Item` or `:Dataset`.
- Story Nodes MUST reference lineage‑traversable entities (no “orphan narratives”).

### 2. Lineage traversal (normative)

Lineage panels traverse:

- `:DERIVED_FROM`
- `:USED`
- `:GENERATED`

### 3. Query guarantees (normative)

Focus Mode queries rely on:

- `acquisition_time`
- tiling keys (`s2_cell_level_12` / `quadkey_z14`)
- optional gazetteer joins (via API, not direct graph access)

This guarantees narrative traceability without recomputation.

---

## 🧪 Validation & CI/CD

### 1. Blocking rules (normative)

Violations MUST block CI ingestion and promotion:

- No `:Item` without provenance
- No `:Asset` without checksum
- No `:Dataset` without lineage
- No Story Node without graph anchoring

### 2. Minimum checks (normative)

- STAC validation (spec + governed extensions)
- Checksum presence and format validation
- Deterministic provenance validation (`Process` required fields)
- Neo4j constraint + index validation
- Idempotency validation (re‑ingest does not duplicate)

---

## 📦 Data & Metadata

### 1. Artifact placement (normative)

- Raw source manifests MUST be recorded under `data/sources/`
- STAC JSON MUST be written under `data/stac/`
- Derived artifacts MUST be written under `data/processed/`
- Run logs and config snapshots MUST be written under `mcp/runs/`

### 2. Asset integrity (normative)

All Assets and Datasets MUST carry:

- cryptographic checksums
- size metadata
- provenance activities

---

## 🌐 STAC, DCAT & PROV Alignment

### 1. STAC

- `:Collection` aligns to STAC Collection
- `:Item` aligns to STAC Item
- `:Asset` aligns to STAC Asset

### 2. DCAT

- STAC Collection MAY be represented as `dcat:Dataset`
- Assets / distributions SHOULD be represented as `dcat:Distribution`
- `license` MUST be present and consistent across STAC/DCAT views

### 3. PROV‑O

- `:Process` = `prov:Activity`
- `:Item|:Asset|:Dataset` = `prov:Entity`
- `:DERIVED_FROM` SHOULD be exportable as `prov:wasDerivedFrom`
- `:USED` and `:GENERATED` SHOULD be exportable as `prov:used` / `prov:wasGeneratedBy`

---

## ⚖ FAIR+CARE & Governance

### 1. Sensitive and Indigenous data controls (normative)

Sensitive data MAY include:

- `care_label`
- `access_label`

NHPA §304 and Indigenous data flags MUST propagate through lineage edges (entity‑to‑entity and activity‑to‑entity).

### 2. Supply chain requirements (normative)

For derived products:

- SBOM and SLSA attestations are mandatory
- `container_digest` and `attestation_ref` MUST be recorded on `:Process`

---

## 🕰️ Version History

| Version | Date | Notes |
|---|---:|---|
| v11.2.6 | 2025-12-12 | Initial governed architecture release (MDP‑compliant formatting). |

---

<div align="center">

📑 **STAC → Knowledge‑Graph Architecture (KFM)**  
Designed for Longevity · Governed for Integrity

[📘 Docs Root](../README.md) ·
[🏗️ Architecture Index](./README.md) ·
[🧱 Data Pipeline Contracts](../data-ops/README.md) ·
[🏛️ Governance Charter](../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC‑BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6

</div>