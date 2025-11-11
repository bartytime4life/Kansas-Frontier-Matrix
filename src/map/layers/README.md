---
title: "🗺️ Kansas Frontier Matrix — Map Layers & Thematic Overlays (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/map/layers/README.md"
version: "v10.0.0"
last_updated: "2025-11-10"
review_cycle: "Continuous / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.0.0/manifest.zip"
telemetry_ref: "../../../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/src-map-layers-v1.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🗺️ **Kansas Frontier Matrix — Map Layers & Thematic Overlays**
`src/map/layers/README.md`

**Purpose:**  
Define, document, and govern all **map layer definitions**, **data-driven visualizations**, and **FAIR+CARE-certified thematic overlays** used in the Kansas Frontier Matrix (KFM).  
These layers provide **historical, environmental, and cultural** context through dynamically governed geospatial visualizations under **MCP-DL v6.3**.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../docs/README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Geospatial%20Certified-orange)](../../../docs/standards/faircare.md)
[![Status: Stable](https://img.shields.io/badge/Status-Operational-success)]()

</div>

---

## 📘 Overview

The **Map Layers Framework** defines all geospatial datasets and overlays rendered in KFM’s interactive 2D/3D maps.  
Each layer represents a **validated FAIR+CARE dataset** — linked directly to `data/archive/` and governed through automated telemetry and checksum lineage.

Every map layer includes:
- A **GeoJSON or vector tile source**
- FAIR+CARE **metadata** (license, provenance, ethics)
- Visual styling (color, opacity, legend)
- Accessibility and sustainability metrics

---

## 🗂️ Directory Layout

```plaintext
src/map/layers/
├── README.md                       # This file — documentation overview
│
├── hazards.geojson                 # Hazard polygons (tornadoes, floods, droughts)
├── climate.geojson                 # Climate zones and temperature anomaly data
├── hydrology.geojson               # Streamflow and aquifer geodata
├── landcover.geojson               # Vegetation and soil classification
├── treaties.geojson                # Historical treaty boundaries (1850–1900)
└── metadata.json                   # Governance, checksum, and FAIR+CARE linkage
```

---

## ⚙️ Layer Metadata Structure

Each `.geojson` or `.json` file must include a `properties.metadata` block aligned with KFM’s data contract (`docs/standards/data-contracts.md`).

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": { "type": "Polygon", "coordinates": [...] },
      "properties": {
        "name": "Flood Risk Zone A",
        "severity": "high",
        "metadata": {
          "dataset_id": "hazards_v10.0.0",
          "license": "CC-BY-4.0",
          "fairstatus": "certified",
          "provenance": "NOAA / FEMA Flood Data (2025)",
          "governance_ref": "docs/standards/governance/ROOT-GOVERNANCE.md"
        }
      }
    }
  ]
}
```

---

## 🧩 Layer Registry Schema

| Field | Description | Example |
|--------|-------------|----------|
| `id` | Unique identifier for the layer | `"hazards_v10"` |
| `source` | GeoJSON or vector tile reference | `"data/archive/2025Q4/hazards_v10.0.0/hazards.geojson"` |
| `type` | Layer type (`fill`, `line`, `circle`, `raster`) | `"fill"` |
| `paint` | Visual style rules | `{ "fill-color": "#d32f2f" }` |
| `metadata` | FAIR+CARE metadata block | see below |
| `visible` | Default visibility state | `true` |
| `zIndex` | Rendering order | `3` |
| `a11y_description` | Accessibility label for screen readers | `"Flood hazard regions in Kansas"` |

---

## 🧠 Example — Hazard Layer Definition

```json
{
  "id": "hazards_v10",
  "type": "fill",
  "source": {
    "type": "geojson",
    "data": "data/archive/2025Q4/hazards_v10.0.0/hazards.geojson"
  },
  "paint": {
    "fill-color": "#e53935",
    "fill-opacity": 0.75,
    "fill-outline-color": "#b71c1c"
  },
  "metadata": {
    "fairstatus": "certified",
    "checksum_verified": true,
    "license": "CC-BY-4.0",
    "provenance": "NOAA / FEMA Flood Data (2025)",
    "validator": "@kfm-hazards-lab"
  }
}
```

---

## 🗺️ Example — Treaty Boundary Layer (Ethics-Sensitive)

```json
{
  "id": "treaties_v10",
  "type": "line",
  "source": {
    "type": "geojson",
    "data": "data/archive/2025Q4/hazards_v10.0.0/treaties.geojson"
  },
  "paint": {
    "line-color": "#1e88e5",
    "line-width": 2
  },
  "metadata": {
    "fairstatus": "certified",
    "care": {
      "statement": "Reviewed and approved by Indigenous Data Council (2025)",
      "reviewer": "FAIR+CARE Council",
      "status": "approved"
    },
    "provenance": "U.S. Treaties & Land Cessions (Kappler 1904)"
  }
}
```

---

## ⚖️ FAIR+CARE Governance Matrix

| Principle | Implementation |
|------------|----------------|
| **Findable** | Layers registered in `config/layers.json` with global UUIDs. |
| **Accessible** | Public GeoJSON/tilesets under CC-BY 4.0 license. |
| **Interoperable** | STAC + DCAT 3.0 metadata alignment. |
| **Reusable** | Open schema and versioned lineage tracking. |
| **CARE** | Treaty and cultural datasets ethically reviewed before display. |

Audit logs recorded in:  
`docs/reports/telemetry/governance_scorecard.json`

---

## ♿ Accessibility Standards

| Feature | Description | Compliance |
|----------|--------------|-------------|
| **Layer Narration** | Screen reader summaries per dataset. | WCAG 2.1 1.2.1 |
| **Keyboard Navigation** | Navigate through layer list with Tab + Enter. | WCAG 2.1 2.1.1 |
| **Color Contrast** | ≥ 4.5:1 across all map layers. | WCAG 2.1 1.4.3 |
| **ARIA Regions** | Accessible labels for major map overlays. | WCAG 2.1 4.1.2 |

---

## ♻️ Sustainability Metrics

| Metric | Target | Verified By |
|---------|---------|--------------|
| `render_energy_wh` | ≤ 0.3 Wh per layer load | @kfm-sustainability |
| `tile_cache_hit_ratio` | ≥ 90% | @kfm-infrastructure |
| `carbon_output_gco2e` | ≤ 0.4 g/session | @kfm-security |
| `a11y_score` | ≥ 95% | @kfm-accessibility |

Telemetry recorded in:  
`releases/v10.0.0/focus-telemetry.json`

---

## 🧾 Governance Metadata Example

```json
{
  "id": "map_layers_registry_v10.0.0",
  "layers_registered": 5,
  "datasets_linked": [
    "data/archive/2025Q4/hazards_v10.0.0/",
    "data/archive/2025Q4/landcover_v10.0.0/"
  ],
  "fairstatus": "certified",
  "governance_registered": true,
  "checksum_verified": true,
  "telemetry_ref": "releases/v10.0.0/focus-telemetry.json",
  "created": "2025-11-10T00:00:00Z"
}
```

---

## 🧩 Validation Workflows

| Workflow | Function | Output |
|-----------|-----------|---------|
| `map-layers-validate.yml` | Validates GeoJSON schema and FAIR+CARE metadata. | `reports/self-validation/map/layers_validation.json` |
| `telemetry-export.yml` | Updates governance and energy metrics. | `releases/v10.0.0/focus-telemetry.json` |
| `ui-accessibility.yml` | Ensures visual accessibility across layers. | `reports/self-validation/ui/a11y_summary.json` |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|---------|----------|
| v10.0.0 | 2025-11-10 | `@kfm-map-governance` | Added unified layer registry schema, FAIR+CARE metadata linking, and sustainable telemetry reporting. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Governed under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to Map Index](../README.md) · [Map Config](../config/README.md) · [Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

