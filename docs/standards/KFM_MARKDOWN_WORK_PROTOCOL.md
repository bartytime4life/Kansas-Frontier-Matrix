---
title: "KFM Markdown Work Protocol"
path: "docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md"
version: "v1.0.0-draft"
last_updated: "2025-12-19"
status: "draft"
doc_kind: "Standard"
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

doc_uuid: "urn:kfm:doc:standards:markdown-work-protocol:v1.0.0-draft"
semantic_document_id: "kfm-standards-markdown-work-protocol-v1.0.0-draft"
event_source_id: "ledger:kfm:doc:standards:markdown-work-protocol:v1.0.0-draft"
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

# KFM Markdown Work Protocol

## 📘 Overview

### Purpose
This standard defines the **mandatory** workflow and constraints for producing Markdown documentation in the Kansas Frontier Matrix (KFM) repository. It exists to ensure that documentation is:

- **Template-first** (every doc conforms to exactly one governed template)
- **Architecture-synced** with the canonical pipeline
- **Repo-grounded** (no invented facts/policies; label uncertainty)
- **CI-clean** (assume strict lint/schema/link/sensitivity checks)
- **API-boundary compliant** (UI never reads the graph directly)

### Scope

| In Scope | Out of Scope |
|---|---|
| Any Markdown authored under `docs/` (standards, guides, design docs, reports, story nodes) | Implementing code changes in `src/`, schema changes in `schemas/`, or pipeline runs |
| Template-driven docs (`docs/templates/…`) | Making claims about executed ETL runs, infra changes, or deployed behavior without evidence |
| API contract documentation (REST/GraphQL) | Introducing new governance/policy beyond what is defined in governed docs |

### Audience
- Primary: KFM contributors authoring or updating Markdown documentation.
- Secondary: reviewers, maintainers, and anyone producing LLM-assisted drafts for KFM.

### Definitions
- **Governed document**: a Markdown doc with YAML front-matter and explicit scope, constraints, and validation steps.
- **Template-first**: every deliverable conforms to *exactly one* governed template (Universal, Story Node, or API Contract Extension).
- **Architecture-synced**: documentation preserves the canonical pipeline ordering and API boundary.
- **Repo-grounded**: no invented facts about the repo/system; if uncertain, explicitly label as “not confirmed in repo” and propose the safest next step.

> Glossary link (expected): `docs/glossary.md` (create if absent).

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide (canonical pipeline + invariants) | `docs/MASTER_GUIDE_v12.md` | Maintainers | Source of truth for ordering + extension points |
| Universal governed doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Maintainers | Default for most docs |
| Story node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Maintainers | Required for Focus Mode narratives |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | Maintainers | Required for endpoint/contract changes |
| This protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | Maintainers | Governs Markdown contributions |

### Definition of done
- [ ] Correct template selected and applied
- [ ] Pipeline ordering and API boundary preserved
- [ ] File placed in correct repo area (data vs docs vs src vs schemas)
- [ ] Claims are sourced to datasets/doc IDs (or marked inference/hypothesis)
- [ ] Validation steps listed and repeatable
- [ ] No secrets, credentials, or sensitive location inference included
- [ ] CI gates considered (lint/schema/link/sensitivity/a11y where applicable)

## 🗂️ Directory Layout

