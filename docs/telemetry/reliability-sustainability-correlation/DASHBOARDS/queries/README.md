---
title: "🔎 Kansas Frontier Matrix — Dashboard Query Library (Reliability × Sustainability) (Diamond⁹ Ω / Crown∞Ω)"
path: "docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/README.md"

version: "v11.2.6"
last_updated: "2025-12-12"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"

signature_ref: "../../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../../releases/v11.2.6/reliability-sustainability-correlation-dashboards-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/reliability-sustainability-correlation-dashboards-v11.2.6.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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
  domain: "telemetry-dashboard-queries"
  applies_to:
    - "docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/**"

fair_category: "F1-A1-I2-R2"
care_label: "FAIR+CARE Governance Aligned"
sensitivity: "Query definitions over aggregated telemetry; must remain non-sensitive"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by Dashboard Query Library v12"

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
  - "docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/README.md@v11.2.4"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "../../../../../schemas/json/kfm-markdown-protocol-v11.2.6.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/kfm-markdown-protocol-v11.2.6-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:telemetry:rsc:dashboards:queries:index:v11.2.6"
semantic_document_id: "kfm-telemetry-rsc-dashboards-queries-index-v11.2.6"
event_source_id: "ledger:kfm:doc:telemetry:rsc:dashboards:queries:index:v11.2.6"
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
  standard: "Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence"
  telemetry: "Transparent Systems · Ethical Metrics · Sustainable Intelligence"
  graph: "Semantics × Provenance × Spatial Intelligence"

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

# 🔎 **KFM — Dashboard Query Library (Reliability × Sustainability)**
`docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/README.md`

**Purpose**  
Define the **governed query library** used by correlation dashboards to compute:
reliability signals (failures, retries, latency, incidents) alongside sustainability signals (energy, carbon, runtime),
with stable semantics suitable for **PR review**, **audits**, and **telemetry-driven governance**.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blue" />
<img src="https://img.shields.io/badge/Queries-Governed-informational" />
<img src="https://img.shields.io/badge/Units-Declared-orange" />
<img src="https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen" />

</div>

---

## 📘 Overview

This directory is the **single source of truth** for dashboard queries used by:

- reliability × sustainability correlation panels
- incident waste tracing views
- workflow cost hotspot dashboards

These queries are treated as **governed specifications**:

- query semantics MUST be stable and versioned
- units MUST be explicit (Wh, gCO₂e, seconds, count, rate)
- time windows MUST be declared (e.g., 5m rate, 24h rollup)
- queries MUST NOT embed secrets, hostnames, or restricted identifiers

**Supported query families (typical)**

- `promql/` — Prometheus time-series (rates, histograms, SLO-like rollups)
- `logql/` — Loki logs (retry storm signatures, error bursts)
- `sql/` — warehouse analytics (batch governance reporting)
- `jq/` — structured JSON shaping for dashboard-friendly outputs

If your stack uses only one engine, keep the others empty and document the choice here.

---

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 📁 telemetry/
    └── 📁 reliability-sustainability-correlation/
        └── 📁 DASHBOARDS/
            └── 📁 queries/
                ├── 📄 README.md
                │
                ├── 📁 promql/
                │   ├── 📄 workflow_duration_seconds.pql
                │   ├── 📄 workflow_energy_wh.pql
                │   ├── 📄 workflow_carbon_gco2e.pql
                │   ├── 📄 retry_rate_5m.pql
                │   └── 📄 failure_rate_5m.pql
                │
                ├── 📁 logql/
                │   ├── 📄 retry_storm_detector.lql
                │   └── 📄 fatal_error_burst.lql
                │
                ├── 📁 sql/
                │   ├── 📄 daily_correlation_rollup.sql
                │   └── 📄 incident_waste_attribution.sql
                │
                ├── 📁 jq/
                │   └── 📄 normalize_dashboard_payload.jq
                │
                ├── 📁 manifests/
                │   ├── 📄 queries.catalog.json
                │   └── 📄 metrics.dictionary.json
                │
                └── 📁 tests/
                    ├── 📄 fixtures.json
                    └── 📄 expected_outputs.json
~~~

**Naming rules (recommended)**

- Filenames MUST be lowercase snake_case.
- Suffix MUST reflect the query engine:
  - `.pql` for PromQL
  - `.lql` for LogQL
  - `.sql` for SQL
  - `.jq` for jq transforms
- If a query is dashboard-specific, prefix with dashboard ID:
  - `rsc_overview__workflow_energy_wh.pql`

---

## 🧭 Context

These queries exist to prevent “dashboard drift”:

- **Dashboards are easy to tweak**; queries must remain governed.
- Correlation claims are sensitive; queries must keep meaning stable across releases.
- Energy/carbon measurements must not be mixed with reliability metrics without:
  - declared units
  - defined joins/groupings
  - documented caveats

This folder is consumed by the dashboard layer at:

- `../definitions/` (dashboards)
- `../panels/` (panel JSON)
- `../screenshots/` (review evidence)

---

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A["Query file change (PR)"] --> B["Query lint and unit checks"]
  B --> C["Panel uses query (dashboard build)"]
  C --> D["Screenshot capture (review evidence)"]
  D --> E["Telemetry and governance review"]
~~~

---

## 🧠 Story Node & Focus Mode Integration

Query revisions may produce Story Nodes such as:

- `urn:kfm:story-node:telemetry:rsc:query-change:<commit_sha>`
- `urn:kfm:story-node:telemetry:rsc:metric-semantics:<metric_id>`

