---
title: "KFM — Historical Data Domain README"
path: "data/historical/README.md"
version: "v1.0.0"
last_updated: "2025-12-19"
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

doc_uuid: "urn:kfm:doc:data:historical:readme:v1.0.0"
semantic_document_id: "kfm-data-historical-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:historical:readme:v1.0.0"
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

# KFM — Historical Data Domain README

## 📘 Overview

### Purpose
This README defines the **Historical** data domain for Kansas Frontier Matrix (KFM): what belongs in this domain, how it is staged through the canonical pipeline, and how it must be cataloged (STAC/DCAT/PROV) to remain provenance-linked and reproducible.

This document is a **domain landing guide**; it does not replace governed schemas, ingestion configs, or API contracts.

### Scope

| In Scope | Out of Scope |
|---|---|
| Primary historical sources (e.g., diaries, newspapers, letters, photographs, historic maps) | Modern-only datasets with no historical relevance (belongs in another domain) |
| Curated historical event/place/person datasets derived from primary sources | Untracked “ad hoc” exports without provenance or stable IDs |
| Geospatial historical layers (points/lines/polygons) and raster scans when they map to time + place | Any content requiring restricted handling that is not yet covered by governance rules (**not confirmed in repo**) |
| Provenance records (PROV) and catalog records (STAC/DCAT) for historical assets | UI or API implementation details (documented elsewhere) |

### Audience
- Primary: data engineers, catalog maintainers, historians/editors preparing ingest-ready materials
- Secondary: API/UI developers consuming cataloged historical assets via contracts (no direct graph access)

### Definitions (link to glossary)
- Link: `docs/glossary.md` (**not confirmed in repo**)
- Terms used in this doc: Historical domain, source bundle, STAC Item, STAC Collection, DCAT dataset, PROV activity, stable ID, redaction/generalization.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Domain landing doc | `data/historical/README.md` | TBD | This file |
| Raw sources (by domain) | `data/sources/historical/` | TBD | Preferred location for source bundles; structure may vary by contributor (**not confirmed in repo**) |
| Staging (raw/work/processed) | `data/raw/historical/`, `data/work/historical/`, `data/processed/historical/` | TBD | Deterministic + idempotent transforms required |
| STAC catalogs | `data/stac/collections/`, `data/stac/items/` | TBD | Historical assets must be represented as STAC Items where applicable |
| DCAT catalogs | `data/catalog/dcat/` | TBD | Dataset-level view of historical resources |
| PROV lineage | `data/prov/` | TBD | `prov:wasDerivedFrom` and `prov:wasGeneratedBy` required for public artifacts |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Domain placement rules align with KFM canonical pipeline ordering
- [ ] Validation steps listed and repeatable (even if commands are placeholders)
- [ ] Sensitivity / redaction expectations stated for historical content
- [ ] Any unknown repo specifics explicitly marked **not confirmed in repo**

## 🗂️ Directory Layout

