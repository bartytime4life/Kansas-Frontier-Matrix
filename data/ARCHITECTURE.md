---
title: "🗄️ Kansas Frontier Matrix — Data System Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/ARCHITECTURE.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:doc:data-architecture:v11.2.6"
semantic_document_id: "kfm-doc-data-architecture"
event_source_id: "ledger:data/ARCHITECTURE.md"
immutability_status: "version-pinned"

sbom_ref: "../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../releases/v11.2.6/manifest.zip"
telemetry_ref: "../releases/v11.2.6/focus-telemetry.json"
telemetry_schema: "../schemas/telemetry/data-architecture-v11.2.6.json"
energy_schema: "../schemas/telemetry/energy-v2.json"
carbon_schema: "../schemas/telemetry/carbon-v2.json"
data_contract_ref: "../docs/data/"

governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

status: "Active / Enforced"
doc_kind: "Architecture"
intent: "data-system-architecture"
role: "data-platform-architecture"
category: "Data · ETL · Governance · FAIR+CARE"

fair_category: "F1-A1-I1-R1"
care_label: "Variable — Dataset Dependent"
sensitivity_level: "Mixed"
public_exposure_risk: "Dataset-level"
indigenous_rights_flag: "Dataset-level"
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: false

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../schemas/json/data-architecture.schema.json"
shape_schema_ref: "../schemas/shacl/data-architecture-shape.ttl"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "metadata-extraction"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified historical claims"
  - "governance-override"
  - "hallucinated-datasets"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Public Document"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next data-platform architecture update"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true
---

<div align="center">

# 🗄️ **Kansas Frontier Matrix — Data System Architecture (v11.2.6)**  
`data/ARCHITECTURE.md`

**Purpose**  
Describe the **end‑to‑end architecture** of the KFM data platform: ingestion, storage, ETL, validation, governance, lineage, STAC/DCAT cataloging, graph loading, and AI‑assisted enrichment — all wired into CI/CD, FAIR+CARE, and sovereignty governance.

This is the **canonical reference** for anyone touching `data/**`:

- ETL & pipeline engineers  
- GIS & spatial analysts  
- AI/ML practitioners  
- Governance & FAIR+CARE reviewers  
- Focus Mode / Story Node architects  

Designed to be **machine‑readable**, **governance‑enforced**, and **GitHub‑safe**.

[📦 Data Directory Overview](README.md) · [🧾 Data Contracts & Catalog Docs](../docs/data/) · [🔄 CI/CD Workflows](../.github/workflows/README.md)

<br/>

<a href="../docs/standards/kfm_markdown_protocol_v11.2.6.md"><img src="https://img.shields.io/badge/Markdown-KFM--MDP_v11.2.6-blue" alt="KFM-MDP v11.2.6"></a>
<a href="../docs/standards/faircare/FAIRCARE-GUIDE.md"><img src="https://img.shields.io/badge/Data-FAIR%2BCARE-gold" alt="FAIR+CARE"></a>
<a href="./stac/README.md"><img src="https://img.shields.io/badge/Metadata-STAC_1.0.0-informational" alt="STAC 1.0.0"></a>
<a href="../docs/data/"><img src="https://img.shields.io/badge/Metadata-DCAT_3.0-informational" alt="DCAT 3.0"></a>
<a href="../docs/standards/governance/ROOT-GOVERNANCE.md"><img src="https://img.shields.io/badge/Lineage-PROV--O_%7C_OpenLineage-success" alt="PROV-O | OpenLineage"></a>
<a href="../LICENSE"><img src="https://img.shields.io/badge/License-MIT-green" alt="License: MIT"></a>

</div>

---

## 📘 Overview

At v11.2.6, the KFM data system:

- Integrates **historical, environmental, cultural, geological, and administrative** information into a unified platform.
- Organizes the data plane **by domain and by lifecycle stage**:
  - **Domain workspaces** (e.g., `air-quality/`, `hydrology/`, `surficial-geology/`) act as governed “entry points” for domain configuration, domain documentation, and domain-specific curation patterns.
  - **Stage directories** (e.g., `raw/`, `work/`, `processed/`) implement the canonical raw→work→processed lifecycle.
- Publishes discoverable, interoperable metadata via:
  - **STAC 1.x** under `data/stac/` for spatiotemporal assets, and
  - **DCAT 3.0 metadata artifacts** maintained under `docs/data/` (catalog documentation, mappings, contracts).
