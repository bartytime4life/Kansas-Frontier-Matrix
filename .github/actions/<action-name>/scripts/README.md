---
title: "KFM GitHub Actions — Local Action Scripts"
path: ".github/actions/<action-name>/scripts/README.md"
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

doc_uuid: "urn:kfm:doc:github-actions:local-action-scripts-readme:<action-name>:v1.0.0"
semantic_document_id: "kfm-github-actions-local-action-scripts-readme-<action-name>-v1.0.0"
event_source_id: "ledger:kfm:doc:github-actions:local-action-scripts-readme:<action-name>:v1.0.0"
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

# KFM GitHub Actions — Local Action Scripts

## 📘 Overview

### Purpose

- Document **authoring conventions** for scripts stored under `.github/actions/<action-name>/scripts/`.
- Ensure scripts are **deterministic**, **repo-local**, and safe for **FAIR+CARE** governance constraints.
- Standardize how scripts implement CI “gates” while preserving KFM’s **contract-first** and **evidence-first** architecture.

### Scope

| In Scope | Out of Scope |
|---|---|
| Script conventions for `.github/actions/<action-name>/scripts/` | Changing workflows under `.github/workflows/` |
| Deterministic “skip vs fail” semantics for optional roots | Defining new governance policy text |
| Safe logging patterns (no sensitive leakage) | Runner provisioning, cloud deployment, secrets ops |
| How scripts call repo-local validators in `tools/` or `src/` when present | Implementing business logic that belongs in pipelines/API/UI |

### Audience

- Primary: CI maintainers and local-action maintainers.
- Secondary: Contributors adding or modifying scripts used by gates (schemas, contracts, story rules, lint).

### Definitions

- Link: `docs/glossary.md` *(not confirmed in repo — recommended canonical location)*

Terms used in this doc:

- **Script**: A repo-local executable (bash/python/node) invoked by a local action (composite) to run a gate.
- **Validator**: A reusable program (preferably in `tools/` or `src/`) that performs the “real” validation.
- **Gate**: A validation check that fails CI if a contract/invariant is violated.
- **Skip**: A deterministic no-op result used when an optional root is absent.
- **Fail**: A deterministic non-zero outcome when required inputs exist but do not validate.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Action scripts README (this doc) | `.github/actions/<action-name>/scripts/README.md` | Action maintainers | Defines script rules and safe patterns |
| Action README | `.github/actions/<action-name>/README.md` | Action maintainers | User-facing contract (inputs/outputs/examples) |
| Local actions overview | `.github/actions/README.md` | Repo maintainers | Local-action conventions and gate mapping |
| Master Guide | `docs/MASTER_GUIDE_v12.md` | KFM maintainers | Pipeline ordering + minimum CI gates |
| Templates | `docs/templates/` | Docs | Universal/story/API governed templates |
| Governance refs | `docs/governance/*` | Governance owners | Safety, ethics, sovereignty obligations |
| Validators | `tools/` or `src/` | Tooling/Eng | Preferred home for shared logic *(if present)* |

### Definition of done for this document

- [ ] Front-matter complete + valid
- [ ] Script conventions are explicit and reproducible
- [ ] “Skip vs fail” behavior is deterministic and documented
- [ ] Security + CARE/sovereignty constraints are stated
- [ ] Code/tree blocks use `~~~` fences

---

## 🗂️ Directory Layout

### This document

