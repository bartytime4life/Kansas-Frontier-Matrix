---
title: "KFM GitHub Actions — <action-name> — scripts/lib"
path: ".github/actions/<action-name>/scripts/lib/README.md"
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

doc_uuid: "urn:kfm:doc:github-actions:<action-name>:scripts-lib-readme:v1.0.0"
semantic_document_id: "kfm-github-actions-<action-name>-scripts-lib-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github-actions:<action-name>:scripts-lib-readme:v1.0.0"
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

# KFM GitHub Actions — `<action-name>` — `scripts/lib`

## 📘 Overview

### Purpose

- Provide a small, repo-local helper library used by `.github/actions/<action-name>/scripts/**` so gate scripts behave consistently (logging, skip/fail, path checks, deterministic iteration).
- Keep “validation logic” out of workflow YAML and out of ad-hoc one-liners by standardizing the glue code between `action.yml` and repo validators (prefer `tools/**` or `src/**` as the canonical homes for validators).

### Scope

| In Scope | Out of Scope |
|---|---|
| Helper modules used by scripts: logging, filesystem checks, git diff helpers, JSON helpers, summary writers | Implementing core validators (schemas/graph/api/ui/story); those belong under `tools/` or subsystem-owned `src/**` |
| Deterministic “skip vs fail” semantics for optional roots | Changing `.github/workflows/**` or branch policies |
| Guardrails against sensitive leakage in CI logs/artifacts | Defining new governance policy (see `docs/governance/*`) |
| Conventions for action script structure, imports, and error handling | Network-dependent logic that makes CI non-deterministic (unless explicitly pinned and documented) |

### Audience

- Primary: maintainers of `.github/actions/<action-name>/`.
- Secondary: contributors extending this action’s scripts or adding new gate steps.

### Definitions (link to glossary)

- Link: `docs/glossary.md` *(not confirmed in repo — recommended canonical location)*

Terms used in this doc:

- **Script entrypoint**: a runnable file under `scripts/` invoked by `action.yml`.
- **Library module**: a file under `scripts/lib/` intended to be sourced/imported by multiple scripts.
- **Gate**: a validation step that fails CI if a required contract/invariant is violated.
- **Skip**: deterministic success exit used when an optional root is absent and `skip_if_missing=true`.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Action contract | `.github/actions/<action-name>/action.yml` | Action owners | Inputs/outputs and runner wiring |
| Action README | `.github/actions/<action-name>/README.md` | Action owners | Gate purpose + usage examples |
| Scripts README | `.github/actions/<action-name>/scripts/README.md` | Action owners | Script entrypoints + conventions |
| This README | `.github/actions/<action-name>/scripts/lib/README.md` | Action owners | Helper library conventions |
| Global local-actions guide | `.github/actions/README.md` | CI maintainers | Shared KFM local-action patterns |
| Validators (preferred) | `tools/**` or `src/**` | Subsystem owners | Actual validation logic and tests |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] Library boundaries are explicit (helpers only; validators live in `tools/` or `src/**`)
- [ ] Skip vs fail semantics are explicit and deterministic
- [ ] Security/sensitivity rules are explicit (what helpers must never print/upload)
- [ ] Examples use `~~~` fences (per KFM Markdown protocol)

---

## 🗂️ Directory Layout

### This document

