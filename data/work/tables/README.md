---
title: "KFM Data Work Tables — README"
path: "data/work/tables/README.md"
version: "v1.0.0"
last_updated: "2025-12-19"
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

doc_uuid: "urn:kfm:doc:data:work:tables:readme:v1.0.0"
semantic_document_id: "kfm-data-work-tables-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:work:tables:readme:v1.0.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# KFM Data Work Tables — README

## 📘 Overview

### Purpose
This directory holds **intermediate tabular outputs** produced during ETL and curation work (e.g., extracts, normalized tables, joins, QA snapshots) **before** promoting artifacts into canonical `data/processed/` outputs and/or catalog products (STAC/DCAT/PROV).

Treat everything here as **work staging**: useful for iterative development, debugging, and reproducibility, but not automatically considered “final” or stable.

### Scope

| In Scope | Out of Scope |
|---|---|
| Intermediate tables (CSV/Parquet) created during ingestion/normalization | Final “published” datasets (use `data/processed/`) |
| Temporary or run-scoped joins/denormalizations | Canonical STAC Items/Collections (use `data/stac/`) |
| QA/validation exports (row counts, null checks, schema snapshots) | Secrets, credentials, tokens |
| Human-in-the-loop curation tables for later promotion | PII or sensitive records (unless governance explicitly approves and storage is restricted — **not confirmed in repo**) |

### Audience
- Primary: ETL/pipeline developers, data curators
- Secondary: reviewers validating reproducibility and provenance

### Definitions (link to glossary)
- Link: `docs/glossary.md` (**not confirmed in repo**)
- Terms used in this doc:
  - **Work tables:** intermediate tables generated during ETL work staging.
  - **Promotion:** the act of moving a vetted work artifact into `data/processed/` and attaching catalogs/provenance where required.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Work tables root | `data/work/tables/` | DataOps | Intermediate tabular artifacts |
| Canonical processed outputs | `data/processed/` | DataOps | Promote stable outputs here |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | DataOps | Where “published” metadata lives |

### Definition of done (for this document)
- [ ] Explains what belongs in `data/work/tables/` vs other `data/` stages
- [ ] Provides a safe naming + layout convention (clearly labeled if “not confirmed in repo”)
- [ ] Includes minimum validation expectations before promotion
- [ ] States governance + sensitivity guardrails (no leakage, no secrets)

## 🗂️ Directory Layout

