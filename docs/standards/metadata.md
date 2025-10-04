<div align="center">

# 🧾 Kansas Frontier Matrix — Metadata Standards  
`docs/standards/metadata.md`

**Purpose:** Establish a unified metadata framework for all datasets, models, and workflows  
within the **Kansas Frontier Matrix (KFM)** — ensuring that each asset is discoverable, validated,  
and linked through reproducible, provenance-aware records.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)

</div>

---

## 📚 Overview

Metadata is the foundation of reproducibility and traceability in the Kansas Frontier Matrix.  
Every dataset, model, or experiment must include a **metadata record** documenting:
- Origin and licensing  
- Spatial, temporal, and thematic coverage  
- Processing lineage and checksum validation  
- Relationships to other datasets, experiments, or workflows  

All KFM metadata follows:
- 🧩 **STAC 1.0.0** — for geospatial data and collections  
- 🧠 **JSON Schema** — for validation and machine readability  
- 🔗 **W3C PROV-O & MCP Provenance Extensions** — for data lineage tracking  

---

## 🧩 Metadata Types

| Type | Format | Purpose | Directory |
|:------|:--------|:----------|:-----------|
| **Dataset Metadata** | STAC Item (JSON) | Describes a single dataset. | `data/stac/<domain>/` |
| **Collection Metadata** | STAC Collection (JSON) | Groups related datasets thematically or temporally. | `data/stac/<domain>/collection.json` |
| **Checksum Metadata** | Plaintext (`.sha256`) | Confirms dataset integrity. | `data/checksums/<domain>/` |
| **Provenance Metadata** | JSON / RDF | Captures data lineage, sources, and transformations. | `docs/templates/provenance.md` |
| **Model Metadata** | JSON / Markdown | Describes analytical or predictive models. | `docs/templates/model_card.md` |
| **Experiment Metadata** | Markdown | Defines parameters, hypotheses, and outcomes. | `docs/templates/experiment.md` |

---

## 🧠 Metadata Schema Requirements

All JSON metadata must be **STAC 1.0.0-compliant** and **JSON Schema-validated**.

### Required STAC Fields

| Field | Type | Description | Example |
|:--------|:------|:-------------|:----------|
| `stac_version` | string | STAC specification version. | `"1.0.0"` |
| `id` | string | Unique dataset identifier. | `"ks_1m_dem_2018_2020"` |
| `type` | string | STAC entity type (e.g., `"Feature"`, `"Collection"`). | `"Feature"` |
| `properties.datetime` | string (ISO 8601) | Dataset timestamp or temporal midpoint. | `"2020-01-01T00:00:00Z"` |
| `properties.license` | string | Licensing terms. | `"CC-BY 4.0"` |
| `properties.description` | string | Human-readable description. | `"Kansas 1-meter DEM derived from LiDAR data"` |
| `bbox` | array | Spatial bounding box `[W, S, E, N]`. | `[-102.05, 36.99, -94.59, 40.00]` |
| `links` | array | References to parent collections, sources, and related datasets. | `[{"rel": "collection", "href": "../collection.json"}]` |
| `assets` | object | Links to data files, thumbnails, and checksums. | See below |

---

### Required Asset Fields

| Field | Type | Description | Example |
|:--------|:------|:-------------|:----------|
| `href` | string | Path or URL to asset. | `"data/processed/terrain/ks_1m_dem_2018_2020.tif"` |
| `type` | string | MIME type of asset. | `"image/tiff; application=geotiff; profile=cloud-optimized"` |
| `roles` | array | Functional role of the asset (e.g., `"data"`, `"metadata"`, `"thumbnail"`). | `["data"]` |
| `title` | string | Asset title or name. | `"Kansas DEM Raster"` |

---

### Optional / Recommended Fields

| Field | Description | Example |
|:--------|:-------------|:-----------|
| `properties.platform` | Source platform or sensor. | `"LiDAR"` |
| `properties.constellation` | Satellite or sensor family. | `"USGS 3DEP"` |
| `properties.providers` | Organizations or teams responsible for data. | `[{"name": "USGS", "roles": ["producer"]}]` |
| `properties.keywords` | Searchable tags or themes. | `["terrain", "elevation", "DEM"]` |
| `assets.thumbnail` | PNG image for visual preview. | `"data/processed/metadata/terrain/thumbnails/ks_1m_dem_2018_2020.png"` |
| `assets.metadata` | Link to detailed provenance record. | `"docs/templates/provenance.md"` |

---

## 🧾 STAC Relationships (Provenance Linkage)

All datasets must include **lineage links** describing origin, derivation, and relationships.

| Relationship Type | STAC Field | Description |
|:--------------------|:------------|:--------------|
| **Source** | `rel:source` | Original dataset used in derivation. |
| **Derived From** | `rel:derived_from` | Parent dataset or collection. |
| **Child Of** | `rel:child_of` | Part of a larger collection. |
| **Thumbnail** | `rel:preview` | Associated image or visualization. |
| **Checksum** | `rel:checksum` | Integrity validation asset. |
| **Documentation** | `rel:documentation` | Link to README or documentation page. |

