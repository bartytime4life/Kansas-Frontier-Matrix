---
title: "🔧 Kansas Frontier Matrix — Remote Sensing Preprocessing Module (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/remote-sensing/preprocessing/README.md"
version: "v10.3.1"
last_updated: "2025-11-14"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/pipelines-remote-sensing-preprocessing-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🔧 **Kansas Frontier Matrix — Remote Sensing Preprocessing Module**  
`src/pipelines/remote-sensing/preprocessing/README.md`

**Purpose:**  
Define the **sensor-specific preprocessing system** for KFM Remote Sensing pipelines (Landsat, Sentinel-1 SAR, Sentinel-2 MSI, NAIP, MODIS/VIIRS).  
This includes **cloud/shadow masking**, **GSD harmonization**, **radiometric & atmospheric correction**, **SAR terrain correction**, **reprojection**, **quality filtering**, and **FAIR+CARE-governed masking** of sensitive AOIs or coordinates.

<img alt="Preprocessing" src="https://img.shields.io/badge/Preprocessing-Geospatial-blue"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Compliant-orange"/>
<img alt="Deterministic" src="https://img.shields.io/badge/Deterministic-Yes-green"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Active-success"/>

</div>

---

## 📘 Overview

The Remote Sensing Preprocessing Module provides the deterministic, reproducible transformation layer that runs **between STAC ingestion and analysis/publishing**.

It supplies pipelines with:

- Clean, cloud-masked, harmonized scenes  
- Reprojected polygons & rasters  
- SAR backscatter in consistent units  
- Derived quality masks & valid-pixel maps  
- Radiometrically normalized optical scenes  
- FAIR+CARE compliant redactions for sensitive AOIs  

This module is imported by:

- LandsatLook ingest  
- Sentinel-2 L2A pipelines  
- Sentinel-1 SAR flood/hazard pipelines  
- Vegetation/spectral indices  
- Drought/thermal detection pipelines  

---

## 🗂️ Directory Layout

~~~~~text
src/pipelines/remote-sensing/preprocessing/
├── README.md                    # This file
│
├── cloud_mask.py                # Optical cloud/shadow/snow masking
├── harmonize_gsd.py             # Resample → unified GSD (10m/30m)
├── reprojection.py              # EPSG:code → EPSG:4326 transforms
├── sar_terrain_correction.py    # RTC for Sentinel-1 GRD
├── sar_speckle_filter.py        # Lee/Refined Lee filters
├── radiometric_normalization.py # Optical/thermal normalization
├── thermal_tools.py             # LST derivation (scale/offset/emissivity)
├── mask_sensitive.py            # CARE-governed masking (H3/generalization)
├── quality_masks.py             # Valid-pixel masks and bitwise QA helpers
└── utils.py                     # Shared helpers (band math, AOI clip, dtype guards)
~~~~~

---

## 🧩 Module Architecture (Indented Mermaid)

~~~~~mermaid
flowchart TD
  A["Raw STAC Assets"] --> B["Preprocessing Layer<br/>cloud_mask · harmonize_gsd · reprojection"]
  B --> C["SAR Tools<br/>terrain_correction · speckle_filter"]
  C --> D["Normalization<br/>optical · thermal"]
  D --> E["Quality Masks<br/>valid_pixel · snow · shadow"]
  E --> F["CARE Masking<br/>sensitive AOIs · H3 generalization"]
  F --> G["Preprocessed Output<br/>raster · metadata · provenance"]
~~~~~

---

## ☁️ cloud_mask.py — Cloud/Shadow/Snow Masking

Implements:

- Fmask-style cloud confidence  
- Sentinel-2 cloud probability integration  
- Snow/ice brightness tests  
- Shadow geometry heuristics  
- Combined mask for optical pipelines  

Generates:

- `cloud_mask` (boolean raster)  
- `valid_pixel_mask`  
- `%cloud_masked` telemetry  

---

## 📏 harmonize_gsd.py — Resampling

Ensures consistent spatial resolution:

- For Landsat: 30m → 30m (identity)  
- For Sentinel-2 L2A: 10m/20m → unified 10m  
- Supports:
  - bilinear  
  - cubic  
  - nearest (for classification masks)  