- Produces provenance and audit evidence:
  - **checksums** under `data/checksums/`,
  - **QA/QC and governance evidence** under `data/reports/`,
  - execution traces and run logs via governed pipeline tooling (see `mcp/` and `tools/`).

Downstream consumers include:

- The **Neo4j knowledge graph** (typed entities + relationships aligned to KFM‑OP and standard ontologies),
- The **API boundary** (the only supported interface for UI),
- **Story Nodes** and **Focus Mode** (evidence-led narrative outputs tied to catalog/provenance).

---

## 🗂️ Directory Layout

Canonical, emoji‑rich layout for `data/` (KFM‑MDP `immediate-one-branch-with-descriptions-and-emojis` profile).

~~~text
📁 data/
├── 📄 README.md                      # Data directory overview & governance (canonical conventions)
├── 📄 ARCHITECTURE.md                # This document (data system architecture)
│
├── 🧭 air-quality/                   # Domain workspace: air quality sources, notes, domain configs
├── 🧭 hydrology/                     # Domain workspace: hydrology datasets, domain configs
├── 🧭 surficial-geology/             # Domain workspace: surficial geology products and curation
├── 🔁 updates/                       # Incremental update payloads (delta ingests, patch bundles)
│
├── 🧾 raw/                           # Raw ingested inputs (append-only; immutable expectations)
├── 🧪 work/                          # Intermediate artifacts (staging; normalization/enrichment)
├── ✅ processed/                     # Canonical processed outputs (analysis-/serving-ready datasets)
│
├── 🛰️ stac/                          # STAC collections & items (spatiotemporal asset metadata)
├── 🔐 checksums/                     # Integrity hashes and verification artifacts
├── 📊 reports/                       # QA/QC, governance evidence, telemetry summaries
├── 🧊 archive/                       # Archived / deprecated datasets (cold storage)
└── (domain and stage READMEs)        # Subdirectories MUST carry local purpose + ownership README
~~~

**Normative rules (data/ level):**

- `raw/` is **append‑only**: corrections and re‑ingests create new versions, never silent overwrites.
- `processed/` outputs MUST be **deterministic** with a replayable pipeline path:
  - `(raw version + config + code + environment) → identical processed artifact`.
- `stac/` MUST remain **schema-valid** and only reference governed, publishable assets.
- `checksums/` + `reports/` MUST provide **tamper-evident integrity** and governance evidence.
- `updates/` MUST be treated as **controlled deltas**: each payload is traceable, validated, and applied by an idempotent process.

---

## 🧭 Context

### How this fits the KFM pipeline

This document describes the “data plane” portion of the KFM system, which flows through:

- **ETL** → **catalogs (STAC / DCAT / PROV)** → **graph (Neo4j)** → **API** → **frontend** → **Story Nodes** → **Focus Mode**

### Key terms

- **Domain workspace**: A domain-scoped folder (e.g., `data/hydrology/`) that hosts domain documentation, domain conventions, and domain configuration patterns.
- **Stage directory**: A lifecycle-scoped folder (e.g., `data/raw/`, `data/work/`, `data/processed/`) that implements the canonical lifecycle.
- **Artifact**: A file or bundle of files representing a dataset, distribution, catalog record, checksum, report, or update payload.

### Scope

- This doc describes architecture, invariants, and interfaces.
- Dataset-specific details belong in:
  - domain READMEs (`data/<domain>/README.md`), and/or
  - catalog and contract documentation (`docs/data/`).

---

## 🧱 Architecture

### Architectural principles

1. **Determinism first**  
   Production data products are reproducible. If the same inputs and configs are re-run under the same environment, the outputs do not change.

2. **Governance as a hard constraint**  
   FAIR+CARE and sovereignty requirements are enforced at pipeline boundaries and before any public exposure.

3. **Catalogs and provenance are first-class outputs**  
   A dataset is not “done” until it has:
   - a discoverable catalog representation, and
   - a traceable lineage record.

4. **Frontend never reads raw files directly**  
   The API boundary is the only supported interface for user-facing layers.

### Data planes and responsibilities

- **Storage plane (`data/`)**  
  Holds raw, intermediate, processed, catalogs, integrity, reports, archives, and update payloads.

- **Contract and catalog documentation plane (`docs/data/`)**  
  Holds dataset contracts, catalog mappings, and schema documentation (including DCAT metadata conventions).

