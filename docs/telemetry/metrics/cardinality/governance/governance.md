---
title: "⚖️ Kansas Frontier Matrix — Cardinality Governance Procedures v11.2.2"
path: "docs/telemetry/metrics/cardinality/governance/governance.md"
version: "v11.2.2"
last_updated: "2025-11-30"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Telemetry Governance Council"
content_stability: "stable"
commit_sha: "<latest-commit-hash>"
signature_ref: "../../../../../releases/v11.2.2/signature.sig"
attestation_ref: "../../../../../releases/v11.2.2/slsa-attestation.json"
sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/otel-metrics.json"
telemetry_schema: "../../../../../schemas/telemetry/metric-cardinality-v1.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
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
  domain: "telemetry-cardinality-governance"
  applies_to:
    - "prometheus"
    - "mimir"
    - "otel"
    - "metrics-governance"
semantic_intent:
  - "governance"
  - "observability"
  - "reliability"
category: "Telemetry · Governance · Standards"
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
sunset_policy: "Supersedes cardinality-governance v11.1.0"
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
  - "docs/telemetry/metrics/cardinality/governance/governance.md@v11.1.0"
  - "docs/telemetry/metrics/cardinality/governance/governance.md@v10.x"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: false
json_schema_ref: "../../../../../schemas/json/telemetry-governance-v1.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/telemetry-governance-v1-shape.ttl"
story_node_refs: []
immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:telemetry:metrics:cardinality:governance:procedures:v11.2.2"
semantic_document_id: "kfm-telemetry-metric-cardinality-governance-procedures-v11.2.2"
event_source_id: "ledger:kfm:doc:telemetry:metrics:cardinality:governance:v11.2.2"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
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
    - "🧪 Enforcement Lifecycle"
    - "🧱 Metric Introduction Workflow"
    - "📉 Label Schema Change Workflow"
    - "🔎 Violation & Spike Handling Procedures"
    - "🛑 Quarantine Logic"
    - "🛠 Remediation Workflow"
    - "📑 Deny-Match Rules (Templates)"
    - "📋 Governance Ticket Template"
    - "🔎 Review Log Entry Template"
    - "🧠 Story Node & Focus Mode Integration"
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
  telemetry: "Transparent Metrics · Ethical Aggregates · Sustainable Intelligence"
layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
requires_purpose_block: true
requires_version_history: true
requires_directory_layout_section: false
requires_governance_links_in_footer: true
deprecated_fields:
  - "old_cardinality_governance_v10"
---

<div align="center">

# ⚖️ **Cardinality Governance Procedures (Detailed Enforcement Specification)**  
`docs/telemetry/metrics/cardinality/governance/governance.md`

**Purpose**  
Define the **step-by-step enforcement logic, escalation chain, deny-match rules, investigation workflow, and governance ticketing protocol** associated with metric cardinality violations in KFM v11.  
This file operationalizes the rules declared in this directory’s `README.md`.

</div>

---

## 📘 Overview

This document formalizes the governance rules that control:

- Approving new metrics  
- Approving new labels  
- Enforcing Active Series Budgets (ASB)  
- Detecting cardinality spikes  
- Quarantining unsafe metrics  
- Requiring remediation and documentation  
- Recording violations in review logs  
- Generating system-level Story Node seeds  

All telemetry systems MUST comply with these procedures.

---

## 🧪 Enforcement Lifecycle

This lifecycle governs **all** cardinality infra changes:

1. **Emit or detect** metric samples  
2. **Validate** samples (CI + runtime)  
3. **Compare** emitted labels against the governance whitelist  
4. **Measure** series growth against ASB  
5. **Trigger** violation pipelines when needed  
6. **Record** anomaly in review logs  
7. **Quarantine** offending metrics if necessary  
8. **Open** governance ticket  
9. **Investigate → fix → restore**  
10. **Capture** remediation in Story Node

---

## 🧱 Metric Introduction Workflow

A new metric may only be introduced after the following steps.

### Step 1 — Submit Metadata

Developer MUST submit:

- `metric_name`  
- Description  
- Allowed label keys  
- Allowed label values (enumerated)  
- Expected cardinality estimate  
- Expected series count in `prod`  
- Owner team  
- Stability classification (`alpha`, `beta`, `stable`)  
- Lineage reference file  

### Step 2 — Validation

- Metadata MUST validate against telemetry schema.  
- CI MUST ensure label keys exist in the cardinality whitelist.  
- CI MUST ensure all values map to a bounded vocabulary.  
- No forbidden labels may appear, even temporarily.

### Step 3 — Governance Approval

Telemetry Governance Council must approve:

- Label vocabularies  
- Expected series count  
- Stability classification  
- Category placement (metrics vs logs vs traces)

### Step 4 — Controlled Deployment

- New metric is enabled in **dev only**.  
- After 48 hours of stability, deployed to **staging**.  
- After review, deployed to **prod**.

No metric may bypass this process.

---

## 📉 Label Schema Change Workflow

Label schema changes are **dangerous** and require strict approval.

### Step 1 — Proposal

Developer must propose:

- New label key  
- Full vocabulary  
- Reason for introduction  
- Query-hygiene impact  
- Estimated ASB delta  
- Expected usage patterns  

### Step 2 — Governance Review

Council will evaluate:

- Cardinality cost  
- Query complexity  
- Query cost in Grafana / Mimir  
- Impact on dashboards  
- FAIR+CARE and privacy implications  

If accepted → proceed.  
If rejected → new label is forbidden.

### Step 3 — Metadata Update

- Telemetry catalog updated.  
- Schema updated.  
- Validation rules regenerated.  
- CI rules refreshed.  

