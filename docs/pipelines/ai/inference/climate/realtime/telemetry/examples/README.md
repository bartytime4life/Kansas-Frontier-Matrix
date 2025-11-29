---
title: "📊🌡️⚡ KFM v11.2.2 — Climate Realtime Telemetry Examples (OTel · PROV-O · XAI Metrics · FAIR+CARE)"
path: "docs/pipelines/ai/inference/climate/realtime/telemetry/examples/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability Engineering · FAIR+CARE Council"
status: "Active / Enforced"
content_stability: "stable"
doc_kind: "Telemetry Examples · Realtime Climate AI"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.2/climate-inference-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/ai-climate-inference-v11.2.2.json"
energy_schema: "../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
data_contract_ref: "../../../../../../../contracts/data-contract-v3.json"

license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Medium-Risk"
sensitivity: "Climate-Inference-Telemetry"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "telemetry"
  - "opentelemetry"
  - "climate-inference"
  - "realtime-metrics"
  - "xai-telemetry"
  - "energy-carbon-metrics"
  - "prov-lineage"
  - "faircare-audit"
  - "seed-locked-reproducibility"

scope:
  domain: "pipelines/ai/inference/climate/realtime/telemetry/examples"
  applies_to:
    - "realtime-inference"
    - "api-handlers"
    - "xai-handlers"
    - "streaming"
    - "rate-limiters"
    - "policy-engine"
    - "care-governance"
    - "prov-xai"

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

# 📊🌡️⚡ **Climate Realtime Telemetry Examples**  
`docs/pipelines/ai/inference/climate/realtime/telemetry/examples/README.md`

**Purpose**  
Provide canonical examples of **OpenTelemetry (OTel)** spans, metrics, logs, and **PROV-O lineage**  
records for realtime Climate AI inference.  
Used to validate pipeline observability, determinism, FAIR+CARE compliance, energy/carbon accounting,  
and XAI interpretability telemetry for REST/WebSocket/gRPC handlers.

</div>

---

## 🗂️ Directory Layout (v11.2.2)

    docs/pipelines/ai/inference/climate/realtime/telemetry/examples/
        📄 README.md                     # This file
        📄 example-span.json             # OTel span example
        📄 example-provenance.json       # PROV-O lineage example
        📄 example-xai-telemetry.json    # XAI attribution telemetry
        📄 example-energy.json           # Energy/Wh telemetry bundle
        📄 example-carbon.json           # Carbon/gCO2e telemetry bundle

---

## 📘 Overview

Realtime Climate AI inference must generate **complete, deterministic telemetry**, including:

- **OTel spans** for inference lifecycle  
- **Metrics** (latency, inference time, XAI time, memory, GPU utilization)  
- **Event logs** for validation failures, CARE denials, throttling events  
- **Energy + carbon bundles** (Wh + gCO₂e per inference)  
- **STAC-linked asset telemetry**  
- **PROV-O lineage** for inference → XAI → streaming chains  
- **Seed-lock indicators** ensuring determinism  
- **CARE flags** in telemetry for protected-region enforcement  

All examples here are **synthetic but schema-valid**.

---

## 🧭 Telemetry Lifecycle (Mermaid-Safe)

```mermaid
flowchart TD
    A[Request Received] --> B[OTel Span Start]
    B --> C[Inference Execution]
    C --> D[XAI Optional]
    D --> E[Assemble Telemetry Bundle]
    E --> F[Attach PROV Metadata]
    F --> G[Emit Metrics Logs]
    G --> H[Write Telemetry Artifact]
```

---

## 🟦 Example: OTel Span (Inference)

```json
{
  "trace_id": "0af7651916cd43dd8448eb211c80319c",
  "span_id": "b9c7c989f97918e1",
  "name": "climate.inference.execute",
  "attributes": {
    "kfm.seed": 42,
    "kfm.model_version": "kfm-climate-v11.2.2",
    "kfm.variables": ["t2m","td2m","u10","v10"],
    "kfm.crs": "EPSG:4326",
    "kfm.care.scope": "public-generalized",
    "kfm.sovereignty.action": "allow",
    "system": "climate-realtime-api"
  },
  "duration_ms": 87.2,
  "status": "OK"
}
```

---

## 🟩 Example: PROV-O Lineage

```json
{
  "prov": {
    "wasGeneratedBy": "urn:kfm:activity:infer:abcd1234",
    "used": [
      "urn:kfm:data:stac:item-123",
      "urn:kfm:data:stac:item-456"
    ],
    "wasInfluencedBy": "urn:kfm:care:decision:h3mask-001",
    "agent": "urn:kfm:service:climate-realtime-api"
  }
}
```

---

## 🟧 Example: XAI Telemetry

```json
{
  "xai": {
    "method": "shap",
    "variable": "t2m",
    "duration_ms": 29.4,
    "attribution_checksum": "1220abcd...",
    "care.scope": "public-generalized",
    "prov.activity": "urn:kfm:activity:xai:efgh5678"
  }
}
```

---

## 🔋 Example: Energy Telemetry (Wh)

```json
{
  "energy_wh": {
    "inference_wh": 0.044,
    "xai_wh": 0.012,
    "total_wh": 0.056
  }
}
```

---

## 🌍 Example: Carbon Telemetry (gCO₂e)

```json
{
  "carbon_gco2e": {
    "inference_g": 0.21,
    "xai_g": 0.09,
    "total_g": 0.30
  }
}
```

---

## 🧪 CI Validation Requirements

CI MUST validate:

- Telemetry schema correctness (OTel + PROV-O + FAIR+CARE + STAC extensions)  
- Deterministic telemetry under seed-lock  
- No missing fields in required bundles (energy, carbon, CARE flags, provenance)  
- All example artifacts in this directory pass JSON Schema validation  
- No prohibited keys (per KFM-PDC v11)  
- All examples include minimal CARE metadata  

Any violation → CI blocks merge.

---

## 🕰 Version History

| Version  | Date       | Notes                                              |
|----------|------------|----------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial telemetry examples for Climate RT v11.2.2  |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Telemetry](../README.md) ·  
[🌡️ Realtime Inference Root](../../README.md) ·  
[🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

