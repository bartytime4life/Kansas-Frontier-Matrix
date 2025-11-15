---
title: "🧼 Kansas Frontier Matrix — Remote Sensing Preprocessing Guide (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/guides/pipelines/preprocessing-guide.md"
version: "v10.3.1"
last_updated: "2025-11-14"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/pipelines-preprocessing-guide-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
kfm_markdown_protocol: "docs/standards/kfm_markdown_output_protocol.md"
---

<div align="center">

# 🧼 **Kansas Frontier Matrix — Remote Sensing Preprocessing Guide**  
`docs/guides/pipelines/preprocessing-guide.md`

**Purpose:**  
Define the authoritative **preprocessing layer** for all Remote Sensing pipelines in the Kansas Frontier Matrix (KFM).  
This layer prepares ingested STAC items for analytics, AI summaries, hazards, indices, and graph/RDF publishing through FAIR+CARE-aligned, deterministic, reproducible transformations.

This guide covers:

- Cloud/shadow/snow masking  
- GSD harmonization  
- Reprojection (GDAL/PROJ)  
- Radiometric normalization  
- Terrain correction (SAR RTC)  
- Bandstack standardization  
- Masking & sovereignty protections  
- CARE-aligned geometry adjustments  
- Preprocessing telemetry & lineage  
- Validation → staging integration (GX)

</div>

---

## 📘 Overview

Preprocessing is the **bridge between ingestion and analytics**, converting raw STAC assets into:

- Harmonized rasters  
- Cloud-free pixel masks  
- Multi-sensor bandstacks  
- Terrain-corrected SAR  
- Normalized optical/spectral surfaces  
- CARE-safe geospatial derivatives  
- Telemetry + lineage-tracked intermediate products  

All steps MUST be deterministic, schema-validated, and reproducible under MCP-DL v6.3.

---

## 🗂️ Directory Layout (Authoritative)

~~~~~text
src/pipelines/remote-sensing/preprocessing/
├── preprocess.py                     # Entrypoint for pipeline-specific orchestrations
├── cloud_mask.py                     # Cloud/shadow/snow mask generation
├── harmonize_gsd.py                  # Resample to common GSD resolution
├── reprojection.py                   # Reproject rasters (GDAL/PROJ)
├── sar_rtc.py                        # Sentinel-1 Terrain Correction (RTC)
├── radiometric_normalization.py      # Optical/spectral normalization
├── bandstack.py                      # Create unified bandstacks for analytics
├── masks/                            # Shared mask operations & utilities
└── utils/                            # Low-level GDAL/numpy helpers
~~~~~

---

## 🧩 Preprocessing Architecture (Indented Mermaid)

~~~~~mermaid
flowchart TD
  A["STAC Ingest<br/>raw bands + metadata"] --> B["Masking<br/>cloud · shadow · snow"]
  B --> C["Reprojection<br/>EPSG:4326 or target CRS"]
  C --> D["GSD Harmonization<br/>10m · 30m · 100m"]
  D --> E["Radiometric Normalization<br/>TOA · SR · log-scale"]
  E --> F["Terrain Correction (SAR)"]
  F --> G["Bandstack Assembly<br/>analytics-ready surfaces"]
  G --> H["Staging<br/>GX-validated + CARE-labeled"]
~~~~~

---

# 🧼 1. Cloud, Shadow & Snow Masking

Masking is **mandatory** for:

- Landsat 
- Sentinel-2  
- NAIP (where cloud metadata exists)  
- MODIS/VIIRS (QC flags)  

### Required cloud-mask sources

| Sensor | Mask Source |
|--------|-------------|
| Landsat C2 L2 | QA_PIXEL, QA_RADSAT |
| Sentinel-2 L2A | SCL (Scene Classification Layer) |
| NAIP | QA metadata |
| MODIS/VIIRS | QC flags |

### Output

- Mask raster (`cloud_mask.tif`)
- Valid-pixel raster (`valid_mask.tif`)
- Telemetry:
  - `cloud_pct`
  - `shadow_pct`
  - `snow_pct`
  - `valid_pct`

---

# 📐 2. GSD Harmonization

All analytics require harmonized resolution:

- Landsat     → 30m  
- Sentinel-2  → 10m  
- Sentinel-1  → 10m  
- NAIP        → 1m/60cm  
- MODIS/VIIRS → 250m/500m/1km depending on product  

Harmonization procedure:

1. Resample using **nearest** for masks, **bilinear** for reflectance  
2. Align to **grid-aligned affine** using reference metadata  
3. Validate GSD target using GX suite: `gsd_check >= required_res`

---

# 🌐 3. Reprojection (GDAL / PROJ)

KFM uses:

- **EPSG:4326** for all published datasets  
- **Native CRS** during processing for accuracy  

Reprojection performed via:

- GDAL Warp (`gdalwarp`)
- Python rasterio warp
- PROJ error resolution via dataset metadata

Outputs:

- `*_reproj.tif`
- Telemetry:  
  - `warp_duration_ms`  
  - `pixels_reprojected`

---

# 🛰 4. Radiometric Normalization

Normalization steps vary by sensor:

### Landsat SR
- Scale factors (0.0000275, -0.2)  
- Saturation correction  
- TOA reflectance for missing SR assets  

### Sentinel-2 L2A
- Divide by 10,000 scale factor  
- Apply scene classification filtering  

### Thermal Products
- Brightness temperature conversion (using metadata K1/K2)  

Telemetry:

- `radiometric_min/max`
- `radiometric_clipped_pixels`
- `radiometric_valid_pct`

---

# 🗻 5. SAR Terrain Correction (RTC)

Required for **Sentinel-1 GRD**:

- Remove geometric distortions  
- Normalize backscatter  
- Apply DEM: USGS 3DEP → COG  
- Apply radiometric calibration  
- Generate incidence-angle layers  
- Multi-looking (optional)  
- Mask layover + shadow

Outputs:

- RTC raster (`rtc_sigma0.tif`)
- Mask raster (`rtc_mask.tif`)
- Telemetry fields:
  - `rtc_duration_ms`
  - `laid_over_pct`
  - `shadow_pct`

---

# 🧱 6. Bandstack Generation

Bandstacks unify spectral/SAR layers:

- Landsat: B1–B7 + QA  
- Sentinel-2: B02, B03, B04, B08, B11, B12  
- Sentinel-1: VV, VH + RTC masks  
- Thermal bands (LST, emissivity)
- Mask layers (cloud, shadow, snow)

Bandstack requirements:

- Must align to **exact grid**  
- Must include **valid_mask**  
- Must include **metadata.json** in same directory

Example structure:

~~~~~text
bandstack/
├── B02.tif
├── B03.tif
├── B04.tif
├── B08.tif
├── cloud_mask.tif
├── valid_mask.tif
└── metadata.json
~~~~~

---

# 🛡 7. CARE & Sovereignty Masking (Mandatory)

Before entering staging:

- Mask or generalize sensitive AOIs  
- Apply H3 generalization (R7 or R5) for restricted labels  
- Inject governance metadata:
  - `kfm:careLabel`
  - `kfm:maskingStrategy`
  - `kfm:sovereigntyFlags[]`

Telemetry MUST include:

- `care_violations`  
- `sovereignty_conflicts`  
- `masking_applied`  

---

# 📊 8. Preprocessing Telemetry Requirements

Each step MUST emit NDJSON to:

~~~~~text
data/processed/telemetry/<pipeline>.ndjson
~~~~~

Required telemetry fields:

- `stage`
- `duration_ms`
- `pixels_processed`
- `pixels_valid`
- `pixels_masked`
- `energy_wh`
- `co2_g`
- `care_violations`
- `errors[]`

Telemetry aggregated to:

~~~~~text
../../../releases/v10.3.0/focus-telemetry.json
~~~~~

---

# 🧬 9. Lineage Requirements

Every preprocessing stage MUST append lineage:

~~~~~text
data/processed/lineage/<dataset>/<version>.jsonld
~~~~~

Lineage MUST include:

- PROV-O Activities  
- Entities (STAC source + derived outputs)  
- GeoSPARQL geometries  
- CIDOC CRM semantics (if applicable)  
- CARE fields  
- Checksums for each raster  

Validated against:

~~~~~text
src/pipelines/remote-sensing/lineage/schemas/lineage.schema.json
~~~~~

---

# 🧪 10. GX Staging Validation

After preprocessing, datasets enter:

~~~~~text
data/work/staging/<pipeline>/
~~~~~

GX suite must validate:

- Schema  
- GSD  
- Mask presence  
- Geometry boundaries  
- Value ranges  
- Required metadata keys  
- CARE compliance  

Passing → eligible for promotion  
Failing → moved to quarantine

---

# 🧭 Developer Workflow (Local)

~~~~~bash
# 1. Preprocess
python preprocess.py --config <config>

# 2. Validate via GX
great_expectations checkpoint run preprocessing_suite

# 3. Promote if valid
python promote.py

# 4. Publish (optional)
python publish.py
~~~~~

---

## 🕰️ Version History

| Version | Date       | Author | Summary |
|---------|------------|--------|---------|
| v10.3.1 | 2025-11-14 | Remote Sensing Team | Initial Remote Sensing Preprocessing Guide; aligned with CARE, lineage, telemetry, and KFM Protocol. |

---

<div align="center">

**Kansas Frontier Matrix — Preprocessing Guide**  
Deterministic Remote Sensing × FAIR+CARE × Provenance × Geospatial Integrity  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  

</div>

