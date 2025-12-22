---
title: "API Contract Fixtures — Invalid Cases"
path: ".github/actions/fixtures/api_contracts/invalid/README.md"
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

doc_uuid: "urn:kfm:doc:ci:fixtures:api-contracts:invalid-readme:v1.0.0"
semantic_document_id: "kfm-ci-fixtures-api-contracts-invalid-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:ci:fixtures:api-contracts:invalid-readme:v1.0.0"
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

# API Contract Fixtures — Invalid Cases

## 📘 Overview

### Purpose

- This directory holds **intentionally invalid** API contract fixtures used to verify that contract validators **fail when they should** (negative testing).
- These files are not examples to copy into production contracts; they exist to prevent validator regressions.

### Scope

| In Scope | Out of Scope |
|---|---|
| Minimal “known-bad” contract specimens (syntax errors, missing required fields, invalid refs, etc.) | Any production contract source-of-truth |
| Deterministic, offline fixtures that can run in CI | Fixtures requiring network calls, external services, or secrets |
| One failure mode per fixture (preferred) | Huge “kitchen sink” fixtures that are hard to diagnose |

### Audience

- Primary: CI / validation maintainers; API contract maintainers
- Secondary: contributors adding or changing validators, schema rules, or contract formats

### Definitions (link to glossary)

- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Fixture**: a small file used in tests to exercise a validator/contract rule.
  - **Invalid fixture**: a fixture that must be rejected by the validator.
  - **Negative test**: a test that passes only when the validator fails on known-bad inputs.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Invalid contract fixtures | `.github/actions/fixtures/api_contracts/invalid/` | CI maintainers | This directory |
| Fixture root (context) | `.github/actions/fixtures/api_contracts/` | CI maintainers | See sibling README (if present) |
| Contract validation workflow(s) | `.github/workflows/` | CI maintainers | Exact workflow name not confirmed in repo |
| API contract sources | `src/server/` | API maintainers | Canonical home in KFM design; exact layout not confirmed in repo |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] Clear explanation of why invalid fixtures exist and how they are used
- [ ] Guidance for adding new invalid fixtures (naming + single-failure principle)
- [ ] Validation steps listed and repeatable (even if placeholders)
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document

