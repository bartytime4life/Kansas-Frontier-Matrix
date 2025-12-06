---
title: "📄 Kansas Frontier Matrix — Documentation Templates Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/templates/README.md"

version: "v11.2.4"
last_updated: "2025-12-06"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly / Autonomous"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
signature_ref: "releases/v11.2.4/signature.sig"
attestation_ref: "releases/v11.2.4/slsa-attestation.json"
sbom_ref: "releases/v11.2.4/sbom.spdx.json"
manifest_ref: "releases/v11.2.4/manifest.zip"
telemetry_ref: "releases/v11.2.4/docs-templates-telemetry.json"
telemetry_schema: "schemas/telemetry/docs-templates-v11.2.4.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-v2.json"

governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

status: "Active / Enforced"
doc_kind: "Standard Index"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"

scope:
  domain: "documentation-templates"
  applies_to:
    - "docs/templates/**"
    - "mcp/experiments/**"
    - "mcp/model_cards/**"
    - "mcp/sops/**"

fair_category: "F1-A1-I2-R2"
care_label: "FAIR+CARE Governance Aligned"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by Documentation Templates Index v12"

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
  - "docs/templates/README.md@v10.2.2"
  - "docs/templates/README.md@v10.0.0"
  - "docs/templates/README.md@v9.7.0"
  - "docs/templates/README.md@v9.5.0"
  - "docs/templates/README.md@v9.0.0"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/kfm-markdown-protocol-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/kfm-markdown-protocol-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:templates:index:v11.2.4"
semantic_document_id: "kfm-docs-templates-index-v11.2.4"
event_source_id: "ledger:kfm:doc:templates:index:v11.2.4"
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
  workflow: ".github/workflows/docs-lint.yml"
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

# 📄 **Kansas Frontier Matrix — Documentation Templates Index**  
`docs/templates/README.md`

**Purpose**  
Centralized index for all **reusable documentation templates** that drive the Kansas Frontier Matrix (KFM) ecosystem.  
Each template is aligned with **MCP‑DL v6.3**, **KFM‑MDP v11.2.4**, and **FAIR+CARE** so that every experiment, model, SOP, and governance report is reproducible, ethically grounded, and machine-parseable.

<img src="https://img.shields.io/badge/Docs-MCP_v6.3-blue" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.4-purple" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-green" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Certified-orange" />
<img src="https://img.shields.io/badge/Status-Stable-success" />

</div>

---

## 📘 Overview

This index describes the **standard template set** used throughout KFM:

- **Experiment Template** — for research, ETL, AI/ML, and historical/archaeological analyses.  
- **Model Card Template** — for AI/ML models, including bias, explainability, and governance metadata.  
- **SOP Template** — for standard operating procedures across pipelines, governance, and operations.

All templates are:

- **Markdown‑based**, KFM‑MDP v11.2.4 compliant.  
- Designed for **machine extraction** into DCAT/STAC catalogs and the KFM knowledge graph.  
- Verified by CI workflows (`docs-lint.yml`, `faircare-validate.yml`, `telemetry-export.yml`) and documented in telemetry.

### Template Catalog

#### Experiment Template — `docs/templates/experiment.md`

**Purpose**  
Standardize documentation of experiments for AI models, ETL pipelines, and analytical studies.

**Canonical Sections (H2/H3 inside template):**

- Metadata (YAML front-matter)  
- Objective & Hypothesis  
- Methodology (data, tools, configs)  
- Results & Discussion  
- Reproducibility (commands, configs, seeds)  
- Validation & Governance (links to FAIR+CARE / audits)

Used in (examples):

- `mcp/experiments/**`  
- `src/pipelines/**/experiments/`  
- `data/analyses/**`

---

#### Model Card Template — `docs/templates/model_card.md`

**Purpose**  
Document the lifecycle of AI/ML models for transparency, explainability, and FAIR+CARE governance.

**Canonical Sections:**

- Metadata (name, version, datasets, license, SBOM/SLSA refs)  
- Intended Use & Limitations  
- Architecture & Training Configuration  
- Datasets & Splits  
- Evaluation Metrics (performance + fairness)  
- Bias, Risk & Mitigation  
- Governance & Abandonment Registry References

Used in:

- `mcp/model_cards/**`  
- Outputs of `ai-train.yml` / `ai-explainability.yml`  
- Governance reviews for production models.

