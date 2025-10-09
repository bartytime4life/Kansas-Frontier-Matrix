<div align="center">

# 🗺️ Kansas Frontier Matrix — Map Wireframe Exports  
`docs/design/mockups/map/wireframes/exports/`

**Purpose:** Store and document the exported **map wireframe images** used for KFM web UI documentation,  
prototyping, and accessibility review.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../..)  
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../../..)  
[![Accessibility](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-yellow)](../../../../../..)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../../LICENSE)

</div>

---

## 🧭 Overview

This directory contains **Figma-exported PNG and SVG wireframes** representing the core **Map Interface layouts**  
of the Kansas Frontier Matrix (KFM) Web UI.  

Each export corresponds to a **specific interaction state or device view**, forming part of the official design  
reference set for development, validation, and documentation purposes.

Exports are used to:
- 🧩 Document map-related UI layouts and overlays within Markdown READMEs.  
- 🌐 Serve as reference assets during frontend component development (React + MapLibreGL).  
- ♿ Support accessibility QA (contrast, labeling, responsive testing).  
- 🔒 Validate file integrity through checksums in CI/CD pipelines.  

---

## 🗂️ Directory Layout

```text
docs/design/mockups/map/wireframes/exports/
├── README.md                     # This file
├── map_ui_default.png             # Primary desktop layout
├── map_ui_mobile.png              # Compact mobile layout
├── map_timeline_overlay.png       # Integrated map + timeline design
└── map_darkmode.png               # Dark theme variant
````

---

## 🧱 Export Standards

| Property              | Standard                                      | Description                              |
| --------------------- | --------------------------------------------- | ---------------------------------------- |
| **Format**            | PNG (preferred), SVG optional                 | Exported directly from Figma master file |
| **Resolution**        | 1920×1080 px (desktop) / 1280×720 px (mobile) | Consistent 16 : 9 ratio                  |
| **DPI**               | 144                                           | Retina-ready resolution                  |
| **Color Space**       | sRGB                                          | Consistent display across browsers       |
| **Naming Convention** | `map_ui_{variant}.png`                        | Lowercase, underscores only              |
| **Accessibility**     | ≥ 4.5 : 1 contrast ratio                      | Meets WCAG 2.1 AA guidelines             |

All exports follow the **Design System Color Token Framework**
(`web/src/styles/tokens.css`) for consistent appearance across all KFM modules.

---

## 🧩 Export Workflow

Exports originate from the Figma master file `map_wireframes_v1.fig` and are tracked for validation.

### 🧱 Steps

1️⃣ **Design Source**
Wireframes finalized and reviewed in Figma.
Naming aligns with MCP and repository structure.

2️⃣ **Export & Naming**
Figma → Export → PNG @2x or SVG →
Use convention: `map_ui_{variant}.png`

3️⃣ **Storage & Tracking**
Save under this directory.
Add metadata entries in `../metadata/map_wireframes_metadata.json`.
Record SHA-256 checksum for each asset.

4️⃣ **Validation & Review**
CI pipeline (`stac-validate.yml`) confirms:

* File presence and naming consistency
* Checksum match
* Metadata completeness
* Accessibility compliance

**Manual Checksum Example:**

```bash
shasum -a 256 *.png > checksums.sha256
```

---

## 🧠 Usage Examples

### 🖼 Documentation Previews

Used in KFM design documentation for visual guidance:

![Map Timeline Overlay](map_timeline_overlay.png)

### 💻 Frontend Implementation Reference

| React Component       | Wireframe Export           |
| --------------------- | -------------------------- |
| `MapView.tsx`         | `map_ui_default.png`       |
| `LayerControls.tsx`   | `map_ui_mobile.png`        |
| `TimelineOverlay.tsx` | `map_timeline_overlay.png` |
| `MapThemeToggle.tsx`  | `map_darkmode.png`         |

Each export acts as the **visual baseline** for component positioning, responsiveness, and visual balance.

---

## ♿ Accessibility & QA Review

Accessibility validation ensures each design export complies with WCAG 2.1 AA.

| Test                     | Requirement                    | Tool                                                 |
| ------------------------ | ------------------------------ | ---------------------------------------------------- |
| **Contrast Ratio**       | ≥ 4.5 : 1                      | Figma Contrast Plugin / Axe DevTools                 |
| **Text Legibility**      | Minimum 12px font size         | Design System Tokens                                 |
| **Alt Text Metadata**    | Required for all exports       | Stored in `../metadata/map_wireframes_metadata.json` |
| **Dark Mode Validation** | Equal visibility in both modes | Manual & Automated QA                                |

Accessibility reports are automatically checked during pull requests and stored in the design QA log.

---

## 🧾 Provenance & Integrity

| Attribute             | Description                                   |
| --------------------- | --------------------------------------------- |
| **Design Source**     | `map_wireframes_v1.fig` (Figma master)        |
| **Generated By**      | KFM Design Team (Figma Export Workflow)       |
| **Checksum Tracking** | SHA-256 recorded in metadata JSON             |
| **Validated In CI**   | `stac-validate.yml`, `jsonschema.yml`         |
| **Reviewed By**       | KFM Design QA & MCP Documentation Review      |
| **License**           | [CC-BY 4.0](../../../../../../LICENSE)        |
| **MCP Compliance**    | Documented → Designed → Validated → Published |

---

## 🧮 CI/CD Validation Pipeline

| Stage | Process                     | Validation Target                                        |
| ----- | --------------------------- | -------------------------------------------------------- |
| **1** | Metadata Schema Check       | `map_wireframes_metadata.json`                           |
| **2** | File Integrity Verification | SHA-256 checksum validation                              |
| **3** | Accessibility Audit         | Contrast + labeling review                               |
| **4** | Provenance Verification     | Figma → Commit → Metadata linkage                        |
| **5** | Documentation Deployment    | Verified assets published to `/docs/design/mockups/map/` |

---

## 📚 Related References

* [🗺 Map Wireframes (Main)](../README.md)
* [🧩 Map Wireframe Metadata](../metadata/README.md)
* [🧱 Web UI Architecture](../../../../../../architecture/web_ui_architecture_review.md)
* [🌐 STAC Catalog](../../../../../../data/stac/catalog.json)
* [♿ Accessibility Design Standards](../../../../../design/reviews/accessibility/README.md)

---

<div align="center">

### Kansas Frontier Matrix — Documentation-First Design

**Spatial Design · Temporal Context · Provenance Integrity**

</div>
