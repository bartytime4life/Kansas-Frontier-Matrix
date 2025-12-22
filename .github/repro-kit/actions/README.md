---
title: "KFM Repro Kit — GitHub Actions"
path: ".github/repro-kit/actions/README.md"
version: "v1.0.0-draft"
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

doc_uuid: "urn:kfm:doc:github:repro-kit:actions-readme:v1.0.0-draft"
semantic_document_id: "kfm-github-repro-kit-actions-readme-v1.0.0-draft"
event_source_id: "ledger:kfm:doc:github:repro-kit:actions-readme:v1.0.0-draft"
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

# KFM Repro Kit — GitHub Actions

## 📘 Overview

### Purpose

This directory contains **reusable GitHub Actions** (preferably *composite actions*) used by KFM CI workflows to enforce repeatable, deterministic validation gates across the repository.

These actions exist to support the CI behavior expectation:

- **validate if present; fail if invalid; skip if not applicable**

(See the parent doc: `.github/repro-kit/README.md`.)

### Scope

| In Scope | Out of Scope |
|---|---|
| Conventions for actions in `.github/repro-kit/actions/` (layout, naming, input/output docs, deterministic rules) | Defining the full set of required actions for every domain (depends on which subsystems are implemented) |
| Guidance for “validate/skip/fail deterministically” patterns | Implementing domain ETLs or schema content (belongs under `src/` / `schemas/` / `data/`) |
| Examples of how workflows should call these actions | Authoritative repo-specific commands (not confirmed in repo) |

### Audience

- **Primary:** KFM maintainers and contributors authoring CI workflows under `.github/workflows/`
- **Secondary:** Domain pack maintainers adding validation to new domains (ETL/catalog/graph/API/UI)

### Definitions (link to glossary)

- Link: `docs/glossary.md`
- Terms used in this doc: **composite action**, **workflow**, **gate**, **deterministic**, **skip-if-not-applicable**, **schema validation**

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Repro Kit root | `.github/repro-kit/README.md` | Maintainers | Parent overview + philosophy for reproducibility |
| Workflows | `.github/workflows/` | Maintainers | CI pipelines call these actions |
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical pipeline ordering + invariants |
| v13 Redesign Blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | KFM Core | CI gate alignment + deterministic behavior expectations |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] File tree reflects intended `actions/` structure
- [ ] Per-action documentation contract defined (inputs/outputs/failure modes)
- [ ] Determinism rules documented (validate/skip/fail)
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document

