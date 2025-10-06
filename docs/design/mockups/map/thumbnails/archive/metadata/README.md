<div align="center">

# 🧾 Kansas Frontier Matrix — Archived Map Thumbnail Metadata  
`docs/design/mockups/map/thumbnails/archive/metadata/`

**Structured · Traceable · Machine-Readable Provenance**

</div>

---

## 🧭 Overview

This directory stores **metadata records (`.json`)** for all archived map thumbnails  
located in `docs/design/mockups/map/thumbnails/archive/`.  

Each metadata file provides a **structured provenance record** that documents  
who created the original thumbnail, when it was archived, why it was replaced,  
and what new version superseded it.  

These records ensure that visual and design lineage within the  
**Kansas Frontier Matrix (KFM)** remains **traceable, auditable, and compliant**  
with the **Master Coder Protocol (MCP)** principles of reproducibility and data integrity.

---

## 📁 Directory Structure

```text
docs/design/mockups/map/thumbnails/archive/metadata/
├── README.md                                     # This documentation (GitHub-safe)
├── *.json                                        # Metadata files for archived thumbnails
└── schema/                                       # JSON Schema definitions for validation

Naming Convention:
YYYYMMDD_map-topic-thumb_v#.json
Example → 20251009_map-treaty-boundaries-thumb_v1.json

⸻

🧱 Purpose

Objective	Description
🧭 Provenance Tracking	Record version history and authorship for archived thumbnails
🧮 Validation	Enforce consistent metadata structure for automated CI checks
🕓 Version Lineage	Connect archived files to their replacements or related components
🧩 Integration	Link visual history to map layer configurations and STAC metadata
📚 Documentation	Ensure design decisions are transparent and reproducible


⸻

🧾 Example Metadata Template

{
  "id": "map-treaty-boundaries-thumb_v1",
  "title": "Treaty Boundaries Map Thumbnail v1",
  "author": "Kansas Frontier Matrix Design Team",
  "created": "2025-10-09",
  "archived": "2025-10-12",
  "superseded_by": "../../20251012_map-treaty-boundaries-thumb.webp",
  "reason": "Color scale and legend updated for accessibility.",
  "source": "../../20251009_map-treaty-boundaries-thumb.webp",
  "related": [
    "../../../icons/",
    "../../../layers/",
    "../../../../../../architecture/README.md"
  ],
  "tags": ["map", "treaty", "archive", "design", "accessibility"],
  "status": "archived",
  "license": "CC-BY-4.0"
}


⸻

🧮 JSON Schema Alignment

All metadata files are validated against the schema stored in:
docs/design/mockups/map/thumbnails/archive/metadata/schema/map_thumbnail_metadata.schema.json

This schema ensures every file contains the required fields and adheres
to KFM’s machine-readable documentation format.

Example Schema (excerpt):

{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Archived Map Thumbnail Metadata Schema",
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

🧩 Metadata Creation Workflow

1. Copy Template

Duplicate the above example into a new .json file using the proper naming format.

2. Fill in Metadata Fields

Include all relevant fields:
	•	Author or design team
	•	Creation and archival dates
	•	Link to source file
	•	Replacement file path
	•	Reason for archival

3. Validate Structure

Run JSON Schema validation locally or via CI:

jsonschema -i metadata/20251009_map-treaty-boundaries-thumb_v1.json schema/map_thumbnail_metadata.schema.json

4. Commit with Context

Record all related changes with provenance:

git add metadata/20251009_map-treaty-boundaries-thumb_v1.json
git commit -m "Added metadata for archived map thumbnail v1 (Treaty Boundaries)"


⸻

🔗 Integration with Knowledge Graph & STAC

Metadata entries are automatically linked into KFM’s knowledge graph and STAC catalog
via their related and superseded_by fields.

Relation	Description
derivedFrom	Links to the original design or export file
replacedBy	Points to the newer thumbnail version
isVersionOf	Indicates design lineage in Neo4j or RDF graph
hasLicense	Defines license inheritance for derived works

This linkage allows historical visual assets to be discoverable and queryable
in semantic graph layers or dataset catalogs.

⸻

🧩 Metadata Best Practices
	•	Use ISO8601 date format for created and archived fields.
	•	Maintain relative paths for all linked files.
	•	Keep "status" as "archived" unless asset is explicitly deprecated.
	•	Always provide a "reason" for archival or replacement.
	•	Limit "tags" to 3–6 concise keywords for searchability.
	•	Run schema validation before committing.
	•	Maintain consistent capitalization and naming conventions.

⸻

⚖️ License

All metadata files in this directory are released under
Creative Commons Attribution 4.0 International (CC-BY 4.0)

Credit: Kansas Frontier Matrix Design Team · 2025

Attribution required when reused or extended; commercial use permitted with credit.

⸻

🗓️ Change Log

Date	Description
2025-10-13	Initial version — metadata structure, example, and schema reference
2025-10-14	Added graph/STAC integration notes and validation workflow