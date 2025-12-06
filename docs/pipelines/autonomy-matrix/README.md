---
title: "🤖 KFM v11 — Autonomy Matrix for Self-Balancing Pipelines (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed pipeline control layer that self-balances KFM ingestion, ETL, AI, and refresh pipelines using cost, energy, carbon, freshness, provenance, and CARE-aware signals."
path: "docs/pipelines/autonomy-matrix/README.md"
version: "v11.2.4"
last_updated: "2025-12-05"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability · Sustainability · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x autonomy-contract compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../releases/v11.2.4/autonomy-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/autonomy-matrix-v1.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

status: "Active / Enforced"
doc_kind: "Pipeline-Control-Layer"
header_profile: "standard"
footer_profile: "standard"

intent: "autonomy-matrix"
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

semantic_intent:
  - "governance"
  - "control-plane"
  - "reliability"
  - "sustainability"
category: "Pipelines · Autonomy · Governance"

sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Internal"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: false

data_steward: "Reliability · Sustainability · FAIR+CARE Council"
ttl_policy: "Indefinite (subject to architecture changes)"
sunset_policy: "Supersede when v12 autonomy architecture is adopted"

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
  - "docs/pipelines/autonomy-matrix/README.md@v11.2.3"
  - "docs/pipelines/autonomy-matrix/README.md@v11.2.2"
  - "docs/pipelines/reliability/README.md"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/docs-pipelines-autonomy-matrix-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/docs-pipelines-autonomy-matrix-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "mutable"

doc_uuid: "urn:kfm:doc:pipelines:autonomy-matrix:v11.2.4"
semantic_document_id: "kfm-pipelines-autonomy-matrix-v11.2.4"
event_source_id: "ledger:kfm:doc:pipelines:autonomy-matrix:v11.2.4"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "3d-context-render"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "governance-override"
  - "unverified-architectural-claims"
  - "narrative-fabrication"

transform_registry:
  allowed:
    - "summary"
    - "timeline-generation"
    - "semantic-highlighting"
    - "3d-context-render"
    - "a11y-adaptations"
    - "diagram-extraction"
    - "metadata-extraction"
  prohibited:
    - "content-alteration"
    - "speculative-additions"
    - "governance-override"
    - "unverified-architectural-claims"
    - "narrative-fabrication"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧭 Context"
    - "⚙️ Decision Model"
    - "🎯 Actions"
    - "🛡️ Governance Evidence & Telemetry"
    - "🧪 Templates & Contracts"
    - "🧩 Relationship to Reliability & Sustainability"
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
requires_directory_layout_section: true
requires_governance_links_in_footer: true

deprecated_fields:
  - "old_markdown_standard_v10.4"
---

<div align="center">

# 🤖 **KFM v11 — Autonomy Matrix for Self-Balancing Pipelines**  
`docs/pipelines/autonomy-matrix/README.md`

