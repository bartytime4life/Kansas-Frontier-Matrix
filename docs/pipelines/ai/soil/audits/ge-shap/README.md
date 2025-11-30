---
title: "🧪 KFM v11 — Soil Model GE + SHAP Drift Audit Layer (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/ai/soil/audits/ge-shap/README.md"
version: "v11.2.3"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council · Reliability WG"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.3/soil-ai-audit-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/ai-soil-audit-v1.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

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

# 🧪 **KFM v11 — Soil Model GE + SHAP Drift Audit Layer**  
### *Reproducibility • Interpretability • Lineage • Reliability*  
`docs/pipelines/ai/soil/audits/ge-shap/`

**Purpose:**  
A deterministic, reproducible, FAIR+CARE-aligned audit layer verifying  
**data integrity**, **model performance drift**, and **interpretability drift**  
using **Great Expectations (GE)** + **SHAP**,  
with complete governance telemetry and PROV-O lineage.

</div>

---

## 🗂️ 1. Directory Layout (Emoji-Prefix)

~~~text
docs/pipelines/ai/soil/audits/ge-shap/
├── 📄 README.md                         # This file
├── 🧪 ge/                               
│   ├── 📁 expectations/                 # Schema, ranges, missingness, stratified checks
│   ├── 📁 checkpoints/                  # CI-run GE checkpoint definitions
│   └── 📁 data_docs/                    # GE HTML reports (artifact-only; never committed)
│
├── 📊 baselines/
│   ├── 📄 metrics.json                  # Canonical MAE/RMSE/R² reference metrics
│   └── 🧠 shap_ref.parquet              # Frozen reference SHAP explanation slice
│
├── 📁 runs/
│   └── {YYYYMMDD}/                     # CI-stamped run folder
│       ├── 📄 metrics.json
│       └── 🧠 shap.parquet
│
├── 🛠️ ci/
│   └── 🔎 audit_gate.py                 # Deterministic, lineage-logged CI validation script
│
└── 📜 reports/                          # Machine-generated JSON summaries (for telemetry)
~~~

---

## 🧬 2. Overview

The Soil AI Audit Layer ensures **model trustworthiness** through three tightly governed dimensions:

### 2.1 Data Drift (GE)
- Schema mismatches  
- Value/range boundary violations  
- Null deviation  
- Distributional anomalies (per ecoregion, soil group, land-cover class)  

### 2.2 Performance Drift (Metrics)
- Baseline metrics frozen in `baselines/metrics.json`  
- Tolerances governed (default: **±5%** MAE/RMSE)  
- Violations halt promotion

### 2.3 Interpretability Drift (SHAP)
- Global reasoning drift via **Jensen–Shannon Divergence**  
- Local reasoning drift via **cosine feature-vector distance**  
- Thresholds governed (default: JSD ≤ 0.12, Cosine ≤ 0.18)  
- Detects “silent” failures where accuracy remains stable but reasoning changes

All results logged to STAC, PROV-O, and telemetry.

---

## 📦 3. GE: Data Integrity Validation

### 3.1 Enforced Expectations  
- Column schema & dtype signature  
- Numeric/categorical domain rules  
- Missing value constraints  
- Stratified tests across soil groups, ecoregions, land-cover regions  
- Variance/outlier stability vs reference distribution

### 3.2 Execution Rules  
- All GE checks anchored to a **fixed validation slice**  
- GE checkpoint failures = **hard CI stop** unless explicitly governance-exempted  
- HTML reports never committed (artifact-only)

---

## 🔍 4. SHAP: Interpretability Drift Detection

### 4.1 Why Interpretability Drift Matters  
Two model versions can show similar accuracy yet **explain their predictions differently**  
→ this can undermine scientific trust in soil suitability, hydrology models, and archaeological inference.

### 4.2 Baseline vs Run  
- Baseline slice stored in:  
  `baselines/shap_ref.parquet`  