- `path`: `.github/actions/<action-name>/scripts/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| CI root | `.github/` | Workflows + local actions |
| Local action | `.github/actions/<action-name>/` | `action.yml` + action README + scripts |
| Action scripts | `.github/actions/<action-name>/scripts/` | Gate wrappers and helper scripts |
| Reusable validators | `tools/` | Validators/utilities invoked by actions *(if present)* |
| Pipelines | `src/pipelines/` | ETL + catalog generation code *(if present)* |
| Graph | `src/graph/` | Graph build/migrations/tests *(if present)* |
| API boundary | `src/server/` | API + contracts + redaction logic *(if present)* |
| UI | `web/` | React + Map UI + Focus Mode *(if present)* |
| Tests | `tests/` | Unit + integration tests *(if present)* |

### Expected scripts layout

~~~text
📁 .github/
└── 📁 actions/
    └── 📁 <action-name>/
        ├── 📄 action.yml
        ├── 📄 README.md
        └── 📁 scripts/
            ├── 📄 README.md
            ├── 📄 <gate-or-helper>.sh         # preferred for thin wrappers
            ├── 📄 <gate-or-helper>.py         # allowed when python tooling is repo-standard
            └── 📁 lib/                         # optional: small shared helpers for this action only
~~~

### Conventions

- **Script names:** `kebab-case` and verbs preferred, e.g. `validate-schemas.sh`, `check-links.sh`.
- **Do not duplicate shared logic:** If logic is reusable across actions, move it to `tools/` (preferred) or a language module under `src/` and keep scripts as wrappers.
- **No YAML front-matter in scripts:** Front-matter is for governed Markdown docs only. Scripts must not start with `---`.
- **Shell safety defaults:** bash scripts must use strict mode unless there is an explicit, documented reason not to.

---

## 🧭 Context

### Scripts are part of CI governance

KFM treats documentation and validation as first-class repo artifacts, with CI enforcing structure and contracts as a compliance mechanism. Scripts in `scripts/` are therefore considered **policy-adjacent glue** and must remain:

- deterministic and reproducible
- minimal and reviewable
- safe for public logs and artifacts

### How this aligns with the canonical pipeline

Pipeline ordering is non-negotiable:

- **ETL → STAC/DCAT/PROV catalogs → Graph → API → UI → Story Nodes → Focus Mode**

CI scripts should enforce the contracts at each boundary without crossing subsystem boundaries improperly (example: UI checks must not read Neo4j directly; they should validate UI contracts and registry artifacts via API/schema expectations).

### Optional roots and incremental adoption

Some roots may be absent in a snapshot. Scripts must implement this rule:

- If a gate depends on a root that is absent, the script should **skip deterministically** and emit a clear notice (e.g., `skipped: missing <root>`).
- If the root exists, validation must be **strict** and must fail deterministically when invalid.

Workflows may enforce stricter branch rules, but scripts should remain stable and predictable.

---

## 🗺️ Diagrams

### Workflow → local action → scripts → validators

~~~mermaid
flowchart LR
  PR["PR / Push"] --> WF["Workflow (.github/workflows/*.yml)"]
  WF --> LA["Local Action (.github/actions/<action-name>)"]
  LA --> SCR["Scripts (.github/actions/<action-name>/scripts)"]
  SCR --> VAL["Repo-local validators (tools/ or src/)"]
  VAL --> OUT["Outputs: logs + summaries + status"]
~~~

---

## 📦 Data & Metadata

### Inputs

Scripts may consume:

- repository checkout (including changed files in PR)
- action inputs passed through `action.yml` (paths/roots/strict/changed-only)
- CI-provided environment variables (e.g., `GITHUB_SHA`, `GITHUB_OUTPUT`, `GITHUB_STEP_SUMMARY`)
- schema/contract files (e.g., `schemas/**`, `src/server/contracts/**`) when present
- produced artifacts to validate (`data/stac/**`, `data/catalog/dcat/**`, `data/prov/**`, Story Nodes)

### Outputs

Scripts may emit:

- exit status for pass/fail
- structured outputs to `GITHUB_OUTPUT` (e.g., `skipped=true`, `checked_count=...`, `error_count=...`)
- a human-readable summary via `GITHUB_STEP_SUMMARY`

Scripts must keep logs:

- actionable (what failed + where)
- safe (no secrets, no restricted coordinates, no PII payload dumps)

### Sensitivity handling

Do not print or upload:

- signed URLs, tokens, credentials
- raw PII fields
- restricted coordinates or culturally sensitive locations (unless governance-approved and the repository is not public)

When reporting invalid items, prefer:

- file paths + stable IDs + counts
- minimal redacted snippets when absolutely required for debugging

---

## 🌐 STAC, DCAT & PROV Alignment

Scripts may be used to validate catalog boundary artifacts when roots exist:

- STAC: `data/stac/**`
- DCAT: `data/catalog/dcat/**`
- PROV: `data/prov/**`

Recommended cross-artifact checks (when applicable):

- no orphan references between Story Nodes / graph ingest / catalogs
- lineage completeness for raw → work → processed → catalog outputs
- stable IDs and stable ordering to keep diffs meaningful

---

## 🧱 Architecture

### Script contract

Scripts in this directory should follow a consistent contract:

- **Inputs via CLI flags** (preferred) rather than implicit environment variables.
- **Deterministic execution**:
  - sort file lists before iterating
  - avoid time-dependent output
  - pin tool versions via lockfiles where applicable
- **Clear exit codes**:
  - `0` for pass and for deterministic skip (skip must still set `skipped=true`)
  - non-zero for fail
- **Structured outputs**:
  - write `skipped=true|false`, `checked_count`, `error_count` to `GITHUB_OUTPUT` when invoked by GitHub Actions.

### Bash strict mode baseline

All bash scripts should start with:

~~~bash
#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'
~~~

Do not enable `set -x` (command echo) unless you are confident no secrets or restricted values can appear in the trace.

### Prefer repo-local validators

Scripts should be wrappers that call into:

- `tools/…` validators *(preferred, if present)*
- language modules under `src/…` *(if present)*
- test runners under `tests/…` *(if present)*

Avoid embedding complex validation logic directly in `scripts/`.

### Example wrapper pattern

~~~bash
#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-}"
SKIP_IF_MISSING="${SKIP_IF_MISSING:-true}"

if [[ -z "${ROOT}" ]]; then
  echo "Usage: $0 <root>"
  exit 2
fi

if [[ "${SKIP_IF_MISSING}" == "true" && ! -e "${ROOT}" ]]; then
  echo "::notice::Skipped: missing ${ROOT}"
  echo "skipped=true" >> "${GITHUB_OUTPUT:-/dev/null}" || true
  exit 0
fi

# Replace with a repo-local validator command.
# Example placeholder:
# tools/validate_schemas --root "${ROOT}"

echo "skipped=false" >> "${GITHUB_OUTPUT:-/dev/null}" || true
~~~

### What scripts must not do

- mutate repository content (unless explicitly part of a dedicated formatting workflow)
- introduce network calls that make results nondeterministic (unless explicitly documented and pinned)
- bypass subsystem boundaries (example: UI scripts should not query Neo4j directly)
- implement AI inference over sensitive locations or generate governance policy text

---

## 🧠 Story Node & Focus Mode Integration

Scripts may implement Story Node gates such as:

- front-matter validation and required section checks
- provenance-linking checks (claims link to evidence identifiers)
- restricted content leakage checks (no sensitive locations exposed)
- schema validation for Story Node structures (if a schema is present)

This supports the invariant that Focus Mode consumes only provenance-linked context bundles and should not surface unsourced narrative.

---

## 🧪 Validation & CI/CD

### Baseline gates this action’s scripts may support

Minimum CI gates for KFM “v12-ready” contributions include:

- Markdown protocol validation
- link/reference checks
- JSON schema validation (STAC/DCAT/PROV, Story Nodes, telemetry, UI registry when present)
- graph integrity tests
- API contract tests (OpenAPI/GraphQL + resolver tests)
- security + sovereignty scanning (secret scan, PII scan, sensitive-location leakage, classification propagation)

### Gate implementation guidance

- Prefer “changed-only” validation for PRs where feasible.
- If an optional root is missing, skip deterministically.
- If the root exists, validate strictly and fail deterministically.

### Local reproduction pattern

~~~bash
# Examples only — replace with repo-specific validator entrypoints.
# Run from repo root.

# Validate a root (skip-if-missing behavior controlled by env)
SKIP_IF_MISSING=true ./.github/actions/<action-name>/scripts/<gate>.sh data/stac/

# If your validator lives in tools/
# tools/<validator> --root data/stac/
~~~

---

## ⚖ FAIR+CARE & Governance

### Classification propagation

Scripts must preserve the invariant:

- No output may be less restricted than any upstream input in its lineage.

If a script detects classification downgrades or sensitive-location leakage, it must fail (or block publication gates), and it must avoid printing the sensitive values in logs.

### Review triggers

Require governance review when a script change:

- affects redaction/generalization behavior
- changes sensitivity/classification evaluation rules
- introduces new scans that may surface restricted info
- modifies how Story Nodes are validated for provenance or sensitive content

### AI usage constraints

Scripts must not:

- infer sensitive locations
- generate new governance policy text

Any AI-assisted validation is unusual for CI and must be opt-in and governance-reviewed.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-29 | Initial governed README for local action `scripts/` conventions | TBD |

---

Footer refs:

- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Local actions overview: `.github/actions/README.md`
- This action: `.github/actions/<action-name>/README.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
