---
title: "README — data/raw (Raw Data Landing Zone)"
path: "data/raw/README.md"
version: "v0.1.0"
last_updated: "2025-12-17"
status: "active"
doc_kind: "Data Directory README"
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
doc_uuid: "urn:kfm:doc:data:raw:readme:c95554d4-6e9b-546f-bf91-9f4ca09ccc61"
semantic_document_id: "kfm-data-raw-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data:raw:readme:v0.1.0"
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

# README — `data/raw/` (Raw Data Landing Zone)

> This document follows KFM Markdown Protocol and is governed by `docs/MASTER_GUIDE_v12.md`.

## 📘 Overview

### Purpose
- Define what belongs in `data/raw/`, how it relates to the KFM pipeline, and the expected contributor workflow for introducing new **raw** inputs.
- Clarify “raw vs. work vs. processed” responsibilities so downstream catalogs (STAC/DCAT/PROV), graph builds, and UI layers remain reproducible.

### Scope
| In Scope | Out of Scope |
|---|---|
| Raw data “landing zone” expectations | Data cleaning/normalization details (belongs in `data/work/`) |
| How raw inputs are represented/tracked | Neo4j graph modeling details |
| Links to manifests and governance references | UI layer configuration details |

### Audience
- Primary: Contributors adding new datasets, maintainers reviewing data additions.
- Secondary: Pipeline developers and Story Node authors who need to trace provenance back to source evidence.

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc (minimum):
  - **Raw**: Original, source-faithful artifacts as obtained from upstream providers (API/download/manual digitization).
  - **Work**: Intermediate staging outputs produced by transforms, QA, and validation.
  - **Processed**: Canonical, validated outputs suitable for cataloging + graph/UI consumption.
  - **Manifest**: A machine-readable source descriptor (typically in `data/sources/`) that the pipeline can fetch + reproduce.

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Raw landing zone | `data/raw/` | Data maintainers | This directory |
| Source manifests | `data/sources/` | Data maintainers | “Catalog of inputs” / fetch configuration |
| Staging workspace | `data/work/` | Pipelines | Transform + QA workspace |
| Canonical outputs | `data/processed/` | Pipelines | Validated outputs |
| Asset catalogs | `data/stac/` | Pipelines | STAC items/collections for processed assets |
| Governance | `docs/governance/*` | Project governance | Sensitivity, ethics, sovereignty |

### Definition of done (for this document)
- [ ] Front-matter complete + valid (path matches, versions set)
- [ ] Directory intent is clear: raw vs work vs processed
- [ ] File tree is present and consistent with how the repo is intended to be used
- [ ] Governance + CARE/sovereignty considerations explicitly stated
- [ ] Validation guidance is repeatable (even if commands are marked “not confirmed in repo”)

## 🗂 Directory Layout

