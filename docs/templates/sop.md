---
title: "🧾 Kansas Frontier Matrix — Standard Operating Procedure (SOP) Template (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/templates/sop.md"

version: "v11.2.4"
last_updated: "2025-12-06"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Autonomous"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
signature_ref: "releases/v11.2.4/signature.sig"
attestation_ref: "releases/v11.2.4/slsa-attestation.json"
sbom_ref: "releases/v11.2.4/sbom.spdx.json"
manifest_ref: "releases/v11.2.4/manifest.zip"
telemetry_ref: "releases/v11.2.4/docs-sop-template-telemetry.json"
telemetry_schema: "schemas/telemetry/docs-sop-template-v11.2.4.json"
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
doc_kind: "Guide"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"

scope:
  domain: "sop-templates"
  applies_to:
    - "docs/templates/sop.md"
    - "docs/sop/*.md"
    - "docs/sops/*.md"

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
sunset_policy: "Superseded by SOP Template v12"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "HowTo"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/templates/sop.md@v10.2.2"
  - "docs/templates/sop.md@v10.0.0"
  - "docs/templates/sop.md@v9.7.0"
  - "docs/templates/sop.md@v9.5.0"
  - "docs/templates/sop.md@v9.0.0"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/kfm-sop-template-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/kfm-sop-template-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:templates:sop:v11.2.4"
semantic_document_id: "kfm-sop-template-v11.2.4"
event_source_id: "ledger:kfm:doc:templates:sop:v11.2.4"
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

# 🧾 **Kansas Frontier Matrix — Standard Operating Procedure (SOP) Template**  
`docs/templates/sop.md`

**Purpose**  
Provide a structured, machine-verifiable template for documenting operational workflows within the Kansas Frontier Matrix (KFM).  
This ensures all processes are **transparent**, **auditable**, and **FAIR+CARE**-aligned under **Master Coder Protocol v6.3** and **KFM-MDP v11.2.4**.

<img src="https://img.shields.io/badge/Docs-MCP_v6.3-blue" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.4-purple" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-green" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Certified-orange" />
<img src="https://img.shields.io/badge/Status-Template-lightgrey" />

</div>

---

## 📘 Overview

### 1. Template Scope

This **SOP Template** standardizes documentation for:

- ETL pipelines and data governance workflows.  
- AI model retraining, explainability, and deployment.  
- FAIR+CARE audits, ledger updates, and schema validation.  
- Sustainability, telemetry, and provenance reporting routines.  

Every SOP created from this template must:

- Be **deterministic and reproducible** (inputs, tools, and outputs are explicit).  
- Be **governed** (linked to FAIR+CARE policies and data sovereignty rules).  
- Be **catalog-ready** (indexable via DCAT/STAC/PROV and graph-insertable).  
- Pass documentation and governance CI checks before adoption in production.

### 2. Author Quickstart

1. Copy this file to `docs/sop/` as `docs/sop/<sop-name>.md`.  
2. Update the YAML front-matter (`title`, `path`, `version`, `last_updated`, etc.).  
3. Fill each H3 section under the headings below (do **not** add new H2 headings).  
4. Run `docs-lint`, `faircare-validate`, and confirm telemetry export via PR checks.  

---

## 🗂️ Directory Layout

SOP templates and concrete SOPs live alongside other documentation and workflows:

~~~text
📁 KansasFrontierMatrix/
├── 📁 docs/                                             # All documentation
│   ├── 📁 templates/                                   # Reusable documentation templates
│   │   📄 README.md                                    # 📄 Templates index + usage
│   │   📄 experiment.md                                # 🧪 Experiment / analysis template
│   │   📄 model_card.md                                # 🤖 AI/ML model card template
│   │   📄 sop.md                                       # 🧾 SOP template (this file)
│   ├── 📁 sop/                                         # 🧾 Concrete SOPs for KFM operations
│   │   📄 etl-lidar-intake.md                          # 🗺️ Example: LiDAR ingestion SOP
│   │   📄 ai-model-retrain.md                          # 🤖 Example: model retrain SOP
│   │   📄 governance-faircare-review.md                # ⚖ Example: FAIR+CARE review SOP
│   └── 📁 workflows/                                   # ⚙️ Workflow documentation (CI/CD)
│       📄 README.md                                    # CI/CD index
├── 📁 .github/
│   └── 📁 workflows/                                   # CI/CD YAML definitions
│       📄 docs-lint.yml                                # 📏 Markdown + SOP structure checks
│       📄 faircare-validate.yml                        # ⚖ FAIR+CARE + governance validation
│       📄 telemetry-export.yml                         # 📈 Telemetry aggregation
├── 📁 releases/                                        # 📦 Versioned releases and artifacts
│   📁 v11.2.4/
│   ├── 📄 sbom.spdx.json                               # 🧬 SBOM for this release
│   ├── 📄 manifest.zip                                 # 📑 Release manifest (checksums, assets)
│   └── 📄 focus-telemetry.json                         # 📈 Unified telemetry ledger
└── 📁 reports/
    ├── 📁 self-validation/                             # ✅ Docs + SOP validation reports
    ├── 📁 faircare/                                    # ⚖ FAIR+CARE reports
    └── 📁 audit/                                       # 🔍 Governance / workflow ledgers
~~~

Concrete SOPs **must**:

- Use `docs/sop/` (or a clearly documented equivalent) as their root.  
- Set `path` in front-matter to the actual repo-relative path.  

---

## 🧭 Context

SOPs are **operational blueprints** describing how KFM activities are carried out:

- They implement **prov:Plan** entities within PROV-O.  
- They are referenced by CI workflows, pipelines, and human-run procedures.  
- They enable **Story Nodes** and **Focus Mode** to narrate *how* KFM performs specific tasks.  

The SOP template is designed to:

- Align with the **KFM Markdown Protocol** (headings, front-matter, diagrams).  
- Provide enough structure for automated extraction into DCAT/STAC and the knowledge graph.  
- Support FAIR+CARE governance decisions by clearly documenting responsibilities and checks.

---

## 🗺️ Diagrams

Authors may include **at most one Mermaid diagram per SOP section** to visualize a process.

Example SOP flow (adapt per SOP):

~~~mermaid
flowchart TD
    A["Start SOP"] --> B["Prepare Environment & Inputs"]
    B --> C["Execute Core Steps"]
    C --> D["Run Validation & QA Checks"]
    D --> E{"All Checks Pass?"}
    E -->|Yes| F["Record Results & Update Telemetry"]
    E -->|No| G["Remediate, Re-run, or Escalate"]
    F --> H["End SOP"]
    G --> H["End SOP (with Issues Logged)"]
~~~

Each SOP should accompany a diagram with:

- A brief textual description of the main path and key decision points.  
- A note on failure handling and escalation.

---

## 🧠 Story Node & Focus Mode Integration

SOPs are used by **Story Nodes** and **Focus Mode** to explain *how* KFM works operationally:

- Focus Mode can surface a SOP when a user asks *“How does KFM retrain models?”* or *“How do we validate STAC catalogs?”*.  
- SOPs can be referenced from Story Nodes via IDs like:  
  `urn:kfm:sop:etl:etl-lidar-intake@v11.2.4`.

When writing an SOP:

- Use **short, clearly scoped steps** so Focus Mode can reframe them cleanly.  
- Keep **one concept per paragraph or list item** for better segmentation.  
- Avoid vague pronouns; refer to systems and files explicitly (`docs/sop/etl-lidar-intake.md`).  

Focus Mode:

- ✅ **MAY** summarize the procedure or highlight key steps.  
- ❌ **MUST NOT** rewrite or override the normative SOP steps.

---

## 🧪 Validation & CI/CD

This section describes **how SOPs are validated**, not how individual SOPs should behave (which goes in their own files).

### 1. Required Workflows

Every SOP derived from this template must pass:

| Workflow                 | Purpose                                         | Key Output                                           |
|--------------------------|-------------------------------------------------|------------------------------------------------------|
| `docs-lint.yml`          | Markdown + front-matter + heading validation   | `reports/self-validation/docs/lint_summary.json`     |
| `faircare-validate.yml`  | FAIR+CARE + governance + sensitivity checks    | `reports/faircare/faircare_summary.json`             |
| `telemetry-export.yml`   | Telemetry aggregation for documentation events | `releases/v11.2.4/focus-telemetry.json`             |

### 2. Example SOP-Related Checks

Concrete SOPs should document:

- Which workflows must succeed (e.g., `stac-validate.yml`, `ai-train.yml` if relevant).  
- Where validation reports are stored (under `reports/`).  
- Any **blocking criteria** (e.g., “deployment blocked unless FAIR+CARE passes with zero critical findings”).

---

## 📦 Data & Metadata

### 1. Required Front-Matter for Concrete SOPs

Each SOP **must** begin with a YAML front-matter block like:

~~~yaml
---
title: "🧾 [SOP Title]"
path: "docs/sop/[filename].md"
version: "vX.Y.Z"
last_updated: "YYYY-MM-DD"
review_cycle: "Annual · Autonomous"
commit_sha: "<commit-hash>"

sbom_ref: "releases/vX.Y.Z/sbom.spdx.json"
manifest_ref: "releases/vX.Y.Z/manifest.zip"
telemetry_ref: "releases/vX.Y.Z/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/docs-sop-template-vX.Y.Z.json"

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---
~~~

CI will **fail** if required keys are missing or malformed.

### 2. SOP Sections (to be used as H3 in Concrete SOPs)

Concrete SOPs should implement these H3 sections under their allowed H2 headings:

- `### 🎯 Purpose`  
- `### 🧩 Scope`  
- `### ⚙️ Prerequisites`  
- `### 🪜 Procedure`  
- `### 🧪 Validation & Quality Assurance`  
- `### 🔄 Change Management`  

Their location in this template:

- Conceptually described under **🧱 Architecture** (see below).  
- Fully instantiated in each SOP file under the same H2 heading.

---

## 🌐 STAC, DCAT & PROV Alignment

SOPs can be treated as **first-class catalog and provenance entities**:

- **DCAT**  
  - Represent an SOP as a `dcat:Dataset` or `dcat:CatalogRecord` with:  
    - `dct:title` = SOP title.  
    - `dct:description` = Brief summary from Purpose section.  
    - `dct:modified` = `last_updated`.  
    - `dct:license` = CC-BY 4.0.  

- **STAC**  
  - SOPs can be assets in a documentation-oriented Collection (e.g., `kfm-docs`).  
  - `id` = SOP semantic ID; `properties.datetime` = `last_updated`.  

- **PROV-O**  
  - Each SOP is a `prov:Plan` (`E29 Design or Procedure` in CIDOC-CRM).  
  - Activities that “follow” the SOP (e.g., ETL jobs) are `prov:Activity` with a `prov:wasAssociatedWith` relationship to agents and `prov:wasInformedBy` the SOP.

Concrete SOPs **may** include a short paragraph describing where they appear in catalogs or provenance graphs.

---

## 🧱 Architecture

This section defines the **structure** of a concrete SOP using this template.

### 🎯 Purpose (H3 in Concrete SOP)

- Short paragraph on *why* the SOP exists and what goal it serves.  
- Should be specific enough to distinguish similar SOPs (e.g., LiDAR vs STAC validation).  

Example snippet:

> Document the steps for validating, packaging, and deploying FAIR+CARE-certified STAC/DCAT metadata for each quarterly archive.

### 🧩 Scope

Use a table to document **inclusions** and **exclusions**:

~~~markdown
### 🧩 Scope

| Included                                  | Excluded                          |
|-------------------------------------------|-----------------------------------|
| STAC/DCAT validation workflows            | Manual editing of STAC JSON       |
| FAIR+CARE audit automation                | Final Council decision text       |
~~~

### ⚙️ Prerequisites

List technical, procedural, or governance dependencies required before execution:

~~~markdown
### ⚙️ Prerequisites

| Requirement      | Description                                  |
|------------------|----------------------------------------------|
| **Environment**  | Python 3.11+, Docker 24+, Git CLI            |
| **Dependencies** | `pystac`, `jsonschema`, `requests`, `pytest`, `kfm-stac-tools` |
| **Credentials**  | GitHub token (read), STAC asset keys (if private) |
| **Validation Scripts** | Located under `tools/validation/` or `src/pipelines/validation/` |
~~~

### 🪜 Procedure

Provide numbered, reproducible instructions. Every step should be deterministic:

~~~markdown
### 🪜 Procedure

1. **Pull latest repository version**  
   ~~~bash
   git pull origin main
   ~~~

2. **Run FAIR+CARE validator**  
   ~~~bash
   make validate-faircare
   ~~~

