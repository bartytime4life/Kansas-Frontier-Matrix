---
title: "Docs — Kansas Frontier Matrix Documentation Index"
path: "docs/README.md"
version: "v1.0.0"
last_updated: "2025-12-22"
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

# Docs — Kansas Frontier Matrix Documentation Index

## 📘 Overview

### Purpose

- Provide a single entry point for navigating `docs/` (the canonical governed documentation area).
- Point contributors to the correct templates/standards before adding or changing documentation.
- Keep documentation **architecture-synced** with the system pipeline:
  **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.

### Scope

| In Scope | Out of Scope |
|---|---|
| Where documentation lives and how it is organized | Full implementation details of pipelines, services, or UI |
| Which templates to use for docs (Universal, Story Node, API Contract) | Debugging runtime failures / operations runbooks |
| Docs-to-data linkage expectations (STAC/DCAT/PROV identifiers, provenance references) | Replacing the Master Guide or templates |

### Audience

- Primary: contributors authoring/maintaining documentation in `docs/`
- Secondary: engineers and reviewers working in ETL, catalogs, graph, API, UI, and story layers

### Definitions

- Link: `docs/glossary.md` (not confirmed in repo)
- Terms commonly used in docs:
  - STAC, DCAT, PROV
  - Neo4j graph
  - Story Nodes
  - Focus Mode
  - Contract tests (API/UI)

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide | `docs/MASTER_GUIDE_v12.md` | TBD | System + pipeline source of truth |
| Universal Doc Template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | TBD | Default governed doc template |
| Story Node Template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | TBD | For narratives + Focus Mode surfacing |
| API Contract Extension Template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | TBD | For REST/GraphQL contract changes |
| Markdown work protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | TBD | not confirmed in repo |
| Governance root | `docs/governance/ROOT_GOVERNANCE.md` | TBD | required reference for governed docs |
| Ethics policy | `docs/governance/ETHICS.md` | TBD | required reference for governed docs |
| Sovereignty policy | `docs/governance/SOVEREIGNTY.md` | TBD | required reference for governed docs |

### Definition of done

- [ ] Front-matter complete + valid, and `path:` matches file location
- [ ] Links resolve (no broken internal references)
- [ ] Any “system rule” stated here is also reflected in the Master Guide (or is explicitly marked as *not confirmed in repo*)
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated when relevant

## 🗂️ Directory Layout

### This document

