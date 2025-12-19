---
title: "Kansas Frontier Matrix — Documentation Hub"
path: "docs/README.md"
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

# Kansas Frontier Matrix Documentation Hub

## 📘 Overview

### Purpose
This directory contains the governed documentation that defines the Kansas Frontier Matrix (KFM) system’s
pipeline ordering, standards, contracts, and narrative conventions. Use this README as the entry point for
finding canonical “source of truth” docs (guides, templates, governance).

### Scope

| In Scope | Out of Scope |
|---|---|
| Canonical guides, templates, standards, governance refs | Implementation details best expressed in code |
| Subsystem documentation (ETL, catalogs, graph, APIs, UI) | Generated artifacts and derived datasets (live under `data/`) |
| Story Node narratives and Focus Mode narrative docs | Non-governed notes and informal drafts without front-matter |

### Audience
- Primary: Contributors writing or updating governed Markdown docs.
- Secondary: Reviewers validating governance, provenance, and contract alignment.

### Definitions
- Glossary link: `docs/glossary.md` (create if missing)
- Terms used here: ETL, STAC, DCAT, PROV-O, Graph, Story Node, Focus Mode.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide | `docs/MASTER_GUIDE_v12.md` | TBD | Canonical pipeline ordering + invariants |
| Templates | `docs/templates/` | TBD | Governed doc formats for repo-wide consistency |
| Governance root | `docs/governance/ROOT_GOVERNANCE.md` | TBD | Approval gates + policy references |
| Ethics | `docs/governance/ETHICS.md` | TBD | Ethics constraints for data and AI usage |
| Sovereignty | `docs/governance/SOVEREIGNTY.md` | TBD | CARE + sensitive-location handling rules |

