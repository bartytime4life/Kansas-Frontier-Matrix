---
title: "KFM Reproducibility Kit — Actions"
path: ".github/repro-kit/actions/README.md"
version: "v1.0.1"
last_updated: "2025-12-29"
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

doc_uuid: "urn:kfm:doc:github:repro-kit-actions-readme:v1.0.1"
semantic_document_id: "kfm-github-repro-kit-actions-readme-v1.0.1"
event_source_id: "ledger:kfm:doc:github:repro-kit-actions-readme:v1.0.1"
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

# KFM Reproducibility Kit — Actions

## 📘 Overview

### Purpose

This directory contains **repo-local GitHub Actions** under `.github/repro-kit/actions/` that support the **reproducibility promise** of the KFM pipeline:

- run **CI-equivalent checks** in a repeatable, reusable way,
- package and/or validate **run manifests**, checksums, and provenance artifacts,
- optionally rerun “golden” fixtures and compare hashes for deterministic regression testing.

### Relationship to `.github/actions`

Use `.github/actions/` for **merge-gating** actions that are core PR checks.

Use `.github/repro-kit/actions/` for **reproducibility helpers** that provide CI/local parity and artifact packaging (and may be called by workflows and/or local repro-kit scripts).

If an action becomes a required PR gate, prefer making its interface available under `.github/actions/` while keeping any heavy logic in a single canonical script location (for example `tools/**`, `src/pipelines/**`, `src/graph/**`) to avoid drift.

### Scope

| In scope | Out of scope |
|---|---|
| Composite actions that help reproduce/validate pipeline outputs and artifacts | Handling production secrets, privileged access, or restricted-data replays |
| Actions that package run manifests / hash reports / provenance bundles for review | Defining new governance policy (see `docs/governance/*`) |
| Wrapper actions that call canonical validators/tests (avoid duplicating logic) | Replacing canonical validators/tests owned elsewhere |

### Audience

- CI maintainers (workflows/actions)
- Repo maintainers + reviewers validating “v12-ready” contributions
- Contributors working on pipelines, catalogs, schemas, graph ingest, APIs, UI, and Story Nodes

### Definitions

- **Deterministic**: same inputs + same config + same code revision ⇒ same outputs (byte-for-byte when practical).
- **Statistically reproducible**: when byte-for-byte output is not practical (for example floating-point variance), results match within a documented tolerance/acceptance rule.
- **Idempotent**: running the same job twice does not duplicate records or produce inconsistent results.
- **Run manifest**: portable record capturing how to reproduce a run (inputs, config, commit SHA, versions, parameters).
- **PROV bundle**: provenance artifacts describing inputs, activities, outputs, and agents.
- **Stable identifier**: ID that does not change unexpectedly between runs; used to link STAC/DCAT/PROV to graph and UI.

### Core invariants this directory helps enforce

These are KFM-wide “do not regress” rules. Actions here may validate and/or package evidence to prove compliance:

1. **Canonical ordering is non-negotiable:** ETL → STAC/DCAT/PROV → Graph → API boundary → UI → Story Nodes → Focus Mode.
2. **API boundary:** UI never reads Neo4j directly; all access is via contracted APIs.
3. **Provenance-first:** STAC/DCAT/PROV are produced and validated before graph ingest and before UI/narrative surfacing.
4. **Contract-first:** schemas + API contracts are first-class artifacts; breaking changes require versioning and compatibility tests.
5. **Evidence-first narrative:** Story Nodes and Focus Mode must not surface unsourced narrative.
6. **Sovereignty and classification propagation:** no output is less restricted than any input in its lineage; UI must not leak sensitive locations by interaction.
7. **Reproducibility discipline:** runs are traceable to code + config + inputs; artifacts include hashes and tool versions.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Repro-kit root README | `.github/repro-kit/README.md` | Repo maintainers | Canonical repro-kit intent + constraints |
| Merge-gating local actions README | `.github/actions/README.md` | CI maintainers | How “local actions” are used by workflows |
| Workflows README | `.github/workflows/README.md` | CI maintainers | How workflows map to gates and outputs |
| Master Guide | `docs/MASTER_GUIDE_v12.md` | KFM maintainers | Canonical pipeline ordering + invariants |
| Governance | `docs/governance/` | Governance owners | Ethics + sovereignty rules |
| Schemas | `schemas/` | Contract owners | JSON schemas (STAC/DCAT/PROV/story/ui/telemetry) |
| API contracts | `src/server/contracts/` | Contract owners | Contract-first boundary (if present) |
| Markdown work protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | Docs | *not confirmed in repo* |

