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

Metadata is the foundation of reproducibility and traceability in KFM.
Every dataset, model, or experiment must include a **metadata record** documenting:

* Origin, licensing, and providers
* Spatial, temporal, and thematic coverage
* Processing lineage, checksums, and build commit
* Relationships to sources, derivatives, and workflows

KFM adopts the following **open standards**:

* 🧩 **STAC 1.0.0** — geospatial Items & Collections (with official extensions)
* 🧠 **JSON Schema** — validation & machine readability
* 🔗 **W3C PROV-O** (+ KFM MCP extensions) — provenance & lineage

All records are validated by CI/CD and the `make` targets in this repo.

---

## 🧩 Metadata Types

| Type                    | Format                     | Purpose                                | Directory                            |
| :---------------------- | :------------------------- | :------------------------------------- | :----------------------------------- |
| **Dataset Metadata**    | STAC **Item** (JSON)       | Single dataset or product.             | `data/stac/<domain>/items/*.json`    |
| **Collection Metadata** | STAC **Collection** (JSON) | Groups related Items (theme/time).     | `data/stac/<domain>/collection.json` |
| **Checksum**            | Plaintext `.sha256`        | Integrity verification (one per file). | `data/checksums/<domain>/`           |
| **Provenance**          | JSON / Markdown            | Lineage, processes, inputs/outputs.    | `docs/templates/provenance.md`       |
| **Model Card**          | JSON / Markdown            | Model metadata & evaluation.           | `docs/templates/model_card.md`       |
| **Experiment Log**      | Markdown                   | Hypothesis, params, results.           | `docs/templates/experiment.md`       |

---

## 🧠 Required STAC Fields (Item)

> Use **`datetime`** for instantaneous or midpoint time; use **`start_datetime`/`end_datetime`** for intervals.

| Field                    | Type      | Description                                                    | Example                                   |
| :----------------------- | :-------- | :------------------------------------------------------------- | :---------------------------------------- |
| `stac_version`           | string    | STAC spec version.                                             | `"1.0.0"`                                 |
| `id`                     | string    | Unique ID (stable).                                            | `"ks_1m_dem_2018_2020"`                   |
| `type`                   | string    | Always `"Feature"` for Items.                                  | `"Feature"`                               |
| `geometry`               | object    | GeoJSON geometry (optional for pure rasters, but recommended). | `{"type":"Polygon","coordinates":[...]}`  |
| `bbox`                   | number[4] | `[W,S,E,N]`.                                                   | `[-102.05,36.99,-94.59,40.00]`            |
| `properties.datetime`    | string    | ISO 8601 timestamp or midpoint.                                | `"2020-01-01T00:00:00Z"`                  |
| `properties.license`     | string    | SPDX or text.                                                  | `"CC-BY-4.0"`                             |
| `properties.description` | string    | Human-readable description.                                    | `"Kansas 1m DEM derived from LiDAR data"` |
| `assets`                 | object    | Files & ancillary assets.                                      | see below                                 |
| `links`                  | array     | Collection link, sources, docs, etc.                           | see below                                 |

### Required Asset Fields

| Field   | Type   | Description                                       | Example                                                      |
| :------ | :----- | :------------------------------------------------ | :----------------------------------------------------------- |
| `href`  | string | Relative repo path or URL.                        | `"data/processed/terrain/ks_1m_dem_2018_2020.tif"`           |
| `type`  | string | MIME type.                                        | `"image/tiff; application=geotiff; profile=cloud-optimized"` |
| `roles` | array  | `["data"]`, `["metadata"]`, `["thumbnail"]`, etc. | `["data"]`                                                   |
| `title` | string | Friendly title.                                   | `"Kansas DEM Raster"`                                        |

> **IDs & paths:** Prefer **relative** repo paths for reproducible builds; allow URLs for external mirrors.

---

## 🧩 Recommended STAC Extensions

> Use official extensions where applicable to increase interoperability and searchability.

