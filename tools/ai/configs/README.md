---
title: "⚙️ Kansas Frontier Matrix — AI Tools Config Profiles"
path: "tools/ai/configs/README.md"

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

doc_uuid: "urn:kfm:doc:tools-ai-configs-readme:v11.2.6"
semantic_document_id: "kfm-doc-tools-ai-configs"
event_source_id: "ledger:tools/ai/configs/README.md"
immutability_status: "mutable-plan"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/tools-ai-governance-v4.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I2-R3"
care_label: "Public · Low-Risk"
classification: "Public"
jurisdiction: "United States · Kansas"
sensitivity: "General"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_data_flag: false

ai_training_allowed: false
ai_training_guidance: "Governance configs and audit policy profiles MUST NOT be used as training data."

machine_readable: true
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "Annual review"
sunset_policy: "Superseded upon next AI-tools platform update"
---

<div align="center">

# ⚙️ **KFM — AI Tools Config Profiles**
`tools/ai/configs/README.md`

**Purpose**  
Define the **canonical configuration profile system** for `tools/ai/` governance tooling:  
thresholds, actions, and policy constraints used by bias audits, explainability audits, drift monitoring, and AI telemetry emission.

</div>

---

## 📘 Overview

### What lives in `tools/ai/configs/`

This directory contains **config profiles** used by `tools/ai/` audit runners and governance utilities to ensure:

- determinism (same config → same decisions, given same inputs)
- reproducibility (configs are versioned, reviewable, and hashable)
- governance compliance (FAIR+CARE + sovereignty constraints are encoded and enforced)
- CI safety (configs are schema-valid, contain no secrets, and are safe to load in automation)

Configs here are treated as **policy-bearing artifacts**. They are not “just defaults”.

### What configs MUST NOT contain (normative)

Configs MUST NOT include:

- secrets (tokens, passwords, keys, access URLs with credentials)
- PII (emails, phone numbers, addresses, SSNs, etc.)
- precise protected-site coordinates or sensitive cultural site identifiers
- raw data samples or record-level payloads

If a threshold depends on sensitive context, encode that as **a label and a governance action** (e.g., “requires review”) rather than embedding sensitive details.

### How configs are used

Audit runners (examples):

- `tools/ai/bias_check.py`
- `tools/ai/focus_audit.py`
- `tools/ai/drift_monitor.py`

…load a profile from this directory to determine:

- which metrics to compute
- what thresholds apply for PASS/WARN/FAIL
- what actions to recommend or enforce (block, review, quarantine, etc.)
- what telemetry fields must be emitted

The runner MUST record:

- the config file path
- a config hash (sha256 recommended)
- the profile ID and version (from config metadata)

### Profile types

Profiles in this directory are typically one of:

1. **Fairness / bias thresholds**  
   What counts as PASS/WARN/FAIL for subgroup metrics (task-specific).

2. **Explainability thresholds**  
   What counts as “adequate explainability coverage”, evidence bundle completeness, and artifact validity.

3. **Drift thresholds**  
   What drift metrics are computed and what triggers warnings/blocks.

4. **Telemetry policy**  
   Minimum required telemetry fields and what collection method is allowed (safe defaults).

5. **Governance actions policy**  
   What happens on WARN/FAIL, escalation routing, and what is blocked automatically.

Not every repo will have every profile type on day one, but the goal is to converge on a complete set before certification.

### Profile selection and overrides

Recommended override order (highest precedence last):

1. Tool defaults (built-in safe baseline)
2. `tools/ai/configs/*default*`
3. Domain profile (e.g., hydrology / archives / remote-sensing)
4. Environment profile (dev/staging/prod) **only when governance permits**
5. Explicit CLI override (allowed only for authorized roles and must be logged)

Normative rule: if a required profile is missing or invalid, the tool MUST fail closed (FAIL) rather than inventing behavior.

---

## 🗂️ Directory Layout

This is the **intended canonical layout**. Keep it accurate as files are added/removed.

~~~text
📁 tools/
└── 🧠 ai/
    └── 📁 configs/
        ├── 📄 README.md                              # This file
        │
        ├── 🧾 fairness_thresholds.default.json        # Default fairness/bias thresholds (task-scoped)
        ├── 🧾 explainability_thresholds.default.json  # Default XAI/evidence-bundle thresholds
        ├── 🧾 drift_thresholds.default.json           # Default drift thresholds (data/output/concept)
        ├── 🧾 telemetry_policy.default.json           # Minimum telemetry + safe collection policy
        ├── 🧾 governance_actions.default.json         # PASS/WARN/FAIL actions + escalation routing
        │
        ├── 📁 domains/                                # Domain-specific overlays (optional; governed)
        │   ├── 🧾 fairness.hydrology.json
        │   ├── 🧾 fairness.remote_sensing.json
        │   ├── 🧾 explainability.focus_mode.json
        │   └── 🧾 drift.timeseries.json
        │
        └── 📁 environments/                           # Environment overlays (optional; strongly constrained)
            ├── 🧾 dev.json
            ├── 🧾 staging.json
            └── 🧾 production.json
~~~

Directory layout rules (normative):

