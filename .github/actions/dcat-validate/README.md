---
title: "♻️ Kansas Frontier Matrix — Reusable GitHub Workflows Library (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: ".github/workflows/reusable/README.md"

version: "v11.2.6"
last_updated: "2025-12-13"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Infrastructure & Provenance Committee"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Component Guide"
intent: "github-reusable-workflows-library"
role: "ci-cd-reuse"
category: "CI/CD · Automation · Governance · Reusability"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

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

classification: "Public"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM Infrastructure & Provenance Committee"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"

provenance_chain:
  - ".github/workflows/reusable/README.md@v11.2.6"

json_schema_ref: "../../../schemas/json/github-reusable-workflows-readme-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/github-reusable-workflows-readme-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:github-workflows:reusable-readme:v11.2.6"
semantic_document_id: "kfm-doc-github-workflows-reusable-readme"
event_source_id: "ledger:.github/workflows/reusable/README.md"
immutability_status: "mutable-plan"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "a11y-adaptations"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true
---

<div align="center">

# ♻️ **Kansas Frontier Matrix — Reusable GitHub Workflows Library**
`.github/workflows/reusable/README.md`

**Purpose**  
Define the **governed reusable workflow library** (GitHub Actions `workflow_call`) used across KFM CI/CD.  
Reusable workflows exist to keep gates **deterministic**, **least-privilege**, **auditable**, and **consistent** across the monorepo.

<img src="https://img.shields.io/badge/Markdown-KFM--MDP_v11.2.6-blueviolet" />
<img src="https://img.shields.io/badge/CI%2FCD-Reusable_Workflows-success" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Governed-orange" />
<img src="https://img.shields.io/badge/License-MIT-green" />

</div>

---

## 📘 Overview

Reusable workflows are the **shared building blocks** for KFM CI/CD:

- Standardize core behaviors (checkout, setup, caching, lint/test/validate patterns).
- Enforce **least-privilege permissions** and explicit secret usage.
- Provide stable **interfaces** (inputs/outputs) so top-level workflows remain readable.
- Centralize consistent **telemetry hooks** (artifacts, reports, lineage events).

**Normative principle**: Top-level workflows orchestrate *what* runs; reusable workflows implement *how* it runs.

---

## 🗂️ Directory Layout

This folder contains reusable workflows invoked via `workflow_call`.

~~~text
.github/
└── 🤖 workflows/
    ├── 📄 README.md                               — Master CI/CD architecture (overview)
    └── ♻️ reusable/                                — Reusable workflows library (this directory)
        ├── 📄 README.md                            — This document
        └── 🧩 <reusable-workflow>.yml              — Reusable workflow(s) (workflow_call entrypoints)
~~~

**Naming conventions**

- Prefer kebab-case: `python-lint.yml`, `node-test.yml`, `stac-validate.yml`.
- Prefer “verb-object” clarity (what the workflow provides), not where it is used.
- Avoid “misc” workflows; split by concern.

---

## 🧭 Context

KFM treats CI/CD as governed infrastructure:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j → API → Frontend → Story Nodes → Focus Mode

Reusable workflows sit inside CI/CD and must preserve:

- Determinism (pinned actions, locked toolchains).
- Traceability (reports + lineage-friendly outputs).
- Governance enforcement (FAIR+CARE + sovereignty constraints).
- Accessibility and documentation standards checks.

---

## 🧱 Architecture

### Workflow interface contract

Each reusable workflow MUST define:

- `on: workflow_call`
- **Inputs** with types and defaults.
- **Outputs** (when meaningful) for upstream orchestration.
- A minimal permission set under `permissions:` (job-level where possible).

Recommended interface pattern:

~~~yaml
on:
  workflow_call:
    inputs:
      fail_level:
        required: false
        type: string
        default: "error"
    secrets:
      GH_TOKEN:
        required: false
~~~

### Least-privilege defaults (recommended)

- Default `permissions: { contents: read }`
- Add write permissions only when strictly needed (e.g., release packaging).
- Never assume secrets exist; require them explicitly via `workflow_call.secrets`.

### Pinned dependencies (normative)

- Third-party actions MUST be pinned by commit SHA.
- Toolchains SHOULD be pinned (Node, Python, Java, etc.) and version-logged to artifacts.

---

## 🧪 Validation & CI/CD

Reusable workflows are expected to be used by top-level workflows under `.github/workflows/`.

**Required behaviors for governed steps**

- Fail fast on deterministic validation failures.
- Produce machine-readable artifacts (JSON where appropriate).
- Never print sensitive values to logs.
- When producing reports, write to predictable paths (e.g., `artifacts/<domain>/...`).

**Expected CI profiles impacted by changes here**

- `markdown-lint`
- `schema-lint`
- `metadata-check`
- `secret-scan`
- `pii-scan`

---

## 📦 Data & Metadata

Reusable workflows SHOULD standardize artifact names and locations so telemetry aggregation is consistent.

Recommended artifact conventions:

- `artifacts/<domain>/<tool>-report.json`
- `artifacts/<domain>/<tool>-summary.json`
- `artifacts/<domain>/run-metadata.json` (versions, start/end timestamps, inputs summary)

Where lineage is emitted, reusable workflows SHOULD include stable identifiers that upstream workflows can incorporate into PROV/OpenLineage exports.

---

## ⚖ FAIR+CARE & Governance

Reusable workflows MUST NOT:

- Bypass FAIR+CARE or sovereignty enforcement.
- Introduce uncontrolled network calls without documentation and justification.
- Introduce floating dependencies (`@latest`, unpinned containers, unpinned CLIs).

If a reusable workflow needs elevated permissions or access, document:

- Why it is required
- The minimal scope
- How it is audited (reports, attestations, telemetry)

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v11.2.6** | 2025-12-13 | Introduced governed README for reusable workflows library; standardized interface, naming, least-privilege, and artifact conventions. |

---

<div align="center">

♻️ **Reusable Workflows Library**  
Deterministic CI/CD · Governed Interfaces · Reusable Infrastructure

[⬅ Workflows Overview](../README.md) ·
[🛡 Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

</div>
