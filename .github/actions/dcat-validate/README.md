---
title: "🗂️ KFM v11.2.2 — DCAT Validation Composite Action"
path: ".github/actions/dcat-validate/README.md"
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
  - ".github/actions/dcat-validate/README.md@v11.2.2"

prov_profile: "PROV-O Plan + KFM Governance Extensions"
openlineage_profile: "OpenLineage v2.5 (CI/CD events)"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../schemas/json/actions-dcat-validate-readme-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/actions-dcat-validate-readme-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:github-actions-dcat-validate:v11.2.2"
semantic_document_id: "kfm-doc-github-actions-dcat-validate"
event_source_id: "ledger:.github/actions/dcat-validate/README.md"

immutability_status: "mutable-plan"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🧪 Validation & CI/CD"
    - "📦 Data & Metadata Contract"
    - "🌐 STAC, DCAT & PROV Alignment"
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
  - "old_dcat_action_readme_v10.4"
---

<div align="center">

# 🗂️ **KFM v11 — DCAT Validation Composite Action**  
`.github/actions/dcat-validate/README.md`

**Purpose**  
Provide a **governed, deterministic composite GitHub Action** that validates **DCAT metadata**  
against **W3C DCAT + KFM-DCAT v11** profiles and blocks merges when catalog metadata  
is incomplete, invalid, or non-compliant.

