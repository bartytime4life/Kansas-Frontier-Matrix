---
title: "KFM Repro Kit — Python Environment"
path: ".github/repro-kit/env/python/README.md"
version: "v1.0.0"
last_updated: "2025-12-30"
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

doc_uuid: "urn:kfm:doc:repro-kit:env:python:readme:v1.0.0"
semantic_document_id: "kfm-repro-kit-env-python-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:repro-kit:env:python:readme:v1.0.0"
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

# KFM Repro Kit — Python Environment

## 📘 Overview

### Purpose

- Define the **canonical, reproducible Python environment** used to run KFM’s Python-based tooling (pipelines, validators, QA, and supporting scripts).
- Reduce drift between developer machines and CI by standardizing **runtime selection**, **dependency pinning**, and **environment snapshotting** for provenance and replay.

> KFM invariants this README supports:
> - deterministic, replayable transforms (same inputs + same env → stable outputs)
> - contract-first validation (schemas + contracts are first-class artifacts)
> - provenance-first narrative (Focus Mode consumes provenance-linked context only)

### Scope

| In Scope | Out of Scope |
|---|---|
| Python runtime conventions (local + CI) | Infrastructure provisioning (cloud accounts, networks, secrets) |
| Dependency declaration + locking strategy | Non-Python environments (Node, Java, system DB installs) |
| Install + verification steps | Authoring ETL logic, graph migrations, UI implementation details |
| Environment snapshot rules for PROV/run logs | Deploy/run instructions for production services |

### Audience

- Primary: CI/Platform maintainers, pipeline maintainers, QA/validation maintainers.
- Secondary: contributors who run ETL/catalog/graph build steps locally.

### Definitions (link to glossary)

- Link: `docs/glossary.md` *(not confirmed in repo)*
- Terms used in this doc:
  - **Repro kit**: a small, repo-local set of conventions/files that make a workflow repeatable.
  - **Lockfile**: a fully pinned dependency set (preferably with hashes) used to recreate an identical environment.
  - **Environment snapshot**: recorded runtime details for a specific run (Python version, lock hash, installed packages).
  - **PROV activity**: the provenance record describing *what ran*, *with what inputs*, *under what software environment*.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `.github/repro-kit/env/python/README.md` | CI/Platform | Canonical Python environment guidance |
| Python env directory | `.github/repro-kit/env/python/` | CI/Platform | Home for lockfiles/specs for Python |
| Dependency spec (recommended) | `.github/repro-kit/env/python/requirements.in` | TBD | Human-edited dependency intent |
| Dependency lock (recommended) | `.github/repro-kit/env/python/requirements.lock` | TBD | Fully pinned install source |
| Master Guide (pipeline invariants) | `docs/MASTER_GUIDE_v12.md` | TBD | Pipeline order + contract-first norms |
| JSON schemas | `schemas/` | Standards | STAC/DCAT/PROV/UI/telemetry schemas |
| Pipeline code | `src/pipelines/` | ETL | ETL + catalog generation code |
| QA/validators | `tools/` | QA | Validators/utilities used in CI/local |
| Run logs & experiments | `mcp/runs/` + `mcp/experiments/` | MCP | Repro artifacts and run evidence |
| Provenance bundles | `data/prov/` | Data stewardship | PROV lineage outputs for datasets |

### Definition of done (for this document)

- [ ] Front-matter complete + valid (matches `path`)
- [ ] Install path documented for Linux/macOS + Windows (or Windows via WSL)
- [ ] Locking strategy documented (how to generate/update lockfile)
- [ ] Validation steps listed and repeatable (incl. env integrity checks)
- [ ] Provenance guidance included (what to record per run)
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document

