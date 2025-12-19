---
title: "KFM CI — Release Checklist"
path: "docs/ci/checklists/RELEASE_CHECKLIST.md"
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

doc_uuid: "urn:kfm:doc:ci:checklists:release-checklist:v1.0.0"
semantic_document_id: "kfm-ci-release-checklist-v1.0.0"
event_source_id: "ledger:kfm:doc:ci:checklists:release-checklist:v1.0.0"
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

# KFM CI — Release Checklist

## 📘 Overview

### Purpose
This checklist is the governed “release gate” for Kansas Frontier Matrix (KFM). It exists to ensure a release does not break the canonical pipeline ordering (ETL → STAC/DCAT/PROV → Neo4j Graph → APIs → React/Map UI → Story Nodes → Focus Mode) and that provenance- and contract-driven delivery remains intact.

### Scope
| In Scope | Out of Scope |
|---|---|
| Validating release readiness across data, catalogs, graph, API, UI, story artifacts, and docs | Operational deployment steps not documented in-repo (not confirmed in repo) |
| Tagging/versioning hygiene and release notes completeness | Platform-specific “how to publish” instructions (not confirmed in repo) |
| Confirming governance/sensitivity triggers are addressed | Creating new policy (prohibited) |

### Audience
- Primary: Release manager / maintainers
- Secondary: Reviewers approving release candidates

### Definitions (link to glossary)
- Link: `docs/glossary.md` (not confirmed in repo)
- Terms used in this doc:
  - “Canonical pipeline”
  - “Contract tests”
  - “Provenance-linked narrative”
  - “Sensitivity / CARE gating”

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| PR checklist | `docs/ci/checklists/PR_CHECKLIST.md` | Maintainers | Must be satisfied for all release-bound PRs |
| CI checklists index | `docs/ci/checklists/README.md` | Maintainers | Navigation + checklist taxonomy |
| Master guide | `docs/MASTER_GUIDE_v12.md` | Maintainers | Pipeline invariants + minimum CI gates |

### Definition of done (for this release)
- [ ] Release scope is defined (version + what’s included)
- [ ] All required validation gates pass (docs, schemas, graph, API, UI, security/sovereignty)
- [ ] Backward compatibility evaluated; breaking changes handled via contract/versioning
- [ ] Release notes are complete and provenance/security considerations are documented
- [ ] Post-release verification steps completed (basic smoke verification + audit expectations)

## 🗂️ Directory Layout

