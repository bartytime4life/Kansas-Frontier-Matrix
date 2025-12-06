---
title: "🧠 KFM v11 — Multi-Tenant Autonomy Decider Variant"
description: "Architecture and design for a multi-tenant, quota- and fairness-aware variant of the KFM v11 Autonomy Decider."
path: "docs/pipelines/autonomy-matrix/decider/designs/variants/multi-tenant.md"
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

intent: "autonomy-matrix-decider-variant-multi-tenant"
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
  - "fairness"
  - "multi-tenant"

category: "Pipelines · Autonomy · Governance · Architecture · Variants"

sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Internal"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: false

data_steward: "Reliability · Sustainability · FAIR+CARE Council"
ttl_policy: "Indefinite (subject to architecture changes)"
sunset_policy: "Supersede when Autonomy Matrix v12 multi-tenant variant is adopted"

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

json_schema_ref: "schemas/json/docs-pipelines-autonomy-decider-variant-multi-tenant-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/docs-pipelines-autonomy-decider-variant-multi-tenant-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "mutable"

doc_uuid: "urn:kfm:doc:pipelines:autonomy-matrix:decider:designs:variants:multi-tenant:v11.2.4"
semantic_document_id: "kfm-pipelines-autonomy-matrix-decider-variant-multi-tenant-v11.2.4"
event_source_id: "ledger:kfm:doc:pipelines:autonomy-matrix:decider:designs:variants:multi-tenant:v11.2.4"

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

# 🧠 **KFM v11 — Multi-Tenant Autonomy Decider Variant**  
`docs/pipelines/autonomy-matrix/decider/designs/variants/multi-tenant.md`

**Purpose:**  
Describe a **multi-tenant variant** of the Autonomy Decider that shares cluster resources  
across multiple tenants and pipelines using **quotas, priority bands, and fairness rules**,  
while preserving determinism, explainability, and FAIR+CARE-aligned governance.

</div>

---

## 📘 Overview

This document defines the **multi-tenant Autonomy Decider variant**:

- Extends the canonical decider with **tenant-aware fairness logic**.  
- Enforces **per-tenant budgets** (cost, energy, carbon) and **priority bands** (P0–P4).  
- Arbitrates between tenants and pipelines when shared resources are constrained.  
- Remains **config-driven** and **deterministic**: same inputs ⇒ same decisions.

Normative Autonomy behavior is defined in:

- `docs/pipelines/autonomy-matrix/README.md`  
- `docs/pipelines/autonomy-matrix/decider/README.md`  

This multi-tenant design is **variant-only**:

- It may be enabled explicitly via config (e.g., `autonomy.variant: multi-tenant`).  
- It must never silently change the canonical single-tenant semantics.  
- Adoption of this variant as default behavior requires a future, versioned spec update.

---

## 🧭 Context

The multi-tenant variant is motivated by environments where:

- **Multiple teams/tenants** share the same compute, storage, and emissions budgets.  
- Pipelines from different tenants:
  - Have different **priority bands** (P0: critical; P3: background),  
  - Draw from **common cluster-level budgets** (cost, energy, carbon),  
  - May have **different CARE/sovereignty constraints**.

Key relationships:

- **Reliability**  
  - Per-pipeline SLOs remain defined in reliability docs and pipeline profiles.  
- **Sustainability**  
  - Cluster-level cost/energy/carbon guardrails must still be respected.  
- **FAIR+CARE & Sovereignty**  
  - Fairness policies must **not** erode protections for sensitive or community-governed data.  
- **Variants & Experiments**  
  - Fairness experiments (see `fairness-experiments.md`) use this variant as their architectural base.

The variant must be compatible with:

- Existing telemetry schemas,  
- Existing pipeline autonomy profiles (with tenant metadata extensions),  
- Existing governance and provenance expectations.

---

## 🧱 Architecture

### High-Level Structure

At a high level, the multi-tenant variant wraps the canonical decider with a **tenant-aware fairness layer**:

~~~mermaid
flowchart LR
    subgraph TENANTS[Tenants & Pipelines]
        TA["Tenant A<br/>Pipelines"]
        TB["Tenant B<br/>Pipelines"]
        TC["Tenant C<br/>Pipelines"]
    end

    TENANTS --> Q["Quota & Fairness Layer<br/>multi-tenant variant"]
    Q --> D["Autonomy Decider Core<br/>canonical scoring + gates"]
    D --> A["Actions<br/>resume / slow / pause / escalate"]
    A --> O["Orchestrators<br/>Airflow · Dagster · LangGraph"]
~~~

**Key idea:**  
The fairness layer **pre-processes** resource demands and budgets across tenants, then feeds derived constraints into the canonical decider, which continues to compute per-pipeline actions as usual.

### Components

#### 1. Tenant Registry

A logical view of tenants and their budgets:

- Tenant ID (synthetic example: `example-tenant-a`).  
- Optional **weight** for fairness policies (e.g., weighted fair sharing).  
- Quotas:
  - Monthly cost, energy, and carbon caps.  
- Governance:
  - CARE labels or categories relevant at tenant level (if any).

#### 2. Fairness Policy Engine

Interprets **tenant registry + telemetry** to determine:

- How much capacity each tenant may draw during a decision horizon.  
- How to allocate **shared headroom** when some tenants underutilize quotas.  
- Whether any tenant is in **quota violation** or **near violation**, and what penalty/bias to apply.

Example policy families (further detailed in `fairness-experiments.md`):

- **Quota-strict** — tenants may never exceed their quotas.  
- **Weighted fair sharing** — spare capacity is redistributed based on tenant weights & priorities.  
- **Priority-band aware** — P0/P1 pipelines can momentarily borrow from lower-priority budgets.

#### 3. Canonical Decider

Unchanged in principle:

- Computes per-pipeline scores and applies gates as defined in the canonical spec.  
- Consumes **effective budgets and penalty weights** supplied by the fairness layer.  
- Remains responsible for:
  - Per-pipeline decisions,  
  - Telemetry emission (decisions & OpenLineage),  
  - Governance evidence.

#### 4. Integration with Orchestrators

The action contract remains the same:

- Each pipeline receives one of `resume`, `slow`, `pause`, or `escalate`.  
- Orchestrators (Airflow, Dagster, LangGraph) interpret actions as before.

Differences:

- In multi-tenant mode, **global context** (tenant & budgets) may influence decisions, but only through config and fairness layer outputs — not through ad hoc logic.

### Invariants

The variant must uphold:

- **Determinism**  
  - Given the same tenant registry, telemetry, and configs, decisions must be identical.  
- **No hidden state**  
  - Any state (e.g., moving averages, fairness allocation) must be observable via telemetry or logs.  
- **Explainability**  
  - For any decision, we must be able to answer:
    - “Which tenant-level rules influenced this?”  
    - “How did fairness/quotas affect this action?”  
- **Compatibility**  
  - Disabling the variant (switching back to single-tenant canonical mode) must:
    - Not require migration of pipeline profiles,  
    - Be achieved via explicit config (e.g., `autonomy.variant: single-tenant`).

---

## 📦 Data & Metadata

The multi-tenant variant introduces **tenant-level metadata** and potentially extends pipeline profiles.

### Tenant-Level Metadata (Conceptual)

This may live outside `docs/` (e.g., under `config/autonomy/tenants/*.yaml`), but the structure is documented here:

~~~yaml
tenant_id: "example-tenant-a"
display_name: "Example Tenant A"
weight: 0.5
budgets:
  monthly_cost_usd: 5000
  monthly_energy_kwh: 800
  monthly_carbon_kgco2e: 200
priority_defaults:
  default_priority_band: "P2"
governance:
  care_label: "Synthetic-General"
  sovereignty_policy: "synthetic-default-v1"
~~~

### Pipeline Profile Extensions (Design-Level)

Pipeline autonomy profiles (`pipeline-profiles/*.yaml`) may include:

~~~yaml
pipeline: "example/hydro-hrrr"
tenant: "example-tenant-a"
priority_band: "P1"
governance:
  care_label: "Synthetic-Waters"
  sovereignty_policy: "synthetic-h3-generalization-v1"