### This document
- `path`: `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Documentation | `docs/` | Canonical governed docs |
| Standards | `docs/standards/` | Normative rules + conventions |
| Templates | `docs/templates/` | Governed templates (Universal / Story / API) |
| Data lifecycle | `data/raw/` → `data/work/` → `data/processed/` | Staged datasets |
| Catalog outputs | `data/stac/` · `data/catalog/dcat/` · `data/prov/` | STAC/DCAT/PROV outputs |
| Graph | `src/graph/` | Ontology bindings, graph build, migrations |
| APIs | `src/server/` (or repo equivalent) | Contracted access layer |
| UI | `web/` | React + Map clients |

### Expected file tree for this sub-area
~~~text
📁 docs/
├── 📁 standards/
│   ├── 📄 README.md
│   └── 📄 KFM_MARKDOWN_WORK_PROTOCOL.md
├── 📁 templates/
│   ├── 📄 TEMPLATE__KFM_UNIVERSAL_DOC.md
│   ├── 📄 TEMPLATE__STORY_NODE_V3.md
│   └── 📄 TEMPLATE__API_CONTRACT_EXTENSION.md
└── 📄 MASTER_GUIDE_v12.md
~~~

## 🧭 Context

### Background
KFM documentation acts as **system contracts**: it constrains how data, metadata, graph semantics, APIs, UI, and story narratives evolve together. As the project scales (more domains, more evidence products, more narrative UX), doc drift becomes a failure mode; this protocol prevents drift by enforcing:

- a single canonical pipeline ordering
- strong provenance expectations
- standard templates with stable metadata front-matter

### Assumptions
- Documentation is reviewed like code: diffs matter, contracts matter, provenance matters.
- Standards and templates are the *allowed* place to define cross-cutting rules.
- Some “expected” referenced docs (governance, glossary) may require creation in the repo if missing.

### Constraints / invariants
- **Canonical pipeline is preserved**: ETL → STAC/DCAT/PROV → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode.
- **API boundary**: Frontend consumes contracts via APIs; it must not query Neo4j directly.
- **No invented repo facts**: if not verifiable, mark as **not confirmed in repo** and propose the safest next step.
- **No claims of actions not performed**: do not state that code was executed, infra changed, commits pushed, or emails sent.

### Required authoring workflow
When producing Markdown work for KFM, the author (human or tool-assisted) must:

1. **Select exactly one template**:
   - Story Node / Focus Mode narrative → `docs/templates/TEMPLATE__STORY_NODE_V3.md`
   - API/endpoint/contract change → `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
   - Everything else → `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
2. **Declare impacted pipeline stage(s)** (ETL / Catalog / Graph / AI / API / UI / Story).
3. **List file paths** to create/modify (and ensure correct placement).
4. **Provide commit-ready Markdown** that adheres to the selected template.
5. **Put notes/assumptions/next steps outside** the commit-ready content.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Do we enforce link integrity checks for intra-repo links in CI? | TBD | TBD |
| Where is the canonical glossary (`docs/glossary.md`) located? | TBD | TBD |
| What is the canonical doc linter command (if any)? | TBD | TBD |

### Future extensions
- Add a “Doc lint + link check” CI job description under `docs/standards/` (requires human review).
- Add a “Citations + evidence” mini-standard for Story Nodes (if Focus Mode expands).

## 🗺️ Diagrams

### System and documentation alignment
~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React/Map UI]
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
| Templates | Markdown | `docs/templates/` | Front-matter keys preserved |
| Evidence refs | IDs/paths | STAC/DCAT/PROV + docs | Links resolve (if link-check enabled) |
| Repo constraints | Standards docs | `docs/standards/` | Reviewer validation |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Governed docs | Markdown | `docs/**` | Must match selected template |
| Story nodes | Markdown | `docs/reports/.../story_nodes/` | Must cite dataset/document IDs |
| API contract docs | Markdown | `docs/**` | Must include contract + tests list |

### Sensitivity and redaction
- Do not include secrets, credentials, tokens, keys, private URLs, or personal data.
- If content could identify a restricted/sensitive location, **generalize** it (region-level) and reference sovereignty rules.

### Quality signals
- Completeness: template sections filled or explicitly marked “N/A”.
- Traceability: dataset/document IDs provided for factual claims.
- Consistency: pipeline ordering and API boundary reiterated when relevant.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- When a doc references a geospatial/temporal asset, include:
  - STAC Collection ID(s)
  - STAC Item ID(s)
  - Path(s) under `data/stac/collections/` and `data/stac/items/`
- Avoid “floating assets” (assets described in prose with no STAC representation).

### DCAT
- When a doc describes a dataset, include:
  - DCAT dataset identifier
  - License mapping
  - Spatial/temporal coverage where relevant
  - Path under `data/catalog/dcat/`

### PROV-O
- When a doc describes how an artifact was produced, include:
  - `prov:wasDerivedFrom` (source IDs)
  - `prov:wasGeneratedBy` (activity/run ID)
  - Path under `data/prov/`

### Narrative evidence rule
- Story Nodes and Focus Mode narratives must link every factual claim to an evidence identifier (STAC item, Document ID, dataset record ID, etc.).

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize | Config + run logs |
| Catalogs | STAC/DCAT/PROV | JSON/JSON-LD + validators |
| Graph | Neo4j | Cypher behind API boundary |
| APIs | Serve contracts | REST/GraphQL |
| UI | Map + narrative | API calls only |
| Story Nodes | Curated narrative | Docs + graph linkage |
| Focus Mode | Contextual synthesis | Provenance-linked bundle |

### Interfaces and contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Templates | `docs/templates/` | Semver; changes require review |
| Standards | `docs/standards/` | Semver; changes require governance review when affecting security/sensitivity |
| API schemas | `src/server/` + docs | Backward compatible or version bump + tests |

### Repo placement rules
- Prefer standard locations:
  - `data/`, `src/`, `docs/`, `mcp/`, `schemas/`, `tests/`, `tools/`, `.github/`, `web/`
- Derived datasets → `data/processed/` (not `src/`)
- Catalog outputs:
  - STAC → `data/stac/...`
  - DCAT → `data/catalog/dcat/`
  - PROV → `data/prov/`
- Run logs and experiment artifacts → `mcp/runs/` or `mcp/experiments/`

### Front-matter and fencing rules
- Keep the selected template’s YAML front-matter keys intact.
- Do not add new YAML fields without governance review.
- Update only appropriate fields (`version`, `last_updated`, `status`).
- `commit_sha` stays as placeholder unless a commit hash is provided.
- In documentation content:
  - Use `~~~` fences for code blocks and diagrams.
  - Reserve triple backticks for chat wrappers only (outside repo files).

## 🧠 Story Node and Focus Mode Integration

### How docs surface in Focus Mode
- Focus Mode must only show provenance-linked narratives.
- Predictive or model-derived content must be:
  - opt-in
  - labeled as prediction
  - accompanied by uncertainty/confidence metadata
  - linked to provenance artifacts

### Optional structured controls
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (template compliance, front-matter validity)
- [ ] Schema validation (STAC/DCAT/PROV where referenced)
- [ ] Graph integrity checks (if doc implies graph changes)
- [ ] API contract tests (if doc changes API behavior)
- [ ] UI checks (if doc changes layer registry or UX contracts)
- [ ] Security + sovereignty checks (sensitive content rules)

### Reproduction
~~~bash
# Placeholder — replace with repo-specific commands:
# 1) markdown lint / link checks
# 2) schema validation (STAC/DCAT/PROV)
# 3) unit + integration tests
~~~

### Telemetry signals
| Signal | Source | Where recorded |
|---|---|---|
| Doc compliance rate | CI | `docs/telemetry/` + `schemas/telemetry/` |
| Broken links | CI | `docs/telemetry/` |
| Sensitivity violations | Review/CI | `docs/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates
- Changes affecting security, sovereignty, or public exposure: **requires human review**
- New sensitive layers or redaction rules: **requires governance review**
- New public-facing endpoints: **requires API + security review**

### CARE and sovereignty considerations
- Treat culturally sensitive and Indigenous content as potentially restricted.
- Do not infer sensitive locations; follow sovereignty policy and redaction requirements.

### AI usage constraints
- Allowed transformations: summarize, structure extraction, translation, keyword indexing.
- Prohibited: generating new policy in-place, inferring sensitive locations, fabricating sources.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0-draft | 2025-12-19 | Initial Markdown work protocol standard | TBD |