---

#### SOP Template — `docs/templates/sop.md`

**Purpose**  
Provide a structured, step‑wise format for repeatable operational workflows.

**Canonical Sections:**

- Purpose & Scope  
- Preconditions & Inputs  
- Procedure (step list)  
- Validation & Rollback  
- Governance & Compliance

Applied to:

- Data ingestion and normalization SOPs.  
- CI/CD and infrastructure runbooks.  
- Governance and review procedures.

---

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 📁 templates/
    📄 README.md               — ← This index (templates catalog)
    📄 experiment.md           — Experiment / analysis documentation template
    📄 model_card.md           — AI/ML model card template
    📄 sop.md                  — Standard Operating Procedure template

📁 mcp/
├── 📁 experiments/            — Concrete experiment docs derived from experiment.md
├── 📁 model_cards/            — Concrete model cards derived from model_card.md
└── 📁 sops/                   — SOPs derived from sop.md

📁 reports/
└── 📁 audit/
    📄 github-workflows-ledger.json  — CI/CD evidence including template usage events

📁 releases/
└── 📁 v11.2.4/
    📄 docs-templates-telemetry.json — Telemetry for template usage & validation
    📄 sbom.spdx.json                — SBOM (docs tooling)
    📄 manifest.zip                  — Manifest (hashes, versions, refs)
~~~

---

## 🧭 Context

Templates live in the documentation layer but are tightly coupled to the full KFM pipeline:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j knowledge graph → API layer → React/MapLibre/Cesium frontend → Story Nodes → Focus Mode

- **Experiments** describe how ETL, AI, and analyses are conducted, enabling **reproducible science**.  
- **Model Cards** document AI components that appear downstream in Focus Mode and Story Nodes.  
- **SOPs** describe governed procedures for operations, governance, and data stewardship.

By enforcing consistent template usage:

- CI/CD can **lint and validate** docs automatically.  
- Catalogs and the **knowledge graph** can ingest documentation as structured entities.  
- Focus Mode can safely overlay narrative context on data, models, and workflows.

---

## 🧠 Story Node & Focus Mode Integration

Templates are written so that their instances can be easily transformed into Story Nodes:

- Experiment docs → `urn:kfm:story-node:experiments:<exp_id>`  
- Model cards → `urn:kfm:story-node:ai-model:<model_id>`  
- SOPs → `urn:kfm:story-node:sop:<process_id>`

Each template:

- Encourages **clear, localized sections** (Objective, Method, Results, Governance) that Focus Mode can surface as answer snippets.  
- Includes **stable identifiers** (e.g., experiment IDs, model IDs) that can be mapped to graph nodes and Story Node targets.  
- Provides **governance links** (FAIR+CARE, SOPs, audits) that Focus Mode can reference but not override.

Focus Mode is allowed to:

- Summarize template‑based docs.  
- Highlight sections relevant to user queries (e.g., “training data” or “limitations”).  

Focus Mode is not allowed to:

- Modify template content or create new policy text.  
- Claim governance or certification status not present in the underlying document.

---

## 🧪 Validation & CI/CD

Templates integrate with KFM CI/CD to ensure every derived document is compliant.

### 1. Primary Validation Workflows

| Workflow                 | Role                                                 | Key Output                                                  |
|--------------------------|------------------------------------------------------|-------------------------------------------------------------|
| `docs-lint.yml`          | Markdown structure, headings, front‑matter, links   | `reports/self-validation/docs/lint_summary.json`            |
| `faircare-validate.yml`  | FAIR+CARE & ethics checks on docs + data            | `reports/faircare/faircare_summary.json`                    |
| `telemetry-export.yml`   | Aggregates template usage & doc metrics into ledger | `releases/v11.2.4/focus-telemetry.json`                     |

Author guidance:

- Any new document created from a template must **keep its YAML scaffold** and fill in required fields.  
- CI will block merges if:
  - YAML front‑matter is incomplete or malformed.  
  - Required sections or governance references are missing.  

---

## 📦 Data & Metadata

Templates themselves are treated as **reference entities**:

- Each template has:
  - A defined **file path** (`docs/templates/*.md`).  
  - A corresponding entry in this index.  
  - Governance metadata in this document’s front‑matter.

Derived documents:

- Should set their own `doc_uuid`, `semantic_document_id`, and `event_source_id`.  
- Inherit governance references (`governance_ref`, `ethics_ref`, `sovereignty_policy`).  
- Must include a **Version History** section and standard footer.

Telemetry for template usage (e.g., number of experiment docs created, model cards updated) is stored in:

- `releases/v11.2.4/docs-templates-telemetry.json`  
- Aggregated and summarized via `telemetry-export.yml`.

---

## 🌐 STAC, DCAT & PROV Alignment

While templates themselves are non‑spatial documentation, they align with KFM’s metadata ecosystem:

- **DCAT**  
  - This index can be modeled as a `dcat:CatalogRecord` with associated `dcat:Dataset` for the template collection.  
  - Individual templates are datasets or distributions of documentation patterns.

- **STAC**  
  - In systems where docs appear alongside spatial datasets, templates may be represented as Items in a `kfm-docs-templates` Collection with `geometry: null` and `datetime = last_updated`.

- **PROV-O**  
  - Template‑based docs are `prov:Entity` instances derived from these template “plans”.  
  - This index acts as a `prov:Plan` for documentation patterns; actual docs use `prov:wasDerivedFrom` to link back.

---

## 🧱 Architecture

In the monorepo architecture:

- `docs/templates/**` defines **documentation contracts**.  
- `mcp/experiments/**`, `mcp/model_cards/**`, `mcp/sops/**` implement those contracts for concrete cases.  
- CI workflows (`docs-lint`, `faircare-validate`, `telemetry-export`) enforce contracts and generate telemetry.  
- The KFM knowledge graph ingests:
  - Template instances as **design/procedure nodes** (CIDOC E29).  
  - Relations between experiments, models, SOPs, datasets, and workflows.

This index is the **single source of truth** for which templates are canonical and where they live.

---

## ⚖ FAIR+CARE & Governance

Templates embed FAIR+CARE expectations into every downstream doc:

- **FAIR**  
  - Metadata front‑matter for **Findability** and **Accessibility**.  
  - JSON‑friendly structures and consistent fields for **Interoperability**.  
  - Version history and provenance for **Reusability**.

- **CARE**  
  - Sections for **Ethics, Bias, and Limitations** in model cards.  
  - Governance references and responsibility notes in experiments and SOPs.  
  - Clear pathways for redaction, anonymization, or generalized reporting where sensitive data is involved.

Governance hooks:

- Use of templates is tracked via telemetry.  
- Councils (FAIR+CARE, Governance, Security) can audit:
  - Which documents use which templates.  
  - Whether docs stay within template constraints (no removal of required sections).  

---

## 🕰️ Version History

| Version   | Date       | Author           | Summary                                                                                                                   |
|----------:|------------|------------------|---------------------------------------------------------------------------------------------------------------------------|
| **v11.2.4** | 2025-12-06 | `@kfm-docs`      | Aligned with KFM‑MDP v11.2.4; expanded front‑matter; converted sections to approved H2 registry; added Story Node & telemetry integration and STAC/DCAT/PROV alignment. |
| v10.2.2  | 2025-11-12 | `@kfm-docs`      | Aligned telemetry refs to v10.2.0; clarified integration with docs-lint and FAIR+CARE workflows.                         |
| v10.0.0  | 2025-11-10 | `@kfm-docs`      | Introduced telemetry schema v2; updated governance workflows and MCP/FAIR+CARE sections.                                 |
| v9.7.0   | 2025-11-05 | `@kfm-docs`      | Unified experiment, model, and SOP templates under a stable release.                                                     |
| v9.5.0   | 2025-10-20 | `@kfm-council`   | Added FAIR+CARE audit metadata and governance integration.                                                               |
| v9.0.0   | 2025-06-01 | `@kfm-core`      | Established baseline templates with MCP compliance.                                                                      |

---

<div align="center">

📄 **Kansas Frontier Matrix — Documentation Templates Index (v11.2.4)**  
Documentation Integrity · FAIR+CARE Governance · Platinum‑Grade Reproducibility  

[⬅ Back to Documentation Index](../README.md) ·  
[📘 Markdown Protocol (KFM‑MDP v11.2.4)](../standards/kfm_markdown_protocol_v11.2.4.md) ·  
[⚖ Governance Charter](../standards/governance/ROOT-GOVERNANCE.md)

</div>
