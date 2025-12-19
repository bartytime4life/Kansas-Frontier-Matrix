---
title: "KFM Pipelines — README"
path: "src/pipelines/README.md"
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

doc_uuid: "urn:kfm:doc:src:pipelines:readme:v1.0.0"
semantic_document_id: "kfm-src-pipelines-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:src:pipelines:readme:v1.0.0"
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

# KFM Pipelines

## 📘 Overview

### Purpose
`src/pipelines/` contains pipeline code that moves data through the **canonical KFM flow**:
ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode.

This README documents:
- What belongs in `src/pipelines/` (and what does not)
- How pipeline outputs should hand off cleanly to catalogs and graph ingestion
- The minimum reproducibility + provenance expectations for pipeline work

### Scope

| In Scope | Out of Scope |
|---|---|
| ETL orchestration + transforms | UI rendering and map layers (`web/`) |
| Catalog generation (STAC / DCAT / PROV) | Direct UI ↔ graph access (forbidden by architecture) |
| Graph build preparation artifacts (inputs for `src/graph/`) | API contracts and endpoint behavior (`src/server/` docs) |
| Pipeline validation + run logs conventions | Story Node authoring (lives under `docs/reports/.../story_nodes/`) |

### Audience
- Primary: Data engineers, pipeline maintainers, ingestion contributors
- Secondary: Graph/API/UI developers who consume pipeline outputs

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc: ETL, STAC, DCAT, PROV-O, “run ID”, “provenance”, “deterministic pipeline”

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Pipeline subsystem docs | `docs/pipelines/` | Maintainers | Design + runbooks (if present) |
| STAC outputs | `data/stac/` | Data/Catalog | Collections + Items |
| DCAT outputs | `data/catalog/dcat/` | Data/Catalog | Dataset views |
| PROV outputs | `data/prov/` | Data/Catalog | Lineage bundles |
| Graph ingestion | `src/graph/` | Graph | Pipelines should not bypass graph ingestion code |

### Definition of done (for this document)
- [ ] Front-matter complete + valid (`path` matches this file)
- [ ] Folder purpose + boundaries are explicit
- [ ] Inputs/outputs + handoffs are described (even if some are TBD)
- [ ] Validation steps are listed and repeatable (no “magic”)
- [ ] Governance + CARE/sovereignty considerations are stated

## 🗂️ Directory Layout