**Purpose:**  
Define the **governance-safe pipeline control layer** that keeps KFM ingestion, ETL, AI, and refresh tasks **stable, efficient, ethical, and sustainable** by issuing deterministic actions — **resume · slow · pause · escalate** — based on cost, energy, carbon, freshness, provenance, and CARE-aware signals.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue "Master Coder Protocol v6.3")]() ·
[![KFM–PDC v11](https://img.shields.io/badge/KFM%E2%80%93PDC-v11.0-informational "Pipeline Contract v11")]() ·
[![Reliability](https://img.shields.io/badge/Domain-Reliability-success "Reliability & Autonomy")]() ·
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold "FAIR+CARE Compliant")]()

</div>

---

## 📘 Overview

The **Autonomy Matrix** is the KFM v11 pipeline control plane that:

- Continuously evaluates pipeline state using:
  - **Cost**, **energy**, and **carbon** burn rates  
  - **Freshness**, **backlog**, and **lag** against SLOs  
  - **Data trust**, **validation results**, and **lineage depth**  
  - **FAIR+CARE** labels, **sensitivity flags**, and sovereignty rules  
- Issues deterministic, explainable actions:
  - **resume** — run at full configured rate  
  - **slow** — reduce rate or concurrency  
  - **pause** — halt until conditions are safe  
  - **escalate** — require human review  

Every decision is:

- **Deterministic** — given the same inputs, the same decision and score are produced.  
- **Explainable** — all contributing metrics, gates, and thresholds are logged as evidence.  
- **Provable** — decisions emit PROV-compliant events, OpenLineage spans, and energy/carbon telemetry.

The Autonomy Matrix sits downstream of deterministic ETL and cataloging (STAC/DCAT/PROV) and upstream of **Neo4j**, **API**, and **UI** layers. It does not mutate raw data; it mutates **pipeline run-state**.

---

## 🗂️ Directory Layout

```text
docs/pipelines/autonomy-matrix/
│
├── 📄 README.md                                  # This file (Autonomy Matrix overview & contract)
│
├── 📂 decider/                                   # LangGraph / control-plane autonomy kernel
│   ├── 📄 README.md                              # High-level architecture and state machine
│   ├── 📄 score-functions.md                     # Freshness, trust, cost, energy, carbon scoring
│   ├── 📄 action-logic.md                        # Decision table → resume/slow/pause/escalate
│   └── 📄 contracts.md                           # Semantics for autonomy actions & invariants
│
├── 📂 pipeline-profiles/                         # Per-pipeline autonomy contracts (YAML)
│   ├── 📄 hydro-hrrr-downscale.yaml
│   ├── 📄 atmo-hrrr-smart.yaml
│   ├── 📄 sat-sentinel1.yaml
│   └── 📄 <other-pipelines>.yaml
│
├── 📂 gates/                                     # Governance & anomaly gates (reusable)
│   ├── 📄 README.md                              # Gate composition, templates, and priorities
│   ├── 📄 care-governance.md                     # CARE compliance, sensitivity, redaction policies
│   ├── 📄 cost-energy-gates.md                   # kWh, CO₂e, cloud cost, burn-rate triggers
│   ├── 📄 freshness-stall-gate.md                # Max-lag, upstream health, backlog limits
│   └── 📄 cardinality-guard.md                   # OTel metric cardinality protection & SLOs
│
├── 📂 telemetry/                                 # Runtime decisions + OpenLineage logs
│   ├── 📄 README.md                              # Schemas, retention, and STAC/DCAT mapping
│   ├── 📄 autonomy-decisions.jsonl               # One record per decision (score + evidence)
│   ├── 📄 action-events.jsonl                    # OpenLineage autonomy events (resume/slow/...)
│   └── 📄 carbon-energy-history.jsonl            # Long-horizon energy/carbon/cost histories
│
└── 📂 examples/                                  # Example usage & reference implementations
    ├── 📄 README.md                              # How to read & replay examples
    ├── 📄 sample-decision.md                     # Fully-worked decision w/ evidence breakdown
    └── 📄 sample-pipeline-profile.yaml           # Template for new autonomy profiles
```

**Author rules:**

- Each directory **MUST** have a `README.md` describing purpose, contracts, and links to schemas.  
- All YAML in `pipeline-profiles/` **MUST** be schema-validated and versioned.  
- All telemetry file formats **MUST** conform to `autonomy-matrix-v1` telemetry schema.  
- No code, configs, or data in `docs/`; they live in `src/`, `config/`, `data/`, and are merely referenced here.

---

## 🧭 Context

Autonomy is defined relative to the canonical KFM pipeline:

> **Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j knowledge graph → API layer → React/MapLibre/Cesium frontend → Story Nodes → Focus Mode**

The Autonomy Matrix:

- Consumes:
  - Pipeline run-metadata (start/end times, statuses, failures)
  - STAC/DCAT catalogs (what datasets exist, where, and with what metadata)
  - PROV/lineage graphs (what entities and activities produced which artifacts)
  - Energy/carbon/cost telemetry
  - FAIR+CARE + sovereignty labels for datasets and pipelines
- Emits:
  - **Autonomy decisions** per pipeline run
  - **Action events** (resume/slow/pause/escalate) with full evidence
  - **Guardrail violations** (gates triggered) with remediation hints

It is a **control plane**, not a data plane: it does not transform data; it governs **whether and how** data pipelines are allowed to run.

---

## ⚙️ Decision Model

At the core is a scoring function that maps pipeline state → scalar score:

```text
score =
  w_fresh * FreshnessScore() +
  w_urg   * TemporalRelevance() +
  w_trust * DataTrust() -
  w_cost  * CostBurnRate() -
  w_energy * EnergyKWhRate() -
  w_carbon * CarbonCO2eRate()
```

**Components:**

- `FreshnessScore()`  
  - Measures lag vs SLO (e.g., max_lag ≤ 2h).  
  - Penalties for backlog growth, upstream stalls, or repeated retries.
- `TemporalRelevance()`  
  - Distinguishes P0 (severe weather / safety), P1 (daily products), P3 (offline analytics).  
  - Higher for “nowcasting” or real-time products; lower for archival backfills.
- `DataTrust()`  
  - Derived from validation outcomes (Great Expectations / schema checks), lineage depth, and PROV completeness.  
  - Penalizes missing provenance, failing QA checks, or “unknown” sources.
- `CostBurnRate()`  
  - Normalized cost per unit time vs budget (USD/hr vs monthly cap).  
  - Includes infra cost, license cost, and storage churn (e.g., repeated rewrites).
- `EnergyKWhRate()` / `CarbonCO2eRate()`  
  - From energy & carbon telemetry, normalized against monthly or annual limits.  
  - Includes per-region carbon intensity and hardware energy profiles.

The autonomy kernel:

- Evaluates the score at configurable intervals (e.g., per run, per window).
- Applies **gates** that can override the numeric score:
  - CARE governance violations (sensitive data mishandling)
  - Critical cost/energy/carbon burn (“kill-switch” thresholds)
  - Metric cardinality explosions
  - Upstream health and freshness crisis

If a gate triggers, it can force **pause** or **escalate**, regardless of the score.

---

## 🎯 Actions

The Autonomy Matrix maps `{score, gates, context}` → one of four canonical actions:

| Action       | Meaning                        | Typical Triggers                                                                 |
|--------------|--------------------------------|-----------------------------------------------------------------------------------|
| **resume**   | Full speed                     | High urgency, within cost/energy/carbon budgets, all gates clear                  |
| **slow**     | Reduced rate / concurrency     | Rising burn rates, near carbon or cost cap, medium urgency                        |
| **pause**    | Halt new work until safe       | CARE violation, severe anomaly, runaway lag/cost, upstream instability            |
| **escalate** | Require human decision / review| Conflicting signals, novel failure modes, governance uncertainty, multi-gate conflict |

**Action semantics:**

- `resume`:
  - Pipelines may run at configured parallelism / schedule.
  - No additional human intervention required.
- `slow`:
  - Reduce concurrency, increase backoff, or switch to cheaper instances.
  - Possibly limit scope (subset of regions or products).
- `pause`:
  - No new runs allowed. In-flight runs may be:
    - Gracefully allowed to finish, or
    - Canceled based on policy.
  - Requires explicit human approval (and a recorded rationale) to change state.
- `escalate`:
  - Autonomy defers to humans (via alerts to on-call / councils).
  - Human decision is recorded and becomes training data for future patterns.

Per-pipeline **autonomy contracts** (see below) define *how* `slow`, `pause`, and `escalate` are implemented at runtime (e.g., which knobs to turn).

---

## 🛡️ Governance Evidence & Telemetry

Every decision produces a structured record (one line JSON per decision) in `telemetry/autonomy-decisions.jsonl`.

**Example decision record:**

```json
{
  "timestamp": "2025-12-05T10:23:42Z",
  "pipeline": "hydro/hrrr-downscale",
  "decision_id": "urn:kfm:autonomy:decision:hydro-hrrr-downscale:20251205T102342Z",
  "action": "slow",
  "score": 0.41,
  "weights": {
    "freshness": 0.35,
    "urgency": 0.40,
    "trust": 0.25,
    "cost": 0.60,
    "energy": 0.40,
    "carbon": 0.50
  },
  "reasons": [
    "burn_rate_over: cost",
    "carbon_budget: 82% month-to-date"
  ],
  "evidence": {
    "freshness": {
      "lag_minutes": 22,
      "max_lag_minutes": 120,
      "backlog_runs": 1
    },
    "cost": {
      "usd_per_hour": 14.3,
      "monthly_cap_usd": 1200,
      "mtd_spend_usd": 984.2
    },
    "energy": {
      "kwh_per_hour": 6.1,
      "mtd_kwh": 320.5,
      "energy_cap_kwh": 400
    },
    "carbon": {
      "kgco2e_per_hour": 2.3,
      "mtd_kgco2e": 125.8,
      "carbon_cap_kgco2e": 150
    }
  },
  "governance": {
    "care_label": "Sensitive-Waters",
    "sovereignty_policy": "dynamic-h3-generalization-v2",
    "priority_band": "P1"
  },
  "provenance": {
    "run_ids": [
      "urn:kfm:pipeline:hydro-hrrr-downscale:run:20251205T093000Z"
    ],
    "stac_items": [
      "kfm-hydro-hrrr-downscale-20251205T09Z"
    ],
    "prov_entities": [
      "urn:kfm:prov:entity:hydro-hrrr-downscale:20251205T09Z"
    ]
  }
}
```

**Telemetry streams:**

- `autonomy-decisions.jsonl`  
  - One record per decision, immutable, append-only.  
  - Indexed as a STAC Item collection and as DCAT datasets for discoverability.
- `action-events.jsonl`  
  - Operational events: actual **resume/slow/pause/escalate** actions taken in orchestrators (Airflow, Dagster, LangGraph).  
  - Mapped to OpenLineage `runEvent` with `eventType` = `autonomy.action`.
- `carbon-energy-history.jsonl`  
  - Aggregated energy/carbon/cost time series per pipeline and environment.  
  - Used for long-range planning and gating.

Telemetry records are **PROV-aligned**: entities (decisions), activities (autonomy-evaluations), and agents (autonomy kernel, reliability council, pipeline owners) can be reconstructed into a lineage graph.

---

## 🧪 Templates & Contracts

### 1. Pipeline Autonomy Profile Template

Per-pipeline autonomy contracts live in `docs/pipelines/autonomy-matrix/pipeline-profiles/*.yaml`.

**Template:**

```yaml
pipeline: "hydro/hrrr-downscale"
owner: "team-hydro@kfm.example.org"

slos:
  availability:
    target: 0.985
    window: "30d"
    error_budget: 0.015
  freshness:
    max_lag: "2h"
  cost:
    monthly_cap_usd: 1200
  energy:
    monthly_cap_kwh: 250
  carbon:
    monthly_cap_kgco2e: 65

governance:
  care_label: "Sensitive-Waters"
  sensitivity: "Elevated"
  sovereignty_policy: "dynamic-h3-generalization-v2"
  priority_band: "P1"   # P0–P4, where P0 is highest urgency
  data_domains:
    - "hydrology"
    - "climate"

autonomy:
  actions:
    - "resume"
    - "slow"
    - "pause"
    - "escalate"
  min_human_review_for_pause: true
  min_human_review_for_escalate: true
  preferred_slow_mechanisms:
    - "reduce_concurrency"
    - "increase_backoff"
    - "lower_resolution"
  allowed_pause_duration: "24h"

gates:
  enabled:
    - "care-governance"
    - "cost-energy"
    - "freshness-stall"
    - "cardinality"
  overrides:
    care-governance:
      hard_fail_on_violation: true
    cost-energy:
      burn_rate_redline: 0.9          # 90% of budget triggers hard pause
    freshness-stall:
      max_consecutive_failures: 3
    cardinality:
      max_label_cardinality: 500

telemetry:
  decision_stream: "autonomy-decisions.jsonl"
  action_stream: "action-events.jsonl"
  energy_carbon_stream: "carbon-energy-history.jsonl"
```

**Contract rules:**

- Every production pipeline **MUST** have a profile.  
- Profiles are **immutable-by-default**; changes require PR + review by Reliability & FAIR+CARE councils.  
- Profiles are schema-validated and referenced in:
  - `src/pipelines/*/` configs
  - `.github/workflows/kfm-ci.yml` gating jobs
  - Story Nodes describing operational behavior

---

## 🧩 Relationship to Reliability & Sustainability

The Autonomy Matrix is the **actuator** for reliability and sustainability policies defined elsewhere:

- **Reliability docs** (`docs/pipelines/reliability/`) define:
  - SLOs, error budgets, incident response, replay & rollback procedures.
- **Energy & carbon docs** (`docs/standards/energy/`, telemetry schemas) define:
  - How to measure kWh/CO₂e, acceptable budget bands, and reporting obligations.
- **CARE & sovereignty docs** (`docs/standards/faircare/`, `docs/sovereignty/`) define:
  - Masking, aggregation, and access rules for sensitive or Indigenous data.

Autonomy then:

- Reads the SLOs, budgets, and labels from the pipeline profile.
- Evaluates live telemetry against those constraints.
- Determines whether pipelines may continue operating as configured.

Any change to:

- Pipeline **SLOs**  
- Energy/carbon/cost **budgets**  
- CARE **labels** or **sovereignty policies**

**MUST** be reflected in:

- The corresponding `pipeline-profiles/*.yaml` entry, and  
- Accepted via reviewed PR before it takes effect in the Autonomy Matrix.

---

## 🕰️ Version History

| Version    | Date       | Summary                                                                                                                       |
|-----------:|-----------:|--------------------------------------------------------------------------------------------------------------------------------|
| **v11.2.4**| 2025-12-05 | Aligned with KFM-MDP v11.2.4. Added full emoji directory layout, telemetry schemas, decision scoring details, and gates model. |
| v11.2.3    | 2025-12-02 | Initial Autonomy Matrix rollout. Defined core actions (resume/slow/pause/escalate) and basic cost/energy/carbon scoring.      |
| v11.2.2    | 2025-11-27 | Pre-Autonomy draft notes integrated into reliability framework; no distinct autonomy contract yet.                            |

---

<div align="center">

🤖 **KFM v11 — Autonomy Matrix for Self-Balancing Pipelines**  
Reliability-Aware · Sustainability-Conscious · FAIR+CARE-Governed  

[📘 Pipelines Index](../README.md) · [🛡 Reliability Framework](../reliability/README.md) · [⚖ Governance](../../governance/ROOT-GOVERNANCE.md)

</div>
