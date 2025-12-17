---
title: "KFM Docs — README"
path: "docs/README.md"
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

doc_uuid: "urn:kfm:doc:docs:readme:v1.0.0"
semantic_document_id: "kfm-docs-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:docs:readme:v1.0.0"
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

# docs/ — Documentation Hub

## 📘 Overview

### Purpose
This README is the entry point for KFM’s governed documentation. It tells you **where to find** canonical specs, templates, and subsystem docs, and **how to add/change docs** without breaking pipeline contracts.

### Scope
| In Scope | Out of Scope |
|---|---|
| Documentation navigation, doc placement, doc templates, and doc-to-pipeline mapping | Implementing ETL/graph/API/UI code changes (those live in `src/`, `web/`, etc.) |

### Audience
- Primary: contributors writing or updating KFM docs
- Secondary: reviewers validating governance, provenance, and contract alignment

### Definitions (link to glossary)
- Link: `docs/glossary.md` *(not confirmed in repo — add if missing)*
- Terms used in this doc: pipeline, STAC/DCAT/PROV, ontology, Story Node, Focus Mode

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guides | `docs/MASTER_GUIDE_v11.md`, `docs/MASTER_GUIDE_v12.md` | Maintainers | Canonical pipeline + system map |
| Governed templates | `docs/templates/` | Maintainers | Required structures for docs |
| Standards | `docs/standards/` | Maintainers | Markdown protocol + schema profiles |
| Subsystem docs | `docs/data/`, `docs/pipelines/`, `docs/graph/`, `docs/design/`, `docs/security/`, `docs/telemetry/` | Subsystem owners | Specs and operational notes |
| Story Nodes | `docs/reports/**/story_nodes/` | Editorial + Maintainers | Narrative artifacts for Focus Mode |

### Definition of done (for this document)
- [x] Front-matter complete + valid
- [x] Provides a docs map aligned to the canonical pipeline
- [x] Points to governed templates and standards
- [x] Notes governance + CARE/sovereignty considerations

## 🗂️ Directory Layout

### This document
- `path`: `docs/README.md` *(must match front-matter)*

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed/STAC outputs |
| Documentation | `docs/` | Canonical governed docs |
| Graph | `src/graph/` + `docs/graph/` | Ontology, labels, relationships, migrations |
| Pipelines | `src/pipelines/` + `docs/pipelines/` | ETL, transforms, catalog build, graph build |
| APIs | `src/server/` + `docs/` | Contracted access layer (REST/GraphQL) |
| Frontend | `web/` + `docs/design/` | Map layers, Focus Mode UX, a11y |
| Telemetry | `docs/telemetry/` + `schemas/telemetry/` | Observability, security, governance metrics |
| Security | `.github/SECURITY.md` + `docs/security/` | Policy + technical standards |
| MCP | `mcp/` + `docs/templates/` | Experiments, model cards, SOPs |

### Expected file tree for this sub-area
~~~text
📁 docs/
├─ 📄 README.md
├─ 📄 MASTER_GUIDE_v11.md               # current baseline (not confirmed in repo)
├─ 📄 MASTER_GUIDE_v12.md               # draft evolution guide
├─ 📁 🧾 standards/                      # KFM-MDP + governed standards
├─ 📁 🧩 templates/                      # governed doc templates
│  ├─ 📄 TEMPLATE__KFM_UNIVERSAL_DOC.md
│  ├─ 📄 TEMPLATE__STORY_NODE_V3.md
│  └─ 📄 TEMPLATE__API_CONTRACT_EXTENSION.md
├─ 📁 🗺️ data/                           # STAC/DCAT mappings, catalog notes
├─ 📁 🧪 pipelines/                       # ETL + catalog build documentation
├─ 📁 🕸️ graph/                           # ontology + graph conventions
├─ 📁 🌐 api/                             # API docs (not confirmed in repo)
├─ 📁 🎨 design/                          # UI/UX + Focus Mode design notes
├─ 📁 🔐 security/                        # security governance manual
├─ 📁 📈 telemetry/                       # logging/metrics governance
└─ 📁 🧵 reports/                          # research notes + Story Nodes
   └─ 📁 📚 story_nodes/                  # optional grouping shortcut (not confirmed in repo)
~~~

## 🧭 Context

