---
title: "🧩 Kansas Frontier Matrix — Workflow Documentation Template (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/templates/workflow_template.md"

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
telemetry_ref: "releases/v11.2.4/docs-workflow-template-telemetry.json"
telemetry_schema: "schemas/telemetry/workflows/template-v11.2.4.json"
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
  domain: "workflow-templates"
  applies_to:
    - "docs/templates/workflow_template.md"
    - "docs/workflows/*.yml.md"

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
sunset_policy: "Superseded by Workflow Documentation Template v12"

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
  - "docs/templates/workflow_template.md@v10.2.2"
  - "docs/templates/workflow_template.md@v10.0.0"
  - "docs/templates/workflow_template.md@v9.9.0"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/kfm-workflow-doc-template-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/kfm-workflow-doc-template-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:templates:workflow-doc:v11.2.4"
semantic_document_id: "kfm-workflow-doc-template-v11.2.4"
event_source_id: "ledger:kfm:doc:templates:workflow-doc:v11.2.4"
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

# 🧩 **Kansas Frontier Matrix — Workflow Documentation Template**  
`docs/templates/workflow_template.md`

**Purpose**  
Provide a **standardized, governance-aligned, machine-validatable template** for documenting all GitHub Actions workflows used across the Kansas Frontier Matrix (KFM).  
This enables **FAIR+CARE-compliant**, **MCP-DL v6.3-certified**, and **Diamond⁹ Ω / Crown∞Ω** automation practices across CI/CD, telemetry, governance, and AI pipelines.

<img src="https://img.shields.io/badge/Docs-MCP_v6.3-blue" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.4-purple" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-green" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Governance_Aligned-orange" />
<img src="https://img.shields.io/badge/Status-Template-lightgrey" />

</div>

---

## 📘 Overview

### Template Scope

Use this template to document **any workflow `.yml` file**, typically located under:

- `.github/workflows/` — CI/CD configuration.  
- `docs/workflows/` — Markdown documentation `*.yml.md` aligned with this template.

Each workflow documentation file **must**:

1. Contain complete **YAML front-matter** (version, SBOM, manifest, telemetry schema, governance refs).  
2. Describe workflow **purpose**, **triggers**, **permissions**, **jobs**, **inputs/outputs**, and **artifacts**.  
3. Declare how the workflow enforces **FAIR+CARE**, **MCP-DL v6.3**, and internal governance policies.  
4. Include a **Mermaid diagram** illustrating workflow logic (≤ 12 nodes, no custom `classDef`).  
5. Provide a **version history table** aligned with KFM release policy.  

### Author Quickstart

1. Copy this template to `docs/workflows/<workflow-name>.yml.md`.  
2. Update the front-matter (`title`, `path`, `version`, `telemetry_schema`, etc.).  
3. Replace placeholder content in each H3 section with workflow-specific details.  
4. Keep directory paths, emojis, and headings consistent with **KFM-MDP v11.2.4**.  
5. Open a PR and ensure CI passes: `docs-lint`, `faircare-validate`, `telemetry-export`.  

---

## 🗂️ Directory Layout

~~~text
📁 KansasFrontierMatrix/
├── 📁 docs/                                            # All documentation
│   ├── 📁 workflows/                                  # ⚙️ Workflow documentation (per CI job)
│   │   📄 README.md                                   # 🧭 CI/CD & governance workflows index
│   │   📄 docs-lint.yml.md                            # 🧪 Docs lint workflow doc
│   │   📄 faircare-validate.yml.md                    # ⚖ FAIR+CARE validation workflow doc
│   │   📄 stac-validate.yml.md                        # 🗂️ STAC/DCAT validation workflow doc
│   │   📄 telemetry-export.yml.md                     # 📈 Telemetry export workflow doc
│   │   📄 ai-train.yml.md                             # 🤖 AI training workflow doc
│   │   📄 ai-explainability.yml.md                    # 🔍 AI explainability workflow doc
│   │   📄 security-supply-chain.yml.md                # 🔒 Supply-chain security workflow doc
│   │   📄 schema-lint.yml.md                          # 📐 Schema lint workflow doc
│   │   📄 workflow_template.yml.md                    # 🧩 Workflow documentation template (instantiated)
│   └── 📁 templates/                                  # 📄 Shared documentation templates
│       📄 README.md                                   # Templates index
│       📄 experiment.md                               # 🧪 Experiment / analysis template
│       📄 model_card.md                               # 🤖 Model card template
│       📄 sop.md                                      # 🧾 SOP template
│       📄 workflow_template.md                        # 🧩 Workflow doc template (this file)
├── 📁 .github/
│   └── 📁 workflows/                                  # Actual GitHub Actions YAML workflows
│       📄 docs-lint.yml                               # 📏 Docs lint workflow
│       📄 faircare-validate.yml                       # ⚖ FAIR+CARE validation workflow
│       📄 stac-validate.yml                           # 🗂️ STAC/DCAT validation workflow
│       📄 telemetry-export.yml                        # 📈 Telemetry aggregation workflow
│       📄 ai-train.yml                                # 🤖 AI training workflow
│       📄 ai-explainability.yml                       # 🔍 Explainability workflow
│       📄 security-supply-chain.yml                   # 🔒 Supply-chain security workflow
│       📄 schema-lint.yml                             # 📐 Schema lint workflow
└── 📁 releases/
    └── 📁 v11.2.4/                                    # 📦 Release artifacts & telemetry
        📄 sbom.spdx.json                              # 🧬 SBOM for this release
        📄 manifest.zip                                # 📑 Asset + checksum manifest
        📄 focus-telemetry.json                        # 📈 Unified telemetry ledger
