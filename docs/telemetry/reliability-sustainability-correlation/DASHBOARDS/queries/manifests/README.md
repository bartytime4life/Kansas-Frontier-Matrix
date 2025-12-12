---
title: "🧾 KFM — Query Manifests (Reliability × Sustainability Correlation Dashboards) (Diamond⁹ Ω / Crown∞Ω)"
path: "docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/manifests/README.md"

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
  domain: "query-manifests"
  applies_to:
    - "docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/manifests/**"
    - "docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/promql/**"
    - "docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/logql/**"
    - "docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/jq/**"

fair_category: "F1-A1-I2-R2"
care_label: "FAIR+CARE Governance Aligned"
sensitivity: "Dashboard metadata only; no secrets, no identities; aggregate-first"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by Query Manifests v12"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"

metadata_profiles:
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/manifests/README.md@v11.2.4"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "../../../../../../schemas/json/kfm-markdown-protocol-v11.2.6.schema.json"
shape_schema_ref: "../../../../../../schemas/shacl/kfm-markdown-protocol-v11.2.6-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:telemetry:rsc:dashboards:queries:manifests:index:v11.2.6"
semantic_document_id: "kfm-telemetry-rsc-dashboards-queries-manifests-index-v11.2.6"
event_source_id: "ledger:kfm:doc:telemetry:rsc:dashboards:queries:manifests:index:v11.2.6"
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

# 🧾 **KFM — Query Manifests**
`docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/manifests/README.md`

**Purpose**  
Define the **manifest layer** that makes dashboard queries **discoverable, auditable, and governed**.  
Manifests describe **what each query is**, **where it lives**, **what metrics/units it produces**, and **how it is allowed to appear** in Reliability × Sustainability correlation dashboards.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Telemetry-Governed-orange" />
<img src="https://img.shields.io/badge/Dashboards-Correlation-informational" />
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
                ├── 📁 manifests/
                │   ├── 📄 README.md                       — ← You are here
                │   ├── 📄 queries.catalog.json             — Canonical catalog of all query IDs
                │   ├── 📄 metrics.dictionary.json          — Units, semantics, ranges, display names
                │   ├── 📄 panels.manifest.json             — Panel → query mapping (optional but recommended)
                │   ├── 📄 datasources.manifest.json        — Prom/Loki/source refs (env-safe, non-secret)
                │   └── 📄 governance.controls.json         — Guardrails for exposure/aggregation
                │
                ├── 📁 promql/
                │   └── 📄 README.md
                │
                ├── 📁 logql/
                │   └── 📄 README.md
                │
                └── 📁 jq/
                    └── 📄 README.md
~~~

---

## 📘 Overview

Manifests exist to prevent “dashboard drift” by making query usage:

- **Explicit** (a query has an ID and a declared intent)
- **Unit-disciplined** (every output metric has an agreed unit and meaning)
- **Reviewable** (governance can approve/deny exposure patterns)
- **Machine-joinable** (dashboards, alerts, and CI checks can reference the same IDs)

This folder is intentionally small and strict: it is the **contract surface** between:

- query implementations (`promql/`, `logql/`, `jq/`)
- dashboards (`DASHBOARDS/`)
- alerts (`ALERTS/`)
- telemetry schemas and governance rules

---

## 🧭 Context

### 1. Why manifests are required

Queries are not “just strings” in KFM. They are governed instruments.

Without manifests:

- panels silently change semantics
- units get mixed (Wh vs kWh; gCO2e vs kgCO2e)
- teams add high-cardinality fields to logs or dashboards without review
- dashboards become un-auditable for FAIR+CARE and provenance

With manifests:

- every panel references a stable `query_id`
- every `query_id` references:
  - engine (`promql`, `logql`, `jq`)
  - file path / source
  - output metric(s)
  - unit(s)
  - allowed audience and aggregation mode

### 2. Non-negotiables

- Manifests MUST stay **aggregate-first**.
- Manifests MUST NOT embed secrets or endpoints requiring credentials.
- Query IDs MUST be stable across releases (deprecate, don’t reuse).

---

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  Q["Query implementations"] --> C["queries.catalog.json"]
  C --> P["panels.manifest.json"]
  P --> D["Dashboards"]
  C --> G["governance.controls.json"]
  G --> D
  C --> M["metrics.dictionary.json"]
  M --> D
~~~

---

## 🧪 Validation & CI/CD

### 1. Validation rules (normative)

CI MUST fail if:

- a manifest file is not valid JSON
- required files are missing (`queries.catalog.json`, `metrics.dictionary.json`)
- any `query_id` referenced by `panels.manifest.json` is missing from `queries.catalog.json`
- any metric referenced by a query is missing from `metrics.dictionary.json`
- any query declares units that conflict with the metric dictionary

### 2. Minimal validator expectations (conceptual)

