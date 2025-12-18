---
title: "README — data/raw/<source_id> (Raw Source Landing Zone)"
path: "data/raw/<source_id>/README.md"
version: "v0.1.0"
last_updated: "2025-12-18"
status: "draft"
doc_kind: "Data Source README"
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

doc_uuid: "urn:kfm:doc:data:raw:<source_id>:readme:v0.1.0"
semantic_document_id: "kfm-data-raw-<source_id>-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data:raw:<source_id>:readme:v0.1.0"
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

# README — `data/raw/<source_id>/`

> Replace `<source_id>` everywhere in this file with the canonical source ID used by your `data/sources/` manifest (if applicable).

## 📘 Overview

### Purpose
- Document what this raw source folder contains, how it was acquired, and how it should be used by the KFM pipeline.
- Provide a stable “source of truth” for file layout, integrity expectations, and licensing/sensitivity notes for this specific source.

### Scope
| In Scope | Out of Scope |
|---|---|
| Source-faithful raw artifacts (downloads, scans, exports) | Cleaning/normalization (belongs in `data/work/`) |
| Acquisition notes, checksums, file inventory | Derived datasets and transforms |
| License + attribution references | Graph modeling + API/UI configuration |
| Provenance anchors (what upstream evidence exists) | Focus Mode narrative writing |

### Audience
- Primary: Data contributors and maintainers adding/updating this source.
- Secondary: Pipeline maintainers validating reproducibility and provenance.

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **source_id**: Canonical identifier for this upstream source.
  - **acquisition**: A concrete retrieval event (date-stamped) that produced raw artifacts.
  - **raw artifact**: The original, source-faithful file as acquired.
  - **sidecar**: A companion file (checksum, notes) stored next to an artifact.
  - **manifest**: A machine-readable source descriptor (typically under `data/sources/`).

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `data/raw/<source_id>/README.md` | Data maintainers | Fill in placeholders |
| Raw artifacts | `data/raw/<source_id>/<YYYY-MM-DD>/...` | Data maintainers | One folder per acquisition |
| Source manifest | `data/sources/<source_id>.*` | Data maintainers | **not confirmed in repo** (exact extension/schema) |
| Work staging | `data/work/<source_id>/...` | Pipelines | Transform + QA area |
| Processed outputs | `data/processed/<domain>/...` | Pipelines | Canonical validated outputs |
| STAC/DCAT/PROV | `data/stac/...` | Pipelines | Catalog entries for processed assets |
| Run logs | `mcp/runs/...` or `mcp/experiments/...` | Pipelines | **not confirmed in repo** (exact location) |

### Definition of done (for this document)
- [ ] Front-matter complete + valid (`path` matches)
- [ ] Source metadata filled (provider, license, acquisition method, expected formats)
- [ ] Directory tree reflects actual on-disk contents
- [ ] Integrity approach defined (checksums and/or large-file tracking)
- [ ] Sensitivity + sovereignty considerations stated (even if “none known”)
- [ ] Reproduction notes point to the source manifest / pipeline entry point (**not confirmed in repo** if unknown)

## 🗂️ Directory Layout

