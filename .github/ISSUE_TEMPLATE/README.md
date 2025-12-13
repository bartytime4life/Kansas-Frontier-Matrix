---
title: "🧩 Kansas Frontier Matrix — Reusable CI/CD Workflows (Workflow Call Library)"
path: ".github/workflows/reusable/README.md"

version: "v11.2.6"
last_updated: "2025-12-13"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council Oversight"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Overview"
intent: "github-reusable-workflows-library"
role: "ci-cd-reusable-workflows"
category: "CI/CD · Governance · Automation · Security · Telemetry"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

classification: "Public Document"
sensitivity: "General"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

telemetry_ref: "../../../releases/v11.2.6/github-infra-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/github-workflows-v4.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

json_schema_ref: "../../../schemas/json/github-reusable-workflows-readme-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/github-reusable-workflows-readme-v11-shape.ttl"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "CreativeWork"
  prov_o: "prov:Plan"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

doc_uuid: "urn:kfm:doc:github-workflows:reusable:readme:v11.2.6"
semantic_document_id: "kfm-doc-github-workflows-reusable-readme"
event_source_id: "ledger:.github/workflows/reusable/README.md"
immutability_status: "mutable-plan"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "United States / Kansas"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next reusable-workflows architecture update"
---

<div align="center">

# 🧩 **Kansas Frontier Matrix — Reusable CI/CD Workflows (Workflow Call Library)**
`.github/workflows/reusable/README.md`

**Purpose**  
Define the **reusable workflow library** (GitHub Actions `workflow_call`) used by KFM’s CI/CD system to:
- reduce duplication across workflows,
- standardize governance/security/telemetry steps,
- enforce consistent interfaces (inputs, secrets, outputs),
- keep CI/CD behavior deterministic and reviewable.

</div>

---

## 📘 Overview

Reusable workflows in this folder are **not triggered directly** by `push` / `pull_request` by default.
They are **called** from “orchestrator” workflows in `.github/workflows/` via:

- `uses: ./.github/workflows/reusable/<workflow>.yml`

This design:

- keeps top-level workflows small and readable,
- makes shared steps (lint, schema validation, security scans, telemetry export) centrally maintained,
- provides stable, typed interfaces for CI/CD building blocks,
- supports governance constraints (least privilege, provenance, FAIR+CARE checks) consistently.

**Conventions**

1. **Only reusable workflows live here**  
   Each `*.yml` file in this directory MUST include:
   - `on: workflow_call`

2. **Interface-first**  
   Reusable workflows MUST declare:
   - `inputs` (typed with defaults where reasonable),
   - `secrets` (explicit, minimal),
   - optional `outputs` (explicit, stable names).

3. **Least-privilege by design**  
   Reusable workflows MUST NOT silently escalate permissions.  
   Callers set the final `permissions:` and pass required secrets explicitly.

4. **Deterministic behavior**  
   Where possible:
   - avoid network-dependent “latest” installs without pinning,
   - pin GitHub Actions to immutable versions/SHAs,
   - produce machine-readable artifacts and summaries consistently.

---

## 🗂️ Directory Layout

~~~text
.github/
└── 🤖 workflows/                                    — Governed CI/CD workflows
    ├── 📄 README.md                                 — Master CI/CD architecture (overview)
    └── 📁 reusable/                                 — Reusable workflows called via workflow_call
        ├── 📄 README.md                             — This document
        └── 📄 *.yml                                 — Reusable workflow definitions (workflow_call)
~~~

---

## 🧭 Context

Reusable workflows are the **workflow-layer equivalent** of library functions:

- Top-level workflows define **policy + orchestration**
  - when things run,
  - what gates apply,
  - what environments are allowed.

- Reusable workflows define **implementation primitives**
  - how linting runs,
  - how validators execute,
  - how telemetry artifacts are produced,
  - how supply-chain checks are applied.

This separation helps keep CI/CD **governable**:
- policies remain visible in orchestrators,
- primitives remain reusable and consistent,
- changes to shared behavior can be reviewed in one place.

---

## 🗺️ Diagrams

~~~mermaid
flowchart TB
  A["Top-level workflow\n(.github/workflows/*.yml)\nPR / push / schedule"] --> B["Calls reusable workflow\nuses: ./.github/workflows/reusable/*.yml"]
  B --> C["Reusable workflow runs\n(workflow_call)\nInputs + secrets + outputs"]
  C --> D["Artifacts + reports\n(telemetry, logs, validation JSON)"]
  D --> E["Caller aggregates + gates\n(required checks / release rules)"]
~~~

---

## 🧱 Architecture

### 1. Interface contract (workflow_call)

A reusable workflow MUST implement `on: workflow_call` and define a stable interface.

