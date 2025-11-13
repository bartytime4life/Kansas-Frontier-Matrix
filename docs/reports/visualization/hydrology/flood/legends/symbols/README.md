---
title: "🗾 Kansas Frontier Matrix — Flood Legend Symbol Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/hydrology/flood/legends/symbols/README.md"
version: "v10.2.0"
last_updated: "2025-11-12"
review_cycle: "Quarterly / FAIR+CARE Visualization Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/reports-visualization-hydrology-flood-symbols-v1.json"
governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🗾 **Kansas Frontier Matrix — Flood Legend Symbol Registry**  
`docs/reports/visualization/hydrology/flood/legends/symbols/README.md`

**Purpose:**  
Define the **standardized symbolography** used in all hydrological flood visualizations across Kansas Frontier Matrix (KFM).  
Ensures all icons, markers, hazard indicators, and map annotations meet **FAIR+CARE ethics**, **WCAG 2.1 AA accessibility**, and **STAC/DCAT provenance** requirements.

![Docs MCP](https://img.shields.io/badge/Docs·MCP-v6.3-blue)
![License](https://img.shields.io/badge/License-CC--BY--4.0-green)
![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Certified-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

This registry catalogs **all flood-related symbols** used in hydrology visualization products such as:
- Flood extent maps  
- Recurrence interval diagrams  
- Flash flood hotspot overlays  
- Drought–flood composite dashboards  
- Focus Mode v2 hydrology panels  

Each symbol includes:
- A machine-readable metadata file  
- Accessibility verification (shape contrast, color safety)  
- FAIR+CARE alignment  
- STAC/DCAT metadata linkage  
- Reproducibility provenance (commit SHA, checksum)

---

## 🗂️ Directory Layout

```plaintext
docs/reports/visualization/hydrology/flood/legends/symbols/
├── README.md                                  # This file
├── flood_marker_major.svg                     # Major flood event marker
├── flood_marker_minor.svg                     # Minor flood event marker
├── flood_marker_flash.svg                     # Flash flood indicator
├── levee_failure_icon.svg                     # Levee failure symbol
├── inundation_boundary.svg                    # Boundary line symbol
└── metadata/                                   # FAIR+CARE/STAC metadata
    ├── flood_marker_major.json
    ├── flood_marker_minor.json
    ├── flood_marker_flash.json
    ├── levee_failure_icon.json
    └── inundation_boundary.json
```

---

## 🧩 Symbol Metadata Requirements

| Field | Description | Required |
|--------|-------------|----------|
| `id` | Unique symbol identifier | ✅ |
| `title` | Human-readable label | ✅ |
| `symbol_type` | Point / line / polygon / annotation | ✅ |
| `description` | Semantic purpose of the symbol | ✅ |
| `color_profile` | Hex values + WCAG contrast rating | ⚙️ |
| `shape_description` | Geometric/semantic explanation | ⚙️ |
| `care_status` | `approved` / `restricted` | ⚙️ |
| `accessibility_score` | 0–1 WCAG 2.1 AA compliance rating | ✅ |
| `checksum_sha256` | Symbol file integrity | ⚙️ |
| `created` | ISO timestamp | ✅ |
| `commit_sha` | Provenance reference | ⚙️ |
| `stac_item` | Linked STAC catalog entry | ⚙️ |

---

## 🧾 Example Symbol Metadata (Major Flood Marker)

```json
{
  "id": "symbol_flood_major_v10",
  "title": "Major Flood Event Marker",
  "symbol_type": "point",
  "description": "Indicates locations where flood severity exceeded the 90th percentile.",
  "color_profile": {
    "fill": "#0047AB",
    "stroke": "#FFFFFF",
    "wcag_contrast_ratio": 4.9
  },
  "shape_description": "Circle with thick white stroke for high visibility.",
  "care_status": "approved",
  "accessibility_score": 0.98,
  "checksum_sha256": "sha256-abc123...def456",
  "created": "2025-11-12T12:10:00Z",
  "commit_sha": "<latest-commit-hash>",
  "stac_item": "kfm-flood-symbols-v10"
}
```

---

## ⚙️ FAIR+CARE & Accessibility Rules

### Required Ethical & Accessibility Validations
- **Colorblind-safe** shapes and hues  
- **WCAG AA-compliant** symbol contrast  
- **CARE protections** for sensitive tribal hydrology areas  
- No symbols may imply **cultural, political, or legal interpretations**  
- Symbols must retain meaning in:
  - High-contrast mode  
  - Screen-reader alt-text mappings  
  - Low-vision magnification  

---

## 🧪 Validation Workflows

| Workflow | Purpose | Output |
|----------|----------|---------|
| `visualization-validate.yml` | Checks metadata fields & accessibility metrics | `metadata_validation.json` |
| `faircare-validate.yml` | CARE ethics audit | `symbol_faircare.json` |
| `stac-validate.yml` | STAC/DCAT registry validation | `stac_validation.json` |
| `telemetry-export.yml` | Sustainability logging | `focus-telemetry.json` |

---

## 📊 Symbol Usage & Provenance Checks

- Every flood visualization must reference one of these registered symbols.  
- Symbols are version-locked and must match the checksum declared in their metadata.  
- Any new or modified symbol requires:
  - FAIR+CARE Board review  
  - Accessibility audit  
  - STAC catalog entry  
  - Updated telemetry event  

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|------|---------|---------|
| v10.2.0 | 2025-11-12 | Hydrology Visualization Board | Initial creation of flood legend symbol registry under FAIR+CARE. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Flood Legends](../README.md) · [Visualization Index](../../../README.md)

</div>

