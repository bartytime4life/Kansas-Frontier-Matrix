---
title: "📊 KFM v11 — P2 Batch Reporting · Deadline Catch‑Up Scenario"
description: "P2 batch reporting scenario where a previously slowed or paused pipeline must resume to meet its reporting deadline in the KFM v11 Autonomy Matrix."
path: "docs/pipelines/autonomy-matrix/examples/scenarios/p2-batch-reporting/scenario-deadline-catchup.md"
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

intent: "autonomy-matrix-scenario-p2-batch-reporting-deadline-catchup"
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
  - "examples"
  - "simulation"
  - "batch-reporting"
  - "deadline"

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
  - "docs/pipelines/autonomy-matrix/decider/score-functions.md@v11.2.4"
  - "docs/pipelines/autonomy-matrix/decider/action-logic.md@v11.2.4"
  - "docs/pipelines/autonomy-matrix/decider/designs/state-machine.md@v11.2.4"
  - "docs/pipelines/autonomy-matrix/README.md@v11.2.3"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/docs-pipelines-autonomy-matrix-scenarios-p2-batch-reporting-deadline-catchup-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/docs-pipelines-autonomy-matrix-scenarios-p2-batch-reporting-deadline-catchup-v11.2.4-shape.ttl"

story_node_refs:
  - "urn:kfm:story-node:pipelines:autonomy-matrix:examples:scenarios:p2-batch-reporting:deadline-catchup"

immutability_status: "mutable"

doc_uuid: "urn:kfm:doc:pipelines:autonomy-matrix:examples:scenarios:p2-batch-reporting:deadline-catchup:v11.2.4"
semantic_document_id: "kfm-pipelines-autonomy-matrix-examples-scenarios-p2-batch-reporting-deadline-catchup-v11.2.4"
event_source_id: "ledger:kfm:doc:pipelines:autonomy-matrix:examples:scenarios:p2-batch-reporting:deadline-catchup:v11.2.4"

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
scenario_id: "p2-batch-reporting:deadline-catchup"
scenario_status: "canonical"
pipeline_id: "p2-batch-reporting"
variant: "single-tenant"
fixture_ref: "../../fixtures/p2-batch-reporting.jsonl#deadline-catchup"
---

<div align="center">

# 📊 **KFM v11 — P2 Batch Reporting · Deadline Catch‑Up Scenario**  
`docs/pipelines/autonomy-matrix/examples/scenarios/p2-batch-reporting/scenario-deadline-catchup.md`

**Purpose:**  
Describe a **P2 batch reporting** scenario where a previously slowed or paused pipeline  
approaches its reporting deadline, causing the Autonomy Decider to **resume** execution  
despite higher cost/carbon, in order to honor reporting windows and SLOs.

</div>

---

## 📘 Overview

### Scenario Summary

This scenario models a **low‑urgency P2 batch reporting pipeline** that:

- Was previously **slowed or paused** to save cost and carbon during off‑hours.  
- Is now approaching a **hard report delivery deadline** (e.g., daily report due at 09:00 local).  
- Still sees **elevated cost/carbon prices** in the current time slot.  
- Has no CARE, sovereignty, or quality issues.

In this situation:

- The **TemporalRelevance()** component increases sharply as the deadline nears.  
- Cost/energy/carbon remain important but **no longer dominate** decisions.  
- The Autonomy Decider must **switch from slow/pause back to resume** so that the report
  completes **before** the deadline, not just as cheaply as possible.

This scenario shows:

> For P2 pipelines, **deadlines act as a hard floor** on autonomy;  
> off‑hours optimization is allowed **only up to the point where it risks lateness**.

---

## 🧭 Context

### Pipeline Context

- **Pipeline family:** `p2-batch-reporting`  
- **Example member:** `reports/daily-hydro-summary` (synthetic).  
- **Urgency band:** `P2` (low urgency; deadline‑driven).  

**Conceptual behavior:**

