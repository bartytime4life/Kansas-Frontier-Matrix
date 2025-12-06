---
title: "🏞️ Kansas Frontier Matrix — Land Use & Historical Overlaps Analysis (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/cross-domain/landuse-historical-overlaps.md"
version: "v11.2.4"
last_updated: "2025-12-06"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Historical Ecology Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x analytical-contract compatible"
status: "Active / Enforced"

doc_kind: "Analysis Study"
intent: "cross-domain-landuse-historical-overlaps-analysis"
role: "cross-domain-analysis"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "cross-domain-analyses"
  applies_to:
    - "historical-ecology"
    - "land-use"
    - "hydrology"
    - "heritage-overlays"
    - "story-nodes"
    - "focus-mode"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Mixed Dataset Classification"
sensitivity: "Mixed (historical + cultural; auto-mask rules apply)"
sensitivity_level: "Medium"
public_exposure_risk: "Medium"
classification: "KFM-Open"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
risk_category: "Historical Ecology & Land Governance"
redaction_required: true

commit_sha: "<latest-commit-hash>"
previous_version_hash: "docs/analyses/cross-domain/landuse-historical-overlaps.md@v10.0.0"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../releases/v11.2.4/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/analyses-crossdomain-landusehistory-v1.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/analyses/cross-domain/landuse-historical-overlaps.md@v10.0.0"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/docs-analyses-cross-domain-landuse-history-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/docs-analyses-cross-domain-landuse-history-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"

doc_uuid: "urn:kfm:doc:analyses:cross-domain:landuse-historical-overlaps:v11.2.4"
semantic_document_id: "kfm-analyses-cross-domain-landuse-historical-overlaps-v11.2.4"
event_source_id: "ledger:kfm:doc:analyses:cross-domain:landuse-historical-overlaps:v11.2.4"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "metadata-extraction"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-historical-claims"
  - "culturally-sensitive-inference"
  - "governance-override"
  - "content-alteration"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🌎 Research Objectives"
    - "⚙️ Datasets & Variables"
    - "🧩 Methods Summary"
    - "🧠 FAIR+CARE Alignment"
    - "📊 Key Findings (v10.0.0 Baseline)"
    - "🧾 Example FAIR+CARE Telemetry Log"
    - "🔍 Ethical Cartography Framework"
    - "🧪 Validation Pipelines"
    - "📈 Quality Metrics"
    - "🕰️ Version History"

diagram_profiles:
  - "mermaid-flowchart-v1"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "diagram-check"
  - "footer-check"
  - "accessibility-check"
  - "provenance-check"

ci_integration:
  workflow: ".github/workflows/cross-domain-analyses.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Cross-Domain Insight × FAIR+CARE Ethics × Historical Stewardship"
  architecture: "Land Use · Historical Geography · Hydrology"
  analysis: "AI-Assisted · Reproducible · Governance-First"
  data-spec: "STAC/DCAT/PROV-O · Open & Governed"
  telemetry: "Explainable Analyses · Traceable Metrics"
  graph: "Land–History–Hydrology Overlaps in the Kansas Knowledge Graph"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_version_history: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true

deprecated_fields: []
---

<div align="center">

# 🏞️ **Kansas Frontier Matrix — Land Use & Historical Overlaps Analysis**  
`docs/analyses/cross-domain/landuse-historical-overlaps.md`