~~~

When instantiating this template:

- Ensure `path` in front-matter matches `docs/workflows/<workflow-name>.yml.md`.  
- Keep emoji labels and comments aligned with this layout for CI and Focus Mode.  

---

## 🧭 Context

Workflow documentation connects:

- The **YAML definition** in `.github/workflows/*.yml`.  
- The **governed narrative** in `docs/workflows/*.yml.md`.  
- The **telemetry and provenance trail** in `releases/*/focus-telemetry.json` and `reports/audit/*`.

Each workflow doc should answer:

- *What* the workflow does.  
- *When* it runs (triggers).  
- *How* it runs (jobs, steps, permissions, caching).  
- *Why* it exists (governance, FAIR+CARE, sustainability rationale).  

Docs are modeled as:

- `prov:Plan` in PROV-O.  
- `E29 Design or Procedure` in CIDOC-CRM.  
- Catalog entries in DCAT/STAC-based documentation collections.  

---

## 🗺️ Diagrams

Workflow docs must include a **Mermaid flowchart** describing the control flow.

### Diagram Rules

- Use `flowchart LR` or `flowchart TD`.  
- At most 12 nodes per diagram.  
- Quoted labels, no `classDef`.  
- One diagram per workflow doc is typical (more allowed if sections are complex).  

### Diagram Template

~~~mermaid
flowchart LR
  A["Trigger (push / PR / schedule / dispatch)"] --> B["Checkout Repository"]
  B --> C["Setup Environment & Dependencies"]
  C --> D["Run Core Jobs (lint / validate / train / scan)"]
  D --> E["Collect Reports & Artifacts"]
  E --> F["Emit & Merge Telemetry"]
  F --> G["Update Governance / Release State"]
~~~

Replace node labels to reflect the actual workflow.

---

## 🧠 Story Node & Focus Mode Integration

Workflow docs are used by **Story Nodes** and **Focus Mode** to explain KFM automation:

- Focus Mode can answer questions like *“What happens when I push STAC changes?”* by rendering relevant workflow sections.  
- Story Nodes may reference workflow docs using stable IDs such as:  
  `urn:kfm:workflow-doc:stac-validate.yml@v11.2.4`.

Author guidelines:

- Keep H3 sections **short and tightly scoped** (Triggers, Jobs, Inputs, Permissions, etc.).  
- Use descriptive, unambiguous phrases (avoid “it”, “this one”; prefer workflow names and filenames).  
- Include concrete file paths and artifact locations so Story Nodes can deep-link.  

Focus Mode:

- ✅ May summarize and highlight portions of this template or derived docs.  
- ❌ Must not invent workflows, jobs, or permissions not present in YAML.  

---

## 🧪 Validation & CI/CD

This template and all workflow docs must pass:

- **`docs-lint.yml`** — Markdown structure, H2/H3 headings, front-matter schema, Mermaid syntax.  
- **`faircare-validate.yml`** — FAIR+CARE labeling, governance fields, sovereignty references.  
- **`telemetry-export.yml`** — Telemetry record for documentation changes and usage.  

Concrete workflow docs **must describe**:

- Their place in the CI pipeline (e.g., gating merges, pre-release checks, telemetry roll-up).  
- Any **hard gates** (e.g., “no release if STAC/DCAT validation fails”).  
- Where validation and audit reports are stored under `reports/`.  

