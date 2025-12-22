---
title: "GitHub Actions Fixtures — API Contracts (README)"
path: ".github/actions/fixtures/api_contracts/README.md"
version: "v1.0.0"
last_updated: "2025-12-22"
status: "draft"
doc_kind: "CI Fixture README"
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

doc_uuid: "urn:kfm:doc:github-actions:fixtures:api-contracts:readme:v1.0.0"
semantic_document_id: "kfm-github-actions-fixtures-api-contracts-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github-actions:fixtures:api-contracts:readme:v1.0.0"
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

# GitHub Actions Fixtures — API Contracts

## 📘 Overview

### Purpose
- Provide **static, deterministic fixture inputs** for CI workflows / GitHub Actions that validate **API contract tooling**.
- Ensure contract validation logic can be tested without depending on the full application runtime.
- Clarify the separation between **canonical contracts** and **fixtures**:
  - **Canonical API contracts:** `src/server/contracts/`
  - **Action/test fixtures:** `.github/actions/fixtures/api_contracts/` (this folder)

### Scope
| In Scope | Out of Scope |
|---|---|
| Minimal contract examples (OpenAPI / GraphQL), plus any expected outputs needed for CI tests | Authoritative API contract definitions (these live under `src/server/contracts/`) |
| Fixture maintenance rules (sync, redaction, determinism) | API implementation code, endpoint behavior, and business logic |
| Documentation for contributors touching CI contract validation | Governance policy authoring (see `docs/governance/*`) |

### Audience
- Primary: Maintainers working on CI workflows and GitHub Actions that lint/validate API contracts.
- Secondary: API maintainers who need to update fixtures when canonical contracts change.

### Definitions (link to glossary)
- **Contract artifact:** machine-validated spec (e.g., OpenAPI, GraphQL schema).
- **Fixture:** a static “golden” test input used by CI to validate tooling behavior.
- **Canonical home:** the single authoritative location for a subsystem’s primary artifacts.

(Glossary reference: `docs/glossary.md` — *not confirmed in repo; add if missing*.)

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Canonical API contracts | `src/server/contracts/` | API maintainers | Must validate in CI; do not duplicate elsewhere |
| Fixture contracts (this folder) | `.github/actions/fixtures/api_contracts/` | CI maintainers | Used for deterministic tests of contract tooling |
| Master Guide | `docs/MASTER_GUIDE_v12.md` | Core maintainers | Defines canonical pipeline & invariants |
| Redesign blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture / governance | “Contracts are canonical” + CI expectations |
| API contract template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API maintainers | Use for API contract changes (not for fixtures) |

### Definition of done (for this document)
- [ ] This README exists and explains what belongs here.
- [ ] Contributors can tell **what is canonical** vs **what is fixture-only**.
- [ ] Fixtures are **non-sensitive**, deterministic, and validate with the same tooling CI uses.
- [ ] A repeatable update pattern is documented (see “Validation & CI/CD”).

## 🗂️ Directory Layout