### Definition of done

- [ ] This README is updated whenever repro-kit actions are added/removed/renamed.
- [ ] Each action directory includes `action.yml` and a minimal per-action `README.md`.
- [ ] Actions are deterministic or explicitly “statistically reproducible” with documented tolerance rules.
- [ ] Actions are idempotent where they write artifacts (no duplicate IDs; predictable paths).
- [ ] Actions fail closed with actionable error messages (no silent skips).
- [ ] Artifacts/logs do not leak restricted locations, culturally sensitive content, secrets, or PII.
- [ ] Actions do not bypass governance/sensitivity checks; they automate and enforce them.
- [ ] Action interfaces are stable (inputs/outputs versioned if changed).

---

## 🗂️ Directory layout

### This document

| Artifact | Path |
|---|---|
| Actions README | `.github/repro-kit/actions/README.md` |

### Related repository paths

| Area | Canonical path |
|---|---|
| Repro-kit root | `.github/repro-kit/README.md` |
| Workflows | `.github/workflows/` |
| Merge-gating local actions | `.github/actions/` |
| Pipelines | `src/pipelines/` |
| STAC catalogs | `data/stac/` |
| DCAT catalogs | `data/catalog/dcat/` |
| PROV bundles | `data/prov/` |
| Graph build/migrations | `src/graph/` |
| API boundary | `src/server/` |
| UI | `web/` |
| Story Nodes | `docs/reports/story_nodes/` |
| MCP runs / experiments | `mcp/` |
| Tests | `tests/` |
| Schemas | `schemas/` |
| Tooling | `tools/` |

### Expected file tree for this sub-area

~~~text
📁 .github/
└── 📁 repro-kit/
    ├── 📄 README.md
    └── 📁 actions/
        ├── 📄 README.md
        └── 📁 <action-name>/
            ├── 📄 action.yml
            ├── 📄 README.md
            ├── 📁 src/                 # optional helper scripts (avoid large runtimes)
            └── 📁 fixtures/             # optional; must be safe-to-publish + non-sensitive
~~~

### Naming conventions

- Action directories use **kebab-case**: `<verb>-<object>` (example: `package-run-manifest`).
- Prefer stable names; if you must rename, provide a migration note and update workflows that reference it.
- If an action is intended to be reusable outside this repo, keep its interface generic; otherwise, make KFM-specific assumptions explicit in the action README.

---

## 🧾 Action index

List actions in this directory here as they land.

| Action | Purpose | Used by | Notes |
|---|---|---|---|
| *(none yet)* |  |  | Add entries as actions land |

---

## 🧩 Adding a new action

Use this checklist to keep actions consistent, discoverable, and governance-safe.

### Steps

1. Create the action directory under `.github/repro-kit/actions/<action-name>/`.
2. Add an `action.yml` with a stable input/output surface.
3. Add an action-local `README.md` that documents usage, artifacts, and failure modes.
4. Update the **Action index** table in this file.
5. Wire the action into `.github/workflows/**` and/or repro-kit root scripts as needed.
6. Ensure logs and artifacts are safe to publish (no secrets, no restricted locations, no PII).
7. If the action validates governed artifacts (STAC/DCAT/PROV/story/ui/contracts), ensure it calls canonical validators rather than re-implementing logic.

