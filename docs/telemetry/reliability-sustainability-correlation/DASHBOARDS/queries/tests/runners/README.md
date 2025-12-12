---
title: "🏃 Kansas Frontier Matrix — Dashboard Query Test Runners (Reliability × Sustainability Correlation) (Diamond⁹ Ω / Crown∞Ω)"
path: "docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/tests/runners/README.md"

version: "v11.2.6"
last_updated: "2025-12-12"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability Engineering · FAIR+CARE Council"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.6/reliability-sustainability-correlation-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/reliability-sustainability-correlation-v11.2.6.json"
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
doc_kind: "Directory README"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles: []

scope:
  domain: "telemetry"
  applies_to:
    - "docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/tests/runners/**"

fair_category: "F1-A1-I2-R2"
care_label: "FAIR+CARE Governance Aligned"
sensitivity: "Query test harness metadata; non-sensitive by default"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by Reliability × Sustainability Correlation v12"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"

metadata_profiles:
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/tests/runners/README.md@v11.2.4"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "../../../../../../../schemas/json/kfm-markdown-protocol-v11.2.6.schema.json"
shape_schema_ref: "../../../../../../../schemas/shacl/kfm-markdown-protocol-v11.2.6-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:telemetry:rsc:dashboards:queries:tests:runners:v11.2.6"
semantic_document_id: "kfm-telemetry-rsc-query-test-runners-v11.2.6"
event_source_id: "ledger:kfm:doc:telemetry:rsc:dashboards:queries:tests:runners:v11.2.6"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "a11y-adaptations"
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
    - "🗺️ Diagrams"
    - "🧠 Story Node & Focus Mode Integration"
    - "🧪 Validation & CI/CD"
    - "📦 Data & Metadata"
    - "🌐 STAC, DCAT & PROV Alignment"
    - "🧱 Architecture"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "metadata-check"
  - "provenance-check"
  - "footer-check"

ci_integration:
  workflow: ".github/workflows/docs-lint.yml"
  environment: "dev → staging → production"

branding_registry:
  telemetry: "Transparent Systems · Ethical Metrics · Sustainable Intelligence"
  graph: "Semantics × Provenance × Spatial Intelligence"

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

# 🏃 **Kansas Frontier Matrix — Dashboard Query Test Runners**
`docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/tests/runners/README.md`

**Purpose**  
Define the **runner contract** and **implementation expectations** for executing **query regression tests**
across Reliability × Sustainability dashboards (PromQL / LogQL / SQL / jq-derived checks), producing **deterministic reports**
and governance-ready telemetry artifacts.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Telemetry-Reliability_%C3%97_Sustainability-informational" />
<img src="https://img.shields.io/badge/Tests-Query_Regression-blue" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Aligned-gold" />
<img src="https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen" />

</div>

---

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 📁 telemetry/
    └── 📁 reliability-sustainability-correlation/
        ├── 📁 ALERTS/
        │   └── 📄 README.md                              — Alert rules, thresholds, and runbooks
        └── 📁 DASHBOARDS/
            ├── 📄 README.md                              — Dashboard philosophy, panels, data contracts
            ├── 📁 screenshots/
            │   └── 📄 README.md                          — Screenshot capture rules (optional evidence)
            └── 📁 queries/
                ├── 📄 README.md                          — Query catalog + naming rules
                ├── 📁 promql/
                │   └── 📄 README.md
                ├── 📁 logql/
                │   └── 📄 README.md
                ├── 📁 jq/
                │   └── 📄 README.md
                ├── 📁 sql/
                │   ├── 📄 README.md
                │   └── 📁 _views/
                │       └── 📄 README.md
                └── 📁 tests/
                    ├── 📄 README.md                      — Test strategy (goldens, fixtures, failure modes)
                    ├── 📁 fixtures/
                    │   ├── 📄 README.md                  — Canonical input fixtures (frozen snapshots)
                    │   └── 📁 derived/
                    │       └── 📄 README.md              — Derived fixtures (normalized, aggregated)
                    ├── 📁 reports/
                    │   └── 📄 README.md                  — Report formats, storage, and retention
                    └── 📁 runners/
                        └── 📄 README.md                  — ← This file (runner contract + expectations)
~~~

---

## 📘 Overview

This directory documents the **test runners** used to execute and validate dashboard queries.

Runners exist to ensure:

- ✅ **Queries continue to work** as schemas, dashboards, and pipelines evolve.  
- ✅ **Results remain stable** (or changes are intentional and reviewed).  
- ✅ **Failures are explainable** with artifacts that can be archived and audited.  
- ✅ **Telemetry is emitted** so reliability and sustainability trends can be correlated over time.

**What belongs here**

- Runner interfaces (contract, required flags, exit codes).  
- Runner expectations (determinism, normalization, redaction).  
- Runner-level conventions shared by suite implementations (PromQL, LogQL, SQL, jq).

**What does NOT belong here**

- Raw fixtures (live under `../fixtures/`).  
- Golden outputs and reports (live under `../reports/`).  
- The query catalog itself (lives under `../../`).