---

## 📦 Data & Metadata

### Required Front-Matter (Concrete Workflow Docs)

Every workflow documentation file must begin with:

~~~yaml
---
title: "⚙️ <Human-Friendly Workflow Name> — `<workflow-name>.yml`"
path: "docs/workflows/<workflow-name>.yml.md"

version: "vX.Y.Z"
last_updated: "YYYY-MM-DD"
review_cycle: "Continuous · Autonomous"
commit_sha: "<latest-commit-hash>"

sbom_ref: "releases/vX.Y.Z/sbom.spdx.json"
manifest_ref: "releases/vX.Y.Z/manifest.zip"
telemetry_ref: "releases/vX.Y.Z/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/workflows/<workflow-name>-vX.json"

governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---
~~~

CI will fail if:

- Any required key is missing or malformed.  
- `path` does not match the actual file location.  
- `telemetry_schema` is not recognized by the telemetry system.  

### Required H3 Sections (Concrete Docs)

Within the allowed H2 headings of this template, each workflow doc should define:

- Under **📘 Overview**  
  - `### Purpose`  

- Under **🧱 Architecture**  
  - `### Triggers & Scope`  
  - `### Workflow Definition (YAML Excerpt)`  
  - `### Jobs Summary`  
  - `### Inputs & Outputs`  
  - `### Permissions (Least Privilege)`  
  - `### Caching & Performance`  
  - `### Failure Modes & Rollback`  

- Under **⚖ FAIR+CARE & Governance**  
  - `### FAIR+CARE Governance Matrix`  

This structure is enforced via `docs-lint.yml` + schema validation.

---

## 🌐 STAC, DCAT & PROV Alignment

Workflow docs can be cataloged and traced like any other asset:

- **DCAT**  
  - Represented as `dcat:Dataset` with distributions for Markdown and rendered HTML.  
  - `dct:title` from front-matter `title`.  
  - `dct:modified` from `last_updated`.  
  - `dct:license` from `license`.  

- **STAC**  
  - Included as Items in a documentation-focused Collection (e.g., `kfm-docs-workflows`).  
  - `id` set to `semantic_document_id` or `<workflow-name>-doc-vX.Y.Z`.  
  - `properties.datetime` set to `last_updated`.  

- **PROV-O**  
  - Workflow doc = `prov:Plan`.  
  - Each CI run = `prov:Activity` that:  
    - `prov:used` the YAML file and repository state.  
    - `prov:wasAssociatedWith` a runner, maintainers.  
    - `prov:generated` artifacts, telemetry events, and governance decisions.  

---

## 🧱 Architecture

This section describes the **content pattern** for each concrete workflow documentation file.

### Triggers & Scope

Document how the workflow is invoked and what paths it watches:

~~~markdown
### Triggers & Scope

| Trigger             | Paths                           | Notes                                  |
|--------------------:|---------------------------------|----------------------------------------|
| `push`              | `src/**`, `data/**`             | Restricted to `main` / `release/**`    |
| `pull_request`      | `docs/**`, `schemas/**`         | Blocks merges on validation failure    |
| `workflow_dispatch` | —                               | Manual execution with inputs           |
| `schedule`          | `0 3 * * *`                     | Nightly governance or telemetry runs   |
~~~

### Workflow Definition (YAML Excerpt)

Include a minimal, accurate YAML excerpt from `.github/workflows/<workflow-name>.yml`:

~~~yaml
name: "Example Workflow — Governed"

on:
  push:
    branches: ["main", "release/**"]
    paths: ["src/**", "data/**"]
  pull_request:
    paths: ["docs/**", "schemas/**"]

permissions:
  contents: read
  id-token: write

jobs:
  example:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4
      - name: Say hello
        run: echo "Hello Kansas Frontier Matrix!"
~~~

### Jobs Summary

Summarize all jobs and their responsibilities:

~~~markdown
### Jobs Summary

| Job        | Purpose                                  | Outputs/Artifacts                       |
|-----------:|------------------------------------------|-----------------------------------------|
| `build`    | Compile or validate project components   | Binaries, bundle manifests              |
| `validate` | Run linting, schema checks, FAIR+CARE    | `reports/**.json`, logs                 |
| `deploy`   | Publish artifacts to releases/registries | `releases/vX.Y.Z/manifest.zip`         |
~~~

### Inputs & Outputs

Document workflow inputs and outputs (ideally with links to schemas):

