<div align="center">

# 🧩 Kansas Frontier Matrix — Panel Wireframe Exports  
`docs/design/mockups/panels/wireframes/exports/`

**Purpose:** Store, document, and version-control exported **visual wireframe images**  
for all KFM panel layouts — including **Detail Panels**, **AI Assistant**, **Layer/Filter Controls**,  
and **Mobile Stack Views**.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../..)  
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../../..)  
[![Accessibility](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-yellow)](../../../../../..)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../../LICENSE)

</div>

---

## 🧭 Overview

This directory contains **static image exports** (PNG/JPG) generated from  
the **Figma master file** `panel_wireframes_v1.fig`.  

These exports provide:
- 📘 Visual documentation for the **Panels Wireframes** module  
- 💻 Implementation reference for **React UI components**  
- 🧪 Validation targets for CI workflows and accessibility audits  
- ♿ Screenshots for inclusion in the **KFM documentation portal**

Each export represents a finalized design state, supporting reproducible handoff between design and code.

---

## 🗂️ Directory Layout

```text
docs/design/mockups/panels/wireframes/exports/
├── README.md                   # This file
├── detail_panel_default.png     # Entity detail and metadata panel
├── ai_assistant_panel.png       # Conversational AI assistant interface
├── filter_layer_panel.png       # Map layer/filter control panel
└── mobile_stack_panel.png       # Responsive stacked mobile layout
````

---

## 🧱 Export Standards

| Property              | Standard                                     | Description                                 |
| --------------------- | -------------------------------------------- | ------------------------------------------- |
| **File Format**       | PNG (preferred) / JPG                        | High-resolution raster images               |
| **Dimensions**        | 1920×1080 px (desktop), 1280×720 px (mobile) | Optimized for documentation and UI previews |
| **DPI**               | 144                                          | Retina and high-density display ready       |
| **Color Profile**     | sRGB                                         | Web-safe color accuracy                     |
| **Background**        | Transparent or `#F5F5F5`                     | Matches KFM light theme                     |
| **Naming Convention** | `panel_{component_name}.png`                 | Lowercase, underscores only                 |
| **Accessibility**     | ≥ 4.5 : 1 contrast ratio                     | Verified per WCAG 2.1 AA                    |

---

## 🧩 Export Workflow

All wireframe exports are derived from Figma frames and validated via MCP pipelines for reproducibility and provenance.

### 1️⃣ Export from Figma

**File → Export → PNG @2x**
Use naming convention: `panel_{component_name}.png`

### 2️⃣ Store and Track

Save exported assets in this directory.
Add entries to `../metadata/panel_wireframes_metadata.json`, including:

* SHA-256 checksums
* License
* Accessibility and provenance fields

### 3️⃣ Validate in CI

During continuous integration (`stac-validate.yml`):

* Verify export existence
* Check checksum integrity
* Confirm metadata fields (license, provenance, accessibility)

**Manual validation example:**

```bash
shasum -a 256 *.png > checksums.sha256
```

---

## 🧠 Usage Examples

### 📘 Markdown Previews

Used in documentation for visual references:

![AI Assistant Panel](ai_assistant_panel.png)

### 💻 Web UI Development

Exports serve as visual design guides for component alignment and structure:

| React Component      | Export Reference           |
| -------------------- | -------------------------- |
| `DetailPanel.tsx`    | `detail_panel_default.png` |
| `AssistantPanel.tsx` | `ai_assistant_panel.png`   |
| `LayerControls.tsx`  | `filter_layer_panel.png`   |
| `PanelStack.tsx`     | `mobile_stack_panel.png`   |

---

## ♿ Accessibility Review

All exports undergo **accessibility QA** for visual clarity and compliance.

| Requirement                 | Standard          | Validation                                             |
| --------------------------- | ----------------- | ------------------------------------------------------ |
| **Contrast Ratio (Text)**   | ≥ 4.5 : 1         | Verified via Figma or design audit                     |
| **Contrast Ratio (Icons)**  | ≥ 3 : 1           | Confirmed manually during review                       |
| **Light/Dark Theme Checks** | Dual verification | Each export tested in both modes                       |
| **Alt Text**                | Required          | Stored in `../metadata/panel_wireframes_metadata.json` |

Accessibility annotations are recorded within metadata for transparency.

---

## 🧾 Provenance & Validation

| Attribute             | Description                                          |
| --------------------- | ---------------------------------------------------- |
| **Design Source**     | `panel_wireframes_v1.fig` (Figma master file)        |
| **Generated By**      | KFM Design System · Figma Export Workflow            |
| **Checksum Tracking** | SHA-256 hashes in metadata JSON                      |
| **Validated By**      | CI pipelines (`stac-validate.yml`, `jsonschema.yml`) |
| **Reviewed By**       | KFM Design QA (Pull Request audits)                  |
| **License**           | [CC-BY 4.0](../../../../../../LICENSE)               |
| **MCP Compliance**    | Documented → Designed → Validated → Published        |

---

## 🧮 CI/CD Integration

| Stage | Action              | Validation Target                                              |
| ----- | ------------------- | -------------------------------------------------------------- |
| **1** | Schema Validation   | `panel_wireframes_metadata.json`                               |
| **2** | File Integrity      | `SHA-256` checksum verification                                |
| **3** | Accessibility Audit | Contrast and alt text review                                   |
| **4** | Provenance Logging  | Figma → Commit → Metadata trace                                |
| **5** | Publication         | Verified documentation export to `docs/design/mockups/panels/` |

---

## 📚 Related References

* [Panels Wireframes (Main)](../README.md)
* [Panel Wireframes Metadata](../metadata/README.md)
* [Map Wireframes](../../../map/wireframes/README.md)
* [AI Assistant Wireframes](../../../ai-assistant/wireframes/README.md)
* [Kansas Frontier Matrix Web UI Architecture](../../../../../../architecture/web_ui_architecture_review.md)

---

<div align="center">

### Kansas Frontier Matrix — Documentation-First Design

**Panels · Provenance · Accessibility · Reproducibility**

</div>
