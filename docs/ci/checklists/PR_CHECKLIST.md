---
title: "CI — Pull Request Checklist"
path: "docs/ci/checklists/PR_CHECKLIST.md"
version: "v1.0.0"
last_updated: "2025-12-19"
status: "draft"
doc_kind: "Checklist"
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

doc_uuid: "urn:kfm:doc:ci:checklists:pr-checklist:v1.0.0"
semantic_document_id: "kfm-ci-checklists-pr-checklist-v1.0.0"
event_source_id: "ledger:kfm:doc:ci:checklists:pr-checklist:v1.0.0"
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

# CI — Pull Request Checklist

## 📘 Overview

### Purpose
This checklist defines the minimum expectations for contributions to the Kansas Frontier Matrix (KFM) repository.
It is intended to keep changes **reviewable, reproducible, provenance-linked, and governance-compliant**, while preserving the canonical pipeline ordering.

### Scope

| In Scope | Out of Scope |
|---|---|
| PR hygiene (summary, scope control, reviewability) | Replacing subsystem-specific SOPs |
| CI readiness (tests/validators run, expected gates understood) | Introducing new governance policy |
| Architecture invariants checks (pipeline ordering, API boundary) | Defining new ontology/schema without a linked governed doc |
| Provenance + sensitivity checks (STAC/DCAT/PROV, redaction) | Publishing sensitive locations or identities without approval |

### Audience
- Primary: Contributors opening PRs
- Secondary: Reviewers, maintainers, governance reviewers

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc (non-exhaustive): ETL, STAC, DCAT, PROV, Neo4j Graph, API boundary, Story Node, Focus Mode

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide (canonical invariants) | `docs/MASTER_GUIDE_v12.md` | Maintainers | Canonical pipeline + minimum CI gates |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Maintainers | Default governed doc template |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Maintainers | Required for story nodes |
| API Contract Extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | Maintainers | Required for API contract changes |
| CI docs entrypoint | `docs/ci/README.md` | Maintainers | CI overview + local workflows (if present) |

### Definition of done (for this document)
- [ ] Checklist items map to KFM’s documented invariants and CI gates (no invented policy)
- [ ] Change-type sections cover all major pipeline stages (data/catalog/graph/api/ui/story)
- [ ] The doc remains safe-by-default for sensitive content (FAIR+CARE and sovereignty)

## 🗂️ Directory Layout

