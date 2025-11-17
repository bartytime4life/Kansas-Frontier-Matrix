---
title: "🗂️ Kansas Frontier Matrix — Cultural Landscape STAC Catalog (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/stac/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/archaeology-cultural-landscapes-stac-v1.json"
governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "STAC Catalog"
intent: "cultural-landscapes-stac"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🗂️ **Kansas Frontier Matrix — Cultural Landscape STAC Catalog**  
`docs/analyses/archaeology/datasets/cultural-landscapes/stac/README.md`

**Purpose:**  
Define the **STAC (SpatioTemporal Asset Catalog)** structure for all cultural landscape datasets in the Kansas Frontier Matrix (KFM).  
This catalog provides **machine-discoverable, FAIR+CARE-compliant metadata** for:

- Regions  
- Routes  
- Interaction Spheres  
- Resource Areas  

Each dataset is represented as a **STAC Item** and grouped within **STAC Collections**, ensuring alignment with:

- STAC 1.0  
- KFM archaeology extension (`kfm:*`)  
- CARE cultural safety extension (`care:*`)  
- DCAT 3.0 mappings  
- PROV-O provenance structure  
- CIDOC-CRM entity linking  
- GeoSPARQL spatial compatibility  

</div>

---

# 📘 Overview

Cultural landscape STAC metadata enables:

- Searchable, machine-readable dataset catalogs  
- Automated ingestion into Neo4j  
- Robust map loading (MapLibre/Cesium)  
- Story Node & Focus Mode v2 narrative generation  
- Validation & governance tracking  
- Ethical and sovereign metadata controls via CARE extension  
- Temporal and spatial synchronization across KFM layers  

All STAC Items and Collections in this directory must pass:

- STAC schema validation  
- KFM archaeology extension schema  
- CARE extension schema  
- DCAT crosswalk validation  
- Metadata alignment checks  
- Provenance linkage validation  

Failure to validate halts dataset ingestion.

---

# 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/stac/
├── README.md                                 # This file
├── collections/                              # STAC Collections for dataset groups
│   ├── regions.json
│   ├── routes.json
│   ├── interaction-spheres.json
│   └── resource-areas.json
├── items/                                    # Individual STAC Items describing datasets
│   ├── flint-hills-region-v1.json
│   ├── smoky-hill-region-v1.json
│   ├── southern-plains-corridor-v1.json
│   └── great-bend-aspect-v2.json
├── schemas/                                  # Validation schemas for Collections & Items
└── templates/                                # Contributor templates (Items + Collections)
~~~

---

# 🧭 Cultural Landscape STAC Collections

Each Collection groups datasets by domain.

| Collection | Purpose | Example File |
|---|---|---|
| **regions** | Generalized cultural regions | `collections/regions.json` |
| **routes** | Travel, trade, migration corridors | `collections/routes.json` |
| **interaction-spheres** | Multi-phase cultural interaction zones | `collections/interaction-spheres.json` |
| **resource-areas** | Procurement, foraging, ecological zones | `collections/resource-areas.json` |

Each STAC Collection must include:

- Title & description  
- Spatial/temporal extent  
- License  
- CARE rollup fields  
- Links to STAC Items  
- Provider & domain metadata  
- Cultural review notes (if required)  

---

# 📦 Required STAC Item Fields (Cultural Landscapes)

Each STAC Item must contain:

### ✔ Core STAC fields
- `id`
- `type: "Feature"`
- `stac_version: "1.0.0"`
- `bbox`
- `geometry`
- `properties`
- `assets`

### ✔ KFM Archaeology fields (`kfm:*`)
| Field | Purpose |
|---|---|
| `kfm:landscape_type` | `"region"`, `"route"`, `"interaction_sphere"`, `"resource_area"` |
| `kfm:culture_phase` | Cultural phase or multi-phase range |
| `kfm:source` | Dataset origin |
| `kfm:provenance` | Link to PROV-O record |
| `kfm:review_cycle` | Governance schedule |

### ✔ CARE fields (`care:*`)
| Field | Requirement |
|---|---|
| `care:sensitivity` | `"generalized"` or `"restricted-generalized"` |
| `care:review` | `"faircare"` or `"tribal"` |
| `care:notes` | Explanation of cultural safety decisions |
| `care:visibility_rules` | `"h3-only"`, `"polygon-generalized"`, `"no-exact-boundaries"` |

### ✔ DCAT fields (within metadata files)
STAC Items must crosswalk cleanly to DCAT metadata.

---

# 🌍 Spatial Requirements

- All geometries must be **generalized** (never exact)  
- Sensitive territories must avoid high-resolution boundaries  
- Allowed geometry types: `Polygon`, `MultiPolygon`, `LineString`, `MultiLineString`  
- CRS must always be **EPSG:4326**  
- Generalization strategies must be documented in provenance  

---

# 🕰️ Temporal Requirements

- Use OWL-Time compatible `start_datetime` and `end_datetime`  
- Temporal spans must reflect cultural-phase scholarship  
- Multi-era Interaction Spheres must list earliest + latest evidence  
- Temporal alignment required with Story Node and Focus Mode timelines  

---

# 🧪 Validation Requirements

All STAC Items & Collections must pass:

1. `stac-item-schema.json`  
2. `stac-collection-schema.json`  
3. `kfm-archaeology-extension.json`  
4. `care-sensitivity-extension.json`  
5. `dcat-crosswalk.json`  
6. Provenance linkage validator  
7. Spatial generalization validator  
8. CI workflows:
   - `artifact-stac-validate.yml`
   - `metadata-validate.yml`
   - `faircare-audit.yml`

Failure = **CI rejection**.

---

# 🧠 Integration Into KFM Ecosystem

### Knowledge Graph Nodes
- `CulturalRegion`  
- `CulturalRoute`  
- `InteractionSphere`  
- `ResourceArea`  

### Relationships
- `OCCURRED_DURING`  
- `CONNECTED_TO`  
- `ASSOCIATED_WITH`  
- `GENERALIZED_FROM`  
- `HAS_PROVENANCE`  
- `HAS_METADATA`  

### Story Nodes
- Provide geographic anchors  
- Shape cultural and ecological narratives  
- Drive movement + diffusion story arcs  

### Focus Mode v2
- Ethical visibility rendering  
- AI interpretive overlays  
- Provenance-aware narrative output  

---

# 📊 Catalog Index (Examples)

| STAC Item | Type | Status | Notes |
|---|---|---|---|
| `flint-hills-region-v1.json` | Region | 🟢 Active | Reviewed; generalized |
| `southern-plains-corridor-v1.json` | Route | 🟢 Active | CARE-reviewed |
| `great-bend-aspect-v2.json` | Interaction Sphere | 🟢 Active | Tribal-reviewed |
| `arkansas-basin-resources-v1.json` | Resource Area | 🟡 Needs Review | Pending cultural approval |

---

# 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.4.0 | 2025-11-17 | Cultural Landscape WG · FAIR+CARE Council | Created STAC catalog for all cultural landscapes; added CARE/DCAT alignment & validation rules |
| v10.0.0 | 2025-11-10 | Landscape Metadata Team | Initial directory scaffold |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Cultural Landscapes](../README.md)

</div>