- `path`: `docs/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed + catalog outputs |
| Documentation | `docs/` | Canonical governed docs |
| Pipelines | `src/pipelines/` | ETL + catalog generation code |
| Catalog | `src/catalog/` | Catalog tooling (STAC/DCAT/PROV) |
| Graph | `src/graph/` | Ontology bindings + graph build |
| API | `src/api/` | API layer (contracts live here) |
| UI | `web/` | React + map clients, layer registry |
| Schemas | `schemas/` | JSON schemas, telemetry schemas |
| Tests | `tests/` | Unit + integration tests |
| Tools | `tools/` | CLI utilities, validators |
| MCP | `mcp/` | Experiments, runs, model cards, SOPs |
| CI | `.github/` | Workflows, CI gates |
| Releases | `releases/` | Versioned packaged artifacts |

### Expected file tree for this sub-area

~~~text
📁 docs/
├── 📄 README.md
├── 📄 MASTER_GUIDE_v12.md
├── 📁 templates/
│   ├── 📄 TEMPLATE__KFM_UNIVERSAL_DOC.md
│   ├── 📄 TEMPLATE__STORY_NODE_V3.md
│   └── 📄 TEMPLATE__API_CONTRACT_EXTENSION.md
├── 📁 standards/
│   └── 📄 KFM_MARKDOWN_WORK_PROTOCOL.md
├── 📁 governance/
│   ├── 📄 ROOT_GOVERNANCE.md
│   ├── 📄 ETHICS.md
│   └── 📄 SOVEREIGNTY.md
├── 📁 architecture/
│   └── 📄 KFM_1_0_SYSTEM_DOCUMENTATION.pdf
├── 📁 data/
│   └── 📄 <domain documentation lives here>
├── 📁 pipelines/
│   └── 📄 <etl + catalog documentation lives here>
├── 📁 graph/
│   └── 📄 <ontology + entity/edge documentation lives here>
├── 📁 api/
│   └── 📄 <API contracts + contract notes live here>
├── 📁 web/
│   └── 📄 <UI docs: Map/Layer registry/a11y/audit>
├── 📁 reports/
│   └── 📁 story_nodes/
│       └── 📄 <story node docs live here>
├── 📁 telemetry/
│   └── 📄 <signals + instrumentation docs>
└── 📁 security/
    └── 📄 <redaction + threat model docs>
~~~

## 🧭 Context

### Background

KFM documentation is not just narrative: it defines and preserves the system’s contracts and invariants across ETL, catalogs, graph, API, UI, and story layers.

### Assumptions

- The paths listed above are **canonical targets** as described in KFM governing materials.
- If a referenced path/document is missing, treat it as **not confirmed in repo** and add it (or update this README and link the correct location).

### Constraints / invariants

- The pipeline order is preserved:
  **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- The UI must consume data through the **API layer** (no direct graph dependency).
- Documentation must not introduce “free-floating facts” that cannot be traced back to governed artifacts or identifiers.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Which `docs/*` subdirectories are present today vs. planned? | TBD | TBD |
| Where is the glossary located (or should it be created)? | TBD | TBD |
| What is the repo’s canonical API schema format (OpenAPI, GraphQL, both)? | TBD | TBD |

### Future extensions

- Add a docs index per major area (data, graph, API, web, story nodes).
- Add a “docs health check” script to validate internal links and required front matter.

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

### Optional: sequence diagram

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

### Data lifecycle

- `data/raw/` → `data/work/` → `data/processed/` → `data/stac/`
- Use `data/reports/` outputs as needed (project-specific).

### Domain expansion pattern

- New domains go under `data/<domain>/...`.
- New domain docs go under `docs/<domain>/...` or `docs/data/<domain>/...` (choose one canonical location and link).

## 🌐 STAC, DCAT & PROV Alignment

### Alignment policy

- Every new dataset must have:
  - STAC Collection + Item(s)
  - DCAT mapping (minimum title/description/license/keywords)
  - PROV activity for the transform that generated it

### Versioning expectations

- New versions should link predecessor/successor relationships.
- Graph should mirror version lineage.

## 🧱 Architecture

### Subsystem contracts

| Subsystem | Contract artifacts | “Do not break” rule |
|---|---|---|
| ETL | configs + run logs + validation | deterministic, replayable |
| Catalogs | STAC/DCAT/PROV schemas + validators | machine-validated |
| Graph | ontology + migrations + constraints | stable labels/edges |
| APIs | OpenAPI/GraphQL schema + tests | backward compat or version bump |
| UI | layer registry + a11y + audit affordances | no hidden data leakage |
| Focus Mode | provenance-linked context bundle | no hallucinated sources |

### Extension points checklist

- [ ] Data: new domain added under `data/<domain>/...`
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + access rules
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

## 🧠 Story Node & Focus Mode Integration

### Story Nodes as machine-ingestible storytelling

- Story Nodes must carry provenance annotations and connect to graph entities.

### Focus Mode rule

- Focus Mode only consumes provenance-linked content.
- Any predictive content must be opt-in and carry uncertainty / confidence metadata.

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

### Telemetry signals

| Signal | Source | Where recorded |
|---|---|---|
| TBD | TBD | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Governance review triggers

- New sensitive layers
- New AI narrative behaviors
- New external data sources
- New public-facing endpoints

### Sovereignty safety

- Document redaction/generalization rules for any restricted locations.

### AI usage constraints

- Ensure the doc’s AI permissions/prohibitions match intended use.
- Do not infer or generate sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial `docs/` README index | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
