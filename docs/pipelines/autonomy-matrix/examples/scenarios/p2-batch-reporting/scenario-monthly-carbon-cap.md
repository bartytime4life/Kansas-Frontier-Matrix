---
title: "📊 KFM v11 — P2 Batch Reporting · Monthly Carbon Cap Scenario"
description: "P2 batch reporting scenario where a non-urgent pipeline is paused after exceeding its monthly carbon budget in the KFM v11 Autonomy Matrix."
path: "docs/pipelines/autonomy-matrix/examples/scenarios/p2-batch-reporting/scenario-monthly-carbon-cap.md"
version: "v11.2.4"
last_updated: "2025-12-06"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability · Sustainability · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "Aligned with Autonomy Matrix v11.2.x (design-only; non-normative)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.4/autonomy-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/autonomy-matrix-v1.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

status: "Active / Enforced"
doc_kind: "Guide"
header_profile: "standard"
footer_profile: "standard"

intent: "autonomy-matrix-scenario-p2-batch-reporting-monthly-carbon-cap"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"

scope:
  domain: "pipelines"
  applies_to:
    - "etl"
    - "ingestion"
    - "ai-inference"
    - "refresh-pipelines"
    - "batch-reporting"
    - "control-plane-simulation"

semantic_intent:
  - "governance"
  - "control-plane"
  - "reliability"
  - "sustainability"
  - "carbon"
  - "examples"
  - "simulation"
  - "batch-reporting"

category: "Pipelines · Autonomy · Examples · Scenarios · P2 Batch Reporting"

sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Internal"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: false

data_steward: "Reliability · Sustainability · FAIR+CARE Council"
ttl_policy: "Indefinite (subject to architecture changes)"
sunset_policy: "Supersede when Autonomy Matrix v12 scenario framework is adopted"

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
  - "docs/pipelines/autonomy-matrix/examples/scenarios/p2-batch-reporting/README.md@v11.2.4"
  - "docs/pipelines/autonomy-matrix/examples/scenarios/README.md@v11.2.4"
  - "docs/pipelines/autonomy-matrix/examples/scenarios/fixtures/README.md@v11.2.4"
  - "docs/pipelines/autonomy-matrix/decider/contracts.md@v11.2.4"
  - "docs/pipelines/autonomy-matrix/decider/score-functions.md@v11.2.4"
  - "docs/pipelines/autonomy-matrix/decider/action-logic.md@v11.2.4"
  - "docs/pipelines/autonomy-matrix/decider/designs/state-machine.md@v11.2.4"
  - "docs/pipelines/autonomy-matrix/README.md@v11.2.3"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/docs-pipelines-autonomy-matrix-scenarios-p2-batch-reporting-monthly-carbon-cap-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/docs-pipelines-autonomy-matrix-scenarios-p2-batch-reporting-monthly-carbon-cap-v11.2.4-shape.ttl"

story_node_refs:
  - "urn:kfm:story-node:pipelines:autonomy-matrix:examples:scenarios:p2-batch-reporting:monthly-carbon-cap"

immutability_status: "mutable"

doc_uuid: "urn:kfm:doc:pipelines:autonomy-matrix:examples:scenarios:p2-batch-reporting:monthly-carbon-cap:v11.2.4"
semantic_document_id: "kfm-pipelines-autonomy-matrix-examples-scenarios-p2-batch-reporting-monthly-carbon-cap-v11.2.4"
event_source_id: "ledger:kfm:doc:pipelines:autonomy-matrix:examples:scenarios:p2-batch-reporting:monthly-carbon-cap:v11.2.4"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "diagram-extraction"
  - "metadata-extraction"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

transform_registry:
  allowed:
    - "summary"
    - "timeline-generation"
    - "semantic-highlighting"
    - "diagram-extraction"
    - "metadata-extraction"
    - "a11y-adaptations"
  prohibited:
    - "content-alteration"
    - "speculative-additions"
    - "unverified-architectural-claims"
    - "narrative-fabrication"
    - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🧭 Context"
    - "🧱 Architecture"
    - "📦 Data & Metadata"
    - "🧪 Validation & CI/CD"
    - "🧠 Story Node & Focus Mode Integration"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "provenance-check"
  - "footer-check"
  - "diagram-check"
  - "accessibility-check"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence"
  architecture: "Designed for Longevity · Governed for Integrity"
  analysis: "Research-Driven · Evidence-Led · FAIR+CARE Grounded"
  data-spec: "Open Data × Responsible Stewardship"
  pipeline: "Deterministic Pipelines · Explainable Autonomy · Open Provenance"
  telemetry: "Transparent Systems · Ethical Metrics · Sustainable Intelligence"
  graph: "Semantics × Provenance × Spatial Intelligence"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_version_history: true
