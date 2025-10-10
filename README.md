<div align="center">

# 💧 Kansas Frontier Matrix — Processed Hydrology Data  
### **Flow · Terrain · Reproducibility** — *Hydrologic foundation layers for Kansas Frontier Matrix*

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/stac-validate.yml?label=STAC%20Validate)](../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/trivy.yml?label=Trivy)](../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-Master%20Coder%20Protocol-6f42c1)](../../../docs/)
[![License](https://img.shields.io/badge/license-MIT%20(code)%20%7C%20CC--BY--4.0%20(data)-blue)](../../../LICENSE)

**Hydrologically conditioned DEMs, flow direction, accumulation, and water masks**  
powering **reproducible watershed, stream, and flood modeling** across Kansas.

</div>

---

## 🌊 Overview

This directory contains **processed hydrologic layers** produced from DEM preprocessing,  
flow-routing, and terrain conditioning workflows. These form the geospatial base for:

- Stream network extraction & basin delineation  
- Flood and runoff modeling  
- Watershed & terrain morphology analysis  
- Historical hydrology comparison and climate-hydrology modeling  

**Primary Sources:**  
- LiDAR 1 m DEMs (Kansas DASC / USGS 3DEP)  
- Historic 10–30 m DEMs  
- NLCD Water and NHD Hydrography layers  
- GNIS geographic features  

**Formats:** COG GeoTIFF (rasters) • GeoJSON (vectors) • EPSG 4326 (WGS84)  
**Indexed In:** `data/stac/items/hydro_*` for discovery, validation, and API access  

---

## 🧱 Directory Layout
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

💦 Core Datasets

Product	File	Description	Source	Units	Format
Filled DEM	dem_filled_1m_ks.tif	Hydrologically conditioned 1 m DEM (sink-filled)	KS LiDAR / USGS 3DEP	m	COG GeoTIFF
Flow Direction (D8)	flow_dir_d8_1m_ks.tif	D8 flow direction grid (1–128 pointers)	Derived via WhiteboxTools	int	COG GeoTIFF
Flow Accumulation (Base)	flow_accum_base_1m_ks.tif	Raw accumulation (pre-threshold)	Derived via WhiteboxTools	cells	COG GeoTIFF
Water Mask	watermask_ks.tif	Binary water layer (NLCD + NHD fusion)	USGS / DASC	binary	COG GeoTIFF
Stream Seeds	stream_seed_points.geojson	Candidate outlets / pour points for basins	Derived	n/a	GeoJSON


⸻

🧩 STAC Metadata Example

{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "flow_dir_d8_1m_ks",
  "properties": {
    "title": "Flow Direction (D8) – Kansas LiDAR DEM",
    "datetime": "2020-01-01T00:00:00Z",
    "processing:software": "WhiteboxTools 2.2.0",
    "mcp_provenance": "sha256:4be51c...",
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

⚙️ Processing Workflow

flowchart TD
  A["Raw DEMs (1 m / 10–30 m)"] --> B["Fill Depressions\nWhiteboxTools FillDepressions"]
  B --> C["D8 Flow Direction\nWhiteboxTools D8Pointer"]
  B --> D["D8 Flow Accumulation\nWhiteboxTools D8FlowAccumulation"]
  C & D --> E["Seed Point Extraction\nThreshold Logic"]
  F["NLCD Water + NHD Hydrography"] --> G["Water Mask\nGDAL Calc"]
  B & C & D & E & G --> H["Reproject → EPSG:4326\nGDAL Warp"]
  H --> I["Convert → COG\nrio cogeo create"]
  I --> J["Visual QC / Validation\nQGIS vs NHD"]
  I --> K["Emit STAC Items\nSTAC 1.0 Schema"]
  I --> L["Compute Checksums\nSHA-256"]
  K & L --> M["Continuous Integration\nSTAC Validate · Hash Verify"]

<!-- END OF MERMAID -->



⸻

🔁 Reproducibility & Validation

Check	Method
Integrity	SHA-256 hash verification (CI pipeline)
Metadata	STAC 1.0 schema validation (make stac-validate)
Pipeline Run	make hydrology or make validate-hydro
Environment	Docker (GDAL + WhiteboxTools + Python)
QA/QC	Visual inspection (QGIS vs NHD streams)


⸻

🧠 Contributing

1️⃣ Add new COG or GeoJSON outputs.
2️⃣ Create matching STAC metadata (metadata/) and checksums (checksums/).
3️⃣ Record inputs and software in DERIVATION.md.
4️⃣ Run make validate-hydro to verify.
5️⃣ Submit PR with sources, licenses, and (preferably) a preview image.

✅ All data must pass STAC and checksum validation before merge.

⸻

📖 References
	•	WhiteboxTools Manual
	•	TauDEM Toolkit
	•	GDAL Documentation
	•	USGS NHD
	•	Kansas DASC Geoportal
	•	STAC 1.0 Specification
	•	Master Coder Protocol Docs

⸻


<div align="center">


“From high plains to river valleys — these grids trace the flow that carved Kansas’s landscape.”

</div>
```