- `path`: `.github/repro-kit/actions/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Workflows | `.github/workflows/` | CI definitions that call reusable actions |
| Repro Kit root | `.github/repro-kit/` | Repro/CI documentation and shared conventions |
| Actions | `.github/repro-kit/actions/` | Reusable actions (composite preferred) |
| Schemas | `schemas/` | JSON Schemas (STAC/DCAT/PROV/story nodes/UI registries/telemetry) |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Validated artifacts produced by pipeline runs |
| Server contracts | `src/server/` | API contracts + contract tests (canonical API boundary) |
| UI | `web/` | UI artifacts validated by CI (schema + lint as applicable) |

### Expected file tree for this sub-area

~~~text
📁 .github/
├── 📁 repro-kit/
│   ├── 📄 README.md
│   └── 📁 actions/
│       ├── 📄 README.md
│       ├── 📁 <action-slug>/
│       │   ├── 📄 action.yml
│       │   ├── 📄 README.md
│       │   └── 📁 src/                        # optional (JS actions)
│       └── 📁 _shared/                        # optional (shared snippets/templates)
└── 📁 workflows/
    └── 📄 <workflow>.yml
~~~

## 🧭 Context

### Background

KFM CI is expected to be **deterministic** and aligned to canonical roots. The repo is structured around a governed pipeline, and CI gates must reflect that structure and enforce validation where artifacts exist.

Reusable actions reduce drift across workflows and help keep gates consistent.

### Assumptions

- GitHub Actions is the CI engine for this repository.
- Actions in this folder are consumed locally via `uses: ./.github/repro-kit/actions/<action-slug>`.
- Each action must be usable in multiple workflows without repo-specific hardcoding.

### Constraints / invariants

- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode is preserved.
- Frontend consumes contracts via APIs (no direct graph dependency).
- CI behavior must remain deterministic:
  - if an optional root is absent, a gate should **skip**
  - if a root is present but invalid, a gate must **fail**
  - if a root is present and valid, a gate must **pass**

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Should we standardize on composite actions vs reusable workflows (workflow_call) for gates? | Maintainers | TBD |
| Which gates run on PR vs main vs release? | Maintainers | TBD |
| Where should “local runner” scripts live (e.g., `tools/` vs `scripts/`)? | Maintainers | TBD (not confirmed in repo) |

### Future extensions

- Add reusable workflows (e.g., `.github/workflows/reusable/*.yml`) that call these actions in standard sequences.
- Add a consistent “report artifact” convention (e.g., JSON + SARIF where applicable) for CI UX.

## 🗺️ Diagrams

### System / CI dataflow diagram (conceptual)

~~~mermaid
flowchart LR
  PR[Pull Request / Push] --> WF[GitHub Workflow<br/>.github/workflows/*]
  WF --> RK[Repro Kit Actions<br/>.github/repro-kit/actions/*]

  RK --> MDP[Markdown Protocol Gate]
  RK --> SCHEMA[Schema Validation Gate<br/>STAC/DCAT/PROV/Story/UI/Telemetry]
  RK --> GRAPH[Graph Integrity Gate]
  RK --> API[API Contract Tests]
  RK --> UI[UI Registry/Lint Gates]
  RK --> SEC[Security + Sovereignty Gates]

  MDP --> RESULT[Pass / Fail / Skip]
  SCHEMA --> RESULT
  GRAPH --> RESULT
  API --> RESULT
  UI --> RESULT
  SEC --> RESULT
~~~

## 📦 Data & Metadata

### Per-action documentation contract (required)

Every action under `.github/repro-kit/actions/<action-slug>/` MUST include a local `README.md` that documents:

- what it validates
- which paths it expects
- required inputs (and defaults)
- outputs (if any)
- failure conditions (what makes it exit non-zero)
- skip behavior (what makes it exit zero but do nothing)

Recommended README sections for each action:

| Section | Required | Notes |
|---|---:|---|
| Purpose | ✅ | 1–3 sentences |
| Inputs | ✅ | Table; include defaults |
| Outputs | ⚠️ | Only if the action emits outputs |
| What it checks | ✅ | Bullet list of validations |
| Skip rules | ✅ | “skip if not applicable” must be explicit |
| Failure modes | ✅ | What triggers hard fail |
| Examples | ✅ | Example `uses:` snippet |

### Example: calling a local action (workflow snippet)

~~~yaml
- name: Validate <thing>
  uses: ./.github/repro-kit/actions/<action-slug>
  with:
    # action-defined inputs (TBD)
    path: "TBD"
~~~

### Sensitivity & redaction

- Actions MUST avoid printing secrets or sensitive values to logs.
- If a gate touches potentially sensitive data (e.g., sovereignty-restricted locations), it MUST only output aggregate / non-sensitive diagnostics and must respect repository governance rules.

### Quality signals

- Stable exit codes:
  - `0` = pass or skip
  - non-zero = fail
- Prefer machine-readable reports when possible (e.g., JSON diagnostics) and keep them deterministic.

## 🌐 STAC, DCAT & PROV Alignment

This folder does not define STAC/DCAT/PROV content, but actions here may enforce validation of:

- STAC outputs under `data/stac/`
- DCAT outputs under `data/catalog/dcat/`
- PROV bundles under `data/prov/`

Actions that validate these outputs should explicitly document:

- which schemas they validate against (expected under `schemas/`)
- what “presence” means (directory exists vs files exist)
- whether validation is strict or warning-only (recommend strict for CI determinism)

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| GitHub Workflows | Orchestrate CI gates | YAML under `.github/workflows/` |
| Repro Kit Actions | Encapsulate repeatable gates | `uses: ./.github/repro-kit/actions/<slug>` |
| Validators | Run schema/lint/test tools | Implemented by action steps (repo-specific tools not confirmed) |
| Artifact outputs | Optional reports for CI | Uploaded by workflows (policy TBD) |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| Action interface (inputs/outputs) | `.github/repro-kit/actions/<slug>/action.yml` | Change requires updating local action README |
| Schema contracts | `schemas/` | Semver + changelog (not enforced here) |
| API contracts | `src/server/` | Contract tests required |

### Extension points checklist (for future work)

- [ ] New action added under `.github/repro-kit/actions/<new-slug>/`
- [ ] `action.yml` includes clear inputs and deterministic behavior
- [ ] Local action `README.md` added with contract + examples
- [ ] Workflow(s) updated to call the action
- [ ] Validation output is stable and does not leak sensitive information

## 🧠 Story Node & Focus Mode Integration

If workflows validate Story Nodes, actions should:

- validate Story Node files under the canonical story node directories (not confirmed in this doc)
- enforce “no unsourced narrative” by requiring provenance-linked claims (implementation depends on story node validator)

## 🧪 Validation & CI/CD

### Validation steps

Recommended minimum gates (as actions or workflow steps):

- [ ] Markdown protocol validation
- [ ] Schema validation (STAC/DCAT/PROV/story nodes/UI registries/telemetry) where applicable
- [ ] Graph integrity checks where applicable
- [ ] API contract tests where applicable
- [ ] Security and sovereignty scanning gates where applicable

### Deterministic skip pattern (recommended)

For any gate targeting an optional root:

- If the target path does not exist, **skip** (exit `0`, log a single-line “SKIP: …”).
- If the target path exists but validation fails, **fail** (exit non-zero, log deterministic diagnostics).
- If the target path exists and validates, **pass** (exit `0`).

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands (not confirmed in repo)
# 1) validate markdown protocol
# 2) validate schemas (STAC/DCAT/PROV/etc.)
# 3) run tests (graph/API/UI as applicable)
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| CI pass/fail/skip counts | GitHub Actions | GitHub run logs (and optionally exported, not confirmed in repo) |
| Validation reports | Actions | As workflow artifacts (optional) |

## ⚖ FAIR+CARE & Governance

### Review gates

Changes that SHOULD trigger maintainer review:

- Any new gate that can block merges
- Any action that processes or logs sensitive data
- Any “security/sovereignty scanning” integration changes

### CARE / sovereignty considerations

- If a validation action touches sovereignty-restricted content, ensure:
  - logs do not reveal restricted locations or sensitive coordinates
  - failure messages remain informative but non-disclosive
  - redaction/generalization behavior is documented

### AI usage constraints

- This doc’s AI permissions/prohibitions must remain aligned with repository governance.
- Actions must not introduce “generated policy” behavior or attempt to infer sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0-draft | 2025-12-22 | Initial scaffolding for repro-kit actions documentation | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
