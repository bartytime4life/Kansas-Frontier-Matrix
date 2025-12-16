---
title: "🧩 Kansas Frontier Matrix — Tabular Explainability Templates (Docs-Safe)"
path: "tools/ai/explainability/docs/examples/tabular/templates/README.md"

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

doc_uuid: "urn:kfm:doc:tools-ai-explainability:tabular:templates-readme:v11.2.6"
semantic_document_id: "kfm-doc-tools-ai-explainability-tabular-templates"
event_source_id: "ledger:tools/ai/explainability/docs/examples/tabular/templates/README.md"
immutability_status: "mutable-plan"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

# NOTE: Update these refs to your governed “current release” bundle when available.
sbom_ref: "../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/tools-ai-governance-v4.json"
energy_schema: "../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

# Optional: point these to real schema files once present in-repo.
json_schema_ref: "../../../../../../../schemas/json/tools-ai-explainability-tabular-templates-v11.schema.json"
shape_schema_ref: "../../../../../../../schemas/shacl/tools-ai-explainability-tabular-templates-v11.shape.ttl"

fair_category: "F1-A1-I2-R3"
care_label: "Public · Low-Risk"
classification: "Public"
jurisdiction: "United States · Kansas"
sensitivity: "General"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_data_flag: false
risk_category: "Low"
redaction_required: true

ai_training_allowed: false
ai_training_guidance: "Templates, example fixtures, and governance artifacts MUST NOT be used as AI training data."

machine_readable: true
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "Annual review"
sunset_policy: "Superseded upon next explainability platform update"

provenance_chain:
  - "tools/ai/explainability/docs/examples/tabular/README.md@v11.2.6"
  - "tools/ai/explainability/docs/examples/README.md@v11.2.6"
---

<div align="center">

# 🧩 **KFM — Tabular Explainability Templates (Docs-Safe)**
`tools/ai/explainability/docs/examples/tabular/templates/README.md`

**Purpose**  
Provide **copy-ready, schema-shaped templates** for tabular explainability artifacts (reports, feature dictionaries, governance flags, manifests) so KFM outputs are **deterministic, CI-validated, provenance-ready**, and **policy-safe** by default.

</div>

---

## 📘 Overview

### What this folder contains

This folder is the **template library** for tabular explainability documentation examples.

Templates here are designed to be:

- **schema-shaped** (stable keys and predictable structure),
- **tool-agnostic** (works whether your explainer is SHAP/LIME/coefficients/permutation/IG),
- **docs-safe** (synthetic placeholders only),
- **CI-friendly** (diffable, small, deterministic).

These templates are intended to support:

- documentation walkthroughs (how to build and read explainability artifacts),
- fixture generation (docs-safe example outputs),
- validator development (schemas and lint rules),
- UI demo wiring (rendering explanation bundles without privileged access).

### What this folder MUST NOT contain

This folder MUST NOT contain:

- real model outputs from production data,
- raw feature tables from real datasets,
- any PII,
- protected-site coordinates or sensitive geometry,
- secrets/tokens/credentials.

If you need to store real artifacts:

- write them under governed run locations such as `mcp/experiments/<run-id>/...`,
- then publish only **sanitized summaries** into docs.

### How templates relate to tabular explainability docs

- `templates/` provides **skeletons**
- `sample_data/` provides **synthetic inputs**
- `outputs/` provides **docs-safe example outputs**
- real runs live under **governed experiment folders**

---

## 🗂️ Directory Layout

This folder sits under the tabular explainability example tree:

~~~text
📁 tools/
└── 🧠 ai/
    └── 📁 explainability/
        └── 📁 docs/
            └── 📁 examples/
                └── 📁 tabular/
                    ├── 📄 README.md
                    ├── 📁 sample_data/
                    │   └── 📄 README.md
                    ├── 📁 outputs/
                    │   └── 📄 README.md
                    └── 📁 templates/
                        └── 📄 README.md              # This file
~~~

Recommended contents for this folder (create if missing; keep aligned with actual files):

~~~text
📁 tools/ai/explainability/docs/examples/tabular/templates/
├── 📄 README.md
│
├── 🧾 xai-report.template.json                    # Combined tabular XAI report (global + local)
├── 🧾 attributions-global-topk.template.json      # Global importance (top-k only)
├── 🧾 attributions-local-topk.template.json       # Local attributions (top-k per example row)
├── 🧾 feature-dictionary.template.json            # Feature dictionary (labels/units/sensitivity)
├── 🧾 governance-flags.template.json              # Display eligibility + redaction/suppression reasons
├── 🧾 output-manifest.template.json               # Docs-safe output inventory + generator identity
└── 🧾 checksums.template.sha256                   # sha256sum-compatible format example (optional)
~~~

**Directory rules (normative):**

