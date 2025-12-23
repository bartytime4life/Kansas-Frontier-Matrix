---
title: "UI Widget Images — README"
path: "web/public/images/ui/widgets/README.md"
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

doc_uuid: "urn:kfm:doc:web:public-images-ui-widgets-readme:v1.0.0"
semantic_document_id: "kfm-web-public-images-ui-widgets-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:public-images-ui-widgets-readme:v1.0.0"
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

# UI Widget Images — README

## 📘 Overview

### Purpose
- Define what belongs in `web/public/images/ui/widgets/` and what does **not**.
- Document a stable path/naming “contract” so UI components can reference assets without churn.
- Capture minimum governance expectations for UI assets (licensing/provenance, sensitive symbolism).

### Scope

| In Scope | Out of Scope |
|---|---|
| Static UI images used by widgets/components (icons, small illustrations) stored under this folder | Dataset/map assets that should be cataloged (STAC/DCAT/PROV), tiles, imagery derived from ETL outputs |
| Folder organization + filename stability | API/UI feature design, Story Node content, layer registries |

### Audience
- Primary: UI/frontend contributors working in `web/`
- Secondary: Designers providing exports, reviewers verifying licensing/provenance, maintainers managing repo hygiene

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Widget image**: A static visual asset used by a UI widget/component (toolbar icon, panel illustration, button glyph).
  - **Public asset**: A file served by the frontend as a static resource (commonly via a `/public/`-style mechanism). *(Exact serving rules depend on the frontend build tool; not confirmed in repo.)*

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Widget images directory | `web/public/images/ui/widgets/` | UI maintainers | Folder contract + stability guidance |
| Master pipeline ordering | `docs/MASTER_GUIDE_v12.md` | KFM core | “What belongs where” boundaries |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | KFM governance | Structure reference |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Directory tree and examples reflect current folder contents (or clearly marked “expected / optional”)
- [ ] Conventions clearly separate “required” vs “proposed (not confirmed in repo)”
- [ ] Licensing/provenance guidance included for any third‑party assets
- [ ] Validation steps are listed (even if repo commands are TBD)

## 🗂️ Directory Layout

