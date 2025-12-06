---
title: "📦 KFM v11 — Autonomy Decider Experiment Fixtures"
description: "Synthetic telemetry and config fixture guidance for Autonomy Decider experiments within the KFM v11 Autonomy Matrix control plane."
path: "docs/pipelines/autonomy-matrix/decider/designs/variants/experiments/fixtures/README.md"
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

sbom_ref: "../../../../../../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.4/autonomy-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/autonomy-matrix-v1.json"
energy_schema: "../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../../governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../sovereignty/INDIGENOUS-DATA-PROTECTION.md"
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

intent: "autonomy-matrix-decider-variants-experiments-fixtures"
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

json_schema_ref: "schemas/json/docs-pipelines-autonomy-decider-variants-experiments-fixtures-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/docs-pipelines-autonomy-decider-variants-experiments-fixtures-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "mutable"

doc_uuid: "urn:kfm:doc:pipelines:autonomy-matrix:decider:designs:variants:experiments:fixtures:v11.2.4"
semantic_document_id: "kfm-pipelines-autonomy-matrix-decider-variants-experiments-fixtures-v11.2.4"
event_source_id: "ledger:kfm:doc:pipelines:autonomy-matrix:decider:designs:variants:experiments:fixtures:v11.2.4"

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

# 📦 **KFM v11 — Autonomy Decider Experiment Fixtures**  
`docs/pipelines/autonomy-matrix/decider/designs/variants/experiments/fixtures/README.md`

**Purpose:**  
Describe how to create, organize, and use **synthetic telemetry and config fixtures** for Autonomy Decider experiments.  
Fixtures here support **deterministic, reproducible simulations** of autonomy behavior without exposing production data.

</div>

---

## 📘 Overview

This document explains the **fixtures** used for Autonomy Decider experiments:

- What fixture files represent (telemetry snapshots, config deltas).  
- How they are structured and named.  
- How CI and offline simulators use them to:
  - Compare canonical vs. experimental autonomy behavior,  
  - Validate fairness, SLO, and sustainability impacts,  
  - Preserve FAIR+CARE and sovereignty constraints.

Key constraints:

- All fixture data is **synthetic** or **strongly anonymized**.  
- No production secrets, PII, or sensitive locations appear here.  
- Fixtures are **stable test inputs** and part of the Autonomy experiment provenance chain.

---

## 🗂️ Directory Layout

~~~text
docs/pipelines/autonomy-matrix/decider/designs/variants/experiments/fixtures/
│
├── 📄 README.md                          # This file (fixture guidance & conventions)
│
├── 📄 fairness-small-sample.json         # Synthetic telemetry for fairness experiments
├── 📄 horizon-daily-vs-hourly.json       # Synthetic telemetry for horizon tuning
├── 📄 thresholds-sample.json             # Synthetic telemetry for cost/energy/carbon thresholds
│
└── 📂 samples/                           # Optional extra example payloads
    ├── 📄 multi-tenant-mix.json          # Mixed-tenant synthetic snapshot
    ├── 📄 carbon-tight-budget.json       # Sample near carbon budget limit
    └── 📄 high-lag-low-cost.json         # Sample with high lag but low cost/energy
~~~

**Author rules:**

- Each fixture file **must** have a short inline comment in this tree describing its purpose.  
- Only **JSON** fixtures live here; YAML configs for decider variants live under `config/autonomy/decider/` (outside `docs/`).  
- If new experiment families are added (e.g., explainability or cluster-level throttling), add corresponding fixture files and update this README.

---

## 📦 Data & Metadata

Fixtures here model **input snapshots** for the decider, not full pipeline histories.

### 1. Fixture Content Expectations

Each JSON fixture should contain:

- **Pipeline context**
  - IDs (synthetic or anonymized),
  - Priority bands, tenant information (if relevant),
  - References to synthetic STAC/DCAT/PROV identifiers (e.g., `kfm-example-*`).