- `queries.catalog.json`:
  - unique `query_id`
  - valid `engine` enum: `promql | logql | jq`
  - `source_path` exists
  - `outputs[]` declared
- `metrics.dictionary.json`:
  - unique `metric_id`
  - `unit` is present
  - `display_name` is present
- `governance.controls.json`:
  - declares default aggregation / exposure rules
  - contains allow/deny patterns for high-risk fields

---

## 📦 Data & Metadata

### 1. `queries.catalog.json` (canonical)

Purpose: **one place** to list every query that the dashboards/alerts are allowed to use.

Recommended shape:

~~~json
{
  "catalog_version": "v11.2.6",
  "domain": "reliability-sustainability-correlation",
  "queries": [
    {
      "query_id": "rsc.failures.by_workflow.1h",
      "engine": "logql",
      "source_path": "../logql/workflow_failures_by_workflow.logql",
      "description": "Count workflow failures grouped by workflow in a 1h window.",
      "outputs": [
        { "metric_id": "ci.failures.count", "unit": "count" }
      ],
      "tags": ["reliability", "ci", "aggregation"],
      "governance": { "aggregation": "required", "exposure": "public" }
    }
  ]
}
~~~

### 2. `metrics.dictionary.json` (unit + semantics)

Purpose: central truth for **metric meaning**.

Recommended shape:

~~~json
{
  "dictionary_version": "v11.2.6",
  "metrics": [
    {
      "metric_id": "ci.energy.wh",
      "display_name": "Energy (Wh)",
      "unit": "Wh",
      "kind": "sustainability",
      "description": "Energy consumed by a workflow run, aggregated and emitted as Wh."
    }
  ]
}
~~~

### 3. `panels.manifest.json` (optional but strongly recommended)

Purpose: declare **panel → query_id** mapping, so dashboards are reproducible and reviewable.

~~~json
{
  "panels_version": "v11.2.6",
  "dashboards": [
    {
      "dashboard_id": "rsc.overview",
      "panels": [
        {
          "panel_id": "rsc.overview.failures_by_workflow",
          "title": "Failures by workflow",
          "query_id": "rsc.failures.by_workflow.1h",
          "recommended_viz": "bar",
          "notes": "Aggregate-only. No run_id exposure."
        }
      ]
    }
  ]
}
~~~

### 4. `datasources.manifest.json` (env-safe; never secrets)

Purpose: document which logical sources a query expects.

~~~json
{
  "datasources_version": "v11.2.6",
  "sources": [
    { "source_id": "loki.kfm", "kind": "loki", "env": ["dev", "staging", "prod"] },
    { "source_id": "prom.kfm", "kind": "prometheus", "env": ["dev", "staging", "prod"] }
  ]
}
~~~

### 5. `governance.controls.json` (guardrails)

Purpose: policy hints that can be validated by CI and used by reviewers.

~~~json
{
  "controls_version": "v11.2.6",
  "defaults": {
    "aggregation_required": true,
    "deny_high_cardinality_fields": true
  },
  "denied_fields": ["email", "token", "secret", "api_key", "session_id"],
  "allowed_group_bys": ["workflow", "environment", "runner_pool"]
}
~~~

---

## 🧱 Architecture

- Query code lives in:
  - `../promql/`
  - `../logql/`
  - `../jq/`
- Manifests live here (`manifests/`) and are the *control plane* for:
  - dashboards
  - alerts
  - review and governance
  - reproducible exports (if you generate snapshots)

Design intent:

- Keep manifests stable and reviewable
- Keep query implementations flexible but referenced by stable IDs
- Prevent dashboards from directly embedding ad-hoc “unknown” queries

---

## ⚖ FAIR+CARE & Governance

- **Findable**: every query is addressable by `query_id`
- **Accessible**: manifests are readable and non-secret
- **Interoperable**: JSON manifests can be ingested into catalogs/graph
- **Reusable**: stable IDs and version history enable long-term audit

CARE constraints (enforced by design):

- no identity-level dashboards by default
- no sovereignty-controlled or culturally sensitive attributes exposed through telemetry queries
- changes to exposure rules require explicit governance review

---

## 🕰️ Version History

| Version | Date       | Author           | Summary                                                                 |
|--------:|------------|------------------|-------------------------------------------------------------------------|
| v11.2.6 | 2025-12-12 | `@kfm-telemetry` | Manifest index established for governed dashboard query catalogs.        |
| v11.2.4 | 2025-12-06 | `@kfm-telemetry` | Prior baseline (superseded by v11.2.6 manifest discipline and layout).   |

---

<div align="center">

🧾 **KFM — Query Manifests (v11.2.6)**  
Catalog-First Queries · Unit-Disciplined Metrics · Governance-Ready Dashboards

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Aligned-gold" />
<img src="https://img.shields.io/badge/Telemetry-Governed-orange" />

[⬅ Query Library](../README.md) ·
[📜 LogQL Pack](../logql/README.md) ·
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

