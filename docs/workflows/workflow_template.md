---
title: "🧩 Kansas Frontier Matrix — CI/CD Workflow Documentation Template"
path: "docs/workflows/workflow_template.md"

version: "v11.2.4"
last_updated: "2025-12-06"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
signature_ref: "releases/v11.2.4/signature.sig"
attestation_ref: "releases/v11.2.4/slsa-attestation.json"
sbom_ref: "releases/v11.2.4/sbom.spdx.json"
manifest_ref: "releases/v11.2.4/manifest.zip"
telemetry_ref: "releases/v11.2.4/docs-workflows-telemetry.json"
telemetry_schema: "schemas/telemetry/docs-workflows-template-v11.2.4.json"
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
  domain: "documentation-templates"
  applies_to:
    - "docs/workflows/*.md"
    - ".github/workflows/*.yml"

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
sunset_policy: "Superseded by CI/CD Workflow Documentation Template v12"

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
  - "docs/workflows/workflow_template.md@v10.2.4"
  - "docs/workflows/workflow_template.md@v1.0.0"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/kfm-markdown-protocol-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/kfm-markdown-protocol-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:workflows:workflow-template:v11.2.4"
semantic_document_id: "kfm-workflow-doc-template-v11.2.4"
event_source_id: "ledger:kfm:doc:workflows:workflow-template:v11.2.4"
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

# 🧩 **Kansas Frontier Matrix — CI/CD Workflow Documentation Template**  
`docs/workflows/workflow_template.md`

**Purpose**  
Provide a **governed, copy‑pasteable template** for documenting any CI/CD workflow in the Kansas Frontier Matrix monorepo.  
Authors use this file as a **baseline** to create new `docs/workflows/<workflow-name>.yml.md` documents that are **KFM‑MDP v11.2.4 compliant**, **telemetry‑aware**, and ready for **Story Node / Focus Mode** integration.

<img src="https://img.shields.io/badge/Docs·MCP-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.4-purple" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-green" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Governance%20Aligned-orange" />
<img src="https://img.shields.io/badge/Status-Template-brightgreen" />

</div>

---

## 📘 Overview

### 1. How to Use This Template

1. **Copy this file** to a new path, for example:  
   `docs/workflows/{{workflow_slug}}.yml.md`
2. **Update the YAML front‑matter**:
   - `title`, `path`, `version`, `last_updated`.  
   - `sbom_ref`, `manifest_ref`, `telemetry_ref`, and `telemetry_schema` for the workflow.  
   - `doc_uuid`, `semantic_document_id`, `event_source_id`, `provenance_chain`.
3. **Replace placeholders** in the body:
   - `{{WORKFLOW_NAME}}`, `{{WORKFLOW_FILE}}`, `{{WORKFLOW_KIND}}`, `{{TELEMETRY_SCHEMA_FILE}}`, etc.
4. **Describe the workflow** under each section using the guidance below.
5. Commit and let `docs-lint.yml` + `schema-lint.yml` enforce compliance.

> **Convention:**  
> Each workflow documentation file **MUST** describe exactly one GitHub Actions workflow defined under `.github/workflows/<workflow-name>.yml`.

### 2. Recommended Naming Pattern

- Workflow file: `.github/workflows/{{workflow_slug}}.yml`  
- Doc file: `docs/workflows/{{workflow_slug}}.yml.md`  
- Telemetry schema: `schemas/telemetry/workflows/{{workflow_slug}}-vX.json`  

Use lower‑kebab‑case for `{{workflow_slug}}` (e.g., `docs-lint`, `stac-validate`, `ai-train`).

---

## 🗂️ Directory Layout

Use this section to show **where the workflow lives** and which scripts / paths it touches.  
Update the placeholders to match the new workflow.

~~~text
📁 docs/
└── 📁 workflows/
    📄 README.md                               — CI/CD & governance workflows index
    📄 workflow_template.md                    — ← This template
    📄 {{workflow_slug}}.yml.md                — Your new workflow documentation

