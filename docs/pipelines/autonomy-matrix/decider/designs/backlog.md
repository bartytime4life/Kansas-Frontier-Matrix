---
title: "🧠 KFM v11 — Single-Tenant Autonomy Decider Variant"
description: "Architecture and design for a simplified, single-tenant variant of the KFM v11 Autonomy Decider for clusters owned by a single team or project."
path: "docs/pipelines/autonomy-matrix/decider/designs/variants/single-tenant.md"
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

intent: "autonomy-matrix-decider-variant-single-tenant"
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
  - "single-tenant"

category: "Pipelines · Autonomy · Governance · Architecture · Variants"

sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Internal"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: false

data_steward: "Reliability · Sustainability · FAIR+CARE Council"
ttl_policy: "Indefinite (subject to architecture changes)"
sunset_policy: "Supersede when Autonomy Matrix v12 single-tenant variant is adopted"

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

json_schema_ref: "schemas/json/docs-pipelines-autonomy-decider-variant-single-tenant-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/docs-pipelines-autonomy-decider-variant-single-tenant-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "mutable"

doc_uuid: "urn:kfm:doc:pipelines:autonomy-matrix:decider:designs:variants:single-tenant:v11.2.4"
semantic_document_id: "kfm-pipelines-autonomy-matrix-decider-variant-single-tenant-v11.2.4"
event_source_id: "ledger:kfm:doc:pipelines:autonomy-matrix:decider:designs:variants:single-tenant:v11.2.4"

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

# 🧠 **KFM v11 — Single-Tenant Autonomy Decider Variant**  
`docs/pipelines/autonomy-matrix/decider/designs/variants/single-tenant.md`

**Purpose:**  
Describe a **single-tenant variant** of the Autonomy Decider optimized for clusters owned  
by a single team or project. This variant simplifies autonomy behavior by removing  
multi-tenant fairness layers while preserving deterministic, config-driven, and  
FAIR+CARE-governed decisions.

</div>

---

## 📘 Overview

The **Single-Tenant Autonomy Decider** is a streamlined deployment of the Autonomy Matrix control-plane for:

- A **single owning team or project** per cluster.  
- Environments where **multi-tenant fairness** is unnecessary or handled elsewhere.  
- Pipelines that still require:
  - SLO-aware autonomy (freshness, availability),  
  - Cost/energy/carbon-aware decisions,  
  - CARE & sovereignty governance,  
  - Deterministic `resume/slow/pause/escalate` actions.

Compared to the **multi-tenant variant**:

- No cross-tenant quotas or fairness arbitration.  
- Budgets and SLOs are interpreted **directly** for the single owner.  
- The action contract and telemetry formats remain compatible with:
  - The canonical decider spec,  
  - Existing orchestrators (Airflow, Dagster, LangGraph).

This variant is especially suitable for:

- Dedicated research clusters,  
- Domain-specific KFM environments (e.g., a single hydrology or archaeology project),  
- Early-stage deployments before multi-tenant needs arise.

---

## 🧭 Context

The single-tenant variant sits within the broader Autonomy Matrix ecosystem:

- **Canonical behavior**  
  - Defined in `docs/pipelines/autonomy-matrix/decider/README.md`.  
- **Variants index**  
  - Described in `docs/pipelines/autonomy-matrix/decider/designs/variants/README.md`.  
- **Experiments**  
  - Fairness, thresholds, and horizon experiments are primarily scoped to multi-tenant or advanced deployments, but some horizon and threshold experiments may also apply here.

When to choose single-tenant:

- Only one team owns and configures pipelines on a cluster.  
- Resource contention is **within** that team, not between teams.  
- Governance primarily concerns:
  - Meeting SLOs,  
  - Staying within cluster-level budgets,  
  - Respecting CARE/sovereignty constraints for that single project.

When not to choose single-tenant:

- Multiple organizational units or external partners share the same cluster.  
- Allocation fairness between tenants is required.  
- Per-tenant quotas and fairness policies must be enforced by the autonomy layer.

---

## 🧱 Architecture

### High-Level Data & Control Flow

The single-tenant variant reuses the canonical decider architecture, but without the tenant-fairness wrapper present in the multi-tenant variant:

~~~mermaid
flowchart LR
    P["Pipelines<br/>single project/team"] --> S["Snapshot Builder<br/>profiles + telemetry"]
    S --> D["Autonomy Decider Core<br/>single-tenant mode"]
    D --> A["Actions<br/>resume / slow / pause / escalate"]
    A --> O["Orchestrators<br/>Airflow · Dagster · LangGraph"]
    D --> T["Telemetry & OpenLineage<br/>decisions + evidence"]
~~~

Characteristics:

- **Snapshot Builder**  
  - Collects:
    - Pipeline autonomy profiles (SLOs, budgets, CARE labels),  
    - Telemetry (lag, cost, energy, carbon, trust signals),  
    - Governance flags (sensitivity, sovereignty policy).  

- **Decider Core (single-tenant mode)**  
  - Runs the same scoring and gate logic as the canonical decider.  
  - Assumes:
    - All pipelines draw from the **same owner’s budgets**,  
    - No cross-tenant arbitration is needed.  
  - May treat global budgets directly, without per-tenant splits.

- **Orchestrators & Telemetry**  
  - Use the same action and telemetry contracts as the canonical decider.  
  - No additional tenant fields are required.

### Simplifications vs Multi-Tenant Variant

