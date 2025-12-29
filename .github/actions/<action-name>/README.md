---
title: "KFM Local Action — <action-name>"
path: ".github/actions/<action-name>/README.md"
version: "v1.0.0"
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

doc_uuid: "urn:kfm:doc:github-actions:local-action:<action-name>:readme:v1.0.0"
semantic_document_id: "kfm-github-action-<action-name>-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github-actions:local-action:<action-name>:readme:v1.0.0"
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

# KFM Local Action — <action-name>

Quick links:

- Local action definition: `.github/actions/<action-name>/action.yml`
- Local actions index: `.github/actions/README.md`
- Master Guide: `docs/MASTER_GUIDE_v12.md`

---

## 📘 Overview

### Purpose

- Define the **contract** (inputs/outputs + behavior) for the local GitHub Action located at `.github/actions/<action-name>/`.
- Ensure CI gate behavior is **deterministic**, **contract-first**, and aligned with the canonical KFM pipeline ordering:
  **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**.
- Standardize **skip vs fail** semantics so workflows can compose gates reliably across optional subsystem roots.

### Scope

| In Scope | Out of Scope |
|---|---|
| Action contract documentation (inputs/outputs, skip/fail, strictness) | Changing workflows under `.github/workflows/` |
| Security/sensitivity handling in logs and artifacts | Defining new governance policy (see `docs/governance/*`) |
| Local reproduction commands for this gate | Runner provisioning, secrets ops, cloud deployment |
| Determinism expectations (pinned versions, stable ordering) | Any UI that reads Neo4j directly (disallowed; UI uses contracted APIs only) |

### Audience

- Primary: CI maintainers and repository maintainers.
- Secondary: Contributors modifying any of:
  - `data/**` (raw/work/processed + catalogs)
  - `schemas/**` *(if present)*
  - `src/pipelines/**`
  - `src/graph/**`
  - `src/server/**`
  - `web/**`
  - `docs/reports/story_nodes/**`

### Definitions (link to glossary)

- Link: `docs/glossary.md` *(not confirmed in repo — recommended canonical location)*

Terms used in this doc:

- **Local action**: An action defined in this repo under `.github/actions/<action-name>/`.
- **Gate**: A validation step that fails CI when a required KFM contract or invariant is violated.
- **Optional root**: A canonical root that may be absent in an incremental-adoption snapshot.
- **Deterministic skip**: A predictable, non-failing “skip” outcome based on declared conditions (e.g., missing root + `skip_if_missing=true`).
- **Strict mode**: Treat warnings as failures (workflow/branch may override).

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `.github/actions/<action-name>/README.md` | CI maintainers | Action contract + usage |
| Action definition | `.github/actions/<action-name>/action.yml` | CI maintainers | Inputs/outputs + composite steps |
| Workflows calling this action | `.github/workflows/*.yml` | CI maintainers | Invoke the gate |
| Validator entrypoint | `<TBD: tools/** or src/**>` | Contract owners | Prefer `tools/` for reusable validators *(if present)* |
| Master Guide | `docs/MASTER_GUIDE_v12.md` | KFM maintainers | Pipeline ordering + minimum gates |
| Templates | `docs/templates/` | Docs | Universal/story/API templates |
| Governance | `docs/governance/*` | Governance owners | FAIR+CARE, sovereignty, ethics |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] Inputs/outputs table matches `action.yml`
- [ ] Skip vs fail semantics explicit (deterministic and testable)
- [ ] Local reproduction command(s) provided (repo-local, pinned)
- [ ] Logs/artifacts handling documented (no sensitive leakage)
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

---

## 🗂️ Directory Layout

### This document

- `path`: `.github/actions/<action-name>/README.md` *(must match front-matter)*

### Expected action folder layout

~~~text
📁 .github/
└── 📁 actions/
    ├── 📄 README.md                          # local actions index
    └── 📁 <action-name>/
        ├── 📄 action.yml                     # required
        ├── 📄 README.md                      # required (this file)
        ├── 📁 scripts/                       # optional; repo-local only
        │   └── 📄 <helper_script>.<ext>
        └── 📁 fixtures/                      # optional; small test fixtures only
            └── 📄 <fixture-file>
