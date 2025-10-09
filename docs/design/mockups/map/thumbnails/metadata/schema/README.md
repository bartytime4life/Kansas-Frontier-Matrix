</div>

---

## 🧭 Overview

This directory provides the **authoritative JSON Schemas** for validating **map thumbnail metadata** stored under  
`docs/design/mockups/map/thumbnails/metadata/`. Conformance to these schemas guarantees:

- 🔗 Interoperability with the KFM **STAC** catalog (`data/stac/items/*.json`)  
- 🧩 Consistent fields across design & data layers (title, license, spatial/temporal extents)  
- 🧾 Provenance and reproducibility (checksum, derived_from, commit)  
- ♿ Accessibility metadata (contrast, alt text) for inclusive documentation and UI previews

---

## 🗂️ Directory Layout

```text
docs/design/mockups/map/thumbnails/metadata/schema/
├── README.md                 # This documentation file
├── thumbnail.schema.json     # Schema for individual thumbnail metadata
└── index.schema.json         # Schema for the aggregated thumbnail index
````

---

## 📘 `thumbnail.schema.json`

**Purpose:** Validate a single map thumbnail metadata record (e.g., `ks_topo_1894.json`).
Each record describes a preview image for one geospatial/historical layer and its linkage to data sources.

### 🧩 Schema Outline (Draft 2020-12)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Map Thumbnail Metadata",
  "type": "object",
  "required": ["id", "title", "thumbnail", "source_stac", "license", "provenance"],
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[a-z0-9_\\-]+$",
      "description": "Unique identifier for the thumbnail (ideally matches STAC item ID)."
    },
    "title": { "type": "string", "description": "Human-readable title." },
    "thumbnail": { "type": "string", "description": "Relative path to PNG/JPG/WebP file." },
    "description": { "type": "string", "description": "Short description of the map layer." },
    "source_stac": {
      "type": "string",
      "description": "Path to linked STAC item (e.g., data/stac/items/ks_topo_1894.json)."
    },
    "spatial_extent": {
      "type": "array",
      "minItems": 4,
      "maxItems": 4,
      "items": { "type": "number" },
      "description": "Bounding box [W, S, E, N] in WGS84 coordinates."
    },
    "temporal_extent": {
      "type": "object",
      "properties": {
        "start": { "type": "string", "format": "date" },
        "end":   { "type": "string", "format": "date" }
      },
      "required": ["start"],
      "additionalProperties": false,
      "description": "Dataset coverage interval; end optional for open-ended ranges."
    },
    "theme": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Design/theme tags (e.g., ['hydrology','cartography'])."
    },
    "color_key": {
      "type": "array",
      "items": { "type": "string", "pattern": "^#([A-Fa-f0-9]{6})$" },
      "description": "Hex color palette representing the layer."
    },
    "license": { "type": "string", "description": "License of the thumbnail asset." },
    "checksum": {
      "type": "string",
      "pattern": "^sha256-[A-Fa-f0-9]+$",
      "description": "SHA-256 checksum for image integrity verification."
    },
    "provenance": {
      "type": "object",
      "required": ["derived_from"],
      "properties": {
        "derived_from": { "type": "string", "description": "Origin file (e.g., COG/GeoJSON) or design export." },
        "created_with": { "type": "string", "description": "Tool/script used to generate the thumbnail." },
        "commit":       { "type": "string", "description": "Git commit hash linking to repo history." }
      },
      "additionalProperties": false
    },
    "accessibility": {
      "type": "object",
      "properties": {
        "contrast_ratio": { "type": "number", "minimum": 4.5 },
        "alt_text":       { "type": "string" }
      },
      "additionalProperties": false,
      "description": "WCAG 2.1 AA metadata (contrast ratio and descriptive alt text)."
    }
  },
  "additionalProperties": false
}
```

---

## 📗 `index.schema.json`

**Purpose:** Validate the aggregated index file (e.g., `thumbnails_metadata.json`) used for bulk validation, search, and catalog integration.

### 🧩 Schema Outline (Draft 2020-12)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Map Thumbnails Metadata Index",
  "type": "object",
  "required": ["version", "thumbnails"],
  "properties": {
    "version": { "type": "string", "pattern": "^\\d+\\.\\d+\\.\\d+$" },
    "updated": { "type": "string", "format": "date-time" },
    "thumbnails": {
      "type": "array",
      "items": { "$ref": "./thumbnail.schema.json" }
    }
  },
  "additionalProperties": false
}
```

---

## 🧮 Validation Workflow

Validation runs automatically via **GitHub Actions**:

| Step  | Check                                   | Workflow            |
| ----- | --------------------------------------- | ------------------- |
| **1** | JSON Schema compliance                  | `jsonschema.yml`    |
| **2** | Checksum integrity (SHA-256)            | `stac-validate.yml` |
| **3** | STAC linkage (resolvable `source_stac`) | `stac-validate.yml` |
| **4** | License & attribution present           | `jsonschema.yml`    |
| **5** | Accessibility metadata present          | `jsonschema.yml`    |

### Manual Validation Example

```bash
python -m jsonschema -i thumbnails_metadata.json schema/thumbnail.schema.json
```

---

## 🔗 Integration Notes

| Component                       | Purpose                                                | Link                                  |
| ------------------------------- | ------------------------------------------------------ | ------------------------------------- |
| **STAC Catalog**                | Connects thumbnails to datasets and temporal metadata. | `data/stac/catalog.json`              |
| **Web UI (React + MapLibreGL)** | Uses thumbnails in Layer Browser and previews.         | `web/config/layers.json`              |
| **Docs Site (MCP)**             | Renders thumbnails in READMEs and indexes.             | `docs/design/mockups/map/thumbnails/` |

---

## 📚 Related References

* [Map Thumbnails Metadata](../README.md)
* [STAC Catalog](../../../../../../data/stac/catalog.json)
* [Kansas Frontier Matrix Architecture](../../../../../../architecture/README.md)
* [Data Format Standards](../../../../../../docs/standards/data-formats.md)

---

<div align="center">

### Kansas Frontier Matrix — Documentation-First Design

**Spatial Context · Interop by Design · Accessible Previews**

</div>
```
