---
title: "🌦️ Kansas Frontier Matrix — AI Environment Overlay Profiles"
path: "tools/ai/configs/environments/README.md"

version: "v11.2.6"
last_updated: "2025-12-15"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous · FAIR+CARE Council Oversight"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Architecture"
header_profile: "standard"
footer_profile: "standard"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:doc:tools-ai-configs-environments-readme:v11.2.6"
semantic_document_id: "kfm-doc-tools-ai-configs-environments"
event_source_id: "ledger:tools/ai/configs/environments/README.md"
immutability_status: "mutable-plan"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/tools-ai-governance-v4.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I2-R3"
care_label: "Public · Low-Risk"
classification: "Public"
jurisdiction: "United States · Kansas"
sensitivity: "General"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_data_flag: false

ai_training_allowed: false
ai_training_guidance: "Environment overlay profiles and policy configs MUST NOT be used as training data."

machine_readable: true
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "Annual review"
sunset_policy: "Superseded upon next AI-tools platform update"
---

<div align="center">

# 🌦️ **KFM — AI Environment Overlay Profiles**
`tools/ai/configs/environments/README.md`

**Purpose**  
Define how **environment-specific configuration overlays** are authored and applied for AI governance tooling—so `dev`, `staging`, and `production` can differ operationally **without weakening** FAIR+CARE, sovereignty, and certification requirements.

</div>

---

## 📘 Overview

### What “environment overlays” are

Environment overlays are **governed configuration fragments** applied on top of:

- base profiles in `tools/ai/configs/`
- optional domain overlays in `tools/ai/configs/domains/`

They exist to support operational differences between environments, such as:

- faster iteration in `dev`
- realistic rehearsal in `staging`
- strict gating and release-grade enforcement in `production`

Environment overlays must remain **policy-safe** and **deterministic**.

### What environment overlays can change (allowed)

An environment overlay MAY:

- change **monitoring cadence** (e.g., run drift checks more frequently in prod)
- change **logging verbosity** (without including sensitive data)
- change **artifact destinations** (within governed allowed destinations)
- change **alerting/escalation routing** (e.g., require review in prod)
- set environment identifiers and tags used in telemetry/provenance

Environment overlays SHOULD NOT:

- change fairness/explainability/drift thresholds in ways that weaken safety
- disable required audits for promotion/certification
- allow publication of restricted artifacts

### What environment overlays MUST NOT change (forbidden)

Environment overlays MUST NOT:

- bypass governance (no “skip audits” flags for production)
- weaken sovereignty policy
- reduce required telemetry completeness for certification paths
- introduce secrets, PII, protected-site coordinates, or raw sensitive samples

---

## 🗂️ Directory Layout

This directory is a subdivision of `tools/ai/configs/`:

~~~text
📁 tools/
└── 🧠 ai/
    └── 📁 configs/
        ├── 📄 README.md                            # Config system overview
        ├── 📁 domains/                              # Domain overlays (optional)
        └── 📁 environments/                         # Environment overlays (this directory)
            └── 📄 README.md                         # This file
~~~

Recommended environment file naming convention:

- `<env>.json` where `<env>` ∈ `{dev, staging, production}`

Example:

~~~text
dev.json
staging.json
production.json
~~~

If your repo uses a different environment taxonomy, document it here and keep the naming stable.

---

## 🧭 Context

### Why environment overlays are tightly constrained

It is common for teams to want “looser rules” in dev.  
In KFM, governance rules are designed so that:

- experimentation is allowed,
- but certification and promotion remain protected.

Therefore, environment overlays should change **how** things are measured and routed, not **whether** they are measured or whether policy applies.

A safe pattern is:

- dev: allow WARN to pass for non-certification experiments, but always record warnings and provenance
- staging: mimic production gates
- production: strict fail-closed gating, strong review escalation

### Selection source (recommended)

Environment overlays should be selected via:

- CI environment variables
- pipeline execution context (dev/staging/prod)
- explicit CLI flag (authorized use only)

Selection must be recorded in:

- telemetry (`environment: "dev|staging|production"`)
- provenance bundles (agent/activity context)

### Overlay application order

Recommended precedence (lowest → highest):

1. **Base profile**
2. **Domain overlay** (if applicable)
3. **Environment overlay**
4. **Explicit CLI override** (rare; must be logged; should not be allowed in production)

---

## 🧱 Architecture

### Merge semantics (recommended)

Environment overlays should be applied via controlled deep-merge with an allow-list of keys:

Allowed override categories:

- `runtime` (timeouts, sampling limits — but never masking safety rules)
- `cadence` (drift check frequency)
- `actions` (escalation routing; stricter in prod)
- `telemetry` (tags and required fields; never fewer fields in prod)
- `artifact_policy` (where artifacts are stored; must remain within governed destinations)

Forbidden override categories:

- disabling audits required by governance
- removing required metrics for certification
- reducing policy safety constraints
- reducing telemetry completeness for certification paths

### Recommended environment policy patterns

**dev**
- allow reduced sampling sizes (for speed) *when not certifying*
- always emit telemetry + provenance
- WARN may be allowed for internal experiments, but must be recorded

**staging**
- match production thresholds and required audits
- validate release packaging and artifact destinations
- require review on WARN

**production**
- strict fail-closed
- require drift cadence appropriate to the system
- require review or block on WARN/FAIL based on governance actions policy
- never allow overrides that reduce safety

---

## 🧪 Validation & CI/CD

### Overlay requirements (normative)

Every environment overlay MUST:

- be valid JSON
- include a `meta` block with:
  - `profile_id`
  - `profile_version`
  - `profile_kind: "environment"`
  - `environment` (dev/staging/production)
  - `overlay_of` (base profile id/version or “merged baseline” id)
  - `last_updated`
  - governance references

- pass safety checks:
  - no secrets
  - no PII
  - no protected-site coordinates
  - no raw samples

### Required audit output linkage (normative)

Any run that applies an environment overlay MUST record:

- `config_environment_overlay_path`
- `config_environment_overlay_profile_id`
- `config_environment_overlay_version`
- `config_environment_overlay_sha256`
- `environment` tag

### Recommended CI checks

CI SHOULD enforce:

- schema validation for environment overlays
- merge validation (ensure required metrics/audits are not disabled)
- safety scan (no secrets/PII)
- production guardrails:
  - fail CI if production overlay attempts to weaken governance constraints

---

## 📦 Data & Metadata

### Environment overlay contract (recommended)

Minimum recommended `meta` block:

~~~json
{
  "meta": {
    "profile_id": "environment.production",
    "profile_version": "11.2.6",
    "profile_kind": "environment",
    "environment": "production",
    "overlay_of": "baseline_merged@11.2.6",
    "owner_role": "ai-governance-registry",
    "last_updated": "2025-12-15",
    "governance_ref": "../../../../docs/standards/governance/ROOT-GOVERNANCE.md",
    "ethics_ref": "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md",
    "sovereignty_policy": "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
  }
}
~~~

Example overlay snippet (illustrative):

~~~json
{
  "meta": {
    "profile_id": "environment.staging",
    "profile_version": "11.2.6",
    "profile_kind": "environment",
    "environment": "staging",
    "overlay_of": "baseline_merged@11.2.6",
    "owner_role": "ai-governance-registry",
    "last_updated": "2025-12-15"
  },
  "cadence": {
    "drift_check": "30d"
  },
  "actions": {
    "on_warn": ["require_review"],
    "on_fail": ["block_certification"]
  },
  "telemetry": {
    "required_fields_add": ["environment", "run_type"]
  },
  "artifact_policy": {
    "run_root_preferred": "mcp/experiments",
    "publish_summaries": false
  }
}
~~~

Notes:

- Use additive keys (e.g., `required_fields_add`) rather than deleting required fields.
- Any “publish_summaries” setting must remain consistent with governance.

---

## 🌐 STAC, DCAT & PROV Alignment

Environment overlays should help preserve reproducibility by:

- ensuring telemetry/provenance records include environment tags
- keeping artifact destinations consistent
- preventing environment-specific behavior from becoming invisible drift

If release packaging happens in production, include environment overlay identity in:

- provenance bundles
- release telemetry snapshots

---

## ⚖ FAIR+CARE & Governance

### Policy constraints (normative)

Environment overlays must comply with:

- `governance_ref`
- `ethics_ref`
- `sovereignty_policy`

They must never be used to bypass sovereign protections or weaken audit requirements for promotion.

### Production guardrail (normative)

Production overlays MUST:

- enforce strict fail-closed behavior for certification paths
- never reduce safety constraints or required audits
- never enable publication of restricted artifacts

### Training prohibition

Environment overlays encode governance behavior and MUST NOT be used as training data (`ai_training_allowed: false`).

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v11.2.6** | 2025-12-15 | Created environments overlay README: defined purpose, constraints, merge/precedence rules, validation requirements, and production guardrails for environment-specific AI governance configuration overlays. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
🌦️ Environment Overlay Profiles · Governed for Integrity

[⬅️ Back to Config Profiles](../README.md) · [🧩 Domain Overlays](../domains/README.md) · [⬅️ Back to AI Tools](../../README.md) · [🛡 Governance](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>