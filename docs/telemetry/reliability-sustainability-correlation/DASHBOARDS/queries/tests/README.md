---
title: "🧪 KFM — Dashboard Query Test Harness (`queries/tests`) (Diamond⁹ Ω / Crown∞Ω)"
path: "docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/tests/README.md"

version: "v11.2.6"
last_updated: "2025-12-12"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"

signature_ref: "../../../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../../../releases/v11.2.6/reliability-sustainability-correlation-tests-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/reliability-sustainability-correlation-tests-v11.2.6.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

status: "Active / Enforced"
doc_kind: "Standard Index"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

scope:
  domain: "dashboard-query-testing"
  applies_to:
    - "docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/tests/**"
    - "docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/**"

fair_category: "F1-A1-I2-R2"
care_label: "FAIR+CARE Governance Aligned"
sensitivity: "Test fixtures and expected outputs; no secrets; no identity-level telemetry"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by Query Test Harness v12"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"

metadata_profiles:
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/tests/README.md@v11.2.4"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "../../../../../../schemas/json/kfm-markdown-protocol-v11.2.6.schema.json"
shape_schema_ref: "../../../../../../schemas/shacl/kfm-markdown-protocol-v11.2.6-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:telemetry:rsc:dashboards:queries:tests:index:v11.2.6"
semantic_document_id: "kfm-telemetry-rsc-dashboards-queries-tests-index-v11.2.6"
event_source_id: "ledger:kfm:doc:telemetry:rsc:dashboards:queries:tests:index:v11.2.6"
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

# 🧪 **KFM — Dashboard Query Test Harness (`queries/tests`)**
`docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/queries/tests/README.md`

**Purpose**  
Provide a governed **test harness** for dashboard query packs (SQL, jq, LogQL, PromQL, etc.) used by the  
**Reliability ↔ Sustainability Correlation (RSC)** dashboards. These tests prevent regressions in:
query semantics, unit consistency (sec/Wh/gCO2e), and panel-critical column naming.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Telemetry-Query_Testing-orange" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Aligned-gold" />
<img src="https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen" />

</div>

---

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 📁 telemetry/
    └── 📁 reliability-sustainability-correlation/
        └── 📁 DASHBOARDS/
            └── 📁 queries/
                ├── 📄 README.md                       — Queries index (what exists + how to run)
                ├── 📁 sql/                            — SQL query pack (portable SQL)
                ├── 📁 jq/                             — JSON extraction and sanity queries
                ├── 📁 promql/                         — Prometheus queries (if used)
                ├── 📁 logql/                          — Loki queries (if used)
                ├── 📁 manifests/                      — Query manifests (panels → query IDs)
                └── 📁 tests/
                    ├── 📄 README.md                   — ← You are here
                    ├── 📁 fixtures/                   — Input datasets (small, deterministic)
                    │   ├── 📄 telemetry_runs.jsonl     — Example: normalized run records
                    │   ├── 📄 telemetry_runs.parquet   — Example: parquet fixture (optional)
                    │   └── 📄 README.md                — Fixture rules and provenance
                    ├── 📁 snapshots/                  — Expected outputs (“golden” results)
                    │   ├── 📄 sql__panel_*.json        — Canonical JSON results per panel query
                    │   ├── 📄 jq__check_*.json         — Canonical JSON results per check
                    │   └── 📄 README.md                — Snapshot update rules
                    ├── 📁 runners/                    — Local runners / adapters
                    │   ├── 📄 run_sql.sh               — SQL runner (duckdb/psql/bq as configured)
                    │   ├── 📄 run_jq.sh                — jq runner
                    │   └── 📄 README.md                — Runner contract + env vars
                    ├── 📁 reports/                    — Generated test reports (gitignored by default)
                    │   ├── 📄 test_summary.json
                    │   └── 📄 diffs/                   — Diff artifacts for failures
                    └── 📄 tests.manifest.json          — Which tests exist + what they validate
~~~

---

## 📘 Overview

This directory is the **guardrail layer** for dashboard queries.

If the dashboards rely on the query packs under `docs/telemetry/.../DASHBOARDS/queries/`, then this folder:

- Provides **fixtures** (small, deterministic telemetry samples).
- Provides **snapshots** (expected outputs per query/check).
- Provides **runners** (how to execute each query pack consistently).
- Produces **reports** suitable for CI artifacts and governance review.

### What “passing” means (normative)

A test run is considered **passing** when:

- Query output shape matches the panel/check contract:
  - required columns/keys exist
  - units are consistent
  - ordering is deterministic (or explicitly normalized)
- No query introduces forbidden fields/dimensions
- No query depends on undefined environment state without declaring it

---

## 🧭 Context

Dashboard queries are a form of **production logic**, even when stored as docs.

Because telemetry is governance-sensitive (even when aggregated), this harness ensures:

