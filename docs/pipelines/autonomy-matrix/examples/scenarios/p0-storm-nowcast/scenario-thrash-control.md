---
title: "⛈️ KFM v11 — P0 Storm Nowcast · Thrash Control Scenario"
description: "P0 storm nowcast scenario where noisy telemetry near thresholds would cause action thrash, but hysteresis and BACKOFF logic keep autonomy behavior stable in the KFM v11 Autonomy Matrix."
path: "docs/pipelines/autonomy-matrix/examples/scenarios/p0-storm-nowcast/scenario-thrash-control.md"
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

intent: "autonomy-matrix-scenario-p0-storm-nowcast-thrash-control"
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

json_schema_ref: "schemas/json/docs-pipelines-autonomy-matrix-scenarios-p0-storm-nowcast-thrash-control-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/docs-pipelines-autonomy-matrix-scenarios-p0-storm-nowcast-thrash-control-v11.2.4-shape.ttl"

story_node_refs:
  - "urn:kfm:story-node:pipelines:autonomy-matrix:examples:scenarios:p0-storm-nowcast:thrash-control"

immutability_status: "mutable"

doc_uuid: "urn:kfm:doc:pipelines:autonomy-matrix:examples:scenarios:p0-storm-nowcast:thrash-control:v11.2.4"
semantic_document_id: "kfm-pipelines-autonomy-matrix-examples-scenarios-p0-storm-nowcast-thrash-control-v11.2.4"
event_source_id: "ledger:kfm:doc:pipelines:autonomy-matrix:examples:scenarios:p0-storm-nowcast:thrash-control:v11.2.4"

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
scenario_id: "p0-storm-nowcast:thrash-control"
scenario_status: "canonical"
pipeline_id: "p0-storm-nowcast"
variant: "single-tenant"
fixture_ref: "../../fixtures/p0-storm-nowcast.jsonl#thrash-control"
---

<div align="center">

# ⛈️ **KFM v11 — P0 Storm Nowcast · Thrash Control Scenario**  
`docs/pipelines/autonomy-matrix/examples/scenarios/p0-storm-nowcast/scenario-thrash-control.md`

**Purpose:**  
Describe a **P0 storm nowcast** scenario where **noisy telemetry near thresholds**  
would cause rapid flipping between `resume` and `slow`, but **hysteresis + BACKOFF**  
keep autonomy behavior **stable and explainable** in the KFM v11 Autonomy Matrix.

</div>

---

## 📘 Overview

### Scenario Summary

This scenario models a P0 storm nowcast pipeline where:

- The storm is active and **urgency remains high**.  
- Freshness lags and cost/energy/carbon metrics **bounce around score thresholds**.  
- If the Autonomy Decider reacted naïvely to every tick, it would **thrash**:
  - `resume → slow → resume → slow…` in short intervals.

Instead, the Autonomy Matrix:

- Detects **frequent action flips** as a sign of instability.  
- Moves the pipeline into a **BACKOFF state** (per the state‑machine design),  
  temporarily rate‑limiting evaluations.  
- Uses hysteresis and prior actions to **smooth behavior** and converge on a stable action.  

This scenario is the canonical example of:

> **Stability over twitchiness** — autonomy must remain predictable under noisy signals.

---

## 🧭 Context

### Pipeline Context

- **Pipeline ID:** `p0-storm-nowcast`  
- **Urgency band:** `P0` (highest urgency).  
- **SLOs (conceptual):**
  - Freshness: `max_lag = 6m` in this window.  
  - Availability: `>= 0.99` over 30 days.  

- **Budgets (synthetic):**
  - Cost: `monthly_cap_usd = 3_000`.  
  - Energy: `monthly_cap_kwh = 800`.  
  - Carbon: `monthly_cap_kgco2e = 210`.  

### Scenario Time Window

- **Scenario window:** `2025‑05‑05T01:00Z`–`2025‑05‑05T01:20Z` (synthetic).  
- **Storm context:**
  - Storm intensity is changing; a mix of strong and decaying cells.  
  - Telemetry for lag and cost is **noisy** (e.g., due to elastic scaling, cache effects).

This scenario is used to test:

- **Action logic stability** near band edges.  
- **State machine BACKOFF** behavior under thrash.  
- Offline Simulator’s ability to replay and visualize the stabilization process.

