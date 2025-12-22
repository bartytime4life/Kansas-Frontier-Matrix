---
title: "Repro Kit — Shared Action Utilities"

path: ".github/repro-kit/actions/_shared/README.md"

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



doc_uuid: "urn:kfm:doc:github:repro-kit:actions-shared-readme:v1.0.0"

semantic_document_id: "kfm-github-repro-kit-actions-shared-readme-v1.0.0"

event_source_id: "ledger:kfm:doc:github:repro-kit:actions-shared-readme:v1.0.0"

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

# Repro Kit — Shared Action Utilities

## 📘 Overview

### Purpose

- Provide a single, documented home for **shared building blocks** used by multiple GitHub Actions under `.github/repro-kit/actions/`.
- Reduce duplication across actions while improving **determinism, auditability, and maintenance**.
- Establish clear rules for what may live in `_shared/` (and what must *not*).

### Scope

| In Scope | Out of Scope |
|---|---|
| Reusable helper scripts and small utilities used by multiple actions (e.g., input validation, safe logging helpers, checksum helpers, temp-dir helpers). | Project domain ETL logic (belongs in `src/pipelines/` or `tools/`). |
| Shared composite-action fragments / conventions (when a stable interface is needed across actions). | Workflow definitions (belongs in `.github/workflows/`). |
| Shared configs used by actions (when these configs are repo-governed and non-secret). | Secrets, credentials, tokens, private keys, or any secret-like material. |
| Shared guardrails for reproducible CI behavior (pinning, idempotence, stable paths). | “One-off” scripts needed by only a single action (keep local to that action unless reused). |

### Audience

- **Primary:** Contributors maintaining GitHub Actions and CI validation gates.
- **Secondary:** Contributors authoring new actions for KFM validation, packaging, or reproducible build tasks.

### Definitions (link to glossary)

- Link: `docs/glossary.md`
- Terms used in this doc include:
  - **Composite Action**: a GitHub Action implemented as a reusable step bundle.
  - **Reproducible / Deterministic**: the same inputs produce the same outputs (or differences are explicitly versioned / provenance-tagged).
  - **Hermetic**: minimal implicit dependencies on the runner (explicit toolchain setup, pinned versions).

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Repro Kit (root) | `.github/repro-kit/README.md` | CI/Build Maintainers | Repro kit overview + adoption in workflows. |
| Repro Kit Actions (index) | `.github/repro-kit/actions/README.md` | CI/Build Maintainers | Catalog of available actions and when to use them. |
| Shared utilities (this doc) | `.github/repro-kit/actions/_shared/README.md` | CI/Build Maintainers | Design rules and usage patterns for shared code. |
| Canonical pipeline map | `docs/MASTER_GUIDE_v12.md` | KFM Core Team | Ensures CI helpers align to repo canonical paths + contracts. |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] `_shared/` purpose and boundaries clearly stated
- [ ] Usage rules prevent secrets/PII leakage in logs
- [ ] Shared helper conventions documented (interfaces, versioning expectations)
- [ ] “Suggested layout” is clearly labeled (no false claims about existing files)

## 🗂️ Directory Layout

### This document

