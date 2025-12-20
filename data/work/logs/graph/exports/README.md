---
title: "KFM — Graph Export Logs (Exports Directory README)"
path: "data/work/logs/graph/exports/README.md"
version: "v1.0.0"
last_updated: "2025-12-20"
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

doc_uuid: "urn:kfm:doc:data:work:logs:graph:exports:readme:v1.0.0"
semantic_document_id: "kfm-data-work-logs-graph-exports-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:work:logs:graph:exports:readme:v1.0.0"
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

# KFM — Graph Export Logs

## 📘 Overview

### Purpose
This directory holds **graph export artifacts** produced during the **Graph** stage (Neo4j build / validation / export workflows). These exports are intended for:
- debugging and regression checks
- provenance/audit support (when paired with PROV run metadata)
- interchange with downstream tooling via the API layer (never direct UI consumption)

This folder is within `data/work/`, meaning it is **work-stage material** and not automatically considered a published dataset.

### Scope

| In Scope | Out of Scope |
|---|---|
| Export outputs from Graph-stage tooling (e.g., node/edge extracts, subgraph bundles) | Authoritative “released” datasets (those belong under `data/processed/` and/or catalog outputs under `data/stac/` / `data/catalog/dcat/`) |
| Export manifests, checksums, and export logs | Secrets, credentials, tokens, or private keys |
| CI-generated “golden” comparison exports (if used) | Public-facing content that is not provenance-linked or not approved for release |
| Redacted/generalized exports (when required) | Any workflow implying the UI reads Neo4j directly |

### Audience
- Primary: Graph maintainers, DataOps, CI maintainers
- Secondary: API maintainers, auditors/reviewers

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc: *export*, *run_id*, *manifest*, *checksum*, *redaction/generalization*, *provenance*

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `data/work/logs/graph/exports/README.md` | Graph/DataOps | Directory purpose + conventions |
| Export run directory | `data/work/logs/graph/exports/<run_id>/` | Graph/DataOps | One folder per export run |
| Export manifest | `data/work/logs/graph/exports/<run_id>/manifest.json` | Graph/DataOps | Recommended: list files + schema + provenance refs |
| Checksums | `data/work/logs/graph/exports/<run_id>/checksums.sha256` | Graph/DataOps | Recommended for integrity validation |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Directory purpose + boundaries clearly stated
- [ ] Example tree included and consistent with `data/work/` intent
- [ ] Validation steps listed (repeatable)
- [ ] Governance + CARE/sovereignty considerations stated for exports

## 🗂️ Directory Layout

