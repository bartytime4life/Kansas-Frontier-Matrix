---
title: "🏗️ Kansas Frontier Matrix — Metadata Validation Telemetry: CI Integration (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/telemetry/metadata-validation/ci/README.md"

version: "v11.2.6"
last_updated: "2025-12-11"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"

signature_ref: "../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../releases/v11.2.6/metadata-validation-ci-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/metadata-validation-ci-v11.2.6.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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
diagram_profiles:
  - "mermaid-flowchart-v1"

scope:
  domain: "telemetry-metadata-validation-ci"
  applies_to:
    - ".github/workflows/docs-lint.yml"
    - ".github/workflows/schema-lint.yml"
    - ".github/workflows/stac-validate.yml"
    - ".github/workflows/faircare-validate.yml"
    - ".github/workflows/telemetry-export.yml"
    - "docs/telemetry/metadata-validation/**"
    - "reports/self-validation/**"
    - "schemas/telemetry/**"
    - "scripts/emit_telemetry.py"
    - "scripts/merge_telemetry.py"
    - "tools/**"

fair_category: "F1-A1-I2-R2"
care_label: "FAIR+CARE Governance Aligned"
sensitivity: "CI telemetry and validation summaries; low-risk when aggregated"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by Metadata Validation Telemetry CI Integration v12"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/telemetry/metadata-validation/ci/README.md@v11.2.4"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "../../../../schemas/json/kfm-markdown-protocol-v11.2.6.schema.json"
shape_schema_ref: "../../../../schemas/shacl/kfm-markdown-protocol-v11.2.6-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:telemetry:metadata-validation:ci:v11.2.6"
semantic_document_id: "kfm-telemetry-metadata-validation-ci-v11.2.6"
event_source_id: "ledger:kfm:doc:telemetry:metadata-validation:ci:v11.2.6"
doc_integrity_checksum: "<sha256>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"
transform_registry:
  allowed:
    - "summary"
    - "timeline-generation"
    - "semantic-highlighting"
    - "a11y-adaptations"
    - "diagram-extraction"
    - "metadata-extraction"
  prohibited:
    - "content-alteration"
    - "speculative-additions"
    - "unverified-architectural-claims"
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
  - "diagram-check"
  - "accessibility-check"
  - "provenance-check"
  - "footer-check"

ci_integration:
  workflow: ".github/workflows/telemetry-export.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence"
  architecture: "Designed for Longevity · Governed for Integrity"
  telemetry: "Transparent Systems · Ethical Metrics · Sustainable Intelligence"
  pipeline: "Deterministic Pipelines · Explainable AI · Open Provenance"
  graph: "Semantics × Provenance × Spatial Intelligence"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

deprecated_fields:
  - "old_markdown_standard_v10.4"
---

<div align="center">

# 🏗️ **Kansas Frontier Matrix — Metadata Validation Telemetry: CI Integration**
`docs/telemetry/metadata-validation/ci/README.md`

**Purpose**  
Define how KFM CI workflows emit **metadata validation telemetry** in a consistent, governance-ready form.  
This standard aligns validation outputs from multiple workflows into a single, queryable telemetry layer for dashboards, catalogs, and the knowledge graph.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Telemetry-Metadata_Validation%3A_CI-informational" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Aligned-gold" />
<img src="https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen" />

</div>

---

## 📘 Overview

### 1. What “CI integration” means here

KFM treats CI validation as a governed data pipeline. Metadata validation telemetry is the mechanism that makes validation outcomes:

- **Comparable across workflows** (stable IDs, consistent severity/result semantics),
- **Auditable across releases** (version-pinned, provenance-friendly),
- **Safe for governance** (no secrets, no PII, no sensitive coordinates),
- **Machine-joinable** with catalogs and the knowledge graph.

This CI integration layer defines **how** to:

- Produce canonical summaries from validators,
- Normalize those summaries into telemetry events,
- Merge events into release-scoped telemetry snapshots.

### 2. Normative contract (what every contributing workflow MUST do)

A workflow that claims to emit metadata validation telemetry MUST:

1. Write machine-readable validation artifacts under `reports/self-validation/**` (or a workflow-specific reports root).
2. Produce either:
   - a canonical JSON summary (`*_summary.json` or `lint_summary.json`), or
   - a structured per-target result file that can be summarized deterministically.
3. Emit telemetry conforming to the schema referenced by `telemetry_schema`.
4. Merge telemetry into a version-pinned release file under `releases/v11.2.6/`.

If any step is missing, telemetry is considered **non-governed** and MUST NOT be used for certification or governance decisions.

---

## 🗂️ Directory Layout

~~~text
📁 .github/
└── 📁 workflows/
    ├── 📄 docs-lint.yml                      — Docs structure + front-matter validation
    ├── 📄 schema-lint.yml                    — JSON Schema + SHACL validation
    ├── 📄 stac-validate.yml                  — STAC/DCAT/PROV validation
    ├── 📄 faircare-validate.yml              — FAIR+CARE governance checks
    └── 📄 telemetry-export.yml               — Telemetry aggregation + merge into releases

📁 docs/
└── 📁 telemetry/
    └── 📁 metadata-validation/
        ├── 📁 checks/
        │   └── 📄 README.md                  — Check taxonomy + event semantics
        ├── 📁 badges/
        │   └── 📄 README.md                  — Badge rules + badge telemetry semantics
        └── 📁 ci/
            └── 📄 README.md                  — ← This document (CI integration contract)

📁 schemas/
└── 📁 telemetry/
    ├── 🧾 metadata-validation-checks-v11.2.6.json  — Check telemetry schema
    ├── 🧾 metadata-validation-badges-v11.2.6.json  — Badge telemetry schema (if used)
    └── 🧾 metadata-validation-ci-v11.2.6.json      — CI integration telemetry schema (this doc)

📁 reports/
└── 📁 self-validation/
    ├── 📁 docs/
    │   └── 📄 lint_summary.json               — Docs lint canonical summary
    ├── 📁 schemas/
    │   └── 📄 lint_summary.json               — Schema lint canonical summary
    ├── 📁 stac/
    │   └── 📄 stac_summary.json               — STAC/DCAT validation summary
    └── 📁 metadata-validation/
        └── 📁 ci/
            ├── 📄 ci_summary.json             — Cross-workflow aggregation summary (optional)
            └── 📄 summary.md                  — Human summary for PRs (optional)

📁 scripts/
├── ✅ emit_telemetry.py                       — Emits telemetry records from summaries
└── ✅ merge_telemetry.py                      — Appends run telemetry → release snapshot

📁 releases/
└── 📁 v11.2.6/
    ├── 🧾 focus-telemetry.json                      — Unified telemetry stream (repo-wide)
    ├── 🧾 metadata-validation-checks-telemetry.json  — Check outcomes (cross-workflow)
    ├── 🧾 metadata-validation-badges-telemetry.json  — Badge outcomes (if used)
    └── 🧾 metadata-validation-ci-telemetry.json      — CI integration telemetry (this layer)

📁 tools/
└── 📁 validation/
    ├── ✅ normalize_check_ids.py              — Stabilizes check IDs across sources (recommended)
    ├── ✅ emit_check_telemetry.py             — Emits check events from tool-native outputs (recommended)
    └── ✅ emit_badge_telemetry.py             — Emits badge events from doc audits (recommended)
~~~

---

## 🧭 Context

### 1. CI as governed pipeline evidence

In KFM, CI outputs are governance evidence. Metadata validation telemetry is used for:

- release gating (required checks),
- governance dashboards,
- catalog/graph ingestion (DCAT/STAC/PROV modeling of validation events),
- longitudinal trend analysis (quality, debt, regressions, sustainability).

### 2. Contributing workflows

Metadata validation telemetry is a “join layer” across these workflow families:

- **Docs validation**
  - `docs-lint.yml` produces doc structural results (front-matter, headings, links, mermaid rules, etc.)
- **Schema validation**
  - `schema-lint.yml` validates JSON Schemas, SHACL, examples/configs
