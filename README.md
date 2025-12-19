---
title: "Kansas Frontier Matrix — Repository README"
path: "README.md"
version: "v1.0.0"
last_updated: "2025-12-19"
status: "active"
doc_kind: "RepoDoc"
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

doc_uuid: "urn:kfm:doc:repo:readme:v1.0.0"
semantic_document_id: "kfm-repo-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:repo:readme:v1.0.0"
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

# Kansas Frontier Matrix

Kansas Frontier Matrix (KFM) is an open-source geospatial platform designed as a “living atlas” of Kansas—integrating historical, cultural, and ecological data into governed catalogs and a knowledge graph, then serving it through contracted APIs to an interactive map and narrative UI.

Status: active development. Some referenced paths may be planned/expected; they are marked accordingly.

## 📘 Overview

### Purpose
- Provide a governed, reproducible pipeline for transforming heterogeneous Kansas-focused sources (documents, images, maps, GIS layers) into:
  - standards-aligned catalogs (STAC / DCAT / PROV)
  - a queryable knowledge graph (Neo4j)
  - contracted APIs for downstream clients (REST/GraphQL)
  - a map + narrative experience surfaced as Story Nodes and Focus Mode

### Canonical pipeline
KFM preserves the following non-negotiable ordering:

**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

### Scope
| In Scope | Out of Scope |
|---|---|
| Data ingestion + normalization pipelines | Ad-hoc, manual edits to production data without provenance |
| STAC/DCAT/PROV catalog generation + validation | UI clients querying Neo4j directly |
| Knowledge graph build + migrations | Unsourced narrative presented as fact in Focus Mode |
| API contracts and access controls | Publishing sensitive locations without redaction controls |
| Map UI + Story Nodes + Focus Mode | Any behavior that violates FAIR+CARE / sovereignty rules |

### Audience
- Primary: contributors and maintainers (data engineering, GIS, graph, web)
- Secondary: researchers, educators, and downstream integrators using KFM data products

### Definitions
- Glossary: `docs/glossary.md` (not confirmed in repo)

### Key artifacts
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | Maintainers | Canonical pipeline + invariants |
| System architecture | `docs/architecture/` | Maintainers | See architecture doc if present |
| Doc templates | `docs/templates/` | Maintainers | Universal docs, Story Nodes, API contracts |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | DataOps | Machine-validated metadata |
| Security baseline | `.github/SECURITY.md` | Maintainers | Security reporting + standards |

### Definition of done
- [ ] README reflects canonical pipeline ordering and API boundary
- [ ] Repo layout section matches the Master Guide expectations
- [ ] Links resolve (or are marked “not confirmed in repo”)
- [ ] No secrets, credentials, or sensitive locations included

## 🗂️ Directory layout

