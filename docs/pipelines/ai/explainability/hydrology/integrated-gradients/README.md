---
title: "💧⚡ KFM v11 — Hydrology Integrated Gradients Explainability (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/ai/explainability/hydrology/integrated-gradients/README.md"
version: "v11.2.3"
last_updated: "2025-11-29"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Hydrology AI WG · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-version-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.3/manifest.zip"
attestation_ref: "../../../../../../releases/v11.2.3/slsa-attestation.json"
signature_ref: "../../../../../../releases/v11.2.3/signature.sig"

telemetry_ref: "../../../../../../releases/v11.2.3/hydro-ig-explainability-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/ai-explainability-hydro-integrated-gradients-v11.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

doc_kind: "Explainability Module"
intent: "hydrology-integrated-gradients-explainability"
fair_category: "F1-A1-I1-R2"
care_label: "CARE-Compliant · Watershed-Sensitive"

classification: "Public (Governed)"
sensitivity: "Low/Moderate (Watershed/tribal hydrology sensitivity)"
machine_extractable: true
jurisdiction: "United States · Kansas"
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# 💧⚡ **Hydrology Integrated Gradients Explainability (KFM v11)**  
`docs/pipelines/ai/explainability/hydrology/integrated-gradients/`

**Purpose**  
Provide the official **v11 Integrated Gradients (IG)** explainability framework for hydrology AI pipelines  
that rely on differentiable models (CNNs, U-Nets, LSTMs, transformers, hybrid physics+AI surrogates).

This template enforces **FAIR+CARE-compliant**, **provenance-rich**, **energy-aware**,  
**watershed-safe** explainability for watershed-scale prediction models.

</div>

---

## 📘 1. Overview

Hydrology AI often uses complex spatiotemporal inputs:

- CAMS atmospheric fields  
- Soil moisture / soil type  
- DEM + terrain derivatives  
- Hydric soils / infiltration indices  
- Landcover transitions  
- Watershed boundaries (HUC4–HUC12)  

Integrated Gradients is needed because:

- It provides **axiomatic, model-faithful attribution**  
- Supports **spatial gradients** across watersheds and hex grids  
- Works with both **temporal** (RNN/LSTM/transformer) and **spatial** (CNN/U-Net) models  
- Generates explainability surfaces suitable for hydrology-focused Focus Mode narratives

---

## 🗂️ 2. Directory Layout (Emoji-Prefix Standard)

~~~text
docs/pipelines/ai/explainability/hydrology/integrated-gradients/
├── 📄 README.md
│
├── ⚡ templates/
│   ├── 📊 ig_global_template.parquet
│   ├── 📍 ig_local_template.parquet
│   ├── 🕒 ig_temporal_template.parquet
│   └── 🧭 ig_h3_template.parquet
│
├── 🌐 stac/
│   ├── 📄 item-template.json
│   └── 📄 collection-template.json
│
├── 🔗 lineage/
│   ├── 🧾 prov-template.json
│   └── 📡 ol-template.json
│
├── 🧪 validation/
│   ├── 📄 validate-integrity.md
│   ├── 📄 validate-huc-watersheds.md
│   ├── 📄 validate-cams-hydro-linkage.md
│   ├── 📄 validate-h3.md
│   └── 📄 validate-sustainability.md
│
└── 📊 examples/
    ├── 📁 global/
    ├── 📁 local/
    ├── 📁 temporal/
    └── 📁 h3/
~~~

---

## ⚙️ 3. IG Explainability Standards (v11)

### Required Metadata

