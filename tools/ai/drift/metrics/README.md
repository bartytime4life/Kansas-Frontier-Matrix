---
title: "📏 Kansas Frontier Matrix — AI Drift Metrics"
path: "tools/ai/drift/metrics/README.md"

version: "v11.2.6"
last_updated: "2025-12-15"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous · FAIR+CARE Council Oversight"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Architecture"
intent: "tools-ai-drift-metrics"
role: "drift-metrics-registry"
category: "AI · Drift · Metrics · Governance · Telemetry"

header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:doc:tools-ai:drift:metrics-readme:v11.2.6"
semantic_document_id: "kfm-doc-tools-ai-drift-metrics"
event_source_id: "ledger:tools/ai/drift/metrics/README.md"
immutability_status: "mutable-plan"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
prov_profile: "KFM-PROV v11"
dcat_profile: "KFM-DCAT v11"
stac_profile: "KFM-STAC v11"

# Release refs: update if your governed “current release” differs.
sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"

telemetry_ref: "../../../../releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/tools-ai-governance-v4.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

# Optional (point these at real schema files if/when present in your repo).
json_schema_ref: "../../../../schemas/json/tools-ai-drift-metrics-v11.schema.json"
shape_schema_ref: "../../../../schemas/shacl/tools-ai-drift-metrics-v11.shape.ttl"

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
ai_training_guidance: "Drift metrics, drift reports, and governance/audit artifacts MUST NOT be used as AI training data."

machine_readable: true
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "Annual review"
sunset_policy: "Superseded upon next AI-tools platform update"

provenance_chain:
  - "tools/ai/drift/README.md@v11.2.6"
  - "tools/ai/README.md@v11.2.6"
---

<div align="center">

# 📏 **KFM — AI Drift Metrics**
`tools/ai/drift/metrics/README.md`

**Purpose**  
Define the **drift metrics layer** used by KFM drift monitoring — including metric taxonomy, naming/versioning rules, output contracts, aggregation patterns, and governance-safe interpretation — so drift scoring stays **deterministic, comparable, provenance-bound, and telemetry-ready**.

</div>

---

## 📘 Overview

### What a “drift metric” is (normative)

A **drift metric** is a numeric signal produced by drift monitoring that quantifies *how different* a current window is from a baseline (or how different performance has become across time).

In KFM, drift metrics MUST be:

- **deterministic** (same inputs → same outputs),
- **summary-based** (computed from safe summaries, not raw records),
- **policy-safe** (no PII, no secrets, no protected-site coordinates),
- **provenance-bound** (metric values must reference the baseline/window summaries and the metric definition/config).

### Detectors vs. metrics vs. decisions (normative separation)

KFM drift is intentionally layered:

1. **Baselines**  
   Govern what “normal” means for a given model + dataset slice.

2. **Detectors**  
   Compute feature-level comparisons between baseline and window summaries.

3. **Metrics**  
   Standardize numeric outputs, interpretability metadata (direction/range), and aggregation-ready shapes.

4. **Aggregation + Threshold Policy**  
   Converts many metrics → a small set of governance-friendly outcomes (PASS/WARN/FAIL inputs).

This file defines the **metrics** layer: what metrics look like, how they are named/versioned, and how they can be aggregated safely.

### Metric layers (recommended taxonomy)

To keep analysis structured, drift metrics are typically grouped into:

- **Distribution drift metrics**  
  Compare baseline vs window distributions (numeric/categorical).

- **Representation drift metrics**  
  Compare embeddings or multivariate summaries.

- **Performance drift metrics (concept drift proxy)**  
  Compare evaluation performance metrics across time windows (requires labels / evaluation).

- **Pipeline/source drift metrics**  
  Track upstream changes (schema changes, missingness, source mix changes).

- **Policy drift metrics**  
  Track changes in redaction/suppression rates or masking behavior (aggregate-only).

This taxonomy is a documentation and reporting convention; exact metric implementations are defined by detector + configuration profiles.

---

## 🗂️ Directory Layout

### Location in the repo

~~~text
📁 tools/
└── 🧠 ai/
    └── 📁 drift/
        └── 📁 metrics/
            └── 📄 README.md                 # This file
