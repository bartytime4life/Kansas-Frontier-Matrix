---
title: "🧩 Kansas Frontier Matrix — Focus Mode Overlays Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/overlays/README.md"
version: "v10.2.0"
last_updated: "2025-11-12"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/reports-visualization-focusmode-overlays-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧩 **Kansas Frontier Matrix — Focus Mode Overlays Index**  
`docs/reports/visualization/focus_mode/overlays/README.md`

**Purpose:**  
Provide a curated and governance-certified index of all **Focus Mode overlays**—dynamic geospatial, temporal, hydrological, archaeological, and narrative layers used within Focus Mode v10+.  
These overlays enable **AI-assisted interpretation**, **temporal-spatial sensemaking**, and **FAIR+CARE-aligned visualization ethics**.

![Docs](https://img.shields.io/badge/Docs·MCP-v6.3-blue)
![License](https://img.shields.io/badge/License-CC--BY--4.0-green)
![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Certified-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

Focus Mode overlays are **algorithmically generated visual layers** that synchronize with timeline scrolling, contextual panel updates, and map navigation.  
These overlays summarize correlations, anomalies, historical alignments, hydrologic signals, entity interactions, and AI-explained narratives.

Each overlay stored here follows:
- **STAC/DCAT-backed metadata**
- **Full checksum lineage**
- **CARE-compliant generalization for sensitive spatial features**
- **WCAG 2.1 AA display safety**
- **FAIR+CARE-certified visual ethics**

---

## 🗂️ Directory Layout

```plaintext
docs/reports/visualization/focus_mode/overlays/
├── drought_overlay.png
├── settlement_density_overlay.webp
├── treaty_boundary_context.svg
├── hydrology_anomaly_overlay.png
├── story_alignment_overlay.json        # AI narrative alignment summary
├── metadata/                           # STAC/DCAT-aligned sidecar metadata
│   ├── drought_overlay.json
│   ├── settlement_density_overlay.json
│   ├── treaty_boundary_context.json
│   ├── hydrology_anomaly_overlay.json
│   └── story_alignment_overlay.json
└── README.md
```

---

## 🧩 Overlay Types

| Overlay Type | Description | Typical Format |
|--------------|-------------|----------------|
| **Hydrology Overlay** | Drought/flood indices, groundwater anomalies, surface moisture gradients. | PNG |
| **Archaeology / Settlement Overlay** | Kernel-density surfaces, cross-era site clusters, inferred habitation zones. | WebP / PNG |
| **Treaty / Boundary Context** | Historical treaty polygons, disputed lines, or relocation pathways. | SVG |
| **AI Narrative Alignment Layer** | Model-backed signals linking story nodes to map locations. | JSON |
| **Temporal Dynamics** | Time-series change layers linked to Focus Mode timeline. | PNG / WebP |

---

## 🔑 Metadata Requirements

Each overlay must include a metadata entry conforming to the Focus Mode visualization schema:

```json
{
  "id": "focusmode_overlay_drought_v10_2025",
  "domain": "focus_mode",
  "type": "hydrology_overlay",
  "fairstatus": "certified",
  "care_status": "approved",
  "asset_file": "drought_overlay.png",
  "checksum_sha256": "sha256-<hash>",
  "generated_by": "focus_mode_overlay_engine_v10.2",
  "created": "2025-11-12T08:52:00Z",
  "stac_extensions": ["https://stac-extensions.github.io/raster/v1.0.0/schema.json"],
  "provenance": "Derived from USDM + Daymet + KFM Hydrology Layers"
}
```

---

## ♿ Accessibility Standards

- Minimum contrast ratio: **4.5:1**  
- Avoid red–green conflict; include texture-based symbology  
- All overlays must have alt-text in metadata JSON  
- Animated overlays require static fallback images  

---

## ⚙️ FAIR+CARE Visualization Governance

| Principle | Implementation |
|-----------|----------------|
| **Findable** | Overlay IDs + metadata stored in STAC/DCAT catalogs |
| **Accessible** | Openly licensed overlays (CC-BY 4.0) |
| **Interoperable** | Spatial formats: PNG, SVG, WebP, JSON + metadata |
| **Reusable** | Backed by commit SHA + reproducible pipeline references |
| **CARE** | Sensitive Indigenous sites masked or generalized |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| v10.2.0 | 2025-11-12 | KFM Visualization Council | Initial index for Focus Mode overlay layer visualizations. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
Master Coder Protocol v6.3 · FAIR+CARE Certified  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Visualization Index](../README.md) · [Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