- `path`: `.github/actions/fixtures/api_contracts/invalid/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| CI / GitHub automation | `.github/` | Workflows and composite actions |
| Contract fixtures | `.github/actions/fixtures/api_contracts/` | Fixture root for API-contract validation |
| Invalid fixtures | `.github/actions/fixtures/api_contracts/invalid/` | Known-bad fixtures (must fail validation) |
| API boundary | `src/server/` | API implementations + contracts (OpenAPI/GraphQL), consumed by UI via APIs |
| Schemas | `schemas/` | JSON Schemas / other interface schemas |
| Documentation | `docs/` | Canonical governed docs + templates |

### Expected file tree for this sub-area

~~~text
📁 .github/
└── 📁 actions/
    └── 📁 fixtures/
        └── 📁 api_contracts/
            └── 📁 invalid/
                ├── 📄 README.md
                └── 📁 <contract_type>/
                    ├── 📄 <id>__<short_reason>.<ext>
                    └── 📄 <id>__<short_reason>.<ext>
~~~

Notes:
- `<contract_type>` is intentionally generic (e.g., `openapi/`, `graphql/`, `jsonschema/`) because supported formats are **not confirmed in repo**.
- Prefer **stable** file names (don’t encode timestamps) so CI expectations remain deterministic.

## 🧭 Context

### Background

Contract validators can regress in subtle ways (e.g., rules removed, resolution behavior changes, “warn only” inadvertently enabled). Invalid fixtures ensure CI catches regressions by asserting:

- The validator still rejects known-bad inputs.
- Rejection remains deterministic and debuggable (small fixtures, one failure mode).

### Assumptions

- A CI job exists that runs contract validation and uses these fixtures as negative tests. (Inferred from directory placement; exact wiring is not confirmed in repo.)
- A “negative test” run is considered successful when the validator **rejects** these fixtures.

### Constraints / invariants

- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode is preserved.
- Frontend consumes contracts via APIs (no direct graph dependency).
- Invalid fixtures MUST NOT include secrets, API keys, private tokens, or real PII.
- Keep fixtures minimal and deterministic:
  - Prefer one clear violation per file.
  - Avoid reliance on validator error-message wording unless the harness explicitly checks it.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Which contract formats are validated (OpenAPI, GraphQL SDL, etc.)? | CI maintainers | TBD |
| Does CI assert only “fails”, or also expected error codes/messages? | CI maintainers | TBD |
| Are `.github/**.md` files subject to Markdown protocol lint in CI? | CI maintainers | TBD |

### Future extensions

- Add a subfolder per contract format if/when new validators are introduced.
- Optionally add a tiny “index” or manifest if the harness benefits from explicit enumeration (not confirmed in repo).

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  Dev[Contributor] --> PR[Pull Request]
  PR --> CI[GitHub Actions CI]

  CI --> Validator[Contract validator: action or script]
  CI --> Fixtures[Invalid fixtures: api_contracts/invalid]
  Fixtures --> Validator

  Validator --> Result{Expected outcome?}
  Result -->|Rejected = PASS| OK[CI check passes]
  Result -->|Accepted = REGRESSION| Fail[CI check fails]
~~~

### Optional: canonical pipeline reminder

~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React/Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Invalid contract fixtures | YAML/JSON/SDL/etc. | `.github/actions/fixtures/api_contracts/invalid/**` | Must be rejected by validator |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| CI validation result | pass/fail + logs | GitHub Actions logs / annotations | N/A |
| Regression signal | PR status check | GitHub PR checks | N/A |

### Sensitivity & redaction

- These fixtures should be **public-safe** by default.
- Do not include real person names, emails, phone numbers, precise sensitive locations, or any access tokens.

### Quality signals

- Deterministic failure (no flakiness)
- Minimal reproduction: each fixture targets one rule/violation
- Stable naming: unchanged file names unless the associated rule meaning changes

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Not applicable: this directory does not define STAC Items/Collections.

### DCAT

- Not applicable: this directory does not define dataset catalog entries.

### PROV-O

- Not applicable: this directory does not define provenance bundles.

### Versioning

- Fixtures should evolve alongside validator rules:
  - If a validator’s expectations change intentionally, update the corresponding fixture(s) and any CI harness expectations in the same PR.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Contract fixtures (this dir) | Provide negative test inputs | File system |
| Contract validator (CI) | Reject invalid inputs | CLI / action step |
| CI workflow | Gate merges on expected validator behavior | GitHub Actions |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| Invalid fixture set | `.github/actions/fixtures/api_contracts/invalid/` | Add fixtures when rules are added; keep deterministic names |
| API schemas (source contracts) | `src/server/` (+ docs) | Contract tests required; versioned APIs |
| JSON schemas (supporting) | `schemas/` | Semver + changelog |

### Extension points checklist (for future work)

- [ ] CI fixtures: add `<contract_type>/` folders as new formats are validated
- [ ] CI harness: ensure new invalid fixtures are enumerated and expected to fail
- [ ] Docs: link from fixture root README to each subfolder README (if added)

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- Indirectly: robust API contract validation reduces the chance that Focus Mode receives malformed payloads.

### Provenance-linked narrative rule

- Not applicable to fixtures, but the broader system rule still stands: every claim must trace to a dataset / record / asset ID.

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
- [ ] API contract tests (invalid fixtures must fail validation)
- [ ] Security checks (no secrets / no PII / no sensitive locations)
- [ ] Determinism check (repeat runs produce the same outcome)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) run the contract validator against invalid fixtures
# <validator-command> .github/actions/fixtures/api_contracts/invalid

# 2) verify CI logic treats "validator rejects fixtures" as PASS
# <test-command>
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| N/A | N/A | N/A |

## ⚖ FAIR+CARE & Governance

### Review gates

- Changes that alter what is considered “valid” vs “invalid” for public API contracts should be reviewed by API + CI maintainers.
- Any change that could weaken validation behavior is a security-relevant change and should receive extra review.

### CARE / sovereignty considerations

- Fixtures should not include culturally sensitive site coordinates, community-restricted knowledge, or any information requiring consent controls.

### AI usage constraints

- Ensure the doc’s AI permissions/prohibitions match intended use (see front-matter).
- Do not use AI to “guess” real sensitive locations for fixtures.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial README for invalid API contract fixtures | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