- Template filenames SHOULD end with `.template.json` (or `.template.sha256`).
- Templates MUST remain small and include **placeholders** (e.g., `<sha256>`, `row:synthetic:000001`).
- Templates MUST prefer **relative references** and stable IDs.

---

## 🧭 Context

### Where tabular explainability sits in the KFM pipeline

Tabular explainability is a governance support layer used across multiple KFM stages:

1. **ETL / Feature Engineering**  
   - produces feature tables (often in `data/work/` or `data/processed/`)
2. **Modeling / Inference**  
   - produces predictions and metrics (in pipelines or tools)
3. **Explainability**  
   - produces evidence artifacts (these templates define shapes)
4. **Cataloging & Provenance Binding**  
   - references dataset IDs (DCAT/STAC) and emits lineage (PROV-O)
5. **APIs → UI**  
   - exposes safe explanation summaries through governed endpoints (no direct graph access)
6. **Story Nodes / Focus Mode**  
   - links explanation artifacts to narrative targets (evidence-first UX)

### Why KFM uses “templates” instead of freeform output

Templates provide:

- deterministic structure for CI checks,
- predictable rendering in UI,
- safer redaction control (known fields to suppress),
- long-term auditability (stable keys across versions).

### Naming conventions (recommended)

- `.template.json` = skeleton only (placeholders)
- `.example.json` = docs-safe fixture output (synthetic/sanitized)
- `.json` without `.example`/`.template` = typically reserved for governed run artifacts

---

## 🧪 Validation & CI/CD

### Determinism requirements (normative)

When templates are used to generate outputs:

- IDs MUST be stable (synthetic IDs are fine)
- arrays MUST be stable-ordered:
  - global importance: sort by `importance` desc then `feature` asc
  - local attributions: sort by `abs(contribution)` desc then `feature` asc
- numeric fields SHOULD be rounded consistently (document precision)
- config references and config hashes MUST be captured in reports/manifests

### CI expectations for templates (recommended)

CI should be able to:

- parse every `.template.json` as valid JSON
- validate templates against a schema (if present) or at minimum check required keys exist
- ensure no “forbidden strings” appear (secrets patterns, private endpoints)
- ensure templates do not embed sensitive content

If you add or change a template:

- update the relevant schema/shape files (if enforced),
- update `outputs/` fixtures as needed,
- update this README’s directory tree.

---

## 📦 Data & Metadata

This section provides **template skeletons** you can paste into files. Do not replace placeholders with real sensitive values in docs.

### Template: `xai-report.template.json` (combined report)

~~~json
{
  "run_id": "<run-id>",
  "status": "EXAMPLE",
  "created_utc": "2025-01-01T00:00:00Z",

  "model": {
    "model_id": "<model-id>",
    "model_version": "<model-version>",
    "model_hash": "<sha256-or-gitref>",
    "task_type": "regression",
    "output": { "name": "<output-name>", "units": "unitless", "range": [0, 1] }
  },

  "dataset": {
    "dataset_id": "<dataset-id>",
    "dataset_version": "<dataset-version>",
    "distribution_ref": "<relative-path-or-id>",
    "slice": {
      "time": "<start>/<end>",
      "spatial": "<coarse-region-bucket>",
      "notes": "Synthetic/docs-safe slice descriptor"
    }
  },

  "config": {
    "profile_ref": "<tools/ai/configs/...>",
    "config_sha256": "<sha256>"
  },

  "methods": [
    {
      "method": "shap",
      "variant": "kernel",
      "background": { "type": "dataset_sample", "seed": 11, "n_rows": 256 }
    }
  ],

  "global_importance_topk": {
    "top_k": 10,
    "features": [
      {
        "feature": "<feature-name>",
        "label": "<human label>",
        "importance": 0.0,
        "units": "<unit-or-null>",
        "display_policy": "bin_only"
      }
    ]
  },

  "local_attributions_topk": [
    {
      "example_row_id": "row:synthetic:000001",
      "prediction": 0.0,
      "expected_value": 0.0,
      "top_k": 8,
      "attributions": [
        {
          "feature": "<feature-name>",
          "value_repr": "bin:low|mid|high",
          "contribution": 0.0
        }
      ]
    }
  ],

  "safety": {
    "classification": "Public",
    "care_label": "Public · Low-Risk",
    "pii_present": false,
    "contains_sensitive_locations": false,
    "contains_secrets": false,
    "redactions_applied": true,
    "suppression_applied": false,
    "suppressed_fields": ["raw_feature_values", "exact_coordinates"]
  },

  "refs": {
    "manifest_ref": "../outputs/output_manifest.example.json",
    "telemetry_ref": "mcp/experiments/<run-id>/telemetry.json",
    "provenance_ref": "mcp/experiments/<run-id>/provenance_bundle.jsonld"
  }
}
~~~

