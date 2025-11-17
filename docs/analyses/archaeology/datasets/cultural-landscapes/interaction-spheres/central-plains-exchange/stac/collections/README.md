---
title: "🗂️🔄 Kansas Frontier Matrix — Central Plains Exchange Interaction Sphere STAC Collections (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/central-plains-exchange/stac/collections/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Cultural Landscape WG · FAIR+CARE Council · Metadata Standards Subcommittee"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/archaeology-central-plains-exchange-stac-collections-v1.json"
governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "STAC Collection Index"
intent: "central-plains-exchange-stac-collections"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🗂️🔄 **STAC Collections — Central Plains Exchange Interaction Sphere**  
`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/central-plains-exchange/stac/collections/README.md`

**Purpose:**  
Document the complete **STAC Collection** layer for the **Central Plains Exchange Interaction Sphere**, ensuring:

- FAIR+CARE governance  
- STAC 1.0 compliance  
- DCAT 3.0 interoperability  
- Spatial/temporal generalization correctness  
- Provenance linkage  
- KFM knowledge-graph integration  
- Story Node + Focus Mode interoperability  

This page defines Collection-level metadata that groups STAC Items relating to the Central Plains Exchange sphere.

</div>

---

# 📘 Overview

A **STAC Collection** is the machine-readable parent object that:
- Groups related STAC Items  
- Defines shared spatial & temporal extents  
- Declares classification metadata (`kfm:*`)  
- Applies cultural safety (`care:*`) at the Collection level  
- Ensures version-aware dataset governance  
- Provides dataset discoverability in KFM & external catalogs  

This directory contains **one** Collection:  
`central-plains-exchange.json`

---

# 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/central-plains-exchange/stac/collections/
├── README.md                                   # This file
└── central-plains-exchange.json                 # STAC Collection for this Interaction Sphere
~~~

---

# 📦 Required Fields for the Collection

The `central-plains-exchange.json` Collection file must include **all** required fields from:

- STAC 1.0  
- KFM Archaeology Extension  
- CARE Cultural Safety Extension  
- DCAT 3.0 crosswalk  
- KFM-MDP v10.4 documentation rules  

### ✔ Core STAC Fields

| Field | Description | Example |
|---|---|---|
| `stac_version` | STAC version used | `"1.0.0"` |
| `type` | Must be `"Collection"` | `"Collection"` |
| `id` | Collection ID | `"central-plains-exchange"` |
| `description` | Summary of sphere | `"Multi-era cultural interaction zone…"` |
| `license` | SPDX ID | `"CC-BY-4.0"` |
| `extent.spatial.bbox` | Generalized bounding box | `[-103,36.8,-94.5,43.2]` |
| `extent.temporal.interval` | OWL-Time interval | `[["0900-01-01T00:00:00Z","1400-01-01T00:00:00Z"]]` |

### ✔ KFM Archaeology Extension (`kfm:*`)

| Field | Description | Example |
|---|---|---|
| `kfm:landscape_type` | Classification | `"interaction_sphere"` |
| `kfm:domain` | KFM domain ID | `"archaeology:interaction-spheres"` |
| `kfm:material_class` | Standardized term | `"cultural-landscape"` |
| `kfm:review_cycle` | Governance cycle | `"Biannual"` |
| `kfm:geometry_generalization` | Method | `"H3-level-6"` |
| `kfm:schema_version` | Metadata schema version | `"1.0.0"` |

### ✔ CARE Cultural Safety Metadata (`care:*`)

| Field | Value | Notes |
|---|---|---|
| `care:sensitivity` | `"generalized"` | Sphere is not protohistoric |
| `care:review` | `"faircare"` | Verified by FAIR+CARE Council |
| `care:notes` | Explanation | `"Generalized polygons used to protect cultural landscapes"` |
| `care:visibility_rules` | `"polygon-generalized"` | Valid for public visualization |

### ✔ Required Links

A STAC Collection must declare its STAC Items.

| rel | href | Purpose |
|---|---|---|
| `"item"` | `"../central-plains-exchange-v1.json"` | Points to sphere-level STAC Item |
| `"root"` | `"../../interaction-spheres.json"` | Links to root Interaction Sphere Collection |

Additional links permitted:
- `"self"`  
- `"parent"`  
- `"license"`  

---

# 🧪 Validation Requirements

The Collection must pass:

### Schema Validation
- `stac-collection-schema.json`  
- `kfm-archaeology-extension.json`  
- `care-sensitivity-extension.json`  
- `dcat-crosswalk.json`

### CI Enforcement
Validation executed via:

- `.github/workflows/artifact-stac-validate.yml`  
- `.github/workflows/metadata-validate.yml`  
- `.github/workflows/faircare-audit.yml`

The Collection **cannot** be committed without passing all validators.

---

# 🧠 Integration Into KFM Ecosystem

### Knowledge Graph Nodes
- `InteractionSphereCollection`
- `InteractionSphere`
- `CulturalPhase`
- `GeneralizedRegion`

### Relationships
- `HAS_ITEM`  
- `HAS_METADATA`  
- `HAS_PROVENANCE`  
- `GENERALIZED_FROM`  
- `CARE_SENSITIVITY`  

### Story Nodes
Used for:
- Multi-era narratives  
- Cultural exchange modeling  
- Long-distance movement stories  

### Focus Mode v2
Uses Collection metadata for:
- Rendering sphere overview  
- Spatial/temporal filtering of interpretation layers  
- Ethical warnings + provenance chips  

---

# 📊 Collection Summary

| Field | Value |
|---|---|
| ID | `central-plains-exchange` |
| Landscape Type | interaction sphere |
| Sensitivity | generalized |
| Review | FAIR+CARE |
| Temporal Extent | AD 900–1400 |
| Spatial Extent | Generalized bounding box |
| Provenance | Fully linked |
| Status | 🟢 Active |

---

# 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.4.0 | 2025-11-17 | Cultural Landscape WG · FAIR+CARE Council | Finalized STAC Collection metadata rules for Central Plains Exchange |
| v10.0.0 | 2025-11-10 | Landscape Metadata Team | Initial Collection metadata scaffold |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE · MCP-DL v6.3  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to STAC for Central Plains Exchange](../README.md)

</div>