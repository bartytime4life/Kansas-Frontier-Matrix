---
title: "Cesium UI Assets — Icons"
path: "web/cesium/assets/images/icons/README.md"
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

doc_uuid: "urn:kfm:doc:web:cesium:assets:icons-readme:v1.0.0"
semantic_document_id: "kfm-web-cesium-assets-icons-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:cesium:assets:icons-readme:v1.0.0"
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

# Cesium UI Assets — Icons

## 📘 Overview

### Purpose

- Define **conventions, safety checks, and attribution rules** for icon assets stored in `web/cesium/assets/images/icons/`.
- Keep icon usage **deterministic**, **auditable**, and **license-compliant** across the UI.

### Scope

| In Scope | Out of Scope |
|---|---|
| Icon files stored in this directory (SVG/PNG), naming, size guidance, and license/attribution handling | Runtime UI code, Cesium/Map rendering logic, third-party library licensing (handled via dependency tooling), fonts, and non-icon imagery |

### Audience

- Primary: UI contributors working under `web/` (Cesium/Map layers, controls, legend/UX elements).
- Secondary: reviewers (governance/security), release packagers, and maintainers.

### Definitions

- **Icon asset**: A small static image used by the UI (e.g., buttons, legends, markers, layer controls).
- **Third-party icon**: Any icon not created in-house for KFM (including icons downloaded from libraries, design systems, or vendors).
- **Attribution record**: The required source/license/credit line(s) needed by an icon’s license.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Cesium assets NOTICE | `web/cesium/assets/NOTICE.md` | UI maintainers | Canonical location for third-party asset attribution/notice entries |
| Imagery fixtures README | `web/cesium/assets/fixtures/imagery/README.md` | UI maintainers | Parallel conventions for non-icon imagery fixtures |

### Definition of done (for icon additions)

- [ ] File name follows the naming rules in this README.
- [ ] File contains **no embedded scripts** (SVG) and no external references (SVG).
- [ ] File size is reasonable for UI delivery (optimize/strip metadata).
- [ ] If third-party: `web/cesium/assets/NOTICE.md` includes a complete attribution entry.
- [ ] Icon does not encode sensitive locations, protected personal info, or culturally restricted imagery.
- [ ] UI usage includes accessible labeling (alt text/ARIA in code where applicable).

## 🗂️ Directory Layout

### This document

- `path`: `web/cesium/assets/images/icons/README.md` (must match front-matter)

### Expected file tree for this sub-area

~~~text
web/cesium/assets/images/icons/
│
├── 📄 README.md
├── 🖼️ <icon-name>.svg
├── 🖼️ <icon-name>.png
└── 🖼️ <icon-name>@2x.png          # optional, if raster is used and high-DPI is needed
~~~

## ✅ Conventions

### 1) File formats

- **Preferred:** `*.svg` (scales cleanly, generally smaller, themeable when authored correctly).
- **Allowed:** `*.png` (use when the icon must be raster, includes complex textures, or is used as a sprite/billboard).
- **Avoid:** formats that complicate audits or delivery (e.g., animated assets) unless there is a documented need and review.

### 2) Naming

Use **lowercase kebab-case**:

- ✅ `kfm-layer-treaties.svg`
- ✅ `kfm-marker-event.png`
- ❌ `TreatyIcon.svg`
- ❌ `kfm marker event.png`

If you maintain multiple variants, encode the variant in the name (not folders):

- `kfm-marker-event.svg`
- `kfm-marker-event--selected.svg`
- `kfm-marker-event@2x.png`

### 3) SVG safety and portability rules

SVGs must be safe to ship and easy to review:

- No scripts, no event handlers, no embedded remote URLs.
- No external file references (fonts/images) unless explicitly required and reviewed.
- Strip unnecessary metadata when possible.

**Recommendation:** keep SVGs “simple” (paths, groups) and avoid editor-specific artifacts.

### 4) Raster guidance (PNG)

If PNG is used:

- Prefer **square** icons where reasonable (e.g., 24×24, 32×32, 48×48), but match UI needs.
- If you add `@2x` variants, keep the same visual bounds and alignment.
- Avoid embedding text in raster icons (text does not scale well and complicates localization).

### 5) Licensing and attribution

- If an icon is **created for KFM**, no additional notice entry is required beyond normal repository licensing.
- If an icon is **third-party**, you must:
  1. Verify the license permits redistribution in this repository context.
  2. Add an attribution entry to: `../../NOTICE.md`
  3. Preserve any required license text files if the license demands it.

If license/terms are ambiguous, treat the asset as **restricted** until reviewed.

### 6) Sensitivity / ethics

Icons are UI-facing and can carry meaning:

- Avoid imagery that could reveal sensitive locations or protected personal information.
- Avoid culturally sensitive symbols, insignia, or restricted knowledge representations unless reviewed under `docs/governance/SOVEREIGNTY.md`.
- Do not encode specific “real-world” private addresses/places into marker art.

## 🧪 Validation (recommended checks)

These are recommended checks for CI or pre-commit hooks (implementation may vary by repo):

- Detect `<script>` tags and event handler attributes in SVG.
- Block remote references (e.g., `href="http..."`) in SVG.
- Enforce filename conventions for new assets.
- Require `NOTICE.md` updates when third-party icons are added.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-24 | Initial icons README for Cesium asset conventions | (you) |

