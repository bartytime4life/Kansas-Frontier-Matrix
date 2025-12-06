---
title: "📜 KFM v11 — Autonomy Decider Contracts"
description: "Canonical contracts between the Autonomy Decider, pipeline profiles, orchestrators, gates, and telemetry for the KFM v11 Autonomy Matrix."
path: "docs/pipelines/autonomy-matrix/decider/contracts.md"
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

intent: "autonomy-matrix-decider-contracts"
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
  - "contracts"

category: "Pipelines · Autonomy · Governance · Architecture · Contracts"

sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Internal"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: false

data_steward: "Reliability · Sustainability · FAIR+CARE Council"
ttl_policy: "Indefinite (subject to architecture changes)"
sunset_policy: "Supersede when Autonomy Matrix v12 decider contract model is adopted"

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
  - "docs/pipelines/autonomy-matrix/decider/action-logic.md@v11.2.4"
  - "docs/pipelines/autonomy-matrix/decider/designs/state-machine.md@v11.2.4"
  - "docs/pipelines/autonomy-matrix/decider/README.md@v11.2.4"
  - "docs/pipelines/autonomy-matrix/README.md@v11.2.3"
  - "docs/pipelines/reliability/README.md"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/docs-pipelines-autonomy-decider-contracts-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/docs-pipelines-autonomy-decider-contracts-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "mutable"

doc_uuid: "urn:kfm:doc:pipelines:autonomy-matrix:decider:contracts:v11.2.4"
semantic_document_id: "kfm-pipelines-autonomy-matrix-decider-contracts-v11.2.4"
event_source_id: "ledger:kfm:doc:pipelines:autonomy-matrix:decider:contracts:v11.2.4"

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
---

<div align="center">

# 📜 **KFM v11 — Autonomy Decider Contracts**  
`docs/pipelines/autonomy-matrix/decider/contracts.md`

**Purpose:**  
Define the **explicit contracts** between the Autonomy Decider and its environment:  
pipeline autonomy profiles, gates, state machine, action objects, orchestrators, telemetry,  
and the Offline Simulator. These contracts must be **config‑driven, deterministic, and  
governance‑safe**, so they can be enforced via schemas, CI, and the KFM knowledge graph.

</div>

---

## 📘 Overview

The Autonomy Decider is not a free‑form service; it is a **contract‑bound control plane**.

This document standardizes the following contract families:

- **Pipeline Autonomy Profile Contract**  
  How each pipeline declares SLOs, budgets, CARE/sovereignty flags, and autonomy options.

- **Gate Contract**  
  How governance and anomaly gates receive snapshots and emit `OK/WARN/BLOCK/ESCALATE` outcomes.

- **State‑Machine Contract**  
  How the Decider represents per‑pipeline autonomy state and allowed transitions (see `state-machine.md`).

- **Action Object Contract**  
  How decisions are encoded as portable objects consumed by orchestrators and telemetry sinks.

- **Orchestrator Contract**  
  How Airflow / Dagster / LangGraph interpret and apply actions.

- **Telemetry & OpenLineage Contract**  
  How events and decisions are logged for audits, dashboards, and Offline Simulator replays.

These contracts:

- Are **design‑time documents** that guide schemas and implementations.  
- Must be enforceable by **JSON Schema / SHACL**, CI checks, and Neo4j graph rules.  
- Provide stable anchors for Focus Mode and Story Nodes.

---

## 🧭 Context

The contracts defined here are used by:

- `docs/pipelines/autonomy-matrix/decider/action-logic.md`  
  (how scores + gates + state become actions),

- `docs/pipelines/autonomy-matrix/decider/designs/state-machine.md`  
  (how per‑pipeline autonomy state evolves),

- `docs/pipelines/autonomy-matrix/decider/designs/variants/*.md`  
  (how variants plug into the same contracts), and

- `docs/pipelines/autonomy-matrix/decider/designs/variants/experiments/*.md`  
  (how experiments use Offline Simulator to evaluate contract‑compatible changes).

The contracts must:

- Support **single‑tenant**, **multi‑tenant**, and **offline‑simulator** variants without divergence.  
- Be **strict enough** to prevent ad‑hoc integration, yet **flexible enough** to evolve in v12+.  
- Map cleanly to **PROV‑O** (plans/activities/entities) and KFM ontologies.