- repeatable results for the same fixture inputs
- predictable panel behavior across engines
- auditable changes (diffs show exactly what changed)

This is especially important for correlation dashboards where unit mistakes can create false relationships.

---

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  Q["Query pack (sql/jq/logql/promql)"] --> F["Fixture dataset"]
  F --> R["Runner executes query"]
  R --> S["Compare to snapshots"]
  S --> P{"Matches?"}
  P -->|yes| A["Publish test summary and telemetry"]
  P -->|no| D["Fail CI and attach diffs"]
~~~

---

## 🧠 Story Node & Focus Mode Integration

Test runs MAY be summarized as Story Nodes, for example:

- `urn:kfm:story-node:telemetry:rsc:queries:test-run:<run_id>`

Focus Mode MAY:

- summarize pass/fail outcomes and which query IDs were impacted
- link to diffs and snapshot updates

Focus Mode MUST NOT:

- rewrite expected outputs
- “explain away” a mismatch without referencing the recorded diffs/reports

---

## 🧪 Validation & CI/CD

### 1. Recommended test types

- **Smoke tests**
  - “Can the runner execute?”
  - “Does it produce valid JSON output?”

- **Contract tests**
  - Column/key presence
  - unit checks (`duration_sec`, `energy_wh`, `carbon_gco2e`)
  - allowed value sets for status fields

- **Golden snapshot tests**
  - Stable, deterministic output comparisons

- **Policy lint**
  - no `SELECT *`
  - explicit projections for views
  - no forbidden columns/dimensions

### 2. CI integration expectations

A CI job (or local script) SHOULD:

1. validate `tests.manifest.json`
2. execute runners against fixtures
3. compare results to snapshots
4. write:
   - `tests/reports/test_summary.json`
   - `tests/reports/diffs/*` on failure
5. emit telemetry (optional but recommended)

---

## 📦 Data & Metadata

### 1. Fixtures (rules)

Fixtures MUST be:

- small enough for fast CI
- deterministic (no time-dependent fields unless fixed)
- non-sensitive
- provenance-stated (where the fixture came from)

### 2. Snapshots (rules)

Snapshots MUST be:

- sorted / normalized
- stable across environments
- updated only via explicit “snapshot update” procedure

Suggested fields inside snapshot metadata blocks:

- `query_id`
- `runner`
- `fixture_id`
- `generated_at`
- `schema_version`

---

## 🌐 STAC, DCAT & PROV Alignment

- **DCAT**
  - Fixtures and snapshots can be treated as governed distributions of a “Query Test Harness” dataset.
- **PROV-O**
  - A test run is a `prov:Activity` using fixture entities and generating:
    - summary report entity
    - diff entities (when failing)
- **STAC**
  - Non-spatial; if cataloged, use `geometry: null`

---

## 🧱 Architecture

Design principles:

- **Deterministic by default**
  - if output order matters, enforce ordering
- **Engine-agnostic core**
  - keep the “contract” consistent even when runners differ
- **Separation of concerns**
  - queries live in pack folders
  - tests live here
  - manifests connect panels → query IDs

---

## ⚖ FAIR+CARE & Governance

This harness supports governance by ensuring:

- dashboard logic is testable and reviewable
- sensitive expansions are caught early (via policy lint + contract checks)
- telemetry-derived claims can be audited back to:
  - query versions
  - fixtures
  - snapshots
  - test run reports

If you need to add a new dimension/field:

1. add it to the approved registry for dashboards (governance-controlled)
2. update fixtures and snapshots
3. document the reason and the expected impact
4. record the change in Version History

---

## 🕰️ Version History

| Version | Date       | Author              | Summary                                                                 |
|--------:|------------|---------------------|-------------------------------------------------------------------------|
| v11.2.6 | 2025-12-12 | `@kfm-telemetry`    | Introduced governed query test harness layout, fixtures, and snapshots. |
| v11.2.4 | 2025-12-06 | `@kfm-telemetry`    | Baseline (superseded by v11.2.6 test harness conventions).              |

---

<div align="center">

🧪 **KFM — Dashboard Query Test Harness (`queries/tests`) (v11.2.6)**  
Deterministic Fixtures · Golden Snapshots · Governance-First Dashboards

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Tests-Governed-informational" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Aligned-gold" />

[⬅ Queries Index](../README.md) ·
[📊 Dashboards Index](../../README.md) ·
[🧭 Correlation Module](../../../README.md) ·
[🧾 Telemetry Index](../../../../README.md) ·
[⚙ Workflows Index](../../../../../workflows/README.md) ·
[📄 Templates Index](../../../../../templates/README.md) ·
[📘 Markdown Protocol](../../../../../standards/kfm_markdown_protocol_v11.2.6.md) ·
[⚖ Governance Charter](../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω

</div>

