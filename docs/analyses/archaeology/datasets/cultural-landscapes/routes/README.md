---
title: "🛤️ Kansas Frontier Matrix — Cultural Landscape Routes (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/routes/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/archaeology-cultural-landscape-routes-v1.json"
governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Dataset Subcategory"
intent: "cultural-landscape-routes"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🛤️ **Kansas Frontier Matrix — Cultural Landscape Routes**  
`docs/analyses/archaeology/datasets/cultural-landscapes/routes/README.md`

**Purpose:**  
Define and govern all **ancient mobility route datasets** within the Kansas Frontier Matrix (KFM).  
Cultural landscape routes represent **generalized paths of movement, migration, trade, subsistence travel, seasonal scheduling, and inter-group connectivity** across prehistoric, protohistoric, and early historic Kansas.

These route datasets support:

- Story Node movement narratives  
- Focus Mode v2 cultural-pathway overlays  
- Neo4j relationship graphing for cultural diffusion  
- MapLibre and Cesium route visualizations  
- Chronological interaction modeling  
- Ecological mobility analysis  

All route datasets must follow **FAIR+CARE**, **STAC/DCAT**, **PROV-O**, **GeoSPARQL**, and **KFM-MDP v10.4**.

</div>

---

# 📘 Overview

Cultural routes are reconstructed from:

- Archaeological evidence (artifact distributions, feature alignments)  
- Ethnohistoric documentation  
- Landscape analysis (least-cost paths, hydrology, ridgelines)  
- Paleoenvironmental context  
- Oral histories (generalized only, with tribal approval)  

Routes do **not** represent exact paths; they are **generalized corridors** derived from multi-source evidence.

Common route types:

- **Seasonal migration paths**  
- **Inter-valley travel routes**  
- **Trade and exchange networks**  
- **Hunting/foraging mobility corridors**  
- **Protohistoric Wichita + Central Plains connectors**  
- **Trail zones inferred from geophysical patterns**  

---

# 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/routes/
├── README.md                          # This file
├── southern-plains-corridor/          # Generalized route polygons/linestrings
├── flint-hills-trailzones/            # Prairie trailzone datasets
├── central-plains-connectors/         # Inter-regional paths (generalized)
├── stac/                              # STAC metadata: Items + Collections
├── metadata/                          # DCAT + CARE metadata for each route dataset
└── provenance/                        # PROV-O lineage logs + cultural reviews
~~~

---

# 🛣️ Route Dataset Requirements

Each route dataset must define:

| Component | Description |
|---|---|
| **Name** | Generalized cultural or ecological route |
| **Route Type** | `"trade"`, `"migration"`, `"seasonal"`, `"foraging"`, `"ritualized"` |
| **Temporal Span** | OWL-Time phase or multi-era range |
| **Spatial Form** | Generalized linestring *or* corridor polygon |
| **Cultural Associations** | Associated cultural phases or groups |
| **Environmental Context** | Hydrology, ridgelines, prairies, resource clusters |
| **Sensitivity** | CARE classification |
| **Provenance** | Full PROV-O lineage log |

Routes may appear as:

- **Corridor polygons** (recommended)
- **Linestrings** (if safely generalized)
- **H3 mosaics** for highly sensitive cultural pathways

---

# 📦 Required Metadata (All Route Datasets)

### ✔ STAC Item Fields

| Field | Requirement |
|---|---|
| `id` | Versioned ID |
| `bbox` | Generalized bounding box |
| `geometry` | LineString, MultiLineString, or corridor Polygon |
| `properties.kfm:landscape_type` | `"route"` |
| `properties.kfm:culture_phase` | Cultural-phase linkage |
| `properties.care:sensitivity` | `"generalized"` or `"restricted-generalized"` |
| `assets.data.href` | GeoJSON/COG link |
| `kfm:provenance` | Required |

### ✔ DCAT Metadata Fields

- `dct:title`  
- `dct:description`  
- `dct:temporal`  
- `dcat:distribution`  
- `dct:license`  
- `dcat:keyword`  

### ✔ CARE Cultural Safety Fields

| Field | Notes |
|---|---|
| `care:sensitivity` | Required for all route sets |
| `care:review` | `"tribal"` REQUIRED for protohistoric routes |
| `care:notes` | Must justify generalization & cultural safety measures |
| `care:visibility_rules` | `"h3-only"` for high sensitivity |

### ✔ Provenance Link

`kfm:provenance` must include:

- Original source descriptions  
- Evidence basis (ethnohistoric, archaeological, geomorphological)  
- All generalization steps  
- CARE + tribal review documentation  

---

# 🧭 Spatial Requirements

- All cultural routes must be **generalized**  
- Sensitive mobility pathways may require **H3-only release**  
- Exact ceremonial trails or sacred-path routes **must not** be mapped  
- Geometries must be simplified to avoid inference of precise navigation  
- CRS must be **EPSG:4326**  
- Include optional corridor-width metadata for map rendering  

---

# 🕰️ Temporal Requirements

Routes must define:

- Cultural-phase alignment  
- Earliest & latest usage windows  
- Environmental-event relevance (drought cycles, floodplains, prairie burns)  
- Narrative uncertainty notes  

Temporal metadata enriches:

- Story Node sequencing  
- AI pathway generation for Focus Mode  
- Archaeology-paleoenvironment correlation  

---

# ⚖️ Cultural Safety & Ethics (FAIR+CARE)

Routes intersect directly with:

- Indigenous sovereignty  
- Sensitive cultural knowledge  
- Migration histories  
- Tribal ecological practices  
- Sacred travel paths  

Thus:

**Forbidden:**

- Exact pathway representations  
- Restricted or sacred routes  
- Unapproved ethnohistoric data  
- Colonial descriptions of movement  

**Required:**

- Cultural review for all protohistoric or tribal-related corridors  
- Summary of cultural context in metadata  
- Partial obfuscation via H3 or polygon corridors  
- Clear CARE classification  

---

# 🧠 Integration Into KFM Ecosystem

### Knowledge Graph

Nodes:
- `CulturalRoute`
- `CulturalPhase`
- `Region`
- `InteractionSphere`
- `ResourceArea`

Edges:
- `CONNECTS`
- `TRAVERSED_BY`
- `ASSOCIATED_WITH`
- `OCCURRED_DURING`
- `GENERALIZED_FROM`
- `HAS_PROVENANCE`
- `CARE_SENSITIVITY`

### Story Nodes

Route datasets enable:

- Cultural movement narratives  
- Seasonal scheduling explanations  
- Trade/exchange story arcs  
- Inter-group interaction histories  

### Focus Mode v2

Provides:

- Movement overlays  
- Ethical warnings  
- Provenance chips  
- Explainability pathways for archaeology + environment networks  

---

# 📊 Dataset Index

| Route Dataset | Category | Status | Last Review | Notes |
|---|---|---|---|---|
| `southern-plains-corridor/v1` | Migration/Trade | 🟢 Active | 2025-11 | Generalized corridor, vetted by FAIR+CARE |
| `flint-hills-trailzones/v1` | Prairie movement routes | 🟢 Active | 2025-11 | STAC/DCAT aligned |
| `central-plains-connectors/v1` | Inter-valley connectors | 🟡 Needs Review | 2025-09 | Tribal consultation pending |

---

# 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.4.0 | 2025-11-17 | Cultural Landscape WG · FAIR+CARE Council | Established cultural route governance, metadata standards, CARE review rules |
| v10.0.0 | 2025-11-10 | Cultural Landscape Team | Initial route dataset scaffolding |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Cultural Landscapes](../README.md)

</div>