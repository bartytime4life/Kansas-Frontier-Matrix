---
title: "🗺️ Kansas Frontier Matrix — Coordinate Reference System (CRS) Standard (Legacy v11.0.0)"
path: "docs/standards/geo/crs-standard.md"

version: "v11.0.0"
last_updated: "2025-11-22"

release_stage: "Superseded / Legacy"
lifecycle: "Retired (Read-Only)"
review_cycle: "None (superseded by CRS, Geometry & Topology v11.2.4)"
content_stability: "frozen"
status: "Superseded"

doc_kind: "Standard (Legacy)"
semantic_document_id: "kfm-crs-standard-v11"
doc_uuid: "urn:kfm:docs:standards:geo:crs-standard:v11"
immutability_status: "version-pinned"

commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../releases/v11.0.0/standards-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/standards-crs-v11.json"

governance_ref: "../governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4 (backfilled)"
accessibility_compliance: "WCAG 2.1 AA+"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
machine_extractable: true
classification: "Public"
jurisdiction: "Kansas / United States"

superseded_by: "docs/standards/geospatial/crs-topology/README.md@v11.2.4"
---

<div align="center">

# 🗺️ **Kansas Frontier Matrix — CRS Standard (Legacy v11.0.0)**  
`docs/standards/geo/crs-standard.md`

> **Legacy Notice (v11.2.4):**  
> This document is preserved as a **historic CRS standard for KFM v11.0.0**.  
> The **active, enforceable CRS specification** now lives at:  
> `docs/standards/geospatial/crs-topology/README.md` (📐 *CRS, Geometry & Topology Governance Standard*).

**Purpose (Legacy):**  
Capture the original v11.0.0 rules for allowed CRSs, reprojection pipelines, metadata requirements, STAC/DCAT alignment, PROV lineage, and MapLibre/Cesium rendering constraints for KFM geospatial datasets.

</div>

---

## 📘 Overview (Legacy Context)

In KFM v11.0.0 this standard ensured consistent, deterministic CRS usage across:

- ETL pipelines  
- STAC catalogs  
- COG rasters and GeoJSON vectors  
- NetCDF/CF datasets  
- Neo4j spatial nodes  
- API responses  
- MapLibre 2D and Cesium 3D rendering  
- Story Nodes (v3) and Focus Mode  

It mandated:

- **Strict CRS safety** — no “mystery projections.”  
- **Traceable transformations** — all reprojections with PROV-O lineage.  
- **Orthometric alignment** — CRS behavior coordinated with vertical/DoD standards.

> 🔁 **For current behavior**, always consult:  
> `docs/standards/geospatial/crs-topology/README.md`.

---

## 🧭 Allowed CRSs in KFM v11.0.0 (Closed Set – Legacy)

To ensure consistency and 3D compatibility, KFM v11.0.0 restricted all datasets to two CRS families.

### 1. Geographic CRS (Global)

**EPSG:4326 — WGS84 (lat/long)**  

- Required for:  
  - STAC geometry  
  - GeoJSON  
  - Story Nodes  
  - Cesium 3D globe  
- Units: **degrees**

### 2. Projected CRS (Kansas Operational)

**EPSG:26914 — NAD83 / UTM Zone 14N**

- Required for:  
  - DEM processing  
  - Hydrology grids  
  - Lidar workflows  
  - DoD generation pipelines  
  - High-resolution raster ETL  
- Units: **meters**

> ✅ These roles are now refined and generalized in the v11.2.4 **CRS, Geometry & Topology Governance Standard**.

---

## 📐 CRS Metadata Requirements (Legacy)

Every dataset **had to** declare CRS explicitly in multiple layers of metadata.

### 1. STAC Item Fields

~~~json
{
  "proj:epsg": 4326,
  "proj:wkt2": "<WKT2 string>",
  "proj:shape": [2048, 2048],
  "proj:transform": [30, 0, -102.05, 0, -30, 40.0]
}
~~~

### 2. Raster (GeoTIFF/COG) Tags

Required GeoTIFF keys:

- `GTModelTypeGeoKey`  
- `GTRasterTypeGeoKey`  
- `GeographicTypeGeoKey`  
- `ProjectedCSTypeGeoKey`  
- `GeogAngularUnitsGeoKey`  
- `ProjLinearUnitsGeoKey`  

### 3. GeoJSON

~~~text
CRS MUST be WGS84 (EPSG:4326)
GeoJSON CRS overrides are NOT allowed.
~~~

### 4. NetCDF / CF (for EPSG:26914-style grids)

~~~text
grid_mapping_name           = "transverse_mercator"
longitude_of_central_meridian = -99
latitude_of_projection_origin = 0
false_easting                = 500000
false_northing               = 0
~~~

---

## 🔄 Reprojection Requirements (ETL v11.0.0)

All reprojections were required to:

1. Be deterministic.  
2. Record provenance using PROV-O.  
3. Preserve Z-axis separately from XY.  
4. Use **GDAL ≥ 3.8** with **PROJ ≥ 9**.  
5. Never alter vertical datum during XY reprojection (vertical handled by vertical/DoD standard).

### 1. Transformation Logging (Legacy Contract)

ETL was required to log at least:

~~~text
source_epsg
target_epsg
transform_parameters
gdal_version
proj_version
prov:activity = "crs-transform-v11"
~~~

### 2. Rasters: Typical Reprojection Pipeline

~~~text
gdalwarp -t_srs EPSG:4326 -r bilinear -co COMPRESS=LZW -co TILED=YES input.tif output_epsg4326.tif
~~~

### 3. Vectors: Typical Pipeline

~~~text
ogr2ogr -t_srs EPSG:4326 output.geojson input.shp
~~~

> ℹ️ In v11.2.4, these pipelines are captured and generalized as part of the **CRS/topology** and **ETL** standards, with PROV bundles referenced via `kfm:crs_transform_ref`.

---

## 🛰 CRS in STAC Collections (Legacy Rules)

Collections were required to declare:

~~~json
{
  "proj:epsg": 4326,
  "proj:centroid": { "lat": 38.5, "lon": -98.2 },
  "proj:bbox": [-102.05, 36.99, -94.6, 40.0]
}
~~~

Projected collections (e.g., UTM-based processing outputs) also needed geographic equivalents for:

- `proj:epsg`  
- `proj:bbox`  
- Any DCAT `dct:spatial` summary.

---

## 🌐 MapLibre & Cesium Rendering Rules (Legacy)

### 1. MapLibre (2D)

- All vector layers must be in **EPSG:4326** or served via Web Mercator tiles.  
- COG rasters served through standard tile pyramids.  
- Vector tiles required geographic coordinates, with server-side tiling handling CRS conversion.

### 2. Cesium (3D)

- Cesium always consumes **WGS84 ellipsoid** coordinates.  
- Projected rasters (EPSG:26914) had to be reprojected to EPSG:4326 before generating tile sets.  
- Heightmaps required **orthometric heights (NAVD88)** per vertical/DoD standard.

---

## 🧩 Story Node v3 & Focus Mode CRS Rules (Legacy)

Every Story Node was expected to use:

~~~text
spacetime.geometry → EPSG:4326
bbox               → EPSG:4326
crs                → "EPSG:4326"
~~~

Focus Mode v3:

- Automatically reprojected all vector/raster geometries to EPSG:4326 for analysis and overlays.  
- Delegated archaeological and Indigenous-sensitive masking behavior to the **archaeology-sensitive-locations** and **geoprivacy** standards (now moved under `docs/standards/geospatial/`).

---

## 🧬 PROV-O Lineage for CRS Transforms (Legacy)

Every CRS transformation required a PROV description, conceptually:

~~~text
prov:used           → input geometry entity
prov:activity       → "crs-transform-v11"
prov:wasGeneratedBy → gdalwarp/ogr2ogr (with version)
prov:generatedAtTime → timestamp
prov:wasAssociatedWith → KFM ETL agent
~~~

Lineage storage:

- In STAC Item metadata (e.g., `"kfm:lineage"` / `kfm:crs_transform_ref` in newer patterns).  
- In Neo4j as `:TransformationEvent` nodes and relationships.

---

## ⚙ CI/CD Validation (Legacy PR Blockers)

Under v11.0.0, a PR was rejected if:

- Raster CRS was missing.  
- Vector CRS was missing.  
- STAC Item lacked `proj:*` fields.  
- GeoJSON was not EPSG:4326.  
- COG outputs skipped reprojecting to EPSG:4326 where required.  
- Cesium layer was delivered in a non-WGS84 coordinate system.  
- No PROV-O lineage described CRS transforms.  
- CRS metadata was inconsistent across assets in the same dataset or collection.

> ✅ These checks are now superseded by the more general **CRS, Geometry & Topology** CI profiles in v11.2.4.

---

## 🕰 Version History

| Version   | Date       | Status       | Notes                                                                                           |
|----------:|------------|-------------|-------------------------------------------------------------------------------------------------|
| v11.0.0   | 2025-11-22 | Superseded  | Initial v11 CRS standard; defined EPSG:4326 / EPSG:26914 roles, STAC/DCAT alignment, and PROV. |

---

<div align="center">

🗺️ **Kansas Frontier Matrix — CRS Standard (Legacy v11.0.0)**  
Consistent · Deterministic · Interoperable (Historical Baseline)  

📌 **Current CRS rules:** [📐 CRS, Geometry & Topology Governance Standard](../geospatial/crs-topology/README.md)  

[🌎 Geospatial Standards Index](../geospatial/README.md) · [⚖ Governance](../governance/ROOT-GOVERNANCE.md)

</div>