| Extension      | Prefix        | Use For              | Notes                                        |
| :------------- | :------------ | :------------------- | :------------------------------------------- |
| **Projection** | `proj:`       | CRS & transform      | Provide EPSG, wkt2, transform, and shape.    |
| **Raster**     | `raster:`     | Bands, nodata, stats | Add band metadata for rasters.               |
| **File**       | `file:`       | Checksums & size     | `file:checksum`, `file:size`, and algorithm. |
| **Scientific** | `sci:`        | DOI, citations       | Link to DOIs and bib references.             |
| **Processing** | `processing:` | Processing steps     | Pipeline name/version.                       |
| **Label**      | `label:`      | Vector labels        | If publishing training labels.               |

**Examples (snippet):**

```json
"proj:epsg": 4326,
"raster:bands": [
  {"data_type": "float32", "nodata": -9999, "histogram": {"count": 256, "min": 200, "max": 1350}}
],
"file:checksum": "sha256:1f2c...b9a",
"sci:doi": "10.5066/P9U6F2U7",
"processing:software": "terrain_pipeline.py@1.3.0"
```

---

## 🔗 STAC Relationships (Lineage & Discoverability)

Use **`links[]`** with appropriate `rel` to express lineage and related resources:

| Relationship  | `rel`           | Description                |
| :------------ | :-------------- | :------------------------- |
| Collection    | `collection`    | Parent collection.         |
| Source        | `source`        | Original/raw data used.    |
| Derived From  | `derived_from`  | Parent Item/Collection.    |
| Child Of      | `child_of`      | Part of a larger dataset.  |
| Documentation | `documentation` | README / standards page.   |
| Preview       | `preview`       | Thumbnail/quicklook image. |
| Checksum      | `checksum`      | Pointer to checksum file.  |

**Example:**

```json
"links": [
  {"rel":"collection","href":"../collection.json"},
  {"rel":"derived_from","href":"../../sources/terrain/usgs_3dep_dem.json"},
  {"rel":"documentation","href":"../../../docs/standards/metadata.md"},
  {"rel":"checksum","href":"../../checksums/terrain/ks_1m_dem_2018_2020.tif.sha256"}
]
```

---

## 🧾 Collection Requirements

A **Collection** defines shared fields and search facets for its Items.

**Required:**

* `stac_version`, `type: "Collection"`, `id`, `description`
* `extent.spatial.bbox` (array of bboxes)
* `extent.temporal.interval` (array of `[start, end]` where end may be `null`)
* `license` (SPDX) or per-item license via `item_assets`
* `links` (self, root, child items optional)

**Recommended:**

* `keywords`, `providers`, `summaries` (common properties)
* Extension summaries (e.g., `proj:epsg`, `raster:bands`)

---

## 🧮 Temporal Guidance

* **Instant datasets:** Use `properties.datetime`.
* **Intervals:** Use `properties.start_datetime` and `properties.end_datetime`.
  Omit `datetime` when an interval is present.
* **Uncertain time:** Provide best approximation; annotate in `description` and `properties["kfm:time_note"]`.

---

## 🧩 KFM MCP Extensions (Item)

KFM extends STAC to embed reproducibility and auditability:

| Field                   | Type    | Description                           |
| :---------------------- | :------ | :------------------------------------ |
| `mcp:checksum_verified` | boolean | `true` if checksum verified at build. |
| `mcp:build_commit`      | string  | Short git hash for the build.         |
| `mcp:processed_by`      | string  | Pipeline/script responsible.          |
| `mcp:validation_log`    | string  | Path to validation log file.          |
| `mcp:reviewer`          | string  | Reviewer or steward name/role.        |