- Generates a daily summary report from hydrology pipelines.  
- Targets a delivery SLO such as **“report available by 09:00 local”**.  
- Can run any time between **00:00–09:00**, with flexible scheduling.

**Synthetic SLOs:**

- Delivery:
  - `delivery_deadline_local = 09:00`
  - `max_delivery_slip = 15m` (soft tolerance for lateness, still considered poor).  

- Availability:
  - `>= 0.99` for daily report generation (missing days are serious, but timing is flexible).

**Budgets (synthetic):**

- `monthly_cap_usd = 800`  
- `monthly_cap_kwh = 260`  
- `monthly_cap_kgco2e = 80`  

Compared to P0/P1:

- P2 can **defer work** aggressively when far from deadlines.  
- As deadlines approach, **urgency rises**; autonomy must ensure timely completion.

### Scenario Time Window

- **Scenario instant:** `2025‑04‑18T13:20:00Z` (synthetic; assume 09:20 local with offset).  
- **Deadline:** `2025‑04‑18T14:00:00Z` (synthetic; “09:00 local” equivalent).  
- **Estimated runtime:** ~30 minutes for full daily batch.  

Thus:

- Time to deadline: ~40 minutes.  
- Expected runtime: ~30 minutes.  
- **Buffer is thin**; further slowdowns risk missing SLO.

We assume this pipeline had been in **slow** or **paused** mode earlier in the night to exploit
cheaper/greener periods.

---

## 🧱 Architecture

This section describes the **snapshot → score & gates → decision** chain.

### Snapshot

Representative synthetic snapshot at the decision tick:

- **Deadline & schedule**
  - `time_to_deadline_min`: `40`  
  - `est_runtime_min`: `30`  
  - `time_buffer_min`: `10` (time_to_deadline − est_runtime)  

- **Cost / energy / carbon (per hour, instantaneous)**
  - `cost_usd_hour`: `3.9` (higher daytime cost)  
  - `kwh_hour`: `1.8`  
  - `carbon_kgco2e_hour`: `0.60`  

- **Budget utilization (month‑to‑date)**
  - `cost_budget_utilization`: `0.63` (63%)  
  - `energy_budget_utilization`: `0.59` (59%)  
  - `carbon_budget_utilization`: `0.57` (57%)  

- **Freshness & backlog**
  - `backlog_batches`: `1` (today’s report batch only; no deep backlog).  
  - `last_successful_run_age_h`: `24` (last daily report was yesterday).  

- **Data quality / trust**
  - `data_trust_index`: `0.93`  
  - `recent_test_pass_rate`: `0.96`  
  - `schema_violations_last_24h`: `0`  

- **Governance / CARE**
  - `care_label`: `Synthetic-Batch-Reporting`  
  - `sovereignty_policy`: `synthetic-reporting-generalization-v1`  

Interpretation:

- **Deadline risk** is the main concern.  
- Cost/carbon are non‑negligible but below hard caps.  
- There is no backlog explosion and quality is fine.

### Score & Gates

#### Component Scores (conceptual)

Using a P2‑oriented score function:

- `TemporalRelevance()` is driven by how close we are to the deadline **and**
  how much runtime we need:

  - With time buffer only ~10 minutes, we treat this as **highly urgent**.  
  - Example value: `TemporalRelevance() = 0.90`.

- `FreshnessScore()` is moderate:
  - Not about real‑time freshness, but about **not skipping days**.  
  - Example: `FreshnessScore() = 0.60`.

- `DataTrust()` is high:
  - Example: `DataTrust() = 0.92`.

- `CostBurnRate()`, `EnergyKWhRate()`, `CarbonCO2eRate()` reflect elevated but acceptable
  utilization. For P2, we may “penalize” them more when far from deadlines; near deadlines,
  they retain influence but are not dominant.

  Example normalized pressures:

  - `CostBurnRate() = 0.55`  
  - `EnergyKWhRate() = 0.50`  
  - `CarbonCO2eRate() = 0.50`  

Using example weights for a P2 reporting profile:

~~~text
w_deadline = 0.35   # part of TemporalRelevance()
w_fresh    = 0.20
w_trust    = 0.15
w_cost     = 0.15
w_energy   = 0.08
w_carbon   = 0.07
~~~

Conceptual raw score:

~~~text
S_raw =
  0.35 * 0.90 +      # deadline-heavy TemporalRelevance
  0.20 * 0.60 +
  0.15 * 0.92 -
  0.15 * 0.55 -
  0.08 * 0.50 -
  0.07 * 0.50
≈ 0.61    # synthetic example
~~~

After normalization:

~~~text
S_norm ≈ 0.61    # in or above the resume band for P2
~~~

Example thresholds for P2:

~~~text
resume_up    = 0.55
resume_down  = 0.35
slow_up      = 0.20
slow_down    = 0.00
pause        = -0.20
~~~

So `S_norm ≈ 0.61`:

- Is **above** `resume_up`.  
- Clearly favors **resume**.

#### Gates

Gate outputs (conceptual):

- `care`:
  - `status`: `OK`
  - `reason_code`: `care_clear`

- `cost_energy` (includes carbon):
  - `status`: `WARN` (daytime cost/carbon are elevated)
  - `reason_code`: `peak_cost_window`
  - `details`:
    - `cost_budget_utilization`: `0.63`
    - `carbon_budget_utilization`: `0.57`
    - `peak_window`: true

- `deadline_window` (part of freshness/deadline gate in P2 profile):
  - `status`: `OK`
  - `reason_code`: `deadline_near`
  - `details`:
    - `time_to_deadline_min`: `40`
    - `est_runtime_min`: `30`

- `cardinality_guard`:
  - `status`: `OK`
  - `reason_code`: `cardinality_normal`

There is **no `BLOCK`** and **no `ESCALATE`**.  
Cost/energy WARN indicates “expensive time slot” but must **yield** to deadline urgency
for P2 reporting.

### Decision & Expected Behavior

Given:

- `S_norm ≈ 0.61` > `resume_up`.  
- Deadline near (`deadline_near`) and runtime ~deadline_buffer.  
- No CARE or quality concerns, budgets not violated.  
- Previous action was likely `slow` or `pause` due to off‑hours optimization.

Action logic:

1. Check critical gates:
   - No `ESCALATE` / `BLOCK` ⇒ scoring determines action.  

2. Score band:
   - `S_norm` in **resume band** ⇒ candidate action `resume`.  

3. Deadline policy:
   - If `deadline_near` and `time_to_deadline_min <= est_runtime_min + safety_margin`,
     **force** `resume` unless governance forbids.

Expected decision:

- **Action:** `resume`  
- **State before:** could be `STABLE` (slow) or `PAUSED`.  
- **State after:** `STABLE` (running at full configured batch rate).  

Illustrative reason codes:

- `deadline_near`  
- `score_in_resume_band`  
- `peak_cost_window_but_deadline_priority`  

Operational semantics:

- Orchestrator:

  - Schedules or immediately triggers the daily batch.  
  - Ensures resources are allocated to finish before the deadline.  
  - Records that higher cost/carbon were accepted due to deadline constraints.

- Autonomy telemetry:

  - Logs the decision as **deadline‑driven catch‑up**, not as a standard resume.

---

## 📦 Data & Metadata

### Scenario Metadata (Logical View)

~~~json
{
  "scenario_id": "p2-batch-reporting:deadline-catchup",
  "scenario_status": "canonical",
  "pipeline_id": "p2-batch-reporting",
  "variant": "single-tenant",
  "fixture_ref": "../../fixtures/p2-batch-reporting.jsonl#deadline-catchup",
  "tags": [
    "p2",
    "batch-reporting",
    "deadline",
    "resume",
    "catchup"
  ]
}
~~~

### Fixture Mapping

`fixture_ref` points into:

- `docs/pipelines/autonomy-matrix/examples/scenarios/fixtures/p2-batch-reporting.jsonl#deadline-catchup`

Fixture slice requirements:

- Encodes a window where:

  - Pipeline is near its deadline.  
  - Cost/energy/carbon are moderately high (peak window).  
  - No gate emits `BLOCK` or `ESCALATE`.  

- Includes fields for:

  - `time_to_deadline_min`, `est_runtime_min`, `time_buffer_min`.  
  - `cost_usd_hour`, `kwh_hour`, `carbon_kgco2e_hour`.  
  - Budget utilization and trust metrics.  
  - `expected.action = "resume"`, `expected.state = "STABLE"`.

Offline Simulator can:

- Replay that slice.  
- Confirm the Autonomy Decider chooses `resume`.  
- Show how **deadline pressure overrules off‑hours cost hesitation**.

Graph alignment:

- `:AutonomyScenario { scenario_id: "p2-batch-reporting:deadline-catchup" }`.  
- Linked via:

  - `[:FOR_PIPELINE]` → `:Pipeline { id: "p2-batch-reporting" }`  
  - `[:USES_FIXTURE]` → `:AutonomyFixture { id: "p2-batch-reporting.jsonl#deadline-catchup" }`

---

## 🧪 Validation & CI/CD

This scenario is a **deadline regression guard** for P2 autonomy behavior.

### CI Expectations

Scenario‑level test:

1. Load fixture slice `p2-batch-reporting.jsonl#deadline-catchup`.  
2. Run Autonomy Decider with P2 batch reporting profile and gates.  
3. Assert:

   - `action == "resume"`  
   - `state_after == "STABLE"`  
   - Reason codes include both a deadline indicator and a resume band indicator  
     (e.g., `deadline_near`, `score_in_resume_band`).  
   - Cost/energy WARN is present but **does not** result in `slow` or `pause`.

4. Fail if:

   - Action is `slow` or `pause` when the deadline window requires `resume`.  
   - Action is `escalate` or `pause` without governance justification.  
   - The system remains in a reduced mode and risks missing the deadline.

### Drift Detection

If changes to:

- TemporalRelevance(),  
- Deadline thresholds,  
- Cost/energy/carbon weighting,  
- Gate configurations,

cause this scenario to **stop resuming near deadlines**, CI should flag that:

- Either autonomy policy changed intentionally (docs & fixtures must be updated), or  
- A regression has weakened deadline guarantees for P2 reporting.

---

## 🧠 Story Node & Focus Mode Integration

This scenario serves as a **reference story** for operators asking:

> “Why did the batch report suddenly start running now, even though costs are high?”

Story Node anchor:

~~~text
urn:kfm:story-node:pipelines:autonomy-matrix:examples:scenarios:p2-batch-reporting:deadline-catchup
~~~

Example narrative:

~~~text
In the P2 batch reporting deadline-catchup scenario, a daily report pipeline has been
slowed during off-hours to save cost and carbon. As the 09:00 delivery deadline nears
and only a small time buffer remains, the Autonomy Decider raises TemporalRelevance and
selects a resume action despite the higher cost/carbon of the current time window.
This ensures the report is delivered on time while leaving a traceable governance record
of the trade-off.
~~~

Focus Mode can:

- Compare live P2 reporting behavior to this scenario.  
- Explain when a real decision matches the canonical deadline catch‑up pattern.  
- Point operators to autonomy profile and gate configuration that encode deadline policies.

---

## 🕰️ Version History

| Version    | Date       | Summary                                                                                                          |
|-----------:|------------|------------------------------------------------------------------------------------------------------------------|
| **v11.2.4**| 2025-12-06 | Initial deadline-catchup scenario for `p2-batch-reporting`: snapshot, score & gates, `resume` decision, CI & SN.|

---

<div align="center">

📊 **KFM v11 — P2 Batch Reporting · Deadline Catch‑Up Scenario**  
Deadline‑Aware · Cost‑Conscious · FAIR+CARE‑Aligned Reporting Autonomy  

[📊 P2 Scenario Family](README.md) · [🎭 Scenario Library Root](../README.md) · [🤖 Autonomy Matrix](../../../README.md)

</div>

