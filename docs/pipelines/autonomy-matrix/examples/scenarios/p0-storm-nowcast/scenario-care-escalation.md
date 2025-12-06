---
title: "⛈️ KFM v11 — P0 Storm Nowcast · CARE Escalation Scenario"
description: "P0 storm nowcast scenario where a CARE/sovereignty governance issue forces escalation regardless of positive autonomy score in the KFM v11 Autonomy Matrix."
path: "docs/pipelines/autonomy-matrix/examples/scenarios/p0-storm-nowcast/scenario-care-escalation.md"
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

intent: "autonomy-matrix-scenario-p0-storm-nowcast-care-escalation"
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
  - "docs/pipelines/autonomy-matrix/decider/contracts.md@v11.2.4"
  - "docs/pipelines/autonomy-matrix/decider/action-logic.md@v11.2.4"
  - "docs/pipelines/autonomy-matrix/decider/designs/state-machine.md@v11.2.4"
  - "docs/pipelines/autonomy-matrix/README.md@v11.2.3"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/docs-pipelines-autonomy-matrix-scenarios-p0-storm-nowcast-care-escalation-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/docs-pipelines-autonomy-matrix-scenarios-p0-storm-nowcast-care-escalation-v11.2.4-shape.ttl"

story_node_refs:
  - "urn:kfm:story-node:pipelines:autonomy-matrix:examples:scenarios:p0-storm-nowcast:care-escalation"

immutability_status: "mutable"

doc_uuid: "urn:kfm:doc:pipelines:autonomy-matrix:examples:scenarios:p0-storm-nowcast:care-escalation:v11.2.4"
semantic_document_id: "kfm-pipelines-autonomy-matrix-examples-scenarios-p0-storm-nowcast-care-escalation-v11.2.4"
event_source_id: "ledger:kfm:doc:pipelines:autonomy-matrix:examples:scenarios:p0-storm-nowcast:care-escalation:v11.2.4"

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
scenario_id: "p0-storm-nowcast:care-escalation"
scenario_status: "canonical"
pipeline_id: "p0-storm-nowcast"
variant: "single-tenant"
fixture_ref: "../../fixtures/p0-storm-nowcast.jsonl#care-escalation"
---

<div align="center">

# ⛈️ **KFM v11 — P0 Storm Nowcast · CARE Escalation Scenario**  
`docs/pipelines/autonomy-matrix/examples/scenarios/p0-storm-nowcast/scenario-care-escalation.md`

**Purpose:**  
Describe a **P0 storm nowcast** scenario where a **CARE / sovereignty governance issue**  
forces the Autonomy Decider to **escalate** (and potentially pause) regardless of  
otherwise favorable score, demonstrating **gate precedence over numeric scoring**.

</div>

---

## 📘 Overview

### Scenario Summary

This scenario models a high‑urgency P0 storm nowcast pipeline where:

- Freshness, urgency, and data trust are **strong**.  
- Cost, energy, and carbon are **within acceptable ranges**.  
- However, an upstream governance issue (e.g., synthetic stand‑in for a real‑world
  sovereignty / sensitive‑location concern) causes the **CARE gate to emit `ESCALATE`**.

In this situation, the Autonomy Decider:

- Computes a **positive autonomy score** that would normally support `resume`.  
- Sees a **hard governance signal** from the CARE gate (`status = ESCALATE`).  
- Emits an **`escalate` action**, regardless of score, and transitions the pipeline
  from `STABLE` to `ESCALATED` state in the state machine.

This scenario is the canonical example of:

> **Governance over numbers** — when CARE/Sovereignty says “escalate”,  
> autonomy must escalate even if telemetry looks healthy.

---

## 🧭 Context

### Pipeline Context

- **Pipeline ID:** `p0-storm-nowcast`  
- **Urgency band:** `P0` (life‑safety / severe weather).  
- **SLOs (conceptual):**
  - Freshness: `max_lag = 5m` in active windows.  
  - Availability: `>= 0.99` over 30 days.  

### Scenario Time Window

- **Scenario window:** `2025‑05‑02T02:00Z`–`2025‑05‑02T02:05Z` (synthetic).  
- **Storm context:**  
  - Active storm cell near sensitive locations.  
  - Outputs are time‑critical, but governance review is required because of how data
    for this scenario is modeled.

### Governance Context (Synthetic Stand‑In)

