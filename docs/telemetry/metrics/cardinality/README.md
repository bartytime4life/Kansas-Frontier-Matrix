---
title: "📊 KFM v11 — Metric Cardinality Management & Safe Label Design (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/telemetry/metrics/cardinality/README.md"
version: "v11.2.2"
last_updated: "2025-11-30"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Telemetry Governance · FAIR+CARE Council"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../../releases/v11.2.2/signature.sig"
attestation_ref: "../../../../releases/v11.2.2/slsa-attestation.json"
sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.2/otel-metrics.json"
telemetry_schema: "../../../../schemas/telemetry/metric-cardinality-v1.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Guideline"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "telemetry"
  applies_to:
    - "metrics"
    - "prometheus"
    - "mimir"
    - "otel"

semantic_intent:
  - "observability"
  - "governance"
  - "reliability"
category: "Telemetry · Observability · Standards"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM Telemetry Governance Council"
ttl_policy: "24 months"
sunset_policy: "Supersedes prior metric cardinality drafts (v11.1.0 and earlier)"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/telemetry/metrics/cardinality/README.md@v11.1.0"
  - "docs/telemetry/metrics/cardinality/README.md@v10.x"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: false

json_schema_ref: "../../../../schemas/json/telemetry-metric-cardinality-v1.schema.json"
shape_schema_ref: "../../../../schemas/shacl/telemetry-metric-cardinality-v1-shape.ttl"
story_node_refs: []
immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:telemetry:metrics:cardinality:v11.2.2"
semantic_document_id: "kfm-telemetry-metric-cardinality-v11.2.2"
event_source_id: "ledger:kfm:doc:telemetry:metrics:cardinality:v11.2.2"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "3d-context-render"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

transform_registry:
  allowed:
    - summary
    - timeline-generation
    - semantic-highlighting
    - 3d-context-render
    - a11y-adaptations
    - diagram-extraction
    - metadata-extraction
  prohibited:
    - content-alteration
    - speculative-additions
    - unverified-architectural-claims
    - narrative-fabrication
    - governance-override

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧭 Context & Scope"
    - "🧱 Cardinality Model"
    - "📊 Labels & Vocabularies"
    - "📉 Reduction Techniques"
    - "🧪 Governance & Controls"
    - "🧠 Story Node & Focus Mode Integration"
    - "⚖ FAIR+CARE & Ethics"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "footer-check"
  - "accessibility-check"
  - "provenance-check"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence"
  architecture: "Designed for Longevity · Governed for Integrity"
  analysis: "Telemetry-Driven · Evidence-Led · FAIR+CARE Grounded"
  data-spec: "Open Metrics × Responsible Cardinality"
  pipeline: "Deterministic Pipelines · Explainable Observability · Open Provenance"
  telemetry: "Transparent Metrics · Ethical Aggregates · Sustainable Intelligence"
  graph: "Semantics × Telemetry × Spatial Intelligence"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_version_history: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true

deprecated_fields:
  - "old_metric_cardinality_standard_v10"
---

<div align="center">

# 📊 **KFM v11 — Metric Cardinality Management & Safe Label Design**  
`docs/telemetry/metrics/cardinality/README.md`

**Purpose**  
Define the **governed standard** for **metric cardinality safety** in the Kansas Frontier Matrix (KFM) v11.2.2.  
This document keeps metrics **deterministic & low-cardinality**, protects **Prometheus/Mimir cost ceilings**, and enforces **FAIR+CARE-aligned telemetry**.

</div>

---

## 🗂️ Directory Layout

~~~text
docs/telemetry/metrics/cardinality/
├── 📄 README.md                       # Metric cardinality standard (this file)
├── 📂 patterns/                       # Best-practice patterns & anti-patterns
│   └── 📄 patterns.md                 # Pattern definitions & examples
├── 📂 governance/                     # Enforcement workflows & guardrails
│   └── 📄 governance.md               # Governance procedures & escalation paths
└── 📂 review-log/                     # Quarterly audit & anomaly records
    └── 📄 review-log.md               # ASB budgets, quarantines, spike reports
~~~