[![KFM-MDP v11.2.2](https://img.shields.io/badge/Markdown-KFM--MDP_v11.2.2-blue)](../../../docs/standards/kfm_markdown_protocol_v11.2.5.md)
· [![KFM-DCAT v11](https://img.shields.io/badge/Profile-KFM--DCAT_v11-purple)]()
· [![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen)]()
· [![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../LICENSE)

</div>

---

## 📘 Overview

The **`dcat-validate` composite action** is the canonical way to verify that all KFM DCAT metadata:

- conforms to **DCAT 3.0** and the internal **KFM-DCAT v11** profile  
- is **syntactically valid RDF** (Turtle/JSON-LD/RDF/XML)  
- includes required **FAIR metadata** (title, description, publisher, license, contact, spatial/temporal coverage)  
- cleanly links to **distributions, data services, and versioned releases**

It is intended to be used by:

- `kfm-ci.yml` for **every PR** touching catalog or dataset metadata  
- `docs_validate.yml` for **documentation metadata sweeps**  
- **Release workflows** to assert that published catalogs are **DCAT-clean** before tagging

Key properties:

- 🧩 **Reusable** – wraps all DCAT checks into a single, pinned composite action  
- 🧬 **Schema-driven** – validates against JSON Schemas + SHACL shapes for KFM-DCAT v11  
- 🛰 **Observable** – emits machine-readable reports + OpenLineage events for metadata checks  
- 🛡 **Gatekeeper** – fails fast on **errors** (and optionally **warnings**) to protect catalog integrity

---

## 🧪 Validation & CI/CD

This composite action is **contract-driven**: workflows may change implementation details,  
but **MUST** preserve the external behaviour defined here.

### 1. Typical Usage

Add to a workflow (e.g. `.github/workflows/ci.yml`):

    - name: ✅ Validate DCAT metadata
      uses: ./.github/actions/dcat-validate
      with:
        catalog_path: docs/catalog/**/*.ttl
        profile: kfm-dcat-v11
        fail_level: error
        report_path: artifacts/dcat/dcat-validation.json

**Recommended workflows**

- **CI (PR)** – `fail_level: error`  
  - Block on hard violations, allow warnings  
- **Nightly / pre-release** – `fail_level: warning`  
  - Enforce stricter metadata hygiene

### 2. Validation Steps (Normative)

The composite action MUST, at minimum:

1. **Discover targets**  
   - Expand `catalog_path` glob(s) relative to `working_directory`  
   - Fail if **no files** are matched

2. **RDF parsing / syntax checks**  
   - Parse each file as RDF (Turtle, JSON-LD, RDF/XML) using a **pinned** toolchain  
   - Record syntax errors per file; syntax errors are always treated as **errors**

3. **Profile validation**  
   - Validate each graph against:
     - **Core DCAT constraints** (datasets, distributions, data services, etc.)  
     - **KFM-DCAT v11 profile** (identifiers, versioning, required contact/licensing, spatial/temporal coverage, etc.)  
   - Use **pinned** JSON Schema + SHACL shape bundles (`dcat_profile`)

4. **Cross-file consistency checks** (at minimum)  
   - Dataset identifiers are unique at catalog scope  
   - Distributions and services refer to existing datasets  
   - Required **version and lineage metadata** is present for versioned datasets

5. **Report generation**  
   - Produce a **single machine-readable report** at `report_path`:
     - per-file error/warning lists  
     - aggregated counts  
     - profile versions used  
     - start/end timestamps

6. **Exit semantics**  
   - If any **error** is present:
     - set composite output `status=failed`  
     - set `error_count > 0`  
     - **fail** the step  
   - If only **warnings** are present and `fail_level: warning`: treat as failure  
   - Otherwise: `status=passed`, `error_count=0`

7. **Telemetry & provenance**  
   - Emit OpenLineage/PROV events bound to `event_source_id`, including:
     - inputs (catalog files)  
     - profile versions  
     - outcome (pass/fail, counts)  
   - MUST NOT log file contents or any sensitive values; only aggregate metadata

Implementation details (tooling, containers, languages) may evolve,  
but they MUST remain **deterministic and pinned** in `action.yml`.

---

## 📦 Data & Metadata Contract

### Inputs

| Input               | Type    | Required | Default                                   | Description                                                                                          |
|--------------------|---------|----------|-------------------------------------------|------------------------------------------------------------------------------------------------------|
| `catalog_path`     | string  | ✅ Yes   | _none_                                    | Glob or path (relative to `working_directory`) to DCAT metadata files (e.g. `docs/catalog/**/*.ttl`). |
| `profile`          | string  | ✅ Yes   | `kfm-dcat-v11`                            | Validation profile identifier (`kfm-dcat-v11`, `kfm-dcat-v11-strict`, etc.).                        |
| `fail_level`       | string  | ❌ No    | `error`                                   | Minimum severity that causes failure: `error` \| `warning`.                                         |
| `working_directory`| string  | ❌ No    | `${{ github.workspace }}`                | Base directory used to resolve `catalog_path`.                                                      |
| `report_path`      | string  | ❌ No    | `artifacts/dcat/dcat-validation.json`     | Path (relative to `working_directory`) where the JSON report will be written.                      |
| `extra_args`       | string  | ❌ No    | `""`                                      | Extra CLI flags passed through to the underlying validator (advanced use only).                     |

### Outputs

| Output          | Type   | Description                                                                                   |
|-----------------|--------|-----------------------------------------------------------------------------------------------|
| `status`        | enum   | `"passed"` or `"failed"` based on `fail_level` and findings.                                  |
| `error_count`   | int    | Total number of validation errors across all files.                                           |
| `warning_count` | int    | Total number of validation warnings across all files.                                         |
| `report_path`   | string | Final resolved path to the generated JSON report.                                             |
| `profile_used`  | string | The effective validation profile identifier (after defaults and normalization).               |

### Report Format (High-Level)

The JSON report MUST, at minimum, include something equivalent to:

    {
      "schema_version": "kfm-dcat-validation-v1",
      "profile": "kfm-dcat-v11",
      "run": {
        "started_at": "2025-11-28T12:34:56Z",
        "finished_at": "2025-11-28T12:34:59Z"
      },
      "summary": {
        "files_scanned": 12,
        "errors": 0,
        "warnings": 3
      },
      "files": [
        {
          "path": "docs/catalog/kansas-history.ttl",
          "errors": [],
          "warnings": [
            {
              "code": "KFM-DCAT-W001",
              "message": "Dataset missing optional dcat:DatasetSeries linkage.",
              "severity": "warning"
            }
          ]
        }
      ]
    }

Exact schema is defined in `telemetry_schema` and SHOULD remain backward-compatible across minor versions.

---

## 🌐 STAC, DCAT & PROV Alignment

The `dcat-validate` action sits in the **catalog governance triangle**:

- **DCAT 3.0 / KFM-DCAT v11**  
  - Ensures datasets, distributions, data services, and dataset series are consistently described.  
  - Enforces key FAIR fields: identifier, title, description, license, publisher, contact, temporal & spatial coverage, access URLs.

- **STAC / KFM-STAC v11**  
  - For datasets with STAC representations, `dcat-validate` SHOULD ensure:
    - DCAT datasets link to STAC Collections/Items via stable IDs  
    - licenses and access URLs are consistent between DCAT and STAC  
    - temporal/spatial extents are compatible

- **PROV / OpenLineage**  
  - Each validation run is modeled as a `prov:Activity` that:
    - **used**: DCAT files (Entities)  
    - **generated**: the validation report (Entity)  
  - OpenLineage events SHOULD reference:
    - `event_source_id` from front-matter  
    - the DCAT profile (`dcat_profile`)  
    - counts & outcomes from the report

This alignment ensures:

- Catalog entries are **discoverable via DCAT**  
- Assets are **browsable via STAC**  
- Lineage is **auditable via PROV/OpenLineage** from raw data through catalog publication

---

## ⚖ FAIR+CARE & Governance

The `dcat-validate` composite action is governed by the following rules:

1. **Pinned implementations only**  
   - ALL third-party actions, containers, and CLIs MUST be pinned by `@<commit_sha>` or `@sha256:<digest>`  
   - No `@v1`, `@latest`, or floating tags allowed

2. **No implicit network or secret usage**  
   - MUST NOT call external network resources except those explicitly documented  
   - MUST NOT read or assume any secrets beyond those passed in via `with:` or environment

3. **Change management**  
   - Any change to inputs/outputs or validation semantics MUST:
     - update `action.yml` and this README in the same PR  
     - update associated JSON/SHACL schemas where relevant  
     - pass `markdown-lint`, `schema-lint`, `metadata-check`, and `provenance-check`

4. **FAIR+CARE & sovereignty**  
   - Validation MUST NOT force exposure of sensitive Indigenous or culturally restricted datasets  
   - Absence of precise coordinates is **valid** when datasets are marked sovereignty-protected per KFM governance  
   - Errors MUST NOT be raised solely for generalized or redacted spatial data where CARE rules apply

5. **CI enforcement**  
   - `kfm-ci.yml` SHOULD treat a failed `dcat-validate` step as a **hard block** for merging  
   - Emergency overrides MUST be explicitly documented by the Infrastructure & Provenance Committee

---

## 🕰️ Version History

| Version | Date       | Summary                                                                                         |
|--------:|------------|-------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-28 | Initial governed DCAT validation composite action; aligned with KFM-DCAT v11 and KFM-MDP v11.2.2 |

---

<div align="center">

🗂️ **KFM v11 — DCAT Validation Composite Action**  
DCAT 3.0 Compliance · Deterministic CI/CD · FAIR+CARE-Aligned Metadata Governance  

[⬅ Composite Actions Library](../README.md) · [⚖ Governance](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

