---
title: "⛏️ Kansas Frontier Matrix — Cultural Landscape Resource Areas (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/resource-areas/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/archaeology-cultural-landscapes-resource-areas-v1.json"
governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Dataset Subcategory"
intent: "cultural-landscape-resource-areas"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# ⛏️ **Kansas Frontier Matrix — Cultural Landscape Resource Areas**  
`docs/analyses/archaeology/datasets/cultural-landscapes/resource-areas/README.md`

**Purpose:**  
Define, document, and govern all **resource-area datasets** within the Kansas Frontier Matrix (KFM).  
Resource areas represent **generalized ecological and geologic zones** that prehistoric and historic peoples used for:

- Material procurement (lithic raw materials, clays, pigments)  
- Subsistence activities (faunal zones, riparian foraging areas)  
- Seasonal mobility and scheduling  
- Trade and exchange networks  
- Cultural-technological development pathways  

These datasets power:

- Story Node resource-use narratives  
- Focus Mode v2 environmental context overlays  
- Neo4j resource-landscape linkage  
- MapLibre polygon layers + Cesium 3D environmental models  
- Cross-domain modeling with paleoenvironment, hydrology, and artifact inventories  

</div>

---

# 📘 Overview

Cultural resource areas represent **archaeologically, ecologically, and culturally significant procurement zones**, such as:

- **Flint/quartzite quarries**  
- **Clay beds & ceramic raw material zones**  
- **High-productivity faunal regions**  
- **Riparian woodland foraging areas**  
- **Paleo-channel resource corridors**  
- **Buffalo-hunting grassland mosaics**  
- **Plant-gathering ecotones**  
- **Toolstone-rich outcrops**  

These areas are always **generalized** to protect Indigenous knowledge and spatial sovereignty.  
No dataset may contain exact coordinates for sacred, restricted, or sensitive resource locations.

---

# 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/resource-areas/
├── README.md                     # This file
├── chert-outcrops/               # Lithic resource areas (generalized polygons/H3)
├── clay-deposits/                # Ceramic resource zones
├── faunal-zones/                 # Ecological hunting/foraging regions
├── riparian-foraging-areas/      # Riverine resource corridors
├── stac/                         # STAC metadata for resource-area datasets
├── metadata/                     # DCAT + CARE metadata for resource-area files
└── provenance/                   # PROV-O lineage & cultural review logs
~~~

---

# 🪨 Resource Area Types

| Category | Description | Notes |
|---|---|---|
| **Chert & Lithic Outcrops** | Toolstone procurement zones | Must be generalized (H3 or polygon simplification) |
| **Clay & Ceramic Raw Material Sources** | Earthen deposits for pottery | Cultural sensitivity review recommended |
| **Faunal Productivity Zones** | Ecological regions tied to subsistence strategies | Paleoenvironment cross-analysis required |
| **Riparian Resource Spaces** | Fishing, foraging, plant gathering | Use generalized hydrology integration |
| **Paleo-Environmental Resource Zones** | Ancient lakebeds, floodplains, loess terraces | Multi-era temporal metadata required |
| **Mixed Resource Areas** | Composite landscape-use regions | Must document which cultural phases apply |

Sensitive zones **cannot** be mapped precisely. All must obey CARE rules.

---

# 📦 Required Metadata (All Resource Area Datasets)

Each resource area dataset must include:

### ✔ STAC Item Requirements

| Field | Requirement |
|---|---|
| `id` | Versioned dataset identifier |
| `type` | `"Feature"` |
| `bbox` | Generalized bounding box |
| `geometry` | Polygon or MultiPolygon only |
| `properties.kfm:landscape_type` | `"resource_area"` |
| `properties.kfm:culture_phase` | Associated cultural phases |
| `properties.care:sensitivity` | Must be `"generalized"` or `"restricted-generalized"` |
| `assets.data.href` | Link to GeoJSON/COG resource polygons |
| `kfm:provenance` | Path to PROV-O lineage JSON |

