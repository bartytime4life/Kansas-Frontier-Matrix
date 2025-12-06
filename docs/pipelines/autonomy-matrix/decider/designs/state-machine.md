---
title: "🧠 KFM v11 — Autonomy Decider State Machine"
description: "Canonical state-machine design for the KFM v11 Autonomy Decider, defining states, events, and transitions for deterministic, explainable pipeline autonomy."
path: "docs/pipelines/autonomy-matrix/decider/designs/state-machine.md"
version: "v11.2.4"
last_updated: "2025-12-05"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability · Sustainability · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "Aligned with Autonomy Matrix v11.2.x (design-only; non-normative)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.4/autonomy-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/autonomy-matrix-v1.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

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
doc_kind: "Architecture"
header_profile: "standard"
footer_profile: "standard"

intent: "autonomy-matrix-decider-state-machine"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"

scope:
  domain: "pipelines"
  applies_to:
    - "control-plane"
    - "etl"
    - "ingestion"
    - "ai-inference"
    - "ai-training"
    - "refresh-pipelines"

semantic_intent:
  - "governance"
  - "control-plane"
  - "reliability"
  - "sustainability"
  - "architecture"
  - "formal-spec"

category: "Pipelines · Autonomy · Governance · Architecture · State Machine"

sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Internal"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: false

data_steward: "Reliability · Sustainability · FAIR+CARE Council"
ttl_policy: "Indefinite (subject to architecture changes)"
sunset_policy: "Supersede when Autonomy Matrix v12 decider state-machine spec is adopted"

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
  - "docs/pipelines/autonomy-matrix/decider/designs/README.md@v11.2.4"
  - "docs/pipelines/autonomy-matrix/decider/README.md@v11.2.4"
  - "docs/pipelines/autonomy-matrix/README.md@v11.2.3"
  - "docs/pipelines/reliability/README.md"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/docs-pipelines-autonomy-decider-state-machine-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/docs-pipelines-autonomy-decider-state-machine-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "mutable"

doc_uuid: "urn:kfm:doc:pipelines:autonomy-matrix:decider:designs:state-machine:v11.2.4"
semantic_document_id: "kfm-pipelines-autonomy-matrix-decider-state-machine-v11.2.4"
event_source_id: "ledger:kfm:doc:pipelines:autonomy-matrix:decider:designs:state-machine:v11.2.4"

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
    - "🗺️ Diagrams"
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
---

<div align="center">

# 🧠 **KFM v11 — Autonomy Decider State Machine**  
`docs/pipelines/autonomy-matrix/decider/designs/state-machine.md`

**Purpose:**  
Define the **canonical state machine** for the Autonomy Decider, including states, events, and transitions  
for per-pipeline autonomy decisions. This design ensures the decider remains **deterministic, explainable,  
and governance-safe** across single-tenant, multi-tenant, and offline-simulator variants.

</div>

---

## 📘 Overview

This document specifies the **state-level behavior** of the Autonomy Decider:

- Identifies the **states** a pipeline can occupy in the control plane (e.g., `IDLE`, `EVALUATING`, `PAUSED`).  
- Defines the **events** (telemetry updates, gates, human overrides) that cause transitions.  
- Describes **transition rules and invariants** that must hold across all implementations:
  - No action without a valid state.  
  - No “teleporting” between incompatible states.  
  - All transitions are **config- and event-driven**, not ad-hoc.

This state-machine design is:

- **Non-normative** for now (design baseline) but intended to converge with canonical specs.  
- A shared reference for:
  - Decider implementations (LangGraph, service-based, or embedded),  
  - Multi-tenant and single-tenant variants,  
  - Offline simulator and experiment frameworks.

---

## 🧭 Context

The Autonomy Decider already has:

- A **scoring model** (cost/energy/carbon/freshness/trust).  
- **Gates** for governance and anomalies (CARE, cost-energy, cardinality, etc.).  
- An action contract: `resume`, `slow`, `pause`, `escalate`.

What has been less explicit is the **runtime lifecycle**:

- When does the decider consider a pipeline “in evaluation” vs “stable”?  
- How are **escalations** and **human overrides** represented?  
- How do **backoff** and **error** states avoid oscillations or runaway behavior?

