---
title: "🧲 Kansas Frontier Matrix — Archaeological Geophysics Datasets (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/geophysics/README.md"
version: "v11.0.0"
last_updated: "2025-11-24"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council · Tribal Sovereignty Board"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_guid: "urn:kfm:doc:archaeology-geophysics-datasets-v11.0.0"
doc_kind: "Dataset Category"
intent: "archaeology-geophysics-datasets"
semantic_document_id: "kfm-doc-archaeology-geophysics-datasets"

sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-geophysics-datasets-v11.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

fair_category: "F1-A1-I1-R1"
care_label: "High-Sensitivity · Sovereignty-Governed"
sensitivity: "Archaeological / Cultural"
sensitivity_level: "Medium"
indigenous_data_flag: true
risk_category: "Moderate"
public_exposure_risk: "Governed"
redaction_required: true

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Governed Public"
jurisdiction: "Kansas / United States"
immutability_status: "mutable-plan"
---

<div align="center">

# 🧲 **Kansas Frontier Matrix — Archaeological Geophysics Datasets (v11)**  
`docs/analyses/archaeology/datasets/geophysics/README.md`

FAIR+CARE Certified · Sovereignty-Governed  
Diamond⁹ Ω / Crown∞Ω · MCP-DL v6.3 · KFM-MDP v11

</div>

---

# 📘 Overview (v11)

The **Archaeological Geophysics Layer** in KFM v11 integrates:

- **Magnetometry** (gradiometer surveys, anomaly grids)  
- **Ground-Penetrating Radar (GPR)** time-slices  
- **Electrical resistivity** transects & grids  
- **LiDAR-derived archaeological features** (generalized)  
- **AI-assisted anomaly detection** (explainability-linked)  
- **Human-validated interpretations** (features, boundaries, structures)

These datasets feed into:

- Settlement detection  
- Cultural landscape reconstruction  
- Time-aligned Story Node v3 narratives  
- Focus Mode v3 explainability + provenance  
- MapLibre 2D & Cesium 3D layers  
- Neo4j graph entities (`GeophysicsSurvey`, `InterpretedFeature`, `LiDARFeature`)

All datasets must pass:

- **FAIR+CARE v11 cultural governance**  
- **Tribal sovereignty review** (when required)  
- **Spatial generalization** (H3 r7–r10)  
- **PROV-O lineage compliance**  
- **DCAT 3.0 / STAC 1.0 v11 metadata validation**

---

# 🗂️ Directory Layout (ASCII-Aligned, v11)

~~~text
docs/analyses/archaeology/datasets/geophysics/
├── README.md                     # This document
├── raw/                          # Open-access PD-only sensor grids
├── processed/                    # Cleaned + filtered + generalized outputs
├── interpreted/                  # Human-validated archaeological feature masks
├── stac/                         # STAC Items/Collections (v11-compliant)
├── metadata/                     # DCAT 3.0 + CARE v11 metadata
└── provenance/                   # PROV-O lineage + sovereignty review bundles
~~~

---

# 🧭 Dataset Categories (v11)

| Category | Description | CARE Level | Allowed | Notes |
|---------|-------------|-----------|---------|-------|
| **Magnetometry** | Magnetic anomalies for feature detection | C2 | Yes | Must be generalized (H3 r7≥) |
| **GPR Time-Slices** | Subsurface reflections | C2–C3 | Conditional | Depth > 30cm only, PD slices only |
| **Electrical Resistivity** | Moisture/soil contrast patterns | C1–C2 | Yes | PD-only |
| **LiDAR Archaeological Features** | DEM-derived structures | C3 | Conditional | Burial/sacred must be excluded |
| **AI-Detected Features** | ML anomaly grids | C2 | Yes | Requires model card + explainability |
| **Human Interpretations** | Verified outlines of features | C2 | Yes | Requires justification metadata |

**Strictly Prohibited:**

- Burial mound locations  
- Sacred ceremonial features  
- Unreviewed raw GPR volumes  
- High-resolution LiDAR showing sensitive cultural features  
- Any dataset lacking sovereignty approval

---

# 📦 v11 Metadata Requirements

## STAC v11 Requirements

Each dataset must include:

- `id`  
- H3-generalized `bbox`  
- Polygon geometries only  
- `start_datetime`, `end_datetime` (OWL-Time)  
- `care:sensitivity`  
- `care:sovereignty`  
- `care:consent_status`  
- CRS metadata (`proj:*`)  
- `kfm:generalization` (H3-r7 to r10)  
- `kfm:survey_type` (magnetometry, GPR, etc.)  
- Assets for data/interpretation/tilesets  
- PROV-O lineage reference