---

## 🧱 Architecture

This section describes how the system behaves over a short sequence of ticks.

### Snapshot Series (Conceptual)

We consider a simplified set of evaluation ticks (one tick per ~2 minutes).  
Values are synthetic and approximate.

| Tick | Time (Z)          | lag_min | cost_usd_hour | S_norm (approx) | Notes                          |
|------|-------------------|--------:|--------------:|----------------:|--------------------------------|
| T0   | 01:00             | 4.0     | 9.5           | 0.74            | Clean conditions               |
| T1   | 01:02             | 5.5     | 10.4          | 0.58            | Slight lag & cost uptick      |
| T2   | 01:04             | 6.2     | 11.0          | 0.45            | Drift down toward slow band   |
| T3   | 01:06             | 4.8     | 9.8           | 0.63            | Jump back into resume band    |
| T4   | 01:08             | 6.5     | 10.9          | 0.46            | Back toward slow band         |
| T5   | 01:10             | 5.0     | 10.2          | 0.60            | Near top of slow/resume edge  |
| T6   | 01:12–01:20 (avg) | 5.3     | 10.1          | 0.55 (smoothed) | Stabilized mid‑band behavior  |

Assume example thresholds from the autonomy profile:

~~~text
resume_up    = 0.60
resume_down  = 0.40
slow_up      = 0.30
slow_down    = 0.10
pause        = -0.10
~~~

### Gate Behavior

Throughout this scenario:

- `care`: `OK` → no governance escalation.  
- `cost_energy`: mostly `OK`, occasionally `WARN` when cost blips up, but never `BLOCK`.  
- `freshness_stall`: `OK` → no hard stall.  
- `cardinality_guard`: `OK`.

So **no `BLOCK` or `ESCALATE`**, meaning:

- Gates do **not** force `pause` or `escalate`.  
- The main issue is **score‑driven thrash** between `resume` and `slow`.

### Action & State Evolution

Conceptual evolution (simplified):

| Tick | State before | Previous action | S_norm | Naïve action | Actual action | State after   | Notes                               |
|------|--------------|-----------------|--------|-------------:|--------------:|--------------|-------------------------------------|
| T0   | STABLE       | resume          | 0.74   | resume       | resume        | STABLE       | Clearly resume                      |
| T1   | STABLE       | resume          | 0.58   | resume       | resume        | STABLE       | Still above `resume_down`           |
| T2   | STABLE       | resume          | 0.45   | slow         | slow          | STABLE       | Crossed into “slow‑leaning” band    |
| T3   | STABLE       | slow            | 0.63   | resume       | resume        | STABLE       | Score bounce → flips back to resume |
| T4   | STABLE       | resume          | 0.46   | slow         | slow          | STABLE       | Flip again → resume → slow          |
| T5   | STABLE       | slow            | 0.60   | resume       | slow          | BACKOFF      | Thrash detected → lock into BACKOFF |
| T6   | BACKOFF      | slow            | 0.55   | resume/slow? | slow          | STABLE       | BACKOFF cooldown ends; stay slow    |

Notes:

- **Naïve action**: what action logic would choose if it ignored thrash/backoff detection.  
- **Actual action**: what the Decider emits under the thrash control design.  

Once the system detects a **pattern of rapid flips** (e.g., resume → slow → resume → slow
over a short time), it:

1. Enters **BACKOFF** at T5.  
2. During BACKOFF:
   - **Rate‑limits evaluations** (e.g., checks every few ticks / minutes).  
   - Uses smoothed scores (`S_norm` ≈ 0.55 over T6) and prior actions.  
3. Exits BACKOFF back to **STABLE** with a **single chosen action** (`slow`) until  
   naturally pulled back into `resume` by more sustained improvements.

This matches the state‑machine design where BACKOFF exists explicitly to:

- Protect against noisy conditions.  
- Prevent rapid state/action oscillation.  
- Maintain predictability for consuming orchestrators and operators.

---

## 📦 Data & Metadata

### Scenario Metadata (Logical View)

