---
title: "🧠 KFM v11 — Autonomy Decider Kernel (Control-Plane Core)"
description: "LangGraph-based autonomy kernel that evaluates pipeline state and issues deterministic resume/slow/pause/escalate actions for the KFM Autonomy Matrix."
path: "docs/pipelines/autonomy-matrix/decider/README.md"
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

sbom_ref: "../../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.4/autonomy-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/autonomy-matrix-v1.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../sovereignty/INDIGENOUS-DATA-PROTECTION.md"
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

intent: "autonomy-matrix-decider"
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

category: "Pipelines · Autonomy · Governance · Control-Plane"

sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Internal"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: false

data_steward: "Reliability · Sustainability · FAIR+CARE Council"
ttl_policy: "Indefinite (subject to architecture changes)"
sunset_policy: "Supersede when Autonomy Matrix v12 decider architecture is adopted"

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
  - "docs/pipelines/autonomy-matrix/README.md@v11.2.4"
  - "docs/pipelines/autonomy-matrix/README.md@v11.2.3"
  - "docs/pipelines/reliability/README.md"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/docs-pipelines-autonomy-decider-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/docs-pipelines-autonomy-decider-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "mutable"

doc_uuid: "urn:kfm:doc:pipelines:autonomy-matrix:decider:v11.2.4"
semantic_document_id: "kfm-pipelines-autonomy-matrix-decider-v11.2.4"
event_source_id: "ledger:kfm:doc:pipelines:autonomy-matrix:decider:v11.2.4"

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
    - "⚙️ State Machine & Control Flow"
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

# 🧠 **KFM v11 — Autonomy Decider Kernel (Control-Plane Core)**  
`docs/pipelines/autonomy-matrix/decider/README.md`

**Purpose:**  
Describe the **Autonomy Decider kernel** — the LangGraph-based control-plane component that evaluates pipeline state and issues deterministic **resume · slow · pause · escalate** actions for the KFM Autonomy Matrix.  
This document defines the decider’s **state machine, inputs/outputs, configuration contracts, and validation rules**, so behavior is reproducible, explainable, and FAIR+CARE-governed.

</div>

---

## 📘 Overview

The **Autonomy Decider** is the core of the KFM pipeline control plane:

- Consumes:
  - Per-pipeline autonomy profiles (`pipeline-profiles/*.yaml`),
  - Live telemetry (cost, energy, carbon, freshness, trust),
  - Governance gates (CARE, sovereignty, cardinality, etc.).
- Computes:
  - A **scalar autonomy score** and a set of **gate outcomes** for each decision tick.
- Emits:
  - A single **canonical action** (`resume`, `slow`, `pause`, `escalate`),
  - Machine-readable **decision records** and **OpenLineage events**.

Design goals:

- **Deterministic** — same inputs ⇒ same decision & score.  
- **Config-driven** — no hard-coded thresholds; all weights and limits live in versioned configs.  
- **Explainable** — every decision carries evidence (metrics, gate evaluations, provenance links).  
- **Pluggable** — decider is a component in the autonomy stack, not tied to any single orchestrator.

The decider does **not** modify data directly. It only changes **run-state** for pipelines (whether and how they are allowed to execute).

---

## 🗂️ Directory Layout

~~~text
docs/pipelines/autonomy-matrix/decider/
│
├── 📄 README.md                       # This file (Autonomy Decider kernel guide)
│
├── 📄 score-functions.md              # Definitions & formulas for all scoring components
├── 📄 action-logic.md                 # Decision tables + mapping {score,gates} → action
├── 📄 contracts.md                    # Invariants & contracts for decider inputs/outputs
│
└── 📂 designs/                        # Optional deeper design notes
    ├── 📄 state-machine.md            # Detailed LangGraph/graph-based state design
    └── 📄 backlog.md                  # Known limitations & future improvements
~~~

**Author rules:**

