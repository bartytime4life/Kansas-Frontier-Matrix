<div align="center">

# 🖼️ Kansas Frontier Matrix — Sketch Thumbnails  
`docs/design/mockups/excalidraw/sketches/exports/thumbnails/`

**Preview · Organized · Lightweight Visual References**

</div>

---

## 🧭 Overview

This directory contains **thumbnail previews** of Excalidraw design sketches.  
Each thumbnail provides a **lightweight visual snapshot** of a design concept — used for documentation indexes, galleries, and quick browsing across the Kansas Frontier Matrix (KFM) design system.

These images are **compressed derivatives** of the original Excalidraw exports found in  
`docs/design/mockups/excalidraw/sketches/exports/`.

They help readers and contributors quickly identify visual assets without loading large `.excalidraw` or `.svg` files.

---

## 📁 Directory Structure

```text
docs/design/mockups/excalidraw/sketches/exports/thumbnails/
├── README.md                            # This spec (GitHub-safe)
├── *.webp                               # Optimized thumbnails (preferred)
├── *.png                                # Fallback raster format (optional)
└── archive/                             # Deprecated or older thumbnail versions

Naming Convention:
YYYYMMDD_topic-shortdesc-thumb.webp
Example → 20251008_timeline-interaction-thumb.webp

⸻

🎯 Purpose

Goal	Description
🧭 Quick Identification	Provide lightweight previews for browsing or gallery views
🧩 Integration	Used in indexes, READMEs, and experiment logs as inline visuals
🖼️ Documentation	Linked in metadata to represent sketches visually
⚙️ Automation	Can be used by build scripts to auto-generate visual directories


⸻

🧱 Workflow for Creating Thumbnails

1. Locate Source File

Use the parent .svg export from
docs/design/mockups/excalidraw/sketches/exports/.

2. Convert to Thumbnail

Resize and compress the image to a web-optimized format:

# Using ImageMagick (recommended)
magick 20251008_timeline-interaction.svg -resize 400x400 thumbnails/20251008_timeline-interaction-thumb.webp

	•	Recommended width: ≤400px (maintain aspect ratio)
	•	Format: .webp preferred, .png allowed for transparency

3. Optimize File Size

Compress using lossless tools (if needed):

cwebp -q 80 input.png -o output.webp

4. Save & Name

Follow the naming convention strictly and store inside /thumbnails/.

5. Link in Metadata

Update the metadata JSON in
docs/design/mockups/excalidraw/sketches/metadata/
to include the new thumbnail path.

⸻

🧾 Example Metadata Reference

{
  "id": "timeline-interaction",
  "title": "Timeline Interaction Concept",
  "author": "Kansas Frontier Matrix Design Team",
  "created": "2025-10-08",
  "source": "../20251008_timeline-interaction.excalidraw",
  "export": "../exports/20251008_timeline-interaction.svg",
  "thumbnail": "../exports/thumbnails/20251008_timeline-interaction-thumb.webp",
  "tags": ["timeline", "ui", "interaction"],
  "status": "active",
  "license": "CC-BY-4.0"
}


⸻

🖥️ Embedding Thumbnails in Docs

Use thumbnails for light, fast previews within documentation:

<a href="../exports/20251008_timeline-interaction.svg">
  <img src="../exports/thumbnails/20251008_timeline-interaction-thumb.webp" 
       width="280" alt="Timeline Interaction Sketch">
</a>

💡 Tip:
Wrap thumbnails in an anchor tag linking to the full export for a clean click-to-expand experience on GitHub or MkDocs.

⸻

🧩 Thumbnail Standards

Attribute	Requirement	Description
Format	.webp (preferred)	Lightweight and efficient compression
Max Width	400 px	Consistent size across all previews
Background	White or transparent	Maintain consistency with exports
Style	Uncluttered, labeled, readable	Avoid small unreadable text
File Size	≤200 KB	Ensures fast GitHub/MkDocs load times


⸻

🔐 Provenance & Versioning

Type	Source	Tracking	Notes
Thumbnail	Derived from export	Git	Commit with reference to parent export
Export	Derived from .excalidraw	Git LFS	Editable master version
Metadata	JSON	Git	Links thumbnail, export, and sketch context

Never overwrite thumbnails. Use new versions (e.g., -v2) when updating visuals to maintain historical lineage.

⸻

⚖️ License

All assets in this directory are distributed under
Creative Commons Attribution 4.0 International (CC-BY 4.0)

Credit: Kansas Frontier Matrix Design Team · 2025

⸻

🗓️ Change Log

Date	Description
2025-10-08	Initial version — standardized workflow, metadata, and embedding guide
2025-10-09	Updated formatting for GitHub-safe rendering and MCP compliance