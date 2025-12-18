---
title: "Hydrology — Processed Hydroclimate (README)"
path: "data/hydrology/processed/hydroclimate/README.md"
version: "v1.0.0"
last_updated: "2025-12-18"
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

doc_uuid: "urn:kfm:doc:data:hydrology:processed:hydroclimate:readme:v1.0.0"
semantic_document_id: "kfm-data-hydrology-processed-hydroclimate-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:hydrology:processed:hydroclimate:readme:v1.0.0"
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

# Hydrology — Processed Hydroclimate

## 📘 Overview

### Purpose
This directory contains **processed hydroclimate data products** for the Hydrology domain in KFM. These are **curated, analysis-ready** artifacts produced by deterministic ETL/transforms and intended to be **cataloged (STAC/DCAT/PROV)** and later consumable via the graph/API/UI pipeline.

### Scope

| In Scope | Out of Scope |
|---|---|
| Curated hydroclimate outputs (grids, station time series, derived indices), plus manifests/checksums and processing notes | Raw downloads, ad-hoc scratch outputs, exploratory notebooks, API payloads, UI-only assets |
| Repeatable aggregation/derivation products (e.g., anomalies, climatologies, “water-year” summaries) | One-off manual edits without provenance; data that cannot be traced to upstream sources |
| Sidecar metadata needed for cataloging & lineage | Private/secrets/credentials; sensitive location inference |

