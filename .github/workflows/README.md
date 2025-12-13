---
title: "🔁 Kansas Frontier Matrix — Reusable GitHub Workflows (KFM CI/CD)"
path: ".github/workflows/reusable/README.md"

version: "v11.2.6"
last_updated: "2025-12-13"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council Oversight"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Index"
intent: "github-reusable-workflows"
role: "ci-cd-reusable-workflows-overview"
category: "CI/CD · Automation · Security · Telemetry"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

classification: "Public"
sensitivity: "General"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
jurisdiction: "Kansas / United States"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

telemetry_schema: "../../../schemas/telemetry/github-workflows-v4.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

json_schema_ref: "../../../schemas/json/github-reusable-workflows-readme-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/github-reusable-workflows-readme-v11-shape.ttl"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "governance-override"
  - "content-alteration"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

doc_uuid: "urn:kfm:doc:github-workflows:reusable:index:v11.2.6"
semantic_document_id: "kfm-doc-github-workflows-reusable-readme"
event_source_id: "ledger:.github/workflows/reusable/README.md"
immutability_status: "mutable-plan"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# 🔁 **Kansas Frontier Matrix — Reusable GitHub Workflows (v11.2.6 LTS)**
`.github/workflows/reusable/README.md`

<img src="https://img.shields.io/badge/Markdown-KFM--MDP_v11.2.6-blue" />
<img src="https://img.shields.io/badge/CI%2FCD-Reusable_Workflows-success" />
<img src="https://img.shields.io/badge/Supply--Chain-Hardened-critical" />
<img src="https://img.shields.io/badge/Telemetry-OpenLineage%20%2B%20OTel-9c27b0" />
<img src="https://img.shields.io/badge/License-MIT-green" />

**Purpose**  
Provide the **canonical index + authoring contract** for **reusable GitHub Actions workflows**
stored under `.github/workflows/reusable/`.

Reusable workflows are treated as **governed CI/CD infrastructure**:
they reduce duplication, centralize policy, and enforce consistent validation across the KFM pipeline
(ETL → catalogs → graph → API → UI → Story Nodes → Focus Mode).

</div>

---

## 📘 Overview

### What lives here

This directory contains **reusable GitHub Actions workflows** designed to be invoked via `workflow_call`.

Use this directory when you need:

- **One canonical implementation** of a repeated CI/CD concern (e.g., linting, schema validation, security scanning).
- **Consistent governance gates** (FAIR+CARE checks, sovereignty masking checks, “no secrets/no PII” enforcement).
- **Shared telemetry emission** patterns (OpenLineage + OpenTelemetry-friendly artifacts).

### What does not live here

Keep these **out of** `reusable/`:

- One-off workflows that are **only used once** (keep them in `.github/workflows/`).
- Repo content that belongs in the pipeline itself (scripts, schemas, validators) — those belong under:
  - `tools/` (validators, lint drivers, CLI helpers)
  - `schemas/` (JSON schema, SHACL, telemetry schema)
  - `src/` (application/pipeline code)
  - `docs/` (standards, architecture, workflow documentation)

### Source of truth

- Master CI/CD architecture: `../README.md`
- Markdown authoring standard: `../../../docs/standards/kfm_markdown_protocol_v11.2.6.md`

---

## 🗂️ Directory Layout

Reusable workflow layouts MUST follow the governed tree style.

~~~text
.github/
└── 🤖 workflows/                                        — Primary workflows + orchestration
    └── 🔁 reusable/                                     — Reusable workflows (called via workflow_call)
        ├── 📄 README.md                                 — ← This document
        ├── 📄 reusable_<domain>_<purpose>.yml            — Reusable workflow contract (on: workflow_call)
        ├── 📄 reusable_<domain>_<purpose>.md             — Optional: per-workflow notes (governance + I/O)
        └── 📁 templates/                                — Optional: snippets for authors (no secrets)
~~~

### Naming conventions (recommended)

- `reusable_<domain>_<purpose>.yml`
  - domain examples: `ci`, `docs`, `security`, `data`, `catalog`, `graph`, `ui`, `ai`, `telemetry`
  - purpose examples: `lint`, `test`, `schema_validate`, `sbom_verify`, `faircare_gate`

---

## 🧭 Context

KFM CI/CD is **policy + provenance**, not just build automation.

Reusable workflows are the **shared “policy modules”** that primary workflows call to ensure:

- consistent enforcement of KFM standards
- predictable artifacts and telemetry
- minimal-permission security posture
- deterministic, replayable validations

In practice:

- `.github/workflows/*.yml` contains **triggers and orchestration**
- `.github/workflows/reusable/*.yml` contains **reusable policy implementations**

---

## 🗺️ Diagrams