- `path`: `.github/actions/<action-name>/scripts/lib/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| CI | `.github/` | Workflows + local actions + policy gates |
| Local actions | `.github/actions/` | Composite/local actions used by workflows |
| Shared validators | `tools/` | Validators/utilities invoked by actions *(if present)* |
| Pipelines | `src/pipelines/` | ETL + catalog generation |
| Graph | `src/graph/` | Graph build/migrations |
| API boundary | `src/server/` | API + contracts + redaction logic |
| UI | `web/` | React/map client; consumes APIs only |
| Story Nodes | `docs/reports/story_nodes/` | Governed narrative nodes (draft/published) |

### Expected file tree for this sub-area

~~~text
📁 .github/
└── 📁 actions/
    └── 📁 <action-name>/
        ├── 📄 action.yml
        ├── 📄 README.md
        └── 📁 scripts/
            ├── 📄 README.md
            ├── 📄 <entrypoint>.sh
            └── 📁 lib/
                └── 📄 README.md
                # Recommended (examples; add only as needed):
                # ├── 📄 log.sh
                # ├── 📄 fs.sh
                # ├── 📄 git.sh
                # ├── 📄 json.sh
                # └── 📄 guardrails.sh
~~~

### Naming and authoring conventions

- **Language:** default to `bash` for composite-action scripts unless the validator requires a runtime (Python/Node).
- **Prefix:** helper functions should use a stable prefix (recommended: `kfm_`) to avoid collisions.
- **Strict mode:** script entrypoints should run with `set -euo pipefail`.
- **Deterministic iteration:** sort file lists using a stable locale (recommended: `LC_ALL=C sort`).
- **No YAML front-matter in code files:** YAML front-matter is for Markdown docs only.

---

## 🧭 Context

### Background

KFM local actions are meant to be thin wiring between workflow inputs and repo-local validators. A shared `scripts/lib`:

- reduces duplication,
- standardizes behavior (skip vs fail, exit codes, summary outputs),
- improves safety (consistent “no payload dumps” and redaction guardrails),
- supports deterministic CI output ordering.

### Assumptions

- Composite actions use `shell: bash` and run on GitHub-hosted runners (or compatible self-hosted runners).
- The action should be able to skip deterministically when optional roots are absent.

### Constraints / invariants

- Preserve canonical ordering: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- UI must never read Neo4j directly; access is via contracted APIs.
- Helpers must not leak restricted coordinates, tokens, signed URLs, or raw PII into logs or artifacts.
- Helpers must not “infer sensitive locations” or generate policy text.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Standardize lint tooling for action scripts (`shellcheck` / `shfmt`)? *(not confirmed in repo)* | CI maintainers | TBD |
| Standardize structured telemetry output locations for CI runs (e.g., `mcp/runs/`)? *(not confirmed in repo)* | CI + MCP owners | TBD |

### Future extensions

- If multiple actions copy identical helpers, consider promoting stable helper code into a repo-level shared location (e.g., under `tools/`), while keeping a single canonical home.
- Add a minimal test harness for helper modules once helper surface area grows (keep deterministic and fast).

---

## 🗺️ Diagrams

### How `scripts/lib` supports a local action gate

~~~mermaid
flowchart LR
  WF[".github/workflows/*.yml"] --> ACT[".github/actions/<action-name>/action.yml"]
  ACT --> S["scripts/<entrypoint>.sh"]
  S --> L["scripts/lib/*.sh (helpers)"]
  S --> V["tools/** or src/** validators"]
  S --> O["GITHUB_OUTPUT + step summary"]
~~~

---

## 📦 Data & Metadata

### Inputs (typical)

| Input | Source | Notes |
|---|---|---|
| Action inputs | Workflow `with:` | Validate/normalize before use |
| Paths/roots | Repo checkout | Optional roots may not exist |
| Changed files | `git diff` or workflow-provided lists | Sort deterministically before iterating |
| Runner env | `$GITHUB_*` env vars | Treat as potentially sensitive |

### Outputs (typical)

| Output | Where | Notes |
|---|---|---|
| `skipped=true|false` | `$GITHUB_OUTPUT` | Deterministic skip signal |
| `checked_count`, `error_count` | `$GITHUB_OUTPUT` | Prefer integers |
| Human summary | `$GITHUB_STEP_SUMMARY` | Safe summaries only |
| Logs | Actions log stream | Avoid payload dumps |

### Sensitivity handling

Helper modules should enable scripts to:

- log counts and stable identifiers rather than full JSON payloads,
- mask secrets (or refuse to echo suspected secret-like values),
- avoid printing raw coordinates and sensitive geometries.

---

## 🌐 STAC, DCAT & PROV Alignment

`scripts/lib/` should not implement STAC/DCAT/PROV validation logic itself. Helpers may:

- locate canonical roots (`data/stac/`, `data/catalog/dcat/`, `data/prov/`),
- apply deterministic skip rules if roots are missing,
- invoke repo validators and normalize outputs for CI.

Any cross-artifact checks remain the validator’s job (not the helper’s), including:

- no orphan references,
- stable IDs,
- PROV lineage completeness (raw → work → processed),
- classification propagation (no silent downgrades).

---

## 🧱 Architecture

### Separation of concerns

**Use `scripts/lib` for plumbing and guardrails:**

- input parsing/normalization,
- consistent logging, grouping, and error handling,
- root/path checks + deterministic skip,
- capturing validator exit codes and summarizing results,
- writing `GITHUB_OUTPUT` and `GITHUB_STEP_SUMMARY` safely.

**Put “real validation” elsewhere:**

- Prefer `tools/` for reusable validators.
- Prefer subsystem-owned code under `src/pipelines/`, `src/graph/`, `src/server/`, `web/` for checks that belong to those subsystems.

### Recommended import pattern (bash)

~~~bash
#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Source only what you need (avoid mega-imports).
source "${SCRIPT_DIR}/lib/log.sh"
source "${SCRIPT_DIR}/lib/fs.sh"

kfm_notice "Starting gate…"
~~~

### Helper module contract

A helper module should:

- be safe to source multiple times (idempotent),
- avoid surprising global state mutation,
- expose small, testable functions,
- return non-zero on errors and never swallow validator failures.

Recommended conventions:

- errors to `stderr`,
- stable sorting (`LC_ALL=C sort`) for file lists,
- strict quoting and input validation.

### Standard “skip vs fail” helper rule

Helpers should implement a consistent rule:

- If `skip_if_missing=true` and required `root`/`path` is missing: emit `skipped=true`, log a notice, exit `0`.
- If the root exists (or skipping is disabled): emit `skipped=false`, run validation, fail deterministically on errors.

---

## 🧠 Story Node & Focus Mode Integration

If this action validates Story Nodes or anything that becomes Focus Mode content:

- Focus Mode consumes **provenance-linked** content only.
- Any predictive/suggestive content must be opt-in, carry uncertainty metadata, and must not infer or reveal sensitive locations.

Helpers can support this by:

- standardizing how validators report missing citations/unresolved IDs,
- preventing payload dumps in logs/summaries,
- surfacing redaction/generalization *signals* (without sensitive details).

---

## 🧪 Validation & CI/CD

### Validation steps (recommended)

- [ ] Lint `scripts/` and `scripts/lib/` (e.g., `shellcheck` / `shfmt`) *(tooling not confirmed in repo)*
- [ ] Run this action in a PR workflow against a minimal fixture
- [ ] Confirm deterministic behavior (same inputs → same outputs/log order)
- [ ] Confirm skip behavior when optional roots are absent
- [ ] Confirm no sensitive material appears in logs or uploaded artifacts

### Reproduction (local, pattern)

~~~bash
# From repo root (example pattern; replace with this action’s concrete entrypoint)
bash .github/actions/<action-name>/scripts/<entrypoint>.sh --help
bash .github/actions/<action-name>/scripts/<entrypoint>.sh --root data/stac --skip-if-missing true
~~~

### Telemetry signals (optional)

If the action emits structured telemetry, keep it schema-validated and stored under a canonical location (e.g., `mcp/runs/`), but treat this as optional until a repo standard exists *(not confirmed in repo)*.

---

## ⚖ FAIR+CARE & Governance

### Review gates

Changes to `scripts/lib` should be reviewed by:

- CI maintainers (behavior, determinism),
- governance/security owners when changes affect redaction, classification propagation, or sovereignty handling.

### CARE / sovereignty considerations

- Treat restricted/culturally sensitive content as high-risk by default.
- Prefer aggregated outputs (counts, IDs) over emitting sensitive coordinates/geometries.

### AI usage constraints

This helper library must not:

- infer sensitive locations,
- generate new policy text,
- present AI-generated content as fact.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-29 | Initial `scripts/lib` README scaffold for local action helper libraries | TBD |

---

Footer refs:

- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