### This document
- `path`: `README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed data, plus catalog outputs |
| Documentation | `docs/` | Canonical governed docs and standards |
| Pipelines | `src/pipelines/` | ETL + catalog generation |
| Graph | `src/graph/` | Ontology bindings + graph build |
| APIs | `src/server/` | Contracted access layer (REST/GraphQL) |
| Frontend | `web/` | React + map clients (MapLibre and optional Cesium) |
| Schemas | `schemas/` | JSON schemas + telemetry schemas |
| Tests | `tests/` | Unit/integration tests |
| Tools | `tools/` | Developer + data tooling |
| MCP | `mcp/` | Experiments, runs, model cards, SOPs |

### Expected repo tree
~~~text
📁 .github/
├── 📄 SECURITY.md
└── 📁 workflows/
    └── 📄 <ci-workflows>.yml

📁 data/
├── 📁 sources/
├── 📁 raw/
├── 📁 work/
├── 📁 processed/
├── 📁 stac/
│   ├── 📁 collections/
│   └── 📁 items/
├── 📁 catalog/
│   └── 📁 dcat/
└── 📁 prov/

📁 docs/
├── 📄 MASTER_GUIDE_v12.md
├── 📁 templates/
│   ├── 📄 TEMPLATE__KFM_UNIVERSAL_DOC.md
│   ├── 📄 TEMPLATE__STORY_NODE_V3.md
│   └── 📄 TEMPLATE__API_CONTRACT_EXTENSION.md
├── 📁 standards/
└── 📁 architecture/
    └── 📄 <KFM_1_0_SYSTEM_DOCUMENTATION>.pdf

📁 mcp/
├── 📁 runs/
└── 📁 experiments/

📁 schemas/
├── 📁 telemetry/
└── 📄 <json-schemas>.json

📁 src/
├── 📁 pipelines/
│   ├── 📁 etl/
│   └── 📁 catalog/
├── 📁 graph/
└── 📁 server/

📁 tests/
📁 tools/
📁 web/
📁 releases/
~~~

## 🧭 Context

### Background
KFM is built to help users explore Kansas history and environmental change across time and space while keeping evidence and provenance first-class.

### Assumptions
- The repo maintains deterministic, replayable ETL and catalog generation.
- Every public-facing narrative is provenance-linked and auditable.

### Constraints and invariants
- The canonical pipeline ordering is preserved.
- Frontend clients consume data via APIs only (no direct graph access).
- Focus Mode and Story Nodes must be provenance-linked: no unsourced narrative.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What are the repo’s current local dev commands and prerequisites? | TBD | TBD |
| Which governance docs are canonical in this repo version? | TBD | TBD |
| Where is the layer registry schema for the frontend? | TBD | TBD |

### Future extensions
- Add new datasets, evidence artifacts, story node types, and security gates using the extension approach described in the Master Guide.
- Expand telemetry governance signals and story node ingestion/versioning as the system grows.

## 🗺️ Diagrams

### End-to-end dataflow
~~~mermaid
flowchart LR
  A[Raw sources] --> B[ETL + normalization]
  B --> C[STAC items + collections]
  B --> D[DCAT dataset views]
  B --> E[PROV lineage bundles]
  C --> F[Neo4j knowledge graph]
  D --> F
  E --> F
  F --> G[API layer]
  G --> H[React map UI]
  H --> I[Story Nodes]
  I --> J[Focus Mode]
~~~

### Query sequence
~~~mermaid
sequenceDiagram
  participant UI
  participant API
  participant Graph
  UI->>API: Focus query(entity_id)
  API->>Graph: fetch subgraph + provenance refs
  Graph-->>API: context bundle
  API-->>UI: narrative + citations + audit flags
~~~

## 📦 Data and metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Source artifacts | PDF, images, CSV, GeoTIFF, Shapefile, HTML | `data/raw/` and external sources | Checksums + format parsers (not confirmed in repo) |
| Source manifests | YAML/JSON | `data/sources/` | Schema + lint (not confirmed in repo) |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Processed datasets | CSV/GeoPackage/GeoJSON (varies) | `data/processed/` | Dataset-specific schemas |
| STAC catalogs | JSON | `data/stac/` | STAC 1.0 + KFM profile |
| DCAT catalogs | JSON-LD / TTL | `data/catalog/dcat/` | DCAT 3 + KFM profile |
| PROV bundles | JSON-LD (expected) | `data/prov/` | PROV-O + KFM profile |
| Story Nodes | Markdown | `docs/reports/<report>/story_nodes/` | Story Node v3 template |

### Sensitivity and redaction
- Datasets and narratives may include culturally sensitive content.
- Any sensitive locations must be generalized or access-controlled per sovereignty and governance rules.

### Quality signals
- Catalog schema validation (STAC/DCAT/PROV)
- Link integrity checks and referential integrity checks
- Geometry validity checks for geospatial artifacts (not confirmed in repo)

## 🌐 STAC, DCAT and PROV alignment

- **STAC**: Assets with spatial/temporal extent are cataloged as STAC Items and grouped in STAC Collections.
- **DCAT**: Dataset-level views are published for discoverability.
- **PROV-O**: Lineage is captured so outputs can be traced back to inputs and pipeline runs.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize sources | Pipeline configs + run logs |
| Catalogs | Generate STAC/DCAT/PROV | JSON + validators |
| Graph | Semantic integration in Neo4j | Import jobs + constraints |
| APIs | Stable contracted access | REST/GraphQL |
| UI | Map + narrative experience | API calls only |
| Story Nodes | Curated narrative artifacts | Markdown + provenance refs |
| Focus Mode | Contextual synthesis | Provenance-linked context bundle |

### Interfaces and contracts
| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog (not confirmed in repo) |
| API schemas | `src/server/` + docs | Contract tests required |
| UI layer registry | `web/` | Schema-validated (exact path not confirmed in repo) |

### Extension points checklist
- [ ] Data: new domain added under `data/<domain>/...`
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + access rules
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

## 🧠 Story Nodes and Focus Mode

- Story Nodes are curated, machine-ingestible narratives with explicit provenance.
- Focus Mode synthesizes a context bundle for an entity/place/event and must render citations and audit flags.

## 🧪 Validation and CI

### Validation steps
- [ ] Markdown protocol checks for governed docs
- [ ] STAC/DCAT/PROV schema validation
- [ ] Graph integrity checks
- [ ] API contract tests
- [ ] UI schema checks
- [ ] Security and sovereignty scanning gates (as applicable)

### Reproduction
~~~bash
# Replace with repo-specific commands when available.
# Example intent:
# 1) validate schemas
# 2) run unit/integration tests
# 3) run doc lint
~~~

### Telemetry signals
| Signal | Source | Where recorded |
|---|---|---|
| Pipeline run metadata | ETL/catalog jobs | `mcp/runs/` (expected) |
| Catalog validation results | STAC/DCAT/PROV validators | `docs/telemetry/` (not confirmed in repo) |
| Security scan summary | CI | GitHub Actions artifacts (not confirmed in repo) |

## ⚖ FAIR+CARE and governance

- KFM uses FAIR principles for findability, accessibility, interoperability, and reuse.
- KFM applies CARE principles for collective benefit, authority to control, responsibility, and ethics—especially for indigenous and culturally sensitive content.

### Review gates
- New sensitive layers, new AI narrative behaviors, new external data sources, or new public endpoints require human review.

## 🤝 Contributing

- Read the Master Guide first: `docs/MASTER_GUIDE_v12.md`
- Use governed templates in `docs/templates/` for:
  - story nodes
  - API contract changes
  - any new governed docs
- Prefer deterministic, idempotent pipelines and include provenance for any new outputs.

## 🕰️ Version history

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial README scaffold aligned to Master Guide v12 | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
