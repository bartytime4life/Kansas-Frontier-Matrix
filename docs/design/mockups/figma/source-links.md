<div align="center">

# 🔗 Kansas Frontier Matrix — Figma Source Links  
`docs/design/mockups/figma/source-links.md`

**Mission:** Maintain a version-controlled registry of all **Figma source projects, component libraries,  
and prototypes** for the **Kansas Frontier Matrix (KFM)**.  
These links ensure design provenance, reproducibility, and collaborative transparency.

[![Design Standards](https://img.shields.io/badge/Design-Human%20Centered-orange)](../../)
[![Accessibility](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-yellow)](../../)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)

</div>

---

## 🎯 Purpose

This document provides a **canonical list of Figma source links** used in the Kansas Frontier Matrix  
for interface design, storytelling layouts, and accessibility validation.  

Each entry includes:
- The **public or team-shareable URL** to the Figma project.  
- **Version number** and last-updated date.  
- **Associated exports** (in `/exports/`).  
- **Design lead / author**.  
- **Related documentation** for context (e.g., `ui-guidelines.md`, `style-guide.md`).  

All URLs are read-only where possible to maintain MCP reproducibility and avoid accidental overwrites.

---

## 🧩 Active Projects

| ID | Title | Figma URL | Version | Owner | Related Docs |
|:--|:--|:--|:--|:--|:--|
| `kfm_ui_core` | **Core Interface Library** (timeline, map, AI assistant) | [Figma Link →](https://www.figma.com/file/ABCDE12345/Kansas-Frontier-Matrix-Core?type=design) | v2.3 | `andy.barta` | [`ui-guidelines.md`](../../ui-guidelines.md), [`interaction-patterns.md`](../../interaction-patterns.md) |
| `kfm_storytelling` | **Storytelling Templates** (guided tour scenes, oral histories) | [Figma Link →](https://www.figma.com/file/FGHIJ67890/KFM-Storytelling-Templates?type=design) | v1.7 | `narrative.team` | [`storytelling.md`](../../storytelling.md) |
| `kfm_color_tokens` | **Design Tokens & Visual Palette** | [Figma Link →](https://www.figma.com/file/KLMNO54321/KFM-Design-Tokens?type=design) | v1.5 | `ui.lab` | [`style-guide.md`](../../style-guide.md) |
| `kfm_mobile` | **Responsive + Mobile Layouts** | [Figma Link →](https://www.figma.com/file/PQRST22222/KFM-Mobile-Views?type=design) | v0.9 | `ui.lab` | [`ui-guidelines.md`](../../ui-guidelines.md) |
| `kfm_accessibility` | **Accessibility & WCAG Review Prototypes** | [Figma Link →](https://www.figma.com/file/UVWXY33333/KFM-Accessibility-Audit?type=design) | v1.2 | `accessibility.team` | [`ui-guidelines.md`](../../ui-guidelines.md), [`style-guide.md`](../../style-guide.md) |

> **Note:** If you add a new Figma project, also export key frames to  
> `/docs/design/mockups/figma/exports/` and update metadata in the corresponding YAML file.

---

## 🧭 Figma Project Structure (Standard Layout)

```mermaid
flowchart TD
    A["🏠 Cover Page\n(Project Overview + Contact Info)"] --> B["🎨 Styles\n(Color · Typography · Tokens)"]
    B --> C["🧩 Components\nButtons · Panels · Legends"]
    C --> D["📱 Screens\nMap · Timeline · Story Panels"]
    D --> E["🧮 Prototypes\nInteractions · Transitions"]
    E --> F["♿ Accessibility Frames\nFocus · Contrast · Motion Checks"]
````

<!-- END OF MERMAID -->

Each Figma project must follow this layer and page structure
to ensure consistency across the entire Frontier Matrix design library.

---

## 🧾 Adding a New Figma Source

To register a new project:

1. 🖌️ **Create Project**
   Use the naming format `KFM_<Module>_<Descriptor>`
   *(e.g., `KFM_Timeline_UI`, `KFM_AI_Drawer`, `KFM_Mobile`)*.
2. 🔗 **Share View-Only Link**

   * Set permissions: “Anyone with the link → can view.”
   * Copy and paste the URL in the table above.
3. 🧾 **Add Metadata File**
   Create `metadata_<id>.yml` under `/docs/design/mockups/figma/`:

   ```yaml
   id: kfm_timeline_v2
   title: KFM Timeline UI Prototype
   version: v2.0
   author: andy.barta
   source: https://www.figma.com/file/12345ABCDE/KFM-Timeline
   description: >
     Refined horizontal scroll, zoom gestures, and keyboard navigation mapping.
   status: in_review
   related_docs:
     - ../../ui-guidelines.md
     - ../../interaction-patterns.md
   license: CC-BY-4.0
   ```
4. 🗂️ **Export Key Frames**
   Save `.png` or `.svg` exports to `/exports/` using the same ID.
5. 🧩 **Log Review**
   Add an entry under `/docs/design/reviews/` after design board approval.

---

## 🧮 Version & Audit Tracking

| Version | Date       | Reviewer             | Notes                                               |
| :------ | :--------- | :------------------- | :-------------------------------------------------- |
| v2.3    | 2025-10-06 | `ui_researcher`      | Core Figma file aligned with React components.      |
| v1.7    | 2025-10-05 | `narrative.team`     | Storytelling templates verified for screen readers. |
| v1.5    | 2025-10-05 | `ui.lab`             | Updated color tokens to match WCAG compliance.      |
| v0.9    | 2025-09-29 | `ui.lab`             | Mobile layout prototype for MapLibre viewports.     |
| v1.2    | 2025-09-25 | `accessibility.team` | Added dark mode and keyboard focus frames.          |

---

## ♿ Accessibility Guidelines for Figma Projects

| Aspect                 | Rule                                        | Tool                          |
| :--------------------- | :------------------------------------------ | :---------------------------- |
| **Contrast Testing**   | Use “Able” or “Contrast” plugin.            | ≥ 4.5 : 1 ratio required.     |
| **Focus Simulation**   | Prototype tab order and focus indicators.   | Figma interactive preview.    |
| **Colorblind Preview** | Verify readability in colorblind filters.   | Built-in Figma simulator.     |
| **Reduced Motion**     | Avoid excessive movement or parallax.       | Design Review in motion mode. |
| **ARIA Mapping**       | Document roles in notes panel for dev team. | Manual annotation.            |

---

## 🧠 Review & Governance

All Figma files are governed by the **KFM Design Review Board**.
Changes must undergo peer review before merging updated exports.

```mermaid
flowchart LR
    A["Designer / Contributor"] --> B["Create or Update Figma File"]
    B --> C["Accessibility Audit"]
    C --> D["Review Board Approval\n(Design + Dev Signoff)"]
    D --> E["Export + Commit\n(README / Exports / Metadata)"]
    E --> F["Version Update in Source-Links.md"]
```

<!-- END OF MERMAID -->

---

## 🧩 Related Files

* [`README.md`](README.md) — Overview of all mockups & metadata structure
* [`../../ui-guidelines.md`](../../ui-guidelines.md) — UX & accessibility rules
* [`../../style-guide.md`](../../style-guide.md) — Color, typography, and layout tokens
* [`../../interaction-patterns.md`](../../interaction-patterns.md) — Behavior and input logic
* [`../../reviews/`](../../reviews/) — Design review logs and MCP compliance reports

---

<div align="center">

### 🔗 “A design without provenance is a rumor —

documenting the source makes creativity reproducible.”
**— Kansas Frontier Matrix Design Team**

</div>
