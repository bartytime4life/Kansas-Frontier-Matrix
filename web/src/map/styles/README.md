---
title: "KFM Map Styles (MapLibre) — README"
path: "web/src/map/styles/README.md"
version: "v1.0.0"
last_updated: "2025-12-25"
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

doc_uuid: "urn:kfm:doc:web:map:styles:readme:v1.0.0"
semantic_document_id: "kfm-web-map-styles-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:map:styles:readme:v1.0.0"

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

> **Purpose (required):** Define how **MapLibre style assets** are organized, named, validated, and governed for the **KFM web UI map**, so style changes remain deterministic, accessible, and do not accidentally reveal sensitive information.

# KFM Map Styles (MapLibre) — README

## 📘 Overview

### Purpose

This directory documents the **map style layer** for KFM’s **web UI map** (MapLibre-style JSON and any supporting style assets). It governs:

- How style files are structured and versioned
- How layer IDs and source names are kept stable (to avoid UI regressions)
- How governance constraints (sensitivity, provenance, sovereignty) apply to *visualization choices*, not just data

### Scope

| In Scope | Out of Scope |
|---|---|
| MapLibre **style JSON** conventions, naming, layer ordering, tokens, sprite/glyph references | ETL pipelines, STAC/DCAT/PROV generation, Neo4j ingest, API implementation |
| Review/validation expectations for style changes | Writing Story Nodes (see story template) |
| How styles interact with the **UI layer registry** (config-driven layers) | Designing the domain ontologies |

### Audience

- Primary: Frontend engineers + cartography maintainers working under `web/`
- Secondary: Data stewards (for provenance + sensitivity review), API maintainers (tile endpoints/contracts)

### Definitions (link to glossary)

- Link: `docs/glossary.md`
- Terms used in this doc:
  - **MapLibre style JSON**: Mapbox style-spec v8 compatible JSON defining sources/layers/paint/layout
  - **Layer registry**: UI configuration that declares selectable map layers (path **not confirmed in repo**; see notes below)
  - **Source**: A style-level data input (vector/raster/geojson) referenced by style layers
  - **Provenance-linked**: UI content that can be traced back to dataset/item IDs (required for Focus Mode narratives)

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `web/src/map/styles/README.md` | UI | Conventions + governance |
| Style JSON files | `web/src/map/styles/**/*.json` | UI | Base styles + overlays (exact layout not confirmed) |
| Layer registry | `web/**/layers/**` | UI | Mentioned as canonical location in project docs; exact directory tree not confirmed in repo |
| API contracts (map/tile/data) | `src/server/contracts/**` | API | UI must not query Neo4j directly (API boundary) |
| Schemas (validation) | `schemas/**` | Platform | Validate layer registry + metadata where present |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Docs/Curators | Focus Mode narrative rules |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] Directory purpose and conventions are explicit
- [ ] Layer/source naming and ordering guidance is clear
- [ ] Validation steps are listed (even if commands are placeholders)
- [ ] Governance + CARE/sovereignty considerations for *visualization* are explicitly stated
- [ ] Footer refs present

---

## 🗂️ Directory Layout

### This document

- `path`: `web/src/map/styles/README.md` (must match front-matter)

### Recommended layout (not confirmed in repo)

~~~text
🌐 web/
└── 🧭 src/
    └── 🗺️ map/
        └── 🎨 styles/
            ├── 📄 README.md
            ├── 🧱 base/                 # base styles (light/dark, etc.) (not confirmed)
            │   ├── 🌞 kfm_base_light.json
            │   └── 🌙 kfm_base_dark.json
            ├── 🧩 overlays/             # optional overlay fragments (not confirmed)
            │   ├── 🏷️ labels.json
            │   └── 🧭 boundaries.json
            ├── 🎛️ tokens/               # shared style tokens/constants (not confirmed)
            │   └── 🎨 theme.ts
            └── 🧿 assets/               # sprite/glyph plumbing (not confirmed)
                ├── 🖼️ sprite.png
                └── 🧾 sprite.json
~~~

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| UI | `web/` | React UI + MapLibre map rendering |
| APIs | `src/server/` | API boundary + contracts (UI consumes APIs) |
| Graph | `src/graph/` | Neo4j ingest + ontology bindings (UI **never** reads graph directly) |
| Catalogs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Published discovery + provenance artifacts |
| Standards | `docs/standards/` | Repo structure + protocol rules (if present) |
| Story Nodes | `docs/reports/story_nodes/` | Curated narratives used in Focus Mode |

---

## 🧭 Context

KFM’s canonical flow is:

**ETL → STAC/DCAT/PROV → Graph → API → UI (React/MapLibre) → Story Nodes → Focus Mode**.

This directory sits in the **UI stage**. Style decisions are still “high-impact” because they can:

- Change interpretation (color ramps, thresholds, label emphasis)
- Accidentally reveal sensitive locations via zoom/interaction
- Break layer selection/highlighting if IDs change

**Non-negotiable:** the UI does **not** query Neo4j directly; it uses contracted APIs.:contentReference[oaicite:3]{index=3}

---

## 🗺️ Diagrams

### Where styles fit

~~~mermaid
flowchart LR
  ETL["ETL / Pipelines"] --> CAT["STAC / DCAT / PROV"]
  CAT --> G["Graph — Neo4j"]
  G --> API["APIs — REST + GraphQL"]
  API --> UI["UI — React + MapLibre"]
  UI --> SN["Story Nodes"]
  SN --> FM["Focus Mode"]
~~~

### Style + registry interaction (conceptual)

