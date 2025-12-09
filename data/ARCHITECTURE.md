---
title: "🗄️ Kansas Frontier Matrix — Data System Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/ARCHITECTURE.md"

version: "v11.2.3"
last_updated: "2025-12-09"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:doc:data-architecture:v11.2.3"
semantic_document_id: "kfm-doc-data-architecture"
event_source_id: "ledger:data/ARCHITECTURE.md"
immutability_status: "version-pinned"

sbom_ref: "../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../releases/v11.2.3/manifest.zip"
telemetry_ref: "../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../schemas/telemetry/data-architecture-v11.2.3.json"
energy_schema: "../schemas/telemetry/energy-v2.json"
carbon_schema: "../schemas/telemetry/carbon-v2.json"
data_contract_ref: "../docs/contracts/data-contract-v3.json"

governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.5"
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

# 🗄️ **Kansas Frontier Matrix — Data System Architecture**  
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

[📦 Data Directory Overview](README.md) · [🔄 CI/CD Workflows](../.github/workflows/README.md)

</div>

---

## 📘 Overview

At v11.2.3, the KFM data system:

- Integrates **historical, environmental, cultural, and geologic data** into a unified platform.  
- Normalizes everything into a **shared spatial, temporal, and semantic frame**.  
- Represents datasets using:
  - **STAC 1.x** catalogs for spatio‑temporal assets,  
  - **DCAT 3.0** catalogs for datasets and distributions,  
  - **JSON‑LD + PROV‑O** for semantic metadata and lineage.  
- Loads curated products into the **Neo4j knowledge graph**, aligned with:
  - CIDOC‑CRM, GeoSPARQL, OWL‑Time, PROV‑O, and KFM‑OP v11.  
- Tracks:
  - **Lineage** (what came from where and how),  
  - **Governance** (FAIR+CARE, sovereignty, risk),  
  - **Sustainability** (energy/carbon telemetry).

Data artifacts ultimately serve:

- **Focus Mode v3** (narrative generation and evidence linking),  
- **Story Nodes v3** (spatiotemporal narrative units),  
- **Public STAC/DCAT catalogs**,  
- **APIs and map UIs** (MapLibre/Cesium web client).

The architecture is designed for:

- **Reproducible ETL**,  
- **Transparent, auditable governance**,  
- **Ethical & sovereign data use**,  
- **Strong sustainability accounting**,  
- **Tight integration with AI & visualization layers**.

---

## 🗂️ Data System Directory Architecture

This architecture builds on the canonical layout documented in `data/README.md` and treats `data/` as the **physical backbone** of the KFM data plane.

~~~text
📁 data/
├── 📄 ARCHITECTURE.md               # This document (data system architecture)
├── 📄 README.md                     # Data directory overview & governance
│
├── 📁 sources/                      # External dataset manifests & source metadata
│   ├── 📁 providers/                # Provider profiles (NOAA, USGS, KGS, tribal partners, etc.)
│   ├── 📁 catalogs/                 # Upstream STAC/DCAT links & harvested descriptors
│   └── 📁 agreements/               # Licensing / MOU summaries (non-sensitive)
│
├── 📁 raw/                          # Original source datasets (immutable, append-only; Git+DVC/LFS)
│   ├── 📁 hydrology/
│   ├── 📁 geology/
│   ├── 📁 history/
│   ├── 📁 remote-sensing/
│   ├── 📁 environmental/
│   └── 📁 cultural-sovereignty/     # Culturally sensitive data (governed, often generalized)
│
├── 📁 work/                         # Cleaned, normalized, enriched intermediates
│   ├── 📁 tables/                   # Normalized tabular data (CSV, Parquet)
│   ├── 📁 spatial/                  # Intermediate GeoJSON/GPKG/rasters/COGs
│   └── 📁 metadata/                 # Pre-STAC/DCAT JSON/JSON-LD, schema snapshots
│
├── 📁 processed/                    # Deterministic, analysis-ready ETL outputs
│   ├── 📁 hydrology/
│   ├── 📁 climate/
│   ├── 📁 ecology/
│   ├── 📁 historical/
│   ├── 📁 hazards/
│   └── 📁 storynodes/               # Precomputed Story Node-ready aggregates (optional)
│
├── 📁 stac/                         # STAC Items & Collections (KFM-STAC v11 profile)
│   ├── 📄 README.md                 # STAC catalog conventions
│   ├── 🧾 catalog.json              # STAC root catalog
│   ├── 📁 missions/                 # EO missions (Landsat, Sentinel, NAIP, etc.)
│   ├── 📁 hydrology/                # Hydrology STAC domain
│   ├── 📁 climate/                  # Climate STAC domain
│   ├── 📁 hazards/                  # Hazards STAC domain
│   ├── 📁 landcover/                # Landcover / land use domain
│   └── 📁 tabular/                  # Tabular/non-spatial STAC items
│
├── 📁 dcat/                         # DCAT 3.0 catalogs (JSON-LD)
│   ├── 🧾 catalog.jsonld            # Root DCAT catalog
│   └── 📁 datasets/                 # DCAT dataset descriptions
│
├── 📁 checksums/                    # SHA-256 lineage & integrity tracking
│   ├── 🧾 raw/
│   ├── 🧾 processed/
│   └── 🧾 stac/
│
├── 📁 reports/                      # Validation, FAIR+CARE, audit, telemetry
│   ├── 🧾 self-validation/          # Schema, STAC/DCAT, CARE, checksum reports
│   ├── 🧾 telemetry/                # Sustainability & performance telemetry
│   └── 🧾 audit/                    # Governance & compliance audits
│
├── 📁 archive/                      # Versioned/superseded datasets (cold storage)
│   └── 📁 <year>/                   # Archived by year / major release
│
└── 📁 tmp/                          # Scratch; NEVER used as an input to production pipelines
~~~