### This document
- `path`: `data/raw/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed/stac outputs |
| Documentation | `docs/` | Canonical governed docs |
| Pipelines | `src/pipelines/` | ETL + catalogs + transforms |
| Schemas | `schemas/` | JSON schemas + telemetry schemas (if present) |
| Frontend | `web/` | React + map clients (if present) |
| MCP | `mcp/` | Experiments, model cards, SOPs |

### Expected file tree for this sub-area
~~~text
📁 data/
├─📁 raw/
│  ├─📄 README.md
│  ├─📁 <source_id>/                       # recommended: one folder per source manifest
│  │  ├─📁 <YYYY-MM-DD>/                   # recommended: acquisition date (or release date)
│  │  │  ├─📄 <original_filename>.<ext>    # raw artifact as acquired
│  │  │  ├─📄 <original_filename>.<ext>.sha256  # optional: checksum sidecar
│  │  │  └─📄 <notes>.md                   # optional: acquisition notes (NO sensitive content)
│  │  └─📄 _SOURCE.md                      # optional: human notes / license reminders
│  └─📄 .gitkeep                           # optional: keep empty directory in git
~~~

Notes:
- The exact per-source folder naming convention is **not confirmed in repo**. If a convention exists, document it here and keep it stable (so the pipeline can be deterministic).

## 🧭 Context

### Background
- KFM uses a staged data lifecycle so raw inputs can be fetched/re-fetched, transforms can be repeated, and outputs can be validated before publication.

### Assumptions
- Raw artifacts may be large (rasters, scans, imagery) and may not be stored directly in Git.
- Source identity is tracked via a manifest (typically `data/sources/*.json`) rather than ad hoc manual downloads.

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode is preserved.
- Frontend consumes contracts via APIs (no direct graph dependency).
- **Raw should remain source-faithful**; transformations belong in `data/work/` and above.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Is DVC used in this repo for raw artifacts? If so, what are the required commands + remote? | TBD | TBD |
| Is there a required folder naming convention under `data/raw/<source_id>/...`? | TBD | TBD |
| Do we require checksum sidecars for raw assets (or does DVC cover this)? | TBD | TBD |

### Future extensions
- Add a schema for raw acquisition metadata sidecars (if needed) under `schemas/`.
- Add automated integrity checks (hash verification, file count assertions) to CI.

## 🗺 Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
    A[data/raw\nRaw downloads] --> B[data/work\nStaging + transforms]
    B --> C[data/processed\nValidated outputs]
    C --> D[data/stac\nCatalogs (STAC/DCAT/PROV)]
    D --> E[Neo4j Graph]
    E --> F[APIs]
    F --> G[React/Map UI]
    G --> H[Story Nodes]
    H --> I[Focus Mode]
~~~

### Optional: sequence diagram (raw acquisition)
~~~mermaid
sequenceDiagram
participant Maintainer
participant Pipeline
participant RawStore as data/raw
participant WorkStore as data/work
Maintainer->>Pipeline: Register/Update source manifest (data/sources/*.json)
Pipeline->>RawStore: Fetch raw artifacts (download/API)
Pipeline->>WorkStore: Transform + QA + validation
Pipeline-->>Maintainer: Run logs + integrity summary
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Scanned maps / rasters | TIFF/GeoTIFF/JPEG/PNG | Upstream archive/API/manual download | Checksum/integrity; geospatial validation occurs in `data/work/` |
| Vector datasets | SHP/GeoJSON/GeoPackage/CSV | Open data portals / archives | Schema + basic sanity; geometry validation occurs in `data/work/` |
| Text documents | TXT/PDF | Digitized archives | File integrity; OCR/NLP occurs in `data/work/` |
| Images | JPG/PNG/TIFF | Archives / scans | File integrity |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Raw artifacts | various | `data/raw/<source_id>/...` | Source-faithful (no transformation contract here) |
| Optional checksum sidecars | `.sha256` | alongside raw artifact | TBD (consider standardizing) |
| Optional acquisition notes | `.md` | alongside raw artifact | Must comply with governance (no sensitive/PII) |

### Sensitivity & redaction
- **Do not** place secrets, credentials, or sensitive personal information in `data/raw/`.
- If a dataset is restricted/sensitive, do not store it in Git-tracked locations; follow governance refs in front matter.
- If public publishing requires generalization/redaction, that must happen downstream (typically `data/work/` → `data/processed/`), with provenance preserved.

### Quality signals
- Integrity: checksum or DVC hash matches acquisition record.
- Reproducibility: raw artifacts are fetchable via manifest (URL/API reference) or documented archival reference.
- Completeness: acquisition date + expected file counts are documented (at minimum in manifest; optionally in `_SOURCE.md`).

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections involved: typically created from **processed** outputs, not raw.
- Items involved: raw artifacts may become STAC Assets later, but STAC Items should point to validated/usable assets.

### DCAT
- Dataset identifiers: should align with `data/sources` manifests (source IDs).
- License mapping: capture source license at manifest-level and propagate to catalogs.

### PROV-O
- `prov:wasDerivedFrom`: processed assets should reference raw artifacts or their stable identifiers/hashes.
- `prov:wasGeneratedBy`: transformations in `data/work/` should be modeled as Activities with Agents (pipeline version, contributor, container digest if available).

### Versioning
- Prefer stable source identifiers and acquisition-date partitioning; do not silently overwrite raw artifacts without recording version changes.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| Source manifests | Describe fetch + metadata | `data/sources/*.json` |
| Raw store | Source-faithful artifacts | `data/raw/` (+ DVC pointers if used) |
| Work store | Transform + QA staging | `data/work/` |
| Processed store | Canonical validated outputs | `data/processed/` |
| Catalog builder | STAC/DCAT/PROV generation | `data/stac/` (+ validators) |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Source manifest schema | `schemas/` (if present) | Semver + changelog |
| Raw artifact tracking | DVC or equivalent | Dataset version linked to commit/run |
| Catalog schemas | `schemas/` + `data/stac/` | Contract tests required |

### Extension points checklist (for future work)
- [ ] Data: new source manifest added under `data/sources/`
- [ ] Raw: acquisition documented (date + integrity signal)
- [ ] Work: transform + QA steps are reproducible
- [ ] PROV: activity + agent identifiers recorded
- [ ] Catalog: STAC/DCAT/PROV updated from processed outputs
- [ ] UI: layer registry entry added (location TBD)
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump (if telemetry exists)

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Raw artifacts do **not** surface directly in Focus Mode.
- Focus Mode should surface **processed** layers + graph entities, with provenance links that allow a user to trace back to raw evidence.

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID (typically in processed/STAC + provenance).

### Optional structured controls
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Ensure `data/sources/*.json` entries are valid and include license/source reference fields (exact schema **not confirmed in repo**).
- [ ] Verify that raw artifacts are either:
  - fetchable/reproducible from manifests, or
  - tracked via a large-file mechanism (e.g., DVC) without bloating Git.
- [ ] Confirm no sensitive/restricted content is committed to Git-tracked locations.

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands (not confirmed in repo)
# 1) validate source manifests (JSON schema)
# 2) fetch raw data for one source
# 3) run pipeline through work → processed → stac for that source
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| Raw fetch timestamp | pipeline run | `mcp/runs/` or `mcp/experiments/` |
| Checksum/hash | DVC or sidecar | alongside artifacts or run logs |

## ⚖ FAIR+CARE & Governance

### Review gates
- Who approves changes? (TBD — follow governance docs)
- What requires council/board sign-off? (TBD — follow governance docs)

### CARE / sovereignty considerations
- Identify communities impacted by the dataset and any special handling rules.
- Do not publish precise locations for culturally sensitive sites; follow sovereignty policy in front matter.

### AI usage constraints
- Ensure this doc’s AI permissions/prohibitions match intended use (front matter).
- Avoid AI-driven inference that could expose sensitive locations or identities.

## 🕰 Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v0.1.0 | 2025-12-17 | Initial `data/raw/README.md` | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
