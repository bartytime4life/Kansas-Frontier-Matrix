---
title: "KFM Research — README"
path: "docs/research/README.md"
version: "v1.0.0"
last_updated: "2025-12-20"
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

doc_uuid: "urn:kfm:doc:research:readme:v1.0.0"
semantic_document_id: "kfm-research-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:research:readme:v1.0.0"
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

# Research

## 📘 Overview

### Purpose
This directory is a **research workspace** for KFM: literature notes, design spikes, evaluation write-ups, and exploratory documentation that helps de-risk future work.

Research artifacts here are **not system contracts**. Anything that becomes normative (a standard, a schema, an API contract, a UI behavior, or a Story Node rule) must be promoted into the appropriate governed area (e.g., `docs/standards/`, `schemas/`, `docs/templates/`, subsystem docs, etc.).

### Scope

| In Scope | Out of Scope |
|---|---|
| Exploration notes (spikes), trade studies, prototypes (writeups), experiment summaries, literature reviews, benchmark notes | Authoritative policy, API contracts, schema definitions, release notes, production runbooks |
| Draft ideas that may later become tickets / governed docs | Raw datasets, derived datasets, and large binary artifacts (store under `data/` / `mcp/` per repo rules) |
| Risk registers + “unknowns list” for planned features | Anything requiring secrets, credentials, or sensitive location inference |

### Audience
- Primary: contributors doing discovery work (ETL/Catalog/Graph/API/UI/Story)
- Secondary: reviewers needing context for design decisions before they become governed contracts

### Definitions (link to glossary)
- Glossary: `docs/glossary.md` (create if missing)
- Terms used in this doc: research spike, trade study, evidence artifact, provenance, Story Node, Focus Mode

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide | `docs/MASTER_GUIDE_v12.md` | KFM | Canonical pipeline + invariants |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | KFM | Default governed doc template |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | KFM | For narrative artifacts with provenance |
| API contract template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | KFM | For REST/GraphQL contract changes |
| MCP area | `mcp/` | KFM | Experiments, SOPs, model cards (if present) |

### Definition of done (for this document)
- [ ] Front-matter complete + valid (`path` matches file location)
- [ ] Research vs. contract boundaries are explicit (what is exploratory vs. governed)
- [ ] Links to canonical templates and promotion paths are present
- [ ] No secrets, credentials, or PII are included
- [ ] Any sensitive content is generalized/redacted and flagged for review

## 🗂️ Directory Layout

