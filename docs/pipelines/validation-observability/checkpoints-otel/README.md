---
title: "📊 KFM v11.2 — GE Checkpoints + OpenTelemetry Metrics Integration (Diamond⁹ Ω / Crown∞Ω)"
path: "docs/pipelines/validation-observability/checkpoints-otel/README.md"
version: "v11.2.0"
last_updated: "2025-11-27"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability Engineering · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.0/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.0/validation-observability-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/validation-observability-v11.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

status: "Active · Enforced"
doc_kind: "Pipeline Module"
intent: "validation-observability-checkpoints-otel"
semantic_document_id: "kfm-doc-validation-observability-checkpoints-otel"
doc_uuid: "urn:kfm:pipeline:validation-observability:checkpoints-otel:v11.2.0"
role: "validation-observability-spec"

classification: "Internal Pipeline Specification"
sensitivity: "Low"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false

fair_category: "F1-A1-I2-R2"
care_label: "Responsible · Ethics · Stewardship"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "PROV-O"
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "FAIR+CARE"

provenance_chain:
  - "docs/pipelines/validation-observability/checkpoints-otel/README.md@v11.0.2"
  - "docs/pipelines/validation-observability/checkpoints-otel/README.md@v11.0.1"
  - "docs/pipelines/validation-observability/checkpoints-otel/README.md@v11.0.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: false

json_schema_ref: "../../../../schemas/json/validation-observability-checkpoints-otel-v11.schema.json"
shape_schema_ref: "../../../../schemas/shacl/validation-observability-checkpoints-otel-v11-shape.ttl"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "speculative-additions"
  - "content-alteration"
  - "governance-override"
  - "narrative-fabrication"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded by next validation/observability redesign"
---

<div align="center">

