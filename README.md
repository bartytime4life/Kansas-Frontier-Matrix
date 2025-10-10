<div align="center">

# 💧 Kansas Frontier Matrix — Processed Hydrology Data  
### **Flow · Terrain · Reproducibility** — *Hydrologic foundation layers for Kansas Frontier Matrix*

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/stac-validate.yml?label=STAC%20Validate)](../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/trivy.yml?label=Trivy)](../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-6f42c1)](../../../docs/)
[![License](https://img.shields.io/badge/license-MIT%20%7C%20CC--BY--4.0-blue)](../../../LICENSE)

**Hydrologically conditioned DEMs, flow direction, accumulation, and water masks**  
powering **reproducible watershed, stream, and flood modeling** across Kansas.

</div>

---

## 1) Overview

Processed hydrologic layers produced from DEM conditioning and flow routing. These underpin:

- Stream extraction & basin delineation  
- Flood/runoff modeling & hazard analysis  
- Watershed & terrain morphology studies  
- Historical hydrology comparison & climate linkage

**Primary Sources:** LiDAR 1 m DEMs (Kansas DASC / USGS 3DEP), historic 10–30 m DEMs, NLCD Water, NHD hydrography  
**Formats:** COG GeoTIFF (rasters) • GeoJSON (vectors) • EPSG:4326 (WGS84)  
**Catalog:** STAC items under `data/stac/items/hydro_*`  

---

## 2) Data Products

| Product | File | Description | Source | Units | Format |
|:--|:--|:--|:--|:--|:--|
| Filled DEM | `dem_filled_1m_ks.tif` | Hydrologically conditioned/sink-filled DEM (1 m) | KS LiDAR / USGS 3DEP | m | COG GeoTIFF |
| Flow Direction (D8) | `flow_dir_d8_1m_ks.tif` | D8 pointer grid (1–128) | Derived (WhiteboxTools) | int | COG GeoTIFF |
| Flow Accumulation | `flow_accum_base_1m_ks.tif` | Raw accumulation (pre-threshold) | Derived (WhiteboxTools) | cells | COG GeoTIFF |
| Water Mask | `watermask_ks.tif` | Binary water layer (NLCD + NHD fusion) | USGS / DASC | binary | COG GeoTIFF |
| Stream Seeds | `stream_seed_points.geojson` | Candidate outlets/pour points | Derived | n/a | GeoJSON |

---

## 3) Directory Layout

```bash
data/
└── processed/
    └── hydrology/
        ├── dem_filled_1m_ks.tif
        ├── flow_dir_d8_1m_ks.tif
        ├── flow_accum_base_1m_ks.tif
        ├── watermask_ks.tif
        ├── stream_seed_points.geojson
        ├── metadata/
        │   ├── dem_filled_1m_ks.json
        │   ├── flow_dir_d8_1m_ks.json
        │   └── flow_accum_base_1m_ks.json
        ├── checksums/
        │   ├── dem_filled_1m_ks.tif.sha256
        │   ├── flow_dir_d8_1m_ks.tif.sha256
        │   └── flow_accum_base_1m_ks.tif.sha256
        └── README.md


⸻

4) Processing Workflow (GitHub-safe Mermaid)

flowchart TD
  A["Raw DEMs (1 m / 10–30 m)"] --> B["Fill Depressions\nWhiteboxTools FillDepressions"]
  B --> C["D8 Flow Direction\nWhiteboxTools D8Pointer"]
  B --> D["D8 Flow Accumulation\nWhiteboxTools D8FlowAccumulation"]
  C --> E["Seed Point Extraction\nThreshold Logic"]
  D --> E
  F["NLCD Water + NHD Hydrography"] --> G["Water Mask\nGDAL Calc"]
  B --> H["Reproject to EPSG:4326\nGDAL Warp"]
  C --> H
  D --> H
  E --> H
  G --> H
  H --> I["Convert to COG\nrio cogeo create"]
  I --> J["Visual QC / Validation\nQGIS vs NHD"]
  I --> K["Emit STAC Items\nSTAC 1.0"]
  I --> L["Compute Checksums\nSHA-256"]
  K --> M["CI Validation\nSTAC Validate · Hash Verify"]
  L --> M

<!-- END OF MERMAID -->



⸻

5) STAC Item (example)

{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "flow_dir_d8_1m_ks",
  "properties": {
    "title": "Flow Direction (D8) – Kansas LiDAR DEM",
    "datetime": "2020-01-01T00:00:00Z",
    "processing:software": "WhiteboxTools 2.2.0",
    "derived_from": ["data/processed/hydrology/dem_filled_1m_ks.tif"],
    "license": "CC-BY-4.0"
  },
  "assets": {
    "data": {
      "href": "./flow_dir_d8_1m_ks.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"]
    }
  },
  "bbox": [-102.05, 36.99, -94.59, 40.00]
}


⸻

6) Reproducibility & Validation

Check	Command / Method
Integrity	sha256sum -c checksums/*.sha256 (CI verifies)
STAC Schema	make stac-validate
Pipeline	make hydrology or make validate-hydro
Environment	Docker (GDAL + WhiteboxTools + Python)
QA/QC	Visual cross-check in QGIS vs NHD

Make targets (typical):

make hydrology         # build hydrology products
make stac-validate     # validate STAC items
make validate-hydro    # checksum + STAC + spot checks


⸻

7) Contributing
	1.	Add new COG/GeoJSON outputs to this folder.
	2.	Create matching STAC JSON under metadata/ and SHA-256 in checksums/.
	3.	Record inputs, params, and software versions in DERIVATION.md.
	4.	Run make validate-hydro locally.
	5.	Open a PR with sources, licenses, and (ideally) a preview PNG.

Gate: all items must pass checksums + STAC validation before merge.

⸻

8) References
	•	GDAL Documentation
	•	WhiteboxTools Manual
	•	TauDEM Toolkit
	•	USGS NHD
	•	Kansas DASC Geoportal
	•	STAC 1.0.0 Specification
	•	MCP (Master Coder Protocol) docs

⸻


<div align="center">


From high plains to river valleys — these grids trace the flow that carved Kansas’s landscape.

</div>
```
