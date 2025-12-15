---
title: "🧩 Kansas Frontier Matrix — AI Domain Overlay Profiles"
path: "tools/ai/configs/domains/README.md"

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

doc_uuid: "urn:kfm:doc:tools-ai-configs-domains-readme:v11.2.6"
semantic_document_id: "kfm-doc-tools-ai-configs-domains"
event_source_id: "ledger:tools/ai/configs/domains/README.md"
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
ai_training_guidance: "Domain overlay profiles and policy configs MUST NOT be used as training data."

machine_readable: true
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "Annual review"
sunset_policy: "Superseded upon next AI-tools platform update"
---

<div align="center">

# 🧩 **KFM — AI Domain Overlay Profiles**
`tools/ai/configs/domains/README.md`

**Purpose**  
Define how **domain-specific AI governance profiles** are authored, validated, and applied as overlays on top of the default `tools/ai/configs/` policies—so audits remain deterministic, FAIR+CARE-aligned, and safe across diverse Kansas-scale domains.

</div>

---

## 📘 Overview

### What “domain overlays” are

Domain overlays are **governed configuration fragments** that tailor AI governance behavior (bias/fairness, explainability, drift, telemetry, actions) to a specific KFM domain such as:

- hydrology and climate time-series
- remote sensing / land cover and raster products
- archives / documents / narrative systems
- infrastructure and hazards
- culturally sensitive domains (policy-restricted)

They exist because a single “one-size default” does not fit every domain—**but the default baseline remains the starting contract**.

### What overlays can change

A domain overlay MAY:

- tighten thresholds (stricter WARN/FAIL gates)
- add required metrics (domain-specific checks)
- require higher explainability coverage
- increase drift monitoring cadence or enforce additional baselines
- require stronger redaction/suppression behavior
- change governance actions for WARN/FAIL (e.g., always require review)
- require extra telemetry fields (or stronger completeness)

A domain overlay MUST NOT:

- weaken governance in a way that reduces safety without explicit authorization and traceable approval
- introduce secrets, PII, or protected-site coordinates
- “invent” cohorts or protected attributes that are not permitted by policy

### Relationship to base profiles

Domain overlays are applied on top of base profiles in `tools/ai/configs/` (examples):

- `fairness_thresholds.default.json`
- `explainability_thresholds.default.json`
- `drift_thresholds.default.json`
- `telemetry_policy.default.json`
- `governance_actions.default.json`

If no domain overlay matches, tools must use base profiles and remain deterministic.

---

## 🗂️ Directory Layout

This directory is a subdivision of `tools/ai/configs/`:

~~~text
📁 tools/
└── 🧠 ai/
    └── 📁 configs/
        ├── 📄 README.md                            # Config system overview
        ├── 🧾 *_thresholds*.json                    # Base profiles (fairness/explainability/drift)
        ├── 🧾 telemetry_policy*.json                # Base telemetry policy
        ├── 🧾 governance_actions*.json               # Base actions policy
        │
        └── 📁 domains/                              # Domain overlays (this directory)
            └── 📄 README.md                         # This file
~~~

Recommended overlay naming convention:

- `<profile_kind>.<domain_id>.json`

Where:

- `profile_kind` ∈ `{fairness, explainability, drift, telemetry, actions}`
- `domain_id` is a stable slug (lower_snake_case or lower-kebab-case) governed by the repo’s domain taxonomy

Example filename patterns (illustrative):

~~~text
fairness.hydrology.json
drift.timeseries.json
explainability.focus_mode.json
telemetry.remote_sensing.json
actions.heritage.json
~~~

Important: the specific domain list is repo-defined. Keep this folder accurate to the actual domains in use.

---

## 🧭 Context

### How domains are determined

A domain overlay should be selected using **stable metadata**, not ad-hoc heuristics.

Preferred sources:

- DCAT dataset metadata (e.g., theme/category fields)
- STAC Collection metadata (collection-level “domain” or “theme” tags)
- pipeline configuration that explicitly declares the domain for a run
- model registry entries that declare `domain_id` and required overlays

Recommended rule:

- domain must be resolvable from **governed metadata** (DCAT/STAC/registry/config)
- if domain cannot be determined, fall back to default profiles (or fail closed if the run requires a domain profile by policy)

### Domain overlays are governance objects

Domain overlays encode policy decisions like:

- which metrics matter in a domain
- what thresholds are acceptable for PASS/WARN/FAIL
- what actions happen on WARN/FAIL
- whether the domain requires review on any non-PASS status

This means overlays must be:

- reviewable
- versioned
- schema-valid
- provenance-bound (config hash recorded in outputs)

---

## 🧱 Architecture

### Overlay application order

Recommended precedence (lowest → highest):

1. **Base profile** (from `tools/ai/configs/`)
2. **Domain overlay** (from `tools/ai/configs/domains/`)
3. **Environment overlay** (if used; from `tools/ai/configs/environments/`)
4. **Explicit CLI override** (only when permitted; must be logged)

### Merge semantics (recommended)

To keep behavior deterministic and auditable:

- overlays should be applied via a **controlled deep-merge**
- only allow overriding an allow-listed set of keys per profile kind
- disallow “silent deletions” of required metrics unless explicitly supported by schema

Recommended approach by data type:

- objects/maps: deep-merge
- arrays/lists:
  - treat `required_metrics` as **set union** (domain can add requirements)
  - treat `prohibited_metrics` as **set union**
- thresholds:
  - domain may tighten values (more strict), but weakening should be rejected by validators unless explicitly authorized and flagged

