<div align="center">

# 🗺️ Kansas Frontier Matrix — Map Thumbnails  
`docs/design/mockups/map/thumbnails/`

**Preview · Lightweight · Spatial Summaries**

</div>

---

## 🧭 Overview

This directory stores **map thumbnails** — lightweight, downscaled previews of  
map designs, thematic layers, and UI concepts created for the  
**Kansas Frontier Matrix (KFM)** project.  

These thumbnails provide **quick visual summaries** for use in READMEs,  
architecture documents, and design indexes, enabling fast recognition of  
map-based components without loading full-resolution maps or live viewers.  

Each thumbnail is a compressed visual reference linked to its corresponding  
map concept or configuration file (`layers.json`, `app.config.json`, etc.),  
supporting the KFM documentation-first and reproducibility ethos of the  
**Master Coder Protocol (MCP)**.

---

## 📁 Directory Structure

```text
docs/design/mockups/map/thumbnails/
├── README.md                          # This spec (GitHub-safe)
├── *.webp                             # Primary thumbnail format (preferred)
├── *.png                              # Fallback raster format (if transparency needed)
├── archive/                           # Deprecated or superseded thumbnails
└── metadata/                          # JSON metadata files describing each thumbnail

Naming Convention:
YYYYMMDD_map-topic-thumb.webp
Example → 20251012_map-layers-overview-thumb.webp

⸻

🎯 Purpose

Goal	Description
🗺️ Visual Preview	Serve as static image previews for map-based KFM components
⚙️ Documentation	Embedded in READMEs, design docs, and experiment reports
🧩 Integration	Linked to map configurations (e.g., layers.json, stac/collections/)
🧠 Comprehension	Help readers quickly grasp spatial composition or theming
🧮 Provenance	Provide traceable link between design concept and implementation


⸻

🧱 Workflow for Creating Thumbnails

1. Generate a Map Snapshot

Capture a relevant view from the live MapLibre interface, Figma mockup, or exported KML/KMZ layer.
Save as a lossless image (PNG, WebP preferred).

2. Resize and Optimize

Create a small, lightweight thumbnail (max width: 480 px) for use in documentation.

# Example using ImageMagick
magick 20251012_map-layers-overview.png -resize 480x480 thumbnails/20251012_map-layers-overview-thumb.webp

3. Compress for Web Use

Use cwebp or oxipng to reduce file size while preserving clarity.

cwebp -q 80 20251012_map-layers-overview-thumb.webp -o 20251012_map-layers-overview-thumb.webp

4. Add Metadata

Create a matching JSON metadata record (see example below) in the /metadata/ subfolder.

5. Commit with Provenance

Include thumbnail, metadata, and source links in the commit message.

git add thumbnails/20251012_map-layers-overview-thumb.webp metadata/20251012_map-layers-overview-thumb.json
git commit -m "Added thumbnail preview for Map Layers Overview (linked to layers.json v1.3)"


⸻

🧾 Example Metadata File

metadata/20251012_map-layers-overview-thumb.json

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


⸻

🖼️ Embedding Thumbnails in Documentation

Embed map thumbnails in Markdown or MkDocs pages as visual previews:

<a href="../exports/20251012_map-layers-overview.png">
  <img src="../thumbnails/20251012_map-layers-overview-thumb.webp" 
       width="380" alt="Map Layers Overview Preview">
</a>

💡 Tip:
Wrap thumbnails in clickable links to their full-size exports for quick visual navigation
without embedding large images directly in documentation.

⸻

🎨 Design & Formatting Standards

Attribute	Requirement	Notes
Max Width	≤480 px	Ensures consistent visual scale across docs
File Format	.webp (preferred), .png (fallback)	WebP recommended for compression
Background	Transparent or neutral gray	Avoid strong background colors
File Size	≤300 KB	Enables fast GitHub rendering
License	CC-BY 4.0	Attribution required for reuse
Metadata	Required	Provides traceability and linkage
Theme	Neutral, light/dark compatible	Ensure visible edges in both modes


⸻

🧩 Integration with Documentation

Context	Use
architecture.md	Overview snapshots of system or layer composition
README.md	Inline gallery previews for navigation, design, or mockups
experiment.md	Visual result logs or test map captures
SOP.md	Step-by-step illustrations for spatial workflows
STAC Docs	Thumbnail previews of map collections or temporal datasets


⸻

🔐 Provenance & Versioning

Artifact	Type	Tracking	Notes
Thumbnail	.webp / .png	Git	Stored in /thumbnails/
Metadata	.json	Git	Captures author, linkage, and version context
Source	.png / .svg	Git LFS	Large or full-resolution maps (optional)

Do not overwrite existing thumbnails — version them by date or suffix (-v2, -v3)
to preserve the design lineage and change history.

⸻

⚖️ License

All thumbnails and metadata are distributed under
Creative Commons Attribution 4.0 International (CC-BY 4.0)

Credit: Kansas Frontier Matrix Design Team · 2025

Attribution required when reused; commercial use permitted with credit.

⸻

🗓️ Change Log

Date	Description
2025-10-12	Initial version — added structure, metadata, and embedding guidelines
2025-10-13	Enhanced with integration examples and compression workflow