---
title: "KFM Web — Cesium Icon Assets"
path: "web/cesium/assets/icons/README.md"
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

doc_uuid: "urn:kfm:doc:web:cesium:assets:icons:readme:v1.0.0"
semantic_document_id: "kfm-web-cesium-assets-icons-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:cesium:assets:icons:readme:v1.0.0"
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

# 🎨 Cesium icon assets

## 📘 Overview

This directory contains **static icon assets** used by the `web/` frontend in Cesium-adjacent UI surfaces, including (but not limited to):

- marker/billboard icons for Cesium entities
- UI control icons (buttons, toggles, legend markers)
- layer/status indicator icons (loading, warning, filtered, etc.)

Icons here are **UI assets** only. They do not change the canonical data pipeline ordering and must not introduce any new direct data access paths (UI always consumes data through contracted APIs).

### Purpose

- Provide a canonical home for Cesium-related icons under `web/`
- Establish consistent conventions for naming, formats, and accessibility
- Ensure license/attribution hygiene for any third-party assets

### Scope

In scope:

- SVG/PNG icons used by Cesium-based UI components and entity styling

Out of scope:

- Data icons embedded in STAC assets (those belong under `data/**`)
- Vector tiles/spritesheets intended for MapLibre style JSON (those belong under MapLibre asset conventions)

### Audience

- UI developers (React/Cesium)
- Design contributors
- Reviewers checking licensing, accessibility, and repository hygiene

### Definition of done

- [ ] This README stays in sync with the directory contents and usage patterns
- [ ] Added icons follow naming + format rules below
- [ ] Any third-party icon has attribution recorded (see “Licensing & attribution”)

---

## 🗂️ Directory Layout

### This document

- `path`: `web/cesium/assets/icons/README.md` (must match front-matter)

### Expected file tree for this sub-area

~~~text
web/
└── 🌐 cesium/
    └── 🧰 assets/
        └── 🎨 icons/
            ├── 📄 README.md
            ├── 🖼️ *.svg
            └── 🖼️ *.png
~~~

> Note: If subfolders are introduced (e.g., `markers/`, `ui/`), they must be added to the tree above and documented in “Naming & file standards”.

---

## 🧭 Context

### Background

KFM’s UI stack may include a Cesium globe/scene alongside other mapping surfaces. Icons in this directory support consistent visual encoding across Cesium entities and UI controls without duplicating assets in multiple locations.

### Assumptions

- The exact module bundler / asset pipeline is **not specified here**; icon referencing may be done via:
  - static public paths, or
  - import-as-URL via the frontend build system.

### Constraints and invariants

- Icons must not embed secrets, tokens, or sensitive location details.
- Avoid vendor-locked proprietary icon packs unless licensing is explicitly compatible.
- Prefer deterministic, reviewable assets (vector-first, optimized).

---

## 🧱 Naming and file standards

### Naming

- Use **kebab-case** and keep names descriptive:
  - `marker-fort.svg`
  - `marker-treaty.svg`
  - `ui-close.svg`
  - `ui-info.svg`
  - `status-warning.svg`
- Avoid spaces, avoid uppercase, avoid ambiguous names like `icon1.svg`.

### Formats

Preferred:

- **SVG** for most icons (scales cleanly across DPI and zoom levels)

Allowed when necessary:

- **PNG** for raster-only artwork that does not translate to SVG

If using PNG:

- Provide consistent sizing (e.g., 24px/32px base) and use an explicit higher-resolution variant policy if needed by the UI (e.g., `@2x`) *only if the build system supports it*.

### Optimization

- SVGs should be kept lean (remove editor metadata, unused groups, hidden layers).
- PNGs should be compressed appropriately for web delivery.

(Exact tooling/commands are intentionally not prescribed here unless a repo-standard toolchain is confirmed.)

---

## 🧭 Using icons in Cesium

This section is **illustrative**. Update it to match the actual `web/` build tool once confirmed.

### Entity billboards

~~~ts
// Example (illustrative):
// - Use an icon as a Cesium Billboard image.
// - The import/URL mechanism depends on the frontend build system.

const iconUrl = "/cesium/assets/icons/marker-fort.svg"; // example static path

viewer.entities.add({
  position: Cesium.Cartesian3.fromDegrees(-95.0, 39.0),
  billboard: {
    image: iconUrl,
    width: 32,
    height: 32,
    verticalOrigin: Cesium.VerticalOrigin.BOTTOM
  }
});
~~~

### UI controls

- Icons used in buttons must be paired with visible labels or `aria-label`.
- Decorative icons should be `aria-hidden="true"` when appropriate.

---

## ♿ Accessibility

- Do not rely on color alone to convey meaning (pair status icons with text or tooltips).
- Maintain sufficient contrast for icons used as UI affordances.
- When an icon is the only content of a control, ensure the control has an accessible name (e.g., `aria-label="Close"`).

---

## ⚖️ Licensing and attribution

All icon assets must be:

- original to the project, **or**
- included under a license compatible with the repository’s licensing and distribution model.

If any third-party icons are included, record attribution below.

### Third-party attributions

| Asset | Source | License | Notes |
|---|---|---|---|
| _None yet_ |  |  |  |

---

## 🧪 Validation and CI

Suggested checks for PR review (adjust if CI enforces these):

- [ ] Filenames follow kebab-case and are descriptive
- [ ] SVGs/PNGs are optimized and reasonably sized
- [ ] UI usage includes accessible labels where required
- [ ] Any third-party asset has attribution recorded above

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-24 | Initial README for Cesium icon assets | TBD |

---

## ⚖️ Footer

Governance references:

- `docs/governance/ROOT_GOVERNANCE.md`
- `docs/governance/ETHICS.md`
- `docs/governance/SOVEREIGNTY.md`
---