~~~mermaid
flowchart TB
  A["PR / Push / Schedule"] --> B["Primary workflow in .github/workflows/"]
  B --> C["Reusable workflow (workflow_call) in .github/workflows/reusable/"]
  C --> D["Repo validators and scripts (tools/ src/ schemas/)"]
  D --> E["Artifacts + telemetry (reports, logs, summaries)"]
~~~

---

## 🧠 Story Node & Focus Mode Integration

Reusable workflows are expected to support Story Nodes / Focus Mode governance by:

- running documentation validators for narrative safety and required metadata
- enforcing model-card and experiment-log completeness (when AI/ML changes occur)
- blocking speculative additions where governed standards prohibit them

Reusable workflows MUST NOT:

- generate or rewrite narrative content
- fabricate evidence, citations, provenance, or governance status
- bypass sovereignty or masking requirements

(Those are enforced by standards and validators; this directory only **runs** them.)

---

## 🧪 Validation & CI/CD

### Required reusable-workflow authoring rules

Every reusable workflow under this directory SHOULD:

- declare `on: workflow_call`
- define **typed** `inputs` with defaults where safe
- define `secrets` expectations explicitly
- use **minimal permissions** (`permissions:`) and avoid `write-all`
- pin third-party actions by **SHA** where feasible (supply-chain hardening)
- emit artifacts in a predictable structure (so telemetry aggregation can find them)

### Example caller pattern (local reusable)

~~~yaml
jobs:
  docs_validate:
    uses: ./.github/workflows/reusable/reusable_docs_validate.yml
    with:
      target_paths: "docs/**"
    secrets: inherit
~~~

### Example reusable contract skeleton

~~~yaml
name: "Reusable: Docs Validate"

on:
  workflow_call:
    inputs:
      target_paths:
        description: "Glob(s) to validate"
        required: true
        type: string
    secrets:
      GH_TOKEN:
        required: false

permissions:
  contents: read

jobs:
  validate:
    name: "Docs validation"
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@<pin-sha-or-version>
      - name: Run validators
        run: |
          echo "Run KFM doc validators here"
~~~

---

## 📦 Data & Metadata

Reusable workflows SHOULD standardize outputs so downstream aggregation is consistent.

Recommended artifact conventions:

- `artifacts/<workflow_name>/reports/**`
- `artifacts/<workflow_name>/logs/**`
- `artifacts/<workflow_name>/telemetry/**`

Recommended metadata signals (inputs or environment):

- `kfm_run_id` (caller-provided)
- `kfm_component` (e.g., `docs`, `stac`, `security`)
- `kfm_profile` (e.g., `markdown-lint`, `schema-lint`)

---

## 🌐 STAC, DCAT & PROV Alignment

Even CI/CD infrastructure is modeled as governed provenance:

- **PROV-O**
  - reusable workflow definition = `prov:Plan`
  - each workflow run = `prov:Activity`
  - runner / bot identity = `prov:Agent`
  - produced logs, SBOMs, reports = `prov:Entity`

- **DCAT**
  - CI artifacts can be described as dataset distributions (when published)

- **STAC**
  - Non-spatial STAC Items can represent released artifacts (geometry null, datetime = run time)

This README does not publish catalogs; it defines the conventions that make it possible.

---

## 🧱 Architecture

### Interface boundaries

Reusable workflows are allowed to:

- call repo tooling (`tools/**`, `src/**`, `schemas/**`) via deterministic scripts
- upload artifacts needed for governance review

Reusable workflows are not allowed to:

- embed data transforms that belong in ETL (those must be deterministic pipelines under `src/` + `data/`)
- “decide” governance outcomes beyond reporting validator results

### Versioning strategy (recommended)

- Reusable workflows should be treated as API surface:
  - avoid breaking input names/types
  - deprecate with clear migration notes
  - keep behavior deterministic for the same inputs + repo ref

---

## ⚖ FAIR+CARE & Governance

Reusable workflows enforce governance by design:

- **No secrets / no PII**: never echo secrets; redact logs if needed.
- **Sovereignty-aware**: do not output or cache precise sensitive locations.
- **Least privilege**: permissions must be explicitly minimized.
- **Auditability**: steps must be traceable via logs + artifacts.
- **Reproducibility**: do not depend on non-pinned mutable external resources when avoidable.

If a reusable workflow must access sensitive resources, it MUST:
- document the justification and constraints in an adjacent `.md` note, and
- require explicit secret inputs (never implicit).

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v11.2.6** | 2025-12-13 | Initial governed index for `.github/workflows/reusable/`; establishes `workflow_call` contract patterns, security posture, and provenance-friendly artifact conventions. |

---

<div align="center">

🔁 **Reusable Workflows Index (v11.2.6)**  
Governed CI/CD · Provenance-Aware · FAIR+CARE-Aligned

[⬅ Workflows Master README](../README.md) ·
[📑 KFM Markdown Protocol](../../../docs/standards/kfm_markdown_protocol_v11.2.6.md) ·
[🏛️ Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

</div>
