---
title: "GitHub Actions — Security Fixtures"
path: ".github/actions/fixtures/security/README.md"
version: "v1.0.0"
last_updated: "2025-12-22"
status: "active"
doc_kind: "Readme"
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

doc_uuid: "urn:kfm:doc:ci:fixtures:security-readme:v1.0.0"
semantic_document_id: "kfm-ci-fixtures-security-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:ci:fixtures:security-readme:v1.0.0"
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

# GitHub Actions — Security Fixtures

## 📘 Overview

### Purpose

- Provide **safe, synthetic fixtures** used by GitHub Actions workflows/actions to validate security-related CI checks (e.g., secret-leak detection behavior, allow/deny path rules, scanner configuration).
- Establish **non-negotiable rules** for what may (and may not) be committed under `.github/actions/fixtures/security/`.

### Scope

| In Scope | Out of Scope |
|---|---|
| Synthetic test inputs for security checks (fixtures) | Any real credentials, API keys, tokens, private cert material |
| Documentation describing fixture intent and constraints | Production config, deploy secrets, or environment files |
| Deterministic, reviewable changes that improve CI coverage | Sensitive personal data (PII), culturally sensitive locations, or real-world incident data |

### Audience

- Primary: Maintainers editing CI workflows/actions and security scanning configuration.
- Secondary: Contributors adding/updating fixture scenarios; reviewers validating that fixtures are safe.

### Definitions (link to glossary)

- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Fixture**: A committed file used as deterministic input for tests/CI checks.
  - **Sentinel string**: A clearly fake marker used to emulate a risky pattern without being usable.
  - **Security scan**: A CI step that searches for leaked secrets or insecure patterns.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `.github/actions/fixtures/security/README.md` | Repo maintainers | Governs fixture safety rules |
| Security fixtures directory | `.github/actions/fixtures/security/` | CI maintainers | Fixture files live here |
| Security policy (if present) | `.github/SECURITY.md` | Security maintainers | Reporting + policy reference |
| Security standards docs (if present) | `docs/security/` | Security maintainers | Technical standards & guidance |
| CI workflows | `.github/workflows/` | CI maintainers | Workflows that may consume these fixtures |
| Composite actions | `.github/actions/` | CI maintainers | Actions that may reference fixtures |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] Fixture safety rules clearly stated (no real secrets/PII)
- [ ] Any repo-specific workflow/action references are accurate (add links when known)
- [ ] Validation steps listed and repeatable (even if commands are placeholders)
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document