- `path`: `.github/repro-kit/actions/_shared/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Workflows | `.github/workflows/` | CI workflows that call actions / gates. |
| Repro Kit actions | `.github/repro-kit/actions/` | Individual actions used by workflows. |
| Shared action utilities | `.github/repro-kit/actions/_shared/` | Reusable scripts, configs, and shared fragments. |
| Core pipeline code | `src/` | ETL, graph, API, etc. (actions should call into these rather than re-implement logic). |
| Data artifacts | `data/` | Outputs; actions should respect canonical output locations. |
| Schemas | `schemas/` | Schema contracts (validated by CI actions). |

### Suggested file tree for this sub-area

> This is a recommended shape; not all subfolders must exist immediately.

~~~text
📁 .github/
└── 📁 repro-kit/
    └── 📁 actions/
        └── 📁 _shared/
            ├── 📄 README.md
            ├── 📁 scripts/               # small reusable scripts (bash/python/node)
            ├── 📁 composite/             # optional shared composite fragments
            └── 📁 configs/               # non-secret shared configs used by actions
~~~

## 🧭 Context

### Why `_shared/` exists

KFM’s CI is expected to be reproducible and enforce repository contracts (schemas, doc protocols, and other validation gates). Shared utilities:

- prevent “copy/paste drift” across actions,
- make it easier to keep behavior consistent when requirements evolve,
- reduce the chance that one action logs sensitive values or writes outputs into non-canonical locations.

### Design principles

- **No secrets.** `_shared/` must never contain credentials, tokens, or private keys.
- **Deterministic by default.** Prefer pinned versions and stable ordering. Avoid time-based output unless explicitly part of the contract.
- **Idempotent behavior.** Running helpers twice should not corrupt state or produce inconsistent outputs.
- **Least surprise.** Shared helpers should be tiny, well-scoped, and documented.
- **Stable interfaces.** If multiple actions depend on a helper, changing its interface is a breaking change.

## 📦 Data & Metadata

### Inputs

Shared utilities generally receive inputs via:

- action inputs (when used by a composite action),
- environment variables, or
- command-line flags (for scripts).

| Input | Format | Where from | Validation |
|---|---|---|---|
| Repo root path | string (path) | calling action | must resolve inside workspace |
| Toolchain version (e.g., node/python) | string | calling action | validate format; pin when possible |
| Cache key prefix | string | calling action/workflow | validate allowed chars |
| Output directory | string (path) | calling action | must be under canonical repo roots |

### Outputs

Shared utilities typically expose outputs as:

- files written to a designated output directory, and/or
- `GITHUB_OUTPUT` values (when used inside composite actions).

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Logs | text | runner logs | must be secret-safe |
| Generated helper artifacts | files | action-defined staging dir | action-owned contract |
| Derived identifiers (hashes, versions) | strings | `GITHUB_OUTPUT` | action-owned contract |

### Sensitivity & redaction

- Assume CI logs are **public** (or at least broadly visible to contributors).
- Do **not** echo environment variables wholesale.
- Prefer “safe logging” wrappers that redact known secret patterns.
- If an action must handle sensitive paths (rare), generalize/omit them in logs.

### Quality signals

- Deterministic ordering (`sort` where relevant).
- Stable checksums for generated artifacts.
- Explicit versions recorded for toolchains.
- Clear error messages with actionable remediation.

## 🌐 STAC, DCAT & PROV Alignment

This directory is not a primary catalog producer. However, shared helpers may be used by actions that:

- validate STAC/DCAT/PROV artifacts,
- enforce canonical output paths, and/or
- stamp provenance identifiers into build/run artifacts.

### STAC

- Collections involved: N/A (unless a calling action validates `data/stac/**`)
- Items involved: N/A (unless a calling action validates `data/stac/**`)
- Extension(s): N/A here (owned by catalog contracts)

### DCAT

- Dataset identifiers: N/A here (owned by catalog contracts)
- License mapping: N/A here
- Contact / publisher mapping: N/A here

### PROV-O

- `prov:wasDerivedFrom`: N/A here (owned by provenance-producing action)
- `prov:wasGeneratedBy`: N/A here (owned by provenance-producing action)
- Activity / Agent identities: N/A here (owned by provenance-producing action)

### Versioning

- Shared utilities should evolve under **semantic versioning at the document level**.
- If a shared helper’s interface changes, downstream actions must be updated in the same PR (or a migration plan must be documented).

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Workflows | Orchestrate CI jobs | `.github/workflows/*.yml` |
| Actions | Provide reusable CI steps | `.github/repro-kit/actions/*` |
| Shared utilities | Reusable helpers for actions | `.github/repro-kit/actions/_shared/*` |
| Repo contracts | Schemas, doc protocol, structure | `schemas/`, `docs/`, canonical roots |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| Shared scripts interface | `_shared/scripts/**` | stable CLI/inputs; changes treated as breaking |
| Shared configs | `_shared/configs/**` | changes require audit for determinism + security |
| Shared composite fragments | `_shared/composite/**` | inputs/outputs documented; changes require coordinated updates |

### Diagrams

~~~mermaid
flowchart LR
  W[Workflow (.github/workflows)] --> A[Action (.github/repro-kit/actions/*)]
  A --> S[Shared Utilities (.github/repro-kit/actions/_shared)]
  A --> R[Repo Contracts (docs/, schemas/, canonical paths)]
  A --> O[Outputs (artifacts, reports, logs)]
~~~

### Extension points checklist (for future work)

- [ ] Add a shared helper only after it is used by 2+ actions (or you can justify the shared surface).
- [ ] Document the helper’s interface (inputs/outputs, exit codes, error modes).
- [ ] Ensure no secrets/PII can be printed by default.
- [ ] Add or update tests where they exist for the calling actions.
- [ ] Update `.github/repro-kit/actions/README.md` if discoverability changes.

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- Direct integration: N/A (this folder supports CI infrastructure).
- Indirect integration: Actions may validate Story Node docs and ensure required structure/citations.

### Provenance-linked narrative rule

- If shared helpers are used to validate Story Nodes, they must treat:
  - missing evidence links as failures (for published nodes),
  - broken internal references as failures.

### Optional structured controls

~~~yaml
focus_layers: []
focus_time: "N/A"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks (if applied to `.github/**`)
- [ ] Action-level linting (YAML validity, composite action validation)
- [ ] Shell/Script linting (if scripts exist; e.g., bash `-n`, shellcheck)
- [ ] Security review (no secrets; least-privilege expectations)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) (optional) run a local workflow runner like `act`
# act -W .github/workflows/<workflow>.yml

# 2) lint scripts (if present)
# shellcheck .github/repro-kit/actions/_shared/scripts/**/*.sh

# 3) validate markdown (if your CI validates .github markdown)
# <repo-specific markdown lint/validator>
~~~

### Telemetry signals (if applicable)

- Shared helpers must not emit telemetry with PII.
- If metrics are written to disk, prefer governed locations (e.g., `mcp/runs/`), and document the schema.

## ⚖ FAIR+CARE & Governance

- `_shared/` is infrastructure code, but it can still influence:
  - what gets logged,
  - where outputs are stored,
  - whether provenance is captured.
- Treat any change that affects logging/redaction behavior as **requires human review**.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial `_shared/` README | TBD |
