---
title: "data/work/tmp — Temporary Workspace"
path: "data/work/tmp/README.md"
version: "v1.0.0"
last_updated: "2025-12-19"
status: "draft"
doc_kind: "Readme"
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

doc_uuid: "urn:kfm:doc:data:work:tmp-readme:v1.0.0"
semantic_document_id: "kfm-data-work-tmp-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:work:tmp-readme:v1.0.0"
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

# data/work/tmp — Temporary Workspace

## 📘 Overview

### Purpose
- Provide an **ephemeral scratch space** for pipeline runs (downloads, decompression, intermediate transforms, and other short-lived artifacts).
- Keep **reproducible / governed** outputs out of `tmp` by “promoting” them into the appropriate stable locations (e.g., `data/work/staging/`, `data/work/processed/`, `data/processed/`, `data/stac/`, `data/catalog/dcat/`, `data/prov/`).

### Scope
**In-scope (temporary / disposable):**
- Partial downloads, extracted archives, intermediate joins, scratch exports, one-off debug artifacts.
- Run-scoped caches that can be safely regenerated.

**Out-of-scope (must NOT live here long-term):**
- Source-of-truth raw ingests → use `data/raw/` (and/or `data/sources/` depending on domain conventions).
- Stable intermediates → use `data/work/staging/` or `data/work/processed/`.
- Published outputs → use `data/processed/` plus catalogs (`data/stac/`, `data/catalog/dcat/`, `data/prov/`).
- Long-lived logs → use `data/work/logs/` or `mcp/runs/` (if applicable).

### Audience
- Pipeline/ETL developers
- Data curators performing ingestion/standardization
- QA/reviewers validating that sensitive or non-reproducible artifacts are not being committed

### Definitions (link to glossary)
- **Work area:** A non-source-of-truth workspace used during ETL.
- **Promotion:** Moving outputs from scratch (`tmp`) into stable, versioned, and governed locations.
- **Run scope:** Files tied to a single execution (often keyed by a run id).

### Key artifacts (what this doc points to)
| Artifact | Where it lives | What it is | Must be committed? |
|---|---|---|---|
| Temporary scratch files | `data/work/tmp/` | Disposable intermediates | **No** |
| Staging-ready data | `data/work/staging/` | Cleaned inputs ready for deterministic transforms | Depends on repo policy |
| Stable work outputs | `data/work/processed/` | Consistent intermediates suitable for review | Depends on repo policy |
| Published processed data | `data/processed/` | Durable, versioned outputs | **Yes (typically)** |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Discovery + provenance artifacts | **Yes** |

### Definition of done (for this document)
- [ ] Describes what belongs in `data/work/tmp/` vs what does not.
- [ ] Includes a clear “do not commit from here” guideline.
- [ ] Shows the expected folder layout and run-scoping convention.
- [ ] Links to canonical pipeline and repository locations.

## 🗂 Directory Layout

### This document
- You are reading: `data/work/tmp/README.md`

### Related repository paths
- `data/README.md`
- `data/work/README.md`
- `data/work/staging/README.md`
- `data/work/processed/README.md`
- `data/work/logs/README.md`
- `docs/MASTER_GUIDE_v12.md`

### Expected file tree for this sub-area
~~~text
📁 data/
└── 📁 work/
    └── 📁 tmp/
        ├── 📄 README.md
        ├── 📄 .gitkeep              # optional (only if repo requires to keep empty dirs)
        └── 📁 runs/                 # optional convention (run-scoped scratch)
            └── 📁 run_<run_id>/     # e.g., run_20251219T153000Z_ab12cd
                ├── 📄 <temp_files...>
                └── 📁 <temp_subdirs...>
~~~

## 🧭 Context

### Background
KFM’s canonical pipeline ordering is:
**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**.

`data/work/tmp/` supports the **ETL** portion by providing a safe “scratchpad” that can be cleaned without breaking provenance or published datasets.

### Assumptions
- Temporary artifacts are **safe to delete** after a successful run.
- Where possible, temporary artifacts are **run-scoped** (e.g., under `data/work/tmp/runs/run_<run_id>/`) to avoid collisions.

> If your pipeline currently writes directly into `data/work/tmp/` without run-scoping, consider adopting a run directory convention to keep artifacts isolated (project convention; confirm with pipeline owners).