### This document
- `path`: `data/historical/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Source bundles | `data/sources/historical/` | Raw contributor/source bundles + manifests (preferred) |
| Raw staging | `data/raw/historical/` | Raw, ingested copies normalized for tooling (no manual edits) |
| Work staging | `data/work/historical/` | Intermediate artifacts, extracted text, temp geopackages, etc. |
| Processed outputs | `data/processed/historical/` | Canonical processed datasets (ready for catalog + graph) |
| STAC outputs | `data/stac/collections/` + `data/stac/items/` | Catalog records for assets (domain-scoped folders allowed) |
| DCAT outputs | `data/catalog/dcat/` | Dataset catalog views (domain-scoped folders allowed) |
| PROV outputs | `data/prov/` | Lineage bundles for transforms/derivations |
| Docs (domain narrative) | `docs/` | Canonical governed docs + story nodes (not stored under `data/`) |

### Expected file tree for this sub-area
~~~text
📁 data/
├── 📁 historical/
│   └── 📄 README.md
├── 📁 sources/
│   └── 📁 historical/
│       ├── 📄 <source-manifest>.yml
│       └── 📁 <source-bundle>/
├── 📁 raw/
│   └── 📁 historical/
├── 📁 work/
│   └── 📁 historical/
├── 📁 processed/
│   └── 📁 historical/
├── 📁 stac/
│   ├── 📁 collections/
│   │   └── 📁 historical/
│   └── 📁 items/
│       └── 📁 historical/
├── 📁 catalog/
│   └── 📁 dcat/
│       └── 📁 historical/
└── 📁 prov/
    └── 📁 historical/
~~~

## 🧭 Context

### Background
KFM is a geospatial + historical knowledge system that requires **deterministic**, **provenance-linked** data products flowing through the canonical pipeline:
ETL → STAC/DCAT/PROV catalogs → Graph → APIs → UI → Story Nodes → Focus Mode.

This historical domain exists to:
- separate historical sources and derived historical datasets from other data domains
- standardize time/place anchoring early (ETL + catalog)
- ensure every narrative claim can trace back to a cataloged source (STAC/DCAT) and lineage record (PROV)

### Assumptions
- Stable identifiers exist (or will be created) for: sources, derived datasets, and catalog items (**not confirmed in repo**)
- Domain-specific assets can be discovered via STAC/DCAT without UI reading the graph directly
- Sensitive historical material may exist and requires governed handling (CARE/sovereignty)

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode ordering is preserved
- Frontend consumes contracts via APIs (no direct graph dependency)
- No unsourced narrative: any derived “summary” must link to evidence IDs

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What is the canonical source-manifest schema for `data/sources/historical/`? | TBD | TBD |
| Which STAC extensions are required for scanned historic maps vs. extracted vectors? | TBD | TBD |
| What redaction/generalization rules apply to personal/tribal/culturally sensitive historical content? | TBD | TBD |

### Future extensions
- Add domain-level “collection registry” mapping historical subdomains (maps, newspapers, diaries, oral histories) to STAC Collection IDs (**not confirmed in repo**)
- Add quality scoring signals for OCR quality, geocoding confidence, and temporal parsing confidence

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[Historical source bundles] --> B[ETL: extract/normalize]
  B --> C[STAC Items + Collections]
  B --> D[DCAT dataset views]
  B --> E[PROV lineage bundles]
  C --> F[Neo4j Graph build]
  D --> F
  E --> F
  F --> G[API Layer]
  G --> H[React/Map UI]
  H --> I[Story Nodes]
  I --> J[Focus Mode]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant UI
  participant API
  participant Catalog as STAC/DCAT/PROV
  participant Graph
  UI->>API: Request historical context bundle (entity_id)
  API->>Graph: fetch subgraph + provenance refs
  Graph-->>API: entity context + referenced IDs
  API->>Catalog: resolve STAC/DCAT/PROV by IDs
  Catalog-->>API: assets + dataset metadata + lineage
  API-->>UI: narrative-safe payload + citations + audit flags
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Historic documents | PDF/TXT/DOCX/HTML | archives, libraries, scans | parse success + checksum |
| Historic maps | GeoTIFF/JP2/PDF scan | map archives | CRS/extent + file integrity |
| Historic photos | JPG/PNG/TIFF | archives, museums | EXIF/time attribution if present |
| Vector layers | GeoJSON/GPKG/Shapefile | curated sources | geometry validity + CRS |
| Tabular datasets | CSV/XLSX/JSON | curated compilations | schema validation + type checks |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Canonical extracted text | TXT/JSON | `data/processed/historical/` | TBD (**not confirmed in repo**) |
| Curated tables | CSV/Parquet/JSON | `data/processed/historical/` | TBD (**not confirmed in repo**) |
| STAC Items | JSON | `data/stac/items/historical/` | STAC 1.0 + KFM profile |
| STAC Collections | JSON | `data/stac/collections/historical/` | STAC 1.0 + KFM profile |
| DCAT dataset records | JSON-LD/Turtle | `data/catalog/dcat/historical/` | DCAT 3 + KFM profile |
| PROV bundles | JSON-LD/Turtle | `data/prov/historical/` | PROV-O + KFM profile |

### Sensitivity & redaction
Historical sources may contain:
- personally identifying information (PII) in letters, diaries, rosters
- culturally sensitive locations or narratives
- sensitive sites (exact coordinates) that require generalization

Rules must follow:
- do not infer sensitive locations
- do not publish restricted coordinates; use generalization when required (**not confirmed in repo** governance specifics)
- ensure API payloads include audit flags for redacted/generalized fields

### Quality signals
- OCR confidence / error rate (if applicable)
- Temporal parsing confidence (date extraction success)
- Geocoding confidence (place-name → coordinate)
- Geometry validity and topology checks (for vector data)
- Completeness checks (required fields present)

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections involved: `historical` (collection IDs **not confirmed in repo**)
- Items involved: per asset (document/map/photo/vector/raster) with spatial + temporal fields where available
- Extension(s): per KFM-STAC profile (**not confirmed in repo** beyond profile name)

### DCAT
- Dataset identifiers: stable dataset IDs for each curated historical dataset (**not confirmed in repo**)
- License mapping: must reflect source license; derived datasets must preserve attribution
- Contact / publisher mapping: per governance docs (**not confirmed in repo**)

### PROV-O
- `prov:wasDerivedFrom`: list the exact source bundle IDs / STAC asset IDs
- `prov:wasGeneratedBy`: pipeline run/activity ID (include deterministic run configuration reference)
- Activity / Agent identities: contributor + pipeline agent identifiers (**not confirmed in repo**)

### Versioning
- When regenerating a dataset, create a new version and link predecessor/successor (STAC versioning links + graph lineage).

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize historical sources | configs + run logs |
| Catalogs | Produce STAC/DCAT/PROV records | JSON/JSON-LD validation |
| Graph | Model entities + relationships | populated via pipeline; queried via API layer |
| APIs | Serve historical domain payloads | REST/GraphQL contracts |
| UI | Render maps/timelines/narratives | API calls only |
| Story Nodes | Curated narrative from evidence | provenance-linked docs |
| Focus Mode | Context bundle synthesis | provenance + audit rendering |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog (**not confirmed in repo**) |
| API schemas | `src/server/` + docs | Contract tests required (**not confirmed in repo**) |
| Layer registry | `web/` | Schema-validated (**not confirmed in repo**) |

### Extension points checklist (for future work)
- [ ] Data: new historical subdomain added under `data/.../historical/...`
- [ ] STAC: new collection/item validation passes
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped with provenance
- [ ] APIs: contract version bump + tests (if needed)
- [ ] UI: layer registry entry + access rules
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Historical entities become focusable via graph + API context bundles.
- Every story node must include citations that resolve to:
  - a STAC item ID and/or DCAT dataset ID
  - a PROV lineage reference for any derived claim

### Provenance-linked narrative rule
Every factual claim must trace to a dataset / record / asset ID. Any predictive content must be opt-in and carry uncertainty/confidence fields.

### Optional structured controls
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (KFM-MDP)
- [ ] Schema validation (STAC/DCAT/PROV)
- [ ] Link integrity checks (catalog references resolve)
- [ ] Geometry validation (if vectors present)
- [ ] Security + sovereignty scanning gates (where applicable)

### Reproduction
~~~bash
# Placeholders — replace with repo-specific commands (not confirmed in repo)

# 1) Validate STAC
# e.g., ./tools/validate-stac.sh data/stac/items/historical

# 2) Validate DCAT + PROV
# e.g., ./tools/validate-schemas.sh data/catalog/dcat/historical data/prov/historical

# 3) Run unit/integration tests
# e.g., npm test / pytest / etc.
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| parse_warnings | ETL parsers | `docs/telemetry/` + `schemas/telemetry/` (**not confirmed in repo**) |
| ocr_confidence | OCR stage | `docs/telemetry/` (**not confirmed in repo**) |
| geocode_confidence | enrichment stage | `docs/telemetry/` (**not confirmed in repo**) |

## ⚖ FAIR+CARE & Governance

### Review gates
- Historian/editor review: required for narrative-facing outputs
- Security council review: required if new sensitive handling is introduced
- FAIR+CARE council review: required if sovereignty rules apply

### CARE / sovereignty considerations
- Do not publish culturally sensitive locations at full precision.
- Ensure restricted knowledge is not inferred or “filled in” by AI transforms.

### AI usage constraints
- Allowed: summarize, structure_extract, translate, keyword_index
- Prohibited: generate_policy, infer_sensitive_locations

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial `data/historical` domain README | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`