---
title: "🧪 KFM v11 — Autonomy Decider Experiment Registry"
description: "Registry and guidance for Autonomy Decider experiments (fairness, horizons, thresholds) within the KFM v11 Autonomy Matrix control plane."
path: "docs/pipelines/autonomy-matrix/decider/designs/variants/experiments/README.md"
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

governance_ref: "../../../../../../governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../sovereignty/INDIGENOUS-DATA-PROTECTION.md"
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

intent: "autonomy-matrix-decider-variants-experiments"
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
  - "experiments"

category: "Pipelines · Autonomy · Governance · Architecture · Experiments"

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

json_schema_ref: "schemas/json/docs-pipelines-autonomy-decider-variants-experiments-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/docs-pipelines-autonomy-decider-variants-experiments-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "mutable"

doc_uuid: "urn:kfm:doc:pipelines:autonomy-matrix:decider:designs:variants:experiments:v11.2.4"
semantic_document_id: "kfm-pipelines-autonomy-matrix-decider-variants-experiments-v11.2.4"
event_source_id: "ledger:kfm:doc:pipelines:autonomy-matrix:decider:designs:variants:experiments:v11.2.4"

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
    - "🧭 Context"
    - "🧱 Architecture"
    - "🧪 Experiment Profiles"
    - "🧪 Validation & CI/CD"
    - "📦 Data & Metadata"
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

# 🧪 **KFM v11 — Autonomy Decider Experiment Registry**  
`docs/pipelines/autonomy-matrix/decider/designs/variants/experiments/README.md`

**Purpose:**  
Define how **Autonomy Decider experiments** are documented, organized, and governed.  
This registry ensures all decider experiments (fairness, horizons, thresholds, etc.) are **config-driven, reproducible,  
and reviewable** before they influence the canonical Autonomy Matrix behavior.

</div>

---

## 📘 Overview

Autonomy Decider experiments explore changes to:

- Scoring functions (e.g., cost vs. carbon weighting),  
- Gate composition (e.g., new CARE or cost-energy gates),  
- Decision horizons (per-run vs. sliding-window decisions),  
- Multi-tenant arbitration strategies (fairness, quotas).

This document:

- Describes the **layout and lifecycle** of experiments under `experiments/`,  
- Defines a **standard experiment profile** (metadata, configs, telemetry),  
- Connects experiments to CI, telemetry, and governance workflows,  
- Keeps experimental work clearly separated from **normative** Autonomy contracts.

Normative contracts remain in:

- `docs/pipelines/autonomy-matrix/decider/README.md`  
- `docs/pipelines/autonomy-matrix/README.md`  

---

## 🗂️ Directory Layout

~~~text
docs/pipelines/autonomy-matrix/decider/designs/variants/experiments/
│
├── 📄 README.md                       # This file (experiment registry & guidance)
│
├── 📄 fairness-experiments.md         # Designs & results for fairness / multi-tenant arbitration
├── 📄 horizon-tuning.md               # Experiments on decision horizons & aggregation windows
├── 📄 cost-energy-thresholds.md       # Experiments on cost/energy/carbon thresholds & burn bands
│
└── 📂 fixtures/                       # Optional example configs and telemetry snapshots
    ├── 📄 fairness-small-sample.json  # Synthetic telemetry for fairness experiments
    ├── 📄 horizon-daily-vs-hourly.json# Synthetic telemetry for horizon tuning
    └── 📄 thresholds-sample.json      # Synthetic telemetry for threshold tuning
~~~

**Author rules:**

- New experiment families **must** get their own `*.md` file here.  
- Telemetry/config snippets go in `fixtures/` as **synthetic** or strongly anonymized examples.  
- Every experiment doc must:
  - Link back to this README,  
  - Declare its status (`exploratory`, `candidate`, `rejected`, `adopted`),  
  - Reference the **canonical decider spec** and any affected schemas.

---

## 🧭 Context

Experiments live at the intersection of:

- **Autonomy contracts** (what the decider is allowed to do),  
- **Reliability SLOs** (availability/freshness/error budgets),  
- **Sustainability goals** (cost, energy, carbon caps),  
- **FAIR+CARE & sovereignty** (who benefits, who controls, how sensitive data is handled).

Key relationships:

- `decider/README.md` — defines the **current** canonical decider behavior.  
- `decider/designs/README.md` — captures broader design space and phases.  
- `decider/designs/variants/README.md` — describes variant decider shapes (single-tenant, multi-tenant, simulator).  
- `decider/designs/variants/experiments/` — this directory, where we prototype changes **before** they are promoted to variants or canonical behavior.

No experiment here is normative on its own; promotion requires:

- Design review (architecture + FAIR+CARE),  
- Offline simulation,  
- CI integration,  
- And a versioned update to canonical docs and schemas.

---

## 🧱 Architecture

Experiments share a common high-level shape:

1. **Define a hypothesis**

   Examples:

   - “Reducing carbon weight from 0.5 → 0.3 will cut unnecessary pauses while staying under carbon budget.”  
   - “Switching fairness strategy from strict quota to weighted sharing improves P1 pipelines without starving P3.”

2. **Specify changes in config/logic**

   - Proposed new weights, gates, or decision rules (YAML/JSON).  
   - Explicit mapping to code paths or decider variant configs.

3. **Run offline simulation**

   - Use historical or synthetic telemetry snapshots.  
   - Apply both **current canonical** and **experimental** logic.  
   - Compare decisions and budget/SLO/CARE outcomes.

