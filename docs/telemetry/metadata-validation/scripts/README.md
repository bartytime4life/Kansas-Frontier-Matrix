---
title: "🧰 Kansas Frontier Matrix — Metadata Validation Telemetry: Scripts (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/telemetry/metadata-validation/scripts/README.md"

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

telemetry_ref: "../../../../releases/v11.2.6/metadata-validation-scripts-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/metadata-validation-scripts-v11.2.6.json"
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
doc_kind: "Standard Index"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"

scope:
  domain: "telemetry-metadata-validation-scripts"
  applies_to:
    - "scripts/emit_telemetry.py"
    - "scripts/merge_telemetry.py"
    - "scripts/make_provenance.py"
    - "scripts/validate_contract.py"
    - "scripts/**"
    - "tools/**"
    - "reports/**"
    - "schemas/telemetry/**"
    - "docs/telemetry/metadata-validation/**"
    - ".github/workflows/docs-lint.yml"
    - ".github/workflows/schema-lint.yml"
    - ".github/workflows/stac-validate.yml"
    - ".github/workflows/faircare-validate.yml"
    - ".github/workflows/telemetry-export.yml"

fair_category: "F1-A1-I2-R2"
care_label: "FAIR+CARE Governance Aligned"
sensitivity: "Telemetry scripts and report normalization; low-risk when summaries are redacted"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by Metadata Validation Telemetry Scripts v12"

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
  - "docs/telemetry/metadata-validation/scripts/README.md@v11.2.4"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "../../../../schemas/json/kfm-markdown-protocol-v11.2.6.schema.json"
shape_schema_ref: "../../../../schemas/shacl/kfm-markdown-protocol-v11.2.6-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:telemetry:metadata-validation:scripts:v11.2.6"
semantic_document_id: "kfm-telemetry-metadata-validation-scripts-v11.2.6"
event_source_id: "ledger:kfm:doc:telemetry:metadata-validation:scripts:v11.2.6"
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

# 🧰 **Kansas Frontier Matrix — Metadata Validation Telemetry: Scripts**
`docs/telemetry/metadata-validation/scripts/README.md`

**Purpose**  
Define the **canonical script contract** for turning metadata-validation reports into **deterministic, governance-ready telemetry**:  
normalizing summaries, redacting sensitive payloads, validating schema conformance, and merging release snapshots.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blue" />
<img src="https://img.shields.io/badge/Telemetry-Metadata_Validation%3A_Scripts-informational" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Aligned-gold" />
<img src="https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen" />

</div>

---

## 📘 Overview

### 1. What this “Scripts” layer governs

Metadata validation produces **reports** (docs/schema/catalog/faircare summaries). This scripts layer governs:

- **Emission**: create a telemetry event from a canonical report summary.
- **Normalization**: map tool-native results to stable `check_id` / severity / counts.
- **Safety**: redact sensitive payloads and prevent secret/PII leakage into telemetry.
- **Schema compliance**: validate telemetry JSON against release-pinned schemas.
- **Merge**: append events into release snapshots without reordering or corruption.

This directory is the **authoritative contract** for how scripts must behave when they participate in metadata-validation telemetry.

### 2. Script families

Metadata validation telemetry relies on two script families:

- **Core telemetry scripts (required)**
  - `scripts/emit_telemetry.py` — transforms canonical report summaries into telemetry events.
  - `scripts/merge_telemetry.py` — merges telemetry events into release-pinned snapshots.

- **Validation and provenance helpers (recommended)**
  - `scripts/validate_contract.py` — contract checks when metadata validation is tied to data contracts.
  - `scripts/make_provenance.py` — lineage exports (PROV-friendly) associated with runs.

If additional scripts exist, they MUST conform to the deterministic and safety constraints in this document.

### 3. Determinism rules (normative)

Scripts in scope MUST:

- produce identical output for the same inputs (commit + configs + report files),
- sort lists deterministically,
- avoid timestamps inside canonical summaries unless explicitly required (and then include them only as ISO-8601),
- never emit telemetry with unstable IDs.

---

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 📁 telemetry/
    └── 📁 metadata-validation/
        ├── 📁 badges/
        │   └── 📄 README.md                         — Badge emission rules and badge registry
        ├── 📁 checks/
        │   └── 📄 README.md                         — Check taxonomy + stable check_id registry
        ├── 📁 ci/
        │   └── 📄 README.md                         — CI merge contract and pipeline wiring
        ├── 📁 reports/
        │   └── 📄 README.md                         — Canonical report artifact contract
        └── 📁 scripts/
            └── 📄 README.md                         — ← This document (script contract)

📁 scripts/
├── 📄 emit_telemetry.py                              — REQUIRED: report summary → telemetry event
├── 📄 merge_telemetry.py                             — REQUIRED: event → release snapshot append
├── 📄 make_provenance.py                             — RECOMMENDED: provenance/lineage export
└── 📄 validate_contract.py                            — OPTIONAL: contract validation (when used)

