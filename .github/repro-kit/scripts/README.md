---
title: "KFM Reproducibility Kit — Scripts"
path: ".github/repro-kit/scripts/README.md"
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

doc_uuid: "urn:kfm:doc:github:repro-kit-scripts-readme:v1.0.0"
semantic_document_id: "kfm-github-repro-kit-scripts-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github:repro-kit-scripts-readme:v1.0.0"
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

# KFM Reproducibility Kit — Scripts

> **Purpose (required):** Provide **repo-local scripts** that let contributors and reviewers run **CI-equivalent validation gates** (and small deterministic fixture runs) locally, aligned to the KFM canonical pipeline and governance constraints.

- Back to repro-kit: `.github/repro-kit/README.md`
- Related: local actions (optional): `.github/repro-kit/actions/` *(not confirmed in repo)*

## 📘 Overview

### Purpose

This directory contains **local wrapper scripts** used to:

- Re-run **CI-like checks locally** (same gates, same failures, same expectations).
- Keep validation aligned to the KFM canonical flow: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- Produce reviewer-friendly artifacts (logs, hashes, run manifests) without introducing privileged paths or non-determinism.

> Note: The scripts area is **optional**. If it exists, it should be kept in sync with CI gates and the repro-kit root README.

### Scope

| In Scope | Out of Scope |
|---|---|
| Local wrappers that mirror minimum CI gates (markdown, schemas, contracts, integrity tests) | Handling production secrets/credentials or privileged access paths |
| Deterministic “fixture-scale” runs and validation using small public/golden inputs | Large-scale production replays of restricted datasets |
| Generating **run manifests**, hash reports, and pointers to canonical outputs | Defining new governance policy or reclassifying sensitivity |
| “Skip if root absent; strict if root exists” behavior for optional repo areas | Bypassing sovereignty / redaction / sensitivity rules |

### Audience

- Primary: contributors and reviewers validating “v12-ready” changes.
- Secondary: CI maintainers keeping local scripts aligned with workflows/actions.

### Definitions (link to glossary)

- Link: `docs/glossary.md` *(not confirmed in repo)*
- Terms used in this doc:
  - **Gate**: A validation step that fails deterministically when a contract/invariant is violated.
  - **Deterministic**: same inputs + config + code revision ⇒ same outputs (byte-for-byte when practical).
  - **Idempotent**: re-running does not duplicate records or produce inconsistent results.
  - **Fixture**: small “golden” dataset(s) for deterministic tests.
  - **Run manifest**: portable record capturing how to reproduce a run (inputs, config, commit SHA, versions, parameters).

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Repro kit root README | `.github/repro-kit/README.md` | Repo maintainers | Parent scope + invariants |
| Workflows | `.github/workflows/` | CI maintainers | CI entrypoints calling gates |
| Local actions | `.github/actions/` | CI maintainers | Composite/local actions used by workflows *(optional, not confirmed in repo)* |
| Validators/utilities | `tools/` | Repo maintainers | Shared validation helpers *(not confirmed in repo)* |
| Schemas | `schemas/` | Contract owners | JSON schemas / validation targets *(not confirmed in repo)* |
| Master Guide | `docs/MASTER_GUIDE_v12.md` | KFM maintainers | Canonical pipeline + minimum gates |

### Definition of done (for this document)

- [ ] Front-matter complete + valid and `path` matches file location
- [ ] Script conventions (inputs/outputs/exit codes/logging) are clear and deterministic
- [ ] Mapping to “minimum CI gates” is documented and kept up to date
- [ ] “Skip if missing; strict if present” rule is stated and reflected in script patterns
- [ ] Governance + CARE/sovereignty constraints explicitly stated (no leakage, no policy generation)

## 🗂️ Directory Layout

### This document

