---
title: "🧠 KFM v11 — Autonomy Decider Designs"
description: "Non-normative design notes for the KFM Autonomy Decider kernel: state machines, control-flow variants, and backlog for the self-balancing pipeline control plane."
path: "docs/pipelines/autonomy-matrix/decider/designs/README.md"
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

sbom_ref: "../../../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.4/autonomy-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/autonomy-matrix-v1.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

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

intent: "autonomy-matrix-decider-designs"
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

category: "Pipelines · Autonomy · Governance · Architecture · Designs"

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
  - "docs/pipelines/autonomy-matrix/decider/README.md@v11.2.4"
  - "docs/pipelines/autonomy-matrix/README.md@v11.2.4"
  - "docs/pipelines/reliability/README.md"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/docs-pipelines-autonomy-decider-designs-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/docs-pipelines-autonomy-decider-designs-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "mutable"

doc_uuid: "urn:kfm:doc:pipelines:autonomy-matrix:decider:designs:v11.2.4"
semantic_document_id: "kfm-pipelines-autonomy-matrix-decider-designs-v11.2.4"
event_source_id: "ledger:kfm:doc:pipelines:autonomy-matrix:decider:designs:v11.2.4"

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

# 🧠 **KFM v11 — Autonomy Decider Designs**  
`docs/pipelines/autonomy-matrix/decider/designs/README.md`

**Purpose:**  
Collect non-normative but **implementation-critical design notes** for the Autonomy Decider kernel:  
state machines, control-flow variants, and backlog items that inform how the KFM pipeline control plane evolves across releases.

</div>

---

## 📘 Overview

This document describes the **design space** for the KFM Autonomy Decider:

- How different **state-machine variants** handle pipeline decisions.  
- What tradeoffs exist between **latency, stability, and explainability**.  
- Which experiments are underway or planned to improve:
  - scoring functions,
  - gate composition,
  - multi-pipeline coordination at cluster scale.

Normative behavior (the contract other components must rely on) is defined in:

- `docs/pipelines/autonomy-matrix/README.md`  
- `docs/pipelines/autonomy-matrix/decider/README.md`  

The designs here are **advisory**: they must not be treated as authoritative policy until integrated into those normative documents and released under a new version.

---

## 🗂️ Directory Layout

~~~text
docs/pipelines/autonomy-matrix/decider/designs/
│
├── 📄 README.md                 # This file (design index & guidance)
│
├── 📄 state-machine.md          # Detailed state diagrams and transition rules
├── 📄 backlog.md                # Known limitations, ideas, and phased improvements
│
└── 📂 variants/                 # Optional experimental decider variants
    ├── 📄 single-tenant.md      # Simplified decider for single-tenant / single-cluster setups
    ├── 📄 multi-tenant.md       # Design for cross-tenant fairness & quotas
    └── 📄 offline-simulator.md  # Offline replay & simulation design notes
~~~

**Author rules:**

- New design notes belong either:
  - in `variants/` (for specific alternative decider shapes), or  
  - in `backlog.md` (for prioritized future changes).  
- Any design that changes **user-visible or API-visible behavior** must be:
  - linked from this README,
  - reflected in a future update of the normative decider spec.

---

## 🧭 Context

The decider is one layer in the Autonomy Matrix:

- **Profiles** (`pipeline-profiles/*.yaml`) define:
  - SLOs, budgets, CARE labels, sovereignty policies.
- **Gates** (`gates/*.md`) define:
  - Hard/soft governance constraints (CARE, cost, freshness, cardinality).
- **Telemetry** (`telemetry/*.jsonl`) provides:
  - Live metrics (lag, cost, energy, carbon, trust).

Design documents in this directory answer questions like:

- Should the decider **act per-run** or **per-window** (e.g., every 5 minutes)?  
- When multiple pipelines are in conflict (e.g., all want more budget), how do we arbitrage?  
- Can we reuse the same LangGraph graph for different tenants or environments?  
- How do we keep explanations short but faithful when dozens of gates contribute?

These notes help architects and implementers reason about those decisions before they become part of the formal contract.

---

## 🧱 Architecture

At a high level, the decider is a **control-plane service** that can be embedded in:

- Orchestrators (e.g., Airflow/Dagster operators),  
- LangGraph graphs coordinating multiple tools,  
- Dedicated autonomy services invoked via HTTP/RPC.

A common “embedded service” architecture looks like:

~~~mermaid
flowchart LR
    P[Pipeline Orchestrator\n(Airflow/Dagster/LangGraph)] --> R[Runtime Snapshot\ntelemetry + profile ref]
    R --> D[Autonomy Decider\n(this component)]
    D --> A[Action Object\nresume/slow/pause/escalate]
    A --> P
    D --> T[Telemetry & OpenLineage\njsonl + events]
~~~

### Key Architectural Decisions (captured in `state-machine.md`)

