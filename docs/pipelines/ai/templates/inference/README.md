---
title: "⚙️ KFM v11.2.2 — Inference Metadata Templates (Realtime · Batch · STAC · Provenance · FAIR+CARE)"
path: "docs/pipelines/ai/templates/inference/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Reliability Engineering · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Template Specification"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/ai-inference-templates-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/ai-inference-templates-v11.2.2.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
data_contract_ref: "../../../../contracts/data-contract-v3.json"

license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Medium-Risk"
sensitivity: "Inference-Metadata"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "inference-metadata"
  - "stac-inference"
  - "realtime-inference"
  - "batch-inference"
  - "ai-governance"
  - "provenance-jsonld"
  - "focus-mode-inference"

scope:
  domain: "ai-templates-inference"
  applies_to:
    - "inference-metadata"
    - "inference-stac"
    - "provenance-jsonld"
    - "batch-inference"
    - "realtime-inference"
    - "focus-mode"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_purpose_block: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true
requires_version_history: true

diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"
---

<div align="center">

# ⚙️ **KFM v11.2.2 — AI Inference Template Suite**  
`docs/pipelines/ai/templates/inference/README.md`

**Purpose:**  
Provide the **canonical metadata templates** for all AI inference pipelines in KFM — including realtime, batch, hybrid, and Focus Mode v3 inference.  
Templates define standard **inference JSON-LD**, **STAC v11 inference Items**, **provenance links**, **FAIR+CARE compliance**, **energy/carbon metadata**, and **explainability attachments**.

</div>

---

## 📘 Overview

This directory contains the **official inference metadata templates** for:

- Realtime inference (API + streaming)  
- Batch inference (nightly / scheduled DAGs)  
- Hybrid inference (batch warm-start → realtime)  
- Focus Mode v3 semantic inference  
- STAC v11 inference outputs  
- JSON-LD provenance blocks  
- FAIR+CARE masking metadata  
- Explainability (XAI) references  

These templates guarantee:

- Deterministic + reproducible inference  
- Machine-extractable metadata  
- Story Node & Focus Mode v3 compatibility  
- Energy/Carbon telemetry inclusion  
- CARE-safe spatial and textual masking  
- STAC v11 compliant dataset items  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/templates/inference/
    ├── 📄 README.md                                   # This file
    │
    ├── 📁 jsonld/                                      # Inference JSON-LD scaffolding
    │   ├── 📄 inference-metadata-template.jsonld       # Canonical inference metadata
    │   ├── 📄 inference-provenance-template.jsonld     # PROV-O compliant lineage
    │   └── 📄 inference-context-template.jsonld        # Focus Mode + Story Node integration
    │
    ├── 📁 stac/                                        # STAC templates for inference outputs
    │   ├── 📄 stac-inference-item-template.json        # STAC Item for inference products
    │   └── 📄 stac-asset-template.json                 # Template for COG/GeoParquet assets
    │
    ├── 📁 batch/                                       # Batch inference templates
    │   ├── 📄 batch-inference-metadata.json
    │   ├── 📄 batch-provenance.jsonld
    │   └── 📄 batch-telemetry-template.json
    │
    ├── 📁 realtime/                                    # Realtime inference templates
    │   ├── 📄 realtime-inference-metadata.json
    │   ├── 📄 realtime-api-contract.yaml
    │   └── 📄 realtime-otel-span-template.json
    │
    └── 📁 mlops/                                       # Drift + deployment + monitoring
        ├── 📄 drift-monitoring-template.json
        ├── 📄 inference-fallback-policy.md
        └── 📄 rollout-config-template.yaml

---

## ⚙️ Template Categories

### 1. 🚀 Realtime Inference Templates  
Provide:

- API contract  
- Input validation schema  
- Output JSON-LD  
- Care mask / privacy rules  
- OTel span attributes  
- STAC-sidecar generation rules  

Realtime inference must be deterministic and governed.

---

### 2. 📆 Batch Inference Templates  
Define:

- Batch inference manifest  
- Upstream STAC dataset references  
- Provenance chain (`prov:*`)  
- Evaluation checks  
- Energy/Carbon telemetry  

Batch inference outputs **MUST** produce STAC Items for geospatial results.

---

### 3. 🧭 Focus Mode v3 Inference Templates  
These templates govern:

- Narrative context windows  
- Evidence fusion blocks  
- Masked semantic windows  
- JSON-LD narrative stubs  

Focus Mode templates include:

- `focus:entity_id`  
- `focus:evidence` (masked)  
- `focus:timeline`  
- `focus:spatial_mask`  

---

### 4. 🧬 Hybrid Inference Templates  
Support pipelines that blend:

- Historical batch inference  
- Realtime incremental inference  
- Contextual overlays for Focus Mode  

Hybrid templates define:

- Inference session IDs  
- Two-tier provenance  
- Cross-domain STAC links  

---

### 5. 📝 Provenance Templates  
All inference bundles must include:

- `prov:used`  
- `prov:wasGeneratedBy`  
- `prov:generatedAtTime`  
- Hash-based lineage for reproducibility  
- Training + model-version fingerprints  

---

## 📡 STAC v11 Integration Requirements

Inference STAC Items MUST include:

- `kfm:inference:model_name`  
- `kfm:inference:model_version`  
- `kfm:inference:method`  
- `kfm:input_items` (array of STAC IDs)  
- CRS + vertical metadata  
- Bounding boxes  
- Asset checksums (`checksum:multihash`)  
- Energy/Carbon metadata  
- Explainability pointers (`kfm:explainability:*`)  

Geospatial outputs (COGs, GeoParquet) MUST be published.

---

## 🧠 Explainability (XAI) Integration

Inference templates embed XAI metadata:

- SHAP global & local vectors  
- CAM/saliency overlays  
- Integrated Gradients  
- Attribution drivers  
- CARE-masked XAI fields  

All explainability MUST be JSON-LD and STAC-compatible.

---

## 🔐 FAIR+CARE Requirements

All inference templates enforce:

- H3 generalization for protected locations  
- No speculation or identity inference  
- Cultural/heritage masking rules  
- Licensed dataset declarations  
- CARE scope fields (`care:*`)  
- Usage restrictions  
- Sovereignty alignment  

Non-compliant inference → **CI & governance block**.

---

## 🧪 Testing Requirements

Templates must pass:

- JSON-LD schema validation  
- STAC extension schema validation  
- FAIR+CARE compliance tests  
- Deterministic hashing tests  
- Inference reproducibility checks  
- Drift testing logic (MLOps)  

Failing any → **PR blocked**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                     |
|----------|------------|-----------------------------------------------------------|
| v11.2.2  | 2025-11-28 | First v11.2.2-compliant inference template suite          |
| v11.0.0  | 2025-11-15 | Initial inference template directory                      |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to AI Template Index](../README.md) · [⚙️ Inference Layer](../../inference/README.md) · [🏛 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