- **Catalog validation**
  - `stac-validate.yml` validates STAC Items/Collections and related DCAT/PROV mappings
- **Governance validation**
  - `faircare-validate.yml` validates FAIR+CARE and sovereignty constraints
- **Telemetry merge**
  - `telemetry-export.yml` aggregates and merges telemetry to release snapshots

This CI integration layer exists so governance systems can answer:

- “What failed, where, and under which rule?”
- “Which workflow produced the evidence?”
- “Is it stable across releases and safe to publish?”

---

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A["Validators run in CI"] --> B["Tool-native reports written"]
  B --> C["Canonical summaries produced"]
  C --> D["Telemetry emitted from summaries"]
  D --> E["Telemetry merged into releases/v11.2.6"]
  E --> F["Dashboards, catalogs, and graph ingest"]
~~~

---

## 🧠 Story Node & Focus Mode Integration

### 1. Story Node patterns

CI integration telemetry can generate Story Nodes such as:

- `urn:kfm:story-node:telemetry:metadata-validation:ci:<run_id>`

These Story Nodes SHOULD summarize:

- which workflows ran,
- which check families were involved (docs/schema/catalog/governance),
- the top failing `check_id`s and affected targets,
- links to summary artifacts.

### 2. Focus Mode behavior (normative)

Focus Mode MAY:

- present “validation health” by directory, workflow, and rule,
- show regression trends across releases,
- link to authoritative specs for remediation.

Focus Mode MUST NOT:

- invent missing workflow runs,
- reclassify severity without recorded telemetry,
- surface sensitive payloads outside governance policy.

---

## 🧪 Validation & CI/CD

### 1. Event taxonomy for CI integration (normative)

This layer is intentionally minimal. CI integration telemetry SHOULD capture:

- that workflows emitted telemetry successfully,
- schema version compatibility,
- merge success/failure,
- aggregation counters (optional).

Recommended event types:

- `metadata_ci_run` — per workflow run (high-level)
- `metadata_ci_merge` — merge action result (append to release snapshot)

### 2. Minimum required fields (normative)

A CI integration telemetry record MUST include:

- `workflow`
- `event_type`
- `run_id`
- `schema_version` (e.g., `v11.2.6`)
- `commit_sha`
- `status` (`success` | `failure` | `partial`)
- `timestamp`

It SHOULD include:

- `artifacts` (list of canonical summary paths)
- `merge_dest` (release telemetry file)
- `workflow_duration_sec`
- `energy_wh`
- `carbon_gco2e`

### 3. Conceptual GitHub Actions pattern

~~~yaml
- name: Produce canonical summary (example)
  run: |
    mkdir -p reports/self-validation/metadata-validation/ci
    python tools/validation/aggregate_validation_summaries.py \
      --docs   reports/self-validation/docs/lint_summary.json \
      --schemas reports/self-validation/schemas/lint_summary.json \
      --stac   reports/self-validation/stac/stac_summary.json \
      --out    reports/self-validation/metadata-validation/ci/ci_summary.json

- name: Emit CI integration telemetry
  run: |
    python scripts/emit_telemetry.py \
      --kind metadata_validation_ci \
      --summary reports/self-validation/metadata-validation/ci/ci_summary.json \
      --out metadata_validation_ci_telemetry.json

- name: Merge CI integration telemetry → release snapshot
  run: |
    python scripts/merge_telemetry.py \
      --in  metadata_validation_ci_telemetry.json \
      --dest releases/v11.2.6/metadata-validation-ci-telemetry.json
~~~

---

## 📦 Data & Metadata

### 1. Canonical artifacts

This CI integration layer assumes the existence of canonical summaries produced by contributor workflows, such as:

- `reports/self-validation/docs/lint_summary.json`
- `reports/self-validation/schemas/lint_summary.json`
- `reports/self-validation/stac/stac_summary.json`
- `reports/faircare/faircare_summary.json` (if used)
- `reports/self-validation/metadata-validation/ci/ci_summary.json` (optional aggregator)

