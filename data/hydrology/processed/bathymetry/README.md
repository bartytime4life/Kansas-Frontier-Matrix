---
title: "Hydrology — Bathymetry (Processed) README"
path: "data/hydrology/processed/bathymetry/README.md"
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

doc_uuid: "urn:kfm:doc:data:hydrology:processed:bathymetry:readme:v0.1.0"
semantic_document_id: "kfm-data-hydrology-processed-bathymetry-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data:hydrology:processed:bathymetry:readme:v0.1.0"
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

# Hydrology — Bathymetry (Processed) README

## 📘 Overview

### Purpose
- Standardize how **bathymetry** (underwater depth/elevation surfaces for waterbodies) is stored, documented, validated, and published as processed outputs.
- Ensure bathymetry products can be used as evidence in Focus Mode with clear provenance (STAC/DCAT/PROV) and consistent interpretation (units, datum, sign convention).

### Scope
| In Scope | Out of Scope |
|---|---|
| Bathymetry rasters (e.g., bathymetric DEMs), contours, footprints, uncertainty layers, and QA artifacts produced by KFM pipelines | Raw sonar/LiDAR vendor archives stored “as-is” (place those in `data/hydrology/raw/` or external storage) |
| Metadata required to interpret bathymetry (vertical datum, units, water surface reference, methods) | Non-bathymetry hydrology outputs (see `data/hydrology/processed/README.md`) |
| Catalog + provenance artifacts enabling safe UI exposure | Any release that bypasses governance review when sensitivity applies |

### Audience
- Primary: GIS analysts, hydrology modelers, data engineers
- Secondary: UI/Focus Mode maintainers who need to present bathymetry with correct caveats

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc: Bathymetry, Sounding, Vertical datum, Water surface reference, Uncertainty, STAC Asset, PROV Activity

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Parent processed README | `data/hydrology/processed/README.md` | Data Steward (Hydrology) — TBD | Promotion rules for processed outputs |
| Bathymetry README | `data/hydrology/processed/bathymetry/README.md` | Data Steward (Hydrology) — TBD | This document |
| Bathymetry datasets | `data/hydrology/processed/bathymetry/` | Data Steward (Hydrology) — TBD | Data products + QA |
| Bathymetry STAC collection(s) | `data/stac/` (IDs TBD) | Catalog Maintainer — TBD | Canonical STAC location; IDs not confirmed |
| Bathymetry DCAT/PROV | `docs/data/` (paths TBD) | Catalog Maintainer — TBD | Canonical DCAT/PROV location; structure not confirmed |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Defines required bathymetry metadata (units, datum, sign convention, method)
- [ ] Lists QA + validation steps (including vertical/horizontal reference checks)
- [ ] States governance/sensitivity considerations
- [ ] Provides reproducible publishing expectations (STAC/DCAT/PROV)

## 🗂️ Directory Layout

