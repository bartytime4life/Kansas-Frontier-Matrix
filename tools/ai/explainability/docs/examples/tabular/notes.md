---
title: "📝 Kansas Frontier Matrix — Tabular Explainability Notes (Examples)"
path: "tools/ai/explainability/docs/examples/tabular/notes.md"

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

doc_uuid: "urn:kfm:doc:tools-ai-explainability-tabular-notes:v11.2.6"
semantic_document_id: "kfm-doc-tools-ai-explainability-tabular-notes"
event_source_id: "ledger:tools/ai/explainability/docs/examples/tabular/notes.md"
immutability_status: "mutable-plan"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

# NOTE: Update these refs to your governed “current release” bundle when available.
sbom_ref: "../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.2/manifest.zip"

telemetry_ref: "../../../../../../releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/tools-ai-governance-v4.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

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
redaction_required: true

ai_training_allowed: false
ai_training_guidance: "Notes and example materials MUST NOT be used as AI training data."

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

# 📝 **KFM — Tabular Explainability Notes (Examples)**
`tools/ai/explainability/docs/examples/tabular/notes.md`

**Purpose**  
Capture **practical, implementation-minded notes** for tabular explainability in KFM:
common pitfalls, baseline choices, feature semantics, redaction patterns, and “how to interpret” guidance.
These notes are written to keep the example suite **policy-safe**, **deterministic**, and **audit-friendly**.

</div>

---

## 📘 Overview

These notes complement:

- **Tabular Examples README**: `./README.md`
- **Long-form walkthrough**: `../example-tabular.md`
- **Docs-safe fixtures**: `./outputs/README.md`
- **Synthetic inputs**: `./sample_data/README.md`
- **Templates**: `./templates/README.md`

### Non-negotiable reminders (read first)

- **Explainability describes model behavior, not truth.**  
  A feature being “important” does not prove causality.

- **Explainability is not a substitute for:**
  - fairness audits (`../../../../fairness/README.md`)
  - drift monitoring (`../../../../drift/README.md`)
  - governance review (`../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md`)

- **Docs-safe outputs must remain safe even under adversarial reading.**  
  If a value could reveal sensitive information, it must be binned, suppressed, or removed.

---

## 🗂️ Directory Layout

Tabular explainability examples live here:

~~~text
📁 tools/
└── 🧠 ai/
    └── 📁 explainability/
        └── 📁 docs/
            └── 📁 examples/
                └── 📁 tabular/
                    ├── 📄 README.md
                    ├── 📄 notes.md
                    ├── 📁 templates/
                    │   └── 📄 README.md
                    ├── 📁 sample_data/
                    │   └── 📄 README.md
                    └── 📁 outputs/
                        └── 📄 README.md
~~~

Other governance-critical dependencies:

~~~text
📁 tools/
└── 🧠 ai/
    ├── 📁 configs/          # Threshold profiles and environment policy (config-driven)
    ├── 📁 fairness/         # Bias/fairness audits
    ├── 📁 drift/            # Drift detection and escalations
    └── 📁 provenance/       # Provenance bundling helpers (if present in repo)
~~~

---

## 🧭 Context

### 1) Choosing an explanation method

The “right” method depends on **model family**, **feature encoding**, and **governance needs**.

Recommended quick matrix:

| If you are using… | Prefer… | Why | Common traps |
|---|---|---|---|
| Linear / GLM | coefficient contributions + permutation importance | stable and interpretable if features are well-defined | scaling/standardization changes interpretation |
| Tree ensembles | TreeSHAP (or equivalent) + permutation | strong local explanations; consistent | correlated features split credit; categorical explosion |
| Tabular neural nets | IG / DeepSHAP style + permutation | handles differentiable paths | baseline choice dominates IG/SHAP stability |
| Any model, governance-first | permutation importance + monotonic checks | tool-agnostic and robust | permutation can be noisy; must seed and average |

**KFM rule of thumb:**  
Use at least one **tool-agnostic** method (permutation) and one **local** method (SHAP-like or IG-like) when feasible.

### 2) Baselines and background data (the hidden control knob)

For SHAP/IG-like methods, the background/baseline dataset heavily influences attributions.

