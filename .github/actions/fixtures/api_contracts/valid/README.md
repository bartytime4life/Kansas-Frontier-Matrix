---
title: "API Contract Fixtures — Valid Cases"
path: ".github/actions/fixtures/api_contracts/valid/README.md"
version: "v1.0.0"
last_updated: "2025-12-22"
status: "draft"
doc_kind: "README"
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

doc_uuid: "urn:kfm:doc:ci:fixtures:api-contracts:valid-readme:v1.0.0"
semantic_document_id: "kfm-ci-fixtures-api-contracts-valid-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:ci:fixtures:api-contracts:valid-readme-v1.0.0"
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

# API Contract Fixtures — Valid Cases

## 📘 Overview

### Purpose
- This directory holds **intentionally valid** API contract fixtures used to verify that contract validators **accept correct inputs** (positive testing).
- These fixtures act as a stable baseline to detect:
  - validator regressions that incorrectly reject valid specs
  - rule changes that break backwards-compatibility unexpectedly
  - environment-dependent behavior (non-deterministic validation)

### Scope

| In Scope | Out of Scope |
|---|---|
| Minimal “known-good” contract specimens that must validate successfully | Authoritative production contracts (source-of-truth) |
| Deterministic fixtures that can run offline in CI | Fixtures that require network access, secrets, or external services |
| Clear coverage of supported contract dialect features | Duplicating the full production API surface |

### Audience
- Primary: CI / validation maintainers; API contract maintainers
- Secondary: contributors extending validators, schema rules, or contract formats

### Definitions (link to glossary)
- Link: `docs/glossary.md` (*not confirmed in repo; add if missing*)
- Terms used here:
  - **Fixture**: static test input used by CI.
  - **Valid fixture**: fixture that must pass validation.
  - **Positive test**: test that passes only when the validator accepts valid input.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Valid contract fixtures | `.github/actions/fixtures/api_contracts/valid/` | CI maintainers | This directory |
