---
title: "📚 KFM v11 — Autonomy Matrix Examples & Replay Guide"
description: "Example decisions, autonomy profiles, and replay patterns for the KFM Autonomy Matrix for Self-Balancing Pipelines."
path: "docs/pipelines/autonomy-matrix/examples/README.md"
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

intent: "autonomy-matrix-examples"
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
category: "Pipelines · Autonomy · Governance · Examples"

sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Internal"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: false

data_steward: "Reliability · Sustainability · FAIR+CARE Council"
ttl_policy: "Indefinite (subject to architecture changes)"
sunset_policy: "Supersede when Autonomy Matrix v12 example set is adopted"

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

json_schema_ref: "schemas/json/docs-pipelines-autonomy-matrix-examples-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/docs-pipelines-autonomy-matrix-examples-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "mutable"

doc_uuid: "urn:kfm:doc:pipelines:autonomy-matrix:examples:v11.2.4"
semantic_document_id: "kfm-pipelines-autonomy-matrix-examples-v11.2.4"
event_source_id: "ledger:kfm:doc:pipelines:autonomy-matrix:examples:v11.2.4"

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
    - "🧪 Example Types"
    - "🧰 How to Reproduce Decisions"
    - "📦 Data & Metadata"
    - "🧠 Story Node & Focus Mode Integration"
    - "🧪 Validation & CI/CD"
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

# 📚 **KFM v11 — Autonomy Matrix Examples & Replay Guide**  
`docs/pipelines/autonomy-matrix/examples/README.md`

**Purpose:**  
Provide **concrete, replayable examples** of the KFM Autonomy Matrix in action, including sample decisions, autonomy profiles, and telemetry snippets.  
These examples are designed to be **deterministic, CI-safe, and FAIR+CARE-aligned**, so engineers can clone, replay, and extend autonomy behavior without ambiguity.

</div>

---

## 📘 Overview

This guide explains how to use the **examples** under `docs/pipelines/autonomy-matrix/examples/` to:

- Understand how the **Autonomy Matrix** evaluates pipelines and chooses actions.  
- Replay real-world–style decisions in local or staging environments.  
- Bootstrap new **pipeline autonomy profiles** and governance gates from working templates.  
- Validate that autonomy behavior remains **deterministic**, **explainable**, and **governance-safe** as pipelines evolve.

Examples here are **didactic**: they illustrate patterns, not production secrets. Any sensitive details (e.g., actual costs or sensitive datasets) must be redacted or generalized.

---

## 🗂️ Directory Layout

~~~text
docs/pipelines/autonomy-matrix/examples/
│
├── 📄 README.md                      # This file (examples + replay guide)
│
├── 📄 sample-decision.md             # Fully-worked decision example (narrative + JSON)
├── 📄 sample-pipeline-profile.yaml   # Template autonomy profile for a single pipeline
├── 📄 sample-gates-scenario.md       # Example of gates (CARE, cost, freshness) triggering
│
└── 📂 scenarios/                     # Optional extended scenarios (if needed)
    ├── 📄 high-urgency-low-cost.md   # P0 weather safety pipeline (resume bias)
    ├── 📄 low-urgency-high-cost.md   # Backfill pipeline hitting cost/energy caps
    └── 📄 mixed-signals-escalate.md  # Conflicting signals → escalate + human review
~~~

**Author rules:**

- Any new example **MUST** be added to this tree, with a short inline comment.  
- Example files:
  - Use **synthetic or anonymized** data; never embed secrets or production identifiers.  
  - Reference the **main Autonomy Matrix README** and relevant `pipeline-profiles/*.yaml`.  
  - Follow KFM-MDP v11.2.4 heading and footer rules.

---

## 🧭 Context

Examples in this directory are tightly coupled to:

- **Autonomy specification:**  
  `docs/pipelines/autonomy-matrix/README.md` — the normative contract for the control plane.
- **Reliability and SLOs:**  
  `docs/pipelines/reliability/README.md` — defines the SLOs and error budgets the Autonomy Matrix enforces.
- **FAIR+CARE & sovereignty:**  
  FAIR+CARE and Indigenous data policies determine how sensitive pipelines may be slowed or paused.

Think of this directory as a **sandbox for understanding behavior**, not a place to define new policy. Policies live in standards and pipeline profiles; examples just **demonstrate** them.

---

## 🧪 Example Types

Examples should fall into one (or more) of these categories:

1. **Decision Walkthroughs (`sample-decision.md`)**  
   - A single autonomy decision, with:
     - The **input state** (pipeline profile + telemetry snapshot),
     - The **computed score** breakdown,
     - The **gates** evaluated and which ones fired,
     - The resulting **action** (resume/slow/pause/escalate),
     - A **narrative explanation** tying it back to governance rules.

2. **Profile Templates (`sample-pipeline-profile.yaml`)**  
   - A complete, schema-valid example of a pipeline autonomy profile:
     - SLOs, budgets, CARE labels, sovereignty policies, gates, and telemetry bindings.
   - Ready to be copied into `pipeline-profiles/` and customized.