Architectural guarantees:

- `raw/` is **immutable and append‑only**; changes must create new versions.  
- `processed/` is **deterministic** (raw + config + code → same result).  
- `stac/` and `dcat/` are **schema‑valid, governance‑approved catalogs**.  
- `checksums/` + `reports/` provide **verifiable integrity and governance evidence**.

---

## 🔄 Data Lifecycle & CI/CD Integration

KFM’s data lifecycle is a **governed pipeline** that aligns with MCP, the ETL architecture guides, and CI/CD workflows in `.github/workflows/`.

~~~mermaid
flowchart TD
  A["📁 sources/\nProvider manifests & upstream catalogs"]
    --> B["📁 raw/\nImmutable ingests (Git+DVC/LFS)"]

  B --> C["📁 work/\nCleaning · normalization · enrichment"]
  C --> D["📁 processed/\nDeterministic ETL outputs"]

  D --> E["📁 stac/\nSTAC Items & Collections"]
  D --> F["📁 dcat/\nDCAT Datasets & Distributions"]

  E --> G["📁 checksums/\nSHA-256 digests (raw/processed/stac)"]
  F --> G

  G --> H["📁 reports/self-validation/\nSchema · FAIR+CARE · provenance"]
  H --> I["Neo4j graph ingest\n(CIDOC · GeoSPARQL · OWL-Time · PROV-O)"]
  I --> J["Focus Mode · Story Nodes · Public Catalogs"]
~~~

**Workflow tie‑ins:**

- `.github/workflows/data_pipeline.yml`  
  - Validates ETL data contracts (KFM‑PDC v11).  
  - Confirms raw → work → processed transitions are reproducible and logged.
- `.github/workflows/stac_validate.yml` / `dcat_validate.yml` / `jsonld_validate.yml`  
  - Enforce STAC/DCAT/JSON‑LD & ontology correctness before merge.  
- `.github/workflows/faircare_validate.yml` / `h3_generalization.yml`  
  - Enforce FAIR+CARE, sovereignty flags, and spatial generalization.  
- `.github/workflows/sbom_verify.yml` / `telemetry_export.yml`  
  - Connect data artifacts to SBOMs and sustainability telemetry.

---

## 🌍 Spatial Architecture (CRS, Geometry, H3)

### CRS Policy

Canonical public CRS:

- **EPSG:4326 (WGS84)** for all published STAC and DCAT spatial extents and for most web‑facing geometry.

Permitted working CRSs (inside `work/` or intermediate steps):

- Equal‑area projections for areal statistics (e.g., EPSG:6933).  
- UTM for local‑scale precision tasks.  
- Historical CRSs for georeferenced legacy maps (recorded explicitly in metadata).

Rules:

- Every spatial dataset MUST:
  - Declare its CRS explicitly in metadata,  
  - Record any reprojection steps (source CRS → target CRS),  
  - Pass geometry validity checks (no self‑intersections, valid polygons, consistent `bbox`).

### H3 Generalization & Indexing

H3 is integral to:

- **Generalization** of sensitive locations (heritage, sacred sites, protected habitats).  
- **Aggregation and indexing** across multiple scales for dashboards and analytics.

Patterns:

- Public datasets that could expose sensitive sites MUST store only **H3 aggregated** coordinates (e.g., at a configured resolution), with raw coordinates retained only in governed, restricted contexts.  
- STAC/DCAT metadata indicate:
  - H3 resolution,  
  - Whether generalization has been applied,  
  - Any residual risk or masking notes.

