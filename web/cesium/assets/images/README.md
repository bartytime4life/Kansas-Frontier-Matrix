---
title: "Cesium UI Assets — Images"
path: "web/cesium/assets/images/README.md"
version: "v1.0.0"
last_updated: "2025-12-24"
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

doc_uuid: "urn:kfm:doc:web:cesium:assets:images:readme:v1.0.0"
semantic_document_id: "kfm-web-cesium-assets-images-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:cesium:assets:images:readme:v1.0.0"
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

# Cesium UI Assets — Images

> **Purpose (required):** Document what belongs in `web/cesium/assets/images/`, how images should be named/optimized/attributed, and what review gates apply before images are referenced by the Cesium UI.

## 📘 Overview

### Purpose

- Provide a single contract for **what image assets belong here** and how they are managed.
- Reduce UI regressions by standardizing **formats, naming, and attribution** for images used by the Cesium client.

### Scope

| In Scope | Out of Scope |
|---|---|
| UI images used by the Cesium experience (icons, markers, UI illustrations, small static images referenced by frontend code) | Dataset assets and evidence artifacts (e.g., STAC Items, raw/work/processed raster/vector outputs, large imagery datasets) |
| Attribution + licensing notes for third‑party images used in the UI | Story Node narrative evidence bundles (store with Story Nodes / provenance artifacts — exact path not confirmed in repo) |
| Basic conventions (naming, optimization, accessibility notes) | Defining geospatial layer semantics (belongs in UI registry/config; not here) |

### Audience

- Primary: Frontend contributors working in `web/cesium/**`
- Secondary: Maintainers performing governance/licensing review for UI-facing assets

### Definitions (link to glossary)

- Link: `docs/glossary.md`
- Terms used in this doc include: **static asset**, **attribution**, **license**, **sensitive location**, **redaction/generalization**, **UI registry**.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This images directory | `web/cesium/assets/images/` | Frontend | Static images used by Cesium UI |
| Cesium UI root (if present) | `web/cesium/` | Frontend | Not confirmed in repo; inferred from this directory path |
| Repo governance baseline | `docs/governance/ROOT_GOVERNANCE.md` | KFM Core | Approval flow + enforcement expectations |
| Sovereignty policy | `docs/governance/SOVEREIGNTY.md` | KFM Core | Applies if assets reveal sensitive locations or community-controlled information |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | KFM Core | Governing structure for this README |

### Definition of done (for this document)

- [ ] Front-matter complete + valid and `path` matches file location
- [ ] What belongs in this directory is explicit (scope + examples)
- [ ] Attribution + licensing expectations documented
- [ ] Basic accessibility expectations documented (alt text rules where applicable)
- [ ] Governance review gates and “sensitive content” cautions included
- [ ] Version history present and kept current

## 🗂️ Directory Layout

### This document

