---
title: "🧪 Kansas Frontier Matrix — Documentation Lint Workflow (`docs-lint.yml`) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/workflows/docs-lint.yml.md"

version: "v11.2.6"
last_updated: "2025-12-11"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
signature_ref: "releases/v11.2.6/signature.sig"
attestation_ref: "releases/v11.2.6/slsa-attestation.json"
sbom_ref: "releases/v11.2.6/sbom.spdx.json"
manifest_ref: "releases/v11.2.6/manifest.zip"
telemetry_ref: "releases/v11.2.6/docs-lint-telemetry.json"
telemetry_schema: "schemas/telemetry/docs-lint-workflow-v11.2.6.json"
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
doc_kind: "Standard"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"

scope:
  domain: "ci-cd-workflows"
  applies_to:
    - ".github/workflows/docs-lint.yml"
    - "docs/**"
    - "**/*.md"
    - "**/*.mdx"

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
sunset_policy: "Superseded by Documentation Lint Workflow v12"

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
  - "docs/workflows/docs-lint.yml.md@v10.2.4"
  - "docs/workflows/docs-lint.yml.md@v10.1.0"
  - "docs/workflows/docs-lint.yml.md@v9.9.0"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/kfm-markdown-protocol-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/kfm-markdown-protocol-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:workflows:docs-lint-yml:v11.2.6"
semantic_document_id: "kfm-workflow-docs-lint-yml-v11.2.6"
event_source_id: "ledger:kfm:doc:workflows:docs-lint-yml:v11.2.6"
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

# 🧪 **Kansas Frontier Matrix — Documentation Lint Workflow (`docs-lint.yml`)**  
`docs/workflows/docs-lint.yml.md`

**Purpose**  
Define the **governed GitHub Actions workflow** that validates all KFM documentation against **KFM‑MDP v11.2.4**, Platinum README rules, **MCP‑DL v6.3**, and **FAIR+CARE** requirements.  
The workflow enforces **front‑matter schemas**, **GFM structure**, **link integrity**, **Mermaid guardrails**, **table width limits**, and **badge/footer ordering**, producing machine‑readable reports and **telemetry** for the governance ledger.

<img src="https://img.shields.io/badge/Docs-MCP--DL_v6.3-blue" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.4-purple" />
<img src="https://img.shields.io/badge/Data-FAIR%2BCARE-gold" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-green" />
<img src="https://img.shields.io/badge/Status-Automated-brightgreen" />

</div>

---

## 📘 Overview

### 1. Workflow Intent

`docs-lint.yml` is the **first line of defense** for high‑integrity, machine‑parseable documentation across the Kansas Frontier Matrix.

It guarantees on every PR and protected‑branch push that:

- ✅ Required **YAML front‑matter** keys and value formats are present and valid.  
- ✅ **GFM structure** conforms to KFM‑MDP v11.2.4:
  - Single H1,
  - Approved emoji‑prefixed H2s,
  - Fenced code blocks with languages and tildes (`~~~`).  
- ✅ **Links** (internal and external) are structurally valid and monitored.  
- ✅ **Style** rules hold:
  - Table row width limits,
  - Heading hierarchy integrity,
  - Mermaid usage constraints.  
- ✅ **Badge + footer** order matches project conventions.  

Findings are exported to `reports/self-validation/docs/lint_summary.json` and summarized into **docs‑lint telemetry**, which is then merged into the KFM‑wide telemetry streams for governance trends.

### 2. Role in the Pipeline

Within the canonical KFM pipeline:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j knowledge graph → API layer → React/MapLibre/Cesium frontend → Story Nodes → Focus Mode

`docs-lint.yml` ensures that **all Markdown input** to catalogs, graph, and Focus Mode is:

- Structurally valid,  
- Semantically tagged (front‑matter),  
- Governance‑ready (license, provenance, FAIR+CARE alignment).

---

## 🗂️ Directory Layout