~~~

### Drift context tree (recommended)

This “context tree” helps readers find the other drift submodules.

~~~text
📁 tools/
└── 🧠 ai/
    └── 📁 drift/
        ├── 📄 README.md                     # Drift subsystem overview (entrypoint)
        ├── 📁 baselines/
        │   └── 📄 README.md                 # Baselines: definitions + lifecycle + storage
        ├── 📁 detectors/
        │   └── 📄 README.md                 # Detectors: taxonomy + input/output contracts
        ├── 📁 metrics/
        │   └── 📄 README.md                 # Metrics: taxonomy + contracts + aggregation (this file)
        └── 📁 docs/
            └── 📄 README.md                 # Drift documentation suite (playbooks, rationales)
~~~

### Target metrics submodule structure (create if missing)

The repo snapshot confirms `tools/ai/` exists, but does not enumerate this deep subtree. The structure below is the **intended governed layout** for drift metrics in KFM v11; keep it aligned with real files as they are added.

~~~text
📁 tools/
└── 🧠 ai/
    └── 📁 drift/
        └── 📁 metrics/
            ├── 📄 README.md                           # This file
            │
            ├── 📁 definitions/                        # Metric definitions (names, ranges, directionality)
            ├── 📁 aggregators/                        # Aggregate feature → cohort → model drift scoring
            ├── 📁 registries/                         # Metric registry + compatibility maps
            ├── 📁 thresholds/                         # Default threshold sets (config-driven; governance-reviewed)
            ├── 📁 validators/                         # Schema/range/safety validators for metric outputs
            ├── 📁 tests/                              # Determinism + invariants (if repo pattern allows)
            └── 📁 docs/                               # Notes that expand this README (optional)
~~~

### Where metric outputs belong (normative)

Do NOT store run outputs under `tools/ai/drift/metrics/`.

Metric outputs belong in governed run artifacts:

~~~text
📁 mcp/
└── 📁 experiments/
    └── 📁 <run-id>/
        ├── 🧾 drift_report.json
        ├── 🧾 telemetry.json
        └── 🧾 provenance_bundle.jsonld
~~~

If promoted to a release package, store under `releases/<version>/...` following your repo’s release conventions.

---

## 🧭 Context

### Why this exists even if detectors already output numbers

Detectors may output numbers, but **metrics** are where KFM standardizes:

- naming (`metric_id`, `metric_version`),
- directionality (`higher_is_more_drift`, etc.),
- expected range (bounded vs unbounded),
- aggregation friendliness (consistent schemas),
- safe explainability fields (notes and references only),
- telemetry binding (consistent metric payloads).

This reduces “metric drift” caused by inconsistent output shapes across detectors and domains.

### Relationship to telemetry infrastructure

The repo snapshot explicitly calls out:

- `schemas/telemetry/` as the home for telemetry schemas including **metrics** telemetry formats, and
- `tools/telemetry/` as the tooling for telemetry and metrics aggregation tools.

This metrics layer should align to those schemas/tools by:

- emitting stable metric keys and IDs,
- including provenance references,
- supporting rollups that telemetry aggregators can consume.

### Relationship to governance

Metrics are inputs to governance; they are not governance decisions.

Governance decisions require:

- explicit threshold policies,
- domain-aware interpretation,
- audit trails and provenance bundles,
- FAIR+CARE and sovereignty constraints.

This README defines how metrics remain policy-safe and audit-ready.

---

## 🗺️ Diagrams

### Drift metrics lifecycle (conceptual)

~~~mermaid
flowchart TD
  A["Baseline summaries<br/>(safe aggregates)"] --> D["Detectors compare<br/>baseline vs window"]
  B["Window summaries<br/>(same feature defs)"] --> D
  D --> E["Metric records<br/>(standardized schema)"]
  E --> F["Aggregation<br/>(feature → cohort → model)"]
  F --> G["Threshold policy<br/>(PASS/WARN/FAIL inputs)"]
  E --> H["Telemetry + provenance refs"]
  G --> I["Governance actions<br/>(review/block/retrain)"]
~~~

Accessibility note: metrics standardize detector outputs, then aggregation and thresholds convert them into actionable governance signals.