**Layout rules**  
- 📂 is used only for directories; 📄 is used only for files.  
- No emojis appear inside the ASCII connectors themselves.  
- Every directory above MUST maintain a `README.md` documenting its local scope.

---

## 📘 Overview

This guideline applies to **all metrics emitted anywhere in KFM v11** (ETL, graph, Focus Mode, UI, infra).  
It standardizes:

- Allowed vs forbidden labels (cardinality whitelist/blacklist).  
- Required binning and normalization rules.  
- Governance controls (Active Series Budgets, spike detection, quarantine).  
- Integration points with Story Nodes and Focus Mode.

Any metric that does **not** comply with this document is considered **out of policy** and may be quarantined or dropped.

---

## 🧭 Context & Scope

- **Audience**: SREs, observability engineers, ETL developers, data scientists, and any team emitting metrics.  
- **Systems covered**: Prometheus, Grafana Mimir, and any OpenTelemetry-based metric exporters in KFM.  
- **Environments**: `dev`, `staging`, `prod`, plus any dedicated research clusters attached to KFM v11.

This document is a **PROV-O `prov:Plan`** for how metrics must look and behave; all telemetry code and dashboards SHOULD claim conformance to this plan.

---

## 🧱 Cardinality Model

### 1. Series Definition

Each unique label set yields a new time series:

~~~text
metric_name{label_a="x", label_b="y"}
~~~

### 2. Risk Drivers

Cardinality risk arises from:

- Per-object labels (IDs, paths, coordinates, unique hashes).  
- Free-form or unbounded label values.  
- Rapidly changing label sets (e.g., new label keys added by deploys).

High cardinality leads to:

- Explosive memory usage.  
- Slow queries and dashboards.  
- Increased storage cost and retention pressure.  
- Difficulty debugging due to metric noise.

This standard mitigates those risks with a **strict label contract** and **governance process**.

---

## 📊 Labels & Vocabularies

### 1. Approved Labels (Whitelist)

The only **default-permitted** labels on KFM metrics are:

- `service`  
- `pipeline`  
- `component`  
- `region`  
- `dataset`  
- `dataset_release`  
- `status`  
- `method`  
- `layer`  
- `zoom_bin`  
- `phase`  
- `op`  

Rules:

- Every label key MUST be documented in the telemetry catalog.  
- Each key MUST have a **finite, documented vocabulary** of values.  
- Adding a new label key requires a governance change recorded in `governance.md`.

### 2. Forbidden Labels

The following labels (or equivalents) are **prohibited** on all metrics:

- `user_id`  
- `request_id`, `session_id`, `trace_id`, `span_id`  
- `tile_id`, `feature_id`, `stac_id`  
- `file_path`, `s3_path`, `http_url`  
- `timestamp`, `ts`  
- `lat`, `lon`, `x`, `y`, `elev`  
- Dynamic H3 cells (for example, `h3_cell="8f28308280f1fff"`)  
- Sensor/instance IDs (`sensor_id`, `pod_name`, `container_id`, `task_id`, etc.)  
- Any unbounded free-form label derived from input or runtime data  

Any metric emitting these labels must be treated as a **policy violation**.

### 3. Examples

#### ✔ Correct

~~~text
kfm_ingest_total{service="etl", dataset="usgs_hydro", status="ok"}
kfm_tile_build_seconds{layer="soil", zoom_bin="9-12", status="success"}
kfm_graph_upserts_total{op="merge", dataset_release="v11.2"}
~~~

#### ❌ Incorrect

~~~text
kfm_ingest_total{stac_id="20251130T2100Z"}
kfm_tile_build_seconds{http_url="/tiles/11/345"}
kfm_graph_upserts_total{feature_id="abc123"}
~~~

---

## 📉 Reduction Techniques

### 1. Binning

Cardinality-prone dimensions MUST be binned:

- Zoom level → `zoom_bin` (`0-4`, `5-8`, `9-12`, `13-16`, `17-22`).  
- Elevation → `elev_bin` (for example, `<=200m`, `200–400m`, `>400m`).  
- Resolution → `low`, `medium`, `high`.  
- File size → `size_class` (`tiny`, `small`, `medium`, `large`, `huge`).  

