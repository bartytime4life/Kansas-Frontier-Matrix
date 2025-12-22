---
title: "GitHub Action — dcat-validate (DCAT validation)"
path: ".github/actions/dcat-validate/README.md"
version: "v1.0.0"
last_updated: "2025-12-22"
status: "draft"
doc_kind: "CI"
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

doc_uuid: "urn:kfm:doc:github:actions:dcat-validate:readme:v1.0.0"
semantic_document_id: "kfm-github-action-dcat-validate-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github:actions:dcat-validate:readme:v1.0.0"
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

# GitHub Action — dcat-validate

## 📘 Overview

### Purpose
This README documents the **local GitHub Action** located at `.github/actions/dcat-validate/`.

Its intent is to validate **DCAT** catalog outputs produced by the KFM catalog stage (typically under `data/catalog/dcat/`) against the repository’s governed **schema/shape constraints** (typically under `schemas/dcat/`).

This supports KFM’s CI posture where **STAC/DCAT/PROV JSON artifacts are validated against schemas in `schemas/`**.

### Scope

| In Scope | Out of Scope |
|---|---|
| Validating DCAT outputs under `data/catalog/dcat/` | Generating DCAT outputs |
| Failing CI when DCAT records are invalid | Building STAC, PROV, graph, API, or UI artifacts |
| Providing a repeatable validation command in CI | Defining the DCAT profile itself (belongs in `docs/standards/` + `schemas/`) |
| (Optional) Emitting a validation report for debugging | Publishing catalogs externally |

### Audience
- Primary: CI maintainers and workflow authors (`.github/workflows/**`)
- Secondary: Catalog maintainers and data/domain pipeline authors