📁 .github/
└── 📁 workflows/
    📄 {{workflow_slug}}.yml                   — GitHub Actions workflow definition

📁 scripts/
└── 📁 {{workflow_domain}}/
    📄 {{workflow_slug}}_main.py               — (Example) main script invoked by workflow
    📄 {{workflow_slug}}_helpers.py            — (Example) helpers for this workflow

📁 reports/
└── 📁 {{workflow_slug}}/
    📄 *.json                                  — Machine-readable outputs & summaries
    📄 *.md                                    — Human-readable summaries (optional)

📁 releases/
└── 📁 v{{release_major_minor}}/
    📄 {{workflow_slug}}-telemetry.json        — Telemetry for this workflow
    📄 sbom.spdx.json                          — Tooling SBOM (if applicable)
    📄 manifest.zip                            — Release manifest (hashes, configs)
~~~

**Author task:** Fill in `{{workflow_slug}}`, `{{workflow_domain}}`, and `{{release_major_minor}}` (for example, `11.2` or `11.2.4`).

---

## 🧭 Context

Use this section to situate the workflow inside the **KFM CI/CD ecosystem**:

- Describe the **purpose** of the workflow in 2–3 sentences.  
- Specify **which phase of the pipeline** it belongs to, e.g.:

  > Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j knowledge graph → API layer → React/MapLibre/Cesium frontend → Story Nodes → Focus Mode  

- List **dependencies** on other workflows (e.g., telemetry exporter, schema-lint).  
- Note any **governance implications** (e.g., “blocks release if docs are invalid”).

### Author Checklist

When filling this section:

- [ ] State the **main responsibility** of `{{WORKFLOW_NAME}}`.  
- [ ] Indicate when it runs (e.g., `pull_request`, `push`, `schedule`).  
- [ ] Mention any **hard gates** (conditions that fail builds).  

---

## 🗺️ Diagrams

Use this section to add one or two mermaid diagrams that **illustrate the workflow**.  
For most workflow docs, a **single flowchart** is sufficient.

### 1. Flowchart Template

Replace node labels to match `{{WORKFLOW_NAME}}` steps.

~~~mermaid
flowchart LR
    A["Trigger: PR / Push / Schedule"] --> B["Checkout Repository"]
    B --> C["Setup Tooling (Python / Node / etc.)"]
    C --> D["Run {{WORKFLOW_NAME}} Core Steps"]
    D --> E["Generate Reports & Artifacts"]
    E --> F["Emit Telemetry Events"]
    F --> G["Update Governance / Dashboards / Gates"]
~~~

### 2. Timeline Template (Optional)

If the workflow has a clear **lifecycle**, use a timeline:

~~~mermaid
timeline
    title {{WORKFLOW_NAME}} — Run Lifecycle
    section Preparation
      T0 : Workflow triggered
      T1 : Repo checked out & environment prepared
    section Execution
      T2 : Core jobs execute
      T3 : Validation & summarization
    section Publication
      T4 : Telemetry merged and validated
      T5 : Governance and dashboards updated
~~~

---

## 🧠 Story Node & Focus Mode Integration

Document how **Story Nodes** and **Focus Mode** might use this workflow’s outputs.

### 1. Story Node Patterns

Examples you can adapt:

- `urn:kfm:story-node:infra:{{workflow_slug}}:<run_id>`  
  - Describes status, impact, or incidents from a specific run.  

- `urn:kfm:story-node:infra:{{workflow_slug}}-trend:<period>`  
  - Summarizes trends in failures, runtime, energy, or errors for the workflow.

### 2. Focus Mode Behavior

Describe what Focus Mode **may** and **must not** do for this workflow:

- **MAY**:
  - Summarize the workflow’s purpose and recent health.  
  - Surface the most recent `reports/**` summaries and telemetry slices.  

