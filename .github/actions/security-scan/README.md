---
title: "🔍 Kansas Frontier Matrix — Security Scan Composite Action"
path: ".github/actions/security-scan/README.md"
version: "v11.2.4"
last_updated: "2025-12-13"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · FAIR+CARE Security Council · Architecture Board"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../releases/v11.2.4/github-infra-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/github-workflows-v4.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

status: "Active / Enforced"
doc_kind: "Guide"
intent: "github-security-scan-action"
role: "security-scan-composite-action"
category: "Security · CI/CD · Composite Action"

classification: "Public Document"
sensitivity: "General (non-sensitive)"
sensitivity_level: "Low"
public_exposure_risk: "Low"
risk_category: "Security"
indigenous_rights_flag: false
redaction_required: false
data_steward: "KFM FAIR+CARE Security Council"

fair_category: "F1-A1-I1-R1"
care_label: "Collective Benefit · Authority to Control · Responsibility · Ethics"

provenance_chain:
  - ".github/actions/security-scan/README.md@v11.2.3"
  - ".github/actions/security-scan/README.md@v11.2.2"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "SoftwareApplication"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../schemas/json/github-actions-security-scan-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/github-actions-security-scan-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:github-actions:security-scan:v11.2.4"
semantic_document_id: "kfm-action-security-scan"
event_source_id: "ledger:.github/actions/security-scan/README.md"
immutability_status: "mutable-plan"
machine_extractable: true

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "metadata-extraction"
ai_transform_prohibited:
  - "speculative-additions"
  - "governance-override"
  - "content-alteration"

accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "United States / Kansas"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next security-scan action update"

prov_profile: "PROV-O Plan + KFM Governance Extensions"
openlineage_profile: "OpenLineage v2.5 · CI/CD and security pipeline events"
---

<div align="center">

# 🔍 **Kansas Frontier Matrix — Security Scan Composite Action**
`.github/actions/security-scan/`

**Purpose**  
Provide a **single, governed entrypoint** for repository‑wide security scanning in KFM CI/CD, including:

- Dependency vulnerability scanning (Python, Node, etc.)
- Secret/credential leakage detection
- Basic workflow hardening & policy checks

This action is typically invoked by:

- `.github/workflows/security_audit.yml` → **governed security gate** for KFM.

</div>

---

## 📘 Overview

The `security-scan` action encapsulates KFM’s **baseline security checks**:

- Normalizes **dependency vulnerability scans** across ecosystems.
- Runs **secret scanning** against the repository (including history, where allowed).
- Optionally enforces **workflow hardening** rules (minimal permissions, pinned actions, etc.).
- Produces **machine-readable results** that can be summarized into CI telemetry and governance dashboards.

It is intended to be:

- **Deterministic** — same inputs → same exit status.
- **Config-driven** — behavior controlled via config files (e.g., `config/security/*.yml`).
- **Composable** — can be reused from any workflow needing a consolidated security pass.

The action MUST fail (exit non‑zero) when a **policy‑relevant violation** is detected (e.g., critical CVEs, hardcoded secrets), so that upstream workflows (e.g., `security-audit`) can block merges or releases.

---

## 🗂️ Directory Layout

~~~text
.github/
├── 📁 actions/                               — Reusable composite actions
│   └── 📁 security-scan/                     — Consolidated security scan action
│       ├── 📄 README.md                      — ← This file (governance & usage)
│       ├── 📄 action.yml                     — GitHub Action descriptor (composite / shell)
│       ├── 📄 entrypoint.sh                  — Main orchestrator script (bash)
│       ├── 📁 config/                        — Optional local security policy config
│       │   ├── 🧾 tools.yml                  — Enabled tools, severity thresholds, ignore rules
│       │   └── 🧾 workflow_policy.yml        — Workflow hardening rules (permissions, pins, etc.)
│       └── 📁 scripts/                       — Helper scripts (optional, language-agnostic)
│           ├── 📄 run_dep_scans.py           — Orchestrates dependency scanners
│           ├── 📄 run_secret_scans.py        — Orchestrates secret scanners
│           └── 📄 summarize_results.py       — Aggregates results → machine-readable summary
└── 📁 workflows/                             — CI/CD workflows
    └── 🧾 security_audit.yml                 — Governed security gate workflow (invokes this action)
