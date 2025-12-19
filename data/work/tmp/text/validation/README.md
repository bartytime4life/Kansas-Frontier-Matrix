---
title: "KFM — data/work/tmp/text/validation README"
path: "data/work/tmp/text/validation/README.md"
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

doc_uuid: "urn:kfm:doc:data:work:tmp:text:validation:readme:v1.0.0"
semantic_document_id: "kfm-data-work-tmp-text-validation-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:work:tmp:text:validation:readme:v1.0.0"
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

# KFM — data/work/tmp/text/validation

## 📘 Overview

### Purpose
This folder is a **work-area for validation artifacts** produced while extracting, cleaning, or normalizing text in the KFM pipeline. It exists to capture *what was checked* and *what failed or passed* before any results are promoted to longer-lived `work/` or `processed/` locations.

### Scope
| In Scope | Out of Scope |
|---|---|
| Validation reports for extracted or transformed text | Canonical, curated datasets intended for downstream use |
| Temporary diagnostics, diffs, samples of failures | Raw source data meant to remain in `data/raw/` |
| Machine-readable checksums/manifests for text validation | Secrets, credentials, tokens, API keys |
| Evidence needed to reproduce “why this text was accepted/rejected” | Personal data or sensitive content not approved for storage |

### Audience
- Primary: ETL/pipeline maintainers working on text extraction + normalization
- Secondary: Curators verifying provenance and quality gates prior to catalog/graph loads

### Definitions
- Glossary link: `docs/glossary.md` (verify exists)
- Terms used here:
  - **Validation artifact**: any report, manifest, or diagnostic output that records quality checks
  - **Promotion**: moving outputs to a longer-lived directory after passing checks
  - **Run ID**: a stable identifier for a pipeline execution (format is implementation-defined)

### Key artifacts
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `data/work/tmp/text/validation/README.md` | DataOps | Folder contract |
| Validation report | (example) `runs/<run_id>/validation_report.json` | ETL | Suggested naming |
| Human-readable summary | (example) `runs/<run_id>/validation_report.md` | ETL | Optional |
| Failure samples | (example) `runs/<run_id>/samples/` | ETL | Keep minimal + redacted |
| Hash/manifest | (example) `runs/<run_id>/hash_manifest.txt` | ETL | Optional |

### Definition of done
- [ ] Front-matter complete and `path` matches this file’s location
- [ ] Folder purpose and non-goals clearly stated
- [ ] Examples are clearly marked as examples and do not imply required filenames
- [ ] Security and sensitivity expectations documented

## 🗂️ Directory Layout

### This document
- `path`: `data/work/tmp/text/validation/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Text work area | `data/work/tmp/text/` | Temporary text artifacts produced during extraction/cleanup |
| Work logs | `data/work/logs/` | Pipeline logs and run diagnostics (verify conventions) |
| Work staging | `data/work/staging/` | Intermediate staged artifacts prior to processing (verify usage) |
| Work processed | `data/work/processed/` | Outputs ready to be promoted to `data/processed/` (verify usage) |
| Curated processed | `data/processed/` | Stable processed outputs used downstream |
| Provenance | `data/prov/` | PROV bundles or provenance exports (if used) |
| Master guide | `docs/MASTER_GUIDE_v12.md` | Canonical pipeline ordering and invariants |

### Expected file tree for this sub-area
This is a suggested organization. The directory may start empty except for this README.

~~~text
📁 data/
└── 📁 work/
    └── 📁 tmp/
        └── 📁 text/
            └── 📁 validation/
                ├── 📄 README.md
                └── 📁 runs/
                    └── 📁 <run_id>/
                        ├── 📄 validation_report.json
                        ├── 📄 validation_report.md
                        ├── 📄 hash_manifest.txt
                        └── 📁 samples/
                            └── 📄 sample_failures.txt
~~~

## 🧭 Context

### Why this folder exists
Text extraction and normalization can introduce silent failures (encoding issues, truncated outputs, malformed delimiters, etc.). This folder provides a dedicated place to store validation evidence so that:
- The ETL stage can be debugged without polluting curated outputs.
- Promotion decisions can be traced to explicit checks and artifacts.
- Downstream steps (catalog/graph/story) only consume vetted outputs.

### How this aligns with the KFM pipeline
This directory supports **ETL and quality gating** prior to any cataloging (STAC/DCAT/PROV) or graph loading. It should not be treated as an API surface or a long-lived “source of truth.”

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A[Text extraction output in data/work/tmp/text] --> B[Validation checks]
  B -->|pass| C[Promote to work processed or curated processed]
  B -->|fail| D[Store reports + samples in data/work/tmp/text/validation]
~~~

## 📦 Data & Metadata

### Inputs
- Temporary text artifacts produced upstream in `data/work/tmp/text/` (exact filenames are pipeline-defined)

### Outputs
- Validation reports and diagnostics that explain:
  - what was checked
  - pass/fail outcomes
  - any remediation hints
  - hashes/manifests when applicable

### Provenance expectations
When possible, validation reports should include:
- `run_id`
- upstream input identifiers or hashes
- tool/version identifiers for validators
- timestamps in ISO 8601 format

## ✅ Validation and QA

### Recommended checks
Pick checks appropriate to the text type being validated.
- Encoding sanity (e.g., UTF-8 decodability)
- Structural sanity (e.g., expected delimiter presence, line count bounds)
- Empty/near-empty output detection
- Truncation detection where feasible
- Hash/manifest generation for reproducibility

### Promotion rules
- Only promote outputs once the relevant checks pass.
- If failures are stored here, ensure samples are minimal and sanitized.

## 🔐 Security, ethics, and sensitivity

- Do not store secrets, credentials, tokens, or private keys.
- If any text content could include sensitive information, store only redacted samples or summary statistics.
- Follow `docs/governance/*` references in the front matter for handling sensitive or culturally restricted material.

## 🧪 Operational notes

- This is a *work/tmp* area. Periodic cleanup may be appropriate depending on repo policy and storage constraints.
- If validation artifacts need to be retained for auditability or release notes, promote them to a long-lived location and record the move in PROV or run logs.

## 🧾 Change log

| Version | Date | Change |
|---|---|---|
| v1.0.0 | 2025-12-19 | Initial README for `data/work/tmp/text/validation/` |
