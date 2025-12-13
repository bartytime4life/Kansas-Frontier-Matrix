---
title: "♻️ KFM GitHub Actions — Reusable Workflows (Docs & Conventions)"
path: ".github/workflows/reusable/README.md"

version: "v1.0.0"
last_updated: "2025-12-13"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · FAIR+CARE Council & Focus Mode Board"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Guide"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"

scope:
  domain: "ci-cd"
  applies_to:
    - ".github/workflows/**"
    - ".github/**/*.md"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"

indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by a newer README revision"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

json_schema_ref: "../../../schemas/json/kfm-markdown-protocol-v11.2.6.schema.json"
shape_schema_ref: "../../../schemas/shacl/kfm-markdown-protocol-v11.2.6-shape.ttl"

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:github:workflows:reusable:readme:v1.0.0"
semantic_document_id: "kfm-gha-reusable-workflows-readme"
event_source_id: "ledger:kfm:doc:github:workflows:reusable:readme:v1.0.0"
doc_integrity_checksum: "<sha256>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "metadata-extraction"
  - "layout-normalization"

ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

fencing_profile: "outer-backticks-inner-tildes-v1"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "footer-check"
  - "accessibility-check"
  - "provenance-check"
  - "secret-scan"
  - "pii-scan"
---

<div align="center">

# ♻️ **Reusable GitHub Actions Workflows**
`.github/workflows/reusable/README.md`

**Purpose**  
Provide the **canonical KFM guidance** for designing, documenting, and consuming **reusable GitHub Actions workflows** (`on: workflow_call`) in a **secure, least‑privilege, CI‑safe** way.

<img src="https://img.shields.io/badge/GitHub_Actions-Reusable_Workflows-blue" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

</div>

---

## 📘 Overview

### What this folder is (and is not)

**This folder is documentation + conventions only.**

GitHub Actions requires workflow files to live directly under:

- `.github/workflows/*.yml`

**Subdirectories under `.github/workflows/` are not supported for workflow YAML discovery.**  
Therefore:

- ✅ Keep *docs, tables, diagrams, templates, and notes* here.
- ❌ Do **not** place actual reusable workflow YAML files in this folder.

### Reusable workflows: the contract

A reusable workflow is a workflow file that includes:

~~~yaml
on:
  workflow_call:
~~~

A “caller” workflow invokes it via `jobs.<job_id>.uses`.

Local (same-repo) calling pattern:

~~~yaml
jobs:
  call-something:
    uses: ./.github/workflows/<workflow-file>.yml
~~~

Cross-repo calling pattern:

~~~yaml
jobs:
  call-something:
    uses: <org-or-user>/<repo>/.github/workflows/<workflow-file>.yml@<ref>
~~~

> KFM guidance: prefer tags or commit SHAs for `<ref>` in cross-repo usage to reduce supply-chain drift.

### Repository documentation expectation

KFM expects workflows to be documented so contributors can understand:
- what the workflow does,
- what inputs/secrets it requires,
- what outputs/artifacts it produces,
- what governance constraints apply.

Recommended companion docs location (repo policy pattern):
- `docs/workflows/<workflow-file>.yml.md` (one doc per workflow)

---

## 🗂️ Directory Layout

**Docs-only layout for this folder (recommended):**

~~~text
📁 .github/
├── 📁 workflows/                                        — Workflow YAML files (GitHub-discovered)
│   ├── 📄 <reusable_workflow>.yml                       — Reusable workflow (MUST live here)
│   └── 📁 reusable/                                     — Docs + conventions (NOT YAML workflows)
│       └── 📄 README.md                                 — ← This document
~~~

**Optional companion documentation layout (recommended):**

~~~text
📁 docs/
└── 📁 workflows/                                        — Human-readable workflow docs
    └── 📄 <reusable_workflow>.yml.md                    — One doc per workflow YAML
~~~

---

## 🧭 Context

### Why KFM uses reusable workflows

Reusable workflows help KFM keep CI behavior consistent across:
- code checks (lint/test/build),
- data pipeline checks (schema validation, deterministic ETL guards),
- documentation checks (Markdown protocol lint, governance links),
- security checks (secret scan, SBOM/provenance generation where applicable).

This supports the KFM “deterministic + governed” philosophy by reducing duplication and encouraging a single, reviewable contract.

### Reusable workflow vs composite action

- **Reusable workflow**: orchestrates **jobs**, runners, and environment permissions (`workflow_call`).
- **Composite action**: encapsulates **steps** and can live in subdirectories like `.github/actions/<name>/action.yml`.

