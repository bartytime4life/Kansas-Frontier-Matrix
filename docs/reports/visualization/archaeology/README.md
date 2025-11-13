---
title: "🏺 Kansas Frontier Matrix — Archaeology Visualization Reports (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/archaeology/README.md"
version: "v10.2.0"
last_updated: "2025-11-12"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/reports-visualization-archaeology-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🏺 **Kansas Frontier Matrix — Archaeology Visualization Reports**  
`docs/reports/visualization/archaeology/README.md`

**Purpose:**  
Provide a governed, FAIR+CARE-compliant index of **archaeological visualizations**, including settlement overlays, temporal density animations, environmental correlation layers, and cultural-heritage spatial products.  
All artifacts follow **sensitivity generalization rules**, **tribal oversight policies**, and **v10.2 provenance standards**.

[![Docs · MCP](https://img.shields.io/badge/Docs·MCP-v6.3-blue)](../../../README.md)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY--4.0-green)](../../../../../LICENSE)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Archaeology-orange)](../../../../standards/faircare.md)  
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)]()

</div>

---

## 📘 Overview

Archaeology-related visualizations in KFM often involve **culturally sensitive**, **historically significant**, or **location-restricted** datasets.  
This directory aggregates **generalized**, **ethically vetted**, and **scientifically valid** spatial products that support research while upholding **Indigenous sovereignty** and **CARE governance**.

All maps and animations are:
- Linked to full provenance metadata (`provenance.json`)  
- Reviewed by the **FAIR+CARE Cultural Heritage Board**  
- Compliant with **spatial generalization rules** for sensitive archaeological sites  
- Registered in **STAC/DCAT visualization catalogs**  
- Logged into `focus-telemetry.json` with energy & carbon metrics  

---

## 🗂️ Directory Layout

```plaintext
docs/reports/visualization/archaeology/
├── README.md
│
├── paleo_overlay.png                 # Cross-era terrain + artifact overlay (generalized)
├── density_timeline.gif              # Archaeological density animation (1850–1930)
├── settlement_hotspots.geojson       # Hotspot model (masked, grid ≥ 5km)
├── provenance.json                   # FAIR+CARE visualization metadata
└── legends/                          # Shared legends and symbol keys
    ├── paleo_legend.svg
    └── hotspot_legend.svg
```

---

## 🧩 Visualization Types Included

| Visualization Type | Description | Sensitivity Class | Format |
|--------------------|-------------|-------------------|---------|
| **Paleo Overlay Map** | Combined paleoenvironment + settlement indicators | Medium | PNG |
| **Density Timeline Animation** | Temporal clustering of settlements across decades | High | GIF |
| **Hotspot Model** | Grid-based aggregation of site likelihood | High | GeoJSON |
| **Terrain Correlation Layers** | Elevation, hydrology, and slope blends | Low | PNG/SVG |

> Sensitive layers (High) must use **≥5 km generalization**, **randomized offsets**, or **grid aggregation** per CARE governance rules.

---

## ⚙️ Provenance & Metadata Requirements (v10.2)

Each visualization must include a matching `provenance.json`:

```json
{
  "asset_id": "kfm_archaeology_density_timeline_2025",
  "generated_by": "workflow:archaeology-visualization.yml",
  "sensitivity_class": "high",
  "generalization_method": "5km grid aggregation + temporal smoothing",
  "datasets_used": [
    "processed_archaeology_sites_v10.2.0",
    "elevation_30m_slope_index_v10.1.0"
  ],
  "faircare_review": "approved",
  "tribal_review_entities": ["Prairie Band Potawatomi Nation"],
  "commit_sha": "<latest-commit-hash>",
  "stac_item": "data/stac/archaeology/density_timeline_v10.2.0.json",
  "telemetry_ref": "releases/v10.2.0/focus-telemetry.json",
  "license": "CC-BY 4.0"
}
```

---

## ⚖️ FAIR+CARE Ethical Alignment

### FAIR

- **Findable:** Registered in STAC/DCAT visualization catalogs  
- **Accessible:** Public under CC-BY 4.0, with provenance  
- **Interoperable:** Uses open geospatial standards (GeoJSON, PNG, GIF)  
- **Reusable:** Full lineage, commit SHA, and dataset references included  

### CARE

- **Collective Benefit:** Supports responsible heritage interpretation  
- **Authority to Control:** Tribal review required for any sensitive layer  
- **Responsibility:** No disclosure of precise site coordinates  
- **Ethics:** Generalization applied per CARE rules (≥5 km displacement or grid aggregation)  

---

## 🧪 Validation Workflows

| Workflow | Purpose | Output |
|----------|---------|---------|
| `faircare-validate.yml` | CARE-sensitive site checks | `faircare_summary.json` |
| `visualization-validate.yml` | CRS, contrast, metadata, and masking verification | `visualization_validate.json` |
| `telemetry-export.yml` | Sustainability & rendering metrics | `focus-telemetry.json` |

---

## 🧭 Rendering Telemetry Targets

| Metric | Target | Notes |
|--------|--------|-------|
| `energy_wh` | ≤ 12 Wh | Based on GPU/CPU rendering window |
| `carbon_gco2e` | ≤ 0.004 | Per ISO 50001 tracking |
| `a11y_contrast` | ≥ 98% | Required for public maps |
| `render_time_ms` | ≤ 2500 ms | On CI reference hardware |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| v10.2.0 | 2025-11-12 | KFM Cultural Heritage Council | Added provenance schema, sensitive site generalization policy, and updated directory layout. |
| v10.1.0 | 2025-11-11 | FAIR+CARE Council | Initial archaeology visualization index. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Master Coder Protocol v6.3 · FAIR+CARE Certified  
**Diamond⁹ Ω / Crown∞Ω Ultimate Certified**

[Back to Visualization Index](../README.md) · [Standards Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

