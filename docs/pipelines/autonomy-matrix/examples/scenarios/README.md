---
title: "🎭 KFM v11 — Autonomy Matrix Scenario Library"
description: "Scenario library for the KFM v11 Autonomy Matrix, capturing realistic autonomy situations for pipelines, including scores, gates, actions, and governance outcomes."
path: "docs/pipelines/autonomy-matrix/examples/scenarios/README.md"
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

sbom_ref: "../../../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.4/autonomy-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/autonomy-matrix-v1.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

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
doc_kind: "Guide"
header_profile: "standard"
footer_profile: "standard"

intent: "autonomy-matrix-scenarios"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"

scope:
  domain: "pipelines"
  applies_to:
    - "etl"
    - "ingestion"
    - "ai-inference"
    - "ai-training"
    - "refresh-pipelines"
    - "control-plane-simulation"

semantic_intent:
  - "governance"
  - "control-plane"
  - "reliability"
  - "sustainability"
  - "examples"
  - "simulation"

category: "Pipelines · Autonomy · Examples · Scenarios"

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
  - "docs/pipelines/autonomy-matrix/examples/README.md@v11.2.4"
  - "docs/pipelines/autonomy-matrix/decider/action-logic.md@v11.2.4"
  - "docs/pipelines/autonomy-matrix/decider/score-functions.md@v11.2.4"
  - "docs/pipelines/autonomy-matrix/decider/designs/state-machine.md@v11.2.4"
  - "docs/pipelines/autonomy-matrix/README.md@v11.2.3"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/docs-pipelines-autonomy-matrix-scenarios-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/docs-pipelines-autonomy-matrix-scenarios-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "mutable"

doc_uuid: "urn:kfm:doc:pipelines:autonomy-matrix:examples:scenarios:readme:v11.2.4"
semantic_document_id: "kfm-pipelines-autonomy-matrix-examples-scenarios-v11.2.4"
event_source_id: "ledger:kfm:doc:pipelines:autonomy-matrix:examples:scenarios:v11.2.4"

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

# 🎭 **KFM v11 — Autonomy Matrix Scenario Library**  
`docs/pipelines/autonomy-matrix/examples/scenarios/README.md`

**Purpose:**  
Provide a **structured scenario library** for the Autonomy Matrix, capturing realistic autonomy  
situations (scores, gates, actions, governance outcomes) as **replayable examples** used by:  
developers, SREs, sustainability teams, and Focus Mode to understand and validate decider behavior.

</div>

---

## 📘 Overview

This directory contains **scenario documents** that describe:

- A specific **pipeline context** (profile, SLOs, budgets, CARE label).  
- A **telemetry situation** (lag, cost/energy/carbon, trust signals).  
- The resulting **gates, score, state, and action** chosen by the Autonomy Decider.  
- The **expected orchestrator behavior** and governance implications.

Scenarios are:

- **Synthetic** by default (no real or sensitive telemetry).  
- **Contract‑aligned** with:
  - Score functions (`decider/score-functions.md`),  
  - Action logic (`decider/action-logic.md`),  
  - State machine (`decider/designs/state-machine.md`),  
  - Contracts (`decider/contracts.md`).  
- Used as fixtures for:
  - Offline Simulator experiments,  
  - Regression tests,  
  - Focus Mode narrative demos.

---

## 🧭 Context

This scenario library sits under:

- `docs/pipelines/autonomy-matrix/examples/` — high‑level examples and patterns.  
- `docs/pipelines/autonomy-matrix/examples/scenarios/` — **this directory**, detailed scenarios.  

It exists to:

- Provide **concrete, reproducible stories** of autonomy in action.  
- Bridge between abstract design docs and real telemetry traces.  
- Seed reusable **fixtures** for simulation and CI.

Scenarios complement:

- **Contracts** — what must be true at each interface.  
- **Score functions** — how the situation is quantified.  
- **Action logic** — how the system chooses `resume/slow/pause/escalate`.  
- **State machine** — how the pipeline moves between `PAUSED`, `STABLE`, `BACKOFF`, etc.

