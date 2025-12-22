---
title: "GitHub Action — STAC Validate"
path: ".github/actions/stac-validate/README.md"
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

doc_uuid: "urn:kfm:doc:github-actions:stac-validate:v1.0.0"
semantic_document_id: "kfm-github-action-stac-validate-v1.0.0"
event_source_id: "ledger:kfm:doc:github-actions:stac-validate:v1.0.0"
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

# GitHub Action — STAC Validate

## 📘 Overview

### Purpose

- Provide a **CI gate** that validates KFM STAC artifacts (Collections + Items) before merge.
- Enforce that STAC outputs remain machine-valid and safe to consume downstream (Graph, API, UI).

### Scope

| In Scope | Out of Scope |
|---|---|
| Validate STAC JSON under `data/stac/**` | Generating STAC or modifying STAC outputs |
| Validate against `schemas/stac/**` (and any referenced STAC/core schemas used by the action) | Validating DCAT/PROV (separate gates/actions) |
| Fail CI on schema errors | Loading Neo4j / API/UI testing |
| Optional: “changed files only” validation (if implemented in the action) | External network link checking unless explicitly implemented + allowed |

### Audience

- Primary: Contributors who modify `data/stac/**`, `schemas/stac/**`, or catalog-generation pipelines.
- Secondary: Reviewers/maintainers who need fast feedback that metadata contracts are preserved.

### Definitions (link to glossary)

- Link: `docs/glossary.md`
- Terms used in this doc:
  - **STAC**: SpatioTemporal Asset Catalog
  - **Collection**: STAC Collection JSON under `data/stac/collections/`
  - **Item**: STAC Item JSON under `data/stac/items/`
  - **KFM-STAC profile**: KFM constraints layered on top of STAC core

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `.github/actions/stac-validate/README.md` | KFM maintainers | Usage + contract |
| Action definition | `.github/actions/stac-validate/action.yml` | KFM maintainers | Inputs/outputs + implementation |
| STAC outputs | `data/stac/collections/**` + `data/stac/items/**` | Catalog stage | Canonical paths |
| STAC schemas | `schemas/stac/**` | Schema owners | KFM constraints + schema bundles |
| Pipeline guide | `docs/MASTER_GUIDE_v12.md` | KFM maintainers | Canonical ordering + invariants |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] Usage example matches the action’s real `action.yml` inputs
- [ ] Validation steps listed and repeatable
- [ ] Notes clarify what this action validates vs what other gates validate
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document

