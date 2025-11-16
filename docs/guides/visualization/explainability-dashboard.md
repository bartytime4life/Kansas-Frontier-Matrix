---
title: "🔍 Kansas Frontier Matrix — Explainability Dashboard & AI Insight Visualization Guide (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/guides/visualization/explainability-dashboard.md"
version: "v10.4.2"
last_updated: "2025-11-16"
review_cycle: "Quarterly · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.2/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.2/manifest.zip"
telemetry_ref: "../../../releases/v10.4.2/pipeline-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/visualization-explainability-v2.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.2"
status: "Active / Enforced"
doc_kind: "Guide"
intent: "explainability-dashboard"
fair_category: "F1-A1-I1-R1"
care_label: "C2-A2-R2-E2"
kfm_readme_template: "Platinum v7.1"
ci_enforced: true
---

<div align="center">

# 🔍 **Kansas Frontier Matrix — Explainability Dashboard & AI Insight Visualization Guide**  
`docs/guides/visualization/explainability-dashboard.md`

**Purpose**  
Define the **architecture, visualization standards, and governance rules** of the **Explainability Dashboard** in the Kansas Frontier Matrix (KFM).  

The dashboard visualizes **Focus Mode AI reasoning**, **SHAP/LIME results**, **counterfactual analyses**, and **graph context**  
to support **transparency**, **auditability**, and **FAIR+CARE v2** alignment for all AI-assisted decisions and narratives.

</div>

---

# 📘 Overview

The Explainability Dashboard is the **primary UI surface** for:

- Inspecting **Focus Mode v2** and other AI model outputs  
- Understanding which features, datasets, and contexts the model uses  
- Examining **counterfactuals** and sensitivity analyses  
- Reviewing **AI behavior over time** (drift, performance, fairness)  
- Linking explainability to **Lineage v2** and **Governance Ledger** entries  

Key objectives:

- Provide **interactive evidence** behind AI outputs  
- Make AI decisions **auditable and contestable**  
- Surface **CARE v2** concerns (sensitivity, sovereignty, cultural data)  
- Capture **Telemetry v2** (latency, energy, fairness metrics)  
- Integrate with Focus Mode UI, Story Nodes, and MapLibre layers  

---

# 🗂️ Directory Context

~~~text
docs/guides/visualization/
├── README.md                        # Visualization overview
├── maplibre-ui-design.md            # Map-based UI framework
├── timeline-visualization.md        # Temporal storytelling interface
├── accessibility-standards.md       # Accessibility and inclusion governance
└── explainability-dashboard.md      # THIS document
~~~

Frontend components live in:

~~~text
web/src/components/ExplainabilityDashboard/
web/src/features/explainability/
~~~

---

# 🧩 Dashboard Architecture (GitHub-Safe Mermaid)

