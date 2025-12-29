---
title: "KFM GitHub Actions — Local Actions"
path: ".github/actions/README.md"
version: "v1.1.1"
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

doc_uuid: "urn:kfm:doc:github-actions:local-actions-readme:v1.1.1"
semantic_document_id: "kfm-github-actions-local-actions-readme-v1.1.1"
event_source_id: "ledger:kfm:doc:github-actions:local-actions-readme:v1.1.1"
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

# KFM GitHub Actions — Local Actions

## 📘 Overview

### Purpose

- Provide **repo-local, reusable GitHub Actions** under `.github/actions/` that implement CI “gates” and helper steps used by workflows in `.github/workflows/`.
- Encode KFM’s **contract-first, provenance-first** invariants as deterministic checks (schemas, linkage, API boundary, classification propagation), so violations fail fast and consistently.
- Centralize gate logic so contract changes (schemas, API contracts, Story Node rules) update CI **in one place**.

### Scope

| In Scope | Out of Scope |
|---|---|
| Local actions under `.github/actions/` (structure, interface conventions, authoring rules) | Implementing or changing workflows under `.github/workflows/` *(this doc only describes how to call local actions)* |
| Guidance for composite actions that enforce KFM contracts/invariants | Changing the canonical pipeline ordering or subsystem boundaries (see `docs/MASTER_GUIDE_v12.md`) |
| Explicit “skip vs fail” semantics for optional roots | Defining new governance policy (see `docs/governance/*`) |
| Repo lint rules that preserve “one canonical home per subsystem” | Runner provisioning, cloud deployment, and secrets operations |

### Audience

- Primary: CI maintainers and repository maintainers.
- Secondary: Contributors adding/modifying:
  - data artifacts (`data/**`)
  - schemas/contracts (`schemas/**`, `src/server/contracts/**` if present)
  - pipelines (`src/pipelines/**`)
  - graph build/ingest (`src/graph/**`)
  - API (`src/server/**`)
  - UI (`web/**`)
  - Story Nodes (`docs/reports/story_nodes/**`)

### Definitions

#### Glossary (canonical link)

- Link: `docs/glossary.md` *(not confirmed in repo — recommended canonical location)*

#### Terms used in this doc

- **Workflow**: A GitHub Actions workflow YAML file under `.github/workflows/`.
- **Local action**: An action defined in this repo under `.github/actions/<action-name>/`.
- **Composite action**: A local action using `runs: using: "composite"` in `action.yml`.
- **Gate**: A deterministic validation step that fails CI if a required contract/invariant is violated.
- **Helper action**: A deterministic step that supports CI (e.g., changed-file detection, formatting summaries) but does not define a contract boundary by itself.
- **Canonical root**: The one blessed directory for a subsystem (e.g., `src/server/` is the API home).
- **Optional root**: A canonical root that may be absent in a given snapshot (incremental adoption).
- **Skip**: The action exits successfully **without** validating because required inputs are absent *and* `skip_if_missing=true`.
- **Fail**: The action exits non‑zero because validation found violations, or because inputs were required and missing.
- **Classification propagation**: Derived artifacts must not “downgrade” sensitivity/classification without explicit review.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `.github/actions/README.md` | Repo maintainers | Documents the local actions area |
| Workflows | `.github/workflows/` | CI maintainers | Call into local actions |
| CI security policy | `.github/SECURITY.md` | Security owners | If present |
| Master Guide | `docs/MASTER_GUIDE_v12.md` | KFM maintainers | Canonical pipeline + minimum CI gates |
| Markdown work protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | Docs + CI | If present; referenced by Master Guide |
| Templates | `docs/templates/` | Docs | Universal/story/API templates |
| v13 redesign blueprint (draft) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture | If present |
| Schemas | `schemas/` | Contract owners | JSON Schemas for STAC/DCAT/PROV/story/ui/telemetry (if present) |
| Tools | `tools/` | Tooling owners | Validators/utilities invoked by actions (if present) |
| Tests | `tests/` | Engineering | Unit + integration tests (if present) |
| Pipelines | `src/pipelines/` | Data engineering | ETL + catalog generation code |
| Graph | `src/graph/` | Graph/ontology | Graph build + migrations |
| API boundary | `src/server/` | API owners | API + contracts + redaction logic |
| UI | `web/` | UI owners | React + map client + Focus Mode UI |
| Story Nodes | `docs/reports/story_nodes/` | Story owners | Draft/published split if defined (pattern) |
| MCP runs/experiments | `mcp/` | Research + ops | Experiments, runs, model cards, SOPs |