All fields and enums described here are **proposed and design‑level** until the corresponding
JSON/SHACL schemas and CI checks are fully implemented.

---

## 🧱 Architecture

### 1. Pipeline Autonomy Profile Contract

Each pipeline has a **profile** (typically YAML) that declares autonomy‑relevant parameters.
At minimum, a contract‑compatible profile includes:

- Identity  
  - `pipeline` — pipeline ID, stable string.  
  - `owner_team` — e.g., `hydro@kfm`.

- SLOs  
  - `slos.availability` — target, window, error budget.  
  - `slos.freshness` — maximum lag.  

- Budgets  
  - `slos.cost.monthly_cap_usd`.  
  - `slos.energy.monthly_cap_kwh`.  
  - `slos.carbon.monthly_cap_kgco2e`.

- Governance  
  - `governance.care_label`.  
  - `governance.sovereignty_policy`.  
  - `governance.priority_band` (e.g., `P0`–`P4`).

- Autonomy  
  - `autonomy.actions` — allowed actions (subset of `resume/slow/pause/escalate`).  
  - `autonomy.action_thresholds` — thresholds used by action logic.  
  - Optional: `autonomy.variant` — `single-tenant`, `multi-tenant`, `offline-sim-only`, etc.

Illustrative snippet (non‑normative):

~~~yaml
pipeline: "example/hydro-hrrr"
owner_team: "hydro@kfm"

slos:
  availability: { target: 0.985, window: 30d, error_budget: 0.015 }
  freshness:    { max_lag: "2h" }
  cost:         { monthly_cap_usd: 1200 }
  energy:       { monthly_cap_kwh: 250 }
  carbon:       { monthly_cap_kgco2e: 65 }

governance:
  care_label: "Synthetic-Waters"
  sovereignty_policy: "synthetic-h3-generalization-v1"
  priority_band: "P1"

autonomy:
  actions: ["resume", "slow", "pause", "escalate"]
  action_thresholds:
    resume_up:    0.60
    resume_down:  0.40
    slow_up:      0.30
    slow_down:    0.10
    pause:       -0.10
  variant: "single-tenant"
~~~

Contract rules:

- Profiles **must validate** against their schema before decider startup.  
- Missing or invalid profile ⇒ autonomy is disabled for that pipeline.  
- Fields like `care_label`, `priority_band`, `variant` must use controlled vocabularies.

---

### 2. Gate Contract

Gates take a **snapshot** and return a discrete outcome plus optional details.

Per gate, the contract is:

- Input:

  - Pipeline ID and autonomy profile reference.  
  - Telemetry snapshot (freshness, cost, energy, carbon, trust metrics).  
  - Governance context (CARE label, sovereignty policy, sensitivity flags).  

- Output:

  - `name` — stable gate ID, e.g., `care`, `cost_energy`, `freshness_stall`, `cardinality_guard`.  
  - `status` — one of `OK`, `WARN`, `BLOCK`, `ESCALATE`.  
  - `reason_code` — short code, e.g., `care_block`, `carbon_budget_hard_cap`.  
  - Optional `details` — small structured object (e.g., current vs limit).

Example gate output (conceptual):

~~~json
{
  "name": "cost_energy",
  "status": "WARN",
  "reason_code": "cost_energy_warn",
  "details": {
    "cost_usd_hour": 14.3,
    "kwh_hour": 6.1,
    "monthly_cost_utilization": 0.82,
    "monthly_energy_utilization": 0.74
  }
}
~~~

Contract rules:

- `status` enum must be consistent across all gates.  
- `reason_code` must come from a documented vocabulary.  
- Gate outputs are combined by the Decider into a summary used by action logic and telemetry.

---

### 3. State‑Machine Contract

The Autonomy Decider’s **state machine** is defined in `state-machine.md`. Contracts here
tell us how implementations expose that state:

- Required fields per pipeline:

  - `state_machine.state` — one of:  
    - `INIT`, `IDLE`, `EVALUATING`, `ACTION_PENDING`, `STABLE`,  
    - `BACKOFF`, `PAUSED`, `ESCALATED`, `DISABLED`.  
  - `state_machine.previous_state`.  
  - `state_machine.last_transition` (ISO‑8601 time).  
  - `state_machine.last_event`.  
  - `state_machine.version` — state‑machine spec version (e.g., `v1`).

Example telemetry fragment:

~~~json
{
  "pipeline": "example/hydro-hrrr",
  "state_machine": {
    "state": "STABLE",
    "previous_state": "ACTION_PENDING",
    "last_transition": "2025-12-06T03:15:00Z",
    "last_event": "EV_ACTION_ACK",
    "version": "v1"
  }
}
~~~

Contract rules:

- Only allowed states and events may be emitted.  
- State transitions must obey the patterns specified in `state-machine.md`.  
- Telemetry consumers and Offline Simulator must be able to reconstruct state evolution.

---

### 4. Action Object Contract

The **Action Object** is the decider’s unit of output consumed by orchestrators and logged to telemetry.

Required fields (conceptual):

- `pipeline` — pipeline ID.  
- `action` — enum: `resume`, `slow`, `pause`, `escalate`.  
- `score` — raw and normalized scores + components.  
- `gates` — per‑gate status summary.  
- `state_context` — previous state and previous action.  
- `reason_codes` — list of short codes.  
- `valid_for` — duration string (e.g., `5m`).  
- `decider_variant` — `single-tenant`, `multi-tenant`, etc.  
- `decider_version` — decider implementation version.

Example:

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
    "care": "OK",
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

Contract rules:

- `action` must always be present and valid.  
- `reason_codes` must be non‑empty and come from a documented set.  
- Orchestrators must **not reinterpret** actions; they only implement predefined semantics per action.

---

### 5. Orchestrator Contract

Orchestrators (Airflow / Dagster / LangGraph / others) consume Action Objects and apply behaviors:

- For `resume`:

  - Enable configured schedule or concurrency for the pipeline.  
  - Clear local “paused” or “blocked” flags, unless a human override exists.

- For `slow`:

  - Reduce concurrency or schedule frequency according to a policy derived from pipeline profile.  
  - Keep the pipeline “enabled” but operating at a lower intensity.

- For `pause`:

  - Stop new runs for the pipeline.  
  - Allow already running tasks to finish or be managed by reliability/rollback logic.  
  - Surface pause reason and relevant gate information to operators.

- For `escalate`:

  - Do not automatically change run state unless configured to do so.  
  - Create or update a human‑visible escalation (ticket, notification, etc.).  
  - Expose decider `reason_codes` and gate details.

Contract rules:

- Orchestrators must log **ack events** (success/failure) when applying actions, so state‑machine telemetry stays accurate.  
- Orchestrators must not silently ignore `pause` or `escalate`; failures must be visible and auditable.

---

### 6. Telemetry & OpenLineage Contract

Telemetry and lineage capture contracts:

- Events:

  - Decision events (Action Objects).  
  - Orchestrator `EV_ACTION_ACK` and `EV_ACTION_ERROR`.  
  - Gate trips and state‑machine transitions.

- Structure:

  - Lineage events should model decisions as `prov:Activity` linking:
    - Input snapshot entity,  
    - State‑machine entity,  
    - Action Object entity.

- Storage:

  - Append‑only JSONL logs for:
    - `autonomy-decisions.jsonl`,  
    - `action-events.jsonl`,  
    - `carbon-energy-history.jsonl`.  

Contract rules:

- All telemetry must validate against the `autonomy-matrix-v1` (and related) schemas.  
- No secrets or sensitive values may be stored in telemetry without explicit governance approval.

---

## 📦 Data & Metadata

From a metadata perspective, the contracts define a small set of **reusable shapes**:

- **PipelineProfile** (DCAT/PROV entity)  
  - Maps to autonomy profile YAML and to `slos/` and `governance/` graph nodes.

- **GateEvaluation** (PROV activity + entity)  
  - Gate evaluation activity that generates a gate result entity.

- **AutonomyDecision** (PROV activity + entity)  
  - Decision activity using snapshot + gate outputs, generating an Action Object entity.

