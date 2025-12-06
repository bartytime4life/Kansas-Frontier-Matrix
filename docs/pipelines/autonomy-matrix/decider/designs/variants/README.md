---
title: "🧠 KFM v11 — Autonomy Decider Variants"
description: "Design variants for the KFM Autonomy Decider kernel, including single-tenant, multi-tenant, and offline simulation control-plane shapes."
path: "docs/pipelines/autonomy-matrix/decider/designs/variants/README.md"
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

intent: "autonomy-matrix-decider-variants"
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

category: "Pipelines · Autonomy · Governance · Architecture · Variants"

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
  - "docs/pipelines/autonomy-matrix/decider/designs/README.md@v11.2.4"
  - "docs/pipelines/autonomy-matrix/decider/README.md@v11.2.4"
  - "docs/pipelines/autonomy-matrix/README.md@v11.2.4"
  - "docs/pipelines/reliability/README.md"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/docs-pipelines-autonomy-decider-variants-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/docs-pipelines-autonomy-decider-variants-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "mutable"

doc_uuid: "urn:kfm:doc:pipelines:autonomy-matrix:decider:designs:variants:v11.2.4"
semantic_document_id: "kfm-pipelines-autonomy-matrix-decider-variants-v11.2.4"
event_source_id: "ledger:kfm:doc:pipelines:autonomy-matrix:decider:designs:variants:v11.2.4"

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
    - "🗺️ Diagrams"
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

# 🧠 **KFM v11 — Autonomy Decider Variants**  
`docs/pipelines/autonomy-matrix/decider/designs/variants/README.md`

**Purpose:**  
Describe **design variants** of the KFM Autonomy Decider kernel — including single-tenant, multi-tenant,  
and offline simulation control-plane shapes — to support different deployment topologies without  
changing the **normative autonomy contract** or compromising determinism, explainability, or FAIR+CARE governance.

</div>

---

## 📘 Overview

This document is the **index and guide** for Autonomy Decider variants:

- Captures **non-normative** but implementation-relevant designs for:
  - 🧩 *Single-tenant decider* — simplified control plane for single-tenant clusters.  
  - 🧩 *Multi-tenant decider* — shared clusters with fairness and quota logic.  
  - 🧩 *Offline simulator* — replay and “what-if” environment for autonomy changes.  
- Ensures each variant:
  - Respects the **canonical autonomy contract** (inputs/outputs, actions, invariants),  
  - Stays **config-driven and deterministic**,  
  - Surfaces its tradeoffs for reliability, sustainability, and governance.

Normative behavior is defined in:

- `docs/pipelines/autonomy-matrix/README.md`  
- `docs/pipelines/autonomy-matrix/decider/README.md`  

Variants here may be promoted to normative status in future versions (e.g., v12), but until then they remain **design space** only.

---

## 🗂️ Directory Layout

~~~text
docs/pipelines/autonomy-matrix/decider/designs/variants/
│
├── 📄 README.md                    # This file (variants index & guidance)
│
├── 📄 single-tenant.md             # Simplified decider for single-tenant clusters
├── 📄 multi-tenant.md              # Multi-tenant fairness and quota-aware decider
├── 📄 offline-simulator.md         # Offline replay & simulation decider design
│
└── 📂 experiments/                 # Optional, time-bounded design explorations
    ├── 📄 fairness-experiments.md  # Proposals for fairness metrics & arbitration rules
    └── 📄 horizon-tuning.md        # Experiments on decision window length & aggregation
~~~

**Author rules:**

- Use this `README.md` as the **entry point**; variant docs must link back here and to the main Decider spec.  
- Any variant that alters **externally visible behavior** must:
  - Explicitly compare itself to the canonical decider, and  
  - Describe a **migration path** (or clearly state “no migration: experimental only”).  
- Files under `experiments/` are strictly **time-bounded proposals**; they must note:
  - Status (`exploratory`, `adopted`, `rejected`),
  - Target autonomy version (e.g., “candidate for v11.3” or “v12+ only”).

---

## 🧭 Context

The canonical Autonomy Decider defines:

- How **per-pipeline snapshots** (profiles + telemetry) become decisions.  
- A deterministic mapping `{score, gates, context} → action`.  
- Contracts for decision records and OpenLineage events.

Variants are introduced to handle scenarios such as:

- Clusters with **multiple teams/tenants** sharing CPU/GPU budgets.  
- Clusters where a single tenant wants **simpler autonomy behavior** (less coordination, more direct SLO mapping).  
- Environments where autonomy logic must be **replayed and validated offline** before roll-out.

This directory:

- Keeps those shapes **explicit**,  
- Prevents “shadow behavior” from emerging in code without design review,  
- Provides a path from **experiment → candidate → normative**.

---

## 🧱 Architecture

### Variant 1 — Single-Tenant Decider

**Goal:** Simplify autonomy for environments where:

- Only one tenant/team owns the cluster, and  
- Resource contention is primarily within that team’s pipelines.

Key characteristics:

- No cross-tenant fairness logic; decisions depend only on:
  - Per-pipeline SLOs and budgets,
  - Global cluster caps (cost, energy, carbon),
  - CARE/sovereignty gates.
- Easier to reason about and simulate:
  - “Do we meet our SLOs?”  
  - “Are we within our budgets?”  
  - “Are we respecting CARE and sovereignty policies?”