**JSON Schema for MCP extension** (copy to `docs/templates/schemas/mcp-extension.schema.json`):

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://kfm.local/schemas/mcp-extension.schema.json",
  "title": "KFM MCP STAC Extension",
  "type": "object",
  "properties": {
    "mcp:checksum_verified": { "type": "boolean" },
    "mcp:build_commit": { "type": "string", "pattern": "^[0-9a-f]{7,40}$" },
    "mcp:processed_by": { "type": "string" },
    "mcp:validation_log": { "type": "string" },
    "mcp:reviewer": { "type": "string" }
  },
  "additionalProperties": true
}
```

---

## 🧾 Copy-Paste Templates

### 1) **STAC Item (Full, with Extensions)**

```json
{
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/projection/v1.0.0/schema.json",
    "https://stac-extensions.github.io/raster/v1.1.0/schema.json",
    "https://stac-extensions.github.io/file/v2.1.0/schema.json",
    "https://stac-extensions.github.io/scientific/v1.0.0/schema.json"
  ],
  "id": "ks_1m_dem_2018_2020",
  "type": "Feature",
  "geometry": null,
  "bbox": [-102.05, 36.99, -94.59, 40.00],
  "properties": {
    "datetime": "2020-01-01T00:00:00Z",
    "license": "CC-BY-4.0",
    "description": "Kansas 1m DEM derived from USGS 3DEP LiDAR (2018–2020).",
    "providers": [{"name": "USGS 3DEP", "roles": ["producer"]}],
    "keywords": ["terrain", "elevation", "LiDAR"],
    "proj:epsg": 4326,
    "mcp:checksum_verified": true,
    "mcp:build_commit": "f3a91b2",
    "mcp:processed_by": "terrain_pipeline.py@1.3.0",
    "mcp:validation_log": "data/work/logs/terrain/stac_validate_ks_dem.log",
    "mcp:reviewer": "Data Governance Team"
  },
  "assets": {
    "data": {
      "href": "data/processed/terrain/ks_1m_dem_2018_2020.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"],
      "title": "Kansas LiDAR DEM",
      "raster:bands": [{"data_type": "float32", "nodata": -9999}]
    },
    "thumbnail": {
      "href": "data/processed/terrain/thumbnails/ks_1m_dem_2018_2020.png",
      "type": "image/png",
      "roles": ["thumbnail"]
    },
    "checksum": {
      "href": "data/checksums/terrain/ks_1m_dem_2018_2020.tif.sha256",
      "type": "text/plain",
      "roles": ["checksum"],
      "file:checksum": "sha256:1f2c...b9a"
    }
  },
  "links": [
    {"rel": "collection", "href": "../collection.json"},
    {"rel": "derived_from", "href": "../../sources/terrain/usgs_3dep_dem.json"},
    {"rel": "documentation", "href": "../../../docs/standards/metadata.md"}
  ]
}
```

### 2) **STAC Collection (Minimal, Search-Optimized)**

```json
{
  "stac_version": "1.0.0",
  "type": "Collection",
  "id": "terrain",
  "description": "Terrain and elevation products for the Kansas Frontier Matrix.",
  "license": "CC-BY-4.0",
  "keywords": ["terrain","elevation","DEM","hillshade","LiDAR"],
  "providers": [
    {"name": "KFM Team", "roles": ["host"]},
    {"name": "USGS 3DEP", "roles": ["producer"]}
  ],
  "extent": {
    "spatial": { "bbox": [[-102.05, 36.99, -94.59, 40.00]] },
    "temporal": { "interval": [["2018-01-01T00:00:00Z", "2020-12-31T23:59:59Z"]] }
  },
  "links": [
    {"rel": "self","href":"collection.json"},
    {"rel": "root","href":"../../catalog.json"}
  ],
  "summaries": {
    "proj:epsg": [4326],
    "raster:bands": [{"data_type": ["float32"]}]
  }
}
```

---

## 🧩 Naming & Storage Conventions

| Element         | Rule                                              | Example                          |
| :-------------- | :------------------------------------------------ | :------------------------------- |
| **Item file**   | `<dataset>.json`                                  | `ks_1m_dem_2018_2020.json`       |
| **Collection**  | `<domain>_collection.json` (or `collection.json`) | `collection.json`                |
| **Checksum**    | `<filename>.<ext>.sha256`                         | `ks_1m_dem_2018_2020.tif.sha256` |
| **Directories** | `data/stac/<domain>/items/` for Items             | `data/stac/terrain/items/`       |
| **IDs**         | Kebab or snake, stable, semantic                  | `ks_1m_dem_2018_2020`            |

---

## 🔄 Validation Workflows (CI + Local)

| Validation            | Tool/Target                           | Output               |
| :-------------------- | :------------------------------------ | :------------------- |
| STAC schema           | `stac-validator`                      | Compliance report    |
| JSON Schema (MCP ext) | `jsonschema`                          | Pass/fail report     |
| Checksums             | `make checksums`                      | Verified/failed list |
| Link integrity        | `.github/workflows/stac-validate.yml` | Broken link report   |

**Local run examples:**

```bash
# Validate a single item
stac-validator data/stac/terrain/items/ks_1m_dem_2018_2020.json

