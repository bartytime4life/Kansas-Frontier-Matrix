---
title: "🏺 Kansas Frontier Matrix — Archaeology Dataset Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/README.md"
version: "v11.0.0"
last_updated: "2025-11-24"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · FAIR+CARE Council · Tribal Sovereignty Review Board"
commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_guid: "urn:kfm:doc:archaeology-datasets-index-v11.0.0"
doc_kind: "Domain Dataset Index"
intent: "archaeology-datasets"
semantic_document_id: "kfm-doc-analyses-archaeology-datasets"
category: "Archaeology · Cultural Landscapes · Heritage Data"

sbom_ref: "../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/archaeology-datasets-v11.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

fair_category: "F1-A1-I1-R1"
care_label: "High-Sensitivity · Sovereignty-Restricted"
sensitivity: "Cultural / Archaeology / Heritage"
indigenous_data_flag: true
risk_category: "Moderate"
public_exposure_risk: "Governed"
redaction_required: true

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Public (Governed)"
jurisdiction: "Kansas / United States"
immutability_status: "mutable-plan"
---

<div align="center">

# 🏺 **Kansas Frontier Matrix — Archaeology Dataset Index (v11)**  
`docs/analyses/archaeology/datasets/README.md`

**FAIR+CARE Certified · Sovereignty-Aligned  
Diamond⁹ Ω · Crown∞Ω Ultimate Certified**

**Purpose:**  
Define the *complete, governed, sovereignty-aligned dataset index* for all archaeological data in KFM v11.  
Includes: remote sensing, geophysical surveys, cultural landscapes, artifact inventories, historical maps, NER-extracted archival entities, sovereignty-governed heritage records, and their **STAC/DCAT metadata**, **provenance chains**, and **H3-generalized spatial footprints**.

</div>

---

# 📘 v11 Overview

The KFM Archaeology Datasets Layer integrates multi-source archaeological evidence:

- 🛰 **LiDAR + SAR + thermal IR**  
- 🧭 **Historic plats, treaties, surveys, and diaries**  
- 🧬 **OCR → NER → GeoLink entity datasets**  
- 🌿 **Paleoenvironmental proxies**  
- 🧱 **Stratigraphic layers and soil horizons**  
- 🧲 **Magnetometry, resistivity, GPR (governed)**  
- 🏞 **Settlement landscapes and cultural corridors**  
- 🔐 **CARE & Sovereignty-restricted cultural data**

All archaeology datasets in v11 must be:

- **FAIR+CARE certified**
- **Sovereignty governed**
- **Spatially generalized (H3 r7–r9)**
- **Provenance-linked (PROV-O)**
- **STAC/DCAT represented**
- **Ethically validated before publication**

---

# 🗂️ Directory Layout (v11)

```text
docs/analyses/archaeology/datasets/
├── README.md
│
├── lidar/                         # DEM derivatives, hillshade, slope, curvature
├── sar/                           # SAR moisture & coherence signals
├── geophysics/                    # Magnetometry, GPR, resistivity (governed)
│   ├── magnetometry/
│   ├── gpr/
│   └── resistivity/
│
├── historical_maps/               # Plats, treaty boundaries, surveys, map scans
├── manuscripts/                   # NER-extracted archival entities (OCR → NER → STAC)
├── stratigraphy/                  # Soil horizons, KGS & USDA profiles
├── paleoenvironment/              # Pollen, charcoal, fauna, lake cores
├── cultural_landscapes/           # Trails, settlements, mound distributions
├── sovereignty/                   # High-sensitivity Indigenous datasets (generalized)
│
├── stac/                          # STAC Items/Collections for all archaeology data
└── metadata/                      # DCAT + CARE metadata + provenance bundles
```

---

# 🧭 Dataset Categories (v11 Expanded)

| Category | Description | Sensitivity | CARE Rules |
|---------|-------------|-------------|------------|
| **LiDAR / SAR** | Landscape geometry + soil moisture anomalies | Medium | Generalize hillshade derivatives |
| **Geophysics** | Magnetometry / GPR / resistivity | High | H3 r8–r10 generalization; sovereignty board approval |
| **Historical Maps** | Treaty, plats, surveys | Low–High | Treaty data requires contextual CARE notes |
| **Manuscripts → NER** | People, places, events extracted from text | Medium | Remove personal identifiers; cultural review |
| **Stratigraphy** | Soil profiles, depositional contexts | Low | Standard FAIR rules |
| **Paleoenvironment** | Pollen, fauna, charcoal, cores | Low | Ecological only; safe |
| **Cultural Landscapes** | Settlements, trails, interaction spheres | High | H3 generalization; sovereignty masking |
| **Sovereignty Datasets** | Tribal heritage datasets | Highest | Strict CARE; no public coordinates |