- **Schema plane (`schemas/`)**  
  Hosts JSON schemas and telemetry schemas used for machine validation.

- **Execution plane (`src/`, `tools/`, `mcp/`)**  
  Hosts pipeline code, validators, deterministic run tooling, and governed run logs / experiment artifacts.

### Update mechanism (`data/updates/`)

`data/updates/` exists to support incremental changes without violating reproducibility:

- Update payloads SHOULD be:
  - immutable bundles with checksums,
  - explicitly versioned,
  - applied by idempotent jobs (safe to re-run),
  - provenance-linked to the artifacts they modify or supersede.

Typical use cases:

- corrected source drops,
- periodic refreshes (e.g., daily sensor additions),
- backfills,
- governance-driven generalization/redaction updates.

---

## 📦 Data & Metadata

### Spatial conventions

- Public-facing geometries and extents SHOULD be representable in **EPSG:4326 (WGS84)** for interoperability.
- Working CRSs may differ (equal-area for stats, UTM for local work), but transformations MUST be recorded.
- Geometry validity checks are mandatory for publishable vector outputs:
  - valid polygons, consistent `bbox`, and explicit CRS declaration.

### Sensitive location handling (generalization)

- Datasets that risk exposing sensitive locations MUST be generalized or masked at publish time.
- Generalization policies (e.g., grid/H3-style aggregation) MUST be declared in metadata and enforced in CI gates.

### Temporal conventions

- Datasets MUST declare temporal coverage:
  - `temporal_start`, `temporal_end` (or an instant),
  - optional uncertainty for approximate historical periods.
- Temporal fields MUST be queryable and usable by Story Nodes / Focus Mode timelines.

### Quality evidence and fitness-for-use

Quality outputs SHOULD be written to `data/reports/` and include:

- completeness and missingness,
- logical consistency,
- positional and temporal accuracy (as applicable),
- thematic accuracy for classified layers.

### Sustainability telemetry

Where available, pipeline telemetry SHOULD be captured and summarized:

- `energy_wh`, `carbon_gco2e`, plus workload and duration metrics
- stored in `data/reports/` and referenced by release telemetry (`telemetry_ref`)

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC (primary asset catalog)

- `data/stac/` is the canonical location for:
  - the STAC root catalog,
  - domain collections,
  - items referencing publishable assets (typically from `data/processed/`).

STAC conventions MUST support:

- stable IDs and predictable paths,
- clear asset roles and media types,
- explicit spatial/temporal extents,
- governance properties (license, access, sensitivity flags, usage constraints).

### DCAT (dataset interoperability metadata)

- DCAT-oriented documentation and catalog conventions are maintained in `docs/data/`.
- DCAT records SHOULD map cleanly to STAC concepts:
  - dataset identifiers are stable and consistent across catalogs,
  - distributions correspond to publishable assets (often via STAC asset links).

### PROV‑O and execution lineage (PROV / OpenLineage)

Lineage is represented at two complementary layers:

- **Logical provenance (PROV‑O)**  
  Captures Entities (datasets/assets), Activities (ETL, curation, inference), and Agents (people/services).

- **Execution lineage (OpenLineage)**  
  Captures run-level job metadata: inputs, outputs, timing, environment, and telemetry.

Storage conventions:

- provenance evidence SHOULD be emitted into governed reports/audit locations,
- run logs and config snapshots SHOULD be captured in governed run directories (see `mcp/`).

### Catalog-to-graph mapping

Catalog metadata and lineage are designed to be ingestible into the knowledge graph:

- datasets and distributions become typed nodes,
- temporal and spatial extents become queryable objects,
- provenance chains become traversable relationships,
- governance flags remain queryable to support safe downstream use.

---

## 🗺️ Diagrams

### End-to-end data lifecycle

~~~mermaid
flowchart TD
  A["Ingest\n(data/raw/)"] --> B["Normalize & Enrich\n(data/work/)"]
  B --> C["Publishable Products\n(data/processed/)"]

  C --> D["STAC Catalog\n(data/stac/)"]
  C --> E["QA/QC + Evidence\n(data/reports/)"]
  C --> F["Integrity\n(data/checksums/)"]

  D --> G["Graph Load\n(Neo4j)"]
  G --> H["API Boundary"]
  H --> I["Story Nodes + Focus Mode"]
~~~

### Domain + stage organization

