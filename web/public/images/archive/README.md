---
title: "KFM — UI Image Archive (web/public/images/archive)"
path: "web/public/images/archive/README.md"
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

doc_uuid: "urn:kfm:doc:web:public-images-archive-readme:v1.0.0"
semantic_document_id: "kfm-web-public-images-archive-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:public-images-archive-readme:v1.0.0"
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

# KFM — UI Image Archive (web/public/images/archive)

## 📘 Overview

### Purpose
This directory holds archived static images that are **not** part of the current shipped UI, but are kept for traceability, historical reference, or future curation.

Use this archive to:
- preserve replaced/deprecated UI imagery without deleting provenance,
- stage candidate imagery before promoting it to an active UI asset or Story Node asset,
- keep “public web assets” separate from evidence products (STAC/DCAT/PROV) and Story Node assets.

### Scope
In scope:
- Deprecated or superseded UI images (backgrounds, illustrations, older screenshots)
- Draft/candidate images that may be promoted later
- Exported figures created for UI-only use (non-evidence)

Out of scope (use canonical homes instead):
- Active UI images → `web/public/images/` (or the project’s active UI asset path)
- Story Node images intended for publication → `docs/reports/story_nodes/.../assets/`
- Evidence assets (maps, geotagged photos, scanned sources, GeoTIFFs, etc.) → treat as data and catalog via STAC/DCAT/PROV in `data/**`

### Audience
- UI developers and designers working under `web/`
- Curators preparing narrative media
- Governance reviewers checking licensing/provenance of public-facing assets

### Definitions (link to glossary)
- Link: `docs/glossary.md` *(if present)*
- **Archived image**: an asset retained for reference but not currently required by the UI build.
- **Promote**: move/copy an asset from this archive into a canonical, actively-consumed location with proper metadata.

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | KFM core maintainers | Canonical pipeline + invariants |
| v13 Redesign Blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture | Canonical homes by stage |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Story/UX | Narrative structure + provenance fields |
| Governance root | `docs/governance/ROOT_GOVERNANCE.md` | Governance | Review gates, licensing, sensitive content |

### Definition of done (for this document)
- [ ] Front-matter `path` matches `web/public/images/archive/README.md`
- [ ] Archive purpose + scope is clear (what belongs here vs elsewhere)
- [ ] Promotion rules documented (to UI / to Story Node assets / to data catalog)
- [ ] Licensing/provenance expectations documented
- [ ] Expected file tree included and uses emojis

## 🗂️ Directory Layout