- No **tenant registry** or **tenant-weighted fairness layer**.  
- No per-tenant quota accounting; only **cluster or project-level budgets** are considered.  
- Fewer sources of complexity in decision explanations:
  - The main drivers are SLOs, budgets, and gates, not cross-tenant policy decisions.

### Compatibility with Multi-Tenant Design

The single-tenant variant should:

- Share as much code and config structure as possible with the multi-tenant and canonical deciders.  
- Allow a **future migration** to multi-tenant mode by:
  - Adding tenant metadata to pipeline profiles,  
  - Enabling multi-tenant configs,  
  - Turning on the fairness layer.

The reverse migration (multi-tenant → single-tenant) should be possible by collapsing tenant metadata into a single owner and using cluster-level budgets.

---

## 📦 Data & Metadata

Even in single-tenant mode, the decider remains **metadata-rich** and governance-aware.

### Pipeline Profiles (Single-Tenant Focus)

A pipeline profile for single-tenant mode may look like:

~~~yaml
pipeline: "example/hydro-hrrr"
owner_team: "hydro@kfm"
priority_band: "P1"

slos:
  availability: { target: 0.985, window: 30d, error_budget: 0.015 }
  freshness:    { max_lag: "2h" }
  cost:         { monthly_cap_usd: 1200 }
  energy:       { monthly_cap_kwh: 250 }
  carbon:       { monthly_cap_kgco2e: 65 }

governance:
  care_label: "Synthetic-Waters"
  sovereignty_policy: "synthetic-h3-generalization-v1"

autonomy:
  actions: ["resume", "slow", "pause", "escalate"]
  # Additional autonomy-specific configuration as defined by canonical decider
~~~

Notes:

- `owner_team` replaces or complements tenant concepts.  
- Budgets are interpreted as **project/cluster-level** rather than per-tenant.  
- CARE labels and sovereignty policies are still mandatory for governance.

### Telemetry

Telemetry remains aligned with the canonical schemas:

- Required metrics:
  - `freshness`, `cost`, `energy`, `carbon`, `trust` signals.  
- Governance context:
  - CARE labels, sensitivity flags, sovereignty policy references.

No tenant-specific fields are required for single-tenant mode, but the schema should remain compatible with multi-tenant telemetry (tenant fields can be omitted or set to a single synthetic/project identifier).

### Config Flags

An implementation may use a config flag to explicitly select this variant, for example:

~~~yaml
autonomy:
  variant: "single-tenant"
~~~

This flag is **design-level** until wired into implementations and schemas.

---

## 🧪 Validation & CI/CD

The single-tenant variant shares most CI expectations with the canonical decider, with some focus areas:

### Config & Schema Checks

- Pipeline profiles must still validate against:
  - Autonomy profile schemas,  
  - SLO and governance schemas.  
- Variant selection (e.g., `autonomy.variant: single-tenant`) must:
  - Be validated as a supported value,  
  - Not silently default to multi-tenant behavior.

### Behavioral Tests

- **Unit tests**:
  - Validate decision logic with:
    - Single-owner budgets,  
    - Various priority bands,  
    - CARE/sovereignty gates.  
- **Integration tests**:
  - Ensure that the same inputs yield:
    - Deterministic decisions,  
    - Proper gate behavior (cost/energy/carbon, CARE, cardinality).

### Regression Tests

- When logic changes in the canonical decider:
  - Single-tenant regression tests must verify:
    - No unexpected action thrash,  
    - SLO behavior remains acceptable,  
    - Budgets are enforced per design.

- When logic changes in multi-tenant variants:
  - Single-tenant tests should confirm:
    - No unintended cross-pollination (e.g., fairness code affecting single-tenant runs).

### Offline Simulator Usage

Although multi-tenant and fairness experiments are more prominent in the simulator, single-tenant configurations should still be exercised:

- Using the **Offline Simulator variant** to:
  - Replay synthetic time-series telemetry,  
  - Evaluate horizon and threshold experiments in single-tenant context,  
  - Confirm stability and budget adherence.

---

## 🧠 Story Node & Focus Mode Integration

The single-tenant variant supports straightforward narratives for:

- Project-specific environments:  
  “How does autonomy behave in the single-owner hydrology cluster?”  

- Pre-multi-tenant phases:  
  “What did autonomy look like before we added multi-tenant fairness?”

To keep this doc Focus Mode–friendly:

- Sections are narrowly scoped (Overview, Context, Architecture, Data/Metadata, CI/CD, Version History).  
- Links to:
  - Variants index,  
  - Canonical decider spec,  
  - Offline simulator and experiments.

Example Story Node anchor:

~~~text
Related Story Node:
urn:kfm:story-node:pipelines:autonomy-matrix:decider:variant:single-tenant:overview
~~~

Story Nodes must clearly label this as a **variant design intended for single-tenant clusters**, not a replacement for multi-tenant or canonical configurations in shared environments.

---

## 🕰️ Version History

| Version    | Date       | Summary                                                                                                               |
|-----------:|------------|-----------------------------------------------------------------------------------------------------------------------|
| **v11.2.4**| 2025-12-05 | Initial single-tenant decider variant design. Defines scope, architecture, metadata expectations, and CI considerations.|

---

<div align="center">

🧠 **KFM v11 — Single-Tenant Autonomy Decider Variant**  
Simplified Control Plane · Single-Owner Stewardship · FAIR+CARE-Governed Autonomy  

[🧠 Decider Variants Index](README.md) · [🧠 Decider Spec](../README.md) · [🤖 Autonomy Matrix Spec](../../../README.md)

</div>

