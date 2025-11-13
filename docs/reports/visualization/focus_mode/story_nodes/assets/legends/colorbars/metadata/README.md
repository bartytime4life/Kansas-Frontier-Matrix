---
title: "🗂️ Kansas Frontier Matrix — Colorbar Metadata Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/colorbars/metadata/README.md"
version: "v10.2.0"
last_updated: "2025-11-12"
review_cycle: "Quarterly / FAIR+CARE Visualization Board"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/reports-visualization-focusmode-colorbars-metadata-v1.json"
governance_ref: "../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🗂️ **Kansas Frontier Matrix — Colorbar Metadata Index**
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/colorbars/metadata/README.md`

**Purpose:**  
Serve as the canonical index for **metadata files** describing each colorbar used in Focus Mode’s visualization and Story Node systems.  
All metadata is FAIR+CARE-certified, checksum-verified, and bound to STAC/DCAT lineage for reproducibility.

![Docs MCP](https://img.shields.io/badge/Docs·MCP-v6.3-blue)
![License CC-BY](https://img.shields.io/badge/License-CC--BY--4.0-green)
![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Certified-orange)
![Status Active](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

Every colorbar asset in Focus Mode (hydrology, climate, landcover, archaeology, terrain) must include a corresponding metadata JSON file.  
This ensures each visualization product remains:

- **Traceable** (checksums, provenance, STAC/DCAT mappings)  
- **Accessible** (public CC-BY 4.0 licensing)  
- **Ethically compliant** (CARE metadata for culturally sensitive domains)  
- **Interoperable** (consistent schema across PNG/SVG/GLB colorbar assets)

Metadata entries also feed into:

- Visualization provenance reports  
- AI narrative explainability overlays  
- STAC catalog registration  
- Governance-led audits and telemetry aggregation  

---

## 🗂️ Directory Layout

```plaintext
docs/reports/visualization/focus_mode/story_nodes/assets/legends/colorbars/metadata/
├── README.md                     # This document
├── field_definitions.md          # Required metadata fields
└── examples/                     # Valid JSON metadata examples
    ├── precipitation.json
    ├── drought_index.json
    ├── elevation_gradient.json
    └── groundwater_change.json
```

---

## 🧱 Metadata Requirements Summary

All metadata files must conform to `field_definitions.md` and include:

| Field | Required | Notes |
|-------|----------|-------|
| `id` | ✅ | Unique, stable identifier |
| `title` | ✅ | Human-readable label |
| `domain` | ✅ | hydrology, climate, archaeology, landcover, terrain |
| `format` | ✅ | PNG or SVG |
| `checksum_sha256` | ✅ | SHA-256 digest |
| `units` | ⚙️ | Required for numeric scales |
| `min_value`, `max_value` | ⚙️ | Required for continuous ranges |
| `provenance` | ✅ | Source pipeline + raw datasets |
| `care` | ⚙️ | CARE sensitivity + approval notes |
| `updated` | ✅ | ISO timestamp |

---

## 🔍 Example Metadata Snippet

```json
{
  "id": "kfm_colorbar_groundwater_v10",
  "title": "Groundwater Δ (Recharge → Depletion)",
  "domain": "hydrology",
  "format": "SVG",
  "units": "meters",
  "min_value": -4,
  "max_value": 3,
  "checksum_sha256": "sha256-d98af1c2a99cf21e13c63a5e71ff...",
  "provenance": {
    "source": "USGS + KDHE",
    "pipeline": "colorbar_render_v3",
    "commit_sha": "<latest-commit-hash>"
  },
  "care": {
    "status": "public",
    "reviewer": "FAIR+CARE Hydrology Committee",
    "date_reviewed": "2025-11-12",
    "statement": "No sensitive well coordinates encoded."
  },
  "updated": "2025-11-12T17:33:00Z"
}
```

---

## ⚙️ FAIR+CARE Visualization Governance

| Principle | Implementation |
|-----------|----------------|
| Findable | Indexed in STAC/DCAT; searchable via metadata catalog |
| Accessible | Public CC-BY 4.0 assets, clear captioning & legend labels |
| Interoperable | JSON-LD ready; STAC-compliant property schemas |
| Reusable | Complete provenance + reproducible rendering workflows |
| CARE | Cultural sensitivity enforcement in color schemes & ranges |

---

## 🧭 Integration Points

Colorbar metadata is consumed by:

- `focus_mode_renderer.py`
- `story_node_compiler.py`
- `stac-validate.yml`
- `telemetry-export.yml`
- `ai-explainability.yml` for legend-bound narrative reasoning  
- Cesium-based **3D Story Context Scenes**

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| v10.2.0 | 2025-11-12 | KFM Visualization Council | Established metadata index with FAIR+CARE/CARE governance requirements. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
Master Coder Protocol v6.3 · FAIR+CARE Certified  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Colorbars](../README.md)

</div>

