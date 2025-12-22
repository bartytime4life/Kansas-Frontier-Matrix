---
title: "GitHub Action — pytest-runner"
path: ".github/actions/pytest-runner/README.md"
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

doc_uuid: "urn:kfm:doc:github-actions:pytest-runner:v1.0.0"
semantic_document_id: "kfm-github-action-pytest-runner-v1.0.0"
event_source_id: "ledger:kfm:doc:github-actions:pytest-runner:v1.0.0"
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

# GitHub Action — pytest-runner

## 📘 Overview

### Purpose

This document defines the intended contract and usage guidance for the reusable GitHub Action located at:

- `.github/actions/pytest-runner/`

The goal is to standardize how KFM runs Python unit tests (`pytest`) inside CI workflows, in line with “CI gate alignment” expectations (deterministic, validate-if-present, fail-if-invalid, skip-if-not-applicable behavior).

### Scope

| In Scope | Out of Scope |
|---|---|
| Setting up Python for CI | Deployments / releases |
| Installing Python dependencies for tests | Publishing packages |
| Running `pytest` with configurable args | Full infra provisioning |
| Optional caching (pip/uv/poetry, depending on implementation) | Security scanning / SAST (separate gates) |
| Optional generation of test artifacts (e.g., JUnit XML / coverage) | Long-running e2e tests that require external services |

### Audience

- Primary: CI maintainers + contributors who need consistent test behavior.
- Secondary: Governance / reviewers auditing validation expectations.

### Definitions (link to glossary)

- Link: `docs/glossary.md`
- Terms used in this doc:
  - **CI gate**
  - **deterministic**
  - **contract artifact**
  - **validate-if-present / fail-if-invalid / skip-if-not-applicable**

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Action implementation | `.github/actions/pytest-runner/action.yml` | CI maintainers | Required for use (not confirmed in repo) |
| This README | `.github/actions/pytest-runner/README.md` | CI maintainers | Keep in sync with `action.yml` |
| Workflows calling the action | `.github/workflows/*.yml` | CI maintainers | Not confirmed in repo |
| Tests | `tests/` | Module owners | `pytest` discovers and runs these |
| Source code under test | `src/` | Module owners | May include pipelines/graph/server/web helpers |
| Security policy | `.github/SECURITY.md` | Maintainers | Disclosure and reporting process |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] README describes the **same inputs/behavior** as `.github/actions/pytest-runner/action.yml`
- [ ] Example workflow snippet is correct for this repo’s expected structure
- [ ] Security constraints are stated (fork PRs, secrets handling)
- [ ] Validation and reproduction steps are listed and repeatable

## 🗂️ Directory Layout

### This document