### This document
- `path`: `data/raw/<source_id>/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Raw landing zone | `data/raw/` | Raw downloads grouped by source |
| Source manifests | `data/sources/` | Fetch + metadata descriptors (**not confirmed in repo**) |
| Staging workspace | `data/work/` | Transform + QA workspace |
| Canonical outputs | `data/processed/` | Validated outputs |
| Asset catalogs | `data/stac/` | STAC/DCAT/PROV catalogs |
| Pipelines | `src/pipelines/` | ETL + transforms (**not confirmed in repo**) |
| Schemas | `schemas/` | Validation schemas (**not confirmed in repo**) |
| Documentation | `docs/` | Governed docs + standards |
| MCP | `mcp/` | Runs/experiments/model cards (**not confirmed in repo**) |

### Expected file tree for this source
~~~text
📁 data/
└─📁 raw/
  └─📁 <source_id>/
    ├─📄 README.md
    ├─📄 _SOURCE.md                     # optional: human notes, attribution, pointers (NO PII)
    ├─📄 _LICENSE.md                    # optional: license summary/terms (no new policy text)
    ├─📁 <YYYY-MM-DD>/                  # acquisition date (recommended)
    │  ├─📄 <original_filename>.<ext>   # raw artifact (source-faithful)
    │  ├─📄 <original_filename>.<ext>.sha256  # optional checksum sidecar
    │  ├─📄 _ACQUISITION_NOTES.md       # optional: what/where/how acquired
    │  └─📁 attachments/                # optional: ancillary files from provider bundle
    └─📁 _inventory/                    # optional: file lists, manifests, counts
       └─📄 inventory_<YYYY-MM-DD>.csv  # optional: name/size/hash table
~~~

## 🧭 Context

### Background
- **Source name:** `<human-readable name>`
- **Provider / publisher:** `<organization>`
- **Provider reference:** `<URL or citation string>` (avoid secrets/tokens)
- **Why this source exists in KFM:** `<1–3 sentences: what question it helps answer>`

### Assumptions
- Raw artifacts are **not** edited in place; any edits produce new artifacts in a new acquisition folder (or are performed in `data/work/`).
- This folder may contain large binaries; use the repo’s large-file mechanism if required (**not confirmed in repo** which mechanism is standard).

### Constraints / invariants
- Preserve canonical ordering: ETL → catalogs → graph → APIs → UI → Story Nodes → Focus Mode.
- Frontend must consume data through APIs (no direct graph access).
- No secrets, credentials, or sensitive personal info in raw notes or filenames.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What is the canonical `data/sources/<source_id>` manifest filename + schema? | TBD | TBD |
| Are checksums required as `.sha256` sidecars, or handled by a tooling layer? | TBD | TBD |
| Does this source have sensitivity constraints (restricted sites, culturally sensitive info)? | TBD | TBD |

### Future extensions
- Add a standardized acquisition metadata sidecar (JSON/YAML) under `schemas/` (**not confirmed in repo**).
- Add automated integrity verification for this source to CI (hash + file count + schema checks).

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A["Upstream provider<br/>System of record"] --> B["data/raw/<source_id><br/>Raw artifacts"]
  B --> C["data/work/<source_id><br/>Staging + QA"]
  C --> D["data/processed/<domain><br/>Validated outputs"]
  D --> E["data/stac<br/>Catalogs: STAC · DCAT · PROV"]
  E --> F["Neo4j graph"]
  F --> G["APIs"]
  G --> H["UI"]
  H --> I["Story Nodes"]
  I --> J["Focus Mode"]
~~~

### Optional: sequence diagram (acquisition event)
~~~mermaid
sequenceDiagram
  participant Maintainer
  participant Manifest as data/sources
  participant Raw as data/raw/<source_id>
  participant Work as data/work/<source_id>
  Maintainer->>Manifest: Add or update manifest entry (source + license + fetch)
  Maintainer->>Raw: Store acquisition bundle (date-stamped)
  Maintainer->>Raw: Record checksums / inventory (optional)
  Maintainer->>Work: Trigger transform + QA (pipeline step)
~~~

## 📦 Data & Metadata

### Source metadata (fill these in)
| Field | Value |
|---|---|
| source_id | `<source_id>` |
| Source name | `<human-readable name>` |
| Provider | `<organization>` |
| Provider URL / reference | `<link or citation string>` |
| License | `<license name + reference>` |
| Acquisition method | `<API / bulk download / scan / export / manual>` |
| Acquisition cadence | `<one-time / monthly / annual / irregular>` |
| Spatial coverage | `<statewide / county / bounding area>` |
| Temporal coverage | `<start–end>` |
| Notes | `<known quirks, encoding, CRS, etc.>` |

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Raw artifact bundle | `<ext list>` | `<provider>` | File integrity (hash/size), bundle completeness |

### Outputs (within this folder)
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Raw artifacts | various | `data/raw/<source_id>/<YYYY-MM-DD>/...` | Source-faithful (no transforms) |
| Checksums (optional) | `.sha256` | alongside artifact | SHA256 (recommended) |
| Inventory (optional) | CSV | `data/raw/<source_id>/_inventory/...` | Columns: filename,size,sha256 (suggested) |

### Sensitivity & redaction
- Sensitivity classification for this source: `<public / restricted / sensitive>` (update front-matter accordingly).
- If sensitive locations exist:
  - Do **not** store precise coordinates in human notes.
  - Ensure downstream processing applies generalization/redaction rules before publication.

### Quality signals
- Integrity: hashes match the acquisition record.
- Completeness: expected file count and expected naming patterns are satisfied.
- Reproducibility: a manifest or citation exists so the acquisition can be explained/repeated.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Expected STAC collection ID (processed): `<collection_id>` (**not confirmed in repo**)
- Expected STAC item IDs (examples): `<item_id_1>`, `<item_id_2>` (**not confirmed in repo**)
- Extensions (if any): `<stac extensions>` (**not confirmed in repo**)

### DCAT
- Dataset identifier: should align with `<source_id>`
- License mapping: ensure STAC/DCAT catalog reflects the upstream license terms.

### PROV-O
- `prov:wasDerivedFrom`: processed entities should reference raw artifacts (or stable identifiers/hashes).
- `prov:wasGeneratedBy`: transformations should be recorded as Activities, with Agents (pipeline version + operator role).

### Versioning
- Raw versions should be partitioned by acquisition date (`<YYYY-MM-DD>`).
- If the provider publishes explicit versions/releases, record them in `_ACQUISITION_NOTES.md` and propagate to processed + catalog layers.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| Upstream provider | Publishes source data | URL/API/archive reference |
| Source manifest | Describes fetch + metadata | `data/sources/<source_id>.*` (**not confirmed in repo**) |
| Raw store | Holds source-faithful artifacts | `data/raw/<source_id>/...` |
| Work store | Transform + QA staging | `data/work/<source_id>/...` |
| Processed store | Canonical outputs | `data/processed/<domain>/...` |
| Catalog builder | STAC/DCAT/PROV generation | `data/stac/...` |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Manifest schema | `schemas/` | Semver + changelog (**not confirmed in repo**) |
| Processed output schema | `schemas/` | Semver + validation |
| Catalog schema | STAC/DCAT/PROV | Validator-pinned |

### Extension points checklist (for future work)
- [ ] Data: new/updated manifest for `<source_id>`
- [ ] Raw: acquisition folder added with notes + integrity signals
- [ ] Work: transform + QA documented/reproducible
- [ ] Processed: canonical outputs regenerated deterministically
- [ ] Catalog: STAC/DCAT/PROV refreshed and validated
- [ ] Graph: lineage links updated (predecessor/successor if versioned)
- [ ] Focus Mode: evidence surfaced with provenance

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Focusable entities enabled by this source: `<places / events / parcels / boundaries / imagery layers / etc.>`
- Evidence expected to be visible: `<processed layer IDs + citations/provenance refs>`

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID (typically STAC + graph entity IDs), not directly to raw filenames alone.

### Optional structured controls
~~~yaml
focus_layers:
  - "<layer_id_or_collection_id>"
focus_time: "<YYYY or range>"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] Manifest validation (schema + required fields) (**not confirmed in repo**)
- [ ] Raw integrity checks (hashes/file counts) (if required for this source)
- [ ] Processed schema validation (geospatial validity, required fields)
- [ ] STAC/DCAT/PROV validation (validator pinned)
- [ ] Security + sovereignty checks (as applicable)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) validate manifest schema
# 2) fetch or verify raw acquisition (if automated)
# 3) run pipeline for <source_id>
# 4) validate processed outputs and catalogs
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| acquisition_date | maintainer/pipeline | `mcp/runs/` (**not confirmed in repo**) |
| sha256 | checksum sidecar/tooling | alongside artifacts or inventory |
| processed_build_id | pipeline run | `mcp/runs/` (**not confirmed in repo**) |

## ⚖ FAIR+CARE & Governance

### Review gates
- Who approves additions/updates to this source? `<TBD>`
- What requires council/board sign-off? `<TBD>`

### CARE / sovereignty considerations
- Communities impacted: `<TBD>`
- Protection rules: `<TBD>`
- If any culturally sensitive information exists, ensure appropriate generalization before publication.

### AI usage constraints
- Ensure this doc’s AI permissions/prohibitions match intended use (front-matter).
- Do not use AI to infer sensitive locations from this source.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v0.1.0 | 2025-12-18 | Initial per-source raw README template for `<source_id>` | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

