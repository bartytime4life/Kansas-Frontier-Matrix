---
title: "KFM — data/work README"
path: "data/work/README.md"
version: "v1.0.0"
last_updated: "2025-12-26"
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

doc_uuid: "urn:kfm:doc:data:work:readme:v1.0.0"
semantic_document_id: "kfm-data-work-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:work:readme:v1.0.0"

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

# data/work — Intermediate Artifacts

> **Purpose (required):** Define what belongs in `data/work/`, how intermediate artifacts must be produced (deterministic + reproducible), and how they are promoted to `data/processed/` for cataloging (STAC/DCAT/PROV), graph ingestion, APIs, and downstream UI/Story/Focus experiences.

## 📘 Overview

### Purpose

- Establish the **placement contract** for intermediate, regenerable artifacts produced by ETL/normalization.
- Prevent “work outputs” from becoming accidental sources of truth by defining **promotion rules** to `data/processed/`.
- Provide minimum expectations for **reproducibility, naming, and governance hygiene** in the intermediate stage.

### Scope

| In Scope | Out of Scope |
|---|---|
| Intermediate artifacts produced during transforms, joins, normalization, QA, and staging | Immutable raw snapshots (belongs in `data/raw/`) |
| Per-domain organization under `data/work/<domain>/` | Canonical “certified” outputs (belongs in `data/processed/`) |
| Guidance for run-scoped output folders and manifests | STAC/DCAT/PROV authoring (belongs in `data/stac/`, `data/catalog/dcat/`, `data/prov/`) |
| Promotion checklist from work → processed | Writing governance policy (belongs in `docs/governance/`) |

### Audience

- **Primary:** Data/pipeline contributors implementing or running deterministic ETL and normalization.
- **Secondary:** Maintainers and governance reviewers auditing lineage and publication readiness.

### Definitions

- Link: `docs/glossary.md`
- Terms used in this doc include: **raw**, **work**, **processed**, **determinism**, **idempotence**, **run_id**, **promotion**, **manifest**, **redaction**, **provenance**.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline ordering + invariants | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical lifecycle + “do not break” rules |
| Universal governed doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | KFM Core | Front-matter + required sections |
| ETL / transforms | `src/pipelines/` | Data Eng | Deterministic, idempotent runs |
| Schemas (STAC/DCAT/PROV and other contracts) | `schemas/` | Data/Platform | Schema lint + validation gates |
| Canonical processed outputs | `data/processed/` | Data Eng | Only certified artifacts should be depended on downstream |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Catalog Build | Machine-validated catalogs + lineage bundles |
| Run manifests / run logs | `mcp/runs/` | Maintainers | Should point to outputs + provenance references (avoid duplication) |
| Domain governance hubs | `data/<domain>/governance/README.md` | Domain owners | Sensitivity/classification and review triggers |

### Definition of done

- [ ] Front-matter complete + valid (`path` matches file location).
- [ ] Work-stage placement rules are explicit and actionable.
- [ ] “Promotion to processed” checklist exists and is repeatable.
- [ ] Validation steps are listed and clearly marked if “not confirmed in repo”.
- [ ] Governance + CARE/sovereignty considerations are explicitly stated.
- [ ] Footer refs present.

## 🗂️ Directory Layout

### This document