### 2. Path & ID Handling

- Paths and URLs must be **normalized** and logged, not labeled.  
- IDs must live in **traces** or **logs**, not metric labels.

### 3. Placement of Volatility

- Metrics: stable categories only.  
- Traces: request/trace/span/feature IDs.  
- Logs: raw URLs, paths, and context payloads.

This reflects **data minimization** and ensures metrics remain both usable and privacy-respecting.

---

## 🧪 Governance & Controls

### 1. Active Series Budget (ASB)

Each environment defines an **Active Series Budget**:

- Hard limit: rejecting new series and alerting when exceeded.  
- Soft limit (for example, 80%): early warning, governance ticket, and Story Node seed.

Budgets are recorded and reviewed in `review-log/`, and may differ for `dev`, `staging`, and `prod`.

### 2. Spike Detection

A spike is declared when:

- A new label key appears at runtime.  
- Total active series increase by ≥30% in 5 minutes.  
- A single metric family expands by more than a configured threshold (for example, +10k series).

Spike handling:

- Persist an anomaly entry in `review-log.md`.  
- Attach provenance details (deployment, config commit, service, labels).  
- Optionally apply **deny-match** rules to block or drop the offending metrics until remediation.

### 3. Quarantine

When a metric is in violation:

- Drop samples at scrape time via relabel/drop rules.  
- Disable recording/alert rules dependent on the metric.  
- Open a governance incident tracked through Telemetry Governance Council.  
- Ensure the incident outcome is reflected in `patterns.md` and `governance.md`.

---

## 🧠 Story Node & Focus Mode Integration

Cardinality anomalies are captured not just as logs, but as **narrative events**.

### 1. Anomaly → Story Node

Upon detection of a significant anomaly:

- Generate a **Story Node seed** with:
  - Summary of the anomaly.  
  - Affected metric(s) and labels.  
  - Series budget impact.  
  - Link to the relevant `review-log` entry and governance ticket.

These seeds can be promoted to full Story Nodes under `docs/story-nodes/system/` (for example, `ci-health.json`, `metrics-cardinality-incident-2025Q4.json`).

### 2. Focus Mode Behavior

When Focus Mode is centered on:

- A metric family; or  
- A telemetry subsystem (e.g. “cardinality governance”); or  
- An environment (e.g. `prod-telemetry`),

it MAY:

- Render a timeline of cardinality incidents.  
- Highlight deployments introducing new labels.  
- Summarize how budget utilization changed over releases.

It MUST:

- Respect `ai_transform_prohibited` constraints.  
- Avoid exposing sensitive IDs or internal-only labels.  
- Include PROV-O lineage for all narrative claims.

---

## ⚖ FAIR+CARE & Ethics

This standard supports FAIR+CARE by:

- Keeping metrics **findable** and analyzable through controlled labels and consistent metadata.  
- Respecting **Authority to Control** by avoiding user- or entity-identifying labels in metrics.  
- Promoting **Responsibility** by codifying cardinality governance and mandatory review.  
- Ensuring **Reusability** by documenting label contracts and metric metadata so others can safely build on them.

Telemetry authors MUST:

- Avoid encoding protected or sensitive attributes in labels.  
- Consider downstream use when defining metrics (e.g. dashboards, public datasets).  
- Escalate concerns when a requested metric appears to violate CARE or sovereignty policies.

---

## 🕰️ Version History

| Version | Date       | Summary                                                                                                           |
|--------:|------------|-------------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Complete rewrite aligned with KFM-MDP v11.2.2; added ASB, spike detection, Story Node integration, and CI checks. |
| v11.1.0 | 2025-08-15 | Introduced explicit whitelist/blacklist label model and baseline query hygiene guidance.                          |
| v10.x   | 2024-03-01 | Initial draft of metric cardinality guidance and informal label recommendations.                                  |

---

<div align="center">

📊 **KFM v11 — Metric Cardinality Management & Safe Label Design**  
Observability With Purpose · Deterministic Metrics · FAIR+CARE Telemetry  

[📘 Docs Root](../../../../README.md) · [🧭 Standards Index](../../../standards/README.md) · [⚖ Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