- **MUST NOT**:
  - Alter or reinterpret telemetry values.  
  - Claim success or certification without underlying evidence from reports.  

> **Author tip:** Link to the workflow’s telemetry schema (e.g., `schemas/telemetry/workflows/{{workflow_slug}}-v3.json`) if relevant.

---

## 🧪 Validation & CI/CD

Use this section to:

- Show the **triggers** and **paths** for `{{WORKFLOW_NAME}}`.  
- Provide a **conceptual YAML stub** (not necessarily exact, but structurally similar).  
- Document which conditions **fail** the job vs. raise warnings.

### 1. Trigger & Scope Table

Fill in concrete values:

| Trigger            | Paths / Workflows                        | Notes                          |
|-------------------:|------------------------------------------|--------------------------------|
| `pull_request`     | `{{paths_for_pr}}`                        | Blocks merge on failure        |
| `push` (protected) | `{{paths_for_push}}`                      | Required on `main` / `release` |
| `schedule`         | `{{cron_or_—}}`                           | Optional regression checks     |
| `workflow_dispatch`| —                                        | Manual / backfill runs         |

### 2. Conceptual YAML Template

Adapt this to your specific workflow:

~~~yaml
name: "{{WORKFLOW_NAME}} (Governed)"

on:
  pull_request:
    paths: {{PULL_REQUEST_PATHS}}
  push:
    branches: ["main", "release/**"]
    paths: {{PUSH_PATHS}}
  schedule:
    - cron: "{{CRON_EXPRESSION}}"
  workflow_dispatch: {}

permissions:
  contents: read
  id-token: write

concurrency:
  group: {{workflow_slug}}-${{ github.ref }}
  cancel-in-progress: true

jobs:
  {{job_slug}}:
    runs-on: ubuntu-22.04
    timeout-minutes: {{TIMEOUT_MINUTES}}
    steps:
      - uses: actions/checkout@v4

      - name: Setup tooling
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: |
          pip install -r requirements.txt

      - name: Run {{WORKFLOW_NAME}} core logic
        run: |
          python scripts/{{workflow_domain}}/{{workflow_slug}}_main.py \
            --config configs/{{workflow_domain}}/{{workflow_slug}}.yaml \
            --out reports/{{workflow_slug}}/

      - name: Upload artifacts
        uses: actions/upload-artifact@v4
        with:
          name: {{workflow_slug}}_reports
          path: reports/{{workflow_slug}}/

      - name: Emit telemetry
        run: |
          python scripts/telemetry/emit_telemetry.py \
            --kind {{workflow_slug}} \
            --summary reports/{{workflow_slug}}/summary.json \
            --out {{workflow_slug}}_telemetry.json

      - name: Append telemetry to unified log
        run: |
          python scripts/telemetry/merge_telemetry.py \
            --in  {{workflow_slug}}_telemetry.json \
            --dest releases/v{{release_major_minor}}/focus-telemetry.json
~~~

### 3. Quality Gates

Describe:

- Which metrics or validation failures **fail the job**.  
- Which conditions are **warnings only** (logged, but allowed to pass).  
- Where thresholds are defined (e.g., `configs/{{workflow_domain}}/{{workflow_slug}}_policy.yaml`).

---

## 📦 Data & Metadata

Use this section to define:

- **Inputs** (e.g., paths, configs, previous reports).  
- **Outputs** (reports, summaries, artifacts, telemetry).  
- **Telemetry contracts** (schema file, key metrics).

### 1. Inputs & Outputs Table

Customize for your workflow:

| Type       | Path / Key                                                | Description                                |
|-----------:|-----------------------------------------------------------|--------------------------------------------|
| **Input**  | `{{input_path_1}}`                                        | Primary data or config                     |
| **Input**  | `{{input_path_2}}`                                        | Secondary data (optional)                  |
| **Output** | `reports/{{workflow_slug}}/summary.json`                  | Machine-readable summary                   |
| **Output** | `reports/{{workflow_slug}}/summary.md`                    | Human-readable PR summary (optional)       |
| **Artifact** | `reports/{{workflow_slug}}/**`                          | Artifact bundle uploaded by workflow       |
| **Telemetry** | `releases/v{{release_major_minor}}/focus-telemetry.json` | Unified ledger (this workflow appended) |

### 2. Telemetry Schema

Document:

- Schema location (e.g., `schemas/telemetry/workflows/{{workflow_slug}}-v3.json`).  
- Key metrics that must be present (e.g., `workflow_duration_sec`, `energy_wh`, `carbon_gco2e`, domain‑specific metrics).  

---

## 🌐 STAC, DCAT & PROV Alignment

If `{{WORKFLOW_NAME}}` interacts with STAC/DCAT/PROV:

- Describe which **STAC Collections/Items** or **DCAT Datasets** it touches.  
- Note whether it **validates**, **generates**, or **updates** catalogs.  
- Explain how runs are represented in **PROV**:

  - Activities: `ex:{{WorkflowCamel}}Run_<run_id>`.  
  - Entities: `ex:{{WorkflowCamel}}Report_<run_id>`.  
  - Agents: `ex:KFM_CI_Bot`, `ex:{{TeamName}}`.

If not applicable, state explicitly that the workflow **does not manipulate catalogs**, and only its **telemetry** may be cataloged as governance data.

---

## 🧱 Architecture

Use this section to tie the workflow into the **code architecture**:

- Which **modules** does it exercise (e.g., `src/pipelines`, `src/api`, `src/web`)?  
- What is the **boundary** of responsibility for the workflow vs. other jobs?  
- Any **configuration-driven patterns** (e.g., all behavior controlled by YAML/JSON).

### Author Checklist

- [ ] Mention relevant modules and scripts.  
- [ ] Clarify any shared libraries or utilities.  
- [ ] Note how failures are surfaced to PR authors (e.g., comments, status checks).

---

## ⚖ FAIR+CARE & Governance

Explain:

- How the workflow contributes to **FAIR** (Findable, Accessible, Interoperable, Reusable) practices.  
- Any **CARE**‑related logic (e.g., treatment of sensitive data in telemetry).  
- Where policies and thresholds are stored (config files, governance docs).

Example points you can reuse and tailor:

- Telemetry avoids storing **person‑level identifiers**; it focuses on systems and runs.  
- Energy and carbon metrics support **sustainability governance**.  
- Workflow results may drive **gates** for releases, especially when ethics or compliance checks are involved.

---

## 🕰️ Version History

Update this table as the template evolves.

| Version    | Date       | Author          | Summary                                                                                                      |
|-----------:|------------|-----------------|--------------------------------------------------------------------------------------------------------------|
| **v11.2.4** | 2025-12-06 | `@kfm-docs`     | Aligned with KFM-MDP v11.2.4; added full front-matter; standardized section layout; integrated Story Node, telemetry, and governance guidance. |
| v10.2.4   | 2025-11-12 | `@kfm-docs`     | Introduced v3 telemetry references and workflow naming conventions.                                         |
| v10.1.0   | 2025-11-10 | `@kfm-docs`     | Added initial workflow documentation skeleton for CI/CD jobs.                                               |
| v1.0.0    | 2025-11-01 | `@kfm-docs`     | Created initial workflow documentation template.                                                            |

---

<div align="center">

🧩 **Kansas Frontier Matrix — CI/CD Workflow Documentation Template (v11.2.4)**  
Documentation-First · FAIR+CARE Governance · CI/CD Discipline  

[⬅ Back to Workflows Index](./README.md) ·  
[📘 Docs Root](../README.md) ·  
[⚖ Governance Charter](../standards/governance/ROOT-GOVERNANCE.md)

</div>

