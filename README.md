<div align="center">

# 💧 Kansas Frontier Matrix — Processed Hydrology Data  
### **Flow · Terrain · Reproducibility** — *Hydrologic foundation layers for Kansas Frontier Matrix*

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../.github/workflows/site.yml)  
[![STAC Validate](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/stac-validate.yml?label=STAC%20Validate)](../../../.github/workflows/stac-validate.yml)  
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../.github/workflows/codeql.yml)  
[![Trivy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/trivy.yml?label=Trivy)](../../../.github/workflows/trivy.yml)  
[![Docs: MCP](https://img.shields.io/badge/Docs-Master%20Coder%20Protocol-6f42c1)](../../../docs/)  
[![License](https://img.shields.io/badge/license-MIT%20(code)%20%7C%20CC--BY%20(data)-blue)](../../../LICENSE)

**Hydrologically conditioned DEMs, flow direction, accumulation, and water masks**  
for reproducible terrain and watershed modeling across Kansas.

</div>

---

## 🌊 Overview

This directory contains **processed hydrologic surfaces and layers** generated from  
DEM preprocessing, flow-routing, and conditioning workflows.

These datasets underpin hydrologic and geomorphic derivatives:  
**flow accumulation, stream extraction, watershed segmentation, and flood modeling.**

**Sources:**  
LiDAR 1 m DEMs (Kansas DASC / USGS 3DEP), historical 10–30 m DEMs, NLCD water, NHD hydrography, and GNIS features.  
**Standards:** Cloud-Optimized GeoTIFF (COG) for rasters, GeoJSON for vectors, EPSG 4326 (WGS84).  
**Catalog:** Indexed under `data/stac/items/hydro_*`.

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
Filled DEM	dem_filled_1m_ks.tif	1 m LiDAR DEM with sink filling for hydrologic continuity	KS LiDAR / USGS 3DEP	m	COG GeoTIFF
Flow Direction (D8)	flow_dir_d8_1m_ks.tif	Downslope pointer grid (ESRI D8 model 1–128)	Derived (WhiteboxTools)	int	COG GeoTIFF
Flow Accumulation (Base)	flow_accum_base_1m_ks.tif	Raw accumulation before stream thresholding	Derived (WhiteboxTools)	cells	COG GeoTIFF
Water Mask	watermask_ks.tif	Binary mask fused from NLCD water + NHD hydrography (1 = water)	USGS / DASC	binary	COG GeoTIFF
Stream Seed Points	stream_seed_points.geojson	Candidate outlets / pour points for watershed delineation	Derived	n/a	GeoJSON


⸻

🧩 STAC Metadata Example

{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "flow_dir_d8_1m_ks",
  "properties": {
    "title": "Flow Direction (D8) – Kansas LiDAR DEM",
    "description": "D8 pointer grid derived from hydro-conditioned 1 m DEM.",
    "datetime": "2020-01-01T00:00:00Z",
    "processing:software": "WhiteboxTools 2.2.0",
    "processing:steps": ["FillDepressions", "D8Pointer"],
    "derived_from": ["data/processed/hydrology/dem_filled_1m_ks.tif"],
    "license": "CC-BY 4.0"
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
  A["Raw DEMs\n(1 m / 10–30 m)"] --> B["Fill Depressions\n(WhiteboxTools)"]
  B --> C["D8 Flow Direction\n(D8Pointer)"]
  B --> D["D8 Flow Accumulation\n(D8FlowAccumulation)"]
  C & D --> E["Seed Point Extraction\n(threshold logic)"]
  F["NLCD Water +\nNHD Hydrography"] --> G["Water Mask\n(GDAL Calc)"]
  B & C & D & E & G --> H["Reproject to EPSG:4326\n(GDAL Warp)"]
  H --> I["Convert to COG\n(rio cogeo create)"]
  I --> J["Visual QC / Validation\n(QGIS vs NHD)"]
  I --> K["Emit STAC Items\n(STAC 1.0 schema)"]
  I --> L["Compute Checksums\n(SHA-256)"]
  K & L --> M["Continuous Integration\n(STAC validate · hash verify)"]
%% END OF MERMAID

Example CLI

whitebox_tools --run=FillDepressions -i dem_1m_ks.tif -o dem_filled_1m_ks.tif
whitebox_tools --run=D8Pointer -i dem_filled_1m_ks.tif -o flow_dir_d8_1m_ks.tif
whitebox_tools --run=D8FlowAccumulation -i dem_filled_1m_ks.tif -o flow_accum_base_1m_ks.tif
gdal_calc.py -A nlcd_water_ks.tif -B nhd_water_ks.tif \
  --outfile=watermask_ks.tif --calc="((A>0)|(B>0)).astype(uint8)"
python tools/hydro/seed_points.py --accum flow_accum_base_1m_ks.tif --threshold 500


⸻

🔁 Reproducibility & Validation

Check	Method
Integrity	SHA-256 hash verification in CI
Metadata	STAC 1.0 schema validation (make stac-validate)
Pipeline	make hydrology or make validate-hydro
Environment	Docker (GDAL + WhiteboxTools + Python)
QA/QC	Visual inspection in QGIS vs NHD streams


⸻

🧠 Contributing

1️⃣ Add new COG or GeoJSON outputs.
2️⃣ Create STAC metadata → metadata/ and checksum → checksums/.
3️⃣ Add DERIVATION.md detailing inputs, tools, parameters.
4️⃣ Validate locally → make validate-hydro.
5️⃣ Submit PR with sources, licenses, and visual examples.

All new data must pass STAC and checksum validation before merge.

⸻

📖 References
	•	WhiteboxTools: https://www.whiteboxgeo.com/manual/wbt_book/hydro.html
	•	TauDEM: https://hydrology.usu.edu/taudem
	•	GDAL: https://gdal.org
	•	USGS NHD: https://www.usgs.gov/national-hydrography
	•	Kansas DASC Hub: https://hub.kansasgis.org
	•	STAC 1.0 Spec: https://stacspec.org
	•	MCP Docs: docs/standards/

⸻


<div align="center">


“From high plains to river valleys — these grids trace the flow that carved Kansas’s landscape.”

</div>