- `path`: `data/work/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Raw staging | `data/raw/` | Immutable source snapshots (append-only; never edited in place) |
| Work staging | `data/work/` | Intermediate artifacts (reproducible; safe to delete/rebuild) |
| Processed staging | `data/processed/` | Canonical outputs for catalogs + graph ingest (schema-validated; versioned) |
| STAC | `data/stac/` | STAC Collections + Items |
| DCAT | `data/catalog/dcat/` | DCAT dataset records (JSON-LD / TTL as adopted) |
| PROV | `data/prov/` | PROV lineage bundles (per run / per dataset) |
| Domain governance | `data/<domain>/governance/` | Domain-specific governance docs and decisions |
| Pipelines | `src/pipelines/` | ETL + catalog builders + transforms |
| Graph | `src/graph/` (+ `data/graph/` if present) | Ontology bindings, graph build, import fixtures |
| API boundary | `src/server/` (or legacy `src/api/` — not confirmed in repo) | Contracts, redaction rules, query services |
| UI | `web/` | React/map UI (must not read Neo4j directly) |

### Expected file tree for this sub-area

> This is the **recommended** structure. Some directories may not exist yet (**not confirmed in repo**).

~~~text
📁 data/
├── 📁 raw/
│   └── 📁 <domain>/                         # immutable source snapshots (append-only)
├── 📁 work/
│   ├── 📄 README.md                         # you are here
│   └── 📁 <domain>/                         # intermediate artifacts (reproducible; safe to delete/rebuild)
│       ├── 📁 <run_id>/                     # run-scoped output folder (recommended)
│       │   ├── 📄 manifest.json             # inputs/params/outputs pointers (recommended)
│       │   ├── 📄 manifest.sha256           # output checksums (recommended)
│       │   └── 📁 artifacts/                # pipeline-defined intermediate outputs
│       └── 📁 _notes/                       # human notes (optional; keep lightweight)
├── 📁 processed/
│   └── 📁 <domain>/                         # canonical processed outputs (schema-validated; versioned)
├── 📁 stac/
│   └── 📁 <domain>/                         # STAC Collections/Items for the domain (layout domain-defined)
├── 📁 catalog/
│   └── 📁 dcat/                             # DCAT dataset records
├── 📁 prov/                                 # PROV bundles (per run / per dataset)
└── 📁 reports/
    └── 📁 <domain>/                         # optional analysis outputs (domain-defined)
~~~

## 🧭 Context

### Background

KFM uses a staged lifecycle for traceability and reproducibility:

- `data/raw/` → `data/work/` → `data/processed/` → `data/stac/` (and optional `data/reports/` outputs)

The `data/work/` stage exists to support **deterministic, idempotent transformations** while keeping `data/raw/` immutable and `data/processed/` trustworthy and diffable.

### Pipeline placement

`data/work/` is an ETL/normalization staging area. Downstream systems should rely on **processed + cataloged + provenance-linked** artifacts, not work outputs.

### Work-stage invariants

- **Regenerable:** Work outputs must be reproducible from `data/raw/` + pipeline configuration and parameters.
- **Non-canonical:** Work outputs are not the “published truth” and should not be treated as stable interfaces.
- **Safe to delete/rebuild:** If you can’t regenerate it deterministically, it likely belongs in `data/processed/` (or needs better pipeline logging).
- **No secrets:** Never place tokens/keys/credentials here (or anywhere in-repo).

### Promotion to processed

Promote an artifact to `data/processed/<domain>/` when it is:

- schema-aligned (where schemas exist),
- QA’d for obvious validity issues,
- labeled with stable IDs,
- and ready to be referenced by STAC/DCAT/PROV, graph ingest, APIs, and UI/Focus contexts.

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  RAW["data/raw/<domain>/"] --> WORK["data/work/<domain>/"]
  WORK --> PROC["data/processed/<domain>/"]
  PROC --> STAC["data/stac/ + data/catalog/dcat/ + data/prov/"]
  STAC --> GRAPH["Neo4j Graph"]
  GRAPH --> API["API Layer"]
  API --> UI["UI — React/MapLibre"]
  UI --> STORY["Story Nodes"]
  STORY --> FOCUS["Focus Mode"]
~~~

## 🧠 Story Node & Focus Mode Integration

- Story Nodes and Focus Mode must be **provenance-linked**.
- **Do not cite `data/work/**` artifacts** as evidence in narratives. Instead, promote to `data/processed/`, emit STAC/DCAT/PROV, and reference the catalog/provenance identifiers.

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Work artifacts are reproducible from raw inputs (idempotent pipeline re-run yields equivalent outputs).
- [ ] A run folder includes a minimal manifest (inputs + parameters + outputs pointers).
- [ ] Checksums exist for any artifact intended to be compared or promoted.
- [ ] No secrets/credentials present.
- [ ] If promoting: processed outputs validated; STAC/DCAT/PROV outputs validated to project profiles.

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) Run a pipeline step that produces work artifacts
# python -m src.pipelines.<domain>.ingest --run-id <run_id>

# 2) Produce or update a hash manifest (recommended)
# python tools/hash_manifest.py data/work/<domain>/<run_id>/artifacts > data/work/<domain>/<run_id>/manifest.sha256

# 3) Promote to processed only after validation
# python -m src.pipelines.<domain>.promote_to_processed --run-id <run_id>
~~~

### Telemetry signals

> Recommended only; schema/location not confirmed in repo.

| Signal | Source | Where recorded |
|---|---|---|
| `work_artifact_emitted` | ETL | `mcp/runs/<run_id>/` (pointer-based) |
| `promotion_to_processed` | ETL | `mcp/runs/<run_id>/` + PROV activity |
| `promotion_blocked` | validation/gov scan | `mcp/runs/<run_id>/` |

## 📦 Data & Metadata

### What belongs in `data/work/`

Typical (pipeline-defined) intermediate artifacts:

- parsed/normalized tables (CSV/Parquet/JSON) prior to certification,
- cleaned or reprojected spatial layers (GeoJSON/GeoPackage, raster subsets),
- intermediate joins/enrichment outputs,
- deduplicated entity tables before ID stabilization,
- QA reports that support promotion decisions (keep lightweight).

### What must not live in `data/work/`

- Immutable raw snapshots (use `data/raw/`).
- “Certified” or published datasets that downstream systems depend on (use `data/processed/`).
- Catalog outputs (use `data/stac/`, `data/catalog/dcat/`, `data/prov/`).
- Large, non-reproducible “one-off” results without manifests (use `data/reports/` or an approved external store — not confirmed in repo).

### Minimum metadata recommended per run folder

Recommended `manifest.json` fields (names are suggestions; exact schema not confirmed in repo):

- `run_id` and timestamp
- input inventory (paths + hashes) from `data/raw/<domain>/`
- pipeline version / commit reference
- parameters (including fixed random seeds if used)
- output inventory (paths + hashes) under `data/work/<domain>/<run_id>/`

## 🌐 STAC, DCAT & PROV Alignment

- Work artifacts are upstream of cataloging.
- Any dataset that becomes user-facing or API-facing must be represented through:
  - **STAC Collection + Item(s)**
  - **DCAT mapping** (minimum title/description/license/keywords)
  - **PROV activity/bundle** linking outputs back to raw inputs and transforms

## 🧱 Architecture

### Subsystem contracts

| Subsystem | Contract artifacts | Do not break |
|---|---|---|
| ETL | configs + run logs + validation | deterministic, replayable |
| Catalogs | STAC/DCAT/PROV schemas + validators | machine-validated |
| Graph | ontology + migrations + constraints | stable labels/edges |
| APIs | OpenAPI/GraphQL schema + tests | backward compat or version bump |
| UI | layer registry + a11y + audit affordances | no hidden data leakage |
| Focus Mode | provenance-linked context bundle | no hallucinated sources |

## ⚖ FAIR+CARE & Governance

### Sensitivity and redaction

- Treat intermediate join/enrichment artifacts conservatively: derived products can introduce sensitivity risk even when source data is open.
- Before promoting or publishing:
  - scan for unintended PII,
  - ensure locations/coordinates do not violate sovereignty constraints,
  - ensure access/redaction rules are applied at the API boundary if needed.

### Review triggers

Governance review is required when:

- introducing a new dataset source,
- changing classification/sensitivity labels,
- publishing any dataset derived from sensitive/restricted inputs,
- adding a UI layer that could reveal sensitive locations by interaction/zoom.

### AI usage constraints

This README’s AI permissions/prohibitions are in front-matter. AI may assist with summarization and structure extraction, but must not be used to generate policy or infer sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---:|---|---|
| v1.0.0 | 2025-12-26 | Initial `data/work/` README defining intermediate-artifact rules and promotion guidance | TBD |

---

## Footer refs

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`
---

