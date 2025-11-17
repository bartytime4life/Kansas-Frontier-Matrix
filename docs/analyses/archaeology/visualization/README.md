---
title: "🗺️ Kansas Frontier Matrix — Archaeology Visualization Framework (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/visualization/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Biannual / Archaeology Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/archaeology-visualization-v1.json"
governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Visualization Framework"
intent: "archaeology-visualization"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🗺️ **Kansas Frontier Matrix — Archaeology Visualization Framework**  
`docs/analyses/archaeology/visualization/README.md`

**Purpose:**  
Define the **visualization standards, map-layer structure, 3D rendering workflows, privacy protections, and narrative integration rules** for archaeological data within the Kansas Frontier Matrix (KFM).  
Ensures every archaeological visualization is:  
- Scientifically valid  
- Culturally respectful  
- FAIR+CARE compliant  
- Technically compatible with **MapLibre**, **Cesium**, **Neo4j**, **Focus Mode v2**, and **Story Nodes**  
- Fully governed under **MCP-DL v6.3** and **KFM v10.4 visualization protocols**

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../README.md)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../../standards/faircare.md)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)  
[![Status: Active](https://img.shields.io/badge/Status-Active-success)](../../../../releases/v10.4.0/manifest.zip)

</div>

---

## 📘 Overview

Archaeological visualizations in KFM include:

- **Site distribution mapping (H3 grids, KDE surfaces)**  
- **Cultural landscape reconstructions (routes, polygons, occupation extents)**  
- **Artifact spatial distributions**  
- **Stratigraphic visualizations (vertical profiles, layer timelines)**  
- **3D terrain + earthwork renderings (Cesium tilesets)**  
- **AI-driven interpretive overlays (Focus Mode v2)**

Each visualization must include:

- Spatial metadata (CRS, bbox, geometry type)  
- Temporal metadata (OWL-Time)  
- STAC/DCAT dataset references  
- CARE sensitivity level  
- CITATION + provenance chain  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/visualization/
├── README.md                   # This file
├── map-layers/                 # GeoJSON, COG, Vector Tiles for archaeological layers
├── 3d-tiles/                   # Cesium / 3D Tiles for mounds, sites, terrain models
├── figures/                    # PNG/SVG charts exported from notebooks
├── styles/                     # MapLibre style JSON fragments for archaeological layers
├── narratives/                 # Story Node + Focus Mode narrative visual links
└── examples/                   # Sample visualization pipelines and outputs
~~~

---

## 🧭 Visualization Types & Standards

| Type | Description | Required Format(s) | Notes |
|---|---|---|---|
| **Site Distribution Maps** | KDE, density, or H3-grid visualizations | GeoJSON, COG | Remove sensitive coordinates; use H3 level 5–7 |
| **Cultural Landscapes** | Settlement extents, movement routes, territorial shapes | GeoJSON, Vector Tiles | Boundaries must be generalized unless tribal-approved |
| **Artifact Distribution Layers** | Spatialized counts, proportions, or types | GeoJSON, Parquet | PD-only artifact data; exclude restricted items |
| **Stratigraphy Views** | Vertical sections, phase models | PNG/SVG + JSON metadata | No excavation unit identifiers if restricted |
| **3D Archaeological Reconstructions** | Mounds, platforms, paleo-landforms | Cesium 3D Tiles | Derived from LiDAR; DEM must be generalized |
| **AI Interpretive Overlays** | Focus Mode insights and highlight maps | GeoJSON + narrative text | CARE tone review required |

---

## 🧩 Required Metadata for All Visualizations

| Requirement | Standard |
|---|---|
| **CRS** | EPSG:4326 or documented alternative |
| **Spatial Extent** | BBOX + GeoJSON geometry |
| **Temporal Extent** | OWL-Time `start`, `end`, `precision` |
| **STAC Item** | `stac_version: 1.0.0`, asset roles, projection info |
| **DCAT Dataset** | `dct:title`, `dct:license`, distribution metadata |
| **Checksum** | SHA-256 |
| **Cultural Sensitivity** | CARE flags: `generalized`, `restricted`, `prohibited` |
| **Provenance** | PROV-O lineage entries |

All archaeological visual layers **must** be listed in the `stac/` directory.

---

## 🌄 2D Map Layer Standards (MapLibre)

### **General Requirements**
- Use **GeoJSON**, **COG**, or **Vector Tiles** for map layers.  
- All coordinate geometries must be **generalized** for sensitive sites.  
- Style tokens must follow `styles/visualization-archaeology.json`.

### **Layer Types**
| Layer | Style | Purpose |
|---|---|---|
| `site-density-h3` | Heatmap → color ramp | Generalized density visualization |
| `cultural-regions` | Soft polygon fill | Territorial + cultural landscape models |
| `artifact-locations` | Symbol layer | Non-sensitive artifact clusters |
| `routes-ancient` | Linework | Movement & trail reconstructions |
| `paleo-surface` | Raster hillshade | Environmental context |

---

## 🏔️ 3D Visualization Standards (Cesium)

### **Tileset Rules**
- Must include `tileset.json` + referenced geometry tiles.  
- All tiles must include:

| Property | Requirement |
|---|---|
| `boundingVolume` | Geo-aligned box or region |
| `geometricError` | Must decrease by level |
| `extensionsUsed` | `3DTILES_metadata`, `3DTILES_content_gltf` |
| `kfm:sensitivity` | CARE flag (string) |

### **Allowed Data Sources**
- Open-access LiDAR  
- Generalized DEMs  
- Derived 3D meshes (PD or licensed)

### **Prohibited**
- Raw LiDAR of sensitive archaeological features  
- Non-generalized burial features  

---

## 🧠 AI-Assisted Visualization (Focus Mode v2 Integration)

Artifacts include:

- **Spatially highlighted regions** tied to Story Nodes  
- **AI narrative overlays** explaining cultural significance  
- **Confidence bands** visualized as shading or opacity  
- **Bias-mitigated descriptions**  
- **Provenance chips** linking to STAC layers  

AI outputs must:

- Use deterministic seed configuration  
- Include explainability artifacts (stored in `narratives/`)  
- Pass cultural review (ethics-review-template.md)

---

## 🧪 Reproducibility Requirements

Every visualization pipeline must include:

| Component | Description |
|---|---|
| **Notebook or script** | Located in `examples/` or analysis directory |
| **Input datasets** | Refer to `datasets/` STAC/DCAT manifests |
| **Parameter list** | Explicit + justified |
| **Versioning** | Notebook + data hashes |
| **Output** | Saved in `map-layers/`, `3d-tiles/`, or `figures/` |

No visualization may be merged unless:

- All scripts execute without error  
- Outputs validate against metadata schemas  
- CARE classification is applied  

---

## 📊 Visualization Index (Examples)

| Visualization | Type | Location | Status | Reviewed |
|---|---|---|---|---|
| `site-density-h3-flint-hills` | H3 Grid | `map-layers/` | 🟢 Active | 2025-10 |
| `great-bend-landscape-v2` | Cultural Landscape | `map-layers/` | 🟢 Active | 2025-11 |
| `paleo-mound-3d-v1` | 3D Tiles | `3d-tiles/` | 🟡 Needs Review | 2025-09 |
| `artifact-ceramic-proportions` | Artifact Distribution | `figures/` | 🟢 Active | 2025-11 |
| `ai-phase-overlay-v1` | AI Overlay | `narratives/` | 🟢 Active | 2025-11 |

---

## ⚖️ FAIR+CARE Visualization Rules

All archaeological visualizations must:

- Avoid publishing exact sacred site coordinates  
- Use **H3 generalization** for sensitive points  
- Provide contextual, respectful narrative descriptions  
- Cite cultural data sources and provenance  
- Avoid colonial, extractive, or dismissive framing  
- Provide disclaimers for uncertain interpretations  
- Include accessibility alt-text for every figure and map  

Forbidden:

- Burial mounds mapped at exact locations  
- Sensitive ceremonial sites  
- Restricted tribal imagery  
- Any non-consented cultural material  

---

## 🧠 Integration Into KFM Ecosystem

Archaeology visualizations feed into:

- **MapLibre layers**  
- **Cesium 3D environments**  
- **Story Node visual contexts**  
- **Focus Mode v2 spatial explanations**  
- **Knowledge graph spatial relationships**  
- **Historical + cultural timelines**

All visualizations must pass the validation rules defined in:  
`../validation/README.md`

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.4.0 | 2025-11-17 | Archaeology Working Group · FAIR+CARE Council | Established archaeology visualization standards; added STAC/DCAT + CARE rules; ensured box-safe formatting |
| v10.0.0 | 2025-11-10 | Archaeology Visualization Team | Initial conceptual structure |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Archaeology Analysis](../README.md)

</div>
