---
title: "data/work/tmp/text/validation/runs — README"
path: "data/work/tmp/text/validation/runs/README.md"
version: "v1.0.0"
last_updated: "2025-12-19"
status: "active"
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

doc_uuid: "urn:kfm:doc:data:work:tmp:text:validation:runs:readme:v1.0.0"
semantic_document_id: "kfm-data-work-tmp-text-validation-runs-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:work:tmp:text:validation:runs:readme:v1.0.0"
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

# data/work/tmp/text/validation/runs — README

## 📘 Overview

### Purpose
This directory stores **per-run, temporary artifacts** produced by **text validation** steps in the KFM ETL pipeline (e.g., validating extracted/OCR’d text quality, structure, encoding, or downstream-ready constraints). It exists to support reproducibility, debugging, and QA without polluting canonical datasets.

### Scope

| In Scope | Out of Scope |
|---|---|
| Per-run folders and artifacts for text validation | Canonical processed datasets (promote elsewhere) |
| Manifests, metrics, findings, and human-readable reports | STAC/DCAT/PROV catalogs (publish elsewhere) |
| Logs associated with a validation run | Long-term audit logs (store in appropriate log area) |

### Audience
- Primary: Pipeline/ETL maintainers, data curators performing QA
- Secondary: Contributors debugging ingestion and extraction

### Definitions
- Link: `docs/glossary.md` *(not confirmed in repo)*
- Terms used in this doc:
  - **run_id**: Unique identifier for a single validation execution.
  - **manifest**: A small metadata file describing inputs, configuration, and outputs for a run.
  - **findings**: Machine-readable issues emitted by validation checks.
  - **promotion**: Moving validated outputs into a non-temporary, canonical location.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Run folder | `data/work/tmp/text/validation/runs/<run_id>/` | ETL maintainers | One folder per run |
| Run manifest | `.../<run_id>/manifest.yaml` | ETL maintainers | Inputs, tool versions, checks, output refs |
| Findings | `.../<run_id>/findings.jsonl` | ETL maintainers | Row-oriented issues/warnings/errors |
| Metrics | `.../<run_id>/metrics.json` | ETL maintainers | Aggregate QA stats |
| Human report | `.../<run_id>/report.md` | Curators / QA | Optional narrative summary |
| Run logs | `.../<run_id>/logs/` | ETL maintainers | Execution logs for debugging |

### Definition of done
- [ ] Front-matter complete + valid
- [ ] Purpose and boundaries of this directory are unambiguous
- [ ] Expected file tree and naming conventions are described
- [ ] Safety notes included (PII/secrets/generalization expectations)
- [ ] Promotion path clearly described (where validated outputs go)

## 🗂️ Directory Layout

