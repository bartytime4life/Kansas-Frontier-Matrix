---
title: "🧩 Kansas Frontier Matrix — Workflow Documentation Template (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/templates/workflow_template.md"

version: "v11.2.4"
last_updated: "2025-12-06"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Guide"
header_profile: "standard"
footer_profile: "standard"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

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
This enables **FAIR+CARE-compliant**, **MCP‑DL v6.3‑certified**, and **Diamond⁹ Ω / Crown∞Ω** automation practices across CI/CD, telemetry, governance, and AI pipelines.

<img src="https://img.shields.io/badge/Docs-MCP_v6.3-blue" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.4-purple" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-green" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Governance_Aligned-orange" />
<img src="https://img.shields.io/badge/Status-Template-lightgrey" />

</div>

---

## 📘 Overview

### Template Scope

Use this template to document **any GitHub Actions workflow** (`.github/workflows/*.yml`), typically via:

- `.github/workflows/*.yml` — executable CI/CD workflow configuration.  
- `docs/workflows/*.yml.md` — Markdown documentation derived from this template.

Every workflow documentation file MUST:

1. Include complete YAML front-matter (version, SBOM, manifest, telemetry, governance).  
2. Describe workflow **purpose**, **triggers**, **permissions**, **jobs**, **inputs/outputs**, and **artifacts**.  
3. Explain how the workflow enforces **FAIR+CARE**, **MCP‑DL v6.3**, and internal governance policies.  
4. Include at least one **Mermaid flowchart** for the high-level control flow (≤ 12 nodes, no `classDef`).  
5. Provide a **Version History** aligned with KFM release practices.

### Author Quickstart

1. Copy this file to: `docs/workflows/<workflow-name>.yml.md`.  
2. Update the YAML front-matter (`title`, `path`, `version`, `telemetry_schema`, etc.).  
3. Fill the H3 sections under each H2 heading with **workflow-specific** details.  
4. Ensure the diagram and YAML excerpts match the actual workflow in `.github/workflows/<workflow-name>.yml`.  
5. Open a PR and confirm CI passes: `docs-lint.yml`, `faircare-validate.yml`, `telemetry-export.yml` (and any workflow-specific jobs).

---

## 🗂️ Directory Layout

~~~text
📁 KansasFrontierMatrix/
├── 📁 docs/                                            # All documentation
│   ├── 📁 workflows/                                  # ⚙️ Per-workflow documentation (this template governs)
│   │   📄 README.md                                   # 🧭 CI/CD & governance workflows index
│   │   📄 docs-lint.yml.md                            # 🧪 Docs lint workflow doc
│   │   📄 faircare-validate.yml.md                    # ⚖ FAIR+CARE validation workflow doc
│   │   📄 stac-validate.yml.md                        # 🗂️ STAC/DCAT validation workflow doc
│   │   📄 telemetry-export.yml.md                     # 📈 Telemetry export workflow doc
│   │   📄 ai-train.yml.md                             # 🤖 AI training workflow doc
│   │   📄 ai-explainability.yml.md                    # 🔍 AI explainability workflow doc
│   │   📄 security-supply-chain.yml.md                # 🔒 Supply-chain security workflow doc
│   │   📄 schema-lint.yml.md                          # 📐 Schema lint workflow doc
│   │   📄 workflow_template.yml.md                    # 🧩 Example instantiation of this template (optional)
│   └── 📁 templates/                                  # 📄 Shared documentation templates
│       📄 README.md                                   # Templates index
│       📄 experiment.md                               # 🧪 Experiment template
│       📄 model_card.md                               # 🤖 Model card template
│       📄 sop.md                                      # 🧾 SOP template
│       📄 workflow_template.md                        # 🧩 Workflow doc template (this file)
├── 📁 .github/
│   └── 📁 workflows/                                  # Actual GitHub Actions YAML
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
        📄 sbom.spdx.json                              # 🧬 SBOM
        📄 manifest.zip                                # 📑 Manifest of assets & checksums
        📄 focus-telemetry.json                        # 📈 Unified telemetry ledger
~~~

When instantiating this template:

- Ensure `path` in front-matter matches the actual Markdown location under `docs/workflows/`.  
- Keep emoji usage and comments consistent with KFM‑MDP v11.2.4 to satisfy linters and Focus Mode.

---

## 🧭 Context

Workflow documentation plays three roles:

1. **Mirror of YAML reality**  
   - Precisely describes the behavior of `.github/workflows/<workflow-name>.yml`.  
   - Changes to the YAML must be accompanied by updates to the corresponding doc.

2. **Governed explanation layer**  
   - Clarifies purpose, scope, permissions, risk, and governance rationale.  
   - Documents how the workflow engages with CARE labels, data sensitivity, and sovereignty rules.

3. **Telemetry & provenance anchor**  
   - Connects workflow runs to telemetry (`focus-telemetry.json`) and audit ledgers.  
   - Acts as a `prov:Plan` describing the expected structure of `prov:Activity` instances (workflow runs).

These docs are consumed by:

- Contributors reading CI/CD and governance behavior.  
- Automated tools (Docs lint, FAIR+CARE validators, contract checkers).  
- Story Nodes and Focus Mode when narrating how KFM operates.

