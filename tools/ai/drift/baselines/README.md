---
title: "🧱 Kansas Frontier Matrix — AI Drift Baselines"
path: "tools/ai/drift/baselines/README.md"

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

doc_uuid: "urn:kfm:doc:tools-ai-drift-baselines-readme:v11.2.6"
semantic_document_id: "kfm-doc-tools-ai-drift-baselines"
event_source_id: "ledger:tools/ai/drift/baselines/README.md"
immutability_status: "mutable-plan"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
prov_profile: "KFM-PROV v11"
dcat_profile: "KFM-DCAT v11"
stac_profile: "KFM-STAC v11"

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"

telemetry_ref: "../../../../releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/tools-ai-governance-v4.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

json_schema_ref: "../../../../schemas/json/tools-ai-drift-baseline-v11.schema.json"
shape_schema_ref: "../../../../schemas/shacl/tools-ai-drift-baseline-v11.shape.ttl"

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
ai_training_guidance: "Baseline artifacts and governance audit records MUST NOT be used as training data."

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

# 🧱 **KFM — AI Drift Baselines**
`tools/ai/drift/baselines/README.md`

**Purpose**  
Define the **baseline system** used by KFM drift monitoring:  
how baselines are built, versioned, stored, validated, and referenced so drift checks remain deterministic, provenance-bound, and governance-safe.

</div>

---

## 📘 Overview

### What a “drift baseline” is (normative)

A **drift baseline** is a governed, versioned representation of “what normal looked like” for a model and a dataset slice, so future windows can be compared consistently.

Baselines are **not** raw datasets. They are **summaries** and **reference distributions** (or reference statistics) used by drift detectors.

A baseline answers:

- *What distribution did this model see (or produce) when it was certified?*
- *Which exact dataset slice and versions does that distribution represent?*
- *What metrics and feature definitions were used to summarize it?*
- *Under what governance constraints was it computed and stored?*

### Why baselines are required

Without baselines, drift monitoring becomes:

- non-reproducible (comparisons change depending on “what you pick today”),
- hard to audit (no stable reference point),
- unsafe (inconsistent choices can hide real drift or overstate it).

KFM uses baselines to keep drift checks:

- deterministic (same baseline + same window → same drift score),
- traceable (baseline identity recorded in telemetry + provenance),
- policy-safe (aggregates and references only).

### Baseline types supported (recommended)

KFM drift monitoring typically uses one of these baseline types:

- **Training baseline**  
  The distribution of inputs/outputs captured from the training/evaluation dataset version used to certify the model.

- **Release baseline**  
  A baseline captured from a certified release packet or a “last known good” production window.

- **Seasonal baseline** (domain-dependent)  
  A baseline chosen for seasonal comparability (e.g., hydrology/climate patterns).

- **Sensor / source baseline** (remote sensing)  
  A baseline tied to a sensor/source version so sensor drift is not confused with model drift.

- **Rolling baseline** (monitoring-only)  
  A trailing window baseline used for operational monitoring; not recommended as the only baseline for certification decisions.

Baseline type must be explicit and recorded.

### Baseline safety rule (normative)

Baselines MUST contain only:

- derived aggregates, histograms, quantiles, or safe summary statistics
- stable IDs and references (DCAT/STAC/provenance IDs)
- checksums/hashes for reproducibility

Baselines MUST NOT contain:

- secrets
- PII
- protected-site coordinates
- raw record-level data dumps

---

## 🗂 Directory Layout

### Where this fits in the repo

Repository snapshot notes that `tools/ai/` exists under `tools/` as the location for **AI evaluation and drift analysis tools** (high-level repo inventory). This directory provides the **baseline submodule** for that drift tooling.

~~~text
📁 tools/
└── 🧠 ai/
    └── 📁 drift/
        └── 📁 baselines/
            └── 📄 README.md                 # This file
~~~

### Target baseline submodule structure (create if missing)

This layout is the **intended** structure for baseline management. Keep it accurate as files are added.

~~~text
📁 tools/
└── 🧠 ai/
    └── 📁 drift/
        └── 📁 baselines/
            ├── 📄 README.md                           # This file
            │
            ├── 📁 builders/                           # Build baseline summaries from a dataset slice
            ├── 📁 selectors/                          # Choose baseline (training/release/seasonal/etc.)
            ├── 📁 formats/                            # Canonical baseline JSON shapes (helpers)
            ├── 📁 validators/                         # Schema + safety validation (no PII/secrets)
            ├── 📁 hashing/                            # Stable hashing and checksum helpers
            └── 📁 docs/                               # Optional notes (publishable and policy-safe)
~~~

### Where baseline artifacts should be stored (normative)

Do not commit large baseline outputs into `tools/ai/drift/baselines/`.

Baseline artifacts should live with governed run artifacts, using the project’s experiment pattern:

~~~text
📁 mcp/
└── 📁 experiments/
    └── 📁 <run-id>/
        ├── 🧾 baseline.json
        ├── 🧾 baseline.sha256
        ├── 🧾 telemetry.json
        └── 🧾 provenance_bundle.jsonld
