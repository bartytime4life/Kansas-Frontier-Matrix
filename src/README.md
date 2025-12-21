---
title: "KFM src/ — Source Code Layout (README)"
path: "src/README.md"
version: "v1.0.0"
last_updated: "2025-12-21"
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

doc_uuid: "urn:kfm:doc:src:readme:v1.0.0"
semantic_document_id: "kfm-src-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:src:readme:v1.0.0"
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

# src/ — KFM Source Code Overview

## 📘 Overview

### Purpose
- Provide a **single, governed map** of what lives under `src/` and how it aligns to KFM’s layered architecture.
- Act as a **navigation + placement contract** so contributors put new code in the correct subsystem and do not break the API boundary.

### Scope
| In Scope | Out of Scope |
|---|---|
| High-level `src/` layout, responsibilities, and contract boundaries | Repo-specific build commands, deployment procedures, and environment secrets |

### Audience
- Primary: KFM developers and maintainers
- Secondary: Data stewards, reviewers, and contributors orienting to KFM’s code layout

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc: ETL, STAC, DCAT, PROV-O, Neo4j, API boundary, Story Nodes, Focus Mode

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide (v12) | `docs/MASTER_GUIDE_v12.md` | TBD | Canonical pipeline + invariants + system inventory |
| v13 Blueprint | `docs/` (see blueprint PDF in architecture set) | TBD | Subsystem design rules + readiness gates |
| Pipelines runbooks | `docs/pipelines/` | TBD | How to run/extend ETL + catalog builds |
| Graph docs | `docs/graph/` | TBD | Ontology, labels/edges, migrations |
| API contracts | `src/server/contracts/` | TBD | Contract-first boundary between UI and graph/catalogs |
| Story Nodes | `docs/reports/story_nodes/` | TBD | Provenance-linked narrative artifacts consumed by UI |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] All claims link to KFM-controlled docs/contracts (as applicable)
- [ ] Validation steps listed and repeatable (placeholders allowed)
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `src/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed outputs, plus catalog + provenance outputs |
| Documentation | `docs/` | Canonical governed docs (Master Guide, runbooks, standards, reports) |
| Pipelines | `src/pipelines/` | ETL + transforms + catalog build orchestration |
| Graph | `src/graph/` | Graph ingestion, ontology bindings, constraints/migrations |
| API boundary | `src/server/` | REST/GraphQL (implementation-defined) + redaction + contracts |
| Schemas | `schemas/` | JSON schemas for STAC/DCAT/PROV/story nodes/telemetry/etc. |
| Frontend | `web/` | React + map clients (MapLibre/Cesium) and layer registries |
| MCP | `mcp/` | Experiments, model cards, prototype runs (non-core) |

### Expected file tree for this sub-area
~~~text
📁 src/
├── 📄 README.md
├── 📁 pipelines/          # ETL + transforms + catalog builders (STAC/DCAT/PROV generation)
├── 📁 graph/              # Graph ingest + ontology bindings + migrations/constraints
└── 📁 server/             # API boundary + contracts + redaction/generalization enforcement
~~~

## 🧭 Context

### Background
- KFM is intentionally **layered**: each stage produces contract artifacts consumed by the next stage.
- `src/` is organized by subsystem so changes remain localized and reviewable.

### Assumptions
- New work follows the Master Guide’s canonical locations and does not introduce UI → database coupling.
- Older/legacy path names (e.g., `src/api/`, `src/web/`) may appear in historical documents; new work should prefer the canonical locations listed above.

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode is preserved.
- Frontend consumes contracts via APIs (no direct graph dependency).
- No unsourced narrative content is published: Story Nodes / Focus Mode must remain provenance-linked.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Are there legacy directories (`src/api/`, `src/web/`) that require migration notes here? | TBD | TBD |
| What is the canonical developer command set for running pipelines/tests in this repo? | TBD | TBD |

### Future extensions
- Extension point A: New data domain ingestion (new ETL pipeline + catalogs + graph linkage)
- Extension point B: New API endpoint (contract + tests + redaction rules + UI consumption)
- Extension point C: New UI layer type (registry entry + schema validation + governance gating)

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[ETL (src/pipelines)] --> B[STAC/DCAT/PROV (data/stac, data/catalog/dcat, data/prov)]
  B --> C[Neo4j Graph (src/graph)]
  C --> D[API boundary (src/server)]
  D --> E[UI (web/)]
  E --> F[Story Nodes (docs/reports/story_nodes)]
  F --> G[Focus Mode (provenance-linked only)]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant UI as UI (web/)
  participant API as API (src/server)
  participant Graph as Graph (Neo4j via src/graph contracts)
  UI->>API: Focus query(entity_id)
  API->>Graph: fetch subgraph + provenance refs
  Graph-->>API: context bundle (entities + evidence refs)
  API-->>UI: narrative + citations + audit flags
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Raw source snapshots | mixed (PDF/CSV/Geo, etc.) | `data/<domain>/raw/` | checksum/hash + schema checks as applicable |
| Work/intermediate transforms | mixed | `data/<domain>/work/` | deterministic transform checks |
| Processed normalized data | tabular/geospatial | `data/<domain>/processed/` | schema + geometry validity + ranges |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| STAC Collections / Items | JSON | `data/stac/**` | `schemas/stac/**` + KFM constraints |
| DCAT dataset records | JSON(-LD) | `data/catalog/dcat/**` | `schemas/dcat/**` |
| PROV bundles | JSON(-LD) | `data/prov/**` | `schemas/prov/**` |
| Graph import artifacts | CSV/Cypher | `data/graph/**` | graph import constraints + ontology bindings |
| API contracts | OpenAPI / GraphQL schema | `src/server/contracts/**` | contract tests required |

### Sensitivity & redaction
- Restricted locations or culturally sensitive knowledge must be protected via:
  - geometry generalization where required,
  - API-level redaction rules,
  - Story Node review gates before publication.

### Quality signals
- Schema validation passes for STAC/DCAT/PROV outputs.
- Deterministic runs and diffable outputs (idempotent pipelines).
- No orphan references (entity/evidence IDs resolve).

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections involved: `data/stac/collections/**`
- Items involved: `data/stac/items/**`
- Extension(s): repo-defined KFM profiles under `schemas/stac/**` (if applicable)

### DCAT
- Dataset identifiers: `data/catalog/dcat/**`
- License mapping: must be explicit and consistent across datasets
- Contact / publisher mapping: provided per dataset record (policy defined in governed docs)

### PROV-O
- `prov:wasDerivedFrom`: connect derived outputs to source entities
- `prov:wasGeneratedBy`: connect outputs to pipeline activities
- Activity / Agent identities: must be stable and traceable (scripts + contributors)

### Versioning
- New versions link predecessor/successor in catalogs and are mirrored in the graph where applicable.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize | Config + run logs |
| Catalogs | STAC/DCAT/PROV emission | JSON + validators |
| Graph | Neo4j ingest + semantics | Cypher + API layer |
| APIs | Serve contracts + governance | REST/GraphQL |
| UI | Map + narrative UX | API calls |
| Story Nodes | Curated narrative artifacts | Graph + docs |
| Focus Mode | Context bundle view | Provenance-linked |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | SemVer + changelog |
| API contracts | `src/server/contracts/` | Backward compatible or version bump + contract tests |
| UI layer registry schema | `schemas/ui/` | Schema-validated in CI |
| UI layer registries | `web/**/layers/**` | Validate against `schemas/ui/` |

### Extension points checklist (for future work)
- [ ] Data: new domain added under `data/<domain>/...`
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + access rules
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Entities become focusable via stable IDs returned by the API.
- Evidence must be shown via resolvable STAC/DCAT/PROV identifiers and provenance/audit affordances.

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID (no uncited facts).

### Optional structured controls
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV)
- [ ] Graph integrity checks
- [ ] API contract tests
- [ ] UI schema checks (layer registry)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) validate schemas
# 2) run unit/integration tests
# 3) run doc lint
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| TBD | TBD | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates
- Changes that affect redaction, sensitive layers, external data sources, or public endpoints require governance review.

### CARE / sovereignty considerations
- Identify communities impacted and protection rules.
- Do not infer or expose sensitive locations; use generalization and redaction policies as required.

### AI usage constraints
- Ensure this doc’s AI permissions/prohibitions match intended use:
  - Allowed: summarize, structure extraction, translate, keyword indexing
  - Prohibited: generating policy, inferring sensitive locations

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-21 | Initial `src/README.md` scaffold aligned to Master Guide v12 / subsystem contracts | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