~~~text
📁 KansasFrontierMatrix/
├── 📚 docs/
│   ├── ⚙️ workflows/
│   │   📄 README.md                           # CI/CD & Governance Workflows index
│   │   📄 docs-lint.yml.md                    # 🧪 Documentation lint workflow spec (this file)
│   └── 📏 standards/
│       📄 kfm_markdown_protocol_v11.2.4.md    # KFM-MDP v11.2.4
│
├── ⚙️ .github/
│   └── 📁 workflows/
│       📄 docs-lint.yml                       # GitHub Actions workflow (docs lint)
│
├── 🛠️ tools/
│   └── 📁 docs/
│       📄 validate_front_matter.py            # Front-matter schema validator
│       📄 validate_mermaid.mjs                # Mermaid usage guardrails
│       📄 audit_tables_and_fences.mjs         # Table width & code fence audit
│       📄 validate_badges_footer.mjs          # Badge ordering & footer checks
│       📄 summarize_docs_lint.mjs             # Aggregates lint JSON → summary
│
├── 📊 reports/
│   └── 📁 self-validation/
│       └── 📁 docs/
│           📄 markdownlint.txt                # Raw markdownlint output
│           📄 frontmatter_validation.json     # Front-matter schema results
│           📄 link_check.log                  # Link checker output
│           📄 mermaid_audit.json              # Mermaid usage analysis
│           📄 format_audit.json               # Tables & fences audit
│           📄 badges_footer_audit.json        # Badge/footer checks
│           📄 lint_summary.json               # Canonical machine-readable summary
│           📄 summary.md                      # Human-readable summary for PRs
│
└── 📦 releases/
    └── 📁 v11.2.6/
        📄 docs-lint-telemetry.json            # Aggregated docs-lint telemetry
        📄 sbom.spdx.json                      # SBOM for docs tooling & dependencies
        📄 manifest.zip                        # Release manifest
~~~

---

## 🧭 Context

### 1. Trigger & Scope

| Trigger            | Paths                                  | Notes                                   |
|-------------------:|----------------------------------------|-----------------------------------------|
| `pull_request`     | `docs/**`, `**/*.md`, `**/*.mdx`       | Required for all PRs touching docs      |
| `push` (protected) | `docs/**`, `**/*.md`, `**/*.mdx`       | Required on `main` and `release/**`     |
| `workflow_dispatch`| —                                      | Manual re‑runs for remediation/hotfixes |

Ignored paths (configurable in linters):

- `node_modules/**`  
- `**/vendor/**`  
- `**/CHANGELOG.md`  
- `**/LICENSE`  
- `**/README-images/**`

### 2. Relationship to Other Workflows

- **Upstream:** none; this workflow acts on repo docs directly.  
- **Peers:** contributes to the same governance & telemetry ecosystem as:
  - `ai-train.yml` (model training),
  - `ai-explainability.yml` (post‑hoc audits),
  - `faircare-validate.yml` (FAIR+CARE validation).
- **Downstream:** its reports are:
  - Ingested into the governance ledger,
  - Used by Focus Mode when summarizing documentation health and coverage.

---

## 🗺️ Diagrams

### 1. High-Level Docs Lint Flow

~~~mermaid
flowchart LR
    A["PR / Push"] --> B["Front-matter & Style Lints"]
    B --> C["Link Check & Mermaid Guardrails"]
    C --> D["Format & Footer Audits"]
    D --> E["Summaries & Artifacts"]
    E --> F["Telemetry Merge → Governance Ledger"]
~~~

---

## 🧠 Story Node & Focus Mode Integration

- Each docs‑lint run is a candidate **Story Node**, such as:

  - `urn:kfm:story-node:docs:lint:<run_id>`

- Story Node content can capture:
  - Number of documents checked,
  - Most common issues,
  - Trend vs. previous runs,
  - Impacted areas (standards vs. guides vs. architecture docs).

**Focus Mode** MAY:

- Surface docs health summaries at:
  - Repo level (e.g., state of all standards),
  - Directory level (e.g., `docs/standards/` vs. `docs/workflows/`).  
- Highlight:
  - Where Markdown violated KFM‑MDP v11.2.4,
  - Which governance or FAIR+CARE rules were triggered.

**Focus Mode MUST NOT**:

- Override or “fix” the authoritative content automatically.  
- Invent lint results; it must rely on stored reports and telemetry.

---

## 🧪 Validation & CI/CD

### 1. Workflow (Conceptual YAML Spec)

