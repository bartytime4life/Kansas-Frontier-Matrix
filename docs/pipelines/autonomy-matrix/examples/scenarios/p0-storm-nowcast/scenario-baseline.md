---
title: "⛈️ KFM v11 — P0 Storm Nowcast · Baseline Scenario"
description: "Canonical baseline scenario for a high-urgency P0 storm nowcast pipeline under normal cost, energy, carbon, and CARE conditions in the KFM v11 Autonomy Matrix."
path: "docs/pipelines/autonomy-matrix/examples/scenarios/p0-storm-nowcast/scenario-baseline.md"
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

sbom_ref: "../../../../../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.4/autonomy-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/autonomy-matrix-v1.json"
energy_schema: "../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
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

intent: "autonomy-matrix-scenario-p0-storm-nowcast-baseline"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"

scope:
  domain: "pipelines"
  applies_to:
    - "etl"
    - "ingestion"
    - "ai-inference"
    - "refresh-pipelines"
    - "control-plane-simulation"

semantic_intent:
  - "governance"
  - "control-plane"
  - "reliability"
  - "sustainability"
  - "examples"
  - "simulation"
  - "high-urgency"

category: "Pipelines · Autonomy · Examples · Scenarios · P0 Storm Nowcast"

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
  - "docs/pipelines/autonomy-matrix/examples/scenarios/p0-storm-nowcast/README.md@v11.2.4"
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

json_schema_ref: "schemas/json/docs-pipelines-autonomy-matrix-scenarios-p0-storm-nowcast-baseline-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/docs-pipelines-autonomy-matrix-scenarios-p0-storm-nowcast-baseline-v11.2.4-shape.ttl"

story_node_refs:
  - "urn:kfm:story-node:pipelines:autonomy-matrix:examples:scenarios:p0-storm-nowcast:baseline"

immutability_status: "mutable"

doc_uuid: "urn:kfm:doc:pipelines:autonomy-matrix:examples:scenarios:p0-storm-nowcast:baseline:v11.2.4"
semantic_document_id: "kfm-pipelines-autonomy-matrix-examples-scenarios-p0-storm-nowcast-baseline-v11.2.4"
event_source_id: "ledger:kfm:doc:pipelines:autonomy-matrix:examples:scenarios:p0-storm-nowcast:baseline:v11.2.4"

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
scenario_id: "p0-storm-nowcast:baseline"
scenario_status: "canonical"
pipeline_id: "p0-storm-nowcast"
variant: "single-tenant"
fixture_ref: "../../fixtures/p0-storm-nowcast.jsonl#baseline"
---

<div align="center">

# ⛈️ **KFM v11 — P0 Storm Nowcast · Baseline Scenario**  
`docs/pipelines/autonomy-matrix/examples/scenarios/p0-storm-nowcast/scenario-baseline.md`

**Purpose:**  
Describe the **canonical baseline scenario** for a high‑urgency P0 storm nowcast pipeline  
under normal cost, energy, carbon, and CARE conditions, showing how the Autonomy Decider  
keeps the pipeline in **STABLE + resume** when all signals support full-speed operation.

</div>

---

## 📘 Overview

### Scenario Summary

This scenario represents a **normal operation window** for a fictional P0 storm nowcast pipeline:

- The storm environment is **active**, so temporal relevance is high.  
- Freshness and backlog are **well within SLO** limits.  
- Cost, energy, and carbon usage are **comfortably under** their monthly budgets.  
- Data tests and lineage checks produce a **high trust score**.  
- CARE governance sees no issues; all gates return `OK`.

In this situation, the Autonomy Decider:

- Computes a **strong positive autonomy score**.  
- Sees no hard governance or anomaly gates.  
- Emits a `resume` action.  
- Keeps the state machine in `STABLE`, with no backoff or escalation.

This scenario is used as a **reference point** for other P0 storm scenarios
(carbon clamp, CARE escalation, thrash control).

---

## 🧭 Context

### Pipeline Context

- **Pipeline ID:** `p0-storm-nowcast`  
- **Urgency band:** `P0` (highest; life‑safety / severe weather class).  
- **SLOs (conceptual):**
  - Freshness: `max_lag = 5m` during active storm windows.  
  - Availability: target `>= 0.99` over a 30‑day window.  
