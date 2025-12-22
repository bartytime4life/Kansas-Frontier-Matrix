---
title: "GitHub Actions Scripts — README"
path: ".github/actions/scripts/README.md"
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

doc_uuid: "urn:kfm:doc:github-actions:scripts-readme:v1.0.0"
semantic_document_id: "kfm-github-actions-scripts-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github-actions:scripts-readme:v1.0.0"
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

# GitHub Actions Scripts — README

## 📘 Overview

### Purpose

- Define the **contracts, conventions, and safety rules** for helper scripts located in `.github/actions/scripts/`.
- Ensure CI automation remains **deterministic, auditable, and secure**, with behavior that supports KFM’s canonical pipeline ordering (ETL → Catalogs → Graph → API → UI → Story → Focus Mode).

### Scope

| In Scope | Out of Scope |
|---|---|
| Scripts used by GitHub Actions workflows/composite actions that run validations, formatting, schema checks, or repo hygiene tasks. | Authoring full workflow files, release management policy, or defining new governance rules (those belong under `docs/governance/`). |
| Script interface rules (inputs, outputs, exit codes), logging conventions, and security constraints. | Implementing data pipelines themselves (ETL/catalog/graph code lives under `src/` + `data/`). |
| How to run scripts locally in a way that mirrors CI as closely as possible. | Choosing a specific language/runtime standard for the whole repo (unless governed elsewhere). |

### Audience

- **Primary:** KFM maintainers and contributors working on CI, validation, and repo automation.
- **Secondary:** Any contributor who needs to understand why CI failed and how to reproduce locally.

### Definitions

- Link: `docs/glossary.md`
- Terms used in this doc: **CI**, **workflow**, **composite action**, **contract**, **idempotent**, **deterministic**, **redaction**.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Scripts directory | `.github/actions/scripts/` | CI maintainers | Helper scripts invoked by workflows/actions. |
| Workflows (caller) | `.github/workflows/` | CI maintainers | Where scripts are typically invoked from. |
| Composite actions (caller, if used) | `.github/actions/` | CI maintainers | Optional layer that may wrap scripts. |
| Governed Markdown templates | `docs/templates/` | Docs maintainers | Governs doc structure and metadata. |
| Schemas | `schemas/` | Schema maintainers | Scripts may validate these or validate artifacts against them. |
| Data & catalogs | `data/` | Data maintainers | Scripts may validate outputs (no mutation unless explicitly intended). |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] Directory purpose + conventions are clear
- [ ] Script “contract” is documented (inputs/outputs/exit codes/logging)
- [ ] Security guidance included (no secret leakage; redaction-aware logging)
- [ ] Local reproduction guidance included (even if commands are placeholders)
- [ ] Version history updated

## 🗂️ Directory Layout

### This document