### Definition of done
- [ ] Front-matter complete + valid (path matches file location)
- [ ] Document is mapped to exactly one governed template
- [ ] Key claims link to governed artifacts (datasets/schemas/docs/tickets as applicable)
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `docs/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed data + catalog outputs |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | STAC/DCAT/PROV artifacts |
| Documentation | `docs/` | Canonical governed docs (this area) |
| Graph | `src/graph/` + `docs/graph/` | Ontology, labels/relations, migrations, graph build docs |
| Pipelines | `src/pipelines/` + `docs/pipelines/` | ETL + transforms + catalog build docs |
| APIs | `src/server/` + `docs/` | Contracted access layer docs (REST/GraphQL) |
| Frontend | `web/` + `docs/design/` | UI design, a11y, layer registry docs |
| Story Nodes | `docs/reports/.../story_nodes/` | Provenance-linked narrative artifacts |
| Telemetry | `docs/telemetry/` + `schemas/telemetry/` | Observability + governance signals |
| MCP | `mcp/` + `docs/templates/` | Experiments, model cards, SOPs, doc templates |

### Expected file tree for this sub-area
~~~text
📁 docs/
├── 📄 README.md
├── 📄 MASTER_GUIDE_v12.md
├── 📄 MASTER_GUIDE_v11.md
├── 📁 templates/
│   ├── 📄 TEMPLATE__KFM_UNIVERSAL_DOC.md
│   ├── 📄 TEMPLATE__STORY_NODE_V3.md
│   └── 📄 TEMPLATE__API_CONTRACT_EXTENSION.md
├── 📁 governance/
│   ├── 📄 ROOT_GOVERNANCE.md
│   ├── 📄 ETHICS.md
│   └── 📄 SOVEREIGNTY.md
├── 📁 standards/
│   └── 📄 <governed-standards-live-here>
├── 📁 data/
│   └── 📄 <catalog-mapping-docs-live-here>
├── 📁 graph/
│   └── 📄 <graph-docs-live-here>
├── 📁 pipelines/
│   └── 📄 <pipeline-docs-live-here>
├── 📁 design/
│   └── 📄 <ui-docs-live-here>
├── 📁 reports/
│   └── 📁 <run-or-release>/
│       └── 📁 story_nodes/
│           └── 📄 <story-node>.md
├── 📁 telemetry/
│   └── 📄 <telemetry-docs-live-here>
└── 📁 security/
    └── 📄 <security-docs-live-here>
~~~

## 🧭 Context

### Background
KFM is a geospatial + historical knowledge system intended to support exploration of Kansas across time
and space using governed data, provenance, and narrative UX. The system’s canonical flow is:

ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode.

### Assumptions
- `docs/MASTER_GUIDE_v12.md` is the canonical pipeline and documentation map.
- Governance references in front-matter resolve within the repo.
- All new governed docs use one template from `docs/templates/`.

### Constraints and invariants
- Canonical ordering is preserved: ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode.
- Frontend consumes contracts via APIs (no direct graph dependency).
- Focus Mode only consumes provenance-linked content.
- Deterministic, replayable pipeline outputs are the baseline expectation.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Does `docs/glossary.md` exist? If not, add it. | TBD | TBD |
| What is the canonical location for API docs under `docs/`? | TBD | TBD |
| Should `docs/README.md` be treated as “active” once reviewed? | TBD | TBD |

### Future extensions
- Add a “Docs Index” page that links to each subsystem’s canonical doc entrypoint.
- Add a “Docs CI” page describing markdown lint + front-matter validation gates.

## 🗺️ Diagrams

### System and dataflow diagram
~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React and Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
~~~

### Optional sequence diagram
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
| Governed documentation edits | Markdown | Contributors | Markdown protocol + front-matter checks |
| Governance references | Markdown | `docs/governance/` | Link integrity checks |
| Templates | Markdown | `docs/templates/` | Template-front-matter lint |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Governed docs | Markdown | `docs/...` | KFM-MDP front-matter + template conformance |
| Narrative artifacts | Markdown | `docs/reports/.../story_nodes/` | Story Node v3 template |

### Sensitivity and redaction
- Public docs must not disclose sensitive locations or restricted data access details.
- When documenting sensitive data handling, describe generalization/redaction behavior at a high level and
reference governance docs for specifics.

### Quality signals
- Link integrity (no broken internal references).
- Template conformance (front-matter keys and required sections present).
- No un-sourced narrative claims in Focus Mode documents.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Catalog outputs: `data/stac/` (collections + items)
- Mapping documentation: `docs/data/` (expected)

### DCAT
- Dataset catalog outputs: `data/catalog/dcat/`
- Dataset identifiers should match DCAT records where applicable.

### PROV-O
- Lineage outputs: `data/prov/`
- Story Nodes should reference `prov:wasDerivedFrom` and `prov:wasGeneratedBy` identifiers where available.

### Versioning
- Use consistent semantic versioning in doc front-matter and keep predecessor/successor links in the
catalog/graph layer (when applicable to datasets).

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize | Config + run logs |
| Catalogs | STAC/DCAT/PROV | JSON/JSON-LD + validator |
| Graph | Neo4j | Cypher via API layer |
| APIs | Serve contracts | REST/GraphQL |
| UI | Map + narrative | API calls |
| Story Nodes | Curated narrative | Docs + graph linkage |
| Focus Mode | Contextual synthesis | Provenance-linked bundles |

### Interfaces and contracts

| Contract | Location | Versioning rule |
|---|---|---|
| Document templates | `docs/templates/` | Semver + version history |
| Catalog schemas | `schemas/` + `data/stac/` | Schema validation required |
| API contracts | `src/server/` + `docs/` | Contract tests required |
| UI registries | `web/` + `docs/design/` | Schema-validated registries |

## 🧠 Story Node & Focus Mode Integration

### How documentation work surfaces in Focus Mode
- Story Nodes are machine-ingestible narrative artifacts that connect to catalog items and graph entities.
- Focus Mode must render citations and provenance references for all factual claims.

### Provenance-linked narrative rule
- Every factual claim must trace to a dataset, record, or asset ID.

### Optional structured controls
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (front-matter keys, path match)
- [ ] Link integrity checks (internal paths)
- [ ] Schema validation (STAC/DCAT/PROV where referenced)
- [ ] Graph integrity checks (for docs that reference graph entities)
- [ ] API contract tests (for docs that define or change contracts)
- [ ] Security and sovereignty checks (for sensitive topics)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands:
# 1) markdown lint
# 2) link checker
# 3) schema validation (stac/dcat/prov)
# 4) unit/integration tests
~~~

### Telemetry signals
| Signal | Source | Where recorded |
|---|---|---|
| Doc lint pass/fail | CI | `docs/telemetry/` (expected) |
| Broken links | CI | `docs/telemetry/` (expected) |

## ⚖ FAIR+CARE & Governance

### Review gates
- Follow `docs/governance/ROOT_GOVERNANCE.md` for what requires council/board sign-off.

### CARE and sovereignty considerations
- Do not infer or disclose sensitive locations.
- Apply redaction/generalization rules per `docs/governance/SOVEREIGNTY.md`.

### AI usage constraints
- AI transforms must respect the permissions/prohibitions declared in front-matter.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial docs hub README | TBD |