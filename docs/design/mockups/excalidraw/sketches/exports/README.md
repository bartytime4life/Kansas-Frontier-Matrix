<div align="center">

# 🖼️ Kansas Frontier Matrix — Excalidraw Exports  
`docs/design/mockups/excalidraw/sketches/exports/`

**Visual · Shareable · Versioned Design Outputs**

</div>

---

## 🧭 Overview

This directory contains **exported visual assets** from the Excalidraw sketches used throughout the  
Kansas Frontier Matrix (KFM) design process.  

Exports in this folder are **render-ready** versions of editable Excalidraw sketches (`.excalidraw`) and are  
used directly in documentation, READMEs, and MCP experiment logs across the repository.  

Each export represents a **versioned design artifact** — a visual checkpoint in the iterative design flow  
from ideation → system architecture → Figma → implementation.

---

## 📁 Directory Structure

```text
docs/design/mockups/excalidraw/sketches/exports/
├── README.md                        # This spec (GitHub-safe)
├── *.svg                            # Vector exports (preferred for docs)
├── *.png                            # Optional raster exports (use sparingly)
└── thumbnails/                      # Reduced-size images for previews or listings

Naming Convention:
YYYYMMDD_topic-shortdesc.svg
Example → 20251006_navigation-flow.svg

⸻

🧩 Purpose
	•	Serve as reference visuals for documentation and design review.
	•	Provide lightweight, portable alternatives to .excalidraw files for rendering in GitHub.
	•	Ensure version control of each visual design milestone through clean SVG exports.
	•	Link sketches to their corresponding Excalidraw sources and metadata for provenance.

⸻

🧱 Workflow for Creating Exports
	1.	Open Source Sketch
Edit the .excalidraw file in /docs/design/mockups/excalidraw/sketches/.
	2.	Export
From Excalidraw → “Export as SVG” (recommended) or “Export as PNG” (if raster needed).
	•	Enable “Embed Scene” metadata when possible for traceability.
	•	Keep aspect ratio consistent with design intent (avoid cropping text).
	3.	Name & Place
Save with proper naming format → YYYYMMDD_topic-shortdesc.svg.
Place in this directory (/exports/) and update corresponding metadata in /metadata/.
	4.	Commit with Context
Include a short message explaining the change and reference related issue/PR.
Example:

git add exports/20251007_timeline-wireframe.svg
git commit -m "Added updated timeline wireframe (iteration 2) – linked to Figma nodes"


	5.	Reference in Docs
Embed visuals in markdown files using relative paths:

![Timeline Wireframe](../exports/20251007_timeline-wireframe.svg)



⸻

🧾 Example Metadata Linkage

Each exported file corresponds to a metadata JSON entry under
docs/design/mockups/excalidraw/sketches/metadata/.

Example: metadata/20251006_navigation-flow.json

{
  "id": "navigation-flow",
  "title": "Navigation Flow — Initial Concept",
  "author": "Kansas Frontier Matrix Design Team",
  "created": "2025-10-06",
  "source": "../20251006_navigation-flow.excalidraw",
  "export": "exports/20251006_navigation-flow.svg",
  "tags": ["navigation", "timeline", "map", "interaction"],
  "related": [
    "docs/design/mockups/figma/components/navigation/README.md"
  ],
  "status": "active",
  "license": "CC-BY-4.0"
}


⸻

🎨 Best Practices
	•	Prefer SVG over PNG for all documentation — vectors scale cleanly and load faster.
	•	Keep exports under 2MB; simplify excessive node counts in Excalidraw if needed.
	•	Use clear labels and groupings for readability when embedding in technical docs.
	•	Include version markers (date or iteration tag) on sketches if multiple revisions exist.
	•	Ensure consistent visual style across all exports:
	•	Font: Virgil or Architect’s Daughter (Excalidraw defaults)
	•	Stroke Width: 1–2px
	•	Padding: 16–24px margin

⸻

🧮 Integration with Documentation

Exported sketches appear in:

Document Type	Integration Purpose
README.md files	Visual summaries for system components
architecture.md	Conceptual or flow diagrams
sop.md	Step-by-step procedural illustrations
experiment.md	Visual hypotheses or workflow comparisons
Figma/Design Sync	Image assets for referencing high-fidelity mockups


⸻

🕓 Provenance & Version Control

Artifact Type	Format	Tracking Method
Editable Sketch	.excalidraw	Git LFS (binary)
Exported Asset	.svg / .png	Git (direct versioning)
Metadata	.json	Git (text-based diff tracking)

All assets include provenance via commit SHA and metadata references.
When a design evolves, do not overwrite — create a new export file (increment date or add -v2).

⸻

⚖️ License

All assets in this folder are released under CC-BY 4.0 International License
unless otherwise noted in metadata.

Credit: Kansas Frontier Matrix Design Team · 2025

⸻

🗓️ Change Log

Date	Description
2025-10-06	Initial version — structure, metadata example, best practices
2025-10-07	Standardized format per KFM Markdown spec; added provenance tips
