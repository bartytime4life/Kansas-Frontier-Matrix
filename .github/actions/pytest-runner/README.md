---
title: "GitHub Action — pytest-runner"
path: ".github/actions/pytest-runner/README.md"
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

doc_uuid: "urn:kfm:doc:github:actions:pytest-runner:readme:v1.0.0"
semantic_document_id: "kfm-github-actions-pytest-runner-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github:actions:pytest-runner:readme:v1.0.0"
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
This document governs the local GitHub Action located at `.github/actions/pytest-runner/` that runs the repository’s Python test suite using `pytest` as a CI gate.

The action is intended to support KFM’s pipeline invariants by ensuring code changes do not break:
- ETL and normalization logic
- STAC/DCAT/PROV catalog build utilities and validators
- graph build/integrity tooling
- API contract behavior (where tests exist)
- UI-adjacent Python tooling (if applicable)

### Scope

| In Scope | Out of Scope |
|---|---|
| Running `pytest` in CI with repo-standard arguments | Deployments (Pages, releases, infra) |
| Installing Python dependencies needed for tests | Running non-Python test frameworks |
| Producing CI-friendly outputs (e.g., junit/coverage) *if implemented* | Performing data writes to `data/` or publishing catalogs |
| Providing a stable interface for workflows to invoke tests | Any privileged operations requiring secrets by default |

### Audience
- Primary: maintainers of CI/CD and Python code paths (`src/`, `tests/`, `tools/`)
- Secondary: contributors writing or updating tests; reviewers validating PR health

### Definitions (link to glossary)
- Link: `docs/glossary.md` *(not confirmed in repo)*
- Terms used in this doc: `pytest`, `junit`, `coverage`, `composite action`, `workflow`

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Action definition | `.github/actions/pytest-runner/action.yml` | CI maintainers | *(not confirmed in repo — expected for a local action)* |
| This README | `.github/actions/pytest-runner/README.md` | CI maintainers | Governed doc (this file) |
| Python tests | `tests/` | Code owners | Exact layout varies *(not confirmed in repo)* |
| Pytest config | `pytest.ini` / `pyproject.toml` | Code owners | *(not confirmed in repo)* |

### Definition of done (for this document)
- [ ] Front-matter complete + valid (`path` matches repo path)
- [ ] Action intent + usage is documented with a stable interface (inputs/outputs)
- [ ] Reproduction steps are documented for local runs
- [ ] Security and sovereignty considerations are explicitly stated
- [ ] Any “expected” behavior that is not implemented is clearly marked *(not confirmed in repo)*

## 🗂️ Directory Layout