~~~yaml
name: "Docs Lint (Governed)"

on:
  pull_request:
    paths: ["docs/**", "**/*.md", "**/*.mdx"]
  push:
    branches: ["main", "release/**"]
    paths: ["docs/**", "**/*.md", "**/*.mdx"]
  workflow_dispatch: {}

permissions:
  contents: read

concurrency:
  group: docs-lint-${{ github.ref }}
  cancel-in-progress: true

jobs:
  lint:
    runs-on: ubuntu-22.04
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: "20"

      - name: Install linters
        run: |
          npm i -g markdownlint-cli@0.39.0 markdown-link-check@3.12.1 remark-cli@11 \
            @github-docs/mdlinks@latest @stoplight/spectral-cli@6
          pipx install yq
          pipx install jsonschema

      - name: Run markdownlint (KFM & Platinum rules)
        run: |
          mkdir -p reports/self-validation/docs
          markdownlint "**/*.md" -c .github/linters/markdownlint.json \
            --ignore "node_modules/**" \
            --ignore "**/CHANGELOG.md" \
            --output reports/self-validation/docs/markdownlint.txt || true

      - name: Validate front-matter schema (KFM-MDP + MCP-DL)
        run: |
          python tools/docs/validate_front_matter.py \
            --schema docs/standards/markdown_frontmatter.schema.json \
            --glob "**/*.md" \
            --out reports/self-validation/docs/frontmatter_validation.json

      - name: Link check (internal & external)
        run: |
          npx markdown-link-check -q -c .github/linters/mlc.config.json \
            -p -r -v $(git ls-files "*.md") \
            | tee reports/self-validation/docs/link_check.log || true

      - name: Mermaid guardrails
        run: |
          node tools/docs/validate_mermaid.mjs \
            --maxPerSection=1 \
            --types "flowchart" "timeline" \
            --paths "docs/**" > reports/self-validation/docs/mermaid_audit.json

      - name: Table width & code fence audit
        run: |
          node tools/docs/audit_tables_and_fences.mjs \
            --maxWidth=100 \
            --requireLang=true \
            --paths "docs/**" > reports/self-validation/docs/format_audit.json

      - name: Badge order & footer check
        run: |
          node tools/docs/validate_badges_footer.mjs \
            --paths "docs/**" \
            --out reports/self-validation/docs/badges_footer_audit.json

      - name: Summarize results
        run: |
          node tools/docs/summarize_docs_lint.mjs \
            --inputs "reports/self-validation/docs/*.json" \
            --markdown "reports/self-validation/docs/summary.md" \
            --json "reports/self-validation/docs/lint_summary.json"

      - name: Upload artifacts
        uses: actions/upload-artifact@v4
        with:
          name: docs_lint_reports
          path: reports/self-validation/docs/

      - name: Emit telemetry
        run: |
          python scripts/emit_telemetry.py \
            --kind docs_lint \
            --summary reports/self-validation/docs/lint_summary.json \
            --out docs_lint_telemetry.json

      - name: Merge telemetry → unified log
        run: |
          python scripts/merge_telemetry.py \
            --in  docs_lint_telemetry.json \
            --dest releases/v11.2.6/docs-lint-telemetry.json
~~~

### 2. Validation Rules (Conceptual)

#### Front-matter

Required keys (for standards & workflow docs), aligned with KFM‑MDP:

| Key                | Rule                                                        |
|--------------------|-------------------------------------------------------------|
| `title`            | Emoji prefix + descriptive title                            |
| `path`             | Repo-relative, matches actual file location                 |
| `version`          | SemVer string (e.g., `v11.2.6`)                             |
| `last_updated`     | ISO‑8601 date (`YYYY-MM-DD`)                                |
| `review_cycle`     | Known enum (e.g., `Continuous · Autonomous`)                |
| `commit_sha`       | Git hash or `<latest-commit-hash>` placeholder              |
| `license`          | SPDX or project license label                               |
| `mcp_version`      | Must reflect MCP-DL version (e.g., `MCP-DL v6.3`)           |
| `governance_ref`   | Valid relative path                                         |
| `telemetry_ref`    | Valid relative path                                         |
| `telemetry_schema` | Valid relative path                                         |

