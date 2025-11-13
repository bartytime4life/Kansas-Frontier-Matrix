---
title: "🧩 Kansas Frontier Matrix — Focus Mode Overlay Metadata Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/overlays/metadata/README.md"
version: "v10.2.0"
last_updated: "2025-11-12"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/reports-visualization-focusmode-overlays-metadata-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧩 **Kansas Frontier Matrix — Focus Mode Overlay Metadata Index**  
`docs/reports/visualization/focus_mode/overlays/metadata/README.md`

**Purpose:**  
Provide a centralized FAIR+CARE-compliant registry of **metadata sidecars** describing every Focus Mode overlay (hydrology, archaeology, treaty boundaries, anomaly layers, AI narrative alignments).  
Each metadata entry defines lineage, checksums, provenance, CARE status, and STAC/DCAT interoperability fields.

![Docs](https://img.shields.io/badge/Docs·MCP-v6.3-blue)
![License](https://img.shields.io/badge/License-CC--BY--4.0-green)
![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Certified-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

Metadata stored here governs **how overlays are interpreted, reproduced, and ethically distributed** within Focus Mode.  
Each JSON file provides:
- Provenance & lineage  
- Spatial/temporal extents  
- Raster/vector schema alignment  
- Ethical notes & CARE masking flags  
- AI-generation descriptors (for narrative overlays)  
- STAC & DCAT mappings  
- SHA-256 integrity checks

These metadata files are referenced directly by the Focus Mode UI, STAC catalog builder, and FAIR+CARE visualization auditor.

---

## 🗂️ Directory Layout

```plaintext
docs/reports/visualization/focus_mode/overlays/metadata/
├── drought_overlay.json
├── settlement_density_overlay.json
├── treaty_boundary_context.json
├── hydrology_anomaly_overlay.json
├── story_alignment_overlay.json
└── README.md
```

---

## 🧩 Metadata Schema Requirements

Each overlay metadata JSON must follow the Focus Mode Metadata Schema:

```json
{
  "id": "focus_overlay_<name>_v10",
  "title": "Drought Severity Overlay (v10)",
  "domain": "hydrology",
  "type": "raster", 
  "fairstatus": "certified",
  "care_status": "approved",
  "asset": "drought_overlay.png",
  "checksum_sha256": "sha256-<hash>",
  "provenance": "Derived from USDM + Daymet + KFM Hydrology Engine",
  "stac_extensions": [
    "https://stac-extensions.github.io/raster/v1.0.0/schema.json"
  ],
  "bbox": [-102.05, 37.0, -94.6, 40.0],
  "datetime": "2025-11-10T00:00:00Z",
  "created": "2025-11-12T09:12:00Z",
  "pipeline_ref": "src/pipelines/visualization/focusmode_overlays_v10/",
  "alt_text": "Raster overlay showing Kansas drought intensity contours aggregated for Focus Mode v10."
}
```

All fields are validated in:
```
.github/workflows/stac-validate.yml
.github/workflows/faircare-validate.yml
.github/workflows/docs-lint.yml
```

---

## 🔑 FAIR+CARE Visualization Requirements

| Requirement | Description |
|------------|-------------|
| **Alt-Text Required** | Every overlay requires descriptive alt-text for accessibility. |
| **Generalization** | Sensitive cultural or archaeological sites must be masked or coarsened. |
| **CARE Reviewer** | Each file must include CARE review status (`approved`, `restricted`, `revision`). |
| **Checksum Integrity** | SHA-256 hash recorded and cross-checked with release manifest. |
| **STAC/DCAT Compliance** | Fields must be machine-ready for catalog syncing. |

---

## ⚙️ Usage in Focus Mode

- Automatically loaded by STAC lookup when user enables an overlay  
- Used by AI narrative generator to reference overlay-specific spatial logic  
- Drives tooltips, legends, and cross-panel highlighting  
- Integrated into temporal playback and density-time graphs  

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| v10.2.0 | 2025-11-12 | KFM Visualization Council | Created metadata index directory with FAIR+CARE and STAC/DCAT integration. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
Master Coder Protocol v6.3 · FAIR+CARE Visualization Certified  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Overlays](../README.md) · [Visualization Index](../../README.md) · [Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

