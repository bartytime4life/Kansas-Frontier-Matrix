---
title: "🏺 Kansas Frontier Matrix — Archaeological Symbol Metadata Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/metadata/archaeological/README.md"
version: "v10.2.3"
last_updated: "2025-11-13"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../../schemas/telemetry/reports-visualization-focus-archaeological-symbols-v1.json"
governance_ref: "../../../../../../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🏺 **Kansas Frontier Matrix — Archaeological Symbol Metadata Overview**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/symbols/metadata/archaeological/README.md`

**Purpose:**  
Define and document the metadata structure governing archaeological symbol sets used across Focus Mode, Story Nodes, map legends, and STAC-linked cultural heritage datasets.

<img alt="Metadata" src="https://img.shields.io/badge/Metadata-Archaeology-brown" />
<img alt="Archaeology" src="https://img.shields.io/badge/Domain-Cultural%20Heritage-maroon" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Certified-gold" />

</div>


---

## 📚 Overview

This directory contains all **canonical metadata definitions** for archaeological symbols representing:

- Excavation areas  
- Artifact discovery locations  
- Historic settlement layers  
- Cultural sites  
- Protected archaeological zones  
- Material culture classifications  

These metadata structures ensure:

- Uniform archaeological symbol semantics  
- FAIR+CARE–aligned cultural heritage treatment  
- Accurate linkage between icons, Story Nodes, and STAC datasets  
- Reproducible and transparent symbol governance  
- Respect for Indigenous cultural knowledge and restricted/sensitive sites  

All archaeological symbols used anywhere in KFM must be defined here.

---

### 🗂️ Directory Layout

    archaeological/
    |-- README.md                                # This document
    |-- archaeological-symbols.json              # Canonical symbol registry
    |-- archaeological-symbols.stac.json         # STAC metadata for symbols
    |-- archaeological-symbols-story-nodes.json  # Story Node binding rules
    |
    └── examples/                                # Developer metadata examples

---

### 🧱 Archaeological Symbol Registry — `archaeological-symbols.json`

Defines each archaeological symbol’s:

- id  
- category (site, artifact, excavation, feature, cultural area)  
- label  
- description  
- svg path  
- png (optional)  
- emoji fallback  
- sensitivity classification (public / restricted / sacred)  
- archaeological_type (feature code / artifact type)  

Example (indented):

    {
      "id": "burial_protected",
      "category": "cultural_site",
      "label": "Protected Burial Area",
      "description": "Culturally sensitive protected burial zone.",
      "svg": "../svg/burial_protected.svg",
      "emoji": "⚱️",
      "archaeological_type": "burial_area",
      "cultural_sensitivity": "restricted"
    }

---

### 🧩 STAC Metadata — `archaeological-symbols.stac.json`

This file defines STAC-compliant symbol metadata for external cataloging:

- Links each SVG asset using `roles: ["legend", "symbol"]`  
- Provides descriptive title and category fields  
- Includes CARE labels and cultural sensitivity metadata  
- Ensures discoverability under the `kfm-legends` collection  

Example (indented):

    {
      "stac_version": "1.0.0",
      "type": "Item",
      "id": "legend-symbols-archaeological-v1",
      "collection": "kfm-legends",
      "assets": {
        "burial_protected_svg": {
          "href": "../svg/burial_protected.svg",
          "type": "image/svg+xml",
          "roles": ["legend", "symbol"],
          "title": "Protected Burial Area Icon"
        }
      }
    }

---

### 🧠 Story Node Bindings — `archaeological-symbols-story-nodes.json`

Controls how archaeological symbols appear in Story Nodes:

- Header or sidebar badge usage  
- Contexts (archaeology, Indigenous history, cultural sites)  
- Emoji fallback rules  
- Sensitivity labels (public, restricted, or sacred)  
- Narrative assistive labeling  

Example (indented):

    {
      "archaeological_discovery": {
        "label": "Archaeological Discovery",
        "badge": true,
        "emoji": "🏺",
        "contexts": ["archaeology", "history"],
        "cultural_sensitivity": "public"
      }
    }

---

### 🧪 Validation & CI

All archaeological metadata undergoes:

- JSON Schema validation  
- STAC validation  
- SVG/PNG asset existence checks  
- Story Node linkage checks  
- Cultural sensitivity compliance audit  
- Snapshot linkage validation (if icons generate preview sheets)  

Local validation (indented):

    make test-legends-archaeological

All metadata must pass CI before merging.

---

### 🕒 Version History

| Version  | Date       | Author        | Notes                                                                |
|----------|------------|---------------|----------------------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial archaeological metadata README, fully memory-rule compliant. |