### This document
- `path`: `src/pipelines/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed/stac outputs |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | STAC/DCAT/PROV materializations |
| Documentation | `docs/` | Canonical governed docs + templates |
| Pipeline docs | `docs/pipelines/` | Pipeline design docs + runbooks |
| Graph | `src/graph/` | Ontology + migrations + ingestion into Neo4j |
| APIs | `src/server/` | Contracted API layer (UI must not call Neo4j directly) |
| Schemas | `schemas/` | JSON schemas (STAC/DCAT/telemetry/etc.) |
| Frontend | `web/` | React + MapLibre/Cesium clients |
| MCP runs | `mcp/` | Experiments + run artifacts (if used) |

### Expected file tree for this sub-area
> NOTE: This is an **expected / recommended layout**. Exact subfolders, CLIs, and runner names are **not confirmed in repo** yet—adjust to match the implementation.

~~~text
📁 src/pipelines/
├── 📄 README.md
├── 📁 etl/                      # extraction + normalization + enrichment (recommended)
│   ├── 📁 configs/               # pipeline configs (YAML/JSON/etc.)
│   ├── 📁 extract/               # source readers/parsers
│   ├── 📁 transform/             # normalization + enrichment steps
│   ├── 📁 load/                  # writes into data/work, data/processed, etc.
│   └── 📁 runners/               # entrypoints/orchestrators
├── 📁 catalog/                   # build STAC/DCAT/PROV outputs (recommended)
│   ├── 📁 stac/
│   ├── 📁 dcat/
│   ├── 📁 prov/
│   └── 📁 validators/
├── 📁 graph_build/               # optional: prep artifacts for src/graph ingestion
├── 📁 shared/                    # shared IO, hashing, logging, utilities
└── 📁 tests/                     # pipeline unit + integration tests
~~~

## 🧭 Context

### Background
KFM is designed as a governed geospatial + historical knowledge system with strict provenance.
Pipelines are the “front door” for new sources, and they must be reproducible, auditable, and standards-aligned.

### Assumptions
- Pipelines are deterministic and idempotent wherever practical.
- Pipeline runs produce stable identifiers and record run metadata (run ID, inputs, outputs, hashes, warnings).
- Catalog artifacts (STAC/DCAT/PROV) are the handoff contract to graph ingestion and downstream systems.

### Constraints / invariants
- **Canonical ordering is preserved:** ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode.
- **API boundary:** the UI never reads Neo4j directly; it consumes contracts via the API layer.
- **No unsourced narrative:** anything that eventually appears in Focus Mode must remain provenance-linked.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What is the canonical pipeline runner/CLI entrypoint? | TBD | TBD |
| Where are pipeline configs stored and how are they validated? | TBD | TBD |
| What is the standard run ID format and where are run logs persisted? | TBD | TBD |

### Future extensions
- Extension point A: Add a new domain ingestion “kit” (parsers + validators + catalog mapping).
- Extension point B: Add evidence artifact generation (derived assets as STAC assets, linked into graph and Focus Mode).

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[ETL: Extract/Transform/Load] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React/Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
~~~

### Optional: pipeline internal flow (recommended)
~~~mermaid
flowchart LR
  S[Raw Sources] --> X[Extract]
  X --> N[Normalize]
  N --> E[Enrich]
  E --> P[data/processed/]
  P --> STAC[data/stac/]
  P --> DCAT[data/catalog/dcat/]
  P --> PROV[data/prov/]
  STAC --> G[Graph ingestion inputs]
  DCAT --> G
  PROV --> G
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Source assets | PDF/CSV/GeoJSON/etc. | `data/raw/` or external registries | checksum + parser validation |
| Pipeline configs | YAML/JSON/etc. | `src/pipelines/**/configs/` (recommended) | schema validation (TBD) |
| Schemas | JSON Schema / RDF shapes | `schemas/` | CI schema lint |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Normalized datasets | domain-specific | `data/processed/` | domain schema (TBD) |
| STAC catalog | JSON | `data/stac/` | STAC profile (KFM-STAC) |
| DCAT dataset views | JSON-LD/Turtle/etc. | `data/catalog/dcat/` | DCAT profile (KFM-DCAT) |
| PROV lineage bundles | JSON-LD/Turtle/etc. | `data/prov/` | PROV profile (KFM-PROV) |
| Run logs / manifests | JSON/MD | `mcp/runs/` (or repo standard) | telemetry schema (if present) |

### Sensitivity & redaction
- Some sources may include sensitive locations or culturally sensitive content.
- Pipelines must support:
  - **Redaction** (remove restricted fields from public outputs)
  - **Generalization** (coarsen geometry/time when required)
  - **Auditability** (keep private/raw material access controlled, but provenance intact)

### Quality signals
- Completeness checks (required fields populated)
- Geometry validity (where applicable)
- Temporal sanity checks (ranges, missing dates)
- Schema validation for STAC/DCAT/PROV artifacts
- Hash-based reproducibility checks (input→output mapping)

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections involved: domain collections under `data/stac/collections/` (expected)
- Items involved: asset items under `data/stac/items/` (expected)
- Extension(s): use KFM’s STAC profile versions defined in front-matter

### DCAT
- Dataset identifiers: map each dataset to a DCAT record under `data/catalog/dcat/`
- License mapping: ensure license appears in catalog artifacts
- Contact / publisher mapping: ensure publisher/maintainer metadata is present

### PROV-O
- `prov:wasDerivedFrom`: list source IDs / source asset identifiers
- `prov:wasGeneratedBy`: pipeline activity/run ID
- Activity / Agent identities: pipeline runner identity + contributor/automation identity (as applicable)

### Versioning
- New versions should link predecessor/successor at the catalog layer and be mirrored in graph lineage.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize | Config + run logs |
| Catalogs | STAC/DCAT/PROV | JSON/LD artifacts + validators |
| Graph | Neo4j | Populated only via graph ingestion layer |
| APIs | Serve contracts | REST/GraphQL |
| UI | Map + narrative | API calls only |
| Story Nodes | Curated narrative | Graph + docs |
| Focus Mode | Contextual synthesis | Provenance-linked bundle |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog |
| Catalog profiles | front-matter + docs | pinned versions (KFM-STAC/DCAT/PROV) |
| Pipeline run metadata | `mcp/runs/` or repo standard | schema-validated when present |

### Extension points checklist (for future work)
- [ ] Data: new domain added under `data/<domain>/...`
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests (if new endpoints)
- [ ] UI: layer registry entry + access rules (if new layers)
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Pipelines do not “author” narrative, but they produce the **evidence layer** that narrative consumes.
- Any derived artifacts that are used in narrative must be cataloged and provenance-linked.

### Provenance-linked narrative rule
- Every claim that reaches Focus Mode must trace to a dataset / record / asset ID.

### Optional structured controls
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (front-matter + structure)
- [ ] Schema validation (STAC/DCAT/PROV)
- [ ] Graph integrity checks (when ingesting outputs)
- [ ] Pipeline unit tests + integration tests (recommended)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands.
# Not confirmed in repo:
# 1) run ETL
# 2) build catalogs
# 3) validate artifacts
# 4) run tests

# e.g.
# <repo-cli> pipelines etl --config <path>
# <repo-cli> pipelines catalog --stac --dcat --prov
# <repo-cli> validate --stac data/stac --dcat data/catalog/dcat --prov data/prov
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| pipeline_run_id | pipeline runner | `mcp/runs/` or telemetry store |
| input_hashes | ETL | run manifest |
| output_hashes | ETL/Catalog | run manifest |
| validation_errors | validators | CI logs + artifacts |

## ⚖ FAIR+CARE & Governance

### Review gates
- New external sources: requires review (license + provenance + sensitivity)
- New sensitive layers: requires sovereignty + ethics review
- New public-facing outputs: ensure redaction/generalization rules are implemented

### CARE / sovereignty considerations
- Identify communities impacted and protection rules (especially for culturally sensitive sites).
- Do not infer sensitive locations or publish restricted coordinates.

### AI usage constraints
- This doc permits summarization/structure extraction, but prohibits generating new policy or inferring sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial `src/pipelines/` README scaffold | TBD |

---
Footer refs:
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