### This document
- `path`: `data/hydrology/processed/bathymetry/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Domain root | `data/hydrology/` | Hydrology domain |
| Processed root | `data/hydrology/processed/` | Contract-stable processed outputs |
| Bathymetry (this area) | `data/hydrology/processed/bathymetry/` | Bathymetry products + QA artifacts |
| STAC catalogs | `data/stac/` | STAC Collections/Items (canonical) |
| DCAT + PROV catalogs | `docs/data/` | DCAT + PROV records (canonical) |

### Expected file tree for this sub-area
~~~text
📁 data/
└─📁 hydrology/
  └─📁 processed/
     └─📁 bathymetry/
        ├─📄 README.md
        ├─📁 rasters/          (optional; recommended)
        ├─📁 vectors/          (optional; recommended)
        ├─📁 tables/           (optional; recommended)
        └─📁 qc/               (optional; recommended)
~~~

## 🧭 Context

### Background
Bathymetry is useful for:
- Understanding reservoir/lake morphology (storage capacity, shoreline change context).
- Supporting historical narratives where water management mattered (reservoir construction, drought response, flood control) without requiring users to interpret raw survey artifacts.

### Assumptions
- A bathymetry product must explicitly state **what “depth” means** (below water surface vs absolute elevation).
- Both **horizontal CRS** and **vertical datum** (and units) must be documented; otherwise the data is not interpretable.
- Waterbody identifiers should be stable (graph IDs or external IDs); this is not confirmed in repo and must be resolved.

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode is preserved.
- Frontend consumes bathymetry via APIs and catalog contracts (no direct file access assumptions).
- Bathymetry releases must pass QA and (if applicable) governance review before being marked “publishable”.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What is the canonical bathymetry sign convention (depth positive downward vs elevation)? | Data Steward (Hydrology) | TBD |
| What vertical datum(s) are accepted for published products (and how do we record conversions)? | Data Steward + Catalog Maintainer | TBD |
| What is the canonical waterbody ID scheme (graph node IDs vs external IDs)? | Ontology Lead | TBD |
| Where are the authoritative bathymetry sources tracked (registry file/format)? | Repo Maintainers | TBD |

### Future extensions
- Add uncertainty surfaces as first-class assets for all bathymetry datasets.
- Add derivative analytics (hypsographic curves, volume-at-elevation tables) with explicit provenance.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[Raw surveys/soundings] --> B[Cleaning + datum/unit normalization]
  B --> C[Gridding / interpolation]
  C --> D[Bathymetry raster + derivatives]
  D --> E[STAC/DCAT/PROV Catalogs]
  E --> F[Graph + APIs]
  F --> G[UI + Focus Mode]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant ETL
  participant QC
  participant Catalog
  ETL->>QC: Generate bathymetry DEM + artifacts
  QC-->>ETL: QC report (pass/fail + metrics)
  ETL->>Catalog: Publish STAC Item (DEM, contours, QC, README)
  Catalog-->>ETL: Validation gate result
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Bathymetry surveys / soundings | CSV / LAS / vendor formats (TBD) | External providers (TBD; track in source registry) | Units/datum recorded, outlier screening |
| Shoreline/footprint references | Vector | Hydrology domain sources (TBD) | Topology/coverage checks |
| Water surface reference (if used) | Table / metadata | Dataset documentation | Consistency with stated depth convention |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Bathymetric DEM (primary) | GeoTIFF / COG | `data/hydrology/processed/bathymetry/rasters/` (recommended) | STAC Item + raster metadata + README link |
| Contours / isobaths | GeoPackage / GeoJSON | `data/hydrology/processed/bathymetry/vectors/` (recommended) | STAC Item asset + attribute schema |
| Soundings (cleaned) | Parquet / CSV | `data/hydrology/processed/bathymetry/tables/` (recommended) | Schema + units + provenance |
| Uncertainty surface (optional) | GeoTIFF / COG | `data/hydrology/processed/bathymetry/rasters/` | Document method + metrics |
| QA artifacts | Markdown/PDF/JSON | `data/hydrology/processed/bathymetry/qc/` | Linked as STAC assets where applicable |

### Sensitivity & redaction
- Bathymetry can indirectly reveal sensitive infrastructure context (e.g., near dams/intakes) depending on resolution and coverage.
- If any release intersects with sovereignty-sensitive water-related context, apply governance review before publishing.

### Quality signals
- Vertical reference correctness: datum + units explicitly stated, conversions documented.
- Reasonable ranges: depths/elevations within plausible bounds for the specific waterbody (rules per dataset; not global).
- Artifact screening: remove spikes/outliers; document interpolation method.
- Coverage: footprint and “no data” holes documented; shoreline alignment checked where applicable.
- Uncertainty: RMSE or equivalent metric reported (preferred).

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections involved: `kfm-hydrology-bathymetry` (proposed; not confirmed in repo).
- Items involved: one Item per waterbody+survey (or per published product bundle) with assets:
  - `dem` (raster), `contours` (vector), `soundings` (table), `qc` (report), `readme` (this doc link or dataset-level doc).
- Extension(s): likely `proj`, `raster`; possibly others depending on asset types (confirm in repo).

### DCAT
- Dataset identifiers: align with bathymetry dataset ID scheme (not confirmed in repo).
- License mapping: ensure license/attribution requirements are carried into DCAT and STAC.
- Contact / publisher mapping: designate KFM maintainer contact (TBD).

### PROV-O
- `prov:wasDerivedFrom`: raw survey IDs + source registry entries + any reference layers used.
- `prov:wasGeneratedBy`: interpolation/gridding activity with run ID (MCP log) and parameters.
- Activity / Agent identities: pipeline job name + git SHA + operator identity (as allowed).

### Versioning
- Use STAC Versioning links and graph predecessor/successor relationships as applicable.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| ETL | Normalize + generate bathymetry products | Config + run logs |
| Catalogs | STAC/DCAT/PROV | JSON + validator |
| Graph | Link waterbodies + surveys + events | Cypher + API layer |
| APIs | Serve bathymetry as layer/evidence | REST/GraphQL |
| UI | Render bathymetry + metadata | API calls |
| Story Nodes | Curate water-management narratives | Graph + docs |
| Focus Mode | Show bathymetry as evidence | Provenance-linked |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog |
| API schemas | `src/server/` + docs | Contract tests required |
| Layer registry | `web/` (path TBD) | Schema-validated |

### Extension points checklist (for future work)
- [ ] Data: bathymetry outputs standardized under `data/hydrology/processed/bathymetry/`
- [ ] STAC: bathymetry collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded (including interpolation parameters)
- [ ] Graph: waterbody links + survey lineage mapped
- [ ] APIs: layer/evidence contract tests added
- [ ] UI: bathymetry layer registry entry + access rules
- [ ] Focus Mode: provenance references enforced for bathymetry-derived claims
- [ ] Telemetry: bathymetry quality metrics captured + schema version bump

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Focusable entities: waterbody/reservoir, survey activity, (optional) infrastructure-related events when explicitly sourced.
- Evidence shown:
  - bathymetry raster visualization
  - dataset metadata (datum/units/method)
  - provenance links (STAC/DCAT/PROV)
  - QC summary metrics

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID.

### Optional structured controls
~~~yaml
focus_layers:
  - "hydrology.bathymetry"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV)
- [ ] Raster validation (CRS, nodata, range checks, metadata completeness)
- [ ] Vector validation (geometry validity, attribute schema)
- [ ] Graph integrity checks (waterbody linkage)
- [ ] API contract tests (if exposed)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) run bathymetry pipeline (config-driven)
# 2) validate outputs (raster/vector + metadata)
# 3) validate STAC/DCAT/PROV artifacts
# 4) run unit/integration tests + doc lint
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| bathymetry_waterbodies_processed_count | ETL job | `docs/telemetry/` + `schemas/telemetry/` |
| bathymetry_rmse_summary | QC step | `docs/telemetry/` + `schemas/telemetry/` |
| bathymetry_validation_failures_count | CI | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates
- Data Steward (Hydrology) approves bathymetry products for publication (QA + interpretability).
- Governance/ethics review if bathymetry resolution/coverage introduces sensitivity concerns.

### CARE / sovereignty considerations
- Identify communities impacted and protection rules.
- If bathymetry intersects with sovereignty-sensitive water contexts, ensure appropriate access controls and narrative framing.

### AI usage constraints
- Ensure doc’s AI permissions/prohibitions match intended use.
- Do not infer sensitive locations or infrastructure conclusions from bathymetry unless explicitly supported by approved sources.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v0.1.0 | 2025-12-18 | Initial bathymetry processed README | TBD |

---
Footer refs:
- Parent processed README: `data/hydrology/processed/README.md`
- Domain README: `data/hydrology/README.md`
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