### Definitions (link to glossary)
- Link: `docs/glossary.md` (not confirmed in repo)
- DCAT: W3C Data Catalog Vocabulary (typically serialized as RDF / JSON-LD)
- JSON-LD: JSON serialization for Linked Data
- “Validation”: checking DCAT records against repository-governed schema/shape constraints

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This Action (local) | `.github/actions/dcat-validate/` | CI owners | Local action invoked by workflows |
| DCAT outputs | `data/catalog/dcat/` | Catalog stage | Canonical home for DCAT outputs |
| DCAT constraints | `schemas/dcat/` | Contracts owners | JSON Schema and/or SHACL shapes (not confirmed in repo) |
| Master Guide | `docs/MASTER_GUIDE_v12.md` | Maintainers | Canonical pipeline ordering |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Action intent and scope are explicit (what it validates + where inputs live)
- [ ] Usage examples are present for GitHub workflows
- [ ] Validation behavior is deterministic and repeatable (same inputs → same results)
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `.github/actions/dcat-validate/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| GitHub Actions (local actions) | `.github/actions/` | Composite/local actions used by workflows |
| Catalog outputs | `data/catalog/dcat/` | DCAT outputs (JSON-LD) |
| Schemas / constraints | `schemas/` | Machine-validated schemas and shape bundles |
| Workflows | `.github/workflows/` | CI pipelines that call this action |

### Expected file tree for this sub-area
~~~text
📁 .github/
└── 📁 actions/
    └── 📁 dcat-validate/
        ├── 📄 README.md          # this document
        ├── 📄 action.yml         # GitHub Action definition (not confirmed in repo)
        └── 📁 scripts/           # helper scripts (optional; not confirmed in repo)
~~~

## 🧭 Context

### Background
KFM treats catalogs (STAC/DCAT/PROV) as **first‑class evidence/contract artifacts** and expects them to validate in CI so metadata errors are caught early and downstream systems can rely on stable contracts.

### Assumptions
- DCAT records are stored under `data/catalog/dcat/` as JSON-LD.
- The repo contains DCAT constraint artifacts under `schemas/dcat/`.
- The CI workflow calling this action follows the policy: **validate if present; fail if invalid; skip if not applicable**.

(If any assumption is wrong, update this README to match `action.yml` and the repo’s actual paths.)

### Constraints / invariants
- Canonical pipeline ordering is preserved:

  **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**

- Validation gates are intended to be deterministic and contract-first:
  - Schemas/specs are canonical in `schemas/`.
  - Catalog outputs live in `data/**` (not in `docs/`).
  - CI should fail on invalid contract artifacts.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Does validation use JSON Schema, SHACL, or both for DCAT JSON-LD? | Catalog + contracts owners | TBD |
| Should the action validate one file, a directory, or both? | CI owners | TBD |
| Should link integrity checks (e.g., referenced distributions) be added? | Catalog owners | TBD |

### Future extensions
- Emit a machine-readable report artifact (`.json`) plus a GitHub job summary.
- Add optional link checks for distributions/assets referenced by DCAT records.
- Add cross-consistency checks (DCAT ↔ STAC ↔ PROV identifiers).

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  PR[Pull request / commit] --> CI[GitHub Actions workflow]
  CI --> A[Local action: dcat-validate]
  A --> D[data/catalog/dcat/**]
  A --> S[schemas/dcat/**]
  A --> R[Result: pass/fail + report]
~~~

## 📦 Data & Metadata

### Inputs validated
- DCAT dataset records (typically JSON-LD) under `data/catalog/dcat/`.

### Outputs
- CI pass/fail signal (job success/failure)
- Optional validation report artifact (format + path not confirmed in repo)

## 🌐 STAC, DCAT & PROV Alignment

- DCAT outputs are part of KFM’s catalog stage and are expected to be validated against governed schemas.
- DCAT records should carry discoverability metadata (title/description/license/keywords at minimum) and link to distributions/assets in a controlled, repeatable way (exact field requirements are governed by the KFM DCAT profile and `schemas/dcat/**`).

## 🧱 Architecture

### Action contract
**Not confirmed in repo:** this README does not assert the actual `action.yml` interface. Treat the following as a *recommended contract shape* and keep it aligned with `action.yml`.

#### Recommended inputs
| Input | Required | Default | Meaning |
|---|---|---:|---|
| `dcat_path` | no | `data/catalog/dcat` | Path to DCAT outputs (file or directory) |
| `schema_path` | no | `schemas/dcat` | Path to DCAT constraints/shapes |
| `fail_on_warning` | no | `true` | Whether warnings should fail CI |
| `report_path` | no | `artifacts/dcat-validate/report.json` | Where to write a report (if supported) |

#### Recommended behavior
- Enumerate DCAT JSON(-LD) records in `dcat_path`
- Validate against `schema_path`
- Exit non‑zero if any invalid records are found

### Example usage in a workflow
~~~yaml
jobs:
  dcat_validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      # Minimal usage (preferred if the action has sensible defaults)
      - name: Validate DCAT
        uses: ./.github/actions/dcat-validate

      # Extended usage (update names to match action.yml; not confirmed in repo)
      # - name: Validate DCAT (explicit paths)
      #   uses: ./.github/actions/dcat-validate
      #   with:
      #     dcat_path: data/catalog/dcat
      #     schema_path: schemas/dcat
~~~

## 🧠 Story Node & Focus Mode Integration
This action is upstream of narrative delivery:
- By ensuring DCAT records are valid, downstream layers (API/UI/Story Nodes) can rely on stable dataset identifiers and metadata.
- Focus Mode must remain provenance-linked; this action supports that stance indirectly by enforcing catalog correctness.

## 🧪 Validation & CI/CD
Recommended CI mapping:
- [ ] Markdown protocol validation for docs (separate job)
- [ ] DCAT validation via this action
- [ ] Fail fast on schema violations
- [ ] Optionally upload a validation report artifact for debugging

## ⚖ FAIR+CARE & Governance

### Governance review triggers
- Changes to DCAT constraint artifacts (`schemas/dcat/**`) likely require contracts owner review.
- New datasets / new public metadata should be reviewed for licensing/attribution completeness.

### CARE / sovereignty considerations
- Metadata can still expose sensitive information (e.g., restricted locations in descriptions).
- If a dataset is sensitive, enforce redaction/generalization **before** publishing DCAT records and ensure reviewers approve the metadata content.

### AI usage constraints
- This README permits summarization/structure extraction but prohibits generating new policy or inferring sensitive locations (see front-matter).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial scaffold for local action README | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
