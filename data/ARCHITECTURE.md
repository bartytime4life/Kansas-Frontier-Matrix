---
title: "🗄️ Kansas Frontier Matrix — Data System Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/ARCHITECTURE.md"

# Versioning & Release
version: "v11.0.0"
last_updated: "2025-11-19"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"

# Integrity & Provenance
commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:doc:data-architecture-v11.0.0"
semantic_document_id: "kfm-doc-data-architecture"
event_source_id: "ledger:data/ARCHITECTURE.md"
immutability_status: "version-pinned"

# Release Artifacts
sbom_ref: "../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../releases/v11.0.0/manifest.zip"
telemetry_ref: "../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../schemas/telemetry/data-architecture-v2.json"
energy_schema: "../schemas/telemetry/energy-v2.json"
carbon_schema: "../schemas/telemetry/carbon-v2.json"
data_contract_ref: "../docs/contracts/data-contract-v3.json"

# Governance & Ethics
governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

# Document Classification
status: "Active / Enforced"
doc_kind: "Architecture"
intent: "data-system-architecture"
role: "data-platform-architecture"
category: "Data · ETL · Governance · FAIR+CARE"

# FAIR + CARE
fair_category: "F1-A1-I1-R1"
care_label: "Variable — Dataset Dependent"
sensitivity_level: "Mixed"
public_exposure_risk: "Dataset-level"
indigenous_rights_flag: "Dataset-level"
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: false

# Ontology Alignment
ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../schemas/json/data-architecture.schema.json"
shape_schema_ref: "../schemas/shacl/data-architecture-shape.ttl"

# AI Usage
ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified historical claims"

# Accessibility & Lifecycle
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Varies by dataset"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next data-platform architecture update"
---

<div align="center">

# 🗄️ **Kansas Frontier Matrix — Data System Architecture**  
`data/ARCHITECTURE.md`

**Purpose**  
Define the **complete v11 architecture** for KFM data ingestion, storage, governance, validation, lineage, STAC/DCAT catalogs, AI enrichment, and graph loading.  

This document is the **canonical reference** for all contributors touching `data/**`:
- ETL engineers  
- AI/ML practitioners  
- GIS specialists  
- Governance & FAIR+CARE reviewers  
- Focus Mode architects  

It is designed to be **machine-readable**, **governance-enforced**, and **GitHub-safe**.

</div>

---

## 1. 📘 High-Level Overview

The KFM Data System:

- Integrates **heterogeneous historical, environmental, cultural, and geologic data**  
- Normalizes it to a **common spatial, temporal, and semantic frame**  
- Encodes it in **STAC/DCAT/JSON-LD** with FAIR+CARE governance metadata  
- Loads it into a **Neo4j knowledge graph** aligned with CIDOC-CRM, GeoSPARQL, OWL-Time, PROV-O, and KFM-OP v11  
- Tracks **lineage, integrity, governance decisions, and sustainability metrics**  
- Exposes results to **Focus Mode**, Story Nodes v3, and public-facing catalogs  

Core goals:

- Reproducible ETL  
- Transparent governance  
- Ethical and sovereign data use  
- Robust sustainability reporting  
- Seamless integration with KFM’s AI and visualization layers  

---

## 2. 🧱 Data System Directory Architecture

The `data/` tree is the **physical backbone** of the data platform.

~~~~text
data/
├── ARCHITECTURE.md             ← this document
├── README.md                   ← user-facing data overview
│
├── raw/                        ← original source datasets (immutable)
│   ├── hydrology/
│   ├── geology/
│   ├── history/
│   ├── remote-sensing/
│   └── sovereignty/
│
├── staging/                    ← cleaned & normalized intermediates
│   ├── tables/                 ← CSV/Parquet after normalization
│   ├── spatial/                ← GeoJSON, GPKG, temporary tiles
│   └── metadata/               ← pre-STAC/DCAT JSON/JSON-LD
│
├── processed/                  ← ETL outputs ready for publication/graph
│   ├── hydrology/
│   ├── climate/
│   ├── ecology/
│   ├── historical/
│   └── storynodes/
│
├── stac/                       ← STAC Items & Collections
│   ├── items/
│   ├── collections/
│   └── catalog.json
│
├── dcat/                       ← DCAT 3.0 JSON-LD datasets & catalogs
│
├── checksums/                  ← SHA-256 lineage & integrity tracking
│   ├── raw/
│   ├── processed/
│   └── stac/
│
├── reports/                    ← validation, FAIR+CARE, and quality outputs
│   ├── self-validation/
│   └── telemetry/
│
├── archive/                    ← retired or superseded datasets (versioned)
│
└── work/                       ← scratch / dev-only staging (not production)
~~~~

