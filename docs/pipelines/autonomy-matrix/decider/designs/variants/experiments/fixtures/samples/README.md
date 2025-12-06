---
title: "📦 KFM v11 — Autonomy Decider Sample Fixture Sets"
description: "Sample synthetic telemetry scenarios for Autonomy Decider experiments within the KFM v11 Autonomy Matrix control plane."
path: "docs/pipelines/autonomy-matrix/decider/designs/variants/experiments/fixtures/samples/README.md"
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

sbom_ref: "../../../../../../../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v11.2.4/autonomy-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/autonomy-matrix-v1.json"
energy_schema: "../../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../../../governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../../faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../../sovereignty/INDIGENOUS-DATA-PROTECTION.md"
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

intent: "autonomy-matrix-decider-variants-experiments-fixtures-samples"
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
  - "test-data"

category: "Pipelines · Autonomy · Governance · Experiments · Fixtures"

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
  - "docs/pipelines/autonomy-matrix/decider/designs/variants/experiments/fixtures/README.md@v11.2.4"
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

json_schema_ref: "schemas/json/docs-pipelines-autonomy-decider-variants-experiments-fixtures-samples-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/docs-pipelines-autonomy-decider-variants-experiments-fixtures-samples-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "mutable"

doc_uuid: "urn:kfm:doc:pipelines:autonomy-matrix:decider:designs:variants:experiments:fixtures:samples:v11.2.4"
semantic_document_id: "kfm-pipelines-autonomy-matrix-decider-variants-experiments-fixtures-samples-v11.2.4"
event_source_id: "ledger:kfm:doc:pipelines:autonomy-matrix:decider:designs:variants:experiments:fixtures:samples:v11.2.4"

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
    - "🗂️ Directory Layout"
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

# 📦 **KFM v11 — Autonomy Decider Sample Fixture Sets**  
`docs/pipelines/autonomy-matrix/decider/designs/variants/experiments/fixtures/samples/README.md`

**Purpose:**  
Describe curated **sample fixture sets** that encode common synthetic scenarios  
used by Autonomy Decider experiments — e.g., multi-tenant mixes, tight carbon budgets,  
and high-lag/low-cost cases — so engineers can quickly understand and reuse them  
across simulations and CI.

</div>

---

## 📘 Overview

This document catalogs the **sample fixture JSON files** under:

~~~text
docs/pipelines/autonomy-matrix/decider/designs/variants/experiments/fixtures/samples/
~~~

These sample fixtures:

- Represent **reusable synthetic scenarios** for Autonomy Decider experiments,  
- Are used by multiple experiment families (fairness, horizons, thresholds),  
- Are **stable reference inputs** for CI and offline simulators.

They are **not** production data and do not define policy; they are teaching and testing aids.

---

## 🗂️ Directory Layout

~~~text
docs/pipelines/autonomy-matrix/decider/designs/variants/experiments/fixtures/samples/
│
├── 📄 README.md                     # This file (sample set descriptions)
│
├── 📄 multi-tenant-mix.json         # Mixed-tenant synthetic snapshot
├── 📄 carbon-tight-budget.json      # Pipelines near carbon budget limit
├── 📄 high-lag-low-cost.json        # Pipelines with high lag but low cost/energy
└── 📄 care-sensitive-vs-general.json# CARE-sensitive vs general-data pipeline mix
~~~

**Author rules:**

- Any new sample fixture **must** be listed here with a one-line description.  
- Samples should be **scenario-style** (multi-pipeline context), not single-run micro-cases  
  — single-run fixtures live one level up in `fixtures/`.  
- All samples must follow the **synthetic/anonymized** rules described in the parent fixtures README.

---

## 📦 Data & Metadata

Each sample fixture is a **JSON document** modeling one synthetic “world state”:

- Multiple pipelines and/or tenants,  
- Telemetry metrics per pipeline,  
- Governance context (CARE label, sovereignty policy, sensitivity).

### Sample: `multi-tenant-mix.json`

Intended to illustrate **multi-tenant fairness** scenarios:

- Several tenants (`example-tenant-a`, `example-tenant-b`, `example-tenant-c`).  
- Mix of priority bands (`P0`–`P3`).  
- Shared cost/energy/carbon budgets where:
  - P1/P2 pipelines compete during busy periods,  
  - P3 pipelines can be slowed/paused with minimal impact.

### Sample: `carbon-tight-budget.json`

Intended to test **carbon-aware gating**:

- Month-to-date `kgco2e` close to budget across several pipelines.  
- Some pipelines high-urgency (e.g., severe-weather-like synthetic cases), others low-urgency.  
- Useful for experiments about:
  - When to slow vs. pause,  
  - How to allocate remaining carbon budget across priorities/tenants.

### Sample: `high-lag-low-cost.json`

Intended to test **freshness vs. cost/energy tension**:

- Pipelines with high lag (SLO at risk) but low cost/energy/carbon footprint.  
- Useful for experiments evaluating:
  - Whether to increase priority (resume) despite low urgency,  
  - How strongly freshness should influence scoring at low resource cost.

### Sample: `care-sensitive-vs-general.json`

Intended to explore **CARE-sensitive vs general-data pipelines**:

- Some pipelines tagged as `care_label: "Synthetic-Sensitive"` with stricter sovereignty policies.  
- Others tagged as `care_label: "Synthetic-General"` with looser constraints.  
- Useful for experiments probing:
  - How gates prioritize protecting sensitive synthetic data,  
  - How autonomy should slow/pause different classes when budgets collide.

All IDs, names, and numeric values are **synthetic**; they should look realistic but be clearly non-production (e.g., `kfm-example-*`, `example-tenant-*`).

---

## 🧪 Validation & CI/CD

Sample fixtures feed into CI and simulation workflows:

- **Schema validation**
  - All JSON under `samples/` must pass:
    - `autonomy-matrix-v1` telemetry schema (plus any variant extensions).

- **Scenario tagging**
  - Experiments referencing a sample should note:
    - `fixture: samples/multi-tenant-mix.json`, etc.  
  - This enables CI to track which scenarios cover which experiments.

- **Regression checks**
  - When autonomy logic changes, CI may:
    - Run canonical vs. experimental deciders against all sample fixtures,  
    - Report how many decisions/actions changed per scenario,  
    - Help reviewers understand scenario-level impacts quickly.

Changes to sample fixtures should be treated like **test data migrations**:

- Explain why the scenario changed (e.g., “add another P0 pipeline to stress fairness logic”),  
- Update experiment docs and test expectations accordingly.

---

## 🧠 Story Node & Focus Mode Integration

These sample scenarios are useful for **narrative explanations**:

- “Show me an example where tenant fairness mattered.”  
- “Explain a carbon-tight scenario where autonomy paused low-priority pipelines.”  
- “What happens when lag is high but cost is low?”

When referencing samples in experiment or design docs:

- Use descriptive text plus file names, e.g.,  
  “In the **multi-tenant mix** sample (`samples/multi-tenant-mix.json`)…”  
- Summarize the scenario’s story (who, what, why) so Focus Mode can surface it as a  
  **Story Node** without reading raw JSON.

Example Story Node anchor:

~~~text
Related Story Node:
urn:kfm:story-node:pipelines:autonomy-matrix:decider:fixtures:sample:multi-tenant-mix
~~~

Story Nodes must always indicate that these are **synthetic** scenarios, not real-world logs.

---

## 🕰️ Version History

| Version    | Date       | Summary                                                                                                       |
|-----------:|------------|---------------------------------------------------------------------------------------------------------------|
| **v11.2.4**| 2025-12-05 | Initial creation of sample fixtures README. Describes sample scenarios (multi-tenant, carbon-tight, etc.) and their roles. |

---

<div align="center">

📦 **KFM v11 — Autonomy Decider Sample Fixture Sets**  
Scenario-Based Synthetic Worlds · Reproducible Simulations · FAIR+CARE-Governed Test Data  

[📦 Fixtures Root](../README.md) · [🧪 Experiment Registry](../../README.md) · [🧠 Decider Variants](../../../README.md)

</div>