~~~json
{
  "scenario_id": "p0-storm-nowcast:thrash-control",
  "scenario_status": "canonical",
  "pipeline_id": "p0-storm-nowcast",
  "variant": "single-tenant",
  "fixture_ref": "../../fixtures/p0-storm-nowcast.jsonl#thrash-control",
  "tags": [
    "p0",
    "storm-nowcast",
    "thrash-control",
    "backoff",
    "hysteresis"
  ]
}
~~~

### Fixture Mapping

- `fixture_ref` points into:

  - `docs/pipelines/autonomy-matrix/examples/scenarios/fixtures/p0-storm-nowcast.jsonl`

The fixture slice for `thrash-control` should:

- Encode a short time window (e.g., 20 minutes) with:

  - Score‑relevant telemetry (lag, cost, energy, carbon) **oscillating near thresholds**.  
  - No CARE or hard cost/energy/carbon violations.  

- Include a label or metadata entry indicating `scenario = "thrash-control"`.

Offline Simulator can:

- Replay the fixture slice.  
- Log score (`S_norm`), actions, and states per tick.  
- Confirm that after brief oscillation, the system:

  - Enters `BACKOFF`,  
  - Then stabilizes on a single action (`slow` in this scenario) when it returns to `STABLE`.

Graph alignment:

- Scenario node `:AutonomyScenario` connects to:

  - `:Pipeline` (`p0-storm-nowcast`),  
  - `:AutonomyFixture` (thrash-control slice),  
  - Design docs for state machine and action logic.

---

## 🧪 Validation & CI/CD

This scenario is a **stability regression guard**.

### CI Expectations

A scenario‑level CI test should:

1. Load the `thrash-control` fixture.  
2. Run the Decider with:

   - Standard P0 storm nowcast profile.  
   - Hysteresis and BACKOFF configurations from state‑machine and action‑logic specs.

3. Assert that:

   - There are **no long‑term action oscillations** after BACKOFF engages.  
   - The number of action flips over the window is **below** a configured threshold.  
   - State machine visits `BACKOFF` at least once when thrash is detected.  
   - The system returns to `STABLE` with a **single dominant action** (`slow` here).

4. Fail if:

   - Actions continue flipping at nearly every tick.  
   - BACKOFF is never used even with repeated resume/slow flips.  
   - The final state remains in `BACKOFF` or an unstable looping pattern.

### Drift Detection

If changes to:

- Thresholds or hysteresis behavior,  
- BACKOFF entry/exit rules,  
- Score smoothing / windows,

cause this scenario to:

- Stop using BACKOFF when it should, or  
- Produce excessive action flips,

CI should flag the behavior as either:

- Intentional change (requiring scenario update and appropriate governance review), or  
- Regression in thrash control.

---

## 🧠 Story Node & Focus Mode Integration

This scenario is a **teaching example** for Focus Mode when operators see “weird” behavior near thresholds.

Story Node ID:

~~~text
urn:kfm:story-node:pipelines:autonomy-matrix:examples:scenarios:p0-storm-nowcast:thrash-control
~~~

Example narrative:

~~~text
In the P0 storm nowcast thrash-control scenario, score and telemetry oscillate near the
resume/slow thresholds. Instead of flipping actions on every tick, the Autonomy Decider
detects repeated flips, enters BACKOFF, and rate-limits evaluations. After observing a
smoothed score around the slow band, it returns to STABLE with a consistent slow action,
keeping behavior predictable for operators and orchestrators.
~~~

Focus Mode can:

- Compare real‑time action and state transitions to this scenario.  
- Explain why BACKOFF appears and how it prevents thrash.  
- Point operators to configuration parameters (thresholds, windows) that influence stability.

---

## 🕰️ Version History

| Version    | Date       | Summary                                                                                                                 |
|-----------:|------------|-------------------------------------------------------------------------------------------------------------------------|
| **v11.2.4**| 2025-12-06 | Initial thrash‑control scenario for `p0-storm-nowcast`: noisy threshold behavior, BACKOFF usage, stability CI guardrail.|

---

<div align="center">

⛈️ **KFM v11 — P0 Storm Nowcast · Thrash Control Scenario**  
Noisy Metrics · Stable Autonomy · BACKOFF‑Driven Thrash Protection  

[⛈️ P0 Scenario Family](README.md) · [🎭 Scenario Library Root](../README.md) · [🤖 Autonomy Matrix](../../../README.md)

</div>
