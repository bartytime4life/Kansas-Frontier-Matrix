---
title: "KFM Data Domain — Air Quality — Domain Notes"
path: "data/air-quality/DOMAIN_NOTES.md"
version: "v1.0.0"
last_updated: "2025-12-20"
status: "draft"
doc_kind: "DomainNotes"
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

doc_uuid: "urn:kfm:doc:data-domain:air-quality:domain-notes:v1.0.0"
semantic_document_id: "kfm-data-domain-air-quality-domain-notes-v1.0.0"
event_source_id: "ledger:kfm:doc:data-domain:air-quality:domain-notes:v1.0.0"
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

# KFM Data Domain — Air Quality — Domain Notes

## 📘 Overview

### Purpose
This document defines the **Air Quality** data domain boundaries and the minimum governance needed to ingest, catalog, model, and publish air-quality data through the KFM pipeline. It is the domain-level “contract” that aligns ETL outputs, STAC/DCAT/PROV metadata, graph mappings, and downstream API/UI/Story usage.

### Scope
| In Scope | Out of Scope |
|---|---|
| Air-quality measurements and related derived indicators for Kansas and relevant surrounding context (time + location anchored). | Personal health/medical data; personally identifying household sensor data without explicit governance; “black-box” claims without provenance. |
| Sensor/station metadata (location, method, operator) required for provenance and reproducibility. | Any data that cannot be licensed for storage and redistribution (until governance review completes). |
| Events/episodes inferred from measurements **only when** rules are documented and provenance-linked. | Uncited narratives and non-reproducible transformations. |

### Audience
- Primary: data engineers, pipeline maintainers, catalog maintainers
- Secondary: graph modelers, API/UI integrators, Story Node authors/reviewers

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc (non-exhaustive): air-quality observation, station/monitor, parameter, units, STAC item/collection, DCAT dataset, PROV activity/agent/entity

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This domain contract | `data/air-quality/DOMAIN_NOTES.md` | Data domain owner | Governs ingestion + metadata expectations |
| Source summaries for datasets used | `docs/research/source_summaries/by_type/` | Research / Data | Each external source should be summarized before ingestion |
| ETL pipelines (air-quality) | `src/pipelines/etl/` | Data Eng | not confirmed in repo |
| Schemas (records/tiles/catalog) | `schemas/` | Data Eng / Platform | not confirmed in repo |
| STAC outputs | `data/stac/` | Catalog | Domain must map assets to STAC where applicable |
| DCAT outputs | `data/catalog/dcat/` | Catalog | Dataset-level metadata + versions |
| PROV outputs | `data/prov/` | Data Eng | Run lineage for transformations |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Every “domain decision” includes a reproducible rule (or is marked “not confirmed in repo”)
- [ ] Inputs/Outputs tables identify formats, validation, and provenance links
- [ ] Sensitivity and redaction considerations explicitly stated (even if “none expected”)
- [ ] Validation steps listed and repeatable

## 🗂️ Directory Layout

