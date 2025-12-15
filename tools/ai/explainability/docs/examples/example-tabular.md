---
title: "🧪 KFM — Explainability Example: Tabular Attribution (Synthetic)"
path: "tools/ai/explainability/docs/examples/example-tabular.md"

version: "v11.2.6"
last_updated: "2025-12-15"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous · FAIR+CARE Council Oversight"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Guide"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:doc:tools-ai-explainability-example-tabular:v11.2.6"
semantic_document_id: "kfm-doc-tools-ai-explainability-example-tabular"
event_source_id: "ledger:tools/ai/explainability/docs/examples/example-tabular.md"
immutability_status: "mutable-plan"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

# Update these refs to your governed “current release” bundle when available.
sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"

telemetry_ref: "../../../../../releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/tools-ai-governance-v4.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

json_schema_ref: "../../../../../schemas/json/tools-ai-explainability-example-v11.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/tools-ai-explainability-example-v11.shape.ttl"

fair_category: "F1-A1-I2-R3"
care_label: "Public · Low-Risk"
classification: "Public"
jurisdiction: "United States · Kansas"

sensitivity: "General"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_data_flag: false
risk_category: "Low"
redaction_required: false

ai_training_allowed: false
ai_training_guidance: "Explainability examples and governance artifacts MUST NOT be used as training data."

machine_readable: true
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "Annual review"
sunset_policy: "Superseded upon next explainability platform update"

provenance_chain:
  - "tools/ai/explainability/docs/examples/README.md@v11.2.6"
---

<div align="center">

# 🧪 **KFM Explainability Example — Tabular Attribution (Synthetic)**
`tools/ai/explainability/docs/examples/example-tabular.md`

**Purpose**  
Demonstrate a **policy-safe tabular explainability bundle** (global + local attributions) using **synthetic values only**, with KFM’s required metadata, integrity placeholders, and governance constraints.

</div>

---

## 📘 Overview

This document is a **toy example** of a tabular explainability output that can be:

- validated by schemas and CI checks,
- stored as a governed run artifact,
- rendered in Focus Mode / operator dashboards (when allowed),
- audited without exposing raw records or sensitive locations.

### What this example demonstrates

- A **manifest** describing an explainability artifact set (identity, safety flags, file inventory).
- An **explanation payload** with:
  - global feature importance (summary)
  - local attribution for one synthetic “case”
  - confidence/quality fields suitable for governance (not marketing)
- **Reference-first** patterns:
  - dataset/model IDs, config refs, provenance pointers
  - checksums placeholders (sha256) for integrity

### What this example intentionally avoids

- Any real-world records, coordinates, protected-site data, or sensitive imagery
- Any PII
- Any secrets/tokens/credentials
- Any “small group drilldown” that could enable re-identification

---

## 🗂️ Directory Layout

This file lives in the explainability examples folder:

~~~text
📁 tools/
└── 🧠 ai/
    └── 🧩 explainability/
        └── 📁 docs/
            └── 📁 examples/
                ├── 📄 README.md
                └── 📄 example-tabular.md              # This file
~~~

Recommended pairing for a self-contained example bundle (create if/when you want a runnable demo set):

~~~text
📁 tools/
└── 🧠 ai/
    └── 🧩 explainability/
        └── 📁 docs/
            └── 📁 examples/
                └── 📁 tabular/
                    ├── 🧾 example_manifest.json       # Artifact inventory + safety flags (synthetic)
                    ├── 🧾 explanation.json            # Global + local attributions (synthetic)
                    └── 📄 notes.md                    # What the example demonstrates (synthetic)
~~~

**Normative rule:** examples in `docs/examples/` MUST remain small and synthetic; real run artifacts belong under governed run folders (e.g., `mcp/experiments/<run-id>/...`).

---

## 🧭 Context

### When tabular explainability is used in KFM

Tabular explainability patterns are used when models operate on structured inputs, such as:

- hydrology and climate predictors (time-window aggregates)
- risk scoring (hazard indices, drought indicators)
- classification/regression over engineered features
- retrieval/ranking features (aggregate-only; never raw sensitive content)