**Example:**
```json
"links": [
  {"rel": "collection", "href": "../collection.json"},
  {"rel": "derived_from", "href": "../../sources/terrain/usgs_3dep_dem.json"},
  {"rel": "checksum", "href": "../../checksums/terrain/ks_1m_dem_2018_2020.tif.sha256"}
]
````

---

## 🧩 Validation Workflows

Metadata validation is automated through CI/CD.

| Validation Type            | Tool / Workflow                       | Output                                 |
| :------------------------- | :------------------------------------ | :------------------------------------- |
| **STAC Validation**        | `stac-validator`                      | Reports STAC schema compliance.        |
| **JSON Schema Validation** | `jsonschema`                          | Checks custom metadata schema.         |
| **Checksum Verification**  | `make checksums`                      | Confirms file integrity.               |
| **Link Validation**        | `.github/workflows/stac-validate.yml` | Confirms all internal links are valid. |

**Manual Validation Example:**

```bash
stac-validator data/stac/terrain/ks_1m_dem_2018_2020.json
```

---

## 🧩 Metadata Naming & Storage Conventions

| Element                | Rule                          | Example                          |
| :--------------------- | :---------------------------- | :------------------------------- |
| **File Naming**        | `<dataset>.json`              | `ks_1m_dem_2018_2020.json`       |
| **Collection Name**    | `<domain>_collection.json`    | `terrain_collection.json`        |
| **Checksum**           | `<filename>.<ext>.sha256`     | `ks_1m_dem_2018_2020.tif.sha256` |
| **Metadata Directory** | `data/stac/<domain>/`         | `data/stac/terrain/`             |
| **Provenance Link**    | Linked via `rel:derived_from` | `docs/templates/provenance.md`   |

---

## 🧠 Extended Metadata Fields (MCP Extensions)

KFM extends STAC Items with additional **MCP-compliant provenance fields**.

| Field                   | Description                                        | Example                                  |
| :---------------------- | :------------------------------------------------- | :--------------------------------------- |
| `mcp:checksum_verified` | Boolean indicating checksum validation success.    | `true`                                   |
| `mcp:build_commit`      | Git commit hash associated with the build.         | `"a3f29e9"`                              |
| `mcp:processed_by`      | Name of pipeline or script that produced the file. | `"terrain_pipeline.py"`                  |
| `mcp:validation_log`    | Path to validation log file.                       | `"data/work/logs/terrain_etl_debug.log"` |
| `mcp:reviewer`          | Responsible reviewer or data steward.              | `"Data Governance Team"`                 |

---

## 🧾 Metadata Example (Full STAC + MCP)

```json
{
  "stac_version": "1.0.0",
  "id": "ks_1m_dem_2018_2020",
  "type": "Feature",
  "properties": {
    "datetime": "2020-01-01T00:00:00Z",
    "license": "Public Domain",
    "description": "Kansas 1m DEM derived from USGS 3DEP LiDAR (2018–2020).",
    "providers": [{"name": "USGS 3DEP", "roles": ["producer"]}],
    "keywords": ["terrain", "elevation", "LiDAR"],
    "mcp:checksum_verified": true,
    "mcp:build_commit": "f3a91b2",
    "mcp:processed_by": "terrain_pipeline.py"
  },
  "bbox": [-102.05, 36.99, -94.59, 40.00],
  "assets": {
    "data": {
      "href": "data/processed/terrain/ks_1m_dem_2018_2020.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"],
      "title": "Kansas LiDAR DEM"
    },
    "checksum": {
      "href": "data/checksums/terrain/ks_1m_dem_2018_2020.tif.sha256",
      "type": "text/plain",
      "roles": ["checksum"]
    }
  },
  "links": [
    {"rel": "collection", "href": "../collection.json"},
    {"rel": "derived_from", "href": "../../sources/terrain/usgs_3dep_dem.json"}
  ]
}
```

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                   |
| :---------------------- | :--------------------------------------------------------------- |
| **Documentation-first** | Metadata schema and structure documented before data release.    |
| **Reproducibility**     | Metadata generation automated through deterministic pipelines.   |
| **Open Standards**      | Follows STAC 1.0.0 and JSON Schema specifications.               |
| **Provenance**          | Includes lineage, commit hash, and checksum references.          |
| **Auditability**        | Validated automatically through CI/CD workflows and stored logs. |

---

## 📎 Related Documentation

| Path                                     | Description                                    |
| :--------------------------------------- | :--------------------------------------------- |
| `docs/standards/data-formats.md`         | Defines approved data and file formats.        |
| `docs/templates/provenance.md`           | Provenance documentation template.             |
| `docs/architecture/data-architecture.md` | Describes data and metadata flow architecture. |
| `.github/workflows/stac-validate.yml`    | CI/CD validation workflow for STAC metadata.   |

---

## 📅 Version History

| Version | Date       | Author                 | Summary                                               |
| :------ | :--------- | :--------------------- | :---------------------------------------------------- |
| v1.0    | 2025-10-04 | KFM Documentation Team | Initial metadata standards for STAC + MCP compliance. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Record Proven. Every Metadata Validated.”*
📍 [`docs/standards/metadata.md`](.) · Official metadata standard for STAC and MCP compliance in KFM.

</div>