~~~

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| CI | `.github/` | Workflows + local actions + policy gates |
| Workflows | `.github/workflows/` | CI entrypoints (PR, push, scheduled) |
| Local actions | `.github/actions/` | Repo-local actions used by workflows |
| Tools | `tools/` | Validators/utilities invoked by actions *(if present)* |
| Tests | `tests/` | Unit + integration tests *(if present)* |
| Schemas | `schemas/` | JSON Schemas (STAC/DCAT/PROV/story/ui/telemetry) *(if present)* |
| Pipelines | `src/pipelines/` | ETL + catalog generation code |
| Graph | `src/graph/` | Graph build/migrations |
| API boundary | `src/server/` | API service + contracts + redaction logic |
| UI | `web/` | React + map client + Focus Mode UI |
| Story Nodes | `docs/reports/story_nodes/` | Governed narratives (draft/published) |

---

## 🧭 Context

### Where this action fits

This action implements a **single CI gate** (or a cohesive sub-gate) that enforces one or more KFM contracts/invariants at a pipeline boundary.

- If the gate validates catalogs: boundary is **ETL → STAC/DCAT/PROV**.
- If the gate validates graph ingest: boundary is **Catalog → Graph**.
- If the gate validates API contracts: boundary is **Graph → API**.
- If the gate validates UI registry/a11y: boundary is **API → UI**.
- If the gate validates Story Nodes: boundary is **UI → Story Nodes → Focus Mode** (provenance-linked only).

### Canonical invariants this action must not violate

- **Contract-first:** schemas + contracts are first-class; breaking changes require compat tests/version bumps.
- **Determinism:** idempotent runs, stable IDs, stable ordering, pinned tool versions.
- **One canonical home per subsystem:** avoid duplicating schema/logic across multiple roots.
- **API boundary:** UI never reads Neo4j directly; all access is via contracted APIs.
- **Focus Mode hard gate:** provenance-linked content only; no unsourced narrative.

---

## 🗺️ Diagrams

### Workflow → local action → validator

~~~mermaid
flowchart LR
  WF[".github/workflows/<workflow>.yml"] --> ACT[".github/actions/<action-name> (composite)"]
  ACT --> VAL["Repo-local validator (tools/** or src/**)"]
  VAL --> OUT["GitHub outputs + step summary + pass/fail"]
~~~

### Skip vs fail decision path

~~~mermaid
flowchart TD
  A["Start"] --> B["Does <root> exist?"]
  B -->|No| C["skip_if_missing == true ?"]
  C -->|Yes| S["SKIP (exit 0) + ::notice:: + outputs.skipped=true"]
  C -->|No| F1["FAIL (exit !=0) + actionable error"]
  B -->|Yes| D["Collect file set (changed_only or full)"]
  D --> E["Run validator deterministically"]
  E -->|Errors| F2["FAIL (exit !=0) + counts + links"]
  E -->|No errors| P["PASS (exit 0) + summary"]
~~~

---

## 📦 Data & Metadata

### Inputs

| Input | Source | Notes |
|---|---|---|
| Repository checkout | `actions/checkout` | Must run before this action |
| `with:` inputs (strings) | Workflow step | See “Action Contract” below |
| Changed-file list (optional) | `git diff` / GitHub context | Used when `changed_only=true` |
| Schemas/contracts (optional) | `schemas/**`, `src/server/contracts/**` | Only if this gate validates them |
| Data artifacts (optional) | `data/**` | Treat as data; do not mutate |

### Outputs

| Output | Where | Notes |
|---|---|---|
| Pass/fail | GitHub Checks | Fails when required contracts are violated |
| Step summary | `$GITHUB_STEP_SUMMARY` | Human-readable gate results (preferred) |
| Action outputs | `$GITHUB_OUTPUT` | For workflow composition (e.g., `skipped=true`) |
| Optional artifacts | Workflow artifacts | Use sparingly; avoid sensitive leakage |