### What “attribution” means here

This example uses the concept of **feature attribution**:

- **global attribution**: “which features generally mattered most”
- **local attribution**: “which features pushed this one output up/down”

KFM treats attribution artifacts as:

- governance evidence (what influenced the model),
- not proof of causation,
- and not a substitute for domain review.

### Safety notes specific to Kansas-scale data

Even tabular data can be sensitive if it encodes:

- protected site proximity,
- fine-grained coordinates,
- or sparse cohort identifiers.

Therefore:

- avoid raw coordinates and exact site distances in explanations,
- prefer coarse region classes or generalized spatial indices if needed,
- suppress subgroup attributions when group sizes are too small.

---

## 🗺️ Diagrams

### Explainability artifact lifecycle (tabular)

~~~mermaid
flowchart TD
  A["Model inference or evaluation<br/>model_id + version/hash"] --> B["Select explainer profile<br/>(config-driven)"]
  B --> C["Compute attributions<br/>(global + local)"]
  C --> D["Safety gate<br/>(no PII/coords; suppress small groups)"]
  D --> E["Validate<br/>(schema + integrity + determinism)"]
  E --> F["Store artifact set<br/>(run_id folder)"]
  F --> G["Register refs<br/>(registry + provenance pointers)"]
  G --> H["Render (if allowed)<br/>(Focus Mode / dashboards)"]
~~~

Accessibility note: the process generates attributions, applies safety rules, validates, stores, registers, and optionally renders.

---

## 📦 Data & Metadata

This section shows **illustrative** JSON shapes. Replace placeholder IDs/hashes with real governed values in real runs.

### Example 1: `example_manifest.json` (illustrative)

~~~json
{
  "example_id": "explainability_example_tabular_v1",
  "example_version": "11.2.6",
  "example_kind": "tabular",
  "created": "2025-12-15T00:00:00Z",

  "model": {
    "model_id": "demo_hydro_tabular_regressor",
    "model_version": "demo",
    "model_hash": "<sha256>"
  },

  "dataset": {
    "dataset_id": "dcat:kfm:dataset:demo-hydro-features",
    "dataset_version": "demo"
  },

  "config": {
    "explainer_profile_ref": "tools/ai/configs/domains/hydrology/explainability.json",
    "config_sha256": "<sha256>"
  },

  "artifacts": [
    { "path": "explanation.json", "media_type": "application/json", "sha256": "<sha256>" }
  ],

  "safety": {
    "classification": "Public",
    "care_label": "Public · Low-Risk",
    "contains_pii": false,
    "contains_secrets": false,
    "contains_sensitive_locations": false,
    "small_group_suppression_applied": false
  },

  "refs": {
    "telemetry_ref": "mcp/experiments/<run-id>/telemetry.json",
    "provenance_bundle_ref": "mcp/experiments/<run-id>/provenance_bundle.jsonld"
  },

  "notes": "Synthetic-only example showing tabular attributions. No real records."
}
~~~

### Example 2: `explanation.json` (illustrative)

This payload includes:

- global feature importance
- one local explanation for a single synthetic case
- quality + governance fields

