---
title: "🌿 Kansas Frontier Matrix — Archaeology AI Interpretations: Environmental Affordances (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/results/ai-interpretations/clusters/environmental-affordances/README.md"
version: "v11.0.0"
last_updated: "2025-11-25"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archaeology-env-affordances-v11.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
---

<div align="center">

# 🌿 Archaeology AI Interpretations — Environmental Affordances  
### docs/analyses/archaeology/results/ai-interpretations/clusters/environmental-affordances/README.md

**Purpose:**  
Provide the KFM-v11 certified environmental-affordance interpretations derived from archaeological AI cluster analysis.  
These outputs feed Story Node v3, Focus Mode v3, Neo4j KG ingestion, environmental overlays, and cross-temporal reasoning.  
All narrative, spatial, temporal, and metadata elements are FAIR+CARE compliant and fully CI-validated.

</div>

---

# 🧭 1. Overview

Environmental Affordance Interpretation is the KFM v11 method for explaining how clusters relate to  
**resources, constraints, and environmental opportunities** present in specific archaeological contexts.

This directory contains:

- Environmental-affordance summary narratives  
- Numeric affordance vectors  
- PROV-O lineage records  
- STAC Items describing spatiotemporal extents  
- DCAT metadata for discovery  
- Graph-safe Story Node–ready JSON-LD bindings  

These outputs allow KFM to generate high-fidelity environmental explanations that integrate with:

- Story Node v3 (narrative linking engine)  
- Focus Mode v3 (dynamic contextual reasoning)  
- GIS overlays (DEM, soils, hydrology, vegetation, hazards)  
- Time-aligned environmental reconstruction  
- AI explainability components (SHAP, vector attribution)

---

# 🌱 2. Environmental Affordance Model (v11 Standard)

All affordance interpretations are derived using the standardized **8-Domain v11 Affordance Schema**:

1. Hydrology Access (perennial vs. ephemeral water; floodplain dynamics)  
2. Topography & Slope (visibility, defensibility, travel efficiency)  
3. Soil Productivity (wild/managed plant potential; horticulture suitability)  
4. Lithic & Raw Materials (chert, sandstone, clay, timber availability)  
5. Faunal Habitat (bison, deer, small game, avian species)  
6. Seasonality Windows (aggregation/splitting periods; wintering sites)  
7. Mobility Corridors (river valleys, ridgelines, passes)  
8. Hazard Factors (drought exposure, flooding risk, wildfire corridors)

These domains produce:

- **Affordance Vector** → machine-readable environmental weighting  
- **Affordance Narrative** → human-readable contextual explanation  
- **Affordance Provenance** → reproducibility, lineage, and trustworthiness  

---

# 🛠️ 3. AI Pipeline (v11 Execution Flow)

Environmental affordance interpretations are generated using:

- Cluster geometry (H3 generalized where required by CARE)  
- DEM, slope, hydrology, soils, ecological rasters  
- Time-bounded environmental models (OWL-Time)  
- Focus Transformer v3 (environmental embedding stack)  
- SHAP explainability (domain-level attribution)  
- Deterministic seed-controlled inference  
- Automated CARE screening (Indigenous site protection)

Pipeline Steps:

1. Extract cluster footprint  
2. Sample environmental layers  
3. Compute affordance vector (8-domain schema)  
4. Execute Focus Transformer v3  
5. Generate narrative  
6. Validate CARE compliance  
7. Export Story Node JSON-LD + STAC Item  
8. Emit PROV-O lineage record  

The result is a fully reproducible, audit-ready interpretation.

---

# 🧪 4. Data & Metadata Standards

All files in this directory must adhere to:

- **STAC 1.0** (Items describing affordance extents and assets)  
- **DCAT 3.0** (dataset catalog metadata)  
- **JSON-LD** (Story Node v3 compatibility)  
- **CIDOC-CRM** (E53 Place, E3 Condition State, E5 Event mapping)  
- **GeoSPARQL** (geometry encoding)  
- **OWL-Time** (temporal intervals)  
- **PROV-O** (lineage: Entity → Activity → Agent)  
- **FAIR+CARE** (ethical, reproducible, respectful data handling)

These metadata systems ensure all affordance interpretations are:

- Searchable  
- Versioned  
- Interoperable  
- Graph-ready  
- Transparent  
- Ethically compliant  

---

# 📂 5. Directory Layout

~~~text
docs/analyses/archaeology/results/ai-interpretations/clusters/environmental-affordances/
├── README.md                       # This file
├── summaries/                      # Story Node–ready affordance narratives (JSON-LD)
├── vectors/                        # Numeric affordance vectors (8-domain schema)
├── provenance/                     # PROV-O lineage records for each interpretation
├── stac/                           # STAC Items describing spatiotemporal extents
└── metadata/                       # DCAT + JSON-LD metadata bindings
~~~

---

# 🗃️ 6. Required Artifacts (per Cluster)

Each cluster’s affordance interpretation MUST include:

### Summary Narrative (`*.summary.jsonld`)
- Environmental context  
- Subsistence implications  
- Mobility implications  
- Limiting factors  
- Seasonal dynamics  
- Uncertainty statement  
- CARE-screening applied flag  

### Affordance Vector (`*.vector.json`)
- Eight domain scores  
- Confidence intervals  
- Explainability breakdown  

### STAC Item (`*.stac.json`)
- Geometry  
- Bounding box  
- Datetime or time interval  
- Asset references  
- License and lineage  

### Provenance (`*.prov.json`)
- Source datasets  
- Processing stages  
- AI pipeline agents  
- Deterministic seeds  

---

# 🧩 7. Example Story Node Binding (v11 Minimal Form)

*(Shown using natural text — NOT a fenced code block to avoid box breakage.)*

Example fields for Story Node v3:

- id: kfm:affordance:cluster_07  
- type: story-node  
- title: Environmental Affordance Summary — Cluster 07  
- spacetime:  
  - geometry: Polygon / MultiPolygon  
  - when: start=1200-01-01, end=1450-01-01, precision=year  
- narrative:  
  - body: “Cluster 07 occupied a riparian–upland ecotone with access to perennial water...”  
- relations:  
  - rel: describes  
  - target: kfm:cluster:07  

This structure is required for downstream narrative integration.

---

# 🔒 8. FAIR+CARE Compliance

Environmental affordance data is **non-sensitive**, yet must follow:

- Indigenous land masking when spatially tied to cultural sites  
- No inference of tribal identity without explicit, verifiable evidence  
- Explicit uncertainty tagging on reconstructions  
- Licensing inheritance from all parent datasets  
- Full reproducibility and transparent provenance  

All automated AI outputs undergo CARE screening before publication.

---

# 🔧 9. Maintenance Rules

- Regenerate affordance outputs whenever cluster boundaries or environmental layers change.  
- Validate all STAC Items after DEM/soils/hydrology updates.  
- All changes must pass:  
  - Markdown structure linting  
  - FAIR+CARE audit  
  - STAC JSON schema validation  
  - KG ingest dry run  
  - Telemetry logging  

No document may be merged unless all checks pass.

---

# 🔗 10. Footer (Required v11 Three-Link Footer)

**← Back to Archaeology AI Interpretations**  
`../README.md`

**↑ Return to Archaeology Results Root**  
`../../README.md`

**🏛 Return to KFM Master Technical Reference**  
`/docs/reference/kfm_v11_master_documentation.md`