3. **Validate schema & STAC/DCAT metadata**  
   ~~~bash
   make validate-schema
   ~~~

4. **Commit validation reports**  
   ~~~bash
   git add reports/faircare/ reports/self-validation/
   git commit -m "chore: FAIR+CARE + schema validation for vX.Y.Z"
   git push origin main
   ~~~

5. **Trigger CI governance sync**  
   - Confirm `governance_sync.yml` passes.  
   - Ensure `focus-telemetry.json` updated for current release.
~~~

### 🧪 Validation & Quality Assurance (Within Concrete SOP)

Concrete SOPs should link to specific checks:

~~~markdown
### 🧪 Validation & Quality Assurance

| Validation Type      | Expected Output                            | Workflow                             |
|----------------------|--------------------------------------------|--------------------------------------|
| Markdown / YAML Lint | No critical errors                         | `.github/workflows/docs-lint.yml`    |
| FAIR+CARE Audit      | Updated `faircare_summary.json`            | `.github/workflows/faircare-validate.yml` |
| Telemetry Log        | Appended entry in `focus-telemetry.json`   | `.github/workflows/telemetry-export.yml`  |
~~~

### 🔄 Change Management

Document how this SOP is updated, reviewed, and approved:

~~~markdown
### 🔄 Change Management

| Stage    | Description                                 | Responsible                      |
|----------|---------------------------------------------|----------------------------------|
| Draft    | Propose changes; open PR                    | Contributor                      |
| Review   | FAIR+CARE + technical validation            | Governance Council & Maintainers |
| Approval | Merge to `main`                             | Repository Maintainer            |
| Publish  | CI runs; telemetry updated                  | CI/CD Pipelines                  |
~~~

---

## ⚖ FAIR+CARE & Governance

Concrete SOPs must explain how they satisfy FAIR+CARE principles:

~~~markdown
### ⚖ FAIR+CARE Mapping

| Principle  | Implementation Example                                      |
|-----------:|-------------------------------------------------------------|
| Findable   | SOP stored in `docs/sop/` with a stable path + version.     |
| Accessible | CC-BY 4.0 Markdown rendered in the repository.              |
| Interoperable | References STAC/DCAT, ISO 19115, and internal contracts. |
| Reusable   | Immutable ledger entries, checksum manifests, automation.   |
| CARE       | Reviewed for inclusivity, cultural impact, data sensitivity. |
~~~

Governance records are typically appended to:

~~~text
reports/audit/github-workflows-ledger.json
~~~

Concrete SOPs should note:

- Who must review changes (roles, e.g., FAIR+CARE Council, Infra team).  
- Any mandatory approvals (e.g., for sensitive or Indigenous data handling SOPs).  

---

## 🕰️ Version History

| Version    | Date       | Author        | Summary                                                                 |
|-----------:|------------|---------------|-------------------------------------------------------------------------|
| **v11.2.4** | 2025-12-06 | `@kfm-docs`   | Upgraded to KFM-MDP v11.2.4; added full metadata block, emoji-rich directory layout, and STAC/DCAT/PROV alignment; clarified SOP H3 section expectations. |
| v10.2.2    | 2025-11-12 | `@kfm-docs`   | Aligned telemetry refs to v10.2.0; clarified governance, CI, and sustainability linkages. |
| v10.0.0    | 2025-11-10 | `@kfm-docs`   | Enhanced telemetry schema; FAIR+CARE integration and ISO 19115 compliance. |
| v9.7.0     | 2025-11-05 | `@kfm-docs`   | Created SOP template with governance integration and CI mapping.        |
| v9.5.0     | 2025-10-20 | `@kfm-docs`   | Added telemetry reporting and automation references.                    |
| v9.0.0     | 2025-06-01 | `@kfm-core`   | Initial SOP template creation.                                          |

---

<div align="center">

🧾 **Kansas Frontier Matrix — SOP Template (v11.2.4)**  
Operational Clarity · FAIR+CARE Governance · Catalog & Graph Ready  

[⬅ Back to Templates Index](README.md) ·  
[📘 Markdown Protocol (KFM-MDP v11.2.4)](../standards/kfm_markdown_protocol_v11.2.4.md) ·  
[⚖ Governance Charter](../standards/governance/ROOT-GOVERNANCE.md)

</div>