### This document
- `path`: `web/public/images/archive/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Active UI images | `web/public/images/` | Images referenced by the UI at runtime/build time |
| UI image archive | `web/public/images/archive/` | Archived, deprecated, or staging images (this directory) |
| Story Nodes | `docs/reports/story_nodes/` | Draft/published story markdown + story assets |
| Story assets | `docs/reports/story_nodes/published/<story_slug>/assets/` | Images/media intended to ship with a published Story Node |
| Data domains | `data/<domain>/` | Raw/work/processed datasets and domain readmes |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | STAC/DCAT/PROV for evidence products |
| API boundary | `src/server/` | Contracted access layer (REST/GraphQL) |
| Frontend | `web/` | React/Map UI implementation |

### Expected file tree for this sub-area
~~~text
📁 web/
└── 📁 public/
    └── 📁 images/
        ├── 📁 archive/
        │   ├── 📄 README.md
        │   ├── 📁 2025/
        │   │   └── 📁 <topic-or-ticket>/
        │   │       ├── 🖼️ <image_file>.<ext>
        │   │       └── 📄 <image_file>.meta.json   # optional (recommended)
        │   └── 📄 manifest.csv                      # optional (recommended)
        └── 🖼️ <active-ui-images...>
~~~

## 🧭 Context

### Background
KFM’s canonical flow is evidence-first: **ETL → catalogs (STAC/DCAT/PROV) → graph → APIs → UI → Story Nodes → Focus Mode**. The UI and Story layers may display images, but published narrative must remain provenance-linked.

This archive exists to prevent “mystery assets” from drifting into active UI or Story Node outputs without clear provenance and licensing.

### Assumptions
- Treat anything under `web/public/` as potentially public-facing/shippable *(confirm the repo’s web build behavior).*
- This folder is not the canonical home for evidence or curated Story Node assets.

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode is preserved.
- `web/` must not connect to Neo4j directly; all graph access is via the API layer.
- Anything promoted into Story Nodes / Focus Mode must have provenance (no uncited narrative media).

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Do we require a per-image `.meta.json` file or a single `manifest.*` file? | TBD | TBD |
| Do we enforce a max file size / dimensions for archived images? | TBD | TBD |
| Should large media use Git LFS or an external asset store? *(policy not confirmed in repo)* | TBD | TBD |

### Future extensions
- Add an optional `schemas/ui/image_manifest.schema.json` and CI validation *(not confirmed in repo).*
- Add an image optimization/preflight step under `tools/` *(not confirmed in repo).*

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  subgraph Archive
    A[web/public/images/archive]
  end

  subgraph UI
    B[web/public/images\nactive]
    U[React/Map UI]
  end

  subgraph Story
    S[docs/reports/story_nodes/.../assets]
    SN[Story Nodes]
    FM[Focus Mode]
  end

  subgraph Evidence
    R[data/<domain>/raw]
    E[ETL]
    C[STAC/DCAT/PROV]
  end

  A -->|promote (UI-only)| B
  A -->|promote (narrative media + citations)| S
  A -->|treat as data (evidence)| R
  R --> E --> C --> U --> SN --> FM
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant UI
  participant API
  participant Graph
  UI->>API: request narrative + media refs
  API->>Graph: fetch subgraph + provenance refs
  Graph-->>API: context bundle
  API-->>UI: narrative + citations + media refs
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Archived raster image | `png` / `jpg` / `webp` | Design exports, replaced UI assets | Manual review (license + provenance) |
| Archived vector image | `svg` | Icon/illustration sources | Manual review + SVG safety scan (if used) |
| Optional per-image metadata | `*.meta.json` | Added by curator/dev | JSON validity (schema if adopted) |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Archived images | image files | `web/public/images/archive/**` | N/A |
| Optional manifest | `csv` / `yaml` / `json` | `web/public/images/archive/manifest.*` | Not confirmed in repo |
| Promoted Story assets | image files + citations | `docs/reports/story_nodes/**/assets/` | Story Node template + validation |

### Sensitivity & redaction
- Do **not** place sensitive/PII-bearing images in `web/public/` paths.
- If an image contains people, private addresses, culturally sensitive sites, or restricted material, it must live in a controlled location with governance review (policy details: see governance docs).

### Quality signals
- Filenames are stable, descriptive, and do not include PII (no full names, phone numbers, etc.).
- Each third‑party image has a recorded source + license + attribution (via `.meta.json` or manifest).
- File sizes are reasonable for repository health (optimize before committing when possible).

## 🌐 STAC, DCAT & PROV Alignment

### STAC
Use STAC when an image is an **evidence asset** (e.g., a map image with spatial/temporal extent, geotagged photo, scanned source used as evidence):
- Store the asset under the appropriate `data/<domain>/...` path.
- Create a corresponding STAC Item under `data/stac/items/` with license + source attribution.
- Do not ship evidence assets solely as UI `public/` files.

### DCAT
If archived images are part of a dataset release, represent the dataset via DCAT under `data/catalog/dcat/` (and link to STAC/evidence assets as applicable).

### PROV-O
If an image is derived (cropped/annotated/filtered), record the transformation lineage (PROV bundle under `data/prov/` for evidence products; Story Node provenance fields for narrative assets).

### Versioning
- Prefer “new file, new name” for changed binaries; keep the prior file when history matters.
- If an archived image becomes active again, promote it (copy/move) into the canonical active location and keep the archive copy (or record its replacement) to preserve traceability.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| UI (static assets) | Serve icons/illustrations | Files under `web/public/**` |
| Story Nodes | Curated narrative + media | `docs/reports/story_nodes/**` + API presentation |
| Catalogs | Evidence metadata | `data/stac/` + `data/catalog/dcat/` + `data/prov/` |
| API boundary | Access-controlled delivery | `src/server/` |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Story Node schema/template | `docs/templates/` | Template versioning; published nodes validate |
| UI asset conventions | This README | Update version + note changes |
| Optional archive manifest schema | `schemas/ui/` | Semver *(not confirmed in repo)* |

### Extension points checklist (for future work)
- [ ] Define (or confirm) canonical active UI image directory and how bundling works.
- [ ] Add optional manifest + schema and validate in CI.
- [ ] Add “promotion” checklist for moving an image to Story Node assets.
- [ ] Add tooling for optimization (size, format) and safety checks (SVG, etc.).

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
Archived images should not appear in Focus Mode directly. If needed in narrative:
1) Promote the image into the Story Node’s `assets/` folder, and  
2) Reference it from the Story Node markdown with required provenance/attribution.

### Provenance-linked narrative rule
If an image will be displayed in a Story Node / Focus Mode context, it must be provenance-linked:
- Source identifier (dataset/document ID, archive ref, or URL)
- License + attribution text
- Any edits/derivatives described (crop, colorization, annotations)
- If the image is evidence-bearing, prefer STAC/DCAT/PROV lineage over ad-hoc UI storage

### Optional structured controls
~~~json
{
  "image_id": "kfm-img-<slug>",
  "source": {
    "type": "url|dataset|document",
    "ref": "<url-or-id>",
    "license": "<spdx-or-text>",
    "attribution": "<required credit line>"
  },
  "created_at": "YYYY-MM-DD",
  "archived_at": "YYYY-MM-DD",
  "notes": "Why this is archived / what replaced it",
  "sha256": "<hash>",
  "promotion": {
    "status": "archived|promoted-to-ui|promoted-to-story|converted-to-evidence",
    "ref": "<new-path-or-story-slug>"
  }
}
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Confirm the image belongs in **archive** (not active UI, not Story Node assets, not evidence assets).
- [ ] Confirm licensing/provenance is recorded (meta file or manifest entry).
- [ ] Confirm filenames avoid PII and sensitive locations.
- [ ] If this repo validates UI assets, run the corresponding lint/CI checks *(commands not confirmed in repo).*

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) run repo lint / markdown lint
# 2) run UI build checks
# 3) (optional) run image optimization/preflight tool
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| Repo size / asset bloat | CI job | `docs/telemetry/` + `schemas/telemetry/` *(if adopted)* |

## ⚖ FAIR+CARE & Governance

### Review gates
- Archived images that are third‑party or historically sensitive should receive governance review before promotion into Story Nodes or other public-facing outputs.

### CARE / sovereignty considerations
- Some imagery may implicate communities, sacred sites, or culturally sensitive material.
- Follow the repo’s sovereignty and ethics guidance; do not publish restricted materials in public web paths.

### AI usage constraints
- Do not use AI to infer or disclose sensitive locations from imagery.
- Ensure that any AI-generated captions/alt text or enhancements are clearly labeled and opt-in when surfaced.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-23 | Initial README for UI image archive | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`