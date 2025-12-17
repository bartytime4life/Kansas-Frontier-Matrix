---
title: "Air Quality — Sources README"
path: "data/air-quality/sources/README.md"
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

# Air Quality — Sources README

## 📘 Overview

### Purpose
This README governs how upstream **air-quality data sources** are documented for the `data/air-quality/` domain. It exists to ensure that every source has:
- clear provenance (where it came from),
- clear legal/usage notes (license/terms),
- clear acquisition method (API/download),
- clear update cadence and versioning expectations.

This file is the “human-facing index” for sources; the ETL → Catalog → Graph → API → UI pipeline remains the canonical flow.

### Scope
| In Scope | Out of Scope |
|---|---|
| Upstream sources feeding the air-quality domain | Building new APIs/endpoints (use API Contract Extension template) |
| License/terms notes, attribution, and access method | Full ETL implementation details (covered in pipeline docs/code) |
| Expected raw/work/processed staging behavior | Ontology/schema changes (covered in graph/schema docs) |
| How sources map to STAC/DCAT/PROV entries | UI styling choices for the layer (covered in UI design docs) |

### Audience
- Primary: Data engineers (ETL), catalog maintainers, QA
- Secondary: Curators, UI integrators, governance reviewers

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Source**: An upstream provider and access method for air-quality observations.
  - **Raw**: Immutable acquired artifacts (as-downloaded).
  - **Work**: Intermediate transforms/staging (not guaranteed stable).
  - **Processed**: Stable outputs intended for catalogs/graph/UI.
  - **STAC/DCAT/PROV**: Catalog + metadata + provenance artifacts supporting traceability.

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `data/air-quality/sources/README.md` | Data | Source inventory + requirements |
| Domain raw | `data/air-quality/raw/` | Data | Downloaded artifacts (immutable) |
| Domain work | `data/air-quality/work/` | Data | Staging + normalization |
| Domain processed | `data/air-quality/processed/` | Data | Stable datasets for catalog/graph |
| STAC/DCAT/PROV outputs | `data/stac/` + `docs/data/` | Data | Catalog + mappings + provenance bundles |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Each source entry documents: access method, terms/license, cadence, and identifiers
- [ ] Inputs/outputs tables updated to match actual artifacts produced
- [ ] Validation steps listed and repeatable
- [ ] Sensitivity and redaction considerations recorded (especially for any privately hosted sensors)
- [ ] Governance review gates identified for adding new sources

## 🗂️ Directory Layout

