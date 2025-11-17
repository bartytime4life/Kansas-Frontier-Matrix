---
title: "🏺🗂️ Kansas Frontier Matrix — Great Bend Aspect Interaction Sphere STAC Catalog (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/great-bend-aspect/stac/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council · Tribal Advisory Consultation Recommended"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/archaeology-great-bend-aspect-stac-v1.json"
governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "STAC Documentation"
intent: "great-bend-aspect-stac"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant (Elevated Sensitivity)"
---

<div align="center">

# 🏺🗂️ **STAC Metadata — Great Bend Aspect Interaction Sphere**  
`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/great-bend-aspect/stac/README.md`

**Purpose:**  
Provide the complete **STAC (SpatioTemporal Asset Catalog)** documentation for the **Great Bend Aspect (GBA) Interaction Sphere**, enabling:

- Machine-readable dataset discovery  
- FAIR+CARE ethical governance  
- Spatial generalization compliance  
- Transparent provenance linkage  
- Knowledge Graph integration  
- Story Node + Focus Mode alignment  
- Widespread schema interoperability (DCAT, PROV-O, CIDOC-CRM, GeoSPARQL)  

The GBA sphere contains culturally sensitive protohistoric components (AD 1600–1700), therefore **elevated CARE requirements** apply.

</div>

---

# 📘 Overview

The **Great Bend Aspect Interaction Sphere** models a Late Prehistoric–Protohistoric cultural network characterized by:

- Shared ceramics (generalized varieties)  
- Horticulture + bison hunting  
- Earthlodge/grass house settlement clusters  
- Interactions with Central Plains, Southern Plains, and early European contacts  
- Environmental constraints across Arkansas River valley + prairie ecotones  

STAC metadata ensures structured, validation-ready, de-identified spatial representation of this culturally important landscape.

---

# 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/great-bend-aspect/stac/
├── README.md                                     # This file
├── great-bend-aspect-v2.json                     # STAC Item
└── collections/
    └── great-bend-aspect.json                    # Collection definition
~~~

---

# 📦 STAC Item Requirements (great-bend-aspect-v2.json)

### ✔ Core STAC Fields

| Field | Example | Notes |
|---|---|---|
| `id` | `"great-bend-aspect-v2"` | Versioned ID |
| `type` | `"Feature"` | Must be Feature |
| `stac_version` | `"1.0.0"` | Required |
| `bbox` | `[-101.8, 37.0, -95.3, 40.5]` | Generalized |
| `geometry` | MultiPolygon | Simplified + H3 generalized |

### ✔ KFM Archaeology Extension (`kfm:*`)

| Field | Value |
|---|---|
| `kfm:landscape_type` | `"interaction_sphere"` |
| `kfm:culture_phase` | `["GBA-Early","GBA-Middle","GBA-Late"]` |
| `kfm:source` | `"Public-domain archaeological synthesis"` |
| `kfm:provenance` | `"../provenance/great-bend-aspect-v2.json"` |
| `kfm:geometry_generalization` | `"H3-level-6"` |
| `kfm:review_cycle` | `"Biannual"` |

### ✔ CARE Metadata (`care:*`)

| Field | Value |
|---|---|
| `care:sensitivity` | `"generalized"` |
| `care:review` | `"faircare"` |
| `care:notes` | `"Sensitive protohistoric features generalized; no restricted cultural information included."` |
| `care:visibility_rules` | `"polygon-generalized"` |

### ✔ Temporal Metadata

| Property | Example |
|---|---|
| `start_datetime` | `"1350-01-01T00:00:00Z"` |
| `end_datetime` | `"1700-01-01T00:00:00Z"` |

### ✔ Assets

| Asset | Purpose |
|---|---|
| `data` | GeoJSON/COG | Generalized polygon |
| `thumbnail` | Optional preview |
| `metadata` | Link to DCAT metadata |

---

# 📂 STAC Collection Requirements (collections/great-bend-aspect.json)

A STAC Collection groups Items and applies domain-level metadata.

### Required Fields

| Field | Value |
|---|---|
| `stac_version` | `"1.0.0"` |
| `type` | `"Collection"` |
| `id` | `"great-bend-aspect"` |
| `description` | Summary of GBA Interaction Sphere |
| `license` | `"CC-BY-4.0"` |
| `extent.spatial.bbox` | Generalized BBOX |
| `extent.temporal.interval` | GBA time range |
| `kfm:landscape_type` | `"interaction_sphere"` |
| `kfm:domain` | `"archaeology:interaction-spheres"` |
| `kfm:material_class` | `"cultural-landscape"` |
| `kfm:review_cycle` | `"Biannual"` |
| `care:sensitivity` | `"generalized"` |
| `care:review` | `"faircare"` |
| `care:notes` | `"Generalized due to protohistoric sensitivity"` |
| `care:visibility_rules` | `"polygon-generalized"` |

### Required Links

| rel | href |
|---|---|
| `"item"` | `"../great-bend-aspect-v2.json"` |
| `"root"` | `"../../interaction-spheres.json"` |

---

# 🧪 Validation Requirements

STAC Items and Collections must pass:

- **stac-item-schema.json**  
- **stac-collection-schema.json**  
- **kfm-archaeology-extension.json**  
- **care-sensitivity-extension.json**  
- **dcat-crosswalk.json**  
- Provenance linkage validation  
- Spatial generalization validator (H3 + simplification)

Validation pipelines:

- `.github/workflows/artifact-stac-validate.yml`  
- `.github/workflows/metadata-validate.yml`  
- `.github/workflows/faircare-audit.yml`

Failure → CI rejection.

---

# 🧠 Integration Into KFM Ecosystem

### Knowledge Graph Integration

Nodes:
- `InteractionSphere`
- `CulturalRegion`
- `CulturalPhase`
- `GeneralizedArea`

Edges:
- `GENERALIZED_FROM`  
- `HAS_METADATA`  
- `HAS_PROVENANCE`  
- `OCCURRED_DURING`  
- `CARE_SENSITIVITY`  

### Story Nodes

STAC Item/Collection metadata supports:

- Time-scope narrative rendering  
- Region-to-region cultural linkage  
- Material-culture diffusion storytelling  

### Focus Mode v2

Supports:

- Ethical transparency overlays  
- Sensitivity banners  
- Provenance-chip display  
- Deductive cultural-phase explanations  

---

# 📊 Catalog Summary

| Item | Sensitivity | Status | Notes |
|---|---|---|---|
| great-bend-aspect-v2.json | generalized | 🟢 Active | CARE-reviewed; culturally respectful generalization |

---

# 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v2 | 2025-11-17 | Cultural Landscape WG · FAIR+CARE Council | Updated STAC metadata; enhanced CARE alignment |
| v1 | 2025-11-10 | Landscape Metadata Team | Initial STAC definition |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE · MCP-DL v6.3 · Tribal Advisory Recommended  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Great Bend Aspect](../README.md)

</div>