- Every JSON config file in this directory MUST include a `meta` block (see below).
- Profiles MUST be small and readable; avoid giant monolithic configs.
- Domain and environment overlays MUST NOT weaken governance requirements unless explicitly authorized and logged.
- If `domains/` or `environments/` is not used, remove it from the tree (do not leave dead structure).

---

## 🧭 Context

### Relationship to the model registry

Config profiles are referenced (directly or indirectly) by model registry entries (e.g., `tools/ai/ai_model_registry.json`) via:

- profile ID + version
- or explicit config file path

The registry SHOULD treat profile changes as governance-relevant and capture:

- when a model was certified under which profile version
- what changed between profile versions (human-readable summary)

### Relationship to data contracts and catalogs

Profiles should not hard-code dataset specifics.

Instead, profiles should:

- define behavior by task type and risk class
- rely on dataset metadata (STAC/DCAT) for:
  - spatial/temporal scope classification
  - sensitivity labels
  - stewardship and licensing constraints
  - provenance lineage requirements

### Governance constraints

This directory is governed by:

- `governance_ref`
- `ethics_ref`
- `sovereignty_policy`

Practical implication:

- Profiles MUST support “requires review” pathways.
- Profiles MUST support redaction-aware behavior (masking, suppression, safe summaries).
- Profiles MUST not enable publication of restricted outputs through configuration tricks.

---

## 🧪 Validation & CI/CD

### Required config structure (recommended contract)

Each config SHOULD be a JSON object with:

- `meta` (required)
- `thresholds` (required for audit profiles)
- `actions` (required for governance action profiles)
- `telemetry` (required for telemetry policy profiles)
- optional `notes` (human-readable rationale; keep it policy-safe)

Minimum `meta` block:

~~~json
{
  "meta": {
    "profile_id": "fairness_thresholds.default",
    "profile_version": "11.2.6",
    "profile_kind": "fairness|explainability|drift|telemetry|actions",
    "owner_role": "ai-governance-registry",
    "last_updated": "2025-12-15",
    "governance_ref": "../../../docs/standards/governance/ROOT-GOVERNANCE.md",
    "ethics_ref": "../../../docs/standards/faircare/FAIRCARE-GUIDE.md",
    "sovereignty_policy": "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
  }
}
~~~

### Example fairness thresholds (illustrative)

Numbers below are placeholders; actual thresholds must be set by governance review.

~~~json
{
  "meta": {
    "profile_id": "fairness_thresholds.default",
    "profile_version": "11.2.6",
    "profile_kind": "fairness",
    "owner_role": "ai-governance-registry",
    "last_updated": "2025-12-15"
  },
  "thresholds": {
    "classification": {
      "required_metrics": [
        "group_error_rate_delta",
        "calibration_delta"
      ],
      "warn": {
        "group_error_rate_delta": "<set-by-governance>",
        "calibration_delta": "<set-by-governance>"
      },
      "fail": {
        "group_error_rate_delta": "<set-by-governance>",
        "calibration_delta": "<set-by-governance>"
      }
    },
    "regression": {
      "required_metrics": [
        "group_mae_delta",
        "tail_error_frequency_delta"
      ],
      "warn": {
        "group_mae_delta": "<set-by-governance>"
      },
      "fail": {
        "group_mae_delta": "<set-by-governance>"
      }
    }
  },
  "actions": {
    "on_warn": ["require_review"],
    "on_fail": ["block_certification", "quarantine"]
  }
}
~~~

### Example drift thresholds (illustrative)

~~~json
{
  "meta": {
    "profile_id": "drift_thresholds.default",
    "profile_version": "11.2.6",
    "profile_kind": "drift",
    "owner_role": "ai-governance-registry",
    "last_updated": "2025-12-15"
  },
  "thresholds": {
    "required_metrics": [
      "psi",
      "ks_pvalue"
    ],
    "warn": {
      "psi": "<set-by-governance>",
      "ks_pvalue": "<set-by-governance>"
    },
    "fail": {
      "psi": "<set-by-governance>",
      "ks_pvalue": "<set-by-governance>"
    }
  },
  "actions": {
    "on_warn": ["monitor", "require_review_if_production"],
    "on_fail": ["block_certification", "retrain_or_recalibrate"]
  }
}
~~~

### Validation rules (normative)

CI SHOULD enforce:

- JSON validity (`.json` parses)
- required keys exist (`meta.profile_id`, `meta.profile_version`, etc.)
- no secrets, no PII, no restricted coordinates
- profile IDs are unique and stable
- profile version matches the repo release policy (or is explicitly documented)

If a schema exists for these profiles, CI MUST validate against it. If a schema does not exist yet, the next governance update should add one and wire it into `tools/validation/`.

### Recording config identity in audit runs (normative)

All audit outputs MUST record:

- `config_path`
- `config_profile_id`
- `config_profile_version`
- `config_sha256`

This prevents “silent policy drift” caused by config changes.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v11.2.6** | 2025-12-15 | Initial configs README for `tools/ai/configs/`; defined canonical profile types, directory structure, recommended config contract, validation rules, and audit-run recording requirements. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
⚙️ AI Config Profiles · Governed for Integrity

[⬅️ Back to AI Tools](../README.md) · [⬅️ Back to Tools](../../README.md) · [🛡 Governance](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>