requires_directory_layout_section: false
requires_governance_links_in_footer: true

deprecated_fields:
  - "old_markdown_standard_v10.4"

# Scenario-specific metadata
scenario_id: "p2-batch-reporting:monthly-carbon-cap"
scenario_status: "canonical"
pipeline_id: "p2-batch-reporting"
variant: "single-tenant"
fixture_ref: "../../fixtures/p2-batch-reporting.jsonl#monthly-carbon-cap"
---

<div align="center">

# 📊 **KFM v11 — P2 Batch Reporting · Monthly Carbon Cap Scenario**  
`docs/pipelines/autonomy-matrix/examples/scenarios/p2-batch-reporting/scenario-monthly-carbon-cap.md`

**Purpose:**  
Describe a **P2 batch reporting** scenario where the pipeline’s **monthly carbon budget is  
exhausted**, and the Autonomy Decider issues a **pause** action for non‑urgent work,  
demonstrating carbon‑aware de‑prioritization of low‑urgency pipelines.

</div>

---

## 📘 Overview

### Scenario Summary

This scenario models a **low‑urgency P2 batch reporting** pipeline that:

- Has run normally throughout the month, consuming incremental carbon budget.  
- Now sits **near or just past** its monthly carbon cap.  
- Has **no immediate report deadline** in the next hours.  
- Has normal data quality and no CARE/sovereignty issues.  

In this context, project policy for P2 workloads states:

- When the **monthly carbon cap is reached or exceeded**,  
  non‑critical batch reporting may be **paused** until:
  - A new accounting period begins, or  
  - A governance override explicitly resumes it.

The Autonomy Decider therefore:

- Recognizes the exhausted carbon budget via the cost/energy/carbon gate.  
- Issues a **`pause` action** instead of `resume` or `slow`.  
- Transitions the pipeline to **PAUSED** state in the Autonomy state machine.  

This scenario illustrates:

> For P2 pipelines, **carbon caps can legitimately trump schedule convenience**,  
> as long as governance requirements and SLO contracts are respected.

---

## 🧭 Context

### Pipeline Context

- **Pipeline family:** `p2-batch-reporting`  
- **Example member:** `reports/monthly-usage-summary` (synthetic).  
- **Urgency band:** `P2` (low urgency, deadline‑driven but not critical).  

Typical behavior:

- Generates monthly summary reports (e.g., aggregated usage, non‑critical metrics).  
- Has a **wide delivery window** (e.g., “by the 3rd of the following month”).  
- Runs several times near the end of the month for validation and retries.

**Synthetic budgets:**

- `monthly_cap_usd = 800`  
- `monthly_cap_kwh = 260`  
- `monthly_cap_kgco2e = 80`  

In this scenario:

- Carbon utilization **crosses** its budget, while cost and energy remain near their caps
  but not yet violated.

### Scenario Time Window

- **Scenario instant:** `2025‑04‑29T22:15:00Z` (synthetic; late in the month).  
- **Monthly carbon accounting period:** `2025‑04‑01T00:00Z`–`2025‑05‑01T00:00Z`.  
- Next scheduled non‑urgent batch run would:

  - Update monthly aggregates,  
  - But is **not required** for any immediate external report.

Thus:

- There is **no tight deadline** compelling execution.  
- The main consideration is **carbon policy compliance** for low‑urgency workloads.

---

## 🧱 Architecture

This section describes the **snapshot → score & gates → decision** chain.

### Snapshot

Representative synthetic snapshot at the decision tick:

- **Carbon & budgets**
  - `carbon_budget_utilization`: `1.07` (107% of monthly cap).  
  - `carbon_kgco2e_mtd`: `85.6` (vs cap = 80.0).  

- **Cost / energy (month‑to‑date)**
  - `cost_budget_utilization`: `0.88` (88%).  
  - `energy_budget_utilization`: `0.86` (86%).  

- **Instantaneous cost/energy/carbon (per hour)**
  - `cost_usd_hour`: `2.3`  
  - `kwh_hour`: `1.0`  
  - `carbon_kgco2e_hour`: `0.35`  

- **Schedule & deadlines**
  - `days_to_soft_deadline`: `4` (e.g., report due by May 3).  
  - `days_to_hard_deadline`: `6` (extended backstop).  
  - `est_runtime_hours`: `0.8` (less than 1 hour).  

- **Backlog & freshness**
  - `backlog_batches`: `0` (no queued runs).  
  - `last_successful_run_age_d`: `26` (last monthly batch was 26 days ago; intermediate runs optional).  