- `path`: `.github/actions/fixtures/security/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| CI workflows | `.github/workflows/` | GitHub Actions workflow definitions |
| Composite actions | `.github/actions/` | Reusable actions consumed by workflows |
| Security fixtures | `.github/actions/fixtures/security/` | Synthetic security test inputs |
| Security policy | `.github/SECURITY.md` | Vulnerability reporting & project policy |
| Governed docs | `docs/` | Canonical governed documentation |
| Governance | `docs/governance/` | Ethics, sovereignty, review gates |

### Expected file tree for this sub-area

~~~text
📁 .github/
├── 📁 actions/
│   ├── 📁 fixtures/
│   │   └── 📁 security/
│   │       ├── 📄 README.md
│   │       └── 📄 <fixture-files-live-here>   (e.g., *.txt, *.json, *.yaml)
│   └── 📁 <composite-actions-live-here>
└── 📁 workflows/
    └── 📄 <security-related-workflows-live-here>
~~~

## 🧭 Context

### Background

KFM’s documentation describes a CI posture where changes must pass repeatable gates (documentation checks, schema validation, graph/API/UI tests, and security scans) before merge/deploy. This directory exists to provide deterministic **fixture inputs** for those security-oriented checks so they can be tested and reviewed like any other artifact.

### Assumptions

- These fixtures are **test-only inputs** and are not shipped or deployed.
- Some fixtures may intentionally resemble risky patterns (to ensure scanners detect them), but they must remain **inert**:
  - never valid,
  - never issued by a real provider,
  - never tied to real identities or locations.
- Workflow-specific behavior (e.g., allowlists, expected-failure logic) is defined in `.github/workflows/` or `.github/actions/` and should be referenced here once confirmed.

### Constraints / invariants

- **No real secrets. Ever.** Do not commit provider-issued keys, tokens, passwords, private keys, certs, or `.env` files.
- **No PII.** Do not include real names, emails, addresses, phone numbers, or user IDs.
- **No culturally sensitive or restricted locations.** Fixtures must not embed precise sensitive sites; use fictional or generalized placeholders.
- Preserve KFM system invariants:
  - ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode is preserved.
  - Frontend consumes contracts via APIs (no direct graph dependency).

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Which workflow(s)/action(s) consume these fixtures today? | TBD | TBD |
| Do any scanners need a path allowlist/denylist for this directory? | TBD | TBD |
| Should fixtures be split by tool (secret-scan vs dependency-scan vs SAST)? | TBD | TBD |

### Future extensions

- Add subfolders by scan type (example: `secrets/`, `deps/`, `sast/`) if the fixture set grows.
- Add a small index file (example: `manifest.yaml`) describing fixture intent (requires governance review if introduced).

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  PR[Pull Request] --> CI[GitHub Actions Workflow]
  CI --> Checkout[Checkout Repo]
  Checkout --> Scan[Security Check Step]
  Scan --> Fixtures[Read Fixtures: .github/actions/fixtures/security/]
  Scan --> Report[Logs / Findings / Artifacts]
  Report --> Gate[Pass/Fail Gate]
~~~

### Optional: sequence diagram

~~~mermaid
sequenceDiagram
  participant Dev as Contributor
  participant CI as GitHub Actions
  participant Scan as Security Step
  participant Fx as Security Fixtures

  Dev->>CI: Open PR / push commit
  CI->>Scan: Run security checks
  Scan->>Fx: Load fixture inputs (read-only)
  Scan-->>CI: Findings + exit code
  CI-->>Dev: Status (pass/fail) + logs
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Fixture files | Text / JSON / YAML | This directory | Must be synthetic; no real secrets/PII; reviewed via CI + code review |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| CI logs / annotations | GitHub Actions logs | CI run output | GitHub Actions conventions |
| Security reports (if configured) | e.g., SARIF / JSON | CI artifacts | Tool-specific (not defined here) |

### Sensitivity & redaction

- Fixtures must remain **public/open** safe. If a fixture’s content could be plausibly mistaken for a real credential or sensitive datum, revise it to use an unmistakable sentinel string (example: `KFM_TEST_ONLY_DO_NOT_USE`) and update the related test configuration.

### Quality signals

- Deterministic, minimal fixtures (small, easy to review).
- Clear naming + headers describing why the fixture exists.
- No accidental triggering of downstream deploy steps (fixtures are inputs only).

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Collections involved: N/A (CI fixtures are not catalog artifacts)
- Items involved: N/A
- Extension(s): N/A

### DCAT

- Dataset identifiers: N/A
- License mapping: N/A
- Contact / publisher mapping: N/A

### PROV-O

- `prov:wasDerivedFrom`: N/A
- `prov:wasGeneratedBy`: N/A
- Activity / Agent identities: N/A

### Versioning

- Fixtures follow repository version control. If fixture meaning changes, treat it as a breaking change for any dependent CI checks and update workflows accordingly.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| CI workflow | Orchestrates security checks | `.github/workflows/*.yml` |
| Composite action (optional) | Encapsulates scan logic | `.github/actions/<action>/action.yml` |
| Security fixtures | Deterministic test inputs | File paths under this directory |
| KFM pipeline (context) | Produces governed artifacts | ETL → catalogs → graph → APIs → UI → stories |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| Fixture safety contract | This README | Review required for changes |
| Workflow configuration | `.github/workflows/` | Update with fixture changes |
| Action inputs/outputs (if applicable) | `.github/actions/` | Keep backward compatibility where possible |

### Extension points checklist (for future work)

- [ ] Add a new fixture file with a short header comment explaining intent
- [ ] Update workflows/actions that consume fixtures
- [ ] Confirm fixtures remain synthetic (no secrets/PII)
- [ ] Add/adjust CI expectations (pass/fail/allowlist) with reviewer sign-off
- [ ] Update this README if new fixture categories are introduced

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- Indirect only: Security fixtures help ensure the CI gate is consistently validating security checks, which protects the integrity of artifacts that eventually support Story Nodes and Focus Mode.

### Provenance-linked narrative rule

- N/A for fixtures. Fixtures must not be used as evidence sources.

### Optional structured controls

~~~yaml
# N/A — this directory is CI-only and should not define Focus Mode controls.
~~~

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks (if this repo enforces them on all `.md`)
- [ ] Security scan configuration sanity checks (as applicable)
- [ ] Ensure fixtures do not contain real secrets/PII (review + automated scans)
- [ ] Ensure workflows that consume fixtures behave as intended (expected pass/fail)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) Run the repo’s CI/security checks locally (if supported)
# 2) Or run the relevant GitHub Actions workflow in a PR branch
# 3) Inspect logs/artifacts to confirm fixture behavior is as intended
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| Security scan findings count | CI workflow output | `docs/telemetry/` + `schemas/telemetry/` (if implemented) |
| Fixture coverage (scenarios) | Repo inventory | `docs/telemetry/` (optional) |

## ⚖ FAIR+CARE & Governance

### Review gates

- Changes under `.github/actions/fixtures/security/` should receive **security-aware review** because they can affect how scanners behave and what the CI gate validates.

### CARE / sovereignty considerations

- Fixtures must not include real community identifiers, culturally sensitive sites, or restricted knowledge. Use fictional placeholders and generalized geography where needed.

### AI usage constraints

- Ensure this document’s AI permissions/prohibitions match intended use (see front-matter).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial README for security fixtures | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
