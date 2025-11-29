---
title: "🌡️📉🔍 KFM v11.2.2 — Anomaly Difference Model (Δ = Realtime − Baseline · Deterministic · XAI-Ready)"
path: "docs/pipelines/ai/inference/climate/models/anomalies/anomaly-diff-model.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
status: "Active / Enforced"
content_stability: "stable"
doc_kind: "Model Component · Anomaly Generation"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.2/climate-inference-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/ai-climate-inference-v11.2.2.json"
energy_schema: "../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
data_contract_ref: "../../../../../contracts/data-contract-v3.json"

license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Medium-Risk"
sensitivity: "Climate-Anomaly-Diff"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "anomaly-diff-model"
  - "climate-anomalies"
  - "delta-computation"
  - "baseline-subtraction"
  - "seed-locked-deterministic"
  - "distribution-consistency"
  - "xai-compatible"
  - "stac-xai"
  - "care-governance"
  - "provenance-delta"

scope:
  domain: "pipelines/ai/inference/climate/models/anomalies"
  applies_to:
    - "anomaly-diff-model.md"
    - "anomaly-baseline.md"
    - "anomaly-generation"
    - "climate-normals"
    - "hazard-driver-support"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_purpose_block: true
requires_version_history: true
requires_governance_links_in_footer: true
diagram_profiles:
  - "mermaid-flowchart-v1"
---

<div align="center">

# 🌡️📉🔍 **Anomaly Difference Model**  
`docs/pipelines/ai/inference/climate/models/anomalies/anomaly-diff-model.md`

**Purpose**  
Define the **difference model** that computes climate anomalies:  
**Δ = Realtime Field − Baseline Field**.  
This is the core anomaly computation used for statewide anomaly maps, hazard driver derivations,  
Story Node v3 climatic narratives, Focus Mode v3 overlays, and all downstream anomaly-aware logic.

</div>

---

## 📘 Overview

The anomaly-diff model produces **signed deviations** from a reference climatology baseline.  
It ensures:

- Deterministic, seed-locked Δ computation  
- Stable anomaly fields across pipeline refresh cycles  
- Support for multiple variable categories (temperature, dewpoint, wind, humidity, precipitation)  
- FAIR+CARE-compliant anomaly distribution  
- Consistent distribution across model-version upgrades  
- XAI-ready anomaly generation for explainability  
- Full PROV-O lineage & STAC-XAI compatibility  

---

## 🧩 Mathematical Definition (ASCII-Safe)

```
delta(x, y, t, v) = realtime(x, y, t, v) - baseline(x, y, v)
```

Where:

- `x, y` = horizontal grid location  
- `t` = timestamp  
- `v` = variable name  
- All fields MUST share CRS + vertical axis + units  

---

## 🗂 Supported Variables

- Temperature anomalies: `t2m`, `t850`, `t700`  
- Dewpoint anomalies: `td2m`  
- Wind anomalies: `u10`, `v10`, upper-level `u*`, `v*`  
- Humidity anomalies  
- Precipitation departure  
- Soil moisture deviation  
- Pressure deviation  

All variables MUST have matching units to baseline fields.

---

## 🧬 Anomaly-Diff Computation Pipeline

```mermaid
flowchart TD
    A[Realtime Field] --> C[CRS And Units Check]
    B[Baseline Field] --> C
    C --> D[Seed Locked Delta Computation]
    D --> E[Optional XAI Attribution]
    E --> F[Assemble Anomaly Grid]
    F --> G[STAC XAI Metadata Packaging]
    G --> H[Return Anomaly Field]
```

---

## 🔍 Input Requirements

### **Realtime Input**
- Source: Downscaled field, native NWP field, or merged HRRR/ERA5  
- CRS: EPSG:4326 or transformable  
- Vertical axis: Defined & compatible  
- Units: MUST match baseline exactly  
- Temporal metadata: ISO 8601  

### **Baseline Input**
- From anomaly-baseline model  
- Must include mean field + optional higher moments  
- Must be validated by CI for completeness  

---

## 📦 Output Structure

Outputs MUST include:

- `anomaly_grid.tif` (COG)  
- `anomaly_metadata.json`  
- `anomaly_summary.json`  
- STAC Item with anomaly metadata  
- Checksums (multihash)  
- FAIR+CARE changes  
- PROV-O lineage block  
- XAI attribution block (if enabled)

---

## 🛡️ CARE + Sovereignty Enforcement

Anomalies must:

- Apply H3 generalization for restricted regions  
- Remove sensitive variable anomalies where required  
- Clearly mark masking or degradation in metadata:  

```json
{
  "care": {
    "masking": "h3-generalized",
    "scope": "public-generalized"
  }
}
```

Failure to comply → CI reject.

---

## 🎛 CI Validation Requirements

CI MUST ensure:

- CRS/units matching  
- Deterministic Δ results  
- PROV-O lineage completeness  
- STAC-XAI block present  
- Baseline metadata valid  
- Seed-lock enforced  
- No missing keys  
- FAIR+CARE attached  

CI failure → ❌ merge blocked.

---

## 🕰 Version History

| Version  | Date       | Notes                                          |
|----------|------------|------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial anomaly-diff model documentation.       |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Anomaly Models](../README.md) ·  
[🌡️ Climate Inference Root](../../README.md) ·  
[🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