### This document
- `path`: `data/air-quality/DOMAIN_NOTES.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Domain notes | `data/air-quality/` | Domain-scoped documentation and pointers |
| Raw inputs (preferred) | `data/raw/air-quality/` | Immutable ingested source files (preferred location) |
| Work / staging (preferred) | `data/work/air-quality/` | Intermediate transforms, QA artifacts |
| Processed outputs (preferred) | `data/processed/air-quality/` | Cleaned, normalized domain outputs |
| STAC | `data/stac/` | Collections + items referencing geospatial assets |
| DCAT | `data/catalog/dcat/` | Dataset catalog (DCAT 3 aligned) |
| PROV | `data/prov/` | Lineage records for runs and derived artifacts |
| Documentation | `docs/` | Canonical governed docs |
| Pipelines | `src/pipelines/` | ETL + catalogs + transforms |
| Schemas | `schemas/` | JSON schemas + telemetry schemas |
| Frontend | `web/` | React + map clients |

### Expected file tree for this sub-area
~~~text
📁 data/
├── 📁 air-quality/
│   └── 📄 DOMAIN_NOTES.md
├── 📁 raw/
│   └── 📁 air-quality/
│       └── 📄 (not confirmed in repo)
├── 📁 work/
│   └── 📁 air-quality/
│       └── 📄 (not confirmed in repo)
├── 📁 processed/
│   └── 📁 air-quality/
│       └── 📄 (not confirmed in repo)
├── 📁 stac/
│   ├── 📁 collections/
│   └── 📁 items/
├── 📁 catalog/
│   └── 📁 dcat/
└── 📁 prov/
~~~

## 🧭 Context

### Background
Air-quality data can support KFM narratives and analysis by providing **time-anchored environmental evidence** that can be linked to places and events (e.g., smoke episodes, industrial development, drought/dust periods), provided provenance and uncertainty are made explicit.

### Assumptions
- Air-quality sources and licensing are **not confirmed in repo**.
- The domain may include both:
  - point time-series (stations/sensors), and/or
  - gridded/raster products (e.g., interpolations or satellite-derived layers),
  depending on what is approved and available.

### Constraints / invariants
- The canonical ordering is preserved: **ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**.
- The frontend consumes data **only via APIs** (no direct graph access).

### How this domain uses Source Summaries
Before ingesting an external dataset or major web source for air-quality:
- Create/update a source summary under `docs/research/source_summaries/by_type/` (dataset/web/report as appropriate).
- Record licensing, update cadence, coverage, and known caveats.
- Reference the source summary ID/path in DCAT metadata and in PROV activities (as `prov:used` / `prov:wasDerivedFrom`), where applicable.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What authoritative air-quality sources are approved for ingestion (EPA, state, academic, community sensors, etc.)? | TBD | TBD |
| Do any station locations require coordinate generalization (private sensors, sensitive sites)? | TBD | TBD |
| What is the canonical parameter vocabulary (PM2.5, O3, etc.) + unit normalization rules? | TBD | TBD |
| What aggregation rules are allowed (hourly → daily → monthly) and how is uncertainty represented? | TBD | TBD |

### Future extensions
- Add raster/surface products (if licensed) as STAC assets for time-enabled mapping.
- Add derived “episode” Events (e.g., smoke days) only with explicit, versioned rules + provenance.
- Integrate AI analysis outputs as evidence products under `mcp/` with strict provenance linkage.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  SRC[Air quality sources] --> ETL[ETL normalize]
  ETL --> CAT[STAC DCAT PROV catalogs]
  CAT --> GRAPH[Neo4j graph]
  GRAPH --> API[APIs]
  API --> UI[React Map UI]
  UI --> STORY[Story nodes]
  STORY --> FOCUS[Focus mode]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant UI
  participant API
  participant Graph
  UI->>API: Query air-quality context(place_id, time_range)
  API->>Graph: Fetch observations + provenance refs
  Graph-->>API: Results + IDs (STAC/DCAT/PROV)
  API-->>UI: Contracted payload + provenance bundle
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Station observations (time-series) | TBD (CSV/JSON/Parquet) | not confirmed in repo | Required fields + unit checks + timestamp validity |
| Station metadata | TBD | not confirmed in repo | Geometry validity + stable station identifiers |
| Raster/surface products (optional) | TBD (COG/NetCDF/etc.) | not confirmed in repo | CRS + bounds + time coverage + checksum |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Normalized observations | TBD | `data/processed/air-quality/` | not confirmed in repo |
| Normalized station registry | TBD | `data/processed/air-quality/` | not confirmed in repo |
| Domain QA report | TBD | `data/work/air-quality/` | not confirmed in repo |
| Catalog artifacts | STAC/DCAT/PROV | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | KFM-STAC / KFM-DCAT / KFM-PROV profiles |

### Sensitivity & redaction
- Default assumption is **public**, but this must be re-validated once sources are chosen.
- If any sensors are on private property or sensitive locations:
  - generalize coordinates in public outputs (e.g., to centroid of a larger area)
  - or omit exact geometry and provide a provenance pointer + access gate
- Do not publish raw station identifiers if they can deanonymize individuals without governance review.

### Quality signals
- Completeness (missing timestamps, missing parameters)
- Range checks (negative concentrations, impossible units)
- Unit normalization checks (e.g., µg/m³ vs ppm where applicable)
- Duplicate detection (same station/parameter/timestamp)
- Geometry validity for station points
- Temporal coverage checks (gaps, overlaps, timezone consistency)

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections involved: not confirmed in repo
- Items involved: not confirmed in repo
- Extension(s): not confirmed in repo

Guidance:
- Use STAC when publishing **spatiotemporal assets** (rasters, tiled vectors, map products).
- If time-series are not themselves “assets”, still link derived maps/aggregations via STAC.

### DCAT
- Dataset identifiers: not confirmed in repo
- License mapping: not confirmed in repo (must be sourced from each dataset’s terms)
- Contact / publisher mapping: not confirmed in repo

Guidance:
- One DCAT dataset per externally sourced dataset per version (and/or per major KFM derived dataset).
- Make update cadence explicit (when known) and tie it to reproducible run IDs.

### PROV-O
- `prov:wasDerivedFrom`: external dataset identifiers + internal artifact IDs
- `prov:wasGeneratedBy`: ETL run activity ID(s)
- Activity / Agent identities: pipeline script/version + operator identity (as applicable)

### Versioning
- Use STAC Versioning links and graph predecessor/successor relationships as applicable.

### Extension points checklist (for future work)
- [ ] Data: domain added under `data/air-quality/.`
- [ ] STAC: collections + items + schema validation
- [ ] PROV: activity + agent identifiers recorded for ETL runs
- [ ] Graph: labels/relations mapped (or subtype approach) + migration plan if needed
- [ ] APIs: contract documented + tests
- [ ] UI: layer registry entry + access rules
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump (if applicable)

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
Potential focusable entities (subject to ontology constraints and governance):
- **Place**: monitoring stations or generalized monitoring areas
- **Artifact**: datasets, derived products, observation series
- **Event**: episodes (e.g., “smoke week”) only when defined by explicit, versioned rules

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID.

### Optional structured controls
~~~yaml
focus_layers:
  - "air_quality"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV)
- [ ] Domain QA checks (ranges, units, timestamps)
- [ ] Graph integrity checks (stable IDs, relationship constraints)
- [ ] API contract tests (if/when endpoints are added)
- [ ] UI schema checks (layer registry)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) validate schemas
# 2) run domain QA
# 3) run doc lint
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| air_quality_ingest_run | ETL | `mcp/runs/` or telemetry schemas (not confirmed in repo) |
| air_quality_qc_failures | QA | `data/work/air-quality/` (not confirmed in repo) |

## ⚖ FAIR+CARE & Governance

### Review gates
- Domain owner approval required before publishing new air-quality datasets publicly.
- Governance review required for any coordinate publication that could expose sensitive sites.

### CARE / sovereignty considerations
- Identify communities impacted and protection rules before publishing fine-grained locations (if any).
- If sources include culturally sensitive locations, apply redaction/generalization policies and document them.

### AI usage constraints
- Ensure this document’s AI permissions/prohibitions match intended use.
- Prohibit “infer_sensitive_locations” remains in effect for this domain documentation.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-20 | Initial Air Quality domain notes scaffold | TBD |

---

Footer refs:
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
