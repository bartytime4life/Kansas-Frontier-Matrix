---
title: "KFM — data/work/staging/ README"
path: "data/work/staging/README.md"
version: "v1.0.0"
last_updated: "2025-12-19"
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

doc_uuid: "urn:kfm:doc:data:work:staging:readme:v1.0.0"
semantic_document_id: "kfm-data-work-staging-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:work:staging:readme:v1.0.0"
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

# KFM — `data/work/staging/`

## 📘 Overview

### Purpose
This directory is the **ephemeral staging area** for ETL runs. It holds **intermediate artifacts** produced during ingestion/extraction/normalization *before* anything is considered stable enough to move into `data/processed/` and cataloged into `data/stac/` (and related DCAT/PROV outputs).

### Scope

| In Scope | Out of Scope |
|---|---|
| Temporary downloads, unpacked archives, extracted text, OCR outputs, parse intermediates, transient geometry conversions, pre-validation outputs | Canonical “published” datasets, curated/approved tables, final geospatial layers, STAC/DCAT/PROV catalogs, anything served to users |

### Audience
- Primary: ETL authors/maintainers; data curators
- Secondary: reviewers performing reproducibility + provenance audits

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc: staging, ETL run, promotion, provenance, STAC/DCAT/PROV

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Data lifecycle ordering | `docs/MASTER_GUIDE_v12.md` | Maintainers | Canonical pipeline + lifecycle |
| Work area | `data/work/` | Maintainers | Non-canonical, reproducible intermediates |
| Processed outputs | `data/processed/` | Maintainers | Candidate canonical datasets (pre-catalog) |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Maintainers | Machine-validated catalogs + lineage |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Directory purpose and “what belongs / what does not” are explicit
- [ ] Promotion rules to `data/processed/` (and then catalogs) are documented
- [ ] Sensitivity / redaction guidance is explicit and consistent with governance refs

## 🗂️ Directory Layout

