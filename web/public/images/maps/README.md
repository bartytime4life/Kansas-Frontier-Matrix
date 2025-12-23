---
title: "KFM Web UI — Map Image Assets (web/public/images/maps)"
path: "web/public/images/maps/README.md"
version: "v1.0.0"
last_updated: "2025-12-23"
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

doc_uuid: "urn:kfm:doc:web:public:images:maps:readme:v1.0.0"
semantic_document_id: "kfm-web-public-images-maps-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:public:images:maps:readme:v1.0.0"
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

# KFM Web UI — Map Image Assets

## 📘 Overview

### Purpose
- Provide a single, documented home for **static, public map image assets** used by the KFM web UI.
- Clarify what belongs here vs. what belongs in the governed data pipeline (ETL → catalogs → graph → APIs → UI → Story Nodes → Focus Mode).
- Establish lightweight conventions for filenames, licensing/attribution, and quality expectations.

### Scope
| In scope | Out of scope |
|---|---|
| Static map images used for UI-only presentation (e.g., landing-page hero maps, legend thumbnails, example map previews). | Canonical geospatial datasets (rasters/vectors), tilesets/COGs, or evidence artifacts that should be governed via STAC/DCAT/PROV. |
| Generic, reusable assets (not story-specific). | Story-specific images/figures (prefer story-node asset folders) unless explicitly promoted for re-use. |
| Images safe to ship in a public build. | Anything containing restricted/sensitive locations or content requiring redaction. |

### Audience
- UI developers working under `web/`.
- Story authors/designers who need reusable map imagery for UI elements (not as evidence).
- Maintainers reviewing licensing, governance, and performance impacts.

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc: map image asset, thumbnail, evidence artifact, Story Node, Focus Mode.

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Map images directory (this) | `web/public/images/maps/` | UI maintainers | Public, static, presentation-only assets |
| UI codebase | `web/` | UI maintainers | React/MapLibre/Cesium UI (contracted to APIs) |
| Master Guide | `docs/MASTER_GUIDE_v12.md` | KFM core team | Canonical pipeline + invariants |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Clear “in scope vs out of scope” guidance
- [ ] Conventions stated: naming, formats, licensing
- [ ] Validation steps listed (even if manual)

## 🗂️ Directory Layout