**Purpose:**  
Analyze **spatial and temporal intersections between historical land ownership, Indigenous territories, and modern land-use patterns** across Kansas.  
This FAIR+CARE-certified analysis integrates **historical, ecological, hydrological, and governance** datasets to identify long-term land-cover changes, ownership transitions, and environmental consequences under KFM v11.2.4 and MCP-DL v6.3.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL_v6.3-blue)](../../README.md)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../standards/faircare/FAIRCARE-GUIDE.md)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)  
[![Status: Active](https://img.shields.io/badge/Status-Active-success)](../../../releases/v11.2.4/manifest.zip)

</div>

---

## 📘 Overview

The **Land Use & Historical Overlaps Analysis** explores how patterns of land use, ownership, and ecological function have shifted since the mid-1800s.  
By overlaying **archival treaties**, **agricultural censuses**, **Indigenous territorial data**, and **modern remote-sensing land cover**, this analysis quantifies changes in:

- Agricultural and settlement expansion.  
- Indigenous and public land transitions.  
- Wetland and prairie ecosystem loss.  
- Floodplain reclamation and alteration of hydrological regimes.  

Results feed:

- Cross-Domain Story Nodes about land change and governance.  
- Focus Mode overlays for land-use history and hydrological impacts.  
- Policy-facing visualizations for conservation, water, and land-justice dialogues.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/cross-domain/
├── 📄 README.md
├── 📄 climate-ecology-linkages.md
├── 📄 hydro-geo-interactions.md
├── 📄 carbon-water-cycles.md
├── 📄 landuse-historical-overlaps.md            # This file
│
├── 📂 datasets/
│   ├── 📄 historical_treaty_boundaries.geojson
│   ├── 📄 landuse_1950_2020.tif
│   ├── 📄 census_agriculture_tracts.csv
│   ├── 📄 indigenous_cultural_sites.json       # restricted / CARE-governed
│   └── 📄 hydrographic_network.geojson
│
├── 📂 methods/
│   ├── 📄 landuse-change-detection.md
│   ├── 📄 historical-overlay-techniques.md
│   └── 📄 ethical-cartography.md
│
├── 📂 results/
│   ├── 📄 landuse-historical-summary.md
│   ├── 📂 tables/
│   │   └── 📄 overlap-statistics.csv
│   ├── 📂 figures/
│   │   ├── 📄 treaty-overlay-visualization.png
│   │   └── 📄 floodplain-conversion-map.svg
│   └── 📂 telemetry-logs/
│       └── 📄 landuse-history-telemetry.jsonl
│
└── 📄 governance.md                             # CDAF-wide governance & review notes
~~~

Author rules:

- Restricted / culturally sensitive content (e.g., precise cultural sites) must be kept in **restricted** datasets and generalized or masked in public figures.  
- Any new artifact for this analysis must be placed under `datasets/`, `methods/`, or `results/` and reflected in this tree.

---

## 🌎 Research Objectives

| Objective | Description | Linked Domains |
|----------:|-------------|----------------|
| **1. Quantify Historical Land Conversion** | Map shifts from Indigenous and ecological lands to agricultural or urban zones. | Historical · Ecology |
| **2. Identify Overlaps Between Treaties & Modern Land Use** | Determine spatial intersections between 19th-century treaty boundaries and 21st-century land cover. | Historical · Hydrology |
| **3. Evaluate Ecological Impact** | Assess how land-use transitions affected wetlands, prairies, biodiversity, and floodplains. | Ecology · Hydrology |
| **4. Create FAIR+CARE Ethical Cartography** | Ensure cultural sites and sensitive areas are anonymized and ethically represented. | Governance · IDGB |
| **5. Enable Public Transparency** | Provide reproducible, open-data land-use history layers for civic education and policy. | FAIR+CARE Council |

---

## ⚙️ Datasets & Variables

### Datasets

| Dataset                               | Description                                               | Source                              | License      |
|---------------------------------------|-----------------------------------------------------------|-------------------------------------|-------------|
| `historical_treaty_boundaries.geojson` | Digitized boundaries from 19th-century treaties & cessions. | Kappler’s *Indian Affairs* / IDGB | CC-BY 4.0   |
| `landuse_1950_2020.tif`              | Multi-temporal land cover raster (cropland, urban, grassland). | USGS NLCD / ESA CCI               | CC-BY 4.0   |
| `census_agriculture_tracts.csv`      | Historical & modern agricultural tract boundaries/metrics.| USDA / Kansas Historical Society   | CC-BY 4.0   |
| `indigenous_cultural_sites.json`     | Cultural geography & heritage layer (restricted).         | IDGB                               | CARE-licensed |
| `hydrographic_network.geojson`       | Rivers and floodplains for hydrological context.          | KFM Hydrology Dataset              | CC-BY 4.0   |

### Key Variables

| Variable                 | Description                                        | Unit/Type         | Domain          |
|--------------------------|----------------------------------------------------|-------------------|-----------------|
| `LandCover_class`       | Categorical land-use/land-cover class              | Enum              | Land Use        |
| `Treaty_area_id`        | Identifier for specific treaty polygon             | String            | Historical      |
| `Indigenous_territory`  | Territory label(s) (CARE-governed)                 | String / Array    | Heritage        |
| `Ag_census_yield`       | Agricultural productivity metrics                  | e.g., bushels/acre| Agriculture     |
| `Wetland_extent`        | Wetland area within analysis unit                  | km²               | Hydrology/Ecology |
| `Prairie_extent`        | Native prairie area                                | km²               | Ecology         |
| `Urban_fraction`        | Proportion of urbanized land                       | 0–1               | Land Use        |

---

## 🧩 Methods Summary

| Step                       | Technique                              | Tools                         | Output                               |
|----------------------------|----------------------------------------|-------------------------------|--------------------------------------|
| Spatial Alignment          | Reprojection & grid harmonization      | QGIS · GDAL                   | CRS-aligned layers                   |
| Historical Overlay         | Time-series overlay of treaties vs land cover | Python · rasterio · GeoPandas | `treaty-landuse-overlap.tif`         |
| Change Detection           | Land-cover classification differencing | NumPy · OpenCV                | `landuse-change-map.png`             |
| Hydrological Context       | Overlay with rivers/floodplains        | ArcGIS · GeoPandas            | Floodplain conversion maps           |
| Ethical Cartography        | Masking/generalization of sensitive data | Custom KFM tooling + QGIS   | Public-safe visualizations           |
| Governance Validation      | FAIR+CARE + IDGB review                | FAIR+CARE pipeline            | Validation & consent reports         |

Method details (e.g., classification legends, thresholds, masking rules) are specified in:

- `methods/landuse-change-detection.md`  
- `methods/historical-overlay-techniques.md`  
- `methods/ethical-cartography.md`

---

## 🧠 FAIR+CARE Alignment

| FAIR Principle | Implementation                                           | CARE Principle      | Implementation                                                          |
|----------------|-----------------------------------------------------------|---------------------|-------------------------------------------------------------------------|
| **Findable**   | Indexed in cross-domain STAC collections with DOIs & temporal extents. | **Collective Benefit** | Supports inclusive land governance and environmental justice work.  |
| **Accessible** | Open-access (non-restricted layers) via KFM Data Hub.    | **Authority to Control** | Restricted heritage layers governed by IDGB, with explicit consent scopes. |
| **Interoperable** | GeoJSON, GeoTIFF, CSV with shared CRS (EPSG:4326).   | **Responsibility**  | Sensitive sites masked; clear caveats & context in legends & docs.   |
| **Reusable**   | Full provenance, temporal metadata, and method docs.     | **Ethics**          | Avoids exploitative or decontextualized use of Indigenous geography.  |

All public maps must:

- Avoid pinpointing specific sacred or burial locations.  
- Use generalization (e.g., H3 grids, buffers) where needed.  
- Include legends conveying uncertainty, temporal ranges, and governance notes.

---

## 📊 Key Findings (v10.0.0 Baseline)

> **Note:** These are **baseline v10.0.0** metrics.  
> v11.2.4 analyses must either reproduce within governance-approved tolerances or document methodological changes.

| Observation                                       | Metric                   | Interpretation                                         |
|---------------------------------------------------|-------------------------:|--------------------------------------------------------|
| Cropland expansion over former prairie ecosystems | **+42% (1950–2020)**     | Major shift to agriculture in central Kansas.         |
| Treaty-defined lands now under agricultural use   | **≈ 67% overlap**        | Indicates substantial conversion of historical territories. |
| Floodplain alteration via levee projects          | **≈ 23% wetland reduction** | Hydrological fragmentation from human modification. |
| Prairie-to-urban conversion                       | **≈ 14% (1950–2020)**    | Urban growth around Topeka & Wichita corridors.       |

Updated tables live in `results/tables/overlap-statistics.csv` with per-watershed and per-county breakdowns.

---

## 🧾 Example FAIR+CARE Telemetry Log

~~~json
{
  "analysis_id": "crossdomain_landuse_history_v11.2.4",
  "datasets_used": [
    "historical_treaty_boundaries.geojson",
    "landuse_1950_2020.tif",
    "census_agriculture_tracts.csv",
    "hydrographic_network.geojson"
  ],
  "methods_used": [
    "landuse-change-detection.md",
    "ethical-cartography.md"
  ],
  "faircare_score": 97.8,
  "provenance_linked": true,
  "consent_verified": true,
  "validated_by": [
    "FAIR+CARE Council",
    "Indigenous Data Governance Board"
  ],
  "last_validated": "2025-12-05T22:55:00Z"
}
~~~

Telemetry entries append to `results/telemetry-logs/landuse-history-telemetry.jsonl` and are summarized in `releases/v11.2.4/focus-telemetry.json`.

---

## 🔍 Ethical Cartography Framework

~~~mermaid
flowchart TD
    A["Historical Land Data<br/>(Treaties, Census, Maps)"]
      --> B["Modern Land Use Layers<br/>(NLCD, ESA CCI, KFM Landcover)"]
    B --> C["Overlay & Change Detection<br/>(Geospatial Analysis)"]
    C --> D["Hydrological Context Integration<br/>(Floodplains, Basins)"]
    D --> E["FAIR+CARE Validation & Ethical Review<br/>(IDGB + Council)"]
    E --> F["Public Visualization & Transparency Portal<br/>(Generalized Layers)"]
~~~

Key rules:

- **No raw cultural site coordinates** in public outputs.  
- **No “blame narratives”** about communities; focus on structural patterns.  
- **Contextual annotations** explaining treaties, land policies, and uncertainties.

---

## 🧪 Validation Pipelines

| Workflow                    | Function                                            | Output                                                |
|----------------------------|-----------------------------------------------------|-------------------------------------------------------|
| `analysis-validation.yml`  | Confirms historical & modern layer alignment, repro. | `reports/analyses/reproducibility-summary.json`   |
| `faircare-audit.yml`      | Verifies consent & ethical publication of cultural layers. | `reports/data/faircare-validation.json`        |
| `telemetry-export.yml`    | Logs FAIR+CARE metrics and reproducibility metadata. | `releases/v11.2.4/focus-telemetry.json`          |
| `geospatial-validation.yml` | Checks CRS, topology, and overlay quality.         | `reports/data/geospatial-validation.json`            |
| `governance-audit.yml`    | Audits treaty/cultural data use and redaction.      | `reports/governance/landuse-history-audit.json`      |

---

## 📈 Quality Metrics

| Metric                         | Target                             | Verified By                      |
|--------------------------------|------------------------------------|----------------------------------|
| FAIR+CARE Compliance           | ≥ 95%                              | FAIR+CARE Council                |
| Historical Boundary Accuracy   | ≥ 90% treaty alignment             | Governance Secretariat           |
| Geospatial CRS Accuracy        | 100% EPSG:4326 alignment           | CI Validation                    |
| Consent Verification (IDGB)    | 100% for restricted sites          | IDGB + FAIR+CARE Council         |
| Data Provenance Completeness   | 100%                               | Telemetry & Governance Reports   |

Non-compliant outputs must be withheld from:

- Public maps and export endpoints, and  
- Story Nodes and Focus Mode narratives, until remediation and re-validation.

---

## 🕰️ Version History

| Version   | Date       | Author                               | Summary                                                                                                                      |
|----------:|-----------:|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| **v11.2.4** | 2025-12-06 | FAIR+CARE Historical Ecology Council | Aligned to KFM-MDP v11.2.4; added governance metadata, telemetry hooks, ethical cartography framework, and CDAF integration. |
| v10.0.0  | 2025-11-10 | FAIR+CARE Historical Ecology Council | Completed cross-domain analysis of historical land use and Indigenous overlaps using FAIR+CARE-validated ethical cartography workflow. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Developed under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Cross-Domain Framework](README.md) · [Carbon–Water Cycles →](carbon-water-cycles.md) · [⚖ Governance Charter](../../standards/governance/ROOT-GOVERNANCE.md)

</div>