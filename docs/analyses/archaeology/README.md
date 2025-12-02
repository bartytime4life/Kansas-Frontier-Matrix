---
title: "🏺 KFM v11.2.3 — Archaeology Analyses Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed index of archaeology analyses in KFM v11, integrating remote sensing, historical cartography, NLP, geomorphology, and sovereignty-aligned workflows."
path: "docs/analyses/archaeology/README.md"
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council · Tribal Sovereignty Board"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_integrity_checksum: "<sha256-of-this-file>"

doc_uuid: "urn:kfm:doc:archaeology-analyses-index-v11.2.3"
semantic_document_id: "kfm-doc-analyses-archaeology-index-v11.2.3"
event_source_id: "ledger:kfm:doc:analyses:archaeology:index:v11.2.3"
doc_kind: "Domain Index"
intent: "archaeology-analyses"
category: "Analyses · Archaeology · Heritage · Historical Landscapes"

sbom_ref: "../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/analyses-archaeology-v11.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-gco2e-v1.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

fair_category: "F1-A1-I1-R1"
care_label: "High-Sensitivity · Sovereignty-Restricted"
sensitivity: "Cultural / Historical / Environmental"
sensitivity_level: "High"
indigenous_rights_flag: true
risk_category: "Moderate"
public_exposure_risk: "Governed"
redaction_required: true

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
immutability_status: "mutable-plan"
jurisdiction: "Kansas / United States"
classification: "Public (Governed)"

header_profile: "standard"
footer_profile: "standard"

data_steward: "Archaeology & Heritage WG · Tribal Sovereignty Board"
provenance_chain:
  - "docs/analyses/archaeology/README.md@v11.0.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

<div align="center">

# 🏺 **Kansas Frontier Matrix — Archaeology Analyses Index (v11)**  
`docs/analyses/archaeology/README.md`  

**Diamond⁹ Ω / Crown∞Ω Ultimate Certified**  
**FAIR+CARE · Tribal Sovereignty-Aligned · Scientifically Rigorous · Culturally Respectful**

</div>

---

## 📘 Overview & Scope

The **Archaeology Domain (KFM v11)** is a unified analytical environment merging:

- 🛰 **Remote sensing** — LiDAR, SAR, thermal IR, multispectral, DEM derivatives  
- 🧭 **Spatial historical geography** — treaties, plats, diaries, surveys, archival photographs  
- 🧬 **Entity extraction from historical texts** — OCR → NER → GeoLink → Story Nodes  
- 🌊 **Hydrological reconstruction** — paleo-channels, floodplains, watershed models  
- 🌿 **Ecological co-analysis** — biomes, soils, slope, resource access  
- 🗺 **Indigenous cultural landscapes** — CARE-restricted + sovereignty protections  
- 🏞 **3D archaeology** — terrain, predicted excavation volumes, architectural inference  
- 🤖 **AI-assisted archaeological inference** — Focus Mode v3, explainability v3.2, narrative risk filters  

KFM v11 treats archaeological data as **high-sensitivity cultural knowledge**, governed by:

- **CARE Principles**  
- **Sovereignty-aligned data policies**  
- **FAIR+CARE Council**  
- **Indigenous Data Governance Board (IDGB)**  

No sensitive site geometries are ever revealed at full resolution in public-facing layers.

---

## 🗂️ Directory Layout (v11 · Normative)