- `path`: `web/cesium/assets/images/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| UI | `web/` | Frontend clients and UI registry/config |
| Cesium UI | `web/cesium/` | Cesium-based map client (not confirmed in repo) |
| Cesium assets | `web/cesium/assets/` | Static assets for Cesium UI (not confirmed in repo) |
| Cesium images | `web/cesium/assets/images/` | This directory: images referenced by Cesium UI |
| Docs + governance | `docs/` | Canonical governed docs and policies |
| API boundary | `src/server/` (or legacy) | Where UI should read from (never Neo4j directly) — exact location not confirmed here |

### Expected file tree for this sub-area

> This structure is recommended. Subfolders may not exist yet (**not confirmed in repo**).

~~~text
📂 web/
└─ 📂 cesium/
   └─ 📂 assets/
      └─ 📂 images/
         ├─ 📄 README.md
         ├─ 📂 icons/                 # SVG preferred (not confirmed in repo)
         ├─ 📂 markers/               # map pins/markers (not confirmed in repo)
         ├─ 📂 logos/                 # only if licensing/permission allows (not confirmed in repo)
         ├─ 📂 ui/                    # UI illustrations (not confirmed in repo)
         └─ 📄 SOURCES_AND_LICENSES.md # recommended attribution log (not confirmed in repo)
~~~

## 🧭 Context

### Background

Cesium is used (or planned) as a 3D visualization path for the KFM UI, enabling terrain/globe rendering and time-dynamic visualization. In that context, this directory holds **presentation assets** (icons/markers/illustrations), not datasets. Keep data assets in the pipeline/catalog locations and treat these as UI-only static files.

### Constraints / invariants

- This directory is for **static UI assets**; it is not a data/catalog location.
- Do not place raw/processed domain data here (GeoTIFFs, COGs, GeoJSON, STAC Items).
- Treat screenshots or images that reveal **restricted/sensitive locations** as high-risk and subject to governance review (see Governance section).

## 🗺️ Diagrams

~~~text
(Design/Source) -> (Add/optimize image in this folder) -> (Reference from UI code)
                 -> (Build pipeline copies/bundles static assets) -> (Deployed UI)
~~~

## 🧠 Story Node & Focus Mode Integration

- This directory supports **UI rendering** (icons/markers/illustrations).
- Any image used as **evidence for a narrative claim** should be provenance-linked and governed as part of the Story Node / evidence bundle (exact storage path for Story Node assets is not confirmed in repo).
- Focus Mode content must remain provenance-linked and avoid orphan/uncited claims; do not use UI imagery to imply unverified facts.

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol check (front-matter + required sections)
- [ ] Secrets scan (ensure no embedded tokens/keys inside SVG metadata, etc.)
- [ ] Licensing check for third-party assets:
  - confirm license compatibility
  - confirm attribution text is recorded (see Data & Metadata)
- [ ] Sensitive content scan (manual review): no screenshots or images that reveal restricted locations/precise sensitive coordinates

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands (not confirmed in repo)
# npm run lint
# npm run build
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| asset_added | git diff | PR / commit history |
| license_verified | reviewer checklist | PR template / review notes (not confirmed in repo) |

## 📦 Data & Metadata

### Naming conventions

- Use **kebab-case** filenames.
- Prefer a semantic prefix:
  - `icon-<name>.svg`
  - `marker-<name>.png`
  - `ui-<name>.webp` (or `.png`)
  - `logo-<org>.svg` (only if permitted)
- Avoid spaces and avoid ambiguous names like `image1.png`.

### Preferred formats (guidance)

- **SVG**: preferred for icons and simple vector marks (ensure safe, minimal SVG content).
- **PNG/WebP**: for raster images; optimize before committing when possible.
- Avoid committing very large binaries without an explicit reason and review.

### Attribution requirements (third-party assets)

If an image is not fully authored in-repo, record these fields in an attribution log (recommended file: `SOURCES_AND_LICENSES.md`, not confirmed in repo):

| Field | Required? | Example |
|---|---:|---|
| File | Yes | `icons/icon-search.svg` |
| Source | Yes | Publisher/site/project name |
| License | Yes | CC-BY-4.0 / CC0 / Public Domain / other |
| Attribution text | If required by license | “© …, used under …” |
| Modified? | Yes | yes/no + short description |
| Date added | Yes | YYYY-MM-DD |
| Notes | Optional | link to approval, if needed |

### Accessibility notes

- Icons used as interactive controls must have accessible labels in UI code (alt/aria-label).
- Do not embed critical text only inside images unless there is an accessible text alternative in the UI.

## 🌐 STAC, DCAT & PROV Alignment

- **N/A for this directory.** These are UI static assets, not catalog artifacts.
- STAC/DCAT/PROV outputs must remain in their canonical pipeline locations; do not mix them into UI asset folders.

## 🧱 Architecture

### How these assets are used

- Images in this directory are intended to be referenced by Cesium UI components (icons, markers, UI elements).
- Keep usage consistent:
  - static assets remain in `web/cesium/assets/images/`
  - data access remains via contracted APIs (UI does not directly query the graph)

## ⚖ FAIR+CARE & Governance

### Review gates

Governance review is recommended/required when changes include:

- adding third‑party logos or brand assets (license/permission confirmation)
- adding images that could reveal **sensitive locations** (e.g., screenshots with precise coordinates or identifiable landmarks)
- any change that affects public-facing UI messaging or could increase interpretability of restricted information

(Approver roles/process are **not confirmed in this directory**; align with `docs/governance/ROOT_GOVERNANCE.md`.)

### CARE / sovereignty considerations

- Treat community- or sovereignty-sensitive content as high risk by default.
- Avoid images that could enable inference of protected sites or culturally sensitive locations.
- If in doubt, prefer generalized/abstract UI assets and document the decision path.

### AI usage constraints

- Ensure this document’s AI permissions/prohibitions match intended use.
- Do not use AI to infer or reconstruct sensitive locations based on UI images or screenshots.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-24 | Initial images directory README (conventions + governance notes) | TBD |

---

### Footer refs

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
---
