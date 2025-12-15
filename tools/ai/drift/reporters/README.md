---
title: "🧾 Kansas Frontier Matrix — AI Drift Reporters"
path: "tools/ai/drift/reporters/README.md"

version: "v11.2.6"
last_updated: "2025-12-15"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous · FAIR+CARE Council Oversight"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Architecture"
intent: "tools-ai-drift-reporters"
role: "drift-reporting-registry"
category: "AI · Drift · Reporting · Governance · Telemetry"

header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:doc:tools-ai:drift:reporters-readme:v11.2.6"
semantic_document_id: "kfm-doc-tools-ai-drift-reporters"
event_source_id: "ledger:tools/ai/drift/reporters/README.md"
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

# Optional (point these at real schema files if/when present).
json_schema_ref: "../../../../schemas/json/tools-ai-drift-reporters-v11.schema.json"
shape_schema_ref: "../../../../schemas/shacl/tools-ai-drift-reporters-v11.shape.ttl"

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
ai_training_guidance: "Drift reports, drift telemetry, and governance/audit artifacts MUST NOT be used as AI training data."

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

# 🧾 **KFM — AI Drift Reporters**
`tools/ai/drift/reporters/README.md`

**Purpose**  
Define the **reporting layer** for KFM drift monitoring — the governed components that transform
**drift metrics + provenance references** into **human-readable reports**, **machine-readable bundles**,
and **telemetry-ready outputs** suitable for CI gates, audits, releases, and dashboards.

</div>

---

## 📘 Overview

### What is a “drift reporter” (normative)

A **drift reporter** is a deterministic renderer/packager that:

- consumes drift outputs (feature summaries, metric records, aggregation results),
- enriches those outputs with stable references (baseline/window/config/code),
- emits governed artifacts in standard formats for:
  - CI visibility,
  - governance review,
  - reproducible release packaging,
  - telemetry ingestion,
  - downstream narrative/UI surfaces.

Drift reporters do **not** compute drift metrics; they **standardize and publish** the results.

### Reporter outputs (canonical artifact set)

For a single drift run, reporters SHOULD be able to emit:

1. **Canonical machine report**  
   `drift_report.json` (schema-valid, stable keys, reference-first)

2. **Human summary**  
   `drift_report.md` (short, CI-friendly, a11y-safe)

3. **Telemetry bundle**  
   `drift_telemetry.json` (metrics suitable for `tools/telemetry/**` aggregation)

4. **Provenance bundle (optional but recommended)**  
   `drift_provenance.jsonld` (PROV-O aligned references)

5. **Checksums and manifest slices (recommended)**  
   `checksums.sha256` and/or a small “artifact manifest” JSON for reproducibility

### Absolute constraints (normative)

Drift reporters MUST:

- be **deterministic** (same inputs → byte-identical outputs when feasible),
- be **policy-safe** (no raw rows, no secrets, no PII, no protected-site coordinates),
- be **reference-first** (prefer stable refs + hashes over embedded raw data),
- be **provenance-bound** (include baseline/window/config/code identity fields),
- fail **closed** when inputs are non-comparable or incomplete on certification paths.

---

## 🗂️ Directory Layout

### Location in the repo

~~~text
📁 tools/
└── 🧠 ai/
    └── 📁 drift/
        └── 📁 reporters/
            └── 📄 README.md                 # This file
~~~

### Drift context tree (recommended)

~~~text
📁 tools/
└── 🧠 ai/
    └── 📁 drift/
        ├── 📄 README.md                     # Drift subsystem overview
        ├── 📁 baselines/
        │   └── 📄 README.md                 # Baselines (definition + lifecycle)
        ├── 📁 detectors/
        │   └── 📄 README.md                 # Detectors (compute drift signals)
        ├── 📁 metrics/
        │   └── 📄 README.md                 # Metrics (standardized numeric records)
        ├── 📁 reporters/
        │   └── 📄 README.md                 # Reporters (render + package outputs) ← you are here
        └── 📁 docs/
            └── 📄 README.md                 # Drift playbooks, rationales, domain guides
