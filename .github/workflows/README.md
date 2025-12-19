---
title: "GitHub Actions Workflows"
path: ".github/workflows/README.md"
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

doc_uuid: "urn:kfm:doc:github:workflows-readme:v1.0.0"
semantic_document_id: "kfm-github-workflows-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github:workflows-readme:v1.0.0"
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

# GitHub Actions Workflows

## 📘 Overview

### Purpose
This directory documents the GitHub Actions workflows that enforce Kansas Frontier Matrix (KFM) CI/CD
quality gates. These gates exist to keep the canonical pipeline and contracts stable across contributions:

ETL → STAC/DCAT/PROV → Neo4j Graph → APIs → React/Map UI → Story Nodes → Focus Mode.

This README is the *human-facing index* for what each workflow checks, what it outputs, and how to extend
the workflow set safely.

### Scope

| In Scope | Out of Scope |
|---|---|
| Workflow intent + ownership | Full implementation details of each job step |
| Minimum CI gates (what must be enforced) | Environment provisioning for self-hosted runners |
| How to add/modify workflows without breaking governance | Production deployment runbooks (unless stored here explicitly) |

### Audience
- Primary: Contributors adding data, schemas, pipelines, graph changes, APIs, UI, or story nodes.
- Secondary: Maintainers enforcing branch protection and governance reviewers.

### Definitions (link to glossary)
- Link: `docs/glossary.md` (not confirmed in repo)
- Terms used in this doc: workflow, job, status check, provenance, STAC, DCAT, PROV, contract test, redaction.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Canonical pipeline + CI gates | `docs/MASTER_GUIDE_v12.md` | Maintainers | Source of truth for minimum validation gates |
| Universal governed doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs maintainers | Formatting + governance headers |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Docs maintainers | Provenance-linked narrative format |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API maintainers | REST/GraphQL contract governance |

### Definition of done (for this document)
- [x] Front-matter complete + valid (template-aligned)
- [ ] Workflow list reflects actual `.yml` files in this directory (requires repo audit)
- [x] Minimum CI gates enumerated and mapped to pipeline stages
- [ ] Local reproduction commands are repo-accurate (requires repo audit)
- [x] Sensitivity + sovereignty + secret-handling expectations stated

## 🗂️ Directory Layout

