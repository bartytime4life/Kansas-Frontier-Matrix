---
title: "Air Quality — Sources (README)"
path: "data/air-quality/sources/README.md"
version: "v1.0.0"
last_updated: "2025-12-17"
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

doc_uuid: "urn:kfm:doc:data:air-quality:sources:readme:v1.0.0"
semantic_document_id: "kfm-data-air-quality-sources-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:air-quality:sources:readme:v1.0.0"
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

# Air Quality — Sources (README)

## 📘 Overview

### Purpose
- Record *upstream* air-quality data sources used (or proposed) for the `air-quality` domain, including license/terms, access method, and provenance expectations.
- Provide a single place to confirm that every source used in pipelines is traceable and governance-reviewable (especially for “new external data sources”).

### Scope

| In Scope | Out of Scope |
|---|---|
| Source registry conventions, required metadata fields, link/license expectations, ingestion notes, validation expectations | Air-quality analysis methods, derived dataset definitions, map styling, API contracts, story node narrative content |

### Audience
- Primary: Data engineers and pipeline maintainers, QA/CI maintainers.
- Secondary: Frontend layer maintainers (need dataset attribution), governance reviewers.

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Upstream source**: authoritative provider of raw air-quality measurements or indices.
  - **Derived dataset**: a transformed product produced by KFM pipelines.
  - **Source contract**: machine-readable metadata about an upstream source (path/schema not confirmed here).
  - **Provenance manifest**: PROV/OpenLineage-like record tying outputs to inputs and code version.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `data/air-quality/sources/README.md` | Data | Domain-scoped source registry |
| Air-quality domain root | `data/air-quality/` | Data | Raw/work/processed outputs |
| Pipeline code (air-quality) | `src/pipelines/` | Data/Platform | Path may vary by repo |
| STAC outputs | `data/stac/` or `data/air-quality/stac/` | Data | Collection + items for datasets |
| Provenance outputs | `data/provenance/` or domain folder | Data/Platform | PROV bundles per run |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Each source entry includes a landing page and explicit license/terms reference
- [ ] Each source entry includes access method + update cadence + expected geographic/temporal coverage
- [ ] Validation steps listed (including link/license checks in CI)
- [ ] Governance triggers and sensitivity notes included (if any sources contain restricted locations)

## 🗂️ Directory Layout

