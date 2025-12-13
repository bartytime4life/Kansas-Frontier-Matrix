---
title: "🧩 Kansas Frontier Matrix — Security Scan Scripts"
path: ".github/actions/security-scan/scripts/README.md"
version: "v11.2.3"
last_updated: "2025-12-13"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · FAIR+CARE Security Council · Architecture Board"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.3/github-infra-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/github-workflows-v4.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

status: "Active / Enforced"
doc_kind: "Component Guide"
intent: "github-security-scan-scripts"
role: "security-scan-script-library"
category: "Security · CI/CD · Tooling"

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
  - ".github/actions/security-scan/scripts/README.md@v11.2.3"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "SoftwareSourceCode"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../schemas/json/github-actions-security-scan-scripts-v11.schema.json"
shape_schema_ref: "../../../../schemas/shacl/github-actions-security-scan-scripts-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:github-actions:security-scan:scripts:v11.2.3"
semantic_document_id: "kfm-action-security-scan-scripts"
event_source_id: "ledger:.github/actions/security-scan/scripts/README.md"
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
sunset_policy: "Superseded upon next security-scan scripts update"

prov_profile: "PROV-O Plan + KFM Governance Extensions"
openlineage_profile: "OpenLineage v2.5 · CI/CD and security pipeline events"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧭 Context"
    - "🧱 Architecture"
    - "📦 Data & Metadata"
    - "🧪 Validation & CI/CD"
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
  workflow: ".github/workflows/security_audit.yml"
  environment: "dev · staging · production"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"

fencing_profile: "outer-backticks-inner-tildes-v1"

requires_purpose_block: true
requires_version_history: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true
---

<div align="center">

# 🧩 **Kansas Frontier Matrix — Security Scan Scripts**  
`.github/actions/security-scan/scripts/`

**Purpose**  
Document the **governed helper scripts** used by the `security-scan` composite action to:

- Orchestrate dependency vulnerability scans across ecosystems  
- Orchestrate secret scanning with redaction guarantees  
- Normalize results into **machine-readable JSON** for policy evaluation & telemetry

</div>

---

## 📘 Overview

The `scripts/` directory contains **language-agnostic orchestration logic** (Python) invoked by:

- `.github/actions/security-scan/entrypoint.sh`  
- (Optionally) `.github/actions/security-scan/action.yml` when used as a composite action

These scripts are designed to be:

- **Deterministic**: same repo state + same config → same result and stable JSON ordering
- **Policy-aware**: severities and thresholds are evaluated against governed config
- **Safe**: secrets must never be printed; findings must be redacted or hashed
- **Composable**: each script can run independently and emits structured outputs

This directory is not a general-purpose CLI toolkit. It is the **internal implementation surface** of the governed action.

---

## 🗂️ Directory Layout

~~~text
.github/actions/security-scan/
└── 📁 scripts/                                    # Helper scripts for security-scan action
    ├── 📄 README.md                               # ← This file
    ├── 🧬 run_dep_scans.py                        # Dependency scanners orchestration + normalization
    ├── 🕵️ run_secret_scans.py                     # Secret scanners orchestration + redaction rules
    └── 📊 summarize_results.py                    # Aggregates tool outputs → policy summary JSON
~~~

> **Normative:** If a new script is added here, it MUST be:
> - referenced from `entrypoint.sh` (or documented as unused),
> - documented in this README under **Architecture**, and
> - covered by at least one CI check under **Validation & CI/CD**.

---

## 🧭 Context

The scripts in this folder sit inside the KFM CI/CD pipeline as part of the **security gate**:

- They implement “glue logic” between third-party scanners and KFM governance policies.
- They should be configured via governed inputs (repo configs), not via ad-hoc environment state.

Related documentation:

- Parent action README: `.github/actions/security-scan/README.md`
- Action config documentation (if present): `.github/actions/security-scan/config/README.md`
- Security governance: `.github/SECURITY.md` and `docs/security/**`
- Governance baseline: `docs/standards/governance/ROOT-GOVERNANCE.md`

---

## 🧱 Architecture

### Script responsibilities (normative contract)

| Script | Responsibility | Primary inputs | Primary outputs | Failure conditions |
|--------|----------------|----------------|-----------------|-------------------|
| `run_dep_scans.py` | Run dependency vulnerability scanners and normalize findings | repo path; tool config; ecosystem detection | JSON findings per tool + per ecosystem | scanner failure; invalid config; policy-relevant critical tool errors |
| `run_secret_scans.py` | Run secret scanners and enforce redaction rules | repo path; ignore patterns; optional history mode | JSON findings (redacted) per tool | any raw secret would be printed; scanner failure; policy-relevant secret hit |
| `summarize_results.py` | Aggregate findings into a single governed summary | dep-scan JSON; secret-scan JSON; thresholds | summary JSON (counts, max severity, decisions) | summary schema invalid; thresholds violated |

### Common interface conventions

All scripts SHOULD support:

- `--repo <path>`: root path to scan (typically `.` / `$GITHUB_WORKSPACE`)
- `--config <path>`: path to a governed config file or config directory
- `--output <path>`: file path where JSON output will be written
- `--format json`: fixed output format (default `json`)
- `--fail-on <severity>`: optional override for action-level wiring (governance-controlled)