Rule of thumb:
- Use **reusable workflows** when you need multi-job orchestration, caching, artifacts, or environments.
- Use **composite actions** when you need step reuse inside many workflows.

---

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A["Caller workflow"] --> B["Reusable workflow (workflow_call)"]
  B --> C["Jobs: lint/test/build/data-validate"]
  C --> D["Artifacts + reports"]
~~~

---

## 🧠 Story Node & Focus Mode Integration

Reusable workflow documentation is “Focus Mode friendly” when it is:
- explicit about inputs/outputs,
- explicit about provenance artifacts (reports, SBOMs, attestations),
- explicit about governance constraints (what is allowed to run, where secrets may be used).

Focus Mode MAY summarize these docs, but MUST NOT invent workflow behavior or security posture.

---

## 🧪 Validation & CI/CD

### Required security posture (KFM baseline)

**Least privilege by default.**  
Prefer setting default workflow permissions to read-only and escalating per-job only when necessary.

Example baseline:

~~~yaml
permissions:
  contents: read
~~~

### Secrets handling

- Never hardcode credentials.
- Only access secrets through `secrets.*`.
- Prefer passing only the minimum required secrets into a reusable workflow.
- If using inherited secrets, document it explicitly in the workflow’s companion doc.

### Local validation guidance

Recommended checks (as policy, adapt to actual repo tooling):
- workflow linting (YAML + action lint rules)
- secret scan (ensure examples contain no real tokens)
- markdown-lint / schema-lint for docs

---

## 📦 Data & Metadata

### Required documentation fields for each reusable workflow (recommended)

Maintain a small “workflow contract” section in the per-workflow doc:

- **File**: `.github/workflows/<name>.yml`
- **Triggers**: `workflow_call` (and any others if dual-purpose)
- **Inputs**: name/type/default/required
- **Secrets**: required vs optional (with descriptions)
- **Outputs**: names and meanings
- **Artifacts**: names, retention, intended consumers
- **Permissions**: minimum required scopes
- **Owners**: CODEOWNERS / review requirements
- **Evidence**: links to CI runs or example PRs (no secrets)

---

## 🌐 STAC, DCAT & PROV Alignment

Workflows are not STAC/DCAT datasets; however, CI outputs should still be provenance-aware.

If a workflow produces:
- SBOMs,
- attestations,
- run logs,
- validation reports,

…document where they are stored and how they are referenced by downstream governance/reporting systems.

---

## 🧱 Architecture

### Naming convention (recommended)

Use a stable naming scheme for callable workflows (file name and `name:` should align):

- `reusable__<domain>__<task>.yml`  
Examples:
- `reusable__python__tests.yml`
- `reusable__docs__markdown_lint.yml`
- `reusable__data__stac_validate.yml`

### Interface convention (recommended)

- Inputs are typed and documented.
- Secrets are enumerated (avoid “magic” secret usage).
- Outputs are explicitly mapped when needed.

Minimal “called” workflow skeleton:

~~~yaml
name: reusable__example__task

on:
  workflow_call:
    inputs:
      example_input:
        type: string
        required: false
        default: ""
    secrets:
      EXAMPLE_SECRET:
        required: false

permissions:
  contents: read

jobs:
  run:
    runs-on: ubuntu-latest
    steps:
      - name: Do the thing
        run: echo "ok"
~~~

Minimal “caller” skeleton:

~~~yaml
name: caller__example

on:
  pull_request:

jobs:
  call:
    uses: ./.github/workflows/reusable__example__task.yml
    with:
      example_input: "hello"
    secrets: inherit
~~~

> Note: `uses:` does not support dynamic expressions; keep workflow references explicit.

---

## ⚖ FAIR+CARE & Governance

### Non-negotiables

- No secrets or PII in docs or examples.
- Every reusable workflow must be auditable:
  - what it runs,
  - what it reads/writes,
  - what evidence it emits.

### Sovereignty awareness

If workflows process datasets with sensitivity controls, ensure:
- masking/generalization policies are applied before publishing artifacts,
- restricted outputs never get uploaded to public artifacts by default.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v1.0.0**  | 2025-12-13 | Initial README for reusable workflow conventions and documentation expectations. |

---

<div align="center">

♻️ **Reusable GitHub Actions Workflows — KFM**  
Deterministic Pipelines · Least Privilege · Governed CI

[🏠 Repo Root](../../../README.md) ·
[📘 Docs](../../../docs/README.md) ·
[📑 Standards](../../../docs/standards/README.md) ·
[🏛️ Governance](../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE](../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Sovereignty Policy](../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC‑BY 4.0

</div>