---

## 🧠 Story Node & Focus Mode Integration

### Narrative drift metrics (recommended patterns)

When drift monitoring applies to Focus Mode / Story Node systems, metrics should remain:

- **aggregate-only**
- **policy-safe**
- **domain-interpretable**

Recommended metric families for narrative systems (examples; configure per domain):

- **retrieval distribution drift**  
  - shift in source type distribution (counts by category, top-k + “other”)
  - shift in time-period buckets (coarse bins; avoid sensitive specifics)

- **evidence density proxies**  
  - citation/ref rate metrics (counts/rates only)
  - “evidence bundle coverage” metrics (percentage of claims linked, if defined)

- **policy drift indicators**  
  - redaction rate shift
  - suppression-trigger rate (small-group suppression, masked-location generalization)

Avoid raw-text outputs in metric payloads. If a narrative example is required, store it as a separate governed artifact with appropriate redaction and do not embed it in drift metric outputs.

---

## 🧪 Validation & CI/CD

### Metric validation expectations (normative)

Every metric record MUST be validated for:

- **schema correctness** (keys and types),
- **range correctness** (if bounded metric, ensure within bounds),
- **directionality correctness** (direction field must match metric definition),
- **reference completeness** (must reference baseline + window identities),
- **policy safety** (no PII/secrets/protected coordinates).

Fail-closed behavior (recommended):

- If a metric cannot be computed due to missing/incomparable inputs, emit:
  - a structured “NOT_COMPUTED / NOT_COMPARABLE” record, and
  - block certification paths unless governance explicitly allows bypass.

### Determinism constraints (normative)

Metric computation MUST:

- avoid randomness unless explicitly seeded and recorded,
- record the exact metric definition version + config hash,
- produce identical results for identical inputs (within documented numeric tolerances).

### CI checks that apply (context)

KFM’s Markdown protocol includes scan-oriented test profiles (e.g., secret and PII scans) and requires consistent fencing/structure for CI-safe docs. Keep examples and any embedded JSON strictly policy-safe.

---

## 📦 Data & Metadata

### Metric record contract (recommended minimal shape)

A metric record should be stable and aggregation-ready.

~~~json
{
  "metric_id": "distribution.js_divergence",
  "metric_version": "1.0.0",

  "scope": {
    "model_id": "focus_mode_v3_narrative",
    "model_version": "11.2.6",
    "dataset_id": "dcat:kfm:dataset:docs-corpus:v11",
    "dataset_version": "v11",
    "feature_name": "embedding_norm",
    "feature_type": "numeric",
    "cohort_id": "all"
  },

  "value": {
    "metric_name": "js_divergence",
    "metric_value": 0.042,
    "expected_range": [0.0, 1.0],
    "direction": "higher_is_more_drift"
  },

  "refs": {
    "baseline_ref": "mcp/experiments/<baseline-run-id>/baseline.json#sha256:<sha256>",
    "window_ref": "mcp/experiments/<run-id>/window_summary.json#sha256:<sha256>",
    "detector_ref": "tools/ai/drift/detectors/<detector_id>",
    "config_ref": "tools/ai/configs/<profile>#sha256:<sha256>"
  },

  "quality": {
    "comparable": true,
    "not_computed_reason": null,
    "suppressed_small_groups": false
  },

  "created": "2025-12-15T00:00:00Z"
}
~~~

Notes:

- The exact set of fields can be expanded, but MUST remain deterministic and schema-valid.
- `baseline_ref` and `window_ref` MUST be stable references (path + hash or similar).
- `cohort_id` MUST be policy-safe (avoid identifiers that could re-identify individuals or protected sites).

### Metric definition registry (recommended)

A metrics registry should define:

- stable metric IDs,
- meaning and directionality,
- expected range,
- supported feature types,
- required inputs (histogram, quantiles, counts, etc.),
- numeric stability notes.

Recommended shape (illustrative):

~~~json
{
  "metric_id": "distribution.js_divergence",
  "metric_version": "1.0.0",
  "feature_types_supported": ["numeric", "categorical"],
  "inputs_required": ["histogram"],
  "expected_range": [0.0, 1.0],
  "direction": "higher_is_more_drift",
  "notes": "Computed on aligned bin edges; fails closed if binning differs."
}
~~~

