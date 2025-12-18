---
title: "KFM Data Architecture (data/ directory)"
path: "data/ARCHITECTURE.md"
version: "v1.0.0"
last_updated: "2025-12-18"
status: "draft"
doc_kind: "Architecture"
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

doc_uuid: "urn:kfm:doc:data:architecture:v1.0.0"
semantic_document_id: "kfm-data-architecture-v1.0.0"
event_source_id: "ledger:kfm:doc:data:architecture:v1.0.0"
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

# KFM Data Architecture (data/ directory)

## 📘 Overview

### Purpose
- Define the **canonical repository layout** for KFM datasets and metadata under `data/`.
- Clarify **what belongs where** across `data/sources/`, `data/raw/`, `data/work/`, `data/processed/`, and `data/stac/`.
- Establish **governed invariants** that keep the end-to-end pipeline reproducible and auditable.

### Scope
| In Scope | Out of Scope |
|---|---|
| Directory structure + responsibilities for `data/` | Implementation details of ETL jobs (see pipeline docs/code) |
| Data lifecycle: ingest → stage → publish | UI rendering details (see `web/`) |
| STAC/DCAT/PROV expectations for published data | Full ontology specification (see `src/graph/` + `docs/graph/`) |
| Versioning expectations for large artifacts (e.g., DVC) | Secrets/credential management (see `SECURITY.md`) |

### Audience
- Primary: ETL/pipeline maintainers, data engineers, reviewers.
- Secondary: Researchers and contributors adding new datasets; story/node authors who need stable dataset references.

### Definitions (link to glossary)
- Link: `docs/glossary.md` (not confirmed in repo)
- Terms used in this doc:
  - **Source manifest**: A machine-readable description of an input dataset (typically in `data/sources/`).
  - **Raw**: As-downloaded inputs (no semantic changes).
  - **Work**: Intermediate/staging outputs (may be transient).
  - **Processed**: Reusable, publication-ready artifacts that downstream systems depend on.
  - **Catalogs**: STAC/DCAT/PROV metadata that describes and links datasets + lineage.

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide (canonical pipeline + invariants) | `docs/MASTER_GUIDE_v12.md` | Maintainers | Source of truth for pipeline ordering |
| Source manifests | `data/sources/` | Data maintainers | Catalog of inputs (URLs, license, coverage, etc.) |
| Raw inputs | `data/raw/` | Data maintainers | As-downloaded; often DVC-tracked for large files |
| Work staging | `data/work/` | Pipeline maintainers | Intermediate artifacts; replayable runs should be deterministic |
| Processed outputs | `data/processed/` | Pipeline maintainers | Downstream-facing artifacts (GeoTIFF/GeoJSON/CSV/etc.) |
| STAC catalogs | `data/stac/` | Pipeline maintainers | Static STAC JSON indexes for processed assets |
| Schemas | `schemas/` | Maintainers | JSON schemas / validation rules (where applicable) |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Directory responsibilities are explicit and non-overlapping
- [ ] “What goes where” examples exist for each major subfolder
- [ ] Validation steps are listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂 Directory Layout