- `path`: `.github/repro-kit/scripts/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Repro kit root | `.github/repro-kit/` | Reproduction helpers (docs/actions/scripts/fixtures/env) |
| Workflows | `.github/workflows/` | CI entrypoints (PR, push, scheduled) |
| Local actions | `.github/actions/` | Composite/local actions used by workflows *(not confirmed in repo)* |
| Pipelines | `src/pipelines/` | Deterministic ETL + transforms *(not confirmed in repo)* |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Generated STAC/DCAT/PROV artifacts *(some roots may be optional)* |
| Graph | `src/graph/` | Graph build + ontology bindings *(not confirmed in repo)* |
| API boundary | `src/server/` | Canonical API access layer *(not confirmed in repo)* |
| UI | `web/` | React/Map UI (never reads Neo4j directly) *(not confirmed in repo)* |
| Story Nodes | `docs/reports/story_nodes/` | Curated narrative artifacts *(not confirmed in repo)* |
| Tests | `tests/` | Unit/integration/contract tests *(not confirmed in repo)* |
| MCP | `mcp/` | Runs/experiments/model cards/SOPs *(not confirmed in repo)* |

### Expected file tree for this sub-area

~~~text
📁 .github/
└── 📁 repro-kit/
    └── 📁 scripts/
        └── 📄 README.md   # This file
~~~

> Optional expansion pattern (create as-needed; naming is conventional, not required):
~~~text
📁 .github/repro-kit/scripts/
├── 📄 README.md
├── 📁 validate/          # wrapper scripts for CI-equivalent validation gates (optional)
├── 📁 run/               # deterministic fixture run entrypoints (optional)
└── 📁 lib/               # shared helpers (optional)
~~~

## 🧭 Context

### Background

KFM emphasizes reproducibility and governed validation:

- Pipelines are designed to be deterministic and logged.
- Validation gates enforce contracts across schemas, catalogs, graph integrity, API contracts, UI registries, and narrative provenance.
- Focus Mode and published narratives must remain provenance-linked (no unsourced outputs).

### Assumptions

- Canonical ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- The UI does **not** read Neo4j directly; an API boundary mediates access and redaction.
- Contract and schema validation are treated as first-class build gates.

### Constraints / invariants

- Scripts must be **idempotent** and **deterministic**.
- If a gate depends on a repo root that is absent, scripts should **skip** the gate; if the root exists, validation is **strict** and fails deterministically.
- Scripts must not introduce secrets, privileged paths, or leakage of restricted/sensitive material.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What is the canonical location for run manifests in this repo (`data/prov/` vs `mcp/runs/` vs `releases/<version>/`)? | TBD | TBD |
| Which fixture datasets are safe to include publicly under `.github/repro-kit/fixtures/`? | TBD | TBD |
| What is the preferred environment locking strategy for scripts (pip-tools/poetry/conda/node lockfiles)? | TBD | TBD |

## 🗺️ Diagrams

### “Local script” flow vs canonical pipeline

~~~mermaid
flowchart LR
  A[Contributor / Reviewer] --> B[.github/repro-kit/scripts/*]
  B --> C[Validators + Test Runners<br/>(Makefile/tools/tests)]
  C --> D[Reports / Logs / Hashes / Manifests]
  D --> E[Catalogs + Provenance<br/>(STAC/DCAT/PROV)]
  E --> F[Graph → API → UI]
  F --> G[Story Nodes → Focus Mode]
~~~

## 🧪 Validation & CI/CD

### Minimum CI gates (baseline)

Scripts in this directory should mirror the baseline CI expectations:

- Markdown protocol validation
- JSON/schema validation (STAC/DCAT/PROV + story nodes + telemetry, as applicable)
- Graph integrity tests
- API contract tests
- UI layer registry schema checks
- Security + sovereignty scanning gates (where applicable)

### CI behavior principle (apply to scripts)

- If a gate depends on a root that does **not** exist in the current repo snapshot, scripts should **skip** that gate.
- If the root exists, validation must be **strict** and must **fail deterministically** when invalid.

### Script interface conventions

When adding scripts here, prefer conventions that keep CI and local runs aligned:

- **Exit codes:** `0` success, `1` validation failure, `2` usage/config error.
- **No hidden state:** avoid writing to global locations; write logs/reports into a caller-provided output directory (or a predictable local path).
- **Deterministic defaults:** fixed seeds where applicable; stable ordering; stable formatting.
- **No secrets:** do not read credentials from developer machines; do not print tokens; do not upload sensitive artifacts.
- **Prefer reuse:** call existing repo entrypoints (e.g., `make …`, `tools/validate/*`, `pytest`, `npm test`) rather than reimplementing validation logic.

### Example placeholders (replace with repo-specific scripts/targets)

~~~bash
# Example placeholders — update when scripts are added to this directory.

# 1) Markdown protocol checks
# .github/repro-kit/scripts/validate/markdown.sh

# 2) Schema validation (STAC/DCAT/PROV/storynodes/ui/telemetry)
# .github/repro-kit/scripts/validate/schemas.sh

# 3) Graph integrity tests
# .github/repro-kit/scripts/validate/graph.sh

# 4) API contract tests
# .github/repro-kit/scripts/validate/api_contracts.sh

# 5) UI registry checks
# .github/repro-kit/scripts/validate/ui_registry.sh

# 6) Security + sovereignty scanning
# .github/repro-kit/scripts/validate/security.sh
~~~

## ⚖ FAIR+CARE & Governance

### Review gates

- CI maintainers should review changes to `.github/workflows/`, `.github/actions/`, and any scripts that define or bypass gates.
- Governance owners should review anything that:
  - changes sovereignty handling or redaction/generalization behavior,
  - affects handling of culturally sensitive or restricted locations,
  - introduces new automated inference over sensitive content.

### CARE / sovereignty considerations

- Scripts must not leak restricted coordinates, culturally sensitive locations, or protected identifiers in logs or artifacts.
- If scripts generate reports, ensure outputs can be safely published in CI logs (or mark outputs as restricted and suppress from public artifacts).

### AI usage constraints

- Ensure scripts do **not** “infer sensitive locations” (directly or indirectly) and do **not** generate new governance policy.
- If any AI tooling is added to scripts (not typical), it must be opt-in and governance-reviewed.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-26 | Initial `.github/repro-kit/scripts/` README scaffold | TBD |

---

## Footer refs (do not remove)

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`