Key architectural guarantees:

- **`raw/` is append-only and immutable**  
- **`processed/` is deterministic** (recomputed from raw + configs)  
- **`stac/` and `dcat/` are always schema-valid**  
- **`checksums/` and `reports/` are governance-enforced**  

---

## 3. 🔄 End-to-End Data Lifecycle

The Data System follows a **multi-phase lifecycle**.

~~~~mermaid
flowchart TD
  A["raw/\n(immutable sources)"]
    --> B["staging/\n(cleaning & normalization)"]
  B --> C["processed/\n(ETL products)"]
  C --> D["stac/ + dcat/\n(metadata catalogs)"]
  D --> E["checksums/\nSHA-256 lineage"]
  E --> F["reports/\nself-validation + FAIR+CARE"]
  F --> G["graph ingest\n(Neo4j · CIDOC-CRM · GeoSPARQL · PROV-O)"]
  G --> H["Focus Mode · Story Nodes · Public Catalogs"]
~~~~

Phases:

1. **Ingest & Capture (raw/)**  
2. **Clean & Normalize (staging/)**  
3. **Transform & Harmonize (processed/)**  
4. **Catalog (stac/, dcat/)**  
5. **Verify & Govern (checksums/, reports/)**  
6. **Load & Publish (graph, portals, Focus Mode)**  

Each phase has **strict entry/exit criteria** enforced by CI/CD and governance workflows.

---

## 4. 🌍 Spatial Architecture (CRS, Tilings, H3)

### 4.1 Coordinate Reference Systems

Canonical CRS:

- **EPSG:4326** (WGS84) for all STAC & DCAT spatial extents  
- Support for additional CRSs at processing stage:
  - Equal-area projections for statistics  
  - UTM for local geometries  
  - Custom CRSs for legacy maps, with explicit transforms  

All published spatial products must:

- Declare CRS  
- Document transform steps  
- Validate geometry integrity  

### 4.2 H3 Integration

H3 is used for:

- Sensitive site generalization  
- Multi-scale aggregation  
- Efficient spatial indexing  

Rules:

- Culturally sensitive or restricted features → stored as generalized H3 cells in public layers  
- High-resolution geometries only accessible in governed contexts (non-public, with explicit approvals)  

---

## 5. ⏱ Temporal Architecture (OWL-Time Alignment)

Temporal data is modeled using OWL-Time and KFM’s temporal norms:

- Every dataset must specify:
  - `temporal_start`  
  - `temporal_end`  
  - Optional uncertainty bounds  

STAC and DCAT mapping:

- STAC → `extent.temporal.interval`  
- DCAT → `dct:temporal`  

Events and processes in the graph:

- Use `time:Instant` or `time:Interval`  
- Map to CIDOC events over time ranges  
- Support historical calendar nuances where needed  

---

## 6. 📊 Metadata Systems (STAC, DCAT, JSON-LD)

### 6.1 STAC

Requirements:

- STAC Items for spatial assets (rasters, vectors, tiles)  
- STAC Collections for grouped datasets  
- STAC Catalog as root index  

Paths:

- Items: `data/stac/items/`  
- Collections: `data/stac/collections/`  
- Root catalog: `data/stac/catalog.json`  

### 6.2 DCAT

DCAT 3.0 JSON-LD used for:

- High-level dataset descriptions  
- Distributions and access URLs  
- Licensing and rights statements  

Paths:

- `data/dcat/*.jsonld`  

### 6.3 JSON-LD Contexts

Custom KFM context includes:

- `kfm_id` for stable dataset IDs  
- CARE metadata for sovereignty and ethics  
- PROV-O, CIDOC-CRM, GeoSPARQL references  

