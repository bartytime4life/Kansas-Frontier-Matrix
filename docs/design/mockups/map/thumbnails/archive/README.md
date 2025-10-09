<div align="center">

# 🗂️ Kansas Frontier Matrix — Archived Map Thumbnails  
`docs/design/mockups/map/thumbnails/archive/`

**Preserved · Traceable · Design Lineage**

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../../..)  
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../../../..)  
[![Archive Integrity](https://img.shields.io/badge/Archive-Integrity-blue)](../../../../../../../.github/workflows/stac-validate.yml)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../../../LICENSE)

</div>

---

## 🧭 Overview

This directory preserves **archived map thumbnails** — superseded versions of  
map previews, spatial visualizations, and design mockups used in the  
**Kansas Frontier Matrix (KFM)** documentation and web UI system.  

Each archived thumbnail maintains the **visual lineage** and **provenance trail**  
of earlier map designs, following the **Master Coder Protocol (MCP)**  
documentation-first principle of *reproducible visual history*.

Archiving ensures that the evolution of Kansas Frontier Matrix’s map  
interfaces — including historical datasets, thematic overlays, and  
UI configurations — remains accessible for research, audit, and continuity.

---

## 🗂️ Directory Layout

```text
docs/design/mockups/map/thumbnails/archive/
├── README.md                                  # This file
├── *.webp                                     # Archived thumbnails (optimized format)
├── *.png                                      # Legacy raster thumbnails (optional)
└── metadata/                                  # JSON metadata for archived versions
````

### 🧱 Naming Convention

`YYYYMMDD_map-topic-thumb_v#.webp`
**Example:** `20251009_map-treaty-boundaries-thumb_v1.webp`

---

## 🎯 Purpose

| Goal                     | Description                                                  |
| ------------------------ | ------------------------------------------------------------ |
| 🕓 **Historical Record** | Preserve legacy map thumbnails for traceability and lineage. |
| 🧩 **Documentation**     | Maintain historical states of KFM spatial compositions.      |
| 🧮 **Audit Trail**       | Enable version-to-version visual comparison and MCP review.  |
| 🧠 **Research**          | Support reproducibility and design provenance studies.       |

---

## 🧱 Archiving Workflow

### 1️⃣ Identify Outdated Thumbnail

Move replaced map previews into this archive.

```bash
mv thumbnails/20251009_map-treaty-boundaries-thumb.webp \
   archive/20251009_map-treaty-boundaries-thumb_v1.webp
```

### 2️⃣ Version the Filename

Add a version suffix (`_v1`, `_v2`, etc.) to indicate revision lineage.

### 3️⃣ Create or Update Metadata

Add a JSON record describing archival details to `/metadata/`.

```json
{
  "id": "map-treaty-boundaries-thumb_v1",
  "title": "Treaty Boundaries Thumbnail v1",
  "author": "Kansas Frontier Matrix Design Team",
  "created": "2025-10-09",
  "archived": "2025-10-12",
  "superseded_by": "../20251012_map-treaty-boundaries-thumb.webp",
  "reason": "Replaced with improved color scale and legend visibility.",
  "related": [
    "../../../../../architecture/README.md",
    "../../../icons/",
    "../../../layers/"
  ],
  "status": "archived",
  "license": "CC-BY-4.0"
}
```

### 4️⃣ Commit with Provenance

Include the archival reason in the commit message.

```bash
git add archive/20251009_map-treaty-boundaries-thumb_v1.webp
git add archive/metadata/20251009_map-treaty-boundaries-thumb_v1.json
git commit -m "Archived map thumbnail v1 (Treaty Boundaries) — superseded by new color map"
```

---

## 🧾 Metadata Conventions

| Field             | Description                            |
| ----------------- | -------------------------------------- |
| **id**            | Unique identifier with version suffix. |
| **title**         | Title and version of the map concept.  |
| **created**       | Original creation date.                |
| **archived**      | Date archived or replaced.             |
| **superseded_by** | Path to replacement or newer version.  |
| **reason**        | Explanation of revision.               |
| **related**       | Linked assets or documentation.        |
| **status**        | `archived` or `deprecated`.            |
| **license**       | Default: `CC-BY-4.0`.                  |

---

## 🖼️ Displaying Archived Thumbnails

Archived thumbnails may be shown in retrospectives or design logs
using **GitHub-safe collapsible sections** for space-efficient comparison.

```html
<details>
  <summary>2025-10-09 — Treaty Boundaries v1 (Archived)</summary>
  <img src="./20251009_map-treaty-boundaries-thumb_v1.webp" 
       width="360" alt="Archived Treaty Boundaries Map Thumbnail v1">
</details>
```

💡 *Tip:*
Collapsible galleries enable side-by-side visual comparison
without cluttering main documentation pages.

---

## 🧠 Design Lineage

Archived thumbnails capture the **progressive refinement** of KFM’s map UI and geospatial visualizations:

* Historical treaty and boundary designs.
* MapLibre configuration layouts (`layers.json`).
* Thematic overlays (hydrology, hazards, terrain).
* Visual changes in basemaps and legends.
* Evolution of timeline-map integration prototypes.

Every archived thumbnail forms part of a **continuous visual audit trail**
— ensuring full MCP reproducibility and temporal design traceability.

---

## 🔒 Provenance & Version Control

| Asset Type    | Format                          | Tracking | Notes                                      |
| ------------- | ------------------------------- | -------- | ------------------------------------------ |
| **Thumbnail** | `.webp` / `.png`                | Git      | Immutable historical snapshot.             |
| **Metadata**  | `.json`                         | Git      | Captures reason, status, and lineage.      |
| **Source**    | `.svg` / `.excalidraw` / `.png` | Git LFS  | Original design references for provenance. |

> 🧭 Never delete archived assets.
> Mark obsolete ones as `"deprecated"` in metadata but retain in the repository for provenance.

---

## ♿ Accessibility & Compliance

| Check                       | Requirement                | Status                         |
| --------------------------- | -------------------------- | ------------------------------ |
| **Contrast Ratio**          | ≥ 4.5 : 1                  | Verified via design QA plugin. |
| **Alt Text**                | Required                   | Recorded in metadata JSON.     |
| **Dual-Mode Compatibility** | Light/Dark mode visibility | Confirmed before archival.     |

Accessibility metadata ensures archived designs remain analyzable and accessible post-deprecation.

---

## ⚖️ License

All archived thumbnails and metadata are distributed under
**Creative Commons Attribution 4.0 International (CC-BY 4.0)**.
Attribution required when reused; commercial reuse permitted with credit.

**© 2025 Kansas Frontier Matrix Design Team**

---

## 🗓️ Change Log

| Date           | Description                                                          |
| -------------- | -------------------------------------------------------------------- |
| **2025-10-12** | Initial version — directory structure, workflow, and metadata guide. |
| **2025-10-13** | Added embedding and lineage documentation examples.                  |

---

<div align="center">

### Kansas Frontier Matrix — Documentation-First Design

**Preservation · Accessibility · Provenance Integrity**

</div>