### Minimal `action.yml` skeleton

~~~yaml
name: "KFM — <Action Name>"
description: "<One sentence purpose>"

inputs:
  artifact_dir:
    description: "Where to write artifacts for upload (workflow artifact staging)."
    required: true

outputs:
  manifest_path:
    description: "Path to the generated run manifest."
    value: ${{ steps.<step_id>.outputs.manifest_path }}

runs:
  using: "composite"
  steps:
    - name: "Run validator or packager"
      id: <step_id>
      shell: bash
      run: |
        set -euo pipefail
        # Call canonical scripts/validators here (tools/**, src/pipelines/**, etc.)
        # Emit outputs for downstream steps.
~~~

---

## 🧭 Context

### Background

KFM treats reproducibility as a first-class requirement: pipeline steps are deterministic where possible, logged, and traceable via run manifests + provenance artifacts.

This `actions/` directory exists so that:

- CI and local reproduction steps do not drift,
- contributors and reviewers can rerun checks consistently,
- reproducibility artifacts can be packaged for audit-friendly review.

### Assumptions

- The canonical pipeline flow is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- The UI does not read Neo4j directly; the API boundary mediates access and enforces redaction/generalization.
- Schema and contract validation are treated as first-class build gates.

### Constraints and invariants

- Actions in this directory should be deterministic and ideally idempotent.
- Actions must not write derived catalogs or pipeline artifacts into `docs/**`. Catalogs belong under `data/**`.
- Prefer “wrapper” actions that call canonical validators/tests rather than re-implementing validation logic.
- Artifacts must avoid restricted details and remain governance-compliant.

---

## 🗺️ Diagrams

> Mermaid rendering note: avoid unquoted `*` (wildcards) inside node labels. Prefer quoted labels like `NODE["text with / and ( )"]`.

### System and dataflow diagram

~~~mermaid
flowchart LR
  TRIG["PR / Push / workflow_dispatch"] --> WF[".github/workflows/"]

  WF --> GA[".github/actions — merge gates"]
  WF --> RK[".github/repro-kit/actions — repro helpers"]

  GA --> V1["Markdown protocol validation"]
  GA --> V2["Schema validation (STAC/DCAT/PROV + Story Nodes)"]
  GA --> V3["Graph integrity tests"]
  GA --> V4["API contract tests"]
  GA --> V5["UI registry schema checks"]
  GA --> V6["Security + sovereignty scans"]

  RK --> M1["Run manifest + hashes"]
  RK --> P1["PROV bundle packaging"]
  RK --> A1["CI artifacts bundle"]
~~~

### Action placement decision diagram

~~~mermaid
flowchart TD
  Q1["Is this a required PR merge gate?"] -->|Yes| A1["Place under .github/actions"]
  Q1 -->|No| Q2["Is the goal packaging or local/CI parity?"]
  Q2 -->|Yes| A2["Place under .github/repro-kit/actions"]
  Q2 -->|No| Q3["Is this a validator/test owned by a subsystem?"]
  Q3 -->|Yes| A3["Keep logic in tools/** or subsystem; wrap from an action"]
  Q3 -->|No| A4["Document rationale; prefer smallest runtime + stable interface"]
~~~

---

## 📦 Data and metadata

### Inputs

| Input | Source | Notes |
|---|---|---|
| Repository checkout | GitHub Actions runner / local checkout | Includes changed files |
| Config + parameters | repo files / workflow inputs | Prefer explicit inputs; avoid hidden defaults |
| Schemas & contracts | `schemas/`, `src/server/contracts/` | May be optional roots depending on repo state |
| Fixtures | `.github/repro-kit/fixtures/` or per-action `fixtures/` | Must be safe-to-publish and non-sensitive |

### Outputs

