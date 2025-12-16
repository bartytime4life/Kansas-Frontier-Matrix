---
title: "🧪 Kansas Frontier Matrix — Tabular Explainability Sample Data (Synthetic, Docs-Safe)"
path: "tools/ai/explainability/docs/examples/tabular/sample_data/README.md"

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

doc_uuid: "urn:kfm:doc:tools-ai-explainability-tabular-sample-data-readme:v11.2.6"
semantic_document_id: "kfm-doc-tools-ai-explainability-tabular-sample-data"
event_source_id: "ledger:tools/ai/explainability/docs/examples/tabular/sample_data/README.md"
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

# Optional (point to real schema files once present in-repo).
json_schema_ref: "../../../../../../../schemas/json/tools-ai-explainability-tabular-sample-data-v11.schema.json"
shape_schema_ref: "../../../../../../../schemas/shacl/tools-ai-explainability-tabular-sample-data-v11.shape.ttl"

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
ai_training_guidance: "Sample data (even synthetic) and explainability artifacts MUST NOT be used as AI training data."

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

# 🧪 **KFM — Tabular Explainability Sample Data (Synthetic, Docs-Safe)**
`tools/ai/explainability/docs/examples/tabular/sample_data/README.md`

**Purpose**  
Document the **synthetic tabular fixtures** used for KFM explainability examples (global importance, local attributions, schema/CI tests) — with strict **policy-safety rules** (no PII, no protected locations, no secrets) and **deterministic generation** guidance.

</div>

---

## 📘 Overview

### What this folder contains

This folder is intended to hold **tiny, synthetic datasets** used to demonstrate and test **tabular explainability**:

- global feature importance example outputs
- local attribution example outputs (per synthetic “row”)
- schema validation fixtures (shape + required fields)
- docs/UI demo fixtures that must remain **diff-friendly** and **public-safe**

These fixtures should be small enough to:

- review in pull requests,
- validate quickly in CI,
- run offline,
- remain stable across platforms.

### What this folder MUST NOT contain

This folder MUST NOT contain:

- real observations from production datasets
- any direct identifiers (names, emails, phone numbers, addresses)
- protected-site coordinates or fine-grained geometry
- restricted Indigenous knowledge
- secrets, tokens, credentials, internal-only endpoints
- raw archived text excerpts from restricted sources
- sensitive imagery (this is tabular-only)

If you need a dataset for an audit, store it as governed run input/output in:

- `mcp/experiments/<run-id>/...` (preferred)
- or `mcp/runs/<run-id>/...` (if that structure is in use)

…and publish only **sanitized summaries** into docs.

### Why synthetic sample data exists (in KFM terms)

KFM explainability is governance-sensitive. Even “just features” can leak sensitive signals (e.g., precise distances, rare subgroup patterns).

Synthetic sample data allows us to:

- prove artifact **shape and contracts**
- test CI validators and deterministic formatting
- demonstrate “how to read an explanation”
- avoid leakage pathways and policy violations

### Core invariants (normative)

1. All sample data here MUST be **synthetic** (or provably non-sensitive and fully redacted).
2. Sample data MUST be **deterministic**:
   - fixed seeds,
   - stable ordering,
   - stable rounding/precision.
3. Sample data MUST be **documentation-safe**:
   - no PII,
   - no secrets,
   - no protected-site coordinates,
   - no re-identification-friendly small cohorts.
4. Sample data MUST be treated as **non-training** material (`ai_training_allowed: false`).

---

## 🗂️ Directory Layout

This folder sits under the tabular explainability examples:

~~~text
📁 tools/
└── 🧠 ai/
    └── 📁 explainability/
        └── 📁 docs/
            └── 📁 examples/
                └── 📁 tabular/
                    ├── 📄 README.md
                    ├── 📁 outputs/
                    │   └── 📄 README.md
                    └── 📁 sample_data/
                        └── 📄 README.md              # This file
~~~

### Recommended contents (keep aligned with what actually exists)

This is a recommended docs-safe layout. Add/remove entries to match the folder.

