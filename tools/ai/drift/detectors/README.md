---
title: "🧭 Kansas Frontier Matrix — AI Drift Detectors"
path: "tools/ai/drift/detectors/README.md"

version: "v11.2.6"
last_updated: "2025-12-15"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous · FAIR+CARE Council Oversight"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Architecture"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:doc:tools-ai-drift-detectors-readme:v11.2.6"
semantic_document_id: "kfm-doc-tools-ai-drift-detectors"
event_source_id: "ledger:tools/ai/drift/detectors/README.md"
immutability_status: "mutable-plan"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
prov_profile: "KFM-PROV v11"
dcat_profile: "KFM-DCAT v11"
stac_profile: "KFM-STAC v11"

# NOTE: Repo snapshot (12-14-25) confirms releases/ exists and cites v11.2.2 as an example.
# Update these refs if your current governed release folder differs.
sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/tools-ai-governance-v4.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

# Optional (not confirmed in repo snapshot): point these at the actual schema files if/when present.
json_schema_ref: "../../../../schemas/json/tools-ai-drift-detector-v11.schema.json"
shape_schema_ref: "../../../../schemas/shacl/tools-ai-drift-detector-v11.shape.ttl"

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
ai_training_guidance: "Detector configs, detector outputs, and drift governance artifacts MUST NOT be used as training data."

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

# 🧭 **KFM — AI Drift Detectors**
`tools/ai/drift/detectors/README.md`

**Purpose**  
Define the **drift detector subsystem** used by KFM drift monitoring:  
the governed set of detector types, their input contracts (baseline + window summaries), output contracts (metrics + severity), and validation rules so drift scores are deterministic, provenance-bound, and policy-safe.

</div>

---

## 📘 Overview

### What a “drift detector” is (normative)

A **drift detector** is a governed, versioned computation that compares:

- a **baseline summary** (what “normal” looked like), and
- a **current window summary** (what is happening now),

and produces:

- one or more drift metrics (numeric),
- optional statistical signals (e.g., p-values, confidence bounds),
- a severity mapping for governance (PASS/WARN/FAIL inputs, not final decisions).

In KFM, detectors operate on **summaries**, not raw data, to preserve:

- reproducibility (stable inputs),
- privacy/safety (no row-level outputs),
- performance (bounded memory and compute).

### What this subsystem governs

This directory defines:

- **detector taxonomy** (what detector kinds exist),
- **detector contracts** (inputs required and outputs produced),
- **selection rules** (which detectors apply to which feature types),
- **safety constraints** (no PII, no secrets, no protected-site coords),
- **validation expectations** (schema + invariant checks).

Repo snapshot (12-14-25) confirms `tools/ai/` exists and is described as “AI evaluation and drift analysis tools.” This detectors submodule is part of that drift analysis umbrella. Deeper `tools/ai/drift/**` structure is not enumerated in the snapshot, so file-level inventories below are treated as **intended canonical structure** unless validated against the live repo checkout.

### Core invariants (normative)

1. **Detectors MUST be deterministic**  
   Same baseline summary + same window summary + same detector config → same drift metric.

2. **Detectors MUST be summary-based**  
   Detectors MUST NOT require raw record-level data as inputs in governed runs.

3. **Detectors MUST be versioned**  
   Every detector must have a stable `detector_id` and a `detector_version`.

4. **Detectors MUST be policy-safe**  
   Detector outputs MUST NOT include:
   - PII,
   - secrets,
   - protected-site coordinates,
   - raw samples.

5. **Missing/invalid detector inputs MUST fail closed** for certification paths.

---

## 🗂️ Directory Layout

### Where this fits in the repo

~~~text
📁 tools/
└── 🧠 ai/
    └── 📁 drift/
        └── 📁 detectors/
            └── 📄 README.md                 # This file
~~~

### Target detectors submodule structure (create if missing)

Keep this structure accurate as detectors are implemented.

~~~text
📁 tools/
└── 🧠 ai/
    └── 📁 drift/
        └── 📁 detectors/
            ├── 📄 README.md                           # This file
            │
            ├── 📁 numeric/                            # Detectors for numeric distributions
            ├── 📁 categorical/                        # Detectors for categorical distributions
            ├── 📁 multivariate/                       # Detectors for multivariate/embedding drift
            ├── 📁 timeseries/                         # Detectors tailored to temporal dynamics (optional)
            │
            ├── 📁 registries/                         # Detector registry + compatibility maps
            ├── 📁 interfaces/                         # Shared detector interfaces/contracts
            ├── 📁 validators/                         # Schema + safety validators for detector outputs
            ├── 📁 tests/                              # Determinism + invariant tests (if repo pattern allows)
            └── 📁 docs/                               # Optional notes (publishable and policy-safe)
~~~

### Where detector outputs belong (normative)

Do not store detector outputs under `tools/ai/drift/detectors/`.

Detector outputs should be stored with governed run artifacts:

~~~text
📁 mcp/
└── 📁 experiments/
    └── 📁 <run-id>/
        ├── 🧾 drift_report.json
        ├── 🧾 telemetry.json
        └── 🧾 provenance_bundle.jsonld
~~~

If drift reports are promoted to release packets, store them in the release folder pattern used by your repo (not confirmed in snapshot at subfolder level).

---

## 🧭 Context

### Detectors vs. drift decisions (normative)

Detectors produce **signals**. They do not make final governance decisions.

A typical chain is:

- detector computes metric(s)
- drift monitor aggregates metrics across features/cohorts
- governance thresholds map aggregate to PASS/WARN/FAIL
- actions policy determines what happens next (alert, block, review, retrain)

This separation matters because:

- detectors should remain general and reusable
- governance remains config-driven and domain-aware
- policy changes should not require rewriting detector math

### Baseline and window summaries as required inputs

Detectors require two inputs:

- **baseline summary**: built via baseline builders (see `tools/ai/drift/baselines/README.md`)
- **window summary**: built from the current evaluation window using the same feature definitions and binning

Detectors must validate:

- feature compatibility (same feature name/type/unit normalization)
- binning compatibility (if histogram-based)
- cohort/slice compatibility (if cohorting is applied)

If compatibility fails, detectors must fail closed (or explicitly emit a “not comparable” status that blocks certification).

### Why KFM prefers detector summaries

Summary-driven detectors:

- enable reproducible comparisons (histograms/quantiles/stats are stable)
- reduce risk of leaking sensitive content
- keep compute bounded for CI and scheduled monitoring

---

## 🗺️ Diagrams

### Detector execution in the drift pipeline (conceptual)

~~~mermaid
flowchart TD
  A["Baseline summary<br/>(from baselines/)"] --> C["Detector compute()"]
  B["Window summary<br/>(current slice)"] --> C
  C --> D["Per-feature drift metrics<br/>(detector output contract)"]
  D --> E["Aggregation layer<br/>(feature → cohort → model score)"]
  E --> F["Threshold policy<br/>(PASS/WARN/FAIL inputs)"]
  F --> G["Governance actions<br/>(review/block/retrain)"]
  D --> H["Telemetry + provenance refs"]
~~~

Accessibility note: detectors sit between summaries and aggregation; they produce metrics and references.

---

## 🧠 Story Node & Focus Mode Integration

### Drift detection for narrative systems (recommended)

For Focus Mode / Story Node systems, drift detection is often about:

- **retrieval drift**: sources used and their distribution changing over time
- **evidence drift**: citation/reference density changing
- **coverage drift**: which regions/time periods/domains are represented changing
- **policy drift**: redaction/suppression patterns changing (should be logged)

Detectors in narrative domains MUST remain policy-safe:

- never store raw narrative text in detector outputs
- compare aggregates and references only (counts, rates, distribution summaries)

Recommended narrative drift features (examples; confirm implementation in code/config):

- citations-per-1k-tokens distribution (summary-only)
- sources-used-count distribution
- source-type exposure distribution (top-k categories)
- redaction-applied rate (boolean rate summary)

---

## 🧪 Validation & CI/CD

### Determinism requirements (normative)

Detector implementations MUST:

- be deterministic (no random sampling unless explicitly pinned and recorded)
- avoid non-deterministic floating behaviors where possible (record versions and tolerances)
- accept explicit config and avoid hidden global state

### Compatibility validation (normative)

Before computing a drift metric, a detector MUST validate:

- `feature_name` matches
- `feature_type` matches (`numeric`, `categorical`, `embedding`, etc.)
- `summary_schema_version` matches (if versioned)
- histogram bin edges match (if histogram-based)
- cohort/slice identifiers match (when comparing cohort-specific summaries)

If these checks fail:

- certification-path drift should FAIL (fail closed), or
- emit an explicit “NOT_COMPARABLE” status that downstream gating treats as FAIL.

### Output validation (normative)

Detector output MUST be:

- schema-valid (when schema exists)
- key-stable (predictable keys and types)
- policy-safe (no PII/secrets/protected coords)

CI SHOULD enforce:

- schema validation on detector outputs (where applicable)
- unit tests for determinism and invariants
- safety scan on drift reports intended for repo storage

---

## 📦 Data & Metadata

### Detector output contract (recommended minimal shape)

A single detector result SHOULD include:

- identity:
  - `detector_id`
  - `detector_version`
- what was measured:
  - `feature_name`
  - `feature_type`
  - optional `cohort_id` (policy-safe cohort label)
- metric:
  - `metric_name`
  - `metric_value`
  - optional `p_value` / `confidence` (if meaningful)
- interpretability:
  - `direction` (optional; e.g., “higher means more drift”)
  - `notes` (policy-safe)
- references:
  - `baseline_ref` (id/hash/path reference)
  - `window_ref` (id/hash/path reference)

