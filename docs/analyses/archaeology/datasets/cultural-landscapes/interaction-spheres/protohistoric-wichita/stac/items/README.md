---
title: "🗺️ Kansas Frontier Matrix — STAC Items: Protohistoric Wichita Interaction Sphere (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/interaction-spheres/protohistoric-wichita/stac/items/README.md"
version: "v10.4.4"
last_updated: "2025-11-17"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../releases/v10.4.4/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v10.4.4/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v10.4.4/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/stac-items-v1.json"
governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.4"
status: "Active · Enforced"
doc_kind: "STAC-Items"
intent: "archaeology · protohistoric-wichita"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🗺️ **STAC Items — Protohistoric Wichita Interaction Sphere**  
`stac/items/README.md`

**Purpose:**  
Define, document, and validate **all STAC Items** representing geospatial/temporal archaeological datasets belonging to the **Protohistoric Wichita Interaction Sphere**, ensuring full alignment with **STAC 1.0.0**, **DCAT 3.0**, **CIDOC-CRM**, **OWL-Time**, **GeoSPARQL**, **Story Node v3**, and **Focus Mode v2** requirements.

</div>

--- ✦ ---

## 1. Overview 📚

This module defines **individual STAC Items** that represent discrete archaeological datasets within the Protohistoric Wichita Interaction Sphere:

- Wichita settlements (generalized via H3 privacy grid)  
- Trade corridors & interaction routes  
- Ceramic petrographic networks  
- Radiocarbon date bands  
- Paleoenvironmental overlays  
- Ethnohistoric cartography layers  

Each item is **FAIR+CARE governed**, spatiotemporally grounded, provenance-linked, and validated under **STAC → DCAT → CIDOC → Graph** interoperability rules.

--- ✦ ---

## 2. Directory Layout (DL-C compliant) 🌳

```

protohistoric-wichita/
├── stac/
│   ├── collection.json
│   ├── items/
│   │   ├── settlements-generalized-h3.json
│   │   ├── trade-corridors.json
│   │   ├── ceramic-network.json
│   │   ├── radiocarbon-bands.json
│   │   ├── paleoenvironmental-overlays.json
│   │   └── ethnohistoric-cartography.json
│   └── README.md

````

--- ✦ ---

## 3. Required Metadata for All STAC Items 🧩

Every STAC Item **must** include:

### 3.1 Core STAC Fields
- `stac_version: "1.0.0"`
- `type: "Feature"`
- `id` (UUID or controlled namespace ID)
- `geometry` (GeoJSON)
- `bbox`
- `properties.datetime` or `start_datetime`/`end_datetime`
- `links`
- `assets`

### 3.2 Required Extensions
- `proj`
- `checksum`
- `scientific`
- `version`
- `history`
- `context` (KFM custom extension mapping to Story Node v3)

### 3.3 Scientific Metadata
- Citation (`scientific:citation`)
- DOI or surrogate PID
- `history:lineage`
- Research notes

### 3.4 CARE Metadata
- Sensitivity flags  
- H3 generalization settings  
- Indigenous governance notes  
- Stewardship attribution  
- Minimization flags  

--- ✦ ---

## 4. Item Summaries 📦

### 4.1 🧍‍♂️ Settlements (Generalized H3)
**ID:** `settlements-generalized-h3`  
Generalized Protohistoric Wichita settlement areas, privacy-protected using H3 indexing.  
**Temporal:** 1350–1750 CE  
**Spatial:** MultiPolygon  

### 4.2 🔄 Trade Corridors
**ID:** `trade-corridors`  
Reconstructed interaction/trade corridors derived from ethnohistoric, geomorphic, and riverine access data.  
**Temporal:** 1400–1750 CE  
**Spatial:** MultiLineString  

### 4.3 🏺 Ceramic Petrographic Network
**ID:** `ceramic-network`  
Petrographic clusters, compositional signatures, and distribution vectors.  
**Temporal:** 1300–1700 CE  

### 4.4 ⏳ Radiocarbon Bands
**ID:** `radiocarbon-bands`  
Bayesian-modeled radiocarbon probability structures for regionally associated sites.  

### 4.5 🌿 Paleoenvironmental Overlays
**ID:** `paleoenvironmental-overlays`  
Hydrology, drought indices, fire regimes, reconstructed vegetation/corridors.  

### 4.6 🗺 Ethnohistoric Cartography
**ID:** `ethnohistoric-cartography`  
Merged cartographic overlays from early French, Spanish, and 19th-century ethnographic atlases.  

--- ✦ ---

## 5. STAC Item Template (Copy/Paste) 📄

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "<item-id>",
  "collection": "protohistoric-wichita",
  "geometry": {},
  "bbox": [],
  "properties": {
    "datetime": null,
    "start_datetime": "",
    "end_datetime": "",
    "proj:epsg": 4326,
    "scientific:citation": "",
    "scientific:doi": "",
    "history:lineage": "",
    "kfm:context_storynode": "",
    "kfm:care_sensitivity": ""
  },
  "assets": {
    "data": {
      "href": "<link>",
      "type": "application/geo+json",
      "roles": ["data"],
      "checksum:multihash": ""
    }
  },
  "links": [
    { "rel": "collection", "href": "../collection.json" },
    { "rel": "alternate", "href": "" },
    { "rel": "provenance", "href": "" }
  ]
}
````

--- ✦ ---

## 6. Knowledge Graph Integration 🕸️

| STAC → Graph | Neo4j Class     | CIDOC CRM |
| ------------ | --------------- | --------- |
| Item         | `Dataset`       | `E73`     |
| Geometry     | `Spatial`       | `E47`     |
| Temporal     | `Temporal`      | `E52`     |
| Asset        | `DigitalObject` | `E84`     |
| Lineage      | `Activity`      | `E7`      |

Outputs generated automatically:

* Story Node v3 candidates
* Focus Mode v2 contextual summaries
* PROV-O lineage triples
* H3-minimized public derivatives

--- ✦ ---

## 7. Validation & CI/CD 🧪

All items must pass:

* `stac-validate`
* JSON Schema validation
* CARE governance audit
* PROV lineage validation
* Ontology alignment
* Graph consistency scan

--- ✦ ---

## 8. Narrative & Focus Mode Binding 🧭

Each STAC Item requires a `kfm:context_storynode` reference linking to:

* Story Node v3 master narrative
* Or auto-generated Focus Mode v2 summary

This enables:

* Storyline maps
* Contextual timeline overlays
* Entity-centric Focus Mode navigation
* Archaeological dossier auto-generation

--- ✦ ---

## 9. Provenance (PROV-O) 🧾

Each item must include:

* Data source origin
* ETL pipeline UUID
* Software agent version
* Transformation events
* Asset checksums

--- ✦ ---

## 10. Standards & Compliance 📎

* STAC 1.0.0
* DCAT 3.0
* CIDOC-CRM v7
* GeoSPARQL 1.1
* OWL-Time
* PROV-O
* Story Node v3
* KFM Ontology v10
* FAIR+CARE

--- ✦ ---

**End of STAC Items README — Protohistoric Wichita Interaction Sphere**
