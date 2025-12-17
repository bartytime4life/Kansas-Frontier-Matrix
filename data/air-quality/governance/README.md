---
title: "Air Quality Data Domain — Governance README"
path: "data/air-quality/governance/README.md"
version: "v1.0.0"
last_updated: "2025-12-17"
status: "draft"
doc_kind: "Guide"
license: "CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP-DL v6.3"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v11.0.0"
dcat_profile: "KFM-DCAT v11.0.0"
prov_profile: "KFM-PROV v11.0.0"

governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:data:air-quality:governance:readme:v1.0.0"
semantic_document_id: "kfm-data-air-quality-governance-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:air-quality:governance:readme:v1.0.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# Air Quality Data Domain — Governance README

## 📘 Overview

### Purpose
- Define governance requirements for **adding, processing, and publishing** air-quality datasets under `data/air-quality/`.
- Ensure all air-quality outputs are **reproducible**, **cataloged (STAC/DCAT)**, and **lineage-tracked (PROV-O)** before they are used downstream (graph → APIs → UI → Story Nodes → Focus Mode).
- Provide a domain entry-point for reviewers to assess **license**, **sensitivity**, **quality signals**, and **provenance completeness**.

### Scope
| In Scope | Out of Scope |
|---|---|
| Domain-specific expectations for air-quality inputs/outputs, folder layout, validation expectations, and STAC/DCAT/PROV deliverables. | Implementing ETL code, changing ontology/schema contracts, or modifying API/UI behavior (those require separate governed docs). |
| Sensitivity/redaction expectations for location/time-series air-quality data. | Defining new project-wide governance policies (see `docs/governance/*`). |
| Minimum metadata fields and provenance linkages required for publishable artifacts. | Narrative authoring rules for Story Nodes (see Story Node templates/docs). |

### Audience
- Primary: Data contributors, ETL/pipeline maintainers, data reviewers.
- Secondary: Graph/API maintainers, UI/story authors who need to understand dataset fitness.

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Observation**: a measured or derived value for a pollutant/indicator at a time (and optionally a location).
  - **Station / Monitor / Sensor**: a fixed (or mobile) measurement source with a known geometry and metadata.
  - **Derived product**: any computed artifact (e.g., aggregates, interpolations, indices) produced from raw observations.
  - **STAC/DCAT/PROV**: catalogs and lineage artifacts required by KFM for discovery and auditability.

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This governance README | `data/air-quality/governance/README.md` | Data domain maintainers | Entry point for air-quality governance. |
| Master Guide (pipeline ordering + extension matrix) | `docs/MASTER_GUIDE_v12.md` | Core maintainers | Canonical ordering: ETL → catalogs → graph → APIs → UI → Story Nodes → Focus Mode. |
| Global governance & ethics | `docs/governance/*` | Governance owners | Authoritative policies for sovereignty/ethics/security. |
| STAC/DCAT/PROV profiles | `data/stac/` + `docs/data/` | Catalog owners | Canonical locations for catalogs and mappings. |
| Domain schemas (if/when defined) | `schemas/` | Schema owners | Add only after schema/ontology review. |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Any domain-specific “rules” here point to the canonical governance docs (`docs/governance/*`) rather than redefining them
- [ ] Validation expectations are listed and repeatable (even if the exact commands live elsewhere)
- [ ] Sensitivity + CARE/sovereignty considerations are explicitly stated for air-quality location/time-series data
- [ ] Open questions are tracked with an owner (or explicitly marked TBD)

## 🗂️ Directory Layout

