<div align="center">

# 🗂️ Kansas Frontier Matrix — Archived Thumbnails  
`docs/design/mockups/excalidraw/sketches/exports/thumbnails/archive/`

**Preserved · Versioned · Historical Visual References**

</div>

---

## 🧭 Overview

This directory contains **archived thumbnail previews** of deprecated or superseded Excalidraw sketches.  
Each file represents a **previous iteration** of a design concept, preserved for provenance, reference, and  
historical documentation under the Kansas Frontier Matrix (KFM) design and documentation framework.

Archiving ensures that older visual assets remain accessible for research, audit, or educational use, even  
after the active versions have been replaced by updated sketches or exports.

---

## 📁 Directory Structure

```text
docs/design/mockups/excalidraw/sketches/exports/thumbnails/archive/
├── README.md                                # This document (GitHub-safe)
├── *.webp                                   # Archived web-optimized thumbnails
├── *.png                                    # Optional legacy or fallback raster images
└── metadata/                                # Optional version history metadata per sketch

Naming Convention:
YYYYMMDD_topic-shortdesc-thumb_v#.webp
Example → 20250920_navigation-flow-thumb_v1.webp

⸻

🎯 Purpose

Goal	Description
🕓 Preserve History	Retain older visual iterations for provenance and design lineage
🧩 Reference Context	Allow comparison of evolving design ideas across versions
🧮 Data Provenance	Ensure traceability from current exports to historical ones
🧠 Research Continuity	Provide a visual audit trail for long-term documentation and MCP review


⸻

🧱 Archiving Workflow

1. Identify Outdated Thumbnail

When a sketch, export, or thumbnail is superseded (e.g., new iteration in /exports/thumbnails/), move the old file here.

2. Rename & Version

Increment the version number at the end of the filename:

mv 20251006_navigation-flow-thumb.webp archive/20251006_navigation-flow-thumb_v1.webp

3. Update Metadata

Create or update a corresponding JSON file in /metadata/:

{
  "id": "navigation-flow-thumb_v1",
  "title": "Navigation Flow Thumbnail v1",
  "author": "Kansas Frontier Matrix Design Team",
  "created": "2025-10-06",
  "status": "archived",
  "superseded_by": "../20251008_navigation-flow-thumb.webp",
  "reason": "Replaced by updated sketch layout",
  "license": "CC-BY-4.0"
}

4. Commit with Provenance

Commit with a message describing the archival reason and reference to replacement:

git add archive/20251006_navigation-flow-thumb_v1.webp
git commit -m "Archived navigation flow thumbnail v1 — superseded by v2 (20251008)"


⸻

🧾 Metadata Conventions

Archived metadata should include:

Field	Description
id	Unique identifier with version suffix
title	Sketch title and version
created	Original creation date
archived	Date moved to archive
superseded_by	Link to the replacement file
reason	Why the version was replaced (clarity, updated mockup, etc.)
license	Default: CC-BY 4.0


⸻

🖼️ Embedding Archived Versions

Archived thumbnails should not be embedded in active documentation except in retrospectives or design history logs.

To embed in a visual changelog or timeline:

<details>
  <summary>2025-09-20 — Navigation Flow v1 (archived)</summary>
  <img src="./20250920_navigation-flow-thumb_v1.webp" width="320" alt="Navigation Flow v1 Thumbnail (Archived)">
</details>

💡 Tip: Use collapsible <details> blocks to avoid cluttering primary documentation pages.

⸻

🔐 Provenance & Version Control

Type	Source	Tracking	Notes
Archived Thumbnail	.webp / .png	Git	Retained for visual history
Metadata	.json	Git	Describes archival status and lineage
Replacement Export	.svg / .png	Git	Lives in parent /exports/ directory

All archives remain under version control for auditability.
Never delete archived files — instead, mark them as deprecated in metadata if obsolete.

⸻

⚖️ License

All archived thumbnails and metadata are released under
Creative Commons Attribution 4.0 International (CC-BY 4.0)

Credit: Kansas Frontier Matrix Design Team · 2025

⸻

🗓️ Change Log

Date	Description
2025-10-09	Initial version — directory structure, workflow, and metadata schema
2025-10-10	Updated per KFM Markdown standard and added embedding guide