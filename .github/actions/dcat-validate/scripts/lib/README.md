---
title: "DCAT Validate Action — scripts/lib"
path: ".github/actions/dcat-validate/scripts/lib/README.md"
version: "v1.0.0"
last_updated: "2025-12-22"
status: "draft"
doc_kind: "README"
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


doc_uuid: "urn:kfm:doc:github:actions:dcat-validate:scripts:lib:readme:v1.0.0"
semantic_document_id: "kfm-gha-dcat-validate-scripts-lib-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github:actions:dcat-validate:scripts:lib:readme:v1.0.0"
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

# DCAT Validate Action — scripts/lib

## 📘 Overview

### Purpose

This folder contains **shared library code** used by the `.github/actions/dcat-validate/scripts/` entrypoints.

It exists to keep DCAT validation logic:
- reusable across multiple scripts/commands,
- deterministic and testable,
- aligned with KFM’s “contracts-first” pipeline (Catalog validators are a guardrail for downstream Graph/API/UI/Story consumption).

### Scope

| In Scope | Out of Scope |
|---|---|
| Shared helper modules used by the `dcat-validate` action scripts | GitHub workflow wiring (`.github/workflows/**`) |
| File discovery and path safety utilities | Dataset-specific ETL or catalog generation |
| Validation orchestration helpers (schema/shapes runner wrappers, error formatting, reporting payload builders) | API/UI behavior (must remain at the API/UI layer) |
| Common logging and exit-code conventions | Any logic that fetches data from the network during CI |

### Audience

- Primary: CI/CD maintainers and catalog maintainers
- Secondary: data-domain contributors troubleshooting DCAT validation failures

### Definitions (link to glossary)

- Link: `docs/glossary.md`
- Terms used in this doc: DCAT, JSON-LD, schema validation, provenance, CI gate, redaction/generalization

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Action root | `.github/actions/dcat-validate/` | TBD | Action metadata and top-level docs |
| Scripts (entrypoints) | `.github/actions/dcat-validate/scripts/` | TBD | CLI wrappers and orchestrators |
| This library directory | `.github/actions/dcat-validate/scripts/lib/` | TBD | Shared helpers used by scripts |
| Master pipeline reference | `docs/MASTER_GUIDE_v12.md` | KFM Core Team | Canonical pipeline ordering + invariants |
| DCAT outputs (canonical) | `data/catalog/dcat/` | Catalog maintainers | DCAT artifacts validated by this action |
| DCAT constraints (canonical) | `schemas/dcat/` | Schema maintainers | Schemas/shapes used by validators |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] Folder purpose and boundaries are explicit (what *can* and *cannot* live here)
- [ ] Validation steps listed and repeatable (local + CI)
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document