| Field | Description | Required |
|------|-------------|----------|
| `model:version` | AI hydrology model version | ✔ |
| `kfm:domain` | `"hydrology"` | ✔ |
| `kfm:explainability_method` | `"integrated-gradients"` | ✔ |
| `kfm:input_variables` | CAMS + hydrology variables | ✔ |
| `baseline_description` | Baseline used for IG integration | ✔ |
| `integration_steps` | # of integration steps | ✔ |
| `datetime` | Timestamp for inference window | ✔ |
| `watershed_id` | HUC-level ID or hydrology region | ✔ |
| CRS | EPSG:4326 (unless H3) | ✔ |
| `kfm:h3_res` | Required for hex attribution | conditional |
| `kfm:sensitivity_flag` | CARE/sovereignty handling | ✔ |
| `kfm:energy_wh` | Compute energy used | ✔ |
| `kfm:carbon_gco2e` | CO₂ equivalent | ✔ |

### Supported Output Types

- **IG Global Attribution** — watershed-scale  
- **IG Local Attribution** — per-grid / per-H3-cell  
- **IG Temporal Attribution** — storm-window contributions  
- **IG H3 Attribution** — privacy-preserving watershed explainability  

---

## 🧪 4. Validation (v11)

### ✔ Hydrologic & Spatial Integrity  
- Attribution grid must align with watershed/HUC/DEM resolution  
- CAMS/hydro linkage validated (precip → infiltration, humidity → ET, aerosols → SM)  
- No NaN/inf values  
- CRS/H3 resolution consistent  

### ✔ Metadata Completeness  
- All required fields populated in STAC & JSON-LD  
- Watershed identifiers correct  
- Input variables listed  
- IG baseline fully documented  

### ✔ CARE/Sovereignty  
- Sensitive tribal waters masked/fuzzed  
- H3 R7–R9 enforced in sensitive locations  
- CARE flag required  

### ✔ Sustainability  
- Energy/carbon < hydrology explainability budget  
- Logged to telemetry and STAC  

Validation failures → rollback via Reliability Layer v11.

---

## 🌐 5. STAC Metadata Templates

IG outputs MUST publish a STAC Item with:

- `datetime`  
- `model:version`  
- `watershed_id`  
- `kfm:explainability_method="integrated-gradients"`  
- `kfm:energy_wh`  
- `kfm:carbon_gco2e`  
- Attribution asset links  
- Provenance references (OpenLineage + PROV-O)

Stored under:

~~~text
stac/item-template.json
stac/collection-template.json
~~~

---

## 🔗 6. Provenance (OpenLineage + PROV-O)

Each IG run MUST emit:

### PROV-O
- `prov:Activity` — IG computation  
- `prov:used` — CAMS inputs + hydrology data  
- `prov:generated` — IG attribution surfaces  
- `prov:wasAssociatedWith` — executing agent  

### OpenLineage
- `runId`  
- Dataset pointers  
- Runtime & event metadata  

Stored under:

~~~text
lineage/prov-template.json
lineage/ol-template.json
~~~

---

## 📡 7. Telemetry (OTel v11)

Each hydrology IG run MUST output:

- `kfm.expl_method="hydrology-ig"`  
- `kfm.expl_energy_wh`  
- `kfm.expl_carbon_gco2e`  
- `kfm.rows_processed`  
- `kfm.expl_latency_ms`  
- GPU/CPU/memory usage  

Telemetry MUST be attached to STAC + lineage events.

---

## 🔮 8. Story Node Integration (Focus Mode v3)

Hydrology IG outputs MUST generate Story Nodes describing:

- Key hydrologic drivers  
- Watershed-scale attribution patterns  
- Event-scale impacts (storms, drought windows)  
- Sensitivity to CAMS variables  
- CARE masking decisions  
- Lineage + sustainability context  

These nodes drive **explainable watershed narratives** across KFM.

---

## 🧭 9. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.3 | 2025-11-29 | Initial v11 IG explainability template for hydrology; full lineage/telemetry/CARE integration. |

---

<div align="center">

💧⚡ **Kansas Frontier Matrix — Hydrology Integrated Gradients Explainability (v11.2.3)**  
Watershed-Safe · Explainable · FAIR+CARE · Provenance-Driven  

[📘 Docs Root](../../../../../..) · [🧠 Hydrology Explainability](../README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>