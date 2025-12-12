---
title: "📈 KFM — PromQL Query Pack (Reliability × Sustainability Dashboards) (Diamond⁹ Ω / Crown∞Ω)"
path: "docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/promql/README.md"

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
  domain: "promql-queries"
  applies_to:
    - "docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/promql/**"

fair_category: "F1-A1-I2-R2"
care_label: "FAIR+CARE Governance Aligned"
sensitivity: "PromQL over aggregated metrics; no secrets; no host-level identifiers"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by PromQL Query Pack v12"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/promql/README.md@v11.2.4"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "../../../../../../schemas/json/kfm-markdown-protocol-v11.2.6.schema.json"
shape_schema_ref: "../../../../../../schemas/shacl/kfm-markdown-protocol-v11.2.6-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:telemetry:rsc:dashboards:queries:promql:index:v11.2.6"
semantic_document_id: "kfm-telemetry-rsc-dashboards-queries-promql-index-v11.2.6"
event_source_id: "ledger:kfm:doc:telemetry:rsc:dashboards:queries:promql:index:v11.2.6"
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

# 📈 **KFM — PromQL Query Pack**
`docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/promql/README.md`

**Purpose**  
Governed **PromQL query pack** used by the Reliability × Sustainability correlation dashboards.
These queries compute rollups for **duration**, **failure/retry rate**, **energy (Wh)**, and **carbon (gCO₂e)** using stable semantics and explicit units.

<img src="https://img.shields.io/badge/PromQL-Governed-informational" />
<img src="https://img.shields.io/badge/Units-Declared-orange" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen" />

</div>

---

## 📘 Overview

This folder contains PromQL queries that power dashboard panels where:

- Reliability metrics (errors, retries, duration, SLO-ish signals)
- are interpreted alongside
- Sustainability metrics (energy, carbon)

**Non-negotiable rules**

- Queries MUST be safe for public exposure (aggregate metrics only).
- Queries MUST declare a window for `rate()` / `increase()` / histogram quantiles.
- Queries MUST avoid high-cardinality label joins unless explicitly justified.
- Units MUST be obvious in the query ID / filename and in the metric dictionary.

---

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 📁 telemetry/
    └── 📁 reliability-sustainability-correlation/
        └── 📁 DASHBOARDS/
            └── 📁 queries/
                └── 📁 promql/
                    ├── 📄 README.md
                    │
                    ├── 📄 workflow_duration_seconds.pql
                    ├── 📄 workflow_failure_rate_5m.pql
                    ├── 📄 workflow_retry_rate_5m.pql
                    │
                    ├── 📄 workflow_energy_wh_sum_1h.pql
                    ├── 📄 workflow_energy_wh_rate_5m.pql
                    │
                    ├── 📄 workflow_carbon_gco2e_sum_1h.pql
                    ├── 📄 workflow_carbon_gco2e_rate_5m.pql
                    │
                    └── 📄 correlation_energy_vs_failures_1h.pql
~~~

If your repo uses different filenames, keep this README consistent with the actual file list and update the layout accordingly.

---

## 🧭 Context

PromQL is used here to support three common dashboard needs:

1. **Time-local rate views**  
   Example: “retry rate over 5 minutes”, “energy burn rate over 5 minutes”.

2. **Rollup / accumulation views**  
   Example: “Wh consumed per hour”, “gCO₂e per hour”.

3. **Correlation proxies**  
   Example: “energy per successful workflow” vs. “energy per failure”, or comparing spikes.

**Caution**

Correlation panels are descriptive. These queries MUST NOT be framed as causal proof.

---

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A["Prometheus metrics"] --> B["PromQL queries (.pql)"]
  B --> C["Dashboard panels"]
  C --> D["Screenshots + review evidence"]
  D --> E["Governance telemetry"]
~~~

---

## 🧪 Validation & CI/CD

Recommended validations for this folder:

- `.pql` files MUST be UTF-8 and non-empty.
- `rate()` and `increase()` MUST specify a window (e.g., `[5m]`, `[1h]`).
- Histogram queries MUST use consistent label sets (avoid accidental many-to-many joins).
- Queries MUST NOT contain:
  - bearer tokens
  - internal hostnames
  - direct runner IDs
  - user identifiers

If a PromQL linter exists, document it in:

- `../../validators/README.md`

---

## 📦 Data & Metadata

### Metric naming expectations

PromQL query outputs should map to a dictionary entry in:

- `../manifests/metrics.dictionary.json`

Expected unit conventions:

- Duration: `sec` or `ms` (be consistent)
- Energy: `wh`
- Carbon: `gco2e`
- Rates: `per_sec` or `per_min` (declare which)

### Query catalog integration

Each `.pql` SHOULD be registered in:

- `../manifests/queries.catalog.json`

with:

- `query_id`
- `path`
- `metrics_emitted`
- `dashboard_ids` / `panel_ids`

---

## 🌐 STAC, DCAT & PROV Alignment

- **DCAT**
  - PromQL pack is a `dcat:Dataset`, `.pql` files are `dcat:Distribution` entries.
- **PROV**
  - The query pack is a `prov:Plan` used by dashboard generation activities.

STAC is optional; treat query artifacts as non-spatial.

---

## ⚖ FAIR+CARE & Governance

- PromQL queries MUST remain interpretable and auditable.
- Queries MUST avoid sensitive operational leakage.
- Governance review SHOULD focus on:
  - semantic stability (does it mean the same thing as last release?)
  - unit correctness
  - label-cardinality risk

---

## 🕰️ Version History

| Version | Date       | Author           | Summary                                                                 |
|--------:|------------|------------------|-------------------------------------------------------------------------|
| v11.2.6 | 2025-12-12 | `@kfm-telemetry` | PromQL query pack index created/updated for governed correlation dashboards. |
| v11.2.4 | 2025-12-06 | `@kfm-telemetry` | Prior baseline (superseded by v11.2.6).                                 |

---

<div align="center">

📈 **KFM — PromQL Query Pack (v11.2.6)**  
Stable Semantics · Declared Units · Cardinality-Safe Queries

<img src="https://img.shields.io/badge/PromQL-Governed-informational" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Aligned-gold" />

[⬅ Query Library](../README.md) ·
[🧾 Query Catalog](../manifests/queries.catalog.json) ·
[📘 Metric Dictionary](../manifests/metrics.dictionary.json) ·
[🧪 Validators](../../validators/README.md) ·
[🖼 Dashboard Screenshots](../../screenshots/README.md) ·
[🚨 Alerts](../../ALERTS/README.md) ·
[⬅ Correlation Module](../../README.md) ·
[⬅ Telemetry Index](../../../README.md) ·
[⚙ Workflows Index](../../../../workflows/README.md) ·
[📘 Markdown Protocol](../../../../standards/kfm_markdown_protocol_v11.2.6.md) ·
[⚖ Governance Charter](../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω

</div>

