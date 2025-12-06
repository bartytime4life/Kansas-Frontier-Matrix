---
title: "🧠 KFM v11 — Autonomy Decider Action Logic"
description: "Canonical mapping from scores, gates, and state-machine context to deterministic resume/slow/pause/escalate actions for the KFM v11 Autonomy Matrix decider."
path: "docs/pipelines/autonomy-matrix/decider/action-logic.md"
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

sbom_ref: "../../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.4/autonomy-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/autonomy-matrix-v1.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
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

intent: "autonomy-matrix-decider-action-logic"
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
  - "action-logic"

category: "Pipelines · Autonomy · Governance · Architecture · Action Logic"

sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Internal"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: false

data_steward: "Reliability · Sustainability · FAIR+CARE Council"
ttl_policy: "Indefinite (subject to architecture changes)"
sunset_policy: "Supersede when Autonomy Matrix v12 action-logic spec is adopted"

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
  - "docs/pipelines/autonomy-matrix/decider/designs/state-machine.md@v11.2.4"
  - "docs/pipelines/autonomy-matrix/decider/README.md@v11.2.4"
  - "docs/pipelines/autonomy-matrix/README.md@v11.2.3"
  - "docs/pipelines/reliability/README.md"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/docs-pipelines-autonomy-decider-action-logic-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/docs-pipelines-autonomy-decider-action-logic-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "mutable"

doc_uuid: "urn:kfm:doc:pipelines:autonomy-matrix:decider:action-logic:v11.2.4"
semantic_document_id: "kfm-pipelines-autonomy-matrix-decider-action-logic-v11.2.4"
event_source_id: "ledger:kfm:doc:pipelines:autonomy-matrix:decider:action-logic:v11.2.4"

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

# 🧠 **KFM v11 — Autonomy Decider Action Logic**  
`docs/pipelines/autonomy-matrix/decider/action-logic.md`

**Purpose:**  
Define the **deterministic mapping** from scores, gates, and state-machine context  
to `resume`, `slow`, `pause`, or `escalate` actions for each pipeline,  
keeping autonomy **governance-first, reproducible, and Focus-Mode-friendly**.

</div>

---

## 📘 Overview

Per pipeline and per evaluation tick, the Autonomy Decider transforms:

- A **snapshot** (autonomy profile + telemetry + governance context),  
- A **score** (freshness, relevance, trust, cost, energy, carbon),  
- A set of **gate outcomes** (CARE, budgets, anomalies), and  
- **State-machine context** (`decider/designs/state-machine.md`),

into exactly one of four actions:

- `resume` — run at configured rate and concurrency.  
- `slow` — reduce rate or concurrency.  
- `pause` — halt until conditions are safe.  
- `escalate` — require human review.

This document standardizes:

- The **three-stage decision flow** (gates → score → mapping).  
- **Thresholds and hysteresis** for stability.  
- A **portable action object** consumed by orchestrators, Offline Simulator, and governance tooling.

All numeric values are **config‑driven** and must be logged for provenance and replay.

---

## 🧭 Context

This action‑logic file sits between:

- **Scoring & gates** (Autonomy Matrix core), and  
- The **state machine** plus orchestrators (Airflow, Dagster, LangGraph).

Related documents:

- `docs/pipelines/autonomy-matrix/README.md` — Autonomy Matrix overview.  
- `docs/pipelines/autonomy-matrix/decider/README.md` — Decider overview.  
- `docs/pipelines/autonomy-matrix/decider/designs/state-machine.md` — per‑pipeline lifecycle.  
- `docs/pipelines/autonomy-matrix/decider/designs/variants/*.md` — single‑tenant, multi‑tenant, offline‑simulator variants.  
- `docs/pipelines/autonomy-matrix/decider/designs/variants/experiments/*.md` — experiments for thresholds, fairness, horizons.

Constraints:

- Same snapshot + config ⇒ same action + reason codes.  
- Governance gates can always override numeric scores.  
- No randomness in action selection; any stochastic experimentation must run only in Offline Simulator with fixed seeds, recorded in `mcp/experiments/`.

---

## 🧱 Architecture

### 1. Three‑Stage Decision Flow

For each pipeline at an evaluation tick, the Autonomy Decider runs:

1. **Hard Gates Stage**

   Gates evaluate governance and anomaly constraints:

   - CARE & sovereignty gates.  
   - Cost / energy / carbon budget gates.  
   - Freshness‑stall and backlog gates.  
   - Cardinality / anomaly guards.  

   Each gate returns one of:

   - `OK`  
   - `WARN`  
   - `BLOCK`  
   - `ESCALATE`

2. **Score Stage**

   Compute a raw score `S` based on:

   - Freshness vs SLO.  
   - Temporal relevance.  
   - Data trust (tests, lineage, QA).  
   - Cost, energy, carbon burn rates.

   Normalize to `S_norm ∈ [-1.0, 1.0]` and log:

   - Raw score,  
   - Normalized score,  
   - Component contributions.

