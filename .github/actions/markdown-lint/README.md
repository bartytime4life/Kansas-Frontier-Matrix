---
title: "🧂 KFM v11.2.2 — Markdown & Front‑Matter Lint Composite Action"
path: ".github/actions/markdown-lint/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Infrastructure & Provenance Committee"
content_stability: "stable"
backward_compatibility: "Aligned with v10.x → v11.x CI/CD model"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"
attestation_ref: "../../../releases/v11.2.2/slsa-attestation.json"
signature_ref: "../../../releases/v11.2.2/signature.sig"
telemetry_ref: "../../../releases/v11.2.2/github-infra-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/actions-library-v11.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Component Guide"
intent: "github-composite-actions"
role: "ci-cd-infrastructure"
category: "CI/CD · Automation · Governance · Reusability"

classification: "Public"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false

care_label: "Collective Benefit · Authority to Control · Responsibility · Ethics"
fair_category: "F1-A1-I1-R1"

data_steward: "KFM Infrastructure & Provenance Committee"

provenance_chain:
  - ".github/actions/markdown-lint/README.md@v11.2.2"

prov_profile: "PROV-O Plan + KFM Governance Extensions"
openlineage_profile: "OpenLineage v2.5 (CI/CD events)"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../schemas/json/actions-markdown-lint-readme-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/actions-markdown-lint-readme-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:github-actions-markdown-lint:v11.2.2"
semantic_document_id: "kfm-doc-github-actions-markdown-lint"
event_source_id: "ledger:.github/actions/markdown-lint/README.md"

immutability_status: "mutable-plan"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🧪 Validation & CI/CD"
    - "🧰 Rule Set & Checks"
    - "📦 Data & Metadata Contract"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "footer-check"
  - "accessibility-check"
  - "provenance-check"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev · staging · production"

branding_registry:
  standard: "Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence"
  architecture: "Designed for Longevity · Governed for Integrity"
  analysis: "CI-Driven · Evidence-Led · FAIR+CARE Grounded"
  data-spec: "Open Pipelines × Responsible Automation"
  pipeline: "Deterministic CI/CD · Explainable Workflows · Open Provenance"
  telemetry: "Transparent Systems · Ethical Metrics · Sustainable Intelligence"
  graph: "Semantics × Provenance × Automation Intelligence"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_version_history: true
requires_directory_layout_section: false
requires_governance_links_in_footer: true

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

deprecated_fields:
  - "old_markdown_lint_action_readme_v10.4"
---

<div align="center">

# 🧂 **KFM v11 — Markdown & Front‑Matter Lint Composite Action**  
`.github/actions/markdown-lint/README.md`

**Purpose**  
Provide a **governed, deterministic composite GitHub Action** for **Markdown + YAML front‑matter linting**  
according to **KFM‑MDP v11.2.2**, ensuring docs are **schema‑aligned**, **accessible**, and **provenance‑safe**  
before they enter the KFM knowledge graph and catalogs.

