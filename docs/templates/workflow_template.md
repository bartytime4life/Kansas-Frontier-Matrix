---
title: "🧩 Kansas Frontier Matrix — Workflow Documentation Template (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/templates/workflow_template.md"

version: "v11.2.6"
last_updated: "2025-12-11"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
signature_ref: "../../releases/v11.2.6/signature.sig"
attestation_ref: "../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../releases/v11.2.6/docs-workflow-template-telemetry.json"
telemetry_schema: "../../schemas/telemetry/workflows/template-v11.2.6.json"
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
  - "docs/templates/workflow_template.md@v11.2.4"
  - "docs/templates/workflow_template.md@v10.2.2"
  - "docs/templates/workflow_template.md@v10.0.0"
  - "docs/templates/workflow_template.md@v9.9.0"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "../../schemas/json/kfm-workflow-doc-template-v11.2.6.schema.json"
shape_schema_ref: "../../schemas/shacl/kfm-workflow-doc-template-v11.2.6-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:templates:workflow-doc:v11.2.6"
semantic_document_id: "kfm-workflow-doc-template-v11.2.6"
event_source_id: "ledger:kfm:doc:templates:workflow-doc:v11.2.6"
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
This enables **FAIR+CARE-compliant**, **MCP-DL v6.3-certified**, and **Diamond⁹ Ω / Crown∞Ω** automation practices throughout CI/CD, telemetry, governance, and AI pipelines, aligned with **KFM‑MDP v11.2.6**.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![KFM‑MDP v11.2.6](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.6-purple)]()  
[![License · CC‑BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Governance_Aligned-orange)]()  
[![Status · Template](https://img.shields.io/badge/Status-Template-lightgrey)]()

</div>

---

## 📘 Overview

### 1. Template Scope

Use this template to document **any workflow `.yml` file**, typically located under:

- `.github/workflows/` — actual CI/CD configuration.  
- `docs/workflows/` — Markdown documentation `*.yml.md` files generated from this template.

Each workflow documentation file must:

1. Contain complete **YAML front-matter** (version, SBOM, manifest, telemetry schema, governance refs).  
2. Describe workflow **purpose**, **trigger conditions**, **permissions**, **jobs**, **inputs/outputs**, and **artifacts**.  
3. Declare how the workflow enforces **FAIR+CARE**, **MCP-DL v6.3**, and internal governance policies.  
4. Include a **Mermaid diagram** illustrating workflow logic (≤ 12 nodes, no custom `classDef`).  
5. Provide a **Version History** table aligned with KFM releases.  

All workflow docs must be compatible with the core KFM pipeline:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j → API → React/MapLibre/Cesium → Story Nodes → Focus Mode

so CI/CD automation can be traced from commit to catalog to graph to narrative.

### 2. Author Quickstart

When documenting a workflow (e.g., `stac-validate.yml`):

1. Copy this template to `docs/workflows/stac-validate.yml.md`.  
2. Update the front-matter (`title`, `path`, `version`, `telemetry_schema`, etc.).  
3. Fill in the sections under the H2 headings below, using H3 subsections where indicated.  
4. Ensure the Mermaid diagram matches the actual YAML definition.  
5. Open a PR and confirm CI passes: `docs-lint`, `faircare-validate`, and `telemetry-export`.  

---

## 🗂️ Directory Layout

Workflow docs and template live in the `docs/` subtree:

~~~text
📁 KansasFrontierMatrix/
  📁 docs/                                 # All documentation
    📁 workflows/                          # ⚙️ Workflow documentation (per CI job)
      📄 README.md                         # 🧭 CI/CD & governance workflows index
      📄 docs-lint.yml.md                  # 🧪 Docs lint workflow doc
      📄 faircare-validate.yml.md          # ⚖ FAIR+CARE validation workflow doc
      📄 stac-validate.yml.md              # 🗂️ STAC/DCAT validation workflow doc
      📄 telemetry-export.yml.md           # 📈 Telemetry export workflow doc
      📄 ai-train.yml.md                   # 🤖 AI training workflow doc
      📄 ai-explainability.yml.md          # 🔍 AI explainability workflow doc
      📄 security-supply-chain.yml.md      # 🔒 Supply-chain security workflow doc
      📄 schema-lint.yml.md                # 📐 Schema lint workflow doc
      📄 workflow_template.md              # 🧩 Workflow documentation template (instantiated copy)
    📁 templates/                          # 📄 Shared documentation templates
      📄 README.md                         # Templates index
      📄 kfm-markdown-template.md          # Core markdown template
      📄 experiment.md                     # 🧪 Experiment template
      📄 model_card.md                     # 🤖 Model card template
      📄 sop.md                            # 🧾 SOP template
      📄 workflow_template.md              # 🧩 Workflow doc template (this file)
  📁 .github/
    📁 workflows/                          # Actual GitHub Actions YAML
      📄 docs-lint.yml                     # 📏 Docs lint workflow
      📄 faircare-validate.yml             # ⚖ FAIR+CARE validation workflow
      📄 stac-validate.yml                 # 🗂️ STAC/DCAT validation workflow
      📄 telemetry-export.yml              # 📈 Telemetry aggregation workflow
      📄 ai-train.yml                      # 🤖 AI training workflow
      📄 ai-explainability.yml             # 🔍 Explainability workflow
      📄 security-supply-chain.yml         # 🔒 Supply-chain security workflow
      📄 schema-lint.yml                   # 📐 Schema lint workflow
  📁 releases/
    📁 v11.2.6/                            # 📦 Release artifacts & telemetry
      🧾 sbom.spdx.json                    # 🧬 SBOM
      🧾 manifest.zip                      # 📑 Manifest of assets & checksums
      🧾 focus-telemetry.json              # 📈 Unified telemetry ledger
~~~

When instantiating this template:

- Ensure the `path` in front-matter matches the actual location in `docs/workflows/`.  
- Keep emojis and comments consistent with the **KFM‑MDP v11.2.6 directory layout rules**.

---

## 🧭 Context

Workflow documentation bridges:

- **YAML reality** in `.github/workflows/*.yml`.  
- **Governed narrative** in `docs/workflows/*.yml.md`.  
- **Telemetry and governance** in `releases/*/focus-telemetry.json` and audit ledgers.

Each workflow doc should answer:

- *What* the workflow does (purpose, scope, jobs).  
- *When* it runs (triggers).  
- *How* it runs (permissions, steps, environment).  
- *Why* it exists (governance & FAIR+CARE rationale).  

Workflow docs:

- Are treated as **plans** (`prov:Plan`, CIDOC `E29`) in the KFM provenance graph.  
- Are used by **Story Nodes** and **Focus Mode** to explain automation behavior.  
- Must remain synchronized with the actual `.yml` definition (drift is a governance issue).

---

## 🗺️ Diagrams

Each workflow doc should include a **Mermaid flowchart** representing the core logic.

### Diagram Rules

- Diagram type: `flowchart LR` or `flowchart TD` only (per `mermaid-flowchart-v1`).  
- At most **12 nodes** to keep diagrams readable.  
- Labels quoted; no custom `classDef`.  
- Use a single diagram for straightforward workflows, or one diagram per major section for very complex ones (still keeping total nodes reasonable).

### Example Diagram Template

~~~mermaid
flowchart LR
  A["Trigger (push / PR / schedule)"] --> B["Checkout Repository"]
  B --> C["Setup Environment & Dependencies"]
  C --> D["Run Core Jobs (lint / validate / train)"]
  D --> E["Collect Reports & Artifacts"]
  E --> F["Emit & Merge Telemetry"]
  F --> G["Update Governance / Release State"]
~~~

The diagram must align with the **YAML excerpt** under **🧱 Architecture**.

---

## 🧠 Story Node & Focus Mode Integration

Workflow documentation is surfaced by **Focus Mode** when users ask:

- “How does CI enforce FAIR+CARE?”  
- “What happens when I push STAC changes?”  
- “Which workflow logs energy and carbon telemetry?”

To support this:

- Use **clear, small H3 sections** per concept (Triggers, Jobs, Inputs/Outputs, etc.).  
- Maintain consistent naming (`name:` in YAML ↔ doc title + headings).  
- Reference concrete workflow IDs and artifact paths (e.g., `reports/self-validation/docs/lint_summary.json`).  

Focus Mode:

- ✅ **MAY** summarize sections and highlight key governance features.  
- ❌ **MUST NOT** invent jobs, permissions, or triggers that aren’t in the YAML or the doc.

---

## 🧪 Validation & CI/CD

This template itself is validated via:

- `docs-lint.yml` (front-matter, headings, Mermaid syntax, directory layout section).  
- `faircare-validate.yml` (ethics + governance alignment).  
- `telemetry-export.yml` (recording template usage and changes).

Concrete workflow docs must describe:

- How their workflow participates in CI chains (e.g., gating merges, releasing artifacts).  
- Which other workflows they depend on (e.g., telemetry collectors, security scans).  
- What **hard gates** exist (e.g., fail on contract violations, fail on PII detection).

---

## 📦 Data & Metadata

### 1. Required Front-Matter for Concrete Workflow Docs

Instantiated workflow docs must start with:

~~~yaml
---
title: "⚙️ <Human-Friendly Name> — `<workflow-name>.yml`"
path: "docs/workflows/<workflow-name>.yml.md"

version: "vX.Y.Z"
last_updated: "YYYY-MM-DD"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Workflow Doc"
header_profile: "standard"
footer_profile: "standard"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

semantic_document_id: "kfm-workflow-doc-<workflow-name>-vX.Y.Z"
doc_uuid: "urn:kfm:doc:workflow:<workflow-name>:vX.Y.Z"
event_source_id: "ledger:docs/workflows/<workflow-name>.yml.md"
immutability_status: "version-pinned"

sbom_ref: "releases/vX.Y.Z/sbom.spdx.json"
manifest_ref: "releases/vX.Y.Z/manifest.zip"
telemetry_ref: "releases/vX.Y.Z/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/workflows/<workflow-name>-vX.json"

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
---
~~~

CI will **reject** docs with:

- Missing front-matter.  
- Mismatched `path` vs. actual location.  
- Incorrect or missing telemetry refs/schemas.

### 2. Required Sections (H3) in Concrete Workflow Docs

Under the H2 headings of this template, concrete docs should include:

- **Under 📘 Overview**
  - `### Purpose` — high-level description.  

- **Under 🧱 Architecture**
  - `### Triggers & Scope`  
  - `### Workflow Definition (YAML Excerpt)`  
  - `### Jobs Summary`  
  - `### Inputs & Outputs`  
  - `### Permissions (Least Privilege)`  
  - `### Caching & Performance`  
  - `### Failure Modes & Rollback`  

- **Under ⚖ FAIR+CARE & Governance**
  - `### FAIR+CARE Governance Matrix`  

This structure keeps docs **Focus-Mode-friendly** and **machine-parseable**.

---

## 🌐 STAC, DCAT & PROV Alignment

Workflow docs themselves can be treated as catalog/provenance entities:

- **DCAT**  
  - Documented as `dcat:Dataset` or `dcat:CatalogRecord` with distributions for:
    - Raw Markdown (`text/markdown`).  
    - Rendered HTML (if site generator is used).  

- **STAC**  
  - Included in a documentation-oriented Collection (e.g., `kfm-docs-workflows`) with:
    - `id` = semantic document ID.  
    - `properties.datetime` = `last_updated`.  
    - `assets.doc` → canonical Markdown source.  

- **PROV-O**  
  - Workflow doc is a `prov:Plan`.  
  - Workflow run is a `prov:Activity` with:
    - `prov:used` (source code, configs).  
    - `prov:wasAssociatedWith` (GitHub Action runner, maintainers).  
    - `prov:generated` (artifacts, telemetry events).  

Concrete docs may optionally include a small note such as:

> This workflow is modeled as `prov:Plan` `urn:kfm:plan:workflow:<workflow-name>@vX.Y.Z` and  
> its executions as `prov:Activity` instances linked via `prov:wasInformedBy`.

---

## 🧱 Architecture

This section describes **what each concrete workflow doc must contain**.

### 🧩 Triggers & Scope

Document triggers and affected paths:

~~~markdown
### 🧩 Triggers & Scope

| Trigger             | Paths                           | Notes                                  |
|---------------------|---------------------------------|----------------------------------------|
| `push`              | `src/**`, `data/**`             | Restricted to `main` / `release/**`    |
| `pull_request`      | `docs/**`, `schemas/**`         | Blocks merges on failure               |
| `workflow_dispatch` | —                               | Manual execution                       |
| `schedule`          | `0 3 * * *`                     | Nightly governance or telemetry runs   |
~~~

### ⚙️ Workflow Definition (YAML Excerpt)

Include a minimal but accurate YAML excerpt:

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

### 🧩 Jobs Summary

Summarize jobs and responsibilities:

~~~markdown
### 🧩 Jobs Summary

| Job        | Purpose                                  | Outputs/Artifacts                       |
|------------|------------------------------------------|-----------------------------------------|
| `build`    | Compile or validate project components   | Binaries, bundle manifests              |
| `validate` | Run linting, schema checks, FAIR+CARE    | `reports/**.json`, logs                 |
| `deploy`   | Publish artifacts to releases/registries | `releases/vX.Y.Z/manifest.zip`         |
~~~

### 📊 Inputs & Outputs

Document inputs (dispatch params, environment) and outputs (artifacts, telemetry):

~~~markdown
### 📊 Inputs & Outputs

| Type      | Field           | Description                                 |
|-----------|-----------------|---------------------------------------------|
| **Input** | `dataset_ref`   | STAC/DCAT dataset or contract ID           |
| **Input** | `config_path`   | Relative path to workflow configuration     |
| **Output**| `reports/validation.json` | Contract or metadata validation report |
| **Output**| `releases/vX.Y.Z/focus-telemetry.json` | Global telemetry ledger entry   |
~~~

### 🔐 Permissions (Least Privilege)

List each permission and justification:

~~~markdown
### 🔐 Permissions (Least Privilege)

| Permission        | Reason                                         |
|-------------------|-----------------------------------------------|
| `contents: read`  | Required to inspect repository files           |
| `id-token: write` | Enables OIDC-based signing / attestations      |
| `packages: write` | Only if workflow uploads packages to registry  |
~~~

Workflows granting more permissions than required must document and justify each one.

### ♻️ Caching & Performance

Describe caching strategy:

~~~markdown
### ♻️ Caching & Performance

- Use `actions/cache@v4` for dependency caches.  
- Cache keys should incorporate lockfiles (e.g., `requirements.lock`, `poetry.lock`, `package-lock.json`).  
- Typical speedup: **40–70%** for repeated runs on active branches.  
~~~

### 🧯 Failure Modes & Rollback

Document expected failure cases and operator actions:

~~~markdown
### 🧯 Failure Modes & Rollback

- **Missing contract fields** → Fail validation job, block merge; fix schema or data and rerun.  
- **STAC link rot or asset failure** → Flag invalid Items, update `abandonment_candidates` registry.  
- **Telemetry merge conflict** → Rerun `telemetry-export.yml` or resolve ledger conflicts.  
- **Security scan failure** → Treat as release blocker; triage vulnerabilities before proceeding.  
~~~

---

## ⚖ FAIR+CARE & Governance

Concrete workflow docs must include a governance summary, typically as:

~~~markdown
### ⚖ FAIR+CARE Governance Matrix

| Principle  | Implementation                                      | Evidence                                  |
|-----------:|-----------------------------------------------------|-------------------------------------------|
| Findable   | Workflow documented with stable ID + metadata       | Front-matter, `docs/workflows/*.yml.md`   |
| Accessible | Artifacts uploaded & retained                       | GitHub Actions artifacts, `reports/**`    |
| Interoperable | JSON Schema, STAC/DCAT compatible outputs       | Schema validation logs                    |
| Reusable   | CC-BY docs + versioned configs + manifests          | LICENSE, configs, `manifest.zip`          |
| CARE       | Sensitive flags respected; ethics guardrails applied| FAIR+CARE reports, council decisions      |
~~~

Governance artifacts:

- `reports/audit/github-workflows-ledger.json` — workflow changes ledger.  
- `reports/faircare/faircare_summary.json` — FAIR+CARE status.  

Workflows that directly touch sensitive or Indigenous data must also reference:

- `docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md`.  

---

## 🕰️ Version History

| Version   | Date       | Author        | Summary                                                                                                                  |
|----------:|-----------:|--------------|--------------------------------------------------------------------------------------------------------------------------|
| v11.2.6   | 2025-12-11 | `@kfm-docs`  | Updated to KFM‑MDP v11.2.6; aligned release and schema paths to v11.2.6; synchronized with Core Markdown & Templates index; clarified pipeline alignment and Story Node integration. |
| v11.2.4   | 2025-12-06 | `@kfm-docs`  | Upgraded to KFM‑MDP v11.2.4; added full v11 metadata, emoji-rich directory layout, Story Node / Focus Mode guidance, and STAC/DCAT/PROV alignment. |
| v10.2.2   | 2025-11-12 | `@kfm-docs`  | Telemetry refs aligned to v10.2.0; strengthened MCP/FAIR+CARE rules and front-matter constraints.                        |
| v10.0.0   | 2025-11-10 | `@kfm-docs`  | Added caching, failure modes, and governance matrix; refined permissions documentation.                                 |
| v9.9.0    | 2025-11-08 | `@kfm-docs`  | Initial workflow documentation template for KFM CI/CD.                                                                   |

---

<div align="center">

🧩 **Kansas Frontier Matrix — Workflow Documentation Template (v11.2.6)**  
Governed Automation · FAIR+CARE Documentation · Sustainable CI/CD  

[⬅ Back to Templates Index](README.md) ·  
[📘 Markdown Protocol (KFM‑MDP v11.2.6)](../standards/kfm_markdown_protocol_v11.2.6.md) ·  
[⚖ Governance Charter](../standards/governance/ROOT-GOVERNANCE.md)

</div>