### Background
KFM is a geospatial + historical knowledge system with governed data, catalogs, graph semantics, APIs, and a map/narrative UI. The documentation here exists to keep those layers consistent, reviewable, and reproducible.

### Assumptions
- Contributors will use a governed template for any new/updated document.
- Directory names listed above are the **canonical targets**; if a folder doesn’t exist yet, it should be introduced via a standard PR (not ad-hoc in unrelated changes).

### Constraints / invariants
- **Canonical pipeline ordering is preserved:** ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → UI → Story Nodes → Focus Mode.
- The frontend consumes contracts via APIs (no direct graph dependency).

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Do we want `docs/api/` (human docs) separate from generated OpenAPI/GraphQL schema outputs? | Maintainers | TBD |
| Should Story Nodes live only under `docs/reports/**/story_nodes/` or also under a single `docs/reports/story_nodes/` index? | Editorial | TBD |

### Future extensions
- A generated `docs/INDEX.md` (or site nav) built from a docs manifest.
- A docs linter gate (link checks + template compliance) wired into CI *(not confirmed in repo)*.

### How to add or update a doc (governed flow)
1. **Pick the right template** (one doc → one template):
   - **Story Node / Focus Mode narrative** → `docs/templates/TEMPLATE__STORY_NODE_V3.md`
   - **API contract change** → `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
   - **Everything else** → `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
2. **Set front-matter**: update `title`, `path`, `version`, `last_updated`, `status`. Keep governance and protocol references intact.
3. **Place the doc** in the folder that matches its pipeline layer (see “Docs map” below).
4. **Make provenance explicit**: link to dataset IDs, schema IDs, tickets, and/or commits where applicable.
5. **Run local checks** *(not confirmed in repo)*: markdown lint, link check, any schema validators.

### Docs map (where to put what)
| You’re documenting… | Put it here | Notes |
|---|---|---|
| Data sources, STAC/DCAT mappings, catalog conventions | `docs/data/` | Keep dataset IDs and collection/item references consistent |
| ETL steps, transforms, catalog build jobs | `docs/pipelines/` | Include validation/repro steps and inputs/outputs |
| Ontology terms, graph schema, migrations | `docs/graph/` | Align to `KFM-ONTO` version and label conventions |
| API endpoints, GraphQL schema, versioning policy | `docs/api/` or relevant doc area | Use API contract template for changes |
| Focus Mode UX, map layers, accessibility | `docs/design/` | UX should stay behind API contracts |
| Threat model, supply chain, secrets, incident response | `docs/security/` | Keep as an index with links per subtopic |
| Telemetry schemas, governance signals, audits | `docs/telemetry/` | Cross-link to `schemas/telemetry/` |
| Story Nodes and narrative research artifacts | `docs/reports/**/story_nodes/` | Evidence-led; no unsourced claims |

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React/Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
~~~

### Optional: sequence diagram (typical Focus Mode request)
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

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Existing docs and templates | Markdown | `docs/` | Template conformance + internal link sanity |
| Governance references | Markdown | `docs/governance/` | Paths resolve; no policy text duplicated here |
| Pipeline/system contracts | Markdown | `docs/MASTER_GUIDE_*.md` | Ensure ordering/invariants aren’t contradicted |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Documentation entry point | Markdown | `docs/README.md` | KFM Universal Doc template |

### Sensitivity & redaction
- This doc is **public/open** and must not include secrets, credentials, or sensitive location details.
- If you link to content that may describe sensitive sites, ensure that doc follows the sovereignty policy and any required generalization/redaction.

### Quality signals
- Links resolve (relative paths, no broken anchors).
- The docs map matches the canonical pipeline.
- New docs use exactly one governed template and keep front-matter consistent.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections involved: *(N/A for this README)*
- Items involved: *(N/A for this README)*
- Extension(s): *(N/A)*

### DCAT
- Dataset identifiers: *(N/A for this README)*
- License mapping: see repository-level licensing docs *(not confirmed in repo)*
- Contact / publisher mapping: *(not confirmed in repo)*

### PROV-O
- `prov:wasDerivedFrom`: *(N/A for this README)*
- `prov:wasGeneratedBy`: *(N/A for this README)*
- Activity / Agent identities: Use repo commit history and governed docs ownership conventions.

### Versioning
- Update `version` and `last_updated` when this navigation changes.
- For contract-impacting edits elsewhere, use the API Contract Extension template and track backward compatibility explicitly.
