---
title: "📚🌪️🧠 KFM v11.2.2 — Hazard Model Examples (Tornado 🌪️ · Hail 🧊 · Flood 🌊 · Fire-Weather 🔥 · Heat ☀️ · Winter ❄️ · FAIR+CARE 🛡️)"
path: "docs/pipelines/ai/models/hazards/examples/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Hazard AI Working Group 🌪️🧠 · FAIR+CARE Council 🛡️"
status: "Active / Enforced"
content_stability: "stable"
doc_kind: "Hazard Models · Example Library 📚🌪️"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/hazard-model-examples-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/ai-hazard-model-examples-v11.2.2.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
data_contract_ref: "../../../../contracts/data-contract-v3.json"

license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Medium-Risk (Hazard Intelligence Examples)"
sensitivity: "Hazard-Examples"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "hazard-examples"
  - "tornado-example"
  - "hail-example"
  - "flood-example"
  - "fireweather-example"
  - "heat-example"
  - "winter-example"
  - "faircare-governance"
  - "sovereignty-protection"
  - "context-grounding"

scope:
  domain: "pipelines/ai/models/hazards/examples"
  applies_to:
    - "README.md"
    - "*"
    - "../evaluation-report.md"
    - "../mlops/*"
    - "../../inference/hazards/*"
    - "../../models/climate/*"
    - "../../models/hydrology/*"
    - "../../models/embeddings/*"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_purpose_block: true
requires_directory_layout_section: true
requires_governance_links-in-footer: true
requires_version_history: true

diagram_profiles:
  - "mermaid-flowchart-v1"
---

<div align="center">

# 📚🌪️🧠 **Hazard Model Examples — KFM v11.2.2 (MAX MODE)**  
`docs/pipelines/ai/models/hazards/examples/README.md`

**Purpose**  
Provide a curated, sovereignty-safe, FAIR+CARE-compliant library of **environmental hazard examples**  
used for hazard model QA, Focus Mode integration, governance review, UI prototyping,  
and deterministic CI tests.

Domains included:  
🌪️ Tornado • 🧊 Hail • 🌊 Flood • 🔥 Fire-Weather • ☀️ Heat • ❄️ Winter

</div>

---

## 🗂️📁🌪️ **Directory Layout (MAX MODE)**

```
docs/pipelines/ai/models/hazards/examples/
    📄 README.md
    📄 example_tornado.json
    📄 example_hail.json
    📄 example_flood.json
    📄 example_fire_weather.json
    📄 example_heat.json
    📄 example_winter.json
    📄 example_xai_block.json
    📄 example_provenance.json
    📄 example_stac_item.json
```

---

## 🧬🌪️📦 **Hazard Example Architecture (Mermaid-Safe)**

```mermaid
flowchart TD
    A[📥 Raw Environmental Inputs] --> B[🌪️ Tornado Example]
    A --> C[🧊 Hail Example]
    A --> D[🌊 Flood Example]
    A --> E[🔥 Fire Weather Example]
    A --> F[☀️ Heat Stress Example]
    A --> G[❄️ Winter Impact Example]
    B --> H[💡 XAI Attribution]
    C --> H
    D --> H
    E --> H
    F --> H
    G --> H
    H --> I[📜 STAC + PROV Example Outputs]
```

---

# 🔍 **Example Set (MAX MODE)**

---

## 🌪️ **1. Tornado Example**

```json
{
  "tornado": {
    "cape_jkg": 2450,
    "cin_jkg": -32,
    "shear_0_1km": 18,
    "shear_0_6km": 34,
    "srh_0_1km": 132,
    "llj_speed_ms": 22,
    "tornado_potential": 0.37
  }
}
```

---

## 🧊 **2. Hail Example**

```json
{
  "hail": {
    "muhail_proxy": 1.82,
    "freeze_level_m": 2650,
    "shear_0_6km": 26,
    "storm_top_temp_c": -58,
    "hail_severity": 0.41
  }
}
```

---

## 🌊 **3. Flood Example**

```json
{
  "flood": {
    "precip_1h_mm": 21.4,
    "precip_3h_mm": 48.0,
    "runoff_mm": 17.2,
    "soil_moisture": 0.41,
    "streamflow_cms": 13.8,
    "flood_risk": 0.33
  }
}
```

---

## 🔥 **4. Fire-Weather Example**

```json
{
  "fire_weather": {
    "temp_c": 36.4,
    "humidity_pct": 18,
    "wind_speed_ms": 12.8,
    "fuel_moisture": 0.11,
    "drought_index": 0.62,
    "fire_weather_risk": 0.28
  }
}
```

---

## ☀️ **5. Heat Example**

```json
{
  "heat": {
    "temp_c": 39.2,
    "dewpoint_c": 26.1,
    "heat_index_c": 47.3,
    "humidity_pct": 54,
    "synoptic_pattern": "ridge",
    "heat_stress": 0.52
  }
}
```

---

## ❄️ **6. Winter Example**

```json
{
  "winter": {
    "temp_c": -7.8,
    "wind_speed_ms": 14.2,
    "snow_ratio": 12.5,
    "wind_chill_c": -18.1,
    "winter_impact": 0.34
  }
}
```

---

## 💡 **7. XAI Attribution Example**

```json
{
  "xai": {
    "importance": {
      "climate": 0.33,
      "hydrology": 0.18,
      "spatial": 0.15,
      "hazard": 0.34
    },
    "seed": 42
  }
}
```

---

## 📜 **8. PROV Example**

```json
{
  "prov": {
    "wasGeneratedBy": "urn:kfm:activity:hazard_example_v11_2_2",
    "used": [
      "urn:kfm:data:climate_item",
      "urn:kfm:data:hydrology_item"
    ],
    "agent": "urn:kfm:service:hazard-example-engine"
  }
}
```

---

## 🌐 **9. STAC Item Example**

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "hazard_example_tornado_v11_2_2",
  "properties": {
    "hazard:type": "tornado",
    "hazard:version": "v11.2.2",
    "hazard:seed": 42,
    "care:masking": "h3-hazard-generalized"
  }
}
```

---

# 🧪📏🔬 **CI Requirements for Examples**

- Deterministic values  
- No sensitive-region cues  
- CARE metadata present  
- XAI attribution included  
- FAIR+CARE aligned  
- Schema validity  
- Physically realistic environmental values  
- No hyper-local geographies  

---

# 🕰️📜 Version History

| Version | Date       | Notes                                             |
|---------|------------|---------------------------------------------------|
| v11.2.2 | 2025-11-28 | Initial Hazard Model Examples Catalog (MAX MODE)  |

---

<div align="center">

### 🔗 Footer  
[🌪️ Back to Hazard Models](../README.md) ·  
[📊 Evaluation Report](../evaluation-report.md) ·  
[🏛 Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