# 📊 **KFM v11.2 — GE Checkpoints + OpenTelemetry Metrics Integration**  
`docs/pipelines/validation-observability/checkpoints-otel/README.md`

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP--DL_v6.3-informational)]()
[![Markdown · KFM-MDP v11.2.2](https://img.shields.io/badge/Markdown-KFM--MDP_v11.2.2-blue)]()
[![Great Expectations](https://img.shields.io/badge/Validation-Great_Expectations-ff9800)]()
[![OpenTelemetry](https://img.shields.io/badge/Telemetry-OTel_v1.x-9c27b0)]()
[![FAIR+CARE](https://img.shields.io/badge/Governance-FAIR%2BCARE-gold)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green)]()

**Purpose**  
Provide the authoritative specification for integrating **Great Expectations (GE)** and **OpenTelemetry (OTel)** into all KFM v11 data pipelines — enforcing deterministic validation, governed metric emissions, lineage logging, FAIR+CARE observability, sustainability telemetry, and CI-driven promotion gating.

</div>

---

## 📘 1. Overview

This module defines how **GE Checkpoints** and **OTel metrics** wrap every **data-mutating operation** within:

- ETL pipelines  
- AI/ML inference runs  
- Harmonization flows  
- Story Node & Focus Mode generation pipelines  
- Conditional ingestion flows  
- Reliable Pipelines v11 DAGs  

The integration provides:

- Deterministic validation  
- Governance-aligned enforcement  
- Real-time metric emission  
- SLO/SLA + error-budget alignment  
- Promotion gating  
- Audit-ready provenance  
- FAIR+CARE compliance signals  
- Sustainability telemetry (energy & carbon)  

---

## 🗂️ 2. Directory Layout (v11.2 · Immediate + One Branch)

```text
📁 docs/pipelines/validation-observability/checkpoints-otel/    — GE + OTel integration spec root
│   📂 examples/                                                — Example checkpoints, runners, CI dry-run docs
│   📂 suites/                                                  — GE expectation suites (per domain)
│   📂 checkpoints/                                             — GE checkpoint YAML definitions
│   📂 runners/                                                 — Python/Ops runners for checkpoints + metrics
│   📄 README.md                                                — This governed module specification
```

Deeper structures (individual suite files, checkpoint YAMLs, etc.) are documented within the respective subdirectories or dataset-specific docs.

---

## 🎯 3. Goals

This subsystem ensures:

- 🔒 **Governed validation** before any data persists  
- 📈 **Uniform metrics** for reliability dashboards and SLOs  
- 🚦 **Promotion gating** based on validation + error budgets  
- 🧪 **Consistent test harness** for all data pipelines  
- 📜 **Complete lineage logs** suitable for audits and replay  
- 🛡 **FAIR+CARE and sovereignty compliance**, enforced via validation  
- ♻ **Sustainability metrics** (energy/carbon) visible to governance bodies  

---

## 🧩 4. GE Checkpoint Contract (v11 Standard)

All GE Checkpoints MUST:

- Use `StoreValidationResultAction`  
- Use `UpdateDataDocsAction` (optional for REST-only deployments, but recommended)  
- Reference an expectation suite under `/suites/`  
- Use naming format:

  ```text
  kfm_<stage>_ckpt.yml
  ```

- Output deterministic, machine-parseable validation results  
- Emit both **row-level** and **table-level** stats where appropriate  
- Produce an error summary JSON to:

  ```text
  data/work/validation/<pipeline>/<timestamp>.json
  ```

### 4.1 Required Expectation Types

- Schema consistency (column presence, types)  
- Null checks (must/must-not be null)  
- Range checks (min/max values within specified limits)  
- Unique keys where expected (primary keys, compound keys)  
- Temporal continuity (no gaps where continuity is required)  
- CRS & spatial metadata presence (for geospatial outputs)  
- Data Contract conformance (field-level constraints, enumerations)  

### 4.2 Optional Domain-Specific Checks

- Climate anomaly distributions (e.g. Z-score thresholds)  
- Hydrology hydrograph continuity (e.g. monotonic series segments)  
- Story Node JSON schema validation  
- Hazard quantile validation (e.g. 95th/99th percentile bounds)  

---

## 📦 5. OTel Metrics Contract (v11)

Pipelines that use this module MUST emit OTel metrics at validation boundaries.

### 5.1 Required Metrics

| Metric Name               | Type      | Description                           |
|--------------------------|-----------|---------------------------------------|
| `kfm.update_errors`      | Counter   | Failed expectations count             |
| `kfm.rows_ingested`      | Counter   | Number of rows successfully committed |
| `kfm.latency_ms`         | Histogram | Pipeline or validation stage latency  |
| `kfm.validation_failures`| Counter   | Aggregated checkpoint failures        |
| `kfm.error_budget_burn`  | Gauge     | SLO error-budget consumption          |

### 5.2 Required Labels

- `pipeline` — pipeline identifier (e.g. `climate_ingest`)  
- `stage` — stage identifier (`fetch`, `transform`, `validate`, `publish`)  
- `table` — logical table name / entity name  
- `env` — environment (`dev`, `stage`, `prod`)  
- `dataset_id` — optional but recommended; aligns with STAC/DCAT IDs  
- `contract_version` — semantic or hash version of Data Contract  

### 5.3 Example Metric

```text
kfm.update_errors{
  pipeline="climate_ingest",
  stage="validate",
  table="climate_raw",
  env="prod",
  contract_version="v11.2.0"
} = 3
```

---

## 🐍 6. Python Runner Standard (v11.2)

Runners in `runners/` MUST:

1. Load the configured GE checkpoint.  
2. Execute deterministically (no hidden non-deterministic operations).  
3. Parse checkpoint results into:
   - pass/fail status  
   - validation statistics  
   - suite identifiers and versions  
4. Emit OTel metrics (using the contract above).  
5. Optionally emit OpenLineage/PROV-O provenance for validation activities.  
6. Write a normalized results JSON to:

   ```text
   data/work/validation/<pipeline>/<timestamp>.json
   ```

7. Exit with status `0` on full success, `1` on any enforced failure.  
8. Emit energy/carbon telemetry if the instrumentation layer is active.

**Critical rule:**  
Runners MUST NOT mutate data **before** validation has run and passed; mutations should occur only in controlled pipeline stages after successful validation.

---

## 🧠 7. Integration with Reliable Pipelines v11

This integration is expected to be called from:

- LangGraph-based ingestion pipelines  
- Airflow controllers  
- LangGraph + lakeFS workflows (branch-based promotion)  

Checkpoints and metrics drive:

- **Retry logic** (e.g. retry on transient failures)  
- **Rollback triggers** (for branch-based merging)  
- **Hotfix gates** (promotion blocks until validation passes)  
- **Freeze/unfreeze state** (e.g. freeze promotion when error budgets are exceeded)  
- **Promotion eligibility** (only validated runs can advance)  
- **Autonomous update rules** for `kfm-auto-update` and similar workflows  
- **Kill-switch enforcement** when repeated failures occur  

On checkpoint failure:

- Pipelines auto-halt  
- OTel metric `kfm.update_errors` increments  
- `kfm.error_budget_burn` is updated  
- Governance ledger receives a structured event  
- Optional on-call alert (Slack/Teams/email/PagerDuty) is emitted  

---

## 📊 8. Dashboards & Observability

Dashboards consuming this module SHOULD track:

- SLO latency (`p50`, `p95`, `p99`) per pipeline/stage  
- Checkpoint success/failure time series  
- Drift detection flags (if any)  
- Row volume changes per run  
- Data Contract compliance percentage  
- Governance flag violations  
- Carbon/energy footprints of validation runs  

Dashboard specs align with:

```text
docs/pipelines/reliability/slo-error-budgets.md
```

and the telemetry schema referenced in `telemetry_schema`.

---

## 🔒 9. Governance, FAIR+CARE, & Sovereignty

Validation and OTel metric outputs are used in:

- CARE compliance reviews  
- Sovereignty redaction & masking checks  
- Sensitive-site spatial tests (e.g. H3 R7–R9)  
- License and usage validation checks  
- FAIR+CARE quarterly accountability reports  

Checkpoint failures:

- MUST be logged in the Governance Ledger, e.g.:

  ```text
  docs/reports/audit/governance-ledger.json
  ```

- SHOULD be referenced by incident/issue management systems when they block promotion.  

---

## 🧪 10. Testing & CI/CD Enforcement

CI/CD workflows MUST enforce:

- GE suite syntax validation  
- Checkpoint YAML validation (against schema)  
- Metric schema dry-runs (OTel metrics)  
- JSON Schema validation for:

  - Validation results JSON  
  - GE suite definitions  
  - Checkpoint configuration files  

Promotion is **blocked** if:

- Any enforced checkpoint has failures  
- Metric emission is missing or malformed  
- Validation payloads fail `validation-observability-v11.json`  
- Lineage information is incomplete (where required)  
- Runner behavior is non-deterministic or not idempotent across identical inputs  

---

## 🕰️ 11. Version History

| Version  | Date       | Summary                                                                                                        |
|---------:|------------|----------------------------------------------------------------------------------------------------------------|
| v11.2.0  | 2025-11-27 | Upgraded to KFM-MDP v11.2.2; added layout standard, telemetry schemas, FAIR+CARE hooks, and clarified CI gating. |
| v11.0.2  | 2025-11-24 | Enriched v11 edition; added error-budget ties, sustainability metrics, sovereignty filters.                    |
| v11.0.1  | 2025-11-23 | Added GE suite directory structure and OTel label requirements.                                                |
| v11.0.0  | 2025-11-23 | Initial module specification.                                                                                  |

---

<div align="center">

**Kansas Frontier Matrix — Validation & Observability**  
*“Validation is governance. Metrics are accountability.”*  

[⬅ Back to Validation & Observability Index](../README.md) ·  
[🏗 Repository Architecture](../../../ARCHITECTURE.md) ·  
[⚖ Governance Standards](../../../standards/README.md)

</div>