[![KFM-MDP v11.2.2](https://img.shields.io/badge/Markdown-KFM--MDP_v11.2.2-blue)](../../../docs/standards/kfm_markdown_protocol_v11.2.2.md)
· [![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Enforced-gold)](../../../docs/standards/faircare/FAIRCARE-GUIDE.md)
· [![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen)]()
· [![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../LICENSE)

</div>

---

## 📘 Overview

The **`markdown-lint` composite action** is the **single entry‑point** for validating all KFM Markdown:

- Ensures **front‑matter** conforms to **KFM‑MDP v11.2.2** and its JSON Schema.  
- Enforces **heading registry** rules and required sections (e.g., Version History, Governance footer).  
- Guards against **broken fences, malformed boxes, and unsafe HTML**.  
- Produces **machine‑readable reports** for CI dashboards, provenance, and audits.

This action is intended to be used by:

- `kfm-ci.yml` on **every PR** touching `*.md`.  
- `docs_validate.yml` for **repository‑wide documentation sweeps**.  
- **Release workflows** to validate docs associated with tagged versions.

Implementation lives in:

- Composite action: `.github/actions/markdown-lint/action.yml`  
- Rule configuration (recommended): `.github/linters/markdown-lint.config.*`  
- Governing spec: `docs/standards/kfm_markdown_protocol_v11.2.2.md`

---

## 🧪 Validation & CI/CD

This composite action is **contract‑driven**: workflows MAY evolve, but the **behavioural contract** below  
MUST remain stable across minor versions of KFM v11.

### 1. Typical Usage

Add to a workflow (e.g. `.github/workflows/kfm-ci.yml`):

```yaml
- name: ✅ Lint Markdown & front-matter (KFM-MDP v11.2.2)
  uses: ./.github/actions/markdown-lint
  with:
    paths: |
      docs/**/*.md
      README.md
    mode: changed
    fail_level: error
    report_path: artifacts/markdown/markdown-lint-report.json
```

**Recommended workflows**

- **CI (PR)**  
  - `mode: changed` + `fail_level: error`  
  - Only changed Markdown files; hard‑fail on errors, allow warnings.

- **Nightly / pre‑release**  
  - `mode: all` + `fail_level: warning`  
  - Full repo sweep; fail on warnings to keep long‑lived docs clean.

### 2. Pipeline Stages (Normative)

The composite action MUST, at minimum, perform the following stages **in order**:

1. **Target discovery**  
   - Resolve `paths` against `working_directory`.  
   - If `mode: changed`, intersect with `git diff` against the base ref.  
   - Fail if no Markdown files are discovered (to catch mis‑configured paths).

2. **Front‑matter extraction**  
   - For each file:
     - Extract the **first YAML front‑matter block** (`--- … ---`) at top‑of‑file (if present).  
     - Disallow **multiple** front‑matter blocks.  
     - Disallow non‑UTF‑8 encodings and leading BOM markers.

3. **Front‑matter schema validation**  
   - Validate against `markdown_protocol_version`’s JSON schema (see `json_schema_ref`).  
   - Enforce (at minimum):
     - Required keys: `title`, `path`, `version`, `last_updated`, `doc_kind`, `status`, `doc_uuid`.  
     - Single front‑matter block per file.  
     - No extra, deprecated keys unless explicitly whitelisted.  
   - Map failures to machine‑readable error codes (e.g., `KFM-MDP-E001`).

4. **Markdown linting**  
   - Run a **pinned** Markdown linter (e.g., `markdownlint-cli2`) with a **checked‑in config**.  
   - Enforce:
     - Single `#` H1 per file.  
     - No skipped heading levels.  
     - No trailing whitespace, mis‑indented lists, or inconsistent fences.  
     - No bare URLs where link text is required (accessibility).

5. **KFM‑MDP rules**  
   - Apply custom rules on top of the generic linter to enforce KFM‑specific constraints:
     - All H2 headings MUST be in `heading_registry.approved_h2`.  
     - Required H2 sections (e.g., Version History) MUST be present for governed docs.  
     - Governance footer links must match `governance_ref`/`ethics_ref`.  
     - Prohibit inline HTML that bypasses accessibility or sanitization rules.

6. **Accessibility & link checks (lightweight)**  
   - Basic pass to detect:
     - Empty link text.  
     - Obvious broken internal anchors (e.g., heading never defined).  
   - Deep link‑checking is out‑of‑scope for this composite and SHOULD be handled elsewhere.

7. **Report generation & telemetry**  
   - Produce a **single JSON report** at `report_path` with:
     - Per‑file lists of errors/warnings.  
     - Aggregated counts per severity and rule.  
     - Start/end timestamps, tool versions, and commit SHA.  
   - Emit OpenLineage events modeled as a `prov:Activity` with:
     - Inputs: markdown files, front‑matter schemas.  
     - Outputs: lint report.  
     - Attributes: commit SHA, `markdown_protocol_version`, counts.

8. **Exit semantics**  
   - If any **error** exists:  
     - Set `status=failed`, `error_count > 0`, and fail the step.  
   - If only warnings exist and `fail_level: warning`: treat as failure.  
   - Otherwise: `status=passed`, `error_count=0`.

All underlying tools (lint CLIs, helper scripts, containers) MUST be **pinned** by commit or digest in `action.yml`.

---

## 🧰 Rule Set & Checks

This action governs three main rule layers: **front‑matter**, **Markdown style**, and **KFM‑specific structure**.

### 1. Front‑matter Rules (KFM‑MDP v11.2.2)

At minimum, the following MUST be enforced:

- Exactly **one** YAML front‑matter block at the top of the document.  
- Required fields (no empty strings):
  - `title`, `path`, `version`, `last_updated`, `doc_kind`, `status`, `doc_uuid`, `semantic_document_id`.  
- `path` MUST match the file’s location relative to repo root.  
- `version` MUST follow the doc’s semantic versioning pattern (e.g., `v11.2.2`).  
- `last_updated` MUST be ISO 8601 date.  
- `markdown_protocol_version` MUST equal `KFM-MDP v11.2.2` for governed v11 docs.  
- Deprecated keys (including those listed in `deprecated_fields`) SHOULD trigger warnings or errors depending on policy.

### 2. Markdown Structure & Style

The Markdown linter config SHOULD, at minimum, enforce:

- Single H1 per file; H1 should match or closely align with `title`.  
- H2 headings limited to the set in `heading_registry.approved_h2`.  
- No heading level jumps (H2 → H4 without H3).  
- Proper fenced code blocks:
  - Language tag present where reasonable (` ```yaml`, ` ```jsonc`, etc.).  
  - Balanced fences (no unclosed blocks).  
- Lists and code blocks indented consistently.  
- No trailing spaces, tabs, or hard tabs for indentation.  
- Lines kept within reasonable length limits for accessibility (unless in code blocks/tables).

### 3. KFM‑Specific Semantics

Additional rules SHOULD enforce:

- **Version History** table present for governed docs, with:
  - Columns: Version, Date, Summary.  
  - Row for current version matching front‑matter `version`/`last_updated`.
- **Governance footer** present, linking at least:
  - Docs root, standards index, governance root.  
- No references to obsolete protocol versions (e.g., older KFM‑MDP or KFM‑OP) unless explicitly documented as historical.  
- No speculative or unverified claims about governance states (e.g., “this bypasses review”); such content SHOULD be flagged.

---

## 📦 Data & Metadata Contract

### Inputs

| Input               | Type    | Required | Default                                    | Description |
|--------------------|---------|----------|--------------------------------------------|-------------|
| `paths`            | string  | ✅ Yes   | _none_                                     | Newline‑separated glob patterns of Markdown files (relative to `working_directory`). |
| `mode`             | string  | ❌ No    | `changed`                                  | One of `changed` \| `all`. `changed` limits to files touched in the current PR. |
| `fail_level`       | string  | ❌ No    | `error`                                    | Minimum severity that causes failure: `error` \| `warning`. |
| `working_directory`| string  | ❌ No    | `${{ github.workspace }}`                 | Base directory for resolving `paths`. |
| `config_path`      | string  | ❌ No    | `.github/linters/markdown-lint.config.*`   | Path to linter configuration (JSONC, YAML, or JS) relative to `working_directory`. |
| `schema_ref`       | string  | ❌ No    | `../../../schemas/json/markdown-frontmatter-v11.schema.json` | JSON Schema used to validate YAML front‑matter. |
| `report_path`      | string  | ❌ No    | `artifacts/markdown/markdown-lint-report.json` | Output path (relative to `working_directory`) for the machine‑readable lint report. |
| `extra_args`       | string  | ❌ No    | `""`                                       | Extra CLI flags passed through to the underlying linter(s) for advanced scenarios. |

### Outputs

| Output          | Type   | Description |
|-----------------|--------|-------------|
| `status`        | enum   | `"passed"` or `"failed"` based on `fail_level` and findings. |
| `error_count`   | int    | Total number of lint errors across all files. |
| `warning_count` | int    | Total number of lint warnings across all files. |
| `files_scanned` | int    | Count of Markdown files processed in this run. |
| `report_path`   | string | Final, resolved path to the generated JSON report. |

### Report Format (High‑Level)

The JSON report MUST, at minimum, follow a structure equivalent to:

```jsonc
{
  "schema_version": "kfm-markdown-lint-report-v1",
  "markdown_protocol_version": "KFM-MDP v11.2.2",
  "run": {
    "started_at": "2025-11-28T12:34:56Z",
    "finished_at": "2025-11-28T12:34:58Z",
    "commit_sha": "<commit>",
    "mode": "changed"
  },
  "summary": {
    "files_scanned": 23,
    "errors": 1,
    "warnings": 5
  },
  "files": [
    {
      "path": "docs/standards/kfm_markdown_protocol_v11.2.2.md",
      "errors": [
        {
          "code": "KFM-MDP-E001",
          "rule": "frontmatter/required-field",
          "message": "Missing required field: doc_uuid",
          "line": 2,
          "column": 1,
          "severity": "error"
        }
      ],
      "warnings": [
        {
          "code": "MD013",
          "rule": "line-length",
          "message": "Line longer than configured maximum.",
          "line": 120,
          "column": 1,
          "severity": "warning"
        }
      ]
    }
  ]
}
```

Exact schema is defined in `telemetry_schema` and MUST remain backward‑compatible across **patch** releases of v11.  

For new fields, additive changes SHOULD be used; breaking changes require a new `schema_version`.

---

## ⚖ FAIR+CARE & Governance

The `markdown-lint` composite action participates in KFM’s governance as follows:

1. **Pinned, deterministic toolchain**  
   - All third‑party actions, CLIs, and containers MUST be pinned with `@<commit_sha>` or `@sha256:<digest>`.  
   - No floating tags like `@v1` or `@latest` are permitted.

2. **No implicit secrets or external I/O**  
   - The action MUST NOT assume or read secrets unless explicitly passed.  
   - External network calls SHOULD be avoided; if used (e.g., for remote rule bundles), they MUST be documented and opt‑in.

3. **FAIR+CARE alignment**  
   - Linting MUST NOT leak sensitive content into telemetry; only aggregate metadata and rule codes are allowed.  
   - Rules MUST respect sovereignty constraints (e.g., not requiring explicit coordinates for sensitive locations).  
   - Accessibility checks (e.g., link text, heading order) support **Responsible** and **Collective Benefit** principles.

4. **Change management**  
   - Any change to the composite’s inputs, outputs, or rule semantics MUST:
     - Update `.github/actions/markdown-lint/action.yml`.  
     - Update this README and associated schemas (`json_schema_ref`, `shape_schema_ref`).  
     - Pass the full test profile: `markdown-lint`, `schema-lint`, `metadata-check`, `footer-check`, `accessibility-check`, `provenance-check`.

5. **CI enforcement**  
   - `kfm-ci.yml` SHOULD treat a failed `markdown-lint` step as a **hard block** for merging governed docs.  
   - Any temporary bypass MUST be:
     - Scoped (file‑ and PR‑specific).  
     - Time‑boxed and recorded in the PR description.  
     - Approved under the Infrastructure & Provenance Committee’s emergency procedures.

---

## 🕰️ Version History

| Version | Date       | Summary                                                                                              |
|--------:|------------|------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-28 | Initial governed Markdown/front‑matter lint composite action; aligned with KFM‑MDP v11.2.2 and CI v11|

---

<div align="center">

🧂 **KFM v11 — Markdown & Front‑Matter Lint Composite Action**  
Protocol‑Aligned Docs · Deterministic Linting · FAIR+CARE‑Aware Documentation Governance  

[⬅ Composite Actions Library](../README.md) · [📘 Markdown Protocol](../../../docs/standards/kfm_markdown_protocol_v11.2.2.md) · [⚖ Governance](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