- **Budgets (synthetic):**
  - Cost: `monthly_cap_usd = 3_000`.  
  - Energy: `monthly_cap_kwh = 800`.  
  - Carbon: `monthly_cap_kgco2e = 210`.  

### Scenario Time Window

- **Scenario window:** `2025‑04‑10T01:00Z`–`2025‑04‑10T01:05Z` (synthetic).  
- **Storm context:**  
  - Active convective weather; nowcast outputs are time‑critical.  
  - No exceptional governance events.

Scenario is designed so that **all inputs support a “run hot” decision**, subject to
standard cost/energy/carbon and governance checks.

---

## 🧱 Architecture

This section describes the **snapshot → score → gates → decision** chain for the scenario.

### Snapshot

Snapshot values are **synthetic** but internally consistent:

- **Freshness & backlog**
  - `lag_min`: `7` (minutes)  
  - `max_lag_slo`: `10` (minutes, for this period; slightly relaxed from hard 5m)  
  - `backlog_slices`: `4` (recent tiles in queue)  

- **Cost / energy / carbon (per hour, instantaneous)**
  - `cost_usd_hour`: `9.5`  
  - `kwh_hour`: `4.0`  
  - `carbon_kgco2e_hour`: `1.2`  

- **Budget utilization (month‑to‑date)**
  - `cost_budget_utilization`: `0.42` (42%)  
  - `energy_budget_utilization`: `0.38` (38%)  
  - `carbon_budget_utilization`: `0.36` (36%)  

- **Data quality / trust**
  - `data_trust_index`: `0.97` (dimensionless)  
  - `recent_test_pass_rate`: `0.99`  
  - `schema_violations_last_24h`: `0`  

- **Governance / CARE**
  - `care_label`: `Synthetic-Storm-Nowcast`  
  - `sovereignty_policy`: `synthetic-h3-generalization-v1`  

### Score & Gates

#### Component Scores (conceptual)

Using the score‑function design, the components might evaluate to:

- `FreshnessScore()`: `0.92`  
  Freshness is strong: `lag_min` is below `max_lag_slo` with modest backlog.

- `TemporalRelevance()`: `0.98`  
  P0 nowcast during an active window; extremely time‑critical.

- `DataTrust()`: `0.97`  
  Tests and lineage are clean; no recent quality issues.

- `CostBurnRate()`: `0.20`  
  Under budget; mild cost pressure reflected as a small positive (or mild penalty later).

- `EnergyKWhRate()`: `0.18`  
  Under energy budget, similar behavior to cost.

- `CarbonCO2eRate()`: `0.15`  
  Under carbon budget; still tracked but not dominant.

Using these components and weights (example):

~~~text
w_fresh  = 0.35
w_urg    = 0.25
w_trust  = 0.20
w_cost   = 0.10
w_energy = 0.05
w_carbon = 0.05
~~~

a conceptual raw score:

~~~text
S_raw =
  0.35 * 0.92 +
  0.25 * 0.98 +
  0.20 * 0.97 -
  0.10 * 0.20 -
  0.05 * 0.18 -
  0.05 * 0.15
≈ 0.78   (synthetic example)
~~~

After normalization:

~~~text
S_norm ≈ 0.78    # in [-1, 1], squarely in the resume band
~~~

#### Gates

Gate outputs for this scenario (design‑level, conceptual):

- `care`:
  - `status`: `OK`
  - `reason_code`: `care_clear`

- `cost_energy`:
  - `status`: `OK`
  - `reason_code`: `cost_energy_normal`

- `freshness_stall`:
  - `status`: `OK`
  - `reason_code`: `freshness_within_slo`

- `cardinality_guard`:
  - `status`: `OK`
  - `reason_code`: `cardinality_normal`

No gate emits `WARN`, `BLOCK`, or `ESCALATE`.

### Decision & Expected Behavior

Given:

- `S_norm ≈ 0.78` (resume band).  
- Gates all `OK`.  
- Prior state `STABLE`, prior action `resume`.

Action logic (per `action-logic.md`) will:

- Skip governance overrides (no `ESCALATE/BLOCK`).  
- Use thresholds such as:

  - `resume_up = 0.60`  
  - `resume_down = 0.40`  

