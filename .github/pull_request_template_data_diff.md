---
title: "Pull Request Template — Data Diff"
path: ".github/pull_request_template_data_diff.md"
version: "v1.0.0"
last_updated: "2025-12-23"
status: "active"
doc_kind: "Template"
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

doc_uuid: "urn:kfm:doc:github:pr-template:data-diff:v1.0.0"
semantic_document_id: "kfm-github-pr-template-data-diff-v1.0.0"
event_source_id: "ledger:kfm:doc:github:pr-template:data-diff:v1.0.0"
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

# Data Diff Pull Request Template

> Use this template when your PR changes **data artifacts** and/or **metadata catalogs**, including (but not limited to) `data/**`, `data/stac/**`, `data/catalog/dcat/**`, `data/prov/**`, and Story Node outputs under `docs/reports/story_nodes/`.

## 📘 Overview

### Purpose

- Make data changes reviewable by requiring **clear diffs**, **provenance**, and **validation evidence**.
- Keep contributions aligned to the canonical ordering: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.

### Scope

| In Scope | Out of Scope |
|---|---|
| Data additions/updates/removals | Pure code refactors with no data impact |
| Catalog/lineage updates (STAC/DCAT/PROV) | Unreviewed policy changes |
| Reproducibility + provenance evidence | Attaching sensitive data or secrets to PR description |

### Audience

- Primary: reviewers of data/ETL/catalog changes.
- Secondary: contributors preparing reproducible data updates.

### Definitions

- Data lifecycle: `data/raw/` → `data/work/` → `data/processed/` → `data/stac/` (+ reports as needed)
- Catalogs:
  - STAC: spatiotemporal asset catalog
  - DCAT: dataset catalog metadata
  - PROV: lineage records

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Data outputs | `data/processed/` | Data maintainers | Derived artifacts only |
| STAC catalogs | `data/stac/` | Catalog maintainers | Collections + Items |
| DCAT catalogs | `data/catalog/dcat/` | Catalog maintainers | Dataset metadata |
| PROV lineage | `data/prov/` | Pipeline maintainers | Activities + derivations |
| Story Nodes | `docs/reports/story_nodes/` | Story editors | Narrative artifacts |
| Schemas | `schemas/` | Schema maintainers | JSON schema validation |

### Definition of done

- [ ] Data diffs are summarized (counts, sizes, key distribution changes).
- [ ] STAC/DCAT/PROV artifacts updated as required.
- [ ] Determinism/reproducibility documented (inputs, versions, run ID).
- [ ] Validation gates pass (schema, graph integrity, security as applicable).
- [ ] No sensitive information is disclosed.

## 🗂️ Directory Layout

### This document

- `path`: `.github/pull_request_template_data_diff.md`

### Expected file tree for affected areas

~~~text
📁 data/
├── 📁 raw/
├── 📁 work/
├── 📁 processed/
├── 📁 stac/
│   ├── 📁 collections/
│   └── 📁 items/
├── 📁 catalog/
│   └── 📁 dcat/
└── 📁 prov/
~~~

## 📦 Data & Metadata

### Summary

<!-- 2–5 sentences: What changed and why? -->

### Data lifecycle impact

Check all that apply and list the paths impacted.

- [ ] `data/raw/` changed:
  - Paths:
- [ ] `data/work/` changed:
  - Paths:
- [ ] `data/processed/` changed:
  - Paths:
- [ ] `data/stac/` changed:
  - Collection IDs:
  - Item IDs:
- [ ] `data/catalog/dcat/` changed:
  - Dataset IDs:
- [ ] `data/prov/` changed:
  - Activity/run IDs:
- [ ] Graph ingestion impacted (Neo4j build/import):
  - Labels/relationships impacted:
- [ ] Story Nodes impacted:
  - Paths:

### Data diff summary

Provide a reviewer-friendly diff. Examples of acceptable summaries:
- record/row counts
- feature counts by geometry type
- key distribution changes (top categories)
- spatial/temporal coverage changes
- file sizes/compression changes

| Artifact | Before | After | How measured | Notes |
|---|---:|---:|---|---|
| (example) row_count |  |  |  |  |
| (example) bbox |  |  |  |  |
| (example) time_range |  |  |  |  |

### Provenance and reproducibility

- Source snapshot(s) / identifiers:
- ETL run ID / manifest (if available):
- Tooling versions (critical):
- Determinism notes (idempotent run? fixed seeds?):

## 🌐 STAC, DCAT & PROV Alignment

Check all that apply:

- [ ] New dataset includes **STAC Collection + Item(s)**.
- [ ] New dataset includes **DCAT mapping** (title/description/license/keywords minimum).
- [ ] New dataset includes **PROV activity/run record** (`prov:wasGeneratedBy`, `prov:wasDerivedFrom`).
- [ ] Version lineage recorded (predecessor/successor links where relevant).

## 🧪 Validation & CI/CD

Confirm validations you ran or that CI will run:

- [ ] Markdown protocol validation
- [ ] JSON schema validation (STAC/DCAT/telemetry as applicable)
- [ ] Graph integrity tests (if graph-related)
- [ ] API contract tests (if API-related)
- [ ] UI layer registry schema checks (if UI-related)
- [ ] Security + sovereignty scanning gates (where applicable)

If any validation was skipped, explain why:

<!-- explanation -->

## ⚖ FAIR+CARE & Governance

- Sensitivity classification change needed?
  - [ ] No
  - [ ] Yes (explain and link to governance artifact)

- Sovereignty / restricted information considered?
  - [ ] Not applicable
  - [ ] Yes, and redaction/generalization rules were applied

- New external data source introduced?
  - [ ] No
  - [ ] Yes (requires human review)

## 🧠 Story Node & Focus Mode Integration

If Story Nodes were changed or added:

- [ ] Each factual claim maps to a cited dataset/document ID.
- [ ] Any predictive content is opt-in and includes uncertainty metadata.
- [ ] Draft vs published workflow respected.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-23 | Initial data-diff PR template | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
