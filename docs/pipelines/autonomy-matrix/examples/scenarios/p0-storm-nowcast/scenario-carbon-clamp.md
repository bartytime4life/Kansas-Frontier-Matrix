---
title: "⛈️ KFM v11 — P0 Storm Nowcast · Carbon Clamp Scenario"
description: "P0 storm nowcast scenario where carbon budgets are near hard limits and the Autonomy Decider must trade off urgency and sustainability in the KFM v11 Autonomy Matrix."
path: "docs/pipelines/autonomy-matrix/examples/scenarios/p0-storm-nowcast/scenario-carbon-clamp.md"
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

intent: "autonomy-matrix-scenario-p0-storm-nowcast-carbon-clamp"
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

json_schema_ref: "schemas/json/docs-pipelines-autonomy-matrix-scenarios-p0-storm-nowcast-carbon-clamp-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/docs-pipelines-autonomy-matrix-scenarios-p0-storm-nowcast-carbon-clamp-v11.2.4-shape.ttl"

story_node_refs:
  - "urn:kfm:story-node:pipelines:autonomy-matrix:examples:scenarios:p0-storm-nowcast:carbon-clamp"

immutability_status: "mutable"

doc_uuid: "urn:kfm:doc:pipelines:autonomy-matrix:examples:scenarios:p0-storm-nowcast:carbon-clamp:v11.2.4"
semantic_document_id: "kfm-pipelines-autonomy-matrix-examples-scenarios-p0-storm-nowcast-carbon-clamp-v11.2.4"
event_source_id: "ledger:kfm:doc:pipelines:autonomy-matrix:examples:scenarios:p0-storm-nowcast:carbon-clamp:v11.2.4"

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
scenario_id: "p0-storm-nowcast:carbon-clamp"
scenario_status: "canonical"
pipeline_id: "p0-storm-nowcast"
variant: "single-tenant"
fixture_ref: "../../fixtures/p0-storm-nowcast.jsonl#carbon-clamp"
---

<div align="center">

# ⛈️ **KFM v11 — P0 Storm Nowcast · Carbon Clamp Scenario**  
`docs/pipelines/autonomy-matrix/examples/scenarios/p0-storm-nowcast/scenario-carbon-clamp.md`

**Purpose:**  
Describe a **high‑urgency storm nowcast** scenario where **carbon budgets are near hard limits**,  
and the Autonomy Decider must **temper full‑speed operation** (via `slow`) while still  
respecting P0 urgency, sustainability constraints, and CARE‑aligned governance.

</div>

---

## 📘 Overview

### Scenario Summary

This scenario represents a **P0 storm nowcast** pipeline during an active weather window, where:

- Freshness and urgency are **still high** (storm is ongoing).  
- Data trust remains **excellent**.  
- **Carbon budget utilization is critically high** (approaching target limits for the month).  
- Sustainability policy for P0 pipelines is configured to **bias toward “slow” under carbon pressure**,  
  not immediate `pause`, but also **not** unconditional `resume`.

In this situation, the Autonomy Decider:

- Computes a strong but **slightly reduced** autonomy score compared to the baseline scenario.  
- Receives a **WARN** status from the cost/energy/carbon gate with a carbon‑specific reason code.  
- Emits a `slow` action, keeping the pipeline running but at **reduced intensity** (e.g., fewer grid points,
  lower concurrency, or less frequent runs).  
- Keeps the state machine in `STABLE` but with a “clamped” operating mode.

This scenario acts as a **reference** for how P0 pipelines can participate in carbon stewardship
without compromising storm nowcast availability outright.

---

## 🧭 Context

### Pipeline Context

- **Pipeline ID:** `p0-storm-nowcast`  
- **Urgency band:** `P0` (highest).  
- **SLOs (conceptual):**
  - Freshness: `max_lag = 8m` in this carbon‑clamp policy window.  
  - Availability: `>= 0.99` over 30 days.  
- **Budgets (synthetic):**
  - Cost: `monthly_cap_usd = 3_000`.  
  - Energy: `monthly_cap_kwh = 800`.  
  - Carbon: `monthly_cap_kgco2e = 210`.  

### Scenario Time Window

- **Scenario window:** `2025‑04‑28T03:00Z`–`2025‑04‑28T03:05Z` (synthetic).  
- **Storm context:**
  - Continuing storm activity, but not in the most intense phase.  
  - Some flexibility exists to **slightly reduce** processing intensity.

### Policy Context

The autonomy policy for P0 pipelines is configured to:

- Treat **carbon hard caps** as **global** concerns, but  
- For P0 pipelines:
  - Use `WARN` and `slow` actions when approaching carbon limits,  
  - Reserve `BLOCK` / `pause` for extreme or multi‑gate failure situations.

This scenario is focused on the **WARN + slow** behavior.

---

## 🧱 Architecture

This section shows the **snapshot → score → gates → decision** chain for the carbon‑clamp scenario.

### Snapshot

All values are **synthetic**, tuned to create meaningful pressure:

- **Freshness & backlog**
  - `lag_min`: `6` (minutes)  
  - `max_lag_slo`: `8` (minutes)  
  - `backlog_slices`: `7`  

- **Cost / energy / carbon (per hour, instantaneous)**
  - `cost_usd_hour`: `10.8`  
  - `kwh_hour`: `4.7`  
  - `carbon_kgco2e_hour`: `1.7`  

- **Budget utilization (month‑to‑date)**
  - `cost_budget_utilization`: `0.83` (83%)  
  - `energy_budget_utilization`: `0.79` (79%)  
  - `carbon_budget_utilization`: `0.97` (97%)  

- **Data quality / trust**
  - `data_trust_index`: `0.96`  
  - `recent_test_pass_rate`: `0.98`  
  - `schema_violations_last_24h`: `0`  

- **Governance / CARE**
  - `care_label`: `Synthetic-Storm-Nowcast`  
  - `sovereignty_policy`: `synthetic-h3-generalization-v1`  

### Score & Gates

#### Component Scores (conceptual)

Following the score‑function design, components might evaluate to:

- `FreshnessScore()`: `0.88`  
  Lag is below SLO but closer to the bound than in baseline.

- `TemporalRelevance()`: `0.93`  
  Storm is active, but not peak intensity; still strongly time‑critical.

- `DataTrust()`: `0.95`  
  Data and tests continue to be robust.

- `CostBurnRate()`: `0.30`  
  Cost utilization is higher than baseline, introducing a stronger negative influence.

- `EnergyKWhRate()`: `0.28`  
  Elevated energy utilization.

- `CarbonCO2eRate()`: `0.80`  
  Very high carbon utilization; near the monthly cap.

Using example weights:

~~~text
w_fresh  = 0.35
w_urg    = 0.25
w_trust  = 0.20
w_cost   = 0.10
w_energy = 0.05
w_carbon = 0.05
~~~

conceptual raw score:

~~~text
S_raw =
  0.35 * 0.88 +
  0.25 * 0.93 +
  0.20 * 0.95 -
  0.10 * 0.30 -
  0.05 * 0.28 -
  0.05 * 0.80
≈ 0.49    # synthetic example
~~~

After normalization:

~~~text
S_norm ≈ 0.49    # between slow band and resume band, sensitive to thresholds
~~~

Illustrative thresholds (from pipeline autonomy profile):

~~~text
resume_up    = 0.60
resume_down  = 0.40
slow_up      = 0.30
slow_down    = 0.10
pause        = -0.10
~~~

#### Gates

Gate outputs for this snapshot (conceptual design):

- `care`:
  - `status`: `OK`
  - `reason_code`: `care_clear`

- `cost_energy` (here including carbon utilization):
  - `status`: `WARN`
  - `reason_code`: `carbon_budget_high`
  - `details` (conceptual):
    - `carbon_budget_utilization`: `0.97`
    - `carbon_policy_mode`: `p0-warn-slow`

- `freshness_stall`:
  - `status`: `OK`
  - `reason_code`: `freshness_within_slo`

- `cardinality_guard`:
  - `status`: `OK`
  - `reason_code`: `cardinality_normal`

No gate emits `BLOCK` or `ESCALATE`, but the **WARN** from cost/energy/carbon
is expected to **bias away from full `resume`**.

### Decision & Expected Behavior

Given:

- `S_norm ≈ 0.49`.  
- Carbon‑driven `WARN` on cost_energy gate.  
- Prior state `STABLE`, prior action `resume`.

Action logic (per `action-logic.md`) will:

- Check for hard governance first:
  - No `ESCALATE`, no `BLOCK` ⇒ proceed to score‑based mapping.  

- Consider thresholds and WARN bias:
  - `S_norm` is **below** `resume_up` (`0.60`) and slightly **above** `resume_down` (`0.40`).  
  - With no WARN, we might remain in `resume` due to hysteresis.  
  - With a **carbon WARN**, policy biases toward `slow`.

Expected decision:

- **Action:** `slow`  
- **State before:** `STABLE`  
- **State after:** `STABLE` (or `STABLE` with a “clamped” annotation in telemetry)  
- **Reason codes (illustrative):**
  - `carbon_budget_high`  
  - `score_in_slow_band`  

Operational semantics (per pipeline profiles and orchestrator contracts):

- **Concurrency or workload reduction**, e.g.:
  - Lower spatial resolution or fewer ensemble members.  
  - Slightly reduced run frequency where latency allows.  

- **No full pause**, ensuring P0 storm nowcast is still available, but with controlled carbon impact.

---

## 📦 Data & Metadata

### Scenario Metadata (Logical View)

Logical scenario metadata:

~~~json
{
  "scenario_id": "p0-storm-nowcast:carbon-clamp",
  "scenario_status": "canonical",
  "pipeline_id": "p0-storm-nowcast",
  "variant": "single-tenant",
  "fixture_ref": "../../fixtures/p0-storm-nowcast.jsonl#carbon-clamp",
  "tags": [
    "p0",
    "storm-nowcast",
    "carbon-clamp",
    "slow",
    "sustainability"
  ]
}
~~~

### Fixture Mapping

- `fixture_ref` points into:

  - `docs/pipelines/autonomy-matrix/examples/scenarios/fixtures/p0-storm-nowcast.jsonl`  

The fixture slice should:

- Encode the **time window** near `2025‑04‑28T03:00Z`.  
- Use metrics aligned with the Snapshot section (within reasonable tolerance).  
- Include labels or metadata identifying this slice as `carbon-clamp`.

Offline Simulator and CI can:

- Load this fixture slice.  
- Run the Decider.  
- Verify that outputs match the expected `slow` action and reason codes.

---

## 🧪 Validation & CI/CD

This scenario is a **sustainability regression guard** for P0 pipelines.

### CI Expectations

A scenario‑level CI test should:

1. Load the carbon‑clamp fixture slice.  
2. Run the Autonomy Decider with the standard P0 storm nowcast profile and configured gates.  
3. Assert:

   - `action == "slow"`  
   - `state_after` remains `STABLE` (or equivalent “stable with clamp” state).  
   - Reason codes include at least `carbon_budget_high` and `score_in_slow_band` (or their canonical equivalents).  

4. Fail if:

   - A `BLOCK` or `ESCALATE` is emitted by gates under this policy.  
   - Action is `resume` (ignoring carbon pressure) or `pause` (over‑reacting).

### Drift Detection

If changes to:

- Score weights,  
- Normalization behavior,  
- Carbon budget policy,  
- Gate logic,

cause divergence from this scenario’s expectations, CI should flag them as:

- Intentional policy re‑design (and the scenario must be updated), or  
- Regression that weakens P0 sustainability behavior.

---

## 🧠 Story Node & Focus Mode Integration

This carbon‑clamp scenario is designed to be surfaced in Focus Mode when:

- A real P0‑like pipeline is slowed due to carbon pressure.  
- Operators ask “Why is the storm nowcast slowed instead of fully resumed?”  

Story Node ID:

~~~text
urn:kfm:story-node:pipelines:autonomy-matrix:examples:scenarios:p0-storm-nowcast:carbon-clamp
~~~

Example narrative:

~~~text
In the P0 storm nowcast carbon-clamp scenario, the pipeline remains highly urgent
and data quality is strong, but monthly carbon utilization climbs to 97% of the
budget. The carbon-aware gate raises a WARN, and the Autonomy Decider responds
with a slow action instead of full resume, reducing workload while preserving
life-safety nowcast coverage.
~~~

Focus Mode can:

- Compare real‑time telemetry with this scenario.  
- Explain why `slow` is appropriate given carbon pressure and configured policy.  
- Highlight that a full pause is reserved for more extreme or multi‑gate issues.

---

## 🕰️ Version History

| Version    | Date       | Summary                                                                                                    |
|-----------:|------------|------------------------------------------------------------------------------------------------------------|
| **v11.2.4**| 2025-12-06 | Initial carbon‑clamp scenario for `p0-storm-nowcast`: snapshot, score/gates, `slow` decision, CI & SN use. |

---

<div align="center">

⛈️ **KFM v11 — P0 Storm Nowcast · Carbon Clamp Scenario**  
High‑Urgency · Carbon‑Aware Autonomy · FAIR+CARE‑Aligned Sustainability Trade‑Offs  

[⛈️ P0 Scenario Family](README.md) · [🎭 Scenario Library Root](../README.md) · [🤖 Autonomy Matrix](../../../README.md)

</div>