This document provides that missing **formal layer**, and ties into:

- Variant docs (single-tenant, multi-tenant, offline-simulator).  
- Experiment docs (fairness, horizons, thresholds).  
- Reliability & governance docs (SLOs, FAIR+CARE).

The state machine is intended to be:

- **Implementation-neutral** (works in LangGraph, Airflow callbacks, standalone services).  
- **Graph-friendly** (states and transitions can be modeled as nodes/edges in the KFM knowledge graph).  

---

## 🧱 Architecture

### 1. Core Per-Pipeline States

For each pipeline, the Autonomy Decider operates over a finite set of states:

1. **`INIT`**  
   - Pipeline profile exists but has not yet completed a full evaluation cycle.  
   - Transition out occurs on first **evaluation tick**.

2. **`IDLE`**  
   - No immediate decision required; last action is considered stable.  
   - The decider awaits new **events** (telemetry change, config change, timer tick).

3. **`EVALUATING`**  
   - Snapshot is captured:
     - Autonomy profile,  
     - Telemetry,  
     - Governance context,  
     - Variant parameters (if any).  
   - Scoring and gates run deterministically.

4. **`ACTION_PENDING`**  
   - An action decision has been computed but not yet:
     - Emitted to orchestrators, or  
     - Logged to telemetry/OpenLineage.  
   - This state exists to ensure we never emit partially formed decisions.

5. **`STABLE`**  
   - The last decision has been successfully **emitted** and **acknowledged** (e.g., orchestrator accepted it).  
   - The decider stores:
     - Previous state,  
     - Action,  
     - Evidence snapshot references.

6. **`BACKOFF`**  
   - Temporarily slowing autonomy evaluation for this pipeline due to:
     - Error rate,  
     - Excessive action thrash,  
     - Rate-limiting constraints.  
   - Limited set of transitions allowed back to `EVALUATING` or `STABLE`.

7. **`PAUSED`**  
   - Pipeline is explicitly under **pause** semantics:
     - CARE violation,  
     - Budget violation,  
     - Manual governance action.  
   - Only specific events (e.g., human unpause, resolution of violation) can move it out.

8. **`ESCALATED`**  
   - Pipeline requires **human review**:
     - Conflicting gate signals,  
     - Uncertain governance tradeoffs.  
   - No automatic transitions back to non-escalated states without human acknowledgement.

9. **`DISABLED`**  
   - Autonomy is disabled for this pipeline:
     - Pipeline decommissioned,  
     - Governance decision to opt out,  
     - Long-term maintenance.  
   - Entry to this state is explicit; exit typically requires configuration change and potentially re-init.

These states apply per pipeline ID; the decider handles many pipelines concurrently, each with its own state instance.

---

### 2. Events and Triggers

Key **events** that can drive state transitions:

- **`EV_TICK`** — Scheduled evaluation tick (timer-based or orchestrator callback).  
- **`EV_TELEMETRY_CHANGE`** — Significant telemetry update (freshness, cost/energy/carbon, trust).  
- **`EV_PROFILE_CHANGE`** — Autonomy profile change (SLO, budgets, CARE labels, etc.).  
- **`EV_GATE_TRIP`** — Governance or anomaly gate triggers (CARE, cost-energy, cardinality, etc.).  
- **`EV_GATE_CLEAR`** — Previously tripped gate is cleared.  
- **`EV_ACTION_ACK`** — Orchestrator acknowledges action application.  
- **`EV_ACTION_ERROR`** — Orchestrator reports failure applying action.  
- **`EV_HUMAN_OVERRIDE`** — Explicit human action:
  - Force `pause`,  
  - Force `resume`,  
  - Acknowledge escalation, etc.  
- **`EV_DISABLE_AUTONOMY`** — Configuration-driven disable.  
- **`EV_ENABLE_AUTONOMY`** — Configuration-driven enable (e.g., from `DISABLED`).

Events are always logged with:

- Timestamp,  
- Pipeline ID,  
- Source (timer, telemetry, governance, human, etc.),  
- Any associated evidence or config version.

---

### 3. Transition Rules (Informal)

A non-exhaustive set of **allowed transitions**:

- `INIT` → `EVALUATING`  
  - On: `EV_TICK` with valid profile and telemetry.