~~~

### Target reporters structure (create if missing)

The repo snapshot does not enumerate this deep subtree; the structure below is the **intended**
KFM v11 layout for reporter implementations. Adjust to match real code when present.

~~~text
📁 tools/
└── 🧠 ai/
    └── 📁 drift/
        └── 📁 reporters/
            ├── 📄 README.md                           # This file
            │
            ├── 📁 schemas/                            # Report schemas + JSON-LD contexts (if local)
            ├── 📁 templates/                          # Markdown templates / partials for consistent output
            ├── 📁 formatters/                         # Pure formatting helpers (no IO)
            ├── 📁 writers/                            # Writers for JSON/MD/JSON-LD/telemetry bundles
            ├── 📁 validators/                         # Output validation and policy-safety checks
            └── 📁 tests/                              # Determinism + shape tests (if repo pattern allows)
~~~

### Where reporter outputs belong (normative)

Reporter outputs MUST NOT be committed under `tools/ai/drift/reporters/`.

Store run outputs under governed run/release locations, e.g.:

~~~text
📁 mcp/
└── 📁 experiments/
    └── 📁 <run-id>/
        ├── 🧾 drift_report.json
        ├── 📄 drift_report.md
        ├── 🧾 drift_telemetry.json
        ├── 🧾 drift_provenance.jsonld
        └── 🧾 checksums.sha256
~~~

Promote certified artifacts into release packages following `releases/<version>/...`.

---

## 🧭 Context

### Why reporters are a separate subsystem

Separating reporting from detection protects stability:

- detectors can evolve internally without changing report consumers,
- CI and governance receive consistent report shapes over time,
- multiple domains can share the same reporting formats.

Reporters are the “contract boundary” between drift computation and decision-making.

### Reporter responsibilities in the KFM pipeline

Reporters sit between:

- **drift computation** (detectors + metrics + aggregation), and
- **governance/operations** (CI gates, dashboards, reviews, releases).

They enable:

- CI-friendly visibility: small summaries + stable links to full artifacts
- reproducible evidence bundles: references, hashes, configs, and provenance
- telemetry ingestion: numeric signals in a stable structure for aggregation

### Relationship to `tools/telemetry/` (recommended)

`tools/telemetry/` exists to aggregate telemetry and metrics.

Drift reporters SHOULD emit drift telemetry in a format that:

- is easy to roll up across runs,
- supports trend charts (windowed over time),
- includes stable scope keys (model_id, dataset_id, cohort_id),
- never includes raw data.

---

## 🗺️ Diagrams

### Drift reporting flow (conceptual)

~~~mermaid
flowchart TD
  A["Baselines<br/>(safe summaries)"] --> D["Detectors + Metrics<br/>(drift signals)"]
  B["Window summaries<br/>(same feature defs)"] --> D
  D --> E["Aggregation<br/>(feature → cohort → model)"]
  E --> R["Reporters<br/>(render + package)"]

  R --> J["🧾 drift_report.json<br/>(canonical machine report)"]
  R --> M["📄 drift_report.md<br/>(human summary)"]
  R --> T["🧾 drift_telemetry.json<br/>(telemetry bundle)"]
  R --> P["🧾 drift_provenance.jsonld<br/>(PROV bundle)"]
~~~

Accessibility note: reporters do not compute metrics; they standardize outputs and attach provenance.

---

## 🧠 Story Node & Focus Mode Integration

### Why reporters matter for narrative systems

For Focus Mode / Story Nodes, drift reporting provides a governed “reliability signal”:

- Has the source mix changed?
- Are citations/evidence proxies stable?
- Did redaction/suppression rates change?
- Are narrative outputs diverging from baseline behavior?

### Recommended “Focus Mode friendly” summary fields