- **Telemetry metrics**
  - Freshness: lag, backlog, run failure counts.  
  - Cost: estimated or synthetic cost per hour, monthly spend.  
  - Energy: kWh per hour, month-to-date kWh.  
  - Carbon: kgCO₂e per hour, month-to-date usage.  
  - Validation/trust: QA status flags, lineage completeness flags.

- **Governance context**
  - CARE labels,
  - Sovereignty policy identifiers,
  - Sensitivity level (e.g., “Synthetic-Waters”, “Synthetic-Climate”).

Example (simplified):

~~~json
{
  "timestamp": "2025-12-05T10:23:42Z",
  "pipeline": "example/hydro-hrrr",
  "tenant": "example-tenant-a",
  "priority_band": "P1",
  "telemetry": {
    "freshness": {
      "lag_minutes": 18,
      "max_lag_minutes": 120,
      "backlog_runs": 2
    },
    "cost": {
      "usd_per_hour": 5.5,
      "mtd_spend_usd": 430.0,
      "monthly_cap_usd": 1200.0
    },
    "energy": {
      "kwh_per_hour": 3.1,
      "mtd_kwh": 210.0,
      "energy_cap_kwh": 400.0
    },
    "carbon": {
      "kgco2e_per_hour": 1.1,
      "mtd_kgco2e": 80.0,
      "carbon_cap_kgco2e": 150.0
    },
    "trust": {
      "qa_pass_rate": 0.99,
      "lineage_complete": true
    }
  },
  "governance": {
    "care_label": "Synthetic-Waters",
    "sovereignty_policy": "synthetic-h3-generalization-v1",
    "sensitivity": "General"
  }
}
~~~

### 2. Synthetic & Anonymized Only

- **Never** include:
  - Real customer names, real emails, internal hostnames.  
  - Exact costs or usage numbers from production.  
  - Precise coordinates of sensitive or Indigenous sites.

- Use realistic ranges and relationships but clearly synthetic identifiers:
  - `example-tenant-a`, `kfm-example-*`, `synthetic-*`.

---

## 🧪 Validation & CI/CD

Fixtures participate directly in CI flows for Autonomy experiments:

- **Schema validation**
  - All JSON fixtures must validate against:
    - `autonomy-matrix-v1` telemetry schema, and
    - Any variant-specific extensions (if present).

- **Replay tests**
  - CI jobs may:
    - Run the canonical decider and experimental variants against the same fixture,  
    - Compare decisions, scores, and gate outcomes,  
    - Produce regression summaries stored outside `docs/`.

- **Change control**
  - Changes to fixtures can affect test expectations:
    - Keep deltas minimal and well-described in PRs.  
    - When fixtures change, update experiment docs and any associated tests to match.

Where possible, fixtures should be **append-only**; avoid destructive edits to existing fixtures that are already referenced by tests or experiment reports.

---

## 🧠 Story Node & Focus Mode Integration

While fixtures themselves are raw JSON, the **stories around them** (in experiment docs) are useful for:

- Teaching how autonomy reacts to different telemetry patterns.  
- Demonstrating fairness, sustainability, or CARE tradeoffs.

This README should help Focus Mode answer questions like:

- “What does `fairness-small-sample.json` represent?”  
- “Which fixtures relate to carbon budget experiments?”  

When documenting fixtures in experiment docs:

- Link to them with descriptive text (not just filenames).  
- Summarize what scenario they encode (e.g., “P1 weather pipeline near carbon cap”).  
- Avoid treating fixtures as policy; they are **examples**, not normative constraints.

---

## 🕰️ Version History

| Version    | Date       | Summary                                                                                          |
|-----------:|------------|--------------------------------------------------------------------------------------------------|
| **v11.2.4**| 2025-12-05 | Initial creation of fixtures README. Defined layout, synthetic data rules, and CI integration.   |

---

<div align="center">

📦 **KFM v11 — Autonomy Decider Experiment Fixtures**  
Synthetic Telemetry · Reproducible Simulations · FAIR+CARE-Governed Test Data  

[🧪 Experiment Registry](../README.md) · [🧠 Decider Variants](../../README.md) · [🤖 Autonomy Matrix Spec](../../../../README.md)

</div>