### This document
- `path`: `data/work/logs/graph/exports/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Work-stage data | `data/work/` | Intermediate and non-authoritative build artifacts |
| Graph logs | `data/work/logs/graph/` | Graph-stage logs, checks, and operational outputs |
| Graph exports (this dir) | `data/work/logs/graph/exports/` | Export bundles per run |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Published catalogs + provenance bundles |
| Graph code | `src/graph/` | Graph build + ontology bindings + migrations |
| API layer | `src/server/` | Contracted access (UI never reads Neo4j directly) |

### Expected file tree for this sub-area
~~~text
📁 data/
└── 📁 work/
    └── 📁 logs/
        └── 📁 graph/
            └── 📁 exports/
                ├── 📄 README.md
                ├── 📁 <run_id>/
                │   ├── 📄 manifest.json
                │   ├── 📄 checksums.sha256
                │   ├── 📄 export.log
                │   ├── 📄 nodes.<ext>
                │   ├── 📄 relationships.<ext>
                │   └── 📄 warnings.json
                └── 📁 <run_id>/
                    └── …
~~~

> Notes:
> - `<run_id>` should be stable and unique per export run (e.g., pipeline run ID, CI run ID, or deterministic hash-based ID).
> - `<ext>` is workflow-dependent (CSV/JSON/GraphML/etc.) and should be documented in `manifest.json`.

## 🧭 Context

### Background
Graph exports are often needed to:
- validate graph integrity (e.g., counts, constraints, relationship completeness)
- provide reproducible “snapshots” for debugging or cross-team review
- support API contract tests by offering known-good fixtures

### Assumptions
- Export bundles are generated by deterministic pipeline tooling (or CI jobs that are tied to a deterministic run configuration).
- Exports may require redaction/generalization if they include sensitive locations or personal data.
- This directory may be treated as ephemeral work output depending on repo policy (not confirmed here).

### Constraints / invariants
- Canonical pipeline ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- Frontend must not read Neo4j directly; any consumption of graph-derived exports is mediated by the API layer.
- `data/work/` is not the canonical home for released datasets or catalogs.
- No secrets/credentials are ever stored in exports or logs.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Should export runs be committed to git or stored only as CI artifacts? | TBD | TBD |
| What is the retention policy for export runs? | TBD | TBD |
| Do we need a schema for `manifest.json` under `schemas/`? | TBD | TBD |

### Future extensions
- Add a governed JSON schema for `manifest.json` (including provenance pointers to PROV activity/run IDs).
- Add an automated integrity check that verifies:
  - checksums exist and match
  - required files are present for the export type
  - manifest references resolve (where applicable)

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[Neo4j Graph Build] --> B[Export Job]
  B --> C[data/work/logs/graph/exports/<run_id>/]
  C --> D[CI Checks / Regression]
  C --> E[API-layer fixtures / audit review]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Graph database state | Neo4j | Graph stage output | Graph integrity checks |
| Export config | YAML/JSON (TBD) | Pipeline/CI | Config lint (TBD) |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Export bundle | CSV/JSON/etc. | `data/work/logs/graph/exports/<run_id>/...` | Documented in manifest (recommended) |
| Manifest | JSON | `.../<run_id>/manifest.json` | Schema (TBD) |
| Checksums | sha256 list | `.../<run_id>/checksums.sha256` | Format check (TBD) |
| Export log | text/json | `.../<run_id>/export.log` | N/A |

### Sensitivity & redaction
If exports contain sensitive locations, culturally sensitive sites, or personal data:
- prefer a **redacted/generalized** export variant for work sharing
- keep any restricted exports access-controlled per governance docs (paths referenced in front matter)

### Quality signals
- Completeness: expected file set exists for the export type
- Integrity: checksums validate
- Traceability: manifest includes provenance pointers (PROV activity/run IDs) when applicable

## 🌐 STAC, DCAT & PROV Alignment

### STAC
Graph exports in this directory are not STAC Items by default. If an export is promoted to a reusable artifact, it should be re-homed and cataloged appropriately.

### DCAT
Graph exports here are not DCAT datasets by default. Promotion requires DCAT mapping under `data/catalog/dcat/`.

### PROV-O
Where feasible, export runs should link to PROV activities:
- `prov:wasGeneratedBy`: export activity/run ID
- `prov:wasDerivedFrom`: graph build run ID and relevant source IDs

### Versioning
If export bundles are used as fixtures, record:
- a stable run identifier
- the upstream graph build identifier
- any schema/version pins in `manifest.json`

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| Graph stage | Build Neo4j graph | Pipeline outputs + constraints |
| Export job | Extract graph slices/bundles | Config + run ID + logs |
| CI checks | Validate expected invariants | Reads export bundle + manifest |
| API layer | Contracted access | REST/GraphQL (no direct UI graph reads) |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Export manifest schema (if added) | `schemas/graph/exports/manifest.schema.json` (TBD) | Semver + changelog |
| Export file formats | `manifest.json` per run | Declare schema/version per run |

### Extension points checklist (for future work)
- [ ] Add schema for manifest
- [ ] Add CI check for checksum validation
- [ ] Add PROV linkage recording for export runs
- [ ] Add redaction/generalization rules where needed

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
This directory does not directly feed Focus Mode. Any narrative or UI usage must flow through:
- Graph → API → UI → Story Nodes → Focus Mode

### Provenance-linked narrative rule
If any export-derived data influences Story Nodes, the Story Node must cite the underlying dataset/document IDs and/or PROV activity IDs.

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Confirm no secrets/credentials present in export artifacts
- [ ] Confirm manifest exists (if used) and lists expected files
- [ ] Confirm checksums validate (if present)
- [ ] Confirm exports respect redaction/generalization requirements (if applicable)

### Reproduction
~~~bash
# Placeholder — replace with repo-specific commands
# 1) run graph export job
# 2) validate manifest + checksums
# 3) run CI integrity checks
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| Export duration | Export job | `data/work/logs/graph/exports/<run_id>/export.log` |
| File counts/sizes | Export job | `.../<run_id>/manifest.json` |

## ⚖ FAIR+CARE & Governance

### Review gates
- Exports that may contain sensitive locations or person-linked records: **requires human review**
- Any promotion of exports to published artifacts: align with STAC/DCAT/PROV requirements

### CARE / sovereignty considerations
- Do not infer or reconstruct sensitive locations from partial data.
- Apply redaction/generalization rules where required (see governance references in front matter).

### AI usage constraints
- This doc permits summarization/structure extraction, but prohibits policy generation and sensitive-location inference.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-20 | Initial README for graph export logs directory | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

