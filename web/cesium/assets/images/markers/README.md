---
title: "Cesium Marker Images"
path: "web/cesium/assets/images/markers/README.md"
version: "v1.0.0"
last_updated: "2025-12-24"
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

doc_uuid: "urn:kfm:doc:web:cesium:assets:images:markers:readme:v1.0.0"
semantic_document_id: "kfm-web-cesium-assets-images-markers-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:cesium:assets:images:markers:readme:v1.0.0"
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

# Cesium Marker Images

> **Purpose (required):** Document how marker image assets in `web/cesium/assets/images/markers/` are stored, named, licensed, and used so the Cesium UI remains lightweight, accessible, and compliant.

## 📘 Overview

### What belongs here

This directory is for **marker images** used to render point features (e.g., Cesium billboards / pins) in the KFM Cesium UI.

Markers are **presentation assets** only:
- They should not encode private data.
- They should not “hard-code” domain meaning that must come from governed datasets or API contracts.
- They must remain safe to ship publicly.

### Scope

| In scope | Out of scope |
|---|---|
| Marker images in `web/cesium/assets/images/markers/` (e.g., `.svg`, `.png`) and related conventions | General UI icons (`web/cesium/assets/icons/`), tileset fixtures (`web/cesium/assets/fixtures/tilesets/`), or application logic / layer registry code |

### Audience

- Frontend contributors working in `web/cesium/**`
- Layer authors configuring point visualizations in the Cesium UI

### Definitions

- **Marker**: An image used to represent a point feature in the 3D globe (typically as a billboard).
- **Variant**: A deliberate visual alternative (e.g., `selected`, `hover`, `disabled`).
- **Retina / HiDPI**: A higher-resolution raster asset (commonly `@2x`) used to preserve crispness on high-density displays.

## 🗂️ Directory Layout

### Location

- **This README:** `web/cesium/assets/images/markers/README.md`
- **Markers directory:** `web/cesium/assets/images/markers/`

### Expected tree

~~~text
📁 web/
└── 📁 cesium/
    └── 📁 assets/
        └── 📁 images/
            └── 📁 markers/
                ├── 📄 README.md
                ├── 🖼️ marker-*.svg
                └── 🖼️ marker-*.png
~~~

### Related asset directories

| Directory | Purpose |
|---|---|
| `web/cesium/assets/icons/` | General UI icons (buttons, menus, etc.) |
| `web/cesium/assets/fixtures/tilesets/` | Local/test tilesets used for development/QA |
| `web/cesium/assets/images/markers/` | Point/marker images used in Cesium map views |

## 🧭 Context

### Naming conventions

Use **kebab-case** and a consistent `marker-` prefix.

**Recommended pattern:**
- `marker-<semantic>-<variant>.<ext>`

Examples:
- `marker-site.svg`
- `marker-site-selected.svg`
- `marker-warning.svg`
- `marker-warning@2x.png` (only for raster/PNG)

Rules:
- Avoid spaces and uppercase.
- Keep names stable once referenced by UI configurations.
- If a marker is deprecated, keep the old file until all references are migrated (then remove in a dedicated cleanup change).

### Formats

Prefer **SVG** for simple icons/pins:
- Scales cleanly
- Typically smaller when optimized
- Easier to recolor (depending on how the UI loads the SVG)

Use **PNG** only when SVG is not suitable (e.g., complex gradients/textures).
If using PNG:
- Provide a crisp base size and (optionally) a `@2x` variant.
- Avoid embedding unnecessary metadata.

### Size and anchor guidance

Markers should be designed so that:
- The visual “tip” of a pin is near the **bottom-center** of the image.
- Transparent padding is minimized (helps picking/anchoring accuracy).
- Variants keep the same canvas size to prevent “jumping” when switching states.

### Accessibility guidance

Markers should not rely on color alone to convey meaning:
- Use shape differences, stroke patterns, or overlays for categories/states.
- Check visibility against typical basemap imagery (light/dark terrain, satellite).

## 📦 Data & Metadata

### Asset registry

When adding or modifying marker assets, update this table so licensing and provenance are explicit.

| File | Intended usage | Source / author | License | Notes |
|---|---|---|---|---|
| (add rows) | | | | |

### Licensing and attribution

- Only include assets you have the rights to redistribute under the repository’s licensing model.
- Record attribution and license in the **Asset registry** above.
- Avoid “unknown origin” icons (even if commonly found online).

## 🧠 Story Node & Focus Mode Integration

Markers may be used by UI layers that appear in Story Nodes or Focus Mode, but:
- Story Nodes should cite **evidence IDs** (STAC/DCAT/PROV) and **entity IDs**; they should not depend on marker filenames.
- Marker selection should be driven by UI configuration and contracted API responses (e.g., feature type/state), not by direct graph access or hidden heuristics.

## 🧪 Validation & CI/CD

### Before committing new marker assets

- [ ] File name follows the naming convention.
- [ ] Asset is optimized (SVG minified; PNG compressed).
- [ ] No embedded secrets/PII (including in metadata).
- [ ] License/provenance recorded in the Asset registry.
- [ ] Visual sanity check in the UI (correct size and anchor).

### Example usage snippet (illustrative)

~~~js
// Illustrative only — adjust imports/paths to match the repo’s build tooling.
const markerUrl = "assets/images/markers/marker-site.svg";

// Example Cesium entity billboard (pseudo-code):
viewer.entities.add({
  position: someCartesian3,
  billboard: {
    image: markerUrl,
    verticalOrigin: Cesium.VerticalOrigin.BOTTOM
  }
});
~~~

## 🧱 Architecture

- This directory is part of the **UI** stage (`web/**`) in KFM’s canonical pipeline.
- Marker assets are **static** and must remain safe for public builds.
- The UI should consume **contracted APIs** and apply any redaction/generalization rules at the boundary (markers must not “reveal” restricted data by design).

## ⚖ FAIR+CARE & Governance

Governance considerations for marker assets:
- Do not introduce marker designs that imply sensitive status unless the UI also enforces the appropriate access controls.
- Prefer neutral, general-purpose markers where possible.
- Changes that introduce new sensitive categories or public-facing “signals” should be flagged for governance review.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-24 | Initial directory README for Cesium marker images | TBD |

---

Footer refs:
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