### Sensitivity handling in CI

This action must:

- Prefer **counts + identifiers** over full payload dumps (e.g., “3 invalid items” rather than full JSON).
- Never print or upload:
  - restricted coordinates that should be generalized
  - signed URLs / access tokens / credentials
  - raw personal data (PII) unless repo is explicitly private and governance-approved

If the validator touches restricted material, ensure its outputs are **reviewable** without exposing the restricted content.

---

## 🌐 STAC, DCAT & PROV Alignment

Fill out this section **only if** this action validates catalogs or provenance.

### What this action validates (if applicable)

- STAC: `data/stac/**` (Collections + Items) against `schemas/stac/**` *(if present)*
- DCAT: `data/catalog/dcat/**` against `schemas/dcat/**` *(if present)*
- PROV: `data/prov/**` against `schemas/prov/**` *(if present)*

### Recommended cross-artifact checks (if applicable)

- No orphan references (Story Nodes and graph ingest references resolve to catalog identifiers).
- Lineage completeness (PROV covers raw → work → processed → publish where applicable).
- Deterministic IDs (stable identifiers across reruns to keep diffs meaningful).

---

## 🧱 Architecture

## Action snapshot

- **Action folder:** `.github/actions/<action-name>/`
- **Gate name:** `<gate-name>`
- **Pipeline boundary:** `<ETL | Catalog | Graph | API | UI | Story>`
- **Primary roots read:** `<e.g., data/stac/, schemas/, docs/reports/story_nodes/>`
- **Validator entrypoint:** `<e.g., tools/<validator> or python -m <module>>`
- **Does the action mutate the repo?** `No` (default expectation)

### How workflows call this action

~~~yaml
- name: Run <gate-name>
  uses: ./.github/actions/<action-name>
  with:
    root: "<path-to-validate>"
    changed_only: "true"
    skip_if_missing: "true"
    strict: "true"
~~~

### Local action contract

GitHub Action inputs are strings. Keep the contract stable; changes require version bump and workflow updates.

#### Inputs

| Input | Required | Default | Example | Description |
|---|---:|---|---|---|
| `root` | ✅ | (none) | `data/stac/` | Root path to validate |
| `paths` | ❌ | (empty) | `schemas/**,data/**` | Optional comma-separated glob list; overrides/extends `root` |
| `changed_only` | ❌ | `true` | `false` | Validate only changed files (PRs) vs full run |
| `skip_if_missing` | ❌ | `true` | `true` | Skip deterministically if `root` (or all `paths`) do not exist |
| `strict` | ❌ | `true` | `false` | Treat warnings as failures |
| `fail_level` | ❌ | `error` | `warning` | Minimum severity that fails the gate (recommended values: `error`, `warning`) |

> If your action does not implement one of these inputs, remove it from this table and ensure `README.md` matches `action.yml`.

#### Outputs

| Output | Type | Description |
|---|---|---|
| `skipped` | `true|false` | Whether the action skipped due to missing inputs/roots |
| `checked_count` | integer-ish string | Number of files checked (or units validated) |
| `error_count` | integer-ish string | Number of errors |
| `warning_count` | integer-ish string | Number of warnings (if tracked) |
| `report_ref` | string | Optional: path/identifier for a report artifact (do not include sensitive data) |

> Ensure these outputs exactly match `action.yml` output mappings.

### Skip vs fail semantics

This action must implement deterministic behavior:

| Scenario | `skip_if_missing` | Expected result | `outputs.skipped` |
|---|---:|---|---|
| `root`/`paths` missing | true | **SKIP** (exit 0 + `::notice::Skipped: missing <root>`) | true |
| `root`/`paths` missing | false | **FAIL** (exit != 0 + actionable message) | false |
| Inputs present; validator returns errors | any | **FAIL** | false |
| Inputs present; validator returns warnings only | `strict=true` | **FAIL** | false |
| Inputs present; validator returns warnings only | `strict=false` | **PASS** (log warnings) | false |
| Inputs present; no files matched (changed-only) | any | **PASS** (exit 0 + notice) | false |