~~~text
docs/
└── analyses/
    └── archaeology/                      # Archaeology domain root
        ├── 📄 README.md                  # This file (domain index)
        │
        ├── 🗂️ datasets/                  # Archaeological source material (governed)
        │   ├── 🛰️ lidar/                 # Hillshade, slope, roughness, CHM, DEM
        │   ├── 📡 sar/                   # Sentinel-1, UAVSAR, moisture anomalies
        │   ├── 🗺️ historical_maps/       # Plats, railroad surveys, treaty boundaries
        │   ├── 📚 manuscripts/           # Diaries, reports, archival letters, NER outputs
        │   ├── 🧲 geophysics/            # Magnetometry, GPR, resistivity (governed)
        │   ├── 🌱 soils/                 # SSURGO/STATSGO infiltration & composition
        │   ├── 🌊 hydrology/             # Paleo-streams, WID data, flooding models
        │   └── 🪶 sovereignty/           # CARE + sovereignty-restricted datasets
        │
        ├── 🧪 methods/                   # Methodological READMEs (normative)
        │   ├── remote_sensing/          # LiDAR+SAR fusion, feature extraction
        │   ├── geoprocessing/           # Slope, roughness, curvature, landform models
        │   ├── nlp/                     # OCR → NER → Linking → Story Node generation
        │   ├── predictive_models/       # AI-based site prediction (Focus v3)
        │   ├── treaty_alignment/        # Boundary alignment, centroid modeling
        │   ├── deformation_models/      # Earthwork geometry normalization
        │   └── cultural_landscape/      # Landscape change & movement corridors
        │
        ├── 📊 results/                   # Published, governed outputs
        │   ├── site_probability_maps/   # Raster probability surfaces (H3 generalized)
        │   ├── geomorphology/           # Landform classifications
        │   ├── hydrology_overlays/      # Paleo-water maps
        │   ├── text_entity_graphs/      # Linked archival–spatial entities
        │   ├── cultural_routes/         # Interaction spheres & paths (generalized)
        │   └── storynodes/              # Story Node v3 collections & narratives
        │
        ├── ✅ validation/                # Validation & review artifacts (governed)
        │   ├── field_notes/             # Field logbooks (redacted / generalized)
        │   ├── drone_surveys/           # Low-res orthos + validation metadata
        │   ├── peer_review/             # Internal/external archaeological reviewers
        │   └── confidence_metrics/      # Statistical/ML validation reports
        │
        ├── 🌐 visualization/             # UI-facing resources
        │   ├── maplibre_layers/         # 2D layers (privacy-hardened)
        │   ├── cesium_tiles/            # 3D terrain tilesets and overlays
        │   ├── embeddings/              # PCA/UMAP embeddings of text/spatial data
        │   └── dashboards/              # FAIR+CARE visualization outputs
        │
        └── 🧾 metadata/                  # STAC · DCAT · PROV-O bundles
            ├── provenance/              # PROV-O lineage bundles
            ├── audit/                   # FAIR+CARE audit snapshots
            └── stac/                    # STAC Items/Collections (generalized)
~~~

This layout is **normative** for all archaeology-related analyses and documentation in KFM v11.

---

## 🧩 Core v11 Analytical Modules

### 🛰 1. Remote Sensing & Feature Extraction

- LiDAR derivatives: slope, curvature, openness, local relief.  
- SAR coherence/texture for soil disturbance and moisture signatures.  
- Thermal IR for nocturnal heat retention and potential structural remains.  
- AI Feature Classifier v3.1 (explainable, bias-audited).

**Outputs (graph-safe):**

- H3-generalized feature clusters.  
- Anomaly heatmaps (privacy-aware).  
- Confidence-weighted probability surfaces.

---

### 🗺 2. Historical Cartography & Treaty Alignment

- 1850s–1930s plats rectified with TPS warping and control points.  
- Treaty polygons validated against legal descriptions and archival sources.  
- Historical trail extraction using OCR-based trajectory analysis and cost surfaces.

**Outputs:**

- Multi-epoch georeferenced boundary atlas.  
- “Lost routes” inferred via elevation- and cost-based modeling.  

---

### 🧬 3. NLP & Text-Based Archaeology

**Pipeline:**

1. OCR v4 (governed, bias-checked).  
2. Domain-tuned NER (persons, places, rivers, settlements, cultural terms).  
3. GeoLink v3 (link entities to spatial/temporal context).  
4. Entity clustering and interaction sphere modeling.  
5. Story Node v3 synthesis with sovereignty and CARE filters.

**Outputs:**

- Temporal entity graphs (Neo4j-ready).  
- Historical interaction spheres.  
- NER + linkage provenance bundles.

---

### 🏞 4. Geomorphology & Settlement Viability

- Paleo-hydrology reconstruction (channels, floodplains, terraces).  
- Resource catchment modeling (water, soils, biota).  
- Slope + soils + distance-to-water viability scoring.

**Outputs:**

- Multi-factor suitability layers.  
- Settlement corridors and landscape viability maps.

---

### 🧪 5. Validation Framework v11

- Drone orthophotos (governed; downsampled/public-safe views).  
- Field validation logs with sensitivity flags and generalized locations.  
- Inter-rater reliability scoring for interpretations.  
- Tribal review and cultural consultation logs.

Validation content is **precision-reduced** for public outputs; full-detail artifacts remain sovereignty-governed.

---

## 🕸️ Story Node & Knowledge Graph Integration

All archaeology analyses are required to emit **graph-safe, Story Node–ready** outputs:

- **Neo4j mapping:**
  - Sites, routes, hydrological features, and entities mapped to controlled node labels.  
  - Relationships use governed, ontology-aligned types (KFM-OP v11; CIDOC-CRM, GeoSPARQL, OWL-Time).  

- **Story Nodes:**
  - Each published analysis may register Story Nodes under `results/storynodes/`.  
  - Story Nodes must:
    - Reference this index via `semantic_document_id`.  
    - Embed PROV-O lineage links into the knowledge graph.  
    - Carry sovereignty and sensitivity flags forward into Focus Mode v3.  

- **Focus Mode v3:**
  - Uses this index as the **authoritative registry** of archaeology analysis modules.  
  - Only graph paths marked as **sovereignty-compliant** and **redaction-complete** are queryable in public Focus Mode profiles.

---

## ⚖️ FAIR + CARE + Sovereignty Enforcement (v11)

| Pillar                  | v11 Implementation                                                                 |
|-------------------------|-------------------------------------------------------------------------------------|
| **Collective Benefit**  | Archaeology analyses must benefit Tribal communities first and foremost.           |
| **Authority to Control**| Sensitive-site geometry generalized to H3 r7–r9 and governed disclosure policies.  |
| **Responsibility**      | Council review required for Story Node publication and external dissemination.     |
| **Ethics**              | AI outputs filtered through cultural sensitivity scoring and human oversight.      |
| **CARE+**               | No disclosure of sacred sites, burials, or private cultural knowledge.             |

All modules MUST reference `sovereignty_policy` and adhere to its redaction and approval workflows.

---

## 🔐 Sensitive Site Handling (v11)

- Full-resolution coordinates **never** stored in publicly queryable STAC items or Story Nodes.  
- Only H3-aggregated centroids are displayed in MapLibre/Cesium, with level chosen per sensitivity.  
- Story Nodes referencing sensitive content are **auto-redacted** or generalized.  
- Sovereignty flags injected into:
  - Focus Mode v3 responses.  
  - All downstream analytics pipelines.  
  - All PROV-O provenance bundles.

Any derivative work must maintain or strengthen this level of protection.

---

## 🔄 Integrated v11 Workflow

~~~mermaid
flowchart LR
    A["Remote Sensing (LiDAR · SAR · IR)"]
      --> C["Feature Extraction + AI Classifier v3"]
      --> D["Geomorphology & Hydrology v11"]
      --> E["Archaeological Modeling"]
      --> G["KFM Knowledge Graph"]

    B["Historical Texts + Maps"]
      --> F["OCR → NER → GeoLink → Story Nodes"]
      --> E

    E --> H["Validation (Field · Drone · Sovereignty Review)"]
    H --> G
    G --> I["Focus Mode v3 (Explainable · CARE-Aware)"]
~~~

This diagram is **descriptive**, not executable; concrete pipelines must be documented in module-specific READMEs.

---

## 🧾 Example v11 Metadata Record

~~~json
{
  "id": "archaeology_analysis_v11_2025Q4",
  "modules": [
    "remote_sensing",
    "historical_cartography",
    "nlp_entity_extraction",
    "geomorphology_modeling",
    "validation_framework_v11"
  ],
  "sovereignty_protected": true,
  "sensitive_geometries_generalized": "H3-r8",
  "faircare_status": "certified",
  "energy_wh": 4.82,
  "carbon_gco2e": 0.53,
  "governance_registered": true,
  "created": "2025-11-24T18:00:00Z",
  "validator": "@kfm-archaeology"
}
~~~

This record shape MUST align with `telemetry_schema` for archaeology analyses and energy/carbon schemas for sustainability.

---

## 🕰 Version History

| Version   | Date       | Summary                                                                 |
|-----------|------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | v11.2 alignment; added status; clarified Story Node/graph integration; sovereignty gates reiterated. |
| v11.0.0   | 2025-11-24 | Full v11 rebuild; CARE+ sovereignty extensions; AI v3 integration; new directory schema. |
| v10.1.0   | 2025-11-11 | Initial Platinum-template archaeology index.                            |

---

<div align="center">

© 2025 Kansas Frontier Matrix · CC-BY 4.0  
**Diamond⁹ Ω / Crown∞Ω Ultimate Certified**  
FAIR+CARE · Sovereignty Aligned · MCP-DL v6.3 · KFM-MDP v11.2.2  

[⬅ Back to Analyses](../README.md) · [🛡 Sovereignty Policy](../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

</div>