3. **Gate Scenarios (`sample-gates-scenario.md`)**  
   - Focus on specific gates (e.g., cost-energy-gates, care-governance, cardinality-guard).
   - Show how inputs cross thresholds and how actions change.

4. **Scenario Series (`scenarios/`)**  
   - Multi-step examples where:
     - Inputs change over time (e.g., cost creeping up, carbon caps nearing),
     - Autonomy decisions change accordingly (resume → slow → escalate).

Each example should clearly state its **type** and **intended lesson** in its Overview section.

---

## 🧰 How to Reproduce Decisions

To keep examples **replayable**, each decision walkthrough must specify:

1. **Config references**  
   - Which autonomy profile(s) were used:
     - `docs/pipelines/autonomy-matrix/pipeline-profiles/<pipeline>.yaml`
   - Which gate configs (if any) were customized.

2. **Telemetry snapshot**  
   - Provide a small JSON block representing the relevant metrics at decision time:
     - Freshness (lag, backlog),
     - Cost/energy/carbon,
     - Validation / trust flags.

3. **CLI / notebook replay** (pseudo-contract)

For example, a decision replay might conceptually look like:

~~~bash
# Conceptual interface — actual path / binary may differ
kfm-autonomy replay \
  --pipeline hydro/hrrr-downscale \
  --profile docs/pipelines/autonomy-matrix/pipeline-profiles/hydro-hrrr-downscale.yaml \
  --snapshot docs/pipelines/autonomy-matrix/examples/data/hydro-lag-high.json \
  --out /tmp/autonomy-decision.json
~~~

4. **Expected outcome**  
   - The example must state the **expected action** (`slow`, `pause`, etc.) and key scores so CI or humans can check that the replay matches the documented behavior.

Where possible, examples should be tied into automated tests (e.g., fixture-based tests in `tests/`), but this README focuses on the **documentation and conceptual replay** side.

---

## 📦 Data & Metadata

Although these examples live in `docs/`, they reference and describe artifacts that live in:

- `docs/pipelines/autonomy-matrix/pipeline-profiles/*.yaml` — source of autonomy contract truth.  
- `data/telemetry/autonomy/` (or equivalent) — actual runtime decision streams.  
- `schemas/telemetry/*.json` — schemas for telemetry records.

For each example:

- If you include a **JSON snippet**, ensure it is:
  - Valid JSON,
  - Conforms to the autonomy telemetry schema (at least structurally),
  - Clearly marked as **synthetic** or **redacted**.

- If the example refers to STAC/DCAT/PROV entities:
  - Use lifelike but **fake IDs** (e.g., `kfm-example-*`),
  - Note clearly that they are **not production identifiers**.

---

## 🧠 Story Node & Focus Mode Integration

Examples are excellent candidates for **Story Nodes** and **Focus Mode overlays**, particularly in:

- Internal developer tooling (explaining why a pipeline was slowed or paused).  
- Training materials for Reliability, FAIR+CARE, and sustainability teams.

When writing examples:

- Keep **sections small and focused**, so they map to clean Story Nodes.  
- Use **clear, explicit nouns** instead of ambiguous pronouns (“this” or “it”).  
- Consider calling out potential Story Node anchors, e.g.:

~~~text
Related Story Node:
urn:kfm:story-node:pipelines:autonomy-matrix:example:hydro-hrrr-downscale:slow
~~~

Autonomy examples must **not** introduce new governance policy; they simply illustrate how **existing** policy behaves under specific conditions.

---

## 🧪 Validation & CI/CD

Even example docs and snippets are **CI-enforced**:

- **Markdown / schema checks**  
  - This README and any example Markdown files must pass:
    - `markdown-lint`
    - `schema-lint` (front-matter, where present)
    - `footer-check`
    - `accessibility-check`

- **Schema validation (YAML / JSON)**  
  - `sample-pipeline-profile.yaml` must validate against the pipeline profile schema.
  - Any JSON in examples, if used as test fixtures, must validate against telemetry schemas.

- **Provenance checks**  
  - Examples should reference:
    - The Autonomy Matrix spec document,
    - Relevant reliability or FAIR+CARE docs,
    - Any associated schemas or test harnesses.

Where appropriate, CI may run dedicated “example replay” tests that reconstruct a decision from example config and telemetry and compare it to the documented expected outcome.

---

## 🕰️ Version History

| Version    | Date       | Summary                                                                                       |
|-----------:|------------|-----------------------------------------------------------------------------------------------|
| **v11.2.4**| 2025-12-05 | Initial creation of `docs/pipelines/autonomy-matrix/examples/README.md`. Defines example types, layout, and replay rules. |

---

<div align="center">

📚 **KFM v11 — Autonomy Matrix Examples & Replay Guide**  
Deterministic Examples · Explainable Autonomy · FAIR+CARE-Governed  

[🤖 Autonomy Matrix Spec](../README.md) · [📘 Pipelines Index](../../README.md) · [⚖ Governance](../../../governance/ROOT-GOVERNANCE.md)

</div>