### Decision policy: fail closed vs fallback

Domain overlays should encode (or inherit) a policy flag like:

- `require_domain_overlay: true|false`

Recommended behavior:

- if `require_domain_overlay: true` and overlay is missing ⇒ FAIL
- otherwise ⇒ use default profile and record that no overlay applied

This makes “domain-required certification paths” enforceable without inventing behavior.

---

## 🧪 Validation & CI/CD

### Overlay requirements (normative)

Every overlay file MUST:

- be valid JSON
- include a `meta` block with:
  - `profile_id` (stable)
  - `profile_version` (semantic)
  - `profile_kind` (fairness/explainability/drift/telemetry/actions)
  - `domain_id`
  - `overlay_of` (base profile id/version this overlays)
  - governance references (or inheritable references)
  - `last_updated`

- be safe:
  - no secrets
  - no PII
  - no protected-site coordinates
  - no raw samples or record-level dumps

- be validated:
  - schema validation (when schemas exist)
  - invariant validation (no forbidden weakening)
  - safety scan

### Required audit output linkage (normative)

Any run that applies a domain overlay MUST record in its outputs:

- `config_domain_overlay_path`
- `config_domain_overlay_profile_id`
- `config_domain_overlay_version`
- `config_domain_overlay_sha256`

This prevents silent drift in policy behavior.

### Recommended CI checks

CI SHOULD enforce:

- JSON schema validation for overlays (profile-kind specific schemas)
- overlay merge validation:
  - confirm merged profile still contains required keys
  - confirm thresholds are not weakened (unless explicitly permitted)
- safety scan (no secrets/PII)
- deterministic formatting / stable key expectations (as required by tooling)

---

## 📦 Data & Metadata

### Overlay contract (recommended)

A domain overlay is a JSON object with `meta` and one or more of:

- `thresholds` (tighten thresholds; add required metrics)
- `actions` (override WARN/FAIL actions to fit domain risk)
- `telemetry` (require additional fields or stricter completeness)
- `policy` (domain-level switches like “require review”)

Minimum recommended `meta` block:

~~~json
{
  "meta": {
    "profile_id": "fairness.hydrology",
    "profile_version": "11.2.6",
    "profile_kind": "fairness",
    "domain_id": "hydrology",
    "overlay_of": "fairness_thresholds.default@11.2.6",
    "owner_role": "ai-governance-registry",
    "last_updated": "2025-12-15",
    "governance_ref": "../../../../docs/standards/governance/ROOT-GOVERNANCE.md",
    "ethics_ref": "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md",
    "sovereignty_policy": "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
  }
}
~~~

Example overlay snippet (illustrative; thresholds must be set by governance):

~~~json
{
  "meta": {
    "profile_id": "drift.timeseries",
    "profile_version": "11.2.6",
    "profile_kind": "drift",
    "domain_id": "timeseries",
    "overlay_of": "drift_thresholds.default@11.2.6",
    "owner_role": "ai-governance-registry",
    "last_updated": "2025-12-15"
  },
  "thresholds": {
    "required_metrics_add": ["seasonal_drift_index"],
    "warn": {
      "aggregate_drift_score": "<set-by-governance>"
    },
    "fail": {
      "aggregate_drift_score": "<set-by-governance>"
    }
  },
  "actions": {
    "on_warn": ["increase_monitoring_cadence", "require_review_if_production"],
    "on_fail": ["block_certification", "retrain_or_recalibrate"]
  }
}
~~~

Notes:

- Use `*_add` semantics (additive) where possible to avoid deletion ambiguity.
- If a domain truly needs to remove a metric, do it through a governed base profile variant—not a silent overlay deletion.

---

## 🌐 STAC, DCAT & PROV Alignment

### Mapping domains to catalogs

Domain overlays should be discoverable via:

- DCAT: dataset theme/category fields that map to `domain_id`
- STAC: collection-level metadata tags that map to `domain_id`

This enables deterministic selection:

- dataset/collection → domain_id → overlay profile → audit run

### Provenance and reproducibility

Every audit run that uses a domain overlay should emit provenance references that include:

- base profile identity
- overlay profile identity
- merged profile hash (recommended)

This makes it possible to reconstruct the exact governance policy used for any run.

---

## ⚖ FAIR+CARE & Governance

### Domain overlays can only tighten safety by default

Default stance:

- overlays can add constraints, not remove them

If a domain overlay must weaken a baseline constraint (rare and high-risk), it must be:

- explicitly authorized through governance,
- recorded as a policy exception,
- validated as intentional (no accidental weakening),
- and traceable in provenance artifacts.

### Sovereignty-sensitive domains

Some domains may require extra controls (e.g., stronger redaction, suppression, aggregation, review gating). Domain overlays are a safe place to encode:

- “always require review” on WARN/FAIL
- “no publishable summaries” flags
- stricter thresholds for evidence bundles and reporting

Do not embed sensitive site metadata into overlay configs.

### Training prohibition

Domain overlays encode governance behavior and MUST NOT be used as training data (`ai_training_allowed: false`).

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v11.2.6** | 2025-12-15 | Created domains overlay README: defined purpose, naming conventions, merge semantics, validation requirements, and catalog/provenance alignment for domain-specific AI governance profiles. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
🧩 Domain Overlay Profiles · Governed for Integrity

[⬅️ Back to Config Profiles](../README.md) · [⬅️ Back to AI Tools](../../README.md) · [🛡 Governance](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>