- **Data quality / trust**
  - `data_trust_index`: `0.95`  
  - `recent_test_pass_rate`: `0.98`  
  - `schema_violations_last_24h`: `0`  

- **Governance / CARE**
  - `care_label`: `Synthetic-Batch-Reporting`  
  - `sovereignty_policy`: `synthetic-reporting-generalization-v1`  

Interpretation:

- Carbon budget has been **exceeded**; other budgets are close but not breached.  
- No urgent deadlines; future optional runs could be rescheduled into a new window.  
- Data and CARE are clear.

### Score & Gates

#### Component Scores (conceptual)

For P2 batch reporting:

- `TemporalRelevance()` is relatively low:
  - Soft deadline is several days away.  
  - Example: `TemporalRelevance() = 0.25`.  

- `FreshnessScore()` is moderate:
  - Some value in updating monthly aggregates, but not urgent.  
  - Example: `FreshnessScore() = 0.40`.  

- `DataTrust()` is high:
  - Example: `DataTrust() = 0.94`.  

- `CostBurnRate()`, `EnergyKWhRate()`, `CarbonCO2eRate()` encode budget pressure:
  - `CostBurnRate() = 0.70`  
  - `EnergyKWhRate() = 0.68`  
  - `CarbonCO2eRate() = 1.00` (fully saturated and exceeded).  

Using example P2 weights:

~~~text
w_deadline = 0.25   # part of TemporalRelevance()
w_fresh    = 0.20
w_trust    = 0.15
w_cost     = 0.15
w_energy   = 0.10
w_carbon   = 0.15
~~~

Conceptual raw score:

~~~text
S_raw =
  0.25 * 0.25 +
  0.20 * 0.40 +
  0.15 * 0.94 -
  0.15 * 0.70 -
  0.10 * 0.68 -
  0.15 * 1.00
≈ -0.03   # synthetic example
~~~

After normalization:

~~~text
S_norm ≈ -0.03    # near or below pause threshold for P2
~~~

Example thresholds for P2:

~~~text
resume_up    = 0.55
resume_down  = 0.35
slow_up      = 0.20
slow_down    = 0.00
pause        = -0.20
~~~

So `S_norm ≈ -0.03` falls:

- **Below** `slow_down` (= 0.00)  
- **Above** `pause` (= -0.20)  

In isolation, this might suggest `slow` or `pause` depending on hysteresis.  
However, **gate decisions** take precedence.

#### Gates

Gate outputs (conceptual):

- `care`:
  - `status`: `OK`
  - `reason_code`: `care_clear`

- `cost_energy` (with carbon emphasis for P2):
  - `status`: `BLOCK`
  - `reason_code`: `carbon_cap_exceeded`
  - `details`:
    - `carbon_budget_utilization`: `1.07`
    - `carbon_cap_behavior`: `pause_p2_noncritical`
    - `workload_urgency_band`: `P2`

- `deadline_window`:
  - `status`: `OK`
  - `reason_code`: `deadline_far`
  - `details`:
    - `days_to_soft_deadline`: `4`
    - `est_runtime_hours`: `0.8`

- `cardinality_guard`:
  - `status`: `OK`
  - `reason_code`: `cardinality_normal`

The **BLOCK** from the carbon gate encodes governance policy:

- For **P2 non‑critical reporting**, when `carbon_cap_exceeded` is true,  
  **autonomy must pause** unless explicitly overridden.

### Decision & Expected Behavior

Given:

- Carbon gate `status = BLOCK` with `reason_code = carbon_cap_exceeded`.  
- No CARE or quality issues.  
- No tight deadline.  

Per action‑logic precedence:

1. If any critical gate emits `ESCALATE` → `action = escalate`.  
2. Else if any critical gate emits `BLOCK` → `action = pause`.  
3. Else score‑based mapping applies.

In this scenario:

- No `ESCALATE`, but carbon gate `BLOCK` ⇒ **`pause` overrides score bands**.

Expected decision:

- **Action:** `pause`  
- **State before:** likely `STABLE` (resume or slow).  
- **State after:** `PAUSED`  

Illustrative reason codes:

- `carbon_cap_exceeded`  
- `p2_noncritical_pause_policy`  

Operational semantics:

- Orchestrator:

  - Marks the pipeline as **autonomy‑paused** until:
    - The next month’s carbon period starts, or  
    - A governance override or manual run is requested.  

  - Suppresses non‑urgent batch jobs for this pipeline.  

- Governance:

  - Telemetry logs clearly link the pause decision to:
    - Carbon cap exceedance,  
    - P2 policy for non‑critical workloads.

---

## 📦 Data & Metadata

### Scenario Metadata (Logical View)