### This document
- `path`: `.github/actions/pytest-runner/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| GitHub workflows | `.github/workflows/` | Workflow entrypoints that call this action *(not confirmed in repo)* |
| Action implementations | `.github/actions/` | Local composite actions used by workflows |
| Python code | `src/` | ETL/catalog/graph/api libs (repo-dependent) |
| Tests | `tests/` | Pytest tests and fixtures *(not confirmed in repo)* |
| Schemas | `schemas/` | JSON schemas for catalogs/telemetry *(not confirmed in repo)* |

### Expected file tree for this sub-area
~~~text
📁 .github/
└── 📁 actions/
    └── 📁 pytest-runner/
        ├── 📄 README.md
        ├── 📄 action.yml                 # not confirmed in repo (expected)
        ├── 📁 scripts/                   # not confirmed in repo (optional)
        │   └── 📄 run_pytest.sh           # not confirmed in repo (optional)
        └── 📁 config/                    # not confirmed in repo (optional)
            └── 📄 pytest.ini              # not confirmed in repo (optional)
~~~

## 🧭 Context

### Background
KFM relies on deterministic, repeatable processing and strict contracts across its pipeline. A reliable Python test gate is a baseline safeguard that prevents regressions from reaching catalog, graph, API, or UI layers.

### Assumptions
- Python is used for some portion of KFM (ETL/catalog tooling/tests) *(not confirmed in repo)*
- The repository uses `pytest` for test execution *(not confirmed in repo)*
- Tests can run in CI without accessing restricted secrets by default

### Constraints / invariants
- Canonical pipeline ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- Frontend must consume data through APIs (no direct graph access).
- CI must not leak secrets or sensitive content via logs/artifacts.
- Prefer deterministic tests (seed randomness; stable fixtures) where relevant.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Supported Python versions in CI? | TBD | TBD |
| Dependency install method (pip/poetry/uv)? | TBD | TBD |
| Should coverage be required for merge? | TBD | TBD |
| Do we publish junit/coverage artifacts on PRs? | TBD | TBD |

### Future extensions
- Add matrix testing across Python versions and OS runners *(requires human review for cost/coverage tradeoffs)*
- Add contract tests for API schemas and schema validation utilities
- Add smoke tests for core pipeline commands

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  PR[Pull Request] --> WF[GitHub Workflow]
  WF --> ACT[Local action: pytest-runner]
  ACT --> PY[Python env + deps]
  PY --> T[pytest execution]
  T --> R[Test reports / coverage (optional)]
  T --> G[Required status check]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant Dev as Contributor
  participant GH as GitHub Actions
  participant A as pytest-runner
  participant Py as Python/pytest

  Dev->>GH: Open PR / push commit
  GH->>A: uses: ./.github/actions/pytest-runner
  A->>Py: install deps + run pytest
  Py-->>A: exit code + (optional) junit/coverage files
  A-->>GH: step success/failure + artifacts (optional)
  GH-->>Dev: PR check status
~~~

## 📦 Data & Metadata

### Inputs
> The inputs below define the **recommended contract** for this action. If the corresponding keys are not implemented in `action.yml`, treat this section as **not confirmed in repo** and align to the actual `action.yml`.

| Input | Format | Where from | Validation |
|---|---|---|---|
| `python-version` | string | workflow `with:` | must be a valid Python semver string |
| `working-directory` | string | workflow `with:` | must exist in repo |
| `requirements-file` | string | workflow `with:` | file exists if provided |
| `pytest-args` | string | workflow `with:` | sanitized; no secret echo |
| `report-junit-path` | string | workflow `with:` | path under workspace |
| `coverage` | boolean | workflow `with:` | true/false |
| `coverage-xml-path` | string | workflow `with:` | path under workspace |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| junit report | XML | `report-junit-path` | junit format *(not confirmed in repo)* |
| coverage report | XML | `coverage-xml-path` | cobertura/coverage.py *(not confirmed in repo)* |

### Sensitivity & redaction
- Test fixtures and artifacts must not contain secrets, credentials, or sensitive locations.
- If any datasets used in tests contain restricted coordinates, prefer synthetic fixtures or generalized geometry.

### Quality signals
- Stable, deterministic tests: avoid time-sensitive assertions; seed randomness when applicable.
- Clear failure modes: failing tests should point to actionable stack traces.

## 🌐 STAC, DCAT & PROV Alignment

Although this action is not itself a catalog generator, it **supports** catalog integrity by running tests that may validate:
- STAC JSON schema conformance and Item/Collection integrity *(if tests exist)*
- DCAT mapping logic *(if tests exist)*
- PROV generation logic *(if tests exist)*

If such tests are present, they should be explicit and named so failures clearly indicate which contract broke.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| pytest-runner action | Orchestrate pytest in CI | `uses: ./.github/actions/pytest-runner` |
| Python toolchain | Install dependencies + run tests | `python -m pytest ...` |
| Reports (optional) | Produce machine-readable CI artifacts | junit/coverage files |

### Interfaces / contracts
#### Recommended action interface (expected)
If this is a composite action, workflows should call it as:

~~~yaml
- name: Run pytest
  uses: ./.github/actions/pytest-runner
  with:
    python-version: "3.11"
    working-directory: "."
    requirements-file: "requirements.txt"
    pytest-args: "-q"
    report-junit-path: "artifacts/junit.xml"
    coverage: true
    coverage-xml-path: "artifacts/coverage.xml"
~~~

> NOTE: The exact input names must match `.github/actions/pytest-runner/action.yml` *(not confirmed in repo)*.

### Extension points checklist (for future work)
- [ ] Add test matrix (py versions / OS) with bounded cost
- [ ] Add artifact upload step gated on PR context
- [ ] Add caching strategy (pip/uv/poetry) with lockfile pinning
- [ ] Add “changed-paths” optimization to skip tests only when safe *(requires human review)*

## 🧠 Story Node & Focus Mode Integration

This action does not directly surface in Story Nodes or Focus Mode. Indirectly, it protects those layers by preventing regressions in upstream pipeline components that generate and serve narrative artifacts.

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Action interface documented (inputs/outputs)
- [ ] Local reproduction steps documented
- [ ] No secrets required by default
- [ ] Logs do not echo sensitive env vars
- [ ] Fails fast on test failure (non-zero exit)

### Reproduction
~~~bash
# Local run (example — adjust to repo layout)
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -r requirements.txt  # or requirements-dev.txt (not confirmed in repo)
python -m pytest -q
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| test pass/fail | pytest exit code | GitHub check run |
| junit report | pytest plugin | artifacts (optional) |
| coverage % | coverage.py | artifacts (optional) |

## ⚖ FAIR+CARE & Governance

### Review gates
- CI maintainers: review any action interface changes
- Security review: required if introducing secrets, elevated permissions, or artifact publishing
- Data governance review: required if tests begin using restricted datasets or sensitive locations

### CARE / sovereignty considerations
- Avoid embedding or exporting sensitive locations in test snapshots or fixtures.
- Prefer synthetic/generic fixtures for restricted content.

### AI usage constraints
- This README inherits repo governance and must not imply prohibited AI actions (e.g., inferring sensitive locations).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial governed README for pytest-runner action | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`