### Determinism expectations

- Pin tool versions (lockfiles; avoid “latest” installs).
- Avoid network calls that change results over time.
- Sort file lists before validating.
- Never mutate the working tree unless explicitly part of a dedicated, reviewed workflow.

### Implementation notes (recommended)

- Write a concise gate summary to `$GITHUB_STEP_SUMMARY` (counts + links).
- Write stable outputs to `$GITHUB_OUTPUT`.
- If invoking scripts, keep them repo-local under `tools/` or `src/` (actions should be thin wrappers).

Example step-summary pattern:

~~~bash
{
  echo "### <gate-name>"
  echo ""
  echo "- Root: \`${ROOT}\`"
  echo "- Checked: ${CHECKED_COUNT}"
  echo "- Errors: ${ERROR_COUNT}"
  echo "- Warnings: ${WARNING_COUNT}"
  echo "- Skipped: ${SKIPPED}"
} >> "$GITHUB_STEP_SUMMARY"
~~~

---

## 🧠 Story Node & Focus Mode Integration

Fill out this section **only if** this action validates Story Nodes or Focus Mode constraints.

### Supported checks (examples)

- Story Node structure (front-matter + required sections)
- Evidence/citation linkage (claims point to catalog identifiers)
- “Fact vs inference vs hypothesis” separation (especially for AI-generated text)
- Sensitive location leakage checks (no restricted coordinates in narrative output)

### Focus Mode rule (hard gate)

- Focus Mode consumes **provenance-linked** content only.
- Any predictive/suggestive content must be opt-in, include uncertainty metadata, and must not infer sensitive locations.

---

## 🧪 Validation & CI/CD

### Gate(s) implemented by this action

- Gate name: `<gate-name>`
- Contract(s) enforced:
  - `<e.g., JSON schema validation>`
  - `<e.g., link/reference integrity>`
  - `<e.g., API contract compatibility>`
  - `<e.g., Story Node provenance rules>`

### Local reproduction

Prefer repo-local, pinned commands. Replace placeholders with your actual validator entrypoint.

~~~bash
# Example:
#   tools/validate_<thing> --root "<root>" --strict true --changed-only false
#
# Required: deterministic behavior, stable ordering, no network dependence unless explicitly documented.

<validator-command> --root "<root>" --strict "<true|false>" --changed-only "<true|false>"
~~~

### Tests

If this action has non-trivial logic:

- Add unit/integration tests under `tests/` *(if present)* for the validator (not just the action wrapper).
- Include small fixtures under `.github/actions/<action-name>/fixtures/` only when necessary.

### Telemetry (optional)

If this gate emits structured telemetry:

- Keep it schema-validated (e.g., `schemas/telemetry/**` *(if present)*).
- Store run artifacts under `mcp/runs/` *(recommended; not confirmed in repo)* or a repo-approved telemetry location.

---

## ⚖ FAIR+CARE & Governance

### Review gates

- CI maintainers approve changes to `.github/workflows/` and `.github/actions/`.
- Governance owners review anything that:
  - changes sovereignty handling or redaction behavior
  - affects culturally sensitive or restricted locations
  - introduces new automated inference over sensitive content

### Sovereignty and safety measures

- This action must not introduce leakage of restricted coordinates or culturally sensitive material into logs or artifacts.
- Classification propagation: derived artifacts must not “downgrade” sensitivity/classification without explicit review.

### AI usage constraints

- This action must not:
  - generate new governance policy text
  - infer or reveal sensitive locations
- If AI tooling is introduced (unusual for CI), it must be opt-in and governance-reviewed.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-29 | Initial action README scaffold aligned to KFM universal doc structure and CI gate conventions | TBD |

---

Footer refs:

- Local actions index: `.github/actions/README.md`
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Templates: `docs/templates/`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
