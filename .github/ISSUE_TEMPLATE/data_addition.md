<div align="center">

# 🧩 Kansas-Frontier-Matrix — Data Addition Request

<!-- Core CI/CD -->
[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../actions/workflows/site.yml)  
[![Tests](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/tests.yml/badge.svg)](../../actions/workflows/tests.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../actions/workflows/stac-validate.yml)  
[![STAC Badges](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](../../actions/workflows/stac-badges.yml)  

<!-- Security -->
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../actions/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../actions/workflows/trivy.yml)  
[![Secret Scanning](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/secret-scanning.yml/badge.svg)](../../actions/workflows/secret-scanning.yml)  
[![OpenSSF Scorecard](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/ossf-scorecard.yml/badge.svg)](../../actions/workflows/ossf-scorecard.yml)  

<!-- Governance -->
[![Roadmap Sync](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/roadmap.yml/badge.svg)](../../actions/workflows/roadmap.yml)  
[![Labels Sync](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/labels.yml/badge.svg)](../../actions/workflows/labels.yml)  
[![PR Labeler](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pr-labeler.yml/badge.svg)](../../actions/workflows/pr-labeler.yml)  
[![Automerge](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/automerge.yml/badge.svg)](../../actions/workflows/automerge.yml)  

<!-- Repo Hygiene -->
![Dependabot](https://img.shields.io/badge/Dependabot-enabled-brightgreen?logo=dependabot)  
![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)  
![License](https://img.shields.io/github/license/bartytime4life/Kansas-Frontier-Matrix)  

</div>

---

## 1) Overview

- **Dataset name**:  
- **Short description** — what it is, why it matters  
- **Primary use case(s)** — layers, timelines, story themes, or AI reasoning it enables  

---

## 2) Source & Licensing

- **Source organization / URL**:  
- **Original citation / DOI (if any)**:  
- **License**: `CC-BY` / `CC0` / `Public Domain` / `Other (specify)`  
- **Redistribution allowed?** yes / no / unclear  
- **Required attribution string**:  

> ✅ We require clear **provenance** and **legal status** before ingestion.

---

## 3) Access & Size

- **Acquisition method**: direct HTTP | API | portal | S3 | request-only  
- **File(s) / endpoints**: list URLs or API queries  
- **Estimated size**: per-file and total  
- **Proposed storage**: **DVC** (preferred for large data) / **Git LFS** / small in-repo  
- **Checksum(s)**: sha256 if available  
- **Mirroring needed?** yes/no (explain)  

> ⚠️ Large rasters/vectors should use **DVC/LFS**, not plain Git.

---

## 4) Data Profile (geospatial)

- **Type**: raster (DEM/COG), vector (points/lines/polys), tiles, docs  
- **Format(s)**: GeoTIFF/COG, GeoJSON, Shapefile, MBTiles/PMTiles, CSV, PDF, KML/KMZ  
- **CRS**: `EPSG:4326` | `EPSG:3857` | other  
- **Resolution / scale**: e.g., 1 m DEM, 1:24k topo  
- **Spatial extent (bbox)**: `minx, miny, maxx, maxy`  
- **Temporal coverage**: single date / range (list years/editions)  
- **Known quirks**: nodata values, tiling, projection oddities, metadata gaps  

---

## 5) Proposed Catalog Entry (STAC-style)

Provide either a **STAC Collection/Item** (`stac/collections/**`, `stac/items/**`) or a **source descriptor** (`data/sources/*.json`).

<details>
<summary>Example Collection</summary>

```json
{
  "stac_version": "1.0.0",
  "type": "Collection",
  "id": "<collection-id>",
  "title": "<human-readable>",
  "description": "<what this dataset is>",
  "license": "CC-BY-4.0",
  "extent": {
    "spatial": { "bbox": [[minx, miny, maxx, maxy]] },
    "temporal": { "interval": [["YYYY-MM-DDT00:00:00Z", "YYYY-MM-DDT23:59:59Z"]] }
  },
  "providers": [
    { "name": "Org", "roles": ["producer", "licensor"], "url": "https://example.org" }
  ],
  "links": [
    { "rel": "self",   "href": "./<file>.json", "type": "application/json" },
    { "rel": "root",   "href": "../catalog.json", "type": "application/json" },
    { "rel": "parent", "href": "../catalog.json", "type": "application/json" }
  ]
}
````

</details>

<details>
<summary>Example Item</summary>

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "<item-id>",
  "collection": "<collection-id>",
  "bbox": [minx, miny, maxx, maxy],
  "geometry": {
    "type": "Polygon",
    "coordinates": [[[minx, miny], [maxx, miny], [maxx, maxy], [minx, maxy], [minx, miny]]]
  },
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
    { "rel": "collection", "href": "../../collections/<collection>.json" },
    { "rel": "parent",     "href": "../../collections/<collection>.json" },
    { "rel": "root",       "href": "../../catalog.json" }
  ]
}
```

</details>

> If proposing web wiring, include a `legendKey` and `category` for the viewer.

---

## 6) Integration Plan (Viewer & Config)

* **Timeline placement**: suggested year(s) / range
* **Legend & category**: symbol in `web/config/legend.json`, group in `web/config/categories.json`
* **Attribution**: string for UI
* **Derivatives**: tiles (PNG/JPEG `{z}/{x}/{y}.png`), hillshade/slope/aspect, thumbnails (if raster)

**Optional layer block (viewer wiring):**

```json
{
  "id": "<layer-id>",
  "title": "<Layer Title>",
  "group": "<Sidebar Group>",
  "type": "geojson",
  "data": "data/processed/<file>.geojson",
  "style": { "lineColor": "#118AB2", "lineWidth": 1.2 },
  "visible": true,
  "time": { "start": "YYYY-01-01", "end": null },
  "legendKey": "<symbol-id>",
  "attribution": "<source / license>"
}
```

---

## 7) Validation & Repro Steps (proposed)

**Commands**

```bash
make fetch           # if applicable
make cogs            # COG conversion
make stac            # (re)generate catalog entries
make site            # update fallback viewer config
make site-config     # render STAC → web/app.config.json
```

**Checks**

```bash
kgt validate-stac stac/items --no-strict || true
make config-validate || true
jq -e 'type == "object"' stac/items/**/*.json
```

---

## 8) Risks / Constraints

* Licenses / usage restrictions: …
* Sensitive locations / heritage concerns: …
* Data quality / uncertainty notes: …

---

## 📑 Roadmap Link (if applicable)

* Milestone: …
* Related epic/issue: …
* Roadmap marker:

  ```
  <!-- roadmap:key=data-<stable-key> -->
  ```

---

## ✅ Checklist

* [ ] Source & license verified (redistribution OK or documented)
* [ ] Size estimated; storage plan (**DVC/LFS/in-repo**) chosen
* [ ] CRS, bbox, temporal coverage specified
* [ ] Draft **STAC** (Item/Collection) or **source descriptor** provided
* [ ] Proposed Make targets / commands listed
* [ ] Validation steps noted (`kgt validate-stac`, `make config-validate`)
* [ ] UI placement (timeline/legend/category) proposed
