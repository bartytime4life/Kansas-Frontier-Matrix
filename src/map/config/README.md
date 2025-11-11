---
title: "🧭 Kansas Frontier Matrix — Map Configuration & Layer Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/map/config/README.md"
version: "v10.0.0"
last_updated: "2025-11-10"
review_cycle: "Continuous / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.0.0/manifest.zip"
telemetry_ref: "../../../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/src-map-config-v1.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧭 **Kansas Frontier Matrix — Map Configuration & Layer Registry**
`src/map/config/README.md`

**Purpose:**  
Define and document the **map configuration registry**, **basemap styles**, and **layer definitions** used across the Kansas Frontier Matrix (KFM) mapping framework.  
All configurations are **token-driven**, **FAIR+CARE-certified**, and validated for accessibility and provenance compliance under **MCP-DL v6.3**.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../docs/README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Geospatial%20Ethics%20Certified-orange)](../../../docs/standards/faircare.md)
[![Status: Stable](https://img.shields.io/badge/Status-Operational-success)]()

</div>

---

## 📘 Overview

This directory contains **machine-readable configuration files** that control all aspects of KFM’s 2D and 3D map visualizations — from **basemaps and overlays** to **styling rules and telemetry registration**.

Each configuration:
- Links to **FAIR+CARE-certified datasets** in `data/archive/`
- Uses **design tokens** from `src/design-tokens/`
- Validates under **OGC GeoJSON**, **STAC 1.0**, and **DCAT 3.0** metadata structures
- Is automatically linted via `map-config-validate.yml`

---

## 🗂️ Directory Layout

```plaintext
src/map/config/
├── README.md                      # This file — documentation overview
│
├── basemaps.json                  # Global basemap definitions (light, dark, terrain, satellite)
├── overlays.json                  # Dynamic data overlay configurations
├── maplibre-style.json            # Combined MapLibre GL JS style definition
├── layers.json                    # Registered thematic layers (hydrology, hazards, landcover, treaties)
└── metadata.json                  # Governance & telemetry linkage metadata
```

---

## ⚙️ Configuration Files Summary

| File | Purpose | Validation Schema |
|------|----------|------------------|
| `basemaps.json` | Defines base map tilesets and attribution. | `schemas/src-map-config-basemaps-v1.json` |
| `overlays.json` | Registers vector and raster overlays for analytics. | `schemas/src-map-config-overlays-v1.json` |
| `maplibre-style.json` | Core MapLibre GL style for frontend rendering. | `schemas/src-map-config-style-v1.json` |
| `layers.json` | Links map layers to archived datasets and FAIR+CARE metadata. | `schemas/src-map-config-layers-v1.json` |
| `metadata.json` | Tracks governance provenance, checksums, and telemetry link. | `schemas/telemetry/src-map-config-v1.json` |

---

## 🧩 Example — `basemaps.json`

```json
{
  "id": "basemap_light",
  "name": "KFM Light Basemap",
  "type": "raster",
  "url": "https://tiles.kfm.dev/light/{z}/{x}/{y}.png",
  "attribution": "© OpenStreetMap · KFM FAIR+CARE 2025",
  "license": "CC-BY-4.0",
  "fairstatus": "certified"
}
```

---

## 🗺️ Example — `overlays.json`

```json
{
  "id": "climate_anomalies_overlay",
  "type": "vector",
  "url": "https://tiles.kfm.dev/climate/anomalies/{z}/{x}/{y}.pbf",
  "paint": {
    "fill-color": [
      "interpolate",
      ["linear"],
      ["get", "temp_anomaly"],
      -5, "#1565c0",
      0, "#ffffff",
      5, "#ef5350"
    ],
    "fill-opacity": 0.8
  },
  "metadata": {
    "dataset": "data/archive/2025Q4/climate_v10.0.0/",
    "provenance": "NOAA NCEI",
    "governance_ref": "docs/standards/governance/ROOT-GOVERNANCE.md"
  }
}
```

---

## 🧠 Layer Governance Example (`layers.json`)

Each thematic layer connects to **archived datasets** validated under FAIR+CARE standards.

```json
{
  "id": "hazards_v10",
  "source": {
    "type": "geojson",
    "url": "data/archive/2025Q4/hazards_v10.0.0/hazards.geojson"
  },
  "metadata": {
    "fairstatus": "certified",
    "governance_registered": true,
    "checksum_verified": true,
    "reviewed_by": "@kfm-geo-governance",
    "timestamp": "2025-11-10T00:00:00Z"
  },
  "style": {
    "fill-color": "#e53935",
    "fill-opacity": 0.7,
    "outline-color": "#b71c1c"
  }
}
```

---

## ⚖️ FAIR+CARE Geospatial Matrix

| Principle | Implementation |
|------------|----------------|
| **Findable** | Basemaps and overlays indexed in DCAT and STAC catalogs. |
| **Accessible** | Public access through MapLibre tilesets and GeoJSON. |
| **Interoperable** | Configs aligned with OGC, STAC, and FAIR+CARE standards. |
| **Reusable** | Licensed under CC-BY 4.0, metadata preserved. |
| **CARE** | Sensitive geographic data reviewed for cultural and ethical relevance. |

---

## ♿ Accessibility Features

| Feature | Description | Compliance |
|----------|--------------|-------------|
| **High Contrast Modes** | Themes derived from `src/theming/high-contrast.css`. | WCAG 2.1 AA |
| **ARIA Labels for Maps** | `aria-label` and `role="region"` on container divs. | WCAG 2.1 4.1.2 |
| **Keyboard Navigation** | Tab, Enter, and Arrow key controls for map layers. | ISO 9241-171 |
| **Alt-text for Basemaps** | Each basemap includes descriptive metadata. | FAIR+CARE A11y |

Accessibility validated by `ui-accessibility.yml`.

---

## 🧮 Sustainability Metrics

| Metric | Description | Target |
|---------|-------------|---------|
| `render_energy_wh` | Avg energy cost per map render | ≤ 0.4 Wh |
| `tile_cache_hit_ratio` | Cached vs. fetched tiles | ≥ 90% |
| `carbon_gco2e` | Carbon output per session | ≤ 0.6 g |
| `config_validation_rate` | Successful schema validations | 100% |

Telemetry data logged in:  
`releases/v10.0.0/focus-telemetry.json`

---

## 🧾 Governance Metadata Example

```json
{
  "id": "map_config_registry_v10.0.0",
  "validated": true,
  "checksum_verified": true,
  "fairstatus": "certified",
  "datasets_linked": 8,
  "governance_registered": true,
  "telemetry_ref": "releases/v10.0.0/focus-telemetry.json",
  "created": "2025-11-10T18:00:00Z",
  "validator": "@kfm-map-governance"
}
```

---

## 🧩 Validation Workflows

| Workflow | Function | Output |
|-----------|-----------|---------|
| `map-config-validate.yml` | Schema and syntax validation for all map configs. | `reports/self-validation/map/config_validation.json` |
| `telemetry-export.yml` | Energy + sustainability metrics update. | `releases/v10.0.0/focus-telemetry.json` |
| `ui-accessibility.yml` | Accessibility testing for basemap and overlay UI. | `reports/self-validation/ui/a11y_summary.json` |

Governance results logged in:  
`docs/reports/telemetry/governance_scorecard.json`

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|---------|----------|
| v10.0.0 | 2025-11-10 | `@kfm-map-governance` | Introduced unified basemap + overlay configuration schema with FAIR+CARE governance and telemetry integration. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Governed under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to Map Index](../README.md) · [Layers](../layers/) · [Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