~~~text
📁 tools/ai/explainability/docs/examples/tabular/sample_data/
├── 📄 README.md
├── 🧾 tabular.synthetic.csv                     # Primary tiny fixture (preferred)
├── 🧾 tabular.synthetic.schema.json             # Optional: schema for the CSV
├── 🧾 feature_dictionary.synthetic.json         # Optional: feature dictionary for interpretability
└── 🧾 generation_manifest.example.json          # Optional: how/when generated (seed + tool versions)
~~~

**Directory rules (normative):**

- Any committed dataset file MUST be:
  - small,
  - synthetic,
  - stable across platforms (avoid locale-sensitive formats),
  - and clearly labeled (e.g., `.synthetic`).
- If you add a new sample data file, update this README and (recommended) add a manifest entry.

---

## 🧭 Context

### How sample data is used by tabular explainability examples

The explainability examples may reference sample data in two ways:

1. **Docs-only walkthroughs**
   - show the idea of global importance and local attribution
   - link to small CSV fixtures to keep examples concrete

2. **Fixture-driven validations**
   - schema/contract tests for explainability JSON output
   - regression tests for deterministic formatting and ordering
   - UI demo fixtures that do not require privileged access

### Types of tabular features represented in synthetic fixtures

Synthetic features SHOULD resemble the kinds of features KFM uses, without reflecting real-world values:

- environmental proxies (e.g., precipitation_30d, soil_moisture_index)
- topographic classes (e.g., slope_bin)
- temporal encodings (e.g., month_bin)
- retrieval/ranking features (e.g., citation_rate_proxy_bin)
- engineered aggregations (e.g., rolling_mean_bin)

Avoid sensitive proxies that can reveal protected locations or rare cohorts. When in doubt, prefer:

- coarse bins (`low/medium/high`)
- capped/rounded values
- invented “demo” categories

---

## 🗺️ Diagrams

### Sample-data-to-explainability flow (docs-safe)

~~~mermaid
flowchart TD
  A["Synthetic tabular fixture<br/>(CSV + schema)"] --> B["Explainability run (demo)<br/>(global + local)"]
  B --> C["Docs-safe outputs<br/>(examples/tabular/outputs)"]
  B --> D["Schema/CI checks<br/>(determinism + safety)"]
  C --> E["Docs walkthrough + UI demos<br/>(no privileged access)"]
~~~

Accessibility note: synthetic inputs enable explainability demos and outputs while remaining safe for docs and CI.

---

## 🧪 Validation & CI/CD

### Required safety checks (normative)

Any file added here MUST pass:

- secret scanning (no tokens/keys/endpoints)
- PII scanning (no personal identifiers)
- policy safety review if feature names could imply sensitive domains

### Determinism requirements (normative)

If sample data is generated by a script:

- seed MUST be fixed and recorded
- ordering MUST be stable (sort by a deterministic key like `row_id`)
- numeric formatting MUST be stable:
  - fixed precision (e.g., 3 decimals) or binned categories
  - avoid scientific notation unless explicitly documented
- timestamps MUST NOT be embedded in the CSV (unless explicitly required and stable)

### CSV formatting rules (recommended)

To keep diffs stable:

- use UTF‑8 encoding
- use `,` delimiter
- use `\n` line endings
- include a header row
- keep row count small (recommended: <= 500)
- avoid embedded commas in values unless quoted consistently

---

## 📦 Data & Metadata

### Recommended CSV columns (synthetic contract)

This is a recommended “starter” schema for `tabular.synthetic.csv`.

**Identity fields (required)**

- `row_id` (string): `row:synthetic:000001` (stable)
- `entity_id` (string): `entity:synthetic:demo:0001` (stable)
- `time_bucket` (string): `2025Q1_demo`, `modern_demo`, etc.
- `region_bucket` (string): coarse region label (non-sensitive), e.g., `kansas_region_demo`

**Feature fields (examples; choose a small set)**

- numeric (prefer bounded or binned):
  - `precip_30d_mm_bin` (`low|mid|high`)
  - `soil_moisture_bin` (`low|mid|high`)
  - `temp_7d_c_bin` (`low|mid|high`)