### This document
- `path`: `web/public/images/maps/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Frontend | `web/` | React UI + map clients |
| Public static assets | `web/public/` | Files served as-is by the web app |
| Story Nodes | `docs/reports/story_nodes/` | Provenance-linked narrative artifacts (preferred home for story-specific images) |
| Governed data assets | `data/` | Raw/work/processed datasets and catalog outputs |

### Expected file tree for this sub-area
~~~text
📁 web/
└── 📁 public/
    └── 📁 images/
        └── 📁 maps/
            ├── 📄 README.md
            ├── 🖼️ example__ks__overview.webp
            ├── 🖼️ example__ks__overview.png
            └── 📄 example__ks__overview.meta.json   # optional; recommended for attribution/provenance
~~~

## 🧭 Context

### Background
- The KFM UI needs some **static** map imagery for lightweight UI experiences (marketing pages, empty states, sample previews).
- Governed datasets and evidence artifacts still flow through the canonical pipeline; this directory is for **presentation-only** assets.

### Assumptions
- Files under `web/public/` are served publicly by the UI build/deploy system.
- The UI can reference these assets by a stable path (example: `/images/maps/<filename>`), independent of the API layer.

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode is preserved.
- Frontend consumes data/contracts via APIs (no direct graph dependency).
- This directory must not become a “shadow data lake.” If an asset is **data**, it must live under `data/**` and be cataloged.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Do we require a `.meta.json` sidecar for every asset? | TBD | TBD |
| Should we standardize image sizes (e.g., thumbnails vs heroes) across the UI? | TBD | TBD |

### Future extensions
- Add an automated image audit step (size, format, missing attribution).
- Add a UI registry entry (if/when a “layer registry schema” exists) that points to these assets.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[Governed datasets<br/>data/**] --> B[STAC/DCAT/PROV<br/>data/stac, data/catalog, data/prov]
  B --> C[Graph<br/>Neo4j]
  C --> D[APIs<br/>src/server]
  D --> E[Web UI<br/>web/]
  F[Static map images<br/>web/public/images/maps] --> E
  E --> G[Story Nodes<br/>docs/reports/story_nodes]
  G --> H[Focus Mode]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant User
  participant UI as Web UI
  participant API
  User->>UI: Load page
  UI->>API: Fetch layer/story data (contracted)
  UI->>UI: Load static image (if needed) from /images/maps/...
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Map image asset | `.webp` / `.png` / `.svg` | Created by UI/story design, or derived from governed sources | License known + file size + visual QA |
| Attribution/provenance sidecar (recommended) | `.meta.json` | Authored with the image | Schema TBD (keep minimal) |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Public static asset served by the UI | image | `web/public/images/maps/<name>.<ext>` | none (static file) |

### Sensitivity & redaction
- Do **not** place imagery that reveals restricted locations or culturally sensitive sites unless governance review explicitly allows public release.
- If an image requires redaction/generalization, treat it as a governed artifact and document the process (ideally via PROV), then publish only the approved derivative here.

### Quality signals
- File size is kept reasonable for web delivery (target: “fast enough on mobile”).
- Image is crisp at expected UI sizes; no illegible labels at thumbnail scale.
- Transparent backgrounds are intentional (avoid accidental alpha artifacts).

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- If a map image is a **thumbnail/preview** for a governed dataset, prefer modeling it as a STAC asset (role: thumbnail/overview) and having the UI reference it from the dataset’s cataloged location.
- Only copy into `web/public/images/maps/` when the image is genuinely UI-only or a curated, governance-approved derivative.

### DCAT
- Public UI assets still need clear licensing/attribution. Ensure the source license is compatible with public distribution.

### PROV-O
- If the asset is derived from governed sources (e.g., cropped from a scanned map), capture lineage as a PROV activity in the governed pipeline. This directory should only receive the final, approved derivative.

### Versioning
- Prefer **additive** updates (new filename/version suffix) over in-place replacement when an asset is referenced externally.
- Suggested filename convention (recommended; not enforced by schema):
  - `topic__region__time__variant.ext` (all lowercase, double-underscore separators)
  - Example: `railroads__ks__1880s__overview.webp`

## 🧱 Architecture

### Components
- Static assets: `web/public/images/maps/*`
- UI consumers: React components under `web/` (MapLibre/Cesium layers, story UI, etc.)
- Governed sources: datasets + catalogs + graph + APIs (do not bypass)

### Interfaces / contracts
- Static assets are referenced by path from the UI.
- All data-driven map layers and narrative context must be pulled via API contracts (not by reaching into the graph).

### Extension points checklist (for future work)
- [ ] Define and validate an optional `.meta.json` schema for attribution/provenance.
- [ ] Add a linter/audit job for `web/public/images/maps/` (size/license/metadata).
- [ ] Add documentation linking Story Nodes to these assets when appropriate.

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- These images may appear as **decorative UI elements** (thumbnails, banners) but must not be treated as “evidence” unless they are provenance-linked and traceable to governed sources.

### Provenance-linked narrative rule
- Focus Mode content must remain provenance-linked. Do not use a static image from this directory as the sole support for a factual claim.

### Optional structured controls
- Not confirmed in repo: a standard field for referencing UI assets from Story Nodes.
- If needed, prefer referencing by a stable public path (`/images/maps/<filename>`) and documenting why it’s presentation-only.

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Confirm filenames follow the recommended convention (kebab-case or `topic__region__...`)
- [ ] Confirm license/attribution is documented (inline or via `.meta.json`)
- [ ] Confirm the asset renders correctly in the UI at intended sizes
- [ ] Confirm file size is reasonable for web delivery

### Reproduction
- If the asset is derived from governed data, document (at minimum):
  - Source dataset identifier
  - Tooling used (e.g., GDAL/QGIS) and settings (crop, reprojection, color)
  - Output parameters (format, resolution, compression)

# Example placeholders — replace with repo-specific commands
# 1) validate schemas
# 2) run unit/integration tests
# 3) run doc lint

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| Asset size regressions | UI build logs | TBD |
| Missing attribution metadata | audit job | TBD |

## ⚖ FAIR+CARE & Governance

### Review gates
- Governance review is required when adding:
  - New imagery with unclear licensing
  - Imagery depicting potentially sensitive or restricted locations
  - Imagery intended to function as evidence in a Story Node / Focus Mode experience

### CARE / sovereignty considerations
- Identify affected communities when imagery could expose culturally sensitive places or narratives.
- Apply generalization/redaction rules consistently, and document decisions.

### AI usage constraints
- Ensure this doc’s AI permissions/prohibitions match intended use (front-matter is authoritative).

## 🕰️ Version History
| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-23 | Initial README for UI map image assets | TBD |

---

Footer refs:
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`