3. **Action Mapping Stage**

   Combine:

   - Gate results.  
   - `S_norm`.  
   - State‑machine context (current state + previous action).  
   - Per‑pipeline thresholds and hysteresis settings.

   Emit exactly one of: `resume`, `slow`, `pause`, `escalate`.

### 2. Gate Precedence

Gate precedence is **strict**:

1. If any critical gate emits `ESCALATE` ⇒ action = `escalate`.  
2. Else if any critical gate emits `BLOCK` ⇒ action = `pause`.  
3. Else run score‑based mapping, where `WARN` contributes to bias toward `slow` / `pause`.

Numeric scores must **never override** `BLOCK` / `ESCALATE` from CARE / sovereignty or other hard governance gates.

### 3. Score and Thresholds (Conceptual)

Conceptual score:

~~~text
S =  w_fresh  * FreshnessScore()
   + w_urg    * TemporalRelevance()
   + w_trust  * DataTrust()
   - w_cost   * CostBurnRate()
   - w_energy * EnergyKWhRate()
   - w_carbon * CarbonCO2eRate()
~~~

Normalized:

~~~text
S_norm = normalize(S)     # S_norm ∈ [-1.0, 1.0]
~~~

Per‑pipeline thresholds (in autonomy profiles), with **up/down** values for hysteresis:

~~~yaml
autonomy:
  action_thresholds:
    resume_up:    0.60   # enter resume
    resume_down:  0.40   # leave resume
    slow_up:      0.30   # enter slow from pause/backoff
    slow_down:    0.10   # leave slow toward pause
    pause:       -0.10   # strong signal to pause
~~~

Ordering constraint:

~~~text
pause < slow_down ≤ slow_up ≤ resume_down ≤ resume_up
~~~

Implementations must validate ordering at config load time.

### 4. State‑Aware Mapping (Informal)

~~~text
function decide_action(snapshot, state, config):

  gates = evaluate_gates(snapshot, config)

  # 1. Hard governance
  if gates.has_any("ESCALATE"):
      return "escalate"

  if gates.has_any("BLOCK"):
      return "pause"

  # 2. Score
  score  = compute_score(snapshot, config)
  s_norm = normalize_score(score, config)
  t      = config.autonomy.action_thresholds

  # 3. State-aware thresholds
  match state.current:
    case "PAUSED":
      if s_norm >= t.resume_up:
          return "resume"
      elif s_norm >= t.slow_up:
          return "slow"
      else:
          return "pause"

    case "BACKOFF":
      if s_norm >= t.resume_up and not gates.has_any("WARN"):
          return "resume"
      elif s_norm >= t.slow_down:
          return "slow"
      else:
          return "pause"

    case "STABLE" | "IDLE" | "INIT" | "EVALUATING":
      if s_norm >= t.resume_up:
          return "resume"
      elif s_norm >= t.slow_down:
          return "slow"
      elif s_norm <= t.pause:
          return "pause"
      else:
          return state.previous_action or "resume"

    case "ESCALATED" | "DISABLED":
      return state.previous_action or "pause"
~~~

This mapping:

- Keeps **governance first** (gates dominate).  
- Uses **hysteresis** to avoid thrash.  
- Falls back to **previous action** in ambiguous regions to preserve stability.

---

## 🗺️ Diagrams

### Action Logic Flow per Evaluation Tick

~~~mermaid
flowchart LR
    SNAP["Snapshot<br/>profile + telemetry"] --> GATES["Hard Gates<br/>CARE / budgets / anomalies"]

    GATES -->|HAS_ESCALATE| ACT_ESC["Action = ESCALATE"]
    GATES -->|HAS_BLOCK|   ACT_PAUSE_HARD["Action = PAUSE_HARD"]
    GATES -->|OK_OR_WARN|  SCORE["Score & Normalize<br/>S → S_norm"]

    SCORE --> MAP["Map with State + Thresholds<br/>hysteresis"]

    MAP -->|choose| ACT_RES["Action = RESUME"]
    MAP -->|choose| ACT_SLOW["Action = SLOW"]
    MAP -->|choose| ACT_PAUSE_SOFT["Action = PAUSE_SOFT"]

    ACT_RES        --> OUT["Action Object"]
    ACT_SLOW       --> OUT
    ACT_PAUSE_SOFT --> OUT
    ACT_ESC        --> OUT
    ACT_PAUSE_HARD --> OUT
~~~

Diagram rules:

- Edge labels avoid parentheses and problematic characters.  
- `<br/>` is used for intra‑label line breaks, consistent with other decider docs.

---

## 📦 Data & Metadata

### 1. Action Object (Conceptual Schema)

The decider emits an **Action Object** per pipeline per evaluation tick:

~~~json
{
  "pipeline": "example/hydro-hrrr",
  "action": "slow",
  "score": {
    "raw": 0.42,
    "normalized": 0.18,
    "components": {
      "freshness": 0.90,
      "temporal_relevance": 0.85,
      "trust": 0.95,
      "cost": 0.35,
      "energy": 0.30,
      "carbon": 0.25
    }
  },
  "gates": {
    'care': "OK",
    "cost_energy": "WARN",
    "freshness_stall": "OK",
    "cardinality_guard": "OK"
  },
  "state_context": {
    "previous_state": "STABLE",
    "previous_action": "resume"
  },
  "reason_codes": [
    "cost_energy_warn",
    "score_in_slow_band"
  ],
  "valid_for": "5m",
  "decider_variant": "single-tenant",
  "decider_version": "v11.2.4"
}
~~~

Conventions:

- `action` ∈ { `resume`, `slow`, `pause`, `escalate` }.  
- `reason_codes` are short, stable identifiers for audit and Focus Mode.  
- `valid_for` ties into horizon‑tuning experiments (how long before re‑evaluation is expected).  
- All example IDs and values in docs should be **synthetic**.

### 2. Reason Code Vocabulary (Illustrative)

Examples (non‑exhaustive):

- `score_in_resume_band`  
- `score_in_slow_band`  
- `score_in_pause_band`  
- `care_block`  
- `care_escalate`  
- `carbon_budget_hard_cap`  
- `cost_energy_warn`  
- `freshness_stall_gate`  
- `thrash_backoff`

A separate reference table or schema should map each code to a human‑readable description for governance tools and Focus Mode.

---

## 🧪 Validation & CI/CD

Action logic participates in CI as follows:

### 1. Config & Schema Validation

- Threshold configs must:

  - Respect ordering and range constraints.  
  - Use bounded numeric ranges (e.g., `-1.0 ≤ thresholds ≤ 1.0`).

- Action objects must validate against:

  - `docs-pipelines-autonomy-decider-action-logic-v11.2.4.schema.json` and associated SHACL shapes.

### 2. Determinism Tests

- Re‑running the decider on identical snapshots must yield:

  - The same `action`.  
  - The same `reason_codes`.  

- No RNG is allowed in decision paths. Any seeds used for experiments in Offline Simulator must be:

  - Fixed,  
  - Logged,  
  - Stored under `mcp/experiments/`.

### 3. Hysteresis & Thrash Tests

Using the **Offline Simulator** variant:

- Replay time‑series fixtures that hover around thresholds.  
- Measure:

  - Action‑change rate per pipeline.  
  - Recovery behavior from `pause` / `backoff`.  
  - Interactions with horizon‑tuning experiments.

Guardrails:

- No pathological oscillation (`resume ⇄ slow` in tight loops without real signal change).  
- No “stuck” behavior where scores clearly improve but actions never upgrade.

### 4. Governance Tests

- Cases with CARE / sovereignty gates emitting `BLOCK` or `ESCALATE` must always:

  - Yield `pause` or `escalate`, regardless of score.

CI SHOULD:

- Include stateful tests focused on action‑logic behavior.  
- Include at least one simulator‑based regression for thresholds.  
- Fail if action enums or reason‑code vocabulary change without corresponding doc/schema updates.

---

## 🧠 Story Node & Focus Mode Integration

Action logic supports Focus Mode explanations such as:

- Why a pipeline is currently **slowed** rather than paused.  
- Why a pipeline was **paused** despite high freshness urgency.  
- Why autonomy is **escalating** instead of acting automatically.

Focus Mode can compose explanations from:

- `action`  
- `score.normalized`  
- `gates`  
- `state_context`  
- `reason_codes`

Example narrative:

~~~text
This pipeline is slowed because cost and energy usage are elevated
("cost_energy_warn") and the normalized autonomy score (0.18)
lies in the configured slow band.
~~~

Example Story Node anchor:

~~~text
Related Story Node:
urn:kfm:story-node:pipelines:autonomy-matrix:decider:action-logic:overview
~~~

Story Nodes must treat this document as the **design reference** for action mapping, with canonical Autonomy Matrix and Decider specs remaining the final normative sources as they are updated.

---

## 🕰️ Version History

| Version    | Date       | Summary                                                                                                         |
|-----------:|------------|-----------------------------------------------------------------------------------------------------------------|
| **v11.2.4**| 2025-12-05 | Initial Autonomy Decider action‑logic design. Defines 3‑stage flow, thresholds, hysteresis, action object, CI. |

---

<div align="center">

🧠 **KFM v11 — Autonomy Decider Action Logic**  
Deterministic Mapping · Explainable Actions · FAIR+CARE‑Governed Autonomy  

[🧠 Decider Spec](README.md) · [🧠 State Machine](designs/state-machine.md) · [🤖 Autonomy Matrix Spec](../README.md)

</div>
