---
title: "Action README — stac-validate"
path: ".github/actions/stac-validate/README.md"
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

doc_uuid: "urn:kfm:doc:github-actions:stac-validate:readme:v1.0.0"
semantic_document_id: "kfm-github-action-stac-validate-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github-actions:stac-validate:readme:v1.0.0"
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

# Action — stac-validate

## 📘 Overview

### Purpose
This repository-local GitHub Action validates STAC JSON artifacts committed to the repo, so that catalog
outputs remain machine-validated and safe to consume downstream.

In KFM, STAC Items and Collections are expected to live under `data/stac/items/` and `data/stac/collections/`
(or an equivalent domain-scoped STAC layout if adopted later). This action is intended to be used as a CI
gate to prevent invalid STAC from merging.

### Scope

| In Scope | Out of Scope |
|---|---|
| Validating STAC JSON structure and schema conformance for repo-tracked STAC assets | Generating STAC (ETL/catalog build), DCAT validation, PROV validation |
| Failing CI on invalid STAC | Repairing or auto-modifying STAC files |
| Optional: link/href integrity checks (if implemented) | Neo4j / API / UI changes |

### Audience
- Primary: Repo maintainers, CI owners, data/catalog contributors
- Secondary: ETL authors, reviewers validating new datasets

### Definitions (link to glossary)
- Link: `docs/glossary.md` (not confirmed in repo)
- Terms used in this doc: STAC Item, STAC Collection, schema validation, CI gate, provenance

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Action README | `.github/actions/stac-validate/README.md` | CI/Platform (TBD) | This document |
| Action definition | `.github/actions/stac-validate/action.yml` | CI/Platform (TBD) | Not confirmed in repo |
| CI workflow(s) | `.github/workflows/*.yml` | CI/Platform (TBD) | Not confirmed in repo |
| STAC outputs | `data/stac/` | Data/Catalog (TBD) | Items + collections |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] README explains what the action validates and where STAC lives
- [ ] Example workflow usage included
- [ ] Validation behavior, failure modes, and troubleshooting documented
- [ ] Security + sovereignty considerations explicitly stated (even if “N/A”)

## 🗂️ Directory Layout

