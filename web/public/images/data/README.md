---
title: "KFM Web UI — Data Images (README)"
path: "web/public/images/data/README.md"
version: "v1.0.0"
last_updated: "2025-12-23"
status: "draft"
doc_kind: "Readme"
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

doc_uuid: "urn:kfm:doc:web:public-images:data-readme:v1.0.0"
semantic_document_id: "kfm-web-public-images-data-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:public-images:data-readme:v1.0.0"
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

# KFM Web UI — Data Images (README)

## 📘 Overview

### Purpose
This directory (`web/public/images/data/`) contains **UI-facing, publicly served** images used to support KFM data exploration and narrative UX (e.g., dataset thumbnails, legends, explanatory figures, evidence-panel imagery).

This README governs:
- What belongs here vs. what belongs in `data/` (canonical datasets)
- How to add images safely (licensing, provenance linkage, sensitivity)
- How to keep image references stable for the UI and Story Nodes

### Scope
| In Scope | Out of Scope |
|---|---|
| Small, web-optimized **static** images that ship with the frontend (thumbnails, legends, diagrams, UI evidence imagery) | Canonical data assets (raster scans, large imagery, tiles, COGs), user uploads, build artifacts, sensitive imagery intended to be access-controlled |
| Images referenced by UI components and/or Story Nodes as supporting visuals | “Source-of-truth” geospatial layers (these must remain in `data/processed/` + catalogs) |
| Decorative visuals **only if** they are clearly data-contextual (e.g., iconography for data domains) | Anything requiring credentials or access gating (this folder is public) |

### Audience
- Primary: Frontend engineers; Story Node authors/curators
- Secondary: Data engineering; governance reviewers (licensing/sensitivity)

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **UI-facing derivative**: a small preview/legend image used for display, not a canonical dataset artifact
  - **Evidence image**: an image used in Story Nodes / Focus Mode as supporting material for a claim (must be provenance-linked via Story Node citations)

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `web/public/images/data/README.md` | Web/UI | Folder governance + conventions |
| Public data images directory | `web/public/images/data/` | Web/UI | Images in this folder are public when deployed |
| Master guide (pipeline invariants) | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical ordering + invariants |
| Canonical data outputs | `data/processed/` + `data/stac/` | Data Eng | Source-of-truth assets + catalogs |
| Lineage bundles | `data/prov/` | Data Eng | Transform provenance for derived artifacts |
| Story Nodes | `docs/reports/story_nodes/` (and/or graph) | Story/Curators | Narrative artifacts with provenance |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Clear “in scope / out of scope” boundary for this directory
- [ ] Minimal conventions for naming + provenance + licensing
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed/stac outputs |
| STAC | `data/stac/` | STAC Collections + Items for canonical assets |
| DCAT | `data/catalog/dcat/` | Dataset catalog views (DCAT 3) |
| PROV | `data/prov/` | Lineage bundles (PROV-O) |
| Documentation | `docs/` | Canonical governed docs |
| Frontend | `web/` | React + map clients + public assets |
| Story Nodes | `docs/reports/story_nodes/` + graph | Narrative artifacts with provenance |

### Expected file tree for this sub-area
~~~text
📁 web/
└── 📁 public/
    └── 📁 images/
        └── 📁 data/
            └── 📄 README.md
~~~

## 🧭 Context

### Background
We need a predictable, reviewable location for **small, stable image assets** that the frontend can reference by URL/path. Without a boundary, teams often mix:
- canonical datasets and derivatives,
- UI previews and source-of-truth imagery,
- licensed third-party assets and project-generated media.

This directory is the “UI asset surface” for **data-context images** only.

### Assumptions
- `web/public/` is publicly served by the deployed site (no access control at this layer).
- UI code references these assets via stable relative paths (treat filenames as an interface).
- Canonical geospatial/image data remains governed in `data/` with STAC/DCAT/PROV alignment.

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode is preserved.
- Frontend consumes contracts via APIs (no direct graph dependency).
- This directory is **public**: do not place sensitive, restricted, or sovereignty-protected imagery here.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Do we require a per-image provenance sidecar (e.g., `*.meta.json`)? | TBD | TBD |
| Do we enforce a max file size / dimensions in CI? | TBD | TBD |
| Do Story Nodes reference these assets directly or via an API-provided asset registry? | TBD | TBD |