~~~json
{
  "explanation_set_id": "demo_tabular_attributions_v1",
  "schema_version": "11.2.6",
  "created": "2025-12-15T00:00:00Z",

  "scope": {
    "model_id": "demo_hydro_tabular_regressor",
    "model_version": "demo",
    "dataset_id": "dcat:kfm:dataset:demo-hydro-features",
    "dataset_version": "demo",
    "task_type": "regression"
  },

  "method": {
    "explainer_id": "shap_like_attribution",
    "explainer_version": "1.0.0",
    "notes": "Synthetic numbers; attribution-like structure only."
  },

  "global": {
    "feature_importance": [
      { "feature": "precip_30d_mm", "importance": 0.42 },
      { "feature": "soil_moisture_index", "importance": 0.27 },
      { "feature": "temp_7d_c", "importance": 0.19 },
      { "feature": "slope_deg", "importance": 0.12 }
    ],
    "importance_normalization": "sum_to_1",
    "interpretation": "Higher importance indicates greater average contribution magnitude."
  },

  "local": [
    {
      "case_id": "demo_case_0001",
      "prediction": {
        "value": 0.73,
        "unit": "normalized_risk_index",
        "baseline_value": 0.50
      },
      "attributions": [
        { "feature": "precip_30d_mm", "value": 48.0, "contribution": 0.18 },
        { "feature": "soil_moisture_index", "value": 0.62, "contribution": 0.09 },
        { "feature": "temp_7d_c", "value": 6.5, "contribution": -0.03 },
        { "feature": "slope_deg", "value": 2.1, "contribution": -0.01 }
      ],
      "contribution_semantics": "positive_increases_prediction",
      "notes": "Synthetic case; values are toy-scale."
    }
  ],

  "quality": {
    "explainability_coverage_score": 0.99,
    "warnings": [],
    "limitations": [
      "Attributions are not causal.",
      "Synthetic demonstration only."
    ]
  },

  "governance": {
    "classification": "Public",
    "care_label": "Public · Low-Risk",
    "redaction_applied": false,
    "suppression_applied": false,
    "reason_codes": []
  },

  "refs": {
    "baseline_ref": "mcp/experiments/<baseline-run-id>/baseline.json#sha256:<sha256>",
    "window_ref": "mcp/experiments/<run-id>/window_summary.json#sha256:<sha256>",
    "telemetry_ref": "mcp/experiments/<run-id>/telemetry.json",
    "provenance_bundle_ref": "mcp/experiments/<run-id>/provenance_bundle.jsonld"
  }
}
~~~

### Human-readable interpretation (safe)

- The model’s **largest global driver** is `precip_30d_mm` in this synthetic example.
- For the synthetic case, precipitation and soil moisture push the prediction upward.
- Temperature and slope slightly reduce the prediction.
- These statements are interpretability aids, not causal claims.

---

## 🧪 Validation & CI/CD

### Example validation checklist (recommended)

For this example bundle (and for real runs), validation SHOULD include:

- **JSON validity** for `example_manifest.json` and `explanation.json`
- **Schema validation** against the governed schema (when present)
- **Determinism checks**:
  - stable ordering for arrays like `feature_importance` and `attributions`
  - fixed rounding (documented if applied)
- **Safety checks**:
  - no secrets
  - no PII
  - no protected-site coordinates
  - no raw record dumps
- **Reference completeness**:
  - model identity present
  - dataset identity present
  - config ref + sha256 present
  - provenance/telemetry pointers present (or explicitly null/omitted for docs-only examples)

### Fail-closed guidance (normative for governed runs)

If any of these are missing or ambiguous in a governed environment:

- classification / sensitivity fields
- dataset/model identity
- config reference
- safety scan results

…then the explainability output MUST be treated as **non-displayable**, and certification-dependent flows should fail closed.

---

## ⚖ FAIR+CARE & Governance

### Why explainability can increase risk if done poorly

Explainability outputs can leak more than model outputs if they:

- reveal sensitive locations through “top features” (e.g., distance-to-site),
- expose rare subgroup signals,
- include raw records for “debugging.”

Therefore, KFM requires:

- **aggregate-first** reporting,
- **reference-first** artifacts,
- **suppression and redaction** when needed,
- explicit governance flags and reason codes.

### Minimal governance commitments for tabular explanations

- No raw IDs that map to individuals or protected locations.
- No precise coordinates.
- No small subgroup breakdown without governance approval.
- Attributions are not used as a sole decision basis; they are audit support.

### Training prohibition

Even examples are governance artifacts: this example and its JSON shapes MUST NOT be used as training data.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v11.2.6** | 2025-12-15 | Added synthetic tabular explainability example: manifest + explanation payload shapes (global/local attributions), safety flags, reference-first provenance pointers, and CI validation checklist. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
🧪 Tabular Explainability Example · Synthetic · Governed for Integrity

[⬅️ Examples Index](./README.md) ·
[⬅️ Explainability Docs](../README.md) ·
[⬅️ Explainability](../../README.md) ·
[🛡 Governance](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

