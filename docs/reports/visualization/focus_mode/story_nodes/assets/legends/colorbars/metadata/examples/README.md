---
title: "🧪 Kansas Frontier Matrix — Colorbar Metadata Examples Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/colorbars/metadata/examples/README.md"
version: "v10.2.0"
last_updated: "2025-11-12"
review_cycle: "Quarterly / FAIR+CARE Visualization Board"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../schemas/telemetry/reports-visualization-focusmode-colorbars-metadata-examples-v1.json"
governance_ref: "../../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧪 **Kansas Frontier Matrix — Colorbar Metadata Examples Index**
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/colorbars/metadata/examples/README.md`

**Purpose:**  
Provide **validated example metadata files** for colorbars used in **Focus Mode Story Nodes**, ensuring schema compliance, FAIR+CARE visualization ethics, and reproducibility across hydrology, climate, archaeology, and landcover domains.

![Docs MCP](https://img.shields.io/badge/Docs·MCP-v6.3-blue)
![License CC-BY](https://img.shields.io/badge/License-CC--BY--4.0-green)
![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Certified-orange)
![Status Active](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

This directory contains **canonical examples** of valid colorbar metadata JSON files used throughout Focus Mode visualizations.  
Examples demonstrate:

- Required vs. optional fields  
- Domain-specific extensions  
- CARE-sensitive treatment of colors and ranges  
- Linkage to provenance, STAC/DCAT metadata, and dataset lineage  
- Telemetry-ready, versioned structure for audits and reproducibility  

All examples conform to rules defined in:

- `../field_definitions.md`  
- KFM Visualization Metadata Schema v10  
- FAIR+CARE Visualization Governance Standards  

---

## 🗂️ Directory Layout

```plaintext
docs/reports/visualization/focus_mode/story_nodes/assets/legends/colorbars/metadata/examples/
├── README.md                         # This file
├── precipitation.json                # Rainfall gradient (mm/day)
├── drought_index.json                # Drought severity spectrum
├── elevation_gradient.json           # Terrain elevation (m)
└── groundwater_change.json           # Aquifer Δ recharge/depletion
```

---

## 🧩 Example Files Summary

| File | Domain | Purpose | Notes |
|------|--------|----------|--------|
| `precipitation.json` | Climate | Daily precipitation gradient | STAC-linked; units (mm/day) |
| `drought_index.json` | Climate/Hazards | Drought severity (0–5 scale) | CARE-reviewed (no sensitive tribal drought records) |
| `elevation_gradient.json` | Terrain | Elevation color ramp | Derived from USGS DEMs |
| `groundwater_change.json` | Hydrology | Aquifer change (m) | Range-mapped; sensitive well coords removed upstream |

---

## 🔍 Metadata Integrity Requirements

All examples include:

| Requirement | Description |
|-------------|-------------|
| SHA-256 checksum | Mandatory for integrity & SBOM tie-in |
| Provenance block | Source data + processing pipeline |
| CARE block | Reviewer, status, notes (if applicable) |
| ISO timestamp | `updated` field for governance audits |
| STAC/DCAT compatibility | Crosswalk-ready metadata fields |

---

## 🧠 Example: Elevation Gradient (Excerpt)

```json
{
  "id": "kfm_colorbar_elevation_v10",
  "title": "Elevation Gradient (0–1200 m)",
  "domain": "terrain",
  "format": "PNG",
  "units": "meters",
  "min_value": 0,
  "max_value": 1200,
  "checksum_sha256": "sha256-a13be9f2c0afe1d44cbea...",
  "provenance": {
    "source": "USGS 3DEP",
    "pipeline": "colorbar_render_v3",
    "commit_sha": "<latest-commit-hash>"
  },
  "care": {
    "status": "public",
    "reviewer": "FAIR+CARE Terrain Board",
    "date_reviewed": "2025-11-12",
    "statement": "No culturally sensitive terrain features encoded."
  },
  "updated": "2025-11-12T17:40:00Z"
}
```

---

## ⚙️ FAIR+CARE Visualization Governance

| Principle | Implementation |
|----------|-----------------|
| Findable | Indexed by STAC ID + searchable model keys |
| Accessible | CC-BY 4.0, standardized colorbar formats |
| Interoperable | JSON-LD ready, FAIR-compliant schema |
| Reusable | Reproducible ranges, units, provenance |
| CARE | Ensures cultural sensitivity in visual encodings |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| v10.2.0 | 2025-11-12 | KFM Visualization Council | Added sample colorbar metadata files + FAIR+CARE alignment. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
FAIR+CARE Certified · Master Coder Protocol v6.3  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Metadata Index](../README.md)

</div>

