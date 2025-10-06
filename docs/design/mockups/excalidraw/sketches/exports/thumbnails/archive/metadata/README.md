<div align="center">

# 🗃️ Kansas Frontier Matrix — Archived Thumbnail Metadata  
`docs/design/mockups/excalidraw/sketches/exports/thumbnails/archive/metadata/`

**Traceable · Documented · Provenance-Driven**

</div>

---

## 🧭 Overview

This directory stores **metadata files** (`.json`) that describe the archived thumbnail assets located in  
`docs/design/mockups/excalidraw/sketches/exports/thumbnails/archive/`.  

Each JSON file records **provenance, version history, and archival context** for a previously active thumbnail.  
These records enable **data lineage tracking** across iterations of Excalidraw sketches, ensuring that the Kansas Frontier Matrix (KFM) maintains full historical traceability under the **Master Coder Protocol (MCP)** framework.

Metadata in this directory supports visual version control — documenting **when**, **why**, and **by whom** a thumbnail was replaced or deprecated.

---

## 📁 Directory Structure

```text
docs/design/mockups/excalidraw/sketches/exports/thumbnails/archive/metadata/
├── README.md                             # This specification (GitHub-safe)
├── *.json                                # Individual metadata records (one per archived thumbnail)
└── schema/                               # Optional JSON Schema validators (for automated checks)

Naming Convention:
YYYYMMDD_topic-shortdesc-thumb_v#.json
Example → 20250920_navigation-flow-thumb_v1.json

⸻

🧩 Purpose

Objective	Description
🧠 Documentation	Preserve detailed metadata about archived thumbnails
🧭 Provenance	Record relationships between old and new visual assets
🧮 Validation	Enable automated CI/CD validation of metadata structure
🧱 Audit Trail	Provide full transparency for design version transitions
🧩 Interoperability	Integrate with STAC/DCAT-style metadata pipelines and graph nodes


⸻

🧾 Example Metadata Template

Each metadata file follows a standardized JSON schema to ensure consistency and interoperability.

{
  "id": "navigation-flow-thumb_v1",
  "title": "Navigation Flow Thumbnail v1",
  "author": "Kansas Frontier Matrix Design Team",
  "created": "2025-09-20",
  "archived": "2025-10-09",
  "superseded_by": "../../20251008_navigation-flow-thumb.webp",
  "reason": "Design iteration improved timeline-marker grouping and color scheme.",
  "source": "../../20250920_navigation-flow-thumb.webp",
  "related": [
    "../../../../../sketches/metadata/20250920_navigation-flow.json"
  ],
  "tags": ["thumbnail", "archive", "navigation", "ui"],
  "status": "archived",
  "license": "CC-BY-4.0"
}


⸻

🧱 JSON Schema (for optional validation)

Stored under:
docs/design/mockups/excalidraw/sketches/exports/thumbnails/archive/metadata/schema/thumbnail_metadata.schema.json

Example structure:

{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Archived Thumbnail Metadata",
  "type": "object",
  "properties": {
    "id": { "type": "string" },
    "title": { "type": "string" },
    "author": { "type": "string" },
    "created": { "type": "string", "format": "date" },
    "archived": { "type": "string", "format": "date" },
    "superseded_by": { "type": "string" },
    "reason": { "type": "string" },
    "source": { "type": "string" },
    "related": { "type": "array", "items": { "type": "string" } },
    "tags": { "type": "array", "items": { "type": "string" } },
    "status": { "enum": ["archived", "deprecated"] },
    "license": { "type": "string" }
  },
  "required": ["id", "title", "author", "created", "archived", "license"]
}


⸻

🧮 Workflow for Archiving Metadata
	1.	Identify Obsolete Thumbnail
When a new thumbnail version is added, mark the old one as archived.
	2.	Create Metadata Record
Duplicate this template and fill in the metadata fields accurately.
	3.	Validate Schema
Run a JSON Schema validation to ensure structure integrity:

python -m json.tool < metadata/20250920_navigation-flow-thumb_v1.json
jsonschema -i metadata/20250920_navigation-flow-thumb_v1.json schema/thumbnail_metadata.schema.json


	4.	Commit with Provenance

git add metadata/20250920_navigation-flow-thumb_v1.json
git commit -m "Archived thumbnail metadata — navigation flow v1 superseded by v2"



⸻

🔗 Integration with STAC & Knowledge Graph

These metadata files can be linked to STAC or Neo4j graph entries as provenance nodes:

Relation	Description
isVersionOf	Connects archived thumbnail to its active successor
derivedFrom	Links to the original .excalidraw sketch
replacedBy	Specifies the new asset superseding the archived version
hasLicense	Embeds rights and attribution in the graph metadata

This ensures that visual lineage is queryable within the broader KFM knowledge ecosystem.

⸻

🧩 Metadata Best Practices
	•	Maintain ISO8601 date formats (YYYY-MM-DD).
	•	Use relative paths (../../) for internal references to avoid broken links.
	•	Include at least one "reason" or "comment" for archival.
	•	Validate with the JSON Schema before merging changes.
	•	Include "license": "CC-BY-4.0" unless otherwise specified.
	•	Use descriptive "tags" (max 5 per file) for searchability.

⸻

⚖️ License

All metadata in this directory is licensed under
Creative Commons Attribution 4.0 International (CC-BY 4.0)

Credit: Kansas Frontier Matrix Design Team · 2025

⸻

🗓️ Change Log

Date	Description
2025-10-10	Initial version — standardized metadata template and schema guide
2025-10-11	Added validation commands and graph integration notes