### This document
- `path`: `data/air-quality/sources/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Domain folders: raw/work/processed |
| Pipelines | `src/pipelines/` | ETL + transforms + catalog build |
| Schemas | `schemas/` | STAC/DCAT/PROV + domain schemas |
| Documentation | `docs/` | Catalog docs, governance, design docs |
| Graph | `src/graph/` | Graph build + ontology bindings |
| Frontend | `web/` | React map client + layer integration |

### Expected file tree for this sub-area
~~~text
data/
  air-quality/
    sources/
      README.md
    raw/
    work/
    processed/
~~~

## 🧭 Context

### Background
Air-quality layers (measurements, indices, derived products) are high-value for environmental narratives and can contextualize events and places in Focus Mode. Sources may vary in cadence (hourly/daily), coverage (point stations vs gridded products), and licensing.

### Assumptions
- Raw artifacts are preserved to support audits and reproducibility.
- Processed outputs are the only inputs to catalog/graph/UI by default.
- Provenance is recorded for each processing run and output artifact.

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode ordering is preserved.
- Frontend consumes contracts via APIs (no direct graph dependency).
- No content should surface in Focus Mode without provenance references.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Which upstream sources are in-scope for v1? | Data | TBD |
| What spatial representation do we standardize on (station points vs grids vs tiles)? | Data/UI | TBD |
| What temporal resolution is “stable” for processed outputs? | Data | TBD |

### Future extensions
- Add a machine-readable sources registry file (e.g., `sources.yaml`) if/when a governed schema is agreed.
- Add derived “air quality story evidence” artifacts (plots, summaries) as versioned outputs.

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

> Mermaid rendering note: keep each edge on its own line (as above) and avoid placing mermaid blocks inside tables.

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant Scheduler
  participant ETL as Air-Quality ETL Job
  participant Raw as data/air-quality/raw
  participant Work as data/air-quality/work
  participant Proc as data/air-quality/processed
  participant STAC as STAC Builder
  participant PROV as PROV Writer

  Scheduler->>ETL: start(run_id)
  ETL->>Raw: acquire artifacts (download/API)
  ETL->>Work: normalize + stage
  ETL->>Proc: export stable outputs
  ETL->>STAC: write collection + items
  ETL->>PROV: write provenance bundle
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Source artifacts (as acquired) | files / API responses | Upstream providers | Hashing + basic format checks |
| Source metadata | structured text | This README + (optional) registry | Human review + schema (if available) |

**Source entry template (for consistent documentation)**
~~~yaml
- source_id: "<stable-id>"
  name: "<human-name>"
  publisher: "<org/agency/community>"
  access:
    type: "api|download|other"
    endpoint: "<tbd>"
    auth: "none|key|oauth|tbd"
  license: "<tbd>"
  update_cadence: "<tbd>"
  spatial_coverage: "US-KS|<tbd>"
  temporal_coverage: "<tbd>"
  variables:
    - "<tbd>"
  notes: "<tbd>"
~~~

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Raw source archive | original formats | `data/air-quality/raw/` | Naming + checksums (project convention) |
| Staging intermediates | parquet/csv/geojson/etc | `data/air-quality/work/` | Internal (not stable) |
| Stable processed datasets | parquet/csv/geojson/tiles/etc | `data/air-quality/processed/` | Domain schema (if defined) |
| STAC collection + items | JSON | `data/stac/` (or domain output path) | STAC validators |
| PROV lineage bundle | JSON-LD / Turtle / JSON | `docs/data/` (or domain output path) | PROV shape/validation rules |

### Sensitivity & redaction
- Environmental data is often public, but **sensor location** can be sensitive if it implies a private residence or protected site.
- If any upstream data includes privately hosted sensors, define generalization/redaction rules before surfacing in UI/Focus Mode.

### Quality signals
- Completeness: missing values by time/region are measured and reported.
- Validity: coordinates in expected bounds; timestamps parseable and monotonic per station/source.
- Consistency: units documented and normalized; variable names stable.
- Deduplication: repeated station-time observations handled deterministically.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections involved: `TBD` (recommend a stable ID like `air-quality` once confirmed)
- Items involved: `TBD` (e.g., per station/time, per day, per tile, depending on product)
- Extension(s): `TBD` (use as applicable; include versioning if source updates)

### DCAT
- Dataset identifiers: `TBD`
- License mapping: record upstream terms clearly and map to DCAT license fields as supported.
- Contact / publisher mapping: capture publisher/org and any attribution requirements.

### PROV-O
- `prov:wasDerivedFrom`: processed outputs → raw artifacts
- `prov:wasGeneratedBy`: processed outputs → ETL run activity
- Activity / Agent identities: stable run IDs + pipeline identity (software agent)

### Versioning
- Use STAC Versioning links and graph predecessor/successor relationships as applicable.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| ETL | Acquire + normalize air-quality sources | Config + run logs |
| Catalogs | STAC/DCAT/PROV | JSON + validators |
| Graph | Index datasets + link to entities | Neo4j + API layer |
| APIs | Serve contracted access | REST/GraphQL |
| UI | Layer rendering + narrative | API calls |
| Focus Mode | Provenance-linked context | Context bundle |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Data domain layout | `data/air-quality/` | Keep paths stable |
| Catalog schemas | `data/stac/` + `schemas/` | Semver + changelog |
| API payloads | `src/server/` + docs | Contract tests required |

### Extension points checklist (for future work)
- [ ] Data: new source documented here and added to acquisition logic
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: labels/relations mapped + migration plan (if needed)
- [ ] APIs: contract version bump + tests (if new outputs are exposed)
- [ ] UI: layer registry entry + access rules
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump (if needed)

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Air-quality layers may appear as:
  - a map overlay (points/tiles),
  - a time-series chart in a Focus panel,
  - evidence artifacts (plots) linked to the underlying STAC items.
- Focus Mode must be able to cite dataset/asset IDs for any charted or narrated value.

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID.

### Optional structured controls
~~~yaml
focus_layers:
  - "air-quality"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV)
- [ ] Domain QA checks (time/space bounds, missingness, units)
- [ ] Graph integrity checks (if indexed)
- [ ] UI schema checks (if layer registry is updated)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) run ETL for air-quality domain (deterministic)
# 2) validate STAC items/collections
# 3) validate PROV bundle
# 4) run domain QA checks
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| etl.air_quality.run | ETL | `docs/telemetry/` + `schemas/telemetry/` |
| etl.air_quality.qa | ETL | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates
- Add/change sources: data owner review + governance review for licensing and sensitivity.
- If privately hosted sensors are included: require explicit sensitivity handling review.

### CARE / sovereignty considerations
- If any data implicates sensitive locations or protected communities, follow sovereignty and redaction rules before publishing in public layers.

### AI usage constraints
- Ensure this doc’s AI permissions/prohibitions match intended use (no policy generation; no sensitive-location inference).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-17 | Initial sources README scaffold for air-quality domain | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
