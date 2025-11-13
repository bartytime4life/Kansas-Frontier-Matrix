---
title: "🏺 Kansas Frontier Matrix — Archaeological Legend Metadata Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/metadata/archaeological/README.md"
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

# 🏺 **Kansas Frontier Matrix — Archaeological Legend Metadata Overview**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/metadata/archaeological/README.md`

**Purpose:**  
Serve as the metadata index for all **archaeological symbol systems** used in Focus Mode, Story Nodes, map legends, and STAC-compliant cultural heritage datasets.

<img alt="Metadata" src="https://img.shields.io/badge/Metadata-Archaeological-brown" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Governed-gold" />
<img alt="STAC" src="https://img.shields.io/badge/STAC-1.0%20Aligned-purple" />

</div>


---

## 📚 Overview

This directory contains the **canonical metadata definition suite** for archaeological symbols used across the Kansas Frontier Matrix (KFM).  
These symbols represent:

- Excavation areas  
- Artifact discovery sites  
- Protected burial zones  
- Cultural heritage locations  
- Settlement layer residues  
- Indigenous archaeological features  
- Material culture classification markers  

The metadata here enforces:

- Consistent symbolic representation  
- FAIR+CARE cultural heritage stewardship  
- Proper linkage to SVG/PNG symbols  
- STAC-compliant dataset publication  
- Story Node integration rules  
- ✓ Full adherence to KFM semantic and ethical standards  

No archaeological symbol may appear anywhere without being defined in this directory.

---

### 🗂️ Directory Layout

    archaeological/
    |-- README.md                                  # This document (index)
    |-- archaeological-symbols.json                # Canonical symbol registry
    |-- archaeological-symbols.stac.json           # STAC metadata for legend/symbol assets
    |-- archaeological-symbols-story-nodes.json    # Story Node usage/binding rules
    |
    └── examples/                                  # Developer-ready example metadata

---

### 🧱 Archaeological Symbol Registry — `archaeological-symbols.json`

Each archaeological symbol definition includes:

- id  
- category (excavation, discovery, cultural site, burial, feature)  
- label  
- description  
- svg path  
- optional png path  
- emoji fallback  
- archaeological_type  
- cultural_sensitivity (public / restricted / sacred)  
- CARE semantic obligations  

Example (indented):

    {
      "id": "archaeological_discovery",
      "category": "discovery",
      "label": "Archaeological Discovery",
      "description": "Indicates the discovery of material cultural remains.",
      "svg": "../svg/archaeological_discovery.svg",
      "emoji": "🏺",
      "archaeological_type": "artifact_find",
      "cultural_sensitivity": "public"
    }

---

### 🧩 STAC Metadata — `archaeological-symbols.stac.json`

Defines STAC metadata for archaeological symbol assets used in KFM’s external datasets.

Properties include:

- Asset roles: `legend`, `symbol`  
- Cultural sensitivity fields  
- Ontology linkages  
- Artifact/historic feature classification  

Example STAC snippet (indented):

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

Story Node binding metadata controls:

- Badge appearance rules  
- Emoji fallback usage  
- Placement (header, timeline, detailed card)  
- Domain-specific contexts  
- CARE visibility restrictions  
- Cultural heritage labeling conventions  

Example (indented):

    {
      "burial_protected": {
        "label": "Protected Burial Area",
        "badge": true,
        "emoji": "⚱️",
        "contexts": ["archaeology", "cultural_history"],
        "display_rules": {
          "timeline": true,
          "header": false
        },
        "cultural_sensitivity": "restricted"
      }
    }

---

### 🧪 Validation & CI

All archaeological metadata must pass:

- JSON Schema validation  
- CARE compliance checks  
- STAC validation  
- File/asset existence checks  
- Story Node linkage tests  
- Optional snapshot linkage  

Local test runner:

    make test-legends-archaeological

---

### 🕒 Version History

| Version  | Date       | Author        | Notes                                                                     |
|----------|------------|---------------|---------------------------------------------------------------------------|
| v10.2.3  | 2025-11-13 | KFM Docs AI   | Initial archaeological metadata overview — fully memory-rule compliant.   |