- `path`: `.github/actions/stac-validate/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| STAC outputs | `data/stac/` | Collections + items produced by catalog stage |
| Schemas | `schemas/stac/` | STAC schemas + KFM constraints |
| Workflows | `.github/workflows/` | CI pipelines calling this action |
| Pipelines | `src/pipelines/` | ETL + catalog build producing `data/stac/**` |
| Governance | `docs/governance/` | FAIR+CARE + sovereignty rules |

### Expected file tree for this sub-area

~~~text
📁 .github/
└── 📁 actions/
    └── 📁 stac-validate/
        ├── 📄 README.md
        ├── 📄 action.yml
        └── 📁 scripts/
            └── 📄 validate-stac.(sh|py|js)
~~~

## 🧭 Context

### Background

KFM uses a governed pipeline where catalogs (STAC/DCAT/PROV) sit between ETL outputs and graph/API/UI consumers. If STAC JSON breaks, it can cascade into ingestion failures, broken UI layers, or missing provenance.

This action exists to make “STAC must validate” a repeatable, automated CI gate.

### Assumptions

- STAC artifacts are committed under `data/stac/collections/` and `data/stac/items/`.
- KFM schema constraints exist under `schemas/stac/`.
- Validation should be deterministic and not depend on external services.

### Constraints / invariants

- Preserve: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- Validation must not mutate repository data (read-only check).
- No inference of sensitive locations; no enrichment; no “fixups” inside CI.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Should validation run on all STAC files or only changed files? | TBD | TBD |
| Which validator engine is pinned (and where)? | TBD | TBD |
| Do we enforce additional KFM rules (stable IDs, collection existence, etc.) beyond JSON Schema? | TBD | TBD |

### Future extensions

- Optional: validate cross-file integrity (e.g., Item `collection` exists as a Collection ID).
- Optional: validate STAC `assets` shape rules (required fields, media types).
- Optional: produce a machine-readable report artifact (SARIF/JSON) for PR annotations.

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  A[ETL outputs<br/>data/&lt;domain&gt;/processed/] --> B[Catalog build]
  B --> C[STAC JSON<br/>data/stac/**]
  C --> D[CI Gate: stac-validate]
  D -->|pass| E[Graph ingest + API + UI consume]
  D -->|fail| F[Fix STAC JSON / schema / pipeline]
~~~

### Optional: sequence diagram

~~~mermaid
sequenceDiagram
  participant Dev as Contributor
  participant CI as GitHub Actions
  participant Repo as Repository

  Dev->>Repo: Push/PR changes (data/stac/**, schemas/stac/**)
  CI->>Repo: Checkout
  CI->>CI: Run stac-validate (this action)
  CI-->>Dev: Pass/Fail + logs
~~~

## 📦 Data & Metadata

### What this action validates

- STAC Collections: `data/stac/collections/**/*.json`
- STAC Items: `data/stac/items/**/*.json`

### Inputs and outputs (action interface)

**Source of truth:** `.github/actions/stac-validate/action.yml`

This README describes the expected interface pattern for a STAC validation action:
- Inputs (typical):
  - `stac_root`: root folder for STAC (default: `data/stac`)
  - `schemas_root`: root folder for schemas (default: `schemas/stac`)
  - `fail_on_warning`: whether warnings should fail CI
  - `changed_only`: validate only changed STAC files (if supported)
- Outputs (typical):
  - logs to stdout
  - optional report path / summary

If the real action uses different names, update this README to match.

## 🌐 STAC, DCAT & PROV Alignment

### Alignment policy

- STAC artifacts are a **contract**: downstream consumers rely on them to be valid.
- Validation should confirm compliance with:
  - STAC core schema expectations used by the action
  - KFM constraints in `schemas/stac/**`

### Versioning expectations

- Schema changes should be versioned and paired with:
  - updated tests/validation rules
  - updated pipelines that emit compliant STAC

## 🧱 Architecture

### How to use in a workflow

~~~yaml
name: Validate STAC

on:
  pull_request:
    paths:
      - "data/stac/**"
      - "schemas/stac/**"
      - ".github/actions/stac-validate/**"

jobs:
  stac-validate:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Validate STAC artifacts
        uses: ./.github/actions/stac-validate
        with:
          stac_root: "data/stac"
          schemas_root: "schemas/stac"
          fail_on_warning: "true"
~~~

### Local validation (developer workflow)

Use the same validator/toolchain that the action uses (see `action.yml`) so results match CI.
If the action provides a script entrypoint under `.github/actions/stac-validate/`, run that locally.

~~~text
# Example patterns (update to match the action):
# - ./ .github/actions/stac-validate/scripts/validate-stac.sh
# - python .github/actions/stac-validate/scripts/validate_stac.py --stac-root data/stac --schemas-root schemas/stac
~~~

## 🧠 Story Node & Focus Mode Integration

- This action does **not** validate Story Nodes.
- Story Node validation is a separate CI gate (front-matter, citations, entity references, redaction compliance).

## 🧪 Validation & CI/CD

### Validation checklist

- [ ] All `data/stac/collections/**/*.json` files validate
- [ ] All `data/stac/items/**/*.json` files validate
- [ ] Schema changes in `schemas/stac/**` are compatible with intended outputs
- [ ] No CI step writes back to `data/stac/**` (validation is read-only)

## ⚖ FAIR+CARE & Governance

### Review gates

- Schema changes in `schemas/stac/**` require maintainer review.
- Changes impacting sensitivity/redaction handling require governance review per:
  - `docs/governance/ROOT_GOVERNANCE.md`
  - `docs/governance/SOVEREIGNTY.md`

### CARE / sovereignty considerations

- This action must not attempt to infer or “repair” sensitive geometries.
- Any restricted-location protections are enforced by:
  - redaction/generalization policies in the pipeline and API boundary
  - dedicated sovereignty scanning gates (if configured)

### AI usage constraints

- This action performs deterministic validation only; no AI generation.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial README for STAC validation action | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
