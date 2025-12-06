---
title: "🧪 KFM v11 — Autonomy Decider Cost/Energy/Carbon Threshold Experiments"
description: "Design and simulation of cost, energy, and carbon threshold & burn-band experiments for the KFM v11 Autonomy Matrix decider."
path: "docs/pipelines/autonomy-matrix/decider/designs/variants/experiments/cost-energy-thresholds.md"
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

intent: "autonomy-matrix-decider-variants-experiments-cost-energy-thresholds"
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

category: "Pipelines · Autonomy · Governance · Experiments · Thresholds"

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

json_schema_ref: "schemas/json/docs-pipelines-autonomy-decider-variants-experiments-cost-energy-thresholds-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/docs-pipelines-autonomy-decider-variants-experiments-cost-energy-thresholds-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "mutable"

doc_uuid: "urn:kfm:doc:pipelines:autonomy-matrix:decider:designs:variants:experiments:cost-energy-thresholds:v11.2.4"
semantic_document_id: "kfm-pipelines-autonomy-matrix-decider-variants-experiments-cost-energy-thresholds-v11.2.4"
event_source_id: "ledger:kfm:doc:pipelines:autonomy-matrix:decider:designs:variants:experiments:cost-energy-thresholds:v11.2.4"

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
requires_directory_layout_section: true
requires_governance_links_in_footer: true

deprecated_fields:
  - "old_markdown_standard_v10.4"
---

<div align="center">

# 🧪 **KFM v11 — Autonomy Decider Cost/Energy/Carbon Threshold Experiments**  
`docs/pipelines/autonomy-matrix/decider/designs/variants/experiments/cost-energy-thresholds.md`

**Purpose:**  
Define and organize experiments that adjust **cost, energy, and carbon thresholds & burn-bands**  
for the Autonomy Decider, so that KFM pipelines can be tuned for **sustainability, reliability,  
and FAIR+CARE governance** without breaking the canonical autonomy contract.

</div>

---

## 📘 Overview

This document describes experiment families where the Autonomy Decider:

- Adjusts **thresholds** and **burn-band curves** for:
  - Cost (USD/hour, month-to-date spend),  
  - Energy (kWh/hour, month-to-date kWh),  
  - Carbon (kgCO₂e/hour, month-to-date CO₂).  
- Examines how those adjustments influence:
  - Pipeline actions (`resume`, `slow`, `pause`, `escalate`),  
  - SLO adherence (freshness, availability),  
  - Budget utilization and sustainability objectives.

These experiments are **non-normative**:

- They propose changes to configuration and decision logic,  
- They must be evaluated via **offline simulation** and **governance review**,  
- They only become normative after updates to the canonical Autonomy Matrix and Decider specs.

---

## 🧭 Context

Cost/energy/carbon thresholds sit at the intersection of:

- **Reliability**  
  - Pipelines must meet SLOs (e.g., freshness, availability) where possible.
- **Sustainability**  
  - KFM must remain within cost, energy, and carbon budgets at project, tenant, and cluster levels.
- **FAIR+CARE & Sovereignty**  
  - Some pipelines are more sensitive or more socially critical than others:
    - E.g., synthetic analogs of safety-related or Indigenous data workflows.

Existing Autonomy behavior:

- Uses weights (`w_cost`, `w_energy`, `w_carbon`) and thresholds defined in pipeline profiles.  
- Applies **gates** (e.g., cost-energy gate) that can override scores when thresholds are crossed.  

Experiments in this document explore:

- Different **shapes** of burn-bands (step functions vs. smooth ramps).  
- Different **redline positions** (e.g., hard cut at 90% of monthly carbon budget).  
- Different **priority-sensitive reactions** (P0 vs. P3 pipelines under the same budget pressures).

---

## 🧪 Experiment Profiles

Each cost/energy/carbon experiment is described via a structured profile (conceptual template):

~~~yaml
experiment_id: "autonomy-thresholds-cec-v1"
title: "Cost/Energy/Carbon Two-Band Thresholds for P1/P3 Pipelines"
status: "exploratory"           # exploratory | candidate | rejected | adopted
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
    - "P1"
    - "P3"

hypothesis:
  text: >
    Introducing a two-band threshold policy (warning at 70%, hard redline at 90% of budget)
    for cost, energy, and carbon will reduce unnecessary 'pause' actions on P1 pipelines,
    while keeping overall monthly budgets within 5% of their targets.

variants:
  baseline:
    description: "Current canonical thresholds and burn-bands"
    config_ref: "config/autonomy/decider/canonical-thresholds.yaml"
  experimental:
    description: "Two-band thresholds with smoother slope in the 70–90% region"
    config_ref: "config/autonomy/decider/cec-two-band-v1.yaml"

fixtures:
  telemetry:
    - "fixtures/thresholds-sample.json"
    - "fixtures/samples/carbon-tight-budget.json"

metrics_of_interest:
  - "num_action_changes"
  - "pause_rate_p1_vs_p3"
  - "budget_overrun_probability"
  - "average_carbon_margin"
~~~

### Example Experiment Families

1. **Two-Band Thresholds (Warning + Hard Redline)**  
   - Introduce **warning band** (e.g., 70–90% of monthly budget):
     - Increase likelihood of `slow`, but avoid `pause` where SLOs are at risk.  
   - Keep **hard redline** (e.g., 90–100%):
     - Strong `pause` bias for lower-priority pipelines.

