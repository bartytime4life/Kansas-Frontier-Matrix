---
title: "🗃️ KFM — SQL Query Pack (Reliability × Sustainability Correlation Dashboards) (Diamond⁹ Ω / Crown∞Ω)"
path: "docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/sql/README.md"

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
diagram_profiles:
  - "mermaid-flowchart-v1"

scope:
  domain: "sql-query-pack"
  applies_to:
    - "docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/sql/**"
    - "docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/manifests/**"

fair_category: "F1-A1-I2-R2"
care_label: "FAIR+CARE Governance Aligned"
sensitivity: "Aggregate telemetry queries; no secrets; no identity-level extraction"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by SQL Query Pack v12"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"

metadata_profiles:
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/sql/README.md@v11.2.4"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "../../../../../../schemas/json/kfm-markdown-protocol-v11.2.6.schema.json"
shape_schema_ref: "../../../../../../schemas/shacl/kfm-markdown-protocol-v11.2.6-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:telemetry:rsc:dashboards:queries:sql:index:v11.2.6"
semantic_document_id: "kfm-telemetry-rsc-dashboards-queries-sql-index-v11.2.6"
event_source_id: "ledger:kfm:doc:telemetry:rsc:dashboards:queries:sql:index:v11.2.6"
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
  - "schema-lint"
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

# 🗃️ **KFM — SQL Query Pack**
`docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/sql/README.md`

**Purpose**  
Provide a governed **SQL query library** used to compute **Reliability × Sustainability** correlation views from telemetry stored in relational or analytical engines (e.g., Postgres, DuckDB, BigQuery, ClickHouse).  
This pack is **manifest-driven**, **unit-disciplined**, and **aggregate-first**, so dashboards remain reproducible and audit-ready.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Queries-SQL-informational" />
<img src="https://img.shields.io/badge/Telemetry-Governed-orange" />
<img src="https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen" />

</div>

---

## 📘 Overview

SQL queries are used when telemetry is materialized into tables (or views) for:

- long-range correlation (weeks/months)
- joins between run outcomes and sustainability fields
- denormalized reporting (dashboards, exports, governance audits)

This folder is **not** a dumping ground of ad-hoc SQL. It is a governed pack where:

- each query has a stable **query_id**
- each query is referenced by the manifest layer
- each query declares its output metrics and units (via the metric dictionary)

---

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 📁 telemetry/
    └── 📁 reliability-sustainability-correlation/
        └── 📁 DASHBOARDS/
            └── 📁 queries/
                ├── 📁 manifests/
                │   ├── 📄 README.md
                │   ├── 📄 queries.catalog.json
                │   ├── 📄 metrics.dictionary.json
                │   ├── 📄 panels.manifest.json
                │   ├── 📄 datasources.manifest.json
                │   └── 📄 governance.controls.json
                │
                ├── 📁 promql/
                │   └── 📄 README.md
                │
                ├── 📁 logql/
                │   └── 📄 README.md
                │
                ├── 📁 jq/
                │   └── 📄 README.md
                │
                └── 📁 sql/
                    ├── 📄 README.md                          — ← You are here
                    ├── 📄 rsc_workflow_energy_by_day.sql      — Example: energy + failures per day
                    ├── 📄 rsc_failures_vs_carbon.sql          — Example: failure rate vs carbon intensity
                    ├── 📄 rsc_duration_p95_vs_energy.sql      — Example: latency–energy coupling
                    └── 📄 _views/README.md                    — Optional: view definitions (engine-specific)
~~~

Notes:

- Query files SHOULD be named by intent (`rsc_<topic>_<grain>.sql`).
- If engine-specific syntax is required, isolate it under `sql/_views/` and document the engine.

---

## 🧭 Context

### 1. What “SQL” means here

This pack targets any environment where KFM telemetry is queryable via SQL:

- local analysis: DuckDB over JSON/Parquet
- warehouse: BigQuery/Snowflake/Redshift
- OLAP: ClickHouse
- service DB: Postgres

The pack remains governed by:

- `manifests/queries.catalog.json` (discoverability + IDs)
- `manifests/metrics.dictionary.json` (units + semantics)
- `manifests/governance.controls.json` (allowed group-bys, exposure, aggregation)

### 2. Reliability × Sustainability correlation

Typical joins and groupings include:

- workflow run outcomes (success/failure, duration)
- energy (Wh)
- carbon (gCO2e)
- environment (dev/staging/prod)
- runner pool label (if defined and governance-approved)

---

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  SQLQ["SQL queries"] --> CAT["Query catalog"]
  CAT --> PAN["Panel mapping"]
  PAN --> DBS["Dashboards"]
  CAT --> MET["Metric dictionary"]
  MET --> DBS
  GOV["Governance controls"] --> CAT
  GOV --> DBS
~~~

---

## 🧠 Story Node & Focus Mode Integration

SQL-backed dashboard views can be summarized as Story Nodes, for example:

- `urn:kfm:story-node:telemetry:rsc:sql-pack:v11.2.6`
- `urn:kfm:story-node:telemetry:rsc:panel:<dashboard_id>:<panel_id>`

Focus Mode MAY:

- summarize what a query measures (from `queries.catalog.json`)
- show how the metric’s unit and meaning are defined (from `metrics.dictionary.json`)
- link to the query source path

Focus Mode MUST NOT:

- expose identity-level fields
- infer root-cause from correlation alone
- modify or “correct” query definitions

---

## 🧪 Validation & CI/CD

### 1. Quality gates (normative)

CI MUST fail if:

- a SQL query is referenced in manifests but missing on disk
- query IDs are duplicated or reused after deprecation
- a query output metric is not in the metric dictionary
- a query violates governance rules (e.g., disallowed group-by or exposure mode)

### 2. Lint expectations (pragmatic)

This pack SHOULD maintain:

- one query per file
- consistent parameter naming
- a short header comment at top of each `.sql` file:
  - query_id
  - grain (hour/day/week)
  - required parameters
  - outputs

Example header pattern:

~~~sql
-- query_id: rsc.duration_p95_vs_energy.day
-- grain: day
-- params: :start_ts, :end_ts, :env
-- outputs: ci.duration.p95.sec, ci.energy.wh
~~~

---

## 📦 Data & Metadata

### 1. Recommended table contract (conceptual)

SQL engines differ; this is a conceptual shape that queries assume.

Minimal columns (recommended):

- `run_id` (string; may be excluded from outputs)
- `workflow` (string)
- `environment` (string)
- `status` (string: success/failure/cancelled)
- `started_at` (timestamp)
- `duration_sec` (number)
- `energy_wh` (number)
- `carbon_gco2e` (number)

If you store telemetry as JSON:

- create a governed view that projects these columns
- document that view under `sql/_views/`

### 2. Example queries

#### A) Failures vs energy by day

~~~sql
-- query_id: rsc.failures_vs_energy.day
-- grain: day
-- params: :start_ts, :end_ts, :env
-- outputs: ci.failures.count, ci.energy.wh

SELECT
  DATE_TRUNC('day', started_at)                 AS day,
  workflow                                      AS workflow,
  COUNT(*) FILTER (WHERE status <> 'success')   AS failures_count,
  SUM(energy_wh)                                AS energy_wh
FROM kfm_telemetry_runs
WHERE started_at >= :start_ts
  AND started_at <  :end_ts
  AND environment = :env
GROUP BY 1, 2
ORDER BY 1, 2;
~~~

#### B) Duration p95 vs energy by day

~~~sql
-- query_id: rsc.duration_p95_vs_energy.day
-- grain: day
-- params: :start_ts, :end_ts, :env
-- outputs: ci.duration.p95.sec, ci.energy.wh

SELECT
  DATE_TRUNC('day', started_at) AS day,
  workflow                      AS workflow,
  PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY duration_sec) AS duration_p95_sec,
  SUM(energy_wh)                AS energy_wh
FROM kfm_telemetry_runs
WHERE started_at >= :start_ts
  AND started_at <  :end_ts
  AND environment = :env
GROUP BY 1, 2
ORDER BY 1, 2;
~~~

### 3. Manifest entry (required)

Every SQL query MUST be registered in the catalog.

~~~json
{
  "query_id": "rsc.duration_p95_vs_energy.day",
  "engine": "sql",
  "source_path": "../sql/rsc_duration_p95_vs_energy.sql",
  "description": "Daily p95 duration alongside energy consumption by workflow.",
  "outputs": [
    { "metric_id": "ci.duration.p95.sec", "unit": "sec" },
    { "metric_id": "ci.energy.wh", "unit": "Wh" }
  ],
  "tags": ["reliability", "sustainability", "correlation", "aggregation"],
  "governance": { "aggregation": "required", "exposure": "public" }
}
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

- **DCAT**
  - Treat this SQL pack as a `dcat:Dataset` whose distributions are:
    - each `.sql` file (`text/plain`)
    - the query catalog (`application/json`)
- **PROV-O**
  - Each executed query run can be modeled as a `prov:Activity` that:
    - `prov:used` the telemetry table/view snapshot (entity)
    - `prov:generated` a dashboard panel dataset (entity)
- **STAC**
  - SQL outputs are typically non-spatial; when cataloged as STAC Items:
    - `geometry: null`
    - include `properties.datetime` for the computed window
    - attach outputs as STAC assets (CSV/JSON)

---

## 🧱 Architecture

- Manifests are the **control plane**.
- SQL files are the **execution plane**.
- Dashboard panels should bind to **query_id**, not raw SQL strings, whenever the dashboard platform allows it.

If direct SQL embedding is required by tooling:

- embed the query text, but keep:
  - the authoritative source in this repo
  - the query_id in the panel description/metadata
  - a CI check to ensure embedded SQL matches the repo version (hash-based)

---

## ⚖ FAIR+CARE & Governance

This pack is governed to avoid harmful telemetry exposure:

- Aggregate-first queries only.
- No secrets, tokens, identities, or sensitive attributes.
- Group-bys restricted to governance-approved dimensions (see `governance.controls.json`).
- Correlation is not causation:
  - dashboards and narrative summaries must avoid definitive causal claims without supporting evidence.

---

## 🕰️ Version History

| Version | Date       | Author           | Summary                                                                 |
|--------:|------------|------------------|-------------------------------------------------------------------------|
| v11.2.6 | 2025-12-12 | `@kfm-telemetry` | Established governed SQL query pack structure and manifest integration. |
| v11.2.4 | 2025-12-06 | `@kfm-telemetry` | Baseline (superseded by v11.2.6 SQL pack discipline and rules).         |

---

<div align="center">

🗃️ **KFM — SQL Query Pack (v11.2.6)**  
Warehouse-Ready Correlation · Manifest-Driven Dashboards · Governance-First Telemetry

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Aligned-gold" />
<img src="https://img.shields.io/badge/SQL-Governed-informational" />

[⬅ Query Library](../README.md) ·
[🧾 Query Manifests](../manifests/README.md) ·
[🧩 PromQL Pack](../promql/README.md) ·
[📜 LogQL Pack](../logql/README.md) ·
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

