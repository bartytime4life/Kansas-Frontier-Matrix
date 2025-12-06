---
title: "🧠 KFM v11 — Offline Simulator Autonomy Decider Variant"
description: "Architecture and design for an offline replay & simulation variant of the KFM v11 Autonomy Decider, used to test autonomy changes on synthetic or historical telemetry."
path: "docs/pipelines/autonomy-matrix/decider/designs/variants/offline-simulator.md"
version: "v11.2.4"
last_updated: "2025-12-05"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability · Sustainability · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "Aligned with Autonomy Matrix v11.2.x (variant-only; non-normative)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.4/autonomy-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/autonomy-matrix-v1.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../sovereignty/INDIGENOUS-DATA-PROTECTION.md"
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

intent: "autonomy-matrix-decider-variant-offline-simulator"
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
  - "simulation"

category: "Pipelines · Autonomy · Governance · Architecture · Variants"

sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Internal"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: false

data_steward: "Reliability · Sustainability · FAIR+CARE Council"
ttl_policy: "Indefinite (subject to architecture changes)"
sunset_policy: "Supersede when Autonomy Matrix v12 offline simulator variant is adopted"

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

json_schema_ref: "schemas/json/docs-pipelines-autonomy-decider-variant-offline-simulator-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/docs-pipelines-autonomy-decider-variant-offline-simulator-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "mutable"

doc_uuid: "urn:kfm:doc:pipelines:autonomy-matrix:decider:designs:variants:offline-simulator:v11.2.4"
semantic_document_id: "kfm-pipelines-autonomy-matrix-decider-variant-offline-simulator-v11.2.4"
event_source_id: "ledger:kfm:doc:pipelines:autonomy-matrix:decider:designs:variants:offline-simulator:v11.2.4"

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

# 🧠 **KFM v11 — Offline Simulator Autonomy Decider Variant**  
`docs/pipelines/autonomy-matrix/decider/designs/variants/offline-simulator.md`

**Purpose:**  
Describe an **offline simulator variant** of the Autonomy Decider that replays synthetic or historical telemetry  
against canonical and experimental autonomy configs, producing **deterministic, explainable reports** for reliability,  
sustainability, and FAIR+CARE governance reviews.

</div>

---

## 📘 Overview

The **Offline Simulator** variant provides a safe environment to:

- Re-run the Autonomy Decider on **captured telemetry** (synthetic or historical).  
- Compare **canonical vs experimental** decider behavior (fairness, thresholds, horizons, etc.).  
- Generate **machine-readable reports** describing:
  - Action changes (`resume/slow/pause/escalate`),  
  - SLO impacts,  
  - Cost/energy/carbon effects,  
  - Governance and CARE implications.

Key properties:

- **Read-only** with respect to production systems:
  - No real pipeline runs are started/stopped.  
  - No live budgets or quotas are modified.  
- **Deterministic & config-driven**:
  - Inputs: autonomy configs, telemetry fixtures, experiment profile.  
  - No hidden randomness; seeds & config refs must be recorded.  
- **Governance-safe**:
  - Designed to help FAIR+CARE and sustainability councils assess autonomy changes before roll-out.

This variant is **non-normative** and used only for experiments and regression validation.

---

## 🧭 Context

The Offline Simulator is a key tool supporting:

- **Variant designs & experiments**  
  - Fairness: `fairness-experiments.md`  
  - Cost/energy/carbon thresholds: `cost-energy-thresholds.md`  
  - Horizon tuning: `horizon-tuning.md`
- **Fixtures & sample scenarios**  
  - Telemetry fixtures: `experiments/fixtures/README.md`  
  - Scenario samples: `experiments/fixtures/samples/README.md`
- **Canonical decider**  
  - Defined in `decider/README.md` and implemented in the control-plane.

Typical workflow:

1. Propose a change (new fairness policy, thresholds, horizons).  
2. Encode change in **experimental autonomy configs**.  
3. Run Offline Simulator with:
   - Canonical config vs experimental config,  
   - Shared fixtures / historical telemetry.  
