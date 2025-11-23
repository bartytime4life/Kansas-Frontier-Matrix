---
title: "🗺️ Kansas Frontier Matrix — Coordinate Reference System (CRS) Standard (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/geo/crs-standard.md"
version: "v11.0.0"
last_updated: "2025-11-22"
review_cycle: "Semiannual / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../releases/v11.0.0/standards-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/standards-crs-v11.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Standard"
semantic_document_id: "kfm-crs-standard-v11"
doc_uuid: "urn:kfm:docs:standards:geo:crs-standard:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🗺️ **Kansas Frontier Matrix — CRS Standard (v11)**  
`docs/standards/geo/crs-standard.md`

**Purpose:**  
Define the mandatory coordinate reference systems (CRS), reprojection rules, metadata requirements, STAC/DCAT alignment, geospatial lineage, and MapLibre/Cesium rendering constraints for all KFM v11 geospatial datasets (rasters, vectors, STAC Items, DEMs, DoDs, hydrology layers, and Story Nodes).

</div>

---

# 📘 Overview

This standard ensures consistent, deterministic CRS usage across:

- ETL pipelines  
- STAC catalogs  
- COG rasters and GeoJSON vectors  
- NetCDF/CF datasets  
- Neo4j spatial nodes  
- API responses  
- MapLibre 2D and Cesium 3D rendering  
- Story Nodes (v3) and Focus Mode  

KFM v11 mandates **strict CRS safety**, **traceable transformations**, and **orthometric alignment** for all spatial assets.

---

# 🧭 1. Allowed CRSs in KFM v11 (Closed Set)

To ensure consistency and 3D compatibility, KFM restricts all datasets to **two CRS families**.

## 1.1 Geographic CRS (Global)
**EPSG:4326 — WGS84 (lat/long)**  
- Required for:  
  - STAC geometry  
  - GeoJSON  
  - Story Nodes  
  - Cesium 3D globe  
- Units: **degrees**

## 1.2 Projected CRS (Kansas Operational)
**EPSG:26914 — NAD83 / UTM Zone 14N**  
- Required for:  
  - DEM processing  
  - Hydrology grids  
  - Lidar workflows  
  - DoD generation pipelines  
  - High-resolution raster ETL  
- Units: **meters**

---

# 📐 2. CRS Metadata Requirements

Every dataset **must** declare CRS explicitly in:

### 2.1 STAC Item Fields
```json
"proj:epsg": 4326,
"proj:wkt2": "<WKT2 string>",
"proj:shape": [height, width],
"proj:transform": [a, b, c, d, e, f]
```

### 2.2 Raster (GeoTIFF/COG) Tags
- `GTModelTypeGeoKey`
- `GTRasterTypeGeoKey`
- `GeographicTypeGeoKey`
- `ProjectedCSTypeGeoKey`
- `GeogAngularUnitsGeoKey`
- `ProjLinearUnitsGeoKey`

### 2.3 GeoJSON
```
CRS MUST be WGS84 (EPSG:4326)
```
GeoJSON CRS overrides are **not allowed**.

### 2.4 NetCDF / CF
```
grid_mapping_name = "transverse_mercator"
longitude_of_central_meridian = -99
latitude_of_projection_origin = 0
false_easting = 500000
false_northing = 0
```

---

# 🔄 3. Reprojection Requirements (ETL v11)

All reprojections MUST:

1. Be deterministic  
2. Record provenance using PROV-O  
3. Preserve Z-axis separately from XY  
4. Use GDAL ≥ 3.8 with PROJ ≥ 9  
5. Never alter vertical datum during XY reprojection  

### 3.1 Strict Transformation Matrix Logging
ETL MUST write:
```
source_epsg
target_epsg
transform_parameters
gdal_version
proj_version
prov:activity  "crs-transform-v11"
```

### 3.2 Rasters: Required Reprojection Pipeline
```
gdalwarp -t_srs EPSG:4326 -r bilinear -co COMPRESS=LZW -co TILED=YES
```

### 3.3 Vectors: Required Pipeline
```
ogr2ogr -t_srs EPSG:4326 output.geojson input.shp
```

---

# 🛰 4. CRS in STAC Collections (Mandatory)

Collections MUST declare:

```json
"proj:epsg": 4326,
"proj:centroid": { "lat": 38.5, "lon": -98.2 },
"proj:bbox": [-102.05, 36.99, -94.6, 40.0]
```

Projected (UTM) collections MUST also declare geographic equivalents.

---

# 🌐 5. MapLibre & Cesium Rendering Rules

## 5.1 MapLibre (2D)
- All layers must be **EPSG:4326** or WebMercator tiles  
- COG tiles served through tile pyramid  
- Vector tiles must use geographic coordinates

## 5.2 Cesium (3D)
- Cesium always consumes **WGS84 ellipsoid**  
- Projected rasters MUST be reprojected to EPSG:4326 before tiling  
- Heightmaps must use orthometric heights (NAVD88)  

---

# 🧩 6. Story Node v3 & Focus Mode CRS Rules

Every Story Node:

```
spacetime.geometry → EPSG:4326
bbox                → EPSG:4326
crs                 → "EPSG:4326"
```

Focus Mode v3 MUST:

- Automatically reproject all vector/raster geometries to EPSG:4326  
- Mask archaeological sites per H3 standard (see archaeology-sensitive-locations.md)  

---

# 🧬 7. PROV-O Lineage for CRS Transforms

Every CRS transformation requires:

```
prov:used → input geometry
prov:activity → "crs-transform-v11"
prov:wasGeneratedBy → gdalwarp/ogr2ogr version
prov:generatedAtTime → timestamp
prov:wasAssociatedWith → KFM ETL agent
```

Lineage is stored both:

- In STAC Item → `"kfm:lineage"`  
- In Neo4j via `:TransformationEvent`

---

# ⚙ 8. CI/CD Validation (PR Blockers)

PR is rejected if:

- Raster CRS missing  
- Vector CRS missing  
- STAC Item lacks `proj:*` fields  
- GeoJSON not EPSG:4326  
- COG not reprojected  
- Cesium layer delivered in non-WGS84  
- No PROV-O lineage  
- CRS metadata inconsistent across files  

---

# 🕰 Version History

- **v11.0.0 (2025-11-22):** Initial v11 release with CRS hardening, STAC/DCAT alignment, PROV-O lineage, and deterministic ETL requirements.

---

<div align="center">

**Kansas Frontier Matrix — CRS Standard v11**  
*Consistent · Deterministic · Interoperable*

</div>

---

### 🔗 Footer  
[⬅ Back to Geo Standards](./README.md) · [🛰 Vertical Axis Standard](./vertical-axis-and-dod.md) · [📘 KFM v11 Reference](../../reference/kfm_v11_master_documentation.md)