- **OrchestratorAction** (PROV activity)  
  - Application of an Action Object to a runtime pipeline environment.

- **AutonomyTelemetryRecord** (data entity)  
  - JSONL entries storing snapshots of decisions and outcomes.

DCAT/STAC alignment:

- The contract schemas (JSON, SHACL) can be treated as **data assets**:

  - `dcat:Dataset` with distributions pointing to schema files.  
  - STAC Items in a `kfm-contracts` Collection with assets pointing to schemas and docs.

Neo4j alignment:

- Nodes:

  - `:AutonomyContract` — representing each contract family.  
  - `:Pipeline`, `:PipelineProfile`, `:Gate`, `:Decision`, `:Action`, `:Orchestrator`.  

- Relationships:

  - `(:Pipeline)-[:HAS_PROFILE]->(:PipelineProfile)`  
  - `(:Decision)-[:USES_GATE_RESULT]->(:GateResult)`  
  - `(:Decision)-[:EMITS_ACTION]->(:Action)`  
  - `(:Action)-[:APPLIED_BY]->(:Orchestrator)`  

These structures allow Focus Mode and Story Nodes to tie narratives back to contract entities.

---

## 🧪 Validation & CI/CD

Contract enforcement is a core CI responsibility:

1. **Schema Linting**

   - JSON/SHACL schemas for:
     - Pipeline profiles.  
     - Gate outputs.  
     - Action Objects.  
     - State‑machine telemetry snippets.  
   - `schema-lint` must ensure all example docs and fixtures are valid.

2. **Contract Tests**

   - Unit tests verifying:
     - Decider rejects invalid profiles or gate outputs.  
     - Orchestrator adapters respect the action enums and semantics.  
   - Integration tests verifying:
     - Full path: profile → snapshot → gates → decision → action → orchestrator ack → telemetry.

3. **Offline Simulator Integration**

   - Simulator runs must:
     - Use the same Action Object and telemetry shapes.  
     - Fail fast on schema violations.  
     - Record experiment metadata in `mcp/experiments/`.

4. **Governance & Provenance Checks**

   - `provenance-check` ensures:
     - Contract docs are in the `provenance_chain` for relevant decider changes.  
     - Telemetry and lineage schemas are referenced correctly in this doc and others.

5. **Breaking‑Change Detection**

   - CI should flag:
     - Removal or renaming of fields in contract schemas.  
     - Changes to enums (`action`, `status`, `reason_codes`) without version bumps and doc updates.

---

## 🧠 Story Node & Focus Mode Integration

Contracts make autonomy **explainable**:

- They define consistent structures for:

  - “What is this pipeline allowed to do?” (profile).  
  - “Why did this gate block or escalate?” (gate contract).  
  - “Why is the pipeline slowed or paused?” (action + reason codes).  
  - “How did orchestrator actually respond?” (orchestrator contract and telemetry).

Focus Mode can:

- Use contract definitions to render:

  - Field‑by‑field explanations for a given pipeline.  
  - Step‑by‑step narratives of decisions for a time interval.  
  - Highlight inconsistencies (e.g., profile says one thing, orchestrator behavior says another).

Example Story Node anchor:

~~~text
Related Story Node:
urn:kfm:story-node:pipelines:autonomy-matrix:decider:contracts:overview
~~~

Story Nodes should:

- Treat this doc as the **design reference** for what is “contractual” vs implementation detail.  
- Always connect back to the canonical Autonomy Matrix and Decider specs for normative behavior.

---

## 🕰️ Version History

| Version    | Date       | Summary                                                                                                           |
|-----------:|------------|-------------------------------------------------------------------------------------------------------------------|
| **v11.2.4**| 2025-12-06 | Initial Autonomy Decider contracts doc. Defines profile, gate, state, action, orchestrator, and telemetry contracts.|

---

<div align="center">

📜 **KFM v11 — Autonomy Decider Contracts**  
Stable Interfaces · Deterministic Behavior · FAIR+CARE‑Governed Integration  

[🧠 Decider Spec](README.md) · [🧠 State Machine](designs/state-machine.md) · [🧠 Action Logic](action-logic.md) · [🤖 Autonomy Matrix](../README.md)

</div>

