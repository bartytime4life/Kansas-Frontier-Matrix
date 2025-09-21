name: "🧩 Data addition request"
about: Propose a new dataset (map, layer, catalog, or document set) for Kansas-Frontier-Matrix
title: "[DATA] <concise dataset name>"
labels: ["data", "enhancement"]
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
- **License**: `CC-BY` / `CC0` / `Public Domain` / `Other (specify)`  
- **Redistribution allowed?** yes / no / unclear  
- **Attribution text required?** Provide exact string if specified.

> We require clear provenance and legal status **before ingestion** (MCP reproducibility & traceability).

---

## 3) Access & Size

- **Acquisition method**: direct HTTP | API | portal | S3 | request-only  
- **File(s) / endpoints**: list URLs or API queries  
- **Estimated size**: (per file and total)  
- **Proposed storage**: **DVC** (preferred for large data) / **Git LFS** / small in-repo  
- **Checksum(s)**: md5/sha256 if available  
- **Mirroring needed?** yes/no (explain)

> Large rasters/vectors should use **DVC/LFS** rather than plain Git.

---

## 4) Data Profile (geospatial)

- **Type**: raster (DEM/COG), vector (points/lines/polys), tiles, docs  
- **Format(s)**: GeoTIFF/COG, GeoJSON, Shapefile, MBTiles, CSV, PDF, KML/KMZ  
- **CRS**: `EPSG:4326` / `EPSG:3857` / other  
- **Resolution / scale**: (e.g., 1 m DEM, 1:24k topo)  
- **Spatial extent (bbox)**: `minx, miny, maxx, maxy`  
- **Temporal coverage**: single date / range; list years/editions where applicable  
- **Known quirks**: nodata values, tiling, projection oddities, missing metadata

---

## 5) Proposed Catalog Entry (STAC-style)

Provide either a **STAC Item/Collection** (preferred: `stac/items/**` / `stac/collections/**`) or a **source descriptor** (`data/sources/*.json`) with:

- `id`, `title`, `description`  
- `bbox`, `datetime` or `start_datetime`/`end_datetime`  
- `assets` (href, type, roles), `license`, `providers`  
- Processing notes (COG/tiling), and link(s) back to the original source

```json
{
  "stac_version": "1.0.0",
  "type": "Collection",
  "id": "<your-id>",
  "title": "<human-readable>",
  "description": "<what this dataset is>",
  "license": "CC-BY-4.0",
  "extent": {
    "spatial": { "bbox": [[minx, miny, maxx, maxy]] },
    "temporal": { "interval": [["YYYY-MM-DDT00:00:00Z", "YYYY-MM-DDT23:59:59Z"]] }
  },
  "providers": [
    { "name": "Org", "roles": ["producer", "licensor"], "url": "https://…" }
  ],
  "links": [
    { "rel": "self", "href": "./<file>.json", "type": "application/json" },
    { "rel": "root", "href": "../catalog.json", "type": "application/json" }
  ]
}
````

*Or a minimal **Item** (for a single layer/COG):*

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "<item-id>",
  "collection": "<collection-id>",
  "bbox": [minx, miny, maxx, maxy],
  "geometry": { "type": "Polygon", "coordinates": [[ [minx,miny], [maxx,miny], [maxx,maxy], [minx,maxy], [minx,miny] ]] },
  "properties": {
    "start_datetime": "YYYY-01-01T00:00:00Z",
    "end_datetime":   "YYYY-12-31T23:59:59Z",
    "datetime": null
  },
  "assets": {
    "data": {
      "href": "path/or/url/to.cog.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"]
    }
  },
  "links": [
    { "rel": "collection", "href": "../collections/<collection>.json" },
    { "rel": "parent",     "href": "../collections/<collection>.json" },
    { "rel": "root",       "href": "../catalog.json" }
  ]
}
```

---

## 6) Integration Plan

* **Placement in timeline / UI**: suggested year(s), opacity, style cues
* **Derivatives**: hillshade/slope/aspect, tiles, thumbnails (if raster)
* **Provenance surface**: how/where attribution should appear in UI
* **Backlinks**: docs/story pages that will reference this dataset

---

## 7) Validation & Repro Steps

**Commands to fetch/prepare (proposed):**

```bash
# minimal deterministic sequence; prefer Make targets
make fetch         # if applicable
make cogs          # COG conversion
make stac          # (re)generate catalog entries
make site          # update static viewer
```

**Checks to run:**

```bash
# STAC validation (requires kgt/jsonschema if installed)
kgt validate-stac stac/items --no-strict || true
```

---

## 8) Risks / Constraints

* Licenses / usage restrictions: …
* Sensitive locations or cultural heritage concerns: …
* Data quality / uncertainty notes: …

---

## Checklist

* [ ] Source & license verified (redistribution OK or documented)
* [ ] Size estimated; storage plan (**DVC/LFS/in-repo**) chosen
* [ ] CRS, bbox, time coverage specified
* [ ] Draft **STAC** (Item/Collection) or **source descriptor** provided
* [ ] Proposed Make targets / commands listed
* [ ] Validation steps noted (`kgt validate-stac`, JSON sanity)
* [ ] UI placement (timeline/style) proposed

```
```