- `path`: `.github/actions/pytest-runner/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| GitHub Actions | `.github/workflows/` | Workflow entrypoints (CI gates) |
| Composite actions | `.github/actions/` | Reusable CI building blocks |
| Source code | `src/` | Pipelines, graph, API/server, etc. |
| Tests | `tests/` | Unit/contract tests run by `pytest` |
| Schemas | `schemas/` | Contract artifacts validated in CI (separate gates) |
| Docs | `docs/` | Canonical governed docs |
| Data | `data/` | Raw/work/processed + catalogs; tests should not mutate committed data |

### Expected subtree (pytest-runner)

~~~text
📁 .github/
└── 📁 actions/
    └── 📁 pytest-runner/
        ├── 📄 action.yml          # Composite action definition (not confirmed in repo)
        └── 📄 README.md           # This doc
~~~

## 🧭 Context

### Where this fits in KFM

KFM’s canonical ordering is:

**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

This action supports the **Validation & CI/CD** layer by running Python tests that protect contracts and invariants across those stages.

### Why use a reusable action

- Avoids “drift” where different workflows install deps / run tests differently.
- Enables consistent defaults (e.g., deterministic installs, consistent pytest args).
- Central place for security posture (especially around forks + secrets).

## 🗺️ Diagrams

~~~mermaid
sequenceDiagram
  participant W as Workflow Job
  participant A as pytest-runner
  participant P as Python Toolchain
  W->>W: Checkout repository
  W->>A: uses: ./.github/actions/pytest-runner
  A->>P: Setup Python + install deps
  A->>P: Run pytest
  P-->>W: Exit code + logs (+ optional artifacts)
~~~

## 📦 Data & Metadata

### Inputs

**Authoritative contract:** inputs MUST be defined in `.github/actions/pytest-runner/action.yml`.

Below is the *intended* minimum interface (update if `action.yml` differs):

| Input | Format | Where from | Validation |
|---|---|---|---|
| `python-version` | string | workflow `with:` | must be a valid `actions/setup-python` version string |
| `working-directory` | string | workflow `with:` | must exist in repo at runtime |
| `install-command` | string | workflow `with:` | MUST be a safe shell command (avoid untrusted interpolation) |
| `pytest-args` | string | workflow `with:` | treated as CLI args |
| `cache` | enum (`none`, `pip`) | workflow `with:` | optional; depends on implementation |

### Outputs

Composite actions may expose outputs, but many do not. If outputs are added, document them here and ensure `action.yml` declares them.

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| (optional) `cache-hit` | string/bool | n/a | mirror cache step output |

### Sensitivity & redaction

- Do **not** print secrets to logs.
- Avoid running this action in contexts where untrusted code can access privileged secrets.
- Tests that require restricted data must use **sanitized fixtures** and avoid embedding sensitive locations or identities.

### Quality signals

- Passing test suite (`pytest` exit code 0)
- Optional: coverage thresholds (if enforced by repository policy)
- Optional: JUnit XML for CI annotations

## 🌐 STAC, DCAT & PROV Alignment

This action does not directly generate STAC/DCAT/PROV artifacts. Indirectly, unit and contract tests may validate:

- STAC/DCAT/PROV schema conformance (if tests exist)
- Deterministic behavior of catalog generation code

If tests generate local catalogs as part of validation, they should write to ephemeral paths (e.g., temp dirs) or designated CI artifacts — not commit outputs.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Workflow caller | Selects runners + matrix strategy | `.github/workflows/*.yml` |
| `pytest-runner` action | Standardizes Python test execution | composite action inputs in `action.yml` |
| Python toolchain | Interpreter + pip/installer | `actions/setup-python` + install command |
| Repository tests | Assertions / contracts | `pytest` test discovery under `tests/` |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| Action contract | `.github/actions/pytest-runner/action.yml` | Semver this README + keep in sync |
| Test invocation standard | `.github/actions/pytest-runner/README.md` | Update alongside action changes |
| Repo structures referenced | `docs/MASTER_GUIDE_v12.md` | Follow canonical paths |

### Extension points checklist (for future work)

- [ ] Add a “requirements mode” input (e.g., `requirements-file`) if repo uses `requirements*.txt`
- [ ] Add a “project mode” input (e.g., editable install with extras) if repo uses `pyproject.toml`
- [ ] Add optional artifact generation (JUnit/coverage) and document paths
- [ ] Add caching strategy details (pip cache keys, lockfile hash)

## 🧠 Story Node & Focus Mode Integration

This action does not directly create Story Nodes or Focus Mode content.

Indirectly, it can help enforce Story Node rules by testing:
- provenance-link requirements in story node schemas (if tests exist)
- “no unsourced narrative” validation gates (if implemented elsewhere)

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks (front-matter/structure)
- [ ] `pytest-runner` README matches `action.yml` inputs/behavior
- [ ] Workflows that reference this action have deterministic behavior:
  - validate if present; fail if invalid; skip if not applicable
- [ ] Test suite passes for the intended Python version matrix

### Usage in a workflow (example)

~~~yaml
name: tests

on:
  pull_request:
  push:

jobs:
  pytest:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Run pytest via composite action
        uses: ./.github/actions/pytest-runner
        with:
          python-version: "3.11"
          working-directory: "."
          install-command: "python -m pip install -U pip && python -m pip install -e .[dev]"
          pytest-args: "-q"
          cache: "pip"
~~~

### Reproduction (local)

~~~bash
# Example placeholders — replace with repo-specific commands
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip

# Choose ONE install approach (depends on repo packaging)
# python -m pip install -r requirements-dev.txt
# python -m pip install -e ".[dev]"

pytest -q
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| CI pass/fail | GitHub Actions | workflow run logs |
| (optional) coverage % | pytest-cov | uploaded artifact / CI annotation |

## ⚖ FAIR+CARE & Governance

### Review gates

- Changes to `.github/actions/pytest-runner/` require review by CI maintainers.
- If test behavior changes could expose sensitive data (fixtures/logging), require governance review (see refs below).

### CARE / sovereignty considerations

- Ensure test fixtures do not leak culturally sensitive content or precise sensitive locations.
- Prefer generalized/sanitized fixtures for any restricted datasets.

### AI usage constraints

- Respect the front-matter `ai_transform_permissions` / `ai_transform_prohibited`.
- Do not use AI tooling to infer or reconstruct sensitive locations from redacted fixtures.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial pytest-runner README (contract + usage) | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