- Current run stored in:  
  `runs/<DATE>/shap.parquet`

### 4.3 Drift Metrics  
- **Global JSD:**  
  Drift in absolute |SHAP| mean distributions  
- **Local Cosine Distance:**  
  Drift across random k-sample rows  

### 4.4 Governance Thresholds  
- `JSD ≤ 0.12`  
- `local cosine median ≤ 0.18`  

Violations: **stop promotion**, log to telemetry, create STAC Issue Item.

---

## ⚙️ 5. CI Audit Gate (Python Reference)

~~~python
# audit_gate.py (excerpt)
import json, pandas as pd, numpy as np
from scipy.spatial.distance import jensenshannon
from numpy.linalg import norm

BASE = "baselines/"
RUN = "runs/{stamp}/"

ref = pd.read_parquet(BASE + "shap_ref.parquet").abs()
cur = pd.read_parquet(RUN  + "shap.parquet").abs()

def normalize(v):
    s = v.sum()
    return v / s if s > 0 else v

ref_g = normalize(ref.mean())
cur_g = normalize(cur.mean())
jsd = float(jensenshannon(ref_g.values, cur_g.values))

if jsd > 0.12:
    exit(2)

# Local drift
k = 64
idx = np.random.choice(min(len(ref), len(cur)), k, replace=False)
local = []
for i in idx:
    a, b = ref.iloc[i].values, cur.iloc[i].values
    cos = 1 - (np.dot(a, b) / (norm(a)*norm(b) + 1e-12))
    local.append(float(cos))

if float(np.median(local)) > 0.18:
    exit(3)

# Performance drift
with open(BASE + "metrics.json") as f: base = json.load(f)
with open(RUN  + "metrics.json") as f: curr = json.load(f)

def pct(a, b): return (b - a) / max(abs(a), 1e-9)

if pct(base["mae"], curr["mae"]) > 0.05 or pct(base["rmse"], curr["rmse"]) > 0.05:
    exit(4)

exit(0)
~~~

---

## 🛡️ 6. Lineage • Provenance • Telemetry

Each audit run emits:

### 📌 Lineage (PROV-O)
- Dataset hashes  
- Model version  
- Validation slice ID  
- SHAP baseline & run hashes  
- Metrics deltas  
- Full CI environment capture  

### 📡 Telemetry
- Drift results (JSD, cosine, metrics deltas)  
- `energy_wh`, `carbon_gco2e`  
- Records processed  
- Any GE/SHAP anomalies  

### 🌐 STAC Integration
For every audit run, a STAC Item is posted containing:

- Drift metrics  
- Decision outcome  
- Provenance references  
- Telemetry bundle  

---

## 🔮 7. Roadmap (v11.3+)

- Stratified interpretability drift by soil taxonomy  
- Multi-slice SHAP monitoring  
- UI drift dashboards  
- Automatic RCA suggestions  
- Integration with change-aware soil refresh triggers  

---

## 🧩 8. Story Node Integration (Focus Mode v3)

Each audit run generates a **Story Node**, including:

- Drift summary (data, performance, interpretability)  
- Affected features & soil units  
- Provenance chain  
- Promotion decision rationale  
- Sensitivity/CARE tags  

Focus Mode uses these to explain soil model changes over time.

---

## 🏁 9. Version History

| Version | Date       | Summary                                                                            |
|--------:|------------|------------------------------------------------------------------------------------|
| v11.2.3 | 2025-11-29 | Aligned with KFM-MDP v11.2.2; updated fences; telemetry + STAC linkage improved.  |
| v11.2.2 | 2025-11-29 | Initial GE+SHAP drift audit release; baseline/SHAP slices formalized.              |

---

<div align="center">

**Kansas Frontier Matrix — Open, Ethical, Reliable**  
FAIR+CARE · Provenance-Driven · Drift-Audited AI Pipelines  

[📘 Docs Root](../../../..) · [🧪 AI Pipelines](../../README.md) · [🛡 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
