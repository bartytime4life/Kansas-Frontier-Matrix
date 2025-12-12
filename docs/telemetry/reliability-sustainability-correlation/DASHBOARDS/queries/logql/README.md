---
title: "📜 KFM — LogQL Query Pack (Reliability × Sustainability Dashboards) (Diamond⁹ Ω / Crown∞Ω)"
path: "docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/logql/README.md"

version: "v11.2.6"
last_updated: "2025-12-12"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"

signature_ref: "../../../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../../../releases/v11.2.6/reliability-sustainability-correlation-dashboards-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/reliability-sustainability-correlation-dashboards-v11.2.6.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

status: "Active / Enforced"
doc_kind: "Standard Index"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "logql-queries"
  applies_to:
    - "docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/logql/**"
    - "releases/**/focus-telemetry*.json"
    - "releases/**/*telemetry*.json"
    - "otel/**"
    - "loki/**"

fair_category: "F1-A1-I2-R2"
care_label: "FAIR+CARE Governance Aligned"
sensitivity: "LogQL filters over aggregated CI/telemetry logs; excludes secrets and identifiers by default"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by LogQL Query Pack v12"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"

metadata_profiles:
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/logql/README.md@v11.2.4"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "../../../../../../schemas/json/kfm-markdown-protocol-v11.2.6.schema.json"
shape_schema_ref: "../../../../../../schemas/shacl/kfm-markdown-protocol-v11.2.6-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:telemetry:rsc:dashboards:queries:logql:index:v11.2.6"
semantic_document_id: "kfm-telemetry-rsc-dashboards-queries-logql-index-v11.2.6"
event_source_id: "ledger:kfm:doc:telemetry:rsc:dashboards:queries:logql:index:v11.2.6"
doc_integrity_checksum: "<sha256>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "a11y-adaptations"
  - "semantic-highlighting"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "narrative-fabrication"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧭 Context"
    - "🗺️ Diagrams"
    - "🧠 Story Node & Focus Mode Integration"
    - "🧪 Validation & CI/CD"
    - "📦 Data & Metadata"
    - "🌐 STAC, DCAT & PROV Alignment"
    - "🧱 Architecture"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "metadata-check"
  - "accessibility-check"
  - "provenance-check"
  - "footer-check"

ci_integration:
  workflow: ".github/workflows/docs-lint.yml"
  environment: "dev → staging → production"

branding_registry:
  telemetry: "Transparent Systems · Ethical Metrics · Sustainable Intelligence"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true
---

<div align="center">

# 📜 **KFM — LogQL Query Pack**
`docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/logql/README.md`

**Purpose**  
Governed **LogQL query pack** for Loki-backed dashboards, enabling correlation views between
**reliability signals** (errors, failures, retries) and **sustainability signals** (energy, carbon) emitted by KFM telemetry.

<img src="https://img.shields.io/badge/LogQL-Loki-informational" />
<img src="https://img.shields.io/badge/Dashboards-Reliability_%C3%97_Sustainability-orange" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen" />

</div>

---

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 📁 telemetry/
    └── 📁 reliability-sustainability-correlation/
        ├── 📁 ALERTS/
        │   └── 📄 README.md
        │
        └── 📁 DASHBOARDS/
            ├── 📄 README.md
            │
            ├── 📁 screenshots/
            │   └── 📄 README.md
            │
            └── 📁 queries/
                ├── 📄 README.md
                │
                ├── 📁 promql/
                │   └── 📄 README.md
                │
                ├── 📁 jq/
                │   └── 📄 README.md
                │
                └── 📁 logql/
                    ├── 📄 README.md
                    │
                    ├── 📄 workflow_failures_by_workflow.logql
                    ├── 📄 workflow_retries_by_workflow.logql
                    ├── 📄 energy_wh_per_success_by_workflow.logql
                    ├── 📄 carbon_gco2e_per_success_by_workflow.logql
                    ├── 📄 duration_p95_by_workflow.logql
                    └── 📄 correlation_energy_vs_failures_by_workflow.logql
~~~

Notes:

- Treat `*.logql` files as **panel-ready** query snippets.
- Keep file names explicit and unit-honest (e.g., `energy_wh_*`, `carbon_gco2e_*`).

---

## 📘 Overview

This folder contains LogQL queries used when telemetry is available as **logs in Loki** (directly, or via OTEL → Loki).

LogQL is best when you need to:

- query **structured JSON log events**
- compute rollups directly from log streams
- build dashboards without a full Prometheus metric pipeline

If you already expose metrics in Prometheus, prefer:

- `../promql/README.md`

If you need JSON export/rollups from artifacts, prefer:

- `../jq/README.md`

---

## 🧭 Context

### 1. What these queries assume

These queries assume telemetry events are stored as structured JSON logs with fields similar to:

- `workflow`
- `run_id`
- `status` (e.g., `success`, `failure`, `cancelled`)
- `workflow_duration_sec`
- `energy_wh`
- `carbon_gco2e`
- `timestamp` (ISO-8601)

They also assume Loki labels exist for scoping, such as:

- `{app="kfm-ci"}` or `{service="telemetry"}`

Your deployment may differ; update label selectors first, then keep the JSON field logic stable.

### 2. Unit discipline

- `energy_wh` stays in Wh unless explicitly converted.
- `carbon_gco2e` stays in gCO2e unless explicitly converted.
- Avoid mixing kWh and Wh or gCO2e and kgCO2e within a single panel without conversion.