In KFM, baseline choice MUST be recorded as metadata, and SHOULD be one of:

- **training baseline**: used for certification (most stable for governance)
- **release baseline**: last certified release slice (preferred for monitoring)
- **rolling baseline**: only for operational monitoring, not certification decisions

**Docs-safe guidance:**  
For examples, use a seeded synthetic background:

- `seed: 11`
- fixed sample size (e.g., 256 rows)
- stable row ordering

### 3) Feature semantics (avoid “encoded feature gibberish”)

Explainability is only as meaningful as feature semantics.

If the model consumes encoded features:

- one-hot encoded categories (`landcover__veg`, `landcover__water`, …)
- hashed features
- embeddings

…then your explainability layer SHOULD aggregate back to a human meaningful feature:

- `landcover` (grouped from one-hot)
- `topic_presence` (aggregated)
- `embedding_norm` / `embedding_cluster` (safe aggregate)

**Docs-safe rule:**  
Do not publish raw embedding coordinates or high-dimensional vectors in examples.

### 4) Correlated features and “credit splitting”

Strong correlations cause explanations to “split credit” unpredictably:

- SHAP values may distribute importance among correlated variables
- permutation importance may understate importance if features are redundant
- coefficient magnitudes can become unstable if multicollinearity is high

Recommended mitigation pattern:

- publish a **correlation cluster summary** (top correlated groups)
- group contributions for “feature families”
- include a note: “importance is not unique under correlation”

### 5) Time and leakage (especially for Kansas-scale time series)

Tabular features often come from time windows (lags/rolling).

Common leakage risks:

- features computed using future information relative to prediction time
- leakage via “release date” or “ingestion date”
- leakage via target-derived features (“post-event mentions”)

KFM guardrail:

- record the window definition in metadata (`window.time`)
- enforce an explicit “as-of” timestamp for any feature calculation
- if the example uses time features, keep them coarse and synthetic

### 6) Small-N and re-identification risk

Tabular explainability can leak information even without names:

- rare feature combinations
- unusual outliers
- small subgroup explanations

Recommended controls (docs-safe):

- bin values (`low/medium/high`)
- suppress rare categories
- suppress “local explanation” output for any cohort below `min_group_n`
- remove raw IDs; use synthetic `row:synthetic:...`

---

## 🗺️ Diagrams

### Practical “tabular explanation → governed artifact” flow

~~~mermaid
flowchart TD
  A["Feature table slice<br/>(versioned)"] --> B["Model inference<br/>(version/hash pinned)"]
  B --> C["Explainability methods<br/>(perm + local method)"]
  C --> D["Attributions<br/>(global + local top-k)"]
  D --> E["Safety layer<br/>(bin/suppress/redact)"]
  E --> F["Report bundle<br/>(report.json + summary.md)"]
  F --> G["Telemetry + provenance<br/>(refs only in docs)"]
  G --> H["Optional UI rendering<br/>(Focus Mode evidence panel)"]
~~~

Accessibility note: outputs flow through a safety layer before becoming publishable artifacts.

---

## 🧠 Story Node & Focus Mode Integration

### What the UI should show (recommended)

For a tabular explanation, the UI should render:

- **Top drivers** (global) as a ranked list (top-k)
- **Local drivers** for a specific focus context (top-k), with binned values:
  - `bin:low|mid|high`
  - `category:<label>`
- A visible **governance notice** if redaction/suppression was applied
- A link to:
  - report JSON reference (governed run artifact)
  - docs-safe summary (optional)

### “Narrative-safe” phrasing for explanations (recommended)

Use phrasing that explicitly attributes to the model:

- ✅ “The model relied most on…”
- ✅ “This factor increased the model’s score…”
- ✅ “Under the model, these features contributed…”
- ❌ “This proves…”
- ❌ “This caused…”
- ❌ “This is definitively why…”

### Gating with drift and fairness (recommended)

If the model is:

- **WARN drift**: show a caution badge and include a “stability note”
- **FAIL drift**: degrade to retrieval-only or block production usage (per policy)
- **fairness FAIL**: block promotion and do not publish local explanations to UI

