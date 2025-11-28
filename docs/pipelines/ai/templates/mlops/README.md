---
title: "🛠️ KFM v11.2.2 — MLOps Template Suite (Drift Monitoring · Retraining · Deployment · FAIR+CARE · Provenance)"
path: "docs/pipelines/ai/templates/mlops/README.md"
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
telemetry_ref: "../../../../../releases/v11.2.2/mlops-templates-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/mlops-templates-v11.2.2.json"
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
sensitivity: "MLOps-Metadata"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "mlops"
  - "deployment"
  - "drift-detection"
  - "retraining"
  - "telemetry"
  - "ai-governance"
  - "provenance"
  - "inference-policy"

scope:
  domain: "ai-templates-mlops"
  applies_to:
    - "drift-monitoring"
    - "retraining"
    - "deployment-configs"
    - "evaluation-schedules"
    - "telemetry"
    - "story-node-propagation"
    - "faircare-audits"

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

# 🛠️ **KFM v11.2.2 — MLOps Template Suite**  
`docs/pipelines/ai/templates/mlops/README.md`

**Purpose:**  
Provide the **canonical MLOps template set** governing deployment, drift detection, retraining workflows, monitoring, fallback policies, and inference governance for all AI/ML models in the Kansas Frontier Matrix.  
Ensures deterministic, FAIR+CARE-compliant, STAC-aligned lifecycle management across climate, hydrology, hazards, NLP, embeddings, and Focus Mode v3 models.

</div>

---

## 📘 Overview

These templates ensure:

- Deterministic AI deployment  
- Stable model versioning  
- Drift-resistant scoring  
- Continuous evaluation  
- FAIR+CARE enforcement  
- Story Node + Focus Mode narrative propagation  
- STAC v11 publishing of inference outputs  
- PROV-O traceability of retraining workflows  
- Energy/Carbon telemetry accountability  

The MLOps templates form the **operational backbone** of KFM’s AI systems.

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/templates/mlops/
    ├── 📄 README.md                                   # This file
    │
    ├── 📁 drift/                                      # Drift detection templates
    │   ├── 📄 drift-monitoring-template.json          # Statistical + semantic drift
    │   ├── 📄 drift-threshold-template.yaml           # Threshold policies (per domain)
    │   └── 📄 drift-alert-template.json               # Alert payload
    │
    ├── 📁 retraining/                                 # Retraining pipeline templates
    │   ├── 📄 retraining-policy-template.md           # Governance + triggers
    │   ├── 📄 retraining-config-template.yaml         # Training pipeline config
    │   └── 📄 retraining-provenance-template.jsonld   # PROV-O lineage
    │
    ├── 📁 deployment/                                 # Inference deployment templates
    │   ├── 📄 deployment-config-template.yaml         # Inference + serving config
    │   ├── 📄 rollout-policy-template.md              # Canary / blue-green / staged rollout
    │   └── 📄 rollback-template.md                    # Reversible rollback specification
    │
    ├── 📁 telemetry/                                  # Telemetry templates
    │   ├── 📄 inference-telemetry-template.json       # Inference metrics
    │   ├── 📄 energy-carbon-template.json             # Energy/Carbon v2 metadata
    │   └── 📄 lineage-span-template.json              # OTel/OpenLineage mapping
    │
    ├── 📁 evaluation/                                 # Continuous evaluation templates
    │   ├── 📄 evaluation-schedule-template.yaml       # Daily/weekly evaluation schedule
    │   ├── 📄 metric-registry-template.json           # Metric definitions
    │   └── 📄 golden-record-template.json             # Regression testing
    │
    └── 📁 governance/                                 # Governance + CARE audits
        ├── 📄 care-scope-template.json                # CARE scoping metadata
        ├── 📄 faircare-audit-template.md              # Ethical + cultural review template
        └── 📄 mlops-governance-index.md               # All policies + required links

---

## 🧬 MLOps Template Types

### 1. 📉 Drift Monitoring Templates  
Define how to detect:

- Statistical drift  
- Feature distribution shifts  
- SHAP/XAI drift  
- Embedding drift  
- Seasonal/temporal model degradation  
- CARE-related semantic drift  

Outputs must be:

- JSON-LD  
- Machine-extractable  
- CI-validated  

---

### 2. 🔄 Retraining Templates  
Retraining templates define:

- Retraining triggers (drift, stale data, CARE policy updates)  
- Parameterized retraining configs  
- Reproducible training metadata  
- PROV-O lineage for the entire retraining pipeline  
- STAC publishing for new model versions  

Retraining MUST be reversible (“rollback-safe”).

---

### 3. 🚀 Deployment Templates  
Deployment templates standardize:

- Model rollout strategies (blue/green, canary, A/B)  
- Serving frameworks (API, batch workers, Focus Mode v3 engines)  
- Model version pinning  
- Inference contract validation  
- Disaster-recovery fallback  

---

### 4. 📊 Telemetry Templates  
Telemetry templates define:

- Inference latency  
- Throughput  
- Error/exception signals  
- Energy/Carbon metrics (`energy_schema`, `carbon_schema`)  
- Lineage spans linking inference → model → training datasets  
- Story Node propagation metadata  

---

### 5. 🧪 Continuous Evaluation Templates  
Evaluation templates define:

- Post-deployment evaluation schedule  
- Metric registry  
- Golden-record checkouts  
- Drift metrics  
- CARE masking validation  

These power long-term model reliability.

---

### 6. 🏛 Governance Templates  
Enforce:

- FAIR+CARE auditing  
- Cultural/ethical restrictions  
- Sensitive term/region masking  
- Model usage restrictions  
- Governance approval references  

MLOps models cannot be promoted without passing governance checks.

---

## 📡 STAC v11 Integration

All inference outputs driven by MLOps templates MUST embed:

- `kfm:ml:model_name`  
- `kfm:ml:model_version`  
- `kfm:input_items`  
- CRS + vertical datum  
- Care-scope + sovereignty metadata  
- Full PROV-O lineage  

---

## 🔐 FAIR+CARE Enforcement

Templates ensure:

- H3 spatial generalization  
- Abstracted narrative elements (no sensitive story leakage)  
- Cultural data control  
- No speculative model outputs  
- Sovereignty policy compliance  

---

## 🕰 Version History

| Version  | Date       | Notes                                                           |
|----------|------------|-----------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Full v11.2.2 uplift; feature-complete MLOps template suite      |
| v11.0.0  | 2025-11-15 | Initial MLOps templates introduced                              |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to AI Template Index](../README.md) · [⚙️ Inference Templates](../inference/README.md) · [🏛 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

