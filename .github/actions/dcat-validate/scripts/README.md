---
title: "GitHub Action DCAT Validate Scripts"
path: ".github/actions/dcat-validate/scripts/README.md"
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

doc_uuid: "urn:kfm:doc:github-actions:dcat-validate:scripts-readme:v1.0.0"
semantic_document_id: "kfm-gha-dcat-validate-scripts-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github-actions:dcat-validate:scripts-readme:v1.0.0"
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

# GitHub Action DCAT Validate Scripts

## 📘 Overview

### Purpose
This directory contains the **implementation scripts** used by the **DCAT validation GitHub Action**.

These scripts are responsible for:
- locating generated **DCAT dataset records**
- validating them against the repo’s governed **KFM-DCAT profile**
- producing CI-friendly output (exit codes, concise logs, and optionally annotations)

### Scope

| In Scope | Out of Scope |
|---|---|
| Scripts under `.github/actions/dcat-validate/scripts/` | Writing or generating DCAT records |
| Local developer workflow for running validation | ETL transforms that produce the catalogs |
| CI-safe output behavior (fail/pass, summaries) | Graph ingestion, API serving, UI rendering |

### Audience
- Primary: CI/CD maintainers and contributors editing validation logic
- Secondary: data pipeline contributors debugging why a DCAT record fails validation

### Definitions
- Link: `docs/glossary.md`
- Terms used in this doc: DCAT, JSON-LD, PROV, profile, catalog, validation

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Action overview | `.github/actions/dcat-validate/README.md` | CI/CD | High-level action docs |
| Action definition | `.github/actions/dcat-validate/` | CI/CD | File name varies by repo conventions |
| Scripts directory | `.github/actions/dcat-validate/scripts/` | CI/CD | This document lives here |
| DCAT outputs | `data/catalog/dcat/` | Catalog | Canonical output location |
| Governed pipeline guide | `docs/MASTER_GUIDE_v12.md` | Docs | Canonical pipeline ordering + invariants |

### Definition of done
- [ ] Front-matter complete and `path` matches file location
- [ ] Script inventory and file tree kept in sync with the actual directory
- [ ] Local “how to run” steps do not assume secrets or proprietary services
- [ ] Logging guidance avoids leaking sensitive content in CI logs
- [ ] Validation steps are repeatable and deterministic

## 🗂️ Directory Layout