~~~markdown
### Inputs & Outputs

| Type      | Field           | Description                                   |
|-----------|-----------------|-----------------------------------------------|
| **Input** | `dataset_ref`   | STAC/DCAT dataset or contract ID             |
| **Input** | `config_path`   | Relative path to workflow configuration       |
| **Output**| `reports/validation.json` | Contract or metadata validation report |
| **Output**| `releases/vX.Y.Z/focus-telemetry.json` | Global telemetry ledger entry   |
~~~

### Permissions (Least Privilege)

Explicitly list and justify each GitHub `permissions` field:

~~~markdown
### Permissions (Least Privilege)

| Permission        | Reason                                         |
|-------------------|------------------------------------------------|
| `contents: read`  | Required to inspect repository files           |
| `id-token: write` | Enables OIDC-based signing / attestations      |
| `packages: write` | Only if workflow uploads packages to registry  |
~~~

Workflows granting broader permissions must document why and who approved them.

### Caching & Performance

Describe caching strategy and performance considerations:

~~~markdown
### Caching & Performance

- Use `actions/cache@v4` for dependency caches (pip, npm, etc.).  
- Cache keys must include lockfiles (e.g., `requirements.lock`, `poetry.lock`, `package-lock.json`).  
- Typical speedup: **40–70%** for repeated runs on active branches.  
- Document any known cold-start or heavy steps (e.g., large model downloads).  
~~~

### Failure Modes & Rollback

Capture expected failures and operator actions:

~~~markdown
### Failure Modes & Rollback

- **Missing contract fields** → Fail validation job; fix schema or data and rerun workflow.  
- **STAC link rot or asset failures** → Flag affected Items, update `abandonment_candidates` registry.  
- **Telemetry merge conflict** → Rerun `telemetry-export.yml` or resolve ledger conflicts manually.  
- **Security scan failure** → Treat as release blocker; triage vulnerabilities before proceeding.  
~~~

---

## ⚖ FAIR+CARE & Governance

Concrete workflow docs must explain how automation upholds FAIR+CARE:

~~~markdown
### FAIR+CARE Governance Matrix

| Principle  | Implementation                                      | Evidence                                  |
|-----------:|-----------------------------------------------------|-------------------------------------------|
| Findable   | Workflow documented with stable ID + metadata       | Front-matter, `docs/workflows/*.yml.md`   |
| Accessible | Artifacts uploaded & retained by policy             | GitHub Actions artifacts, `reports/**`    |
| Interoperable | JSON Schema, STAC/DCAT compatible outputs       | Schema validation logs                    |
| Reusable   | CC-BY docs + versioned configs + manifests          | LICENSE, configs, `manifest.zip`          |
| CARE       | Sensitive flags respected; ethics guardrails applied| FAIR+CARE reports, council decisions      |
~~~

Governance artifacts:

- `reports/audit/github-workflows-ledger.json` — workflow-change ledger.  
- `reports/faircare/faircare_summary.json` — FAIR+CARE outcomes.  

Workflows ingesting or exposing Indigenous or sensitive data should also reference:

- `../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md`.  

---

## 🕰️ Version History

| Version   | Date       | Author        | Summary                                                                 |
|----------:|------------|---------------|-------------------------------------------------------------------------|
| **v11.2.4** | 2025-12-06 | `@kfm-docs`   | Upgraded to KFM-MDP v11.2.4; added full v11 metadata, emoji directory layout, Story Node/Focus Mode guidance, and STAC/DCAT/PROV alignment for workflow docs. |
| v10.2.2   | 2025-11-12 | `@kfm-docs`   | Telemetry refs aligned to v10.2.0; strengthened MCP/FAIR+CARE rules and front-matter constraints. |
| v10.0.0   | 2025-11-10 | `@kfm-docs`   | Added caching, failure modes, governance matrix, and required fields.   |
| v9.9.0    | 2025-11-08 | `@kfm-docs`   | Initial workflow documentation template for KFM CI/CD.                  |

---

<div align="center">

🧩 **Kansas Frontier Matrix — Workflow Documentation Template (v11.2.4)**  
Governed Automation · FAIR+CARE Documentation · Sustainable CI/CD  

[⬅ Back to Templates Index](README.md) ·  
[📘 Markdown Protocol (KFM-MDP v11.2.4)](../standards/kfm_markdown_protocol_v11.2.4.md) ·  
[⚖ Governance Charter](../standards/governance/ROOT-GOVERNANCE.md)

</div>