---

## 🗺️ Diagrams

Each workflow doc should include at least one **Mermaid flowchart** that mirrors the workflow’s logical stages.

### Diagram Rules

- Type: `flowchart LR` or `flowchart TD`.  
- Max 12 nodes for clarity.  
- No `classDef` or theme overrides.  
- Node labels should match job/step names where practical.

### Example Flowchart Template

~~~mermaid
flowchart LR
  A["Trigger (push / PR / schedule / dispatch)"] --> B["Checkout Repository"]
  B --> C["Setup Environment & Dependencies"]
  C --> D["Run Core Jobs (lint / validate / train / scan)"]
  D --> E["Collect Reports & Artifacts"]
  E --> F["Emit & Merge Telemetry"]
  F --> G["Update Governance / Release State"]
~~~

Replace this with a version tailored to the concrete workflow (job names, critical branches, etc.), and describe any important branches or failure paths in the surrounding text.

---

## 🧠 Story Node & Focus Mode Integration

Workflow docs feed the narrative layer by explaining automation:

- Story Nodes may reference workflows for **“how this system behaves”** narratives, e.g.:  
  `urn:kfm:workflow-doc:stac-validate.yml@v11.2.4`.

- Focus Mode may:
  - Surface a workflow doc when a user asks “What does `docs-lint.yml` do?”  
  - Show high-level purpose, triggers, and governance constraints.  

Author guidance:

- Use short, focused H3 sections (e.g. “Triggers & Scope”, “Permissions”, “Failure Modes & Rollback”).  
- Prefer explicit references (`docs-lint.yml`, `schema-lint.yml`) over pronouns.  
- Include stable identifiers such as workflow file names and job IDs.

Focus Mode:

- ✅ MAY summarize and highlight parts of the doc and link to related standards.  
- ❌ MUST NOT invent new jobs, triggers, or permissions that are not in the YAML or documentation.

---

## 🧪 Validation & CI/CD

This template and all derived workflow docs participate in the KFM docs CI stack:

- **`docs-lint.yml`**
  - Validates:
    - YAML front-matter (presence + basic structure).  
    - Heading order and emoji usage (per H2 registry).  
    - Mermaid syntax and directory layout formatting.

- **`faircare-validate.yml`**
  - Ensures:
    - Governance and CARE fields are present and coherent.  
    - No obvious violations of sovereignty or classification policies in doc metadata.

- **`telemetry-export.yml`**
  - Aggregates:
    - Documentation changes.  
    - Workflow metadata.  
    - Governance and validation results into `focus-telemetry.json`.

Concrete workflow docs should also describe **how their workflows** impact CI/CD:

- Whether they are **required** for PR merges.  
- Which artifacts they generate under `reports/` and `releases/`.  
- How they interact with other workflows (chaining, “needs” relationships).

---

## 📦 Data & Metadata

### Required Front-Matter for Concrete Workflow Docs

All `docs/workflows/*.yml.md` MUST start with:

~~~yaml
---
title: "⚙️ <Human-Friendly Name> — `<workflow-name>.yml`"
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

CI will treat missing or malformed front-matter as a **hard failure**.

### Recommended Metadata Extensions

Concrete docs are encouraged to add:

- `workflow_name`: `<workflow-name>` (without `.yml`).  
- `category`: `lint` · `validate` · `deploy` · `security` · `telemetry` · `ai`.  
- `risk_level`: `low` · `moderate` · `high` (for governance triage).  
- `tags`: `["stac", "dcat", "slsa", "security", "faircare"]` as appropriate.

This data improves telemetry, graph ingestion, and Focus Mode semantic routing.

---

## 🌐 STAC, DCAT & PROV Alignment

While workflow docs are not geospatial datasets, they still participate in the same metadata ecosystem.

- **DCAT**
  - Each workflow doc can be a `dcat:Dataset` with:
    - `dct:title` = front-matter `title`.  
    - `dct:description` = Overview + Purpose summary.  
    - `dct:modified` = `last_updated`.  
    - `dct:license` = `license`.  
  - Distributions:
    - Markdown file (`text/markdown`).  
    - Rendered HTML (if a site exists).

- **STAC**
  - In a documentation collection (e.g., `kfm-docs-workflows`):
    - `id` derived from `semantic_document_id` or `<workflow-name>-vX.Y.Z`.  
    - `properties.datetime` = `last_updated`.  
    - `assets.docs` → link to this file.

- **PROV-O**
  - This template and each derived doc are `prov:Plan`.  
  - Workflow runs are `prov:Activity` instances linked via:
    - `prov:wasInformedBy` (this doc).  
    - `prov:used` (the YAML workflow file, configs).  
    - `prov:generated` (reports, artifacts, telemetry events).

This alignment allows auditors to trace from a workflow run back to the **governing documentation plan**.

---

## 🧱 Architecture

Concrete workflow docs using this template should implement the following H3 structure under **Architecture**.

### Triggers & Scope

Describe **when** the workflow runs and **what** it watches:

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

Provide an accurate excerpt from `.github/workflows/<workflow-name>.yml`:

~~~yaml
name: "Example Workflow — Governed"

on:
  pull_request:
    paths: ["docs/**", "schemas/**"]

permissions:
  contents: read
  id-token: write

jobs:
  validate-docs:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4
      - name: Run docs lint
        run: make lint-docs
~~~

### Jobs Summary

~~~markdown
### Jobs Summary

| Job               | Purpose                                        | Outputs/Artifacts                       |
|------------------:|------------------------------------------------|-----------------------------------------|
| `validate-docs`   | Lint Markdown + schemas                        | `reports/self-validation/docs/*.json`   |
| `validate-stac`   | STAC/DCAT contract validation                  | `reports/self-validation/stac/*.json`   |
| `telemetry-merge` | Merge telemetry fragments into release ledger  | `releases/vX.Y.Z/focus-telemetry.json`  |
~~~

### Inputs & Outputs

~~~markdown
### Inputs & Outputs

| Type      | Field            | Description                                  |
|-----------|------------------|----------------------------------------------|
| **Input** | `dataset_ref`    | STAC/DCAT dataset or contract ID             |
| **Input** | `config_path`    | Path to workflow config (eg. `configs/ci/`)  |
| **Output**| `reports/*.json` | Validation / audit reports                   |
| **Output**| `manifest.zip`   | Release artifact manifest                    |
~~~

### Permissions (Least Privilege)

~~~markdown
### Permissions (Least Privilege)

| Permission        | Reason                                         |
|-------------------|------------------------------------------------|
| `contents: read`  | Required to read workflow and project files    |
| `id-token: write` | Enables OIDC signing / attestations            |
| `packages: write` | Only if publishing artifacts or container images |
~~~

### Caching & Performance

~~~markdown
### Caching & Performance

- Use `actions/cache@v4` for dependencies.  
- Include lockfiles in cache keys (`requirements.lock`, `package-lock.json`, etc.).  
- Document any large downloads (models, tiles) and mitigation (warm caches, prebuilt images).  
~~~

### Failure Modes & Rollback

~~~markdown
### Failure Modes & Rollback

- **Validation failures** → block merge; fix issues and rerun.  
- **Telemetry merge conflicts** → re-run `telemetry-export.yml` or resolve ledger conflicts.  
- **Security scan failures** → treat as release blockers and follow security SOPs.  
- **SLSA / attestation failures** → revoke or delay release until revalidated.  
~~~

---

## ⚖ FAIR+CARE & Governance

Concrete workflow docs must define how automation supports FAIR+CARE:

~~~markdown
### FAIR+CARE Governance Matrix

| Principle  | Implementation                                      | Evidence                                  |
|-----------:|-----------------------------------------------------|-------------------------------------------|
| Findable   | Docs in `docs/workflows/` with stable paths + IDs   | Front-matter, `semantic_document_id`      |
| Accessible | Public or controlled access per classification      | License in front-matter, repo visibility  |
| Interoperable | JSON/CSV/NDJSON outputs; STAC/DCAT-compatible   | Validation logs, schema references        |
| Reusable   | CC-BY docs, versioned configs, SBOM + manifest      | `sbom.spdx.json`, `manifest.zip`          |
| CARE       | Aware of CARE tags, sovereignty; avoids overreach   | FAIR+CARE reports, sovereignty policy refs |
~~~

Governance hooks:

- Reference relevant SOPs (e.g., `docs/sop/governance-faircare-review.md`).  
- Link to audit and FAIR+CARE reports:
  - `reports/audit/github-workflows-ledger.json`  
  - `reports/faircare/faircare_summary.json`  

Workflows that process Indigenous or sensitive data MUST explicitly reference:

- `../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md`  
- Any domain-specific heritage standards that apply.

---

## 🕰️ Version History

| Version    | Date       | Author        | Summary                                                                 |
|-----------:|------------|---------------|-------------------------------------------------------------------------|
| **v11.2.4** | 2025-12-06 | `@kfm-docs`   | Upgraded to KFM‑MDP v11.2.4; added full v11 metadata, emoji-rich directory layout, Story Node / Focus Mode guidance, and STAC/DCAT/PROV alignment for workflow docs. |
| v10.2.2    | 2025-11-12 | `@kfm-docs`   | Aligned telemetry refs to v10.2.0; strengthened MCP/FAIR+CARE rules and front-matter constraints. |
| v10.0.0    | 2025-11-10 | `@kfm-docs`   | Added caching, failure modes, and governance matrix; refined permissions documentation. |
| v9.9.0     | 2025-11-08 | `@kfm-docs`   | Initial workflow documentation template for KFM CI/CD.                   |

---

<div align="center">

🧩 **Kansas Frontier Matrix — Workflow Documentation Template (v11.2.4)**  
Governed Automation · FAIR+CARE Documentation · Sustainable CI/CD  

[⬅ Back to Templates Index](README.md) ·  
[📘 Markdown Protocol (KFM‑MDP v11.2.4)](../standards/kfm_markdown_protocol_v11.2.4.md) ·  
[⚖ Governance Charter](../standards/governance/ROOT-GOVERNANCE.md)

</div>