---

## 🧱 Architecture

### 1. Directory Layout

~~~text
docs/pipelines/autonomy-matrix/examples/scenarios/
│
├── 📄 README.md                         # This file: scenario library overview & conventions
│
├── 📂 p0-storm-nowcast/                 # High-urgency, high-freshness, sustainability-aware scenario family
│   ├── 📄 scenario-baseline.md          # Normal operation, high urgency, acceptable cost/energy/carbon
│   ├── 📄 scenario-carbon-clamp.md      # Carbon budget exceeded → slow/pause behavior
│   └── 📄 scenario-care-escalation.md   # CARE gate override → escalate action
│
├── 📂 p1-hydro-forecast/                # Hydrology forecast scenarios (HRRR downscale, etc.)
│   ├── 📄 scenario-backlog-pressure.md  # Backlog growth & freshness stall
│   └── 📄 scenario-thrash-control.md    # Hysteresis & backoff under noisy telemetry
│
├── 📂 p2-batch-reporting/               # Lower-urgency, cost-sensitive batch pipelines
│   └── 📄 scenario-cost-throttle.md     # Cost overrun → slow & pause patterns
│
└── 📂 fixtures/                         # Scenario-aligned simulator fixtures
    ├── 📄 README.md                     # Fixture format & mapping to scenarios
    ├── 📄 p0-storm-nowcast.jsonl        # Synthetic telemetry for storm-nowcast scenarios
    └── 📄 p1-hydro-forecast.jsonl       # Synthetic telemetry for hydro forecast scenarios
~~~

Author rules:

- Scenarios must live in **pipeline‑family subdirectories** (e.g., `p0-storm-nowcast/`).  
- Each scenario file must follow KFM‑MDP v11.2.4 and include:
  - A Purpose block.  
  - A clear **Scenario ID** and **Status** (e.g., `draft`, `canonical`).  
  - Links to relevant profiles, contracts, and experiments.  
- `fixtures/` contains **machine‑readable inputs** for Offline Simulator and tests.

---

### 2. Scenario Document Shape

Each scenario file (e.g., `scenario-baseline.md`) should follow a consistent pattern:

- Front‑matter (scenario metadata).  
- Human‑readable **setup**.  
- Tabular **telemetry snapshot**.  
- Derived **score and gate outcomes**.  
- Resulting **state + action**.  
- Notes on **expected orchestrator behavior** and **governance considerations**.

Illustrative skeleton:

~~~markdown
---
scenario_id: "p0-storm-nowcast:baseline"
scenario_status: "canonical"
pipeline_id: "p0-storm-nowcast"
variant: "single-tenant"
fixture_ref: "../../fixtures/p0-storm-nowcast.jsonl#baseline"
---

## Scenario

Short description of the situation.

## Snapshot

- Time window: 2025‑04‑10T01:00Z – 2025‑04‑10T01:05Z
- Key metrics:
  - lag_min: 7
  - backlog_slices: 4
  - cost_usd_hour: 9.5
  - kwh_hour: 4.0
  - carbon_kgco2e_hour: 1.2
  - data_trust_index: 0.97

## Score & Gates

- FreshnessScore: 0.92
- TemporalRelevance: 0.98
- DataTrust: 0.97
- CostBurnRate: 0.20
- EnergyKWhRate: 0.18
- CarbonCO2eRate: 0.15

- Gates:
  - care: OK
  - cost_energy: OK
  - freshness_stall: OK
  - cardinality_guard: OK

## Decision

- State before: STABLE
- State after: STABLE
- Action: resume
- Reason codes:
  - score_in_resume_band
~~~

Exact headings inside scenarios can differ, but the **Scenario → Snapshot → Score & Gates → Decision** pattern must be recognizable.

---

## 📦 Data & Metadata

Scenarios interact with data and metadata in several ways:

- **Scenario docs** are:

  - `TechArticle`‑like documents describing design‑time examples.  
  - Linked to specific **pipeline profiles**, **fixtures**, and **experiments**.

- **Fixtures** are:

  - JSONL files that encode **time‑series telemetry** used in Offline Simulator.  
  - Mapped to scenario IDs via `fixture_ref` fields.

- **Experiments**:

  - May reference scenarios to express “run the simulator with these inputs and compare outcomes to the scenario’s expected action/state”.

Minimal metadata checklist per scenario:

1. `scenario_id` (globally unique within Autonomy Matrix).  
2. `pipeline_id` (links to autonomy profile).  
3. `variant` (`single-tenant`, `multi-tenant`, etc.).  
4. `fixture_ref` (or explicit statement that scenario is “documentation‑only”).  
5. Status (`draft`, `canonical`, `deprecated`).

Neo4j alignment:

- Nodes:

  - `:AutonomyScenario`  
  - `:AutonomyFixture`  

- Relationships:

  - `(:AutonomyScenario)-[:USES_FIXTURE]->(:AutonomyFixture)`  
  - `(:AutonomyScenario)-[:FOR_PIPELINE]->(:Pipeline)`  
  - `(:Experiment)-[:EVALUATES_SCENARIO]->(:AutonomyScenario)`

This allows Focus Mode and governance to navigate from “what happened” to “what should have happened”.

---

## 🧪 Validation & CI/CD

Scenarios must be **first‑class citizens** in CI:

1. **Schema Validation**

   - Scenario front‑matter fields validated via JSON/SHACL:
     - `scenario_id`, `pipeline_id`, `variant`, `fixture_ref`, `scenario_status`.  

2. **Fixture Consistency**

   - Every `fixture_ref` must resolve to an existing JSONL file and (optionally) record subset.  
   - Offline Simulator configs must include **at least some canonical scenarios**.

3. **Replay Tests**

   - CI can run a small suite where:
     - Inputs: scenario fixture slices.  
     - Expected outputs: state + action + reason codes from scenario doc.  
   - Any divergence is flagged as potential regression or scenario drift.

4. **Governance Review Hooks**

   - Adding or updating **canonical** scenarios for sensitive pipelines (e.g., CARE‑labeled) may
     require FAIR+CARE or governance review, especially if they encode new gate behaviors.

---

## 🧠 Story Node & Focus Mode Integration

Scenarios are natural **Story Nodes**:

- Each scenario is a self‑contained narrative:

  - “Given this pipeline profile and telemetry, gates and score yield this action and state.”

- Focus Mode can:

  - Surface a scenario as an example when a similar real‑time situation occurs.  
  - Use scenario metadata and fixtures to explain **why** a particular decision is expected.

Example Story Node anchor for this library:

~~~text
Related Story Node:
urn:kfm:story-node:pipelines:autonomy-matrix:examples:scenarios:overview
~~~

Scenario‑specific Story Nodes might be:

~~~text
urn:kfm:story-node:pipelines:autonomy-matrix:examples:scenarios:p0-storm-nowcast:baseline
urn:kfm:story-node:pipelines:autonomy-matrix:examples:scenarios:p1-hydro-forecast:backlog-pressure
~~~

These IDs give Focus Mode a stable way to link UI explanations to concrete scenario docs.

---

## 🕰️ Version History

| Version    | Date       | Summary                                                                                                   |
|-----------:|------------|-----------------------------------------------------------------------------------------------------------|
| **v11.2.4**| 2025-12-06 | Initial Autonomy Matrix Scenario Library README: layout, scenario shape, fixtures conventions, CI hooks. |

---

<div align="center">

🎭 **KFM v11 — Autonomy Matrix Scenario Library**  
Concrete Situations · Replayable Fixtures · FAIR+CARE‑Aligned Autonomy Stories  

[🤖 Autonomy Matrix](../../README.md) · [🧠 Decider](../../decider/README.md) · [📚 Examples Root](../README.md)

</div>