### Template: `feature-dictionary.template.json`

~~~json
{
  "feature_dictionary_version": "v11.2.6",
  "features": [
    {
      "name": "<feature-name>",
      "label": "<human label>",
      "units": "<unit-or-null>",
      "transform": "none|log1p|zscore|clip",
      "missing_policy": "impute:median|default:0|drop",
      "sensitivity": "general|contextual|sensitive",
      "display_policy": "raw_allowed|bin_only|suppress",
      "notes": "Keep this meaningful; explainability is only as good as feature names."
    }
  ]
}
~~~

### Template: `governance-flags.template.json`

~~~json
{
  "display_eligibility": {
    "ui_allowed": true,
    "withheld_components": [],
    "reasons_if_denied": []
  },
  "safety_controls": {
    "no_raw_rows": true,
    "no_precise_coordinates": true,
    "suppress_small_groups": true,
    "min_group_n": 50
  },
  "policy": {
    "classification": "Public",
    "care_label": "Public · Low-Risk",
    "redaction_applied": true,
    "suppression_applied": false,
    "reason_codes": ["SMALL_GROUP_SUPPRESSION_ENABLED"]
  }
}
~~~

### Template: `output-manifest.template.json`

~~~json
{
  "manifest_id": "kfm:example:tabular:xai:outputs:<version>",
  "version": "v11.2.6",
  "created": "2025-12-16",
  "scope": "tabular explainability templates and docs-safe example outputs",
  "generator": {
    "tool": "kfm-explainability",
    "tool_version": "<pin-me>",
    "config_ref": "<tools/ai/configs/...>",
    "config_sha256": "<sha256>"
  },
  "files": [
    { "path": "xai_report.example.json", "role": "combined_report", "sha256": "<sha256>" },
    { "path": "xai_summary.example.md", "role": "human_summary", "sha256": "<sha256>" }
  ],
  "safety": {
    "classification": "Public",
    "care_label": "Public · Low-Risk",
    "pii_present": false,
    "contains_sensitive_locations": false,
    "contains_secrets": false,
    "notes": "Docs-safe fixtures only; do not store production artifacts here."
  }
}
~~~

### Template: `checksums.template.sha256` (sha256sum-compatible)

~~~text
<sha256>  attributions-global-topk.template.json
<sha256>  attributions-local-topk.template.json
<sha256>  feature-dictionary.template.json
<sha256>  governance-flags.template.json
<sha256>  output-manifest.template.json
<sha256>  xai-report.template.json
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

### DCAT (typical for tabular explainability)

Tabular explainability outputs are commonly attached as “analysis/report distributions” of a dataset:

- dataset ID → referenced in `dataset.dataset_id`
- distribution references → referenced by `distribution_ref`
- explainability bundle → can be referenced as an audit/report artifact

Rule: prefer IDs/refs, not embedded DCAT payloads in example templates.

### STAC (optional for tabular)

If a tabular slice is anchored to a spatiotemporal geometry (e.g., H3 cell interval), you MAY also reference STAC Items, but templates should:

- avoid precise geometry,
- use coarse region buckets when needed,
- remain reference-first.

### PROV-O (recommended for all explainability runs)

Template fields are designed to support a PROV mapping:

- `run_id` → `prov:Activity` identifier
- `model` + `dataset` → `prov:Entity` inputs (`prov:used`)
- `xai_report` + manifest + telemetry → generated entities (`prov:generated`)
- `refs.provenance_ref` → pointer to a PROV bundle (JSON-LD)

---

## ⚖ FAIR+CARE & Governance

### Why templates include explicit safety fields

Explainability outputs can leak sensitive information if:

- they include raw feature values,
- they include precise coordinates/distances,
- they include small-cohort subgroup explanations.

Therefore, templates always include:

- `classification` and `care_label`
- redaction/suppression flags
- a place to record reason codes

### Publication rule (normative)

Anything in `docs/examples/**` must be safe for public exposure.

If a field could ever contain restricted data, the template should model:

- binned representation (`value_repr`)
- suppression (`display_policy: suppress`)
- withheld component lists with reason codes

### Training prohibition

Even though these are templates, they are part of the governance surface area and MUST NOT be used for AI training data.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v11.2.6** | 2025-12-16 | Created tabular templates README: defined recommended template set (report, feature dictionary, governance flags, manifest, checksums), determinism/safety rules, and DCAT/STAC/PROV alignment guidance for KFM tabular explainability. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
🧩 Tabular Explainability Templates · Docs-Safe · Governed for Integrity

[⬅️ Tabular Examples](../README.md) ·
[🧪 Sample Data](../sample_data/README.md) ·
[📤 Outputs](../outputs/README.md) ·
[🧪 Examples Index](../../README.md) ·
[🛡 Governance](../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