- `score-functions.md`, `action-logic.md`, and `contracts.md` **must** reference this README as their normative parent.  
- `designs/` holds non-normative, exploratory material; only this README and the main Autonomy Matrix README are considered **authoritative**.  
- Any change to state machine semantics or action contracts must update:
  - This README,  
  - `contracts.md`, and  
  - Associated schemas/tests referenced under **🧪 Validation & CI/CD**.

---

## 🧭 Context

This component is one layer in the full KFM stack:

> **Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j knowledge graph → API layer → React/MapLibre/Cesium frontend → Story Nodes → Focus Mode**

Within the Autonomy Matrix:

- The **main spec** is defined in  
  `docs/pipelines/autonomy-matrix/README.md`.
- **Pipeline autonomy profiles** live in  
  `docs/pipelines/autonomy-matrix/pipeline-profiles/*.yaml`.
- **Gates and governance rules** live in  
  `docs/pipelines/autonomy-matrix/gates/*.md`.
- **Telemetry & OpenLineage records** are described in  
  `docs/pipelines/autonomy-matrix/telemetry/README.md`.

The decider:

- Interprets autonomy profiles + live telemetry,  
- Applies gates and scoring rules,  
- Produces actions and decision records consumed by orchestrators (Airflow, Dagster, LangGraph pipelines, etc.), and by governance dashboards.

---

## ⚙️ State Machine & Control Flow

At a high level, the decider runs a **state machine** on a per-pipeline basis. Conceptually:

~~~mermaid
flowchart LR
    S[Start\ninput snapshot] --> L[Load Profile & Gates]
    L --> V[Validate Inputs]
    V -->|ok| C[Compute Scores]
    V -->|invalid| E[Error & Escalate]

    C --> G[Evaluate Gates]
    G --> D[Select Action\nresume/slow/pause/escalate]

    D --> T[Emit Telemetry & OpenLineage]
    T --> X[Done]
    E --> T
~~~

### States (conceptual)

- **Start**  
  - Inputs: pipeline ID, snapshot timestamp, telemetry bundle, optional hints.  
  - Precondition: snapshot is immutable for the decision.

- **Load Profile & Gates**  
  - Load `pipeline-profiles/<pipeline>.yaml`.  
  - Resolve gate configs (CARE, cost-energy, freshness, cardinality, etc.).

- **Validate Inputs**  
  - Check that:
    - Telemetry is structurally valid (schema-checked),
    - Required metrics (lag, cost, energy, carbon, trust signals) are present,
    - The profile is valid for this pipeline & environment.
  - On failure: emit an **error decision** that defaults to **escalate** with reasons.

- **Compute Scores**  
  - Apply scoring functions defined in `score-functions.md`:
    - `FreshnessScore`
    - `TemporalRelevance`
    - `DataTrust`
    - `CostBurnRate`
    - `EnergyKWhRate`
    - `CarbonCO2eRate`
  - Aggregate into a single scalar score using profile-configured weights.

- **Evaluate Gates**  
  - For each enabled gate:
    - Evaluate whether preconditions are violated (e.g., budget exceeded, CARE breach).
  - Gates may:
    - Hard override the action (e.g., force `pause`),
    - Annotate evidence without overriding (soft warnings).

- **Select Action**  
  - Combine `{score, gates, context}` with decision tables from `action-logic.md`.  
  - Choose one of: `resume`, `slow`, `pause`, `escalate`.

- **Emit Telemetry & OpenLineage**  
  - Write a decision record to `autonomy-decisions.jsonl`.  
  - Emit an OpenLineage event describing the autonomy action and evidence.  
  - Return an action object to the caller.

### Contracts

`contracts.md` must define, at minimum:

- **Input contract**  
  - Required fields in the decision request (pipeline id, environment, snapshot, profile ref, etc.).
- **Output contract**  
  - Shape of the action object, including:
    - `decision_id`, `action`, `score`, `reasons`, `evidence`, `gates`, `provenance`.
- **Invariants**  
  - Determinism: for a fixed input, the same output must be produced.  
  - Idempotency: re-sending the same action to an orchestrator must not produce double-side effects.  
  - Governance: gates with `hard_fail` flags must always override numeric scores.

