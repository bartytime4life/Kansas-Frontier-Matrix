<div align="center">

# 🗺️ Kansas Frontier Matrix — Map Thumbnails  
`docs/design/mockups/map/thumbnails/`

**Preview · Lightweight · Spatial Summaries**

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../..)  
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../..)  
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../../.github/workflows/stac-validate.yml)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../LICENSE)

</div>

---

## 🧭 Overview

This directory stores **map thumbnails** — lightweight, optimized visual previews representing key map designs,  
thematic layers, or UI compositions within the **Kansas Frontier Matrix (KFM)** design system.

These thumbnails are used in:
- 📘 Documentation (READMEs, architecture diagrams, and experiments)  
- 🌐 Web UI mockups and preview panels  
- 🧩 MCP documentation galleries and design indexes  

Each thumbnail provides a **quick spatial summary**, improving comprehension and navigation without the overhead of rendering large interactive maps.

All thumbnails comply with the **Master Coder Protocol (MCP)**: reproducible, traceable, and version-controlled.

---

## 🗂️ Directory Layout

```text
docs/design/mockups/map/thumbnails/
├── README.md                          # This file
├── *.webp                             # Optimized thumbnails (preferred format)
├── *.png                              # Fallback raster format (transparency supported)
├── archive/                           # Legacy or superseded thumbnails
└── metadata/                          # JSON metadata describing each thumbnail
````

### 🧱 Naming Convention

`YYYYMMDD_map-topic-thumb.webp`
**Example:** `20251012_map-layers-overview-thumb.webp`

---

## 🎯 Purpose

| Goal                   | Description                                                                |
| ---------------------- | -------------------------------------------------------------------------- |
| 🗺️ **Visual Preview** | Static image preview for map-based KFM components.                         |
| ⚙️ **Documentation**   | Embedded in READMEs, SOPs, and experiments for reference.                  |
| 🧩 **Integration**     | Linked to map configurations (e.g., `layers.json`, `stac/catalog.json`).   |
| 🧠 **Comprehension**   | Provides immediate context to spatial layouts and layer structure.         |
| 🧮 **Provenance**      | Tracks lineage between design concepts, exports, and live implementations. |

---

## 🧱 Workflow for Creating Thumbnails

### 1️⃣ Generate a Map Snapshot

Capture from the **MapLibre viewer**, **Figma wireframe**, or **KML/KMZ overlay**.
Save as a lossless format (PNG preferred).

### 2️⃣ Resize and Optimize

Resize for web use (max width: 480 px).

```bash
magick 20251012_map-layers-overview.png -resize 480x480 \
  thumbnails/20251012_map-layers-overview-thumb.webp
```

### 3️⃣ Compress for Web

Reduce file size using compression utilities.

```bash
cwebp -q 80 thumbnails/20251012_map-layers-overview-thumb.webp \
  -o thumbnails/20251012_map-layers-overview-thumb.webp
```

### 4️⃣ Add Metadata

Create a `.json` record under `/metadata/` documenting provenance, author, and links.

### 5️⃣ Commit with Provenance

```bash
git add thumbnails/20251012_map-layers-overview-thumb.webp \
        metadata/20251012_map-layers-overview-thumb.json
git commit -m "Add map thumbnail for Map Layers Overview (linked to layers.json v1.3)"
```

---

## 🧾 Example Metadata Record

**File:** `metadata/20251012_map-layers-overview-thumb.json`

```json
{
  "id": "map-layers-overview",
  "title": "Map Layers Overview",
  "author": "Kansas Frontier Matrix Design Team",
  "created": "2025-10-12",
  "source": "../exports/20251012_map-layers-overview.png",
  "thumbnail": "../thumbnails/20251012_map-layers-overview-thumb.webp",
  "related": [
    "../../map/icons/",
    "../../map/layers/",
    "../../../architecture/README.md"
  ],
  "tags": ["map", "layers", "stac", "overview"],
  "status": "active",
  "license": "CC-BY-4.0"
}
```

Metadata records are validated via JSON Schema (`metadata/schema/thumbnail.schema.json`)
and checked automatically during CI/CD builds.

---

## 🖼️ Embedding Thumbnails in Documentation

You can embed thumbnails in Markdown as static or linked previews.

```markdown
<a href="../exports/20251012_map-layers-overview.png">
  <img src="../thumbnails/20251012_map-layers-overview-thumb.webp"
       width="380" alt="Map Layers Overview Preview">
</a>
```

> 💡 **Tip:** Use clickable thumbnails that link to full-resolution exports to balance clarity and performance.

---

## 🎨 Design & Formatting Standards

| Attribute       | Requirement                          | Notes                                     |
| --------------- | ------------------------------------ | ----------------------------------------- |
| **Max Width**   | ≤ 480 px                             | Consistent scale across docs.             |
| **File Format** | `.webp` (preferred), `.png` fallback | WebP = better compression ratio.          |
| **Background**  | Transparent or neutral gray          | Avoid bold or saturated tones.            |
| **File Size**   | ≤ 300 KB                             | Optimized for GitHub rendering.           |
| **License**     | CC-BY 4.0                            | Attribution required for reuse.           |
| **Metadata**    | Required                             | Ensures traceability and reproducibility. |
| **Theme**       | Dual-mode compatible                 | Visible in light and dark themes.         |

---

## 🧩 Integration with Documentation

| Context           | Example Usage                                          |
| ----------------- | ------------------------------------------------------ |
| `architecture.md` | Overview snapshots of system or map composition.       |
| `README.md`       | Inline galleries linking to design mockups.            |
| `experiment.md`   | Visual summaries of analysis results or data overlays. |
| `SOP.md`          | Step-by-step workflow illustrations.                   |
| STAC Docs         | Previews for collections and temporal datasets.        |

---

## 🔐 Provenance & Versioning

| Artifact      | Type             | Tracking | Notes                           |
| ------------- | ---------------- | -------- | ------------------------------- |
| **Thumbnail** | `.webp` / `.png` | Git      | Stored under `/thumbnails/`.    |
| **Metadata**  | `.json`          | Git      | Records lineage and references. |
| **Source**    | `.png` / `.svg`  | Git LFS  | For large design exports.       |

> 🧭 **Do not overwrite** existing thumbnails. Use date or version suffixes (`-v2`, `-v3`)
> to maintain a traceable visual history of design evolution.

---

## ⚖️ License

All thumbnails and metadata are licensed under
**Creative Commons Attribution 4.0 International (CC-BY 4.0)**.
Attribution required; commercial reuse permitted with credit.

**© 2025 Kansas Frontier Matrix Design Team**

---

## 🗓️ Change Log

| Date           | Description                                                                           |
| -------------- | ------------------------------------------------------------------------------------- |
| **2025-10-12** | Initial version — added structure, metadata, and embedding standards.                 |
| **2025-10-13** | Enhanced with integration examples, compression workflow, and accessibility guidance. |

---

<div align="center">

### Kansas Frontier Matrix — Documentation-First Design

**Spatial Clarity · Lightweight Documentation · Provenance by Design**

</div>