Example skeleton:

~~~yaml
name: "Reusable · <purpose>"

on:
  workflow_call:
    inputs:
      run_mode:
        type: string
        required: false
        default: "ci"
      fail_fast:
        type: boolean
        required: false
        default: true
    secrets:
      OPTIONAL_TOKEN:
        required: false
    outputs:
      report_path:
        description: "Path to generated report artifact"
        value: ${{ jobs.<job_id>.outputs.report_path }}

jobs:
  <job_id>:
    runs-on: ubuntu-latest
    outputs:
      report_path: ${{ steps.set_outputs.outputs.report_path }}
    steps:
      - name: Checkout
        uses: actions/checkout@<PINNED_VERSION_OR_SHA>

      - name: Run
        run: echo "do work"

      - id: set_outputs
        run: echo "report_path=reports/<file>.json" >> "$GITHUB_OUTPUT"
~~~

### 2. Calling pattern (from top-level workflows)

Callers invoke reusables using `uses:` at the job level:

~~~yaml
jobs:
  shared_validation:
    name: "Shared Validation"
    uses: ./.github/workflows/reusable/<workflow>.yml
    permissions:
      contents: read
      actions: read
    with:
      run_mode: "pr"
      fail_fast: true
    secrets:
      OPTIONAL_TOKEN: ${{ secrets.OPTIONAL_TOKEN }}
~~~

### 3. Naming and structure

Recommended naming conventions:

- File: `reusable_<domain>_<purpose>.yml`
  - Examples (illustrative): `reusable_docs_validate.yml`, `reusable_security_audit.yml`
- Job names should be short, consistent, and stable.
- Inputs should prefer:
  - `string`, `boolean`, `number` types,
  - stable enums documented in the workflow description.

### 4. Security guardrails (mandatory)

Reusable workflows SHOULD:

- avoid `pull_request_target` unless explicitly justified and separately governed,
- avoid writing to the repo unless required and explicitly granted by caller permissions,
- treat all PR content as untrusted input,
- minimize secret exposure:
  - pass secrets only to the job/steps that require them,
  - never echo secrets,
  - never write secrets into artifacts or logs.

---

## 🧪 Validation & CI/CD

Reusable workflows are subject to the same governance standards as orchestrators.

Minimum expectations:

- YAML structure must be valid and consistent.
- `workflow_call` interface changes MUST be treated as breaking changes unless backwards-compatible.
- Any reusable workflow producing artifacts MUST:
  - clearly name and document the artifact(s),
  - use stable paths and formats,
  - emit a concise run summary.

Recommended checks (implementation-dependent):

- workflow linting (YAML + GitHub Actions best practices),
- pinned action verification,
- permissions review (least privilege),
- secret/PII scanning across emitted artifacts.

---

## 📦 Data & Metadata

Reusable workflows MAY emit:

- validation reports (JSON),
- schema lint results,
- provenance/lineage events (where configured),
- telemetry summaries for aggregation.

Where artifacts are emitted:

- use machine-readable formats first (`.json`, `.sarif`, `.xml` where applicable),
- keep filenames stable to support deterministic downstream aggregation,
- avoid embedding restricted or sensitive content.

---

## 🌐 STAC, DCAT & PROV Alignment

This folder primarily concerns CI/CD infrastructure, but CI/CD outputs are still provenance-relevant:

- Each reusable workflow run can be modeled as a `prov:Activity`.
- Outputs (reports, logs, telemetry JSON) are `prov:Entity` artifacts.
- The caller workflow and repository policies act as `prov:Plan` references.

Where CI/CD artifacts are cataloged, they SHOULD carry:

- version (repo release or workflow version),
- timestamp,
- input scope (paths changed, dataset IDs where applicable),
- governance flags (if the workflow enforces FAIR+CARE or sovereignty constraints).

---

## ⚖ FAIR+CARE & Governance

Reusable workflows are governance-bearing infrastructure:

- They MUST NOT weaken sovereignty protections or bypass masking/generalization checks.
- They MUST keep enforcement deterministic and reviewable.
- They MUST remain compatible with repository-wide scanning (secrets, PII, policy checks).

If a reusable workflow is introduced that affects sensitive data handling, it MUST be reviewed under:

- `governance_ref`
- `ethics_ref`
- `sovereignty_policy`

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v11.2.6** | 2025-12-13 | Initial governed README for `.github/workflows/reusable/`; defines reusable workflow purpose, interface contracts, security guardrails, and governance alignment. |

---

<div align="center">

🧩 **KFM Reusable Workflows Library**  
Deterministic Primitives · Least Privilege · Governance-Aware CI/CD

[⬅ Workflows Master Architecture](../README.md) ·
[🏛️ Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

</div>