autonomy:
  actions: ["resume", "slow", "pause", "escalate"]
  # existing fields...
~~~

These fields:

- Are consistent with the fairness and experiment docs.  
- Remain **design proposals** until schemas and canonical docs explicitly adopt them.

### Telemetry Additions

Telemetry for multi-tenant mode may include:

- Tenant identifiers and weights,  
- Per-tenant budget utilization metrics,  
- Fairness policy outcomes (e.g., “borrowed_capacity”, “quota_violation_flags”).

Example (simplified):

~~~json
{
  "pipeline": "example/hydro-hrrr",
  "tenant": "example-tenant-a",
  "priority_band": "P1",
  "decision": "slow",
  "fairness": {
    "policy": "weighted-fair-sharing",
    "tenant_weight": 0.5,
    "tenant_quota_utilization": {
      "cost": 0.76,
      "energy": 0.68,
      "carbon": 0.73
    },
    "sharing_state": "under_quota_with_borrowed_capacity"
  }
}
~~~

All IDs and values for examples must be **synthetic** or anonymized.

---

## 🧪 Validation & CI/CD

The multi-tenant variant is guarded by:

### Config & Schema Validation

- Tenant configs and extended pipeline profiles must validate against:
  - Autonomy profile and tenant schemas (JSON/SHACL).  
- CI must ensure:
  - No variant-only fields leak into canonical mode unintentionally.  
  - Disabling the variant still yields valid configs.

### Behavioral Tests

- **Unit tests** for fairness layer:
  - Quota-strict behavior,  
  - Weighted-fair-sharing behavior,  
  - Priority-band-aware behavior.  
- **Integration tests** for decider + fairness:
  - Use fixtures from `fixtures/` and `fixtures/samples/`.  
  - Compare canonical (single-tenant) and multi-tenant decisions.

### Regression & Guardrails

- CI should compute:
  - Changes in slowdown/pause rates per tenant & priority band,  
  - Quota violation counts,  
  - Effects on cost/energy/carbon budgets.

Guardrails:

- No tenant should be permanently starved without explicit design justification.  
- CARE-sensitive synthetic workloads must not suffer worsened protection.  
- Changes must be explainable using telemetry and logs.

### Feature Flags

- Multi-tenant mode must be gated behind:
  - Explicit config flags (e.g., `autonomy.variant: multi-tenant`),  
  - Environment-scoped rollout strategies (e.g., staging-only first).

---

## 🧠 Story Node & Focus Mode Integration

This variant underpins narratives such as:

- “How does KFM share resources fairly across tenants?”  
- “Why was Tenant B slowed more than Tenant A during a budget crunch?”  
- “What changed when we enabled multi-tenant autonomy?”

To support Story Nodes and Focus Mode:

- Keep this doc **high-level and structured**, with clear section scopes.  
- Let experiment docs (`fairness-experiments.md`, `cost-energy-thresholds.md`, `horizon-tuning.md`) carry scenario-specific stories.  
- Use explicit references to:
  - Tenant-level configs,  
  - Fairness policies,  
  - Telemetry schemas.

Example Story Node anchor:

~~~text
Related Story Node:
urn:kfm:story-node:pipelines:autonomy-matrix:decider:variant:multi-tenant:overview
~~~

Story Nodes must clearly label this as a **variant design**, not default behavior, unless future specs promote it.

---

## 🕰️ Version History

| Version    | Date       | Summary                                                                                                             |
|-----------:|------------|---------------------------------------------------------------------------------------------------------------------|
| **v11.2.4**| 2025-12-05 | Initial multi-tenant decider variant design. Defines fairness layer, tenant metadata, invariants, and CI expectations.|

---

<div align="center">

🧠 **KFM v11 — Multi-Tenant Autonomy Decider Variant**  
Fairness-Aware Control Plane · Multi-Tenant Stewardship · FAIR+CARE-Governed Resource Sharing  

[🧠 Decider Variants Index](README.md) · [🧪 Fairness Experiments](experiments/fairness-experiments.md) · [🤖 Autonomy Matrix Spec](../../../README.md)

</div>