| Fixture root (context) | `.github/actions/fixtures/api_contracts/` | CI maintainers | See sibling README (if present) |
| Contract validation workflow(s) | `.github/workflows/` | CI maintainers | Exact workflow name not confirmed in repo |
| API contract sources (canonical) | `src/server/` | API maintainers | Canonical home in KFM design; exact layout not confirmed in repo |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Clear explanation of why valid fixtures exist and how CI uses them
- [ ] Guidance for adding new valid fixtures (naming + minimalism)
- [ ] Validation steps listed and repeatable (even if placeholders)
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `.github/actions/fixtures/api_contracts/valid/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| CI / GitHub automation | `.github/` | Workflows and composite actions |
| Contract fixtures | `.github/actions/fixtures/api_contracts/` | Fixture root for API-contract validation |
| Valid fixtures | `.github/actions/fixtures/api_contracts/valid/` | Known-good fixtures (must pass validation) |
| API boundary | `src/server/` | API implementations + contracts (OpenAPI/GraphQL), consumed by UI via APIs |
| Schemas | `schemas/` | JSON Schemas / other interface schemas |
| Documentation | `docs/` | Canonical governed docs + templates |

### Expected file tree for this sub-area
~~~text
📁 .github/
└── 📁 actions/
    └── 📁 fixtures/
        └── 📁 api_contracts/
            └── 📁 valid/
                ├── 📄 README.md
                └── 📁 <contract_type>/
                    ├── 📄 <id>__<short_purpose>.<ext>
                    └── 📄 <id>__<short_purpose>.<ext>
~~~

Notes:
- `<contract_type>` is intentionally generic (e.g., `openapi/`, `graphql/`, `jsonschema/`) because supported formats are **not confirmed in repo**.
- Prefer **stable** names (no timestamps) to keep expectations deterministic.
- Favor “one concept per fixture” to keep test failures easy to diagnose.

## 🧭 Context

### Background
Contract validators can regress in multiple ways:
- accepting malformed specs
- rejecting valid specs due to rule changes
- behaving differently across environments or tool versions

Valid fixtures provide a reliable positive baseline so CI can assert:
- “validators still accept what we consider correct”
- “we did not unintentionally tighten/loosen validation rules”
- “contract tooling behaves deterministically”

### Assumptions
- A CI job exists that runs contract validation and uses these fixtures as positive tests. (Inferred from directory placement; exact wiring is not confirmed in repo.)
- A “positive test” run is considered successful when the validator **accepts** these fixtures.

### Constraints / invariants
- Preserve the canonical pipeline ordering:
  **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- Frontend consumes contracts via APIs (no direct graph dependency).
- Valid fixtures MUST NOT include secrets, API keys, private tokens, or real PII.
- Deterministic fixtures only:
  - Avoid “generated at runtime” IDs or timestamps.
  - Avoid external $refs unless they resolve locally within the fixture directory (or the validator’s standard local resolution paths).

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Which contract formats are validated (OpenAPI, GraphQL SDL, etc.)? | CI maintainers | TBD |
| Does CI check “pass only”, or also snapshot error-free outputs? | CI maintainers | TBD |
| Are `.github/**.md` files subject to Markdown protocol lint in CI? | CI maintainers | TBD |

### Future extensions
- Add format-specific subfolders once supported contract types are confirmed.
- Optionally add a manifest (e.g., `fixtures.yaml`) if the harness benefits from explicit enumeration (*not confirmed in repo*).
- Add “compatibility fixtures” to represent supported legacy features if the project maintains old clients (*not confirmed in repo*).

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  Dev[Contributor] --> PR[Pull Request]
  PR --> CI[GitHub Actions CI]

  CI --> Validator[Contract validator: action or script]
  CI --> Fixtures[Valid fixtures: api_contracts/valid]
  Fixtures --> Validator

  Validator --> Result{Expected outcome?}
  Result -->|Accepted = PASS| OK[CI check passes]
  Result -->|Rejected = REGRESSION| Fail[CI check fails]
~~~

### Canonical pipeline reminder
~~~mermaid
flowchart LR
  A[ETL] --> B[STAC, DCAT, PROV]
  B --> C[Neo4j graph]
  C --> D[APIs]
  D --> E[React and Map UI]
  E --> F[Story nodes]
  F --> G[Focus mode]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Valid contract fixtures | YAML/JSON/SDL/etc. | `.github/actions/fixtures/api_contracts/valid/**` | Must be accepted by validator |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| CI validation result | pass/fail + logs | GitHub Actions logs / annotations | N/A |
| Regression signal | PR status check | GitHub PR checks | N/A |

### Sensitivity & redaction
- Fixtures should be **public-safe** by default.
- Do not include real person names, emails, phone numbers, precise sensitive locations, or any access tokens.

### Quality signals
- Deterministic pass (no flakiness)
- Minimal and well-scoped fixtures (one purpose per file)
- Stable naming; no ambiguous fixture intent
- Fixture coverage aligns with currently supported contract dialect features

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Not applicable: this directory is for API contract fixtures, not catalog artifacts.

### DCAT
- Not applicable: this directory does not define dataset catalog entries.

### PROV-O
- Not applicable: this directory does not define provenance bundles.

### Versioning
- Fixtures evolve alongside validator rules.
- If a validator’s expectations change intentionally, update:
  - the relevant fixtures here
  - the CI harness expectations
  - any related documentation
  in the same PR.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| Valid fixtures (this dir) | Provide positive test inputs | File system |
| Contract validator (CI) | Accept valid inputs | CLI / action step |
| CI workflow | Gate merges on validator behavior | GitHub Actions |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Valid fixture set | `.github/actions/fixtures/api_contracts/valid/` | Add fixtures when features/rules are added; keep deterministic names |
| API schemas (source contracts) | `src/server/` (+ docs) | Contract tests required; versioned APIs |
| JSON schemas (supporting) | `schemas/` | Semver + changelog |

### Extension points checklist (for future work)
- [ ] Add `<contract_type>/` folders as new formats are validated
- [ ] Ensure CI enumerates new fixtures and expects them to pass
- [ ] Link from fixture root README to this README (if not already linked)

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Indirectly: robust API contract validation helps ensure Focus Mode receives stable, schema-consistent payloads.

### Provenance-linked narrative rule
- Not applicable to fixtures; they must not be used as narrative evidence.

### Optional structured controls
~~~yaml
focus_layers:
  - "N/A (fixtures)"
focus_time: "N/A"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (if applied to `.github/**.md`)
- [ ] API contract tests (valid fixtures must pass validation)
- [ ] Security checks (no secrets / no PII / no sensitive locations)
- [ ] Determinism check (repeat runs produce the same outcome)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands

# 1) run the contract validator against valid fixtures
# <validator-command> .github/actions/fixtures/api_contracts/valid

# 2) verify the CI job treats "validator accepts fixtures" as PASS
# <test-command>
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| N/A | N/A | N/A |

## ⚖ FAIR+CARE & Governance

### Review gates
- Fixture changes: review by CI/workflow maintainers.
- Canonical contract changes: review by API maintainers + any governance reviewers required for public-facing endpoints.

### CARE / sovereignty considerations
- Fixtures should not include culturally sensitive site coordinates, community-restricted knowledge, or any information requiring consent controls.

### AI usage constraints
- Ensure the doc’s AI permissions/prohibitions match intended use (see front-matter).
- Do not use AI to infer or invent sensitive locations for fixture content.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial README for valid API contract fixtures | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

