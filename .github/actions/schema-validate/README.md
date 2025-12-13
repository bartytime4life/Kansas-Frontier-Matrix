---
title: "📐 KFM v11.2.2 — Schema Validation Composite Action"
path: ".github/actions/schema-validate/README.md"
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
  - ".github/actions/schema-validate/README.md@v11.2.2"

prov_profile: "PROV-O Plan + KFM Governance Extensions"
openlineage_profile: "OpenLineage v2.5 (CI/CD events)"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../schemas/json/actions-schema-validate-readme-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/actions-schema-validate-readme-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:github-actions-schema-validate:v11.2.2"
semantic_document_id: "kfm-doc-github-actions-schema-validate"
event_source_id: "ledger:.github/actions/schema-validate/README.md"

immutability_status: "mutable-plan"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🧪 Validation & CI/CD"
    - "🧰 Schema Types & Profiles"
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
  - "old_schema_validate_action_readme_v10.4"
---

<div align="center">

# 📐 **KFM v11 — Schema Validation Composite Action**  
`.github/actions/schema-validate/README.md`

**Purpose**  
Provide a **governed, deterministic composite GitHub Action** for validating **JSON / YAML / JSON‑LD**  
(and related KFM metadata documents) against **registered JSON Schemas & SHACL shapes**, including  
**STAC**, **DCAT**, **telemetry**, and **Story Node / Focus Mode** profiles.