Outputs include metadata tag:

~~~~~text
kfm:gsd_harmonized = 10
~~~~~

---

## 🌍 reprojection.py — CRS Alignment

Standardizes all geometries & rasters to:

~~~~~text
EPSG:4326
~~~~~

Supports:

- Raster reprojection (GDAL/rasterio)  
- Polygon reprojection (Shapely/pyproj)  
- Precision reduction for privacy (governed by CARE labels)

---

## 📡 sar_terrain_correction.py — Sentinel-1 GRD Terrain Correction

Implements:

- Range-Doppler Terrain Correction (RTC)  
- DEM alignment (SRTM/Kansas DEM)  
- Gamma0/sigma0 options  
- Mask invalid incidence angles  
- Telemetry: RTC duration, failures, masked %  

---

## 🛰️ sar_speckle_filter.py — Speckle Reduction

Filters:

- **Lee**  
- **Refined Lee**  
- Hybrid multi-looking  

Logs:

- `filter_type`, `window_size`, `pixels_smoothed`  

---

## 🔆 radiometric_normalization.py — Optical Standardization

Ensures consistency across sensors/time:

- Reflectance normalization  
- Solar angle adjustments  
- Scale-factor correction  
- Histogram matching (optional)  
- Telemetry: reflectance stats  

---

## 🌡️ thermal_tools.py — Thermal Infrared Tools

Used for drought/heat pipelines:

- LST derivation using:
  - scale factor  
  - thermal constants  
  - emissivity correction  
- Valid range filtering  
- Telemetry: min/max LST  

---

## 🧯 quality_masks.py — QA Derivation

Derives:

- `valid_pixel_mask`  
- Combined masks for spectral indices  
- Landsat QA_PIXEL bits  
- Sentinel-2 `SCL` classes  

Outputs percent of valid pixels for telemetry.

---

## 🛡️ mask_sensitive.py — CARE Masking

Implements FAIR+CARE governance:

- Mask footprint/rasters inside sensitive AOIs  
- H3 generalization for restricted polygons  
- Precision reduction for coordinates  
- Telemetry: `care_violations`, `masked_cells`  

Governance ledger updated via provenance utils.

---

## 🧰 utils.py — Shared Helpers

Contains:

- Band math  
- AOI clipping  
- Stats summaries  
- dtype guards  
- JSON-LD helpers  
- Metadata propagation  

---

## ⚖️ FAIR+CARE Integration

Preprocessing MUST:

- Honor `care_label` from config  
- Mask restricted AOIs  
- Log governance flags to telemetry  
- Preserve provenance metadata (source → mask → output)  
- Use generalized geometries where required  

Governance logs written to:

~~~~~text
../../../../../docs/reports/audit/data_provenance_ledger.json
~~~~~

---

## 📡 Telemetry

Writes NDJSON entries for:

- stage (`cloud_mask`,`harmonize_gsd`,`reproject`,…)  
- duration  
- pixels processed  
- mask coverage  
- care flags  
- energy/CO₂e estimates  

Aggregated into:

~~~~~text
../../../../../releases/v10.3.0/focus-telemetry.json
~~~~~

---

## 🧪 Testing & CI

Must pass:

- Unit tests (pytest)  
- rasterio/GDAL integration tests  
- CRS round-trip tests  
- SAR filter property tests  
- FAIR+CARE masking tests  
- `telemetry-export.yml`  
- `faircare-validate.yml`  
- `codeql.yml`  
- `trivy.yml`  

---

## 🕰️ Version History

| Version | Date       | Author | Summary |
|---------|------------|--------|---------|
| v10.3.1 | 2025-11-14 | Remote Sensing Team | Introduced full preprocessing module; aligned with FAIR+CARE masking, SAR RTC, telem. v3, reprojection, spectral normalization. |

---

<div align="center">

**Kansas Frontier Matrix — Remote Sensing Preprocessing Layer**  
Deterministic Geoprocessing × FAIR+CARE × Provenance × Scientific Integrity  
© 2025 Kansas Frontier Matrix — MIT License  

</div>