Example (illustrative):

~~~json
{
  "detector_id": "js_divergence_numeric",
  "detector_version": "1.0.0",
  "feature_name": "embedding_norm",
  "feature_type": "numeric",
  "metric_name": "js_divergence",
  "metric_value": 0.042,
  "direction": "higher_is_more_drift",
  "refs": {
    "baseline_ref": "mcp/experiments/<baseline-run-id>/baseline.json#sha256:<sha256>",
    "window_ref": "mcp/experiments/<run-id>/window_summary.json#sha256:<sha256>"
  }
}
~~~

### Detector registry (recommended)

KFM drift monitoring benefits from a registry that maps:

- detector → supported feature types
- detector → required summary inputs
- detector → default thresholds (optional; thresholds usually live in config profiles)

If implemented, place it under `detectors/registries/` and ensure it is governed and versioned.

---

## 🌐 STAC, DCAT & PROV Alignment

### DCAT alignment

When detectors operate on dataset-level summaries:

- reference datasets using stable DCAT identifiers (`dataset_id`, `dataset_version`)
- drift reports should link to the dataset metadata rather than embedding raw data

### STAC alignment

When detectors operate on spatial assets:

- reference STAC Item IDs and asset keys
- compute drift on safe aggregates (histograms, quantiles) derived from assets

### PROV-O alignment

Detector computation can be represented as part of the drift monitoring activity:

- baseline summary: `prov:Entity`
- window summary: `prov:Entity`
- detector run: `prov:Activity`
- detector result: `prov:Entity`
- agent (CI runner/pipeline): `prov:Agent`

Relations:

- `prov:used` (activity uses baseline and window summaries)
- `prov:wasGeneratedBy` (detector result generated by detector activity)
- `prov:wasAssociatedWith` (activity associated with a governed agent)

This ensures detector outputs remain traceable and auditable.

---

## 🧱 Architecture

### Detector taxonomy (recommended categories)

These categories are common in drift systems. Confirm exact implementation in code/config.

#### Numeric distribution detectors
Operate on numeric feature summaries (histograms/quantiles/stats):

- divergence-based (e.g., JS/KL on histograms)
- distance-based (e.g., Wasserstein/EMD on binned distributions)
- test-based (e.g., KS test using binned approximations or summary proxies)
- stability indices (e.g., PSI using histogram bins)

#### Categorical distribution detectors
Operate on categorical counts (top-k + “other” bucket):

- total variation distance (TVD) on category distributions
- chi-square-like comparisons (aggregate-only; avoid small cell leaks)
- entropy shift comparisons

#### Multivariate / embedding drift detectors
Operate on embedding summary statistics (aggregated):

- centroid shift (mean vector delta; store only safe aggregates)
- covariance/variance shift (summary-level)
- MMD-like approximations (only if deterministic and summary-compatible)

#### Time-series drift detectors (domain-dependent)
Operate on temporal summary features:

- seasonal profile drift (compare seasonal summaries)
- change-point or regime-shift signals (aggregate-only outputs)

### Detector selection rules (recommended defaults)

Selection should be config-driven, but a typical safe mapping is:

- numeric → one divergence detector + one distance detector
- categorical → one distribution distance detector
- embeddings → centroid/covariance summary drift
- timeseries domains → add seasonal drift feature and corresponding detector

### Adding a new detector (recommended process)

1. Implement detector under the correct category folder.
2. Add detector to the detector registry (if used).
3. Add/adjust config profiles to select and threshold the detector.
4. Add determinism tests and safety validations.
5. Update drift monitor docs and version history.
6. Ensure CI passes (schema-lint, markdown-lint, tests, safety scans).

---

## ⚖ FAIR+CARE & Governance

### Safety constraints (normative)

Detectors MUST:

- avoid PII and secrets in outputs
- avoid storing protected-site coordinates
- suppress small cohort outputs if they risk re-identification
- store only aggregates and stable references

### Sovereignty-sensitive domains

For domains requiring masking/generalization:

- detectors should operate on generalized spatial resolutions (e.g., coarse region classes)
- avoid “drill-down” metrics that could reveal restricted locations
- ensure suppression rules are enforced for low-count cohorts

### Training prohibition

Detector configs and detector outputs are governance artifacts and MUST NOT be used as training data (`ai_training_allowed: false`).

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v11.2.6** | 2025-12-15 | Created drift detectors README: defined detector purpose and invariants, intended directory structure, input/output contracts, determinism and validation rules, and provenance/catalog alignment for KFM AI drift detector implementations. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
🧭 Drift Detectors · Governed for Integrity

[⬅️ Back to Drift Monitoring](../README.md) · [🧱 Baselines](../baselines/README.md) · [⚙️ Config Profiles](../../configs/README.md) · [📡 Telemetry](../../telemetry/README.md) · [🧾 Provenance](../../provenance/README.md) · [🛡 Governance](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>