### This document
- `path`: `data/air-quality/sources/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed/stac outputs |
| Air-quality domain | `data/air-quality/` | Domain-specific lifecycle folders |
| Documentation | `docs/` | Canonical governed docs |
| Pipelines | `src/pipelines/` | ETL + transforms |
| Schemas | `schemas/` | JSON schemas + contract validation |
| CI / Tests | `tests/` + workflows | Validation and link/license checks |

### Expected file tree for this sub-area
~~~text
📁 data/
└── 📁 air-quality/
    ├── 📁 raw/
    ├── 📁 work/
    ├── 📁 processed/
    ├── 📁 stac/
    ├── 📁 reports/
    ├── 📁 provenance/
    └── 📁 sources/
        └── 📝 README.md
~~~

## 🧭 Context

### Background
Air-quality layers can be time-varying and are often consumed as “current conditions” as well as historical time series. KFM requires deterministic, provenance-linked pipelines: sources must be documented with licenses and stable identifiers, and derived outputs must be publishable into STAC/DCAT/PROV so the UI and Focus Mode can show evidence and attribution.

### Assumptions
- Air-quality sources may include both:
  - Official regulatory monitoring (station-based)
  - Community sensors (may have more complex privacy/terms)
  - Modeled surfaces (gridded, derived)
- The authoritative schema/location for “source contracts” may be centralized (not confirmed here).

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode is preserved.
- Frontend consumes contracts via APIs (no direct graph dependency).
- New external data sources are a governance review trigger (see governance section).

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What are the initial air-quality datasets committed for v12 (pollutants, indices, cadence)? | TBD | TBD |
| Where is the canonical source-contract schema and validator located? | TBD | TBD |
| Do any sources impose redistribution constraints requiring special handling? | TBD | TBD |

### Future extensions
- Add per-source “data dictionary” docs (fields + QA flags).
- Add per-source automated freshness checks (scheduled CI) for API-based sources.
- Add “derived dataset registry” mapping raw → processed → STAC collection ids.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  S[Upstream Sources<br/>APIs / downloads] --> R[data/air-quality/raw]
  R --> W[data/air-quality/work]
  W --> P[data/air-quality/processed]
  P --> C[STAC Collection + Items]
  P --> V[PROV lineage bundle]
  C --> G[Graph index (Neo4j)]
  G --> A[APIs]
  A --> U[Map UI + Focus Mode]
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Upstream source payloads | CSV/JSON/GeoTIFF/etc. | External publishers | Checksums + schema checks (as available) |
| Source metadata | Markdown + (optional) JSON | `data/air-quality/sources/` and/or `data/sources/` | Link/license validation; schema validation if defined |
| Pipeline parameters | JSON/YAML | `src/pipelines/` configs | Schema-validated (if schema exists) |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Normalized tables | Parquet/CSV | `data/air-quality/processed/` | Domain schema (TBD) |
| Geospatial layers | GeoJSON/COG/PMTiles | `data/air-quality/processed/` | Layer contract (TBD) |
| STAC catalog entries | JSON | `data/air-quality/stac/` or `data/stac/` | STAC 1.x + extensions |
| DCAT views | JSON-LD/RDF | `data/dcat/` or `docs/data/` | DCAT profile |
| Provenance | JSON-LD | `data/air-quality/provenance/` | PROV profile |

### Sensitivity & redaction
- Most regulatory air-quality data is public, but community sensor sources may:
  - Include fine-grained location tied to individuals/property
  - Have terms restricting redistribution
- If any source is sensitive:
  - Document required generalization (e.g., aggregate to county/tract or grid)
  - Ensure UI layer gating prevents precise coordinate exposure

### Quality signals
- Completeness: expected station coverage/time coverage per period
- Value sanity: pollutant ranges, AQI range checks, missingness thresholds
- Spatial validity: valid geometries; consistent CRS; station points within expected region

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Each publishable dataset should have:
  - A STAC Collection (dataset-level)
  - STAC Items (per time slice / tile / station set), as appropriate
- Assets should include machine-readable attribution/license fields where applicable.

### DCAT
- Minimum mapping expected:
  - Title, description, license, keywords, publisher/contact
- Use stable dataset identifiers so UI and Focus Mode can reference them.

### PROV-O
- For each pipeline run that produces air-quality outputs:
  - Record the transformation activity and inputs (source ids + versions)
  - Tie outputs to code version (`commit_sha`) for reproducibility

### Versioning
- New versions link predecessor/successor.
- Graph mirrors version lineage.

### Extension points checklist (for future work)
- [ ] Data: new domain added under `data/<domain>/.`
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + access rules
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Air-quality layers may provide contextual evidence for:
  - Environmental events (smoke/dust/drought conditions)
  - Health/environment narratives at place + time
- Focus Mode must only present air-quality claims that trace to dataset ids/time windows.

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID.

### Optional structured controls
~~~yaml
focus_layers:
  - "air_quality_TBD"
focus_time: "TBD"
focus_center: [-98.0000, 38.0000]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] Source link + license checks for any registered source
- [ ] Schema validation (STAC/DCAT/PROV) for published catalogs
- [ ] Data quality checks (ranges, missingness, geometry validity)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) fetch raw source(s)
# 2) run air-quality pipeline
# 3) validate STAC/DCAT/PROV
# 4) run domain quality checks
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| source_link_check_failed | CI | `docs/telemetry/` + `schemas/telemetry/` |
| air_quality_pipeline_run | pipeline | `mcp/runs/` or domain provenance folder |

## ⚖ FAIR+CARE & Governance

### Review gates
- Governance review triggers include:
  - New external data sources
  - Any sources with redistribution restrictions
  - Any source containing potentially sensitive location detail

### CARE / sovereignty considerations
- If a source intersects protected/sovereign communities or sensitive sites:
  - Document redaction/generalization rules
  - Ensure gating is enforced end-to-end (catalog → API → UI)

### AI usage constraints
- Ensure doc’s AI permissions/prohibitions match intended use.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-17 | Initial draft air-quality sources README | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