### 2. Release-level outputs

Release telemetry snapshots MUST be version-pinned:

- `releases/v11.2.6/metadata-validation-ci-telemetry.json`
- `releases/v11.2.6/metadata-validation-checks-telemetry.json`
- `releases/v11.2.6/metadata-validation-badges-telemetry.json` (if badges telemetry is enabled)

These snapshots are considered governance evidence for the release series.

---

## 🌐 STAC, DCAT & PROV Alignment

### 1. DCAT

Model CI integration telemetry as a DCAT Dataset:

- `dct:title`: "KFM Metadata Validation Telemetry — CI Integration"
- Distributions:
  - `metadata-validation-ci-telemetry.json`
  - per-run summaries (`ci_summary.json`, `summary.md` where present)

### 2. STAC

Optional pattern:

- Collection: `kfm-ci-metadata-validation`
- Items: one per `run_id`
- Assets: telemetry + canonical summaries (`geometry: null`).

### 3. PROV-O

- Activity: `ex:MetadataValidationCI_<run_id>`
- Used: repo state at `commit_sha`, contributor summaries
- Generated: CI integration telemetry record + merged release snapshot
- Agents: CI runner as `prov:SoftwareAgent`.

---

## 🧱 Architecture

### 1. Separation of concerns

- Workflows produce **domain-native** reports (docs lint, schema lint, STAC validation).
- Emitters normalize into **telemetry** (stable schema).
- Merge step appends telemetry to a **release snapshot** (time-series evidence).

### 2. Determinism requirements

To remain governed, CI integration MUST be deterministic:

- no nondeterministic ordering of emitted events,
- stable check IDs (see `docs/telemetry/metadata-validation/checks/README.md`),
- version-pinned schemas and release paths.

---

## ⚖ FAIR+CARE & Governance

Metadata validation telemetry is governance evidence, so it MUST:

- avoid secrets and tokens,
- avoid raw PII and sensitive site details,
- prefer category/count reporting over raw payloads,
- respect sovereignty flags (do not publish restricted coordinates or culturally sensitive details).

If a workflow needs to reference restricted findings, it SHOULD:

- emit a redacted check event,
- provide a governance-safe pointer (e.g., internal artifact path) rather than embedding the sensitive detail.

---

## 🕰️ Version History

| Version   | Date       | Author        | Summary                                                                 |
|----------:|-----------:|---------------|-------------------------------------------------------------------------|
| v11.2.6   | 2025-12-11 | `@kfm-docs`   | Built from scratch: CI integration contract for metadata validation telemetry, including artifact expectations, emission/merge patterns, and governance-safe constraints. |
| v11.2.4   | 2025-12-06 | `@kfm-docs`   | Prior baseline guidance (superseded by v11.2.6 rewrite).                |

---

<div align="center">

🏗️ **KFM — Metadata Validation Telemetry: CI Integration (v11.2.6)**  
Deterministic Evidence · Release-Pinned Telemetry · Governance-Ready CI

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blue" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Aligned-gold" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-green" />

[⬅ Metadata Validation Telemetry](../README.md) ·
[⬅ Telemetry Home](../../README.md) ·
[✅ Checks Telemetry](../checks/README.md) ·
[🏷 Badges Telemetry](../badges/README.md) ·
[⚙ Workflows Index](../../../workflows/README.md) ·
[🧪 Docs Lint Workflow](../../../workflows/docs-lint.yml.md) ·
[🧩 Schema Lint Workflow](../../../workflows/schema-lint.yml.md) ·
[🗺 STAC Validate Workflow](../../../workflows/stac-validate.yml.md) ·
[⚖ FAIR+CARE Validate Workflow](../../../workflows/faircare-validate.yml.md) ·
[⚙ Telemetry Export Workflow](../../../workflows/telemetry-export.yml.md) ·
[📘 Docs Root](../../../README.md) ·
[📘 Markdown Protocol](../../../standards/kfm_markdown_protocol_v11.2.6.md) ·
[⚖ Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[📚 Glossary](../../../glossary.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω  

</div>