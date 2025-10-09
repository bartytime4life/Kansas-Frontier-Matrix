<div align="center">

# 🗺️ Kansas Frontier Matrix — Map Thumbnails Metadata  
`docs/design/mockups/map/thumbnails/metadata/`

**Purpose:** Define and validate the **metadata conventions** for **map thumbnail images**  
used across Kansas Frontier Matrix (KFM) documentation, web UI, and STAC-based datasets.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../..)  
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../..)  
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../../.github/workflows/stac-validate.yml)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../LICENSE)

</div>

---

## 🧭 Overview

This directory contains **metadata JSON files** describing the **visual, semantic, and provenance attributes**  
of map thumbnail images used in KFM documentation, UI previews, and STAC layer catalogs.

Each thumbnail metadata entry links a **visual representation** of a map layer or dataset  
to its **corresponding STAC Item**, ensuring data integrity, discoverability, and reproducibility.

Metadata records document:
- ✅ **Thumbnail metadata** (title, dataset, theme, creation date, color keys).  
- 🧩 **Semantic attributes** (region, temporal coverage, thematic category).  
- 🧾 **Provenance & checksums** for traceable validation.  
- 🔗 **Cross-links** to STAC, design mockups, and related data documentation.  

All metadata entries are validated automatically under **MCP-compliant CI/CD pipelines**, ensuring  
alignment with STAC 1.0.0 and DCAT Dataset conventions.

---

## 🗂️ Directory Layout

```text
docs/design/mockups/map/thumbnails/metadata/
├── README.md                     # This file
├── thumbnails_metadata.json      # Aggregated metadata index
├── {layer_id}.json               # Individual metadata record for each map layer
└── schema/                       # JSON Schemas for validation
    ├── thumbnail.schema.json
    └── index.schema.json
````

---

## 🧱 Metadata Schema

Each metadata record conforms to `schema/thumbnail.schema.json` —
a simplified JSON Schema derived from **STAC Asset** and **DCAT Dataset** models.

### Example Record

```json
{
  "id": "ks_topo_1894",
  "title": "USGS Kansas Topographic Map (1894)",
  "thumbnail": "../archive/ks_topo_1894.png",
  "source_stac": "../../../data/stac/items/ks_topo_1894.json",
  "spatial_extent": [-102.0, 37.0, -94.6, 40.0],
  "temporal_extent": { "start": "1894-01-01", "end": "1894-12-31" },
  "theme": ["topographic", "historical", "cartography"],
  "color_key": ["#d4b483", "#b9975b", "#9e7b39"],
  "creator": "Kansas Geological Survey / USGS",
  "license": "Public Domain",
  "checksum": "sha256-abcdef123456...",
  "provenance": {
    "derived_from": "data/processed/topo_1894_cog.tif",
    "created_with": "scripts/generate_thumbnails.py",
    "commit": "{{ GIT_COMMIT }}"
  }
}
```

All metadata files are validated automatically during CI/CD via **STAC validation** and **JSON Schema linting**.

---

## 🧩 Metadata Field Reference

| Field               | Type   | Description                                                 |
| ------------------- | ------ | ----------------------------------------------------------- |
| **id**              | string | Unique identifier for the map thumbnail (kebab-case).       |
| **title**           | string | Human-readable map or dataset name.                         |
| **thumbnail**       | string | Path to the preview image (relative to this directory).     |
| **source_stac**     | string | Path to the associated STAC Item JSON file.                 |
| **spatial_extent**  | array  | Bounding box `[west, south, east, north]` for map extent.   |
| **temporal_extent** | object | Start and end dates for the dataset coverage.               |
| **theme**           | array  | Tags describing content (e.g., `"hydrology"`, `"geology"`). |
| **color_key**       | array  | Key color palette representing the layer.                   |
| **creator**         | string | Data source or author attribution.                          |
| **license**         | string | License type (CC-BY-4.0, Public Domain, etc.).              |
| **checksum**        | string | SHA-256 hash for image integrity.                           |
| **provenance**      | object | Records lineage, toolchain, and commit linkage.             |

---

## 🧮 Validation Workflow

Validation runs automatically via **GitHub Actions** workflows (`jsonschema.yml`, `stac-validate.yml`)
and ensures that all metadata conforms to MCP and STAC standards.

| Validation Step           | Description                                              | Workflow            |
| ------------------------- | -------------------------------------------------------- | ------------------- |
| **Schema Validation**     | Checks JSON structure and field presence.                | `jsonschema.yml`    |
| **Checksum Validation**   | Confirms SHA-256 matches asset file.                     | `stac-validate.yml` |
| **STAC Cross-Linking**    | Ensures all `source_stac` fields resolve to valid Items. | `stac-validate.yml` |
| **License & Attribution** | Confirms presence of author and license fields.          | `jsonschema.yml`    |

### Manual Validation Example

```bash
python -m jsonschema -i thumbnails_metadata.json schema/thumbnail.schema.json
```

---

## 🧠 Integration with the Web UI

| Integration Target                 | Purpose                                                            | Implementation                    |
| ---------------------------------- | ------------------------------------------------------------------ | --------------------------------- |
| **React / MapLibre Layer Browser** | Provides thumbnail previews for layer selection.                   | Reads `thumbnails_metadata.json`. |
| **STAC Catalog Browser**           | Displays map thumbnails in temporal and thematic views.            | References `source_stac`.         |
| **Documentation**                  | Embeds thumbnail previews in READMEs and data summaries.           | Linked via Markdown or HTML.      |
| **Automation Scripts**             | Automatically rebuilds metadata during `make docs` or ETL updates. | `scripts/generate_thumbnails.py`. |

> 🧩 If a `source_stac` file is missing or invalid, the system defaults to a placeholder icon for graceful degradation.

---

## ♿ Accessibility & Compliance

| Check                   | Requirement            | Validation                                      |
| ----------------------- | ---------------------- | ----------------------------------------------- |
| **Contrast Ratio**      | ≥ 4.5 : 1              | Verified using Figma and design QA tools.       |
| **Alt Text**            | Required               | Defined in corresponding documentation.         |
| **File Size**           | ≤ 300 KB               | Ensures fast loading and responsive previewing. |
| **Theme Compatibility** | Dual-mode (light/dark) | Tested during design QA.                        |

Accessibility results are logged in **metadata QA reports** and stored in GitHub Action summaries.

---

## 🧾 Provenance & Integrity

| Attribute            | Description                                    |
| -------------------- | ---------------------------------------------- |
| **Generated By**     | `scripts/generate_thumbnails.py`               |
| **Validated In CI**  | `stac-validate.yml`, `jsonschema.yml`          |
| **Checksums**        | SHA-256 validation recorded in metadata.       |
| **Linked Artifacts** | STAC items, design exports, and documentation. |
| **License**          | [CC-BY 4.0](../../../../../LICENSE)            |
| **MCP Compliance**   | Documented → Validated → Published.            |

---

## 📚 Related References

* [🗺 Map Thumbnails (Main)](../README.md)
* [🧩 Map Wireframe Thumbnails Metadata](../../wireframes/thumbnails/metadata/README.md)
* [🧱 Kansas Frontier Matrix Web UI Architecture](../../../../../../architecture/web_ui_architecture_review.md)
* [🌐 STAC Catalog](../../../../../../data/stac/catalog.json)
* [♿ Accessibility Design Standards](../../../../../design/reviews/accessibility/README.md)

---

<div align="center">

### Kansas Frontier Matrix — Documentation-First Design

**Spatial Context · Provenance Integrity · Accessible Visualization**

</div>
