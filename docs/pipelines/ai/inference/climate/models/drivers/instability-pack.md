---
title: "🌪️📦⚡ KFM v11.2.2 — Instability Pack (Composite Hazard Driver · CAPE/CIN/Shear/LLJ · Deterministic · XAI-Ready)"
path: "docs/pipelines/ai/inference/climate/models/drivers/instability-pack.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
status: "Active / Enforced"
content_stability: "stable"
doc_kind: "Model Component · Hazard Driver Composite · Instability Suite"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.2/climate-drivers-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/ai-climate-drivers-v11.2.2.json"
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
sensitivity: "Hazard-Drivers-InstabilityPack"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "instability-pack"
  - "hazard-driver-suite"
  - "cape-cin"
  - "shear-llj"
  - "composite-instability"
  - "severe-weather-signals"
  - "deterministic-seed"
  - "xai-compatible"
  - "stac-xai"
  - "prov-lineage"

scope:
  domain: "pipelines/ai/inference/climate/models/drivers"
  applies_to:
    - "instability-pack.md"
    - "cape-driver.md"
    - "cin-driver.md"
    - "shear-driver.md"
    - "llj-driver.md"
    - "hazard-driver-core"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_purpose_block: true
requires_governance_links_in_footer: true
requires_version_history: true
diagram_profiles:
  - "mermaid-flowchart-v1"
---

<div align="center">

# 🌪️📦⚡ **Instability Pack — Composite Hazard Driver**  
`docs/pipelines/ai/inference/climate/models/drivers/instability-pack.md`

**Purpose**  
Define the **Instability Pack** — a composite hazard-driver model combining CAPE, CIN, shear,  
low-level jet (LLJ), lapse rates, and other severe-weather ingredients into a unified signal.  
This pack powers hazard probability chains, downstream severe-weather models, and Story Node v3  
meteorological narratives.  
All computations MUST be deterministic, XAI-compatible, and FAIR+CARE-governed.

</div>

---

## 📘 Overview

The Instability Pack blends multiple atmospheric instability drivers into a coherent, interpretable  
representation of severe-weather potential.

Primary components:

- **CAPE** (positive buoyant energy)  
- **CIN** (inhibiting energy)  
- **Shear** (0–1 km, 0–3 km, bulk, deep-layer)  
- **Low-Level Jet (LLJ)**  
- **Lapse rates** (surface–3 km, 700–500 mb)  
- **Moisture transport vectors**  
- **Dewpoint depression fields**  
- **Lift indicators** (optional)  

Uses seed-locked deterministic algebraic combination and scaled normalization.

---

## 🧩 Instability Pack Pipeline

```mermaid
flowchart TD
    A[CAPE Driver] --> D[Normalize Inputs]
    B[CIN Driver] --> D
    C[Shear/LLJ Drivers] --> D
    E[Lapse Rates And Moisture] --> D
    D --> F[Deterministic Weighted Combination]
    F --> G[Composite Instability Score]
    G --> H[XAI Importance Attribution]
    H --> I[STAC XAI Metadata Assembly]
```

---

## 🧬 Normalization & Fusion

Each driver is normalized to prevent dominance:

```
cape_norm = CAPE / cape_scale
cin_norm  = CIN / cin_scale      (note CIN negative → normalization preserves sign)
shear_norm = shear / shear_scale
llj_norm   = llj / llj_scale
lr_norm    = lapse_rate / lr_scale
```

Composite score:

```
instability = w1*cape_norm + w2*(-cin_norm) + w3*shear_norm
            + w4*llj_norm + w5*lr_norm + w6*moisture_norm
```

Where:

- `w1...w6` are deterministic weights  
- All components MUST include metadata with units, CRS, vertical axes  

---

## 🧱 Inputs Required

### **Core Drivers**
- CAPE  
- CIN  
- Shear  
- LLJ  
- Lapse rates  

### **Secondary Drivers (Optional)**
- Moisture flux convergence  
- Dewpoint depressions  
- Surface lift indices  

### **Metadata**
- CRS: `EPSG:4326`  
- Vertical axis explicitly defined  
- Units included for all drivers  
- ISO 8601 timestamps  

### **Seed-Lock**
- Required for deterministic composite generation  
- Ensures reproducibility across refresh cycles  

---

## 📦 Outputs

The Instability Pack MUST produce:

- `instability_grid.tif`  
- `instability_metadata.json`  
- `instability_summary.json`  
- XAI attribution map  
- STAC Item for composite instability  
- Checksums (multihash)  
- Full PROV lineage block  

---

## 🔍 XAI Integration

XAI MUST provide:

- Contributions of CAPE, CIN, shear, LLJ, lapse rates  
- Sensitivity to changes in humidity or moisture transport  
- Explanation weights (w1–w6)  
- Temporal narrative (driver evolution)  

XAI metadata MUST include:

- Deterministic seeds  
- Model version  
- CARE scope  

---

## 🛡️ CARE + Sovereignty Enforcement

Composite instability MUST:

- Mask protected spatial regions  
- Smooth hyperlocal hot spots in sovereignty-limited domains  
- Attach explicit CARE metadata:

```json
{
  "care": {
    "masking": "h3-generalized",
    "scope": "public-generalized",
    "notes": ["Composite instability generalized within protected regions"]
  }
}
```

---

## 🧪 CI Validation Requirements

CI MUST check:

- Deterministic combination rules  
- Presence + validity of all base driver metadata  
- CRS + units consistency  
- STAC-XAI compliance  
- PROV-O lineage completeness  
- Proper CARE masking  
- Missing-field detection  

Failure → ❌ merge blocked.

---

## 🕰 Version History

| Version  | Date       | Notes                                                  |
|----------|------------|--------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial instability pack hazard driver documentation   |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Driver Models](../README.md) ·  
[🌡️ Climate Inference Root](../../README.md) ·  
[🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