Compliance is enforced by:

- `h3_masking_check.py` invoked in `h3_generalization.yml`.  

---

## ⏱ Temporal Architecture (OWL‑Time & Event Modeling)

Temporal representation uses **OWL‑Time** and KFM‑OP v11 patterns:

- Each dataset must define:
  - `temporal_start`, `temporal_end`,  
  - Optional uncertainty (e.g., `temporal_uncertainty`, `approximate` flags).

Mappings:

- **STAC**: `extent.temporal.interval` (Instant or Interval).  
- **DCAT**: `dct:temporal` (TimePeriod).  
- **Graph**: `time:Instant` and `time:Interval` nodes attached to datasets, features, and Story Nodes.

Implications:

- Focus Mode timelines are driven directly from these temporal objects.  
- Historical datasets can represent vague/approximate periods while remaining queryable (e.g., “late 19th century” modeled as a TimePeriod with uncertainty).

---

## 📊 Metadata Systems — STAC, DCAT, JSON‑LD

### STAC (KFM‑STAC v11 Profile)

- STAC is the **primary schema** for spatial & spatiotemporal assets.  
- `data/stac/` organizes:
  - Root `catalog.json`,  
  - Domain collections (hydrology, climate, hazards, landcover, missions, tabular),  
  - Items referencing assets in `processed/`.

KFM‑STAC v11 profile extends STAC with:

- `kfm_id` (stable internal identifier).  
- FAIR+CARE and sovereignty flags.  
- Lineage references (links to PROV‑O/OpenLineage documents and checksums).  
- Domain‑specific fields (e.g., hydrologic unit, climate variable codes).

Validation:

- Implemented via `.github/actions/stac-validate/` and `stac_validate.yml`.  
- Failures block merges to main/release branches.

### DCAT 3.0

- DCAT provides web‑native dataset descriptions for interoperability.  
- `data/dcat/catalog.jsonld` is the root; each dataset is described under `data/dcat/datasets/`.

Mappings:

- STAC `collection.id` → `dcat:Dataset` `dct:identifier`.  
- STAC Item assets → DCAT `dcat:Distribution`.  
- Licenses → `dct:license`.  
- Access constraints, CARE flags, and sovereignty notes recorded in DCAT as annotations and additional properties.

### JSON‑LD & Ontologies

Core ontologies:

- CIDOC‑CRM — cultural/historical entities.  
- GeoSPARQL — spatial relationships.  
- OWL‑Time — temporal entities/intervals.  
- PROV‑O — provenance (Entities, Activities, Agents).  
- KFM‑OP v11 — KFM‑specific domain types and roles.

JSON‑LD contexts:

- Ensure that STAC/DCAT metadata can be ingested directly into the graph.  
- Encode FAIR+CARE, sovereignty policies, and risk categories as machine‑readable properties.

---

## 🧮 ETL Architecture & Data Contracts

Pipelines live primarily under `src/pipelines/` and are governed by **KFM‑PDC v11** and `data_contract_ref`:

- **Extract**  
  - Ingest from external sources into `data/raw/` and/or `data/sources/`.  
  - Capture source manifests and initial checksums.

- **Transform**  
  - Normalize schemas into `data/work/tables/` and `data/work/spatial/`.  
  - Apply cleaning, harmonization, enrichment, and derived metrics.  
  - Enforce column‑level contracts (types, ranges, nullability).

- **Load**  
  - Emit deterministic products to `data/processed/**`.  
  - Generate STAC Items/Collections and DCAT datasets.  
  - Trigger lineage & telemetry emission.

Data contracts:

- Stored in `../docs/contracts/` and/or `config/data_contracts/`.  
- Define allowed field sets, encodings, and quality thresholds.  
- Enforced by `validate_pipelines.py` and `data_pipeline.yml`.

Reproducibility:

- Every ETL run must be re‑runnable given:
  - Raw data versions (DVC + checksums),  
  - ETL config,  
  - Containerized environment (e.g., Docker image tags),  
  - Pipeline commit hash.

---

## 🧬 Lineage Architecture (PROV‑O & OpenLineage)

Lineage is modeled at two layers:

1. **Logical provenance (PROV‑O + JSON‑LD)**  
   - Datasets, tables, layers → `prov:Entity`.  
   - Pipeline runs, AI transforms, manual curation → `prov:Activity`.  
   - Automation, services, human maintainers → `prov:Agent`.  