This file does not define gating policy (governance does), but examples should demonstrate the pattern.

---

## 🧪 Validation & CI/CD

### Determinism checklist (minimum)

When generating example outputs:

- fixed seed (recorded)
- stable row ordering
- stable sorting of attributions
- stable rounding precision
- stable config identity recorded (config path + hash)

### Docs-safe publication checklist (minimum)

Before committing any `.example.*` outputs:

- no raw identifiers
- no PII
- no secrets
- no protected coordinates
- no rare-category leakage (apply suppression)
- include a manifest entry (recommended)

### “Fail-closed” guidance for example generation scripts

If a script cannot confidently apply policy rules:

- fail and do not write outputs
- require explicit config/profile selection (no silent defaults)
- record exactly which rule set was applied

---

## 📦 Data & Metadata

### Recommended metadata fields for tabular explanation artifacts

Even examples should include these fields (as placeholders if needed):

- model identity:
  - `model_id`, `model_version`, `model_hash`
- dataset identity:
  - `dataset_id`, `dataset_version`
- explanation context:
  - `methods[]` (method name + variant)
  - `background` / `baseline` (type + seed + n)
- safety controls:
  - `redactions_applied`, `suppression_applied`, `suppressed_fields[]`
- provenance pointers:
  - `run_id`
  - `telemetry_ref`
  - `provenance_ref`

### Recommended “reason codes” for suppression/redaction

Use reason codes in example outputs so downstream tools can interpret them:

- `PII_RISK_SUPPRESSED`
- `SMALL_GROUP_SUPPRESSED`
- `SENSITIVE_LOCATION_REDACTED`
- `RAW_VALUES_WITHHELD`
- `RELEASE_BASELINE_REQUIRED`
- `CONFIG_MISSING_FAIL_CLOSED`

Reason codes should be treated as stable, machine-readable strings.

---

## 🌐 STAC, DCAT & PROV Alignment

### DCAT-first for tabular explainability

Tabular artifacts are usually best represented as:

- DCAT dataset/distribution references (source dataset + explanation bundle as a derived distribution)
- stable IDs for dataset/version and report/version

Keep examples reference-first:

- store IDs, paths, or pointers
- avoid embedding complete catalog payloads in docs

### STAC optional (only when tabular slices are explicitly spatiotemporal)

If the rows correspond to a spatiotemporal slice (e.g., H3/time window), you MAY represent the slice as a STAC Item with:

- generalized geometry
- temporal interval
- assets referencing the tabular distribution and the explanation report

### PROV-O recommended for all explainability runs

Map the run as:

- `prov:Activity` = “tabular explainability computation”
- `prov:used`:
  - model entity
  - dataset slice entity
  - config entity
- `prov:generated`:
  - report entity
  - telemetry entity
  - summary entity

Docs should store pointers to the PROV bundle; do not embed sensitive run payloads here.

---

## ⚖ FAIR+CARE & Governance

### Publication rule (normative)

Anything under `docs/examples/**` (including this notes file) must be safe for public exposure.

That implies:

- no sensitive or restricted content
- no implied authority beyond governance
- no “certification claims” that aren’t backed by a governed ledger

### Why tabular explainability is governance-sensitive

Even simple feature attributions can expose:

- sensitive patterns about communities
- sensitive relationships between conditions and protected sites
- “where the model is looking” in ways that reveal restricted spatial detail

Therefore, examples must always:

- prefer binned values
- suppress rare patterns
- include clear redaction indicators

### Training prohibition

These notes, templates, and example fixtures are governance-support materials and MUST NOT be used as training data.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v11.2.6** | 2025-12-16 | Created tabular explainability notes: method/baseline guidance, feature semantics pitfalls, safety + suppression patterns, determinism checklist, and catalog/provenance alignment notes for the example suite. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
📝 Tabular Explainability Notes · Docs-Safe · Governed for Integrity

[⬅️ Tabular Examples](./README.md) ·
[📄 Long-Form Walkthrough](../example-tabular.md) ·
[📤 Outputs](./outputs/README.md) ·
[🧪 Sample Data](./sample_data/README.md) ·
[🧩 Templates](./templates/README.md)

</div>