[![KFM-MDP v11.2.2](https://img.shields.io/badge/Markdown-KFM--MDP_v11.2.2-blue)](../../../docs/standards/kfm_markdown_protocol_v11.2.2.md)
· [![KFM-PDC v11](https://img.shields.io/badge/Pipeline_Contract-KFM--PDC_v11-indigo)]()
· [![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen)]()
· [![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../LICENSE)

</div>

---

## 📘 Overview

The **`schema-validate` composite action** is the canonical way to enforce **schema contracts** in KFM CI:

- Validates **JSON, YAML, JSON‑LD** documents against **versioned JSON Schemas** and **SHACL shapes**.  
- Supports multiple **profiles** including:
  - Core configuration (`kfm-config`),  
  - STAC (`kfm-stac-item`, `kfm-stac-collection`),  
  - DCAT (`kfm-dcat-v11`),  
  - Telemetry (CI, energy, carbon),  
  - Story Node / Focus Mode metadata.  
- Produces **machine‑readable validation reports** for CI dashboards and provenance.  
- Emits **OpenLineage / PROV** events that document schema checks applied to each artifact.

This action SHOULD be used by:

- `kfm-ci.yml` for **every PR** touching JSON/YAML configuration, STAC, DCAT, or telemetry.  
- Data and metadata pipelines before **publishing** to STAC/DCAT catalogs.  
- Release workflows to ensure **schemas & shapes remain compatible** with KFM profiles.

Where `markdown-lint` guards **docs**, `schema-validate` guards the **structured metadata & configuration layer**.

---

## 🧪 Validation & CI/CD

This composite action is **contract‑driven**: implementation details MAY evolve, but the contract below MUST  
remain stable across v11.x.

### 1. Typical Usage

Simple example in `.github/workflows/kfm-ci.yml`:

~~~yaml
- name: 📐 Validate JSON/YAML schemas (core)
  uses: ./.github/actions/schema-validate
  with:
    paths: |
      data/**/*.json
      data/**/*.yaml
      docs/**/*.schema.json
    profile: "kfm-config"
    fail_level: error
    report_path: artifacts/schema/schema-validation-core.json
~~~

STAC‑specific example:

~~~yaml
- name: 🛰 Validate STAC metadata
  uses: ./.github/actions/schema-validate
  with:
    paths: data/stac/**/*.json
    profile: "kfm-stac-item"
    fail_level: error
    report_path: artifacts/schema/stac-validation.json
~~~

DCAT‑telemetry example (e.g., CI telemetry):

~~~yaml
- name: 📊 Validate CI telemetry schema
  uses: ./.github/actions/schema-validate
  with:
    paths: telemetry/**/*.json
    profile: "kfm-telemetry-ci-v11"
    fail_level: warning
    report_path: artifacts/schema/telemetry-ci-validation.json
~~~

### 2. Normative Execution Stages

For every invocation, the composite action MUST perform at least:

1. **Target discovery**  
   - Resolve `paths` against `working_directory`.  
   - Respect `mode` when implemented (e.g., `changed` vs `all`).  
   - Fail with a configuration error if **no files** are discovered.

2. **Profile resolution**  
   - Interpret `profile` to:
     - Load the appropriate **JSON Schema bundle** and optional **SHACL shapes**.  
     - Select the correct **draft** (e.g., JSON Schema draft‑07 / 2020‑12).  
   - Profiles MUST be versioned and documented (e.g., `kfm-stac-item@v11`).

3. **Schema validation**  
   - Use a **pinned** schema engine (e.g., `ajv`, `python-jsonschema`) wrapped by a pinned container/CLI.  
   - For each file:
     - Parse JSON/YAML (using strict parsers; reject trailing commas, duplicate keys, etc.).  
     - Validate against:
       - Base schema(s) for the profile.  
       - Any compositional/allOf/oneOf rules in profile.  
   - Collect error & warning diagnostics, including:
     - JSON Pointer / path,  
     - Error code and human‑readable message,  
     - Severity.

4. **Shape / semantic validation (optional but recommended)**  
   - When `use_shapes: true` and a SHACL shape exists for the profile:
     - Convert JSON/JSON‑LD to RDF as required.  
     - Run SHACL engine with **pinned** implementation.  
     - Combine shape results into the same report under separate section.

5. **Report generation**  
   - Aggregate results into a single JSON report at `report_path`:
     - Input list and applied profile(s).  
     - Per‑file violations.  
     - Summary counts by severity and rule.  
     - Schema and shape versions used.  
     - Start/end timestamps.

6. **Exit semantics**  
   - If any **error** is present:
     - Set `status=failed` and `error_count > 0`.  
     - Fail the step when `fail_level: error`.  
   - If only **warnings** exist and `fail_level: warning`: also fail.  
   - Otherwise: `status=passed`, `error_count=0`.

7. **Telemetry & provenance**  
   - Emit telemetry conforming to `telemetry_schema`:
     - Run metadata, counts, profile, and schema versions.  
   - Emit OpenLineage/PROV events:
     - `prov:Activity` uses Entities (schema files + validated docs) and generates report Entity.  
     - Attach `event_source_id`, `commit_sha`, `profile`, and versions.

All underlying tools MUST be pinned by `@<commit_sha>` or container digests in `action.yml`.

---

## 🧰 Schema Types & Profiles

The `schema-validate` action is designed to work across multiple KFM schema families via **profiles**:

### 1. Core configuration profiles

Examples (names illustrative):

- `kfm-config` – generic KFM JSON/YAML configuration files.  
- `kfm-ci-config` – CI‑specific configuration (e.g., workflow metadata, feature flags).  

These profiles are typically backed by JSON Schemas in:

- `schemas/json/config/*.schema.json`  
- Optionally complemented by SHACL for semantic constraints.

### 2. STAC profiles

For STAC entities:

- `kfm-stac-item` – STAC Items aligned with `KFM-STAC v11`.  
- `kfm-stac-collection` – STAC Collections.  
- `kfm-stac-catalog` – STAC Catalogs.

These profiles MUST:

- Use STAC JSON Schemas, extended with KFM‑specific requirements.  
- Ensure:
  - Correct STAC version,  
  - Asset `roles` and required metadata,  
  - Provenance links (where required by KFM).

### 3. DCAT and catalog profiles

While DCAT‑RDF is primarily handled via the `dcat-validate` action, JSON or JSON‑LD DCAT representations MAY use:

- `kfm-dcat-json-v11` – JSON/JSON‑LD DCAT aligned with KFM‑DCAT v11.

### 4. Telemetry profiles

For CI, energy, and carbon telemetry:

- `kfm-telemetry-ci-v11`  
- `kfm-telemetry-energy-v2`  
- `kfm-telemetry-carbon-v2`

These profiles ensure:

- Correct schema versions,  
- Required fields (e.g., `schema_version`, `run`, `summary` blocks),  
- Units and value ranges where applicable.

### 5. Story Node & Focus Mode profiles

For narrative/graph‑aligned documents:

- `kfm-story-node-v1`  
- `kfm-focus-mode-v1`

These schemas align with KFM’s knowledge graph and Story Node specification, ensuring:

- Explicit spatial and temporal extents when required,  
- Links to graph node identifiers,  
- Governance fields (classification, sensitivity, etc.).

---

## 📦 Data & Metadata Contract

### Inputs

| Input               | Type    | Required | Default                                    | Description |
|--------------------|---------|----------|--------------------------------------------|-------------|
| `paths`            | string  | ✅ Yes   | _none_                                     | Newline‑separated glob patterns of schema‑validated files (JSON/YAML/JSON‑LD). |
| `profile`          | string  | ✅ Yes   | _none_                                     | Validation profile identifier (e.g., `kfm-config`, `kfm-stac-item`, `kfm-telemetry-ci-v11`). |
| `mode`             | string  | ❌ No    | `all`                                      | Future‑facing: one of `all` \| `changed`. `all` validates all matching files. |
| `fail_level`       | string  | ❌ No    | `error`                                    | Minimum severity that causes failure: `error` \| `warning`. |
| `working_directory`| string  | ❌ No    | `${{ github.workspace }}`                 | Base directory for resolving `paths`. |
| `schema_root`      | string  | ❌ No    | `schemas/json`                             | Base directory or URI for JSON Schemas referenced by `profile`. |
| `shape_root`       | string  | ❌ No    | `schemas/shacl`                            | Base directory or URI for SHACL shapes referenced by `profile`. |
| `use_shapes`       | boolean | ❌ No    | `false`                                    | Whether to apply SHACL validation in addition to JSON Schema. |
| `report_path`      | string  | ❌ No    | `artifacts/schema/schema-validation.json`  | Path (relative) where the JSON validation report is written. |
| `telemetry_path`   | string  | ❌ No    | `artifacts/schema/schema-validation-telemetry.json` | Path (relative) for summary telemetry JSON. |
| `extra_args`       | string  | ❌ No    | `""`                                       | Extra CLI flags passed to underlying schema engine(s) for advanced use. |

### Outputs

| Output          | Type   | Description |
|-----------------|--------|-------------|
| `status`        | enum   | `"passed"` or `"failed"` based on `fail_level` and findings. |
| `error_count`   | int    | Total number of validation errors across all files. |
| `warning_count` | int    | Total number of validation warnings across all files. |
| `files_scanned` | int    | Count of files processed. |
| `report_path`   | string | Final resolved path to the JSON validation report. |
| `telemetry`     | string | Final resolved path to telemetry JSON report. |

### Report Format (High‑Level)

At minimum, the report MUST follow a structure equivalent to:

~~~jsonc
{
  "schema_version": "kfm-schema-validation-report-v1",
  "profile": "kfm-config",
  "run": {
    "started_at": "2025-11-28T12:00:00Z",
    "finished_at": "2025-11-28T12:00:03Z",
    "duration_seconds": 3.01
  },
  "summary": {
    "files_scanned": 14,
    "errors": 1,
    "warnings": 2
  },
  "files": [
    {
      "path": "data/config/core.json",
      "errors": [
        {
          "code": "KFM-SCHEMA-E001",
          "message": "Required property 'version' is missing.",
          "json_pointer": "/",
          "severity": "error"
        }
      ],
      "warnings": [
        {
          "code": "KFM-SCHEMA-W010",
          "message": "Property 'debug' is discouraged in production profiles.",
          "json_pointer": "/debug",
          "severity": "warning"
        }
      ]
    }
  ]
}
~~~

Exact schema is defined in `telemetry_schema` and MUST remain backward‑compatible across v11 patch releases.  
Additive fields SHOULD be used for extensions; breaking changes require a new `schema_version` value.

---

## ⚖ FAIR+CARE & Governance

The `schema-validate` composite action has the following governance requirements:

1. **Pinned, deterministic toolchain**  
   - All underlying actions and schema engines MUST be pinned to `@<commit_sha>` or `@sha256:<digest>`.  
   - Schema and shape bundles MUST be versioned and stored in the repo (or a governed schema registry).

2. **No implicit network or secret usage**  
   - Validation MUST run against locally available schemas/shapes by default.  
   - If remote schema resolution is supported, it MUST be:
     - Explicitly documented,  
     - Opt‑in, and  
     - Routed through approved mirrors or registries.

3. **Reproducibility & provenance**  
   - Validation results MUST be reproducible from:
     - Repository state (commit SHA),  
     - Profile & schema versions,  
     - CLI arguments and environment.  
   - PROV/OpenLineage metadata MUST capture which schemas and shapes were used.

4. **FAIR+CARE alignment**  
   - Validation telemetry MUST NOT include full document contents, only paths and aggregate results.  
   - For sensitive or sovereignty‑protected documents:
     - Schemas SHOULD allow generalized/obfuscated fields (e.g., approximate locations).  
     - Error messages MUST NOT expose redacted content; they may reference field names and types only.

5. **Change management**  
   - Any change to:
     - Supported profiles,  
     - Input/output contracts,  
     - Telemetry or report structure  
     MUST be accompanied by:
       - Updates to `action.yml` and this README,  
       - Updates to JSON/SHACL schemas,  
       - Passing the full `test_profiles` suite.

6. **CI enforcement**  
   - `kfm-ci.yml` SHOULD treat a failed `schema-validate` step as a **hard block** for merging when:  
     - Config or catalog metadata is involved,  
     - Telemetry impacting governance is invalid.  
   - Overrides MUST be:
     - Narrow in scope,  
     - Explicitly justified in PR text,  
     - Time‑bounded and tracked by the Infrastructure & Provenance Committee.

---

## 🕰️ Version History

| Version | Date       | Summary                                                                                                 |
|--------:|------------|---------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-28 | Initial governed Schema Validation composite action; unified JSON/YAML schema validation + telemetry v1 |

---

<div align="center">

📐 **KFM v11 — Schema Validation Composite Action**  
Schema‑Safe Pipelines · Deterministic Validation · FAIR+CARE‑Aligned Metadata Governance  

[⬅ Composite Actions Library](../README.md) · [📘 Markdown Protocol](../../../docs/standards/kfm_markdown_protocol_v11.2.2.md) · [⚖ Governance](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