- `path`: `.github/actions/scripts/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| GitHub automation | `.github/` | Workflows, actions, automation docs |
| Documentation | `docs/` | Canonical governed docs + templates |
| Schemas | `schemas/` | JSON Schemas for STAC/DCAT/PROV/story nodes/telemetry/etc. |
| Data | `data/` | Raw/work/processed + STAC/DCAT/PROV outputs |
| Pipelines | `src/pipelines/` | ETL + catalog generation code |
| Graph | `src/graph/` | Graph build + ontology bindings |
| API | `src/api/` (or `src/server/`, if used) | API layer contracts + services |
| UI | `web/` | React/Map UI (MapLibre/related) |

### Expected file tree for this sub-area

~~~text
📁 .github/
├── 📁 actions/
│   ├── 📁 scripts/
│   │   └── 📄 README.md
│   └── 📄 <optional: composite actions live here>
└── 📁 workflows/
    └── 📄 <workflows that invoke scripts live here>
~~~

## 🧭 Context

### Background

GitHub Actions workflows often need small, reusable “glue” logic:
- validating schemas and catalogs,
- enforcing documentation protocol rules,
- checking deterministic outputs,
- verifying repo hygiene and policy constraints.

Keeping those concerns in **scripts** (instead of repeating YAML blocks) improves maintainability, local reproducibility, and auditability.

### Assumptions

- Scripts may be called from workflows and/or composite actions.
- CI should be able to run scripts non-interactively and fail fast on invalid states.
- CI validation should support KFM’s layered architecture and provenance-first constraints.

### Constraints / invariants

- **Canonical pipeline order is preserved:** ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode.
- **Frontend consumes contracts via APIs** (no direct graph dependency).
- Scripts must be **idempotent**: repeated runs produce the same result (unless explicitly designed to generate versioned artifacts).
- Scripts must be **safe by default**:
  - no credentials in logs,
  - no writing outside the workspace,
  - no silent network side effects unless explicitly documented.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What script runtimes are “allowed” (bash/python/node) for this repo? | TBD | TBD |
| Do we require a specific lint toolset for scripts (shellcheck, ruff, eslint)? | TBD | TBD |
| Should scripts be permitted to write artifacts back into `data/` or only validate? | TBD | TBD |

### Future extensions

- Add a “script contract linter” gate (validate headers, inputs/outputs docs, logging rules).
- Add standardized reporting outputs (e.g., machine-readable JSON summaries) for downstream CI annotations.

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  A[.github/workflows/*] --> B[.github/actions/* (optional)]
  B --> C[.github/actions/scripts/*]
  A --> C

  C --> D[Validate artifacts: docs/schemas/data]
  D --> E{Pass?}
  E -- yes --> F[CI green]
  E -- no --> G[CI red + actionable logs]
~~~

### Optional: sequence diagram

~~~mermaid
sequenceDiagram
  participant Runner as GitHub Runner
  participant WF as Workflow Step
  participant Script as Script (this folder)

  Runner->>WF: Start job
  WF->>Script: Execute script with env + args
  Script-->>WF: Exit code + stdout/stderr
  WF-->>Runner: Annotate logs / fail or succeed
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Repo content | Files | Checkout workspace | Script checks existence + expected structure |
| Script args | CLI flags/args | Workflow step | Validate required args; provide `--help` |
| Environment | Env vars | Workflow runner | Validate presence/format; avoid leaking secrets |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Exit status | Integer | N/A | `0` success; non-`0` failure |
| Logs | stdout/stderr | GitHub Actions logs | Do not print secrets; prefer actionable messages |
| Optional reports | Text/JSON (optional) | Workspace (if used) | Document file name + schema if introduced |

### Sensitivity & redaction

- Do **not** print secrets, tokens, or sensitive content to logs.
- If a script handles potentially sensitive locations/content:
  - redact or generalize as required before outputting,
  - document the redaction behavior here and in the caller workflow.

### Quality signals

- Fail fast on invalid input.
- Use consistent, grep-able log prefixes (e.g., `ERROR:`, `WARN:`) to improve CI readability.
- Prefer deterministic ordering (sorted outputs) to avoid flaky diffs.

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Collections involved: N/A for this README (depends on repo datasets).
- Items involved: N/A for this README.
- Extension(s): N/A for this README.

### DCAT

- Dataset identifiers: N/A for this README.
- License mapping: N/A for this README.
- Contact / publisher mapping: N/A for this README.

### PROV-O

- `prov:wasDerivedFrom`: N/A for this README.
- `prov:wasGeneratedBy`: N/A for this README.
- Activity / Agent identities: N/A for this README.

### Versioning

- If scripts emit versioned artifacts (reports, generated catalogs, etc.), document:
  - where versions are written,
  - how predecessor/successor relationships are recorded (if applicable),
  - and whether output is intended to be committed or treated as CI-only artifacts.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Workflows | Orchestrate CI steps | GitHub Actions YAML |
| Composite actions (optional) | Reusable step bundles | `action.yml` + inputs/outputs |
| Scripts (this folder) | Perform checks/automation | CLI args + env vars + exit codes |
| Repo artifacts | Data/docs/schemas validated by scripts | Files in workspace |
| CI logging | Human-readable failure context | stdout/stderr + annotations |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| Script CLI contract | Each script file (header + `--help`) | Backward compat or caller updates |
| Exit codes | Each script | Stable meanings; document breaking changes |
| Output artifacts (if any) | Workspace paths | Semver + changelog if treated as stable inputs elsewhere |

### Extension points checklist (for future work)

- [ ] Add new script under `.github/actions/scripts/`
- [ ] Document its purpose + inputs/outputs in this README
- [ ] Ensure it is deterministic and idempotent
- [ ] Ensure it does not leak secrets / sensitive content
- [ ] Add/adjust workflow invocation (and keep it minimal)
- [ ] Add/adjust CI gates only with clear failure messaging
- [ ] If it introduces new schemas or reports, add schema validation and versioning notes

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- Indirectly: scripts can enforce that Story Node docs and related assets meet provenance and validation rules before changes merge.

### Provenance-linked narrative rule

- Scripts that validate narrative content should enforce: **every claim traces to a dataset/record/asset ID** (where such validation is implemented).

### Optional structured controls

~~~yaml
# N/A for this README. If a script enforces Focus Mode defaults,
# document the allowed keys and validation rules here.
~~~

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks (where applicable)
- [ ] Schema validation (STAC/DCAT/PROV/story nodes/telemetry) (where applicable)
- [ ] Script linting (language-appropriate)
- [ ] Script smoke test (runs in CI with representative inputs)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands
#
# If a script is invoked in CI, it SHOULD be runnable locally in the same way.

# 1) List scripts and read their --help
# ls .github/actions/scripts
# .github/actions/scripts/<script_name> --help

# 2) Run the script with the same inputs the workflow uses
# .github/actions/scripts/<script_name> <args>

# 3) If applicable: run any repo-wide validators invoked by CI
# <repo-specific command>
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| Script runtime | CI runner | CI logs / job summary (if enabled) |
| Validation pass/fail | Script exit code | CI check status |
| Artifact hashes (optional) | Script output | CI logs / artifact metadata |

## ⚖ FAIR+CARE & Governance

### Review gates

- Changes to scripts that:
  - introduce new data outputs,
  - touch restricted/sensitive content,
  - or alter validation semantics
  should receive additional maintainer review.

### CARE / sovereignty considerations

- If scripts validate or transform culturally sensitive or restricted-location datasets:
  - apply redaction/generalization rules before emitting logs/artifacts,
  - ensure policy references remain authoritative in `docs/governance/`.

### AI usage constraints

- This README permits: summarize, structure extraction, translation, keyword indexing.
- This README prohibits: generating new governance policy and inferring sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial README for `.github/actions/scripts/` | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

