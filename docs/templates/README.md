---
title: "📄 Kansas Frontier Matrix — Documentation Templates Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/templates/README.md"

version: "v11.2.6"
last_updated: "2025-12-11"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
signature_ref: "../../releases/v11.2.6/signature.sig"
attestation_ref: "../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../releases/v11.2.6/docs-templates-telemetry.json"
telemetry_schema: "../../schemas/telemetry/docs-templates-v11.2.6.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
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
  - "docs/templates/README.md@v11.2.4"
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

json_schema_ref: "../../schemas/json/kfm-markdown-protocol-v11.2.6.schema.json"
shape_schema_ref: "../../schemas/shacl/kfm-markdown-protocol-v11.2.6-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:templates:index:v11.2.6"
semantic_document_id: "kfm-docs-templates-index-v11.2.6"
event_source_id: "ledger:kfm:doc:templates:index:v11.2.6"
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
Each template is aligned with **MCP‑DL v6.3**, **KFM‑MDP v11.2.6**, and **FAIR+CARE**, so that every experiment, model, SOP, and governance report is reproducible, ethically grounded, and machine-parseable.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![KFM‑MDP v11.2.6](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.6-purple)]()  
[![License · CC‑BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Governance%20Aligned-orange)]()  
[![Status · Stable](https://img.shields.io/badge/Status-Stable%20%2F%20Enforced-brightgreen)]()

</div>

---

## 📘 Overview

This index describes the **standard template set** used throughout KFM:

- **Experiment Template** — for research, ETL, AI/ML, and historical/archaeological analyses.  
- **Model Card Template** — for AI/ML models, including bias, explainability, and governance metadata.  
- **SOP Template** — for standard operating procedures across pipelines, governance, and operations.  
- **Core Markdown Template** — for any new KFM document requiring KFM‑MDP v11.2.6 compliance.

All templates are:

- **Markdown‑based**, KFM‑MDP v11.2.6 compliant.  
- Designed for **machine extraction** into DCAT/STAC catalogs and the KFM knowledge graph.  
- Verified by CI workflows (`docs-lint.yml`, FAIR+CARE validation, telemetry export) and reported via docs-templates telemetry.

### Template Catalog

#### 1. Core Markdown Template — `docs/templates/kfm-markdown-template.md`

**Purpose**  
Provides the **canonical pattern** for any KFM Markdown file:

- YAML front‑matter ordering and required fields.  
- Approved emoji + label heading patterns.  
- Directory layout style and governance footer rules.

Use as the **starting point** for:

- Domain READMEs (`docs/data/**/README.md`).  
- Standards and governance docs (`docs/standards/**`).  
- API and architecture docs (`src/api/**/README.md`, `docs/architecture/**`).

---

#### 2. Experiment Template — `docs/templates/experiment.md`

**Purpose**  
Standardize documentation of experiments for AI models, ETL pipelines, and analyses.

**Canonical Sections (H2/H3 inside template):**

- Metadata (front‑matter)  
- Objective & Hypothesis  
- Methodology (data, tools, configs)  
- Results & Discussion  
- Reproducibility (commands, configs, seeds)  
- Validation & Governance (FAIR+CARE, SOP links)

Used in (examples):

- `mcp/experiments/**`  
- `src/pipelines/**/experiments/`  
- `data/analyses/**`

---

#### 3. Model Card Template — `docs/templates/model_card.md`

**Purpose**  
Document AI/ML models for transparency, explainability, and FAIR+CARE governance.

**Canonical Sections:**

- Metadata (name, version, datasets, license, SBOM/SLSA refs)  
- Intended Use & Limitations  
- Architecture & Training Configuration  
- Datasets & Splits  
- Evaluation Metrics (performance + fairness)  
- Bias, Risk & Mitigation  
- Governance & Abandonment / Retirement plans

Used in:

- `mcp/model_cards/**`  
- Outputs of training/explainability workflows.  
- Governance reviews for production models.

---

#### 4. SOP Template — `docs/templates/sop.md`

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
  📁 templates/
    📄 README.md                # ← This index (templates catalog)
    📄 kfm-markdown-template.md # Core KFM-MDP v11.2.6 markdown template
    📄 experiment.md            # Experiment / analysis documentation template
    📄 model_card.md            # AI/ML model card template
    📄 sop.md                   # Standard Operating Procedure template

📁 mcp/
  📁 experiments/               # Concrete experiment docs derived from experiment.md
  📁 model_cards/               # Concrete model cards derived from model_card.md
  📁 sops/                      # SOPs derived from sop.md

📁 reports/
  📁 audit/
    📄 github-workflows-ledger.json  # CI/CD evidence including template usage events

📁 releases/
  📁 v11.2.6/
    📄 docs-templates-telemetry.json # Telemetry for template usage & validation
    📄 sbom.spdx.json                # SBOM for docs tooling & dependencies
    📄 manifest.zip                  # Manifest (hashes, versions, references)
~~~

Any new template added under `docs/templates/` MUST be registered here and in the Template Catalog above.

---

## 🧭 Context

Templates live in the documentation layer but are tightly coupled to the full KFM pipeline:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j knowledge graph → API layer → React/MapLibre/Cesium frontend → Story Nodes → Focus Mode

- **Experiments** describe how ETL, AI, and analyses are conducted → reproducible science.  
- **Model Cards** document AI components that surface in APIs, Focus Mode, and Story Nodes.  
- **SOPs** describe governed procedures for operations, governance, and stewardship.  
- **Core Markdown Template** ensures every doc these workflows depend on is structurally consistent and catalog‑ready.

By enforcing consistent template usage:

- CI/CD can **lint and validate** docs automatically.  
- STAC/DCAT/PROV catalogs and the **knowledge graph** can ingest documentation as structured entities.  
- Focus Mode can safely overlay narrative context on data, models, and workflows without rewriting policy.

---

## 🗺️ Diagrams

High-level flow for template usage and enforcement:

~~~mermaid
flowchart LR
  TPL[docs/templates/*.md<br/>Templates] --> DOCS[Concrete Docs<br/>experiments / model_cards / sops]
  DOCS --> CI[CI Workflows<br/>docs-lint · faircare-validate · telemetry-export]
  CI --> CAT[STAC/DCAT/PROV & Graph<br/>Doc Catalogs]
  CAT --> FM[Story Nodes & Focus Mode]
~~~

Timelines or more detailed diagrams SHOULD be stored in separate diagram-specific docs or sections that reference this index.

---

## 🧠 Story Node & Focus Mode Integration

Template-based documents are designed to be **Story Node–friendly**:

- Experiment docs → potential `story_node` instances for ETL/AI/analysis narratives.  
- Model cards → `story_node` entries for AI models (capabilities, risks, provenance).  
- SOPs → process-focused Story Nodes describing how KFM operates and governs itself.

Story Node / Focus Mode behaviors:

- MAY:
  - Summarize template-based docs.  
  - Extract sections like “Objective”, “Method”, “Limitations”.  
  - Link to telemetry and provenance for context.

- MUST NOT:
  - Alter normative content of templates or derived docs.  
  - Create new policy or certification language not present in the underlying document.  
  - Override governance status or labels.

Template instances should:

- Include stable IDs (experiment IDs, model IDs, SOP IDs) for graph linkage.  
- Maintain clear separation between data-backed facts, interpretation, and speculation.

---

## 🧪 Validation & CI/CD

Templates integrate with KFM CI/CD to ensure every derived document is compliant.

### 1. Primary Validation Workflows

| Workflow                 | Role                                              | Key Output                                            |
|--------------------------|---------------------------------------------------|-------------------------------------------------------|
| `docs-lint.yml`          | Markdown structure, headings, front‑matter, links | `reports/self-validation/docs/lint_summary.json`      |
| `faircare-validate.yml`  | FAIR+CARE & ethics checks on docs + data         | `reports/faircare/faircare_summary.json`              |
| `telemetry-export.yml`   | Aggregates template usage & doc metrics           | `releases/v11.2.6/docs-templates-telemetry.json`      |

Author guidance:

- Any new document created from a template must **keep the YAML scaffold** and fill in required fields.  
- CI will block merges if:
  - Front‑matter is incomplete or malformed.  
  - Required sections or governance references are missing.  
  - Disallowed headings or missing Version History/footer are detected.

---

## 📦 Data & Metadata

Templates are treated as **reference entities**:

- Each template file:
  - Has a stable path (`docs/templates/*.md`).  
  - Is indexed by this document and by doc catalogs.  
  - Carries governance metadata in its own front‑matter.

Derived documents:

- Set their own `doc_uuid`, `semantic_document_id`, and `event_source_id`.  
- Inherit governance references (`governance_ref`, `ethics_ref`, `sovereignty_policy`) as appropriate.  
- MUST include:
  - A `🕰️ Version History` section.  
  - The standard governance footer (Docs Root, Standards/Markdown Protocol, Governance Charter).

Telemetry for template usage (e.g., counts of experiment/model/SOP docs, validation status) is stored in:

- `releases/v11.2.6/docs-templates-telemetry.json`, and  
- Referenced by observability dashboards and audits.

---

## 🌐 STAC, DCAT & PROV Alignment

Templates themselves are non‑spatial, but align with KFM’s metadata ecosystem:

- **DCAT**  
  - This index acts as a `dcat:CatalogRecord` with associated `dcat:Dataset` for the template collection.  
  - Individual templates can be modeled as distributions (e.g., `mediaType: text/markdown`).

- **STAC**  
  - A `kfm-docs-templates` STAC Collection may list templates as Items with `geometry: null` and `datetime = last_updated`.  
  - Links from data collections to relevant templates (e.g., experiment template used for a given domain) may be added as `links` with custom `rel` types.

- **PROV-O**  
  - This index is a `prov:Plan` describing documentation patterns.  
  - Concrete docs use `prov:wasDerivedFrom` to link back to specific template versions.  
  - CI workflows and template-based generators (`mcp` tools) are `prov:Activity` instances associated with appropriate `prov:Agent`s.

---

## 🧱 Architecture

In the KFM monorepo architecture:

- `docs/templates/**` defines **documentation contracts**.  
- `mcp/experiments/**`, `mcp/model_cards/**`, `mcp/sops/**`, and other derived docs implement those contracts.  
- CI workflows:
  - Enforce structural constraints via lint and schema checks.  
  - Export telemetry that tracks compliance and coverage.  
- The knowledge graph ingests:
  - Template instances as CIDOC `E29 Design or Procedure`.  
  - Relations between experiments, models, SOPs, datasets, and workflow Activities.

This index is the **single source of truth** for:

- Which templates are canonical.  
- Where they live.  
- How they must be validated and governed.

---

## ⚖ FAIR+CARE & Governance

Templates embed FAIR+CARE expectations into every downstream doc:

- **FAIR**  
  - Front‑matter ensures **Findability** and **Accessibility**.  
  - Standardized fields support **Interoperability** with catalogs and graph.  
  - Version history and provenance enable **Reusability**.

- **CARE**  
  - Model cards include sections for Ethics, Bias, and Limitations.  
  - Experiments and SOPs include governance references and responsibility notes.  
  - Templates provide hooks for redaction, anonymization, or generalization when sensitive or sovereign data is involved.

Governance hooks:

- Template use is logged via telemetry and can be audited.  
- Councils (FAIR+CARE, Governance, Security) can track:
  - Which documents use which template versions.  
  - Whether required sections or governance notes have been removed or altered.

AI/agent systems may **summarize** or **highlight** template-based docs but MUST NOT:

- Alter normative text.  
- Introduce speculative governance statements.  
- Override policies defined here or in KFM-MDP / governance docs.

---

## 🕰️ Version History

| Version   | Date       | Author         | Summary                                                                                                                      |
|----------:|-----------:|----------------|------------------------------------------------------------------------------------------------------------------------------|
| v11.2.6   | 2025-12-11 | `@kfm-docs`    | Updated to KFM‑MDP v11.2.6; added Core Markdown Template, aligned paths to v11.2.6 releases/schemas, reorganized sections to heading registry, clarified STAC/DCAT/PROV and CI integration. |
| v11.2.4   | 2025-12-06 | `@kfm-docs`    | Expanded front‑matter; converted sections to approved H2 registry; added Story Node & telemetry integration and metadata alignment. |
| v10.2.2   | 2025-11-12 | `@kfm-docs`    | Aligned telemetry refs to v10.2.0; clarified integration with docs-lint and FAIR+CARE workflows.                            |
| v10.0.0   | 2025-11-10 | `@kfm-docs`    | Introduced telemetry schema v2; updated governance workflows and MCP/FAIR+CARE sections.                                    |
| v9.7.0    | 2025-11-05 | `@kfm-docs`    | Unified experiment, model, and SOP templates under a stable release.                                                        |
| v9.5.0    | 2025-10-20 | `@kfm-council` | Added FAIR+CARE audit metadata and governance integration.                                                                  |
| v9.0.0    | 2025-06-01 | `@kfm-core`    | Established baseline templates with MCP compliance.                                                                         |

---

<div align="center">

📄 **Kansas Frontier Matrix — Documentation Templates Index (v11.2.6)**  
Documentation Integrity · FAIR+CARE Governance · Platinum‑Grade Reproducibility  

[⬅ Back to Documentation Index](../README.md) ·  
[📘 Markdown Protocol (KFM‑MDP v11.2.6)](../standards/kfm_markdown_protocol_v11.2.6.md) ·  
[⚖ Governance Charter](../standards/governance/ROOT-GOVERNANCE.md)

</div>