---

## 🧭 Context

### Runner design constraints (normative)

Runners MUST:

- Be **deterministic** (stable ordering, stable rounding rules where applicable).
- Be **non-interactive** (CI-safe; no prompts).
- Support **offline fixtures** (no required access to production systems).
- Produce **machine-readable outputs** for governance ingestion.
- Return meaningful **exit codes**:
  - `0` = pass
  - `1` = test failures (regression mismatch / threshold breach)
  - `2` = runner/config error (misconfiguration, missing fixtures, schema mismatch)

Runners SHOULD:

- Normalize output fields (sorting, timestamps, float rounding, null handling).
- Redact secrets and unsafe strings from logs and reports.
- Provide a single **run manifest** summarizing:
  - suite(s) executed
  - input fixture set(s)
  - runner version / commit SHA
  - result counts and failure summaries

---

## 🧪 Validation & CI/CD

### Local execution (recommended shape)

Runners SHOULD expose a stable CLI with flags such as:

- `--suite <promql|logql|sql|jq|all>`
- `--fixtures <path>`
- `--queries <path>`
- `--out <path>`
- `--baseline <path>` (optional golden reference)
- `--fail-fast` (optional)

Example (schematic):

~~~bash
# From: docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/tests/
# Run all suites using frozen fixtures and write a report bundle.
./runners/run_all.sh \
  --fixtures ./fixtures \
  --queries  ../ \
  --out      ./reports/_local_run
~~~

### CI integration (expected behavior)

In CI, runners SHOULD:

- write reports into `docs/**/reports/` (or a CI artifact directory)
- emit a summary JSON that can be merged into telemetry streams
- avoid querying live backends unless explicitly configured and approved by governance

---

## 📦 Data & Metadata

### Inputs (by convention)

- Query definitions:
  - `docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/**`
- Test fixtures:
  - `../fixtures/`
  - `../fixtures/derived/`

### Outputs (by convention)

- Report bundle directory (per run):
  - `../reports/<run_id>/`
- Minimal required artifacts:
  - `run_manifest.json` (what ran, against what, when, using which commit)
  - `summary.json` (pass/fail counts + high-level failures)
  - `failures.json` (structured list of mismatches / threshold breaches)

### Suggested `summary.json` shape (schematic)

~~~json
{
  "run_id": "rsc-qtests_<timestamp>_<shortsha>",
  "suites": ["promql", "logql", "sql", "jq"],
  "queries_root": "docs/telemetry/.../DASHBOARDS/queries",
  "fixtures_root": "docs/telemetry/.../DASHBOARDS/queries/tests/fixtures",
  "passed": 148,
  "failed": 2,
  "errors": 0,
  "timestamp": "<utc-iso8601>",
  "commit_sha": "<git-sha>"
}
~~~

---

## 🧱 Architecture

A runner set typically contains:

- **Suite adapters**
  - translate “query spec → execution → normalized result”
- **Normalizers**
  - stable sort, stable rounding, stable timestamp handling
- **Comparators**
  - compare normalized output to goldens
- **Report writers**
  - JSON summaries + optional human-readable markdown
- **Redaction filters**
  - strip tokens, internal hostnames, or environment-only identifiers

This layering keeps query tests portable across environments while preserving governance-grade evidence.

---

## ⚖ FAIR+CARE & Governance

Even though these are “just queries,” runners must still uphold governance rules:

- **No secrets in queries**
  - Runners MUST fail (or hard-redact) if tokens/credentials appear in committed query specs.
- **No accidental disclosure**
  - Reports SHOULD avoid embedding raw log lines that may contain sensitive identifiers.
- **Truthful reporting**
  - Runners MUST report what was actually executed (fixtures, versions, suite).
- **Change discipline**
  - If a golden needs to change, the PR MUST explain why (schema change, metric definition change, bug fix).

---

## 🕰️ Version History

| Version | Date       | Author            | Summary                                                                 |
|--------:|------------|-------------------|-------------------------------------------------------------------------|
| v11.2.6 | 2025-12-12 | `@kfm-observability` | Created/normalized runner README; defined deterministic runner contract and report expectations under KFM‑MDP v11.2.6. |

---

<div align="center">

🏃 **KFM — Dashboard Query Test Runners (v11.2.6)**  
Deterministic Tests · Governed Evidence · Reliability × Sustainability Correlation

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Telemetry-Governed-informational" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Aligned-gold" />

[⬅ Tests Index](../README.md) ·
[🧪 Fixtures](../fixtures/README.md) ·
[📦 Reports](../reports/README.md) ·
[🧾 Queries Root](../../README.md) ·
[📊 Dashboards](../../../README.md) ·
[📈 RSC Telemetry Root](../../../../README.md) ·
[📡 Telemetry Docs Root](../../../../../README.md) ·
[📘 Docs Root](../../../../../../README.md) ·
[📘 Markdown Protocol](../../../../../../standards/kfm_markdown_protocol_v11.2.6.md) ·
[⚖ Governance Charter](../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω

</div>
