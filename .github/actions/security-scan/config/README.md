---
title: "⚙️ Kansas Frontier Matrix — Security Scan Configuration"
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
intent: "security-scan-config"
role: "security-scan-config"
category: "Security · CI/CD · Configuration"

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
  schema_org: "TechArticle"
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
sunset_policy: "Superseded upon next security-scan config schema update"

prov_profile: "PROV-O Plan + KFM Governance Extensions"
openlineage_profile: "OpenLineage v2.5 · CI/CD and security pipeline events"
---

<div align="center">

# ⚙️ **Kansas Frontier Matrix — Security Scan Configuration**
`.github/actions/security-scan/config/`

**Purpose**  
Define the **governed, repo-local configuration** used by the KFM `security-scan` composite action to run:

- Dependency vulnerability scans (Python, Node, etc.)
- Secret/credential leakage detection
- Workflow hardening & policy checks

</div>

---

## 📘 Overview

This folder contains the **default configuration** for the `security-scan` action.

### What belongs here

- **Policy knobs** (what tools run, what counts as a failure, what is ignored under governance).
- **Machine-readable, diff-friendly** YAML configurations.
- **Non-sensitive** configuration only (no secrets, tokens, credentials, PII).

### What does NOT belong here

- Secrets (ever).
- “Temporary” bypasses without documentation (use governed ignore entries with reason + expiration).
- Tool output artifacts (those should be produced per-run by workflows and stored as CI artifacts when needed).

---

## 🗂️ Directory Layout

~~~text
.github/
└── 🧱 actions/
    └── 🔍 security-scan/
        └── ⚙️ config/
            ├── 📄 README.md               — This file (what configs exist + how to use them)
            ├── 🧾 tools.yml               — Tool enablement, thresholds, ignore rules, scan scope
            └── 🧾 workflow_policy.yml     — Workflow hardening rules for `.github/workflows/**`
~~~

---

## 🧭 Context

The `security-scan` action is designed to be **config-driven**.

### Configuration resolution (expected contract)

A workflow or script invoking the action SHOULD follow this precedence:

1. **Explicit config path** (via action input like `config: ...`, or script argument/env var if implemented)
2. **Repo-local default** config in this directory
3. **Action defaults** (only if no config files are present)

If the implementation deviates from this contract, update this README and the action README (`../README.md`) to match.

### Typical usage patterns

**Use the repo-local defaults** (most common):

~~~bash
bash .github/actions/security-scan/entrypoint.sh .
~~~

**Override with a custom config** (e.g., in a workflow):

~~~yaml
- name: 🔐 Security Scan
  uses: ./.github/actions/security-scan
  with:
    path: .
    config: ".github/actions/security-scan/config/tools.yml"
~~~

---

## 📦 Data & Metadata

All configuration files here are YAML and MUST remain:

- **Deterministic in interpretation** (same config + same repo state ⇒ same policy evaluation rules)
- **Governance-auditable** (ignore rules have reason + expiry; thresholds are explicit)
- **Non-sensitive** (no tokens, no credentials, no secret patterns that reveal real secrets)

### `tools.yml` contract

`tools.yml` defines:

- Which scanners are enabled
- What severities fail CI
- Ignore rules (with justification + expiration)
- Path scopes (optional) for targeted scans

Minimal example (illustrative):

~~~yaml
version: "v11"
policy:
  fail_on:
    critical: true
    high: true
    medium: false
    low: false

scopes:
  root: "."
  include:
    - "src/**"
    - "docs/**"
  exclude:
    - "data/**"
    - "mcp/runs/**"

dependency_scans:
  python:
    enabled: true
    tools:
      pip_audit:
        enabled: true
      osv_scanner:
        enabled: true

  node:
    enabled: true
    tools:
      npm_audit:
        enabled: true
        production_only: true

secret_scans:
  enabled: true
  tools:
    gitleaks:
      enabled: true
      scan_history: false

ignore:
  vulnerabilities:
    - id: "CVE-2099-0000"
      reason: "False positive (documented in upstream issue #1234)."
      expires: "2026-01-01"
  secrets:
    - fingerprint: "EXAMPLE_FINGERPRINT_HASH"
      reason: "Test fixture string (non-secret), validated by Security Council."
      expires: "2026-01-01"
~~~

**Normative: ignore entries MUST include `reason` and `expires`.**

### `workflow_policy.yml` contract

`workflow_policy.yml` defines guardrails for `.github/workflows/**`, such as:

- Minimal permissions requirements
- Action pinning rules
- Disallowed events/anti-patterns (e.g., unsafe usage patterns)

Minimal example (illustrative):

~~~yaml
version: "v11"
workflow_hardening:
  enabled: true

permissions:
  require_explicit_block: true
  default_read_only: true

actions:
  require_pinning: true
  pinning_mode: "sha"   # allowed values should be validated by the implementation

events:
  deny:
    - "pull_request_target"

paths:
  include:
    - ".github/workflows/**"
~~~

**Normative: policy MUST prefer least privilege and reproducible action references.**

---

## 🧪 Validation & CI/CD

### Where this is enforced

- Primary workflow gate (expected): `.github/workflows/security_audit.yml`
- The action README (`../README.md`) documents how `security-scan` is invoked and how failures block merges/releases.

### Minimum checks that MUST remain true

- This README remains KFM-MDP compliant (front-matter, headings, version history).
- Config files do not contain secrets/credentials.
- Changes to thresholds/ignore rules are reviewable in diff form and have documented rationale.

### Quick local validation

From repo root:

~~~bash
bash .github/actions/security-scan/entrypoint.sh .
~~~

---

## ⚖ FAIR+CARE & Governance

Security configuration is **governed** because it changes what KFM treats as “acceptable risk.”

### Governance expectations

- Severity thresholds SHOULD be stable and changed only with explicit rationale.
- Ignore rules MUST be:
  - Specific (avoid broad wildcards),
  - Time-bounded (`expires`),
  - Justified (`reason`),
  - Reviewable by the Security Council (and other required bodies per governance).

### Sovereignty and sensitive data

Even though these configs are “just CI,” they MUST NOT introduce mechanisms that:

- Leak sensitive locations, protected datasets, or restricted identifiers into logs or telemetry,
- Encourage collection of raw secrets/PII in scan outputs.

---

## 🕰️ Version History

| Version | Date       | Summary                                                                 |
|--------:|------------|-------------------------------------------------------------------------|
| v11.2.3 | 2025-12-13 | Initial governed README for `security-scan` configuration (`tools.yml`, `workflow_policy.yml`). |

---

<div align="center">

⚙️ **Kansas Frontier Matrix — Security Scan Configuration (v11.2.3)**  
Secure by Design · FAIR+CARE-Governed · Policy-as-Code  

[⬅ Security Scan Action](../README.md) · [🛡 Security Policy](../../../SECURITY.md) · [📚 Security Governance](../../../../docs/security/README.md)

</div>