### Future extensions
- Add a lightweight **asset manifest** (schema-validated) mapping images → dataset/document IDs.
- Add automated thumbnail/legend generation from STAC Items (if/when desired).
- Add CI checks for file size, format, licensing attribution, and broken references.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React/Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]

  subgraph PublicAssets[Public web assets]
    H[/images/data/*]
  end

  E -. references .-> H
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant UI
  participant API
  participant Graph
  UI->>API: Focus query(entity_id)
  API->>Graph: fetch subgraph + provenance refs
  Graph-->>API: context bundle
  API-->>UI: narrative + citations + audit flags
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| UI preview images (thumbnails) | `webp/png/svg` | Authored by team or derived from canonical assets | Manual review; license/provenance review |
| Legends / explanatory figures | `svg/png` | Authored from dataset semantics | Visual QA; check that labels match current layer/version |
| Evidence-support images | `webp/png` | Derived from governed data or public-domain sources | Must be provenance-linked in Story Node references |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Public UI data images | `webp/png/svg/jpg` | `web/public/images/data/` | Path stability is the contract (filenames as interface) |

### Sensitivity & redaction
- This folder is **public-by-default**. Do not include:
  - images that reveal sensitive locations that require generalization/redaction,
  - imagery under restrictive licensing that cannot be redistributed,
  - imagery containing PII (faces, addresses, private property details) unless explicitly governed and permitted.

### Quality signals
- Prefer web-optimized formats (SVG for vector; WebP/PNG for raster where appropriate).
- Keep images readable at typical UI sizes (including mobile).
- Avoid encoding critical meaning via color alone (accessibility).

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections involved: *if an image is a preview of a STAC asset*, the canonical asset remains in STAC (`data/stac/…`).
- Items involved: preview images should be traceable to the relevant STAC Item/Asset **via Story Node citations or an asset registry** (mechanism TBD).
- Extension(s): N/A for this folder directly (this folder is not the canonical STAC asset store).

### DCAT
- Dataset identifiers: images that function as dataset previews should be attributable to a DCAT dataset record (mapping mechanism TBD).
- License mapping: any third-party image must have a compatible license and attribution recorded.

### PROV-O
- `prov:wasDerivedFrom`: if a preview/evidence image is derived from a governed dataset, provenance should be recordable (mechanism TBD).
- `prov:wasGeneratedBy`: if generated by a pipeline, link to the transform activity/run that produced it.
- Activity / Agent identities: as per `data/prov/` conventions.

### Versioning
- Treat file paths under `web/public/images/data/` as **stable interfaces**.
- Avoid renaming once referenced in UI or Story Nodes. If change is necessary:
  - keep the old path temporarily (or provide a migration path),
  - update all in-repo references in the same change.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| Public assets | Serve static images | URL/path under `web/public/…` |
| UI | Render map + narrative + evidence | References assets by path; consumes APIs |
| APIs | Provide data/story contracts | REST/GraphQL |
| Story Nodes | Provenance-linked narrative | Stored/retrieved content; references evidence |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Static asset path contract | `web/public/images/data/**` | Avoid renames; treat paths as public API |
| Story Node evidence references | `docs/reports/story_nodes/` + API payloads | Must remain provenance-linked |
| Governance constraints | `docs/governance/*` | Review-gated updates |

### Extension points checklist (for future work)
- [ ] Data: generate new preview images from governed assets (automation)
- [ ] Catalogs: link previews to STAC/DCAT identifiers (manifest/schema)
- [ ] PROV: record generation lineage for derived previews (if pipeline-generated)
- [ ] UI: add consistent UI components that consume preview images safely
- [ ] Focus Mode: ensure evidence panels reference provenance IDs

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Data images in this folder may appear as:
  - dataset thumbnails in browse/search results,
  - legend images for specific layers,
  - evidence images embedded in Story Node panels.

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID.
- If an image is used as evidence in a narrative context, the **Story Node must carry citations** that connect it to source dataset/document IDs.

### Optional structured controls
~~~yaml
focus_layers:
  - "data-images"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] Ensure images are safe for public release (no sensitive content; licensing verified)
- [ ] Ensure references are not broken (UI/story references resolve to existing files)
- [ ] Optional: file size + dimension checks (if CI gate exists/added)
- [ ] Optional: image optimization pass (if tooling exists/added)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) run web build
# 2) run UI lint/tests
# 3) run link/reference checks (if present)
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| TBD | TBD | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates
- UI maintainers review: naming/path stability; performance impact
- Governance review (as needed): licensing, sensitivity, sovereignty constraints

### CARE / sovereignty considerations
- If imagery could expose culturally sensitive sites, sacred locations, or restricted community knowledge:
  - do not publish here,
  - follow sovereignty policy and any required redaction/generalization practices.

### AI usage constraints
- Ensure this doc’s AI permissions/prohibitions match intended use (see front-matter).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-23 | Initial README for `web/public/images/data/` | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`