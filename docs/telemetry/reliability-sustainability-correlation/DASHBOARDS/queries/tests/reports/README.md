---
title: "📊 KFM — Query Test Reports (`tests/reports`) (Diamond⁹ Ω / Crown∞Ω)"
path: "docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/tests/reports/README.md"

version: "v11.2.6"
last_updated: "2025-12-12"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"

signature_ref: "../../../../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../../../../releases/v11.2.6/reliability-sustainability-correlation-tests-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/reliability-sustainability-correlation-tests-v11.2.6.json"
energy_schema: "../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

status: "Active / Enforced"
doc_kind: "Standard"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "telemetry-query-test-reports"
  applies_to:
    - "docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/tests/reports/**"

fair_category: "F1-A1-I2-R2"
care_label: "FAIR+CARE Governance Aligned"
sensitivity: "Synthetic/minimized test outputs; no secrets; no identity-level records"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by Query Test Reports v12"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"

metadata_profiles:
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/tests/README.md@v11.2.6"
  - "docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/tests/README.md@v11.2.4"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "../../../../../../../schemas/json/kfm-markdown-protocol-v11.2.6.schema.json"
shape_schema_ref: "../../../../../../../schemas/shacl/kfm-markdown-protocol-v11.2.6-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:telemetry:rsc:dashboards:queries:tests:reports:v11.2.6"
semantic_document_id: "kfm-telemetry-rsc-queries-tests-reports-v11.2.6"
event_source_id: "ledger:kfm:doc:telemetry:rsc:dashboards:queries:tests:reports:v11.2.6"
doc_integrity_checksum: "<sha256>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "a11y-adaptations"
  - "semantic-highlighting"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "narrative-fabrication"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧭 Context"
    - "📦 Data & Metadata"
    - "🧪 Validation & CI/CD"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "accessibility-check"
  - "provenance-check"
  - "footer-check"

ci_integration:
  workflow: ".github/workflows/docs-lint.yml"
  environment: "dev → staging → production"

branding_registry:
  telemetry: "Transparent Systems · Ethical Metrics · Sustainable Intelligence"

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

# 📊 **KFM — Query Test Reports**
`docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/tests/reports/README.md`

**Purpose**  
Define the **governed report artifacts** produced (or snapshotted) by the dashboard query test harness, including
summaries, diffs, and machine-readable evidence suitable for telemetry merge and governance review.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Tests-Reports-informational" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Aligned-gold" />
<img src="https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen" />

</div>

---

## 📘 Overview

This directory is the **report surface** for query regression tests.

It exists to capture:

- **human-readable** summaries (what changed, what failed, what passed)
- **machine-readable** summaries (stable shapes for automation and dashboards)
- **diff evidence** (expected vs actual outputs; normalized comparisons)
- **governance-ready traces** (run IDs, inputs, versions, checksums)

### Normative rules

Reports MUST:

- be derived from:
  - canonical fixtures (`../fixtures/`)
  - derived fixtures (`../fixtures/derived/`) when generation is required
- be reproducible (same fixtures + same query pack → same report results)
- avoid “engine-specific noise” (ordering, formatting, non-deterministic timestamps) unless explicitly recorded

Reports MUST NOT:

- include secrets, tokens, or live environment variables
- include identity-level data (fixtures are synthetic/minimized)
- replace canonical fixtures as a source of truth

---

## 🗂️ Directory Layout

~~~text
📁 queries/
└── 📁 tests/
    ├── 📁 fixtures/
    │   ├── 📄 README.md                    — Fixture rules & canonical sources
    │   └── 📁 derived/
    │       └── 📄 README.md                — Derived fixture contracts & determinism rules
    └── 📁 reports/
        ├── 📄 README.md                    — ← You are here (report artifacts contract)
        ├── 📄 reports.manifest.json        — Report registry (what exists, why, hashes, provenance)
        ├── 📄 summary.json                 — Canonical machine-readable test summary (preferred)
        ├── 📄 summary.md                   — Human-readable summary (PR-friendly)
        ├── 📄 junit.xml                    — Optional CI integration (test runner friendly)
        ├── 📁 diffs/
        │   ├── 📄 expected_vs_actual.json  — Normalized diff payloads (stable ordering)
        │   └── 📄 README.md                — Diff semantics (tolerances, rounding, null rules)
        ├── 📁 snapshots/
        │   ├── 📄 expected.json            — “Golden” expected outputs (if stored here)
        │   ├── 📄 actual.json              — Latest run outputs (if stored here)
        │   └── 📄 README.md                — Snapshot policy (when committed vs artifact-only)
        └── 📁 logs/
            ├── 📄 runner.log               — Optional execution logs (sanitized)
            └── 📄 README.md                — Log redaction rules
