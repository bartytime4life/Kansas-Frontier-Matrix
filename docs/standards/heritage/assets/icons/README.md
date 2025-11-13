---
title: "🏺 Kansas Frontier Matrix — Heritage Standards Icon Library (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/heritage/assets/icons/README.md"
version: "v10.2.3"
last_updated: "2025-11-13"
review_cycle: "Annual / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/standards-heritage-icons-v1.json"
governance_ref: "../../../governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🏺 **Kansas Frontier Matrix — Heritage Standards Icon Library**  
`docs/standards/heritage/assets/icons/README.md`

**Purpose:**  
Provide a centralized library of **FAIR+CARE-approved vector icon assets** for heritage standards, including protection level badges, cultural sensitivity markers, H3 indicators, and abstract representations used across Story Nodes, STAC metadata, ethical warnings, and governance dashboards.

<img alt="Icon Library" src="https://img.shields.io/badge/Icons-Heritage_Standards-brown" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold" />
<img alt="Protection Level" src="https://img.shields.io/badge/Protection_Level-III-red" />

</div>


---

## 📚 Overview

This directory contains **all approved heritage icon assets**, used across:

- Story Nodes (heritage-tagged nodes)
- H3 masking explanations
- Sensitive-site warnings
- Protection-level badges (I–III)
- CARE cultural-sensitivity indicators
- STAC/DCAT dataset documentation
- Focus Mode UI components
- Governance & audit dashboards

All icons are:

- **FAIR+CARE-compliant**
- **Abstract**, non-representational
- **Vector-first (SVG only)**
- **WCAG-accessible**
- **Culturally respectful**  
- Explicitly **non-depictive**: no sacred objects, no site silhouettes, no culturally sensitive imagery

---

### 🗂️ Directory Layout

    icons/
    |-- README.md                                   # This document
    |
    |-- heritage_protected.svg                      # Generic icon for protected heritage data
    |-- heritage_level_I.svg                        # Level I protection badge
    |-- heritage_level_II.svg                       # Level II protection badge
    |-- heritage_level_III.svg                      # Level III protection badge (default for KFM)
    |
    |-- care_flag_public.svg                        # CARE tag: public-level cultural data
    |-- care_flag_restricted.svg                    # CARE tag: restricted cultural data
    |-- care_flag_sacred.svg                        # CARE tag: sacred or closed data
    |
    |-- h3_generalization.svg                       # Icon representing H3 spatial masking
    |-- coordinate_removed.svg                      # Icon indicating coordinate-stripping requirement
    |
    |-- risk_indicator_low.svg                      # Low cultural risk
    |-- risk_indicator_medium.svg                   # Medium cultural risk
    |-- risk_indicator_high.svg                     # High cultural risk
    |
    └── ...                                         # Additional CARE/heritage-safe icons

---

## 🎨 Icon Standards & Requirements

All icons must adhere to strict KFM standards:

### 🧩 Format Requirements
- **SVG only (vector-based)**
- Clean markup; no editor metadata (Inkscape/Illustrator junk)
- No embedded rasters
- No filters, glows, blurs, drop shadows

### 🧩 Ethical Requirements (FAIR+CARE)
- No cultural object depictions  
- No sacred imagery  
- No reconstruction silhouettes  
- No identifiable site markers  
- Only **abstract symbols** (shapes, color coding, badges)

### 🧩 Spatial Safety Requirements
- Icons must never encode:
  - location hints  
  - geographic shapes  
  - approximate coordinates  
  - site outlines  

### 🧩 Accessibility Requirements
- WCAG 2.1 AA contrast  
- Readable at:
  - **32×32 px** interactive  
  - **16 pt** print  
- Shape + color redundancy  

---

## 🔗 Metadata & Integration Requirements

Each icon must be referenced through metadata files in:

- `docs/standards/heritage/schemas/`
- `docs/standards/heritage/examples/`
- STAC “legend/symbol” assets when appropriate
- Story Node heritage metadata blocks

### Example metadata mapping (indented):

    {
      "id": "heritage_protected",
      "label": "Protected Heritage Marker",
      "svg": "../icons/heritage_protected.svg",
      "care_level": "Level III",
      "description": "Indicates generalized, protected cultural data."
    }

---

## 🛡️ Governance & Review

Before inclusion, each icon must undergo:

- **Heritage Stewardship Unit review**
- **FAIR+CARE Council approval**
- Cultural-safety vetting  
- Accessibility compliance checking  
- Schema alignment validation  

Icons added without proper review must not be used in any KFM system.

---

## 🧪 Validation

Local validator (pseudo):

    make validate-heritage-assets

Checks include:

- File existence  
- Metadata linkage  
- SVG hygiene rules  
- CARE-compliant structure  

---

## 🕒 Version History

| Version  | Date       | Notes                                                                  |
|----------|------------|------------------------------------------------------------------------|
| v10.2.3  | 2025-11-13 | Initial heritage icon index — fully memory-rule compliant.             |
