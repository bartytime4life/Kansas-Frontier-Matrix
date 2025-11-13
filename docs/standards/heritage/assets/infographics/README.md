---
title: "🗺️ Kansas Frontier Matrix — Heritage Infographics Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/heritage/assets/infographics/README.md"
version: "v10.2.3"
last_updated: "2025-11-13"
review_cycle: "Annual / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/standards-heritage-infographics-v1.json"
governance_ref: "../../../governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🗺️ **Kansas Frontier Matrix — Heritage Infographics Index**  
`docs/standards/heritage/assets/infographics/README.md`

**Purpose:**  
Serve as the centralized reference for all **infographics, educational diagrams, risk matrices, and visual explainers** used in the KFM Heritage Standards Suite (H3, CARE, archaeological sensitivity, protection levels, etc.).

<img alt="Infographics" src="https://img.shields.io/badge/Infographics-Heritage_Standards-brown" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold" />
<img alt="Protected Data" src="https://img.shields.io/badge/Protection-Level_III-red" />

</div>


---

## 📚 Overview

This directory includes **visual educational materials** that support:

- Heritage protection workflows  
- H3 generalization explanations  
- Cultural sensitivity + CARE labeling  
- Heritage risk mitigation matrices  
- Public-facing communication diagrams  
- STAC/DCAT documentation visuals  
- Training materials for analysts and researchers  

All infographics must:

- Use abstract, non-sensitive graphics  
- Avoid any depiction of cultural or sacred objects  
- Comply with FAIR+CARE ethical communication standards  
- Maintain WCAG 2.1 AA contrast  
- Follow KFM visual branding guidelines  
- Use SVG as primary format (vector-first)  

---

### 🗂️ Directory Layout

    infographics/
    |-- README.md                              # This document
    |
    |-- heritage_risk_matrix.svg               # Cultural + archaeological risk model
    |-- h3-resolution-scale.svg                # H3 resolution explainer (r5–r9)
    |-- h3-generalization-overview.svg         # H3 workflow for heritage masking
    |-- care-sensitivity-levels.svg            # CARE cultural sensitivity diagram
    |-- heritage_protection_levels.svg         # Level I–III protection explainer
    |-- spatial_masking_vs_precision.svg       # Comparison graphic for masking methods
    |
    └── ...                                    # Additional educational diagrams

---

## 🎨 Infographic Requirements

- **All diagrams must be vector-based (SVG)**  
- **No sacred imagery or sensitive site shapes**  
- **No geographic detail finer than H3-r7**  
- Abstraction only—hexes, layers, arrows, conceptual icons  
- Must meet FAIR+CARE review before inclusion  
- Must include metadata comments describing:  
  - creator  
  - date  
  - version  
  - CARE classification  
  - intended use  

---

## 🛡️ Governance Checks

All new infographics must pass:

- **Heritage Stewardship Review**  
- **FAIR+CARE Council approval**  
- **Schema linkage validation** (if applicable)  
- **No sensitive or culturally inappropriate outputs**  
- **Accessibility test**—WCAG 2.1 AA minimum

Local validator:

    make validate-heritage-assets

---

## 🕒 Version History

| Version  | Date       | Notes                                                                         |
|----------|------------|-------------------------------------------------------------------------------|
| v10.2.3  | 2025-11-13 | Initial heritage infographics index — fully memory-rule compliant.            |
