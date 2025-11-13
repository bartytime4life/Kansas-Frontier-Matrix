---
title: "🏺 Kansas Frontier Matrix — Heritage Standards Examples Library (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/heritage/examples/README.md"
version: "v10.2.3"
last_updated: "2025-11-13"
review_cycle: "Annual / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/standards-heritage-examples-v1.json"
governance_ref: "../../governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🏺 **Kansas Frontier Matrix — Heritage Standards Examples Library**  
`docs/standards/heritage/examples/README.md`

**Purpose:**  
Provide a complete set of **developer-ready, FAIR+CARE compliant example files** demonstrating how to implement all heritage standards, including H3 generalization, sensitive-site metadata, lineage requirements, and STAC/DCAT publication workflows.

<img alt="Examples" src="https://img.shields.io/badge/Examples-Heritage_Standards-brown" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold" />
<img alt="Heritage Protection" src="https://img.shields.io/badge/Protection-Level_III-red" />

</div>


---

## 📚 Overview

This directory contains **fully validated example files** used as templates for:

- H3 spatial generalization  
- Sensitive-location metadata  
- Archaeological protection schemas  
- STAC Item creation  
- DCAT metadata integration  
- Story Node heritage metadata  
- Cultural sensitivity tagging (CARE)  
- Lineage & reproducibility fields  

All examples:

- Follow KFM’s strict **Markdown Protocol**
- Contain **indented JSON blocks only**
- Are 100% **FAIR+CARE compliant**
- Match the formal schemas under `docs/standards/heritage/schemas/`
- Use **memory-rule formatting** with proper heading hierarchy

Use these when implementing or validating heritage pipelines.

---

### 🗂️ Directory Layout

    examples/
    |-- README.md                           # This index document
    |
    |-- h3-generalization-demo.json         # Example H3-converted heritage dataset
    |-- sensitive-location-example.json     # Example protected metadata entry
    |-- heritage-dataset-stac.json          # Example STAC Item (heritage)
    |-- heritage-dataset-dcat.json          # Example DCAT metadata extract
    |-- provenance-lineage-example.json     # Example lineage + reproducibility block
    |
    └── storynode-heritage-demo.json        # Example Story Node heritage metadata

---

## 🧱 Example — H3 Generalization Output (r7)

    {
      "h3_id": "872830829ffffff",
      "h3_resolution": 7,
      "site_count": 4,
      "periods": ["Archaic", "Late Prehistoric"],
      "heritage_protected": true,
      "generalization_method": "H3",
      "raw_coordinates_removed": true
    }

---

## 🏺 Example — Sensitive Location Metadata

    {
      "id": "KS-ARCH-004198",
      "type": "heritage_site",
      "cultural_sensitivity": "restricted",
      "legal_basis": "NHPA Section 304",
      "care_level": "Level III",
      "tribal_affiliation": ["Kaw Nation"],
      "description": "Earthen mound feature with significant cultural history.",
      "h3_id": "872830829ffffff",
      "h3_resolution": 7
    }

---

## 📦 Example — STAC Item (Heritage)

    {
      "stac_version": "1.0.0",
      "type": "Item",
      "id": "ks-heritage-generalized-2025",
      "collection": "kfm-heritage",
      "properties": {
        "heritage_protected": true,
        "generalization_method": "H3",
        "h3_resolution": 7,
        "raw_coordinates_removed": true,
        "care_level": "Level III"
      },
      "assets": {
        "hex_geojson": {
          "href": "hexes/ks-heritage-2025.geojson",
          "type": "application/geo+json",
          "roles": ["data"]
        }
      }
    }

---

## 🗃️ Example — DCAT Metadata Extract

    {
      "dct:title": "Kansas Protected Heritage (Generalized to H3-r7)",
      "dct:spatialResolution": "H3-r7",
      "dct:provenance": "Generalized from protected archaeological coordinates",
      "dct:conformsTo": "KFM H3 Heritage Generalization Standard",
      "dct:rights": "NHPA §304 restrictions apply"
    }

---

## 🧬 Example — Lineage & Reproducibility

    {
      "version": "2025.10.31",
      "lineage": {
        "predecessor": "2025.07.15",
        "successor": "2026.02.01",
        "latest": "2026.02.01"
      },
      "reproducibility": {
        "workflow_hash": "sha256-b94c…",
        "inputs_hash": "sha256-09af…"
      }
    }

---

## 🧩 Example — Story Node Heritage Metadata

    {
      "id": "node-ks-heritage-102",
      "type": "story-node",
      "title": "Ancient Mound Site (Generalized)",
      "heritage_protected": true,
      "h3_id": "872830829ffffff",
      "h3_resolution": 7,
      "cultural_sensitivity": "restricted",
      "periods": ["Late Woodland"],
      "summary": "A generalized representation of an important heritage location.",
      "display_rules": {
        "map": "hex",
        "timeline": true
      }
    }

---

## 🕒 Version History

| Version  | Date       | Notes                                                                 |
|----------|------------|-----------------------------------------------------------------------|
| v10.2.3  | 2025-11-13 | Initial examples library — fully memory-rule compliant.               |
