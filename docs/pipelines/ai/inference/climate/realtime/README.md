---
title: "🌡️⚡🤖 KFM v11.2.2 — Climate AI Realtime Inference Pipelines (Streaming · STAC-XAI · FAIR+CARE · Deterministic)"
path: "docs/pipelines/ai/inference/climate/realtime/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Pipeline Subcomponent (Realtime Climate Inference)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/climate-inference-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/ai-climate-inference-v11.2.2.json"
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
sensitivity: "Climate-Inference-Realtime"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "climate-realtime-inference"
  - "streaming-prediction"
  - "api-inference"
  - "climate-driver-realtime"
  - "hazard-linked-realtime"
  - "xai-realtime"
  - "stac-xai"
  - "prov-xai"
  - "story-node-climate"
  - "focus-mode-climate"
  - "faircare-governance"

scope:
  domain: "pipelines/ai/inference/climate/realtime"
  applies_to:
    - "streaming-inference"
    - "api-inference-server"
    - "realtime-driver-generation"
    - "realtime-xai"
    - "model-serving"
    - "energy-carbon-telemetry"
    - "faircare-governance"
    - "prov-xai"
    - "stac-xai"

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

# 🌡️⚡🤖 **Climate AI Realtime Inference Pipelines — KFM v11.2.2**  
`docs/pipelines/ai/inference/climate/realtime/README.md`

**Purpose:**  
Define the **realtime climate inference subsystem** for the Kansas Frontier Matrix, enabling streaming + on-demand AI-powered climate predictions (downscaled fields, anomalies, hazard-linked drivers) with deterministic seeds, **STAC-XAI semantics**, **FAIR+CARE safeguards**, and full **PROV-O lineage** for governance.

</div>

---

## 📘 Overview

The realtime climate inference engine provides **low-latency**, **governed**, and **deterministic** AI climate predictions.

Supported capabilities:

- ⚡ Streaming API inference (WebSockets, SSE, gRPC)  
- 🌡️ Instant downscaled climate variable predictions  
- 📉 Realtime anomaly evaluation  
- 💨 Hazard-linked climate driver inference (CAPE, SRH, LLJ, lapse rates, etc.)  
- 🗺️ Small-tile spatial predictions (if enabled)  
- 🧩 SHAP/IG/CAM/spatial attribution explainability on-demand  
- 🔗 STAC-XAI + JSON-LD explainability bundling  
- 🛡️ CARE + sovereignty masking  
- 📜 PROV-O lineage for every inference session  

Realtime inference supports:

- Focus Mode v3 live climate overlays  
- Story Node climate event generation  
- Hazard pipeline upstream dependencies  
- Research-grade reproducibility  

---

## ⚡ Realtime Inference Modes

### 1. **On-Demand REST/GraphQL Inference**
For clients requesting specific:
- Times  
- Variables  
- Geographic bounding boxes  

Outputs include:
- Downscaled values  
- Drivers  
- SHAP/IG attribution (optional)  
- JSON-LD semantics  

### 2. **Streaming (SSE / WebSocket / gRPC)**
Continuous climate predictions for:
- Dashboards  
- Hazard nowcasting  
- Monitoring pipelines  

### 3. **Tile-Based Realtime Predictions**
Small GeoParquet tiles for:
- Focus Mode v3  
- MapLibre interactive layers  

### 4. **Realtime Explainability**
Optional XAI inference on-demand:
- SHAP local  
- IG local  
- CAMs  
- Spatial attribution mini-rasters  

---

## 🏗️ Realtime Architecture (GitHub-Safe Mermaid)

```mermaid
flowchart TD
    A[Receive Realtime Request] --> B[Load Latest Model]
    B --> C[Seed-Locked Inference]
    C --> D[Optional Bias Correction]
    D --> E[Generate Climate Drivers]
    E --> F[Optional XAI Computation]
    F --> G[Return Results to Client]
    G --> H[Emit STAC-XAI Metadata and PROV Lineage]
```

---

## 🧩 Realtime Features (v11.2.2)

- Deterministic inference across runs  
- Model version pinning  
- Strict input validation (CRS, vertical datum, time windows)  
- CARE + Sovereignty filtering  
- Optional rate-limited XAI calls  
- OpenTelemetry spans with climate-specific fields  
- Automatic STAC-XAI item generation for persistent outputs  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/inference/climate/realtime/
    ├── 📄 README.md                                  # This file
    │
    ├── ⚡ realtime_inference_server.py                # Main inference server
    ├── 📄 server-config.yaml                          # Ports, model versions, throttles
    │
    ├── 📁 handlers/                                   # API handlers
    │   ├── 📄 rest_handler.py
    │   ├── 📄 websocket_handler.py
    │   └── 📄 grpc_handler.py
    │
    ├── 📁 xai/                                        # On-demand explainability
    │   ├── 📄 shap.py
    │   ├── 📄 ig.py
    │   ├── 📄 cams.py
    │   └── 📄 spatial.py
    │
    ├── 📁 stac/                                       # Optional STAC item writer
    │   ├── 📄 README.md
    │   └── 📄 stac_writer.py
    │
    └── 📁 telemetry/
        ├── 📄 README.md
        └── 📄 realtime-otel-config.yaml

---

## 📡 STAC-XAI Requirements

Realtime inference can write STAC Items when configured.

All generated Items MUST contain:

- `kfm:explainability:method`  
- `kfm:explainability:{local|spatial}`  
- `kfm:model_version`  
- `kfm:input_items`  
- CRS + vertical metadata  
- CARE + sovereignty metadata  
- PROV-O lineage entries  
- `checksum:multihash` if persisted  

---

## 🧾 PROV-O Lineage Requirements

Each inference session MUST include:

- `prov:wasGeneratedBy` (session UUID)  
- `prov:used` (input sets, model version)  
- `prov:generatedAtTime`  
- `prov:Agent` (model + software ID)  

Optional:
- `prov:wasDerivedFrom` for multimodal XAI  

---

## 🔐 FAIR+CARE & Sovereignty Rules

Realtime predictions must:

- Apply H3 spatial generalization for sensitive locations  
- Include CARE metadata in all JSON-LD bundles  
- Respect tribal sovereignty directives  
- Use non-speculative, governance-approved climate language  
- Enforce Data Contract v3 restrictions  

Realtime *XAI* must mask sensitive geographic inference.

---

## 🧪 CI & Validation Rules

Realtime pipeline code MUST pass:

- Deterministic inference tests  
- XAI correctness tests  
- CARE + sovereignty linting  
- STAC-XAI metadata validation  
- JSON-LD schema validation  
- OpenTelemetry trace schema validation  
- Throughput + latency performance thresholds  
- Model version pin checks  

Failures → ❌ merge blocked.

---

## 🕰 Version History

| Version | Date       | Notes                                                              |
|---------|------------|--------------------------------------------------------------------|
| v11.2.2 | 2025-11-28 | Initial realtime climate inference documentation (KFM v11.2.2)      |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Climate Inference](../README.md) · [🧠 AI Pipeline Layer](../../../README.md) · [🏛 Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