### ✔ DCAT Metadata

Includes fields:

- `dct:title`  
- `dct:description`  
- `dcat:distribution`  
- `dct:temporal`  
- `dct:license`  
- `dcat:keyword`  

### ✔ CARE Cultural Safety Metadata

(required for all cultural landscapes)

| Field | Notes |
|---|---|
| `care:sensitivity` | Sensitive/critical areas → `"restricted-generalized"` |
| `care:review` | `"faircare"` or `"tribal"` |
| `care:notes` | Ethical + cultural explanations |
| `care:visibility_rules` | `"polygon-generalized"` / `"h3-only"` |

### ✔ Provenance Linkage

`kfm:provenance` must reference PROV-O logs documenting:

- Source datasets  
- Geologic/ecological basis  
- H3 or polygon generalization  
- Tribal/cultural reviews (if required)  
- Processing & simplification methods  

---

# 🌍 Spatial Requirements

All resource areas must:

- Use **EPSG:4326**  
- Apply **H3 generalization** or polygon simplification  
- Include hydrological + ecological contextualization  
- Avoid marking exact sourcing locations  
- Flatten/simplify boundaries to avoid sensitive exposure  

The more sensitive the resource area, the **more generalized** the geometry must be.

---

# 🕰️ Temporal Requirements

Resource areas must include:

- Cultural-phase epochs (OWL-Time)  
- Environmental context (climate regime, eco-period)  
- Notes on shifting resource availability across centuries  

Temporal metadata supports:

- Story Node environmental arcs  
- Climate–culture overlays  
- Predictive modeling of movement & subsistence  

---

# ⚖️ Cultural Safety & Ethics (FAIR+CARE)

Resource areas intersect deeply with:

- Indigenous ecological knowledge  
- Subsistence sovereignty  
- Sacred plant/animal domains  
- Tribal land-use history  

Therefore:

**Forbidden:**

- Exact clay pits, quarries, sacred plant zones  
- Detailed faunal kill sites  
- Revealing sensitive resource-use pathways  

**Mandatory:**

- CARE classification  
- Cultural review for all high-risk regions  
- Ethical descriptions (non-colonial, non-extractive)  
- Provenance logs describing generalization steps  

---

# 🧠 Integration Into KFM Ecosystem

### Knowledge Graph

Nodes:
- `ResourceArea`  
- `CulturalLandscape`  
- `CulturalPhase`  
- `EcologicalZone`  

Relationships:
- `OCCURRED_DURING`  
- `ASSOCIATED_WITH`  
- `LOCATED_IN`  
- `GENERALIZED_FROM`  
- `HAS_PROVENANCE`  

### Story Nodes

Resource areas shape narrative content on:

- Subsistence strategies  
- Toolstone acquisition  
- Mobility routes  
- Ecological adaptation  

### Focus Mode v2

Supports:

- AI explanations of resource–culture interactions  
- Ethical warnings (sensitivity chips)  
- Provenance transparency overlays  

---

# 📊 Dataset Index

| Resource Dataset | Category | Status | Last Review | Notes |
|---|---|---|---|---|
| `chert-outcrops/flint-hills-v1` | Lithic | 🟢 Active | 2025-11 | Generalized; culturally reviewed |
| `clay-deposits/prairie-beds-v1` | Ceramic | 🟢 Active | 2025-10 | STAC/DCAT compliant |
| `faunal-zones/tallgrass-v1` | Faunal | 🟡 Needs Review | 2025-09 | Requires ecological verification |
| `riparian-foraging-areas/arkansas-basin-v1` | Riparian | 🟢 Active | 2025-11 | Provenance validated |

---

# 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.4.0 | 2025-11-17 | Cultural Landscape WG · FAIR+CARE Council | Established resource-area governance, metadata rules, STAC/DCAT/CARE requirements |
| v10.0.0 | 2025-11-10 | Resource Landscape Team | Initial directory scaffold |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Cultural Landscapes](../README.md)

</div>