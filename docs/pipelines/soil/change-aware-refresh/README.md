---
title: "🧩 KFM v11 — Soil & Terrain Change-Aware Refresh Pipeline (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/soil/change-aware-refresh/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Soil Systems · FAIR+CARE Council"
backward_compatibility: "Aligned with v10.x → v11.x ETL transformation rules"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../../releases/v11.2.2/signature.sig"
attestation_ref: "../../../../releases/v11.2.2/slsa-attestation.json"
sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"

telemetry_ref: "../../../../releases/v11.2.2/soil-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/soil-change-aware-refresh-v1.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
status: "Active / Enforced"
doc_kind: "Pipeline Module"
intent: "soil-change-aware-refresh"
fair_category: "F1-A2-I1-R1"
care_label: "CARE · Indigenous Data Sensitivity (Low/Moderate · Monitored)"
classification: "Public"
sensitivity: "Low"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "United States · Kansas"
---

<div align="center">

# 🧩 **KFM v11 — Soil & Terrain Change-Aware Refresh Pipeline**
### *Dynamic Drift-Driven Updates for SDA, gNATSGO & Terrain Layers*

**Purpose**  
Enable soil & terrain datasets to refresh **only when upstream change signals justify it**, reducing compute cost,  
storage churn, and energy/carbon, while maintaining scientific integrity across hydrology, archaeology, ecology,  
climate science, and land-cover modeling.

</div>

---

## 🌱 1. Overview

The **Change-Aware Refresh Pipeline** introduces a governed, evidence-based **drift detection model** for soil  
and terrain datasets, enabling:

- **Skip** — negligible drift  
- **Subset-Rebuild** — localized H3 region drift  
- **Full-Rebuild** — red-level drift (schema or spatial topology changes)

Every decision is captured as a **signed STAC Item** with full provenance & telemetry.

---

## 🔁 2. Core Logic

### 2.1 Upstream Triggers
- SDA release notifications  
- gNATSGO annual/minor updates  
- KS DEM/LiDAR tile refresh  
- lakeFS commits  
- Manual override (Soil Systems WG)

### 2.2 Drift Signals
- **Schema Drift**: field diffs, renames, type/unit changes  
- **Value Drift**: categorical/numerical shifts  
- **Statistical Drift**: PSI, KL, KS tests  
- **Spatial Drift**: H3 area fraction changed  
- **External Drift**: upstream version jumps, metadata mutations

### 2.3 Threshold Logic

| Level | Meaning | Action |
|-------|---------|--------|
| Green | negligible | Skip |
| Amber | localized | Subset-Rebuild |
| Red   | major/schema | Full-Rebuild |

### 2.4 Decision → STAC Item  

The pipeline emits a machine-discoverable STAC record with drift signals + action + lineage + energy/carbon.

---

## 📏 3. Drift Threshold Table

| Drift Type | Metric | Green | Amber | Red |
|------------|--------|-------|--------|------|
| Schema | field diff count | 0 | 1–2 | ≥3 or type change |
| Value Dist. | PSI | <0.10 | 0.10–0.25 | ≥0.25 |
| Numeric Dist. | KS-test p | >0.20 | 0.05–0.20 | <0.05 |
| Categorical | enum delta | none | minor | new/removed enum |
| Spatial | area changed | <2% | 2–12% | ≥12% |
| Upstream | version bump | patch | minor | major |

---

## 🗄️ 4. Decision Record Schema

~~~json
{
  "layer": "soil_gNATSGO_v2025",
  "time_window": { "start": "2025-10-01", "end": "2025-11-01" },
  "signals": [
    { "name": "psi", "metric": "psi", "value": 0.04, "threshold": "green", "status": "green" },
    { "name": "schema", "metric": "field_diff", "value": 0, "threshold": "green", "status": "green" }
  ],
  "action": "skip",
  "scope": { "h3_res": 6, "cells_touched": 0, "pct_area": 0.0 },
  "lineage_refs": {
    "upstream": [],
    "lakefs_commit": "<hash>",
    "stac_items": []
  },
  "cost_energy": { "cpu_seconds": 0, "kwh": 0.0, "co2e": 0.0 },
  "slo": { "freshness_ok": true, "max_age_days": 60 }
}
~~~

---

## 🧬 5. Integration with KFM Systems

### 5.1 LangGraph DAG
- Deterministic transitions: `IDLE → EVALUATE → SKIP/SUBSET/FULL`  
- Idempotent soil transformations  
- WAL semantics with lakeFS  
- v10.x→v11.x compatibility transforms

### 5.2 OpenTelemetry & OpenLineage
- Drift metrics exported as OTel metrics  
- OpenLineage events before/after rebuild  
- Drift decisions encoded in `refresh_decision` facet

### 5.3 CARE & Indigenous Sensitivity
- Some soil/hydric units overlap archaeologically sensitive zones  
- H3 generalization prevents overexposure  
- CARE policies govern masking + downstream controls

---

## 📂 6. Directory Layout (Emoji-Prefix)

~~~text
docs/pipelines/soil/change-aware-refresh/
├── 📄 README.md
├── 📊 signals.yml
├── 🧾 decision-schema.json
├── 🧠 dag/
│   ├── 🧩 refresh_dag.py
│   └── 🧰 utils.py
├── 🌐 stac/
│   ├── 🧾 template.json
│   └── 📁 examples/
└── 🧪 tests/
    ├── 🧪 test_signals.py
    └── 🧪 test_partition_diff.py
~~~

---

## 🪶 7. FAIR+CARE Alignment

- **FAIR:** full provenance, explicit versioning, STAC Items  
- **CARE:** masking for sensitive areas, avoids unnecessary over-refresh  
- **Sustainability:** logs energy/carbon for refresh decisions

---

## 🧭 8. Version History

| Version | Date | Summary |
|--------:|------|---------|
| v11.2.2 | 2025-11-29 | Initial governed release of Change-Aware Refresh pipeline |

---

<div align="center">

🌱 **Kansas Frontier Matrix — Soil Systems v11.2.2**  
FAIR+CARE · Sustainable Intelligence · Drift-Aware ETL  

[📘 Docs Root](../../../..) · [🧪 Pipelines](../../README.md) · [🛡 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