# Validate MCP extension fields
python -m jsonschema \
  -i data/stac/terrain/items/ks_1m_dem_2018_2020.json \
  docs/templates/schemas/mcp-extension.schema.json

# Verify checksums
make checksums
```

---

## 🔗 Provenance & PROV-O Mapping

KFM provenance aligns STAC links with W3C PROV-O concepts:

| Concept            | PROV-O                 | STAC Expression                      |
| :----------------- | :--------------------- | :----------------------------------- |
| Entity (dataset)   | `prov:Entity`          | STAC Item / Asset                    |
| Activity (process) | `prov:Activity`        | `processing:` fields, pipeline names |
| Agent (person/org) | `prov:Agent`           | `providers[]`, `mcp:reviewer`        |
| Used (inputs)      | `prov:used`            | `links[rel="source"]`                |
| WasDerivedFrom     | `prov:wasDerivedFrom`  | `links[rel="derived_from"]`          |
| WasAttributedTo    | `prov:wasAttributedTo` | `providers[].roles`                  |

Add a human-readable provenance stub per dataset in `docs/templates/provenance.md` and link via `links.rel=documentation`.

---

## ✅ MCP Compliance Summary

| MCP Principle           | Implementation                                                         |
| :---------------------- | :--------------------------------------------------------------------- |
| **Documentation-first** | Item/Collection templates & schemas provided before data release.      |
| **Reproducibility**     | Deterministic pipelines + checksums + commit hash in metadata.         |
| **Open Standards**      | STAC 1.0.0 + official extensions + JSON Schema.                        |
| **Provenance**          | STAC `links` + PROV-O mapping + `mcp:*` fields.                        |
| **Auditability**        | CI validates Items/Collections, links, and checksums with stored logs. |

---

## 📎 Related Documentation

| Path                                     | Description                    |
| :--------------------------------------- | :----------------------------- |
| `docs/standards/data-formats.md`         | Approved data/file formats.    |
| `docs/templates/provenance.md`           | Provenance authoring template. |
| `docs/architecture/data-architecture.md` | End-to-end data/metadata flow. |
| `.github/workflows/stac-validate.yml`    | CI validation workflow.        |

---

## 📅 Version History

| Version | Date       | Author                 | Summary                                                                                                             |
| :------ | :--------- | :--------------------- | :------------------------------------------------------------------------------------------------------------------ |
| v1.1    | 2025-10-05 | KFM Documentation Team | Added extensions (proj, raster, file, sci, processing), Item/Collection templates, PROV-O mapping, MCP JSON Schema. |
| v1.0    | 2025-10-04 | KFM Documentation Team | Initial metadata standards for STAC + MCP compliance.                                                               |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Record Proven. Every Metadata Validated.”*
📍 [`docs/standards/metadata.md`](.) · Official metadata standard for STAC + MCP compliance.

</div>
