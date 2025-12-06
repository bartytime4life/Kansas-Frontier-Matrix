---
title: "📊 KFM v11 — Autonomy Decider Score Functions"
description: "Design and contracts for KFM v11 Autonomy Decider score functions: component metrics, normalization, and aggregation into a single autonomy score."
path: "docs/pipelines/autonomy-matrix/decider/score-functions.md"
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

intent: "autonomy-matrix-decider-score-functions"
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
  - "scoring"

category: "Pipelines · Autonomy · Governance · Architecture · Scoring"

sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Internal"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: false

data_steward: "Reliability · Sustainability · FAIR+CARE Council"
ttl_policy: "Indefinite (subject to architecture changes)"
sunset_policy: "Supersede when Autonomy Matrix v12 score-function spec is adopted"

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

json_schema_ref: "schemas/json/docs-pipelines-autonomy-decider-score-functions-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/docs-pipelines-autonomy-decider-score-functions-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "mutable"

doc_uuid: "urn:kfm:doc:pipelines:autonomy-matrix:decider:score-functions:v11.2.4"
semantic_document_id: "kfm-pipelines-autonomy-matrix-decider-score-functions-v11.2.4"
event_source_id: "ledger:kfm:doc:pipelines:autonomy-matrix:decider:score-functions:v11.2.4"

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

# 📊 **KFM v11 — Autonomy Decider Score Functions**  
`docs/pipelines/autonomy-matrix/decider/score-functions.md`

**Purpose:**  
Specify the **component score functions** and **aggregation rules** used by the Autonomy Decider  
to compute a normalized autonomy score per pipeline and evaluation tick, in a way that is  
**deterministic, reproducible, and governance‑safe** across all Autonomy Matrix variants.

</div>

---

## 📘 Overview

The Autonomy Decider does not rely on a single opaque “magic” score. Instead, it builds a
normalized score from a **small, well‑defined set of component score functions**:

- `FreshnessScore()` — SLO‑aware lag and backlog.  
- `TemporalRelevance()` — how time‑critical the pipeline’s outputs are.  
- `DataTrust()` — data quality, test results, lineage confidence.  
- `CostBurnRate()` — monetary spend relative to cost budgets.  
- `EnergyKWhRate()` — power usage relative to energy budgets.  
- `CarbonCO2eRate()` — emissions relative to carbon budgets.

These functions feed into a normalized score `S_norm ∈ [-1.0, 1.0]` used by:

- **Action Logic** (`action-logic.md`) to choose `resume/slow/pause/escalate`.  
- **State Machine** (`state-machine.md`) to understand stability and thrash.  
- **Offline Simulator** (variants/experiments) to test threshold and horizon changes.

This document defines:

- What each component function measures.  
- How inputs are normalized and weighted.  
- How the final score is computed and logged.  
- How these pieces are wired into contracts and CI.

All formulas are design‑level and must be backed by schemas and tests before production use.

---

## 🧭 Context

Score functions are one of three core pieces of the Decider design:

- **Score Functions** (this doc)  
  Pure, deterministic mappings from telemetry + config to dimensionless components and a final score.

- **Action Logic** (`action-logic.md`)  
  Threshold‑ and state‑aware mapping from score + gates to a discrete action.

- **State Machine** (`state-machine.md`)  
  Per‑pipeline lifecycle that structures when and how decisions are evaluated and applied.

Score functions must:

- Be **config‑driven** (weights, target ranges, SLOs).  
- Produce **bounded, comparable outputs** suitable for aggregation.  
- Integrate cleanly with gate outcomes (which enforce hard constraints).

Variants (single‑tenant, multi‑tenant, offline simulator) may:

- Adjust weights or incorporate tenant‑level fairness.  
- Use different time horizons or smoothing windows.  

…but they must always implement this score‑function contract.

---

## 🧱 Architecture

### 1. Component Score Functions

Each component returns a real number in a **bounded range**, typically `[-1.0, 1.0]`:

- Positive = “good for running now”.  
- Negative = “bad or risky to run now”.

At a conceptual level:

~~~text
FreshnessScore()        ∈ [-1, 1]
TemporalRelevance()     ∈ [-1, 1]
DataTrust()             ∈ [-1, 1]
CostBurnRate()          ∈ [-1, 1]
EnergyKWhRate()         ∈ [-1, 1]
CarbonCO2eRate()        ∈ [-1, 1]
~~~

#### 1.1 FreshnessScore()

Measures how closely the pipeline meets its freshness SLO:

- Inputs:

  - Current lag vs `slos.freshness.max_lag`.  
  - Backlog depth (e.g., number of pending slices).  

- Desired behavior:

  - Near zero lag and moderate backlog ⇒ close to `+1`.  
  - Lag approaching max_lag ⇒ decays toward `0`.  
  - Lag far beyond max_lag ⇒ decays toward `-1`.