### Constraints / invariants
- **No long-term dependencies:** downstream steps should not rely on files remaining in `tmp` after completion.
- **No secrets / credentials:** never store tokens, private keys, or connection strings here.
- **Sensitive data caution:** even temporary copies can be sensitive—avoid committing and ensure cleanup.
- **Promotion rule:** if an artifact is required for reproducibility, cataloging, or review, move it out of `tmp` into a governed location.

### Open questions
- Should the repo enforce a standard run directory name (e.g., `run_<YYYYMMDDTHHMMSSZ>_<short_hash>`)?
- Should there be an automated cleanup step (make target / script) and a documented retention window?

### Future extensions
- Add a cleanup script and retention policy doc (e.g., `tools/cleanup_tmp.sh`) aligned with governance and CI checks.
- Add disk-usage telemetry alerts if runs can be large.

## 🗺 Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[data/raw] --> B[data/work/tmp]
  B --> C[data/work/staging]
  C --> D[data/work/processed]
  D --> E[data/processed]
  E --> F[data/stac + data/catalog/dcat + data/prov]
  F --> G[Neo4j]
  G --> H[APIs]
  H --> I[React/Map UI]
  I --> J[Story Nodes]
  J --> K[Focus Mode]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant ETL as ETL Pipeline
  participant TMP as data/work/tmp
  participant STAGE as data/work/staging
  participant PROC as data/work/processed
  ETL->>TMP: write scratch intermediates
  ETL->>STAGE: promote staging-ready outputs
  ETL->>PROC: promote stable intermediates (optional)
  ETL-->>TMP: cleanup tmp artifacts (recommended)
~~~

## 📦 Data & Metadata

### Inputs
- Any transient inputs generated during ingestion: downloaded archives, extracted files, intermediate tables, temporary GIS exports, etc.

### Outputs
- Expected: **none** that are relied upon long-term.
- Any output needed for reproducibility should be promoted out of `tmp` and documented in the appropriate README.

### Sensitivity & redaction
- Treat `tmp` as potentially containing sensitive content (even briefly).
- Do not commit contents from `tmp`.
- If sensitive data must be handled, ensure redaction/filters occur before promotion into stable locations.

### Quality signals
- N/A for `tmp` itself. Quality checks should run on promoted artifacts (staging/processed outputs).

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- `tmp` artifacts should **not** be referenced by STAC Items/Collections.

### DCAT
- `tmp` artifacts should **not** be referenced by DCAT dataset entries.

### PROV-O
- If a transformation uses temp artifacts, provenance should describe **inputs and promoted outputs**, not require `tmp` files to remain.

### Versioning
- Any versioning that matters should happen at the dataset/catalog layer, not in `tmp`.

## 🧱 Architecture

### Components
- ETL scripts may read/write here as a scratch space.
- Cleanup steps (manual or automated) should keep the directory tidy between runs.

### Interfaces / contracts
- No API or UI component should consume from `data/work/tmp/` directly.
- Only promoted, governed outputs should be used for catalogs and downstream ingestion.

### Extension points checklist (for future work)
- [ ] Standardize run id naming
- [ ] Add cleanup tooling + documentation
- [ ] Add CI guardrails to prevent committing `tmp` artifacts

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- It should not. `tmp` is intentionally non-user-facing and non-citable.

### Provenance-linked narrative rule
- Only promoted, cataloged, and provenance-backed artifacts should be used as evidence for narratives.

### Optional structured controls
~~~yaml
focus_layers:
  include:
    - "cataloged_datasets_only"
  exclude:
    - "data/work/tmp/**"
~~~

## 🧪 Validation & CI/CD

### Validation steps
- Confirm `data/work/tmp/` is excluded from version control (typically via `.gitignore`).
- Confirm pipeline steps promote required artifacts out of `tmp`.
- Confirm cleanup does not remove promoted artifacts.

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) run ETL
# 2) validate catalogs
# 3) run tests / lint
~~~

### Telemetry signals (if applicable)
- Disk usage under `data/work/tmp/`
- Run directory count
- Cleanup success/failure

## ⚖ FAIR+CARE & Governance

### Review gates
- PR review should confirm no `tmp` artifacts were committed.
- Any change that affects handling of sensitive data requires human review.

### CARE / sovereignty considerations
- Temporary storage still counts as “handling” data; apply sovereignty constraints before promotion and publication.

### AI usage constraints
- Do not run AI transforms on sensitive data without following governance constraints and recording provenance.

## 🕰 Version History
| Version | Date | Change | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial README for `data/work/tmp/` | <name/handle> |
