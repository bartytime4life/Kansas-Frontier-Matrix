---
name: "🧩 Data addition request"
about: Propose a new dataset (map, layer, catalog, document set) for Kansas-Frontier-Matrix
title: "[DATA] <concise dataset name>"
labels: data, enhancement
assignees: ""
---

## 1) Overview

**Dataset name**  
**Short description** (what it is, why it matters)  
**Primary use case(s)** (layers/timelines/AI reasoning it enables)

---

## 2) Source & Licensing

- **Source organization / URL**:  
- **Original citation / DOI (if any)**:  
- **License**: `CC-BY / CC-BY-NC / Public Domain / Other`  
- **Redistribution allowed?** yes / no / unclear  
- **Attribution text required?** Provide exact string if specified.

> We require clear provenance and legal status before ingestion (MCP reproducibility & traceability).:contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}

---

## 3) Access & Size

- **Acquisition method**: direct HTTP | API | portal | S3 | request-only
- **File(s) / endpoints**: list URLs or API queries
- **Estimated size**: (per file and total)
- **Proposed storage**: DVC (preferred for large data) / Git LFS / small in-repo
- **Checksum(s)**: md5/sha256 if available
- **Mirroring needed?** yes/no (explain)

> Large rasters/vectors should be DVC/LFS rather than committed directly.:contentReference[oaicite:2]{index=2}

---

## 4) Data Profile (geospatial)

- **Type**: raster (DEM/COG), vector (points/lines/polys), tiles, docs
- **Format(s)**: GeoTIFF/COG, GeoJSON, Shapefile, MBTiles, CSV, PDF, KML/KMZ
- **CRS**: `EPSG:4326 / EPSG:3857 / other`
- **Resolution / scale**: (e.g., 1 m DEM, 1:24k topo)
- **Spatial extent (bbox)**: `minx, miny, maxx, maxy`
- **Temporal coverage**: single date / range; list years/editions where applicable
- **Known quirks**: nodata values, tiling, projection oddities, missing metadata

---

## 5) STAC / Catalog Entry (proposed)

Provide the STAC-like JSON (or `data/sources/*.json`) you propose to add, with:
- `id`, `title`, `description`
- `bbox`, `datetime` or `start_datetime`/`end_datetime`
- `assets` (href, type, roles), `license`, `providers`
- Any processing notes (COG/tiling), and links back to the original source

> The repo uses a STAC-style catalog to register layers and drive the static viewer & pipeline.:contentReference[oaicite:3]{index=3}

```json
{
  "id": "<your-id>",
  "title": "<human-readable>",
  "description": "<what this dataset is>",
  "license": "CC-BY-4.0",
  "extent": {
    "spatial": { "bbox": [[minx, miny, maxx, maxy]] },
    "temporal": { "interval": [["YYYY-MM-DD", "YYYY-MM-DD"]] }
  },
  "assets": {
    "source": {
      "href": "https://…/file.tif",
      "type": "image/tiff; application=geotiff",
      "roles": ["data", "source"]
    }
  },
  "providers": [
    { "name": "Org", "roles": ["producer","licensor"], "url": "https://…" }
  ]
}


