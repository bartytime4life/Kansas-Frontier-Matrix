---
title: "KFM Reproducibility Kit — Actions"
path: ".github/repro-kit/actions/README.md"
version: "v1.0.0"
last_updated: "2025-12-26"
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

doc_uuid: "urn:kfm:doc:github:repro-kit-actions-readme:v1.0.0"
semantic_document_id: "kfm-github-repro-kit-actions-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github:repro-kit-actions-readme:v1.0.0"
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

> Relationship to `.github/actions/`:
> - `.github/actions/` is the home for **merge-gating CI actions** used by workflows.
> - `.github/repro-kit/actions/` is the home for **reproducibility helpers** (often used in CI *and* locally via repro-kit scripts).  
> If an action is a required PR gate, prefer `.github/actions/` unless there is a strong reason to keep it in the repro-kit.

### Scope

| In scope | Out of scope |
|---|---|
| Composite actions that help reproduce/validate pipeline outputs and artifacts | Handling production secrets, privileged access, or restricted data replays |
| Actions that package run manifests / hash reports / provenance bundles for review | Defining new governance policy (see `docs/governance/*`) |
| Actions used by workflows *and/or* repro-kit scripts to keep steps consistent | Replacing canonical validators/tests owned elsewhere (use wrappers, not duplicates) |

### Audience

- CI maintainers (workflows/actions)
- Repo maintainers + reviewers validating “v12-ready” contributions
- Contributors working on pipelines, catalogs, schemas, graph ingest, APIs, UI, and Story Nodes

### Definitions

(Refer to the repro-kit README for canonical definitions.)

- **Deterministic**: same inputs + same config + same code revision ⇒ same outputs (byte-for-byte when practical).
- **Idempotent**: running the same job twice does not duplicate records or produce inconsistent results.
- **Run manifest**: portable record capturing how to reproduce a run (inputs, config, commit SHA, versions, parameters).
- **PROV bundle**: provenance artifacts describing inputs, activities, outputs, and agents.
- **Stable identifier**: ID that does not change unexpectedly between runs; used to link STAC/DCAT/PROV to graph and UI.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Repro-kit root README | `.github/repro-kit/README.md` | Repo maintainers | Canonical repro-kit intent + constraints |
| Local actions README | `.github/actions/README.md` | CI maintainers | Merge-gating “local actions” guidance |
| Workflows README | `.github/workflows/README.md` | CI maintainers | How workflows map to gates and outputs |
| Master Guide | `docs/MASTER_GUIDE_v12.md` | KFM maintainers | Canonical pipeline ordering + invariants |
| Governance | `docs/governance/` | Governance owners | Ethics + sovereignty rules |
| Schemas / contracts | `schemas/`, `src/server/contracts/` | Contract owners | Validation targets (if present) |

### Definition of done

- [ ] This README is updated whenever repro-kit actions are added/removed/renamed.
- [ ] Each action directory includes `action.yml` and a minimal per-action `README.md`.
- [ ] Actions are deterministic and fail in a consistent, explainable way.
- [ ] Logs/artifacts do not leak restricted locations or culturally sensitive content.
- [ ] Actions do not bypass governance/sensitivity checks; they only automate them.

---

## 🗂️ Directory Layout

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
| MCP runs / experiments | `mcp/` |
| Tests | `tests/` |
| Schemas | `schemas/` |

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
            └── 📁 src/                 # optional helper scripts (avoid large runtimes)
~~~

---

## 🧭 Context

### Background

KFM’s architecture treats reproducibility as a first-class requirement: pipeline steps should be deterministic, logged, and traceable via manifests + provenance artifacts.

This `actions/` directory exists so that:
- CI and local reproduction steps do not drift,
- contributors and reviewers can rerun checks consistently,
- reproducibility artifacts can be packaged for audit-friendly review.

### Assumptions

- The canonical pipeline flow is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- The UI does not read Neo4j directly; the API boundary mediates access and enforces redaction/generalization.
- Contract and schema validation are treated as first-class build gates.

### Constraints / invariants

- Actions in this directory should be **deterministic** and ideally **idempotent**.
- If an action produces artifacts (manifests/reports), outputs must avoid restricted details and remain governance-compliant.
- Prefer “wrapper” actions that call canonical validators/tests rather than re-implementing validation logic.

### Boundary with `.github/actions/`

Use `.github/repro-kit/actions/` when the primary purpose is **reproducibility packaging** or **local/CI parity**.

Use `.github/actions/` when:
- the action is a required merge gate, or
- it is primarily CI glue with no repro-manifest packaging responsibilities.

### Action index

If/when actions are added here, list them below.

| Action | Purpose | Used by | Notes |
|---|---|---|---|
| *(none yet)* |  |  | Add entries as actions land |

---

## 🗺️ Diagrams

> Mermaid rendering note:
> - Avoid unquoted `*` (wildcards) inside node labels.
> - Prefer quoted labels: `NODE["text with / and ( )"]`.

### System / dataflow diagram

~~~mermaid
flowchart LR
  TRIG["PR / Push / workflow_dispatch"] --> WF[".github/workflows/"]

  WF --> GA[".github/actions (merge gates)"]
  WF --> RK[".github/repro-kit/actions (repro helpers)"]

  GA --> V1["Markdown protocol validation"]
  GA --> V2["Schema validation (STAC/DCAT/PROV + Story Nodes)"]
  GA --> V3["Graph integrity tests"]
  GA --> V4["API contract tests"]
  GA --> V5["UI registry schema checks"]
  GA --> V6["Security + sovereignty scans"]

  RK --> M1["Run manifest + hashes"]
  RK --> P1["PROV bundle packaging"]
  RK --> A1["CI artifacts / optional release bundle"]
