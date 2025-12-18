---
title: "Hydrology Data Domain — README"
path: "data/hydrology/README.md"
version: "v0.1.0"
last_updated: "2025-12-18"
status: "draft"
doc_kind: "README"
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

doc_uuid: "urn:kfm:doc:data:hydrology:readme:v0.1.0"
semantic_document_id: "kfm-data-hydrology-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data:hydrology:readme:v0.1.0"
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

# Hydrology Data Domain — README

## 📘 Overview

### Purpose
- Define how **hydrology datasets** (surface water, groundwater, watersheds, and related hydrologic context layers) are organized, ingested, cataloged, and governed in KFM.
- Provide a single domain index that points to the **ETL → catalogs (STAC/DCAT/PROV) → graph → APIs → UI → Story Nodes → Focus Mode** integration surfaces for hydrology.

### Scope
| In Scope | Out of Scope |
|---|---|
| Rivers/streams, lakes/reservoirs, wetlands, watersheds/hydrobasins, aquifers/groundwater context layers, flood/drought context layers (where available), hydrology-related time series (where available) | Oceanography, global-scale hydrology outside KS context, ungoverned ad-hoc analyses not tracked by PROV, any “direct-to-frontend” data wiring that bypasses APIs |

### Audience
- Primary: Data engineers / GIS pipeline maintainers working in `src/pipelines/` and `data/*`
- Secondary: Graph/ontology maintainers, API maintainers, UI layer maintainers, Story Node authors

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc: Hydrology layer, Watershed, Hydrography, Gauge/time series, STAC Collection/Item, DCAT Dataset, PROV Activity/Entity, Sensitivity classification

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Hydrology domain index (this file) | `data/hydrology/README.md` | TBD | Primary entry point for this domain |
| Hydrology sources registry | `data/sources/hydrology_sources.json` | TBD | Declares upstream sources, license, update cadence, and retrieval hints (if present) |
| Raw staging (hydrology) | `data/raw/hydrology/` | Pipelines | Immutable-ish source snapshots; do not hand-edit |
| Work staging (hydrology) | `data/work/hydrology/` | Pipelines | Intermediate transforms; safe to delete/rebuild |
| Processed outputs (hydrology) | `data/processed/hydrology/` | Pipelines | Cleaned, normalized layers ready for catalog + graph |
| STAC catalogs (hydrology) | `data/stac/` (see layout below) | Catalog maintainers | Collection(s)/Item(s) describing hydrology assets |
| DCAT mappings / exports | `docs/data/` | Catalog maintainers | Mappings + export artifacts (if enabled) |
| PROV lineage artifacts | `docs/data/` (or domain lineage location) | Pipelines | PROV records linking raw→processed→published |
| Pipeline implementation | `src/pipelines/` | Pipelines | Hydrology ETL modules/configs (if implemented) |
| Graph mappings / ontology hooks | `src/graph/` + `docs/graph/` | Graph maintainers | Hydrology entities/relationships and migration rules |
| API surfacing | `src/server/` + docs | API maintainers | REST/GraphQL endpoints that expose hydrology context |
| UI layer surfacing | `web/` + `docs/design/` | UI maintainers | Declarative layer registry + rendering rules |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] All claims link to datasets / schemas / tickets / commits (as applicable)
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `data/hydrology/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Domain index docs | `data/hydrology/` | Domain README + small domain notes/manifests (no large binaries) |
| Source registry | `data/sources/` | Source manifests (URLs, licensing, update notes, checksums) |
| Raw data | `data/raw/hydrology/` | Source snapshots (as-delivered) |
| Work data | `data/work/hydrology/` | Intermediate transforms, staging, scratch outputs |
| Processed data | `data/processed/hydrology/` | Canonical processed layers/time series for KFM |
| STAC catalogs | `data/stac/` | STAC catalogs/collections/items for all domains |
| DCAT/PROV docs | `docs/data/` | DCAT datasets + PROV lineage + mapping docs |
| Pipelines | `src/pipelines/` + `docs/pipelines/` | Hydrology ETL, transforms, catalog build hooks |
| Graph | `src/graph/` + `docs/graph/` | Ontology labels/relations + hydrology mapping/migrations |
| APIs | `src/server/` + docs | Contracted access layer (REST/GraphQL) |
| Frontend | `web/` + `docs/design/` | Map layers + Focus Mode UX |

### Expected file tree for this sub-area
~~~text
📁 data
├── 📁 hydrology
│   └── 📄 README.md
├── 📁 sources
│   └── 📄 hydrology_sources.json
├── 📁 raw
│   └── 📁 hydrology
│       ├── 📄 <source>__<dataset>__<version-or-date>.<ext>
│       └── 📄 checksums.<txt|json>
├── 📁 work
│   └── 📁 hydrology
│       ├── 📁 staging
│       └── 📁 transforms
├── 📁 processed
│   └── 📁 hydrology
│       ├── 📁 vectors
│       ├── 📁 rasters
│       ├── 📁 timeseries
│       └── 📄 manifest.json
└── 📁 stac
    ├── 📁 collections
    │   └── 📁 hydrology
    │       └── 📄 collection.json
    └── 📁 items
        └── 📁 hydrology
            └── 📄 <item-id>.json
~~~

## 🧭 Context

### Background
Hydrology is a core “environment context” domain: water features (rivers/streams), floodplains, and related hydrologic conditions can be used as map layers and as analytical context for historical narratives.

### Assumptions
- The canonical KFM pipeline ordering is maintained: **ETL → STAC/DCAT/PROV → graph → APIs → UI → Story Nodes → Focus Mode**.
- Processed hydrology layers intended for the web map should be in a web-friendly CRS (commonly WGS84 / EPSG:4326), with original CRS recorded in metadata.

### Constraints / invariants (do not break)
- No direct frontend access to raw data or graph DB; all UI access must go through contracted APIs.
- Deterministic, replayable transforms (pinned versions; stable IDs; recorded provenance).
- Respect FAIR+CARE and sovereignty policy for sensitive hydrology-related locations and infrastructure.

### Open questions (track as issues)
| Question | Why it matters | Owner | Status |
|---|---|---|---|
| Do we store PROV JSON under `docs/data/prov/` or alongside STAC assets? | Enables consistent lineage discovery | TBD | TBD |
| Do hydrology time series live as STAC assets, graph nodes, or both? | Impacts query patterns and UI charts | TBD | TBD |
| Which hydrology entities are modeled in graph (River, Watershed, Gauge, FloodEvent)? | Impacts ontology + API contracts | TBD | TBD |

### Future extensions (explicit extension points)
- Link major floods/droughts and water-management infrastructure to timelines and events (requires new graph relations + story node templates).
- Optional integration with hydrologic modeling outputs (e.g., flood inundation rasters) as evidence artifacts (requires STAC assets + provenance + UI layer rules).

## 🗺️ Diagrams

### Hydrology domain flow (canonical)
~~~mermaid
flowchart LR
  A[Upstream hydrology sources] --> B[ETL: ingest/normalize]
  B --> C[STAC/DCAT/PROV catalogs]
  C --> D[Neo4j graph (optional enrichment)]
  D --> E[APIs (REST/GraphQL)]
  E --> F[React/Map UI layers]
  F --> G[Story Nodes]
  G --> H[Focus Mode (provenance-linked)]
~~~

### “Add a new hydrology dataset” (high level)
~~~mermaid
sequenceDiagram
  participant S as Source Registry
  participant R as data/raw/hydrology
  participant P as Hydrology ETL
  participant C as STAC/DCAT/PROV
  participant G as Graph Build
  participant A as API Layer
  participant U as UI Layer Registry

  S->>R: Register + snapshot upstream source
  R->>P: ETL reads raw snapshot
  P->>P: Normalize CRS/time/fields
  P->>C: Emit STAC Item + PROV lineage (+ DCAT mapping)
  C->>G: (Optional) Create/refresh hydrology entities/links
  G->>A: Expose via contracted endpoints
  A->>U: UI consumes via API/layer registry (no direct data access)
~~~

## 📦 Data & Metadata

### Input categories (typical)
| Input type | Common formats | Expected properties | Notes |
|---|---|---|---|
| Vector hydrography | GeoPackage/GeoJSON/Shapefile | Valid geometry, CRS known, feature class/type | Normalize schema + IDs during ETL |
| Raster hydrology derivatives | GeoTIFF/COG | CRS, resolution, nodata, temporal extent (if applicable) | Prefer COG for large rasters (if supported) |
| Time series | CSV/Parquet/JSON | Station/gauge ID, timestamp, units, QA flags | Consider whether charting requires API endpoints |

### Output categories (KFM canonical)
| Output | Location | Must include | Notes |
|---|---|---|---|
| Processed hydrology layers | `data/processed/hydrology/` | Stable IDs, CRS, time fields (if applicable), dataset-level metadata | Deterministic regeneration required |
| STAC Collection/Items | `data/stac/` | Assets linking to processed outputs; spatial/temporal extents | Validator must pass in CI |
| DCAT dataset + mapping | `docs/data/` | Dataset metadata + distribution links | Required if DCAT export enabled |
| PROV lineage | `docs/data/` (or agreed location) | prov:used raw entities; prov:wasGeneratedBy activity; tool versions | Must link raw→processed→published |
| Graph entities (optional) | `src/graph/` build outputs | Mapped node labels + relations | Only if hydrology participates in graph queries |

### Sensitivity & redaction notes
Hydrology data can become sensitive when it reveals:
- precise locations of restricted infrastructure or culturally sensitive water-related sites,
- private well locations or landowner-specific assets,
- locations requiring sovereignty governance review.

If any dataset is sensitive:
- ensure sensitivity classification is set in metadata,
- apply generalization or access controls in API/UI according to governance,
- do not expose restricted coordinates in public layers.

### Quality signals (recommended)
- Geometry validity (no self-intersections), consistent CRS, correct bounding boxes.
- Stable identifiers for features/stations; avoid re-keying across releases without mapping tables.
- Temporal fields (if present) use ISO date/datetime conventions; time ranges are explicit.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Hydrology assets are described as STAC Collections/Items under `data/stac/`.
- Each STAC Item should reference the processed asset(s) and include:
  - spatial footprint + bbox,
  - temporal metadata (if applicable),
  - asset roles (e.g., “data”, “metadata”, “thumbnail” if used),
  - links to provenance artifacts (PROV) and (if enabled) DCAT dataset identifiers.

### DCAT
- If DCAT export is enabled, maintain a mapping from hydrology STAC metadata to:
  - dataset-level metadata (title, description, keywords/themes),
  - distributions (download/asset links),
  - publisher/creator/license.

### PROV-O
- Each hydrology processing run should record:
  - `prov:Activity` for the ETL run (with run_id, tool versions, parameters/config hash),
  - `prov:Entity` for raw snapshots and processed outputs,
  - `prov:used` and `prov:wasGeneratedBy` edges that link raw→run→processed.

### Versioning
- Prefer stable dataset IDs and feature IDs; changes should be tracked via PROV lineage.
- Use STAC Item versioning conventions where applicable; keep validator versions pinned in CI.

## 🧱 Architecture

### How hydrology participates in the KFM pipeline
- Data Stage: declared in `data/sources/` and staged through `data/raw/` → `data/work/` → `data/processed/`.
- Catalog Stage: hydrology outputs are indexed via STAC (and optionally DCAT + PROV artifacts).
- Graph Stage (optional): hydrology entities may be represented in Neo4j for semantic linking (e.g., “Event occurred near River/Watershed”), but the UI must not query Neo4j directly.
- API Stage: hydrology layers are surfaced through versioned API contracts.
- UI Stage: layers are toggled/filtered via a declarative registry and rendered through the API layer.

### Extension points checklist (for future work)
- [ ] Add new hydrology dataset (raw/work/processed + STAC Item)
- [ ] Add DCAT export entry + mapping doc (if enabled)
- [ ] Add PROV run recorder + lineage linkouts
- [ ] Add graph entity type(s) (requires ontology + migration + tests)
- [ ] Add API endpoints/fields (requires contract change doc + tests)
- [ ] Add UI layer registry entry (requires schema validation + a11y considerations)
- [ ] Add Story Node patterns that cite hydrology evidence

## 🧠 Story Node & Focus Mode Integration

### Where hydrology shows up
- As map layers (rivers/streams, flood extents, watershed boundaries) that can be toggled and filtered by time where applicable.
- As contextual evidence in Story Nodes (e.g., “near a major river crossing”), with links back to STAC/PROV artifacts.
- In Focus Mode, hydrology context should only appear if it is provenance-linked and permitted by governance (sensitivity-aware).

### Required provenance behaviors
- Focus Mode must not display unsourced hydrology claims.
- Any derived hydrology analysis product shown in Focus Mode must link to:
  - its STAC Item,
  - the PROV activity that produced it,
  - and any upstream raw source entity where possible.

## 🧪 Validation & CI/CD

### Validation steps (minimum)
- [ ] STAC JSON validates against pinned KFM-STAC profile + validator version
- [ ] (If enabled) DCAT export validates against KFM-DCAT profile
- [ ] PROV artifacts are present and link raw→processed deterministically
- [ ] Geospatial checks: geometry validity + CRS declared + bbox correct
- [ ] Time checks: ISO date/datetime; begin/end ranges consistent
- [ ] Sensitivity checks: restricted layers are not published to public outputs
- [ ] If APIs/UI change: contract tests + schema validation for layer registry

### Reproduction (deterministic rerun)
~~~bash
# Pseudocode (replace with actual repo commands)
# 1) Confirm source registry entry exists
# 2) Run hydrology ETL to regenerate processed outputs
# 3) Rebuild STAC/DCAT/PROV artifacts
# 4) (Optional) Rebuild graph + run API contract tests
~~~

### Telemetry signals (recommended)
| Signal | Why | Where logged |
|---|---|---|
| hydrology_etl_run_id | Traceability to PROV | `mcp/runs/` or telemetry store |
| hydrology_processed_feature_count | Regression detection | CI artifact / telemetry |
| stac_validation_pass_rate | Catalog health | CI artifact |
| sensitivity_redaction_events | Governance compliance | Security/telemetry |

## ⚖ FAIR+CARE & Governance

### Review gates (required when applicable)
- Data steward review for new/updated hydrology datasets
- Security/governance review if any dataset may expose sensitive locations/infrastructure
- Ontology/graph review if new hydrology entity types or relations are introduced
- API contract review if endpoints or schemas change

### CARE considerations (domain notes)
- Water-related locations and infrastructure may intersect with sensitive community knowledge.
- If sovereign or culturally sensitive data is present, follow sovereignty policy and apply access controls/generalization.

### AI usage constraints
- This document permits summarization/structuring/translation/keyword indexing.
- Prohibited: generating new policy or inferring sensitive locations beyond what is explicitly governed and sourced.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v0.1.0 | 2025-12-18 | Initial hydrology data domain README | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`