---
title: "🧷 KFM — Query Test Fixtures (`queries/tests/fixtures`) (Diamond⁹ Ω / Crown∞Ω)"
path: "docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/tests/fixtures/README.md"

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
  domain: "telemetry-query-fixtures"
  applies_to:
    - "docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/tests/fixtures/**"

fair_category: "F1-A1-I2-R2"
care_label: "FAIR+CARE Governance Aligned"
sensitivity: "Synthetic or minimized telemetry fixtures; no secrets; no identity-level records"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by Query Fixtures v12"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"

metadata_profiles:
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/tests/fixtures/README.md@v11.2.4"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "../../../../../../../schemas/json/kfm-markdown-protocol-v11.2.6.schema.json"
shape_schema_ref: "../../../../../../../schemas/shacl/kfm-markdown-protocol-v11.2.6-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:telemetry:rsc:dashboards:queries:tests:fixtures:v11.2.6"
semantic_document_id: "kfm-telemetry-rsc-queries-tests-fixtures-v11.2.6"
event_source_id: "ledger:kfm:doc:telemetry:rsc:dashboards:queries:tests:fixtures:v11.2.6"
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

# 🧷 **KFM — Query Test Fixtures**
`docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/tests/fixtures/README.md`

**Purpose**  
Define the governed **fixture set** used by the dashboard query test harness. Fixtures are small, deterministic,
and policy-safe telemetry samples that enable repeatable tests for query semantics, units, and correlation math.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Fixtures-Deterministic-informational" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Aligned-gold" />
<img src="https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen" />

</div>

---

## 📘 Overview

Fixtures in this directory are designed to validate query packs used by the **Reliability ↔ Sustainability Correlation**
dashboards without relying on live systems.

A fixture is a **minimal dataset** that:

- represents typical telemetry run records and edge cases
- is deterministic across platforms and engines
- contains no secrets and no identity-level data
- is small enough for fast CI

### Normative rules

Fixtures MUST:

- include only **aggregated** or **synthetic** telemetry values
- include the canonical metrics expected by dashboards:
  - `workflow_duration_sec`
  - `energy_wh`
  - `carbon_gco2e`
  - reliability signals (success/fail, error counts, retry counts) when applicable
- be stable under sort/normalization
- document provenance (how and why it was created)

Fixtures MUST NOT:

- include API keys, tokens, or raw logs
- include user identities or sensitive site coordinates
- drift units (e.g., mixing Wh with kWh without explicit conversion)

---

## 🗂️ Directory Layout

~~~text
📁 fixtures/
├── 📄 README.md                      — ← You are here (fixture rules + provenance)
├── 📄 fixtures.manifest.json         — Fixture registry (IDs, formats, intended tests)
├── 📄 telemetry_runs.jsonl           — Canonical JSONL fixture: one run record per line
├── 📄 telemetry_runs.json            — Optional: same data as a single JSON array
├── 📄 telemetry_runs.parquet         — Optional: parquet version for SQL engines
├── 📄 telemetry_runs.csv             — Optional: csv version for quick local testing
└── 📁 derived/
    ├── 📄 expected_units.json        — Unit expectations (sec/Wh/gCO2e) for tests
    └── 📄 README.md                  — Notes for derived/generated fixture artifacts
~~~

If you add a new fixture file, you MUST update `fixtures.manifest.json`.

---

## 🧭 Context

The query packs under:

- `../../sql/`
- `../../jq/`
- `../../promql/`
- `../../logql/`

are used to power dashboard panels and governance views. Fixtures give us an offline, reproducible way to prove:

- queries return the correct fields
- joins/filters behave as expected
- correlation calculations are not misled by missing values or unit errors
- changes to telemetry schemas do not break dashboards silently

---

## 📦 Data & Metadata

### 1. Canonical record shape (recommended)

Each record in `telemetry_runs.jsonl` SHOULD include:

- identifiers
  - `run_id` (string, stable)
  - `workflow` (string)
  - `timestamp` (UTC ISO-8601)
- reliability
  - `status` (`success` | `failure` | `cancelled`)
  - `jobs_succeeded` (int)
  - `jobs_failed` (int)
  - `retries` (int)
- sustainability
  - `workflow_duration_sec` (number)
  - `energy_wh` (number)
  - `carbon_gco2e` (number)
- optional dimensions
  - `runner_type` (string)
  - `branch` (string)
  - `release_version` (string)

### 2. Units (normative)

- duration: **seconds** (`*_sec`)
- energy: **watt-hours** (`*_wh`)
- carbon: **grams CO2e** (`*_gco2e`)

If a fixture uses any other unit, it MUST:

- include an explicit unit field, AND
- include a derived normalized field in the canonical units above.

### 3. Provenance (required)

Each fixture entry in `fixtures.manifest.json` MUST capture:

- `fixture_id`
- `source` (synthetic | minimized-from-prod | simulated)
- `generation_script` (path if applicable)
- `hash_sha256` (or placeholder)
- `notes` (why this fixture exists / what it tests)

---

## 🧪 Validation & CI/CD

Fixtures are validated by:

- `docs-lint.yml` (structure and front-matter consistency)
- the query test harness runners (schema + unit checks)
- snapshot comparisons in `../snapshots/`

A fixture update SHOULD be accompanied by:

- updated snapshots (if expected outputs change)
- an explicit Version History entry (here and/or in test harness README)

---

## ⚖ FAIR+CARE & Governance

Fixtures are governed inputs. Even when synthetic, they can influence what dashboards suggest.

Therefore:

- fixtures are treated as **public, non-sensitive artifacts**
- changes are reviewed as if they were changes to production query logic
- any new dimensions must respect sovereignty and privacy policies referenced below

---

## 🕰️ Version History

| Version | Date       | Author            | Summary                                                        |
|--------:|------------|-------------------|----------------------------------------------------------------|
| v11.2.6 | 2025-12-12 | `@kfm-telemetry`  | Established governed fixture rules and canonical units policy. |
| v11.2.4 | 2025-12-06 | `@kfm-telemetry`  | Baseline fixture folder (superseded by v11.2.6 conventions).   |

---

<div align="center">

🧷 **KFM — Query Test Fixtures (v11.2.6)**  
Small · Deterministic · Policy-Safe · Engine-Friendly

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Units-sec%20%7C%20Wh%20%7C%20gCO2e-informational" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Aligned-gold" />

[⬅ Test Harness](../README.md) ·
[🧾 Query Packs](../../README.md) ·
[📊 Dashboards Index](../../../README.md) ·
[🧭 Correlation Module](../../../../README.md) ·
[📘 Markdown Protocol](../../../../../../standards/kfm_markdown_protocol_v11.2.6.md) ·
[⚖ Governance Charter](../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω

</div>

