---
title: "📊 Kansas Frontier Matrix — Explainability Examples: Tabular"
path: "tools/ai/explainability/docs/examples/tabular/README.md"

version: "v11.2.6"
last_updated: "2025-12-16"
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

doc_uuid: "urn:kfm:doc:tools-ai-explainability-examples-tabular-readme:v11.2.6"
semantic_document_id: "kfm-doc-tools-ai-explainability-examples-tabular"
event_source_id: "ledger:tools/ai/explainability/docs/examples/tabular/README.md"
immutability_status: "mutable-plan"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

# NOTE: These refs should point to your governed "current release" bundle.
# If the repo has a newer release packet than v11.2.2, update these paths.
sbom_ref: "../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.2/focus-telemetry.json"

governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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
ai_training_guidance: "Explainability examples and example outputs MUST NOT be used as training data."

machine_readable: true
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "Annual review"
sunset_policy: "Superseded upon next AI-tools platform update"

provenance_chain:
  - "tools/ai/explainability/docs/examples/README.md@v11.2.6"
---

<div align="center">

# 📊 **KFM — Explainability Examples: Tabular**
`tools/ai/explainability/docs/examples/tabular/README.md`

**Purpose**  
Provide **tabular-model explainability example patterns** for Kansas Frontier Matrix (KFM):  
how to generate, validate, and publish **policy-safe** explanation bundles for structured (row/column) models—**with provenance, governance flags, and Focus Mode compatibility**.

</div>

---

## 📘 Overview

### What “tabular” means in KFM

In KFM, **tabular** refers to structured rows where each row represents an observation such as:

- a **place-time unit** (e.g., county-month, watershed-week, H3-cell-day),
- an **entity-time unit** (e.g., facility-year, event-window),
- a **document-derived feature vector** (e.g., counts, embeddings, retrieval features),
- a **model input frame** for forecasting or scoring (e.g., hydrology predictors, climate indices, risk scores).

Tabular models can be:

- linear / GLM family (logistic regression, Poisson, etc.)
- tree/ensemble (random forest, gradient-boosted trees)
- shallow neural nets for structured features
- time-series features presented as tabular (lags/rolling features)  
  *(time-series-specific explanations still count as “tabular” here if the model consumes a feature table)*

### What these examples cover

This folder documents **example patterns** for producing explainability artifacts for tabular workloads, including:

- **Global importance** (what features generally matter)
- **Local explanations** (what mattered for a specific row / prediction)
- **Stability checks** (do explanations change wildly if you resample backgrounds)
- **Redaction rules** (PII/protected attribute safety, small-N safety)
- **Provenance binding** (model hash, dataset version, config hash, run ID)
- **Publishing rules** (what can live in docs vs what must remain in `mcp/experiments/`)

### What these examples intentionally avoid

To stay compliant and reusable:

- No real sensitive records (no PII, no protected-site coordinates, no restricted data slices)
- No assumptions about a specific ML stack (SHAP/LIME are referenced as common methods, but the docs remain tool-agnostic)
- No “magic” hidden network calls in workflows (examples assume deterministic offline operation)

### Core invariants

1. Explainability MUST be **traceable** (model + dataset + config + run IDs).
2. Explainability MUST be **policy-safe** (no secrets, no PII, no restricted coordinates).
3. Explainability MUST be **reproducible** (config-driven, seeded where sampling occurs).
4. Explainability MUST be **honest**:
   - “explanation ≠ proof”
   - treat results as evidence about model behavior, not truth about the world.

---

## 🗂️ Directory Layout

This folder is part of the Explainability examples tree:

~~~text
📁 tools/
└── 🧠 ai/
    └── 📁 explainability/
        └── 📁 docs/
            └── 📁 examples/
                ├── 📄 README.md                         # Examples index (overview)
                ├── 📄 example-tabular.md                # Tabular walkthrough (long-form)
                ├── 📄 example-narrative.md              # Narrative walkthrough (long-form)
                ├── 📄 example-remote-sensing.md         # Remote-sensing walkthrough (long-form)
                │
                ├── 📁 integrity/                        # Guardrails for examples
                │   └── 📄 README.md
                ├── 📁 narrative/                        # Narrative examples (Focus Mode / Story Nodes)
                │   └── 📄 README.md
                ├── 📁 remote_sensing/                   # Raster/imagery examples
                │   └── 📄 README.md
                └── 📁 tabular/                          # This folder (tabular examples)
                    └── 📄 README.md
~~~

Recommended (docs-safe) contents for tabular examples:

~~~text
📁 tools/ai/explainability/docs/examples/tabular/
├── 📄 README.md                        # This file (patterns + contracts)
├── 📁 templates/                       # OPTIONAL: sanitized templates (schema-shaped, no real data)
│   ├── 🧾 xai-report.template.json
│   ├── 🧾 feature-dictionary.template.json
│   └── 🧾 governance-flags.template.json
├── 📁 sample_data/                     # OPTIONAL: synthetic datasets only (tiny, docs-safe)
│   └── 🧾 tabular.synthetic.csv
└── 📁 outputs/                         # OPTIONAL: sanitized example outputs (PASS PII scan)
    ├── 🧾 xai-report.example.json
    └── 📄 xai-summary.example.md
~~~

Normative storage rule:

- **Do not** store real run outputs here.
- Real explainability runs MUST write artifacts under:
  - `mcp/experiments/<run-id>/...` (preferred), or
  - `mcp/runs/<run-id>/...` (if that structure is in use),
  and only publish **sanitized summaries** into docs.

---

## 🧭 Context

### Where tabular explainability shows up in KFM

Tabular explainability is commonly used for:

- **forecasting** (hydrology/climate time-series represented as feature tables)
- **risk scoring** (flood/fire/drought indices, hazard likelihood scores)
- **ranking** (retrieval scoring features, relevance weights for focus contexts)
- **fusion models** mixing:
  - environmental metrics (e.g., soil moisture, drought index),
  - geography-derived features (e.g., distance-to-water, slope class),
  - archival/text-derived features (e.g., mentions, counts, topic weights)

The value proposition is consistent: **show why a model behaved the way it did** using *policy-safe, provenance-rich evidence*.

### Method selection matrix (recommended)

| Model family | Global explanation | Local explanation | Notes |
|---|---|---|---|
| Linear / GLM | standardized coefficients, permutation importance | coefficient contributions (per row), SHAP (optional) | watch correlated features; document scaling |
| Tree ensembles | permutation importance, gain/cover (if available) | TreeSHAP / SHAP, path explanations | strong default for tabular transparency |
| Tabular neural nets | permutation importance, sensitivity tests | Integrated Gradients / DeepSHAP / KernelSHAP | require careful baseline selection |
| Time-series-as-tabular | horizon-wise feature importance | per-horizon SHAP/attribution summaries | avoid leaking future information in features |

KFM guidance:

- Prefer **tooling that emits stable machine-readable artifacts** and supports deterministic baselines.
- Prefer **aggregate-safe** explanations (binned features, top-N) when the domain is sensitive.

### Common pitfalls (KFM-safe warnings)

- **Correlated features:** SHAP/importance can split credit unpredictably; document correlation clusters.
- **Data leakage:** features that “peek” at the target can make explanations misleading; run leakage checks.
- **Small-N slices:** subgroup-level explanations can reveal sensitive patterns; apply suppression rules.
- **Opaque feature engineering:** if a feature name is meaningless, explanations are meaningless—publish a feature dictionary.

---

## 🗺️ Diagrams

### Tabular explainability artifact flow

~~~mermaid
flowchart TD
  A["Select model + dataset slice<br/>(IDs + versions)"] --> B["Select target rows<br/>(row_id / entity_id)"]
  B --> C["Choose explanation method(s)<br/>(coeffs · permutation · SHAP · IG)"]
  C --> D["Compute global + local attributions<br/>(seeded where applicable)"]
  D --> E["Apply redaction + safety rules<br/>(PII, sensitive attrs, small-N)"]
  E --> F["Validate report shape<br/>(schema-lint + required fields)"]
  F --> G["Write artifacts<br/>report.json + summary.md + telemetry.json"]
  G --> H["Bind provenance<br/>(prov activity + entity refs)"]
  H --> I["Optional: register link in model registry<br/>+ surface in Focus Mode"]
~~~

Accessibility note: the flow starts with selecting a versioned model/dataset, then computes attributions, applies safety redactions, validates, writes artifacts, and finally binds provenance and registers links for consumption.

---

## 🧠 Story Node & Focus Mode Integration

### How tabular explanations appear to users

KFM’s UI/Focus experiences are designed to be explainable:

- Narrative or insight panels can offer an **AI explanation toggle**
- Explanations should highlight:
  - the **top contributing factors**
  - linked evidence (datasets/documents) where applicable
  - governance notices (e.g., “some details blurred due to policy”)

### Story Node binding pattern (recommended)

When an explanation supports a Story Node, store only **references** in the Story Node payload:

~~~json
{
  "story_node_id": "urn:kfm:story:example:tabular-xai",
  "focus_target": {
    "type": "geo:h3",
    "id": "h3:8a2a1072b59ffff"
  },
  "evidence": [
    {
      "kind": "ai_explainability",
      "title": "Tabular model explanation (local)",
      "artifact_ref": "mcp/experiments/2025-12-16_tabular_xai_run_001/xai/report.json",
      "policy_safe_summary_ref": "tools/ai/explainability/docs/examples/tabular/outputs/xai-summary.example.md"
    }
  ],
  "governance": {
    "classification": "Public",
    "redactions_applied": true
  }
}
~~~

Normative UI contract:

- Story Nodes MUST NOT embed large raw explanation payloads.
- Story Nodes MUST reference versioned artifacts (ideally in experiment folders) and optionally link to docs-safe summaries.

---

## 🧪 Validation & CI/CD

### Determinism requirements (normative)

Explainability runs MUST:

- accept method selection + thresholds via config (do not hard-code)
- record config path and config hash in outputs
- pin random seeds if background sampling is used
- emit stable JSON keys and stable ordering where feasible

### Minimum artifact set (recommended)

A tabular explainability run SHOULD produce:

- `xai/report.json` — machine-readable explanation bundle
- `xai/summary.md` — human-readable, policy-safe summary
- `telemetry.json` — runtime + energy/carbon + summary metrics
- `provenance.jsonld` — provenance binding (PROV-O compatible)

### Fail-closed conditions (normative)

A run MUST return FAIL (or be treated as non-certifying) if:

- model identity is missing or ambiguous
- dataset identity/version is missing
- baseline/background selection is not recorded
- redaction rules cannot be applied (missing governance metadata)
- output fails schema validation (if schemas are enforced in the repo)

### Docs publication safety gate (normative)

If you publish example outputs under `docs/examples/**`:

- They MUST be synthetic or sanitized
- They MUST pass “no secrets / no PII” scanning
- They MUST NOT include raw row identifiers that could be linked to people or protected sites

---

## 📦 Data & Metadata

### Recommended report shape (tabular explainability bundle)

This is a **recommended** structure for `report.json` (illustrative; adapt to your governed schema if one exists):

~~~json
{
  "run_id": "2025-12-16_tabular_xai_run_001",
  "status": "PASS",
  "created_utc": "2025-12-16T00:00:00Z",

  "model": {
    "model_id": "example_tabular_risk_model",
    "model_version": "v11.2.6",
    "model_hash": "<sha256-or-gitref>",
    "task": "regression",
    "output": {
      "name": "risk_score",
      "units": "unitless",
      "range": [0, 1]
    }
  },

  "dataset": {
    "dataset_id": "dcat:kfm:dataset:example:tabular",
    "dataset_version": "v11",
    "distribution_ref": "data/processed/example/tabular.parquet",
    "slice": {
      "time": "2025-10-01/2025-12-01",
      "spatial": "kansas_statewide",
      "notes": "example slice (docs-safe)"
    }
  },

  "explainability": {
    "methods": [
      {
        "method": "shap",
        "variant": "tree_shap",
        "background": {
          "type": "dataset_sample",
          "seed": 11,
          "n_rows": 256,
          "notes": "seeded sample for reproducibility"
        }
      },
      {
        "method": "permutation_importance",
        "seed": 11,
        "n_repeats": 5
      }
    ],

    "global_importance": {
      "top_k": 10,
      "features": [
        {
          "name": "soil_moisture",
          "label": "Soil moisture (surface)",
          "direction_hint": "higher → higher risk_score",
          "importance": 0.21,
          "units": "fraction"
        }
      ]
    },

    "local_explanations": [
      {
        "row_id": "row:synthetic:00042",
        "prediction": 0.73,
        "expected_value": 0.41,
        "top_k": 8,
        "attributions": [
          {
            "feature": "flood_risk_index",
            "value_repr": "bin:high",
            "shap_value": 0.18
          },
          {
            "feature": "proximity_to_water_m",
            "value_repr": "bin:near",
            "shap_value": 0.11
          }
        ]
      }
    ]
  },

  "safety": {
    "redactions_applied": true,
    "redaction_ruleset": "kfm_public_low_risk_v1",
    "suppressed_fields": ["raw_feature_values", "exact_coordinates"]
  },

  "provenance": {
    "commit_sha": "<latest-commit-hash>",
    "inputs": [
      "data_contract_ref:<path-or-id>",
      "model_registry_ref:tools/ai/registry/ai_model_registry.json"
    ],
    "artifacts": [
      "mcp/experiments/2025-12-16_tabular_xai_run_001/xai/report.json",
      "mcp/experiments/2025-12-16_tabular_xai_run_001/telemetry.json"
    ]
  }
}
~~~