### Definition of done (for this document)

- [ ] Front‑matter complete + valid (`path` matches file location)
- [ ] Mermaid diagrams render (no parse errors)
- [ ] Canonical roots + repo top-levels match `docs/MASTER_GUIDE_v12.md`
- [ ] CI gates list and telemetry signals match Master Guide baseline (any extras are marked optional)
- [ ] “Skip vs fail” semantics are explicit and deterministic
- [ ] Repo lint rules and security/governance constraints are stated
- [ ] Code/tree blocks use `~~~` fences (per KFM Markdown protocol)

---

## 🗂️ Directory Layout

### This document

- `path`: `.github/actions/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| CI | `.github/` | Workflows + local actions + policy gates |
| Workflows | `.github/workflows/` | CI entrypoints (PR, push, scheduled) |
| Local actions | `.github/actions/` | Composite/local actions used by workflows |
| Data domains | `data/` | Staged data + catalog outputs (STAC/DCAT/PROV) |
| Raw inputs | `data/raw/` | Raw source snapshots (by domain) |
| Work inputs | `data/work/` | Intermediate artifacts (by domain) |
| Processed outputs | `data/processed/` | Derived artifacts (by domain) |
| STAC outputs | `data/stac/` | STAC collections + items |
| DCAT outputs | `data/catalog/dcat/` | DCAT datasets/distributions |
| PROV outputs | `data/prov/` | Provenance bundles |
| Documentation | `docs/` | Canonical governed docs (guides, designs, domain notes) |
| Templates | `docs/templates/` | Governed doc templates (universal/story/API) |
| Architecture | `docs/architecture/` | System designs, roadmaps, ADRs (if present) |
| Schemas | `schemas/` | JSON Schemas (STAC/DCAT/PROV/story/ui/telemetry) (if present) |
| Pipelines | `src/pipelines/` | ETL + catalog generation code |
| Graph | `src/graph/` | Ontology bindings + graph build/migrations |
| API boundary | `src/server/` | API service + contracts + redaction logic |
| UI | `web/` | React + map client + Focus Mode UI |
| MCP | `mcp/` | Experiments, runs, model cards, SOPs |
| Tests | `tests/` | Unit + integration tests (if present) |
| Tools | `tools/` | Validators, utilities, QA scripts (if present) |
| Releases | `releases/` | Versioned packaged artifacts (if used) |

### Repo top-levels (context)

The following top-level layout is the **canonical expectation** (some roots may be optional during incremental adoption):

~~~text
📁 .github/
├── 📁 workflows/
├── 📁 actions/
│   ├── 📄 README.md
│   └── 📁 <action-name>/
│       ├── 📄 action.yml
│       └── 📄 README.md
└── 📄 SECURITY.md                         # if present

📁 data/
├── 📁 raw/
│   └── 📁 <domain>/
├── 📁 work/
│   └── 📁 <domain>/
├── 📁 processed/
│   └── 📁 <domain>/
├── 📁 stac/
│   ├── 📁 collections/
│   └── 📁 items/
├── 📁 catalog/
│   └── 📁 dcat/
└── 📁 prov/

📁 docs/
├── 📄 MASTER_GUIDE_v12.md
├── 📁 templates/
│   ├── 📄 TEMPLATE__KFM_UNIVERSAL_DOC.md
│   ├── 📄 TEMPLATE__STORY_NODE_V3.md
│   └── 📄 TEMPLATE__API_CONTRACT_EXTENSION.md
├── 📁 architecture/
│   ├── 📄 KFM_REDESIGN_BLUEPRINT_v13.md   # if present
│   ├── 📄 KFM_NEXT_STAGES_BLUEPRINT.md    # if present
│   └── 📄 KFM_VISION_FULL_ARCHITECTURE.md # if present
└── 📁 reports/
    └── 📁 story_nodes/                    # pattern; draft/published split if defined

📁 mcp/
📁 schemas/                                # if present
📁 src/
📁 tests/                                  # if present
📁 tools/                                  # if present
📁 web/                                    # if present
📁 releases/                               # if present
~~~

### Expected local action layout

~~~text
📁 .github/
├── 📁 workflows/
│   └── 📄 <workflow>.yml
└── 📁 actions/
    ├── 📄 README.md
    ├── 📁 <action-name>/                 # kebab-case; stable name
    │   ├── 📄 action.yml                 # required
    │   ├── 📄 README.md                  # required (inputs/outputs + examples)
    │   ├── 📁 scripts/                   # optional; repo-local only
    │   └── 📁 fixtures/                  # optional; small test fixtures only
    └── 📁 <another-action-name>/
        ├── 📄 action.yml
        └── 📄 README.md
~~~

### Naming, versioning, and documentation conventions

- **Directory names:** use `kebab-case` (e.g., `validate-schemas`, `lint-repo`).
- **Action README required:** every action must document:
  - purpose + which gate(s) it implements
  - inputs/outputs (with defaults)
  - skip vs fail behavior
  - security/sensitivity handling (what it will never print or upload)
  - local reproduction command(s), if applicable
- **Action interface stability:** treat `inputs:` and `outputs:` in `action.yml` as a **public interface**. If you must introduce breaking changes, prefer a new action folder (e.g., `validate-schemas-v2`) over silently changing semantics.
- **No YAML front-matter in code files:** YAML front-matter is for Markdown docs; scripts/configs must not embed `---` front-matter blocks.

### Local actions inventory (recommended)

Maintain a lightweight index of what exists under `.github/actions/`:

| Action folder | Type (gate/helper) | Primary gate | Reads roots | Notes |
|---|---|---|---|---|
| `TBD` | gate | `TBD` | `TBD` | Add one row per action |

---

## 🧭 Context

### CI gates as an explicit part of the KFM architecture

KFM’s repository structure and CI are **compliance mechanisms**, not “nice-to-have” automation:

- Canonical ordering: **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**
- Local actions should enforce contracts at each boundary (schemas, invariants, provenance linkage), so invalid artifacts fail fast.

### Canonical subsystem homes (one home per subsystem)

Local actions should reinforce (not undermine) the “one canonical home per subsystem” rule:

- Pipelines: `src/pipelines/`
- Catalog build/validation tooling: `tools/` and/or `src/pipelines/` (keep one canonical home)
- Graph build: `src/graph/`
- API boundary: `src/server/` (contracts under `src/server/contracts/**` if present)
- UI: `web/`

In particular: **UI code must never read Neo4j/graph storage directly** — all access is via contracted APIs.

### Why local actions?

Local actions are a maintainability and governance tool:

- One gate → one implementation → reused everywhere.
- When a contract changes (schema version, Story Node rules, API contracts), CI logic changes **in one place**.

### What local actions must avoid

Local actions are validation-oriented and should not:

- mutate repository content (unless explicitly part of a dedicated, reviewed workflow)
- rely on network calls that change results over time (unless explicitly documented and pinned)
- emit sensitive content (restricted coordinates, signed URLs, personal data) into logs or artifacts
- perform AI inference over sensitive locations or generate new policy text

### Optional roots and incremental adoption

Some canonical roots may be absent in a given snapshot. Local actions and workflows should follow this rule:

- If a gate depends on a root that is absent, the gate should **skip deterministically** (and log “skipped: missing `<root>`”) *when* `skip_if_missing=true`.
- If the root exists, validation must be **strict** and must fail deterministically when invalid.

Workflows may choose to override skip behavior for release/protected branches by setting `skip_if_missing=false`.

---

## 🗺️ Diagrams

### KFM pipeline ordering and CI gate touchpoints

~~~mermaid
flowchart LR
  ETL["ETL (src/pipelines/)"] --> CAT["Catalog outputs (data/stac/ + data/catalog/dcat/ + data/prov/)"]
  CAT --> GRAPH["Graph build/ingest (src/graph/)"]
  GRAPH --> API["API boundary (src/server/)"]
  API --> UI["UI (web/)"]
  UI --> STORY["Story Nodes (docs/reports/story_nodes/)"]
  STORY --> FOCUS["Focus Mode (provenance-linked only)"]

  subgraph CI["CI gates (via .github/workflows/ + .github/actions/)"]
    G_MD["Markdown protocol + repo lint"]
    G_LINKS["Link/reference checks"]
    G_SCHEMA["Schema validation (STAC/DCAT/PROV/story/ui/telemetry)"]
    G_GRAPH["Graph integrity tests"]
    G_API["API contract tests"]
    G_UI["UI registry + accessibility checks"]
    G_SEC["Security + sovereignty scanning"]
  end

  CI -.-> ETL
  CI -.-> CAT
  CI -.-> GRAPH
  CI -.-> API
  CI -.-> UI
  CI -.-> STORY
~~~

### Workflows → local actions → gates

~~~mermaid
flowchart LR
  PR["Pull Request / Push"] --> WF[".github/workflows/ (workflow files)"]
  WF --> ACT[".github/actions/ (local actions)"]

  ACT --> G1["Markdown protocol + repo lint"]
  ACT --> G2["Link/reference checks"]
  ACT --> G3["Schema validation (STAC/DCAT/PROV + Story Node + UI/telemetry)"]
  ACT --> G4["Graph integrity tests"]
  ACT --> G5["API contract tests (OpenAPI/GraphQL)"]
  ACT --> G6["UI layer registry checks + accessibility gates"]
  ACT --> G7["Security + sovereignty scans (as applicable)"]
~~~

---

## 📦 Data & Metadata

### Inputs

| Input | Source | Notes |
|---|---|---|
| Repository checkout | GitHub Actions runner | Includes PR/push contents |
| Changed-file lists | GitHub context or git diff | Prefer “changed-only” execution for speed |
| Schemas + contracts | `schemas/**`, `src/server/contracts/**` (if present) | Optional roots depending on repo state |
| Data artifacts | `data/**` | Treat outputs as data, not code |
| Story Nodes | `docs/reports/story_nodes/**` | Must remain provenance-linked and governed |

### Outputs

| Output | Where | Notes |
|---|---|---|
| Pass/fail status | GitHub Checks | Blocks merge when required gates fail |
| Logs | GitHub Actions logs | Keep non-sensitive and actionable |
| Step summaries | GitHub job summary | Recommended for human-readable gate output |
| Optional reports/artifacts | Workflow artifacts | Use only when necessary; avoid leaking restricted info |

### Sensitivity handling in CI

- Prefer **counts and identifiers** over full payload dumps in logs (e.g., “3 invalid STAC items”, not full JSON).
- Never upload artifacts that contain:
  - restricted coordinates that should be generalized
  - signed URLs / access tokens / credentials
  - raw personal data (PII) unless repo is explicitly private and governance-approved
- If a gate must handle restricted material, its output should be **explicitly reviewed** by governance owners before being made public.

---

## 🌐 STAC, DCAT & PROV Alignment

Local actions in this directory may validate:

- STAC Collections/Items: `data/stac/**` against `schemas/stac/**` (if present)
- DCAT datasets/distributions: `data/catalog/dcat/**` against `schemas/dcat/**` (if present)
- PROV bundles: `data/prov/**` against `schemas/prov/**` (if present)

Recommended cross-artifact checks (when roots exist):

- **No orphan references:** Story Nodes and graph ingest references must resolve to STAC/DCAT/PROV identifiers.
- **Lineage completeness:** PROV covers raw → work → processed → catalog/graph activities where applicable.
- **Deterministic IDs:** stable identifiers across reruns, to keep diffs meaningful.
- **No downgrades:** no output may be less restricted than any upstream input in its lineage (classification propagation).

> Actions that emit artifacts must ensure those artifacts are safe for logs and do not contain restricted coordinates, signed URLs, or sensitive material.

---

## 🧱 Architecture

### How workflows reference local actions

A workflow step can call a local action via a relative path:

~~~yaml
- name: Run schema validation gate
  uses: ./.github/actions/<action-name>
  with:
    root: "data/stac/"
    skip_if_missing: "true"
~~~

### Local action “gate contract” (recommended standard)

Every gate-style local action should behave like a small service with a clear interface.

**Required:**

- `action.yml` declares inputs, outputs, and `runs: using: "composite"` (preferred).
- `README.md` documents:
  - what the action validates (which gate)
  - which canonical roots it reads
  - what it outputs (logs, summaries, outputs)
  - what “skip” means vs “fail”

**Standard inputs (pattern):**

- `root` / `paths`: what to validate
- `changed_only`: validate only changed files (default: `true` for PRs)
- `skip_if_missing`: skip if the root/path is missing (default: `true` for optional roots)
- `strict`: treat warnings as failures (default: `true`; may be overridden by branch policy)

**Standard outputs (pattern):**

- `skipped`: `true|false`
- `checked_count`: number of files checked (0 when skipped)
- `error_count`: number of errors found

**Logging policy (required):**

- Use GitHub annotations for actionable output:
  - `::notice::` for skips
  - `::warning::` for non-fatal findings (only if `strict=false`)
  - `::error::` for failures
- Prefer a short human-readable summary written to `$GITHUB_STEP_SUMMARY` (counts, next steps), not raw payload dumps.
- Do not print secrets, signed URLs, raw PII, or precise restricted coordinates.

### Composite action skeleton (recommended)

~~~yaml
name: "KFM Gate — <Gate Name>"
description: "Runs the <gate> validation for KFM."
inputs:
  root:
    description: "Root path to validate."
    required: true
  skip_if_missing:
    description: "Skip deterministically if root path does not exist."
    required: false
    default: "true"
  strict:
    description: "Fail on warnings."
    required: false
    default: "true"
outputs:
  skipped:
    description: "Whether the action skipped due to missing inputs."
    value: ${{ steps.run.outputs.skipped }}
  checked_count:
    description: "Number of files checked."
    value: ${{ steps.run.outputs.checked_count }}
  error_count:
    description: "Number of errors found."
    value: ${{ steps.run.outputs.error_count }}
runs:
  using: "composite"
  steps:
    - id: run
      shell: bash
      run: |
        set -euo pipefail
        ROOT="${{ inputs.root }}"

        if [[ "${{ inputs.skip_if_missing }}" == "true" && ! -e "${ROOT}" ]]; then
          echo "skipped=true" >> "$GITHUB_OUTPUT"
          echo "checked_count=0" >> "$GITHUB_OUTPUT"
          echo "error_count=0" >> "$GITHUB_OUTPUT"
          echo "::notice::Skipped: missing ${ROOT}"
          exit 0
        fi

        # Call a repo-local validator (preferred home: tools/ or src/).
        # Replace <command> with the repo’s concrete validator entrypoint.
        # Ensure it returns a non-zero exit code on failure.
        <command> "${ROOT}"

        echo "skipped=false" >> "$GITHUB_OUTPUT"
        echo "checked_count=<tbd>" >> "$GITHUB_OUTPUT"
        echo "error_count=<tbd>" >> "$GITHUB_OUTPUT"
~~~

### Where to put shared validation logic

Prefer to keep “real” validation logic out of workflow YAML:

- **Reusable validators:** `tools/` (preferred) or language-appropriate modules under `src/`.
- **Pipeline-specific checks:** `src/pipelines/` or `src/graph/` (tests under `tests/`).
- **Local actions:** thin wrappers that wire inputs → validator invocation + consistent skip/fail semantics.

### Determinism expectations

- Pin tool versions (via lockfiles) and keep outputs diffable.
- Avoid network calls that change results over time.
- Ensure stable ordering (sort file lists before validating).
- Never mutate the working tree unless explicitly part of a dedicated “format” workflow.

---

## 🧠 Story Node & Focus Mode Integration

Local actions may implement Story Node gates such as:

- validating Story Node structure (front-matter, required sections)
- citations/provenance-linking rules (claims link to evidence identifiers)
- entity reference resolution (IDs/links resolve)
- redaction/generalization compliance for restricted material

This supports the invariant that published narratives must not be unsourced, and that Focus Mode surfaces **provenance-linked** content only.

---

## 🧪 Validation & CI/CD

### Minimum CI gates (baseline)

Workflows should enforce these baseline gates via local actions and/or workflow steps:

- [ ] Markdown protocol validation (front-matter + required sections)
- [ ] Link/reference checks (no orphan pointers)
- [ ] JSON Schema validation:
  - STAC/DCAT/PROV
  - Story Node schemas (if present)
  - telemetry schemas (if present)
  - UI layer registry schemas (if present)
- [ ] Graph integrity tests (constraints, expected labels/edges)
- [ ] API contract tests (OpenAPI/GraphQL schema + resolver tests)
- [ ] Security + sovereignty scanning gates (as applicable):
  - secret scanning
  - PII scanning
  - sensitive-location leakage checks
  - classification propagation checks (no downgrades without review)

### Supply chain integrity (optional for release workflows)

Where this repo uses release workflows, CI/CD may also include supply-chain integrity steps (kept deterministic and pinned):

- **SBOM generation** for build artifacts (stored/published under `releases/` if used).
- **SLSA provenance attestations** for released artifacts.
- Verification gates that ensure provenance and SBOMs are present before publishing.

If adopted, implement these as local actions to keep workflows thin and to standardize logging and skip/fail behavior.

### Repo lint rules (baseline)

Enforce:

- no YAML front-matter in code files (front-matter is for Markdown docs)
- no `README.me`
- no duplicate canonical homes without explicit deprecation markers

### Gate → root mapping (recommended)

| Gate | Canonical roots read | Pipeline stage boundary | Suggested local action | Skip rule |
|---|---|---|---|---|
| Markdown protocol validation | `docs/**`, `.github/**`, `README.md` | Docs/contracts | `validate-markdown-protocol/` | Never skip |
| Link/reference checks | Entire repo | Docs/contracts | `check-links/` | Never skip |
| Schema validation | `schemas/**`, `data/**`, `docs/reports/story_nodes/**`, `web/**` | Catalog + story + UI | `validate-schemas/` | Skip only if `schemas/` absent |
| Graph integrity tests | `src/graph/**`, `tests/**` | Graph | `test-graph-integrity/` | Skip if graph roots absent |
| API contract tests | `src/server/**`, `src/server/contracts/**`, `tests/**` | API boundary | `test-api-contracts/` | Skip if API roots absent |
| UI registry + a11y checks | `web/**`, `schemas/ui/**` | UI | `validate-ui/` | Skip if UI roots absent |
| Security + sovereignty scans | Entire repo (filtered) | Cross-cutting | `security-scan/` | Never skip for secret scanning; other scans may be opt-in |

> Action folder names are a recommendation. If your repo uses different action folder names, keep the mapping consistent and update this table.

### CI behavior principle

- If a gate depends on a root that does not exist in the current repo snapshot, the workflow should **skip** that gate (unless branch policy requires strict enforcement).
- If the root exists, validation must be **strict** and must **fail deterministically** when invalid.

### Local reproduction (pattern)

~~~bash
# Example placeholders — replace with repo-specific validator entrypoints.
# Prefer repo-local commands (tools/ + tests/) over ad-hoc one-liners.

# 1) Markdown protocol checks
# <TBD: tools/validate_markdown_protocol ...>

# 2) Link/reference checks
# <TBD: tools/check_links ...>

# 3) Schema validation (STAC/DCAT/PROV/storynodes/ui/telemetry)
# <TBD: tools/validate_schemas ...>

# 4) Graph integrity tests
# <TBD: pytest -k graph ...>  (or equivalent)

# 5) API contract tests
# <TBD: pytest -k contracts ...> (or equivalent)

# 6) Security + sovereignty scanning
# <TBD: tools/security_scan ...>
~~~

### Telemetry signals (recommended)

If CI emits structured telemetry (optional), keep it schema-validated and store it under a canonical path (e.g., `docs/telemetry/` + `schemas/telemetry/` if present, or `mcp/runs/` for run logs).

Recommended signals:

- `classification_assigned` (dataset_id, sensitivity, classification)
- `redaction_applied` (method, fields_removed, geometry_generalization)
- `promotion_blocked` (reason, scan_results_ref)
- `catalog_published` (scope, counts, validation_status)
- `focus_mode_redaction_notice_shown` (layer_id, redaction_method)

---

## ⚖ FAIR+CARE & Governance

### Review gates

- CI maintainers approve changes to `.github/workflows/` and `.github/actions/`.
- Governance owners review anything that:
  - changes sovereignty handling or redaction behavior
  - affects handling of culturally sensitive or restricted locations
  - introduces new automated inference over sensitive content
  - changes classification/sensitivity metadata, or publishes artifacts derived from restricted inputs

### CARE / sovereignty considerations

- CI must not introduce leakage of restricted coordinates or culturally sensitive material.
- Redaction/generalization must be documented and enforced:
  - in datasets (`data/processed/**`),
  - in catalogs (STAC/DCAT),
  - in API responses (redaction policies),
  - and in UI rendering (CARE gating).
- No output may be less restricted than any upstream input in its lineage.

### AI usage constraints

- Action logic must not infer sensitive locations or generate new governance policy text.
- If an action uses AI tooling (unusual for CI), it must be opt-in and governance-reviewed.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.1.1 | 2025-12-29 | Aligned canonical roots, baseline CI gates, and telemetry signals to Master Guide v12; clarified gate contract and inventory pattern | TBD |
| v1.1.0 | 2025-12-28 | Align gates + repo lint rules with Master Guide v12 and v13 blueprint; expanded action contract conventions | TBD |
| v1.0.0 | 2025-12-22 | Initial README for local actions | TBD |

---

Footer refs:

- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Templates: `docs/templates/`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`