---
title: "KFM Data Work Tmp Text — README"
path: "data/work/tmp/text/README.md"
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

doc_uuid: "urn:kfm:doc:data:work:tmp:text:readme:v1.0.0"
semantic_document_id: "kfm-data-work-tmp-text-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:work:tmp:text:readme:v1.0.0"
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

# KFM Data Work Tmp Text — README

## 📘 Overview

### Purpose
This folder holds **temporary, intermediate text artifacts** created during ETL extraction and normalization (e.g., extracted PDF text, OCR text output, or “pre-clean” text used before structured parsing). It is part of the `data/work/` staging area and should not be treated as canonical outputs.

This directory supports the canonical pipeline ordering documented in `docs/MASTER_GUIDE_v12.md` (ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode).

### Scope
| In Scope | Out of Scope |
|---|---|
| Intermediate extracted text (`.txt`, `.md`, `.json` sidecars) used to support parsing, QA, and downstream transforms | Canonical published text outputs (promote those to `data/processed/` and/or `data/stac/` as appropriate) |
| Short-lived artifacts created per run / per source | Story nodes, narrative documents, or UI-facing text |
| Debuggable/traceable “workbench” outputs | Long-term archival storage |

### Audience
- Primary: ETL / pipeline maintainers
- Secondary: data QA reviewers

### Definitions (link to glossary)
- Link: `docs/glossary.md` (not confirmed in repo)
- Terms used in this doc: ETL, extraction, normalization, provenance, run ID, sidecar metadata

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| ETL run outputs (temporary) | `data/work/tmp/text/…` | ETL | Intermediate only; may be cleared between runs |
| Work logs | `data/work/logs/…` | ETL | Expected to link run IDs to artifacts |
| Work metadata sidecars | `data/work/metadata/…` | ETL | Used to capture extraction warnings + inputs |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Folder purpose and “what belongs here” is explicit
- [ ] Promoting artifacts to `data/processed/` / `data/stac/` is described
- [ ] Sensitivity and redaction expectations stated (no leakage via temp artifacts)

## 🗂️ Directory Layout

### This document
- `path`: `data/work/tmp/text/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Raw inputs | `data/raw/` | Source files (PDF/CSV/images/etc.) |
| Work staging | `data/work/` | Intermediate outputs and run-local artifacts |
| Processed outputs | `data/processed/` | Stable, versioned derived datasets |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Published catalogs and lineage bundles |

### Expected file tree for this sub-area
~~~text
📁 data/work/tmp/text/
├── 📄 README.md
├── 📁 <run_id>/
│   ├── 📄 <source_id>__<asset_id>.txt
│   ├── 📄 <source_id>__<asset_id>.json
│   └── 📄 <source_id>__<asset_id>.warnings.json
└── 📁 <scratch>/
    └── 📄 <any-temporary-text-artifacts>
~~~

> Naming conventions above are **recommended**, not confirmed in repo. Prefer stable IDs already used by the ETL/config system.

## 🧭 Context

### Background
Text extraction is often required as an intermediate step before:
- NLP/entity extraction,
- structured parsing,
- QA (spot-checking OCR),
- or generating provenance-aware downstream products.

Keeping these artifacts organized makes ETL runs easier to debug and reproduce.

### Assumptions
- Temporary artifacts may be **cleared** between runs or excluded from long-term retention.
- Any “publishable” text artifact should be promoted and versioned in `data/processed/` and linked via STAC/DCAT/PROV.

### Constraints / invariants
- Preserve the canonical pipeline ordering: ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode.
- Frontend/UI should never depend on this temp directory directly (UI reads via APIs).

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Should `data/work/tmp/` be gitignored by default (and to what extent)? | TBD | TBD |
| What is the canonical `<run_id>` format (timestamp, hash, UUID)? | TBD | TBD |

### Future extensions
- Add a small sidecar schema in `schemas/` for extraction warning outputs (if not already present).
- Add a deterministic “promotion” step that moves selected artifacts from `data/work/tmp/text/` → `data/processed/`.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[data/raw sources] --> B[ETL extraction]
  B --> C[data/work/tmp/text]
  C --> D[Normalization/Parsing]
  D --> E[data/processed]
  E --> F[STAC/DCAT/PROV]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Source documents | PDF/TXT/HTML/images | `data/raw/` or source fetch | hash recorded + parse warnings captured |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Extracted text | `.txt` / `.md` | `data/work/tmp/text/...` | not confirmed in repo |
| Extraction sidecar metadata | `.json` | `data/work/tmp/text/...` | not confirmed in repo |

### Sensitivity & redaction
- Extracted text may contain sensitive content (including PII) depending on source material.
- Do not treat raw extracted text as automatically safe for publication. Promote to `data/processed/` only after appropriate review/redaction consistent with governance references.

### Quality signals
- Extraction warnings captured (missing pages, encoding issues, OCR confidence if available).
- Deterministic reruns produce identical text outputs for identical inputs/configs (where feasible).

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- This temp directory is **not** a STAC source of truth.
- If extracted text becomes a durable artifact, promote it and attach it as a STAC asset under `data/stac/…` (collection/item) with appropriate links.

### DCAT
- DCAT mappings should reference stable, published datasets (not temporary ETL artifacts).

### PROV-O
- When promoting artifacts, ensure `prov:wasDerivedFrom` points to raw inputs and `prov:wasGeneratedBy` points to the ETL activity/run ID (recorded elsewhere).

### Versioning
- Temporary artifacts may be overwritten; published artifacts must use explicit versioning and predecessor/successor links where applicable.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| ETL | extraction + normalization | configs + run logs |
| Work staging | intermediate artifacts | filesystem paths under `data/work/` |
| Catalogs | publishable metadata | STAC/DCAT/PROV outputs |
| APIs/UI | consume published contracts | never read `data/work/tmp/` directly |

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Confirm temp artifacts are not referenced by STAC/DCAT outputs
- [ ] Confirm sensitive text isn’t accidentally promoted or exposed
- [ ] Confirm run logs/metadata exist for traceability (location may vary)

### Reproduction
~~~bash
# Placeholder (repo-specific commands not confirmed in repo)
# 1) run ETL extraction for a source bundle
# 2) confirm extracted text appears under data/work/tmp/text/<run_id>/
# 3) validate promotion step outputs under data/processed/ (if implemented)
~~~

## ⚖ FAIR+CARE & Governance

### Review gates
- If extracted text contains sensitive or culturally restricted content: requires human review before promotion/public exposure.

### CARE / sovereignty considerations
- Do not infer or expose sensitive locations or protected knowledge from extracted text artifacts.

### AI usage constraints
- Follow `ai_transform_prohibited` list for any automated transforms over this directory.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial README for `data/work/tmp/text/` | TBD |

---
Footer refs:
- Master guide: `docs/MASTER_GUIDE_v12.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