| Output | Where | Notes |
|---|---|---|
| Pass/fail status | GitHub Checks | Fail closed when required |
| Logs | Actions logs | Keep non-sensitive and actionable |
| Run manifest | Workflow artifact | Capture code + config + inputs + versions |
| Hash report | Workflow artifact | Supports deterministic regression checks |
| PROV bundle | `data/prov/**` or workflow artifact | Prefer linking rather than duplicating payloads |
| Optional attestations | Workflow artifact / releases | Only if adopted by the repo |

### Run manifest minimum fields

Actions that emit a run manifest should include (at minimum):

- `run_id` (workflow run ID or equivalent)
- `git` (commit SHA, branch/ref)
- `runner` (OS, architecture)
- `tool_versions` (language runtime + key tools/validators)
- `inputs` (stable IDs and paths; avoid sensitive coordinates)
- `outputs` (artifact names/paths; STAC/DCAT/PROV identifiers when applicable)
- `reproducibility_mode` (`deterministic` | `statistical`) and, if statistical, the tolerance rule used

---

## 🌐 STAC, DCAT and PROV alignment

### What actions here may validate

Depending on what exists in the repo snapshot, actions here may validate:

- STAC collections/items under `data/stac/**`
- DCAT dataset/distribution metadata under `data/catalog/dcat/**`
- PROV bundles under `data/prov/**`
- Story Node schemas and citation rules (when Story Nodes are changed)
- UI layer registry schemas (when UI registry files are changed)

### What actions here may emit

Actions here may help package or verify reproducibility artifacts such as:

- run manifests (commit SHA, tool versions, inputs, config)
- checksums/hashes for fixtures and outputs
- PROV bundles that describe activities + entities for the run

Important: “packaging” must not change the semantic content of catalog/provenance artifacts; it should only bundle, hash, and report.

### Linking rules

- Actions that produce a run manifest should link to stable identifiers wherever possible:
  - STAC Collection/Item IDs
  - DCAT dataset IDs
  - PROV bundle/activity IDs
- Actions should prefer pointers and identifiers over duplicating large payloads (especially for evidence artifacts).
- If an action touches Story Nodes, it must preserve evidence-first constraints: every factual claim remains provenance-linked.

---

## 🧱 Architecture

### How workflows reference these actions

Reference repo-local actions via relative paths:

~~~yaml
jobs:
  repro:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Package run manifest
        uses: ./.github/repro-kit/actions/<action-name>
        with:
          artifact_dir: "repro-artifacts/"
~~~

### Action types supported here

- Composite actions are recommended for orchestration and parity.
- Docker/JS actions are possible but should be justified with runtime and maintainability constraints.

### Action documentation expectations

Each action directory should include:

- `action.yml` (required)
- `README.md` describing:
  - purpose
  - inputs/outputs
  - failure modes and exit codes
  - where artifacts go and how they are named
  - how to reproduce locally if the repo supports it

### Recommended interface pattern

For reproducibility actions, prefer explicit inputs like:

- `target_root` (what to validate/package)
- `artifact_name` and `artifact_dir`
- `fail_on_diff` (for hash comparisons)
- `reproducibility_mode` (`deterministic` | `statistical`)
- `tolerance_rule` (only when statistical mode is used)

---

## 🧠 Story Node and Focus Mode integration

If an action validates Story Nodes or narrative artifacts, it should enforce:

- citations and provenance-linking rules
- entity reference resolution (IDs/links resolve)
- redaction/generalization compliance for restricted material

This supports the invariant that published narratives must not be unsourced and that Focus Mode surfaces provenance-linked content only.

---

## 🧪 Validation and CI/CD

### Minimum CI gates for v12-ready contributions

Repro-kit actions should support and must never weaken the minimum CI gates used to keep KFM v12-ready:

- Markdown protocol validation (front-matter + required sections)
- Link/reference checks (no orphan pointers)
- JSON schema validation:
  - STAC/DCAT/PROV
  - story node schemas (if present)
  - telemetry schemas (if present)
  - UI layer registry schemas (if present)
