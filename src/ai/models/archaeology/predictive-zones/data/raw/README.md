---
title: "🗺️ Kansas Frontier Matrix — Raw Data Layers for Archaeology Predictive Zones (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/ai/models/archaeology/predictive-zones/data/raw/README.md"
version: "v9.9.0"
last_updated: "2025-11-08"
review_cycle: "Continuous / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v9.9.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v9.9.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v9.9.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/src-ai-models-archaeology-predictivezones-raw-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "Restricted · CC-BY 4.0 (Derived Data)"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🗺️ **Kansas Frontier Matrix — Raw Data Layers for Archaeology Predictive Zones**  
`src/ai/models/archaeology/predictive-zones/data/raw/README.md`

**Purpose:**  
Describe and document the **raw geospatial, environmental, and cultural data sources** used to train and validate the **Archaeology Predictive Zones** model suite within the Kansas Frontier Matrix (KFM).  
These layers provide the foundational variables for site probability mapping while maintaining strict **FAIR+CARE ethical governance** and **ISO 19115 metadata compliance**.

[![Docs · MCP](https://img.shields.io/badge/Docs·MCP-v6.3-blue)](../../../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Governed-orange)](../../../../../../docs/standards/faircare.md)
[![Status: Controlled](https://img.shields.io/badge/Status-Controlled-critical)](#)

</div>

---

## 📘 Overview

The **raw data layers** described here represent diverse datasets used for **archaeological predictive modeling**.  
They include **remote sensing imagery**, **LIDAR-derived terrain models**, **hydrological and soil indices**, and **archival cultural inventories**.  

These datasets are treated as **restricted-access resources** under the **CARE Principles**, requiring **FAIR+CARE Council** review before redistribution or external publication.

---

## 🗂️ Directory Layout

```plaintext
src/ai/models/archaeology/predictive-zones/data/raw/
├── README.md                            # This file
│
├── lidar_dem_1m_kansas.tif              # 1m-resolution Digital Elevation Model (USGS)
├── soil_moisture_index_2025.tif         # Soil moisture from USDA SMAP (2025 composite)
├── hydrology_vector.geojson             # Stream networks and hydrological boundaries
├── vegetation_density_2024.tif          # NDVI-based vegetation coverage (Sentinel-2 / MODIS)
├── cultural_sites_inventory.geojson     # Known site points from state and federal inventories
└── heritage_areas_mask.geojson          # Mask for restricted Indigenous heritage zones
```

---

## ⚙️ Source Metadata Summary

| Dataset | Source / Provider | Type | CRS | FAIR+CARE Tag | Access Level |
|----------|------------------|------|-----|----------------|---------------|
| **USGS LIDAR DEM (1m)** | USGS 3DEP | Raster (GeoTIFF) | EPSG:5070 | public | Open |
| **Soil Moisture Index** | USDA SMAP 2025 | Raster (GeoTIFF) | EPSG:4326 | public | Open |
| **Hydrology Vector** | Kansas DASC | GeoJSON | EPSG:4326 | public | Open |
| **Vegetation NDVI Composite** | MODIS / Sentinel-2 | Raster (GeoTIFF) | EPSG:4326 | public | Open |
| **Cultural Sites Inventory** | KHS + SHPO + NPS | GeoJSON | EPSG:4326 | restricted | Controlled |
| **Heritage Area Mask** | Tribal & Indigenous governance data (various councils) | GeoJSON | EPSG:4326 | sensitive | Protected |

> ⚠️ *Datasets tagged as `restricted` or `sensitive` require Council authorization for usage or redistribution.*

---

## 🧠 Data Governance Rules

| Classification | Usage Policy | Required Action |
|----------------|--------------|-----------------|
| `public` | Freely used for model training and visualization. | None |
| `restricted` | Requires FAIR+CARE Council oversight; must not be shown publicly. | Apply masking before output |
| `sensitive` | Includes heritage or sacred sites; AI must not model these directly. | Redact or generalize geometry |
| `derived` | Resultant datasets must retain attribution to source data. | Include provenance metadata |

All records logged under:  
`releases/v9.9.0/governance/ledger_snapshot.json`

---

## 🧩 Metadata Fields (`metadata.json` template)

```json
{
  "id": "raw_layer_lidar_dem_1m_kansas",
  "title": "Kansas LIDAR DEM 1m (USGS 3DEP)",
  "source": "USGS 3DEP / https://earthexplorer.usgs.gov/",
  "description": "High-resolution digital elevation model covering the state of Kansas used for archaeological predictive mapping.",
  "license": "Public Domain / USGS",
  "crs": "EPSG:5070",
  "resolution_m": 1,
  "extent": [-102.1, 36.9, -94.6, 40.1],
  "care_tag": "public",
  "checksum_sha256": "sha256:47bfb0e4df1c3a77e0b4a4e9...",
  "downloaded": "2025-09-12T10:00:00Z",
  "validated": "2025-09-13T14:45:00Z",
  "governance_ref": "../../../../../../docs/standards/faircare.md"
}
```

---

## ⚖️ FAIR+CARE Compliance Summary

| FAIR Principle | Implementation | Validation |
|----------------|----------------|-------------|
| **Findable** | Catalogued under STAC/DCAT with persistent IDs. | `stac-validate.yml` |
| **Accessible** | Open links for public datasets; controlled for restricted layers. | Governance ledger |
| **Interoperable** | GeoTIFF and GeoJSON formats; consistent CRS. | `validation/schema_validation.json` |
| **Reusable** | Attribution and license metadata preserved. | SPDX SBOM |
| **CARE – Authority to Control** | Tribal consultation for site masks. | `care_ethics_review.json` |
| **CARE – Ethics** | Sensitive geometry generalized to 5 km cells. | FAIR+CARE audit logs |

---

## 🧮 Validation & Telemetry Integration

All ingestion and validation steps produce automated logs recorded in the telemetry system.

| Metric | Description | Example |
|--------|--------------|---------|
| `datasets_ingested` | Number of raw sources validated. | 6 |
| `validation_errors` | Schema or checksum failures. | 0 |
| `energy_wh` | Processing energy use. | 27.6 |
| `carbon_gco2e` | Carbon equivalent emission. | 12.8 |
| `care_flagged` | Files with ethical restrictions. | 2 |

Telemetry data exported to:  
`releases/v9.9.0/focus-telemetry.json`  
Schema: `schemas/telemetry/src-ai-models-archaeology-predictivezones-raw-v1.json`

---

## 🧾 Citation

```text
Kansas Frontier Matrix (2025). Raw Data Layers for Archaeology Predictive Zones (v9.9.0).
FAIR+CARE-compliant raw dataset inventory supporting archaeological predictive modeling and cultural landscape analysis in the Kansas Frontier Matrix.
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------:|------|--------|----------|
| v9.9.0 | 2025-11-08 | `@kfm-data` | Created documentation for raw archaeology data layers; added governance and FAIR+CARE compliance rules. |

---

<div align="center">

**Kansas Frontier Matrix**  
*Responsible Data × FAIR+CARE Ethics × Cultural Stewardship*  
© 2025 Kansas Frontier Matrix · CC-BY 4.0 · Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Predictive Zones Data](../README.md) · [Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