- `path`: `.github/repro-kit/env/python/README.md` *(must match front-matter)*

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| CI | `.github/` | Workflows + policy gates |
| Pipelines | `src/pipelines/` | ETL + catalog generation |
| Tools | `tools/` | Validators, utilities, QA scripts |
| Schemas | `schemas/` | JSON Schemas (STAC/DCAT/PROV/UI/telemetry/story) |
| Data staging | `data/raw/` → `data/work/` → `data/processed/` | Data lifecycle staging for deterministic ETL |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` | Metadata catalogs for discovery/boundary artifacts |
| Provenance | `data/prov/` | PROV lineage bundles (inputs, activity, agents) |
| Graph | `src/graph/` | Ontology bindings + graph build/migrations |
| API boundary | `src/server/` | Contracted API layer (no direct UI→graph access) |
| UI | `web/` | React + map client + Focus Mode UI |
| MCP | `mcp/` | Runs, experiments, artifacts |

### Expected file tree for this sub-area

~~~text
📁 .github/
└── 📁 repro-kit/
    └── 📁 env/
        └── 📁 python/
            ├── 📄 README.md
            ├── 📄 requirements.in                 # recommended (human-edited)
            ├── 📄 requirements.lock               # recommended (pinned; prefer hashes)
            ├── 📄 requirements-dev.in             # optional (dev-only tools)
            ├── 📄 requirements-dev.lock           # optional
            ├── 📄 constraints.txt                 # optional (constraints overlay)
            ├── 📄 .python-version                 # optional (pin runtime for local tools)
            └── 📁 wheelhouse/                     # optional (offline installs / air-gapped)
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Python runtime | `X.Y.Z` | Local install or CI toolchain | `python --version` matches pinned/expected |
| Dependency spec | `requirements.in` | This directory | PR review + lint (if configured) |
| Dependency lock | `requirements.lock` | Generated from spec | Install succeeds from clean env |
| Optional constraints | `constraints.txt` | This directory | Install succeeds with constraints applied |
| Optional wheel cache | directory | `wheelhouse/` | Hash match + reproducible install |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Local virtual environment | directory | `.venv/` *(recommended; gitignored)* | Must be reproducible from lock |
| Environment snapshot | text/json | `mcp/runs/<run_id>/env/` *(recommended)* | Telemetry schema *(if present)* |
| Vulnerability/license scan output | text/json | CI logs or `mcp/runs/<run_id>/security/` *(optional)* | Tool-defined |
| SBOM (optional) | SPDX/CycloneDX | `mcp/runs/<run_id>/sbom/` *(optional)* | SPDX/CycloneDX spec |

### Sensitivity & redaction

- This repro-kit does **not** require sensitive data.
- **Do not** record secrets in:
  - lockfiles,
  - environment snapshots,
  - CI logs.
- If environment snapshots include env vars, they must be **allowlisted** (e.g., `PYTHONHASHSEED`, `TZ`) and must **exclude** tokens/credentials.

### Quality signals

- Install is reproducible from a clean machine/runner using only the lockfile.
- Dependency drift is detectable (lock hash + `pip check` + optional “freeze compare”).
- Deterministic runtime controls are available where relevant (fixed seeds, stable locale/timezone).

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- This Python environment is not itself a STAC dataset.
- However, any dataset produced using this environment should:
  - publish STAC Collections/Items in canonical locations (`data/stac/…`),
  - link to the run’s provenance bundle (see PROV-O below) so outputs are reproducible.

### DCAT

- This Python environment is not itself a DCAT dataset.
- If a dependency update changes published outputs, ensure:
  - dataset metadata is updated (version/date/description),
  - distributions remain valid and discoverable.

### PROV-O

Record software environment as part of the activity that generated outputs:

- `prov:wasGeneratedBy`: dataset outputs → generating ETL/catalog/graph activity
- `prov:used`: include **the lockfile** as an entity used by the activity (and optionally the Python version/runtime identifier)
- `prov:wasAssociatedWith`: identify the agent (CI runner, maintainer, or service account)
- Optional (recommended): include `commit_sha` and lockfile hash for replay.

### Versioning

- Treat lockfile changes as a reproducibility-relevant change:
  - If outputs are unchanged, record the new environment snapshot + run metadata.
  - If outputs change, bump dataset versions and update corresponding PROV/STAC/DCAT records.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Python Env (this repro-kit) | Reproducible runtime + dependency set | Lockfile + install steps |
| ETL | Ingest + normalize | Config + run logs |
| Catalogs | STAC/DCAT/PROV boundary artifacts | JSON + validator |
| Graph | Neo4j graph build + ontology | Cypher + API layer |
| APIs | Serve contracts | REST/GraphQL |
| UI | Map + narrative | API calls (no direct graph access) |
| Story Nodes | Curated narrative artifacts | Graph + docs |
| Focus Mode | Provenance-linked synthesis | Context bundle references |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| Python dependency lock | `.github/repro-kit/env/python/requirements.lock` | Review-required; rerun validations; record lock hash |
| JSON schemas | `schemas/` | Semver + changelog (if used) |
| API schemas | `src/server/` + docs | Contract tests required |
| Layer registry | `web/…` | Schema-validated |

### Extension points checklist (for future work)

- [ ] Env: add dependency to spec; regenerate lock; record change rationale
- [ ] Env: verify clean install + `pip check`
- [ ] Data: new domain added under `data/<domain>/…`
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + access rules
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- This environment enables repeatable generation of:
  - governed Story Nodes,
  - evidence artifacts (analysis outputs) that Story Nodes reference,
  - provenance bundles that Focus Mode requires.

### Provenance-linked narrative rule

- Any story or synthesis surfaced to users must be traceable to dataset IDs and/or source assets.
- Environment reproducibility is part of that traceability: an auditor should be able to re-run the pipeline with the lockfile to reproduce evidence products.

### Optional structured controls

~~~yaml
python_env_profile:
  python_version: "TBD"                         # pin in CI and mirror locally
  lockfile: ".github/repro-kit/env/python/requirements.lock"
  install_mode: "locked"                        # "locked" | "unlocked"
  deterministic_controls:
    timezone: "UTC"
    pythonhashseed: "0"
~~~

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks (if configured)
- [ ] Environment install from lockfile (clean venv)
- [ ] `pip check` (dependency consistency)
- [ ] Schema validation (STAC/DCAT/PROV)
- [ ] Graph integrity checks
- [ ] API contract tests (as applicable)
- [ ] UI schema checks (layer registry)
- [ ] Security scanning gates (dependency/license/vuln), where applicable

### Reproduction

~~~bash
# Example commands — adjust paths to match repo conventions.

# 0) Choose Python
python --version

# 1) Create a clean virtualenv (macOS/Linux)
python -m venv .venv
. .venv/bin/activate

# Windows (PowerShell) alternative:
# py -m venv .venv
# .\.venv\Scripts\Activate.ps1

python -m pip install --upgrade pip

# 2) Install from lock (preferred)
# If you use hashed locks, add --require-hashes.
python -m pip install -r .github/repro-kit/env/python/requirements.lock

# 3) Sanity check
python -m pip check

# 4) Run validations/tests (placeholders — replace with repo tasks)
# python tools/validate_schemas.py
# python -m pytest -q
~~~

~~~yaml
# CI hint (GitHub Actions) — illustrative only:
# - uses: actions/setup-python@v5
#   with:
#     python-version: "3.x"
#     cache: "pip"
# - run: python -m pip install -r .github/repro-kit/env/python/requirements.lock
# - run: python -m pip check
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| `python_version` | runtime | `mcp/runs/<run_id>/env/` *(recommended)* |
| `lockfile_sha256` | lockfile hash | `mcp/runs/<run_id>/env/` + PROV entity *(recommended)* |
| `dependency_drift` | compare installed vs lock | CI logs *(optional)* |
| `vuln_scan_summary` | scanner output | CI logs or `docs/telemetry/` *(optional)* |

## ⚖ FAIR+CARE & Governance

### Review gates

- Dependency updates should be reviewed by:
  - CI/Platform maintainers (reproducibility + compatibility),
  - Security reviewer (vuln/license risk) when changes introduce new packages or major upgrades.

### CARE / sovereignty considerations

- This environment does not itself introduce sovereignty risk, but it supports pipelines that may process sensitive domain data.
- Ensure tooling used in this environment respects:
  - redaction/generalization rules in governed domain modules,
  - any restricted-location handling,
  - PII/secret scanning gates.

### AI usage constraints

- Ensure this doc’s AI permissions/prohibitions match intended use (front-matter).
- Do not use AI tooling to invent provenance or fabricate evidence; Focus Mode requires provenance-linked content.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-30 | Initial Python repro-kit README | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

