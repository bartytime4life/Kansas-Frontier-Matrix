---
title: "🌦️ Kansas Frontier Matrix — Climate Basemap Assets Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/maps/climate/README.md"
version: "v10.2.0"
last_updated: "2025-11-12"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/reports-visualization-focusmode-climate-basemaps-v1.json"
governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🌦️ **Kansas Frontier Matrix — Climate Basemap Assets Index**  
`docs/reports/visualization/focus_mode/story_nodes/assets/maps/climate/README.md`

**Purpose:**  
Provide the authoritative index of **climate-layer basemap assets** used within Focus Mode Story Nodes, supporting temporal–spatial climate narratives, anomaly diagnostics, seasonal composite overlays, and historical climate reconstruction workflows.  
All items follow **FAIR+CARE**, **ISO 19115**, **DCAT 3.0**, and **STAC 1.0**.

![Docs MCP](https://img.shields.io/badge/Docs·MCP-v6.3-blue)
![License CC-BY](https://img.shields.io/badge/License-CC--BY--4.0-green)
![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Certified-orange)
![Status Active](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

Climate basemaps support **temperature, precipitation, drought–wetness cycles**, seasonality, ENSO-phase overlays, and long-term change analysis.  
They underpin Focus Mode climate story nodes including:
- Century-scale warming overlays  
- Seasonal precipitation composites  
- Drought anomaly surfaces (SPI / SPEI / PDSI)  
- Climate–hydrology correlation layers  
- Climate–archaeology environmental context maps  
- Climate era segmentation (pre-1950 vs post-1950 regime shift)

All assets include **STAC metadata**, **checksum verification**, **provenance lineage**, and **accessibility-compliant color ramps**.

---

## 🗂️ Directory Layout

```plaintext
docs/reports/visualization/focus_mode/story_nodes/assets/maps/climate/
├── README.md
├── temperature_anomaly_surface.tif
├── precipitation_seasonal_composite.png
├── drought_spi_overlay.geojson
├── climate_change_rate_map.svg
├── climate_regime_shift_3d.glb
└── stac.json
```

---

## 🧩 Metadata Requirements (Climate Basemap)

| Field | Description |
|-------|-------------|
| `id` | Global climate-layer asset ID |
| `type` | `"climate_basemap"` |
| `checksum_sha256` | Required SHA-256 integrity verification |
| `projection` | Typically `EPSG:4326` |
| `climate_domain` | e.g., `"temperature"`, `"precipitation"`, `"drought"`, `"climate_change"` |
| `temporal_extent` | Period represented (e.g., `1895–2025`) |
| `care.status` | Public or generalized (no sensitive well/landowner links) |
| `generalization.method` | Any applied temporal/spatial smoothing |
| `provenance` | NOAA, NIDIS, PRISM, Daymet, CPC, etc. |
| `updated` | ISO timestamp |
| `stac_extensions` | `proj`, `raster`, `version`, `checksum` |

---

## 🌡️ Example Metadata Record (Temperature Anomaly Surface)

```json
{
  "id": "kfm_temperature_anomaly_surface_v10",
  "type": "climate_basemap",
  "path": "temperature_anomaly_surface.tif",
  "checksum_sha256": "sha256-cc8dd07cf6b97d22b8f50c983c448b4ade57b7d709d3e748e728b1d08f48ccce",
  "projection": "EPSG:4326",
  "climate_domain": "temperature",
  "temporal_extent": "1895–2025",
  "care": {
    "status": "public",
    "reason": "Dataset contains no sensitive personal data.",
    "authority": "FAIR+CARE Climate Review Board"
  },
  "generalization": {
    "method": "spatial smoothing + temporal rolling window",
    "window": "10-year running mean"
  },
  "provenance": {
    "datasets": ["NOAA NCEI", "PRISM Climate Group"],
    "agreements": []
  },
  "updated": "2025-11-12T17:16:00Z",
  "stac_extensions": ["proj", "raster", "checksum", "version"]
}
```

---

## 🌧️ Climate Map Types Supported

| Map Type | Description | Format |
|----------|-------------|--------|
| **Temperature Anomalies** | Annual/decadal anomaly rasters | TIFF |
| **Precipitation Composites** | Seasonal/annual precipitation intensity | PNG, TIFF |
| **Drought Indices** | SPI, SPEI, PDSI surface layers | GeoTIFF, GeoJSON |
| **Climate Change Rate** | Trend slope maps (°C/decade) | SVG, PNG |
| **ENSO Phases** | Warm/neutral/cold overlays | PNG |
| **Climate Regime Shifts** | Statistical breakpoints | GLB (3D), PNG |

---

## 🧠 FAIR+CARE Climate Requirements

| Criterion | Implementation |
|----------|----------------|
| **Collective Benefit** | Visualizes climate risk without exposing private land-owner data |
| **Authority to Control** | Climate indicators derived from public-domain sources |
| **Responsibility** | Anomalies validated and smoothed to prevent misinterpretation |
| **Ethics** | Basemaps avoid overprecision where it may misrepresent localized impacts |

---

## 🧭 STAC Requirements

Each folder must include a `stac.json` with:
- `stac_version: "1.0.0"`
- `type: "Collection"`
- `assets` (with MIME types + checksums)
- STAC extensions:
  - `proj`
  - `raster`
  - `checksum`
  - `version`
- Custom fields:
  - `"kfm:climate_domain"`
  - `"kfm:care_tag"`
  - `"kfm:generalization_method"`

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| v10.2.0 | 2025-11-12 | KFM Climate Visualization Board | Initial climate basemap asset index with domain segmentation and FAIR+CARE integration. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
Master Coder Protocol v6.3 · FAIR+CARE Certified  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Map Assets](../README.md)

</div>

