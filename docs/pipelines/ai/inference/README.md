---
title: "⚙️ KFM v11.2.2 — AI Inference Pipelines (Realtime · Batch · Deterministic · FAIR+CARE)"
path: "docs/pipelines/ai/inference/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"
review_cycle: "Quarterly · FAIR+CARE Council · Reliability Engineering"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Pipeline Layer"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.2/ai-inference-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/ai-inference-v11.2.2.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
data_contract_ref: "../../../contracts/data-contract-v3.json"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

care_label: "Public · Medium-Risk"
fair_category: "F1-A1-I1-R1"
sensitivity: "AI-Inference"
sensitivity_level: "Medium"
public_exposure_risk: "Moderate"

semantic_intent:
  - "ai-inference"
  - "batch-inference"
  - "realtime-inference"
  - "deterministic-ai"
  - "stac-output"
  - "focus-mode-integration"

scope:
  domain: "ai-inference"
  applies_to:
    - "climate"
    - "hydrology"
    - "hazards"
    - "embeddings"
    - "focus-mode"
    - "stac-outputs"
    - "graph-writes"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"
---

<div align="center">

# ⚙️ **KFM v11.2.2 — AI Inference Pipelines**  
`docs/pipelines/ai/inference/README.md`

**Purpose:**  
Define the **deterministic, reproducible, governed inference layer** for all AI/ML models in the Kansas Frontier Matrix.  
Covers **realtime inference**, **batch inference**, **STAC-producing inference**, and **Focus Mode v3 semantic inference**, with strict **FAIR+CARE**, **PROV-O**, and **KFM-STAC v11** alignment.

</div>

---

## 📘 Overview

The **inference layer** transforms validated KFM datasets into:

- Climate forecasts  
- Streamflow/reservoir predictions  
- Hazard/wildfire risk outputs  
- Embeddings for semantic search  
- Focus Mode v3 contextual reasoning  
- Story Node v3 narratives  
- Geospatial derivative layers (maps, rasters, overlays)  

Inference pipelines support:

- **Realtime inference** (API + streaming)  
- **Batch inference** (scheduled autonomous DAGs)  
- **Hybrid inference** (batch warm-start → realtime refinement)  

All results must be:

- Deterministic (seed-locked)  
- Reproducible  
- Versioned  
- FAIR+CARE aligned  
- Published as STAC v11 Items if geospatial  
- Lineage-complete (OpenLineage / PROV-O)  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/inference/
    ├── 📄 README.md                              # This file
    │
    ├── 📁 climate/                               # Climate inference (forecasts, anomalies)
    │   ├── 📄 forecast-batch.md
    │   └── 📄 realtime-climate.md
    │
    ├── 📁 hydrology/                             # Streamflow, soil moisture, reservoir level models
    │   ├── 📄 streamflow-inference.md
    │   └── 📄 reservoirs-inference.md
    │
    ├── 📁 hazards/                               # Wildfire + severe-weather inference
    │   ├── 📄 wildfire-probability.md
    │   └── 📄 severe-weather-risk.md
    │
    ├── 📁 embeddings/                            # Embeddings for semantic search + NLP/graph tasks
    │   ├── 📄 text-embeddings.md
    │   └── 📄 geo-embeddings.md
    │
    └── 📁 focus/                                 # Focus Mode v3 inference engines
        ├── 📄 context-reasoner.md
        └── 📄 narrative-builder.md

---

## ⚙️ Inference Pipeline Classes

### 1. 🚀 Realtime Inference  
Used for API-driven or streaming tasks:

- Climate nowcasting  
- Hazard/wildfire probability  
- Entity/embedding queries  
- Focus Mode semantic reasoning  

**Requirements:**

- <50ms model load (pre-warmed)  
- Deterministic for identical inputs  
- Input validation + CARE masking  
- OTel spans for each inference call  
- Graph-safe outputs (Neo4j entities)  
- Optional STAC Items for map-layer outputs  

