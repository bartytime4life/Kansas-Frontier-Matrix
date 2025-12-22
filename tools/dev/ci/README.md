---
title: "KFM Dev CI — Local Reproduction + Gate Map"
path: "tools/dev/ci/README.md"
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

doc_uuid: "urn:kfm:doc:tools:dev:ci:readme:v1.0.0"
semantic_document_id: "kfm-tools-dev-ci-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:tools:dev:ci:readme:v1.0.0"
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

# KFM Dev CI — Local Reproduction + Gate Map

## 📘 Overview

### Purpose

This directory is the **developer-facing CI companion**:
- a single, repo-local place to explain **what CI is expected to check** (and why),
- how those checks map to KFM’s canonical pipeline ordering,
- and how to **reproduce CI gates locally** (when scripts/entrypoints exist).

This doc does **not** define governance policy; it points to canonical governance and standards docs.

### Scope

| In Scope | Out of Scope |
|---|---|
| CI gate inventory + mapping to KFM pipeline stages | Hosting-specific CI configuration (secrets, runners) |
| Repo-lint conventions enforced by CI | Writing new dataset ETL logic (see pipelines docs) |
| How to reproduce checks locally (best-effort) | Publishing data, releases, or deployments |

### Audience

- Primary: contributors running CI checks locally (engineers, data engineers).
- Secondary: reviewers validating PR readiness and contract alignment.

### Definitions (link to glossary)

- Link: `docs/glossary.md`
- Terms used in this doc: CI gate, repo lint, schema validation, contract test, provenance, redaction.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline invariants | `docs/MASTER_GUIDE_v12.md` | KFM maintainers | Canonical pipeline ordering + system inventory |
| Repo structure + CI mapping | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | KFM maintainers | “validate if present; fail if invalid; skip if not applicable” |
| Governed templates | `docs/templates/` | KFM maintainers | Universal / Story Node / API Contract templates |
| Validation schemas | `schemas/` | KFM maintainers | STAC / DCAT / PROV / storynodes / ui / telemetry |
| CI workflow definitions | `.github/workflows/` | KFM maintainers | If present; source of truth for exact commands |
| Local helper scripts | `tools/dev/ci/` | KFM maintainers | If present; should be callable by CI + devs |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] CI gates listed and mapped to pipeline stages
- [ ] Local reproduction guidance is present (even if command stubs are placeholders)
- [ ] Repo-lint rules documented (non-negotiables)
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document

- `path`: `tools/dev/ci/README.md` (must match front-matter)

### File tree

~~~text
📁 tools/
└── 📁 dev/
    └── 📁 ci/
        └── 📄 README.md
~~~

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed + catalog outputs (STAC/DCAT/PROV) |
| Documentation | `docs/` | Canonical governed docs + templates + standards |
| Schemas | `schemas/` | JSON schema & validation profiles (STAC/DCAT/PROV/etc.) |
| Pipelines | `src/pipelines/` | ETL + transforms + catalog build entrypoints |
| Graph | `src/graph/` | Ontology + graph build + migrations |
| API | `src/server/` | API layer + contracts (UI never reads Neo4j directly) |
| UI | `web/` | React/MapLibre UI + story rendering |
| Tests | `tests/` | Unit/integration/contract tests |
| CI workflows | `.github/workflows/` | Workflow definitions (if present) |

## 🧭 Canonical pipeline ordering (what CI must protect)

KFM’s non-negotiable ordering (do not bypass):
1) ETL  
2) STAC/DCAT/PROV catalogs  
3) Graph (Neo4j)  
4) APIs  
5) UI (React/Map)  
6) Story Nodes  
7) Focus Mode

**CI gates must be staged so that later layers cannot ship if earlier layers are invalid**, even if a PR only “touches UI.”

## 📦 Data & Metadata

### CI artifacts (build/test outputs)

CI may generate ephemeral artifacts such as:
- validation reports (schema lint output),
- unit/integration test results,
- build logs.

**Note:** The exact artifact formats/paths are **repo-specific** and should match CI workflow definitions.

## 🌐 STAC, DCAT & PROV Alignment

CI should ensure that (when present in a branch/PR):
- STAC artifacts validate against STAC schemas/profiles,
- DCAT outputs validate against DCAT schemas/profiles,
- PROV bundles validate against PROV schemas/profiles,
- identifiers remain stable and linkable from Story Nodes and API payloads.

## 🧱 Architecture

### Design intent

This folder is intended to host **shared, local-callable CI helpers** that can be invoked by:
- CI workflows (e.g., GitHub Actions), and
- developers reproducing checks locally.