Implementation detail (design‑level): typically a smoothed, monotonic function of lag ratio,
with optional backlog sensitivity.

#### 1.2 TemporalRelevance()

Measures how time‑sensitive a pipeline’s outputs are **for the current moment**:

- Inputs:

  - Priority band (e.g., `P0` … `P4`).  
  - Pipeline type (e.g., nowcasting vs batch reporting).  
  - Optionally: user‑defined relevance schedules.

- Desired behavior:

  - Highly time‑critical pipelines in their active window ⇒ near `+1`.  
  - Low‑priority or off‑window pipelines ⇒ closer to `0` or slightly negative.

This function allows non‑urgent pipelines to slow or pause earlier than urgent ones.

#### 1.3 DataTrust()

Measures confidence in pipeline outputs:

- Inputs:

  - Recent test pass/fail rates.  
  - Schema validation results.  
  - Lineage completeness, missing data ratios.  

- Desired behavior:

  - Strong data quality and lineage ⇒ near `+1`.  
  - Mild issues or transient failures ⇒ around `0`.  
  - Severe or repeated failures ⇒ strongly negative.

Gates may still **hard‑block** on some conditions, but DataTrust contributes a soft
penalty to the overall score.

#### 1.4 CostBurnRate()

Measures cost pressure:

- Inputs:

  - Current hourly cost estimate (e.g., USD/hour).  
  - Month‑to‑date cost utilization vs budget.  

- Desired behavior:

  - Well under budget ⇒ near `0` (or mildly positive if desired).  
  - Near budget ⇒ negative bias.  
  - Over budget ⇒ strongly negative.

Note that cost gates may still emit `WARN` or `BLOCK`. CostBurnRate is the soft component
used in scoring, while gates enforce hard caps.

#### 1.5 EnergyKWhRate()

Measures energy pressure:

- Inputs:

  - Estimated kWh/hour for the pipeline.  
  - Month‑to‑date kWh utilization vs budget.  

- Behavior is analogous to CostBurnRate, but targeting energy budgets.

#### 1.6 CarbonCO2eRate()

Measures emissions pressure:

- Inputs:

  - Estimated kgCO2e/hour.  
  - Month‑to‑date kgCO2e vs carbon budget.  

Again, behavior is similar to CostBurnRate, but focused on carbon.

---

### 2. Aggregation into a Single Score

All component scores are combined into a weighted sum and normalized:

~~~text
S_raw =
  w_fresh  * FreshnessScore()        +
  w_urg    * TemporalRelevance()     +
  w_trust  * DataTrust()             -
  w_cost   * CostBurnRate()          -
  w_energy * EnergyKWhRate()         -
  w_carbon * CarbonCO2eRate()
~~~

Weights are specified per pipeline (or per profile family) and must be non‑negative:

~~~yaml
autonomy:
  score_weights:
    fresh:   0.35
    urg:     0.25
    trust:   0.20
    cost:    0.10
    energy:  0.05
    carbon:  0.05
~~~

Normalization clamps or rescales `S_raw` into a stable range:

~~~text
S_norm = normalize(S_raw)     # S_norm ∈ [-1.0, 1.0]
~~~

`S_norm` is the value used by:

- Action thresholds (`resume_up`, `slow_down`, etc.).  
- Telemetry and Offline Simulator plots.  
- Focus Mode explanations.

---

### 3. Determinism & Purity

Score functions **must** be:

- **Pure** — same inputs ⇒ same outputs; no side effects.  
- **Deterministic** — no RNG, no external time dependencies; any horizon windows are based on
  explicit time‑series snapshots given to the function.  
- **Config‑driven** — weights, ranges, and smoothing windows come from versioned config.

Any experimentation with stochastic methods must be:

- Confined to Offline Simulator.  
- Reproducible via fixed seeds and logged configs under `mcp/experiments/`.

---

## 🗺️ Diagrams

### Score Function Flow

~~~mermaid
flowchart LR
    TELE["Telemetry<br/>lag / backlog / cost / energy / carbon / QA"] --> COMP["Component Functions<br/>Freshness / Relevance / Trust / Cost / Energy / Carbon"]

    COMP --> AGG["Weighted Aggregation<br/>S_raw = Σ w_i * score_i"]
    AGG --> NORM["Normalization<br/>S_norm ∈ [-1, 1]"]
    NORM --> OUT["Score Output<br/>used by Action Logic"]
~~~

Diagram notes:

- Edge labels are simple node‑to‑node arrows to avoid parser issues.  
- `<br/>` is used for line breaks inside node labels.

---

## 📦 Data & Metadata

### 1. Score Telemetry Shape (Conceptual)

Per decision, score telemetry should include:

~~~json
{
  "pipeline": "example/hydro-hrrr",
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
    },
    "weights": {
      "fresh": 0.35,
      "urg": 0.25,
      "trust": 0.20,
      "cost": 0.10,
      "energy": 0.05,
      "carbon": 0.05
    }
  }
}
~~~

This matches the score block inside the Decider Action Object contract (`action-logic.md`).

### 2. Config Shape (Conceptual)

Score function configuration is stored in autonomy profiles or shared policy files:

~~~yaml
autonomy:
  score_weights:
    fresh:   0.35
    urg:     0.25
    trust:   0.20
    cost:    0.10
    energy:  0.05
    carbon:  0.05

  score_norm:
    method: "tanh-clamp"
    lower_bound: -1.0
    upper_bound:  1.0

  score_windows:
    freshness_lag:  "15m"
    backlog_depth:  "60m"
    cost_window:    "1h"
    energy_window:  "1h"
    carbon_window:  "1h"
~~~

Config rules (design‑level):

- `score_weights` must sum to a reasonable positive value; relative ratios matter more than absolute sum.  
- `score_norm` must define a stable normalization method (e.g., linear clamp, tanh).  
- `score_windows` define how far back telemetry is considered for each component.

### 3. PROV / DCAT Alignment

Conceptually:

- Score computations are `prov:Activity` instances that:

  - `prov:use` telemetry and profile entities.  
  - `prov:generate` score entities.

- The schemas for score telemetry and config can be treated as:

  - `dcat:Dataset` with distributions referencing JSON/SHACL schemas.  
  - STAC Items within a `kfm-contracts` or `kfm-telemetry` Collection.

This allows detailed score behavior to be analyzed in the KFM knowledge graph.

---

## 🧪 Validation & CI/CD

Score functions must pass several layers of validation:

### 1. Schema & Config Validation

- JSON/SHACL schemas for:

  - Score telemetry blocks.  
  - Score‑related fields in autonomy profiles.  

- CI checks:

  - Ensure mandatory component keys exist (freshness, relevance, trust, cost, energy, carbon).  
  - Enforce numeric ranges (e.g., `-1.0 ≤ score_component ≤ 1.0`).  
  - Validate `score_weights` and normalization config.

### 2. Unit Tests

- For each component function:

  - Known input fixtures ⇒ expected outputs.  
  - Edge cases (e.g., exactly at SLO boundary, far over budget) verified.  

- For aggregation:

  - Known component + weight combos ⇒ expected `S_raw` and `S_norm`.  
  - Idempotence of normalization within defined range.

### 3. Offline Simulator Tests

Offline Simulator runs (see variants/experiments docs) must:

- Use real or synthetic time‑series fixtures.  
- Evaluate:

  - Score trajectories for different pipelines and configurations.  
  - Sensitivity to window sizes and weight changes.  

- Log:

  - `S_norm` over time.  
  - Component contributions and reason codes used later in Action Logic.

### 4. Governance & Sustainability Checks

- Ensure cost/energy/carbon components are:

  - Derived from governance‑approved telemetry sources.  
  - In line with sustainability reporting requirements.  

- CI should fail if:

  - Components are removed without an updated governance review.  
  - Carbon/energy components are silently disabled.

---

## 🧠 Story Node & Focus Mode Integration

Score functions power explanations like:

- “How urgent is it to run this pipeline right now?”  
- “Why is the autonomy score low even though freshness is good?”  
- “How much do cost or carbon constraints contribute to decisions?”

Focus Mode can use:

- `score.normalized`,  
- `score.components`,  
- `score.weights`,

to generate compact narratives, for example:

~~~text
This pipeline's normalized autonomy score is 0.18.
Freshness and trust are high, but cost and carbon components
are negative, pulling the overall score into the slow band.
~~~

A Story Node anchor might be:

~~~text
Related Story Node:
urn:kfm:story-node:pipelines:autonomy-matrix:decider:score-functions:overview
~~~

Story Nodes must:

- Reflect score‑function behavior as described here.  
- Defer to `action-logic.md` for how scores map into actions.  
- Avoid inventing new scoring dimensions not present in configs or telemetry.

---

## 🕰️ Version History

| Version    | Date       | Summary                                                                                                       |
|-----------:|------------|---------------------------------------------------------------------------------------------------------------|
| **v11.2.4**| 2025-12-06 | Initial Autonomy Decider score‑functions design: component definitions, aggregation, normalization, and CI.   |

---

<div align="center">

📊 **KFM v11 — Autonomy Decider Score Functions**  
Structured Metrics · Normalized Scores · FAIR+CARE‑Aligned Autonomy  

[🧠 Decider Spec](README.md) · [🧠 Action Logic](action-logic.md) · [🧠 State Machine](designs/state-machine.md) · [🤖 Autonomy Matrix](../README.md)

</div>