~~~

If a baseline is promoted to a release packet, store it under a release directory (path must match repo release conventions):

~~~text
📁 releases/
└── 📁 <version>/
    └── 📁 ai/
        └── 📁 baselines/
            ├── 🧾 baseline.<baseline_id>.json
            └── 🧾 baseline.<baseline_id>.sha256
~~~

Note: the exact release subpath for AI baselines must match existing repo release conventions.

---

## 🧭 Context

### Baselines are a contract between drift detectors and governance

Drift detectors need baselines that are:

- consistent in feature definitions,
- consistent in binning / summary method,
- consistent in governance redaction/suppression rules,
- linked to exact model/data/config identity.

Therefore, baseline building is a **governed activity**, not an ad-hoc preprocessing step.

### Baseline selection is as important as drift math (normative)

A drift score is only meaningful if baseline selection is defensible.

Baseline selection must always specify:

- baseline type (training / release / seasonal / sensor / rolling)
- baseline slice definition (time interval, spatial scope category, cohort labels)
- baseline provenance reference (where the baseline came from)
- baseline checksum (sha256)

If any baseline selection input is missing, drift monitoring should fail closed for certification paths.

### Baseline scope dimensions (recommended)

Baseline scope is typically defined by:

- **time**: instant or interval, seasonality tag
- **space**: region classes (avoid precise restricted locations; use generalized regions or H3 tiers where policy requires)
- **domain**: hydrology, remote sensing, narrative retrieval, etc.
- **model**: model_id + version/hash
- **data**: dataset_id + version (+ STAC/DCAT refs)
- **config**: drift profile id/version + sha256

Baselines should not be “global” unless governance explicitly allows it and the domain supports it.

---

## 🗺 Diagrams

### Baseline lifecycle and use (conceptual)

~~~mermaid
flowchart TD
  A["Choose baseline strategy<br/>(training | release | seasonal | sensor | rolling)"] --> B["Select dataset slice<br/>(ID + version + interval)"]
  B --> C["Compute baseline summaries<br/>(histograms/quantiles/stats)"]
  C --> D["Validate baseline<br/>(schema + safety + completeness)"]
  D -->|PASS| E["Store baseline artifact<br/>(mcp/experiments/<run-id>/...)"]
  D -->|FAIL| F["Fail closed<br/>(block certification / require review)"]
  E --> G["Drift run selects baseline<br/>(baseline_id + sha256)"]
  G --> H["Compare current window<br/>→ compute drift metrics"]
  H --> I["Emit drift report + telemetry<br/>(references baseline)"]
~~~

Accessibility note: baselines are built from slices, validated, stored with hashes, then referenced by drift runs.

---

## 🧪 Validation & CI/CD

### Baseline config inputs (normative)

Baseline building MUST be config-driven (via `tools/ai/configs/` profiles), including:

- which features/metrics are summarized
- binning strategy (explicit bin edges or deterministic binning rules)
- suppression rules for small cohorts (privacy/safety)
- required output fields
- storage destination policy (mcp experiments vs release promotion)

Baseline builders must record:

- `config_profile_id`
- `config_profile_version`
- `config_sha256`

### Fail-closed conditions (normative)

Baseline validation MUST FAIL if:

- model identity is missing (when baseline is model-scoped)
- dataset identity/version is missing
- slice definition is missing or ambiguous
- baseline contains disallowed content (PII/secrets/protected coordinates)
- required summary fields are missing
- schema validation fails (when schema is enforced)

### CI checks (recommended)

When baseline artifacts are included in PRs/releases, CI should enforce:

- JSON validity + schema validation
- `sha256` checksum file present and correct
- safety scan (no secrets/PII)
- deterministic key presence checks
- baseline selection references in drift reports are resolvable

---

## 📦 Data & Metadata

### Baseline artifact: recommended minimal shape

A baseline artifact is a JSON object with:

- identity (`baseline_id`, `baseline_version`, `baseline_type`)
- scope (dataset slice + model scope)
- config identity (profile + sha256)
- summary content (histograms/quantiles/stats)
- safety and suppression record
- hashes/checksums (or external checksum file reference)
- references to provenance and telemetry

Example (illustrative):

~~~json
{
  "baseline_id": "focus_mode_v3_docs_corpus_release_baseline_2025_11",
  "baseline_version": "11.2.6",
  "baseline_type": "release",
  "model": {
    "model_id": "focus_mode_v3_narrative",
    "model_version": "11.2.6"
  },
  "dataset": {
    "dataset_id": "dcat:kfm:dataset:docs-corpus:v11",
    "dataset_version": "v11",
    "slice": {
      "time": "2025-10-15/2025-11-15",
      "notes": "release baseline slice"
    }
  },
  "config": {
    "profile_id": "drift_thresholds.default",
    "profile_version": "11.2.6",
    "config_sha256": "<sha256>"
  },
  "summaries": {
    "numeric": [
      {
        "feature": "embedding_norm",
        "stats": { "mean": 0.0, "std": 1.0, "p50": 0.0, "p95": 0.0 },
        "histogram": { "bin_edges": [0, 1], "counts": [0] }
      }
    ],
    "categorical": [
      {
        "feature": "source_type",
        "top_k": [
          { "value": "docs", "count": 0 },
          { "value": "datasets", "count": 0 }
        ]
      }
    ]
  },
  "safety": {
    "contains_pii": false,
    "contains_secrets": false,
    "protected_location_precision": "none",
    "suppressed_small_groups": true
  },
  "refs": {
    "telemetry_ref": "mcp/experiments/<run-id>/telemetry.json",
    "provenance_bundle_ref": "mcp/experiments/<run-id>/provenance_bundle.jsonld"
  }
}
~~~

