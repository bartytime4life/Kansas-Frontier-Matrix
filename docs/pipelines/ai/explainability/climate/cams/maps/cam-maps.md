---
title: "🌍 KFM v11 — CAMS Climate Explainability Maps (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/ai/explainability/climate/cams/maps/cam-maps.md"
version: "v11.2.3"
last_updated: "2025-11-29"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate AI Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.3/manifest.zip"
attestation_ref: "../../../../../../../releases/v11.2.3/slsa-attestation.json"
signature_ref: "../../../../../../../releases/v11.2.3/signature.sig"

telemetry_ref: "../../../../../../../releases/v11.2.3/cams-explainability-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/ai-explainability-cams-maps-v11.json"
energy_schema: "../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

doc_kind: "Explainability Module"
intent: "cams-ai-explainability-maps"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Respectful · Climate Transparency"

classification: "Public (Governed)"
sensitivity: "Low"
machine_extractable: true
jurisdiction: "United States · Kansas"
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# 🌍 **KFM v11 — CAMS Climate Explainability Maps**  
`docs/pipelines/ai/explainability/climate/cams/maps/cam-maps.md`

**Purpose**  
Provide the governed v11 standard for **explainability maps** derived from **CAMS climate model outputs**,  
including SHAP/attribution landscapes, global/temporal influence maps, energy-aware rendering,  
and provenance-linked visualization metadata.

Explainability maps allow KFM users to understand **why** CAMS-based AI climate predictions behave as they do.

</div>

---

## 📘 1. Overview

CAMS (Copernicus Atmosphere Monitoring Service) climate layers feed several KFM AI climate pipelines  
(e.g., PM2.5 inference, ozone prediction, smoke transport explainers).

To ensure transparency:

- Raw climate fields → **model inputs**
- AI decision surfaces → **explainability maps**
- Attribution signals → **SHAP / Gradient Surfaces**
- Metadata → **STAC + PROV-O**
- Energy/carbon → **OTel telemetry**

This module defines how climate explainability maps are generated, validated, versioned,  
and published inside the KFM system.

---

## 🧠 2. Explainability Map Types (CAMS AI)

### 2.1 SHAP Mean Attribution Maps  
- Global attribution magnitude per CAMS variable  
- Temporal aggregation options: hourly/daily/monthly  
- Multiscale H3 overlays available (R3–R7)

### 2.2 Local Attribution Tiles  
- SHAP-per-pixel (or per-H3 cell) for a given prediction slice  
- Typically used for event-scale analysis (smoke, ozone exceedances)

### 2.3 Sensitivity Maps  
- Model-response maps: ∂Y/∂X per CAMS driver  
- Generated through perturbation or surrogate interpreters

### 2.4 Gradient Fields  
- Explainable-gradient maps for CNN-based climate downscalers  
- Used mainly in climate-risk explainability

Each map type must include explicit **model version**, **input fields**, and  
**explainability method** (shap, grad, surrogate, perturbation).

---

## 🧪 3. Validation Rules (v11)

Explainability maps must pass:

### ✔ Metadata Validation  
- Required STAC fields  
- Temporal extent must align with CAMS input window  
- Model version pinned  
- Geographic CRS = EPSG:4326

### ✔ Numerical Validation  
- SHAP values finite, not NaN/inf  
- Normalized global SHAP sum ± tolerance  
- Local attribution tiles match expected shape (H3 or lat/lon grid)

### ✔ Governance Validation  
- CARE: no exposure of sensitive ecological or tribal areas  
- Provenance: complete lineage (model + input + explainability run)  
- Sustainability: energy/carbon < pipeline budgets

Validation failures → automatic rollback (Reliability Layer v11).

---

## 🗂️ 4. Directory Layout (Emoji-Prefix Standard)

~~~text
docs/pipelines/ai/explainability/climate/cams/maps/
├── 📄 cam-maps.md                    # This file
├── 🧠 global/                        # Global SHAP magnitude maps
│   ├── 🌍 shap_global.parquet
│   └── 🌐 stac/
│       └── item-global.json
│
├── 📍 local/                         # Local attribution maps
│   ├── 📡 shap_local_*.parquet
│   └── 🌐 stac/
│       └── items/
│
├── 🔬 sensitivity/                   # Sensitivity & gradient maps
│   ├── 🔬 sens_*.parquet
│   └── 🌐 stac/
│       └── items/
│
└── 🔗 lineage/                       # Provenance + model metadata
    ├── 🧾 prov-template.json
    └── 📄 model-metadata.json
~~~

---

## 🌐 5. STAC Metadata (Required Fields)

Every explainability map MUST publish a STAC Item with:

| Field | Description |
|-------|-------------|
| `datetime` | Representative timestamp of the CAMS inference window |
| `model:version` | Version of CAMS-driven AI model |
| `kfm:explainability_method` | shap, grad, perturbation, surrogate |
| `kfm:h3_res` | If H3 generalization applied |
| `kfm:sensitivity_flag` | CARE-sensitive location handling |
| `kfm:energy_wh` | Compute energy estimate |
| `kfm:carbon_gco2e` | Carbon estimate |
| Assets | Parquet data, visualizations, provenance bundle |

Example item stored under **`stac/item-template.json`**.

---

## 🔧 6. Provenance & Lineage (OpenLineage + PROV-O)

Each explainability run MUST emit:

- `openlineage_run_id`  
- Inputs (CAMS layers + derived fields)  
- Outputs (SHAP global/local maps)  
- Activity graph (explainability pipeline nodes)  
- Associated CAMS model version  
- Energy/carbon metrics  

All metadata MUST be written into:

~~~text
docs/pipelines/ai/explainability/climate/cams/maps/lineage/
~~~

---

## 📡 7. Telemetry (OTel)

Each explainability run emits:

- `kfm.rows_processed`  
- `kfm.expl_energy_wh`  
- `kfm.expl_carbon_gco2e`  
- `kfm.expl_method` (shap/grad/etc.)  
- `kfm.expl_cells` (count)  
- `kfm.expl_latency_ms`  

Telemetry exported via OTLP/gRPC and attached to the STAC Item.

---

## 📈 8. Rendering Guidance (Optional)

Explainability maps often require:

- Per-cell normalization  
- Signed SHAP color mapping  
- Sequential color ramps for sensitivity  
- Divergent ramps for SHAP ± contribution  
- Multi-scale views (H3 R3–R7)  
- Event-to-global zoom storytelling in Focus Mode  

---

## 🔮 9. Story Node Integration (Focus Mode v3)

Each explainability output should create a **Story Node** describing:

- Influential climate drivers  
- Spatial distribution of attribution  
- Model reasoning shifts  
- Sensitivity hotspots  
- Temporal evolution across CAMS runs  
- FAIR+CARE notes for impacted regions  

---

## 🧭 10. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.3 | 2025-11-29 | Initial explainability maps spec for CAMS climate pipelines; v11-aligned; emoji-layout applied. |

---

<div align="center">

🌍 **Kansas Frontier Matrix — CAMS Climate Explainability Maps (v11.2.3)**  
Transparent · Interpretable · FAIR+CARE-Aligned · Energy-Aware  

[📘 Docs Root](../../../../../..) · [🤖 AI Pipelines](../../../README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>