### This document
- `path`: `.github/actions/dcat-validate/scripts/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| GitHub Actions | `.github/actions/` | Local action implementations |
| DCAT catalogs | `data/catalog/dcat/` | DCAT dataset records produced by pipelines |
| STAC catalogs | `data/stac/` | STAC items/collections |
| PROV lineage | `data/prov/` | Provenance bundles for pipeline activities |
| Schemas | `schemas/` | JSON schemas, SHACL shapes, or schema bindings |

### Expected file tree for this sub-area
~~~text
📁 .github/
└── 📁 actions/
    └── 📁 dcat-validate/
        ├── 📄 README.md
        ├── 📄 <action-definition-file>   # not confirmed in repo: update to actual file name
        └── 📁 scripts/
            ├── 📄 README.md
            ├── 📄 <entrypoint-script>     # not confirmed in repo: update to actual file name
            ├── 📄 <helpers-or-library>    # optional
            └── 📁 <fixtures>              # optional
~~~

## 🧭 Context

### Background
KFM treats catalog outputs as governed artifacts, and CI is expected to enforce validation gates so that
invalid catalogs do not propagate into downstream stages (graph, APIs, UI, story nodes).

This scripts folder exists to keep validation logic **close to** the GitHub Action that runs it, while still
remaining deterministic and reviewable.

### Assumptions
- DCAT records live under `data/catalog/dcat/`.
- The action uses these scripts as the validation entrypoint.
- Exact script names and runtimes are repository-dependent and must be kept current in this README.

### Constraints and invariants
- Preserve canonical pipeline ordering: ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story → Focus Mode.
- Scripts must be deterministic and CI-safe:
  - no reliance on local machine state
  - stable exit codes
  - minimal, non-sensitive logs
- Do not leak sensitive information into GitHub Action logs. Prefer paths + record identifiers over full payload dumps.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What is the canonical entrypoint filename for this action? | CI/CD | TBD |
| What is the authoritative schema/shape location for DCAT validation? | Catalog | TBD |
| Should CI annotate failing files inline (GitHub annotations) or only print a summary? | CI/CD | TBD |

### Future extensions
- Add optional “warning mode” for non-blocking checks (style, optional fields).
- Add a “changed files only” mode for faster PR validation.

## 🗺️ Diagrams

### System and validation flow
~~~mermaid
flowchart LR
  A[Pipeline outputs DCAT records] --> B[data/catalog/dcat/]
  B --> C[GitHub Action dcat-validate]
  C --> D[Scripts in this folder]
  D --> E{Valid?}
  E -- Yes --> F[CI pass]
  E -- No --> G[CI fail + summary]
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| DCAT records | JSON-LD / Turtle / RDF | `data/catalog/dcat/` | Parse + profile checks |
| Profile rules | Config / schema / shapes | `schemas/` or action-local | Must be versioned |
| File selection | glob / file list | CI step | Deterministic ordering recommended |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Pass/fail signal | exit code | CI runtime | 0 success, nonzero failure |
| Validation report | console log / summary | CI runtime | Human-readable + concise |
| Optional artifacts | text/json | CI artifacts | Keep stable for downstream parsing |

### Sensitivity and redaction
Even when catalogs are public, validation logs should avoid printing entire records.
Recommended log behavior:
- print the failing file path(s)
- print a short error code/category
- print a small excerpt only when necessary (and never secrets)

### Quality signals
Typical checks to implement or support (depending on profile rules):
- required fields present
- valid RDF/JSON-LD parse
- stable dataset identifiers
- license field present and non-empty
- spatial/temporal coverage fields well-formed

## 🌐 STAC, DCAT & PROV Alignment

### STAC
This action focuses on **DCAT** validation, but catalogs are part of the same governed “catalog stage”.
If DCAT records reference STAC items/collections, validators may optionally check that references resolve.

### DCAT
- Primary outputs live under: `data/catalog/dcat/`
- Validation should be aligned to: `KFM-DCAT v11.0.0`

### PROV-O
If DCAT records include provenance pointers, validators may optionally check:
- identifiers are present
- values are well-formed (IDs, URNs, or run IDs as defined by the repo)

### Versioning
- Prefer versioned profile rules and stable identifiers.
- If records are versioned, ensure predecessor/successor links are not broken.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Entry script | Orchestrate validation run | CLI args or env vars |
| Validators | Apply profile checks | Functions/modules |
| Report formatter | Produce CI-friendly output | stdout/stderr + exit code |

### Interfaces and contracts

| Contract | Location | Versioning rule |
|---|---|---|
| Markdown protocol | repo-wide | CI enforces front-matter validity |
| DCAT profile rules | `schemas/` or action-local | Semver preferred + changelog |
| File locations | `data/catalog/dcat/` | Treated as canonical output path |

### Extension points checklist
- [ ] Add new rule: update profile rules and tests
- [ ] Add new input location: update action + scripts documentation
- [ ] Add new output artifact: keep format stable and documented
- [ ] Add annotations: ensure messages are short and non-sensitive

## 🧠 Story Node and Focus Mode Integration

### How this work surfaces in Focus Mode
Not directly. This action is a **catalog stage guardrail**.

Indirectly, invalid catalogs can break downstream provenance-linked narratives, so keeping catalogs valid supports
Focus Mode’s “no unsourced narrative” invariant.

### Provenance-linked narrative rule
Every narrative claim must trace to a dataset/record/asset ID. This validator helps ensure catalogs used as
evidence pointers remain well-formed.

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Scripts run without network access (unless explicitly required and documented)
- [ ] Scripts run deterministically on the same inputs
- [ ] Failures identify the file(s) and the rule category
- [ ] Logs do not dump full datasets or sensitive strings
- [ ] README inventory matches the actual scripts directory

### Reproduction
~~~bash
# From the repo root:
# 1) Inspect what scripts exist
ls -la .github/actions/dcat-validate/scripts

# 2) Run the entrypoint (update <entrypoint-script> to the actual filename)
./.github/actions/dcat-validate/scripts/<entrypoint-script> --help

# 3) Validate the canonical DCAT output directory
./.github/actions/dcat-validate/scripts/<entrypoint-script> --input data/catalog/dcat
~~~

### Telemetry signals
| Signal | Source | Where recorded |
|---|---|---|
| Validation pass/fail | GitHub Action job | Workflow logs |
| Failing file count | Scripts | Workflow logs / summary |
| Rule category counts | Scripts | Optional job summary |

## ⚖ FAIR+CARE & Governance

### Review gates
- Changes to validation rules or profile bindings should receive:
  - Catalog maintainer review
  - CI/CD maintainer review
- If validation logic affects how sensitive metadata is logged, it requires human review.

### CARE and sovereignty considerations
- Avoid printing precise locations or sensitive fields when logging invalid records.
- If a dataset is classified as restricted, ensure the validator does not echo restricted values.

### AI usage constraints
- This directory is for deterministic validation scripts.
- AI-generated modifications to validation rules must be reviewed by a human maintainer.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial scripts README for DCAT validation action | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`