### This document
- `path`: `docs/ci/checklists/PR_CHECKLIST.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Documentation | `docs/` | Canonical governed docs |
| CI docs | `docs/ci/` | CI overview + checklists |
| Templates | `docs/templates/` | Governed templates (Universal / Story Node / API Contract Extension) |
| Schemas | `schemas/` | JSON schemas + telemetry schemas |
| Pipelines | `src/pipelines/` | ETL + catalogs + transforms |
| Graph | `src/graph/` | Graph build + ontology bindings |
| APIs | `src/server/` | Contracted access layer |
| UI | `web/` | Map + narrative UI |

### Expected file tree for this sub-area
~~~text
📁 docs/
├── 📁 ci/
│   ├── 📄 README.md
│   └── 📁 checklists/
│       ├── 📄 README.md
│       └── 📄 PR_CHECKLIST.md
~~~

## 🧭 Context

### Background
KFM’s pipeline is intentionally modular and governed. CI is expected to protect:
- determinism and reproducibility,
- provenance-first outputs,
- strict API boundaries (UI does not read the graph directly),
- FAIR+CARE and sovereignty constraints for sensitive content.

### Constraints / invariants
- Preserve canonical ordering: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- Frontend consumes graph content **via APIs** (no direct Neo4j dependency).
- Story content must remain provenance-linked and non-speculative.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What are the repo’s canonical local CI commands (make/npm/poetry/etc.)? | Maintainers | TBD |

## 🗺️ Diagrams

### System / pipeline invariant (reference)
~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React/Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
~~~

## 🧪 Validation & CI/CD

### PR metadata checklist (required)
- [ ] Title is concise and imperative (e.g., “Add STAC validation for …”)
- [ ] Description includes:
  - [ ] what changed (1–3 bullets)
  - [ ] why it changed (link to issue/ticket if applicable)
  - [ ] how it was validated (tests/validators run)
  - [ ] risks/rollback notes (if applicable)
- [ ] Scope is limited to one coherent change set (split PRs if needed)
- [ ] Self-review completed (diff reviewed by the author)

### KFM governance + architecture checklist (required)
- [ ] The PR does **not** violate the canonical pipeline ordering
- [ ] The UI does **not** read Neo4j directly (all graph access remains behind API contracts)
- [ ] Any narrative content remains provenance-linked and avoids speculation
- [ ] No secrets, credentials, or tokens are introduced (including in examples, fixtures, screenshots)
- [ ] No PII or sensitive locations are introduced without documented handling (redaction/generalization + approvals)

### Change-type checklists

#### A) Docs-only changes
- [ ] Any new governed doc uses an approved template (Universal / Story Node / API Contract Extension)
- [ ] Front-matter is complete and `path:` matches the file location
- [ ] Links are relative and resolve within the repo
- [ ] Diagrams (mermaid) render and do not contain sensitive details

#### B) Data / ETL / transforms (`src/pipelines/`, `data/`)
- [ ] ETL steps are deterministic and idempotent (no duplicate loads on re-run)
- [ ] New/updated source inputs include license + attribution metadata
- [ ] Outputs land in correct staging area (`data/raw/` → `data/work/` → `data/processed/` → `data/stac/` as applicable)
- [ ] Transform/run metadata is recorded for provenance (run IDs / hashes / timestamps) as applicable

#### C) Catalog changes (STAC / DCAT / PROV)
- [ ] STAC items/collections validate against the repo’s STAC profile expectations
- [ ] Collection ↔ item integrity holds (items belong to correct collections; links not broken)
- [ ] DCAT dataset identifiers and license mapping are updated consistently
- [ ] PROV lineage references are included for derived products (prov:wasDerivedFrom, prov:wasGeneratedBy)

#### D) Graph changes (`src/graph/`, ontology bindings, migrations)
- [ ] Ontology changes are documented and versioned (migration plan included where needed)
- [ ] Node/edge labels align with repo ontology conventions (no ad-hoc labels without doc)
- [ ] Graph integrity checks (constraints/uniqueness) are satisfied
- [ ] Provenance references for ingested entities are retained

#### E) API changes (`src/server/` and/or API docs)
- [ ] API changes are documented using the API Contract Extension template
- [ ] Backward compatibility assessed:
  - [ ] non-breaking change OR
  - [ ] version bump / deprecation plan included
- [ ] Contract tests updated/added (OpenAPI/GraphQL schema lint + integration/unit tests as applicable)
- [ ] Responses include provenance references when feeding Focus Mode or story rendering

#### F) UI changes (`web/`)
- [ ] UI changes rely on API contracts (no direct graph calls)
- [ ] Any layer registry changes are schema-validated (if a layer registry exists)
- [ ] Accessibility checks performed (keyboard nav, labels, contrast, focus states)
- [ ] New UI surfaces include provenance rendering and sensitivity notices where applicable

#### G) Story Nodes / Focus Mode changes
- [ ] Story Nodes follow the Story Node template (v3)
- [ ] Every factual claim maps to a cited dataset/document ID (no unsourced narrative)
- [ ] Sensitive details are generalized/redacted per governance docs
- [ ] Focus Mode behavior does not expose restricted content by default

### Evidence of validation (required)
Provide *at least one* of:
- [ ] CI run link (preferred in PR conversation)
- [ ] A short summary of which validators/tests were executed locally (commands optional if not standardized)
- [ ] Output artifacts/log references (where the repo records them)

~~~bash
# Optional placeholder: replace with repo-standard commands if/when documented
# - schema validation (STAC/DCAT/PROV, telemetry)
# - unit/integration tests
# - doc lint / markdown protocol checks
~~~

## 🧑‍⚖️ Reviewer checklist (recommended minimum)
- [ ] PR description matches actual diff
- [ ] Scope is appropriate (no unrelated changes)
- [ ] Pipeline invariants preserved (ordering + API boundary)
- [ ] Validation evidence is credible (CI or local summary)
- [ ] Sensitive content handling is correct (or escalated for required review)
- [ ] Any contract/schema changes include versioning + tests

## ⚖ FAIR+CARE & Governance

### Review gates (trigger-based)
Escalate for additional review when a PR introduces or changes:
- [ ] New external data source(s)
- [ ] New public-facing endpoints
- [ ] New layers that may include sensitive locations or cultural context
- [ ] New AI narrative behaviors in Focus Mode
- [ ] Any change that affects sovereignty rules or redaction/generalization behavior

### AI usage constraints
- Follow the document’s `ai_transform_permissions` / `ai_transform_prohibited` constraints.
- No generated policy language should be introduced via AI outputs without governance review.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial PR checklist | TBD |

---
Footer refs:
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Templates: `docs/templates/`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

