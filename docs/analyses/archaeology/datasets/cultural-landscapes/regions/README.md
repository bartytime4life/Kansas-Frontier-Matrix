---
title: "🗺️ Kansas Frontier Matrix — Cultural Landscape Regions (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/regions/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/archaeology-cultural-landscape-regions-v1.json"
governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Dataset Subcategory"
intent: "cultural-landscape-regions"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🗺️ **Kansas Frontier Matrix — Cultural Landscape Regions**  
`docs/analyses/archaeology/datasets/cultural-landscapes/regions/README.md`

**Purpose:**  
Define and govern all **cultural landscape region datasets** included in the Kansas Frontier Matrix (KFM).  
These regions represent **generalized archaeological, cultural, historical, and environmental territories** used for:

- Chronological-cultural mapping  
- Story Node regional narratives  
- Focus Mode v2 interpretive overlays  
- MapLibre & Cesium polygon visualizations  
- Cultural-phase modeling and AI reasoning  
- Environmental → cultural interaction synthesis  
- Archaeological settlement & landscape analysis  

All datasets must comply with **FAIR+CARE**, **STAC/DCAT**, **PROV-O**, **GeoSPARQL**, **CIDOC-CRM**, and **KFM-MDP v10.4**.

</div>

---

# 📘 Overview

**Cultural landscape regions** are high-level landscape zones representing spatial aspects of:

- Prehistoric and protohistoric cultural phases  
- Settlement patterns  
- Resource availability and ecological niches  
- Cultural interaction territories  
- Migration pathways  
- Long-term human–environment relationships

Regions are **never mapped at full precision**—they are generalized polygons derived from:

- Literature synthesis  
- Environmental models  
- Aggregated archaeological datasets  
- Pollen/charcoal/paleoecological proxies  
- Geophysics and LiDAR interpreted surfaces  

Common region types include:

- **Settlement Regions**  
- **Subsistence Zones**  
- **Territorial / Cultural Extents (generalized)**  
- **Cultural Phases by Drainage Basin**  
- **Eco-cultural Landscapes**  

---

# 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/regions/
├── README.md                          # This file
├── flint-hills-region/                # Generalized polygon + STAC + metadata + provenance
├── smoky-hill-region/                 # Cultural-ecological region polygons
├── arkansas-river-basin/              # Multi-phase region dataset
├── stac/                              # STAC Items & Collections for region datasets
├── metadata/                          # DCAT + CARE + region-level context info
└── provenance/                        # PROV-O lineage logs and review documentation
~~~

---

# 🌄 Region Definition Requirements

Each region dataset must define:

| Element | Description |
|---|---|
| **Region Name** | Culturally/archaeologically recognized landscape zone |
| **Temporal Span** | One or more phases (OWL-Time) |
| **Spatial Representation** | Generalized polygon or H3 mosaic |
| **Environmental Context** | Biome/soil/topography connections |
| **Cultural Connections** | Material culture, settlement, subsistence indicators |
| **Sources** | Archaeology, geomorphology, paleoenvironment references |
| **Sensitivity Classification** | CARE-compliant |

---

# 🧭 Examples of Cultural Landscape Regions

### **Flint Hills Cultural–Ecological Region**
- Tallgrass prairie + chert-rich ecotone  
- Strong correlation with Late Prehistoric settlement clusters  
- Lithic raw material availability shaping regional patterns  

### **Smoky Hill Cultural Drainage Region**
- Environmental corridor linking several cultural phases  
- Aggregates fluvial, ecological, and archaeological evidence  

### **Arkansas River Basin Cultural Region**
- Multi-phase cultural landscape used for settlement/timeline synthesis  
- Important for protohistoric intercultural movements  

---

# 📦 Required Metadata (Region Datasets)

Region datasets must include:

### ✔ STAC Item Fields
- `id` (versioned, semantic)  
- `bbox` (generalized)  
- `geometry` (Polygon/MultiPolygon)  
- `properties.kfm:culture_phase`  
- `properties.care:sensitivity`  
- `assets.data.href`  
- `kfm:provenance`  

### ✔ DCAT Metadata
- `dct:title`  
- `dct:description`  
- `dcat:distribution`  
- `dct:temporal`  
- `dct:license`  
- `dcat:keyword`  

### ✔ CARE Metadata
Regions must include:

| CARE Field | Allowed |
|---|---|---|
| `care:sensitivity` | `generalized`, `restricted-generalized` |
| `care:review` | `faircare`, `tribal` |
| `care:notes` | Explanation of generalization & cultural review |
| `care:visibility_rules` | `polygon-generalized`, `h3-only`, `no-exact-boundaries` |

### ✔ Provenance Link
Every region must specify:

- `kfm:provenance`: path to PROV-O record documenting generalization, review, and source lineage

---

# 🧭 Spatial Requirements

- All regions must use **generalized polygons**  
- Sensitive boundaries must avoid precision  
- Territorial regions must not represent exact or disputed borders  
- For high-sensitivity zones → use **H3-only**  
- CRS must be **EPSG:4326**  
- Include topological simplification for polygons  

---

# 🕰️ Temporal Requirements

Regions must include:

- OWL-Time compatible temporal coverage  
- Cultural-phase references (Late Prehistoric, Middle Ceramic, etc.)  
- If multi-era, specify earliest & latest documented presence  
- Optional: uncertainty metadata  

---

# 🧪 Validation Requirements

All region datasets must pass:

- Region metadata schema  
- CARE cultural safety schema  
- DCAT compliance  
- STAC Item + Collection schema validation  
- Provenance linkage validation  
- Spatial generalization audit  
- CI workflows:

  - `metadata-validate.yml`  
  - `faircare-audit.yml`  
  - `artifact-stac-validate.yml`  

Failure to meet any criteria results in **CI rejection** and governance halt.

---

# 🧠 Integration Into KFM Ecosystem

### **Knowledge Graph**
Nodes:
- `CulturalRegion`
- `EnvironmentalRegion`
- `CulturalPhase`
- `ResourceZone`

Relationships:
- `PART_OF`  
- `ASSOCIATED_WITH`  
- `OCCURRED_DURING`  
- `GENERALIZED_FROM`  
- `HAS_PROVENANCE`  

### **Story Nodes**
Regions provide:

- Anchors for cultural narratives  
- Landscape-scale interpretive arcs  
- Multi-phase cultural consistency  

### **Focus Mode v2**
Region metadata supports:

- Spatial contextualization  
- Regional cultural explanations  
- Ethical visibility constraints  
- Provenance-chip injection  

---

# 📊 Dataset Index

| Region Dataset | Category | Status | Last Review | Notes |
|---|---|---|---|---|
| `flint-hills-region/v1` | Eco-cultural region | 🟢 Active | 2025-11 | Generalized + approved |
| `smoky-hill-region/v1` | Cultural drainage | 🟢 Active | 2025-10 | STAC/DCAT aligned |
| `arkansas-river-basin/v1` | Multi-era region | 🟡 Needs Review | 2025-09 | Tribal review required |

---

# 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.4.0 | 2025-11-17 | Cultural Landscape WG · FAIR+CARE Council | Established region-level governance, metadata rules, STAC/DCAT/CARE requirements |
| v10.0.0 | 2025-11-10 | Cultural Landscape Team | Initial directory scaffold |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Cultural Landscapes](../README.md)

</div>