📁 reports/
└── 📁 self-validation/
    ├── 📁 docs/
    │   └── 📄 lint_summary.json                       — Docs validation canonical summary
    ├── 📁 schemas/
    │   └── 📄 lint_summary.json                       — Schema validation canonical summary
    └── 📁 stac/
        └── 📄 stac_summary.json                       — STAC/DCAT/PROV validation summary

📁 reports/
└── 📁 faircare/
    ├── 📄 faircare_summary.json                       — FAIR+CARE canonical summary
    ├── 📄 pii_scan.json                               — Redacted findings (policy-controlled)
    └── 📄 provenance_trace.json                       — Lineage artifact (optional)

📁 schemas/
└── 📁 telemetry/
    ├── 🧾 metadata-validation-scripts-v11.2.6.json     — Telemetry schema for script events
    ├── 🧾 metadata-validation-reports-v11.2.6.json      — Telemetry schema for report-derived events
    └── 🧾 metadata-validation-ci-v11.2.6.json           — Telemetry schema for CI merge evidence

📁 releases/
└── 📁 v11.2.6/
    ├── 🧾 metadata-validation-scripts-telemetry.json    — Script-run telemetry events (release-pinned)
    ├── 🧾 metadata-validation-reports-telemetry.json    — Report-derived telemetry (release-pinned)
    └── 📦 manifest.zip                                   — Manifest (hashes, refs, attestations)
~~~

---

## 🧭 Context

### 1. How this connects to workflows

Workflows produce canonical summaries; scripts emit and merge telemetry.

Typical flow:

- `docs-lint.yml` writes `reports/self-validation/docs/lint_summary.json`
- `schema-lint.yml` writes `reports/self-validation/schemas/lint_summary.json`
- `stac-validate.yml` writes `reports/self-validation/stac/stac_summary.json`
- `faircare-validate.yml` writes `reports/faircare/faircare_summary.json` (+ related artifacts)

Then:

- `scripts/emit_telemetry.py` turns those summaries into telemetry events
- `scripts/merge_telemetry.py` merges events into `releases/v11.2.6/*telemetry.json`

### 2. Why scripts are governed

Script drift is one of the fastest ways to break governance evidence:

- inconsistent fields across runs,
- non-deterministic ordering,
- unstable identifiers,
- accidental leakage of sensitive content.

This document exists to prevent that by defining a stable contract.

---

## 🗺️ Diagrams

### 1. Canonical pipeline (scripts view)

~~~mermaid
flowchart LR
  A["Validation workflow run"] --> B["Canonical summary report JSON"]
  B --> C["emit_telemetry.py"]
  C --> D["Telemetry event JSON"]
  D --> E["merge_telemetry.py"]
  E --> F["Release telemetry snapshot"]
~~~

### 2. Timeline: script behavior in CI

~~~mermaid
timeline
  title Metadata Validation Telemetry Scripts - Run Lifecycle
  section Reports
    T0 : Workflow writes canonical report summary
    T1 : Summary validated for required keys
  section Telemetry
    T2 : emit_telemetry transforms summary into event JSON
    T3 : merge_telemetry appends event into release snapshot
  section Governance
    T4 : Snapshot is indexed for dashboards and audits
~~~

---

## 🧠 Story Node & Focus Mode Integration

### 1. Story Nodes for telemetry script events

Scripts can generate story nodes like:

- `urn:kfm:story-node:telemetry:metadata-validation:scripts:<run_id>`

Recommended summary facets:

- what report kinds were emitted (docs/schema/stac/faircare),
- counts and severities (as totals),
- schema conformance (pass/fail),
- merge outcome (appended, skipped, rejected with reason).

### 2. Focus Mode constraints (normative)

Focus Mode MAY:

- summarize script health and telemetry integrity,
- show last successful merge per release,
- surface common reasons for telemetry rejection.

Focus Mode MUST NOT:

- synthesize new events when telemetry is missing,
- “repair” report results in narrative form,
- expose redacted payloads (PII/secrets/sensitive geo).

---

## 🧪 Validation & CI/CD

### 1. Script contracts (normative)

#### `scripts/emit_telemetry.py`

MUST:

- accept a `--kind` (e.g., `docs_lint`, `schema_lint`, `stac_validate`, `faircare_validate`, `metadata_validation_reports`)
- accept `--summary` pointing to a canonical summary JSON
- write `--out` telemetry event JSON
- validate output against the declared `telemetry_schema`
- refuse to emit if:
  - `check_id` values are missing where violations exist,
  - severity values are unknown,
  - redaction constraints are violated.

#### `scripts/merge_telemetry.py`

MUST:

- accept `--in` telemetry event JSON
- accept `--dest` release snapshot JSON file
- append events deterministically and validate resulting JSON
- preserve existing events and ordering rules
- refuse to merge if:
  - schema validation fails,
  - `run_id` collides with an existing event (unless an explicit overwrite policy is configured),
  - dest file is not release-pinned or is outside allowed paths.

### 2. CI requirements (normative)

CI jobs that call these scripts MUST:

- run schema validation after emission and after merge,
- persist:
  - the telemetry event,
  - the updated release snapshot,
  - the tool versions (captured in manifest or provenance).

---

## 📦 Data & Metadata

### 1. Inputs

Scripts operate on:

- canonical summary reports (JSON)
- optional supplemental artifacts:
  - `pii_scan.json` (redacted)
  - provenance traces
  - policy/threshold configs

### 2. Outputs

- **Telemetry event JSON** (single run)
- **Release telemetry snapshot JSON** (append-only, version pinned)

### 3. Example usage (local or CI)

~~~bash
# Emit an event from a canonical docs summary
python scripts/emit_telemetry.py \
  --kind docs_lint \
  --summary reports/self-validation/docs/lint_summary.json \
  --out /tmp/docs_lint_telemetry.json

# Merge into the release snapshot
python scripts/merge_telemetry.py \
  --in  /tmp/docs_lint_telemetry.json \
  --dest releases/v11.2.6/metadata-validation-reports-telemetry.json
~~~

### 4. Minimal event shape (schematic)

~~~json
{
  "workflow": "docs-lint",
  "kind": "docs_lint",
  "run_id": "docs-lint_2025-12-11T19:11:00Z",
  "schema_version": "v11.2.6",
  "status": "pass",
  "counts": {
    "targets_checked": 286,
    "errors": 0,
    "warnings": 4,
    "info": 0
  },
  "energy_wh": 2.1,
  "carbon_gco2e": 0.0008,
  "timestamp": "2025-12-11T19:11:00Z"
}
~~~

Event shape is governed by:

- `telemetry_schema` and
- the check registry under `docs/telemetry/metadata-validation/checks/`.

---

## 🌐 STAC, DCAT & PROV Alignment

### 1. DCAT

Script output files can be modeled as DCAT distributions:

- `metadata-validation-scripts-telemetry.json` as `application/json`
- release snapshot events as a dataset series for governance analytics

### 2. STAC

- Optional STAC Collection: `kfm-ci-metadata-validation`
- Items per `run_id`, with assets:
  - emitted telemetry event
  - updated release snapshot (or pointer)

Non-spatial: `geometry: null`.

### 3. PROV-O

- Activity:
  - `ex:TelemetryEmit_<run_id>` and `ex:TelemetryMerge_<run_id>`
- Entities:
  - canonical report summary (used)
  - telemetry event JSON (generated)
  - release snapshot (generated/updated)
- Agent:
  - CI runner as `prov:SoftwareAgent`

This explicitly connects: report → event → release snapshot.

---

## 🧱 Architecture

### 1. Separation of responsibilities

- Validation tools create tool-native outputs.
- Summarizers create canonical summaries.
- `emit_telemetry` normalizes summaries into events.
- `merge_telemetry` appends events into release snapshots.

This prevents “business logic” from being scattered across workflows.

### 2. Safety by default

Scripts MUST:

- redact or refuse unsafe content,
- prefer safe pointers over embedding sensitive payloads,
- keep event payloads small and structured.

---

## ⚖ FAIR+CARE & Governance

### 1. Governance constraints enforced by scripts

Scripts are governance controls because they can:

- prevent leakage of PII/secrets into telemetry,
- enforce stable identifiers and check registries,
- keep evidence deterministic and comparable across time.

### 2. Sovereignty-aware handling

If any report implicates culturally sensitive assets:

- scripts MUST ensure telemetry does not expose restricted geometry, identifiers, or location details,
- and MUST respect the sovereignty policy referenced in front-matter.

---

## 🕰️ Version History

| Version   | Date       | Author       | Summary                                                                 |
|----------:|-----------:|--------------|-------------------------------------------------------------------------|
| v11.2.6   | 2025-12-11 | `@kfm-docs`  | Built from scratch: defines deterministic, redaction-first contract for telemetry scripts and how they emit/merge release snapshots. |
| v11.2.4   | 2025-12-06 | `@kfm-docs`  | Prior baseline guidance (superseded by v11.2.6 rewrite).                |

---

<div align="center">

🧰 **KFM — Metadata Validation Telemetry: Scripts (v11.2.6)**  
Deterministic Emit · Safe Merge · Release-Pinned Evidence

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blue" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Aligned-gold" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-green" />

[⬅ Metadata Validation Telemetry](../README.md) ·
[⬅ Telemetry Home](../../README.md) ·
[🏷 Badges](../badges/README.md) ·
[✅ Checks](../checks/README.md) ·
[📦 Reports](../reports/README.md) ·
[🏗 CI Integration](../ci/README.md) ·
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