### This document
- `path`: `data/work/tables/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Raw intake | `data/raw/` | Original, minimally touched sources |
| Work staging | `data/work/` | Intermediate artifacts, scratch work |
| Work tables | `data/work/tables/` | Intermediate tabular extracts/joins |
| Processed outputs | `data/processed/` | Vetted, stable, reusable datasets |
| STAC catalogs | `data/stac/` | STAC Collections + Items |
| DCAT catalogs | `data/catalog/dcat/` | DCAT dataset views |
| PROV bundles | `data/prov/` | Provenance lineage bundles |

### Expected file tree for this sub-area
> This is an **illustrative** structure (some folders/filenames are **not confirmed in repo**).  
> Adjust to match the repo’s actual conventions once established.

~~~text
📁 data/
└── 📁 work/
    └── 📁 tables/
        ├── 📄 README.md
        ├── 📁 <domain>/                         # not confirmed in repo
        │   └── 📁 <dataset_or_source>/           # not confirmed in repo
        │       ├── 📁 run_<run_id>/              # not confirmed in repo
        │       │   ├── 📄 <table>.csv
        │       │   ├── 📄 <table>.parquet
        │       │   ├── 📄 schema.json            # not confirmed in repo
        │       │   ├── 📄 manifest.json          # not confirmed in repo
        │       │   └── 📄 checksums.sha256       # not confirmed in repo
        │       └── 📁 latest/                    # not confirmed in repo
        │           └── 📄 <table>.parquet
        └── 📁 _tmp/                              # not confirmed in repo
~~~

## 🧭 Context

### Background
KFM’s canonical ordering is preserved end-to-end:
**ETL → STAC/DCAT/PROV catalogs → Graph → APIs → UI → Story Nodes → Focus Mode**.

`data/work/tables/` sits firmly in the **ETL/work staging** portion. It is where tabular artifacts may be iterated on, compared across runs, and validated before becoming long-lived, cataloged data products.

### Assumptions
- ETL outputs should be deterministic and reproducible (same inputs/config → same outputs).
- Work tables may be overwritten or superseded; stable/curated artifacts should be promoted out.

### Constraints / invariants
- Maintain canonical pipeline ordering (do not treat work tables as “published” outputs).
- **No secrets or credentials** in any `data/` directory.
- **No sensitive or restricted locations/records** unless governance explicitly allows and storage rules exist (**not confirmed in repo**).
- Frontend consumes data through APIs (no direct graph dependency).

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Preferred “work table” format defaults (CSV vs Parquet) | TBD | TBD |
| Required sidecar metadata format (schema.json/manifest.json) | TBD | TBD |
| Run ID convention (timestamp? git SHA? both?) | TBD | TBD |

### Future extensions
- Add a governed schema for table sidecars (schema + manifest) under `schemas/` (**not confirmed in repo**).
- Add automated validation summaries (row counts, null distribution, uniqueness) emitted per run.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[data/raw sources] --> B[ETL transforms]
  B --> C[data/work/tables intermediate tables]
  C --> D[data/processed promoted datasets]
  D --> E[STAC/DCAT/PROV catalogs]
  E --> F[Graph + APIs + UI]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Raw tables/text extracts | CSV/JSON/TXT | `data/raw/` or source ingestion | Basic parse + encoding checks |
| Intermediate transforms | CSV/Parquet | prior ETL step | schema + row-count sanity |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Work tables | CSV / Parquet | `data/work/tables/...` | Local schema contract (recommended; **not confirmed in repo**) |
| QA snapshots | CSV / JSON | `data/work/tables/...` | Local conventions |

### Recommended naming conventions
> Recommended guidance (final conventions **not confirmed in repo**):

- Use `snake_case` for filenames and columns.
- Prefer **one table per file** (avoid multi-sheet work artifacts in this folder).
- If multiple runs exist, keep outputs under a run folder (`run_<run_id>/`) to avoid silent overwrites.
- If a “latest” pointer is needed, ensure it’s derived from an explicit run and reproducible.

### Sensitivity & redaction
- If any work table contains potentially sensitive fields (PII, culturally sensitive locations, restricted site coordinates), do **not** commit it to the repository unless governance explicitly authorizes it.
- Prefer generating **redacted/public** work tables for collaboration and review.

### Quality signals
Before promoting a table out of `data/work/tables/`, capture at least:
- Row count and column count
- Percent missing per column
- Uniqueness checks for expected keys
- Range checks for numeric fields
- Geometry validity (if geometry columns exist; **not confirmed in repo**)

## 🌐 STAC, DCAT & PROV Alignment

### STAC
Work tables are not automatically STAC assets. If a work table becomes a durable evidence artifact, consider promotion to `data/processed/` and then:
- Model it as a cataloged asset (STAC Item/Collection) when appropriate.

### DCAT
Work tables are not DCAT datasets by default. Promotion to a recognized dataset should include DCAT mapping.

### PROV-O
When promoted, ensure provenance can be expressed:
- `prov:wasDerivedFrom`: source IDs (raw sources and intermediate steps)
- `prov:wasGeneratedBy`: pipeline run/activity ID

### Versioning
- Prefer immutable run outputs + explicit promotion rather than in-place edits.
- If work tables are used downstream, pin to a specific run artifact rather than a moving “latest” pointer.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| ETL | Extract/normalize/create interim tables | Deterministic runs + logs |
| Work tables | Hold intermediate tabular artifacts | File paths + optional sidecars |
| Promotion step | Move vetted work artifacts to stable area | Versioned outputs + catalogs |

### Interfaces / contracts
If a work table is used by multiple pipeline steps, define:
- a stable schema (column names/types/meaning),
- a key strategy (unique IDs),
- and an upgrade plan if the schema changes (**not confirmed in repo**).

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Confirm no secrets/credentials present in committed artifacts
- [ ] Confirm no restricted/sensitive data is committed without approvals
- [ ] Validate format consistency (CSV/Parquet readability)
- [ ] Run row-count and key uniqueness sanity checks
- [ ] If promoting: add/validate STAC/DCAT/PROV artifacts

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands (not confirmed in repo)
# 1) run ETL step that writes to data/work/tables
# 2) run validation checks
# 3) promote vetted outputs to data/processed
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| ETL run metadata | pipeline runner | `mcp/runs/` or `docs/telemetry/` (not confirmed in repo) |

## ⚖ FAIR+CARE & Governance

### Review gates
- Any table promoted to `data/processed/` should be reviewed for:
  - provenance completeness,
  - license/attribution,
  - sensitivity classification.

### CARE / sovereignty considerations
- Do not infer or expose sensitive locations.
- If a dataset implicates community stewardship or cultural sensitivity, follow sovereignty guidance.

### AI usage constraints
This README does not authorize generating new “facts.” Any AI assistance should remain within:
- summarization,
- structure extraction,
- keyword indexing,
and must not infer sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial README for `data/work/tables/` | TBD |