### This document
- `path`: `docs/research/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Research (this area) | `docs/research/` | Exploratory docs: spikes, literature, evaluations |
| Data domains | `data/` | Raw/work/processed/stac outputs |
| Documentation | `docs/` | Canonical governed docs |
| Graph | `src/graph/` | Graph build + ontology bindings |
| Pipelines | `src/pipelines/` | ETL + catalogs + transforms |
| Schemas | `schemas/` | JSON schemas + telemetry schemas |
| Frontend | `web/` | React + map clients |
| MCP | `mcp/` | Experiments, model cards, SOPs |

### Expected file tree for this sub-area
~~~text
📁 docs/
└── 📁 research/
    ├── 📄 README.md
    ├── 📁 literature/              # Paper notes + citations (no full-text unless licensed)
    ├── 📁 spikes/                  # Short experiments/prototypes + findings
    ├── 📁 evaluations/             # Benchmarks, comparisons, QA notes
    ├── 📁 drafts/                  # In-progress writeups before promotion
    └── 📁 references/              # Indexes/bibliographies (avoid copying copyrighted texts)
~~~

## 🧭 Context

### Background
KFM is a geospatial + historical knowledge system built around a non-negotiable pipeline ordering:
ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode.

This research area exists to capture the exploratory work required to safely extend the system without breaking contracts, provenance requirements, or governance rules.

### Assumptions
- Research artifacts are allowed to be incomplete and exploratory.
- Any “decision” in research is provisional until moved into the appropriate governed doc/template.
- Research docs should still be written so they can be reviewed and reused.

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode ordering is preserved.
- Frontend consumes contracts via APIs (no direct graph dependency).
- Do not add derived datasets or catalog outputs to `src/`; keep them under `data/processed/` and `data/stac/` / `data/catalog/dcat/` / `data/prov/` as applicable.
- Do not include secrets/credentials; avoid PII; generalize sensitive locations per sovereignty rules.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Should research docs be linted with the same strictness as governed docs? | TBD | TBD |
| What is the canonical “promotion path” for research → subsystem doc → contract/template? | TBD | TBD |

### Future extensions
- Add per-domain research indexes (ETL, Catalog, Graph, API, UI, Story/Focus).
- Add a lightweight “promotion checklist” doc once a governance location is confirmed.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  R[Research notes & spikes] --> D[Governed docs / templates / tickets]
  D --> A[ETL]
  A --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> E[APIs]
  E --> F[React/Map UI]
  F --> G[Story Nodes]
  G --> H[Focus Mode]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant Research as Research Doc
  participant Ticket as Issue/Ticket
  participant GovDoc as Governed Doc/Template
  Research->>Ticket: Propose change + risks + evidence
  Ticket->>GovDoc: Promote to contract/standard
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Papers / references | citation + notes | `docs/research/literature/` | citation present; no large copyrighted copies |
| Spike results | markdown + small figures | `docs/research/spikes/` | reproducibility notes; parameters captured |
| Proposed contracts | markdown | promote to `docs/templates/` or `docs/` | template compliance + review |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Research notes | Markdown | `docs/research/**` | Markdown protocol + repo lint |
| Candidate requirements | Markdown | promote to `docs/` | Universal template (governed) |
| Contract proposals | Markdown | promote to `docs/` | API/Story templates as applicable |

### Sensitivity & redaction
- If a research note includes potentially sensitive locations or cultural content, generalize geometry/coordinates and flag for governance review.
- Do not include personal identifiers or private communications in public docs.

### Quality signals
- Clear question statement + assumptions
- Reproducible steps (commands, params, versions) where applicable
- Evidence links (datasets, STAC item IDs, PROV run IDs) where applicable
- Explicit labeling of fact vs. inference vs. hypothesis

## 🌐 STAC, DCAT & PROV Alignment

### STAC
If research work produces a **new geospatial evidence artifact** intended for discovery or UI use, it must be recorded as a STAC Item/Collection in the canonical catalog locations before it is treated as a system artifact.

### DCAT
If research work produces a **new dataset view** intended for publication/consumption, it must have a DCAT mapping (title/description/license/keywords at minimum).

### PROV-O
If research work produces a **derived artifact** (transformed data, model output, evidence panel), capture lineage:
- `prov:wasDerivedFrom`: source IDs
- `prov:wasGeneratedBy`: pipeline activity/run ID
- Agent / activity identities where applicable

### Versioning
- Prefer stable identifiers for promoted artifacts.
- Link predecessor/successor for catalog items when versioning is introduced.

## 🧱 Architecture

### Components
This research area is not a runtime component; it is documentation that informs:
- subsystem documentation (`docs/pipelines/`, `docs/graph/`, `docs/design/`, etc.)
- templates and contracts (`docs/templates/`)
- implementation work (`src/`, `web/`, `schemas/`, `data/`)

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Universal governed docs | `docs/` | Semver + changelog where applicable |
| JSON schemas | `schemas/` | Semver + schema validation required |
| API contracts | `docs/` + `src/server/` | backward compat or version bump |
| Story Nodes | `docs/reports/.../story_nodes/` | provenance required; version history |

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
Research notes do not surface directly in Focus Mode.

To surface narrative content:
- promote to Story Nodes using `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- ensure each claim is provenance-linked (dataset/document IDs)
- ensure sensitivity/generalization rules are followed

### Provenance-linked narrative rule
- Every claim that ships to UI/Focus Mode must trace to a dataset / record / asset ID.

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
- [ ] No secrets/credentials/PII included
- [ ] If any artifacts are promoted: schema validation (STAC/DCAT/PROV) + contract tests

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) run doc lint
# 2) validate schemas (if referenced)
# 3) run tests (if any code changes are involved)
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| TBD | TBD | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates
- Research docs: peer review encouraged
- Promotion to governed contracts/templates: required review (per governance refs)
- Any sensitive content: sovereignty/ethics review required

### CARE / sovereignty considerations
- Identify impacted communities and protection rules before publishing sensitive details.

### AI usage constraints
- Ensure AI permissions/prohibitions match intended use.
- Do not imply prohibited AI actions (e.g., inferring sensitive locations).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-20 | Initial research README scaffold | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