### This document
- `path`: `.github/actions/stac-validate/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| GitHub Actions | `.github/actions/` | Repo-local reusable actions |
| Workflows | `.github/workflows/` | CI pipelines invoking actions |
| STAC catalogs | `data/stac/` | STAC Collections + Items (JSON) |
| Schemas | `schemas/` | JSON schemas (if repo-managed) |

### Expected file tree for this sub-area
~~~text
📁 .github/
└── 📁 actions/
    └── 📁 stac-validate/
        ├── 📄 README.md
        ├── 📄 action.yml                         # not confirmed in repo
        ├── 📄 LICENSE                            # optional, not confirmed in repo
        └── 📁 scripts/                           # optional, not confirmed in repo
            ├── 📄 validate.sh                    # not confirmed in repo
            └── 📄 validate.py                    # not confirmed in repo
~~~

## 🧭 Context

### Background
KFM’s canonical pipeline includes a catalog stage where STAC is used to describe spatiotemporal assets,
and CI is expected to enforce machine validation for these artifacts.

This action is intended to provide the “STAC validation” piece of that CI posture, ensuring PRs cannot
merge invalid STAC JSON.

### Assumptions
- The exact validator implementation (binary/library/container) is **not confirmed in repo** by this README alone.
- The authoritative contract for inputs/outputs is the action definition file (`action.yml`) **(not confirmed in repo)**.
- Validation is deterministic: same inputs → same results.

### Constraints / invariants
- This action must be safe in CI: **no secrets required**, **no repo writes**, and **no network dependency** unless explicitly approved.
- Validation must not weaken governance: if restricted/sensitive content must be redacted upstream, this action does not “fix” that— it only detects invalid structure.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Which STAC validator is used (pystac, stac-validator, custom schemas)? | TBD | TBD |
| What STAC version + extensions are required (KFM-STAC profile details)? | TBD | TBD |
| Should href/link integrity checks be enforced in CI? | TBD | TBD |

### Future extensions
- Link/href integrity checks (broken links, missing assets)
- Extension schema enforcement (project-specific STAC profile checks)
- Optional DCAT/PROV validation companion actions (separate actions recommended)

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  PR[Pull Request] --> CI[GitHub Actions CI]
  CI --> A[stac-validate action]
  A --> V[Validate STAC JSON]
  V -->|pass| OK[✅ Merge allowed]
  V -->|fail| NO[❌ CI fails; fix STAC]
~~~

## 📦 Data & Metadata

### Inputs
The authoritative input list is defined in `.github/actions/stac-validate/action.yml` (not confirmed in repo).

The following inputs are a **recommended contract** (not confirmed in repo) that keeps the action generic
and reusable:

| Input (proposed) | Format | Where from | Validation |
|---|---|---|---|
| `stac_root` | string path | workflow `with:` | directory exists |
| `include_glob` | glob | workflow `with:` | glob parses |
| `exclude_glob` | glob | workflow `with:` | glob parses |
| `fail_on_warnings` | boolean | workflow `with:` | true/false |
| `check_links` | boolean | workflow `with:` | true/false |

### Outputs
This action should fail the workflow step on invalid STAC. If outputs are implemented, keep them minimal:

| Output (proposed) | Format | Path | Contract / Schema |
|---|---|---|---|
| `validated_file_count` | integer | step output | not confirmed in repo |
| `error_count` | integer | step output | not confirmed in repo |

### Sensitivity & redaction
- This action does not perform redaction.
- If any STAC metadata contains restricted location detail, the governance policy must be applied **before**
  committing those STAC artifacts.

### Quality signals
- Number of STAC files validated
- Number of schema errors/warnings
- Optional: missing/invalid `bbox`, invalid geometry, invalid datetime fields (validator-dependent)

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Expected target directories:
  - `data/stac/collections/`
  - `data/stac/items/`
- This action is the CI enforcement layer that helps keep STAC artifacts machine-validated.

### DCAT
- Out of scope for this action. Use a separate validator action if needed.

### PROV-O
- Out of scope for this action. Use a separate validator action if needed.

### Versioning
- If STAC versioning links (predecessor/successor) are required by KFM profile, the validator and/or custom checks should enforce them.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Workflow | Decides when to run validation | `.github/workflows/*.yml` |
| stac-validate action | Runs STAC schema validation | `uses: ./.github/actions/stac-validate` |
| Validator tool | Performs actual validation | not confirmed in repo |

### Interfaces / contracts

#### Example usage in a workflow
~~~yaml
name: Validate STAC

on:
  pull_request:
    paths:
      - "data/stac/**.json"

jobs:
  stac_validate:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Validate STAC catalogs
        uses: ./.github/actions/stac-validate
        with:
          stac_root: "data/stac"          # not confirmed in repo
          fail_on_warnings: true         # not confirmed in repo
~~~

#### Minimal usage (if the action has sensible defaults)
~~~yaml
- uses: ./.github/actions/stac-validate
~~~

### Extension points checklist (for future work)
- [ ] Add custom checks for KFM-STAC profile compliance
- [ ] Add optional link/href integrity checks
- [ ] Add summary output for PR annotations (counts + file list)

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
This action does not directly change Story Nodes or Focus Mode behavior. Indirectly, it helps ensure the
catalog layer (STAC) remains valid for downstream ingestion and UI discovery.

### Provenance-linked narrative rule
N/A for this action (no narrative generation).

## 🧪 Validation & CI/CD

### Validation steps
- [ ] CI triggers on changes to `data/stac/**`
- [ ] Action validates STAC JSON and fails CI on schema errors
- [ ] Validation output is readable in CI logs

### Reproduction
~~~bash
# Repo-local reproduction depends on the validator tool used (not confirmed in repo).
# Recommended pattern:
# 1) run the validator against data/stac
# 2) ensure it matches CI behavior (same schema set, same ignore rules)
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| `stac_validation_pass/fail` | CI logs | GitHub Actions logs |
| `validated_file_count` | action output | workflow summaries (optional) |

## ⚖ FAIR+CARE & Governance

### Review gates
- If this action changes what is considered “valid” STAC (schema set, custom rules), treat as a governance-impacting change and route for review (security + data governance as applicable).

### CARE / sovereignty considerations
- If any datasets require location generalization, ensure the STAC artifacts committed to the repo comply before validation (this action only validates structure, not sensitivity).

### AI usage constraints
- None. This action should not invoke LLMs.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial README for repo-local STAC validation action | TBD |

---
Footer refs:
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`