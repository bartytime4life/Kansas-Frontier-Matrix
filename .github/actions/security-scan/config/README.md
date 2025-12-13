---
title: "🔍 Kansas Frontier Matrix — Security Scan Action Config"
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

json_schema_ref: "../../../../schemas/json/github-actions-security-scan-config-v11.schema.json"
shape_schema_ref: "../../../../schemas/shacl/github-actions-security-scan-config-v11-shape.ttl"

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

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧭 Context"
    - "📦 Data & Metadata"
    - "🧪 Validation & CI/CD"
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
---

<div align="center">

# 🔍 **KFM — Security Scan Action Config**
`.github/actions/security-scan/config/`

**Purpose**  
Document and govern the configuration that controls **dependency scanning**, **secret scanning**, and
(optional) **workflow hardening checks**.

</div>

---

## 📘 Overview

Security scanning is intentionally policy-driven. This config directory defines:

- Which tools are enabled
- Severity thresholds that fail CI
- Ignore rules (with governance justification)
- Workflow hardening policy rules for `.github/workflows/**`

This keeps outcomes deterministic and reviewable.

---

## 🗂️ Directory Layout

~~~text
.github/actions/security-scan/
└── 📁 config/                                  # Governed security scan configuration
    ├── 📄 README.md                            # ← This file
    ├── 🧾 tools.yml                            # Enabled tools, severity thresholds, ignore rules
    └── 🧾 workflow_policy.yml                  # Workflow hardening rules (permissions, pins, etc.)
~~~

---

## 🧭 Context

This config is consumed by:

- `.github/actions/security-scan/entrypoint.sh`
- `.github/actions/security-scan/scripts/run_dep_scans.py`
- `.github/actions/security-scan/scripts/run_secret_scans.py`
- `.github/actions/security-scan/scripts/summarize_results.py`

---

## 📦 Data & Metadata

### `tools.yml`

Typical settings:
- scanners enabled (dependency + secret scanning)
- severity thresholds (fail on critical/high)
- per-ecosystem toggles (python/node)
- ignore rules (with explicit rationale, expiration, and scope)

Example shape:

~~~yaml
dependency_scans:
  python:
    enabled: true
    tools: ["pip-audit", "osv-scanner"]
  node:
    enabled: true
    tools: ["npm-audit", "osv-scanner"]

thresholds:
  fail_on_critical: true
  fail_on_high: true
  fail_on_medium: false

ignore:
  - id: "CVE-0000-0000"
    reason: "False positive in transitive dependency; tracked in issue #123"
    scope: "python"
    expires: "2026-03-01"
~~~

### `workflow_policy.yml`

Defines hardening rules (examples):
- `permissions:` must be minimal
- actions must be pinned (no floating tags)
- prohibit unsafe events/patterns as governed

Example shape:

~~~yaml
workflow_policy:
  require_pinned_actions: true
  require_permissions_block: true
  deny_events:
    - "pull_request_target"
  deny_patterns:
    - "curl | bash"
~~~

---

## 🧪 Validation & CI/CD

Any config change MUST:
- be reviewed by the Security Council,
- update any relevant workflow docs,
- pass CI schema validation and markdown checks.

Config MUST NOT introduce:
- network endpoints,
- credentials,
- secret allowlists that weaken scanning without explicit governance.

---

## 🕰️ Version History

| Version | Date       | Summary                                                           |
|--------:|------------|-------------------------------------------------------------------|
| v11.2.3 | 2025-12-13 | Added config README; documented tools.yml and workflow policy rules. |

---

<div align="center">

🔍 **KFM — Security Scan Action Config (v11.2.3)**  
Policy-Driven DevSecOps · Deterministic Gates · Governed Exceptions  

[⬅ Security Scan Action](../README.md) · [🧱 Actions Library](../../README.md) · [⚖ Governance](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
