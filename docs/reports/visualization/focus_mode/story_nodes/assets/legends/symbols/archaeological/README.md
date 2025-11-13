---
title: "🏺 Kansas Frontier Matrix — Archaeological Legend Symbols Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/archaeological/README.md"
version: "v10.2.0"
last_updated: "2025-11-12"
review_cycle: "Quarterly / FAIR+CARE Heritage Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/reports-visualization-focusmode-archsymbols-v1.json"
governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🏺 **Archaeological Legend Symbols — Focus Mode Story Node System**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/archaeological/README.md`

**Purpose:**  
Define and inventory all **archaeological legend symbols** used in Focus Mode’s story node visualizations, including habitation sites, artifact class markers, protected heritage indicators, and culturally sensitive symbology.  
All icons adhere to **FAIR+CARE cultural governance**, **WCAG accessibility**, and KFM’s **v10 visualization standards**.

![Docs](https://img.shields.io/badge/Docs·MCP-v6.3-blue)
![License](https://img.shields.io/badge/License-CC--BY--4.0-green)
![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Certified-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

The archaeological symbol set ensures consistent, respectful, and accessible visualization of historical and pre-contact cultural information within Focus Mode.  
These symbols appear in:

- Story Node maps & timelines  
- 2D MapLibre layers  
- 3D Cesium scenes  
- AI-generated narrative context panes  

All representations must follow **generalization guidelines** for sensitive heritage locations.

---

## 🗂️ Directory Layout

```plaintext
archaeological/
├── README.md                          # This file
├── village_generalized.svg            # Generalized habitation site
├── pottery_marker.svg                 # Ceramic artifact class marker
├── mound_protected.svg                # Burial mound (restricted CARE)
├── excavation_unit.svg                # Archaeological excavation trench
├── sacred_site_restricted.svg         # Restricted sacred location (heavily generalized)
└── metadata/
    ├── README.md
    ├── field_definitions.md
    └── examples/
```

---

## 🧩 Archaeological Symbol Categories

| Category | Description | CARE Status |
|---------|-------------|-------------|
| **Habitation / Villages** | Generalized settlement indicators; no precise coordinates | Approved |
| **Ceramic / Lithic Markers** | Artifact-type indicators for maps & timelines | Approved |
| **Excavation Units** | Excavation trench or grid markers | Approved |
| **Burial / Mound Sites** | Sensitive cultural sites requiring high-level generalization (≥20 km) | Restricted |
| **Sacred Sites** | Restricted; only shown with tribal approval and coarse spatial masking | Restricted |

---

## 🧠 Design & Accessibility Requirements

### SVG Format Rules
- Vector only (no raster)  
- ViewBox: `0 0 24 24`  
- Stroke width: 2px equivalent  
- Rounded line caps/joins  

### Accessibility (WCAG 2.1 AA)
- Icon contrast ≥ **3:1**  
- Provide `<title>` and `<desc>` in SVG markup  
- Icons must remain distinguishable at **18–32px** render sizes  

---

## ⚖️ CARE Governance Requirements

Sensitive archaeological symbols (mounds, sacred areas) require:

- CARE metadata block (`status: "restricted"` or `"approved"` with conditions)  
- Review by the **FAIR+CARE Heritage Council**  
- Spatial generalization before visualization  
- Inclusion in governance ledger (dataset + symbology approval)  

Example CARE metadata entry:

```json
{
  "id": "arch_symbol_sacred_site_restricted_v10",
  "care": {
    "status": "restricted",
    "reviewer": "FAIR+CARE Heritage Council",
    "statement": "Symbol may only represent generalized cultural zones.",
    "date_reviewed": "2025-11-12"
  }
}
```

---

## 🔍 Provenance & Telemetry Integration

All archaeological symbols must integrate with:

- **focus-telemetry.json** (energy, carbon, validation metrics)  
- **SBOM entries** for artifact integrity  
- **Manifest-linked checksums** (SHA-256)  
- **Story Node metadata schemas**  

Validation workflows:
- `faircare-validate.yml`  
- `docs-lint.yml`  
- `telemetry-export.yml`  

---

## 🧾 Example Symbol Definition

```json
{
  "id": "village_generalized_v10",
  "title": "Generalized Village Marker",
  "domain": "archaeology",
  "format": "SVG",
  "checksum_sha256": "sha256-a34fbb129c9e...",
  "care": {
    "status": "approved",
    "statement": "Generalized spatially to 15 km cluster resolution."
  },
  "updated": "2025-11-12T19:51:00Z"
}
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| v10.2.0 | 2025-11-12 | FAIR+CARE Heritage Council | Initial archaeological symbol index with CARE-sensitive rules and v10 metadata. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · Master Coder Protocol v6.3  
**Diamond⁹ Ω / Crown∞Ω Ultimate Certified**

[⬅ Back to Legend Symbols](../README.md)

</div>