~~~mermaid
flowchart LR
  subgraph Domain_Workspaces["Domain Workspaces (Entry Points)"]
    AQ["data/air-quality/"]
    HY["data/hydrology/"]
    SG["data/surficial-geology/"]
  end

  subgraph Stages["Lifecycle Stages (Canonical)"]
    RAW["data/raw/"]
    WORK["data/work/"]
    PROC["data/processed/"]
    STAC["data/stac/"]
  end

  AQ --- RAW
  HY --- RAW
  SG --- RAW

  RAW --> WORK --> PROC --> STAC
~~~

### Incremental update flow

~~~mermaid
flowchart TD
  U["Update Payload\n(data/updates/)"] --> V["Validate\n(tools/validation + CI)"]
  V --> A["Apply Idempotently\n(raw/work/processed)"]
  A --> C["Rebuild/Extend Catalog\n(data/stac/)"]
  A --> R["Emit Evidence\n(reports + checksums)"]
~~~

---

## 🧪 Validation & CI/CD

Validation is embedded in the architecture and enforced through:

- **Local and CI validators** under `tools/validation/`
- **Schemas** under `schemas/` (JSON schemas; telemetry schemas; additional profiles where applicable)
- **CI workflows** under `.github/workflows/` (see `.github/workflows/README.md`)

Expected validation gates for publishable changes:

1. **Schema validation**
   - tabular contracts (types, ranges, nullability),
   - spatial validity (geometry, CRS declarations, extents),
   - metadata shape validation for catalog artifacts.

2. **STAC validation**
   - STAC spec compliance,
   - KFM profile expectations (IDs, required properties, asset roles).

3. **Integrity verification**
   - checksum generation and verification,
   - release packaging alignment (manifest/SBOM where applicable).

4. **FAIR+CARE and sovereignty checks**
   - required governance fields present,
   - masking/generalization rules enforced for sensitive datasets.

5. **Report generation**
   - QA/QC summaries and audit evidence written to `data/reports/`.

---

## 🧠 Story Node & Focus Mode Integration

The data system supports narrative layers via:

- **Processed products** that are safe and performant for downstream use (`data/processed/`)
- **Catalog metadata** that enables discovery, filtering, and evidence linking (`data/stac/`)
- **Graph mappings** that provide typed entities/relationships and provenance

Design constraints:

- Story Nodes MUST remain evidence-led:
  - every claim should be traceable to underlying assets and provenance.
- Focus Mode MUST respect governance flags:
  - sensitivity labels, access constraints, and sovereignty controls must be enforced at query time.
- Narrative outputs should be qualified by data quality evidence:
  - uncertainty and fitness-for-use should inform narrative confidence.

---

## ⚖ FAIR+CARE & Governance

FAIR+CARE and sovereignty are enforced across the lifecycle:

- **Ingestion**
  - licensing and rights captured early,
  - initial sensitivity and stewardship flags assigned.

- **Transformation**
  - generalization and redaction applied as required,
  - provenance recorded for every transformation step.

- **Publication**
  - only governance-approved assets appear in catalogs,
  - public distributions must be safe by default.

Authoritative references:

- Governance: `../docs/standards/governance/ROOT-GOVERNANCE.md`
- FAIR+CARE: `../docs/standards/faircare/FAIRCARE-GUIDE.md`
- Sovereignty: `../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md`

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Updated to KFM‑MDP v11.2.6; normalized H2 headings to registry; aligned `data/` layout with current domain+stage structure (`air-quality/`, `hydrology/`, `surficial-geology/`, `updates/`); clarified DCAT/contracts location under `docs/data/`; removed tool-only citation markers. |
| v11.2.3 | 2025-12-09 | Prior stable architecture baseline for v11.2.3. |
| v11.2.2 | 2025-11-27 | Canonicalized layout and governance references; established baseline lifecycle narrative. |
| v11.0.0 | 2025-11-19 | Initial v11 data system architecture definition. |

---

<div align="center">

🗄️ **Kansas Frontier Matrix — Data System Architecture (v11.2.6)**  
Data‑First · FAIR+CARE‑Governed · Provenance‑Aware  

© 2025 Kansas Frontier Matrix — MIT License  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · KFM‑OP v11.0  

[⬅ Back to Data Overview](README.md) ·  
[⬅ Back to Repository Root](../README.md) ·  
[🧾 Data Contracts & Catalog Docs](../docs/data/) ·  
[⚖ Governance Charter](../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