Reporters SHOULD produce a compact summary block suitable for UI display and indexing:

- `overall_status`: `PASS | WARN | FAIL | NOT_COMPARABLE`
- `top_drift_drivers`: small list of feature/category names (no raw values)
- `baseline_ref`, `window_ref`: stable refs + hashes
- `run_id`, `created`, `model_id`, `dataset_id`
- `action_recommended`: `monitor | review | recalibrate | retrain | retire`
- `governance_flags`: e.g., `policy_drift_detected`, `small_group_suppression_applied`

Do NOT emit raw narrative content as part of drift reports.

---

## 🧪 Validation & CI/CD

### Reporter validation gates (normative)

Reporter outputs MUST pass:

- **schema checks** (JSON structure, required keys)
- **reference completeness** (baseline/window/config/code refs present)
- **policy safety checks** (no secrets/PII/protected coordinates)
- **determinism checks** (stable ordering, stable rounding rules, stable timestamps policy)

Recommended output-stability rules:

- stable sort order for lists (metrics, cohorts, drivers)
- explicit numeric rounding policy (recorded in report metadata)
- if timestamps are required, include them, but avoid embedding values that make
  deterministic rebuilds impossible unless the build context requires it (CI may accept).

### CI usage pattern (recommended)

In a drift CI job:

1. run detectors/metrics
2. aggregate
3. run reporters:
   - emit `drift_report.json` + `drift_report.md`
   - emit `drift_telemetry.json`
   - emit `checksums.sha256`
4. validate outputs
5. attach artifacts to CI run and/or store in `mcp/experiments/<run-id>/`

---

## 📦 Data & Metadata

### Canonical report contract (recommended)

The canonical report SHOULD be **reference-first** and include:

- identity
  - `report_id`, `run_id`, `created`
- scope
  - `model_id`, `model_version`, `dataset_id`, `dataset_version`, `cohort_id`
- comparability
  - `comparable: true/false`, `not_comparable_reason`
- baseline and window refs
  - `baseline_ref`, `window_ref` (path + hash or equivalent)
- configuration refs
  - `detector_set_ref`, `metric_set_ref`, `threshold_profile_ref` (each with hash)
- results
  - `status` (PASS/WARN/FAIL/NOT_COMPARABLE)
  - `rollups` (small set of aggregate drift indicators)
  - `top_drivers` (names + metric ids, not raw values)
- governance
  - `care_label`, `sensitivity`, `redaction_required`, `small_group_suppression_applied`
- provenance pointers
  - `commit_sha`, `code_ref`, `provenance_bundle_ref` (if separate)

### Example minimal report (illustrative)

~~~json
{
  "report_id": "drift_report:focus_mode_v3:2025-12-15:<run-id>",
  "run_id": "<run-id>",
  "created": "2025-12-15T00:00:00Z",

  "scope": {
    "model_id": "focus_mode_v3",
    "model_version": "11.2.6",
    "dataset_id": "dcat:kfm:dataset:docs-corpus:v11",
    "dataset_version": "v11",
    "cohort_id": "all"
  },

  "comparability": {
    "comparable": true,
    "not_comparable_reason": null
  },

  "refs": {
    "baseline_ref": "mcp/experiments/<baseline-run-id>/baseline.json#sha256:<sha256>",
    "window_ref": "mcp/experiments/<run-id>/window_summary.json#sha256:<sha256>",
    "threshold_profile_ref": "tools/ai/configs/<profile>#sha256:<sha256>"
  },

  "results": {
    "status": "WARN",
    "rollups": {
      "input_drift_score": 0.12,
      "output_drift_score": 0.05
    },
    "top_drivers": [
      { "metric_id": "distribution.js_divergence", "feature": "embedding_norm" }
    ],
    "action_recommended": "review"
  },

  "governance": {
    "care_label": "Public · Low-Risk",
    "sensitivity": "General",
    "small_group_suppression_applied": true,
    "policy_drift_detected": false
  }
}
~~~

