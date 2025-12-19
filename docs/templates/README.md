---
title: "Templates — README"
path: "docs/templates/README.md"
version: "v1.0.0"
last_updated: "2025-12-19"
status: "active"
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

doc_uuid: "urn:kfm:doc:templates:readme:v1.0.0"
semantic_document_id: "kfm-templates-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:templates:readme:v1.0.0"
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

# Templates — README

## 📘 Overview

### Purpose
This directory contains **governed Markdown templates** for Kansas Frontier Matrix (KFM) documentation.
Use these templates to keep docs consistent with KFM’s canonical pipeline, provenance expectations, and API/UI boundaries.

### Scope

| In Scope | Out of Scope |
|---|---|
| Selecting the correct template | Authoring subsystem content (domain-specific details) |
| How to instantiate + validate a governed doc | Implementing ETL/Graph/API/UI code |
| Template inventory + intended usage | Non-governed scratch notes |

### Audience
- Primary: Contributors authoring or updating docs under `docs/`
- Secondary: Reviewers validating doc compliance and architecture alignment

### Definitions
- Glossary (expected): `docs/glossary.md` (**not confirmed in repo**)
- Canonical pipeline ordering (source of truth): `docs/MASTER_GUIDE_v12.md`

### Key artifacts (what this folder points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide (canonical pipeline + invariants) | `docs/MASTER_GUIDE_v12.md` | Maintainers | Pipeline ordering + extension matrix |
| Universal governed doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Maintainers | Default for most docs |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Maintainers | Focus Mode / narrative nodes |
| API Contract Extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | Maintainers | REST/GraphQL contract changes |

### Definition of done (for this document)
- [ ] Front-matter keys present and valid (no unapproved keys added)
- [ ] Template inventory matches `docs/templates/`
- [ ] Template selection guidance is clear and architecture-synced
- [ ] Validation checklist is included and repeatable (commands may be placeholders if repo tooling is not confirmed)

## 🗂️ Directory Layout

### This document
- `path`: `docs/templates/README.md`

### Expected file tree for this sub-area
~~~text
📁 docs/
├── 📁 templates/
│   ├── 📄 README.md
│   ├── 📄 TEMPLATE__KFM_UNIVERSAL_DOC.md
│   ├── 📄 TEMPLATE__STORY_NODE_V3.md
│   └── 📄 TEMPLATE__API_CONTRACT_EXTENSION.md
└── 📄 MASTER_GUIDE_v12.md
~~~

## 🧭 Context

### Why templates exist
KFM documentation is part of the system’s “contract surface”:
- It preserves the **canonical pipeline ordering** and keeps extensions consistent.
- It enforces **governed metadata** (front-matter + provenance expectations).
- It reduces drift between data, catalogs, graph semantics, APIs, UI, and narratives.

### Constraints / invariants (do not break)
- Canonical pipeline ordering is preserved: **ETL → STAC/DCAT/PROV → Neo4j → APIs → React/Map UI → Story Nodes → Focus Mode**.
- Frontend consumes data through **API contracts** (no direct graph reads).
- Narrative outputs must remain **evidence-linked** (no unsourced claims inside Story/Focus contexts).

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Where is the canonical glossary (`docs/glossary.md`)? | TBD | TBD |
| What is the repo’s exact doc-lint command? | TBD | TBD |

### Future extensions
- Add additional governed templates if new doc types become common (e.g., ontology extension, catalog mapping guide). (**not confirmed in repo**)

## 🧭 Template selection

Use **exactly one** governed template per deliverable:

| If you are creating… | Use this template | Output location (typical) |
|---|---|---|
| Any general documentation, guides, standards, design notes | `TEMPLATE__KFM_UNIVERSAL_DOC.md` | `docs/<area>/...` |
| Story node / Focus Mode narrative artifact | `TEMPLATE__STORY_NODE_V3.md` | `docs/reports/.../story_nodes/...` |
| API contract addition/change (REST/GraphQL) | `TEMPLATE__API_CONTRACT_EXTENSION.md` | `docs/api/...` (or equivalent) |

## 🧩 How to use a template

### Minimal workflow
1. Copy the correct template into its target location.
2. Update YAML front-matter:
   - `title`, `path`, `version`, `last_updated`, `status`
   - `doc_uuid`, `semantic_document_id`, `event_source_id`
   - Keep **all front-matter keys** intact; do not add new keys without governance review.
3. Fill in sections with repo-grounded references:
   - Link to schemas, dataset IDs, catalog IDs, run IDs, and API contracts where applicable.
4. Compute and fill `doc_integrity_checksum` (sha256) as required by your tooling. (**command not confirmed in repo**)
5. Run the repo’s doc validation gates (see checklist below).

### Notes for Story Nodes
When using the Story Node template:
- Keep tone neutral and evidence-led.
- Every factual claim must map to a cited dataset/document ID.
- Include any required Focus Mode controls only if they are supported by the UI.

### Notes for API contracts
When using the API Contract Extension template:
- Define data sensitivity and redaction behavior.
- Include contract tests (OpenAPI / GraphQL) and describe backwards compatibility expectations.

## 🗺️ Diagrams

### Template-to-pipeline alignment
~~~mermaid
flowchart LR
  A[Doc need identified] --> B{Select template}
  B -->|General doc| C[TEMPLATE__KFM_UNIVERSAL_DOC.md]
  B -->|Story/Focus| D[TEMPLATE__STORY_NODE_V3.md]
  B -->|API change| E[TEMPLATE__API_CONTRACT_EXTENSION.md]
  C --> F[Validate + review]
  D --> F
  E --> F
  F --> G[Commit to repo]
~~~

## 🧪 Validation & CI/CD

### Validation checklist (minimum expectations)
- [ ] Markdown protocol checks (front-matter + fencing conventions)
- [ ] Schema validation for any referenced STAC/DCAT/PROV artifacts (if applicable)
- [ ] Graph integrity checks (if doc implies new labels/relations)
- [ ] API contract tests (if doc modifies/extends API)
- [ ] UI layer registry schema checks (if doc modifies layers)
- [ ] Security + sovereignty review triggers evaluated (if applicable)

### Reproduction
~~~bash
# Repo-specific commands are not confirmed in repo.
# Replace with actual doc lint / schema validation / test commands once defined.
~~~

## ⚖ FAIR+CARE & Governance

### Review gates
- Template changes should be treated as governance-impacting changes.
- New sensitive content requires sovereignty/redaction rules and reviewer sign-off.

### AI usage constraints
- AI transforms should follow the front-matter permissions/prohibitions.
- Prohibited: generating new policy text or inferring sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial templates README | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`