~~~

> **Normative:** Any structural change to this directory MUST be reflected here and in  
> `.github/workflows/security_audit.yml` and relevant security docs under `docs/security/`.

---

## 🧱 Architecture

### Action invocation patterns

Within the KFM repository this action MAY be used in two equivalent forms:

1. **Direct script invocation** (current pattern in `security_audit.yml`):

~~~yaml
- name: 🔐 Consolidated Security Scan (Composite Action)
  run: |
    set -euo pipefail
    bash .github/actions/security-scan/entrypoint.sh .
~~~

2. **Composite action usage** (if `action.yml` is defined as a composite action):

~~~yaml
- name: 🔐 Consolidated Security Scan
  uses: ./.github/actions/security-scan
  with:
    path: .
~~~

> The repo MUST treat these two forms as equivalent in behavior. If `action.yml` is added or changed,  
> `security_audit.yml` MUST be updated to use the canonical interface.

### Inputs (proposed, for `action.yml`)

| Name                  | Type    | Default | Description                                                              |
|-----------------------|---------|---------|--------------------------------------------------------------------------|
| `path`                | string  | `.`     | Root path to scan (usually the repo root).                               |
| `config`              | string  | `""`    | Optional security config file (e.g., `config/security/tools.yml`).       |
| `fail_on_critical`    | boolean | `true`  | Fail the job when critical issues are found.                             |
| `fail_on_high`        | boolean | `true`  | Fail the job when high‑severity issues are found.                        |
| `fail_on_medium`      | boolean | `false` | Optionally fail on medium issues (governance‑controlled).                |
| `secret_scan_history` | boolean | `false` | If `true`, scan git history (may be expensive).                          |
| `output_summary`      | string  | `""`    | Optional path for a JSON summary file (e.g., `_security-summary.json`).  |

> **Schema note:** These inputs MUST be reflected in the JSON Schema at  
> `schemas/json/github-actions-security-scan-v11.schema.json`.

### Outputs (proposed)

| Name           | Type   | Description                                                    |
|----------------|--------|----------------------------------------------------------------|
| `issues_found` | number | Total number of policy‑relevant issues discovered.            |
| `severity_max` | string | Highest severity observed (e.g., `none`, `low`, `medium`).    |
| `summary_path` | string | Path to JSON summary if produced (e.g., `_security-summary.json`). |

These outputs are mainly intended for internal workflows (e.g., telemetry aggregation).

### Execution flow

At a high level:

1. **Dependency scans**
   - Python: `pip-audit`, `osv-scanner`, or equivalent.
   - Node: `npm audit` (with scripts disabled), `osv-scanner` if configured.
   - Additional ecosystems configurable via `config/security/tools.yml`.

2. **Secret scans**
   - Use one or more scanners (e.g., `gitleaks`, `trufflehog`) configured by KFM policy.
   - Redact or hash secrets in logs (never print raw secrets).

3. **Workflow hardening checks (optional)**
   - Validate `.github/workflows/**` against `workflow_policy.yml`:
     - Minimal `permissions:` blocks.
     - Pinned actions rather than floating tags.
     - No unsafe `pull_request_target` usage.

4. **Policy evaluation**
   - Severity thresholds and ignore rules pulled from `config/security/tools.yml`.
   - Exit non‑zero if thresholds are violated.

5. **Summary output**
   - Optionally write a **JSON summary file** (issues, severities, counts per tool).
   - Designed to be consumed later by `telemetry_export.yml` and security dashboards.

### Implementation notes

- `entrypoint.sh` SHOULD:
  - Enable strict bash flags (`set -euo pipefail`).
  - Orchestrate sub‑tools via `scripts/*.py` or CLI tools.
  - Normalize exit codes into a single governed result.

- `scripts/run_dep_scans.py` (if present) SHOULD:
  - Read tool configuration (e.g., which ecosystems to scan).
  - Produce structured JSON on stdout or in a file.

- `scripts/run_secret_scans.py` SHOULD:
  - Honor ignore lists and redaction policies.
  - Avoid uploading raw secrets to logs or artifacts.