~~~

---

## 📦 Data & Metadata

### Inputs

| Input | Source | Notes |
|---|---|---|
| Repository checkout | GitHub Actions runner / local checkout | Includes changed files |
| Config + parameters | repo files / workflow inputs | Prefer explicit inputs; avoid hidden defaults |
| Schemas & contracts | `schemas/`, `src/server/contracts/` | May be optional roots depending on repo state |
| Fixtures (optional) | `.github/repro-kit/fixtures/` | Must be safe-to-publish and non-sensitive |

### Outputs

| Output | Where | Notes |
|---|---|---|
| Pass/fail status | GitHub Checks | Fail-closed when required |
| Logs | Actions logs | Keep non-sensitive and actionable |
| Run manifest | CI artifact or repo-standard location | Location and filename conventions may be set in repro-kit root |
| Hash comparison report | CI artifact | Used for deterministic regression checks |
| Optional SBOM / attestations | CI artifact / releases | Only if your repo adopts these practices |

### Naming + storage conventions

- Prefer outputs that can be attached as **workflow artifacts** unless the repo defines a canonical committed location.
- If a committed location is used (e.g., `releases/<version>/...`), ensure governance review if artifacts could expose sensitive data.
- For any artifact that refers to datasets, always prefer stable IDs and provenance-linked references.

---

## 🌐 STAC, DCAT & PROV Alignment

### What actions in this directory may validate

Depending on what exists in the repo snapshot, actions here may validate:

- STAC collections/items under `data/stac/**` (if present)
- DCAT dataset/distribution metadata under `data/catalog/dcat/**` (if present)
- PROV bundles under `data/prov/**` (if present)

### What actions in this directory may emit

Actions here may help package or verify reproducibility artifacts such as:

- run manifests (commit SHA, tool versions, inputs, config)
- checksums/hashes for fixtures and outputs
- PROV bundles that describe activities + entities for the run

> Important: “Packaging” should not change the semantic content of catalog/provenance artifacts; it should only bundle, hash, and report.

### Linking rules

- If an action produces a run manifest, it should include:
  - commit SHA
  - tool/runtime versions
  - input dataset identifiers (not raw sensitive coordinates)
  - output artifact pointers (paths or artifact names)
- If an action touches Story Nodes, ensure every factual claim remains evidence-led and provenance-linked.

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

      # Example repro-kit action usage
      - name: Package run manifest (example)
        uses: ./.github/repro-kit/actions/<action-name>
        with:
          # inputs defined by that action.yml
          output_dir: "repro-artifacts/"
~~~

### Action types supported here

- **Composite actions** (`runs: using: composite`) are recommended for repro-kit orchestration.
- Docker/JS actions are possible but should be justified (runtime constraints, performance, etc.).

### Action documentation expectations

Each action directory should include:

- `action.yml` (required)
- `README.md` explaining:
  - purpose
  - inputs/outputs
  - what constitutes failure
  - where artifacts go
  - how to reproduce locally (if applicable)

### Recommended interface pattern (guidance)

For reproducibility actions, prefer explicit inputs like:

- `target_root` (what to validate/package)
- `artifact_name` / `artifact_dir`
- `fail_on_diff` (for hash comparisons)
- `redaction_mode` (only if repo has a defined policy; otherwise omit)

---

## 🧠 Story Node & Focus Mode Integration

If an action validates Story Nodes or narrative artifacts, it should enforce:

- citations/provenance-linking rules
- entity reference resolution (IDs/links resolve)
- redaction/generalization compliance for restricted material

This supports the invariant that **published narratives must not be unsourced** and that Focus Mode surfaces **provenance-linked** content only.

---

## 🧪 Validation & CI/CD

### Where this fits in CI

Repro-kit actions typically support CI by:

- bundling reproducibility artifacts for review,
- rerunning CI-equivalent checks via shared steps,
- optionally running fixture-based “golden” regression checks.

They should not weaken required CI gates.

### Suggested jobs (examples only)

- Run schema validation for catalogs and metadata
- Run unit/integration tests (pipelines / graph / API / UI)
- Run doc lint and markdown protocol checks
- Optional: rerun a “golden” fixture pipeline and compare hashes

### Reproduction

> Commands below are **examples only** (actual commands are **not confirmed in repo**). Replace with repo-specific scripts/actions.

~~~bash
# 1) run schema validation (STAC/DCAT/PROV)
# <TBD>

# 2) run unit/integration tests
# <TBD>

# 3) run doc lint / markdown protocol validation
# <TBD>

# 4) optional: rerun golden fixture + compare hashes
# <TBD>
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| Repro run id | repro-kit actions/scripts | `mcp/runs/` or CI artifacts |
| Schema validation summary | validators | CI logs |
| Hash comparison report | repro-kit | CI artifacts |

---

## ⚖ FAIR+CARE & Governance

### Review gates

Governance review is required when changes introduce:

- new sensitive layers,
- new AI narrative behaviors,
- new external data sources,
- new public-facing endpoints,
- new behaviors that could expose restricted locations (including via logs/artifacts).

### CARE / sovereignty considerations

- If a reproduction involves culturally sensitive data or restricted locations, document the redaction/generalization behavior.
- CI artifacts must not re-expose restricted geometry or identifiers through logs, manifests, or packaged bundles.

### AI usage constraints

- AI-assisted outputs that surface in user-facing contexts must remain evidence-led and provenance-linked.
- Action logic must not “infer sensitive locations” or “generate policy.”

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-26 | Initial `.github/repro-kit/actions/README.md` scaffold | TBD |

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
---