~~~mermaid
flowchart TB
  REG[UI Layer Registry] -->|declares layers + metadata| MAP[Map Component]
  STYLE[MapLibre Style JSON] -->|base paint/layout rules| MAP
  API[API endpoints] -->|vector/raster/geojson payloads| MAP
  MAP -->|renders| USER[User]
~~~

---

## 🧠 Story Node & Focus Mode Integration

Focus Mode v3 requires that content displayed is **provenance-linked**, and AI-generated elements must be clearly indicated (opt-in).:contentReference[oaicite:4]{index=4}

Style design should support that rule by enabling:

- **Selection/highlight layers** (e.g., when a Story Node references an entity/asset)
- **Legibility at context scales** (users can verify what they are seeing)
- **Uncertainty-aware styling** (recommended):
  - Prefer lower opacity, dashed outlines, or less saturated ramps for uncertain/estimated layers
  - Avoid “alarm colors” unless the underlying data product is actually a thresholded alert

> Not confirmed in repo: any reserved KFM layer IDs for hover/selection.  
> Recommended (if you adopt a convention): reserve a stable prefix like `kfm:ui:*` for hover/selection/highlight layers.

---

## 📦 Data & Metadata

Even though this is UI-only, map styling must remain aligned with:

- Dataset licensing and attribution (surface in UI where required)
- Classification/sensitivity (do not expose restricted layers via style defaults)
- Provenance (enable “what am I looking at?” link-outs)

### Recommended: embed minimal KFM metadata in style JSON (not confirmed in repo)

MapLibre styles allow a free-form `metadata` object. Recommended pattern:

~~~json
{
  "version": 8,
  "name": "KFM Base (Light)",
  "metadata": {
    "kfm": {
      "style_id": "kfm_base_light",
      "style_semver": "v1.0.0",
      "jurisdiction": "US-KS",
      "notes": "Base map only; domain layers come from the UI registry."
    }
  }
}
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

Styles should **not** become a second metadata system.

- Data product metadata belongs in STAC/DCAT/PROV and API contracts.
- UI configuration (layer registry) should reference stable identifiers (dataset IDs, collection IDs, item IDs).
- Styles should focus on paint/layout/labeling—while still enabling provenance UI affordances.

---

## 🧱 Architecture

### Invariants

- UI consumes data through **APIs**; it must not read Neo4j directly.:contentReference[oaicite:5]{index=5}
- Layer discoverability and toggling should be **config-driven** (layer registry) rather than hard-coded styling logic (exact registry path not confirmed in repo).
- Keep style identifiers stable to avoid breaking:
  - UI toggles
  - Story Node highlighting
  - Legend rendering

### Naming conventions (recommended)

Not confirmed in repo — adopt if useful:

- Style IDs: `kfm_*` (e.g., `kfm_base_light`)
- Layer IDs: `kfm:<domain>:<layer>` (e.g., `kfm:historical:treaties`)
- Source IDs: `src_<provider>_<type>` (e.g., `src_kfm_vector_basemap`)

### Layer ordering (recommended)

General ordering guidance (MapLibre draws later layers “on top”):

1. Raster terrain/hillshade (if used)
2. Basemap fills/landcover
3. Reference boundaries/roads/water
4. Domain overlays (time-aware layers)
5. Labels + POIs (ensure readable halos)
6. UI-only selection/hover highlight layers

---

## 🧪 Validation & CI/CD

### Validation steps (recommended)

- [ ] JSON lint (valid syntax)
- [ ] MapLibre style validation against style-spec v8 (tooling **not confirmed in repo**)
- [ ] UI schema checks (layer registry validation, if present):contentReference[oaicite:6]{index=6}
- [ ] Secrets scan (ensure style JSON does not embed tokens/keys)
- [ ] Accessibility check:
  - labels readable at common zooms
  - sufficient contrast for key thematic layers (WCAG-minded)
- [ ] Visual regression snapshots for base styles (tooling not confirmed)

### Reproduction (placeholders — replace with repo-specific commands)

~~~bash
# 1) Lint UI
# npm run lint

# 2) Validate styles (not confirmed in repo)
# node tools/validate_map_style.mjs web/src/map/styles/**/*.json

# 3) Run UI tests (not confirmed in repo)
# npm test
~~~

---

## ⚖ FAIR+CARE & Governance

### Review gates

Governance review is recommended/required when a style change:

- introduces a new visible layer (or makes an existing layer easier to discover)
- changes symbology such that it could reveal sensitive locations through interaction/zoom
- modifies attribution/licensing display expectations
- changes how uncertainty is communicated (e.g., “estimated” layers styled like “confirmed” layers)

### CARE / sovereignty considerations

- If a layer intersects sovereignty-controlled areas or culturally sensitive places:
  - prefer aggregation/generalization in the served data product
  - ensure the UI does not amplify sensitive detail via styling (e.g., high-contrast pinpoint symbols)
- Follow `docs/governance/SOVEREIGNTY.md` for policy (file presence not confirmed in repo).

### AI usage constraints

- Allowed: summarization, structure extraction, translation, keyword indexing.
- Prohibited: generating new policy; inferring sensitive locations.
- Any AI-assisted styling guidance must be reviewed by a human maintainer before publication.

---

## 🕰️ Version History

| Version | Date | Change summary | Author | PR / Issue |
|---|---:|---|---|---|
| v1.0.0 | 2025-12-25 | Initial README for MapLibre style conventions and governance | TBD | TBD |

---

## Footer refs (do not remove)

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- v13 blueprint (if adopted): `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`
---