- `path`: `.github/actions/dcat-validate/scripts/lib/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| GitHub Actions (local actions) | `.github/actions/` | Action implementations vendored in-repo |
| DCAT validate action | `.github/actions/dcat-validate/` | DCAT validation action package |
| Action scripts | `.github/actions/dcat-validate/scripts/` | Script entrypoints (language-specific) |
| Action shared libs | `.github/actions/dcat-validate/scripts/lib/` | Shared helper modules (this folder) |
| DCAT outputs | `data/catalog/dcat/` | Catalog stage outputs (JSON-LD/RDF) |
| DCAT schemas | `schemas/dcat/` | DCAT constraints and validation resources |

### Expected file tree for this sub-area

~~~text
📁 .github/
└── 📁 actions/
    └── 📁 dcat-validate/
        └── 📁 scripts/
            └── 📁 lib/
                ├── 📄 README.md
                ├── 📄 <shared-module-1>.<ext>
                ├── 📄 <shared-module-2>.<ext>
                └── 📄 <test-helpers>.<ext>
~~~

> **not confirmed in repo:** The implementation language and exact module filenames/extensions. Keep this README language-neutral until actual modules exist.

## 📦 Data & Metadata

### Data lifecycle (required staging)

This directory contains **code**, not datasets. It should treat repository data as **read-only inputs** during CI runs.

Expected high-level behavior:
- Read DCAT artifacts from the canonical catalog outputs location (e.g., `data/catalog/dcat/**`).
- Validate against DCAT constraints located under the canonical schemas location (e.g., `schemas/dcat/**`).
- Emit **structured results** (stdout + optional machine-readable report) but do **not** write derived datasets to `data/processed/` from CI.

### Domain expansion pattern

- Keep domain-specific rules out of this `lib/` folder when possible.
- Prefer expressing DCAT constraints via schema/shape artifacts under `schemas/dcat/`.
- If the validator needs a domain mapping, treat it as configuration and keep it versioned and reviewable (avoid hardcoding rules in code).

## 🌐 STAC, DCAT & PROV Alignment

### Provenance requirements

This library should support (or at least not block) checks that enforce KFM’s minimum metadata expectations, such as:
- a minimal DCAT mapping per dataset (title/description/license/keywords),
- provenance linkage expectations (where DCAT records reference the dataset lineage that is tracked elsewhere in the pipeline).

> The validator’s job is to enforce **machine-validated contracts** at the Catalog boundary so downstream stages don’t ingest malformed metadata.

### Versioning expectations

If dataset versioning is expressed in DCAT artifacts, validation helpers should:
- encourage explicit predecessor/successor linkage,
- avoid “silent overwrite” patterns where versions cannot be audited or diffed.

## 🧱 Architecture

### Subsystem contracts (what must exist for each subsystem)

| Subsystem | Contract artifacts | “Do not break” rule |
|---|---|---|
| Catalog validation (this action) | DCAT schemas/constraints + validator runner + stable exit codes | Fail fast on invalid metadata; deterministic results |
| Catalog outputs | `data/catalog/dcat/**` | Canonical paths; machine-readable metadata |
| Graph | Ontology + migrations + constraints | UI does not read Neo4j directly; graph remains provenance-linked |
| APIs | OpenAPI/GraphQL + contract tests | API is the boundary; enforce redaction at API layer |
| UI | Layer registry + audit affordances | No hidden data leakage; provenance visible in Focus Mode |

### Next-evolution extension points

- Add new checks by adding/adjusting constraints under `schemas/dcat/` when feasible.
- Keep the `lib/` functions small and composable so scripts can mix-and-match checks (e.g., schema validation, link integrity, required-field checks).

## 🧠 Story Node & Focus Mode Integration

### Story Nodes as “machine-ingestible storytelling”

This library does not author Story Nodes, but it protects downstream narrative quality by ensuring catalogs remain valid inputs for provenance-linked UI experiences.

### Focus Mode rule

- Focus Mode only consumes provenance-linked content.
- Validators should never encourage workflows that introduce unsourced narrative or infer sensitive locations.

## 🧪 Validation & CI/CD

### Minimum CI gates for “v12-ready” contributions

When modifying code in this folder, ensure (at minimum):
- lint/format checks for the action language,
- deterministic validator runs (same input → same output),
- DCAT schema/constraint validation executes in CI,
- security scanning gates remain intact (no secrets, no unsafe shell usage, no network calls unless explicitly governed).

### Validation checklist

- [ ] No repository writes outside CI scratch/temp directories
- [ ] Inputs are only from tracked repo paths (no network fetches)
- [ ] Exit codes are stable and documented
- [ ] Errors are actionable (file path, failing rule, minimal repro)
- [ ] Any redaction/generalization rule enforcement remains contract-driven

## ⚖ FAIR+CARE & Governance

### Governance review triggers

Escalate for review when changes:
- alter what is considered “valid” DCAT (policy/contract semantics),
- add new external data sources for validation (network calls),
- introduce new redaction/generalization enforcement behavior.

### Sovereignty safety

- Do not infer sensitive locations.
- If validation involves restricted locations or culturally sensitive knowledge, ensure the checks align with `docs/governance/SOVEREIGNTY.md` and do not leak restricted details into CI logs.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial README for dcat-validate scripts/lib | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