### This document
- `path`: `data/work/staging/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Work (ephemeral) | `data/work/` | Intermediate run outputs; not stable |
| Tables (work) | `data/work/tables/` | Structured/intermediate tabular outputs |
| Raw | `data/raw/` | Original source drops (immutable by convention) |
| Processed | `data/processed/` | Promoted, reviewable datasets |
| STAC catalogs | `data/stac/` | STAC items/collections for assets |
| DCAT catalogs | `data/catalog/dcat/` | Dataset-level catalog views |
| PROV lineage | `data/prov/` | Lineage bundles for transformations |

### Expected file tree for this sub-area
> **Note:** This is a *recommended* organization. Adjust to match actual pipeline layout once ETL configs are implemented.

~~~text
📁 data/
└── 📁 work/
    └── 📁 staging/
        ├── 📄 README.md
        ├── 📁 <run_id_or_run_date>/
        │   ├── 📁 <source_slug>/
        │   │   ├── 📄 manifest.json
        │   │   ├── 📁 downloads/
        │   │   ├── 📁 extracted/
        │   │   ├── 📁 ocr/
        │   │   └── 📁 logs/
        │   └── 📄 run_summary.md
        └── 📁 _scratch/
            └── (optional local-only scratchpad; avoid committing large or sensitive content)
~~~

## 🧭 Context

### Background
KFM’s pipeline stages require deterministic, auditable transformations. `data/work/staging/` exists to keep *unstable* artifacts separate from the versioned “published” outputs while still enabling reproducibility and troubleshooting.

### Assumptions
- ETL runs produce **run IDs** and keep enough metadata to reconstruct lineage.
- Staging outputs may be large and/or noisy; only a subset gets promoted.

### Constraints / invariants
- Canonical pipeline ordering is preserved: ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode.
- The frontend/UI must never depend directly on `data/work/*`.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What is the canonical run ID format (date-based, hash-based, or both)? | TBD | TBD |
| Do we commit staging outputs to git, or keep most via ignored artifacts with manifests only? | TBD | TBD |

### Future extensions
- Add run manifests that map directly into PROV activities.
- Add automated validation reports alongside staged artifacts.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[data/raw] --> B[data/work/staging]
  B --> C[data/work/tables]
  C --> D[data/processed]
  D --> E[data/stac + data/catalog/dcat + data/prov]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Source drops | PDF/CSV/XLSX/GeoJSON/GeoTIFF/etc. | `data/raw/` or controlled download | Hashes recorded; basic type validation |
| Extraction configs | YAML/JSON | `src/pipelines/` (expected) | Lint + schema checks (as applicable) |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Staged artifacts | mixed | `data/work/staging/<run>/...` | Manifest required (recommended) |
| Parse logs | text/json | `.../logs/` | Must not include secrets/PII |
| Run summary | Markdown | `.../run_summary.md` | Human-readable run notes |

### Sensitivity & redaction
- **Do not** place secrets, credentials, tokens, or private keys in staging.
- If staged content may contain sensitive locations or restricted cultural data, store only the **minimum** needed for processing and ensure redaction/generalization steps are applied before promotion.

### Quality signals
Recommended checks (apply as relevant to the artifact type):
- Checksums for downloads and extracted payloads
- File type/encoding validation for extracted text
- Geometry validity checks for vector data (if produced)
- Row/column sanity checks for extracted tables (if produced)

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Staging outputs are **not** STAC items.
- Only promote stable assets to `data/processed/` and then catalog into `data/stac/`.

### DCAT
- DCAT dataset records are created for promoted datasets, not staging intermediates.

### PROV-O
- Staging should retain enough run metadata to produce:
  - `prov:wasDerivedFrom` source IDs
  - `prov:wasGeneratedBy` pipeline activity/run ID

### Versioning
- Treat staging as **non-versioned** (or at most run-scoped).
- Versioning occurs when data is promoted into processed + catalogs.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| ETL | Extract/normalize into staged artifacts | Run configs + run logs |
| Catalogs | Create machine-validated metadata | STAC/DCAT/PROV schemas |
| Graph | Build semantic graph from cataloged artifacts | API boundary (no direct UI) |
| APIs | Serve contracted access | REST/GraphQL |
| UI | Render maps + narratives | API calls only |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| ETL run manifests (recommended) | `data/work/staging/.../manifest.json` | Semver once formalized |
| Promotion checklists | `docs/` (future) | Governed doc updates |

### Extension points checklist (for future work)
- [ ] Add a `manifest.json` schema under `schemas/`
- [ ] Record ETL activities into `data/prov/`
- [ ] Promote validated outputs to `data/processed/`
- [ ] Generate STAC/DCAT entries for published assets

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
It should **not** surface directly. Focus Mode must be powered by provenance-linked, cataloged outputs (processed + STAC/DCAT/PROV + graph).

### Provenance-linked narrative rule
No narrative content should reference staging artifacts directly as evidence; evidence must be a cataloged asset ID.

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Ensure staging does not contain secrets or restricted material
- [ ] Verify manifests exist for staged runs (recommended)
- [ ] Promote only after validation into `data/processed/`
- [ ] Run schema validation when generating STAC/DCAT/PROV

### Reproduction
~~~bash
# Placeholder — replace with repo-specific commands once ETL tooling exists
# 1) run ETL to staging
# 2) validate staged artifacts
# 3) promote to processed
# 4) build catalogs (STAC/DCAT/PROV)
~~~

## ⚖ FAIR+CARE & Governance

### Review gates
- Staging organization changes: maintainer review
- Any change impacting redaction/sensitivity: governance review (as applicable)

### CARE / sovereignty considerations
- If data includes culturally sensitive sites or restricted knowledge, apply sovereignty rules before promotion.

### AI usage constraints
- No “speculative additions” or inferring sensitive locations from partial signals.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial `data/work/staging/` README | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`