Preferred characteristics for helper scripts (when added):
- deterministic + idempotent
- cross-platform (avoid OS-specific shell when possible)
- no secrets / no hardcoded credentials
- clear exit codes + machine-readable output when practical

### “Validate if present” principle

If an artifact category exists in the repo (schemas, catalogs, story nodes, etc.), CI should:
- validate it if present,
- fail the run if invalid,
- skip checks that don’t apply to the change set.

## 🧠 Story Node & Focus Mode Integration

CI must treat Story Nodes as governed outputs:
- validate Story Node front-matter and required keys,
- require evidence/provenance links,
- enforce redaction/generalization rules for sensitive content,
- ensure “no prohibited AI actions implied” (e.g., do not infer sensitive locations).

See Story Node template and governance docs for exact expectations.

## 🧪 Validation & CI/CD

### Minimum CI gate set (baseline)

CI should cover at least:
- Markdown protocol checks (front-matter + structure)
- Schema validation for STAC/DCAT/PROV (where present)
- Graph integrity checks (ontology + constraints)
- API contract tests (OpenAPI/GraphQL contracts, if present)
- UI layer registry schema checks (if present)
- Security + sovereignty scanning gates (secrets/PII/sensitive location rules)

### CI gate map (recommended)

| Pipeline stage | Typical change areas | Gate(s) to run | “Source of truth” |
|---|---|---|---|
| Docs | `docs/`, templates | markdown protocol + link checks | templates + standards |
| ETL | `src/pipelines/`, `data/<domain>/raw|work|processed` | unit tests + deterministic outputs | pipeline docs + tests |
| Catalog | `data/stac/`, `data/catalog/dcat/`, `data/prov/`, `schemas/` | schema validation (STAC/DCAT/PROV) | `schemas/` + profiles |
| Graph | `src/graph/`, `data/graph/` | ontology + constraint + integrity checks | graph docs + tests |
| API | `src/server/` | contract tests + integration tests | API contract docs |
| UI | `web/` | build + lint + UI schema checks | UI docs + tests |
| Story | `docs/reports/story_nodes/` | story node validation (front-matter, citations, redaction) | Story Node template |
| Focus Mode | `web/` story rendering | integration tests (if present) | UI + story contracts |

### Repo lint rules (non-negotiables)

At minimum:
- **No YAML front-matter in code files** (reserve governed YAML headers for governed markdown/docs).
- **No “README.me” files** (use `README.md`).
- **No duplicate canonical homes without explicit deprecation markers** (avoid ambiguous subsystem roots).

### Running CI checks locally

Exact commands are **repo-specific**. The safest way to reproduce CI locally is:
1) Inspect `.github/workflows/` and copy the commands from the relevant jobs.
2) Run those commands in the same runtime (python/node versions, env vars).

If this repo later adds local helpers in `tools/dev/ci/`, prefer wrappers like:

~~~bash
# Placeholder examples — replace with real entrypoints if/when they exist.

# 1) Docs / markdown protocol
# ./tools/dev/ci/validate_docs.sh

# 2) Schemas
# ./tools/dev/ci/validate_schemas.sh

# 3) Tests
# ./tools/dev/ci/run_tests.sh

# 4) UI build/lint
# ./tools/dev/ci/validate_ui.sh
~~~

### Adding a new CI gate (checklist)

- [ ] Identify pipeline stage impacted (ETL / Catalog / Graph / API / UI / Story)
- [ ] Define/extend a schema or contract in `schemas/` or `docs/templates/`
- [ ] Add a validator (prefer deterministic, cross-platform)
- [ ] Wire validator into CI workflow(s)
- [ ] Add/extend tests for the validator itself
- [ ] Update this README gate map + troubleshooting notes

### Troubleshooting (common patterns)

- **Schema validation fails**: confirm artifacts exist in expected locations; do not “fix” by relaxing schemas without governance review.
- **Repo lint fails**: remove front-matter from non-doc files; rename any `README.me` to `README.md`.
- **Story Node validation fails**: ensure citations resolve, entity IDs exist (or have creation tickets), and sensitive info rules are met.

## ⚖ FAIR+CARE & Governance

### Review gates

This doc is non-authoritative; changes to:
- standards (`docs/standards/`)
- templates (`docs/templates/`)
- governance (`docs/governance/`)
- schemas (`schemas/`)
should be treated as **requires human review**.

### CARE / sovereignty considerations

CI must not encourage:
- inference of sensitive locations,
- disclosure of protected community knowledge,
- bypassing redaction/generalization rules.

### AI usage constraints

This document permits AI transforms like summarization/structure extraction, but prohibits generating governance policy or inferring sensitive locations (see front-matter).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial CI README scaffold | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
