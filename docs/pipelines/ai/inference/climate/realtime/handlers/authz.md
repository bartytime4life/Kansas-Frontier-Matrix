---
title: "🌡️🛡️🔐 KFM v11.2.2 — Climate AI Realtime Inference Authorization Layer (AuthZ · Policy Engine · FAIR+CARE)"
path: "docs/pipelines/ai/inference/climate/realtime/handlers/authz.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
status: "Active / Enforced"
content_stability: "stable"
doc_kind: "Pipeline Subcomponent (Authorization Layer)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-sha256>"
doc_integrity_checksum: "<sha256>"

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
sensitivity: "Climate-Inference-Authorization"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "realtime-authz"
  - "climate-inference-authorization"
  - "policy-engine"
  - "rbac-abac"
  - "faircare-enforcement"
  - "sovereignty-controls"
  - "rate-limit-authz"
  - "ip-governance"
  - "focusmode-policy"

scope:
  domain: "pipelines/ai/inference/climate/realtime/handlers/authz"
  applies_to:
    - "rest-handler"
    - "websocket-handler"
    - "grpc-handler"
    - "policy-engine"
    - "rate-limiters"
    - "sovereignty-checks"
    - "dataset-permissions"
    - "xai-visibility-controls"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

diagram_profiles:
  - "mermaid-flowchart-v1"
---

<div align="center">

# 🌡️🛡️🔐 **Climate AI Realtime Inference — Authorization Layer (AuthZ)**  
`docs/pipelines/ai/inference/climate/realtime/handlers/authz.md`

**Purpose:**  
Define the **authorization policy engine** governing realtime climate inference requests.  
Enforces **RBAC + ABAC**, FAIR+CARE protections, sovereignty rules, dataset-level permissions,  
and XAI visibility constraints for REST, WebSocket, and gRPC handlers.

</div>

---

## 📘 Overview

The Authorization Layer (AuthZ) is the **policy gatekeeper** for the realtime inference system:

- Enforces **who** can access **which models**, **which variables**, and **which resolutions**  
- Applies **CARE & sovereignty rules** to mask or deny sensitive geospatial outputs  
- Validates **scope of use**, **rate class**, and **policy tier**  
- Binds **per-endpoint policies** to **realtime handlers**  
- Governs **access to XAI explanations**, including spatial attribution  
- Ensures **dataset licensing**, **temporal access windows**, and **model-version permissions**

AuthZ runs *before* the inference router, providing deterministic, audited policy decisions.

---

## 🗂️ Directory Layout (v11.2.2)

    docs/pipelines/ai/inference/climate/realtime/handlers/
        📄 README.md
        📄 rest-handler.md
        📄 websocket-handler.md
        📄 grpc-handler.md
        📄 input-validation.md
        📄 xai-handlers.md
        📄 care-governance.md
        📄 prov-xai.md
        📄 stac-xai.md
        📄 rate-limiters.md
        📄 authz.md                # ← This file

---

## 🧩 AuthZ Policy Layers

### 1. 🧑‍🤝‍🧑 RBAC (Role-Based Access Control)
Roles defined at system level:

- `public`
- `research-basic`
- `research-advanced`
- `internal-ops`
- `admin-governance`
- `restricted-tribal-sovereign` (special class requiring CARE filtering)

### 2. 🧬 ABAC (Attribute-Based Access Control)
Attributes enforced:

- `variable_set`  
- `resolution`  
- `model_version`  
- `geographic_scope`  
- `temporal_scope`  
- `requester_affiliation`  
- `license_type`  
- `xai_mode`  
- `rate_class`

### 3. 🪶 Sovereignty & CARE Enforcement  
Rules triggered when:

- Requests intersect **tribal boundaries**  
- Spatial resolution exceeds allowed threshold  
- XAI attribution could expose sensitive locations  
- Model output intersects protected ecological zones

---

## 🔐 Authorization Flow (Mermaid-Safe)

```mermaid
flowchart TD
    A[Incoming Request] --> B[Extract Identity And Attributes]
    B --> C[RBAC Role Check]
    C --> D[ABAC Policy Match]
    D --> E[CARE Sovereignty Check]
    E --> F[XAI Visibility Permissions]
    F --> G[Rate Class Evaluation]
    G --> H[Final Permit Or Deny]
    H --> I[Emit PROV Record]
```

---

## 🎛 Policy Enforcement Rules

AuthZ MUST enforce:

- Temporal constraints (e.g., only allow recent models for certain roles)  
- Model-version access classes  
- Spatial masking for sensitive zones  
- Resolution downgrading  
- XAI mode gating (SHAP / IG / CAM allowed only for permitted roles)  
- WebSocket session-level caps  
- gRPC binary-stream authorization at message boundaries  

---

## 🧪 CI Validation Requirements

CI must validate:

- Deterministic policy evaluation  
- Policy table schema validity  
- No unbounded privileges  
- No bypass of CARE or sovereignty filters  
- All decisions logged with PROV-O lineage  
- All rules version-pinned and hashed  

---

## 🧠 XAI Authorization

XAI exposure requires:

- Allowed user role  
- Allowed variable set  
- Spatial extent approval  
- CARE compliance check  
- Sovereignty masks applied  
- Stamped provenance on every XAI asset  

Failure at any stage → XAI disabled for the response.

---

## 🕰 Version History

| Version  | Date       | Notes                                          |
|----------|------------|------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial AuthZ subsystem documentation.         |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Handlers](../README.md) ·  
[🌡️ Climate Inference Root](../../README.md) ·  
[🏛 Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

