<div align="center">

# 🪶 Kansas Frontier Matrix — Excalidraw Sketches  
`docs/design/mockups/excalidraw/sketches/`

**Rapid · Visual · System Thinking**

</div>

---

## 🪶 Overview

The **Excalidraw Sketches** directory captures **early-stage visual design artifacts** for the Kansas Frontier Matrix (KFM).  
These are quick, conceptual diagrams—bridging **ideation → mockup → implementation**—used to explore complex interactions  
such as system architecture, temporal-spatial flows, and user interface dynamics before formal Figma or production builds.

Each sketch serves as a **visual hypothesis** within the MCP (Master Coder Protocol) framework—documenting thought  
process, decisions, and transitions between design phases.

---

## 📁 Directory Structure

```text
docs/design/mockups/excalidraw/sketches/
├── README.md                   # This spec (GitHub-safe)
├── *.excalidraw                # Raw editable sketches (JSON-based)
├── exports/                    # SVG/PNG exports for GitHub display
└── metadata/                   # Optional metadata (author, tags, refs)

Naming Convention:
YYYYMMDD_topic-shortdesc.excalidraw
Example → 20251006_timeline-scrubber-concept.excalidraw

⸻

🧭 Workflow
	1.	Create sketches using Excalidraw (web or desktop).
	2.	Export as both .excalidraw (source) and .svg (for GitHub/MkDocs rendering).
	•	Keep file size ≤ 1MB and centered on the canvas.
	•	Save exports in /exports/ using the same base filename.
	3.	Link each sketch to related design assets or specs:
	•	Figma components → /docs/design/mockups/figma/…
	•	Architecture diagrams → /docs/architecture/…
	•	UI/UX modules → /docs/design/mockups/components/…
	4.	Annotate in /metadata/ (JSON) with author, tags, date, and relationships.

⸻

🧾 Example Metadata

{
  "id": "timeline-scrubber-concept",
  "title": "Timeline Scrubber Interaction Concept",
  "author": "Kansas Frontier Matrix Design Team",
  "created": "2025-10-06",
  "related": [
    "docs/design/mockups/figma/components/navigation/README.md"
  ],
  "tags": ["timeline", "interaction", "ui", "design"],
  "description": "Explores early ideas for timeline scrubbing and playback within map synchronization context."
}


⸻

🖼️ Embedding Sketches in Docs

Embed sketches in documentation (e.g., README or SOP):

![Timeline Scrubber Concept](../excalidraw/sketches/exports/20251006_timeline-scrubber-concept.svg)

💡 Tip:
Use .svg for high-quality vector rendering on GitHub.
Avoid .png when scaling or transparency is required.

⸻

🔐 Provenance & Versioning
	•	.excalidraw files are tracked via Git LFS for binary storage optimization.
	•	Each sketch is versioned with a commit reference and optional metadata.
	•	Commit messages should include context (author, intent, related PRs).
	•	When a concept moves to production UI:
	•	Reference its sketch in the PR.
	•	Update the metadata field "status": "implemented".

⸻

🧩 Maintainer Notes
	•	Keep .excalidraw and .svg in sync for every update.
	•	Use sketches as visual companions in architecture, UI, and experiment docs.
	•	Archive outdated sketches under /archive/ after major design iterations.
	•	Include metadata for authorship, tags, and license (default: CC-BY 4.0).
	•	Prefer minimal annotation in drawings—details belong in metadata and commit logs.

⸻

⚖️ License

All sketches, exports, and metadata in this directory are released under:
Creative Commons Attribution 4.0 International (CC-BY 4.0)

Credit: Kansas Frontier Matrix Design Team · 2025

⸻

🗓️ Change Log

Date	Description
2025-10-06	Initial version — structure, metadata schema, embedding guide
2025-10-07	Formatted per KFM Markdown standards for GitHub compatibility