To keep the scenario safe and synthetic:

- We assume that **if this were real data**, it would involve locations and attributes
  governed by **Indigenous data sovereignty or similar CARE policies**.  
- The CARE gate is configured to treat this combination of attributes as **“requires
  human review before automated release”**.

Thus:

- From the Autonomy Matrix perspective, this appears as a synthetic condition that
  **always triggers `ESCALATE`** for this snapshot.

---

## 🧱 Architecture

This section shows the **snapshot → score → gates → decision** chain under CARE escalation.

### Snapshot

All values are synthetic, chosen to make the governance effect clear:

- **Freshness & backlog**
  - `lag_min`: `3` (minutes)  
  - `max_lag_slo`: `5` (minutes)  
  - `backlog_slices`: `3`  

- **Cost / energy / carbon (per hour, instantaneous)**
  - `cost_usd_hour`: `9.1`  
  - `kwh_hour`: `3.9`  
  - `carbon_kgco2e_hour`: `1.1`  

- **Budget utilization (month‑to‑date)**
  - `cost_budget_utilization`: `0.40` (40%)  
  - `energy_budget_utilization`: `0.35` (35%)  
  - `carbon_budget_utilization`: `0.33` (33%)  

- **Data quality / trust**
  - `data_trust_index`: `0.96`  
  - `recent_test_pass_rate`: `0.98`  
  - `schema_violations_last_24h`: `0`  

- **Governance / CARE (synthetic)**
  - `care_label`: `Synthetic-Storm-Nowcast`  
  - `sovereignty_policy`: `synthetic-h3-sensitive-window-v1`  
  - `governance_context`: synthetic stand‑in for “requires sovereignty review”.

### Score & Gates

#### Component Scores (conceptual)

Using the score‑function design, components might evaluate to:

- `FreshnessScore()`: `0.95`  
- `TemporalRelevance()`: `0.98`  
- `DataTrust()`: `0.95`  
- `CostBurnRate()`: `0.18`  
- `EnergyKWhRate()`: `0.15`  
- `CarbonCO2eRate()`: `0.12`  

With example weights:

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
  0.35 * 0.95 +
  0.25 * 0.98 +
  0.20 * 0.95 -
  0.10 * 0.18 -
  0.05 * 0.15 -
  0.05 * 0.12
≈ 0.82    # synthetic example
~~~

After normalization:

~~~text
S_norm ≈ 0.82    # clearly in the resume band numerically
~~~

If we looked **only at score**, we would almost certainly choose `resume`.

#### Gates

Gate outputs for this snapshot (conceptual):

- `care`:
  - `status`: `ESCALATE`
  - `reason_code`: `care_requires_human_review`
  - `details` (synthetic):
    - `trigger`: `sovereignty_sensitive_context`
    - `policy`: `sovereignty-escalate-v1`

- `cost_energy`:
  - `status`: `OK`
  - `reason_code`: `cost_energy_normal`

- `freshness_stall`:
  - `status`: `OK`
  - `reason_code`: `freshness_within_slo`

- `cardinality_guard`:
  - `status`: `OK`
  - `reason_code`: `cardinality_normal`

Critically:

- **CARE gate status = `ESCALATE`**, which must dominate the decision regardless of `S_norm`.

### Decision & Expected Behavior

Given:

- `S_norm ≈ 0.82` (strongly “resume”).  
- CARE gate `status = ESCALATE`.  
- Prior state `STABLE`, prior action `resume`.

Per `action-logic.md`, gate precedence is:

1. If any critical gate emits `ESCALATE` ⇒ `action = escalate`.  
2. Else if any critical gate emits `BLOCK` ⇒ `action = pause`.  
3. Else proceed to score‑based mapping.

So the Autonomy Decider will:

- Ignore the numeric “resume” suggestion.  
- Emit:

  - **Action:** `escalate`  
  - **State before:** `STABLE`  
  - **State after:** `ESCALATED`  

- **Reason codes (illustrative):**
  - `care_requires_human_review`  
  - `gate_precedence_over_score`

Operational expectations:

- Orchestrator:

  - Does **not** automatically change run state unless policy says to.  
  - Creates/updates a **human escalation artifact** (ticket, page, etc.).  
  - Surfaces CARE gate details to reviewers.

- Human reviewers:

  - Decide whether to continue, slow, or pause runs in light of governance context.  
  - May override or update autonomy policy for future similar conditions.