- `scripts/summarize_results.py` SHOULD:
  - Merge multiple tool outputs into a unified schema.
  - Respect configured severity thresholds.

Any change to tool selection, thresholds, or policy interpretation MUST be:

1. Reflected in `config/security/*.yml`.
2. Documented here under **Execution flow**.
3. Tested via `security_audit.yml` and, where appropriate, `docs/security/` examples.

---

## 🧪 Validation & CI/CD

### Example usage

#### From `security_audit.yml` (script invocation)

~~~yaml
- name: 🔐 Consolidated Security Scan (Composite Action)
  run: |
    set -euo pipefail
    if [[ ! -d ".github/actions/security-scan" ]]; then
      echo "::error::Missing .github/actions/security-scan directory."
      exit 1
    fi
    bash .github/actions/security-scan/entrypoint.sh .
~~~

#### As a composite action (recommended long‑term pattern)

~~~yaml
jobs:
  security-audit:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4

      - name: 🔐 Security Scan
        uses: ./.github/actions/security-scan
        with:
          path: .
          config: "config/security/tools.yml"
          fail_on_critical: true
          fail_on_high: true
          fail_on_medium: false
          secret_scan_history: false
          output_summary: "_security-summary.json"
~~~

### Pass/fail contract

- The action MUST fail (exit non‑zero) on **policy‑relevant violations** (severity thresholds, secrets detected, workflow-policy violations).
- The action SHOULD emit a single summarized result (stdout + optional JSON file) suitable for downstream parsing.
- The action MUST NOT leak secrets, credentials, or PII in logs or artifacts.

---

## 📦 Data & Metadata

This action contributes to:

- `security_audit.yml` job status and logs.
- Telemetry metrics (via `telemetry_export.yml`), including:
  - Number of vulnerabilities by severity.
  - Count of secrets detected or blocked.
  - Workflow-policy violations.

Telemetry should never contain:

- Raw secrets or credentials.
- Direct PII/PHI.
- Exact locations or identifiers from sensitive sovereign datasets.

Where needed, summary metrics SHOULD be anonymized or bucketed.

---

## 🌐 STAC, DCAT & PROV Alignment

### DCAT

- This document can be modeled as a documentation dataset (`dcat:Dataset` or `dcat:CatalogRecord`).
- `semantic_document_id` maps to `dct:identifier`.
- Markdown is a `dcat:Distribution` (`mediaType: text/markdown`).

### PROV-O

- This document is a `prov:Plan` (see `ontology_alignment.prov_o`).
- Each run of the security scan is a `prov:Activity`.
- CI bots, councils, and maintainers are `prov:Agent`s.
- Produced telemetry and summaries are `prov:Entity` instances linked with `prov:wasGeneratedBy`.

---

## ⚖ FAIR+CARE & Governance

This action is **governance-bound** and contributes to supply-chain integrity:

- Violations with release or merge impact MUST be treated as **policy-relevant** and enforceable.
- Governance and ethics references in front‑matter are **binding** and must remain accurate:
  - `governance_ref`
  - `ethics_ref`
  - `sovereignty_policy`

**Redaction is mandatory** for any secret-scan output. Do not print raw secrets or tokens under any circumstances.

---

## 🕰️ Version History

| Version | Date       | Summary                                                                                                   |
|--------:|------------|-----------------------------------------------------------------------------------------------------------|
| v11.2.4 | 2025-12-13 | Aligned headings and fencing with KFM-MDP v11.2.6; normalized directory-tree icons; clarified CI contract. |
| v11.2.3 | 2025-12-09 | Aligned with KFM-MDP v11.2.5; documented inputs/outputs; clarified composite vs script usage.             |
| v11.2.2 | 2025-11-28 | Initial governed README for security-scan; aligned with `security_audit.yml` and security policy.          |

---

<div align="center">

🔍 **Kansas Frontier Matrix — Security Scan Composite Action (v11.2.4)**  
Secure by Design · FAIR+CARE-Governed · Supply-Chain Aware  

[⬅ GitHub Infra Overview](../../README.md) · [🛡 Security Policy](../../SECURITY.md) · [📚 Security Governance](../../../docs/security/README.md)

</div>