### This document
- `path`: `data/air-quality/governance/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Air-quality domain | `data/air-quality/` | Domain-scoped data + governance artifacts |
| Domain governance | `data/air-quality/governance/` | This README + domain review notes/checklists |
| Domain staged data | `data/air-quality/raw/` / `work/` / `processed/` | Domain-specific raw → intermediate → publishable outputs (see “Constraints” for layout decision) |
| STAC/DCAT/PROV catalogs | `data/stac/` + `docs/data/` | Catalog generation outputs + mappings |
| Pipelines | `src/pipelines/` + `docs/pipelines/` | ETL + transforms + catalog build docs (if/when implemented for air-quality) |
| Schemas | `schemas/` | JSON schemas (domain + telemetry) |
| Security policy | `.github/SECURITY.md` + `docs/security/` | Security requirements and technical standards |
| MCP logs/experiments | `mcp/` | Run logs, experiments, SOPs (location depends on project convention) |

### Expected file tree for this sub-area
~~~text
📁 data/
  📁 air-quality/
    📁 governance/
      📄 README.md
      📄 (optional) intake_checklist.md
      📄 (optional) dataset_registry.(yml|yaml|json)
    📁 raw/
      📄 (inputs land here; immutable snapshots preferred)
    📁 work/
      📄 (intermediate transforms; safe to delete/regenerate)
    📁 processed/
      📄 (publishable, versioned, schema-aligned outputs)
    📁 (optional) stac/
      📄 (local staging only; canonical catalogs live under data/stac/)
~~~

## 🧭 Context

### Background
- Air-quality datasets (stations, observations, derived indicators) are time-sensitive and can be high-volume.
- KFM requires that any data used for graph- or narrative-facing outputs be **discoverable (cataloged)** and **auditable (provenance complete)**.

### Assumptions
- Air-quality data may be ingested as:
  - station metadata (static-ish)
  - observation time series (high-frequency)
  - derived products (aggregations, indices, rasters, anomalies)
- This domain may start with “catalog-only” integration (Data + Catalog) before graph/API/UI wiring, per the Master Guide “Extension Matrix”.

### Constraints / invariants
- **Pipeline ordering is preserved:** ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode.
- **Frontend consumes contracts via APIs** (no direct graph dependency).
- **Reproducibility:** processed outputs must be regenerable from raw + configs + pinned tool versions (where applicable).
- **Licensing:** every dataset must have clear license/terms captured in metadata before publishing any derivative.
- **Sovereignty & sensitivity:** if any inputs contain sensitive location signals, apply redaction/generalization rules from `docs/governance/SOVEREIGNTY.md` and security standards.

> Practical intake rule-of-thumb for this domain:
> 1) Register source + license → 2) land raw snapshot → 3) normalize to processed outputs → 4) generate STAC/DCAT/PROV → 5) validate → 6) only then allow downstream use.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Confirm whether this repo uses **domain-local** staging (`data/air-quality/{raw,work,processed}`) vs **global stage dirs** with a domain subfolder. | TBD | TBD |
| Define/confirm canonical output formats (e.g., GeoParquet vs GeoPackage vs CSV/Parquet) for air-quality time series + station layers. | TBD | TBD |
| Determine whether any air-quality sources include sensitive locations requiring generalization at publish time. | TBD | TBD |

### Future extensions
- Add derived “evidence products” (e.g., anomaly episodes, spatial aggregations) with explicit PROV activities and quality metrics.
- Add optional graph entities (stations, observations, episodes) if/when product requirements justify graph/API/UI integration.
- Add telemetry signals for ingestion quality (completeness, lag, schema drift).

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  subgraph AirQualityDomain["Air Quality Domain (data/air-quality/)"]
    R["Raw inputs<br/>data/air-quality/raw/"] --> W["Work / staging<br/>data/air-quality/work/"]
    W --> P["Processed outputs<br/>data/air-quality/processed/"]
  end

  P --> C["STAC/DCAT/PROV catalogs<br/>data/stac/ + docs/data/"]
  C --> G["Neo4j Graph (optional)<br/>src/graph/"]
  G --> A["APIs (optional)<br/>src/server/"]
  A --> U["UI / Map (optional)<br/>web/"]
  U --> S["Story Nodes (optional)<br/>docs/reports/.../story_nodes/"]
  S --> F["Focus Mode (optional)"]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant UI
  participant API
  participant Graph
  UI->>API: Query air-quality layer / narrative context
  API->>Graph: fetch entities + provenance refs (optional)
  Graph-->>API: context bundle
  API-->>UI: data + citations + audit flags
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Station / monitor metadata | CSV / GeoJSON / GeoPackage | Registered source (TBD) | Unique IDs, geometry validity, required fields present |
| Observation time series | CSV / JSON / Parquet / API extract | Registered source (TBD) | Time parsing, units present, non-negative where applicable, QA flags preserved |
| Derived surfaces / indicators (optional) | GeoTIFF / NetCDF / Parquet | Registered source or KFM-derived | CRS/extent checks, nodata handling, range checks, provenance complete |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Normalized stations layer | GeoParquet / GeoPackage / GeoJSON | `data/air-quality/processed/stations/` | TBD (recommend: `schemas/air-quality/stations.*`) |
| Normalized observations | Parquet / CSV | `data/air-quality/processed/observations/` | TBD (recommend: `schemas/air-quality/observations.*`) |
| Derived products (optional) | Parquet / GeoTIFF / GeoJSON | `data/air-quality/processed/derived/` | TBD (recommend: `schemas/air-quality/derived.*`) |
| STAC Items / Collections | JSON | `data/stac/` (recommended subfolder: `air-quality/`) | STAC core + KFM profile + approved extensions |
| DCAT dataset record(s) | RDF/JSON-LD/Turtle (project choice) | `docs/data/` | KFM-DCAT profile |
| PROV activities/entities | JSON-LD/Turtle (project choice) | `docs/data/` | KFM-PROV profile |

### Sensitivity & redaction
- Air-quality sources can embed sensitive signals via:
  - precise sensor locations (especially non-regulatory/community sensors)
  - timestamps that allow re-identification when combined with other datasets
- If sensitivity is identified by governance review or source terms:
  - publish only generalized geometries (grid/area-level) or omit coordinates from public outputs
  - ensure provenance remains valid while sensitive fields are redacted (publish “public provenance” where needed)

### Quality signals
Define and log at least the following checks for publishable outputs:
- **Completeness:** expected temporal coverage vs missingness
- **Value ranges:** pollutant values within plausible bounds; no impossible negatives (where applicable)
- **Unit normalization:** units preserved or normalized with explicit mapping
- **Geometry validity:** valid points/polygons, consistent CRS assumptions for published assets
- **De-duplication:** no duplicate station IDs; no duplicate time records per (station, pollutant, datetime)
- **Schema drift:** detect and document upstream field changes
- **Provenance completeness:** every processed output points to raw input(s) + the activity that generated it

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections involved:
  - `air-quality` (recommended top-level domain collection; exact IDs TBD)
  - optional sub-collections for stations/observations/derived products
- Items involved:
  - one item per publishable asset or partition (e.g., by date range, region, station group), depending on volume
- Extension(s):
  - **STAC Versioning Extension** is required for updates
  - use only approved STAC extensions (e.g., projection/raster/vector) when applicable; otherwise require schema/ontology review for custom fields

### DCAT
- Dataset identifiers:
  - Must be stable and consistent with STAC collection identifiers (mapping documented in `docs/data/`)
- License mapping:
  - Must map source license/terms to DCAT license metadata for each dataset/distribution
- Contact / publisher mapping:
  - Capture publisher/maintainer where available; avoid embedding personal emails/PII in public outputs unless policy allows

### PROV-O
- `prov:wasDerivedFrom`:
  - Processed outputs must link back to raw inputs
- `prov:wasGeneratedBy`:
  - Each processed asset must link to the ETL/transformation activity that produced it
- Activity / Agent identities:
  - Use stable IDs for pipeline runs and responsible agents (human or system), aligned to project conventions
  - If publishing provenance publicly, redact sensitive operational details per security guidance while preserving traceability

### Versioning
- Use STAC Versioning links and graph predecessor/successor relationships as applicable.
- Domain guidance:
  - Raw snapshots should be treated as immutable “versions”.
  - Processed outputs should carry explicit version tags that can be traced to: (raw version + pipeline version/config + run ID).
  - When a dataset changes materially (schema, semantics, unit conventions), update this README and record the rationale in the relevant governed docs.