---

# 🌐 Required Metadata (v11 Standards)

Every dataset must include:

| Requirement | Standard |
|------------|----------|
| Spatial Extent | GeoJSON bbox + H3 footprint |
| Temporal Extent | OWL-Time interval + precision |
| CRS | EPSG:4326 (required) |
| Checksum | SHA-256 |
| Provenance | PROV-O bundle |
| Cultural Sensitivity | CARE flags + sovereignty notes |
| STAC Item | `stac_version: 1.0.0` |
| DCAT Dataset | `dcat:Dataset` |

Example STAC Item (properly nested for v11):

~~~json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "archaeology-cultural-landscapes-v11",
  "bbox": [-102, 37, -94.6, 40],
  "properties": {
    "kfm:domain": "archaeology",
    "kfm:temporal": "multi-period",
    "care:sensitivity": "high",
    "care:sovereignty": "protected",
    "kfm:generalization": "H3-r8"
  },
  "assets": {
    "footprint": {
      "href": "https://example.com/cultural_landscape_h3.geojson",
      "type": "application/geo+json",
      "roles": ["data"]
    }
  }
}
~~~

---

# 🧩 How These Datasets Feed KFM v11

## 🔄 Neo4j Knowledge Graph
Nodes:
- `Site`, `Artifact`, `Culture`, `OccupationPhase`,  
- `LandscapeUnit`, `GeomorphUnit`, `HydroUnit`,  
- `StoryNode`, `Document`, `Event`.

Edges:
- `LOCATED_AT`, `INFERRED_FROM`,  
- `OCCURRED_IN`, `ASSOCIATED_WITH`,  
- `MENTIONED_IN`, `HAS_PROVENANCE`.

## 🧠 Focus Mode v3
- AI summaries with cultural sensitivity gating  
- Explainability overlays (what data influenced what insight)  
- Sovereignty-aware behavior

## 🗺 MapLibre & Cesium Layers
- H3-generalized footprints  
- Cultural corridors  
- Geophysics anomaly overlays  
- Historical alignments  

---

# 🔐 CARE + Sovereignty Enforcement

## Prohibited Without Review
- Exact coordinates of sacred sites  
- Burial mounds / human remains  
- Restricted tribal archives  
- Non-consensual heritage datasets  
- Any geometry below H3 r7  

## Required
- CARE annotation in metadata  
- Sovereignty notice chips in UI  
- Generalization logs  
- Consent or cultural custodial review  

---

# 📊 Dataset Status Summary (v11)

| Dataset | Category | CARE Level | Sovereignty | Status | Notes |
|--------|----------|------------|-------------|--------|-------|
| `statewide-gazetteer-v11` | Gazetteers | Medium | Yes | 🟢 Active | Coordinates generalized |
| `magnetometry-ks-river-v11` | Geophysics | High | Yes | 🟡 Review | Needs sovereignty re-check |
| `paleo-charcoal-v11` | Environment | Low | No | 🟢 Active | Clean & FAIR |
| `protohistoric-routes-v11` | Cultural Landscapes | High | Yes | 🟢 Active | H3 r8 geometry |

---

# 🧾 Example v11 Dataset Provenance Record

```json
{
  "id": "arch_dataset_v11_protohistoric_routes",
  "checksum_sha256": "a0c4ce5012bd...",
  "care_level": "high",
  "sovereignty_protected": true,
  "generalization_method": "H3-r8",
  "derived_from": [
    "historical_maps/1850_plats.tif",
    "manuscripts/diaries_ocr_v4.json"
  ],
  "validated_by": [
    "FAIR+CARE Council",
    "Tribal Sovereignty Review Board"
  ],
  "timestamp": "2025-11-24T14:00:00Z"
}
```

---

# 🕰 Version History

| Version | Date | Summary |
|--------:|------|---------|
| **v11.0.0** | 2025-11-24 | Full v11 rebuild; sovereignty dataset class; expanded STAC/DCAT; H3 r7–r10 rules; cultural safety expansion. |
| v10.4.0 | 2025-11-17 | v10 final: dataset index, STAC/DCAT requirements. |
| v10.0.0 | 2025-11-10 | Initial dataset structure. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · Sovereignty Aligned  
MCP-DL v6.3 · KFM-MDP v11 · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to Archaeology Analyses](../README.md)

</div>