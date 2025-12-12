---
title: "🪟 KFM — SQL Views (RSC Dashboards) (`sql/_views`) (Diamond⁹ Ω / Crown∞Ω)"
path: "docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/sql/_views/README.md"

version: "v11.2.6"
last_updated: "2025-12-12"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"

signature_ref: "../../../../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../../../../releases/v11.2.6/reliability-sustainability-correlation-dashboards-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/reliability-sustainability-correlation-dashboards-v11.2.6.json"
energy_schema: "../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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
  domain: "sql-views"
  applies_to:
    - "docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/sql/_views/**"

fair_category: "F1-A1-I2-R2"
care_label: "FAIR+CARE Governance Aligned"
sensitivity: "Aggregate telemetry projection views; no secrets; no identity-level extraction"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by SQL Views v12"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"

metadata_profiles:
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/sql/_views/README.md@v11.2.4"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "../../../../../../../schemas/json/kfm-markdown-protocol-v11.2.6.schema.json"
shape_schema_ref: "../../../../../../../schemas/shacl/kfm-markdown-protocol-v11.2.6-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:telemetry:rsc:dashboards:queries:sql:views:index:v11.2.6"
semantic_document_id: "kfm-telemetry-rsc-dashboards-queries-sql-views-index-v11.2.6"
event_source_id: "ledger:kfm:doc:telemetry:rsc:dashboards:queries:sql:views:index:v11.2.6"
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

# 🪟 **KFM — SQL Views (`sql/_views`)**
`docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/sql/_views/README.md`

**Purpose**  
Provide optional **engine-specific SQL view definitions** that normalize raw telemetry into a governed, query-friendly shape for the RSC dashboards.  
Views are treated as **projection layers**: they should *standardize columns and units* without changing meaning or introducing non-governed joins.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/SQL-Views-informational" />
<img src="https://img.shields.io/badge/Telemetry-Governed-orange" />
<img src="https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen" />

</div>

---

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 📁 telemetry/
    └── 📁 reliability-sustainability-correlation/
        └── 📁 DASHBOARDS/
            └── 📁 queries/
                └── 📁 sql/
                    ├── 📄 README.md                 — SQL query pack (portable SQL)
                    └── 📁 _views/
                        ├── 📄 README.md            — ← You are here
                        ├── 📄 view_kfm_runs.sql     — Example: base run projection (portable-ish)
                        ├── 📄 pg_views.sql          — Postgres-specific view definitions
                        ├── 📄 duckdb_views.sql      — DuckDB-specific view definitions
                        ├── 📄 bq_views.sql          — BigQuery-specific view definitions
                        └── 📄 ch_views.sql          — ClickHouse-specific view definitions
~~~

Conventions:

- Put one engine’s view set in a single file when possible.
- If a view name is referenced by dashboards, it MUST be listed in the manifests layer.

---

## 📘 Overview

The SQL query pack assumes a table or view with a stable contract (recommended name: `kfm_telemetry_runs`).

However, real telemetry storage differs:

- JSON blobs in a table
- Parquet/JSON files queried via DuckDB
- partitioned tables in a warehouse
- column name drift across pipelines

This folder provides governed views that:

- map raw fields → canonical columns
- enforce units (sec, Wh, gCO2e)
- enforce the minimum schema needed by dashboards

Views MUST NOT:

- de-anonymize or expose identity-level attributes
- join in secrets or sensitive dimensions
- “fix” missing data by inventing values (use `NULL` and document)

---

## 🧭 Context

### 1. Canonical output contract for views

All engine-specific views SHOULD project (at minimum):

- `run_id` (string)
- `workflow` (string)
- `environment` (string)
- `status` (string)
- `started_at` (timestamp)
- `duration_sec` (number)
- `energy_wh` (number)
- `carbon_gco2e` (number)

Optional (only if governance allows and manifests list it):

- `runner_pool` (string)
- `repo` (string)
- `ref` (string)
- `commit_sha` (string)

### 2. Naming rules

- Prefer stable view name: `kfm_telemetry_runs`
- If multiple layers exist:
  - `kfm_telemetry_runs_raw`
  - `kfm_telemetry_runs` (cleaned projection)
  - `kfm_telemetry_runs_daily` (optional rollups; keep rollups in queries when feasible)