---

## 7. 🧠 AI / Enrichment Architecture

AI pipelines:

- OCR for scanned documents and maps  
- NER and entity linking for treaties, events, people, places  
- Topic modeling and clustering for Story Node enrichment  
- Predictive modeling (e.g., climate/hydrology projections)  

All AI-derived products in `data/processed/` must include:

- Model name + version  
- Training dataset references  
- Limitations and known risks  
- AI-driven fields clearly labeled  

AI metrics stored in:

- `data/reports/self-validation/ai/`  
- `docs/reports/audit/ai_model_audits.json`  

---

## 8. 🧮 ETL Architecture (Pipelines)

Pipelines live under `src/pipelines/**` and use `data/**` as their storage backbone.

High-level ETL stages:

1. **Extract** → copy or stream into `data/raw/`  
2. **Transform** → normalize into `data/staging/` and then `data/processed/`  
3. **Load** → push to `data/stac/`, `data/dcat/`, and then graph  

All pipelines must:

- Be deterministic (no external randomness without seeds)  
- Log transformations and decisions  
- Write validation results to `data/reports/self-validation/`  

---

## 9. 🧬 Lineage & PROV-O Architecture

Lineage is described via PROV-O:

- Entities: datasets, files, derived layers (prov:Entity)  
- Activities: ETL runs, AI inferences (prov:Activity)  
- Agents: pipelines, operators, institutions (prov:Agent)  

Exports stored in:

- `data/lineage/prov/` (if present; or equivalent namespace)  
- `docs/reports/audit/data_provenance_ledger.json`  

Lineage rules:

- Every major transformation must include:
  - Source datasets  
  - Parameters/configs  
  - Tool and version  
  - Time of execution  

Checksums support lineage verification (see checksums/).

---

## 10. ⚖️ Governance, FAIR+CARE & Sovereignty

FAIR+CARE governance is applied **per dataset** and **per transformation**.

Governance artifacts:

- CARE metadata stored alongside STAC/DCAT  
- Governance decisions logged to `docs/reports/audit/governance-ledger.json`  
- Indigenous data flagged via `indigenous_rights_flag` in STAC/DCAT extensions  

Rules:

- No sensitive Indigenous or cultural data is published without explicit governance review  
- Masking/generalization must be applied as per `sovereignty_policy` configs  

---

## 11. 🌱 Sustainability & Telemetry Architecture

Sustainability metrics include:

- Energy per ETL run (Wh)  
- Carbon estimates (gCO₂e)  
- Storage usage  
- Data and model drift indicators  

Telemetry stored in:

- `data/reports/telemetry/`  
- `releases/<version>/focus-telemetry.json`  

Collected from:

- CI/CD workflows  
- Validation tools  
- Runtime measurement hooks  

---

## 12. 📈 Data Quality & ISO 19157

Quality dimensions:

- Completeness  
- Consistency  
- Accuracy  
- Timeliness  
- Validity  

Metrics recorded in:

- `data/reports/self-validation/quality/`  

Validated against:

- ISO 19157 quality measures  
- Internal KFM rules for each dataset type  

---

## 13. 🧩 Data Ontology — Entity Classes

This section defines the **data ontology** for KFM’s data layer.  

Each class is mapped to:

- CIDOC-CRM  
- DCAT  
- Schema.org  
- PROV-O  
- GeoSPARQL  

### 13.1 Core Entities

| KFM Entity        | Description                          | CIDOC-CRM | Schema.org | DCAT      | GeoSPARQL | PROV-O   |
|-------------------|--------------------------------------|-----------|------------|-----------|-----------|----------|
| Dataset           | Logical dataset                      | E73       | Dataset    | dcat:Dataset | n/a     | Entity   |
| Layer             | Spatial layer (raster/vector)        | E36/E53   | Dataset    | dcat:Distribution | FeatureCollection | Entity |
| Feature           | Individual spatial feature           | E53       | Place      | n/a       | Feature   | Entity   |
| Scan              | Image of document/map                | E38       | ImageObject| dcat:Distribution | n/a  | Entity   |
| RasterTile        | Tiled raster asset (COG tile, etc.)  | E36/E73   | Dataset    | dcat:Distribution | n/a | Entity   |
| Table             | Tabular dataset (Parquet, CSV)       | E73       | Dataset    | dcat:Distribution | n/a | Entity   |
| StoryNodeData     | Data slice used by Story Nodes       | E31/E73   | CreativeWork | n/a      | FeatureCollection | Entity |
| SensorStream      | Time-series sensor data              | E16       | Dataset    | dcat:Dataset | n/a   | Entity   |