### This document
- `path`: `.github/actions/fixtures/api_contracts/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Canonical API home | `src/server/` | API code + contract validation boundary |
| Canonical API contracts | `src/server/contracts/` | OpenAPI/GraphQL specs (authoritative) |
| API docs (human-readable) | `docs/api/` | *Not confirmed in repo; expected location for rendered docs* |
| CI workflows | `.github/workflows/` | Workflow definitions that call actions/validators |
| Composite actions | `.github/actions/` | Reusable actions that may consume these fixtures |

### Expected file tree for this sub-area
~~~text
📁 .github/
└── 📁 actions/
    └── 📁 fixtures/
        └── 📁 api_contracts/
            ├── 📄 README.md
            ├── 📁 openapi/         # optional: OpenAPI YAML/JSON fixtures
            ├── 📁 graphql/         # optional: GraphQL SDL fixtures
            └── 📁 snapshots/       # optional: expected outputs (lint reports, diffs)
~~~

> Note: `openapi/`, `graphql/`, and `snapshots/` are recommended conventions. If your action/tooling expects a different structure, document it here and keep fixtures consistent.

## 🧭 Context

### Background
KFM is designed as a **contract-first** system with a strict pipeline ordering:
**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**.

Within that, API contracts are first-class artifacts and are expected to validate in CI. This fixture directory exists to make CI validation of *contract tooling* stable and reproducible, even as real contracts evolve.

### Assumptions
- CI includes at least one workflow or composite action that validates API contracts and can be pointed at fixture files.
- Fixtures are allowed to be **minimal subsets** (they do not need to represent the full production contract surface).

### Constraints / invariants
- **Fixtures are never canonical.** Do not treat this folder as a source-of-truth for API contracts.
- **No sensitive content:** do not include secrets, credentials, private URLs, or restricted location details.
- **Deterministic:** fixtures must be stable over time (avoid timestamps, randomized IDs, or environment-dependent outputs).
- **Match supported contract dialects:** keep fixture syntax aligned with whatever the repo’s validators support (OpenAPI version, GraphQL SDL conventions, etc.).

### Open questions
- Which specific workflow(s) or composite action(s) consume these fixtures? (*not confirmed in repo*)
- Is there an existing sync script (e.g., under `tools/`) that copies canonical contracts into fixtures for testing? (*not confirmed in repo*)

### Future extensions
- Add a small sync utility (example: `tools/ci/sync_api_contract_fixtures.*`) that:
  - Copies a curated subset of canonical contracts from `src/server/contracts/`
  - Redacts/normalizes as needed
  - Updates `snapshots/` deterministically
- Add a CI check to ensure fixtures remain valid and do not drift unexpectedly.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  Dev[Developer changes] --> Canon[Canonical contracts<br/>src/server/contracts]
  Canon --> CI[CI contract validation]
  CI --> Action[GitHub Action / validator tooling]
  Action --> Fixtures[Fixtures<br/>.github/actions/fixtures/api_contracts]
  Action --> Report[Pass/Fail + reports]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant Dev as Developer
  participant CI as CI Workflow
  participant Act as Action/Validator
  participant Fix as Fixture Contracts
  participant Can as Canonical Contracts

  Dev->>CI: push PR
  CI->>Act: run contract validation
  Act->>Fix: load fixtures (self-test)
  Act->>Can: validate canonical contracts
  Act-->>CI: results (pass/fail)
  CI-->>Dev: status checks
~~~

## 📦 Data & Metadata

### Inputs
- Contract fixture files (expected):
  - OpenAPI YAML/JSON (if applicable)
  - GraphQL schema SDL (if applicable)
- Optional expected outputs:
  - Lint reports
  - Snapshot diffs
  - Structured validation summaries (JSON)

### Outputs
- CI pass/fail signal for contract tooling validation.
- Optional artifacts:
  - validation reports
  - logs
  - snapshots

### Sensitivity & redaction
- Keep fixtures **synthetic** and **non-sensitive**.
- If fixtures mirror real endpoints, ensure they do not reveal restricted location data or governance-restricted attributes.

### Quality signals
- Fixtures parse cleanly (YAML/JSON/SDL syntax valid).
- Fixtures validate with the repo’s contract validators.
- Fixture updates are reviewed and do not introduce nondeterminism.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Not directly applicable: fixtures here are for API contracts, not catalog artifacts.
- If fixtures include example API payloads, prefer payload fragments that reference stable STAC IDs (where helpful) rather than embedding full datasets.

### DCAT
- Not directly applicable, except as referenced identifiers in example payloads.

### PROV-O
- Not directly applicable, except as referenced identifiers in example payloads.

### Versioning
- Fixtures should track canonical contract evolution, but should not be used to version the API itself.
- API versioning (e.g., v1/v2) is governed by the canonical contracts under `src/server/contracts/` and related docs.

## 🧱 Architecture

### Components
| Component | Role | Canonical location |
|---|---|---|
| Canonical contracts | Source-of-truth specs | `src/server/contracts/` |
| CI workflows | Invoke validation gates | `.github/workflows/` |
| GitHub Actions / validators | Implement contract checks | `.github/actions/` and/or `tools/` |
| Fixture contracts | Deterministic action/tooling inputs | `.github/actions/fixtures/api_contracts/` |

### Interfaces / contracts
- Fixture file formats must align with whatever the validator expects:
  - OpenAPI YAML/JSON (version depends on repo validators)
  - GraphQL SDL (if applicable)
- If a validator/action expects specific filenames or directory structure, document that contract here and keep it stable.

### Extension points checklist (for future work)
- [ ] Add a new fixture contract: place in the appropriate subfolder and document intent.
- [ ] If validator expectations change (input names, directory layout), update this README and adjust CI tests.
- [ ] If canonical contracts change, evaluate whether fixture updates are needed to cover new validation behavior.
- [ ] Keep fixtures redacted and deterministic; re-run validations before merging.

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Indirect: API contracts are the boundary that the UI (including Focus Mode) relies on.
- Keeping contract validation strong helps ensure Focus Mode receives stable, provenance-friendly payloads.

### Provenance-linked narrative rule
- Fixtures must not be used to justify narrative claims; they are CI artifacts only.
- Narrative content must be provenance-linked via Story Nodes and evidence artifacts.

### Optional structured controls
- N/A for this directory (fixtures are not user-facing).

## 🧪 Validation & CI/CD

### Validation steps
- CI should validate:
  - Fixture syntax (YAML/JSON/SDL)
  - Fixture contract validity (same validators used for canonical contracts)
  - Determinism (no environment-dependent outputs)
- Local reproduction (*not confirmed in repo*):
  - Run the same validator commands used in CI (see `.github/workflows/` and/or `tools/`).
  - Optionally run workflows locally using a GitHub Actions runner emulator (e.g., `act`) if the repo supports it.

### Reproduction
- Identify which workflow/job consumes these fixtures by searching the repo for:
  - `fixtures/api_contracts`
  - `.github/actions/fixtures/api_contracts`
- Run that workflow’s underlying validation commands locally (if exposed).

### Telemetry signals (if applicable)
- N/A (fixtures are static CI inputs).
- If CI emits validation summaries, consider storing them as build artifacts rather than committing large logs.

## ⚖ FAIR+CARE & Governance

### Review gates
- Fixture changes: review by CI/workflow maintainers.
- Canonical contract changes: review by API maintainers + any governance reviewers required for public-facing endpoints.

### CARE / sovereignty considerations
- Do not include restricted or culturally sensitive location details in fixtures.
- Do not include data that would violate sovereignty rules; keep fixtures synthetic.

### AI usage constraints
- Follow the front-matter AI transform permissions/prohibitions for this document.
- Do not use AI tooling to infer sensitive locations or to generate governance policy content.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial README for API contract fixtures | TBD |

---

Footer refs:
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Redesign Blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