---

## 📦 Data & Metadata

### Scenario Metadata (Logical View)

~~~json
{
  "scenario_id": "p0-storm-nowcast:care-escalation",
  "scenario_status": "canonical",
  "pipeline_id": "p0-storm-nowcast",
  "variant": "single-tenant",
  "fixture_ref": "../../fixtures/p0-storm-nowcast.jsonl#care-escalation",
  "tags": [
    "p0",
    "storm-nowcast",
    "care-escalation",
    "governance",
    "escalate"
  ]
}
~~~

### Fixture Mapping

- `fixture_ref` points into:

  - `docs/pipelines/autonomy-matrix/examples/scenarios/fixtures/p0-storm-nowcast.jsonl`  

Fixture slice requirements:

- Encodes telemetry consistent with the Snapshot section.  
- Includes synthetic governance markers that cause the **CARE gate to emit `ESCALATE`**.  
- Is labeled or otherwise identifiable as the `care-escalation` slice.

Offline Simulator and CI can:

- Load the fixture slice.  
- Run the Autonomy Decider.  
- Verify that `action == "escalate"` and the state transition matches expectations.

Graph alignment:

- Scenario appears as an `:AutonomyScenario` node linked to:
  - `:Pipeline` (`p0-storm-nowcast`),  
  - `:AutonomyFixture` (care‑escalation slice),  
  - Governance policy nodes (CARE and sovereignty policies).

---

## 🧪 Validation & CI/CD

This scenario is a **governance regression guard** for P0 pipelines.

### CI Expectations

A scenario‑level CI test should:

1. Load the `care-escalation` fixture slice.  
2. Run the Autonomy Decider with the standard P0 storm nowcast profile and configured gates.  
3. Assert:

   - `action == "escalate"`  
   - `state_after == "ESCALATED"` (per state‑machine spec).  
   - CARE gate `status == "ESCALATE"`.  
   - Reason codes include `care_requires_human_review` (or canonical equivalent).  

4. Fail if:

   - Score‑based logic overrides CARE escalation (e.g., `action == "resume"`).  
   - CARE gate fails to emit `ESCALATE` under fixture conditions.  
   - State machine does not enter `ESCALATED` when an escalate action is emitted.

### Drift Detection

If changes to:

- CARE policy configuration,  
- Gate implementation,  
- Action logic gate precedence,

cause divergence from this scenario, CI should mark:

- Intentional policy change (requiring scenario update and governance sign‑off), or  
- Regression that weakens CARE governance precedence.

---

## 🧠 Story Node & Focus Mode Integration

This scenario is designed to be surfaced in Focus Mode whenever:

- A real P0‑like pipeline is under **CARE‑driven escalation**, or  
- Operators ask “Why are we escalated instead of just resuming, when metrics look fine?”.

Story Node ID:

~~~text
urn:kfm:story-node:pipelines:autonomy-matrix:examples:scenarios:p0-storm-nowcast:care-escalation
~~~

Example narrative:

~~~text
In the P0 storm nowcast CARE-escalation scenario, freshness, urgency, and data quality
are all strong, and cost, energy, and carbon usage remain within budget. However, the
CARE gate detects a sovereignty-sensitive context and emits an ESCALATE status.
According to Autonomy Matrix policy, this overrides the positive autonomy score and the
Decider issues an escalate action, moving the pipeline into ESCALATED state for human review.
~~~

Focus Mode can:

- Compare real‑time conditions to this scenario.  
- Explain that **governance, not metrics, is driving escalation**.  
- Provide operators links to relevant governance docs and CARE policies.

---

## 🕰️ Version History

| Version    | Date       | Summary                                                                                                          |
|-----------:|------------|------------------------------------------------------------------------------------------------------------------|
| **v11.2.4**| 2025-12-06 | Initial CARE escalation scenario for `p0-storm-nowcast`: snapshot, score vs gates, `escalate` decision, CI & SN. |

---

<div align="center">

⛈️ **KFM v11 — P0 Storm Nowcast · CARE Escalation Scenario**  
Governance‑First · CARE‑Aligned · Deterministic Escalation  

[⛈️ P0 Scenario Family](README.md) · [🎭 Scenario Library Root](../README.md) · [🤖 Autonomy Matrix](../../../README.md)

</div>