4. Inspect **diffs** in decisions and outcomes.  
5. Use results to decide whether to:
   - Reject,  
   - Refine, or  
   - Promote the change.

The simulator prevents “dark” behavior changes from reaching production without evidence.

---

## 🧱 Architecture

### High-Level Flow

~~~mermaid
flowchart LR
    C["Configs<br/>canonical & experimental"] --> S["Offline Simulator<br/>variant engine"]
    F["Fixtures & Telemetry<br/>synthetic / historical"] --> S
    S --> D["Decision Streams<br/>canonical vs experimental"]
    D --> M["Metrics & Diffs<br/>SLO · cost · energy · carbon · fairness"]
    M --> R["Reports<br/>human & machine-readable"]
~~~

### Core Components

1. **Scenario Catalog**

   - References to:
     - `fixtures/*.json` (time-series telemetry snapshots),  
     - `fixtures/samples/*.json` (multi-tenant and edge-case scenarios).  
   - Optionally, references to **offline historical telemetry** stored outside `docs/` (with appropriate access controls).

2. **Config Loader**

   - Loads:
     - Canonical decider config (e.g., `config/autonomy/decider/canonical.yaml`),  
     - Experimental decider config (e.g., `config/autonomy/decider/fairness-wfs-v1.yaml`).  
   - Resolves:
     - Pipeline autonomy profiles (`pipeline-profiles/*.yaml`),  
     - Tenant configs (for multi-tenant variant),  
     - Gate settings (CARE, cost-energy, cardinality, etc.).

3. **Replay Engine**

   - Treats each fixture as a **time-ordered stream**:
     - Replays telemetry samples through:
       - Canonical decider,  
       - Experimental decider (one or more variants).  
   - Produces **decision sequences**:
     - Per pipeline, per tenant, per decision tick.

4. **Diff & Metrics Aggregator**

   - Compares canonical vs experimental decisions:
     - Counts action changes,  
     - Computes thrash, SLO violations, budget deltas, fairness metrics.  
   - Aggregates results over:
     - Pipelines, tenants, priority bands, time windows.

5. **Report Generator**

   - Emits:
     - Machine-readable summaries (JSON) for CI and dashboards,  
     - High-level Markdown/HTML summaries for humans (may live outside this tree).  
   - Summaries must:
     - Identify experiment IDs and configs used,  
     - Contain enough detail for governance reviewers.

### Conceptual CLI Interface

The exact binary name and paths are implementation-dependent, but a conceptual CLI might look like:

~~~bash
kfm-autonomy-sim \
  --scenario docs/pipelines/autonomy-matrix/decider/designs/variants/experiments/fixtures/horizon-daily-vs-hourly.json \
  --baseline-config config/autonomy/decider/canonical.yaml \
  --experiment-config config/autonomy/decider/horizon-5m-ewma.yaml \
  --out results/autonomy/horizon-5m-ewma-summary.json
~~~

The CLI (or equivalent API) must:

- Log all config and fixture references,  
- Produce deterministic outputs for the same inputs.

---

## 📦 Data & Metadata

The Offline Simulator interacts with several data layers:

### Fixtures & Scenarios

- Defined and documented in:
  - `experiments/fixtures/README.md`  
  - `experiments/fixtures/samples/README.md`  
- Must be:
  - Synthetic or strongly anonymized,  
  - Schema-valid telemetry sequences,  
  - Tagged with scenario types (multi-tenant, carbon-tight, high-lag-low-cost, etc.).

### Configs

- Canonical and experimental configs live under repo `config/` (outside `docs/`), but this doc defines:
  - Required fields,  
  - Variant-agnostic vs variant-specific parameters,  
  - How they are referenced in experiment profiles.

Example config snippet (illustrative, non-normative):

~~~yaml
autonomy:
  variant: "multi-tenant-offline-sim"   # conceptual flag
  horizon:
    mode: "sliding-window"
    window: "5m"
  fairness:
    policy: "weighted-fair-sharing"
    tenant_weights:
      example-tenant-a: 0.5
      example-tenant-b: 0.3
      example-tenant-c: 0.2
