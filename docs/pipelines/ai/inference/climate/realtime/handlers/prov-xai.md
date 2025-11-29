---
title: "🧩📜🤖 KFM v11.2.2 — Climate AI Realtime PROV-XAI Handler (Lineage · Attribution Provenance · FAIR+CARE)"
path: "docs/pipelines/ai/inference/climate/realtime/handlers/prov-xai.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council · Provenance Board"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Handler Subcomponent · PROV + XAI Lineage Assembly"

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
sensitivity: "Climate-Inference-PROV-XAI"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "prov-xai"
  - "xai-lineage"
  - "explainability-tracing"
  - "provenance-metadata"
  - "stac-xai"
  - "care-governance"
  - "focus-mode-climate"
  - "story-node-climate"
  - "auditability"
  - "deterministic-xai"

scope:
  domain: "pipelines/ai/inference/climate/realtime/handlers"
  applies_to:
    - "prov-xai"
    - "rest-handler"
    - "websocket-handler"
    - "grpc-handler"
    - "xai-handlers"
    - "care-governance"
    - "stac-xai"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_purpose_block: true
requires_governance_links_in_footer: true
requires_version_history: true

diagram_profiles:
  - "mermaid-flowchart-v1"
---

<div align="center">

# 🧩📜🤖 **Climate AI Realtime PROV-XAI Handler**  
`docs/pipelines/ai/inference/climate/realtime/handlers/prov-xai.md`

**Purpose**  
Define the provenance assembly subsystem responsible for creating **PROV-O compliant lineage** for all XAI computations in the realtime Climate AI pipeline.  
This includes inference lineage, XAI activity lineage, CARE-influenced decisions, and STAC-XAI linkages for transparent, auditable, and deterministic explainability.

</div>

---

## 📘 Overview

The PROV-XAI subsystem creates **structured provenance metadata** describing:

- Which input data was used  
- Which models and versions ran  
- Which XAI method produced the attribution  
- Which CARE governance decisions influenced the result  
- How the inference/XAI chain connects to upstream STAC Items  
- Deterministic seeds and parameters used  
- Which services (agents) performed the operations  

This metadata is added to:

- REST responses  
- WebSocket frames  
- gRPC binary responses  

and feeds:

- FAIR audit logs  
- Story Node v3 generation  
- Focus Mode v3 “explain the explanation” views  
- Internal compliance and reproducibility audits  

---

## 🧭 PROV-XAI Architecture (Mermaid-Safe)

```mermaid
flowchart TD
    A[Inference or XAI Output] --> B[Collect Input Metadata]
    B --> C[Assemble STAC Item References]
    C --> D[Apply CARE Decision Context]
    D --> E[Build PROV Activities and Agents]
    E --> F[Attach Checksums and Seeds]
    F --> G[Generate JSON LD PROV Block]
    G --> H[Return to Handler for Final Assembly]
```

---

## 🧩 Provenance Objects

### **Entities (`prov:Entity`)**
Include:

- Input STAC Items  
- Model versions + variants  
- Derived climate fields  
- XAI attribution arrays  
- Bounding boxes / CRS metadata  
- CARE decisions (as “influencing entities”)  

Example:

```json
{
  "prov:Entity": {
    "input_item_1": {
      "type": "stac:Item",
      "href": "https://…/stac/item-uuid"
    }
  }
}
```

---

### **Activities (`prov:Activity`)**
Represent:

- Inference run  
- XAI computation  
- CARE evaluation steps  
- Masking/generalization application  

Example:

```json
{
  "prov:Activity": {
    "urn:kfm:activity:xai:abcd": {
      "startedAtTime": "2025-06-03T12:00:00Z",
      "endedAtTime": "2025-06-03T12:00:00Z",
      "kfm:seed": 42,
      "kfm:xai_method": "shap"
    }
  }
}
```

---

### **Agents (`prov:Agent`)**
Represent:

- Climate inference service  
- XAI service  
- CARE governance engine  
- KFM API layer  

Example:

```json
{
  "prov:Agent": {
    "urn:kfm:service:climate-realtime-api": {
      "type": "SoftwareAgent",
      "version": "v11.2.2"
    }
  }
}
```

---

## 🔗 Provenance Relationships

Each XAI output MUST include:

- `prov:wasGeneratedBy` → XAI activity  
- `prov:used` → STAC Items, inference fields, CARE decisions  
- `prov:wasInfluencedBy` → CARE governance entity  
- `prov:wasAssociatedWith` → XAI agent  

Example:

```json
{
  "prov": {
    "wasGeneratedBy": "urn:kfm:activity:xai:abcd",
    "used": [
      "urn:kfm:data:stac:item-uuid-1",
      "urn:kfm:data:stac:item-uuid-2"
    ],
    "wasInfluencedBy": "urn:kfm:care:decision:qwerty",
    "agent": "urn:kfm:service:climate-xai-engine"
  }
}
```

---

## 🔒 Determinism, Seeds, and Checksum Requirements

The handler MUST embed:

- `seed`: integer used for deterministic attribution  
- `checksum.multihash`: multihash of model inputs  
- `checksum.xai`: hash of the XAI output array  
- `checksum.activity`: hash of activity metadata  

All checksums MUST use **multihash SHA-256**.

---

## 🌍 CARE-Aware Provenance

CARE governance decisions MUST appear in PROV via:

- `prov:wasInfluencedBy`  
- `prov:used` referencing CARE decision entities  

Example CARE provenance entity:

```json
{
  "prov:Entity": {
    "urn:kfm:care:decision:qwerty": {
      "masking_level": "h3-generalized",
      "policy": "INDIGENOUS-DATA-PROTECTION",
      "scope": "public-generalized"
    }
  }
}
```

---

## 📦 STAC-XAI Integration

PROV-XAI MUST integrate with STAC-XAI:

- Reference upstream STAC Items  
- Record variable lists  
- Record bounding boxes + CRS  
- Reference XAI-derived assets like CAM fields  

XAI outputs become STAC Assets:

```json
{
  "stac": {
    "assets": {
      "xai_heatmap": {
        "href": "s3://…/xai/heatmap.tif",
        "type": "image/tiff",
        "roles": ["xai", "explanation"]
      }
    }
  }
}
```

---

## 🧪 Testing and CI Requirements

CI MUST ensure:

- All handlers attach valid PROV blocks  
- Missing provenance triggers CI failure  
- XAI activities always include seeds + timestamps  
- All CARE decisions appear in provenance  
- STAC-XAI integration fields are correct  
- JSON-LD passes schema validation  

Tests MUST include:

- Local XAI provenance  
- Spatial XAI provenance  
- CARE-impacted provenance  
- Multi-STAC input provenance  
- Checksum reproducibility tests  

---

## 🕰 Version History

| Version  | Date       | Notes                                                |
|----------|------------|------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial PROV-XAI handler specification for v11.2.2   |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Handlers](README.md) ·  
[🌡️ Realtime Inference Root](../README.md) ·  
[🏛 Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