4. **Summarize outcomes**

   - Quantitative metrics (e.g., # of actions changed, SLO impacts, budget usage).  
   - Qualitative notes (e.g., increased complexity, explainability concerns).

5. **Recommend a status**

   - `rejected` / `hold` / `candidate-for-next-minor` / `adopted-in-vX.Y`.

Each experiment doc should walk through these phases explicitly.

---

## 🧪 Experiment Profiles

To keep experiments consistent and machine-readable, each must be described with an **experiment profile** block (conceptual):

~~~yaml
experiment_id: "autonomy-fairness-wfs-v1"
title: "Weighted Fair Sharing for Multi-Tenant Decider"
status: "exploratory"           # exploratory | candidate | rejected | adopted
target_version: "v11.3.x"       # first version where adoption is considered
owner_team: "reliability-autonomy@kfm"
created_at: "2025-12-05"
related_docs:
  - "../multi-tenant.md"
  - "../../README.md"
  - "../../../../README.md"     # Autonomy Matrix spec
scope:
  pipelines:
    - "hydro/*"
    - "atmo/*"
  environments:
    - "staging"
hypothesis:
  text: >
    Weighted fair sharing based on priority_band will reduce P1 slowdowns
    by 30% without violating P3 quotas or carbon budgets.
variants:
  baseline:
    config_ref: "config/autonomy/decider/canonical.yaml"
  experimental:
    config_ref: "config/autonomy/decider/fairness-wfs-v1.yaml"
fixtures:
  telemetry:
    - "fixtures/fairness-small-sample.json"
metrics_of_interest:
  - "num_action_changes"
  - "p1_slowdown_rate"
  - "quota_violations"
  - "carbon_budget_overruns"
~~~

This profile can be:

- Embedded in the experiment doc, or  
- Stored alongside it (e.g., in `fixtures/`) and referenced from text.

Experiments should be **replayable** via a standard CLI/notebook pattern, even if that CLI is hypothetical at first.

---

## 🧪 Validation & CI/CD

Even though experiments are non-normative, they are subject to governance:

- **Markdown & schema checks**
  - Front-matter validation via `schema-lint`.  
  - Structural lint (`markdown-lint`, `accessibility-check`).  

- **Experiment profile checks**
  - Minimal fields present (`experiment_id`, `status`, `owner_team`, `target_version`).  
  - Status transitions enforced (e.g., `adopted` experiments must link to the PR and version that adopted them).

- **Simulation checks (when wired)**
  - CI jobs can:
    - Run experimental configs against a small set of fixtures,  
    - Assert “no catastrophic behavior” (e.g., never pause all P0 pipelines).

- **Governance checks**
  - Ensure experiments do not propose:
    - Ignoring FAIR+CARE or sovereignty policies,  
    - Abandoning provenance or explainability requirements.

A typical CI flow for an experiment PR:

1. Lint docs and experiment profile.  
2. Run simulation on a minimal fixture set.  
3. Generate an experiment summary artifact (JSON/Markdown) attached to the PR.  

---

## 📦 Data & Metadata

Experiments involve multiple data/metadata layers:

- **Configs**
  - Experimental decider configs under `config/autonomy/decider/` (not in this dir, but referenced).  
  - Pipeline autonomy profiles (unchanged, or changed in a controlled branch).

- **Telemetry**
  - Synthetic fixtures in `fixtures/`.  
  - Optionally, snapshots of **real telemetry** stored in a restricted area and summarized or anonymized here.

- **Results**
  - Aggregated experiment results:  
    - Stored as JSON (e.g., `results/fairness-wfs-v1.summary.json`) in non-docs locations,  
    - Summarized in these Markdown files.

All examples in this directory must:

- Use synthetic or clearly anonymized values,  
- Avoid leaking internal IDs or sensitive cost info,  
- Mark example IDs as non-production (e.g., `kfm-example-*`).

---

## 🧠 Story Node & Focus Mode Integration

Experiment docs tell the story of **how** and **why** autonomy evolves:

- They are useful for:
  - Autonomy engineering retrospectives,  
  - FAIR+CARE and sustainability reviews,  
  - Training new reliability/ML engineers.

To keep them friendly for Story Nodes and Focus Mode:

- Keep sections **narrow** (one experiment family per file).  
- Clearly mark **Status** and **Target Version** at the top of each experiment description.  
- Provide short, bullet-point summaries of:
  - Hypothesis,  
  - Key findings,  
  - Decision (adopt / reject / hold).

Example Story Node anchor:

~~~text
Related Story Node:
urn:kfm:story-node:pipelines:autonomy-matrix:decider:experiment:fairness-wfs-v1
~~~

Story Nodes must treat these docs as **design narrative**, not policy; canonical behavior is always taken from the main Autonomy Matrix and Decider specs.

---

## 🕰️ Version History

| Version    | Date       | Summary                                                                                                                        |
|-----------:|------------|--------------------------------------------------------------------------------------------------------------------------------|
| **v11.2.4**| 2025-12-05 | Initial creation of Autonomy Decider Experiment Registry README. Defines layout, experiment profile template, and CI/gov hooks.|

---

<div align="center">

🧪 **KFM v11 — Autonomy Decider Experiment Registry**  
Simulation-First Autonomy · Reproducible Experiments · FAIR+CARE-Governed Evolution  

[🧠 Decider Variants](../README.md) · [🧠 Decider Designs](../../README.md) · [🤖 Autonomy Matrix Spec](../../../README.md)

</div>