### Step 4 — Deployment

Same 3-stage deploy as metric introduction (`dev` → `staging` → `prod`).

---

## 🔎 Violation & Spike Handling Procedures

Violations include:

- Forbidden labels  
- Unbounded values or free-text  
- Per-entity ID labels  
- New label keys without approval  
- Raw paths or URLs  
- Any label not enumerated  
- Unexpected ASB explosion  

### 3.1 Spike detection thresholds

A spike is declared when:

- ≥30% series growth in 5 minutes  
- >10k new series in a metric family  
- A new label key appears  
- Cardinality shift coincides with a deploy  

### 3.2 Spike Handling Workflow

1. **Detect spike** (scraper / Mimir / CI).  
2. **Emit spike event** to governance pipeline.  
3. **Write anomaly** to `review-log.md`.  
4. **Attach**:
   - Service  
   - Environment  
   - Time window  
   - Offending label(s)  
   - Cardinality delta  
5. **Evaluate** need for deny-match rule.  
6. **Open governance ticket**.  
7. **Create Story Node seed**.  
8. **Begin investigation**.  

---

## 🛑 Quarantine Logic

Quarantine is a **hard safety measure**.  
A metric MUST be quarantined when:

- A forbidden label is detected.  
- ASB exceeds hard threshold.  
- A new label key appears without approval.  
- Free-form or unique label values appear.  
- Emitted labels violate allowed vocabulary.  

### Quarantine Steps

1. Inject **drop rule** (scrape-time reject).  
2. Inject **deny-match** (block queries & recording rules).  
3. Notify service owners.  
4. Add entry to review log.  
5. Force governance ticket creation.  
6. Require remediation plan.  
7. Attach PROV-O lineage.  

### While Quarantined

- Dashboards referencing the metric MUST display fallback visuals.  
- Alerts referencing the metric MUST be paused or revised.  
- Metric MUST NOT re-enter the environment until governance re-approves.  

---

## 🛠 Remediation Workflow

### Step 1 — Verify Root Cause

Identify:

- Commit / deploy introducing the issue.  
- Feature flag or config change.  
- Label key and value(s).  

### Step 2 — Remove Offending Code

Fix metric exporter:

- Remove forbidden label.  
- Replace with binned category.  
- Normalize path.  
- Move ID to trace or log.  

### Step 3 — Regenerate Metadata

Update:

- `allowed_labels`  
- `forbidden_labels`  
- Vocabularies  
- Lineage files  

### Step 4 — Validation

- Static check.  
- CI schema validation.  
- Prometheus rule validation.  
- Mimir rule ingestion dry-run.  

### Step 5 — Staged Redeploy

- **dev** → verification.  
- **staging** → baseline cardinality.  
- **prod** → full reactivation.  

### Step 6 — Document Story Node

A remediation Story Node MUST be created.

---

## 📑 Deny-Match Rules (Templates)

A deny-match blocks ingestion or recording of metrics violating rules.

### Template 1 — Block Entire Metric

~~~text
- action: drop
  match:
    metric_name: "kfm_graph_upserts_total"
~~~

### Template 2 — Block Forbidden Label Key

~~~text
- action: drop
  match_re:
    label_name: "(feature_id|tile_id|trace_id)"
~~~

### Template 3 — Block Values

~~~text
- action: drop
  match_re:
    layer: "^(.*)$"
    value: "(.*[A-Z].*)$"
~~~

### Template 4 — Emergency Quarantine

~~~text
- action: drop
  match_re:
    __name__: ".*"
  source_labels: [ offending_label ]
~~~

---

## 📋 Governance Ticket Template

A telemetry governance ticket MUST include:

- Metric family  
- Offending label(s)  
- Type of violation  
- Severity level  
- ASB delta  
- Spike duration  
- Environment  
- Service owner  
- Deployment hash  
- Attached anomaly log  
- Required remediation steps  
- Link to Story Node seed  

---

## 🔎 Review Log Entry Template

Every anomaly MUST be appended to:

`docs/telemetry/metrics/cardinality/review-log/review-log.md`

Format:

~~~text
### [2025-11-30] Cardinality Violation — <metric_name>

- Environment: prod
- Service: tiler
- Offending Label(s): feature_id="abc123"
- Cardinality Delta: +42,331 series
- Trigger: Deploy 91fca2d
- Action: Quarantined
- Governance Ticket: GOV-2025-113
- Story Node Seed: urn:kfm:story:telemetry:cardinality:violation:2025-11-30-tiler
~~~

---

## 🧠 Story Node & Focus Mode Integration

- Every governance event produces a **Story Node seed**.  
- PROV-O lineage MUST be attached.  
- Focus Mode MAY generate:
  - Cardinality “Spike Timeline”.  
  - “Quarantine and Restore” narrative.  
  - Deployment/label mapping.  
- Investigative steps become narrative material.  
- Resolution MUST close the narrative loop.  

---

## 🕰️ Version History

| Version | Date       | Summary                                                                                           |
|--------:|------------|---------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Converted to full governed document with complete metadata; aligned with KFM-MDP v11.2.2.        |
| v11.1.0 | 2025-08-15 | Prior detailed procedures for cardinality governance and enforcement.                             |
| v10.x   | 2024-03-01 | Initial governance draft capturing basic enforcement steps for metric cardinality violations.     |

---

<div align="center">

⚖️ **Cardinality Governance Procedures**  
Telemetry Stability · Deterministic Metrics · FAIR+CARE-Aligned  

[📘 Docs Root](../../../../README.md) · [🧭 Standards Index](../../../standards/README.md) · [⚖ Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