If `--output` is omitted, scripts MAY emit JSON to stdout, but MUST NOT interleave logs with JSON.

### Example orchestration flow

~~~text
entrypoint.sh
  ├─ run_dep_scans.py      → _security-deps.json
  ├─ run_secret_scans.py   → _security-secrets.json
  └─ summarize_results.py  → _security-summary.json (and exit code)
~~~

### Exit code semantics

To keep behavior consistent across tools and workflows:

- `0` = success (no policy-relevant violations)
- `1` = policy violation (threshold exceeded, secret detected, etc.)
- `2` = execution/system error (misconfiguration, tool missing, parse error)

> **Normative:** A “tool crash” MUST NOT be silently downgraded to a passing status.

---

## 📦 Data & Metadata

### Normalized finding schema (recommended)

All tool outputs SHOULD normalize into:

~~~json
{
  "tool": "pip-audit",
  "tool_version": "X.Y.Z",
  "run": {
    "repo": ".",
    "started_at": "2025-12-13T00:00:00Z",
    "ended_at": "2025-12-13T00:00:30Z"
  },
  "findings": [
    {
      "id": "CVE-YYYY-NNNN",
      "type": "dependency_vulnerability",
      "severity": "critical",
      "package": {
        "name": "example",
        "version": "1.2.3",
        "ecosystem": "python"
      },
      "evidence": {
        "file": "requirements.txt",
        "line": 42
      },
      "links": [
        "https://osv.dev/vulnerability/..."
      ]
    }
  ],
  "counts": {
    "critical": 0,
    "high": 1,
    "medium": 2,
    "low": 3
  }
}
~~~

### Summary schema (recommended)

`summarize_results.py` SHOULD emit a single summary document:

~~~json
{
  "action": "security-scan",
  "version": "v11.2.3",
  "repo": ".",
  "issues_found": 3,
  "severity_max": "high",
  "policy": {
    "fail_on_critical": true,
    "fail_on_high": true,
    "fail_on_medium": false
  },
  "by_category": {
    "dependency_vulnerability": { "critical": 0, "high": 1, "medium": 2, "low": 0 },
    "secret": { "critical": 0, "high": 0, "medium": 0, "low": 0 }
  },
  "decision": {
    "status": "fail",
    "exit_code": 1,
    "reasons": [
      "High severity dependency vulnerability threshold exceeded"
    ]
  },
  "artifacts": {
    "dependency_report": "_security-deps.json",
    "secret_report": "_security-secrets.json"
  }
}
~~~

### Redaction requirements (non-negotiable)

Secret-related findings MUST:

- avoid printing raw secret values in JSON, logs, or GitHub step summaries
- store only **hashes**, **prefix/suffix fragments**, or **rule identifiers**
- mask any accidental exposure using GitHub masking (`::add-mask::`) if encountered

---

## 🧪 Validation & CI/CD

### Required CI behaviors

The scripts and their outputs MUST be compatible with:

- `.github/workflows/security_audit.yml` as the enforcing workflow gate
- repository secret scanning (CI) and PII scanning (CI) on documentation and outputs
- schema linting for any produced JSON summary (when checked in or published)

### Local runbook (developer workflow)

From repo root:

~~~bash
set -euo pipefail

python .github/actions/security-scan/scripts/run_dep_scans.py \
  --repo . \
  --config .github/actions/security-scan/config/tools.yml \
  --output _security-deps.json

python .github/actions/security-scan/scripts/run_secret_scans.py \
  --repo . \
  --config .github/actions/security-scan/config/tools.yml \
  --output _security-secrets.json

python .github/actions/security-scan/scripts/summarize_results.py \
  --repo . \
  --config .github/actions/security-scan/config/tools.yml \
  --deps _security-deps.json \
  --secrets _security-secrets.json \
  --output _security-summary.json
~~~

> **Note:** The exact scanner binaries invoked (and their versions) are governance-controlled and
> should be pinned by the action’s dependency management approach.

---

## ⚖ FAIR+CARE & Governance

These scripts are part of the **security boundary** and MUST adhere to governance constraints:

- **No secrets / no PII** in logs, JSON outputs, or artifacts
- **Minimal disclosure**: findings should be actionable without exposing sensitive values
- **Deterministic reporting**: stable ordering, stable severity mapping, stable output schema
- **Sovereignty-aware posture**: scanning output MUST NOT reveal sensitive locations, restricted
  identifiers, or protected cultural knowledge if present in repository artifacts

If a scan discovers content that appears to violate sovereignty protections or privacy constraints:

- treat it as a governed incident (see `.github/SECURITY.md`)
- redact outputs immediately and fail closed where required by policy

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.3 | 2025-12-13 | Initial governed documentation for `security-scan` helper scripts: interfaces, schemas, redaction rules. |

---

<div align="center">

🧩 **KFM — Security Scan Scripts (v11.2.3)**  
Deterministic Orchestration · Redaction-Safe · Governance-Enforced  

[⬅ Security Scan Action](../README.md) · [⬅ Composite Actions Library](../../README.md) · [🛡 Security Policy](../../../SECURITY.md) · [⚖ Governance](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

