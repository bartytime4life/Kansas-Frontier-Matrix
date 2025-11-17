---
title: "🔄 Kansas Frontier Matrix — Central Plains Exchange Interaction Sphere (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/central-plains-exchange/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/archaeology-central-plains-exchange-v1.json"
governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Dataset"
intent: "cultural-landscape-interaction-sphere-central-plains-exchange"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🔄 **Central Plains Exchange Interaction Sphere**  
`docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/central-plains-exchange/README.md`

**Purpose:**  
Document, govern, and ethically contextualize the **Central Plains Exchange Interaction Sphere**, a generalized cultural region representing broad-scale interaction, exchange, technological circulation, and shared traditions across the central Great Plains.

This dataset synthesizes archaeological, paleoenvironmental, geophysical, and ethnohistoric evidence to map a **multi-phase cultural interaction zone**, providing:

- Cultural-layer integration  
- Network-based archaeological context  
- Story Node anchors  
- Focus Mode v2 interpretive overlays  
- MapLibre/Cesium polygon & heatmap layers  
- Generalized territory modeling for CARE compliance  

</div>

---

# 📘 Overview

The **Central Plains Exchange Interaction Sphere** encompasses a large, multi-century cultural zone defined by:

- Shared material culture distributions  
- Exchange of raw materials (chert, ceramic tempers, fauna)  
- Overlapping house forms & settlement architecture  
- Ceramic style continuities across drainages  
- Paleoenvironmental correlates (prairie ecotones, riparian corridors)  
- Inter-valley social connectivity (Republican, Smoky Hill, Platte, Solomon, Kansas Rivers)

It represents a **generalized** regional interaction environment during:

- The **Central Plains Tradition** (ca. AD 900–1400)  
- Transitional Late Prehistoric phases  
- Early protohistoric networks prior to European intrusion  

No dataset attempts to define precise cultural boundaries—only generalized, evidence-based interaction areas.

---

# 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/central-plains-exchange/
├── README.md                                  # This file
├── central-plains-exchange.geojson            # Generalized MultiPolygon representation
├── stac/                                       # STAC Item for this interaction sphere
│   └── central-plains-exchange-v1.json
├── metadata/                                   # DCAT + CARE + cultural notes
│   └── central-plains-exchange-v1.json
└── provenance/                                 # PROV-O lineage + review logs
    └── central-plains-exchange-v1.json
~~~

---

# 🌀 Cultural Definition

| Dimension | Description |
|---|---|
| **Cultural Cohesion** | Shared house forms, ceramic typologies, mound features (generalized) |
| **Exchange Networks** | Raw material flow (Flint Hills → Republican basin → Platte basin) |
| **Settlement Dynamics** | Semi-sedentary villages with horticulture & bison exploitation |
| **Environmental Context** | Tallgrass–shortgrass prairie transitions, alluvial valleys |
| **Subsistence** | Mixed horticulture, bison hunting, broad-spectrum resource use |
| **Multi-Phase Overlap** | Early Caddoan, Plains Woodland legacies, Late Prehistoric transitions |

All interpretations derive from published archaeological research and publicly available data.

---

# 🌍 Spatial Representation

The interaction sphere is represented as:

- A **generalized MultiPolygon**
- H3 mosaic (levels 5–7)
- CRS: **EPSG:4326**

Generalization is mandatory for:

- Sensitive village landscapes  
- High-density artifact distributions  
- Potentially restricted cultural knowledge  

---

# 🕰️ Temporal Context

| Phase | Approx. Dates | Notes |
|---|---|---|
| Early Central Plains Tradition | AD 900–1050 | Initial formation of regional coherence |
| Middle CPT | AD 1050–1250 | Peak cultural exchange and settlement expansion |
| Late CPT / Transitional | AD 1250–1400 | Increasing mobility + diffusion with Great Bend Aspect |

OWL-Time metadata is included in STAC + DCAT.

---

# 📦 STAC Item Summary (Excerpt)

~~~json
{
  "id": "central-plains-exchange-v1",
  "type": "Feature",
  "stac_version": "1.0.0",
  "bbox": [-103.0, 36.8, -94.5, 43.2],
  "properties": {
    "kfm:culture_phase": ["CPT-Early", "CPT-Middle", "CPT-Late"],
    "care:sensitivity": "generalized",
    "kfm:provenance": "../provenance/central-plains-exchange-v1.json"
  }
}
~~~

(Full STAC Item stored under `stac/`.)

---

# ⚖️ Cultural & Ethical Considerations (FAIR+CARE)

The **Central Plains Exchange Sphere** is culturally significant for multiple descendant Indigenous communities.

### Mandatory Rules  
- No exact settlement coordinates  
- No sacred or ceremonial boundary definitions  
- No restricted ethnographic information  
- Narrative framing avoids colonial or essentialist terminology  
- Cultural consultation required for protohistoric overlaps  
- Spatial generalization is enforced (H3/Polygon simplification)

### CARE Metadata Fields
- `care:sensitivity: "generalized"`  
- `care:review: "faircare"` (additional tribal review required if flagged)  
- `care:notes` documenting generalization, ethical choices, and dataset limitations  

---

# 🧪 Provenance (PROV-O Requirements)

Provenance logs must capture:

- Raw dataset origin (literature, open GIS, PD resources)  
- GIS transformations (simplification, H3 generalization)  
- Interpretive synthesis steps  
- Cultural and ethical review (FAIR+CARE, tribal where applicable)  
- Lineage from raw → generalized → processed  

Stored in:  
`provenance/central-plains-exchange-v1.json`

---

# 🧠 Integration Into KFM Ecosystem

### Knowledge Graph Nodes
- `InteractionSphere`  
- `CulturalPhase`  
- `EnvironmentalZone`  
- `CulturalRegion`  

### Relationships
- `ASSOCIATED_WITH`  
- `GENERALIZED_FROM`  
- `CONNECTED_TO`  
- `OCCURRED_DURING`  
- `HAS_PROVENANCE`

### Story Nodes
- Region-based cultural histories  
- Broad archaeological pattern interpretation  

### Focus Mode v2
- Cultural-network overlays  
- Movement & diffusion interpretability  
- Provenance-chip transparency  

---

# 📊 Dataset Status

| Version | Status | Review | Notes |
|---|---|---|---|
| v1 | 🟢 Active | 2025-11 | Fully generalized; STAC/DCAT/CARE validated |

---

# 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v1 | 2025-11-17 | Cultural Landscape WG · FAIR+CARE Council | Initial release of Central Plains Exchange interaction sphere dataset |
| v0.1 | 2025-11-10 | Landscape Modeling Team | Prototype polygon + metadata draft |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Interaction Spheres](../README.md)

</div>