- `IDLE` → `EVALUATING`  
  - On: `EV_TICK`, `EV_TELEMETRY_CHANGE`, or `EV_PROFILE_CHANGE`.

- `EVALUATING` → `ACTION_PENDING`  
  - On: scoring + gates produce a decision.

- `ACTION_PENDING` → `STABLE`  
  - On: `EV_ACTION_ACK` and decision persisted to telemetry/OpenLineage.

- `STABLE` → `IDLE`  
  - On: post-ack stable condition, no immediate re-evaluation needed.

- `ANY_STATE` → `PAUSED`  
  - On: `EV_GATE_TRIP` for **hard** governance gate, or explicit `EV_HUMAN_OVERRIDE` to pause.

- `ANY_STATE` → `ESCALATED`  
  - On: decision conflict or governance uncertainty requiring review.

- `STABLE` / `IDLE` → `BACKOFF`  
  - On: excessive thrash or error rate detected.

- `BACKOFF` → `EVALUATING`  
  - On: backoff timer expiry or human override.

- `ANY_STATE` → `DISABLED`  
  - On: `EV_DISABLE_AUTONOMY` config change.

- `DISABLED` → `INIT`  
  - On: `EV_ENABLE_AUTONOMY` + valid profile.

**Forbidden patterns** (must be guarded in code and tests):

- Direct `EVALUATING` → `PAUSED` without emitting an action or recording evidence.  
- Direct `PAUSED` → `STABLE` without explicit `EV_GATE_CLEAR` or `EV_HUMAN_OVERRIDE`.  
- Direct `ESCALATED` → `IDLE` or `STABLE` without `EV_HUMAN_OVERRIDE` / acknowledgement.

---

## 🗺️ Diagrams

### 1. High-Level Per-Pipeline State Machine

~~~mermaid
flowchart LR
    INIT["INIT<br/>Profile present, no full eval yet"]
      -->|EV_TICK| EVAL["EVALUATING<br/>snapshot + scoring + gates"]

    IDLE["IDLE<br/>waiting for events"]
      -->|EV_TICK / EV_TELEMETRY_CHANGE / EV_PROFILE_CHANGE| EVAL

    EVAL -->|decision computed| PEND["ACTION_PENDING<br/>action not yet acked"]
    PEND -->|EV_ACTION_ACK| STABLE["STABLE<br/>action applied & logged"]
    STABLE -->|no immediate work| IDLE

    STABLE -->|thrash / error rate| BACKOFF["BACKOFF<br/>rate-limited eval"]
    BACKOFF -->|backoff timer / override| EVAL

    EVAL -->|hard gate trip| PAUSED["PAUSED<br/>governance hold"]
    STABLE -->|EV_GATE_TRIP| PAUSED
    IDLE -->|EV_GATE_TRIP| PAUSED

    PAUSED -->|EV_GATE_CLEAR / EV_HUMAN_OVERRIDE| EVAL

    EVAL -->|conflict / uncertainty| ESC["ESCALATED<br/>human review"]
    STABLE -->|EV_HUMAN_OVERRIDE_ESCALATE| ESC
    ESC -->|EV_HUMAN_OVERRIDE_ACK| EVAL

    INIT -->|EV_DISABLE_AUTONOMY| DIS["DISABLED<br/>autonomy off"]
    IDLE -->|EV_DISABLE_AUTONOMY| DIS
    STABLE -->|EV_DISABLE_AUTONOMY| DIS
    PAUSED -->|EV_DISABLE_AUTONOMY| DIS
    ESC -->|EV_DISABLE_AUTONOMY| DIS

    DIS -->|EV_ENABLE_AUTONOMY| INIT
~~~

**Notes:**

- Labels avoid `\n` and use `<br/>` for multi-line compatibility.  
- This diagram is **illustrative**; exact implementation must use the formal state/transition tables.

---

## 📦 Data & Metadata

The state machine must be **observable** and **provenance-aware**.

### 1. State Telemetry

For each pipeline, telemetry MAY include fields like:

~~~json
{
  "pipeline": "example/hydro-hrrr",
  "state_machine": {
    "state": "STABLE",
    "previous_state": "ACTION_PENDING",
    "last_transition": "2025-12-05T11:15:00Z",
    "last_event": "EV_ACTION_ACK",
    "state_machine_version": "v1"
  }
}
~~~

Where:

- `state` is one of the canonical states.  
- `state_machine_version` maps to this spec’s `version` or a finer-grained internal revision.

### 2. OpenLineage / PROV Alignment

State transitions can be expressed as:

- Entities: pipeline state snapshots, decision records.  
- Activities: evaluation runs, gate checks, human overrides.  
- Agents: decider service, orchestrators, human operators.

A transition is then:

- `prov:Activity` that:
  - `prov:used` previous state snapshot and triggering events.  
  - `prov:generated` the new state and decision record.  

This enables state evolution to be traced in the KFM knowledge graph.

### 3. Config Hooks

Autonomy configs may include optional state-machine-related tuning:

~~~yaml
autonomy:
  state_machine:
    backoff:
      enabled: true
      min_interval: "1m"
      max_interval: "30m"
    thrash_detection:
      window: "15m"
      max_transitions: 10
~~~

These fields are design-level until formally adopted in schemas & canonical docs.

---

## 🧪 Validation & CI/CD

State-machine behavior must be validated through:

### 1. Static Validation

- **Schema checks** for any state-related config or telemetry fields.  
- **Enum checks** ensuring:
  - Only defined states are used,  
  - Only defined events are logged.

### 2. Transition Tests

- Unit tests that:
  - Enumerate allowed transitions,  
  - Explicitly assert **forbidden transitions** (e.g., `PAUSED` → `STABLE` without events).  

- Property-style tests that:
  - Start from `INIT`,  
  - Apply randomly sampled valid events,  
  - Assert the system never:
    - Enters unknown states,  
    - Violates invariants (e.g., action emitted while not in `ACTION_PENDING` / `EVALUATING`).

### 3. Integration & Simulator Tests

- Use the **Offline Simulator** variant to:
  - Replay time-series telemetry,  
  - Observe state trajectories for pipelines,  
  - Confirm:
    - No pathological oscillations,  
    - Backoff functions as designed,  
    - Escalation and pause semantics are preserved.

CI SHOULD include:

- At least one test suite explicitly named for state-machine behavior (e.g., `tests/autonomy/state_machine/`).  
- Checks that state-machine version changes are accompanied by:
  - Updated diagrams,  
  - Updated tests,  
  - Updated docs referencing new semantics.

---

## 🧠 Story Node & Focus Mode Integration

The state machine underpins **how Focus Mode explains autonomy**:

- “This pipeline is currently **PAUSED** due to a CARE gate; last transition at 2025‑12‑05T11:15Z.”  
- “Autonomy is in **BACKOFF** because actions changed too frequently in the past 15 minutes.”  
- “The pipeline is **ESCALATED** awaiting human review; autonomy will not resume until acknowledged.”

To support this:

- State names must be **stable and descriptive**.  
- Transitions must have clear, text-friendly descriptions.  
- Docs should provide:
  - Short definitions of each state,  
  - Example scenarios for key states (especially `PAUSED`, `ESCALATED`, `BACKOFF`).

Example Story Node anchor:

~~~text
Related Story Node:
urn:kfm:story-node:pipelines:autonomy-matrix:decider:state-machine:overview
~~~

Focus Mode can use this spec to:

- Map observed telemetry fields (`state_machine.state`) to human-readable explanations.  
- Provide simple timelines (“INIT → EVALUATING → ACTION_PENDING → STABLE → IDLE → …”).

---

## 🕰️ Version History

| Version    | Date       | Summary                                                                                                                    |
|-----------:|------------|----------------------------------------------------------------------------------------------------------------------------|
| **v11.2.4**| 2025-12-05 | Initial Autonomy Decider state-machine design. Defines canonical states, events, transitions, invariants, and CI guidance. |

---

<div align="center">

🧠 **KFM v11 — Autonomy Decider State Machine**  
Deterministic Control · Explainable Lifecycles · FAIR+CARE-Governed Autonomy  

[🧠 Decider Designs](README.md) · [🧠 Decider Spec](../README.md) · [🤖 Autonomy Matrix Spec](../../README.md)

</div>

