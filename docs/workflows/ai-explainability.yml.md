---
title: "🤖 Kansas Frontier Matrix — AI Explainability & Bias Audit Workflow (`ai-explainability.yml`)"
path: "docs/workflows/ai-explainability.yml.md"

version: "v11.2.6"
last_updated: "2025-12-11"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council & AI Governance WG"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
signature_ref: "releases/v11.2.6/signature.sig"
attestation_ref: "releases/v11.2.6/slsa-attestation.json"
sbom_ref: "releases/v11.2.6/sbom.spdx.json"
manifest_ref: "releases/v11.2.6/manifest.zip"
telemetry_ref: "releases/v11.2.6/ai-explainability-telemetry.json"
telemetry_schema: "schemas/telemetry/ai-explainability-workflow-v11.2.6.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-v2.json"

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

status: "Active / Enforced"
doc_kind: "Standard"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"

scope:
  domain: "ci-cd-workflows"
  applies_to:
    - "github-actions"
    - "ai-governance"
    - "model-explainability"

fair_category: "F1-A1-I2-R2"
care_label: "FAIR+CARE Governance Aligned"
sensitivity: "Model telemetry; low-risk when aggregated"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by AI Explainability Workflow v12"

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
  - "docs/workflows/ai-explainability.yml.md@v11.2.4"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: false
  must_reference_origin_root: true

doc_uuid: "urn:kfm:doc:workflows:ai-explainability-yml:v11.2.6"
semantic_document_id: "kfm-workflow-ai-explainability-yml-v11.2.6"
event_source_id: "ledger:kfm:doc:workflows:ai-explainability-yml:v11.2.6"
doc_integrity_checksum: "<sha256>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "3d-context-render"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
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
    - "3d-context-render"
    - "a11y-adaptations"
    - "diagram-extraction"
    - "metadata-extraction"
  prohibited:
    - "content-alteration"
    - "speculative-additions"
    - "unverified-architectural-claims"
    - "narrative-fabrication"
    - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧭 Context"
    - "🗺️ Diagrams"
    - "🧠 Story Node & Focus Mode Integration"
    - "🧪 Validation & CI/CD"
    - "📦 Data & Metadata"
    - "🌐 STAC, DCAT & PROV Alignment"
    - "🧱 Architecture"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "diagram-check"
  - "accessibility-check"
  - "provenance-check"
  - "footer-check"

ci_integration:
  workflow: ".github/workflows/ai-explainability.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence"
  architecture: "Designed for Longevity · Governed for Integrity"
  analysis: "Research-Driven · Evidence-Led · FAIR+CARE Grounded"
  data-spec: "Open Data × Responsible Stewardship"
  pipeline: "Deterministic Pipelines · Explainable AI · Open Provenance"
  telemetry: "Transparent Systems · Ethical Metrics · Sustainable Intelligence"
  graph: "Semantics × Provenance × Spatial Intelligence"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

deprecated_fields:
  - "old_markdown_standard_v10.4"
---

<div align="center">

# 🤖 **Kansas Frontier Matrix — AI Explainability & Bias Audit Workflow (`ai-explainability.yml`)**  
`docs/workflows/ai-explainability.yml.md`

**Purpose**  
Define the **governed CI/CD workflow** that runs AI explainability, fairness, and drift audits for KFM models.  
This workflow turns every model change into a **documented, reproducible, and PROV-traceable** explainability report,  
feeding the Neo4j knowledge graph, STAC/DCAT catalogs, and FAIR+CARE governance dashboards.

<img src="https://img.shields.io/badge/Docs-MCP--DL_v6.3-blue" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.4-purple" />
<img src="https://img.shields.io/badge/AI-Explainability_%26_Bias_Audit-orange" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Governance_Aligned-gold" />
<img src="https://img.shields.io/badge/CI%2FCD-GitHub_Actions-success" />

</div>

---

## 📘 Overview

### 1. Workflow Intent

The `ai-explainability.yml` GitHub Actions workflow:

- Runs **explainability and bias audits** whenever models or training configs change.  
- Produces **versioned, deterministic** artifacts (SHAP/feature attributions, fairness metrics, drift checks).  
- Emits **telemetry** (duration, energy, carbon, FAIR+CARE scores) into `ai-explainability-telemetry.json` and the unified KFM telemetry ledger.  
- Writes **lineage-ready metadata** so results can be ingested into:
  - Neo4j (`:ModelVersion`, `:ExplainabilityRun`, `:Dataset` nodes + typed relationships),  
  - STAC/DCAT catalogs (explainability reports as datasets/items),  
  - Governance dashboards and Story Nodes.

This document is the **canonical plan** for that workflow under KFM-MDP v11.2.4 and MCP-DL v6.3.

### 2. Triggers (High-Level)

The workflow is expected to trigger on:

- `push` / `pull_request` to:
  - `src/models/**`
  - `mcp/model_cards/**`
  - `configs/models/**`
- Manual dispatch (`workflow_dispatch`) for ad-hoc audits and backfills.

Exact trigger patterns live in `.github/workflows/ai-explainability.yml` and must stay in sync with this spec.

### 3. Responsibilities

This workflow is responsible for:

- **Reproducible audits**  
  - All runs are config-driven (`configs/models/<model>.yaml`) with fixed random seeds logged.
- **Governed outputs**  
  - Metrics mapped to FAIR+CARE governance matrix and model cards.
- **Provenance & cataloging**  
  - Every run emits PROV-compliant lineage and DCAT/STAC metadata fragments.
- **Sustainability**  
  - Energy and carbon metrics captured per run and fed into sustainability reports.

---

## 🗂️ Directory Layout

~~~text
📁 .github/
└── 📁 workflows/
    📄 ai-explainability.yml             — GitHub Actions workflow (explainability & bias audit)

📁 docs/
└── 📁 workflows/
    📄 README.md                         — CI/CD & Governance Workflows index
    📄 ai-explainability.yml.md          — ← This specification

📁 src/
└── 📁 models/
    📁 <model_family>/
        📄 train.py                      — Training entrypoint (consumed by CI/CD)
        📄 explainability.py             — Shared explainability routines (SHAP, LIME, etc.)

📁 configs/
└── 📁 models/
    📄 <model_name>.yaml                 — Model config (paths, seeds, explainability settings)

📁 tools/
└── 📁 ai/
    📄 run_explainability_audit.py       — CLI entrypoint used by the workflow
    📄 explainability_schema.json        — Local validation schema for audit outputs

📁 mcp/
└── 📁 experiments/
    📄 <timestamp>_AI-EXPL-<id>.md       — Human-readable experiment logs (linked from CI)

📁 data/
└── 📁 processed/
    📁 models/
        📁 <model_name>/
            📄 model_metadata.json       — Model version manifest
            📄 explainability_report.json
            📄 fairness_metrics.json
            📄 drift_report.json
~~~

---

## 🧭 Context

### 1. Relation to Other Workflows

- **Upstream:**  
  - `ai-train.yml` produces model artifacts and base metrics that this workflow audits.
- **Sibling workflows:**  
  - `ai-explainability.yml` complements `faircare-validate.yml` by focusing on **model-level** risk,  
    while FAIR+CARE validation focuses on **dataset and documentation** compliance.
- **Downstream:**  
  - Telemetry feeds into governance dashboards and Focus Mode Story Nodes for models.

### 2. MCP & Reproducibility

In line with MCP 2.0, all audits must be:

- **Config-driven** – no hard-coded magic values; configs stored in git and versioned with the run ID.  
- **Deterministic** – seeds pinned and logged; reruns with the same config over the same data must reproduce metrics.  
- **Documented** – each run links to an `mcp/experiments/*AI-EXPL-*.md` log, generated or updated by the workflow.

---

## 🗺️ Diagrams

### 1. High-Level Workflow (GitHub Actions)

```mermaid
flowchart LR
    A["Code / Config Change"] --> B["ai-explainability.yml Triggered"]
    B --> C["Checkout & Setup Python"]
    C --> D["Resolve Model + Dataset from Config"]
    D --> E["Run Explainability & Fairness Audit CLI"]
    E --> F["Validate Outputs (JSON Schema)"]
    F --> G["Upload Artifacts & Telemetry"]
    G --> H["Update Graph & Catalogs (via API)"]
    H --> I["Post Status & Links to PR"]