### Feature dictionary (recommended companion)

For tabular explainability to be meaningful, maintain a **feature dictionary** with:

- human label
- unit
- transform (log, z-score, clip)
- missingness policy
- sensitivity flag (safe to show raw? must bin? must suppress?)

Illustrative structure:

~~~json
{
  "feature_dictionary_version": "v11",
  "features": [
    {
      "name": "soil_moisture",
      "label": "Soil moisture (surface)",
      "units": "fraction",
      "transform": "none",
      "missing_policy": "impute:median",
      "sensitivity": "general"
    },
    {
      "name": "mentioned_in_diaries_count",
      "label": "Mentions in diaries (count)",
      "units": "count",
      "transform": "log1p",
      "missing_policy": "default:0",
      "sensitivity": "contextual",
      "display_policy": "bin_only"
    }
  ]
}
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

### DCAT (primary for tabular)

For tabular datasets, DCAT is usually the primary catalog representation:

- dataset identity → `dct:identifier`
- dataset version → `dcat:version` or equivalent governed field
- distributions → `dcat:Distribution` (CSV/Parquet/GeoParquet/etc.)
- explainability bundles can be treated as derived “analysis distributions” or “reports” linked to the dataset

### STAC (when tabular is spatial-temporal)

If the tabular rows are anchored to geometry/time (e.g., H3 cell + interval), you MAY additionally represent slices as STAC Items:

- `geometry` = generalized area (policy-safe)
- `properties.datetime` or interval = window definition
- assets = pointers to tabular slices (e.g., GeoParquet) and explanation reports

Rule: do not publish restricted coordinates as STAC geometry; use generalization where required.

### PROV-O (always for explainability runs)

Each explainability run should be representable as:

- `prov:Activity` — “tabular explainability computation”
- `prov:used` — model entity + dataset slice entity + config entity
- `prov:generated` — report entity + summary entity + telemetry entity
- `prov:wasAssociatedWith` — agent (CI runner / maintainer role)

This makes explainability an auditable lineage event.

---

## 🧱 Architecture

### Separation of concerns (recommended)

A robust tabular explainability subsystem typically separates:

1. **Extract** inputs  
   - dataset slice (versioned)
   - model artifact (hash/version)
   - feature dictionary

2. **Explain**  
   - method adapters (coeffs, permutation, SHAP, IG)
   - background/baseline selection strategies

3. **Redact**  
   - feature-level display policies (raw vs binned vs suppressed)
   - small-N suppression for subgroup slices

4. **Report**  
   - canonical JSON bundle
   - compact Markdown summary for human review

5. **Bind provenance**  
   - run ID, config hash, environment pin
   - link to model registry entry (if governed)

### “Evidence-first” phrasing (normative)

When producing the human summary:

- describe attributions as “the model relied on…”
- avoid claiming “the world is…” unless the claim is supported by cited data sources
- keep a clear distinction between:
  - **input facts** (from datasets)
  - **model interpretation** (from explainability)

---

## ⚖ FAIR+CARE & Governance

### Safety constraints (normative)

Tabular explainability outputs MUST NOT:

- reveal PII (direct or indirect identifiers)
- reveal protected-site coordinates or restricted cultural information
- embed secrets, tokens, credentials, or internal-only endpoints

### Small-N and subgroup constraints (recommended)

If explanations are computed over cohorts or subgroups:

- apply minimum-N thresholds before publishing
- suppress or bin attributes that could allow re-identification
- prefer aggregate-safe reporting (top-N features without raw values)

### Cross-link governance checks (recommended)

- If fairness/protected attribute audits apply, link to:
  - `tools/ai/fairness/README.md`
- If drift monitoring applies (inputs change across time windows), link to:
  - `tools/ai/drift/README.md`

Explainability does not replace fairness or drift gates; it complements them.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v11.2.6** | 2025-12-16 | Created tabular examples README: tabular definitions, method matrix, artifact contract templates, Focus Mode/Story Node binding pattern, CI determinism and fail-closed rules, and STAC/DCAT/PROV alignment guidance. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
📊 Tabular Explainability Examples · Governed for Integrity

[⬅️ Examples Index](../README.md) ·
[🧩 Explainability Docs](../../README.md) ·
[🧠 AI Tools](../../../../README.md) ·
[🛡 Governance](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