### Audience
- Primary: Hydrology ETL + catalog maintainers
- Secondary: Analysts/modelers, Story Node authors, UI/layer integrators

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc (non-exhaustive):
  - **Hydroclimate**: climate variables relevant to hydrology (precipitation, temperature, ET, snow, drought indices).
  - **Water year**: hydrologic accounting year (definition must be explicit per dataset; *not confirmed in repo*).
  - **Anomaly**: deviation from a defined baseline climatology (baseline period must be explicit).

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Hydroclimate processed assets | `data/hydrology/processed/hydroclimate/` | Hydrology domain | This directory |
| Catalog records (STAC/DCAT/PROV) | `data/stac/` (expected) | Catalog build | Exact hydrology subtree *not confirmed in repo* |
| Run logs / provenance bundles | `mcp/runs/` (expected) | ETL ops | Run IDs should be referenced from PROV |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Directory purpose and boundaries are clear (raw/work/processed separation)
- [ ] Expected file tree reflects reality (or uses explicit “optional/TBD” markers)
- [ ] Outputs table includes path patterns and intended contracts
- [ ] Validation steps are listed and repeatable (even if commands are placeholders)
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `data/hydrology/processed/hydroclimate/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Hydrology domain root | `data/hydrology/` | Domain-scoped organization (raw/work/processed) |
| Raw hydroclimate (expected) | `data/hydrology/raw/hydroclimate/` | Immutable source drops (*not confirmed in repo*) |
| Work hydroclimate (expected) | `data/hydrology/work/hydroclimate/` | Intermediate/transient artifacts (*not confirmed in repo*) |
| Processed hydrology | `data/hydrology/processed/` | Curated outputs ready for cataloging |
| **This directory** | `data/hydrology/processed/hydroclimate/` | Processed hydroclimate outputs |
| Sibling processed areas (expected) | `data/hydrology/processed/bathymetry/` | Bathymetry products |
| Sibling processed areas (expected) | `data/hydrology/processed/ecological-surveys/` | Eco survey products |
| Catalog root | `data/stac/` | STAC catalogs (Collections/Items) |
| Pipelines | `src/pipelines/` | ETL + transforms + catalog builds (*entrypoints not confirmed*) |
| Schemas | `schemas/` | JSON schemas + profiles |
| Telemetry | `docs/telemetry/` + `schemas/telemetry/` | Observability + governance metrics |

### Expected file tree for this sub-area
~~~text
data/
└── 📁 hydrology/
    └── 📁 processed/
        └── 📁 hydroclimate/
            ├── 📄 README.md
            ├── 📁 gridded/                   # rasters / NetCDF (variable-organized)
            │   └── 📁 <variable>/            # e.g., precipitation, temperature, etc. (not confirmed in repo)
            ├── 📁 stations/                  # station time series + station metadata
            │   └── 📁 <network-or-variable>/ # not confirmed in repo
            ├── 📁 derived/                   # anomalies / indices / aggregations
            │   └── 📁 <product>/             # not confirmed in repo
            └── 📁 manifests/                 # inventories + checksums for CI gates
                ├── 📄 inventory.(csv|json)   # format not confirmed in repo
                └── 📄 checksums.sha256
~~~

## 🧭 Context

### Background
Hydroclimate products provide environmental context and modeling inputs for hydrologic interpretation (e.g., precipitation/temperature regimes, drought and flood context, seasonal variability). In KFM, these datasets are most useful when they can be:
- discovered and filtered by time and place (catalog + graph),
- rendered as map layers (UI),
- cited as evidence in Story Nodes / Focus Mode narratives.

### Where this fits in the canonical pipeline
This directory is part of the **ETL outputs** that must be produced before the catalogs and graph layers are generated:
- ETL outputs → **STAC/DCAT/PROV** catalogs → Neo4j graph → APIs → UI → Story Nodes → Focus Mode.

### Sensitivity considerations
Hydroclimate data is typically public, but **do not assume** all station-linked data is non-sensitive:
- If any station/sensor coordinates are on private land or otherwise restricted, generalize/redact per governance/sovereignty guidance (*policy specifics live in governance docs; not duplicated here*).
- Avoid publishing derived layers that could inadvertently reveal restricted facilities or sensitive monitoring locations.

### AI usage constraints
- Ensure the front-matter AI permissions/prohibitions remain appropriate for this document and do not enable prohibited inference (e.g., “infer_sensitive_locations”).

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A[Upstream hydroclimate sources<br/>(raw)] --> B[Deterministic ETL/Transforms<br/>(work)]
  B --> C[Processed hydroclimate assets<br/>data/hydrology/processed/hydroclimate]
  C --> D[Catalog generation<br/>STAC/DCAT/PROV]
  D --> E[Graph ingest<br/>Neo4j]
  E --> F[Contracted access layer<br/>APIs]
  F --> G[React/Map UI layers]
  G --> H[Story Nodes + Focus Mode<br/>provenance-linked narratives]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
participant ETL as ETL/Transforms
participant FS as data/processed
participant CAT as Catalog Build
participant API as API Layer
participant UI as UI/Focus Mode

ETL->>FS: write processed assets + manifests
CAT->>FS: read processed assets
CAT->>CAT: emit STAC/DCAT/PROV records
API->>CAT: query catalog/graph-derived indices (not direct FS access)
UI->>API: request hydroclimate context for view/time
API-->>UI: layer pointers + provenance refs
~~~

## 📦 Data & Metadata

### Inputs
**Not confirmed in repo (examples only):**
- Gridded climate products (e.g., precipitation/temperature surfaces)
- Station observations (precip, temp, wind, snow, etc.)
- Reanalysis/derived hydroclimate indices

When documenting a *real* input, always capture:
- upstream dataset identifier(s)
- license/usage constraints
- temporal coverage + resolution
- spatial reference/extent + resolution
- transformation parameters (baseline periods, aggregation windows, water-year definition, etc.)

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Gridded variables (per variable/time-slice) | GeoTIFF / NetCDF (*TBD*) | `gridded/<variable>/...` | STAC Item assets (KFM-STAC profile) |
| Station time series | CSV / Parquet (*TBD*) | `stations/<network-or-variable>/...` | Dataset schema (*not confirmed in repo*) + STAC/PROV pointers |
| Derived products (anomalies / indices / aggregates) | GeoTIFF / CSV (*TBD*) | `derived/<product>/...` | STAC Item assets + PROV lineage |
| Inventory manifest | CSV / JSON (*TBD*) | `manifests/inventory.(csv|json)` | Manifest conventions (*not confirmed in repo*) |
| Checksums | sha256 text | `manifests/checksums.sha256` | Integrity gate (required for reproducibility) |

### Sensitivity & redaction
- If station coordinates are sensitive: publish generalized geometry (e.g., coarse grid / bounding region) and store exact coordinates under restricted governance (if supported).
- Do not include private API keys, credentials, or restricted download URLs in manifests.

### Quality signals
Define (and eventually automate) checks such as:
- Spatial validity: CRS declared and consistent; extents intersect expected region; no flipped axes.
- Temporal validity: timestamps parse; coverage matches declared range; expected cadence (daily/monthly) holds.
- Units + nodata: units explicit; nodata consistent; no silent unit changes across versions.
- Completeness: missingness rates per time-slice/station; “holes” flagged and explained.
- Outliers: physically implausible values flagged (thresholds must be documented per variable).
- Reproducibility: checksums match; run IDs and parameters recorded.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections involved: *not confirmed in repo* (expected: a hydrology/hydroclimate collection or equivalent)
- Items involved: one Item per spatiotemporal asset grouping (variable × time-range × region), or per-file if required
- Extension(s): choose based on asset type (raster, projection, datacube/scientific, etc. as appropriate)

Minimum expectation:
- Every processed asset that is intended for use downstream must be discoverable via STAC and link to the physical file(s) in this directory.

### DCAT
- Dataset identifiers: must be stable across revisions
- License mapping: must reflect upstream restrictions
- Contact/publisher mapping: *TBD / not confirmed in repo*

### PROV-O
Record lineage at least to the level:
- `prov:used`: upstream source identifiers (raw/work inputs)
- `prov:wasGeneratedBy`: ETL/transform activity (include run ID)
- `prov:generatedAtTime`: timestamp
- `prov:wasAssociatedWith`: pipeline agent (script/container/tool identity)

### Versioning
- Use SemVer for dataset products where applicable.
- Represent “previous” relationships using STAC Version links and/or graph predecessor/successor relationships.
- Recompute and store checksums on every versioned release.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| ETL/Transforms | Ingest + normalize + derive hydroclimate products | Config + run logs (*entrypoints not confirmed in repo*) |
| Processed FS layout | Stable storage for curated artifacts | Files + manifests + checksums |
| Catalog build | Emit STAC/DCAT/PROV for processed assets | JSON + validators |
| Graph build | Ingest catalog metadata into Neo4j | Graph migration + loaders |
| APIs | Provide contracted read access | REST/GraphQL (no direct FS/graph access from UI) |
| UI | Map layers + Focus Mode narrative experience | Layer registry + API calls |

### Interfaces & contracts (examples)
| Contract type | Location | Notes |
|---|---|---|
| STAC profile | `data/stac/` + schema profile | Validate Items/Collections against KFM-STAC |
| PROV profile | `data/stac/` (or provenance store) | Must link from datasets/items to activities |
| Checksums/inventory | `manifests/` | Used by CI integrity gates |

### Extension points checklist (for future work)
- [ ] Data: add new hydroclimate variable/product under `gridded/` or `derived/`
- [ ] Catalog: add/extend STAC Collection + validate Items
- [ ] PROV: record activity/agent identities and inputs/outputs
- [ ] Graph: map new product type to ontology terms (if needed)
- [ ] APIs/UI: register new layer only through APIs (no direct file/graph access)
- [ ] Focus Mode: ensure narratives cite dataset/item IDs and provenance refs
- [ ] Telemetry: add new quality signals + bump telemetry schema if required

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
Hydroclimate products can surface as:
- contextual map layers (e.g., “drought severity” or “precip anomaly”),
- evidence artifacts referenced by Story Nodes (e.g., “conditions during year X”),
- temporal comparison views (baseline vs event period).

### Provenance-linked narrative rule
Every narrative claim that depends on hydroclimate data must reference:
- the dataset/STAC Item ID(s),
- the time window used,
- the transformation/baseline definition (e.g., anomaly baseline),
- the provenance activity/run ID.

### Optional structured controls
~~~yaml
focus_layers:
  - "TBD"          # e.g., hydroclimate-precip-anomaly (not confirmed in repo)
focus_time: "TBD"  # e.g., 1934-07 or 1934-WY (definition must be explicit)
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV) for any catalog records emitted for these assets
- [ ] Geospatial sanity checks (CRS, extents, nodata, timestamp parsing)
- [ ] Manifest + checksum generation updated for new/changed assets
- [ ] Regression checks on derived indices (baseline windows, aggregation logic)

~~~bash
# Example placeholders — replace with repo-specific commands
# 1) doc lint / markdown protocol checks
# 2) validate STAC/DCAT/PROV JSON against pinned validators
# 3) run geospatial sanity checks (bbox/CRS/nodata/time)
# 4) generate/update manifests + checksums
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| processed_asset_count | ETL run summary | `docs/telemetry/` + `schemas/telemetry/` (*expected*) |
| temporal_coverage | ETL metadata | run logs + catalog properties |
| missingness_rate | QC step | run logs + telemetry |
| validation_pass_rate | CI validators | CI logs + telemetry |
| checksum_mismatches | integrity gate | CI logs |

## ⚖ FAIR+CARE & Governance

### Review gates
- Approver(s): TBD (*not confirmed in repo*)
- Required sign-off when:
  - adding new upstream sources/licenses,
  - publishing higher-resolution products that change exposure risk,
  - changing baseline definitions or derived-index semantics,
  - introducing new schema fields or ontology mappings.

### CARE / sovereignty considerations
- If any hydroclimate products intersect with tribal governance constraints or protected knowledge contexts, apply sovereignty guidance and ensure publication rules are respected.
- Avoid “precision leakage” when combining layers could reveal restricted infrastructure or sensitive monitoring sites.

### AI usage constraints
- Ensure this README’s AI permissions/prohibitions remain consistent with governance.
- Do not use AI outputs to infer or publish sensitive locations.

## 🕰 Version History
| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-18 | Initial README for processed hydroclimate directory | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
