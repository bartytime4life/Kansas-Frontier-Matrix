---
title: "🌡️⬇️🤖 KFM v11.2.2 — Climate Downscaling Models (High-Resolution Inference · Deterministic · XAI-Ready)"
path: "docs/pipelines/ai/inference/climate/models/downscaling/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
status: "Active / Enforced"
content_stability: "stable"
doc_kind: "Model Subcategory · Downscaling"

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
sensitivity: "Climate-Downscaling-Models"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "downscaling-models"
  - "climate-high-resolution"
  - "unet-downscaler"
  - "transformer-downscaler"
  - "deterministic-seed-locked"
  - "xai-ready-models"

scope:
  domain: "pipelines/ai/inference/climate/models/downscaling"
  applies_to:
    - "unet-downscaler.md"
    - "transformer-downscaler.md"
    - "deterministic-downscaling"
    - "xai-compatible-downscaling"

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

# 🌡️⬇️🤖 **Climate Downscaling Models — KFM v11.2.2**  
`docs/pipelines/ai/inference/climate/models/downscaling/README.md`

**Purpose**  
Define, govern, and validate the downscaling models supporting **Climate AI inference**, producing **high-resolution climate surfaces** integrated across the KFM pipeline, Story Node v3, and Focus Mode v3.

</div>

---

## 📘 Overview

Downscaling models transform **coarse atmospheric or land-surface grids** into **fine-scale surfaces** used for statewide realtime and batch inference.

Used in:

- Realtime map tile generation  
- Batch statewide reanalysis  
- Derived hazard drivers (CAPE, CIN, SRH, LLJ)  
- Climate/meteorology-linked Story Nodes  
- Focus Mode v3 dynamic narratives  
- FAIR+CARE-compliant climate provenance  
- STAC-XAI v11 catalog publishing  

All models MUST be:

- 🔒 **Deterministic** (strict seed-lock)  
- 🧠 **XAI-ready** (SHAP, IG, CAM)  
- 🌍 **CRS + vertical axis explicit**  
- 🪶 **Lightweight + reproducible**  
- 📦 **STAC v11 + DCAT v11 compliant**  
- ⚖️ **FAIR+CARE + sovereignty aligned**  

---

## 🗂️ Directory Layout (v11.2.2)

*(Indented block is fully safe — no box break, no parser break)*

    docs/pipelines/ai/inference/climate/models/downscaling/
        📄 README.md                    # This file
        📄 unet-downscaler.md           # U-Net model card
        📄 transformer-downscaler.md    # Transformer model card

---

## 🧩 Model Types

### 🧱 U-Net Downscaler  
- Encoder/decoder  
- Strong spatial fidelity  
- Good for temperature, RH, soil moisture  
- CAM + IG support  
- Seed-locked determinism  

### 🔮 Transformer Downscaler  
- Temporal/context-aware  
- Multivariate downscaling  
- SHAP + IG compatible  
- Stable non-autoregressive tile inference  

---

## 🧬 Downscaling Pipeline Flow

```mermaid
flowchart TD
    A[Coarse Climate Input] --> B[Load Downscaling Model]
    B --> C[Seed-Locked Inference]
    C --> D[High-Resolution Grid]
    D --> E[XAI Processing]
    E --> F[STAC-XAI Metadata Assembly]
    F --> G[Telemetry + PROV-O Lineage]
```
<!-- mermaid-end -->

---

## 🎛 Model Requirements

Cards MUST specify:

- Architecture + hyperparameters  
- Variables (input + output)  
- Preprocessing + normalization  
- Seed-lock parameters  
- CRS (horizontal + vertical)  
- Training datasets + licensing  
- Metrics: RMSE, MAE, bias, corr  
- XAI compatibility (SHAP/IG/CAM)  
- Energy (Wh) + Carbon (gCO₂e) telemetry  
- FAIR+CARE + sovereignty assessment  
- STAC-XAI data asset description  
- Deterministic inference test vector  

---

## 🧪 CI Validation

CI MUST enforce:

- Schema correctness (model card JSON schema)  
- Deterministic reproduction via test vector  
- FAIR+CARE compliance  
- Sovereignty constraints  
- XAI integration fields  
- CRS + vertical metadata  
- STAC-XAI metadata blocks  
- PROV-O lineage  

CI failure → 🚫 merge blocked.

---

## 🕰 Version History

| Version | Date       | Notes                                              |
| ------- | ---------- | -------------------------------------------------- |
| v11.2.2 | 2025-11-28 | Initial release of downscaling model documentation |

---

<div align="center">

### 🔗 Footer

[⬅ Back to Climate Models](../README.md) ·  
[🌡️ Climate Pipeline Root](../../README.md) ·  
[🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