---

### 2. 📆 Batch Inference  
Used for nightly or scheduled inference DAGs:

- Climate anomalies  
- Streamflow & hydrological indicators  
- Erosion/sediment predictions  
- DEM-derived hazard indicators  
- Batch embeddings  

**Requirements:**

- Seed-locked reproducibility  
- Full OpenLineage job/timeline chain  
- STAC Items for geospatial surfaces  
- XAI mandatory (SHAP / IG / CAMs)  
- Must write energy/carbon telemetry  

---

### 3. 🧭 Focus Mode v3 Semantic Inference  
Focus Mode inference is an **AI reasoning pipeline** that synthesizes:

- Graph entities (Neo4j)  
- STAC metadata  
- Time windows  
- Spatial footprints  
- Explainability drivers  
- CARE masks  

It outputs structured:

- Focus JSON  
- Story Node snapshots  
- Narrative windows  

**STRICT RULES:**

- Must NOT hallucinate or speculate  
- Must cite provenance for ALL statements  
- Must honor CARE masking + generalization rules  
- All outputs must be deterministic at fixed seed  

---

### 4. 🧬 Cross-Domain Inference Pipelines  
Examples:

- Soil × terrain × hydrology suitability  
- Climate × vegetation × hazard projections  
- Archaeology affordance overlays (DEM-driven)  
- Weather × trail networks for historic simulation  

Cross-domain inference MUST:

- Use STAC Collections as input  
- Register upstream STAC Item IDs  
- Emit multi-source PROV-O chains  
- Log XAI factors used in fusion  

---

## 📡 STAC Publishing Requirements

All **geospatial inference outputs** must be published as STAC v11 Items with:

- `kfm:inference:method`  
- `kfm:model_version`  
- `kfm:explainability:*`  
- `kfm:input_items` (array of STAC IDs)  
- PROV-O fields (`prov:used`, `prov:wasGeneratedBy`)  
- CRS + vertical datum  
- Full bounding boxes  
- Asset checksums (`checksum:multihash`)  

Outputs MAY include:

- GeoParquet tiles  
- COG rasters (slope, hazard grids, risk maps)  
- Vector overlays (predicted features, clusters)  
- Story Node graphs  

---

## 🧠 Explainability Layer Requirements

Inference pipelines MUST include:

- SHAP (global + local) for tabular/structured models  
- CAMs or saliency maps for deep geospatial models  
- Integrated Gradients for DEM/terrain neural nets  
- CARE masking for heritage-sensitive features  
- JSON-LD XAI exports (`kfm:explainability:*`)  

Outputs feed:

- STAC  
- Story Nodes  
- Focus Mode v3 evidence panels  
- Internal audit dashboards  

---

## 🔐 FAIR+CARE Rules

Inference MUST:

- Avoid revealing exact coordinates of protected archaeology  
- Apply masking, generalization, or abstraction  
- Document training data + limitations  
- Include governance citations  
- NEVER speculate on tribal identity or protected cultural knowledge  

Any violation → **automatic block** in CI and control-plane.

---

## 🧪 Testing Requirements

Inference pipelines MUST pass:

- Unit tests  
- Integration tests (DAG + ETL + model)  
- Deterministic seed-locked regression tests  
- XAI stability tests  
- FAIR+CARE rule tests  
- STAC validation  
- Schema tests (vertical axis, CRS, DCAT mappings)  

ALL failures → PR blocked.

---

## 🕰 Version History

| Version  | Date       | Notes                                                        |
|----------|------------|--------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Full v11.2.2 uplift; telemetry update; FAIR+CARE refinements |
| v11.0.0  | 2025-11-22 | Initial AI inference layer specification                     |

---

<div align="center">

### 🔗 Footer  
[⬅ AI Pipelines Index](../README.md) · [📘 Standards](../../../standards/README.md) · [🔐 FAIR+CARE](../../../standards/faircare/FAIRCARE-GUIDE.md)

</div>
