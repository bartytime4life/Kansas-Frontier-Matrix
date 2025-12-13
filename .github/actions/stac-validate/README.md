---
title: "🔧 Kansas Frontier Matrix — Security Scan Configuration"
path: ".github/actions/security-scan/config/README.md"
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
doc_kind: "Guide"
intent: "github-security-scan-action-config"
role: "security-scan-config"
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
  - ".github/actions/security-scan/config/README.md@v11.2.3"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "SoftwareApplication"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../schemas/json/github-actions-security-scan-v11.schema.json"
shape_schema_ref: "../../../../schemas/shacl/github-actions-security-scan-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:github-actions:security-scan:config:v11.2.3"
semantic_document_id: "kfm-action-security-scan-config"
event_source_id: "ledger:.github/actions/security-scan/config/README.md"
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
sunset_policy: "Superseded upon next security-scan config update"

prov_profile: "PROV-O Plan + KFM Governance Extensions"
openlineage_profile: "OpenLineage v2.5 · CI/CD and security pipeline events"
---

<div align="center">

# 🔧 **Kansas Frontier Matrix — Security Scan Configuration**
`.github/actions/security-scan/config/`

**Purpose**  
Define the **governed configuration surface** for the `security-scan` composite action — including
tool enablement, severity thresholds, ignore rules, and workflow-hardening policy.

This configuration is designed to be:

- **Deterministic** — same repo + same config → same policy decision.
- **Config-driven** — workflows pass *inputs*, config files hold *policy*.
- **Auditable** — changes are reviewable, versioned, and governance-linked.

</div>

---

## 📘 Overview

This directory contains **policy configuration** consumed by `.github/actions/security-scan/entrypoint.sh`
(and any helper scripts) to standardize security scanning behavior across KFM workflows.

### What belongs here

- Tool selection and enablement flags (dependency/secret/workflow scanners).
- Severity thresholds (fail vs warn vs ignore).
- Ignore rules (scoped and justified; never blanket-ignores).
- Workflow hardening rules (permissions, pinned actions, disallowed events).

### What must NOT belong here (normative)

- Secrets, credentials, tokens, or private keys.
- PII/PHI.
- Any data that would violate sovereignty policy or governance constraints.

### Precedence (normative)

When multiple configuration sources are present, apply precedence in this order:

1. **Workflow inputs** (explicit per-run overrides)
2. **Repository config files** in this directory
3. **Action defaults** (embedded fallbacks)

---

## 🗂️ Directory Layout

~~~text
.github/
└── 📁 actions/                                        # Reusable composite actions
    └── 📁 security-scan/                              # Consolidated security scan action
        └── 📁 config/                                 # ← Governed policy configuration
            ├── 📄 README.md                           # ← This file
            ├── 🧾 tools.yml                           # Tool enablement + thresholds + ignore rules
            └── 🧾 workflow_policy.yml                 # Workflow hardening rules (permissions, pins, events)
~~~

---

## 🧱 Architecture

### 1) `tools.yml` contract (normative)

`tools.yml` defines:

- Which scanners run
- How findings are classified
- What severities are policy-relevant
- What (limited, scoped) ignore rules exist

Recommended shape:

~~~yaml
version: "v11"
defaults:
  fail_on:
    critical: true
    high: true
    medium: false
    low: false
  redact_logs: true

dependency_scanning:
  enabled: true
  tools:
    pip_audit:
      enabled: true
      args: []
    npm_audit:
      enabled: true
      args:
        - "--audit-level=high"

secret_scanning:
  enabled: true
  scan_history: false
  tools:
    gitleaks:
      enabled: true
      args: []
ignore:
  vulnerabilities:
    - id: "CVE-2099-0000"
      reason: "False positive (validated by maintainers); tracked in issue #<id>."
      expires: "2026-06-30"
  paths:
    - pattern: "data/processed/**"
      reason: "Generated artifacts (must still be secret-scanned upstream before landing)."
      expires: "2026-06-30"
outputs:
  summary_json: "_security-summary.json"
~~~

**Rules:**

- `ignore.*` entries MUST include a **reason** and an **expiry**.
- Ignore rules MUST be **narrowly scoped** (IDs or paths) and MUST NOT disable whole classes of scanning.
- If `outputs.summary_json` is set, the action SHOULD write a machine-readable summary at that path.

### 2) `workflow_policy.yml` contract (normative)

`workflow_policy.yml` defines workflow hardening checks for `.github/workflows/**`.

Recommended shape:

~~~yaml
version: "v11"
workflow_hardening:
  enabled: true

  require_minimal_permissions: true
  require_pinned_actions: true

  disallow_events:
    - "pull_request_target"

  required_permissions:
    contents: "read"

  allow_unpinned_actions:
    - "actions/checkout@v4"
    - "actions/setup-python@v5"
~~~

**Rules:**

- If `require_pinned_actions: true`, workflows MUST NOT use floating tags except those explicitly allowlisted.
- `disallow_events` violations MUST be treated as policy-relevant failures unless explicitly waived by governance.

### 3) JSON Schema alignment (normative)

Any additions or changes to the configuration surface MUST be reflected in:

- `schemas/json/github-actions-security-scan-v11.schema.json`
- `schemas/shacl/github-actions-security-scan-v11-shape.ttl`

---

## 🧪 Validation & CI/CD

### Local sanity checks (recommended)

- Validate YAML syntax (`tools.yml`, `workflow_policy.yml`).
- Run the action entrypoint against a known-safe path and confirm:
  - Fail/warn behavior matches configured thresholds
  - Ignore rules apply only where expected
  - No raw secrets appear in logs

### CI expectations (normative)

- CI MUST fail if:
  - YAML is invalid
  - Schema/shape validation fails
  - Ignore rules are missing `reason` or `expires`
  - Workflow hardening rules are violated (when enabled)

---

## ⚖ FAIR+CARE & Governance

- Changes to thresholds and ignores are **governance-relevant**.
- Any ignore rule that suppresses a **critical/high** finding MUST be:
  - time-limited (`expires`)
  - justified (`reason`)
  - traceable (issue/ticket link where applicable)
- Telemetry generated from these configs MUST remain non-sensitive (no secrets, no PII, no sensitive locations).

---

## 🕰️ Version History

| Version | Date       | Summary                                                                 |
|--------:|------------|-------------------------------------------------------------------------|
| v11.2.3 | 2025-12-13 | Initial governed README for `security-scan/config`; defined config contracts. |

---

<div align="center">

🔧 **Kansas Frontier Matrix — Security Scan Configuration (v11.2.3)**  
Policy-as-Code · FAIR+CARE-Governed · CI-Safe  

[⬅ Security Scan Action README](../README.md) · [⬅ GitHub Infra Overview](../../README.md) · [🛡 Security Policy](../../../SECURITY.md) · [📚 Security Governance](../../../../docs/security/README.md)

</div>
