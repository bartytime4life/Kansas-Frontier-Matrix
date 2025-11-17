---
title: "🌿 Kansas Frontier Matrix — Paleoenvironment Datasets (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/paleoenvironment/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-paleoenvironment-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Dataset Category"
intent: "archaeology-paleoenvironment-datasets"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🌿 **Kansas Frontier Matrix — Paleoenvironment Datasets**  
`docs/analyses/archaeology/datasets/paleoenvironment/README.md`

**Purpose:**  
Define, index, and govern all **paleoenvironmental datasets** used in the Kansas Frontier Matrix (KFM) for reconstructing climate, ecology, hydrology, and environmental contexts relevant to prehistoric and historic cultural landscapes.  
These datasets support:

- Eco-cultural correlation  
- Occupation phase modeling  
- Climate-driven archaeological interpretations  
- Story Nodes & Focus Mode v2  
- MapLibre & Cesium environmental reconstructions  
- AI-assisted trend detection (pollen, charcoal, macrofossils)

Only datasets that are **open-access**, **public-domain**, or ethically cleared through **FAIR+CARE** review may be included.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../../README.md)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../../../standards/faircare.md)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../LICENSE)  
[![Status: Active](https://img.shields.io/badge/Status-Active-success)](../../../../../releases/v10.4.0/manifest.zip)

</div>

---

## 📘 Overview

Paleoenvironment datasets in KFM include:

- **Pollen cores**  
- **Charcoal deposits & fire histories**  
- **Macrofossil & fauna records**  
- **Lake sediment cores**  
- **Dendrochronology (tree-ring) datasets**  
- **Hydrology-linked eco proxies**  
- **Climate variance indicators (SPEI, PDSI, anomalies)**  
- **AI-augmented paleoenvironment reconstructions**

These datasets provide **environmental context** for archaeological phenomena such as:

- Settlement shifts  
- Subsistence transitions  
- Fire regimes and prairie dynamics  
- Cultural adaptation to drought/flood cycles  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/paleoenvironment/
├── README.md                          # This file
├── pollen/                            # Pollen core datasets & interpretations
├── charcoal/                          # Charcoal & fire-history proxies
├── fauna/                             # Open-access faunal paleo datasets
├── sediments/                         # Sediment-core profiles + geochemistry
├── dendrochronology/                  # Tree-ring climate reconstructions
├── climate-proxies/                   # Derived drought/flood indices
├── stac/                              # STAC Items/Collections for paleo datasets
├── metadata/                          # DCAT + CARE metadata
└── provenance/                        # Processing lineage (PROV-O)
~~~

---

## 🧭 Paleoenvironment Dataset Categories

| Category | Description | Allowed | Notes |
|---|---|---|---|
| **Pollen Cores** | Vegetation reconstruction over time | ✅ | Must include depth–age model |
| **Charcoal** | Fire history & prairie burning indicators | ✅ | Requires temporal calibration |
| **Faunal Paleo Data** | Pleistocene/Holocene fauna indicators | ⚠️ | No sensitive species unless PD |
| **Sediment Cores** | Lake/river basin environmental records | ✅ | Geochemical profiles allowed |
| **Dendrochronology** | Tree-ring temperature/precip signals | ✅ | PD datasets only |
| **Climate Proxy Layers** | Drought, moisture, temp proxies | ✅ | Downscaled derivatives must cite algorithms |
| **Ancient Hydrology** | Paleo flood/drought cycles | ⚠️ | Must avoid sensitive tribal water data |

Forbidden:

- Restricted paleofaunal data from protected sites  
- Human remains or burial-linked eco samples  
- Unverified proprietary core datasets  
- Tribal-restricted water or ecology datasets  

---

## 📦 Required Metadata (All Paleoenvironment Datasets)

### ✔ STAC 1.0 Item Requirements

| Field | Description |
|---|---|
| `id` | Global unique identifier |
| `bbox` | Generalized bounding box or H3 mosaic |
| `geometry` | Point/Polygon (generalized if sensitive) |
| `properties.datetime` | Core start/end or proxy interval |
| `kfm:proxy_type` | `"pollen"`, `"charcoal"`, `"tree_rings"`, etc. |
| `care:sensitivity` | `"general"`, `"generalized"`, `"restricted"` |
| `assets` | Data file links (CSV, GeoJSON, COG) |

### ✔ DCAT 3.0 Metadata

| Field | Example |
|---|---|
| `dct:title` | "Pollen Core – Flint Hills Basin" |
| `dct:license` | `"CC-BY 4.0"` |
| `dct:temporal` | OWL-Time time range |
| `dcat:distribution` | GeoJSON/CSV/COG |

### ✔ PROV-O Provenance

Includes:

- Original archive source  
- Sampling metadata  
- Lab methods  
- Calibration model (age-depth, Bayesian, etc.)  
- Processing parameters & scripts  
- Analyst + review cycle  

---

## 🧪 Data Preparation Requirements

All paleoenvironment datasets must:

- Include **depth–age models** for cores  
- Specify **sampling resolution** and **calibration curve**  
- Include **error bounds** for dating (σ, confidence intervals)  
- Use standardized schema fields  
- Provide climate proxy metadata (e.g., `biomass_fire_proxy`, `aridity_index`)  
- Pass cultural and environmental ethics review  
- Include PROV-O logs in `provenance/`  

Generalization rules (for sensitive eco-cultural regions):

- Replace exact coordinates with H3 regions  
- Omit exact lake/pond identifiers if culturally sensitive  
- Remove detailed fauna data if species is sacred or restricted  

---

## 🛰️ Integration Into KFM

### **Knowledge Graph (Neo4j)**

Nodes:

- `PaleoRecord`
- `PollenCore`
- `CharcoalProxy`
- `SedimentLayer`
- `TreeRingSeries`
- `ClimateProxy`
- `HydroProxy`

Relationships:

- `INDICATES`
- `CORRELATED_WITH`
- `OCCURRED_DURING`
- `LOCATED_AT`
- `GENERALIZED_FROM`

### **Focus Mode v2**

Paleo datasets power:

- Climate–culture correlations  
- Eco-cultural story nodes  
- Narrative explanations of environmental shifts  
- Confidence bands and proxy uncertainty overlays  

All Focus Mode narratives undergo tone + cultural validation.

### **Visualization Outputs**

Typical derivative layers:

- Pollen distribution reconstructions  
- Charcoal accumulation maps  
- Paleo flood/drought layers  
- Time-slice environmental visualizations  
- Cesium 3D sediment-core renderings  

All visual layers must follow `visualization` and `validation` standards.

---

## 📊 Dataset Index

| Dataset | Category | Location | Status | Last Review | Notes |
|---|---|---|---|---|---|
| `pollen/flint-hills-core-v1` | Pollen | `pollen/` | 🟢 Active | 2025-11 | Depth–age model validated |
| `charcoal/prairie-fire-history-v1` | Charcoal | `charcoal/` | 🟢 Active | 2025-11 | Proxy normalization complete |
| `fauna/pleistocene-fauna-v1` | Faunal | `fauna/` | 🟡 Needs Review | 2025-09 | Verify sacred species exclusions |
| `sediments/smoky-hill-core-v2` | Sediments | `sediments/` | 🟢 Active | 2025-11 | Geochem metadata validated |

---

## 🧠 Example STAC Item (Pollen Core)

~~~json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "pollen-flint-hills-v1",
  "bbox": [-101.2, 37.5, -95.4, 40.1],
  "properties": {
    "kfm:proxy_type": "pollen",
    "care:sensitivity": "generalized",
    "start_datetime": "8500-01-01T00:00:00Z",
    "end_datetime": "0-01-01T00:00:00Z",
    "kfm:provenance": "provenance/pollen-flint-hills-v1.json"
  },
  "assets": {
    "core_data": {
      "href": "https://example.com/pollen/flint_hills_core_v1.csv",
      "type": "text/csv",
      "roles": ["data"]
    }
  }
}
~~~

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.4.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council | Created paleoenvironment dataset index; added ethical + scientific metadata rules; ensured box-safe formatting |
| v10.0.0 | 2025-11-10 | Paleoenvironment Dataset Team | Initial conceptual structure |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Archaeology Datasets](../README.md)

</div>