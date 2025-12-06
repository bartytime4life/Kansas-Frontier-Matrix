---
title: "🧪 KFM v11 — Autonomy Decider Horizon Tuning Experiments"
description: "Design and simulation of decision horizon and aggregation-window experiments for the KFM v11 Autonomy Matrix decider."
path: "docs/pipelines/autonomy-matrix/decider/designs/variants/experiments/horizon-tuning.md"
version: "v11.2.4"
last_updated: "2025-12-05"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability · Sustainability · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "Aligned with Autonomy Matrix v11.2.x"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.4/autonomy-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/autonomy-matrix-v1.json"
energy_schema: "../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../sovereignty/INDIGENOUS-DATA-PROTECTION.md"
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

intent: "autonomy-matrix-decider-variants-experiments-horizon"
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
  - "experiments"
  - "time-series"

category: "Pipelines · Autonomy · Governance · Experiments · Horizons"

sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Internal"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: false

data_steward: "Reliability · Sustainability · FAIR+CARE Council"
ttl_policy: "Indefinite (subject to architecture changes)"
sunset_policy: "Supersede when Autonomy Matrix v12 decider experiment framework is adopted"

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
  - "docs/pipelines/autonomy-matrix/decider/designs/variants/experiments/README.md@v11.2.4"
  - "docs/pipelines/autonomy-matrix/decider/designs/variants/README.md@v11.2.4"
  - "docs/pipelines/autonomy-matrix/decider/designs/README.md@v11.2.4"
  - "docs/pipelines/autonomy-matrix/decider/README.md@v11.2.4"
  - "docs/pipelines/autonomy-matrix/README.md@v11.2.4"
  - "docs/pipelines/reliability/README.md"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/docs-pipelines-autonomy-decider-variants-experiments-horizon-tuning-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/docs-pipelines-autonomy-decider-variants-experiments-horizon-tuning-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "mutable"

doc_uuid: "urn:kfm:doc:pipelines:autonomy-matrix:decider:designs:variants:experiments:horizon-tuning:v11.2.4"
semantic_document_id: "kfm-pipelines-autonomy-matrix-decider-variants-experiments-horizon-tuning-v11.2.4"
event_source_id: "ledger:kfm:doc:pipelines:autonomy-matrix:decider:designs:variants:experiments:horizon-tuning:v11.2.4"

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
    - "🧪 Experiment Profiles"
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

# 🧪 **KFM v11 — Autonomy Decider Horizon Tuning Experiments**  
`docs/pipelines/autonomy-matrix/decider/designs/variants/experiments/horizon-tuning.md`

**Purpose:**  
Define experiment families that tune the **decision horizon and aggregation windows**  
used by the Autonomy Decider — balancing **responsiveness vs. stability** for KFM pipelines  
under reliability, sustainability, and FAIR+CARE constraints.

</div>

---

## 📘 Overview

This document describes experiments where the Autonomy Decider:

- Changes **how often** decisions are made (per-run, per-window, hybrid).  
- Modifies **how telemetry is aggregated** over time (sliding windows, tumbling windows, EWMA).  
- Studies the impact on:
  - Action thrash (`resume ↔ slow ↔ pause` oscillations),  
  - SLO performance (freshness, availability),  
  - Cost/energy/carbon efficiency.

Horizon tuning is about **time**, not just thresholds or fairness:

- Short horizons → fast reaction, potential thrash.  
- Long horizons → stable behavior, potential lag behind real-world changes.

Experiments here are **non-normative**; they guide future changes to canonical behavior.

---

## 🧭 Context

Decision horizons interact with:

- **Autonomy profiles**  
  (e.g., desired freshness, cost/energy/carbon budgets, sensitivity to short-term spikes).  
- **Telemetry cadence**  
  (how frequently metrics are produced and ingested).  
- **Orchestrator behavior**  
  (how often pipelines can start/stop; granularity of schedules).  
- **Governance expectations**  
  (how quickly autonomy must react to serious anomalies vs. normal fluctuations).

Key questions:

- Should autonomy decide **per-run** or **per time-window** (e.g., every 5 minutes)?  
- How much **history** should influence a decision (last N runs, last M minutes)?  
- How do horizon choices differ between:
  - High-urgency synthetic analogs of safety-critical workloads vs.  
  - Low-urgency backfills or archival tasks?

Horizon tuning experiments use synthetic or anonymized telemetry fixtures to explore these tradeoffs before any production change.

---

## 🧪 Experiment Profiles

Each horizon tuning experiment should be described by a structured profile, similar to other experiment docs.

### Generic Horizon Experiment Template

~~~yaml
experiment_id: "autonomy-horizon-5m-vs-30m-v1"
title: "5-Minute vs 30-Minute Decision Horizons"
status: "exploratory"          # exploratory | candidate | rejected | adopted
target_version: "v11.3.x"
owner_team: "reliability-autonomy@kfm"
created_at: "2025-12-05"

scope:
  pipelines:
    - "example/hydro-*"
    - "example/atmo-*"
  environments:
    - "staging"
  priority_bands:
    - "P0"
    - "P1"
    - "P3"

hypothesis:
  text: >
    Moving from per-run decisions to a 5-minute sliding-window horizon will reduce
    action thrash by at least 40% while keeping SLO violations within 2% of current levels.
    A 30-minute horizon is expected to be too sluggish for P0/P1 workloads.

horizon_policy:
  baseline:
    mode: "per-run"
    window: null
    smoothing: "none"
  experimental_short:
    mode: "sliding-window"
    window: "5m"
    smoothing: "ewma"
  experimental_long:
    mode: "sliding-window"
    window: "30m"
    smoothing: "ewma"

variants:
  baseline:
    config_ref: "config/autonomy/decider/horizon-per-run.yaml"
  short_window:
    config_ref: "config/autonomy/decider/horizon-5m-ewma.yaml"
  long_window:
    config_ref: "config/autonomy/decider/horizon-30m-ewma.yaml"

fixtures:
  telemetry:
    - "fixtures/horizon-daily-vs-hourly.json"
    - "fixtures/samples/high-lag-low-cost.json"

metrics_of_interest:
  - "action_thrash_rate"
  - "p0_slo_violation_rate"
  - "p1_slo_violation_rate"
  - "average_lag_change"
  - "cost_energy_carbon_drift"
~~~

### Family 1 — Per-Run vs Sliding Windows

Goal:

- Compare **per-run** decisions with **sliding-window** decisions:
  - Per-run: every pipeline run triggers an autonomy decision.  
  - Sliding-window: autonomy decides based on aggregated metrics over a time window (e.g., last 5 minutes).

Questions:

- Does sliding-window smoothing reduce action thrash without hiding important signals?  
- Does it delay critical decisions in high-urgency workloads?

### Family 2 — Short vs Long Windows

Goal:

- Compare **short** and **long** windows, e.g., 5 minutes vs 30 minutes vs 60 minutes.

Questions:

- At what window length do decisions become **too sluggish** for P0/P1 pipelines?  
- At what length do we get **maximal stability** without unacceptable SLO degradation?  
- Do lower-priority pipelines benefit disproportionately from longer windows (e.g., fewer pauses)?

### Family 3 — Smoothing vs No Smoothing

Goal:

- Compare decisions with and without additional smoothing (e.g., EWMA) of telemetry metrics.

Questions:

- Does smoothing reduce sensitivity to noisy spikes in cost/energy/carbon/math metrics?  
- Does smoothing introduce **lag** that harms responsiveness to true anomalies?  
- Can we make smoothing **priority-sensitive** (more smoothing for low-priority, less for high-priority)?

---

## 📦 Data & Metadata

Horizon tuning relies on:

- **Time-series telemetry** that covers multiple runs/windows, not single snapshots:  
  - Per-pipeline sequences of lag, cost, energy, carbon, trust, etc.  
- **Sample fixtures** such as:
  - `fixtures/horizon-daily-vs-hourly.json` — synthetic daily vs hourly cadence scenarios.  
  - `fixtures/samples/high-lag-low-cost.json` — scenarios where lag is high but resource usage is low.

A minimal time-series fixture might look like:

~~~json
{
  "pipeline": "example/hydro-hrrr",
  "priority_band": "P1",
  "samples": [
    {
      "timestamp": "2025-12-05T00:00:00Z",
      "lag_minutes": 10,
      "cost_usd": 4.2,
      "kwh": 2.1,
      "kgco2e": 0.9
    },
    {
      "timestamp": "2025-12-05T00:05:00Z",
      "lag_minutes": 12,
      "cost_usd": 4.4,
      "kwh": 2.2,
      "kgco2e": 0.9
    }
  ]
}
~~~

All IDs and values:

- Must be **synthetic** or strongly anonymized.  
- Should be realistic enough to expose edge cases (spikes, dips, plateau behavior).  

Horizon experiments may also propose new config fields (design-only until schemas are updated), such as:

~~~yaml
autonomy:
  horizon:
    mode: "sliding-window"   # per-run | sliding-window | tumbling-window
    window: "5m"
    smoothing: "ewma"        # none | ewma | median
    smoothing_half_life: "15m"
~~~

These fields remain **proposed** until reflected in schemas and canonical docs.

---

## 🧪 Validation & CI/CD

Horizon tuning experiments must comply with the same rigorous CI standards as other Autonomy experiments:

1. **Schema Validation**

   - Telemetry fixtures must validate against:
     - Base telemetry schema (with time-series support or wrappers).  
   - Experimental configs must either:
     - Use existing fields, or  
     - Be validated against experimental schemas gated by branches or flags.

2. **Time-Series Replays**

   - For each experiment profile:
     - Run the canonical decider (per-run or current horizon) over the fixture sequence.  
     - Run the experimental decider (different horizon/smoothing).  
   - Record action sequences over time:
     - How often the action changes,  
     - How long the system stays in each state (resume/slow/pause/escalate).

3. **Metrics & Guardrails**

   - Key metrics:
     - **action_thrash_rate** — number of state changes per hour/day.  
     - **slo_violation_rate** — per-priority band.  
     - **mean/median lag** vs baseline.  
     - **cost/energy/carbon drift** — impact on sustainability metrics.

   - Guardrails:
     - No runaway thrash or oscillation loops.  
     - No unacceptable SLO degradation for high-priority pipelines.  
     - No behavior that undermines CARE-related protections (e.g., delayed reactions to sensitive anomalies).

4. **Reporting**

   - CI should generate concise reports (outside `docs/`) summarizing horizon experiment outcomes:  
     - “5m window reduced thrash by 45% with <1% SLO degradation for P1; 30m window caused 5% SLO degradation.”

Experiments that pass these checks may be considered for `candidate` or `adopted` status in future releases.

---

## 🧠 Story Node & Focus Mode Integration

Horizon tuning experiments enable narratives like:

- “Why did autonomy stop thrashing between resume and slow for this pipeline?”  
- “What changed when we moved to a 5-minute window for decider decisions?”  
- “How does smoothing affect our view of cost and carbon spikes?”

To support Story Node and Focus Mode:

- Keep experiment family descriptions short and clearly labeled.  
- Emphasize:
  - The **before/after** story (baseline vs experimental),  
  - Key numerical results (thrash reduction, SLO impact),  
  - Governance decisions (e.g., why a particular horizon was rejected).

Example Story Node anchor:

~~~text
Related Story Node:
urn:kfm:story-node:pipelines:autonomy-matrix:decider:experiment:horizon-tuning:5m-vs-30m
~~~

Story Nodes must clearly differentiate between **current canonical horizon behavior** and **experimental variants**.

---

## 🕰️ Version History

| Version    | Date       | Summary                                                                                                                      |
|-----------:|------------|------------------------------------------------------------------------------------------------------------------------------|
| **v11.2.4**| 2025-12-05 | Initial creation of horizon tuning experiment doc. Defines experiment families (per-run vs windows, short vs long, smoothing) and CI/gov hooks. |

---

<div align="center">

🧪 **KFM v11 — Autonomy Decider Horizon Tuning Experiments**  
Time-Aware Autonomy · Stable Yet Responsive Control · FAIR+CARE-Governed Horizons  

[🧪 Experiment Registry](README.md) · [📦 Fixtures](fixtures/README.md) · [🧠 Decider Variants](../README.md)

</div>