2. **Execution‑level lineage (OpenLineage)**  
   - Each ETL or model run emits OpenLineage events (jobs, runs, inputs, outputs).  
   - These events can be replayed to understand how a given artifact was produced.

Storage:

- JSON/JSON‑LD lineage documents under `data/reports/audit/` and `data/reports/self-validation/lineage/`.  
- Summaries and time‑series metrics in telemetry outputs (`focus-telemetry.json`).  
- Graph representation in Neo4j for queryable lineage (e.g., “what raw sources contributed to this Story Node?”).

Guarantees:

- Every production dataset in `processed/` that feeds UI/graphs must have:
  - A discoverable PROV‑O trace, and  
  - At least one OpenLineage run record for its generating pipelines.

---

## 🧠 AI & Enrichment Architecture

AI/ML is used to **augment** — not silently replace — data:

Use cases:

- OCR and layout analysis for historical documents and maps.  
- NLP entity extraction (places, people, events) from textual sources.  
- Derived indices (e.g., drought indices from multi‑source climate data).  
- Pre‑aggregation and summarization for Focus Mode & Story Nodes.

Constraints:

- All AI‑derived products must:
  - Be materialized in `data/work/` or `data/processed/` with AI‑specific metadata,  
  - Record model details (name, version, provider, seed where relevant),  
  - Capture training data provenance at a sensible level of abstraction,  
  - Be clearly labeled as AI‑derived in STAC/DCAT and graph metadata.

Governance:

- AI behavior and model deployment are gated by `ai_behavior_check.yml` and `focusmode_mlops.yml`.  
- High‑impact AI transforms (e.g., classification of heritage sites) may require explicit FAIR+CARE and sovereignty council review.

---

## ⚖ FAIR+CARE & Sovereignty in the Data System

FAIR+CARE and sovereignty are **first‑class architecture concerns**, not post‑hoc labels.

Enforcement points:

- **Ingestion**  
  - Data in `sources/` and `raw/` includes license and sovereignty notes.  
  - Early tagging of sensitive or sovereign datasets.

- **Transformation**  
  - Aggregation/generalization for sensitive locations.  
  - Removal or obfuscation of PII/PHI.

- **Publication**  
  - Public datasets appear only in catalogs once FAIR+CARE and sovereignty checks pass.  
  - H3 or other masks applied for any high‑risk coordinates.

- **Exposure**  
  - APIs and UI layers respect flags indicating:
    - Usage constraints,  
    - Attribution requirements,  
    - Contact points for data stewards.

Violations:

- CI pipelines block merges when:
  - Required CARE labels or sovereignty flags are missing,  
  - Sensitive spatial precision is detected in public domains.

---

## 🌱 Sustainability & Telemetry Architecture

KFM treats **sustainability telemetry** as part of the data system:

Metrics captured:

- `energy_wh` — energy consumed by ETL/model runs,  
- `carbon_gco2e` — estimated emissions,  
- Workload metrics (`records_processed`, `bytes_processed`, `compute_time_s`).

Where stored:

- `data/reports/telemetry/` (data‑plane view),  
- Versioned release telemetry (e.g., `../releases/v11.2.3/focus-telemetry.json`).

Governance:

- Telemetry informs:
  - ETL scheduling decisions (e.g., off‑peak windows),  
  - Optimization priorities (e.g., materializing expensive joins vs. caching),  
  - FAIR+CARE stewardship discussions where data processing may impact energy budgets.

---

## 📈 Data Quality & Fitness‑for‑Use

Quality controls draw from ISO 19157‑style dimensions:

- **Completeness** — coverage & missingness.  
- **Logical consistency** — referential integrity, valid code lists.  
- **Positional accuracy** — spatial precision and error models.  
- **Temporal accuracy** — correct timestamps, intervals, and chronology.  
- **Thematic accuracy** — correctness of classifications and labels.

Outputs:

- Stored under `data/reports/self-validation/quality/`.  
- Summaries can be attached to STAC Collections and DCAT Datasets as quality notes.  
- Focus Mode and Story Nodes use this information to:
  - Qualify narratives with confidence levels,  
  - Avoid over‑claiming precision where quality is low.

---

## 🧩 Ontology & Entity Classes

Core data‑layer entity classes and mappings:

