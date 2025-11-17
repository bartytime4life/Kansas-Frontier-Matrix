---
title: "🏺🗂️ Kansas Frontier Matrix — Great Bend Aspect Interaction Sphere STAC Collections (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/great-bend-aspect/stac/collections/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council · Tribal Advisory Consultation Recommended"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/archaeology-great-bend-aspect-stac-collections-v1.json"
governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "STAC Collection Index"
intent: "great-bend-aspect-stac-collections"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant (Elevated Sensitivity)"
---

<div align="center">

# 🏺🗂️ **STAC Collections — Great Bend Aspect Interaction Sphere**  
`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/great-bend-aspect/stac/collections/README.md`

**Purpose:**  
Define and document the **STAC Collection layer** for the **Great Bend Aspect (GBA) Interaction Sphere** within the Kansas Frontier Matrix.  
Collections ensure dataset discoverability, temporal and spatial harmonization, cultural safety enforcement, and machine-readable governance.

The Great Bend Aspect contains **Late Prehistoric + Protohistoric** components → **elevated cultural sensitivity**, requiring enhanced CARE compliance and recommended tribal advisory review.

</div>

---

# 📘 Overview

This directory defines the **STAC Collection** for the GBA Interaction Sphere.  
A STAC Collection:

- Groups all STAC Items for the dataset  
- Defines shared temporal & spatial metadata  
- Applies cultural safety metadata at the collection level  
- Ensures DCAT crosswalk consistency  
- Aligns with KFM archaeology & CARE extensions  
- Integrates with Knowledge Graph, Story Nodes, and Focus Mode v2  

This folder contains **one** Collection:

- `great-bend-aspect.json`

---

# 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/great-bend-aspect/stac/collections/
├── README.md                        # This file
└── great-bend-aspect.json           # STAC Collection for this Interaction Sphere
~~~

---

# 📦 Required STAC Collection Fields

The `great-bend-aspect.json` Collection must include:

---

## ✔ Core STAC Fields

| Field | Description | Example |
|---|---|---|
| `stac_version` | STAC version | `"1.0.0"` |
| `type` | Must be `"Collection"` | `"Collection"` |
| `id` | Collection identifier | `"great-bend-aspect"` |
| `description` | Cultural summary | `"Generalized GBA interaction sphere"` |
| `license` | Dataset license | `"CC-BY-4.0"` |

---

## ✔ Extent (Spatial + Temporal)

### Spatial
- Must reflect the **generalized** extent of the GBA Interaction Sphere  
- BBOX example:  