Place registries under `metrics/registries/` if used, and keep them governed and versioned.

---

## 🌐 STAC, DCAT & PROV Alignment

### DCAT alignment

Metrics are not datasets, but drift reports and telemetry bundles can be represented as **distributions** or audit artifacts that reference datasets.

Recommended:

- use DCAT identifiers for datasets in metric scope fields,
- publish summary-level drift reports as distributions where appropriate,
- keep raw drift windows and baseline computation details as provenance references.

### STAC alignment

When drift metrics relate to spatial assets:

- reference STAC Items/Assets by ID/key
- compute metrics from safe summary products (e.g., per-band histograms, region-level aggregates)
- avoid embedding spatial data extracts in metric outputs

### PROV-O alignment

Metric computation can be represented as:

- metric record: `prov:Entity`
- metric computation: `prov:Activity`
- baseline summary, window summary: `prov:Entity`
- configuration profile: `prov:Entity`
- CI runner/pipeline: `prov:Agent`

Key links:

- metric computation `prov:used` baseline + window + config
- metric record `prov:wasGeneratedBy` metric computation activity
- activity `prov:wasAssociatedWith` a governed agent

This makes metrics auditable and replayable.

---

## 🧱 Architecture

### Aggregation strategy (recommended)

Drift typically produces many feature-level metrics. KFM should aggregate in stages:

1. **Feature-level**  
   metric per feature (and optionally per cohort).

2. **Cohort-level**  
   aggregate within cohort (e.g., median drift across features, weighted aggregates).

3. **Model-level**  
   produce a compact model drift score or category-specific rollups:
   - input drift rollup
   - output drift rollup
   - performance drift rollup (if available)

Aggregation should be:

- config-driven,
- deterministic,
- transparent (record which features/cohorts were included and why),
- policy-safe (suppress cohorts with low counts).

### Metric comparability rules (normative)

Metrics MUST NOT be aggregated across incomparable definitions.

Incomparability triggers include:

- feature definition changes (units/normalization change),
- histogram binning mismatch (for histogram-based metrics),
- cohort definition changes (labels or slicing rules differ),
- baseline type mismatch when strict comparability is required.

If comparability fails, aggregation MUST either:

- exclude the metric with a recorded reason, or
- fail closed for certification paths.

### Adding a new metric (recommended process)

1. Define the metric in the registry (ID, version, direction, range, required inputs).
2. Implement computation in a deterministic way (prefer summary-driven).
3. Add validator rules (range/type/reference checks).
4. Add test cases for determinism and known-edge behavior.
5. Add/adjust config profiles to select and threshold the metric.
6. Update drift docs/playbooks if interpretation changes.
7. Ensure CI scans and schema lint pass.

---

## ⚖ FAIR+CARE & Governance

### Safety constraints (normative)

Drift metrics MUST:

- never log raw inputs or raw outputs,
- never include PII or secrets,
- never include protected-site coordinates or overly precise sensitive locations,
- suppress small-group metrics when re-identification risk exists.

### Governance control points

Changes to any of the following should require governance review:

- metric definitions that change meaning/range/direction,
- threshold policies for PASS/WARN/FAIL inputs,
- cohort definitions or suppression rules,
- any domain guide that affects how drift outcomes are interpreted.

### Training prohibition

Drift metrics and drift reports are governance artifacts and MUST NOT be used as AI training data.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v11.2.6** | 2025-12-15 | Created drift metrics README: defined drift metric purpose and contracts, recommended metrics taxonomy and registry patterns, aggregation strategy, comparability rules, and provenance/telemetry alignment for governance-safe drift monitoring in KFM v11. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
📏 Drift Metrics · Governed for Integrity

[⬅️ Back to Drift Monitoring](../README.md) · [🧱 Baselines](../baselines/README.md) · [🧭 Detectors](../detectors/README.md) · [📚 Drift Docs](../docs/README.md) · [⚙️ Configs](../../configs/README.md) · [📡 Telemetry](../../telemetry/README.md) · [🧾 Provenance](../../provenance/README.md) · [🛡 Governance](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>