| KFM Entity    | Description                              | CIDOC       | Schema.org     | DCAT              | PROV‑O     |
|---------------|------------------------------------------|-------------|----------------|-------------------|-----------|
| Dataset       | Logical grouped data product             | E73         | Dataset        | dcat:Dataset      | Entity    |
| Distribution  | Particular file/asset of a dataset       | E73         | DataDownload   | dcat:Distribution | Entity    |
| Feature       | Spatial feature (vector)                 | E53 Place   | Place          | n/a               | Entity    |
| RasterLayer   | Spatial raster layer                     | E36/E73     | Dataset        | Distribution      | Entity    |
| Table         | Tabular dataset                          | E73         | Dataset        | Distribution      | Entity    |
| SensorStream  | Time‑series sensor stream                | E16/E73     | Dataset        | Dataset           | Entity    |

These are reflected in:

- STAC & DCAT metadata,  
- JSON‑LD context mappings,  
- Graph labels and relationship types.

---

## 🔗 STAC/DCAT → Graph Mapping

Canonical mappings into Neo4j:

- STAC `collection.id` → `(:Dataset {kfm_id, stac_id})`.  
- STAC `item.id` → `(:DatasetInstance {kfm_item_id})` or `(:Distribution)` depending on design.  
- STAC `geometry` → `(:Geometry)` with GeoSPARQL WKT/GeoJSON and relationships like `:HAS_GEOMETRY`.  
- DCAT `dct:identifier` → `Dataset.kfm_id`.  
- DCAT `dcat:distribution` → `(:Distribution)` nodes pointing at STAC assets.  
- OWL‑Time intervals → `(:TimeInterval)` connected by `:HAS_TEMPORAL_EXTENT`.  
- PROV‑O lineage → `(:Entity)-[:wasGeneratedBy]->(:Activity)-[:used]->(:Entity)`.

This ensures a **continuous semantic path** from on‑disk files in `data/**` to knowledge graph nodes used by Focus Mode and Story Nodes.

---

## 🧰 Validation Toolchain & CI Hooks

Validation is not optional — it is embedded in architecture:

Components:

- Schema validation (JSON Schema, SHACL, table contracts).  
- STAC/DCAT/JSON‑LD validators (`stac-validate`, `dcat-validate`, `schema-validate`).  
- FAIR+CARE & sovereignty checks (`run_faircare_checks.py`, `h3_masking_check.py`).  
- Checksum verifiers (matching `checksums/` vs. actual files and manifests).  
- Quality assessment tools (e.g., Great Expectations‑style tests).  
- Telemetry summarizers.

CI pipelines:

- Merges to `main`/`release/**` branches are blocked when critical validation fails.  
- Data‑touching PRs should expect:
  - `data_pipeline.yml`,  
  - `stac_validate.yml`,  
  - `dcat_validate.yml`,  
  - `jsonld_validate.yml`,  
  - `faircare_validate.yml`,  
  - `h3_generalization.yml`  
  to run as appropriate.

---

## 🧭 Contributor Workflow (Data Architecture)

When you:

- **Add a new dataset**, or  
- **Extend the data architecture**, or  
- **Introduce a new domain folder under `processed/` or `stac/`**,

you should:

1. Place files in the **correct subdirectory** under `data/`.  
2. Update or add:
   - STAC Collection/Items in `data/stac/**`,  
   - DCAT Dataset record(s) in `data/dcat/datasets/`.  
3. Define or update **data contracts** in `../docs/contracts/` or config.  
4. Ensure FAIR+CARE & sovereignty metadata are set correctly.  
5. Run local validations where possible (schema, STAC/DCAT, FAIR+CARE, H3).  
6. Submit a PR and respond to:
   - CI failures,  
   - Governance/FAIR+CARE comments,  
   - Architecture review requests.

---

## 🕰️ Version History

| Version | Date       | Summary                                                                                                                                            |
|--------:|------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| v11.2.3 | 2025-12-09 | Aligned with KFM-MDP v11.2.5; synced layout with `data/README.md`; tightened ontology alignment; clarified CI hooks, DVC/lineage semantics, and AI/FAIR+CARE wiring. |
| v11.2.2 | 2025-11-27 | Canonicalized directory layout; added telemetry/schema references; integrated STAC/DCAT/JSON‑LD and checksums into architecture narrative.        |
| v11.0.0 | 2025-11-19 | Initial v11 data system architecture; defined raw→work→processed lifecycle, baseline governance, and ETL patterns.                               |

---

<div align="center">

🗄️ **Kansas Frontier Matrix — Data System Architecture (v11.2.3)**  
Data‑First · FAIR+CARE‑Governed · Provenance‑Aware  

© 2025 Kansas Frontier Matrix — MIT License  
MCP‑DL v6.3 · KFM‑MDP v11.2.5 · KFM‑OP v11.0  

[⬅ Back to Data Overview](README.md) ·  
[⬅ Back to Repository Root](../README.md) ·  
[⚖ Governance Charter](../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>