---

## 🧪 Validation & CI/CD

Recommended validation approach:

- Maintain a tiny replayable log fixture (JSON lines) and test queries via `logcli`.
- Ensure every query:
  - parses JSON safely (`| json`)
  - guards missing fields (filter before `unwrap`)
  - uses a bounded range selector (`[5m]`, `[1h]`, `[24h]`)

Example CI smoke step (conceptual):

~~~bash
# Example only: adjust Loki address, auth, and label selectors.
logcli query '{app="kfm-ci"} | json | workflow != ""' --since=1h --limit=10
~~~

---

## 📦 Data & Metadata

### 1. JSON log event shape (recommended)

Prefer emitting telemetry logs as JSON where numeric fields are real numbers:

~~~json
{
  "workflow": "docs-lint",
  "run_id": "docs-lint_2025-12-11T17:31:32Z",
  "status": "success",
  "workflow_duration_sec": 92,
  "energy_wh": 2.3,
  "carbon_gco2e": 0.0009,
  "timestamp": "2025-12-11T17:31:32Z"
}
~~~

### 2. Core query patterns

#### A) Failures by workflow

~~~logql
sum by (workflow) (
  count_over_time(
    {app="kfm-ci"} | json | workflow != "" | status = "failure" [1h]
  )
)
~~~

#### B) Retries by workflow (if `attempt` is logged)

~~~logql
sum by (workflow) (
  count_over_time(
    {app="kfm-ci"} | json | workflow != "" | attempt != 1 [24h]
  )
)
~~~

#### C) Average energy per successful run by workflow

~~~logql
(
  sum by (workflow) (
    sum_over_time(
      {app="kfm-ci"} | json | status = "success" | unwrap energy_wh [24h]
    )
  )
)
/
(
  sum by (workflow) (
    count_over_time(
      {app="kfm-ci"} | json | status = "success" [24h]
    )
  )
)
~~~

#### D) Average carbon per successful run by workflow

~~~logql
(
  sum by (workflow) (
    sum_over_time(
      {app="kfm-ci"} | json | status = "success" | unwrap carbon_gco2e [24h]
    )
  )
)
/
(
  sum by (workflow) (
    count_over_time(
      {app="kfm-ci"} | json | status = "success" [24h]
    )
  )
)
~~~

#### E) p95 duration by workflow (requires `unwrap`)

Different Loki builds support different quantile behaviors. Start with:

~~~logql
quantile_over_time(
  0.95,
  {app="kfm-ci"} | json | workflow != "" | unwrap workflow_duration_sec [24h]
)
~~~

If you need per-workflow separation, ensure `workflow` is a Loki label (preferred), or
emit workflow as a label via your ingestion pipeline.

#### F) Correlation-style proxy: energy per failure (daily)

~~~logql
(
  sum by (workflow) (
    sum_over_time(
      {app="kfm-ci"} | json | unwrap energy_wh [24h]
    )
  )
)
/
(
  sum by (workflow) (
    count_over_time(
      {app="kfm-ci"} | json | status = "failure" [24h]
    )
  )
)
~~~

Interpretation rule:

- This is not “causality”.
- It is a dashboard-friendly derived indicator that can flag regressions.

---

## 🌐 STAC, DCAT & PROV Alignment

- LogQL queries are governed “plans” that generate derived dashboard views.
- Derived time-window exports (if you store them) can be registered as:
  - DCAT Distributions (JSON/CSV)
  - PROV Entities generated by a dashboard build Activity

---

## ⚖ FAIR+CARE & Governance

- Default queries MUST remain aggregate-first.
- Do not emit high-cardinality identifiers into dashboards unless governance explicitly allows it.
- Do not join or expose:
  - secrets
  - tokens
  - private repository URLs
  - restricted or sovereignty-controlled attributes

If a panel must surface a “top offenders” list:

- keep it scoped to workflow names, not individuals.

---

## 🕰️ Version History

| Version | Date       | Author           | Summary                                                           |
|--------:|------------|------------------|-------------------------------------------------------------------|
| v11.2.6 | 2025-12-12 | `@kfm-telemetry` | LogQL query pack index created/updated for Loki-backed dashboards. |
| v11.2.4 | 2025-12-06 | `@kfm-telemetry` | Prior baseline (superseded by v11.2.6).                           |

---

<div align="center">

📜 **KFM — LogQL Query Pack (v11.2.6)**  
Loki-Backed Panels · JSON-Safe Queries · Unit-Disciplined Rollups

<img src="https://img.shields.io/badge/Loki-LogQL-informational" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Aligned-gold" />

[⬅ Query Library](../README.md) ·
[🧾 Query Catalog](../manifests/queries.catalog.json) ·
[📘 Metric Dictionary](../manifests/metrics.dictionary.json) ·
[🧩 PromQL Pack](../promql/README.md) ·
[🧰 jq Pack](../jq/README.md) ·
[🖼 Dashboard Screenshots](../../screenshots/README.md) ·
[📊 Dashboards Index](../../README.md) ·
[🚨 Alerts](../../../ALERTS/README.md) ·
[🧭 Correlation Module](../../../README.md) ·
[🧾 Telemetry Index](../../../../README.md) ·
[⚙ Workflows Index](../../../../../workflows/README.md) ·
[📘 Markdown Protocol](../../../../../standards/kfm_markdown_protocol_v11.2.6.md) ·
[⚖ Governance Charter](../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω

</div>

