---
title: "🌡️⚡📞 KFM v11.2.2 — Climate AI Realtime Inference Handlers (REST · WebSocket · gRPC · FAIR+CARE)"
path: "docs/pipelines/ai/inference/climate/realtime/handlers/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Pipeline Subcomponent (API Handlers)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.2/climate-inference-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/ai-climate-inference-v11.2.2.json"
energy_schema: "../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
data_contract_ref: "../../../../../../contracts/data-contract-v3.json"

license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Medium-Risk"
sensitivity: "Climate-Inference-Realtime-Handlers"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "climate-realtime-handlers"
  - "api-handlers"
  - "rest-handler"
  - "websocket-handler"
  - "grpc-handler"
  - "streaming-inference"
  - "care-governance"
  - "prov-xai"
  - "stac-xai"
  - "focus-mode-climate"
  - "story-node-climate"

scope:
  domain: "pipelines/ai/inference/climate/realtime/handlers"
  applies_to:
    - "rest-handler"
    - "websocket-handler"
    - "grpc-handler"
    - "input-validation"
    - "xai-handlers"
    - "care-governance"
    - "prov-xai"
    - "stac-xai"
    - "rate-limiters"
    - "authz"
    - "streaming-handlers"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_purpose_block: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true
requires_version_history: true

diagram_profiles:
  - "mermaid-flowchart-v1"
---

<div align="center">

# 🌡️⚡📞 **Climate AI Realtime Inference — API Handlers**  
`docs/pipelines/ai/inference/climate/realtime/handlers/README.md`

**Purpose:**  
Define the **API handler layer** for realtime climate inference.  
This includes REST, WebSocket, and gRPC handlers that process user requests, validate inputs, route inference calls, attach FAIR+CARE safeguards, and return deterministic XAI-aware climate predictions.

</div>

---

## 📘 Overview

The realtime handler subsystem provides:

- High-performance request processing  
- Deterministic routing to inference engines  
- XAI-aware output packaging  
- STAC-XAI metadata binding  
- CARE + sovereignty enforcement  
- Input validation (CRS, vertical, variable sets, time windows)  
- Safe streaming and backpressure mechanisms  
- Story Node + Focus Mode integration hooks  

Handlers sit between clients and the realtime inference engine.

---

## 🔌 Handler Types

### 1. 🌐 REST Handler (`rest_handler.py`)
Supports:
- `/infer`
- `/drivers`
- `/explain/local`
- `/explain/spatial`
- `/health`

Responsibilities:
- Parse & validate request payload  
- Check CRS/vertical axis  
- Enforce rate limits  
- Apply CARE + sovereignty filters  
- Route to inference engine  
- Serialize JSON-LD or array responses  
- Emit OTel spans + PROV lineage  

---

### 2. 🔗 WebSocket Handler (`websocket_handler.py`)
Provides streaming inference via:

- WebSockets  
- SSE-like continuous mode if allowed  

Responsibilities:
- Maintain persistent session  
- Stream climate predictions/tiles  
- Push XAI deltas on-demand  
- Enforce CARE masking for spatial data  
- Track session-level PROV lineage  
- Throttle based on client capability  

---

### 3. 🛰️ gRPC Handler (`grpc_handler.py`)
Optimized for:

- High-throughput data ingestion  
- Internal KFM service-to-service communication  
- Hazard pipeline dependencies  

Responsibilities:
- Strict protobuf schema validation  
- Deterministic binary responses  
- Built-in observability hooks  
- CARE-transparent messaging  
- Full STAC-XAI integration metadata  

---

## 🧭 Handler Architecture (Mermaid-Safe)

```mermaid
flowchart TD
    A[Incoming Request] --> B[Input Validation]
    B --> C[CARE - Sovereignty Enforcement]
    C --> D[Inference Router]
    D --> E[Seed-Locked Climate Inference]
    E --> F[Optional XAI Processing]
    F --> G[Response Formatter]
    G --> H[Return Response to Client]
    H --> I[Telemetry + PROV Lineage]
```

---

## 🧪 Input Validation Requirements

Handlers MUST validate:

- `variable_set`  
- Time windows (ISO-8601)  
- CRS (`proj:epsg`) + vertical axis  
- Bounding boxes or grid indices  
- Model version compatibility  
- Request shape + required fields  
- CARE violation patterns  
- Sovereignty protection requirements  

Invalid requests → **reject with structured error**.

---

## 🔐 FAIR+CARE Safeguards

Handlers MUST enforce:

- H3 spatial masking  
- Removal of sensitive geospatial context  
- CARE scope tagging  
- Non-speculative climate language  
- Data Contract v3 compliance  
- Community governance constraints  

---

## 🧩 XAI Integration

Handlers may activate on-demand XAI:

- SHAP local  
- IG local  
- CAM spatial  
- Spatial attribution  
- Narrative driver extraction  

All results MUST:

- Be wrapped in JSON-LD  
- Include `kfm:model_version`, `kfm:input_items`, `checksum:multihash`  
- Include CARE + sovereignty annotations  
- Attach PROV lineage  

---

## 🧪 CI & Test Requirements

Tests MUST cover:

- REST/WS/gRPC routing  
- Input validation  
- CRS + vertical checks  
- Rate limiting  
- Backpressure + session control  
- XAI correctness  
- CARE + sovereignty enforcement  
- PROV + STAC-XAI metadata  
- Telemetry span coverage  
- Deterministic outputs under seed lock  

---

## 🕰 Version History

| Version  | Date       | Notes                                                              |
|----------|------------|--------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial realtime handler subsystem for Climate AI Inference v11.2.2 |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Realtime Inference](../README.md) · [🌡️ Climate Inference Root](../../README.md) · [🏛 Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