### This document
- `path`: `data/ARCHITECTURE.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed/stac organization |
| Documentation | `docs/` | Canonical governed docs and standards |
| Pipelines | `src/pipelines/` (and/or `scripts/`) | ETL + transforms + catalog builders |
| Schemas | `schemas/` | JSON schemas, metadata contracts, telemetry schemas |
| Graph | `src/graph/` | Graph build + ontology bindings |
| Frontend | `web/` | React + map clients (consumes data via APIs/contracts) |
| MCP runs/experiments | `mcp/` | Experiments, run logs, model cards, SOPs |

### Expected file tree for this sub-area
~~~text
📁 data/
├── 📄 ARCHITECTURE.md
├── 📁 sources/
│   ├── 📄 <source_id>.json                 # input manifests (catalog of sources)
│   └── 📄 README.md                        # optional: human notes for source manifests
├── 📁 raw/
│   └── 📁 <source_id>/                     # as-downloaded inputs (often DVC pointers for large files)
├── 📁 work/
│   └── 📁 <run_id>/                        # staging outputs for a specific replayable pipeline run
├── 📁 processed/
│   └── 📁 <dataset_id>/                    # publication-ready artifacts used by downstream stages
└── 📁 stac/
    ├── 📄 catalog.json                     # optional: STAC root catalog (static; structure may vary)
    ├── 📁 collections/                     # STAC Collections (structure may vary)
    └── 📁 items/                           # STAC Items (structure may vary)
~~~

Notes:
- The **exact naming** of `<source_id>`, `<run_id>`, and `<dataset_id>` is a governed convention. Where not explicitly defined elsewhere, treat the patterns above as **recommended** (not confirmed in repo) and align with the nearest existing convention before introducing a new one.
- Some earlier materials may refer to `data/interim/`. In v12 documentation, **`data/work/` is the canonical staging location** for intermediate artifacts.

## 🧭 Context

### Background
KFM is an end-to-end pipeline that transforms heterogeneous historical sources into standardized datasets, catalogs, a knowledge graph, and finally narrative/UI experiences. The `data/` directory is the **contract boundary** between ingestion, cataloging, and downstream consumption.

### Assumptions
- Contributors add datasets by:
  1) defining/adding a source manifest in `data/sources/`, then
  2) ingesting into `data/raw/`, staging in `data/work/`, and publishing to `data/processed/`, then
  3) updating catalogs in `data/stac/`.
- Large binaries may be tracked with a data versioning tool (e.g., DVC) rather than stored directly in Git.

### Constraints / invariants
- The canonical pipeline order is preserved: **ETL → STAC/DCAT/PROV catalogs → Graph → APIs → UI → Story Nodes → Focus Mode**.
- Data must move through required folders: `data/raw/ → data/work/ → data/processed/` before publication.
- Frontend consumers must not directly depend on the graph store. Contracts are accessed through APIs and/or published catalogs.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What is the canonical ID format for `<run_id>` and `<dataset_id>`? | TBD | TBD |
| Do we enforce a single “per-domain” subfolder convention under `data/processed/`? | TBD | TBD |

### Future extensions
- Optional STAC API deployment (dynamic search) in addition to static `data/stac/` JSON publication.
- Per-domain dataset partitions (e.g., `data/processed/geology/…`, `data/processed/demography/…`) if/when governance approves.

## 🗺 Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[data/sources<br/>source manifests] --> B[data/raw<br/>downloads]
  B --> C[data/work<br/>staging]
  C --> D[data/processed<br/>published artifacts]
  D --> E[data/stac<br/>STAC + DCAT + PROV metadata]
  E --> F[Graph build<br/>(Neo4j)]
  F --> G[APIs]
  G --> H[Web UI]
  H --> I[Story Nodes]
  I --> J[Focus Mode]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant Contributor
  participant Pipeline as ETL Pipeline
  participant FS as data/
  participant Catalog as data/stac/
  Contributor->>FS: Add/Update data/sources/<source_id>.json
  Contributor->>Pipeline: Run ingest + transforms
  Pipeline->>FS: Write downloads to data/raw/<source_id>/
  Pipeline->>FS: Write intermediates to data/work/<run_id>/
  Pipeline->>FS: Write outputs to data/processed/<dataset_id>/
  Pipeline->>Catalog: Generate/Update STAC Items/Collections (+ DCAT + PROV links)
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Source manifests | JSON | `data/sources/*.json` | Link + license fields present; schema checks (where available) |
| Raw downloads | Mixed (TIFF, PDF, CSV, SHP, etc.) | External sources referenced in manifests | Checksums (recommended); file type sanity |
| Human notes (optional) | Markdown | `data/sources/README.md` | Lint + link check |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Staging/intermediate artifacts | Mixed | `data/work/<run_id>/…` | Best-effort; must be reproducible |
| Published datasets | GeoTIFF/COG, GeoJSON, CSV/Parquet, etc. | `data/processed/<dataset_id>/…` | Valid geometry/projection; expected column schema (where defined) |
| Static catalogs | STAC JSON (+ DCAT/PROV-aligned metadata) | `data/stac/…` | KFM-STAC/KFM-DCAT/KFM-PROV profiles (where enforced) |

### Sensitivity & redaction
- If a dataset or derived artifact contains sensitive locations, culturally sensitive context, or restricted material:
  - follow `docs/governance/SOVEREIGNTY.md` and `docs/governance/ETHICS.md`
  - prefer generalization/redaction in public outputs
  - ensure metadata does not disclose prohibited details (including indirectly)

### Quality signals
Recommended checks (adapt to each dataset type):
- **Source manifest QA**: URL reachable; license present; citation/attribution fields present where required.
- **Geospatial QA**: projection present + correct; geometry validity; bounding boxes/extents reasonable.
- **Determinism**: same inputs produce byte-identical or functionally identical outputs (as defined per dataset).
- **Catalog QA**: STAC validation; required fields; consistent IDs and links to derived assets.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Each **published dataset** should have:
  - a **STAC Collection** (dataset-level metadata)
  - one or more **STAC Items** (asset-level metadata)
- Catalog files are stored under `data/stac/` (static JSON publication) unless/ until a STAC API is deployed.

### DCAT
- Each dataset should map to a DCAT description that includes:
  - title, description, license, keywords
  - distribution(s) / access method(s) for artifacts
- Mapping is intended to improve interoperability with external catalog ecosystems.

### PROV-O
- Each derived artifact should be traceable with provenance relationships, including:
  - what source inputs were **used**
  - what process/tool **generated** the output
  - when it was generated
- Where supported, align with a `kfm:lineage` block in metadata.

### Versioning
- Code and data should be version-synchronized:
  - tag releases in Git
  - track large binary versions via a content-addressable mechanism (e.g., DVC) when applicable
- For catalogs, prefer explicit version notes and stable identifiers that allow downstream systems to resolve “previous” vs “current” representations.

## 🧱 Architecture

### Design principles
- **Reproducibility first**: a clean clone + documented commands can recreate `data/processed/` and `data/stac/`.
- **Metadata as a contract**: manifests and catalogs are treated as first-class governed artifacts.
- **Separation of concerns**:
  - `data/sources/` declares intent and provenance of inputs
  - `data/raw/` holds unmodified evidence
  - `data/work/` holds intermediate computations
  - `data/processed/` holds stable outputs
  - `data/stac/` exposes discovery + provenance metadata for downstream stages

### Folder responsibilities (normative)
| Folder | Role | Allowed contents | Not allowed |
|---|---|---|---|
| `data/sources/` | Input catalog | Source manifests + optional human notes | Raw binaries |
| `data/raw/` | Evidence store | As-downloaded inputs | Manually edited “fixed” files without provenance |
| `data/work/` | Staging | Intermediate outputs; logs (if co-located) | Long-lived public assets relied on by UI/graph |
| `data/processed/` | Published artifacts | Reusable, validated outputs | Untracked one-off experiments |
| `data/stac/` | Discovery + lineage | STAC JSON (+ DCAT/PROV-aligned content) | Data binaries (store binaries in processed) |

### Naming conventions (recommended; not confirmed in repo)
- `<source_id>`: short, lowercase, underscores; stable across time (e.g., `usgs_historic_topo`)
- `<run_id>`: timestamped run identity (e.g., `run_2025-12-18_001`) or CI run identity
- `<dataset_id>`: stable “product” identifier (e.g., `railroads_1870`) separated from version details

If repository governance defines a different convention, **use that convention** and update this document.

### Promotion workflow (raw → work → processed → stac)
1. Add/update manifest in `data/sources/`.
2. Ingest/download into `data/raw/` (record checksums + source refs where possible).
3. Transform and stage in `data/work/` (record run parameters + tool versions).
4. Publish validated outputs into `data/processed/`.
5. Generate/update `data/stac/` entries referencing the processed artifacts and their provenance.

## 🧠 Story Node & Focus Mode Integration

- `data/processed/` + `data/stac/` are the **evidence backbone** that supports narrative features:
  - story nodes can cite dataset identifiers and STAC items as the provenance anchor for map layers
  - Focus Mode should rely on provenance-linked assets (no “orphan” narratives)
- When writing narratives, prefer referencing stable dataset IDs and catalog entries rather than ad-hoc file paths.

## 🧪 Validation & CI/CD

### Minimum validation set (expected)
- Source manifest checks:
  - required fields present (including license)
  - referenced URLs are reachable (where feasible)
- Data integrity checks (dataset-specific):
  - geospatial metadata validation for raster/vector outputs (projection, bounds)
  - schema/column checks for tabular outputs
- Catalog checks:
  - STAC JSON validates against the KFM-STAC profile (where enforced)
  - IDs/links resolve to the intended processed assets

### CI/CD integration (recommended)
- Treat data and metadata as “code”:
  - run validation on pull requests that touch `data/sources/`, `data/processed/`, or `data/stac/`
  - fail fast on broken links, missing licenses, invalid STAC, or invalid geometry

## ⚖ FAIR+CARE & Governance

### FAIR+CARE alignment
- **Findable**: datasets are indexed via `data/stac/` and referenced by stable IDs.
- **Accessible**: access methods are described in metadata; restricted data is handled per governance.
- **Interoperable**: metadata aligns to STAC/DCAT/PROV; data uses standard geospatial/tabular formats.
- **Reusable**: licenses and provenance are explicit; transformations are reproducible.

### Governance requirements
- Follow:
  - `docs/governance/ROOT_GOVERNANCE.md`
  - `docs/governance/ETHICS.md`
  - `docs/governance/SOVEREIGNTY.md`
  - `SECURITY.md`
- Never add sensitive location inference to metadata. If unsure, escalate for governance review.

## 🕰 Version History
| Version | Date | Change | Author | Commit |
|---|---|---|---|---|
| v1.0.0 | 2025-12-18 | Initial `data/` architecture doc (draft) | TBD | `<latest-commit-hash>` |