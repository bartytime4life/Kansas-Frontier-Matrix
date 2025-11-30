---
title: "🧪 KFM v11 — Soil AI Audit Suite (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/ai/soil/audits/README.md"
version: "v11.2.3"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability WG · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.3/soil-ai-audit-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/ai-soil-audit-suite-v11.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-Aware · Provenance-Logged · Sensitivity-Screened"
classification: "Public (Governed)"
sensitivity: "Low/Moderate"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "United States · Kansas"
---

<div align="center">

# 🧪 **KFM v11 — Soil AI Audit Suite**  
`docs/pipelines/ai/soil/audits/`

**Purpose**  
Define the governed **v11 soil-model audit suite**, covering:  
- **Data integrity audits** (GE),  
- **Performance drift detection**,  
- **Interpretability drift** (SHAP),  
- **Telemetry-logged reliability assessments**, and  
- **FAIR+CARE-aligned model auditing**  
for all AI pipelines using soil, terrain, hydric, or pedologic inputs.

This directory is the **parent index** for all soil AI audit modules.

</div>

---

## 📘 1. Overview

Soil-driven AI pipelines (suitability modeling, hydrologic surrogates, ecological forecasting,  
archaeological affordance models, etc.) must meet strict **governance, reliability, and  
interpretability requirements**.

The Soil AI Audit Suite provides:

- **Deterministic validation** of input data slices (Great Expectations)  
- **Reproducible baseline-vs-run model metric comparisons**  
- **SHAP-based interpretability drift detection** (global + local)  
- **OpenLineage provenance capture**  
- **Telemetry for energy, carbon, anomaly counts**  
- **CARE-aware handling of sensitive soil/landscape attributes**  
- **STAC/DCAT-aligned audit artifacts**  

This suite ensures that **soil-informed AI outputs remain trustworthy over time**, even as  
soil datasets refresh, upstream transformations shift, or new model versions deploy.

---

## 🗂️ 2. Directory Layout (Emoji-Prefix Standard)

~~~text
docs/pipelines/ai/soil/audits/
├── 📄 README.md                         # This file (root index)
│
├── 🧪 ge-shap/                           # GE + SHAP drift auditor (data, performance, interpretability)
│   ├── 📄 README.md
│   ├── 🧪 ge/
│   ├── 📊 baselines/
│   ├── 📁 runs/
│   ├── 🛠️ ci/
│   └── 📜 reports/
│
├── 🧾 metrics/                           # Canonical baseline metrics (MAE/RMSE/R²), thresholds, slices
│   ├── 📄 README.md
│   ├── 📄 soil-baselines.json
│   └── 📁 slices/
│
├── 🔍 explain/                           # Explainability tools (global/local SHAP profiles, PDP/ICE refs)
│   ├── 📄 README.md
│   ├── 🔍 global/
│   ├── 🔍 local/
│   └── 📊 reference/
│
├── 🧬 lineage/                           # Audit provenance models + trace bundles (PROV-O / STAC)
│   ├── 📄 README.md
│   ├── 🌐 prov-template.json
│   └── 🔗 lineage-rules.yml
│
└── 📦 stac/                              # Audit STAC Item/Collection templates (drift, baselines, audits)
    ├── 📄 README.md
    ├── 🗂️ collections/
    └── 🗂️ items/
~~~

---

## 🧬 3. Components of the Soil AI Audit Suite

### 3.1 GE (Great Expectations) — Data Integrity
Validates:

- Schema correctness  
- Categorical + numeric domain stability  
- Nulls, outliers, distribution drift  
- Stratified anomaly checks (ecoregion, soil group, land cover)

### 3.2 SHAP — Interpretability Drift
Detects:

- **Global drift** via Jensen–Shannon divergence  
- **Local drift** via cosine distance  
- Feature importance distribution shifts  
- Explanatory instability even when accuracy is flat

### 3.3 Metric Drift — Performance Reliability
- MAE, RMSE, R² deltas against frozen references  
- Governance thresholds prevent silent degradation  
- All deltas logged to telemetry + STAC

### 3.4 Model Baselines
- Frozen validation slices  
- Reference SHAP values  
- Reference metrics  
- Baseline STAC Items (governed artifacts)

### 3.5 Provenance + Telemetry
- OpenLineage provenance chains  
- Energy & carbon metrics  
- Dataset/model/version hash capture  
- Full audit-trail per run

### 3.6 CARE & Indigenous Sensitivity
- Pedologic attributes intersecting cultural landscapes flagged  
- Explainability surfaces masked when needed  
- Audit results tagged with CARE labels

---

## 🔗 4. Workflow Summary

~~~text
Model Inputs → GE Data Checks  
             → Baseline Comparisons  
             → SHAP Drift Analysis  
             → Lineage Capture  
             → Telemetry Emission  
             → STAC Audit Item  
             → Promotion / Block Decision
~~~

This process ensures **no soil-model version progresses** without:

- Valid data slice  
- Stable metrics  
- Stable interpretability  
- Clean provenance  
- Ethical review compliance

---

## 🔮 5. Roadmap (v11.3+)

- Multi-slice SHAP stratification (per soil taxonomy, land-cover class)  
- Unified audit dashboard in main KFM UI  
- Soil model “explainability maps” integration  
- Weighted drift scoring for ensemble models  
- Drift-driven root-cause suggestion engine  

---

## 🧩 6. Story Node Integration (Focus Mode v3)

Each audit run produces a **Story Node** with:

- Drift results  
- Impacted features  
- Sensitivity flags  
- Promotion decisions  
- Provenance+telemetry bundle linkage  

Focus Mode uses these to build **auditable data/AI timelines** across versions.

---

## 🏁 7. Version History

| Version | Date       | Summary                                                                    |
|--------:|------------|----------------------------------------------------------------------------|
| v11.2.3 | 2025-11-29 | Root audit suite created; aligned with GE+SHAP v11.2.3; emoji layout added |
| v11.2.2 | 2025-11-29 | Initial AI soil audit components established                               |

---

<div align="center">

🧪 **Kansas Frontier Matrix — Soil AI Audit Suite (v11.2.3)**  
FAIR+CARE · Explainable AI · Drift-Resilient Modeling · Full Provenance  

[📘 Docs Root](../../../..) · [🧪 AI Pipelines](../README.md) · [🛡 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