Missing or malformed keys **fail** the workflow.

#### Structure & Style

- Single **H1** per file, typically in a centered header block.  
- H2 headings drawn from the **approved registry** in KFM‑MDP (Overview, Directory Layout, etc.).  
- Tables:
  - Minimum 3 columns,
  - Each rendered row ≤ 100 characters (approx).  
- Code fences:
  - Use tildes (`~~~`) in standards,
  - Must declare language where applicable (`json`, `yaml`, `bash`, `mermaid`, `text`, ...).  
- Mermaid:
  - Only allowed profiles: `flowchart` and `timeline`,
  - At most one diagram per section (for standards),
  - Must parse without errors.  

#### Links

- Internal links must resolve within the repo (checked using `git ls-files`).  
- External links are checked with retry/backoff; soft failures are recorded in logs.  
- Anchor links must match GitHub’s generated heading IDs.

---

## 📦 Data & Metadata

### 1. Lint Artifacts

Primary outputs for each run:

- `reports/self-validation/docs/markdownlint.txt`  
- `reports/self-validation/docs/frontmatter_validation.json`  
- `reports/self-validation/docs/link_check.log`  
- `reports/self-validation/docs/mermaid_audit.json`  
- `reports/self-validation/docs/format_audit.json`  
- `reports/self-validation/docs/badges_footer_audit.json`  
- `reports/self-validation/docs/lint_summary.json` (canonical JSON summary)  
- `reports/self-validation/docs/summary.md` (human‑readable summary)

These are uploaded as CI artifacts and may also be harvested into catalogs/graphs.

### 2. Telemetry Records

Each run contributes to `releases/v11.2.6/docs-lint-telemetry.json`. Typical fields:

~~~json
{
  "workflow": "docs-lint",
  "run_id": "docs-lint_2025-12-11T17-30-00Z",
  "docs_checked": 286,
  "errors": 3,
  "warnings": 19,
  "frontmatter_failures": 1,
  "link_failures": 2,
  "mermaid_issues": 0,
  "workflow_duration_sec": 92,
  "energy_wh": 2.3,
  "carbon_gco2e": 0.0009,
  "timestamp": "2025-12-11T17:31:32Z"
}
~~~

Schema specifics live in `schemas/telemetry/docs-lint-workflow-v11.2.6.json`.

---

## 🌐 STAC, DCAT & PROV Alignment

### 1. PROV-O View

For each run:

- **Entities**:
  - `ex:DocsLintReport_<run_id>` (lint_summary + supporting files),
  - Individual docs as `prov:Entity` (already modeled elsewhere).
- **Activity**:
  - `ex:DocsLintRun_<run_id>` (this CI run).
- **Agents**:
  - `ex:KFM_CI_Bot` (`prov:SoftwareAgent`),
  - Documentation maintainers (`prov:Person` / `prov:Organization`).

Relations:

- `ex:DocsLintRun_<run_id> prov:used` → repo state (commit SHA).  
- `ex:DocsLintReport_<run_id> prov:wasGeneratedBy ex:DocsLintRun_<run_id>`.  
- `ex:DocsLintRun_<run_id> prov:wasAssociatedWith ex:KFM_CI_Bot`.

### 2. DCAT

Treat lint reports as a `dcat:Dataset` series:

- `dct:title`: "KFM Documentation Lint Reports"  
- `dct:description`: "Automated lint and governance results for KFM Markdown documentation."  
- `dcat:distribution`:
  - `lint_summary.json` (JSON),
  - `summary.md` (Markdown),
  - Optionally compressed bundles of raw logs.

Per‑run datasets may be identified by `run_id`.

### 3. STAC

For environments that store CI results alongside other datasets:

- A `kfm-ci-docs` STAC Collection can hold lint runs as Items:
  - `id`: `docs-lint-<run_id>`
  - `properties.datetime`: run completion time.
  - `assets`:
    - `lint-summary` → `lint_summary.json`
    - `human-summary` → `summary.md`

As documentation is non‑spatial, `geometry` may be `null` and `bbox` omitted.

---

## 🧱 Architecture

### 1. Module Boundaries

