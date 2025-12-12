---
title: "🧾 KFM — Derived Fixture Artifacts (`fixtures/derived`) (Diamond⁹ Ω / Crown∞Ω)"
path: "docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/tests/fixtures/derived/README.md"

version: "v11.2.6"
last_updated: "2025-12-12"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"

signature_ref: "../../../../../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../../../../../releases/v11.2.6/reliability-sustainability-correlation-tests-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/reliability-sustainability-correlation-tests-v11.2.6.json"
energy_schema: "../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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
  domain: "telemetry-query-fixtures-derived"
  applies_to:
    - "docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/tests/fixtures/derived/**"

fair_category: "F1-A1-I2-R2"
care_label: "FAIR+CARE Governance Aligned"
sensitivity: "Derived artifacts from synthetic/minimized fixtures; no secrets; no identity-level records"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by Derived Fixture Artifacts v12"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"

metadata_profiles:
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/tests/fixtures/README.md@v11.2.6"
  - "docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/tests/fixtures/README.md@v11.2.4"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "../../../../../../../../schemas/json/kfm-markdown-protocol-v11.2.6.schema.json"
shape_schema_ref: "../../../../../../../../schemas/shacl/kfm-markdown-protocol-v11.2.6-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:telemetry:rsc:dashboards:queries:tests:fixtures:derived:v11.2.6"
semantic_document_id: "kfm-telemetry-rsc-queries-tests-fixtures-derived-v11.2.6"
event_source_id: "ledger:kfm:doc:telemetry:rsc:dashboards:queries:tests:fixtures:derived:v11.2.6"
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

# 🧾 **KFM — Derived Fixture Artifacts**
`docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/tests/fixtures/derived/README.md`

**Purpose**  
Document the governed **derived outputs** generated from canonical query fixtures (normalized unit maps, expected outputs,
and lightweight indexes) used by the dashboard query test harness.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Fixtures-Derived-informational" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Aligned-gold" />
<img src="https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen" />

</div>

---

## 📘 Overview

This folder contains **derived artifacts** created from the canonical fixtures in:

- `../telemetry_runs.jsonl` (recommended canonical source)
- `../fixtures.manifest.json` (fixture registry)

Derived artifacts exist to support:

- deterministic unit normalization checks
- query regression tests (expected fields, shapes, and totals)
- engine compatibility (e.g., JSONL vs. JSON array vs. parquet)

### Normative rules

Derived artifacts MUST:

- be reproducible from canonical fixtures
- be deterministic (ordering, formatting, and rounding rules must be stable)
- preserve canonical units:
  - seconds (`*_sec`)
  - watt-hours (`*_wh`)
  - grams CO2e (`*_gco2e`)
- remain policy-safe (no secrets, no identity-level records)

Derived artifacts MUST NOT:

- become the “source of truth” for fixture content
- be edited manually if they are generated outputs (see CI rules below)

---

## 🗂️ Directory Layout

~~~text
📁 fixtures/
├── 📄 README.md                         — Fixture rules (canonical source policy)
├── 📄 fixtures.manifest.json            — Fixture registry (IDs, hashes, intent)
├── 📄 telemetry_runs.jsonl              — Canonical run records (recommended)
└── 📁 derived/
    ├── 📄 README.md                     — ← You are here (derived artifact rules)
    ├── 📄 expected_units.json           — Unit expectations + normalization map
    ├── 📄 expected_fields.json          — Expected column/field sets per engine/query-pack
    ├── 📄 expected_aggregates.json      — Expected totals/rollups for regression tests
    ├── 📄 expected_null_handling.json   — Expected behavior for missing values and defaults
    └── 📄 derived.manifest.json         — Derived artifact registry (source + generation metadata)
~~~

If an artifact is present in `derived/`, it MUST be registered in `derived.manifest.json`.

---

## 🧭 Context

The dashboard correlation layer relies on query packs (SQL, jq, PromQL, LogQL) that can drift subtly when:

- telemetry schemas evolve
- engines interpret nulls or types differently
- units or rounding rules change

Derived artifacts provide a stable, audited baseline so tests can answer:

- Did the query return the correct fields?
- Are units consistent and normalized?
- Do totals match expected results for the fixture set?
- Did null/empty handling change?

---

## 📦 Data & Metadata

### 1. Derived artifact types

**`expected_units.json`** (normative for unit checks)

- Declares:
  - canonical unit expectations per metric key
  - allowed aliases (if any)
  - required normalized outputs (if normalization is supported)

**`expected_fields.json`** (schema drift early warning)

- Declares:
  - minimal required fields per query result type
  - optional fields allowed without failing tests
  - deprecations (if present)

**`expected_aggregates.json`** (regression assertions)

- Declares:
  - expected counts, sums, and ratios (where relevant)
  - acceptable tolerance rules (if needed for float math)
  - fixtures covered by each aggregate assertion

### 2. Manifest requirements

`derived.manifest.json` MUST include, for each derived file:

- `artifact_id`
- `artifact_path`
- `source_fixture_paths`
- `generation_method` (script name or “manual” only when explicitly allowed)
- `hash_sha256` (or placeholder)
- `notes` (what this artifact proves)

---

## 🧪 Validation & CI/CD

Derived artifacts are enforced as part of the query regression pipeline:

- If an artifact is designated “generated” in `derived.manifest.json`:
  - CI MUST fail when the file changes without a corresponding fixture change
  - CI SHOULD validate determinism (sorted keys, stable formatting)

Recommended enforcement pattern:

- canonical fixtures change → regenerate derived artifacts → update manifests → run regression tests
- derived artifacts change alone → fail (unless explicitly permitted and explained)

---

## ⚖ FAIR+CARE & Governance

Even synthetic or minimized fixtures can shape governance narratives via dashboards.

Therefore:

- derived artifacts must remain:
  - reproducible
  - auditable
  - non-sensitive
- derived outputs MUST NOT include:
  - raw logs
  - user identifiers
  - secret material
  - restricted/sensitive site locations

Any new dimension added to expected outputs SHOULD be reviewed for:

- sovereignty implications
- potential re-identification risk
- accidental leakage via “helpful” debug fields

---

## 🕰️ Version History

| Version | Date       | Author            | Summary                                                                 |
|--------:|------------|-------------------|-------------------------------------------------------------------------|
| v11.2.6 | 2025-12-12 | `@kfm-telemetry`  | Defined derived artifact contracts, registry requirements, and CI rules. |
| v11.2.4 | 2025-12-06 | `@kfm-telemetry`  | Baseline derived folder concept (superseded by v11.2.6 conventions).     |

---

<div align="center">

🧾 **KFM — Derived Fixture Artifacts (v11.2.6)**  
Deterministic Derivations · Unit Safety · Regression-Ready

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Units-sec%20%7C%20Wh%20%7C%20gCO2e-informational" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Aligned-gold" />

[⬅ Fixtures](../README.md) ·
[🧪 Tests](../../README.md) ·
[🧾 Query Packs](../../../README.md) ·
[📊 Dashboards Index](../../../../README.md) ·
[🧭 Correlation Module](../../../../../README.md) ·
[📘 Markdown Protocol](../../../../../../../standards/kfm_markdown_protocol_v11.2.6.md) ·
[⚖ Governance Charter](../../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω

</div>

