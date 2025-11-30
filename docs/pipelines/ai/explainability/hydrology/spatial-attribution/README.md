---
title: "💧🗺️ KFM v11 — Hydrology Spatial Attribution Explainability (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/ai/explainability/hydrology/spatial-attribution/README.md"
version: "v11.2.3"
last_updated: "2025-11-29"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Hydrology AI WG · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.3/manifest.zip"
attestation_ref: "../../../../../../releases/v11.2.3/slsa-attestation.json"
signature_ref: "../../../../../../releases/v11.2.3/signature.sig"

telemetry_ref: "../../../../../../releases/v11.2.3/hydro-spatial-attribution-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/ai-explainability-hydro-spatial-attribution-v11.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

doc_kind: "Explainability Module"
intent: "hydrology-spatial-attribution"
fair_category: "F1-A1-I1-R2"
care_label: "CARE-Compliant · Watershed-Sensitive · Spatial-Transparency"

classification: "Public (Governed)"
sensitivity: "Low/Moderate (Watershed/tribal hydrology sensitivity)"
machine_extractable: true
jurisdiction: "United States · Kansas"
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# 💧🗺️ **Hydrology Spatial Attribution Explainability (KFM v11)**  
`docs/pipelines/ai/explainability/hydrology/spatial-attribution/`

**Purpose**  
Define the **v11 spatial attribution explainability standard** for hydrology AI pipelines,  
enabling watershed-aware visualization of spatial drivers, climate-hydrology interactions,  
and terrain-soil couplings derived from SHAP, Integrated Gradients, Sensitivity Maps,  
Gradient Fields, and H3 Attribution layers.

Hydrology spatial attribution maps answer:  
> **“Where on the landscape does the AI model derive its hydrologic understanding?”**

</div>

---

## 📘 1. Overview

Hydrology AI models leverage rich spatiotemporal predictors:

- CAMS atmospheric fields (precipitation proxies, aerosols, humidity, wind, temp)  
- Soil moisture, soil type, hydric soils  
- DEM + terrain derivatives  
- Landcover transitions  
- Watershed geometry (HUC4–HUC12)  
- H3 hex partitions for privacy & multi-scale semantics  

Spatial attribution helps explain:

- Watershed-critical zones of influence  
- Storm-path sensitivity  
- Terrain- and landform-driven hydrology responses  
- Coupled climate–hydrology dynamics  
- Temporal evolution of hydrologic influence  
- CARE-governed safe generalization in sensitive tribal watersheds

---

## 🗂️ 2. Directory Layout (Emoji-Prefix Standard)

~~~text
docs/pipelines/ai/explainability/hydrology/spatial-attribution/
├── 📄 README.md
│
├── 🧠 templates/                              # Hydrology spatial attribution templates
│   ├── 🌍 global_spatial_template.parquet
│   ├── 📍 local_spatial_template.parquet
│   ├── 🧭 h3_spatial_template.parquet
│   ├── 🔬 sensitivity_spatial_template.parquet
│   └── 🕒 temporal_spatial_template.parquet
│
├── 🌐 stac/                                   # STAC templates
│   ├── 📄 item-template.json
│   └── 📄 collection-template.json
│
├── 🔗 lineage/                                # PROV-O + OpenLineage binding templates
│   ├── 🧾 prov-template.json
│   └── 📡 ol-template.json
│
├── 🧪 validation/                              # Spatial explainability validators
│   ├── 📄 validate-watershed.md
│   ├── 📄 validate-spatial-integrity.md
│   ├── 📄 validate-h3.md
│   ├── 📄 validate-temporal.md
│   └── 📄 validate-metadata.md
│
└── 📊 examples/                               # Example hydrology spatial attribution runs
    ├── 📁 global/
    ├── 📁 local/
    ├── 📁 h3/
    └── 📁 temporal/
~~~

---

## 🧬 3. Hydrology Spatial Attribution Standards (v11)

Each spatial attribution artifact MUST include:

| Field | Required | Description |
|-------|----------|-------------|
| `model:version` | ✔ | Hydrology AI model version |
| `kfm:domain` | ✔ | `"hydrology"` |
| `kfm:explainability_method` | ✔ | shap, ig, sensitivity, gradient, spatial-attribution |
| `kfm:input_variables` | ✔ | Climate/soil/terrain/hydro predictors |
| `watershed_id` | ✔ | HUC-level watershed ID |
| `datetime` | ✔ | Event/inference timestamp |
| `CRS` | ✔ | EPSG:4326 unless H3 |
| `kfm:h3_res` | conditional | Required if using H3 explainability |
| `kfm:sensitivity_flag` | ✔ | CARE/sovereignty handling for tribal/wetland/watershed areas |
| `kfm:energy_wh` | ✔ | Compute energy usage |
| `kfm:carbon_gco2e` | ✔ | Environmental impact |
| `spatial_extent` | ✔ | Bounding box or watershed geometry |

Supported output forms:

- **Global Spatial Attribution** (watershed-scale aggregate)  
- **Local Spatial Attribution** (event-level attribution maps)  
- **Temporal Spatial Attribution** (storm windows, flood evolution)  
- **H3 Spatial Attribution** (hex-based privacy-aware maps)  
- **Sensitivity Maps**  

---

## 🧪 4. Validation Requirements (v11)

### ✔ Spatial Integrity  
- Attribution grid aligns with watershed geometry  
- CRS/H3 metadata consistent  
- No NaN/inf  
- Watershed clipping preserves topology  

### ✔ Metadata Completeness  
- Model version pinned  
- Required STAC fields present  
- CAMS/soil/terrain inputs listed  
- Watershed identifier valid  

### ✔ CARE & Sovereignty  
- Masking or H3 elevation required for sensitive hydrologic areas  
- No reversible coordinates for protected tribal watersheds  
- CARE flag required  

### ✔ Sustainability  
- Energy & carbon within hydrology explainability budget  
- Telemetry linked in STAC + lineage  

Validation failures → rollback (Reliability Layer v11).

---

## 🌐 5. STAC Templates

Spatial attribution MUST produce a STAC Item including:

- `datetime`  
- `watershed_id`  
- `model:version`  
- `kfm:domain="hydrology"`  
- `kfm:explainability_method`  
- `kfm:energy_wh`  
- `kfm:carbon_gco2e`  
- `kfm:h3_res` (if used)  
- Attribution assets (parquet/png/json)  
- Provenance links  

Stored in:

~~~text
stac/item-template.json
stac/collection-template.json
~~~

---

## 🔗 6. Provenance (PROV-O + OpenLineage)

Each hydrology spatial attribution run MUST include:

### PROV-O  
- `prov:Activity` — spatial explainability run  
- `prov:used` — CAMS + hydrology + terrain/soil datasets  
- `prov:generated` — spatial attribution artifacts  
- `prov:wasAssociatedWith` — pipeline agent  

### OpenLineage  
- runId  
- inputs  
- outputs  
- spatial metadata  
- energy/carbon  

Stored under:

~~~text
lineage/prov-template.json
lineage/ol-template.json
~~~

---

## 📡 7. Telemetry (OTel v11)

Each run MUST export:

- `kfm.expl_method="hydrology-spatial-attribution"`  
- `kfm.expl_energy_wh`  
- `kfm.expl_carbon_gco2e`  
- `kfm.rows_processed`  
- `kfm.expl_latency_ms`  
- CPU/GPU utilization  
- Output cell count (grid/H3)

Telemetry is attached to STAC + lineage and included in release-level bundles.

---

## 🔮 8. Story Node Integration (Focus Mode v3)

Hydrology spatial attribution explains:

- Watershed response zones  
- Climate–hydrology coupling  
- Terrain-forcing effects  
- Sensitivity distributions  
- Temporal storm evolution  
- CARE notes  
- Provenance chain + sustainability footprint  

Story Nodes help produce hydrology explainability narratives across KFM.

---

## 🧭 9. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.3 | 2025-11-29 | Initial v11 hydrology spatial attribution template; lineage + CARE integrated. |

---

<div align="center">

💧🗺️ **Kansas Frontier Matrix — Hydrology Spatial Attribution (v11.2.3)**  
Watershed-Aware · Climate-Coupled · Explainable · FAIR+CARE  

[📘 Docs Root](../../../../../..) · [🧠 Hydrology Explainability](../README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>