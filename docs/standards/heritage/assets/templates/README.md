---
title: "🏺 Kansas Frontier Matrix — Heritage Standards Templates Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/heritage/assets/templates/README.md"
version: "v10.2.3"
last_updated: "2025-11-13"
review_cycle: "Annual / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/standards-heritage-templates-v1.json"
governance_ref: "../../../governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🏺 **Kansas Frontier Matrix — Heritage Standards Templates Index**  
`docs/standards/heritage/assets/templates/README.md`

**Purpose:**  
Provide the official template set for **H3 generalization**, **heritage-sensitive STAC Items**, **DCAT metadata**, and **Story Node heritage integration**, ensuring consistent, FAIR+CARE-aligned modeling across all KFM heritage workflows.

<img alt="Templates" src="https://img.shields.io/badge/Templates-Heritage_Standards-brown" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold" />
<img alt="Protection" src="https://img.shields.io/badge/Protection-Level_III-red" />

</div>


---

## 📚 Overview

This template directory provides **ready-to-use, schema-compliant** JSON files for:

- Heritage STAC Item definitions  
- Generalized H3 heritage dataset packaging  
- DCAT metadata blocks  
- Story Node heritage metadata  
- Lineage and reproducibility templates  
- CARE sensitivity declarations  

All templates:

- Follow KFM Markdown + memory rules  
- Contain **indented JSON only** (no nested code fencing)  
- Conform to STAC 1.0 + DCAT 3.0  
- Enforce FAIR+CARE cultural governance  
- Match schemas under `docs/standards/heritage/schemas/`  

---

### 🗂️ Directory Layout

    templates/
    |-- README.md                                 # This document
    |-- heritage_stac_template.json               # STAC Item template for heritage datasets
    |-- heritage_dcat_template.json               # DCAT metadata template
    |-- storynode_heritage_template.json          # Story Node heritage metadata template
    |-- lineage_provenance_template.json          # Provenance + versioning + reproducibility
    └── h3_generalization_template.json           # Standard H3 mapping template

---

## 🧱 Template — Heritage STAC Item

    {
      "stac_version": "1.0.0",
      "type": "Item",
      "id": "<dataset-id>",
      "collection": "kfm-heritage",
      "properties": {
        "heritage_protected": true,
        "generalization_method": "H3",
        "h3_resolution": 7,
        "raw_coordinates_removed": true,
        "legal_basis": "NHPA Section 304",
        "care_level": "Level III"
      },
      "assets": {
        "generalized_hexes": {
          "href": "<path-to-hex-geojson>",
          "type": "application/geo+json",
          "roles": ["data"]
        }
      }
    }

---

## 🧩 Template — DCAT Metadata Extract

    {
      "dct:title": "<Dataset Title>",
      "dct:spatialResolution": "H3-r7",
      "dct:provenance": "Generalized from protected archaeological coordinates",
      "dct:conformsTo": "KFM H3 Heritage Generalization Standard",
      "dct:rights": "NHPA §304 confidentiality applies"
    }

---

## 🧠 Template — Story Node Heritage Metadata

    {
      "id": "<storynode-id>",
      "type": "story-node",
      "title": "<Title>",
      "heritage_protected": true,
      "h3_id": "<h3-index>",
      "h3_resolution": 7,
      "cultural_sensitivity": "<public|restricted|sacred>",
      "periods": ["<Period>"],
      "summary": "<Generalized narrative text>",
      "display_rules": {
        "map": "hex",
        "timeline": true,
        "header": false
      }
    }

---

## 🧬 Template — Lineage & Reproducibility

    {
      "version": "<version-string>",
      "lineage": {
        "predecessor": "<previous-version>",
        "successor": "<next-version>",
        "latest": "<latest-version>"
      },
      "reproducibility": {
        "workflow_hash": "<sha256-hash>",
        "inputs_hash": "<sha256-hash>"
      }
    }

---

## 🛡️ Template — H3 Generalization

    {
      "h3_id": "<hex-id>",
      "h3_resolution": 7,
      "generalization_method": "H3",
      "raw_coordinates_removed": true,
      "heritage_protected": true,
      "care_level": "Level III"
    }

---

## 🕒 Version History

| Version  | Date       | Notes                                                                         |
|----------|------------|-------------------------------------------------------------------------------|
| v10.2.3  | 2025-11-13 | Initial heritage templates index — fully memory-rule compliant.                |
