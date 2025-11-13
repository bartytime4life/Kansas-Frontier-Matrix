---
title: "🏺 Kansas Frontier Matrix — Archaeological Basemap Assets Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/maps/archaeological/README.md"
version: "v10.2.0"
last_updated: "2025-11-12"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/reports-visualization-focusmode-archaeo-basemaps-v1.json"
governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC BY-NC 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🏺 **Kansas Frontier Matrix — Archaeological Basemap Assets Index**  
`docs/reports/visualization/focus_mode/story_nodes/assets/maps/archaeological/README.md`

**Purpose:**  
Catalog and govern **archaeology-focused basemaps** used in Focus Mode Story Nodes, including generalized site overlays, cultural landscapes, excavation-phase contours, temporal layers, and Indigenous stewardship-aligned cartography.  
All assets follow **FAIR+CARE**, **CIDOC CRM**, **DCAT 3.0**, and **KFM Sensitive-Site Generalization Protocol**.

![Docs](https://img.shields.io/badge/Docs·MCP-v6.3-blue)
![License](https://img.shields.io/badge/License-CC--BY--NC%204.0-green)
![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Certified-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

Archaeological basemaps support **story nodes, cultural timelines, Indigenous land interpretations, heritage analytics, paleoenvironmental overlays**, and **CARE-aligned visual storytelling**.  
These layers intentionally exclude precise coordinates for sensitive sites and instead provide **generalized, aggregated, or buffered** geographic features.

All assets must include:
- **Spatial generalization (≥ 5km or site-class thresholds)**  
- **CARE metadata**  
- **Checksum-verified rasters/vectors**  
- **STAC entries**  
- **Accessibility-compliant palettes**  
- **Temporal provenance** (period, excavation era, cultural phase)

---

## 🗂️ Directory Layout

```plaintext
docs/reports/visualization/focus_mode/story_nodes/assets/maps/archaeological/
├── README.md
├── generalized_cultural_landscape.png
├── pre_contact_topography.png
├── excavation_phase_overlay.svg
├── indigenous_stewardship_regions.geojson
└── stac.json
```

---

## 🧩 Required Metadata Fields (per asset)

| Field | Description |
|-------|-------------|
| `id` | Unique asset identifier |
| `type` | `"archaeological_basemap"` |
| `path` | Relative file path |
| `checksum_sha256` | Required integrity hash |
| `projection` | Default EPSG:4326 |
| `temporal_extent` | Cultural/archaeological period represented |
| `cultural_context` | Associated cultural horizon, tribal history, or temporal tradition |
| `care.status` | `generalized` · `restricted` · `public_non_sensitive` |
| `generalization.method` | Technique applied (masking, buffering, aggregation, etc.) |
| `updated` | ISO timestamp |
| `provenance` | Data origin, excavation sources, and community agreements |

---

## 🗺️ Example Metadata Record (Generalized Cultural Landscape)

```json
{
  "id": "cultural_landscape_generalized_v10",
  "type": "archaeological_basemap",
  "path": "generalized_cultural_landscape.png",
  "checksum_sha256": "sha256-a8f02c7d02f98e3ac81fd29ab639f4b82ed01aa8376f77f29e4a24e0b91c98a4",
  "projection": "EPSG:4326",
  "temporal_extent": "1000 BCE – 1850 CE",
  "cultural_context": "Kanza, Osage, Pawnee, Wichita cultural regions",
  "generalization": {
    "method": "5km spatial buffer + centroid aggregation",
    "notes": "Sensitive sites redacted following tribal sovereignty MOU."
  },
  "care": {
    "status": "generalized",
    "authority": "FAIR+CARE Council + Tribal Heritage Representatives"
  },
  "provenance": {
    "datasets": [
      "kansas_frontier_archival_surveys",
      "usgs_historic_topo",
      "tribal_knowledge_maps (restricted)"
    ],
    "agreements": ["MOU_2025_TRIBAL_SOVEREIGNTY"]
  },
  "updated": "2025-11-12T16:30:00Z"
}
```

---

## 🧠 FAIR+CARE Integration

| Principle | Implementation |
|----------|----------------|
| **Collective Benefit** | Supports public storytelling without exposing sacred locations |
| **Authority to Control** | Tribal sovereignty MOUs govern precision & visibility |
| **Responsibility** | Spatial generalization + redaction for high-risk sites |
| **Ethics** | Continuous review by Indigenous Data Steward & FAIR+CARE Council |

---

## 🎨 Cartographic Style Requirements

| Category | Rule |
|----------|------|
| **Contrast** | WCAG 2.1 AA minimum |
| **Cultural Sensitivity** | Avoid symbols or colors with sacred meaning unless authorized |
| **Basemap Tone** | Neutral earth-tone palette preferred |
| **Generalization Level** | Minimum 5km buffer for site-class areas unless approved |
| **No Exact Coordinates** | Forbidden unless dataset is explicitly public-domain and non-sensitive |

---

## 🧭 STAC Requirements

Each folder must include a `stac.json` with:

- `stac_version`: `"1.0.0"`  
- `assets` → reference each file with checksum  
- `extensions`: `proj`, `version`, `checksum`, `scientific`  
- `kfm:care_tag` field (`generalized`, `restricted`, or `non_sensitive`)  
- `kfm:generalization_method`  

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| v10.2.0 | 2025-11-12 | KFM Visualization Council | Initial archaeological basemap asset index, fully aligned with CARE + generalization rules. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
Master Coder Protocol v6.3 · FAIR+CARE Certified  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Map Assets](../README.md)

</div>