### This document
- `path`: `docs/ci/checklists/RELEASE_CHECKLIST.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| CI docs | `docs/ci/` | CI conventions, checklists, release guidance |
| Checklists | `docs/ci/checklists/` | PR + release gates |
| Schemas | `schemas/` | JSON schemas (STAC/DCAT/PROV/telemetry as applicable) |
| Tests | `tests/` | Unit/integration/contract tests (not confirmed in repo) |
| Workflows | `.github/workflows/` | CI pipelines (not confirmed in repo) |
| Releases | `releases/` | Release notes/artifacts (not confirmed in repo) |

### Expected file tree for this sub-area
~~~text
📁 docs/
└── 📁 ci/
    └── 📁 checklists/
        ├── 📄 README.md
        ├── 📄 PR_CHECKLIST.md
        └── 📄 RELEASE_CHECKLIST.md
~~~

## 🧭 Context

### Background
Releases in KFM must preserve:
- The canonical pipeline ordering and handoff artifacts.
- The API boundary: **UI does not read Neo4j directly** (all consumption via API contracts).
- Provenance-first narrative: **Focus Mode must not contain unsourced narrative**.

### Assumptions
- The repository has CI automation that can run schema validation, tests, and doc lint (not confirmed in repo).
- Versioning follows a semver-like discipline (not confirmed in repo).

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode ordering is preserved.
- Frontend consumes contracts via APIs (no direct graph dependency).
- No sensitive locations are inferred or newly disclosed by documentation artifacts.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What is the canonical release branching strategy (e.g., `main` + tags vs `release/*`)? (not confirmed in repo) | TBD | TBD |
| Where are release notes stored and how are they generated? (not confirmed in repo) | TBD | TBD |
| What tooling exists for schema validation, graph integrity tests, and contract tests? (not confirmed in repo) | TBD | TBD |

### Future extensions
- Add a “Release Candidate (RC)” checklist variant if RCs are adopted (not confirmed in repo).
- Add automation references to concrete workflow names once `.github/workflows/` is finalized (not confirmed in repo).

## 🗺️ Diagrams

### Release gate coverage (conceptual)
~~~mermaid
flowchart LR
  A[Code + Data Changes] --> B[CI Gates]
  B --> C[Catalog Validation: STAC/DCAT/PROV]
  B --> D[Graph Integrity]
  B --> E[API Contract Tests]
  B --> F[UI Build + A11y]
  B --> G[Story Node + Provenance Checks]
  C --> H[Release Tag + Notes]
  D --> H
  E --> H
  F --> H
  G --> H
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Release candidate commit set | Git refs | PRs merged to release target | PR checklist satisfied |
| Schemas | JSON / JSON-LD | `schemas/` | Schema lint/validation |
| Catalog outputs | STAC/DCAT/PROV | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Schema + integrity checks |
| Docs | Markdown | `docs/` | Markdown protocol checks |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Release notes | Markdown | `releases/` (not confirmed in repo) | Repo convention (TBD) |
| Tagged release | Git tag | e.g., `vX.Y.Z` (not confirmed in repo) | Versioning convention (TBD) |
| Build artifacts | varies | CI artifacts store (not confirmed in repo) | CI pipeline definition (TBD) |

### Sensitivity & redaction
- [ ] Confirm no new sensitive locations (or restricted site coordinates) are included in public docs, story nodes, or UI layer registries.
- [ ] If any content is sensitive, ensure generalization/redaction rules are applied and reviewed (requires human review).

### Quality signals
- [ ] STAC Items/Collections validate and resolve (no broken links).
- [ ] DCAT mappings include minimum title/description/license/keywords where required.
- [ ] PROV lineage is present for generated artifacts (activity/run IDs where applicable).

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- [ ] Any new datasets include STAC Collection + Items (if applicable).
- [ ] Collections/Items validate against the project profile.
- [ ] Links and assets resolve (no broken-link regressions).

### DCAT
- [ ] DCAT dataset record exists/updated for any new dataset (if applicable).
- [ ] License + publisher/contact mapping are present where required.

### PROV-O
- [ ] Any generated artifacts include provenance references (`prov:wasDerivedFrom`, `prov:wasGeneratedBy`) where applicable.
- [ ] Run identifiers are captured for release-critical transforms (not confirmed in repo).

### Versioning
- [ ] Predecessor/successor lineage is recorded for versioned datasets where applicable.
- [ ] Graph mirrors version lineage where applicable (not confirmed in repo).

## 🧱 Architecture

### Components (release impact checklist)
| Component | Release concerns | Interface to verify |
|---|---|---|
| ETL | deterministic + replayable runs | configs + run logs |
| Catalogs | machine-validated outputs | STAC/DCAT/PROV JSON + validators |
| Graph | stable labels/edges + migrations safe | graph build + constraints |
| APIs | backward compat or version bump | OpenAPI/GraphQL schema + tests |
| UI | no hidden data leakage; a11y | build + layer registry schema |
| Story Nodes | provenance-linked narrative | citations + entity links |
| Focus Mode | no hallucinated sources | context bundle + audit flags |

### Interfaces / contracts
- [ ] UI uses API contracts only (no direct graph reads).
- [ ] Any API contract changes are either backward compatible or versioned with deprecation notes.
- [ ] Schema versions are bumped consistently where required.

### Extension points checklist (for release readiness)
- [ ] New domains follow `data/<domain>/...` placement rules.
- [ ] Derived datasets are in `data/processed/`, not `src/`.
- [ ] Any new Story Node types have governed templates and validation rules (not confirmed in repo).

## 🧠 Story Node & Focus Mode Integration

### Provenance-linked narrative rule
- [ ] Every factual claim in Story Nodes must map to cited dataset/document IDs.
- [ ] Any predictive content is opt-in and includes uncertainty/confidence fields (if present).

### Focus Mode behavior expectations
- [ ] Citation rendering remains functional.
- [ ] Audit panel expectations remain intact (warnings, citations, sensitivity notices).

## 🧪 Validation & CI/CD

### Release validation checklist (run in order)
#### 0) Governance + change classification
- [ ] Identify whether release includes any of:
  - New sensitive layers
  - New AI narrative behaviors
  - New external data sources
  - New public-facing endpoints
- [ ] If yes to any: mark **requires human review** and record reviewer sign-offs.

#### 1) Documentation integrity
- [ ] Markdown protocol checks pass for changed docs.
- [ ] All new/updated governed docs have valid front-matter (path, version, last_updated).
- [ ] No references to nonexistent files unless explicitly marked “not confirmed in repo”.

#### 2) Schema validation (STAC/DCAT/PROV/telemetry)
- [ ] JSON schema validation passes for all changed schema-bound assets.
- [ ] STAC/DCAT/PROV alignment checks pass (where applicable).

#### 3) Graph integrity
- [ ] Graph build/migrations (if any) are applied safely (not confirmed in repo).
- [ ] Constraint and integrity tests pass (not confirmed in repo).

#### 4) API contract tests
- [ ] REST/GraphQL schema lint passes (if applicable).
- [ ] Contract tests pass; breaking changes are versioned or explicitly handled.

#### 5) UI checks
- [ ] UI builds successfully.
- [ ] Layer registry schema checks pass (if present).
- [ ] A11y checks pass for release-critical UI changes (not confirmed in repo).

#### 6) Security + sovereignty checks
- [ ] Security scanning gates pass (where applicable).
- [ ] Sovereignty/CARE checks pass for any restricted content (where applicable).

### Reproduction
~~~bash
# Placeholders — replace with repo-specific commands (not confirmed in repo)
# 1) run doc lint / markdown protocol validation
# 2) validate STAC/DCAT/PROV schemas + link integrity
# 3) run unit/integration tests + graph integrity tests
# 4) run API contract tests (OpenAPI / GraphQL)
# 5) build UI + run a11y checks
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| Release validation run ID | CI system | `mcp/runs/` or CI logs (not confirmed in repo) |
| Schema validation report | validator | CI artifacts (not confirmed in repo) |

## ⚖ FAIR+CARE & Governance

### Review gates
- [ ] FAIR+CARE council review required? (yes/no)
- [ ] Security council review required? (yes/no)
- [ ] Historian/editor review required? (yes/no)

### CARE / sovereignty considerations
- [ ] Identify communities impacted by any new content.
- [ ] Ensure sensitive locations are generalized/redacted where required.

### AI usage constraints
- [ ] Ensure this document does not imply prohibited AI actions (e.g., generating policy, inferring sensitive locations).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial release checklist (draft) | TBD |
---

Footer refs:
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Checklist index: `docs/ci/checklists/README.md`
- PR checklist: `docs/ci/checklists/PR_CHECKLIST.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