---

## 🧪 Validation & CI/CD

The decider is **heavily tested** and wired into KFM CI:

- **Config & Schema Validation**
  - All decision requests and telemetry samples used in tests must validate against:
    - `autonomy-matrix-v1` telemetry schema,  
    - `docs-pipelines-autonomy-decider-v11.2.4.schema.json`.

- **Unit & Property Tests**
  - **Score functions**:
    - Monotonicity properties (e.g., higher cost ⇒ lower score, all else equal),
    - Boundary conditions (0 and 1 extremes).
  - **Gates**:
    - Specific scenarios where triggering conditions yield forced `pause` or `escalate`.
  - **Determinism**:
    - Replay the same snapshot multiple times and assert identical decisions.

- **Golden Decision Fixtures**
  - Examples from `docs/pipelines/autonomy-matrix/examples/` should be mirrored as test fixtures under `tests/`.
  - CI compares the **actual decision output** against the documented expected action and key metrics.

- **Linting & Governance Checks**
  - Markdown + schema lint for all decider docs.
  - Provenance checks to ensure this README references the main Autonomy Matrix spec and reliability docs.
  - Optional energy/carbon tests to ensure decider overhead is bounded and monitored.

---

## 📦 Data & Metadata

The decider itself is **metadata-rich**:

- **Configurations**
  - Autonomy profiles (`pipeline-profiles/*.yaml`) define:
    - SLOs and budgets,
    - CARE labels and sovereignty policies,
    - Gate configurations,
    - Weight vectors for scoring.
  - Decider runtime config (not stored here) may live under `config/autonomy/decider/*.yaml` and should be referenced in design docs.

- **Telemetry**
  - Decision records and action events are cataloged as:
    - DCAT datasets,  
    - STAC Items in a monitoring collection,  
    - PROV entities & activities describing autonomy decisions.

- **Ontological Role**
  - Each decision is a `prov:Entity` generated by an autonomy `prov:Activity` (the decider evaluation), associated with:
    - Pipeline agents (teams),
    - System agents (autonomy services),
    - Governance bodies (FAIR+CARE council).

This README establishes the **semantic contract** for those entities and activities; schemas in `schemas/json/` and `schemas/shacl/` provide machine-level constraints.

---

## 🧠 Story Node & Focus Mode Integration

The decider is a prime target for **Story Nodes** and Focus Mode overlays:

- **Developer explanations**
  - “Why was pipeline X slowed at 02:37?”  
  - “Which gates were responsible for this pause?”

- **Governance transparency**
  - Story Nodes can summarize autonomy behavior over time, linking to specific decisions and gates.

When writing decider documentation and examples:

- Use **clear topic sentences** and keep sections narrowly scoped.  
- Reference concrete artifacts (`pipeline-profiles/*.yaml`, telemetry paths) rather than hand-wavy descriptions.  
- Suggest Story Node anchors where helpful, e.g.:

~~~text
Related Story Node:
urn:kfm:story-node:pipelines:autonomy-matrix:decider:hydro-hrrr-downscale:slow
~~~

Focus Mode MUST NOT alter the normative content of this README; it may only summarize, highlight, or contextualize.

---

## 🕰️ Version History

| Version    | Date       | Summary                                                                                                       |
|-----------:|------------|---------------------------------------------------------------------------------------------------------------|
| **v11.2.4**| 2025-12-05 | Initial Autonomy Decider kernel guide. Defines state machine, contracts, CI requirements, and metadata roles. |

---

<div align="center">

🧠 **KFM v11 — Autonomy Decider Kernel (Control-Plane Core)**  
Deterministic Decisions · Explainable Governance · FAIR+CARE-Aligned Control Plane  

[🤖 Autonomy Matrix Spec](../README.md) · [📚 Examples](../examples/README.md) · [⚖ Governance](../../../governance/ROOT-GOVERNANCE.md)

</div>

