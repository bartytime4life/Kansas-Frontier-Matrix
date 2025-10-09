<div align="center">

# 🧾 Kansas Frontier Matrix — Archived Map Thumbnail Metadata  
`docs/design/mockups/map/thumbnails/archive/metadata/`

**Structured · Traceable · Machine-Readable Provenance**

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../../../..)  
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../../../../..)  
[![Schema Validation](https://img.shields.io/badge/Schema-Validated-orange)](https://json-schema.org)  
[![Archive Integrity](https://img.shields.io/badge/Archive-Integrity-blue)](../../../../../../../../.github/workflows/stac-validate.yml)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../../../../LICENSE)

</div>

---

## 🧭 Overview

This directory contains **metadata records (`.json`)** for all archived map thumbnails  
found under `docs/design/mockups/map/thumbnails/archive/`.  

Each metadata file captures:
- 🧩 **Provenance** — when, why, and by whom a thumbnail was archived.  
- 🔗 **Lineage** — the connection between old and new thumbnail versions.  
- 🧮 **Validation data** — checksums, licensing, and STAC links.  
- 🧠 **Contextual relationships** — related components and datasets.  

These records create a **traceable visual history** within the Kansas Frontier Matrix (KFM)  
and uphold the **Master Coder Protocol (MCP)** standard for documentation-first design lineage.

---

## 🗂️ Directory Layout

```text
docs/design/mockups/map/thumbnails/archive/metadata/
├── README.md                            # This documentation (GitHub-safe)
├── *.json                               # Metadata files describing archived thumbnails
└── schema/                              # JSON Schema definitions for validation
````

### 📛 Naming Convention

`YYYYMMDD_map-topic-thumb_v#.json`
**Example:** `20251009_map-treaty-boundaries-thumb_v1.json`

---

## 🧱 Purpose

| Objective                  | Description                                                          |
| -------------------------- | -------------------------------------------------------------------- |
| 🧭 **Provenance Tracking** | Records authorship and reason for archival.                          |
| 🧮 **Validation**          | Enforces schema compliance for MCP pipeline checks.                  |
| 🕓 **Version Lineage**     | Connects deprecated and replacement thumbnail versions.              |
| 🧩 **Integration**         | Links archived assets to STAC metadata and map layer configurations. |
| 📚 **Documentation**       | Enables long-term auditability and transparency.                     |

---

## 🧾 Example Metadata Template

```json
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
```

All archived metadata files are validated automatically in CI
using the schema stored in:
`docs/design/mockups/map/thumbnails/archive/metadata/schema/map_thumbnail_metadata.schema.json`

---

## 🧮 JSON Schema Alignment

### Example Schema (Excerpt)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
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
```

This schema guarantees:

* ✅ Structural uniformity across all archived metadata.
* 🔒 Consistent versioning and linkage patterns.
* 🧾 Metadata completeness for downstream ingestion into KFM’s knowledge systems.

---

## 🧩 Metadata Creation Workflow

### 1️⃣ Copy Template

Duplicate the above JSON example using the standard naming format.

### 2️⃣ Fill in Metadata Fields

Provide complete information:

* Author(s)
* Created & archived dates
* Superseding file path
* Archival reason
* License and tags

### 3️⃣ Validate Structure

Run JSON Schema validation manually or in CI:

```bash
python -m jsonschema -i metadata/20251009_map-treaty-boundaries-thumb_v1.json \
  schema/map_thumbnail_metadata.schema.json
```

### 4️⃣ Commit with Context

Document archival details in the commit message:

```bash
git add metadata/20251009_map-treaty-boundaries-thumb_v1.json
git commit -m "Added metadata for archived map thumbnail v1 (Treaty Boundaries)"
```

---

## 🔗 Integration with Knowledge Graph & STAC

Each metadata file links archived assets to KFM’s knowledge graph and STAC catalogs
for persistent semantic relationships.

| Relation        | Description                                     |
| --------------- | ----------------------------------------------- |
| **derivedFrom** | Links to the original design or dataset source. |
| **replacedBy**  | Connects to the newer, superseding thumbnail.   |
| **isVersionOf** | Declares lineage within RDF or Neo4j.           |
| **hasLicense**  | Inherits license from parent dataset.           |

This metadata enables **automated provenance queries**, allowing design artifacts
to be discoverable in semantic layers and historical visual catalogs.

---

## 🧩 Metadata Best Practices

| Best Practice       | Guideline                                        |
| ------------------- | ------------------------------------------------ |
| **Date Format**     | Use ISO8601 (YYYY-MM-DD).                        |
| **Relative Paths**  | Maintain relative file linking for portability.  |
| **Status Field**    | Use `"archived"` unless explicitly deprecated.   |
| **Archival Reason** | Always include a descriptive rationale.          |
| **Tag Limit**       | 3–6 concise, relevant tags.                      |
| **Validation**      | Run schema checks before committing.             |
| **Versioning**      | Append `_v1`, `_v2`, etc. for revision tracking. |

---

## ♿ Accessibility & Preservation

| Metric             | Standard  | Description                                       |
| ------------------ | --------- | ------------------------------------------------- |
| **Alt Text**       | Required  | Stored in UI references or documentation context. |
| **Color Contrast** | ≥ 4.5 : 1 | Maintained in archived assets.                    |
| **Dual Theme**     | Verified  | Works under light/dark mode documentation.        |

Accessibility attributes from these archives ensure that legacy designs remain inclusive and referenceable.

---

## ⚖️ License

All archived thumbnail metadata are released under
**Creative Commons Attribution 4.0 International (CC-BY 4.0)**.
Attribution required; commercial use permitted with credit.

**© 2025 Kansas Frontier Matrix Design Team**

---

## 🗓️ Change Log

| Date           | Description                                               |
| -------------- | --------------------------------------------------------- |
| **2025-10-13** | Initial version — metadata schema and example template.   |
| **2025-10-14** | Added integration with Knowledge Graph & STAC references. |
| **2025-10-15** | Improved workflow automation and validation guidance.     |

---

<div align="center">

### Kansas Frontier Matrix — Documentation-First Design

**Preservation · Accessibility · Provenance Integrity**

</div>