~~~

If a file exists under `reports/`, it MUST be registered in `reports.manifest.json`.

---

## 🧭 Context

The reliability ↔ sustainability correlation dashboards depend on query packs that may run across multiple engines:

- SQL (warehouse views)
- jq (JSON transformations)
- PromQL / LogQL (observability backends)

Regression tests ensure that:

- outputs remain stable as schemas evolve
- unit normalization stays correct (sec, Wh, gCO2e)
- null handling does not silently change results
- the dashboards do not “pass” while the data meaning drifts

This directory provides **evidence** for that claim in a shape that can be:

- uploaded as CI artifacts
- summarized in PR checks
- merged into governance telemetry streams (when configured)

---

## 📦 Data & Metadata

### 1. Canonical machine-readable summary

`summary.json` SHOULD include at minimum:

- `run_id`
- `query_pack_id` (or `pack` + `engine`)
- `fixture_set_id` (or fixture hash reference)
- `commit_sha`
- `started_at`, `ended_at`
- `status` (`pass` / `fail`)
- `assertions_total`, `assertions_passed`, `assertions_failed`
- `failures[]` (each with `assertion_id`, `reason`, `artifact_path`)

### 2. Manifest requirements

`reports.manifest.json` MUST include, for each report artifact:

- `artifact_id`
- `artifact_path`
- `artifact_kind` (summary, diff, snapshot, junit, log)
- `source_fixture_paths`
- `generation_method` (script or runner)
- `hash_sha256` (or placeholder)
- `notes` (what this artifact proves)

---

## 🧪 Validation & CI/CD

Reports in this directory are validated through:

- **docs-lint** (KFM-MDP v11.2.6 structure for this README and any `summary.md`)
- **schema-lint** (if `summary.json` / manifests are schema-governed)
- **query regression harness** (ensures diffs are deterministic and unit-safe)

### Expected CI behavior

- If `summary.json` is committed:
  - CI SHOULD verify it matches regenerated results for the canonical fixtures
- If `summary.json` is artifact-only:
  - this directory SHOULD still document:
    - file shapes
    - naming conventions
    - manifest semantics

---

## ⚖ FAIR+CARE & Governance

These reports are governance artifacts, even when synthetic:

- they influence operational decisions (alerts/dashboards)
- they support audit claims (“we validate correlation logic”)

Therefore:

- keep outputs minimized
- keep outputs deterministic
- keep outputs non-sensitive

If any report ever contains sensitive markers, it MUST be:

- removed or redacted immediately
- documented as an incident in the appropriate governance channel (per referenced standards)

---

## 🕰️ Version History

| Version | Date       | Author            | Summary                                                                 |
|--------:|------------|-------------------|-------------------------------------------------------------------------|
| v11.2.6 | 2025-12-12 | `@kfm-telemetry`  | Established report artifact contracts, manifest requirements, and CI rules. |
| v11.2.4 | 2025-12-06 | `@kfm-telemetry`  | Baseline reports folder concept (superseded by v11.2.6 conventions).     |

---

<div align="center">

📊 **KFM — Query Test Reports (v11.2.6)**  
Deterministic Evidence · Regression Safety · Governance-Ready Outputs

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Reports-summary.json%20%7C%20diffs%20%7C%20junit-informational" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Aligned-gold" />

[⬅ Tests](../README.md) ·
[🧩 Fixtures](../fixtures/README.md) ·
[🧾 Derived Fixtures](../fixtures/derived/README.md) ·
[🧾 Query Packs](../../README.md) ·
[📊 Dashboards Index](../../../README.md) ·
[🧭 Correlation Module](../../../../README.md) ·
[📘 Docs Root](../../../../../../README.md) ·
[📘 Markdown Protocol](../../../../../../standards/kfm_markdown_protocol_v11.2.6.md) ·
[⚖ Governance Charter](../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω

</div>

