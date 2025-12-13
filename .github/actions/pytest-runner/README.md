---
title: "♻️ Kansas Frontier Matrix — Reusable Workflows Library (Governed CI/CD Building Blocks)"
path: ".github/workflows/reusable/README.md"
version: "v11.2.6"
last_updated: "2025-12-13"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Infrastructure & Provenance Committee"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.6/manifest.zip"
attestation_ref: "../../../releases/v11.2.6/slsa-attestation.json"
signature_ref: "../../../releases/v11.2.6/signature.sig"

telemetry_ref: "../../../releases/v11.2.6/github-infra-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/github-workflows-v4.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

status: "Active / Enforced"
doc_kind: "Overview"
intent: "github-reusable-workflows"
role: "ci-cd-reusable-library"
category: "CI/CD · Automation · Governance · Reusability"

classification: "Public Document"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM Infrastructure & Provenance Committee"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"

provenance_chain:
  - ".github/workflows/reusable/README.md@v11.2.6"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: false
  must_reference_origin_root: false

json_schema_ref: "../../../schemas/json/github-workflows-readme-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/github-workflows-readme-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:github-workflows:reusable-readme:v11.2.6"
semantic_document_id: "kfm-doc-github-workflows-reusable-readme"
event_source_id: "ledger:.github/workflows/reusable/README.md"
immutability_status: "mutable-plan"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"
  - "content-alteration"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧱 Architecture"
    - "🧪 Validation & CI/CD"
    - "📦 Data & Metadata"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "footer-check"
  - "accessibility-check"
  - "provenance-check"
  - "secret-scan"
  - "pii-scan"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_version_history: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true
---

<div align="center">

# ♻️ **Kansas Frontier Matrix — Reusable Workflows Library (v11.2.6)**
`.github/workflows/reusable/README.md`

**Purpose**  
Document the **reusable workflow library** (`workflow_call`) used by Kansas Frontier Matrix CI/CD to keep
pipelines **deterministic, governed, auditable, and consistent** across PR validation, scheduled runs, and releases.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/CI%2FCD-Reusable_Workflows-success" />
<img src="https://img.shields.io/badge/Governance-FAIR%2BCARE-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

</div>

---

## 📘 Overview

Reusable workflows are **governed building blocks** for `.github/workflows/*`:

- A *caller workflow* handles triggers (`pull_request`, `push`, `schedule`, `workflow_dispatch`).
- A *reusable workflow* (this directory) implements **standard job logic** via `on: workflow_call`.
- Composite actions under `.github/actions/*` provide **step-level reuse** inside reusable workflows.

This structure reduces drift and keeps critical behavior consistent:

- identical lint/test/validate semantics across callers,
- standardized artifacts and telemetry,
- centralized permission and secret handling,
- deterministic tooling and pinned dependencies.

**When to use what**

- Use a **reusable workflow** when you need to reuse **jobs** (multiple steps, artifacts, permissions, strategy matrices).
- Use a **composite action** when you need to reuse **steps** (a single unit of behavior inside a job).

**Library contract (non-negotiable)**

All reusable workflows in this folder MUST:

- declare `on: workflow_call`,
- document inputs/outputs (via this README index + inline comments in the workflow),
- use least-privilege `permissions`,
- emit artifacts/telemetry to stable locations (see `📦 Data & Metadata`),
- avoid leaking secrets to logs, artifacts, or telemetry.

---

## 🗂️ Directory Layout

~~~text
.github/
└── 🤖 workflows/                                      — Governed CI/CD workflows
    ├── 📄 README.md                                   — Master architecture (caller workflows)
    └── 📁 reusable/                                   — Reusable workflows library (workflow_call)
        ├── 📄 README.md                               — This library index
        ├── 📄 _template.reusable.yml                  — Canonical template for new reusables
        ├── 📄 python_ci.reusable.yml                  — Python lint + unit tests + coverage (example)
        ├── 📄 node_ci.reusable.yml                    — Node/TS lint + unit tests + build (example)
        ├── 📄 docs_validate.reusable.yml              — Markdown/front-matter validation bundle (example)
        ├── 📄 stac_validate.reusable.yml              — STAC validation bundle (example)
        ├── 📄 dcat_validate.reusable.yml              — DCAT validation bundle (example)
        └── 📄 telemetry_export.reusable.yml           — Telemetry aggregation/export bundle (example)
~~~