~~~json
{
  "scenario_id": "p2-batch-reporting:monthly-carbon-cap",
  "scenario_status": "canonical",
  "pipeline_id": "p2-batch-reporting",
  "variant": "single-tenant",
  "fixture_ref": "../../fixtures/p2-batch-reporting.jsonl#monthly-carbon-cap",
  "tags": [
    "p2",
    "batch-reporting",
    "carbon-cap",
    "pause",
    "sustainability"
  ]
}
~~~

### Fixture Mapping

`fixture_ref` points into:

- `docs/pipelines/autonomy-matrix/examples/scenarios/fixtures/p2-batch-reporting.jsonl#monthly-carbon-cap`

Fixture slice requirements:

- Encodes one or more ticks late in the month where:

  - `carbon_budget_utilization >= 1.0`.  
  - `cost_budget_utilization` and `energy_budget_utilization` are high but < 1.0.  
  - `days_to_soft_deadline` is several days, not hours.  
  - No CARE or data quality violations.  

- Includes `expected` fields like:

~~~json
"expected": {
  "scenario_id": "p2-batch-reporting:monthly-carbon-cap",
  "state": "PAUSED",
  "action": "pause"
}
~~~

Offline Simulator can:

- Replay the slice.  
- Confirm that the Decider:

  - Emits `pause` with carbon‑cap reasons.  
  - Moves the state to `PAUSED`.  

Graph alignment:

- `:AutonomyScenario { scenario_id: "p2-batch-reporting:monthly-carbon-cap" }`  
- Links to:

  - `(:Pipeline { id: "p2-batch-reporting" })` via `[:FOR_PIPELINE]`  
  - `(:AutonomyFixture { id: "p2-batch-reporting.jsonl#monthly-carbon-cap" })` via `[:USES_FIXTURE]`

---

## 🧪 Validation & CI/CD

This scenario is a **sustainability and governance regression guard** for P2 autonomy.

### CI Expectations

Scenario‑level test:

1. Load fixture slice `p2-batch-reporting.jsonl#monthly-carbon-cap`.  
2. Run Autonomy Decider with the P2 batch reporting profile and gates.  
3. Assert:

   - `action == "pause"`  
   - `state_after == "PAUSED"`  
   - Cost/energy/carbon gate `status == "BLOCK"` with reason including `carbon_cap_exceeded`.  
   - No `ESCALATE` unless policy explicitly calls for human escalation.  

4. Fail if:

   - Action is `resume` or `slow` despite `carbon_cap_exceeded` for P2 non‑critical workloads.  
   - Action is `escalate` where policy states simple pause is sufficient.  
   - Carbon gate does not trip even though utilization ≥ 1.0 in the fixture.

### Drift Detection

If changes to:

- Carbon budget thresholds,  
- P2 carbon policies,  
- Gate implementation,

cause divergence from this scenario’s expected behavior, CI should flag them as:

- **Policy updates** → scenario + fixtures + governance docs must be updated, or  
- **Regressions** → autonomy no longer respects P2 carbon‑cap rules.

---

## 🧠 Story Node & Focus Mode Integration

This scenario underpins explanations for:

> “Why is my low‑priority monthly report paused even though systems are healthy?”

Story Node anchor:

~~~text
urn:kfm:story-node:pipelines:autonomy-matrix:examples:scenarios:p2-batch-reporting:monthly-carbon-cap
~~~

Example narrative:

~~~text
In the P2 batch reporting monthly-carbon-cap scenario, a non-critical reporting pipeline
reaches 107% of its monthly carbon budget near the end of the month. There are no urgent
deadlines and data quality is good, but the Autonomy Decider honors the carbon policy for
P2 workloads by issuing a pause action. The pipeline enters PAUSED state until the next
carbon accounting period or a governance override explicitly resumes it.
~~~

Focus Mode can:

- Surface this scenario when operators see `pause` decisions tied to carbon caps.  
- Highlight that **carbon governance**, not errors or deadlines, is driving the pause.  
- Point users to carbon budget configuration and P2 policy docs.

---

## 🕰️ Version History

| Version    | Date       | Summary                                                                                                              |
|-----------:|------------|----------------------------------------------------------------------------------------------------------------------|
| **v11.2.4**| 2025-12-06 | Initial monthly-carbon-cap scenario for `p2-batch-reporting`: carbon cap BLOCK gate, `pause` decision, CI & SN role. |

---

<div align="center">

📊 **KFM v11 — P2 Batch Reporting · Monthly Carbon Cap Scenario**  
Carbon‑Cap Aware · Governance‑First · FAIR+CARE‑Aligned Batch Autonomy  

[📊 P2 Scenario Family](README.md) · [🎭 Scenario Library Root](../README.md) · [🤖 Autonomy Matrix](../../../README.md)

</div>

