<div align="center">

# 🗂️ Kansas Frontier Matrix — Archived Map Thumbnails  
`docs/design/mockups/map/thumbnails/archive/`

**Preserved · Traceable · Design Lineage**

</div>

---

## 🧭 Overview

This directory stores **archived map thumbnails** — previous iterations of  
map design previews and spatial compositions for the **Kansas Frontier Matrix (KFM)**.  

Each file represents a **superseded or deprecated visual artifact**, retained to  
maintain the project’s full **provenance and design evolution record** under the  
**Master Coder Protocol (MCP)** documentation-first philosophy.  

These archived thumbnails provide visual history for how map and layer designs  
have evolved across the system’s development lifecycle.

---

## 📁 Directory Structure

```text
docs/design/mockups/map/thumbnails/archive/
├── README.md                                  # This documentation (GitHub-safe)
├── *.webp                                     # Archived thumbnails (optimized format)
├── *.png                                      # Legacy raster thumbnails (optional)
└── metadata/                                  # Metadata describing archived versions

Naming Convention:
YYYYMMDD_map-topic-thumb_v#.webp
Example → 20251009_map-treaty-boundaries-thumb_v1.webp

⸻

🎯 Purpose

Goal	Description
🕓 Historical Record	Preserve superseded thumbnails for reference and lineage
🧩 Documentation	Maintain access to previous visual states of KFM maps
🧮 Audit Trail	Enable visual diffing of map designs between iterations
🧠 Research	Support design analysis, MCP reviews, and reproducibility studies


⸻

🧱 Archiving Workflow

1. Identify Outdated Thumbnail

When a map preview or design snapshot is updated or replaced, move the previous file here.

mv thumbnails/20251009_map-treaty-boundaries-thumb.webp archive/20251009_map-treaty-boundaries-thumb_v1.webp

2. Version the Filename

Add a version suffix (_v1, _v2, etc.) to track revision history.

3. Create or Update Metadata

Each archived thumbnail requires a metadata file under /metadata/.

{
  "id": "map-treaty-boundaries-thumb_v1",
  "title": "Treaty Boundaries Thumbnail v1",
  "author": "Kansas Frontier Matrix Design Team",
  "created": "2025-10-09",
  "archived": "2025-10-12",
  "superseded_by": "../20251012_map-treaty-boundaries-thumb.webp",
  "reason": "Replaced by new treaty boundaries map overlay with improved color scale.",
  "related": [
    "../../../../../architecture/README.md",
    "../../../icons/",
    "../../../layers/"
  ],
  "status": "archived",
  "license": "CC-BY-4.0"
}

4. Commit with Provenance

Include the archival reason in the commit message:

git add archive/20251009_map-treaty-boundaries-thumb_v1.webp
git add archive/metadata/20251009_map-treaty-boundaries-thumb_v1.json
git commit -m "Archived map thumbnail v1 (treaty boundaries) — superseded by updated color map"


⸻

🧾 Metadata Conventions

Field	Description
id	Unique identifier with version suffix
title	Map concept title and version
created	Original thumbnail creation date
archived	Date archived or replaced
superseded_by	Path to replacement thumbnail
reason	Explanation of archival or revision
related	Linked components (icons, layers, documents)
status	"archived" or "deprecated"
license	Licensing info (default: CC-BY-4.0)


⸻

🖼️ Displaying Archived Thumbnails in Docs

Archived thumbnails can be embedded in changelogs or retrospectives using
GitHub-safe collapsible details blocks:

<details>
  <summary>2025-10-09 — Treaty Boundaries v1 (Archived)</summary>
  <img src="./20251009_map-treaty-boundaries-thumb_v1.webp" width="360" alt="Archived Treaty Boundaries Map Thumbnail v1">
</details>

💡 Tip: Collapsible archives allow visual comparison without cluttering main documentation pages.

⸻

🧮 Design Lineage

Archived thumbnails document the evolution of KFM map design.
This helps maintain visual continuity between versions of:
	•	MapLibre configurations (layers.json)
	•	Historical map overlays
	•	Treaty and boundary maps
	•	Thematic datasets (climate, hazards, hydrology)
	•	UI design prototypes (timeline, controls, legends)

Each archived thumbnail represents a concrete visual state of the system
and supports reproducibility and visual traceability in documentation.

⸻

🔐 Provenance & Version Control

Asset Type	Format	Tracking	Notes
Thumbnail	.webp / .png	Git	Preserved as visual evidence of previous map versions
Metadata	.json	Git	Describes archival reason and links to successor
Source	.svg / .png / .excalidraw	Git LFS	Original design sources referenced for lineage

Never delete archived thumbnails — they are part of the official project record.
Instead, mark them as "deprecated" in metadata when obsolete.

⸻

⚖️ License

All archived thumbnails and metadata are distributed under
Creative Commons Attribution 4.0 International (CC-BY 4.0)

Credit: Kansas Frontier Matrix Design Team · 2025

Attribution required when reused or referenced; commercial use permitted with credit.

⸻

🗓️ Change Log

Date	Description
2025-10-12	Initial version — directory structure, workflow, and metadata guide
2025-10-13	Added embedding examples and lineage documentation section