Focus Mode MAY:

- summarize the intent of a query using the manifest metadata
- explain “what changed” across versions (diff + reason)

Focus Mode MUST NOT:

- infer causality from a correlation chart
- claim “optimized” or “improved” without evidence from governed metrics

---

## 🧪 Validation & CI/CD

### 1. What gets validated

At minimum, CI SHOULD validate:

- file naming + extension rules
- presence of manifests under `manifests/`
- query text safety:
  - no secrets, tokens, credentials
  - no internal-only hostnames
- unit declarations in `metrics.dictionary.json` for every metric referenced by dashboards

### 2. Recommended checks (implementation-agnostic)

- **PromQL sanity**
  - forbid unbounded label explosions (cardinality guardrails)
  - require explicit windows for `rate()` / `increase()`
- **LogQL sanity**
  - require bounded time windows
  - ban regex patterns known to be expensive unless justified
- **SQL sanity**
  - require deterministic ordering in export queries
  - require explicit timezone handling for daily rollups
- **Regression fixtures**
  - `tests/fixtures.json` + `tests/expected_outputs.json` used by a validator script

If a dedicated validator exists, document it in `../../validators/README.md` and link it in the footer.

---

## 📦 Data & Metadata

### 1. Required manifests

**`manifests/queries.catalog.json`** SHOULD list each query:

- `query_id`
- `engine` (`promql`, `logql`, `sql`, `jq`)
- `path`
- `dashboard_ids` / `panel_ids` that use it
- `metrics_emitted` (IDs)
- `owner` (team) and `reviewer_group` (optional)

**`manifests/metrics.dictionary.json`** SHOULD define:

- `metric_id`
- `description`
- `unit` (e.g., `wh`, `gco2e`, `sec`, `count`, `ratio`)
- `aggregation` (sum, avg, p95, rate)
- `allowed_dimensions` (labels permitted)

### 2. Non-sensitive guarantee

All query libraries must be safe for public repo exposure:

- aggregate at workflow/job/service level
- avoid per-user or per-machine identifiers
- avoid coordinates and site-level sensitive markers

---

## 🌐 STAC, DCAT & PROV Alignment

- **DCAT**
  - The query library may be modeled as a `dcat:Dataset` with `dcat:Distribution` entries per query file.
  - Media types: `text/plain` (PromQL/LogQL), `application/sql`, `application/jq`.

- **PROV-O**
  - Query library = `prov:Plan`
  - Query change = `prov:Activity` (PR / commit)
  - Generated dashboards/reports = `prov:Entity` derived from these plans

STAC is optional; if used, treat query packs as non-spatial assets with `geometry: null`.

---

## 🧱 Architecture

Queries are “contract glue” between:

- telemetry storage (metrics/logs/traces)
- dashboards (panel configs)
- governance (alerts, evidence, trend reporting)

**Design rule**

Dashboards MUST refer to query IDs (via `queries.catalog.json`) rather than inlining “mystery queries” inside panel JSON.

---

## ⚖ FAIR+CARE & Governance

- **FAIR**
  - Findable: query IDs + catalogs
  - Accessible: stored in git with stable paths
  - Interoperable: normalized metric dictionary and unit conventions
  - Reusable: version history + fixtures for regression checks

- **CARE**
  - Avoid extractive or harmful interpretations (correlation ≠ causation)
  - Prevent accidental exposure of sensitive operational detail
  - Require explicit stewardship (owners, reviewer group)

If a query would expose sensitive patterns, it MUST be moved behind governance controls and removed from this public tree.

---

## 🕰️ Version History

| Version | Date       | Author           | Summary                                                                 |
|--------:|------------|------------------|-------------------------------------------------------------------------|
| v11.2.6 | 2025-12-12 | `@kfm-telemetry` | Established governed query library index, naming rules, manifests, and validation guidance under KFM-MDP v11.2.6. |
| v11.2.4 | 2025-12-06 | `@kfm-telemetry` | Prior baseline (superseded by v11.2.6).                                 |

---

<div align="center">

🔎 **KFM — Dashboard Query Library (Reliability × Sustainability) (v11.2.6)**  
Governed Semantics · Declared Units · Regression-Safe Queries

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blue" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Aligned-gold" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-green" />

[⬅ Dashboards](../README.md) ·
[🧩 Definitions](../definitions/README.md) ·
[🧱 Panels](../panels/README.md) ·
[🖼 Screenshots](../screenshots/README.md) ·
[🚨 Alerts](../../ALERTS/README.md) ·
[⬅ Correlation Module](../../README.md) ·
[⬅ Telemetry Index](../../../README.md) ·
[🧾 Specs](../../specs/README.md) ·
[🧪 Validators](../../validators/README.md) ·
[📦 Storage](../../storage/README.md) ·
[📦 Reports](../../reports/README.md) ·
[⚙ Workflows Index](../../../../workflows/README.md) ·
[⚙ Telemetry Export Workflow](../../../../workflows/telemetry-export.yml.md) ·
[📘 Docs Root](../../../../README.md) ·
[📘 Markdown Protocol](../../../../standards/kfm_markdown_protocol_v11.2.6.md) ·
[⚖ Governance Charter](../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⚡ Energy Schema](../../../../../schemas/telemetry/energy-v2.json) ·
[🌿 Carbon Schema](../../../../../schemas/telemetry/carbon-v2.json)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω

</div>