### This document
- `path`: `.github/workflows/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| GitHub Actions workflows | `.github/workflows/` | CI checks, scheduled jobs, release automation |
| Composite actions (optional) | `.github/actions/` | Reusable action steps (not confirmed in repo) |
| Documentation | `docs/` | Governed system docs + templates |
| Data domains | `data/` | Raw/work/processed/stac outputs |
| Schemas | `schemas/` | JSON schemas + telemetry schemas |
| Pipelines | `src/pipelines/` | ETL + catalog + transforms |
| Graph | `src/graph/` | Ontology bindings + migrations |
| APIs | `src/server/` | REST/GraphQL layer (contract boundary) |
| UI | `web/` | React + map clients |
| Tests | `tests/` | Unit/integration/contract tests |

### Expected file tree for this sub-area
The exact workflow filenames are **not confirmed in repo**. This is the recommended baseline set; align
names to existing files if they already exist.

~~~text
📁 .github/
└── 📁 workflows/
    ├── 📄 README.md
    ├── 📄 ci.yml
    ├── 📄 docs.yml
    ├── 📄 schemas.yml
    ├── 📄 graph.yml
    ├── 📄 api-contracts.yml
    ├── 📄 ui.yml
    ├── 📄 security.yml
    └── 📄 release.yml
~~~

## 🧭 Context

### Background
KFM is a pipeline-driven system with strict, contract-first boundaries. CI workflows are the enforcement
mechanism that prevents:
- invalid catalog outputs (STAC/DCAT/PROV),
- broken graph integrity or ontology drift,
- API contract regressions,
- UI schema drift or provenance leakage,
- story node narrative without evidence.

### Assumptions
- This repository uses GitHub Actions as the CI runner.
- Workflows run on pull requests and (optionally) on a schedule for freshness checks.
- Command details are repo-specific and must be updated once the actual build tooling is confirmed.

### Constraints / invariants
- The canonical pipeline ordering is preserved.
- UI never reads Neo4j directly; all data access is mediated through API contracts.
- All public-facing narrative must be provenance-linked (dataset/document IDs).
- Deterministic, replayable pipeline steps are required (no silent nondeterminism).
- No secrets/credentials committed; workflows must use GitHub Secrets/OIDC and least privilege.
- No prohibited AI actions implied (e.g., inferring sensitive locations).

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What are the exact commands/entrypoints for schema validation (STAC/DCAT/PROV)? | Maintainers | TBD |
| What are the exact graph integrity test commands and constraints checks? | Graph maintainers | TBD |
| What contract-test harness is used (OpenAPI, GraphQL schema lint, etc.)? | API maintainers | TBD |
| What doc lint/Markdown protocol checker is used in CI? | Docs maintainers | TBD |

### Future extensions
- Add per-domain workflow matrices (run only the checks impacted by changed paths).
- Add required “provenance bundle” artifact upload for PR review (e.g., validation reports).

## 🗺️ Diagrams

### CI gate overview
~~~mermaid
flowchart LR
  PR[Pull Request / Push] --> GA[GitHub Actions]
  GA --> Docs[Docs + Markdown protocol]
  GA --> Schemas[STAC/DCAT/PROV + schema validation]
  GA --> Graph[Graph integrity + migrations]
  GA --> API[API contract + tests]
  GA --> UI[UI build + registry schema]
  GA --> Sec[Security + sovereignty checks]
  Docs --> Pass[Required checks green]
  Schemas --> Pass
  Graph --> Pass
  API --> Pass
  UI --> Pass
  Sec --> Pass
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Source code + configs | repo files | Git checkout | lint + tests |
| Data artifacts (if committed) | JSON/GeoJSON/CSV/etc. | `data/` | schema + integrity |
| Schemas | JSON Schema | `schemas/` | schema lint + tests |
| Docs | Markdown | `docs/` + other `.md` | markdown protocol + lint |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Status checks | GitHub check runs | GitHub UI | branch protection rules |
| Validation reports (recommended) | JSON/TXT/MD | CI artifacts | schema-defined if persisted |
| Build/test logs | text | CI artifacts | n/a |

### Sensitivity & redaction
- Workflows must not echo secrets into logs.
- If workflows touch restricted/sensitive datasets (locations/communities), they must:
  - enforce redaction/generalization rules at the API boundary,
  - fail PRs that attempt to expose restricted fields in public outputs,
  - require governance review when changing sensitivity classifications.

### Quality signals
- Required checks should include:
  - schema validity (STAC/DCAT/PROV),
  - graph integrity and constraint checks,
  - API contract tests,
  - UI schema checks (layer registry),
  - doc protocol compliance.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
CI should validate (at minimum):
- Items and collections are valid STAC JSON and reference each other correctly.
- Required links and assets resolve (no broken internal links).
- Geometry and bbox are present/valid where required.

Expected locations (per KFM pipeline conventions):
- `data/stac/collections/`
- `data/stac/items/`

### DCAT
CI should validate:
- DCAT records conform to the project’s DCAT profile.
- Dataset identifiers and license fields are present.
- Distribution links resolve (or are intentionally stubbed with a TODO marker).

Expected location:
- `data/catalog/dcat/`

### PROV-O
CI should validate:
- Each generated artifact can point to a `prov:wasDerivedFrom` source ID.
- Each build/run activity has a stable run identifier (prov activity/run ID).
- Provenance bundles are present when required.

Expected location:
- `data/prov/`

### Versioning
- If STAC items/collections are versioned, CI should enforce predecessor/successor link correctness.
- Graph and API contract versions must not regress without a documented version bump.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| GitHub Actions workflows | Run validation gates on changes | status checks + artifacts |
| Composite actions (optional) | Reuse common steps | `uses: ./.github/actions/<name>` |
| Branch protection | Require checks before merge | GitHub settings |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog |
| API schemas | `src/server/` + docs | contract tests required |
| Layer registry | `web/` (registry path TBD) | schema-validated |

### Extension points checklist (for future work)
When adding a new workflow or expanding an existing one, ensure:
- [ ] It maps to one or more pipeline stages (ETL / Catalog / Graph / API / UI / Story).
- [ ] It is deterministic and version-pinned where possible.
- [ ] It outputs actionable failure messages (what to fix + where).
- [ ] It does not require secrets for PRs from forks (use safe fallbacks).
- [ ] It does not bypass governance/sensitivity gates.

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
Workflows should enforce that Story Nodes:
- are provenance-linked (dataset/document IDs are present),
- do not contain unsourced factual claims,
- do not imply prohibited AI actions (e.g., inferring sensitive locations).

### Provenance-linked narrative rule
Every claim must trace to a dataset / record / asset ID (or be explicitly marked as hypothesis/inference).

## 🧪 Validation & CI/CD

### Minimum CI gates (v12-ready baseline)
These gates must be enforced by one or more workflows:
- [ ] Markdown protocol validation
- [ ] JSON schema validation (STAC/DCAT/PROV and telemetry if applicable)
- [ ] Graph integrity checks
- [ ] API contract tests
- [ ] UI layer registry schema checks
- [ ] Security and sovereignty scanning gates (as applicable)

### Reproduction
Repo-specific commands are **not confirmed in repo**. Replace the placeholders below with the project’s
actual scripts/targets once identified.

~~~bash
# Example placeholders — replace with repo-specific commands

# Docs + markdown protocol
# <command>

# STAC/DCAT/PROV schema validation
# <command>

# Graph integrity checks
# <command>

# API contract tests
# <command>

# UI build + registry schema checks
# <command>

# Security scans (deps/secrets)
# <command>
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| CI gate pass/fail counts | GitHub checks | `docs/telemetry/` + `schemas/telemetry/` (not confirmed in repo) |
| Schema validation errors | CI job artifacts | CI artifacts store |
| Security scan findings | CI job artifacts | CI artifacts store |

## ⚖ FAIR+CARE & Governance

### Review gates
- Changes that affect **public exposure** of data (especially sensitive content) require governance review.
- Changes that introduce new external data sources require provenance + licensing review.
- Changes that add predictive/AI outputs require uncertainty/confidence metadata and opt-in UX behavior.

### CARE / sovereignty considerations
- Do not expose restricted locations or culturally sensitive information.
- When in doubt: generalize, redact, and route for human review.

### AI usage constraints
This directory’s workflows must not introduce automation that violates:
- `ai_transform_prohibited` constraints in governed docs (e.g., “infer_sensitive_locations”).
- provenance-first narrative rules for Focus Mode.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial workflows README scaffold | TBD |

---
Footer refs:
- Master guide: `docs/MASTER_GUIDE_v12.md`
- Universal doc template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- API contract extension template: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`