### Variant 2 — Multi-Tenant Decider

**Goal:** Provide fairness and quota management across multiple tenants.

Key characteristics:

- Maintains per-tenant **quotas** (cost, energy, carbon) and **priority bands**.  
- Arbitrates when multiple tenants demand more resources than the cluster can provide.  
- May use fairness policies such as:
  - Weighted fair sharing,
  - Priority bands (P0–P4),
  - Minimum/maximum guaranteed shares.

### Variant 3 — Offline Simulator

**Goal:** Safely test autonomy logic on historical data before production rollout.

Key characteristics:

- Reads historical telemetry and decisions from `telemetry/*.jsonl` (or a clone).  
- Applies a **candidate decider variant** to those snapshots.  
- Produces a report:
  - How many decisions would have changed,  
  - How budgets and SLOs would have been affected,  
  - How often gates would have triggered.

Used for:

- Regression checks when updating scoring/gating logic.  
- Evaluating new fairness or sustainability policies.

---

## 🗺️ Diagrams

A typical **multi-tenant variant** introduces an extra fairness layer around the canonical decider:

~~~mermaid
flowchart LR
    subgraph TENANTS[Tenants]
        T1["Tenant A<br/>Pipelines"] 
        T2["Tenant B<br/>Pipelines"]
        T3["Tenant C<br/>Pipelines"]
    end

    TENANTS --> Q["Quota & Fairness Layer<br/>(multi-tenant variant)"]
    Q --> D["Autonomy Decider Core<br/>canonical scoring + gates"]
    D --> A["Actions<br/>resume / slow / pause / escalate"]
    A --> R["Orchestrators<br/>Airflow · Dagster · LangGraph"]
~~~

Variant-specific docs (e.g., `multi-tenant.md`) should:

- Provide their own diagrams with tenant- or environment-specific detail.  
- Clearly label **what is re-used** from the canonical decider vs. what is new.  

Avoid using `\n` in Mermaid labels; use `<br/>` for line breaks to keep Mermaid parsers happy.

---

## 🧪 Validation & CI/CD

Variant designs are still subject to **strong validation**, even before they become normative:

- **Design-level checks**
  - Markdown, schema, and accessibility lint as usual.  
  - Provenance checks to ensure variants reference:
    - Canonical Autonomy Matrix spec,
    - Decider spec,
    - Any relevant schemas.

- **Implementation gating**
  - A variant should not be enabled in production **by default** until:
    - It has an associated design doc in this directory,
    - There is a clearly defined **config flag** (e.g., `autonomy.variant: multi-tenant`),
    - There are tests demonstrating its behavior on fixtures.

- **Simulation-first workflow**
  - New variants must typically go through the offline simulator:
    - Run on historical telemetry,
    - Compare decisions vs. canonical decider,
    - Produce a regression report attached to the PR.

CI SHOULD include:

- Variant-specific test suites (e.g., `tests/autonomy/variants/`).  
- A check that no variant is **secretly enabled** without an explicit config and design reference.

---

## 📦 Data & Metadata

Variants interact with:

- **Autonomy profiles**
  - May add variant-specific fields (e.g., per-tenant quotas).  
  - Such changes must be proposed here before changing schemas.
- **Telemetry**
  - Multi-tenant variants might require:
    - Tenant identifiers,  
    - Per-tenant aggregated metrics,  
    - Additional fairness metadata in decision records.

When proposing a variant that extends metadata:

- Provide example snippets (YAML/JSON) in the variant doc.  
- Tag fields explicitly as **proposed** until schemas and normative docs are updated.  

Example (illustrative, not yet normative):

~~~yaml
tenant:
  id: "tenant-a"
  quota:
    monthly_cost_usd: 5000
    monthly_energy_kwh: 800
    monthly_carbon_kgco2e: 200
  priority_band: "P1"
~~~

---

## 🧠 Story Node & Focus Mode Integration

Variants are primarily internal to engineers, but Focus Mode may surface them in:

- Internal design reviews,  
- Training for reliability and autonomy teams,  
- “Why we changed decider behavior” narratives.

To keep these docs Story-Node friendly:

- Label sections clearly as **variant** vs. **canonical**.  
- Start variant docs with a short **“When to use this variant”** paragraph.  
- Summarize tradeoffs in bullet lists so Focus Mode can extract them cleanly.

Example Story Node anchor:

~~~text
Related Story Node:
urn:kfm:story-node:pipelines:autonomy-matrix:decider:variants:multi-tenant:overview
~~~

---

## 🕰️ Version History

| Version    | Date       | Summary                                                                                                               |
|-----------:|------------|-----------------------------------------------------------------------------------------------------------------------|
| **v11.2.4**| 2025-12-05 | Initial creation of Autonomy Decider Variants README. Defines single-tenant, multi-tenant, and offline simulator roles and how they relate to the canonical decider. |

---

<div align="center">

🧠 **KFM v11 — Autonomy Decider Variants**  
Design-First Autonomy · Fairness-Aware Control Plane · Simulation-Backed Evolution  

[🧠 Decider Designs](../README.md) · [🧠 Decider Spec](../../README.md) · [🤖 Autonomy Matrix Spec](../../../README.md)

</div>