## DCAT 3.0 Requirements

- `dct:title`  
- `dct:license` (PD, CC-BY, CC0)  
- `dcat:distribution`  
- `dct:temporal`  
- `dcat:keyword`  
- `dct:provenance`  

## CARE v11 Requirements

- Cultural sensitivity level  
- Sovereignty governance pathway  
- Consent verification  
- Required masking notes  
- Cultural context description  

---

# 🧪 Processing Requirements (v11)

All geophysical datasets must be:

- Cleaned and noise-filtered  
- Spatially generalized using:
  - H3 r7 (minimum)
  - H3 r10 (maximum detail allowed)  
- Provenance-documented (PROV-O bundle required)  
- Validated through FAIR+CARE + sovereignty review  
- Converted to open, accessible formats:
  - COG  
  - GeoTIFF  
  - Generalized PNG (for interpreted features)  
  - GeoJSON for feature outlines  
- Accompanied by:
  - Processing notes  
  - QC logs  
  - Model cards (for ML outputs)  

---

# 🛰 Integration Into KFM Systems (v11)

## Neo4j Graph Entities

Nodes:
- `GeophysicsSurvey`
- `MagnetometryGrid`
- `GPRSlice`
- `ResistivityTransect`
- `LiDARFeature`
- `InterpretedFeature`

Relationships:
- `DETECTS_FEATURE`
- `LOCATED_AT`
- `GENERALIZED_FROM`
- `ASSOCIATED_WITH`
- `CULTURALLY_FILTERED_VIA`

## Story Node v3 Integration

Geophysics data supports:

- Cultural landscape chapters  
- Feature-based narratives  
- Settlement expansion timelines  
- AI explainability overlays  
- Provenance chips & sovereignty disclaimers  

## Focus Mode v3 Integration

- AI narratives gated by sovereignty rules  
- High-sensitivity redaction filters  
- Explainability (SHAP / IG)  
- Confidence-weighted anomaly summaries  

## Mapping Integration

- MapLibre 2D generalized grids  
- Cesium 3D elevation + feature extrusions  
- Time-enabled archaeological layers  

---

# 📊 Dataset Index (v11)

| Dataset | Category | CARE | Sovereignty | Status | Last Review | Notes |
|---|---|---|---|---|---|---|
| `magnetometry/north-ks-v2` | Magnetometry | C2 | Yes | 🟢 Active | 2025-11 | Fully generalized |
| `gpr/high-plains-v3` | GPR | C3 | Yes | 🟡 Review | 2025-10 | Depth + sovereignty review pending |
| `lidar/prairie-features-v2` | LiDAR | C3–C4 | Yes | 🔒 Hold | 2025-11 | Potential burial features detected |
| `interpretations/central-ks-v2` | Interpretation | C2 | Yes | 🟢 Active | 2025-11 | Cultural review completed |

---

# 🧠 Example STAC Item (v11)

~~~json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "magnetometry-north-ks-v2",
  "bbox": [-101.8, 37.4, -95.8, 40.1],
  "geometry": {
    "type": "Polygon",
    "coordinates": [[[ ... ]]]
  },
  "properties": {
    "kfm:survey_type": "magnetometry",
    "care:sensitivity": "generalized",
    "care:sovereignty": "protected",
    "care:consent_status": "approved",
    "kfm:generalization": "H3-r8",
    "kfm:provenance": "provenance/mag-north-ks-v2.json"
  },
  "assets": {
    "grid": {
      "href": "https://example.org/geophysics/mag_north_ks_v2.tif",
      "type": "image/tiff; application=geotiff",
      "roles": ["data"]
    }
  }
}
~~~

---

# 🕰 Version History

| Version | Date | Summary |
|--------:|------|---------|
| **v11.0.0** | 2025-11-24 | Full v11 rebuild; CARE v11; sovereignty gating; H3 r7–r10; STAC/DCAT v11; PROV-O lineage v11 |
| v10.4.0 | 2025-11-17 | First complete v10 index |
| v10.0.0 | 2025-11-10 | Initial geophysics dataset structure |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE v11 · Sovereignty-Governed  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
KFM-MDP v11.0 · MCP-DL v6.3  

[⬅ Back to Archaeology Datasets](../README.md)

</div>