- categorical:
  - `slope_bin` (`flat|gentle|steep`)
  - `landcover_bin` (`water|veg|built|bare`)
- retrieval proxies (safe, coarse):
  - `evidence_density_bin` (`low|mid|high`)
  - `citation_rate_bin` (`low|mid|high`)

**Target/prediction fields (optional; if needed for demos)**

- `target_bin` (`low|mid|high`) OR
- `target_value` (float, bounded)  
  *(avoid real-world units if not needed)*

### Example CSV (illustrative)

~~~text
row_id,entity_id,time_bucket,region_bucket,precip_30d_mm_bin,soil_moisture_bin,temp_7d_c_bin,slope_bin,landcover_bin,target_bin
row:synthetic:000001,entity:synthetic:demo:0001,modern_demo,kansas_region_demo,high,mid,low,gentle,veg,high
row:synthetic:000002,entity:synthetic:demo:0002,modern_demo,kansas_region_demo,low,low,mid,flat,built,low
row:synthetic:000003,entity:synthetic:demo:0003,modern_demo,kansas_region_demo,mid,high,high,steep,bare,mid
~~~

### Feature dictionary (recommended companion)

If this folder includes `feature_dictionary.synthetic.json`, it SHOULD document:

- human-friendly labels
- units or bin semantics
- transforms (if any)
- sensitivity classification
- display policy: `raw_allowed | bin_only | suppress`

Illustrative shape:

~~~json
{
  "feature_dictionary_version": "v11.2.6",
  "features": [
    {
      "name": "precip_30d_mm_bin",
      "label": "Precipitation (30-day) — binned",
      "units": "mm",
      "bin_semantics": { "low": "0–10", "mid": "10–40", "high": "40+" },
      "sensitivity": "general",
      "display_policy": "bin_only"
    }
  ],
  "notes": "Synthetic-only dictionary for explainability demos."
}
~~~

### Generation manifest (recommended)

If the sample data is generated, add a `generation_manifest.example.json` describing:

- generator script (path)
- seed
- tool versions (pinned)
- generation date (optional; but don’t bake it into the CSV unless required)
- sha256 checksums for generated files

Illustrative shape:

~~~json
{
  "manifest_id": "kfm:sample-data:tabular:synthetic:v11.2.6",
  "seed": 11,
  "generator": {
    "script_ref": "tools/ai/explainability/scripts/generate_tabular_synthetic.py",
    "python_version": "3.11.x",
    "dependencies_ref": "tools/ai/requirements-tools-ai.txt"
  },
  "outputs": [
    { "path": "tabular.synthetic.csv", "sha256": "<sha256>" },
    { "path": "feature_dictionary.synthetic.json", "sha256": "<sha256>" }
  ],
  "safety": {
    "pii_present": false,
    "contains_sensitive_locations": false,
    "notes": "Synthetic-only fixture for docs/CI."
  }
}
~~~

---

## ⚖ FAIR+CARE & Governance

### Policy constraints (normative)

Sample data MUST comply with:

- `governance_ref`
- `ethics_ref`
- `sovereignty_policy`

Practical implications:

- do not create “synthetic” data that still encodes a protected location pattern
- do not include culturally sensitive categories unless fully synthetic and clearly fictional
- prefer coarse buckets and invented identifiers

### Publication rule

Only publish what is safe for a public repository. If there is any doubt:

- do not commit the dataset here,
- publish only an abstract schema and a tiny, purely synthetic example row set.

### Training prohibition

Even though this is synthetic, this folder is part of governance and documentation fixtures and MUST NOT be used as training data.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v11.2.6** | 2025-12-16 | Created tabular sample-data README: docs-safe synthetic fixture rules, recommended CSV schema, determinism + CI validation guidance, and FAIR+CARE publication constraints. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
🧪 Tabular Sample Data · Synthetic · Docs-Safe · Governed for Integrity

[⬅️ Tabular Examples](../README.md) ·
[📤 Outputs](../outputs/README.md) ·
[🧪 Examples Index](../../README.md) ·
[🧩 Explainability Docs](../../../README.md) ·
[🧠 AI Tools](../../../../../README.md) ·
[🛡 Governance](../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

