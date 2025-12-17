---
title: "KFM Data Directory — README"
path: "data/README.md"
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

doc_uuid: "urn:kfm:doc:data:readme:v1.0.0"
semantic_document_id: "kfm-data-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:readme:v1.0.0"
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

# KFM Data Directory — README

## 📘 Overview

### Purpose
- Define what belongs in `data/` and how it moves through the canonical KFM data lifecycle:
  `data/raw → data/work → data/processed` and into catalog outputs under `data/stac/`.
- Provide a single, governed place to describe **where** data artifacts live, **what quality gates apply**, and **how provenance + sensitivity are handled** before data is treated as “publishable / certified”.

### Scope
| In Scope | Out of Scope |
|---|---|
| Folder conventions and staging rules for `data/` | Implementation details of ETL jobs (see `src/pipelines/`) |
| Expectations for dataset-level README/schema docs | Graph ontology/modeling rules (see `docs/graph/`) |
| Provenance and catalog output placement (STAC/DCAT/PROV) | API/UI behavior (see `src/server/`, `web/`) |
| Sensitivity / redaction expectations for data artifacts | Governance policy authoring (see `docs/governance/`) |

### Audience
- Primary: Data + pipeline contributors maintaining ingestion and transforms
- Secondary: Reviewers (governance/security), historians/editors validating source traceability, UI/API developers consuming cataloged products

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **raw**: Landed source materials as received (or as close as feasible)
  - **work**: Intermediate artifacts created during cleaning/normalization
  - **processed**: Certified, “publishable” artifacts intended for downstream use (catalog + graph ingestion)
  - **catalogs**: Machine-readable metadata products (STAC/DCAT/PROV) used for discovery + lineage

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Canonical pipeline ordering | `docs/MASTER_GUIDE_v12.md` | KFM Maintainers | “ETL → catalogs → graph → APIs → UI → story” |
| Data staging rules (summary) | `data/README.md` | Data/Pipeline Maintainers (TBD) | This document |
| Data domains and stage folders | `data/raw/`, `data/work/`, `data/processed/` | Data/Pipeline Maintainers (TBD) | Source → intermediate → certified |
| Catalog outputs | `data/stac/` | Data/Pipeline Maintainers (TBD) | STAC/DCAT/PROV outputs (plus mappings in `docs/data/`) |
| Pipeline implementation | `src/pipelines/` | Engineering | ETL + transforms + catalog build |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Directory tree reflects current `data/` layout (no invented paths)
- [ ] Staging semantics are explicit (what belongs in raw/work/processed)
- [ ] Validation steps listed and repeatable (even if “TBD: see pipeline docs”)
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `data/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed/stac outputs |
| Raw inputs | `data/raw/` | Landed inputs (or references/pointers if large) |
| Working / staging | `data/work/` | Intermediate artifacts + normalization outputs |
| Certified outputs | `data/processed/` | Curated, downstream-ready data products |
| Catalog products | `data/stac/` | STAC/DCAT/PROV outputs used for discovery + lineage |
| Catalog mappings | `docs/data/` | Mapping docs / profiles that explain catalog fields |
| ETL + builds | `src/pipelines/` | Deterministic transforms and catalog generation |
| Schemas | `schemas/` | JSON schemas / validation contracts (where applicable) |
| Runs / experiments | `mcp/` | Experiment logs, model cards, SOPs (not data storage) |

### Expected file tree for this sub-area
~~~text
data/
├── 📄 README.md
├── 📁 raw/
│   └── 📁 <domain>/
│       └── 📄 <source artifacts…>
├── 📁 work/
│   └── 📁 <domain>/
│       └── 📄 <intermediate artifacts…>
├── 📁 processed/
│   └── 📁 <domain>/
│       ├── 📄 README.md
│       └── 📄 <certified artifacts…>
└── 📁 stac/
    └── 📄 <catalog outputs…>
~~~

## 🧭 Context

### Background
KFM treats data as a governed product. Data artifacts move through explicit stages so that:
- raw inputs remain auditable,
- intermediate work can be reproduced or discarded safely,
- processed outputs are stable inputs into catalog generation and graph ingestion.

Large data artifacts may be tracked outside Git using DVC (pointers + checksums in-repo) while keeping code + metadata version-synchronized. (If DVC is enabled in this repository, contributors should follow the project’s DVC conventions and remotes.)

### Assumptions
- Each dataset belongs to a **domain** (folder name conventions are project-specific).
- Anything in `data/processed/` is assumed **safe enough** and **validated enough** to drive cataloging and downstream consumption (graph/API/UI) without ad-hoc fixes.

### Constraints / invariants
- Canonical pipeline ordering is preserved: ETL → STAC/DCAT/PROV catalogs → Graph → APIs → UI → Story Nodes → Focus Mode.
- Promotion to `data/processed/` happens only after validation gates (schema/quality/provenance/sensitivity) are satisfied.
- If sensitivity is involved (e.g., culturally sensitive site locations), data must be generalized/redacted prior to public outputs.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What are the canonical domain folder names under `data/*/`? | TBD | TBD |
| Where is the authoritative dataset registry/changelog maintained (STAC only, or additional log)? | TBD | TBD |
| Are large binaries tracked via DVC in this repo (and where is the DVC remote documented)? | TBD | TBD |
| What is the retention policy for `data/work/` intermediates? | TBD | TBD |

### Future extensions
- Add a new data domain:
  - create parallel `raw/work/processed` subfolders,
  - add dataset-level `README.md` describing sources and transforms,
  - ensure catalog outputs exist in `data/stac/` with provenance.
- Add/standardize dataset schemas under `schemas/` for stronger CI validation.

## 🗺️ Diagrams

### UI / dataflow diagram
~~~mermaid
 flowchart LR
  U["User"] --> C["Map Controls UI (React)"]
  R["Layer Registry / Catalog JSON"] --> C
  C --> S["Map State"]
  S --> M["Map Engine (MapLibre/Leaflet/Cesium)"]
  S --> A11Y["ARIA Status / Live Region"]
  C --> API["APIs"]
  API --> G["Graph/Data Services"]
  C --> D["Dossier / Details Panel"]
  D --> A11Y
~~~

### System / dataflow diagram
~~~mermaid
 flowchart LR
  subgraph DATA["data/"]
    R["data/raw"] --> W["data/work"] --> P["data/processed"]
  end

  P --> C["data/stac (STAC/DCAT/PROV)"]
  C --> G["Neo4j graph"]
  G --> A["APIs"]
  A --> U["Web UI"]
  U --> S["Story Nodes"]
  S --> F["Focus Mode"]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant Contributor
  participant Pipeline as ETL/Pipeline
  participant Catalog as STAC/DCAT/PROV
  Contributor->>Pipeline: Add/refresh raw sources in data/raw/<domain>/
  Pipeline->>Pipeline: Normalize + stage intermediates in data/work/<domain>/
  Pipeline->>Pipeline: Validate + certify outputs in data/processed/<domain>/
  Pipeline->>Catalog: Emit/refresh catalog entries in data/stac/
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Source datasets | mixed (CSV/GeoJSON/GeoTIFF/etc.) | External authoritative sources | Checksums; format sanity; schema checks (where defined) |
| Source documents | mixed (PDF/text/images) | Archives/collections | Metadata completeness; provenance references |
| Geometries | GeoJSON/WKT/etc. | Derived from source or authoritative geodata | Geometry validity checks; CRS checks |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Raw landed artifacts | mixed | `data/raw/<domain>/` | Source inventory + checksums (as applicable) |
| Intermediate transforms | mixed | `data/work/<domain>/` | Repeatable transforms (pipeline-defined) |
| Certified datasets | mixed | `data/processed/<domain>/` | Domain schema/README required |
| Catalog metadata | JSON (+ JSON-LD where applicable) | `data/stac/` (+ mappings in `docs/data/`) | KFM-STAC/KFM-DCAT/KFM-PROV profiles |

### Sensitivity & redaction
- Before promotion to `data/processed/`, pipelines and/or reviewers should:
  - scan for sensitive information (PII, culturally sensitive locations),
  - generalize/omit fields as required by governance,
  - mark artifacts requiring restricted handling (if applicable).

### Quality signals
- Define and enforce, per domain as needed:
  - completeness checks (required fields present),
  - range checks for numeric attributes,
  - geometry validity (where spatial),
  - provenance completeness (source + transformation references),
  - deterministic output generation (no “untracked manual fixes”).

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- `data/stac/` stores catalog outputs describing data products for discovery.
- Processed artifacts should be represented as STAC Collections/Items with assets pointing to the data (or to external storage locations, if used).
- Extensions may be used for domain metadata where needed (consistent with KFM-STAC profile).

### DCAT
- DCAT dataset descriptors should be derivable from the same authoritative metadata used for STAC.
- License + publisher/contact metadata should be explicit and consistent with governance rules.

### PROV-O
- Provenance must link outputs back to inputs and processing activities:
  - `prov:used`: which inputs were consumed
  - `prov:wasGeneratedBy`: which activity produced the output
  - `prov:wasDerivedFrom`: derivation relationships when applicable
- Run/activity identifiers should be stable enough to support auditing.

### Versioning
- Use STAC Versioning links and graph predecessor/successor relationships as applicable.
- When a dataset is updated, ensure older versions remain traceable (via provenance and/or catalog links).
