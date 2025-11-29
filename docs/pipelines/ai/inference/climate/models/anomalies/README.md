---
title: "🌡️📉🤖 KFM v11.2.2 — Climate Anomaly Models (Deviation Layers · Deterministic · XAI-Ready)"
path: "docs/pipelines/ai/inference/climate/models/anomalies/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
status: "Active / Enforced"
content_stability: "stable"
doc_kind: "Model Subcategory · Climate Anomalies"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.2/climate-inference-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/ai-climate-inference-v11.2.2.json"

governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
data_contract_ref: "../../../../../../contracts/data-contract-v3.json"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Medium-Risk"
sensitivity: "Climate-Anomaly-Models"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "climate-anomalies"
  - "deviation-fields"
  - "long-term-normals"
  - "bias-detection"
  - "xai-ready"
  - "seed-locked-inference"

scope:
  domain: "pipelines/ai/inference/climate/models/anomalies"
  applies_to:
    - "climatology-baseline"
    - "anomaly-diff-models"
    - "xai-anomaly-explanations"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_directory_layout_section: true
requires_purpose_block: true
requires_version_history: true
requires_governance_links_in_footer: true
diagram_profiles:
  - "mermaid-flowchart-v1"
---

<div align="center">

# 🌡️📉🤖 **Climate Anomaly Models — KFM v11.2.2**  
`docs/pipelines/ai/inference/climate/models/anomalies/README.md`

**Purpose**  
Define and govern the anomaly-generation models that compute **deviations from climatology** for use in realtime inference, statewide anomaly maps, hazard analyses, and Focus Mode v3 narratives.

</div>

---

## 📘 Overview

Climate anomaly models produce **deviation surfaces** by comparing realtime or forecast fields against:

- PRISM normals  
- NCEI 30-year climate normals  
- Downscaled HRRR/ERA5 baselines  
- Long-term statewide climatologies  
- Model-generated climatology (if selected)  

Anomalies are primary drivers for:

- Heatwave detection  
- Cold spell analysis  
- Rainfall departure maps  
- Drought onset signals  
- Soil moisture deficit/surplus  
- Hazard risk chains (fire weather, flooding)  
- Story Node v3 anomaly-context text  
- Focus Mode v3 in-situ anomaly overlays  

Models MUST be:

- Deterministic  
- FAIR+CARE aligned  
- XAI-compatible  
- STAC-XAI v11 publishable  
- CRS/vertical-axis explicit  
- Provenance-rich (PROV-O)  

---

## 🗂️ Directory Layout (v11.2.2)

    docs/pipelines/ai/inference/climate/models/anomalies/
        📄 README.md                # This file
        📄 anomaly-baseline.md      # Climatology baseline description
        📄 anomaly-diff-model.md    # Anomaly-generation model card

---

## 🧩 Anomaly Model Types

### 🧱 Baseline Climatology Model  
Defines the reference against which anomalies are computed.

Options:  
- Static 30-yr normals (1991–2020)  
- Rolling multi-decadal climatology  
- Downscaled historical reanalysis  

### 📉 Anomaly Difference Model  
Computes Δ(field) = realtime_field – baseline_climatology.

Supports:  
- Temperature anomalies  
- Dewpoint anomalies  
- Precipitation departures  
- Soil moisture deviations  
- Fire-weather indices  
- Energy-balance anomaly fields  

---

## 🧬 Anomaly Pipeline Flow

```mermaid
flowchart TD
    A[Realtime Climate Input] --> B[Baseline Climatology]
    B --> C[Seed-Locked Δ Computation]
    A --> C
    C --> D[XAI Interpretation]
    D --> E[STAC-XAI Metadata Assembly]
    E --> F[Telemetry + PROV-O Lineage]
```
<!-- mermaid-end -->

---

## 🎛 Model Requirements

Each anomaly model card MUST include:

- Baseline definition (dataset, period)  
- Variables included  
- Preprocessing rules  
- Deterministic (seed-locked) diff computation  
- CRS + vertical-axis metadata  
- Metrics: MBE, RMSE, MAE, corr  
- Energy + carbon telemetry  
- FAIR+CARE review  
- Sovereignty-safe evaluation  
- XAI compatibility (SHAP, IG)  
- STAC-XAI asset metadata  

---

## 🧪 CI Requirements

CI MUST verify:

- Model-card schema validity  
- Baseline metadata completeness  
- Deterministic reproduction  
- Variable consistency  
- FAIR+CARE compliance  
- Sovereignty safety  
- XAI fields present  
- CRS + vertical-axis fields present  
- STAC-XAI blocks valid  
- PROV-O lineage correct  

CI failure → 🚫 merge blocked.

---

## 🕰 Version History

| Version | Date       | Notes                                      |
| ------- | ---------- | ------------------------------------------ |
| v11.2.2 | 2025-11-28 | Initial anomaly model documentation added. |

---

<div align="center">

### 🔗 Footer

[⬅ Back to Climate Models](../README.md) ·  
[🌡️ Climate Pipeline Root](../../README.md) ·  
[🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