- Graph integrity tests (constraints, expected labels/edges)
- API contract tests (OpenAPI/GraphQL schema + resolver tests)
- Security + sovereignty scanning gates:
  - secret scan
  - PII scan
  - sensitive-location leakage checks
  - classification propagation checks

### Validation ownership map

Actions in this directory should generally wrap validators owned by the relevant subsystem:

| Gate | Canonical owner | Typical code home | Typical data home |
|---|---|---|---|
| Markdown protocol + link checks | Docs/CI | `tools/**` and/or `.github/actions/**` | n/a |
| STAC/DCAT/PROV schema validation | Data/Catalog | `tools/**` or `src/pipelines/**` | `data/stac/**`, `data/catalog/dcat/**`, `data/prov/**` |
| Graph integrity tests | Graph | `src/graph/**`, `tests/**` | `data/graph/**` |
| API contract tests | API | `src/server/**`, `tests/**` | n/a |
| UI registry schema checks | UI | `web/**`, `schemas/ui/**`, `tests/**` | n/a |
| Governance scans | Governance/CI | `.github/**`, `tools/**` | n/a |
| Repro packaging | Repro-kit | `.github/repro-kit/**` | workflow artifacts, `mcp/runs/**` |

### Suggested jobs

The job list below is illustrative; the exact workflow design depends on repo conventions:

- Validate markdown protocol + internal link references
- Validate schemas for STAC/DCAT/PROV/story/ui/telemetry as applicable
- Run graph integrity constraints/tests if graph artifacts changed
- Run API contract tests if contracts changed
- Run UI tests and accessibility checks if UI changed
- Package a run manifest + hash report for reviewer audit

### Local reproduction

Local reproduction commands, wrappers, or scripts should live in the repro-kit root and call the same underlying validators as CI. If local reproduction is not supported yet, add a short note in `.github/repro-kit/README.md` describing the intended approach.

### Telemetry signals

If your repo captures telemetry, the following signals are recommended for reproducibility and governance auditing:

| Signal | Suggested fields | Where recorded |
|---|---|---|
| `catalog_published` | scope, counts, validation_status | CI logs / run manifest |
| `classification_assigned` | dataset_id, sensitivity, classification | run manifest / audit log |
| `redaction_applied` | method, fields_removed, geometry_generalization | run manifest / PROV |
| `promotion_blocked` | reason, scan_results_ref | CI logs |
| `focus_mode_redaction_notice_shown` | layer_id, redaction_method | UI telemetry |

---

## ⚖ FAIR+CARE and governance

### Governance review triggers

Governance review is required when changes introduce:

- new sensitive layers or content intersecting sovereignty obligations,
- new AI narrative behaviors or automated summarization that could be interpreted as “fact,”
- new external data sources (license/provenance review),
- new public-facing endpoints or layer interactions that could reveal sensitive locations,
- any classification/sensitivity change or publication derived from restricted inputs.

### CARE and sovereignty considerations

- If a reproduction run involves culturally sensitive data or restricted locations, document the redaction/generalization behavior in the run manifest and ensure artifacts do not re-expose restricted geometry or identifiers.
- Ensure classification propagation checks are enforced: outputs must not be less restricted than any input in their lineage.

### AI usage constraints

- Actions must not generate policy or infer sensitive locations.
- Any AI-assisted outputs that surface in user-facing contexts must remain evidence-led and provenance-linked.
- Any opt-in AI summaries must include uncertainty metadata and must be excluded from Focus Mode by default.

---

## 🕰️ Version history

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-26 | Initial `.github/repro-kit/actions/README.md` scaffold | TBD |
| v1.0.1 | 2025-12-29 | Aligned with Master Guide v12 invariants + CI gates; clarified action interfaces and governance expectations | TBD |

---

Footer refs:

- Repro-kit root: `.github/repro-kit/README.md`
- Local actions: `.github/actions/README.md`
- Workflows: `.github/workflows/README.md`
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Templates: `docs/templates/`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