### This document
- `path`: `web/public/images/ui/widgets/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed + STAC/DCAT/PROV outputs |
| Documentation | `docs/` | Canonical governed docs |
| Graph | `src/graph/` | Graph build + ontology bindings |
| Pipelines | `src/pipelines/` | ETL + catalogs + transforms |
| Schemas | `schemas/` | JSON schemas + telemetry schemas |
| Frontend | `web/` | React + map clients |
| MCP | `mcp/` | Experiments, model cards, SOPs |

### Expected file tree for this sub-area
~~~text
📁 web/
└── 📁 public/
    └── 📁 images/
        └── 📁 ui/
            └── 📁 widgets/
                ├── 📄 README.md
                ├── 📄 (optional) LICENSES.md              # third‑party attributions (if any)
                ├── 📄 (optional) SOURCES.md               # provenance notes (if any)
                ├── 🖼️ icon-*.svg                          # recommended for simple icons
                ├── 🖼️ illus-*.png                         # recommended for raster illustrations
                └── 🖼️ (other widget assets as needed)
~~~

## 🧭 Context

### Background
Widget images are UI-only assets. Without a documented contract, these files often drift into inconsistent naming, untracked licensing, and accidental mixing of UI art with dataset-derived imagery.

### Assumptions
- The frontend build tool serves `web/public/` contents as static assets at runtime. *(Not confirmed in repo; validate with the current web stack.)*
- UI widget images do **not** carry evidence claims; evidence belongs in catalogs/graph and is rendered with citations in the UI.

### Constraints / invariants
- Preserve canonical ordering: ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode.
- UI consumes graph/catalog content through the API boundary (no direct Neo4j dependency).
- Do not place dataset-derived imagery here unless it is clearly “UI chrome” (decorative) and not a data artifact. Data artifacts should be cataloged under `data/` and referenced via the API/catalog.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What is the frontend bundler/framework, and what are the exact static asset URL rules? | TBD | TBD |
| Do we want a formal naming convention + linter for UI assets? | TBD | TBD |
| Do we need a required `LICENSES.md` / `SOURCES.md` policy for third‑party art? | TBD | TBD |

### Future extensions
- Add an asset naming lint/check (CI) if the widget library expands.
- Add a lightweight manifest (JSON) if runtime discovery/registration becomes necessary. *(Not confirmed in repo.)*

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
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant UI as UI (Web App)
  participant Assets as Static Assets
  UI->>Assets: GET /images/ui/widgets/<file>
  Assets-->>UI: 200 image bytes
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Widget icon source | SVG (preferred) | Design export or hand-authored | Render check + SVG lint/opt (TBD) |
| Widget illustration source | PNG/WebP (as needed) | Design export | File-size + visual QA (TBD) |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Widget images | SVG / PNG / WebP | `web/public/images/ui/widgets/` | Stable paths + naming contract (this README) |

### Sensitivity & redaction
- Avoid embedding sensitive locations, private names, or culturally sensitive identifiers into artwork.
- If an icon/illustration could be interpreted as sensitive or culturally specific, route through governance review (see below).

### Quality signals
- Assets are optimized for web delivery (minimized size, no unnecessary metadata).
- Icons render crisply at typical UI sizes.
- Filenames are stable and descriptive.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Not applicable for UI widget images.
- If an image is a **geospatial asset** (map, raster, scan, tile), it belongs under `data/` and must be cataloged via STAC.

### DCAT
- Not applicable for UI widget images.
- Dataset-level metadata should be captured in DCAT under `data/catalog/dcat/`.

### PROV-O
- Not applicable for UI widget images.
- ETL/data transformation lineage belongs under `data/prov/`.

### Versioning
- Prefer additive changes (new files) over renaming/replacing referenced files.
- If a referenced file must be replaced, treat the path as a public contract: update all UI references in the same change set.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| UI static assets (this folder) | Provide UI widget visuals | Static file paths (served by web stack) |
| UI | Map + narrative | API calls + static assets |
| APIs | Serve contracts | REST/GraphQL |
| Graph | Neo4j | API layer only |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Widget image path contract | `web/public/images/ui/widgets/` | Avoid breaking renames; treat paths as stable |
| UI layer registry | `web/cesium/layers/regions.json` | Schema-validated *(if present in repo)* |

### Extension points checklist (for future work)
- [ ] Add a new widget image file (SVG/PNG/WebP)
- [ ] Confirm license/provenance for the new asset (especially third‑party art)
- [ ] Ensure path stability (avoid renames)
- [ ] Update this README if new conventions/categories are introduced

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Indirectly: widget images may be used as UI affordances inside Focus Mode views (buttons, panels, toolbars).
- Widget images must not encode claims/evidence; evidence remains provenance-linked via APIs and citations.

### Provenance-linked narrative rule
- No narrative claims are made by these assets; Focus Mode narrative must remain provenance-linked.

### Optional structured controls
~~~yaml
# Not applicable (UI asset directory). No Focus Mode controls defined here.
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (if applied outside `docs/`; not confirmed)
- [ ] Asset filenames follow this README’s conventions
- [ ] Images load correctly in the UI (manual QA)
- [ ] License/provenance captured for any third‑party assets

### Reproduction
~~~bash
# Placeholder — replace with repo-specific commands.
# 1) run UI lint/build
# 2) load the app and verify widget icons render
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| N/A | N/A | N/A |

## ⚖ FAIR+CARE & Governance

### Review gates
- New third‑party assets (license/provenance review)
- Any asset that could be culturally sensitive or misrepresent communities
- Any change that replaces/renames widely referenced assets

### CARE / sovereignty considerations
- Avoid using sacred/protected symbols without approval.
- If an icon depicts a culturally sensitive motif, document the rationale and obtain the appropriate review.

### AI usage constraints
- This README allows summarization/structuring, but prohibits generating new policy or inferring sensitive locations (see front-matter).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-23 | Initial widget images README | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`