- **Decision frequency**  
  - Per-run, per-window, or hybrid (window-level baseline, run-level overrides).
- **Aggregation strategy**  
  - How metrics across regions, tenants, or shards are aggregated before scoring.
- **Failure handling**  
  - What happens if:
    - Telemetry is missing or delayed,  
    - Profile load fails,  
    - Gate evaluation errors.

### Experimental Variants (captured under `variants/`)

- **Single-tenant**  
  - Simplified fairness logic; focus on SLOs and budgets within one project.
- **Multi-tenant**  
  - Shared cluster; fairness between tenants, quotas per team, and global carbon budgets.
- **Offline simulator**  
  - Batch replays of historical telemetry to validate new scoring/gating logic before production rollout.

Each variant document must explicitly state:

- Which invariants it shares with the canonical decider,  
- Which invariants it relaxes or adds,  
- What migration path exists (if any) from the current canonical behavior.

---

## 🗺️ Diagrams

Design docs under this directory are expected to include **Mermaid diagrams** for:

- State machines (e.g., decision lifecycle, error handling paths).  
- Data flow (snapshot ingress → decider → telemetry/lineage outputs).  
- Multi-pipeline coordination where applicable.

Use only the approved diagram profiles:

- `mermaid-flowchart-v1` for state and data flow diagrams.  
- `mermaid-timeline-v1` if you need to show evolution over releases.

Example (to be extended in `state-machine.md`):

~~~mermaid
flowchart TD
    Idle --> SnapshotReady
    SnapshotReady --> Evaluating
    Evaluating --> DecisionReady
    DecisionReady --> Idle
    Evaluating --> Error
    Error --> Escalated
~~~

Each diagram must be:

- Accompanied by a short caption describing its purpose.  
- Kept in sync with the text and any referenced schemas or contracts.

---

## 🧪 Validation & CI/CD

Although design docs are non-normative, they are still:

- **Linted and schema-validated**:
  - `markdown-lint` for structure,
  - `schema-lint` for front-matter,
  - `accessibility-check` for headings and links.  
- **Provenance-checked**:
  - Ensure design notes consistently reference the normative decider spec and Autonomy Matrix spec.  
- **Linked into tests** (where relevant):
  - When a design is adopted, its corresponding tests in `tests/` should reference the design or state-machine version in comments, so engineers can track why tests look the way they do.

CI SHOULD fail if:

- A design document claims a behavior that contradicts the current normative spec **without** referencing a planned migration or future version.  
- Front-matter is missing required fields (including provenance links back to decider and Autonomy Matrix specs).

---

## 📦 Data & Metadata

Designs interact with metadata in several ways:

- **Config shapes**  
  - Proposed changes to autonomy profile schemas must be described here before being implemented:
    - New gate types,
    - New scoring weights,
    - New telemetry channels.
- **Telemetry extensions**  
  - If designs require additional metrics (e.g., GPU utilization, storage churn), they must:
    - Be added to telemetry schemas in `schemas/telemetry/`,
    - Have associated notes here explaining how they influence decisions.

When documenting a proposed schema change:

- Include a minimal YAML/JSON **example snippet**.  
- Note whether it is backward compatible or requires a migration.

Example (illustrative only):

~~~yaml
autonomy:
  weights:
    freshness: 0.40
    urgency: 0.35
    trust: 0.25
    cost: 0.60
    energy: 0.40
    carbon: 0.50
  horizon:
    decision_window: "5m"
    aggregation: "sliding"
~~~

These are **design proposals** until the schemas and normative docs are updated.

---

## 🧠 Story Node & Focus Mode Integration

Design docs are useful for:

- Internal **engineer onboarding** to the decider.  
- Explaining **why** certain tradeoffs were made (e.g., fairness vs. latency).  
- Providing historical context for how autonomy behavior evolved.

To make them Focus Mode–friendly:

- Keep each H2/H3 section focused on a single concept.  
- Use bullet lists for tradeoffs and pros/cons.  
- Clearly mark:
  - “Adopted design” vs. “Rejected alternative” vs. “Open question”.

Story Nodes may link to specific design sections, but UI components should always **distinguish design notes from normative behavior** (e.g., with labels like “Design Proposal”).

---

## 🕰️ Version History

| Version    | Date       | Summary                                                                                                      |
|-----------:|------------|--------------------------------------------------------------------------------------------------------------|
| **v11.2.4**| 2025-12-05 | Initial creation of Autonomy Decider Designs README. Captures scope, directory layout, architecture hooks, and CI expectations. |

---

<div align="center">

🧠 **KFM v11 — Autonomy Decider Designs**  
Design-First Autonomy · Explainable Control Plane · FAIR+CARE-Governed Evolution  

[🧠 Decider Spec](../README.md) · [🤖 Autonomy Matrix Spec](../../README.md) · [⚖ Governance](../../../../governance/ROOT-GOVERNANCE.md)

</div>