```mermaid
flowchart TD

A["Focus Mode / AI Outputs<br/>predictions · scores · explanations"] --> B["Explainability Engine<br/>SHAP · LIME · feature attributions"]
B --> C["Counterfactuals & Sensitivity<br/>what-if scenarios"]
C --> D["Visualization Layer<br/>React + charts (Plotly/Recharts)"]
D --> E["Telemetry v2 Collector<br/>latency · energy · fairness"]
E --> F["Governance & Lineage<br/>Ledger entries · audits"]
````

---

# 1️⃣ Component Overview (React)

| Component                 | Function                                                 | Libraries / Tools                      |
| ------------------------- | -------------------------------------------------------- | -------------------------------------- |
| `ExplainabilityDashboard` | Root container; wires data, layout, and state            | React + Feature state                  |
| `AttributionView`         | Feature importance plots (global/local SHAP, LIME)       | Plotly/Recharts/D3                     |
| `CounterfactualPanel`     | “What-if” exploration for parameters or scenario changes | Plotly/ECharts/Vega-Lite               |
| `FaithfulnessChart`       | Shows model faithfulness & calibration over time         | Recharts/Plotly                        |
| `InsightSummary`          | Text + small visuals summarizing AI decision reasoning   | React + Markdown                       |
| `ProvenanceGraphPanel`    | Visualizes data & entity provenance for given prediction | Graph visualization over Neo4j results |
| `EthicsReviewPanel`       | CARE v2 flags, risk levels, and reviewer comments        | FAIR+CARE Council integration          |
| `TelemetryHook`           | Collects frontend Telemetry v2 metrics                   | Telemetry API / writer                 |

---

# 2️⃣ Data Model for Explainability Outputs

Explainability outputs are typically produced by the AI pipeline and saved as JSON.

### 2.1 Local Explanation (Single Inference)

```json
{
  "explainability_id": "focus-explain-2025-11-16-0003",
  "model_id": "focus-transformer-v2",
  "task": "site-historical-inference",
  "entity_id": "storynode-1867-medicine-lodge",
  "prediction": "high-importance-site",
  "confidence": 0.91,
  "top_features": ["soil_moisture", "plat_1870", "distance_to_river"],
  "feature_attributions": {
    "soil_moisture": 0.32,
    "plat_1870": 0.27,
    "distance_to_river": 0.19,
    "elevation": -0.05
  },
  "counterfactuals": [
    {
      "description": "If distance_to_river increased by 2km",
      "prediction": "medium-importance-site",
      "confidence": 0.72
    }
  ],
  "faithfulness_score": 0.89,
  "faircare_status": "pass",
  "careLabel": "sensitive",
  "timestamp": "2025-11-16T12:00:00Z"
}
```

### 2.2 Global Summary

```json
{
  "model_id": "focus-transformer-v2",
  "shap_summary": {
    "soil_moisture": 0.31,
    "plat_1870": 0.29,
    "distance_to_river": 0.21,
    "slope": 0.11,
    "landcover_class": 0.08
  },
  "global_faircare_status": "pass",
  "last_updated": "2025-11-16T11:00:00Z"
}
```

---

# 3️⃣ Visualization Elements

| Visualization Type    | Description                                         | Data Source                                     |
| --------------------- | --------------------------------------------------- | ----------------------------------------------- |
| SHAP Summary Plot     | Feature importance across many samples              | `reports/ai/explainability/shap-summary.json`   |
| LIME Local Plot       | Local feature influence for a specific instance     | `reports/ai/explainability/lime-local.json`     |
| Counterfactual Matrix | Heatmap / table of “what-if” predictions            | `reports/ai/explainability/counterfactual.json` |
| Faithfulness Timeline | Time series of model calibration & fidelity         | Telemetry v2, model evaluation datasets         |
| Provenance Graph      | Shows which datasets/entities contributed to output | Neo4j queries + lineage references              |

Visuals must:

* Use colorblind-safe palettes
* Provide alt text & ARIA labels
* Provide numeric values on hover and for screen readers

---

# 4️⃣ FAIR+CARE v2 Integration for Explainability

Explainability dashboards must **not**:

* Reveal sensitive or restricted entities without CARE gating
* Expose raw PII or sensitive attributes in charts
* Present AI judgements without context, confidence, or limitations

Instead, they must:

* Display **CARE v2 classification** for each explanation (`careLabel`, `maskingStrategy`)
* Provide **disclaimers** and **method summaries** for each model
* Require extra confirmation for **restricted** contexts (e.g. sensitive cultural sites)

Explainability outputs feed into:

* Governance Ledger entries about model usage
* Lineage v2 for model outputs (**who** generated **what**, based on **which data**)
* FAIR+CARE risk review flows

---

# 5️⃣ Accessibility (WCAG 2.1 AA) in Explainability UI

Explainability views must:

* Provide textual equivalents for charts (table view or summary)

* Support keyboard navigation across:

  * Feature lists
  * Chart sections
  * Counterfactual scenarios

* Ensure color-coded signals (e.g., red vs green) are also available via shapes, icons, or text.

* Respect `prefers-reduced-motion` for animated transitions.

Use `docs/guides/visualization/accessibility-standards.md` for details, including:

* Minimum font sizes
* Contrast guidelines
* Screen-reader announcements for critical warnings

---

# 6️⃣ Telemetry v2 for Explainability

Explainability Dashboard interactions should emit Telemetry v2 events:

* `explainability:view` — view opened
* `explainability:feature-hover` — user hovered over a feature explanation
* `explainability:counterfactual-run` — user ran a what-if scenario
* `explainability:model-switch` — user switched between model versions
* `explainability:download-report` — user exported explanation data

Example Telemetry v2 event:

```json
{
  "pipeline": "web-ui",
  "stage": "explainability-runtime",
  "run_id": "exp-session-2025-11-16-0007",
  "status": "success",
  "duration_ms": 300000,
  "energy_wh": 0.008,
  "co2_g": 0.0031,
  "events": {
    "view_count": 5,
    "counterfactual_runs": 2,
    "model_switches": 1
  },
  "care_violations": 0,
  "timestamp": "2025-11-16T12:20:00Z"
}
```

---

# 7️⃣ CI/CD Validation Workflows (Explainability)

| Workflow                        | Purpose                                                  | Output Artifact                                             |
| ------------------------------- | -------------------------------------------------------- | ----------------------------------------------------------- |
| `ai-explainability.yml`         | Run SHAP/LIME/counterfactual computations                | `reports/ai/explainability/*.json`                          |
| `ui-accessibility-validate.yml` | Test dashboard accessibility (Lighthouse/axe)            | `reports/accessibility/explainability-ui.json`              |
| `telemetry-export.yml`          | Export interactions & resource metrics for the dashboard | `data/telemetry/explainability.ndjson`                      |
| `faircare-validate.yml`         | Validate ethical appropriateness of AI explanations      | `reports/faircare/explainability-audit.json`                |
| `lineage-validate.yml`          | Validate lineage v2 bundles for AI explanation flows     | `reports/lineage/ai-explainability-lineage-validation.json` |

These workflows must be required on branches that modify:

* `web/src/components/ExplainabilityDashboard/**`
* `src/pipelines/ai/explainability/**`
* `docs/guides/visualization/explainability-dashboard.md`

---

# 8️⃣ Example Governance Ledger Entry (Explainability)

```json
{
  "ledger_id": "explainability-ledger-2025-11-16-0001",
  "component": "Explainability Dashboard",
  "model_id": "focus-transformer-v2",
  "explainability_id": "focus-explain-2025-11-16-0003",
  "faithfulness_score": 0.89,
  "faircare_status": "pass",
  "careLabel": "sensitive",
  "lineageRef": "data/processed/lineage/ai/focus-explain-2025-11-16-0003.jsonld",
  "telemetryRef": "data/telemetry/explainability.ndjson",
  "timestamp": "2025-11-16T12:25:00Z",
  "auditor": "FAIR+CARE Council"
}
```

---

# 9️⃣ Developer Checklist (Explainability Dashboard)

Before shipping explainability changes:

* [ ] SHAP/LIME/counterfactual computations are correct and deterministic.
* [ ] Explainability JSON structure matches schemas.
* [ ] CARE v2 metadata attached to high-risk explanations (e.g., sensitive site inferences).
* [ ] A11y validations pass (charts + interactions accessible).
* [ ] Telemetry v2 events emitted for key interactions.
* [ ] Governance & lineage workflows updated for new model or context.

---

# 🕰 Version History

| Version | Date       | Summary                                                                                           |
| ------: | ---------- | ------------------------------------------------------------------------------------------------- |
| v10.4.2 | 2025-11-16 | Upgraded to KFM-MDP v10.4.2; integrated Telemetry v2, CARE v2, Lineage v2, CI validation patterns |
| v10.0.0 | 2025-11-09 | Initial explainability dashboard design with FAIR+CARE integration and accessibility compliance   |

---

<div align="center">

**Kansas Frontier Matrix — Explainability Dashboard (v10.4.2)**
AI Transparency × FAIR+CARE v2 × Accessible Explainability × Immutable Governance
© 2025 Kansas Frontier Matrix — CC-BY 4.0 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