2. **Smooth Burn-Bands (Gradual Penalty Curves)**  
   - Replace piecewise-linear or step thresholds with a smooth curve:
     - Penalty grows smoothly as budget utilization rises.  
   - Goal: avoid abrupt behavior changes at single thresholds.

3. **Priority-Weighted Redlines**  
   - Different thresholds for different priority bands:
     - P0/P1: later redlines, more tolerance near budget caps,  
     - P3/P4: earlier redlines, more aggressive slowing/pausing.

Each family must:

- Specify its **experiment_id**,  
- Reference relevant **configs** and **fixtures**,  
- Provide clear **success criteria** (what “good” looks like).

---

## 📦 Data & Metadata

Cost/energy/carbon threshold experiments touch:

- **Autonomy profile fields** (in `pipeline-profiles/*.yaml`):
  - `slos.cost.monthly_cap_usd`
  - `slos.energy.monthly_cap_kwh`
  - `slos.carbon.monthly_cap_kgco2e`
  - Potential proposed fields (design-only, non-normative until schemas updated):
    - `autonomy.thresholds.cost.warning_band`
    - `autonomy.thresholds.energy.warning_band`
    - `autonomy.thresholds.carbon.warning_band`

- **Telemetry fields** (fixtures + real telemetry):
  - `cost.usd_per_hour`, `cost.mtd_spend_usd`, `cost.monthly_cap_usd`  
  - `energy.kwh_per_hour`, `energy.mtd_kwh`, `energy.energy_cap_kwh`  
  - `carbon.kgco2e_per_hour`, `carbon.mtd_kgco2e`, `carbon.carbon_cap_kgco2e`

- **Governance context**:
  - Priority bands (`P0`–`P4`),
  - CARE labels and sovereignty policies (may affect which pipelines are slowed/paused first).

When proposing new config fields or semantics:

- Mark them clearly as **proposed** until:
  - Schemas in `schemas/telemetry/` and `schemas/json/` are updated,  
  - Canonical docs are revised.

Example (non-normative, design-only snippet):

~~~yaml
autonomy:
  thresholds:
    cost:
      warning_band: 0.70
      redline: 0.90
    energy:
      warning_band: 0.70
      redline: 0.90
    carbon:
      warning_band: 0.70
      redline: 0.90
~~~

---

## 🧪 Validation & CI/CD

Cost/energy/carbon experiments must pass through a **simulation-first** pipeline:

1. **Schema & config validation**
   - Experimental configs must validate against:
     - Existing schemas (if fields are already supported), or  
     - Experimental schemas in branches earmarked for future versions.

2. **Fixture-based replay**
   - For each experiment profile:
     - Run canonical and experimental decider logic on:
       - `fixtures/thresholds-sample.json`,  
       - `fixtures/samples/carbon-tight-budget.json`,  
       - Other relevant scenarios.
   - Record:
     - Number and distribution of action changes,  
     - Budget outcomes (final utilization, overrun counts),  
     - SLO impacts (changed pause/slow rates on P1 vs P3).

3. **Regression reporting**
   - CI should produce a concise report (outside `docs/`) summarizing:
     - Key metrics-of-interest,  
     - Any obvious regressions (e.g., “P1 pause rate increased by 25%”).

4. **Governance checks**
   - Confirm that no experiment:
     - Weakens CARE/sovereignty protections,  
     - Allows budgets to consistently overshoot agreed limits,  
     - Eliminates explainability (e.g., thresholds so complex they cannot be described clearly).

Only experiments with acceptable CI & governance outcomes should be considered `candidate` or `adopted`.

---

## 🧠 Story Node & Focus Mode Integration

These experiments support narrative questions like:

- “Why did a pipeline slow down as we approached our carbon budget?”  
- “What would have happened if we used smoother burn-bands?”  
- “How do thresholds differ for P1 vs P3 pipelines?”

To keep this doc friendly for Story Nodes and Focus Mode:

- Keep experiment descriptions **short and focused**.  
- Use clear labels (`Two-Band Thresholds`, `Smooth Burn-Bands`, `Priority-Weighted Redlines`).  
- Summarize the **story** of each experiment family:
  - What changed,  
  - Why it was tried,  
  - Whether it helped.

Example Story Node anchor:

~~~text
Related Story Node:
urn:kfm:story-node:pipelines:autonomy-matrix:decider:experiment:cost-energy-thresholds:overview
~~~

Story Nodes must present these as **design explorations**, not current policy, unless and until the canonical Autonomy Matrix and Decider specs are updated.

---

## 🕰️ Version History

| Version    | Date       | Summary                                                                                                                  |
|-----------:|------------|--------------------------------------------------------------------------------------------------------------------------|
| **v11.2.4**| 2025-12-05 | Initial creation of cost/energy/carbon threshold experiment doc. Defines experiment profiles, data requirements, and CI hooks. |

---

<div align="center">

🧪 **KFM v11 — Autonomy Decider Cost/Energy/Carbon Threshold Experiments**  
Budget-Aware Autonomy · Sustainability-Conscious Decisions · FAIR+CARE-Governed Tuning  

[🧪 Experiment Registry](README.md) · [📦 Fixtures](fixtures/README.md) · [🧠 Decider Variants](../README.md)

</div>