**Note**  
The filenames above illustrate the *intended pattern*. Keep the directory index current as workflows are added/renamed.

---

## 🧱 Architecture

Reusable workflows sit between **caller workflows** and **composite actions**.

~~~mermaid
flowchart TB
  A["Caller workflow (triggered)\n.github/workflows/*.yml"] --> B["Reusable workflow\n.github/workflows/reusable/*.yml\n(on: workflow_call)"]
  B --> C["Composite actions\n.github/actions/*\n(step reuse)"]
  B --> D["Artifacts + reports\nartifacts/** or uploaded artifacts"]
  B --> E["Telemetry + lineage\nreleases/<version>/github-infra-telemetry.json\n(OpenLineage/PROV summaries)"]
~~~

**Design goals**

- **Determinism**: behavior is config-driven and repeatable.
- **Consistency**: one canonical implementation for common CI jobs.
- **Governance**: enforce FAIR+CARE and sovereignty policies at the workflow boundary.
- **Security**: least privilege, pinned actions, and careful artifact/log hygiene.
- **Observability**: machine-readable outputs for dashboards and audits.

---

## 🧪 Validation & CI/CD

### Calling a reusable workflow

In a caller workflow job:

~~~yaml
jobs:
  python_ci:
    name: "🐍 Python CI (reusable)"
    uses: ./.github/workflows/reusable/python_ci.reusable.yml
    with:
      python_version: "3.11"
      test_paths: |
        tests/
      min_coverage: 85
    secrets: inherit
~~~

### Required conventions

Reusable workflows SHOULD:

- define `inputs` with types and defaults,
- define `outputs` for downstream jobs (e.g., `status`, `coverage`, `artifact_name`),
- standardize artifact paths (avoid per-job ad-hoc naming),
- centralize tool bootstrapping (setup runtime, caching, lockfile installation),
- avoid “helpful” implicit fallbacks that hide misconfiguration.

### Permissions and secrets

Reusable workflows MUST explicitly declare minimal permissions, for example:

~~~yaml
permissions:
  contents: read
  pull-requests: read
~~~

Guidance:

- Prefer `contents: read` unless the workflow must write tags/releases.
- Prefer passing secrets through `secrets: inherit` only when the reusable workflow genuinely needs them.
- Never print secret values; never serialize them into telemetry.

---

## 📦 Data & Metadata

Reusable workflows are expected to emit:

- **Artifacts** (test reports, lint JSON, schema validation reports)
- **Telemetry summaries** (counts, durations, outcomes, tool versions)
- **Provenance-friendly identifiers** (commit SHA, workflow/job names, profile versions)

### Artifact conventions

Recommended layout (inside the runner workspace):

~~~text
artifacts/
├── markdown/                    — Markdown + front-matter lint reports
├── dcat/                        — DCAT validation outputs
├── stac/                        — STAC validation outputs
├── pytest/                       — JUnit + coverage + pytest telemetry
└── telemetry/                    — Aggregated CI telemetry (machine readable)
~~~

### Telemetry hygiene

Telemetry MUST contain:

- counts, durations, versions, statuses,
- file paths (relative) and rule codes (when needed),

Telemetry MUST NOT contain:

- raw file contents,
- secrets,
- precise sensitive coordinates,
- PII.

---

## ⚖ FAIR+CARE & Governance

This library is part of KFM’s governance surface:

- Reusable workflows are treated as **policy-bearing infrastructure**.
- They must respect sovereignty protections and masking/generalization rules when validating or exporting data artifacts.
- All third-party GitHub Actions used inside reusables MUST be pinned by SHA in the workflow file.
- Any contract changes (inputs/outputs, failure semantics, artifact paths) MUST be updated in:
  - the reusable workflow file,
  - this README index,
  - any affected schemas or CI checks.

Minimum CI expectations:

- `markdown-lint` and `schema-lint` pass for this README.
- Secret scanning and PII scanning remain clean.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v11.2.6** | 2025-12-13 | Added governed index README for reusable workflows library; defined conventions for workflow_call usage, artifacts, telemetry hygiene, and governance rules. |

---

<div align="center">

♻️ **KFM Reusable Workflows Library**  
Deterministic CI/CD · Governed Automation · Provenance-Aware Execution

[⬅ Workflows Master Architecture](../README.md) ·
[🧩 Composite Actions](../../actions/README.md) ·
[⚖ Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../docs/standards/faircare/FAIRCARE-GUIDE.md)

</div>
