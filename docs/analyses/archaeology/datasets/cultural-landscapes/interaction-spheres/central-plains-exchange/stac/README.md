---
title: "🗂️🔄 Kansas Frontier Matrix — Central Plains Exchange Interaction Sphere STAC Documentation (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/central-plains-exchange/stac/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/archaeology-central-plains-exchange-stac-v1.json"
governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "STAC Documentation"
intent: "central-plains-exchange-stac"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🗂️🔄 **STAC Metadata — Central Plains Exchange Interaction Sphere**  
`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/central-plains-exchange/stac/README.md`

**Purpose:**  
Provide the authoritative **STAC (SpatioTemporal Asset Catalog)** documentation for the **Central Plains Exchange Interaction Sphere** dataset in the Kansas Frontier Matrix (KFM).  
This STAC layer ensures machine-readable, version-controlled, FAIR+CARE-compliant metadata for all downstream processes:

- Knowledge Graph ingestion  
- Story Node generation  
- Focus Mode v2 interpretive overlays  
- Spatial visualization (MapLibre + Cesium)  
- ETL reproducibility  
- DCAT interoperability  
- Ethical, cultural, and generalization governance  

</div>

---

# 📘 Overview

The **Central Plains Exchange Interaction Sphere** represents a large, multi-era cultural region spanning the Republican, Smoky Hill, Solomon, Platte, and Kansas Rivers and their associated prairie–riverine ecotones.

STAC metadata captures:

- Spatial generalization (H3-level 6 + polygon smoothing)  
- Cultural-phase associations  
- Context-specific sensitivity rules (CARE)  
- Dataset provenance & lineage  
- Temporal coverage (AD 900–1400)  
- Distribution assets (GeoJSON/COG layers)  

This dataset is considered **medium sensitivity** → generalization required, tribal review *not* mandatory.

---

# 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/central-plains-exchange/stac/
├── README.md                               # This file
├── central-plains-exchange-v1.json         # STAC Item
└── collections/                            # STAC Collections
    └── central-plains-exchange.json        # Collection metadata
~~~

---

# 📦 STAC Item Requirements (central-plains-exchange-v1.json)

Below is the required structure for this Interaction Sphere’s STAC Item:

### ✔ Core STAC Fields

| Field | Example | Notes |
|---|---|---|
| `id` | `"central-plains-exchange-v1"` | Versioned ID |
| `type` | `"Feature"` | Required |
| `stac_version` | `"1.0.0"` | Fixed value |
| `bbox` | `[-103.0, 36.8, -94.5, 43.2]` | Generalized bounding box |
| `geometry` | MultiPolygon | Generalized spatial extent |

### ✔ KFM Archaeology Extension (`kfm:*`)

| Field | Example |
|---|---|
| `kfm:landscape_type` | `"interaction_sphere"` |
| `kfm:culture_phase` | `["CPT-Early","CPT-Middle","CPT-Late"]` |
| `kfm:source` | `"Archaeological synthesis (PD)"` |
| `kfm:provenance` | `"../provenance/central-plains-exchange-v1.json"` |
| `kfm:review_cycle` | `"Biannual"` |
| `kfm:geometry_generalization` | `"H3-level-6"` |

### ✔ CARE Metadata (`care:*`)

| Field | Value |
|---|---|
| `care:sensitivity` | `"generalized"` |
| `care:review` | `"faircare"` |
| `care:notes` | `"Generalization applied to avoid sensitive cultural inference"` |
| `care:visibility_rules` | `"polygon-generalized"` |

### ✔ Temporal Metadata

| Field | Example |
|---|---|
| `properties.start_datetime` | `"0900-01-01T00:00:00Z"` |
| `properties.end_datetime` | `"1400-01-01T00:00:00Z"` |

OWL-Time compliance recommended.

### ✔ Asset Listings

| Asset | Description |
|---|---|
| `data` | Generalized GeoJSON/COG polygon dataset |
| `thumbnail` | Optional static preview image |
| `metadata` | Links to extended narrative or DCAT records |

---

# 📂 STAC Collection (collections/central-plains-exchange.json)

Each Interaction Sphere must have a dedicated STAC Collection.

### Required Fields

| Field | Value |
|---|---|
| `id` | `"central-plains-exchange"` |
| `type` | `"Collection"` |
| `stac_version` | `"1.0.0"` |
| `description` | Cultural summary |
| `extent.spatial` | Generalized BBOX |
| `extent.temporal` | Cultural-phase date span |
| `license` | `"CC-BY-4.0"` |
| `kfm:material_class` | `"cultural-landscape"` |
| `kfm:domain` | `"archaeology:interaction-spheres"` |
| `kfm:review_cycle` | `"Biannual"` |
| `care:sensitivity` | `"generalized"` |

### Required Links

| rel | href |
|---|---|
| `"item"` | `"../central-plains-exchange-v1.json"` |
| `"root"` | `"../../stac/interaction-spheres.json"` |

---

# 🧪 Validation Rules

The STAC Item and Collection must pass:

- `stac-item-schema.json`  
- `stac-collection-schema.json`  
- `kfm-archaeology-extension.json`  
- `care-sensitivity-extension.json`  
- `dcat-crosswalk.json`  
- Provenance linkage validation  
- Spatial generalization validator  

CI workflows enforcing compliance:

- `.github/workflows/artifact-stac-validate.yml`  
- `.github/workflows/metadata-validate.yml`  
- `.github/workflows/faircare-audit.yml`  

Noncompliance halts dataset ingestion & publication.

---

# 🧠 Integration Into the KFM Ecosystem

### Knowledge Graph
Nodes:
- `InteractionSphere`
- `CulturalPhase`
- `EnvironmentalContext`
- `GeneralizedRegion`

Edges:
- `ASSOCIATED_WITH`
- `OCCURRED_DURING`
- `GENERALIZED_FROM`
- `HAS_PROVENANCE`
- `HAS_METADATA`
- `CARE_SENSITIVITY`

### Story Nodes
Enable:

- Cultural diffusion narratives  
- Multi-valley interaction summaries  
- Phase-based storyline sequencing  

### Focus Mode v2
Uses STAC metadata for:

- Provenance chips  
- Ethical-sensitivity warnings  
- Region-level interpretive overlays  

---

# 📊 STAC Item Overview

| Item | Sensitivity | Status | Review |
|---|---|---|---|
| `central-plains-exchange-v1.json` | generalized | 🟢 Active | FAIR+CARE |

---

# 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v1 | 2025-11-17 | Cultural Landscape WG · FAIR+CARE Council | First STAC-compliant release of Central Plains Exchange Interaction Sphere metadata |
| v0.1 | 2025-11-10 | Landscape Metadata Team | Prototype STAC draft |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Central Plains Exchange Sphere](../README.md)

</div>