- **Workflow orchestration**: `.github/workflows/docs-lint.yml`  
- **Lint tooling**: `tools/docs/*.py` / `*.mjs`  
- **Docs**: This spec (`docs/workflows/docs-lint.yml.md`) plus KFM‑MDP and related standards.  

The workflow:

- Calls reusable scripts (no inline complex logic in YAML).  
- Does not directly know about STAC/DCAT/PROV; instead, it writes well‑shaped JSON that cataloging pipelines can ingest.

### 2. Determinism & Reproducibility

- Config for lint rules lives in:
  - `.github/linters/markdownlint.json`,
  - `.github/linters/mlc.config.json`,
  - Script‑specific config files under `tools/docs/`.  
- Given the same commit, configs, and environment, the workflow produces identical reports.

---

## ⚖ FAIR+CARE & Governance

### 1. FAIR

| Aspect       | Implementation                                                  |
|--------------|-----------------------------------------------------------------|
| Findable     | Stable artifact paths, structured front‑matter, catalog records |
| Accessible   | Public CI artifacts and logs where policy allows               |
| Interoperable| JSON summaries, DCAT‑style references, PROV alignment          |
| Reusable     | CC‑BY docs; deterministic, reproducible lints                  |

### 2. CARE

- **Collective Benefit**: Ensures all docs meet governance expectations before merge.  
- **Authority to Control**: Governance refs embedded in front‑matter; lint checks for their presence.  
- **Responsibility**: Failing lint results block merges until fixed, encouraging responsible documentation.  
- **Ethics**: Lints can evolve to flag potential ethical issues in narrative (e.g., harmful terminology) according to FAIR+CARE guidelines.

### 3. Governance Hooks

- This workflow is a **required check** for protected branches.  
- Governance dashboards can query telemetry and lint histories to:
  - Identify areas of chronic non‑compliance,
  - Prioritize documentation refactors or training.

---

## 🕰️ Version History

| Version    | Date       | Author        | Summary                                                                                                               |
|-----------:|------------|--------------|-----------------------------------------------------------------------------------------------------------------------|
| **v11.2.6** | 2025-12-11 | `@kfm-docs`  | Aligned to KFM v11.2.6; updated release and telemetry paths to `v11.2.6`, adopted emoji root directory layout, and extended footer navigation. |
| v11.2.4   | 2025-12-06 | `@kfm-docs`  | Updated to align with KFM‑MDP v11.2.4; expanded front‑matter; added STAC/DCAT/PROV alignment and Story Node hooks; introduced dedicated `docs-lint-telemetry.json`. |
| v10.2.4   | 2025-11-12 | `@kfm-docs`  | Upgraded to telemetry schema v3; unified artifact paths under `reports/self-validation/docs/`; strengthened table/code‑fence audits. |
| v10.1.0   | 2025-11-10 | `@kfm-docs`  | Introduced telemetry v2; improved Mermaid guardrails; migrated to `upload-artifact@v4`.                               |
| v9.9.0    | 2025-11-08 | `@kfm-docs`  | Initial governed docs‑lint workflow documentation.                                                                     |

---

<div align="center">

🧪 **Kansas Frontier Matrix — Documentation Lint Workflow (`docs-lint.yml`) · v11.2.6**  
Documentation Excellence · FAIR+CARE Governance · Sustainable CI/CD  

<img src="https://img.shields.io/badge/Docs-MCP--DL_v6.3-blue" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.4-purple" />
<img src="https://img.shields.io/badge/Docs--Lint-v11.2.6-informational" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-green" />

[⬅ Back to Workflows Index](./README.md) ·  
[📘 Docs Root](../README.md) ·  
[📚 Glossary](../glossary.md) ·  
[📐 Markdown Protocol (KFM-MDP v11.2.4)](../standards/kfm_markdown_protocol_v11.2.4.md) ·  
[⚖ Governance Charter](../standards/governance/ROOT-GOVERNANCE.md) ·  
[🤝 FAIR+CARE Guide](../standards/faircare/FAIRCARE-GUIDE.md) ·  
[🪶 Indigenous Data Protection](../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

  
© 2025 Kansas Frontier Matrix — CC-BY 4.0 for this document  
MCP-DL v6.3 · KFM-MDP v11.2.4 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  

</div>