---

## 14. 🔗 Ontology Property Mapping (STAC/DCAT → Graph)

Mapping examples:

- STAC `id` → `kfm_id` (graph node)  
- STAC `properties.datetime` → OWL-Time `time:Instant`  
- STAC `bbox` → GeoSPARQL `geosparql:hasGeometry`  
- DCAT `dct:license` → PROV-O / license property on Dataset  
- DCAT `dct:temporal` → OWL-Time Interval on Dataset  

This ensures **semantic continuity** from `data/**` to the graph layer.

---

## 15. 🧮 STAC/DCAT Promotion Flow

Promotion from `raw/` to STAC/DCAT:

1. Dataset ingested into `raw/`  
2. Cleaned/normalized into `staging/`  
3. Processed into `processed/`  
4. STAC Item + Collection generated under `stac/`  
5. DCAT Dataset created under `dcat/`  
6. Validation & governance checks run (schema + FAIR+CARE)  
7. Telemetry & lineage recorded  
8. Graph ingestion authorized  

---

## 16. 🧰 Validation Tool Integration

Validation tools from `tools/validation/` integrate with `data/**`:

- `schema_check.py` → validates STAC/DCAT + contracts  
- `faircare_validator.py` → inspects CARE & license metadata  
- `checksum_audit.py` → ensures SHA-256 chain integrity  
- `ai_explainability_audit.py` → AI metrics for enriched datasets  

Architecture ensures that **no dataset** is promoted without:

- Schema validity  
- Governance approval (where needed)  
- Integrity guarantees  

---

## 17. 🔁 ETL & Data System in CI/CD

`.github/workflows/*` enforce:

- Data schema validation on PRs touching `data/**`  
- Governance routing for CARE-sensitive data  
- Telemetry export for ETL workloads  
- Dependency and security checks for ETL tools  

Data System architecture is **tightly coupled** with CI/CD via:

- STAC/DCAT validators  
- FAIR+CARE validators  
- Telemetry exporters  

---

## 18. 🔍 Observability & Dashboards

Observability provides:

- ETL run histories  
- Validation pass/fail trends  
- Governance decisions over time  
- Energy and carbon metrics by pipeline  
- Data drift over time and geography  

Dashboards read from:

- `docs/reports/telemetry/`  
- `docs/reports/audit/`  
- `releases/*/focus-telemetry.json`  

---

## 19. 🧭 Contributor Workflow

For data contributors:

1. Propose new dataset via `data_submission` issue template  
2. Add files under `data/raw/` or `data/staging/`  
3. Implement or update ETL pipeline under `src/pipelines/**`  
4. Run local validation (where possible)  
5. Open PR  
6. Let CI/CD handle validation, governance, and telemetry  
7. Resolve any validation or governance issues  

All steps must be tracked through PR templates and CI reports.

---

## 20. 🕰️ Version History

| Version | Date       | Summary                                                                                     |
|--------:|------------|---------------------------------------------------------------------------------------------|
| v11.0.0 | 2025-11-19 | Full v11 data system rebuild; added ontology tables, sustainability, governance, and CI/CD coupling. |
| v10.4.0 | 2025-11-15 | v10.4 data architecture; lifecycle & governance integration.                               |
| v10.3.2 | 2025-11-14 | Added drift + sustainability tracking and extended provenance.                             |
| v10.0.0 | 2025-11-10 | Initial data platform architecture under v10.                                              |

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT License**  
Data System Architecture · FAIR+CARE Certified  
MCP-DL v6.3 · KFM-MDP v11.0 · KFM-OP v11.0 · Diamond⁹ Ω / Crown∞Ω  

[Back to Data Overview](README.md) · [Repository Root](../README.md) · [Governance Charter](../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
