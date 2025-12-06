---
title: "🧱 KFM v11 — Autonomy Matrix Scenario Fixtures"
description: "Canonical JSONL fixture library for Autonomy Matrix scenarios, used by the Offline Simulator, CI, and governance audits."
path: "docs/pipelines/autonomy-matrix/examples/scenarios/fixtures/README.md"
version: "v11.2.4"
last_updated: "2025-12-06"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability · Sustainability · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "Aligned with Autonomy Matrix v11.2.x (design-only; non-normative)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.4/autonomy-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/autonomy-matrix-v1.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
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

intent: "autonomy-matrix-scenario-fixtures"
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
    - "control-plane-simulation"

semantic_intent:
  - "governance"
  - "control-plane"
  - "reliability"
  - "sustainability"
  - "examples"
  - "simulation"
  - "fixtures"

category: "Pipelines · Autonomy · Examples · Scenario Fixtures"

sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Internal"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: false

data_steward: "Reliability · Sustainability · FAIR+CARE Council"
ttl_policy: "Indefinite (subject to architecture changes)"
sunset_policy: "Supersede when Autonomy Matrix v12 scenario fixture framework is adopted"

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
  - "docs/pipelines/autonomy-matrix/examples/scenarios/README.md@v11.2.4"
  - "docs/pipelines/autonomy-matrix/examples/README.md@v11.2.4"
  - "docs/pipelines/autonomy-matrix/decider/contracts.md@v11.2.4"
  - "docs/pipelines/autonomy-matrix/decider/score-functions.md@v11.2.4"
  - "docs/pipelines/autonomy-matrix/decider/action-logic.md@v11.2.4"
  - "docs/pipelines/autonomy-matrix/decider/designs/state-machine.md@v11.2.4"
  - "docs/pipelines/autonomy-matrix/README.md@v11.2.3"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/docs-pipelines-autonomy-matrix-scenario-fixtures-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/docs-pipelines-autonomy-matrix-scenario-fixtures-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "mutable"

doc_uuid: "urn:kfm:doc:pipelines:autonomy-matrix:examples:scenarios:fixtures:readme:v11.2.4"
semantic_document_id: "kfm-pipelines-autonomy-matrix-examples-scenarios-fixtures-v11.2.4"
event_source_id: "ledger:kfm:doc:pipelines:autonomy-matrix:examples:scenarios:fixtures:v11.2.4"

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

# 🧱 **KFM v11 — Autonomy Matrix Scenario Fixtures**  
`docs/pipelines/autonomy-matrix/examples/scenarios/fixtures/README.md`

**Purpose:**  
Define the **canonical fixture library** for Autonomy Matrix scenarios: JSONL files that  
encode **replayable telemetry segments** used by the Offline Simulator, CI, dashboards,  
and Focus Mode to validate autonomy behavior against documented scenarios.

</div>

---

## 📘 Overview

Scenario fixtures are:

- **JSONL time‑series files** that mirror the contracts in:
  - `decider/contracts.md` (snapshot + gates + actions), and
  - `decider/score-functions.md` / `decider/action-logic.md`.  
- **Non-secret, synthetic** telemetry slices that correspond to:
  - P0 storm nowcast scenarios (`p0-storm-nowcast:*`),  
  - P1 hydro forecast scenarios (`p1-hydro-forecast:*`),  
  - Future scenario families.

Primary uses:

- **Offline Simulator**  
  Replay decisions for design, tuning, and operator training.

- **CI / Regression Tests**  
  Ensure changes to score functions, gates, or state machine do **not** break canonical behavior.

- **Governance & Focus Mode**  
  Provide concrete, inspectable evidence for “what should happen” in documented scenarios.

Fixtures are **not** raw production telemetry; they are curated, scenario‑focused slices.

---

## 🗂️ Directory Layout

~~~text
docs/pipelines/autonomy-matrix/examples/scenarios/fixtures/
│
├── 📄 README.md                      # This file: fixture format & conventions
│
├── 📄 p0-storm-nowcast.jsonl         # Synthetic P0 storm nowcast fixtures
├── 📄 p1-hydro-forecast.jsonl        # Synthetic P1 hydro forecast fixtures
└── 📄 <future-family>.jsonl          # Placeholder for other scenario families (P2+, AI, etc.)
~~~

Author rules:

- All fixtures in this directory **MUST** be:
  - JSON Lines (`*.jsonl`), UTF‑8, LF‑terminated.
  - **Synthetic or sufficiently anonymized** — no direct production streams.
- Each JSONL file may contain **multiple labeled slices**, referenced via `fixture_ref` fields in scenario docs.
- File names must match their **scenario family**, e.g.:
  - `p0-storm-nowcast.jsonl` for `p0-storm-nowcast:*` scenarios.
  - `p1-hydro-forecast.jsonl` for `p1-hydro-forecast:*` scenarios.

---

## 📦 Data & Metadata

### 1. Record Shape

Each fixture record represents a **single evaluation tick** or **time bucket**.  
A minimal shape (conceptual) looks like:

~~~json
{
  "fixture_family": "p0-storm-nowcast",
  "fixture_slice_id": "baseline",
  "t": "2025-04-10T01:02:00Z",
  "pipeline_id": "p0-storm-nowcast",
  "metrics": {
    "lag_min": 7,
    "backlog_slices": 4,
    "cost_usd_hour": 9.5,
    "kwh_hour": 4.0,
    "carbon_kgco2e_hour": 1.2,
    "cost_budget_utilization": 0.42,
    "energy_budget_utilization": 0.38,
    "carbon_budget_utilization": 0.36,
    "data_trust_index": 0.97
  },
  "governance": {
    "care_label": "Synthetic-Storm-Nowcast",
    "sovereignty_policy": "synthetic-h3-generalization-v1",
    "care_trigger": null
  },
  "expected": {
    "scenario_id": "p0-storm-nowcast:baseline",
    "state": "STABLE",
    "action": "resume"
  }
}
~~~

Concrete schemas are defined in:

- `telemetry_schema` (`autonomy-matrix-v1.json`)  
- `json_schema_ref` for scenario fixtures (this doc’s front‑matter).

### 2. Fixture Identification

Scenario docs reference fixtures via `fixture_ref`, e.g.:

~~~yaml
fixture_ref: "../../fixtures/p0-storm-nowcast.jsonl#baseline"
~~~

Convention:

- Path portion → JSONL file in this directory.  
- Anchor (`#baseline`) → `fixture_slice_id` (or equivalent) in each record.

Each JSONL file:

- May contain multiple slices:
  - `baseline`, `carbon-clamp`, `care-escalation`, `thrash-control`, etc.  
- Should ensure that **each slice** has at least:
  - Stable `fixture_slice_id`.  
  - Stable `scenario_id` in the `expected` block (for scenario‑bound fixtures).

### 3. Families in v11.2.4

Currently modeled families:

- `p0-storm-nowcast.jsonl`  
  - Slices:
    - `baseline`
    - `carbon-clamp`
    - `care-escalation`
    - `thrash-control`

- `p1-hydro-forecast.jsonl`  
  - Slices:
    - `backlog-pressure`
    - `thrash-control` (hydro variant)

Additional families can be added as new scenario directories appear.

---

## 🧪 Validation & CI/CD

Fixtures are **first‑class citizens** in CI:

1. **Schema Validation**

   - All JSONL records must validate against:
     - `telemetry_schema` (`autonomy-matrix-v1.json`),
     - plus any **family‑specific constraints** (e.g., required metrics for hydro).

2. **Fixture–Scenario Consistency**

   - For each documented scenario with a `fixture_ref`:
     - The referenced JSONL file must exist.
     - There must be at least one record with matching `fixture_slice_id`.
     - The `expected.scenario_id` should match the scenario’s `scenario_id`.

3. **Replay Tests**

   - CI jobs may:
     - Load selected fixture slices.  
     - Run the Autonomy Decider with the appropriate pipeline profile and gates.  
     - Compare actual `action` / `state` / reason codes to `expected` values and scenario docs.

4. **Drift Detection**

   - When score functions, gates, or state machine change:
     - Replay against fixtures to detect **behavioral drift**.
     - Flag differences for review as:
       - Intended policy changes (requires docs/scenarios update), or  
       - Regressions (requires code fixes).

5. **Data Quality Checks**

   - Simple linting (e.g., monotonic timestamps within a slice, missing fields) is encouraged.
   - Telemetry seeds for simulation must be reproducible and documented (see MCP experiment logs).

---

## 🧠 Story Node & Focus Mode Integration

Fixtures themselves are **not** Story Nodes, but they support them:

- Story Nodes live at the **scenario level** (e.g., baseline, carbon‑clamp, backlog‑pressure).  
- Each Story Node points to:
  - Its scenario Markdown,  
  - The corresponding fixture slice.

Example conceptual linkage:

~~~text
Story Node:
  urn:kfm:story-node:pipelines:autonomy-matrix:examples:scenarios:p0-storm-nowcast:baseline

Scenario:
  docs/pipelines/autonomy-matrix/examples/scenarios/p0-storm-nowcast/scenario-baseline.md

Fixture:
  docs/pipelines/autonomy-matrix/examples/scenarios/fixtures/p0-storm-nowcast.jsonl#baseline
~~~

Focus Mode can:

- Use fixtures behind the scenes to:
  - Re-simulate autonomy decisions when explaining behavior.  
  - Show how real‑time signals compare to **canonical fixture traces**.  
- But must **never** treat fixtures as production truth — they are **didactic examples**, not live telemetry.

---

## 🕰️ Version History

| Version    | Date       | Summary                                                                                                                  |
|-----------:|------------|--------------------------------------------------------------------------------------------------------------------------|
| **v11.2.4**| 2025-12-06 | Initial Autonomy Matrix fixtures README: layout, record shape, fixture_ref conventions, CI integration, Story Node role. |

---

<div align="center">

🧱 **KFM v11 — Autonomy Matrix Scenario Fixtures**  
Replayable Telemetry · Deterministic Tests · FAIR+CARE‑Aligned Simulation  

[🎭 Scenario Library Root](../README.md) · [🤖 Autonomy Matrix](../../../README.md) · [🧠 Decider](../../../decider/README.md)

</div>

