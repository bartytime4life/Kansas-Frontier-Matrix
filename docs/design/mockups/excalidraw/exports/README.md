<div align="center">

# 🖼️ Kansas Frontier Matrix — Excalidraw Exports  
`docs/design/mockups/excalidraw/exports/`

**Visual · Shareable · Reproducible Design Assets**

</div>

---

## 🪶 Overview

This directory contains **render-ready visual exports** of Excalidraw sketches used in the  
Kansas Frontier Matrix (KFM) design documentation system.  

Exports here are **derived artifacts** from the editable `.excalidraw` sketches  
(`docs/design/mockups/excalidraw/sketches/`) and are intended for embedding  
into READMEs, SOPs, and architecture documents across the repository.  

These files illustrate **early prototypes, workflows, and design concepts** — from navigation  
layouts and architecture diagrams to map/timeline interactions — following KFM’s  
documentation-first and MCP (Master Coder Protocol) principles.

---

## 📁 Directory Structure

```text
docs/design/mockups/excalidraw/exports/
├── README.md                         # This spec (GitHub-safe)
├── *.svg                             # Vector exports (preferred for all docs)
├── *.png                             # Raster exports (if vector is unsuitable)
└── thumbnails/                       # Compressed 400px-wide preview images

Naming Convention:
YYYYMMDD_topic-shortdesc.svg
Example → 20251007_system-architecture-concept.svg

⸻

🎯 Purpose

Goal	Description
🧭 Design Communication	Provide high-quality visual references for system, UI, and workflow concepts.
📚 Documentation Integration	Embed lightweight diagrams directly into Markdown files across /docs/.
🧩 Version Traceability	Maintain commit-linked visual checkpoints in the design workflow.
🪶 Accessibility	Offer visual summaries for readers who learn best through diagrammatic content.


⸻

🧱 Workflow

1. Source Sketch Creation

Create or update .excalidraw sketches in:
docs/design/mockups/excalidraw/sketches/

2. Export

From Excalidraw →
	•	“Export as SVG” (preferred)
	•	“Export as PNG” (if raster required)

Enable “Embed Scene Data” for traceability.
Ensure proper padding and centering for GitHub display.

3. Save & Name

Use the defined naming convention and save to this directory.
Each exported file should correspond to a metadata entry
in /docs/design/mockups/excalidraw/sketches/metadata/.

4. Thumbnail Generation (Optional)

Create a 400px-wide .webp or .png preview and place it in /thumbnails/.
See thumbnails/README.md for workflow details.

5. Commit with Provenance

Include the related metadata and describe changes clearly:

git add exports/20251007_navigation-flow.svg
git commit -m "Added navigation flow export (iteration 2) — linked to Figma node refs"


⸻

🧾 Example Metadata Linkage

Each export should have an accompanying .json file under /metadata/ that references it:

{
  "id": "system-architecture-concept",
  "title": "System Architecture Concept",
  "author": "Kansas Frontier Matrix Design Team",
  "created": "2025-10-07",
  "source": "../sketches/20251007_system-architecture-concept.excalidraw",
  "export": "exports/20251007_system-architecture-concept.svg",
  "thumbnail": "exports/thumbnails/20251007_system-architecture-concept-thumb.webp",
  "tags": ["architecture", "system", "ETL", "web-ui"],
  "status": "active",
  "license": "CC-BY-4.0"
}


⸻

🖼️ Embedding Exports in Docs

To embed a sketch export in another Markdown file:

![System Architecture Concept](../excalidraw/exports/20251007_system-architecture-concept.svg)

💡 Tip: SVG files scale crisply on all screens and load faster in GitHub and MkDocs.
Use .png only when vector text or strokes render incorrectly.

⸻

🧮 Integration with Documentation

Exports from this directory are commonly referenced in:

Document Type	Integration Purpose
architecture.md	Conceptual and data flow diagrams
README.md (component-level)	Visual UI previews and navigation layouts
sop.md	Step-by-step process visualizations
experiment.md	Visual representation of hypotheses and model flows
Figma → Docs	Bridging low-fidelity sketches to high-fidelity Figma mockups


⸻

🧩 Design Standards
	•	Maintain consistent visual hierarchy (titles, arrows, groupings).
	•	Use Excalidraw defaults: font Virgil, stroke width 1–2px, consistent margin (16–24px).
	•	Ensure accessibility: label key shapes, use color + text redundancy.
	•	Prefer neutral backgrounds (white or transparent).
	•	Avoid embedded raster screenshots inside vector exports.

⸻

🔐 Provenance & Versioning

Asset Type	Format	Tracking	Notes
Editable Sketch	.excalidraw	Git LFS	Stored in /sketches/
Exported Asset	.svg / .png	Git	Versioned directly
Metadata	.json	Git	Links export + provenance
Thumbnails	.webp / .png	Git	Used in galleries and indexes

All changes must be traceable to a commit ID, author, and design iteration.
Never overwrite existing exports—version them (-v2, -v3) when updating.

⸻

⚖️ License

All visual assets in this directory are released under
Creative Commons Attribution 4.0 International (CC-BY 4.0)

Credit: Kansas Frontier Matrix Design Team · 2025

⸻

🗓️ Change Log

Date	Description
2025-10-07	Initial version — structured for GitHub-safe rendering, metadata link
2025-10-08	Updated formatting and design standards alignment with KFM Markdown