~~~

### Experiment Profiles

- Located in `experiments/*.md`, they:
  - Reference scenarios, configs, metrics-of-interest, and target versions.  
  - Provide the **semantic context** for simulator runs.

### Reports

- Simulator outputs are not stored under `docs/` by default, but may be referenced here as examples:
  - `results/autonomy/<experiment-id>.summary.json` (outside `docs/`).  
- Reports must:
  - Include experiment IDs, config hashes, and fixture IDs,  
  - Be consistent with PROV-O patterns (entities, activities, agents).

All example IDs must be synthetic (e.g., `kfm-example-*`, `example-tenant-*`).

---

## 🧪 Validation & CI/CD

The Offline Simulator variant is central to Autonomy CI:

1. **Schema Validation**

   - Fixtures:
     - Validate against telemetry schemas (`autonomy-matrix-v1`, etc.).  
   - Configs:
     - Validate against decider/variant config schemas.  
   - Experiment profiles:
     - Validate minimal fields (`experiment_id`, `status`, `target_version`, etc.).

2. **Smoke Tests**

   - CI must run a small subset of simulations on each change affecting:
     - Decider logic,  
     - Gate logic,  
     - Variant configs,  
     - Telemetry schemas.  
   - Smoke tests confirm:
     - Simulator runs to completion,  
     - Outputs are structurally valid,  
     - No catastrophic regressions (e.g., all pipelines paused).

3. **Experiment-Specific Jobs**

   - For specific experiments (fairness, thresholds, horizons), CI jobs can:
     - Run offline simulations using their configured scenarios,  
     - Compare metrics-of-interest against acceptance criteria (where defined),  
     - Attach synthetic summary artifacts to PRs.

4. **Governance Hooks**

   - Simulator jobs can produce:
     - Lightweight Markdown or JSON “governance digests” summarizing:
       - SLO impacts,  
       - Resource usage changes,  
       - Fairness/CARE implications.  
   - These digests can be surfaced to FAIR+CARE and sustainability reviewers.

Using the Offline Simulator should be a **required step** before enabling any non-trivial autonomy variant in production environments.

---

## 🧠 Story Node & Focus Mode Integration

The Offline Simulator enables stories like:

- “What would have happened if we had used the new fairness policy last month?”  
- “How does a 5-minute horizon change behavior vs per-run decisions?”  
- “Did our carbon-conscious thresholds meaningfully reduce emissions in simulations?”

To support Story Nodes and Focus Mode:

- Keep this doc at **architecture level** (what the simulator is, not every experiment detail).  
- Let experiment docs provide scenario-specific narratives.  
- Use clear references to:
  - Experiment files (`experiments/*.md`),  
  - Fixture sets (`experiments/fixtures/*.json`),  
  - Conceptual CLI commands.

Example Story Node anchor:

~~~text
Related Story Node:
urn:kfm:story-node:pipelines:autonomy-matrix:decider:variant:offline-simulator:overview
~~~

Story Nodes must emphasize that the Offline Simulator:

- Runs **offline**,  
- Uses **synthetic or anonymized data**,  
- Precedes any production change to autonomy behavior.

---

## 🕰️ Version History

| Version    | Date       | Summary                                                                                                                         |
|-----------:|------------|---------------------------------------------------------------------------------------------------------------------------------|
| **v11.2.4**| 2025-12-05 | Initial Offline Simulator variant design. Defines architecture, components, data expectations, CI role, and Story Node context. |

---

<div align="center">

🧠 **KFM v11 — Offline Simulator Autonomy Decider Variant**  
Simulation-First Autonomy · Safe Experimentation · FAIR+CARE-Governed Rollouts  

[🧠 Decider Variants Index](README.md) · [🧪 Experiment Registry](experiments/README.md) · [🤖 Autonomy Matrix Spec](../../../README.md)

</div>

