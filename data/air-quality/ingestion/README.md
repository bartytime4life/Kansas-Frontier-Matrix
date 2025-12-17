---
title: "KFM Air Quality — Ingestion README"
path: "data/air-quality/ingestion/README.md"
version: "v1.0.0"
last_updated: "2025-12-17"
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

doc_uuid: "urn:kfm:doc:data:air-quality:ingestion-readme:v1.0.0"
semantic_document_id: "kfm-data-air-quality-ingestion-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:air-quality:ingestion-readme:v1.0.0"
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

# KFM Air Quality — Ingestion README

## 📘 Overview

### Purpose
- Define how the **Air Quality** domain is ingested into the KFM pipeline, including:
  - what belongs in the domain’s **ingestion documentation area** (`data/air-quality/ingestion/`),
  - where **raw landed artifacts** live (`data/raw/air-quality/`),
  - what minimal **metadata + provenance expectations** apply at ingestion time (before certification).
- Ensure ingestion steps remain aligned to the canonical KFM lifecycle:
  `data/raw → data/work → data/processed → data/stac`.

### Scope
| In Scope | Out of Scope |
|---|---|
| Air-quality ingestion conventions, checklists, and inputs/outputs expectations | Implementation details of ETL jobs (see `src/pipelines/`) |
| Requirements for landing raw data and capturing checksums/provenance pointers | Graph modeling / ontology design (see `docs/graph/`) |
| What must exist before promoting artifacts to `data/processed/air-quality/` | API/UI behavior (see `src/server/`, `web/`) |
| STAC/DCAT/PROV *expectations* for air-quality artifacts | Governance policy authoring (see `docs/governance/`) |

### Audience
- Primary: Data + pipeline contributors responsible for air-quality ingestion and refresh cycles
- Secondary: Governance/security reviewers; historians/editors validating traceability; API/UI consumers of cataloged outputs

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **ingestion**: the controlled acquisition + landing of source materials into `data/raw/air-quality/`
  - **raw**: landed source artifacts (as received, or as close as feasible)
  - **work**: intermediate artifacts produced during cleaning/normalization
  - **processed**: certified artifacts approved for downstream use (catalog + graph ingestion)
  - **catalogs**: STAC/DCAT/PROV outputs used for discovery + lineage

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Canonical pipeline ordering | `docs/MASTER_GUIDE_v12.md` | KFM Maintainers | ETL → catalogs → graph → APIs → UI → story |
| Data directory rules | `data/README.md` | Data/Pipeline Maintainers | Governs raw/work/processed/stac semantics |
| Pipeline implementation | `src/pipelines/` | Engineering | Deterministic ingestion/transforms |
| Domain docs (recommended) | `docs/data/air-quality/` | TBD | Not confirmed in repo; choose a canonical home and link |

### Definition of done (for this document)
- [ ] Front-matter complete + valid (path matches)
- [ ] This sub-area’s file tree documented (no “mystery folders”)
- [ ] Raw landing rules are explicit (where, naming, checksums)
- [ ] Validation steps listed and repeatable (even if commands are placeholders)
- [ ] Provenance expectations stated (inputs, run/activity IDs, output pointers)
- [ ] Sensitivity + governance considerations stated (even if “public by default”)

## 🗂️ Directory Layout