### This document
- `path`: `data/work/tmp/text/validation/runs/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Temporary text validation workspace | `data/work/tmp/text/validation/` | Validation configuration, shared utilities, and this runs area |
| Temporary work artifacts | `data/work/tmp/` | Ephemeral workspace (safe to prune) |
| Work data | `data/work/` | Non-canonical intermediate results |
| Canonical staged-by-domain pattern | `data/<domain>/{raw,work,processed,stac}/` | Domain-specific data lifecycle (if used) |
| Catalog outputs | `data/stac/` / `data/catalog/dcat/` | STAC/DCAT records for discoverability |
| Provenance outputs | `data/prov/` | PROV run/activity outputs for lineage |
| Pipelines | `src/pipelines/` | ETL + catalog builders + transforms |
| Schemas | `schemas/` | Validation schemas for data and metadata |

### Expected file tree for this sub-area
~~~text
📁 data/
└── 📁 work/
    └── 📁 tmp/
        └── 📁 text/
            └── 📁 validation/
                └── 📁 runs/
                    ├── 📄 README.md
                    ├── 📁 20251219T153012Z__text-validate__src-<source_id>__<hash8>/
                    │   ├── 📄 manifest.yaml
                    │   ├── 📄 findings.jsonl
                    │   ├── 📄 metrics.json
                    │   ├── 📄 summary.json
                    │   ├── 📄 report.md
                    │   └── 📁 logs/
                    │       └── 📄 run.log
                    └── 📄 _index.jsonl
~~~

## 🧭 Context

### Background
Text extraction (including OCR and parsing) can produce noisy or malformed outputs. Validation runs provide an auditable, repeatable way to:
- detect structural/encoding issues early,
- quantify quality,
- decide whether to promote a result to a downstream stage.

### Assumptions
- Run artifacts are **temporary** and may be pruned.
- Input documents should be **referenced by path + checksum** in manifests whenever possible rather than duplicated here.
- Promotion targets exist elsewhere (e.g., `data/work/processed/` or domain-specific `data/<domain>/processed/`).

### Constraints / invariants
- Canonical system ordering is preserved:
  - ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode
- Validation run artifacts are **not** consumed directly by UI or graph loaders.
- Frontend consumes data via APIs (no direct graph dependency).

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Retention / pruning policy for `runs/` | TBD | TBD |
| Standard `run_id` format across pipelines | TBD | TBD |
| Standard manifest schema location in `schemas/` | TBD | TBD |

### Future extensions
- Emit a lightweight **run index** compatible with telemetry / dashboards.
- Export selected validation summaries into `data/prov/` for long-term lineage.
- Add automated redaction checks for known sensitive patterns (requires governance review).

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[Text extraction output] --> B[Validation checks]
  B --> C{Pass?}
  C -- Yes --> D[Promote validated output]
  C -- No --> E[Record findings + iterate]
  B --> F[data/work/tmp/text/validation/runs/<run_id>/]
~~~

## 📦 Data & Metadata

### What typically gets stored here
- Machine-readable:
  - `findings.jsonl` (issue-per-line)
  - `metrics.json` (aggregates)
  - `summary.json` (pass/fail + counts + pointers)
- Human-readable:
  - `report.md` (optional QA narrative)
- Operational:
  - `logs/run.log`

### Suggested minimal fields for `manifest.yaml`
~~~yaml
run_id: "20251219T153012Z__text-validate__src-<source_id>__<hash8>"
created_at: "2025-12-19T15:30:12Z"
inputs:
  - path: "data/.../source.ext"
    sha256: "<input-sha256>"
toolchain:
  extractor: "<name+version>"
  validator: "<name+version>"
checks:
  - id: "encoding/utf8"
  - id: "language/detect"
  - id: "structure/required-fields"
outputs:
  findings: "findings.jsonl"
  metrics: "metrics.json"
  summary: "summary.json"
status: "pass|fail"
~~~

## 🌐 STAC, DCAT & PROV Alignment

- This directory is **not** a catalog output location.
- If validation results must be long-lived and traceable:
  - record an activity/run artifact under `data/prov/` (PROV),
  - promote validated derived assets into `data/processed/` (or domain-scoped `data/<domain>/processed/`),
  - generate/refresh STAC/DCAT metadata in their canonical locations.

## 🧱 Architecture

### Naming conventions
- Recommended `run_id` pattern:
  - `YYYYMMDDThhmmssZ__<pipeline-step>__src-<source_id>__<hash8>`
- Run folder should be self-contained and readable without external context (via `manifest.yaml` + `summary.json`).

### Promotion guidance
When a run passes and outputs should persist:
1. Copy/emit validated text outputs to the appropriate **non-temporary** stage directory.
2. Ensure provenance identifiers (activity/run IDs) are captured for lineage.
3. Do not store large raw inputs in `runs/`; prefer references.

## 🧠 Story Node & Focus Mode Integration
Validation runs do not directly feed Story Nodes. Only **promoted** and **cataloged** artifacts should be eligible as evidence inputs for graph ingestion and narrative/story generation.

## 🧪 Validation & CI/CD

- [ ] Run folder contains `manifest.yaml`
- [ ] `summary.json` includes pass/fail and pointers to `findings` and `metrics`
- [ ] No secrets/credentials are written into logs or manifests
- [ ] Potential PII is handled according to governance requirements (redaction/generalization as needed)
- [ ] Markdown files remain protocol-compliant (front matter present, sections structured)

## ⚖ FAIR+CARE & Governance

- Treat extracted text as **potentially sensitive** until reviewed.
- Avoid committing raw, high-risk content into `runs/` (prefer references + hashed IDs).
- If content relates to culturally sensitive materials or restricted locations:
  - use generalization/redaction in reports,
  - route for human review per governance policy.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial README for text validation run artifacts | TBD |