---

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  RAW["Raw telemetry storage"] --> VIEW["Governed view projection"]
  VIEW --> SQLQ["SQL query pack"]
  SQLQ --> PAN["Dashboard panels"]
~~~

---

## 🧪 Validation & CI/CD

CI SHOULD validate (where feasible):

- file presence and naming conventions
- referenced view names exist in view files
- governance constraints:
  - no forbidden columns
  - no forbidden joins
  - no SELECT * (prefer explicit projections)

If view definitions are executed as part of tests:

- do so against fixture datasets
- log schema snapshots in `reports/` (not in dashboards)

---

## 📦 Data & Metadata

### 1. Example view pattern (portable baseline)

Use this pattern when your storage is already tabular.

~~~sql
-- view_id: rsc.view.kfm_telemetry_runs
-- outputs: kfm_telemetry_runs (canonical projection)

CREATE OR REPLACE VIEW kfm_telemetry_runs AS
SELECT
  run_id,
  workflow,
  environment,
  status,
  started_at,
  duration_sec,
  energy_wh,
  carbon_gco2e
FROM kfm_telemetry_runs_raw;
~~~

### 2. JSON extraction example (Postgres-ish)

~~~sql
-- view_id: rsc.view.kfm_telemetry_runs.pg_json
-- note: example only; ensure governance-approved keys and types

CREATE OR REPLACE VIEW kfm_telemetry_runs AS
SELECT
  (payload->>'run_id')::text                         AS run_id,
  (payload->>'workflow')::text                       AS workflow,
  (payload->>'environment')::text                    AS environment,
  COALESCE((payload->>'status')::text, 'unknown')    AS status,
  (payload->>'timestamp')::timestamptz               AS started_at,
  NULLIF((payload->>'workflow_duration_sec')::numeric, 0) AS duration_sec,
  (payload->>'energy_wh')::numeric                   AS energy_wh,
  (payload->>'carbon_gco2e')::numeric                AS carbon_gco2e
FROM telemetry_events;
~~~

Governance note:

- If `timestamp` is not `started_at`, rename appropriately and document the mapping.

---

## 🌐 STAC, DCAT & PROV Alignment

- **DCAT**
  - Treat each view file as a `dcat:Distribution` of the SQL Views dataset.
- **PROV-O**
  - The view definition is a `prov:Plan` and the view materialization (if done) is a `prov:Activity`.
- **STAC**
  - Views are non-spatial; if cataloged, represent as STAC Items with `geometry: null`.

---

## ⚖ FAIR+CARE & Governance

This folder exists to keep dashboards safe:

- canonical projections reduce accidental exposure
- explicit projections prevent “extra columns” from creeping into panels
- engine-specific differences stay documented and reviewable

If you need to add a new column:

1. Add it to the governance controls (approved dimension list).
2. Add it to the metric dictionary (if it’s a metric) or to the dimension registry (if you maintain one).
3. Update views and document why.
4. Update any dashboards/panels that rely on it.
5. Record in Version History.

---

## 🕰️ Version History

| Version | Date       | Author           | Summary                                                                 |
|--------:|------------|------------------|-------------------------------------------------------------------------|
| v11.2.6 | 2025-12-12 | `@kfm-telemetry` | Introduced governed SQL views layer for engine-specific normalization. |
| v11.2.4 | 2025-12-06 | `@kfm-telemetry` | Baseline (superseded by v11.2.6 view governance and conventions).      |

---

<div align="center">

🪟 **KFM — SQL Views (`sql/_views`) (v11.2.6)**  
Engine-Specific Projections · Canonical Columns · Governance-First Telemetry

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Aligned-gold" />
<img src="https://img.shields.io/badge/SQL-Views-informational" />

[⬅ SQL Query Pack](../README.md) ·
[🧾 Query Manifests](../../manifests/README.md) ·
[📊 Dashboards Index](../../../README.md) ·
[🖼 Dashboard Screenshots](../../../screenshots/README.md) ·
[🚨 Alerts](../../../../ALERTS/README.md) ·
[🧭 Correlation Module](../../../../README.md) ·
[🧾 Telemetry Index](../../../../../README.md) ·
[⚙ Workflows Index](../../../../../workflows/README.md) ·
[📘 Markdown Protocol](../../../../../standards/kfm_markdown_protocol_v11.2.6.md) ·
[⚖ Governance Charter](../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω

</div>