- Conclude:

  - **Action:** `resume`  
  - **State before:** `STABLE`  
  - **State after:** `STABLE`  
  - **Reason codes (illustrative):**
    - `score_in_resume_band`  
    - `all_gates_ok`  

Expected orchestrator behavior:

- Keep the pipeline running at configured P0 rate, no slowdowns or pauses.  
- Record an `EV_ACTION_ACK` event confirming successful application of `resume`.

---

## 📦 Data & Metadata

### Scenario Metadata (Logical View)

Logical metadata for this scenario:

~~~json
{
  "scenario_id": "p0-storm-nowcast:baseline",
  "scenario_status": "canonical",
  "pipeline_id": "p0-storm-nowcast",
  "variant": "single-tenant",
  "fixture_ref": "../../fixtures/p0-storm-nowcast.jsonl#baseline",
  "tags": [
    "p0",
    "storm-nowcast",
    "baseline",
    "resume",
    "stable"
  ]
}
~~~

### Fixture Mapping

- `fixture_ref` points into:

  - `docs/pipelines/autonomy-matrix/examples/scenarios/fixtures/p0-storm-nowcast.jsonl`  

- The corresponding fixture slice should encode:

  - Time window *≈* `2025‑04‑10T01:00Z`–`2025‑04‑10T01:05Z`.  
  - Metrics aligned with the Snapshot section.  
  - Labels indicating this is the **baseline** scenario segment.

Offline Simulator and CI may:

- Load that fixture.  
- Run the Decider.  
- Compare resulting action/state/reason codes against the expectations in this doc.

---

## 🧪 Validation & CI/CD

This scenario acts as a **regression guard** for P0 autonomy behavior.

### CI Expectations

A minimal CI scenario test should:

1. Load the baseline fixture slice referenced by `fixture_ref`.  
2. Run the Decider with the standard P0 storm nowcast profile and configured gates.  
3. Assert:

   - `action == "resume"`  
   - `state_after == "STABLE"` (or `STABLE` ↔ `IDLE` for specific orchestrator config).  
   - Reason codes include `score_in_resume_band` and `all_gates_ok` (or equivalent).  

4. Fail if:

   - Any gate emits `WARN`, `BLOCK`, or `ESCALATE` for this snapshot.  
   - Action is `slow`, `pause`, or `escalate`.

### Drift Detection

If later changes to:

- Score functions,  
- Thresholds,  
- Gate behaviors,

cause divergence from this scenario, CI should flag:

- Either update to scenario documentation and expectations (intentional change), or  
- A regression in autonomy behavior that needs investigation.

---

## 🧠 Story Node & Focus Mode Integration

This scenario is directly usable as a **Story Node** for Focus Mode:

- Story Node ID:

  ~~~text
  urn:kfm:story-node:pipelines:autonomy-matrix:examples:scenarios:p0-storm-nowcast:baseline
  ~~~

- Example narrative snippet:

  ~~~text
  In the P0 storm nowcast baseline scenario, freshness, urgency, and data trust
  are all high, while cost, energy, and carbon usage are comfortably under budget.
  No governance or anomaly gates fire. The Autonomy Decider keeps the pipeline
  in STABLE with a resume action, running at full configured rate.
  ~~~

Focus Mode may surface this scenario:

- When explaining why a real P0‑like pipeline is currently `resume + STABLE`.  
- As a reference comparison when behavior differs (e.g., when cost/carbon pressure grows).

---

## 🕰️ Version History

| Version    | Date       | Summary                                                                                       |
|-----------:|------------|-----------------------------------------------------------------------------------------------|
| **v11.2.4**| 2025-12-06 | Initial baseline scenario for `p0-storm-nowcast`: snapshot, score & gates, decision, CI usage.|

---

<div align="center">

⛈️ **KFM v11 — P0 Storm Nowcast · Baseline Scenario**  
High‑Urgency · Stable Autonomy · FAIR+CARE‑Aligned Behavior  

[⛈️ P0 Scenario Family](README.md) · [🎭 Scenario Library Root](../README.md) · [🤖 Autonomy Matrix](../../../README.md)

</div>

