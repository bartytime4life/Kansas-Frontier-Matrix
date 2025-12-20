---
title: "CI Runbooks — README"
path: "docs/ci/runbooks/README.md"
version: "v1.0.0"
last_updated: "2025-12-19"
status: "draft"
doc_kind: "RunbookIndex"
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

doc_uuid: "urn:kfm:doc:ci:runbooks:readme:v1.0.0"
semantic_document_id: "kfm-ci-runbooks-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:ci:runbooks:readme:v1.0.0"
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

# CI Runbooks — README

## 📘 Overview

### Purpose
- Provide step-by-step operational procedures (“runbooks”) for diagnosing and fixing CI failures in the Kansas Frontier Matrix (KFM) repository.
- Reduce time-to-triage while preserving KFM’s non-negotiable pipeline ordering and governance invariants.

### Scope
| In Scope | Out of Scope |
|---|---|
| CI failure triage and resolution steps | Defining governance policy (see governance docs) |
| Common failure modes: lint, tests, schema validation, contract checks | Implementing new subsystems without design review |
| “How to reproduce locally” guidance (repo commands TBD) | Incident comms / postmortems (unless explicitly added as runbooks) |

### Audience
- Primary: Maintainers, reviewers, CI owners
- Secondary: Contributors diagnosing their own PR failures

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc: CI, gate, runbook, checklist, pipeline stage, contract test, schema validation, provenance

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| CI overview | `docs/ci/README.md` | Maintainers | Entry point for CI conventions |
| Checklists index | `docs/ci/checklists/README.md` | Maintainers | When to use checklists vs runbooks |
| PR checklist | `docs/ci/checklists/PR_CHECKLIST.md` | Maintainers | Pre-merge gates |
| Release checklist | `docs/ci/checklists/RELEASE_CHECKLIST.md` | Maintainers | Release/packaging gates |
| Workflows | `.github/workflows/` | CI owners | Not confirmed in repo; link once present |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Runbook directory structure documented
- [ ] Naming conventions for runbooks defined
- [ ] Clear mapping from failure type → runbook
- [ ] Validation steps listed and repeatable (commands may be placeholders if not confirmed in repo)
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `docs/ci/runbooks/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| CI docs | `docs/ci/` | CI overview + contributor guidance |
| Checklists | `docs/ci/checklists/` | PR / release / recurring “do this before merge” lists |
| Runbooks | `docs/ci/runbooks/` | “When X breaks, do Y” operational guides |
| Workflows | `.github/workflows/` | CI runners + jobs (not confirmed in repo) |
| Schemas | `schemas/` | JSON schemas + telemetry schemas (if applicable) |
| Tests | `tests/` | Unit/integration/contract tests |
| Pipelines | `src/pipelines/` | ETL + catalog build jobs |
| Graph | `src/graph/` | graph build + ontology bindings |
| API | `src/server/` | contracted access layer (REST/GraphQL), if applicable |
| UI | `web/` | React + MapLibre UI, if applicable |

### Expected file tree for this sub-area
~~~text
📁 docs/
├── 📁 ci/
│   ├── 📄 README.md
│   ├── 📁 checklists/
│   │   ├── 📄 README.md
│   │   ├── 📄 PR_CHECKLIST.md
│   │   └── 📄 RELEASE_CHECKLIST.md
│   └── 📁 runbooks/
│       ├── 📄 README.md
│       ├── 📄 RUNBOOK__CI_TRIAGE.md                (recommended)
│       ├── 📄 RUNBOOK__DOCS_LINT_FAIL.md           (recommended)
│       ├── 📄 RUNBOOK__SCHEMA_VALIDATION_FAIL.md   (recommended)
│       ├── 📄 RUNBOOK__TESTS_FAIL.md               (recommended)
│       ├── 📄 RUNBOOK__SECURITY_SCAN_FAIL.md       (recommended)
│       └── 📄 RUNBOOK__RELEASE_PIPELINE_FAIL.md    (recommended)
~~~

## 🧭 Context

### Background
KFM’s pipeline is ordered and contract-driven. CI gates exist to keep that order stable and ensure that changes do not silently break catalogs, graph integrity, API contracts, or UI safety constraints.

### Assumptions
- Contributors will encounter CI failures in PRs and need a predictable path to diagnose them.
- CI should fail “loudly” at the earliest gate that can detect a violation.

### Constraints / invariants
- Canonical pipeline ordering is preserved (ETL → Catalogs → Graph → APIs → UI → Story Nodes → Focus Mode).
- Frontend consumes contracts via APIs (no direct graph dependency).
- No secrets/credentials in logs, docs, or artifacts.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What are the exact workflow job names and commands for local reproduction? | CI owners | TBD |
| Which schema validators are used (STAC/DCAT/PROV/telemetry)? | Maintainers | TBD |

### Future extensions
- Add runbooks for domain-specific pipelines (e.g., OCR ingest, geo reprojection, catalog rebuild).
- Add a “CI failure classifier” that links common log patterns to the correct runbook.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[CI Trigger: PR/Push] --> B[Lint / Formatting Gates]
  B --> C[Schema Validation Gates]
  C --> D[Tests (unit/integration)]
  D --> E[Contract Gates (API/UI)]
  E --> F[Security / Governance Gates]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant Dev as Developer
  participant CI as CI Runner
  participant Repo as Repo
  Dev->>Repo: Push / Open PR
  Repo->>CI: Start workflow(s)
  CI->>CI: Run gates in order
  CI-->>Dev: Status + logs
  Dev->>CI: Follow matching runbook
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Source changes | git diff | PR branch | Lint + tests + schema checks |
| Schemas | JSON/JSON-LD | `schemas/` | Validator (tooling TBD) |
| Catalogs | JSON/JSON-LD | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Catalog validators (tooling TBD) |
| Logs | text | CI runner | Redacted (no secrets) |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| CI status | checks | PR | “pass/fail” gates |
| Test reports | text/junit | CI artifacts | test framework schema |
| Build artifacts | files | CI artifacts | versioned where applicable |

### Sensitivity & redaction
- CI logs must not include secrets, tokens, or restricted locations/identifiers.
- If any runbook requires sharing logs externally, sanitize first.

### Quality signals
- Deterministic outputs where expected (same inputs → same results).
- Schema integrity: STAC/DCAT/PROV files validate and referential links resolve.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- CI should validate item/collection integrity and links (validator tooling not confirmed in repo).

### DCAT
- CI should verify required fields exist for any new dataset publication (validator tooling not confirmed in repo).

### PROV-O
- CI should ensure provenance bundles are present for generated artifacts where required.

### Versioning
- Runbooks should call out when a failure implies a contract version bump vs a simple fix.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| CI workflows | Run gates | `.github/workflows/` |
| Validators | Schema + link checks | CLI/tools (TBD) |
| Test runner | Execute tests | `tests/` |
| Security scanners | Secret/dependency checks | CI tools (TBD) |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Markdown protocol | `docs/` | Must remain CI-clean |
| JSON schemas | `schemas/` | Semver + changelog |
| Catalog structures | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Must validate + keep links consistent |

### Extension points checklist (for future work)
- [ ] Add new runbook file for a new CI gate
- [ ] Add log-pattern → runbook mapping to the CI overview
- [ ] Add contract tests when introducing a new API surface

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- CI should block merges that would allow unsourced narrative or break provenance linkage requirements.
- Predictive/AI content must remain opt-in and carry uncertainty/metadata (enforced by contracts where applicable).

### Provenance-linked narrative rule
- Every claim in user-facing Focus Mode contexts must trace to a dataset / record / asset ID.

### Optional structured controls
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### When to use a checklist vs a runbook
- **Checklist:** planned work (“before merge, ensure X, Y, Z”).
- **Runbook:** unplanned breakage (“CI failed on X; here’s what to do next”).

### Recommended runbook template (copy into each RUNBOOK__*.md)
~~~text
# RUNBOOK — <short name>

## Trigger
- What CI check(s) failed?

## Impact
- What is blocked? (PR merge, release, deployment)

## Fast Triage
- 3–5 quick checks to confirm the failure class.

## Diagnosis
- Common root causes + where to look in logs.

## Fix
- Step-by-step remediation guidance.
- If commands are required, note: "not confirmed in repo" until validated.

## Verify
- How to confirm locally and in CI.

## Notes / Gotchas
- Determinism, version bumps, redaction, etc.

## References
- Links to related docs/checklists/schemas.
~~~

### Validation steps
- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV + any telemetry schemas)
- [ ] Graph integrity checks (if graph build runs in CI)
- [ ] API contract tests (if API is changed)
- [ ] UI schema checks (layer registry, a11y) if applicable
- [ ] Security and sovereignty checks (as applicable)

### Reproduction
~~~bash
# not confirmed in repo:
# Add repo-specific commands for:
# 1) docs lint
# 2) schema validation
# 3) tests
# 4) contract checks
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| CI failure class | CI logs | `docs/ci/` or telemetry store (TBD) |

## ⚖ FAIR+CARE & Governance

### Review gates
- Changes that introduce new sensitive layers, new AI narrative behaviors, new external sources, or new public endpoints may require additional review (see governance refs).

### CARE / sovereignty considerations
- Runbooks must never instruct contributors to “work around” sovereignty/sensitivity enforcement.

### AI usage constraints
- Runbooks may summarize logs and suggest debugging steps.
- Runbooks must not invent facts about datasets, locations, or provenance.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial runbooks index | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