Numbers and features above are placeholders. Real baseline fields must match the drift detectors and the governed config profiles.

### Feature definitions (normative)

Baseline summaries must include enough metadata to interpret them:

- feature name and type
- unit or normalization note (if applicable)
- binning method and bin edges (if histogram-based)
- cohort/slice description (if cohorting is applied)

If a feature definition changes between versions, it must be treated as:

- a new baseline version, or
- a new baseline_id

---

## 🌐 STAC, DCAT & PROV Alignment

### DCAT: dataset baselines and distributions

Baselines should reference datasets by DCAT identifiers where possible:

- `dataset_id` → DCAT dataset identifier
- baseline artifact (if published) may be treated as a distribution artifact linked to the dataset or the model governance package

Baseline artifacts should not replace dataset metadata; they are audit-support artifacts.

### STAC: baselines for spatial assets (optional)

When drift monitoring is applied to spatial outputs (tiles, rasters, vectors):

- baseline summaries should reference STAC Collection/Item IDs and asset keys
- baseline content should remain aggregated (e.g., histograms of pixel values, safe region summaries)
- do not embed tiles or images in baseline JSON

### PROV-O: baselines as first-class Entities (recommended)

Represent baseline building as:

- baseline artifact: `prov:Entity`
- baseline build: `prov:Activity`
- builder agent (CI/pipeline/operator role): `prov:Agent`

Key relationships:

- `prov:used`:
  - dataset slice entity
  - model artifact entity (if model-scoped)
  - config profile entity
- `prov:wasGeneratedBy`:
  - baseline entity generated by baseline-build activity
- `prov:wasAssociatedWith`:
  - baseline-build activity associated with a governed agent

This ensures baselines are reproducible and auditable.

---

## 🧱 Architecture

### Designing baselines for different task types (recommended patterns)

**Tabular / time-series (hydrology, climate)**  
- per-feature histograms or quantiles
- seasonal tags and seasonal baselines where required
- separate baselines per sensor/source version when input sources shift

**Remote sensing (rasters, segmentation/classification)**  
- per-band histograms
- region-level safe aggregates
- baseline per sensor/source (to avoid confusing sensor drift with model drift)

**Retrieval / ranking**  
- distribution of retrieved source types (safe aggregates)
- rank position distribution (e.g., “how often a source type appears in top-k”)
- coverage/parity proxies by policy-permitted cohorts

**Narrative generation**  
- safe output aggregates:
  - length distribution
  - citation rate proxies (refs per 1k tokens)
  - evidence density proxies (percent claims linked) if defined by tooling
- avoid storing raw text; store only aggregates and references

### Baseline versioning strategy (normative)

Baseline IDs should change when any of the following changes:

- model version/hash changes (for model-scoped baselines)
- dataset version changes
- feature set changes
- binning strategy changes
- governance redaction/suppression rules change
- config profile sha256 changes

A baseline is only comparable if its definitions are comparable.

---

## ⚖ FAIR+CARE & Governance

### Sovereignty and sensitive domains (normative)

Baselines must be safe under:

- `governance_ref`
- `ethics_ref`
- `sovereignty_policy`

Operationally:

- aggregate at safe spatial resolutions for sensitive content (generalize; never store protected coordinates)
- suppress small groups (avoid re-identification)
- never store raw sensitive imagery patches or raw narrative text in baseline artifacts

### Publication rule

Baseline artifacts intended for wide publication must be:

- aggregated
- redaction-safe
- approved by governance policy for the domain

Otherwise, store baselines only in governed run artifacts (`mcp/experiments/...`) and reference them by ID/hash.

### Training prohibition

Baseline artifacts and governance audit records MUST NOT be used as training data (`ai_training_allowed: false`).

---

## 🕰 Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v11.2.6** | 2025-12-15 | Created drift baselines README: defined baseline types, lifecycle, storage destinations, validation/fail-closed rules, recommended baseline artifact shape, and STAC/DCAT/PROV alignment for KFM AI drift baseline management. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
🧱 Drift Baselines · Governed for Integrity

[⬅️ Back to Drift Monitoring](../README.md) · [⚙️ Config Profiles](../../configs/README.md) · [📡 Telemetry](../../telemetry/README.md) · [🧾 Provenance](../../provenance/README.md) · [🛡 Governance](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>