This example is illustrative; enforce a real schema once the project defines it.

---

## 🌐 STAC, DCAT & PROV Alignment

### DCAT (recommended)

Drift reports can be treated as audit artifacts or distributions that reference datasets:

- `dataset_id` should be a DCAT identifier
- drift report can be a `dcat:Distribution` attached to a catalog record for audits
- `mediaType`: `application/json` (or `text/markdown` for the human report)

### STAC (recommended when drift pertains to spatial assets)

If drift relates to STAC-indexed assets (COGs, vectors, tiles):

- reference STAC Item/Asset IDs in scope fields
- avoid embedding spatial extracts
- compute drift from safe summaries (histograms, counts, aggregated metrics)

### PROV-O (recommended)

Represent reporting as:

- `prov:Activity`: “drift reporting”
- `prov:Entity`: report files (`drift_report.json`, etc.)
- `prov:used`: baseline summary, window summary, config entities
- `prov:wasGeneratedBy`: report entity ← activity
- `prov:wasAssociatedWith`: CI runner / pipeline agent

Keep the PROV bundle reference-first; do not duplicate large payloads.

---

## 🧱 Architecture

### Reporter API (recommended)

Reporters SHOULD implement a small, stable interface:

- Inputs:
  - `run_context` (run_id, commit_sha, environment)
  - `scope` (model/dataset/cohort identifiers)
  - `baseline_ref`, `window_ref`
  - `metrics_records` (or reference to them)
  - `rollups` and `status` from aggregation/threshold policy
  - `policy_flags` (suppression applied, redaction mode)

- Outputs:
  - `drift_report.json`
  - `drift_report.md`
  - `drift_telemetry.json`
  - optional: `drift_provenance.jsonld`
  - checksums/manifest

### Reporter profiles (recommended)

Support multiple reporter “profiles” so downstream consumers stay stable:

- `reporter-json-v1` — canonical machine report
- `reporter-md-v1` — CI-friendly human summary
- `reporter-telemetry-v1` — telemetry bundle for aggregation
- `reporter-jsonld-prov-v1` — provenance bundle (PROV-O)

Record the reporter profile in each output.

### Output stability and sorting (normative)

To keep outputs reproducible, reporters MUST:

- use stable sorting for lists (metrics, drivers, cohorts)
- avoid non-deterministic map ordering
- record rounding rules and units where numeric values appear
- avoid embedding environment-specific absolute paths

---

## ⚖ FAIR+CARE & Governance

### Safety requirements (normative)

Drift reporter outputs MUST NOT include:

- raw rows/records from datasets
- raw imagery tiles or sensitive excerpts
- secrets, tokens, credentials
- precise protected cultural site locations
- identifiers that enable re-identification via small groups

Reporters MUST support:

- **small-group suppression** for cohort metrics
- **redaction flags** and “fail closed” behaviors when policy requires

### Governance change control (normative)

Any change to:

- report schema,
- severity interpretation,
- required metadata fields,
- suppression/redaction behavior,

MUST be reviewed under the governance references in the front-matter and version-bumped.

### Training prohibition

All drift reporting artifacts are governance outputs and MUST NOT be used as training data.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v11.2.6** | 2025-12-15 | Created drift reporters README: defined reporter role, canonical output set (JSON/MD/telemetry/PROV), determinism + policy-safety constraints, and reference-first reporting contracts for CI/governance/release packaging. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
🧾 Drift Reporters · Governed for Integrity

[⬅️ Back to Drift Monitoring](../README.md) · [📏 Metrics](../metrics/README.md) · [🧭 Detectors](../detectors/README.md) · [🧱 Baselines](../baselines/README.md) · [📚 Drift Docs](../docs/README.md) · [⚙️ Configs](../../configs/README.md) · [📡 Telemetry](../../telemetry/README.md) · [🧾 Provenance](../../provenance/README.md) · [🛡 Governance](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>