### This document
- `path`: `data/air-quality/ingestion/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Air-quality domain docs/config | `data/air-quality/` | Domain-scoped documentation and small metadata artifacts |
| Ingestion docs (this area) | `data/air-quality/ingestion/` | Ingestion expectations + checklists (not bulk data) |
| Raw landed artifacts | `data/raw/air-quality/` | Source-landed files or tracked pointers (if large) |
| Working artifacts | `data/work/air-quality/` | Intermediates produced by ETL |
| Certified outputs | `data/processed/air-quality/` | Curated artifacts ready for catalog + graph |
| Catalog outputs | `data/stac/` | STAC/DCAT/PROV outputs for all domains |
| Pipeline implementation | `src/pipelines/` | Code that performs ingestion/transforms |
| Schemas/contracts | `schemas/` | Validation rules (if present/defined) |
| Runs/experiments | `mcp/` | Run logs, experiment notes, model cards (not data storage) |

### Expected file tree for this sub-area
~~~text
data/
├── 📁 air-quality/
│   └── 📁 ingestion/
│       └── 📄 README.md
├── 📁 raw/
│   └── 📁 air-quality/
│       └── 📄 <landed source artifacts…>
├── 📁 work/
│   └── 📁 air-quality/
│       └── 📄 <intermediate artifacts…>
├── 📁 processed/
│   └── 📁 air-quality/
│       ├── 📄 README.md
│       └── 📄 <certified artifacts…>
└── 📁 stac/
    └── 📄 <catalog outputs…>
~~~

### Extension points checklist (for future work)
- [ ] Data: domain folder expanded under `data/air-quality/` (additional docs/mappings as needed)
- [ ] STAC: air-quality collection + items validated to profile
- [ ] PROV: activity + agent identifiers recorded for each refresh
- [ ] Graph: labels/relations mapped (if/when graph ingestion is implemented)
- [ ] APIs: contract additions tested (if/when exposed)
- [ ] UI: layer registry entry + access rules (if/when visualized)
- [ ] Focus Mode: provenance references enforced (if used in narrative contexts)
- [ ] Telemetry: ingestion/run signals recorded (if applicable)

## 🧭 Context

### Background
The Air Quality domain is inherently spatiotemporal (measurements observed at places over time). Ingestion must preserve:
- **source traceability** (where data came from and when),
- **deterministic refreshability** (replayable jobs with stable outputs),
- **consistent staging** (`raw → work → processed`) before catalog emission.

### Assumptions
- Air-quality sources are acquired from external providers (TBD per dataset).
- The ingestion mechanism is implemented in `src/pipelines/` (this folder documents expectations, not code).

### Constraints / invariants
- Canonical order is preserved: ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode.
- Bulk data artifacts belong in `data/raw/air-quality/` (or tracked pointers) — **not** in `data/air-quality/ingestion/`.
- Promotion to `data/processed/air-quality/` requires validation + provenance completeness.
- If any sensitivity risk exists (e.g., derived datasets that could reveal sensitive locations), redact/generalize before public outputs.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What are the canonical source systems for air-quality in this repo? | TBD | TBD |
| What is the canonical “refresh cadence” (daily/weekly/monthly) for each source? | TBD | TBD |
| Are large source dumps tracked with DVC in this repository? | TBD | TBD |
| What schema contracts exist (or should exist) for air-quality processed outputs? | TBD | TBD |

## 🗺️ Diagrams

### Air-quality ingestion flow (domain view)
~~~mermaid
flowchart LR
  S["External Sources (TBD)"] --> R["data/raw/air-quality/ (landed)"]
  R --> W["data/work/air-quality/ (normalize/clean)"]
  W --> P["data/processed/air-quality/ (certified)"]
  P --> C["data/stac/ (STAC/DCAT/PROV)"]
  C --> G["Graph (Neo4j)"]
  G --> A["APIs"]
  A --> U["UI Layers / Focus Mode (optional)"]
~~~

## 📦 Data & Metadata

### Inputs (at ingestion time)
| Input | Format | Where from | Minimum validation |
|---|---|---|---|
| Source datasets | mixed (CSV/JSON/GeoJSON/NetCDF/etc.) | External providers (TBD) | Checksums; format sanity; license recorded (if known) |
| Source docs/metadata | text/PDF/web exports | Provider documentation | Capture title, publisher, license/terms, retrieval date |

### Outputs (at ingestion time)
| Output | Format | Path | Notes |
|---|---|---|---|
| Landed raw artifacts | mixed | `data/raw/air-quality/` | Prefer stable naming + checksums |
| Intermediate artifacts | mixed | `data/work/air-quality/` | Pipeline-defined; safe to delete/rebuild |
| Certified artifacts | mixed | `data/processed/air-quality/` | Must include dataset README + schema adherence |
| Catalog metadata | JSON (+ JSON-LD where applicable) | `data/stac/` | STAC/DCAT/PROV aligned + validated |

### Sensitivity & redaction
- Default assumption: air-quality measurements are public/open.
- However, derived products can introduce sensitivity risk depending on joins/enrichment. Before publishing:
  - scan for unintended PII,
  - ensure coordinates/locations do not violate any sovereignty constraints,
  - follow governance requirements for any restricted layers.

### Quality signals (recommended minimum)
- Required fields present (domain-defined)
- Timestamp parseability + time zone convention defined
- Location fields valid (if spatial)
- Deterministic IDs (stable station/feature identifiers, if applicable)
- Provenance completeness (source ID + retrieval date + transform activity ID)

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Processed air-quality artifacts should be represented in STAC as Collections/Items with Assets that point to the certified artifacts (or to external storage locations if used).
- Spatial + temporal extents should reflect the **certified output**, not the raw source dump.
- Extensions should be used only when justified and consistent with the KFM-STAC profile.

### DCAT
- DCAT dataset descriptors should be derivable from the same authoritative metadata used for STAC.
- At minimum: `title`, `description`, `license`, and `keywords` must be present and consistent.

### PROV-O
- Provenance must link:
  - the certified entity (output) back to raw inputs and transform activities,
  - run/activity identifiers to timestamps,
  - agents/tools responsible for the transform (as applicable).
- Granularity rule (recommended): “one ingestion refresh” = one PROV Activity (unless a finer plan is defined).

### Versioning
- New dataset versions must link predecessor/successor (catalog-level), and the graph should mirror that lineage (when graph ingestion exists).
- Avoid overwriting in-place without a lineage trail; prefer “new version + links”.

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Potential outcomes (optional / domain-dependent):
  - a focusable layer representing air-quality measurements over time,
  - evidence panels linking measurements to catalog/provenance references.

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID.

### Optional structured controls
~~~yaml
focus_layers:
  - "air_quality:<TBD-layer-id>"
focus_time: "<TBD-time-window>"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (KFM-MDP)
- [ ] Raw artifact inventory present + checksums recorded (if applicable)
- [ ] Processed outputs schema-validated (if schema exists)
- [ ] STAC/DCAT/PROV outputs validated to profile (KFM-STAC/KFM-DCAT/KFM-PROV)
- [ ] Security + sovereignty checks (as applicable)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands

# 1) Run the air-quality ingestion pipeline
# (see src/pipelines/ for the authoritative implementation)

# 2) Validate generated artifacts (schemas + catalogs)
# (see schemas/ and docs/standards/)

# 3) Run doc lint / markdown checks
# (see docs/standards/ for KFM-MDP tooling)
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| ingestion_run_id | pipeline | `mcp/runs/` |
| source_retrieval_timestamp | ingestion | `mcp/runs/` |
| catalog_validation_result | CI | `mcp/runs/` or CI logs |

## ⚖ FAIR+CARE & Governance

### Review gates
- Data/Pipeline Maintainers: confirm staging + reproducibility
- Governance/Security Review: confirm sensitivity classification + sovereignty compliance (when applicable)

### CARE / sovereignty considerations
- If air-quality data intersects with community-defined sensitive areas or restricted knowledge, apply governance-approved generalization/redaction rules prior to public outputs.

### AI usage constraints
- Ensure this doc’s AI permissions/prohibitions match intended use (see front-matter).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-17 | Initial air-quality ingestion README | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Data Directory Guide: `data/README.md`
