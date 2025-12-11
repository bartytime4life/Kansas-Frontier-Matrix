---
title: "🏷️ Kansas Frontier Matrix — Metadata Validation Telemetry: Badges (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/telemetry/metadata-validation/badges/README.md"

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

telemetry_ref: "../../../../releases/v11.2.6/metadata-validation-badges-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/metadata-validation-badges-v11.2.6.json"
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
  domain: "telemetry-metadata-validation-badges"
  applies_to:
    - "docs/**"
    - "mcp/**"
    - ".github/workflows/docs-lint.yml"
    - ".github/workflows/telemetry-export.yml"
    - "tools/docs/**"
    - "schemas/telemetry/**"
  non_goals:
    - "Defining footer rules (see docs/telemetry/metadata-validation/footers/* if present)"
    - "Defining full doc-lint workflow behavior (see docs/workflows/docs-lint.yml.md)"

fair_category: "F1-A1-I2-R2"
care_label: "FAIR+CARE Governance Aligned"
sensitivity: "Documentation metadata telemetry; low-risk when aggregated"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by Metadata Validation Badges Telemetry v12"

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
  - "docs/telemetry/metadata-validation/badges/README.md@v11.2.4"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "../../../../schemas/json/kfm-markdown-protocol-v11.2.6.schema.json"
shape_schema_ref: "../../../../schemas/shacl/kfm-markdown-protocol-v11.2.6-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:telemetry:metadata-validation:badges:v11.2.6"
semantic_document_id: "kfm-telemetry-metadata-validation-badges-v11.2.6"
event_source_id: "ledger:kfm:doc:telemetry:metadata-validation:badges:v11.2.6"
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
  workflow: ".github/workflows/docs-lint.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence"
  architecture: "Designed for Longevity · Governed for Integrity"
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

deprecated_fields:
  - "old_markdown_standard_v10.4"
---

<div align="center">

# 🏷️ **Kansas Frontier Matrix — Metadata Validation Telemetry: Badges**
`docs/telemetry/metadata-validation/badges/README.md`

**Purpose**  
Define the **badge validation rules** and the **telemetry emitted** when KFM documentation is checked for
badge presence, ordering, version consistency, and governance-safe claims.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Telemetry-Metadata_Validation%3A_Badges-informational" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Aligned-gold" />
<img src="https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen" />

</div>

---

## 📘 Overview

### 1. What “badge validation” means in KFM

In KFM documentation, a **badge row** is a compact, human-readable status surface that must remain:

- **Truthful** (no misleading certification or compliance claims),
- **Consistent** (same badge profile across standards/guides),
- **Version-aligned** (badge version strings match front-matter versions where required),
- **Machine-checkable** (deterministic parsing + stable identifiers).

This telemetry stream captures both:

- **Run-level summaries** (how many docs were checked; how many badge failures occurred), and
- **Doc-level violations** (missing badge row, unknown badge, order violation, version mismatch).

### 2. Badge profile (normative)

This README standardizes the `root-centered-badge-row` profile:

- Badges appear inside the initial `<div align="center"> ... </div>` header block.
- Badges MUST be rendered as `<img ... />` tags (preferred) or a single consistent alternative approved by the docs-lint configuration.
- Badge text MUST NOT assert governance states that are not recorded elsewhere (e.g., do not claim “Certified” unless the doc is under that certification program and governed).

---

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 📁 telemetry/
    └── 📁 metadata-validation/
        ├── 📁 badges/
        │   └── 📄 README.md                                     # ← This standard (badge rules + telemetry)
        ├── 📁 examples/                                         # Optional: example payloads (if present)
        │   └── 📄 README.md
        ├── 📁 specs/                                            # Optional: schema semantics (if present)
        │   └── 📄 README.md
        └── 📁 validators/                                       # Optional: validator docs (if present)
            └── 📄 README.md

📁 schemas/
└── 📁 telemetry/
    └── 🧾 metadata-validation-badges-v11.2.6.json               # Canonical schema for this telemetry stream

📁 tools/
└── 📁 docs/
    ├── ✅ validate_badges_footer.mjs                            # Badge extraction + compliance checks
    └── 📄 summarize_docs_lint.mjs                               # Aggregates checks → summary/telemetry

📁 reports/
└── 📁 self-validation/
    └── 📁 metadata-validation/
        └── 📁 badges/
            ├── 📄 badge_audit.json                              # Detailed findings (per doc)
            ├── 📄 lint_summary.json                             # Canonical machine-readable summary
            └── 📄 summary.md                                    # Human-readable summary

📁 releases/
└── 📁 v11.2.6/
    ├── 🧾 metadata-validation-badges-telemetry.json             # Aggregated telemetry for badge validation
    ├── 🧾 sbom.spdx.json
    └── 📦 manifest.zip
~~~

---

## 🧭 Context

### 1. Why badges are governed metadata

Badges are not decoration; they are a public-facing claim surface. In KFM they function as:

- a quick compliance synopsis for maintainers,
- a scan target for CI,
- a governance signal for readers.

A wrong badge can:

- misrepresent license or governance state,
- imply certification that does not exist,
- confuse version alignment between docs and standards.

### 2. Relationship to CI workflows

Badge validation commonly runs inside:

- `docs-lint.yml` (documentation compliance),
- `telemetry-export.yml` (aggregation / rollup, if used).

This README defines the **expected outputs and telemetry** regardless of the exact runner wiring.

---

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A["Markdown docs changed"] --> B["Badge validator parses header block"]
  B --> C{"Compliant?"}
  C -->|Yes| D["Emit pass summary + telemetry counters"]
  C -->|No| E["Emit violations + fail gate (per policy)"]
  D --> F["Telemetry rollup (release)"]
  E --> F
  F --> G["Governance dashboards / graph ingest"]
~~~

---

## 🧠 Story Node & Focus Mode Integration

Badge validation telemetry can be represented as Story Nodes:

- `urn:kfm:story-node:telemetry:metadata-validation:badges:<run_id>`

Focus Mode MAY:

- summarize badge compliance trends (by folder, by doc_kind, by release),
- highlight repeated failure modes (missing badge row, version mismatch),
- link from a doc to its latest badge audit record.

Focus Mode MUST NOT:

- infer certification status solely from badges,
- override document metadata or rewrite badge claims,
- expose any internal-only badge policy exceptions unless explicitly recorded.

---

## 🧪 Validation & CI/CD

### 1. Validation rules (normative)

The badge validator MUST check:

- **Presence**: required badge row exists for governed documents (per policy).
- **Ordering**: badges appear in a stable order (project-configured).
- **Version consistency**:
  - the `KFM-MDP` badge version matches `markdown_protocol_version` when present,
  - the `MCP` badge version matches `mcp_version` when present,
  - license badge matches `license` when present.
- **No misleading claims**:
  - disallow unapproved “Certified / Official / Verified” variants unless authorized by governance policy.

### 2. Severity policy (recommended defaults)

| Rule class                 | Suggested severity | Suggested gate behavior |
|---------------------------|--------------------|-------------------------|
| Missing badge row          | error              | fail for governed docs  |
| Unknown badge              | warning/error      | configurable             |
| Order violation            | warning            | configurable             |
| Version mismatch           | error              | fail                    |
| Misleading claim keyword   | error              | fail                    |

### 3. Conceptual CI step

~~~yaml
- name: Badge validation (metadata)
  run: |
    mkdir -p reports/self-validation/metadata-validation/badges
    node tools/docs/validate_badges_footer.mjs \
      --paths "docs/**" \
      --out reports/self-validation/metadata-validation/badges/badge_audit.json

    node tools/docs/summarize_docs_lint.mjs \
      --inputs "reports/self-validation/metadata-validation/badges/*.json" \
      --json "reports/self-validation/metadata-validation/badges/lint_summary.json" \
      --markdown "reports/self-validation/metadata-validation/badges/summary.md"
~~~

---

## 📦 Data & Metadata

### 1. Telemetry event types

This stream supports two primary shapes:

- **Run summary event** (`badge_validation_run`)
- **Violation event** (`badge_validation_violation`)

### 2. Minimum fields (recommended)

All telemetry entries SHOULD include:

- `workflow` (e.g., `docs-lint` or `metadata-validation`)
- `run_id` (globally unique)
- `schema_version` (e.g., `v11.2.6`)
- `timestamp` (UTC ISO-8601)
- `docs_checked` (integer)
- `violations` (integer)
- sustainability fields where available:
  - `workflow_duration_sec`
  - `energy_wh`
  - `carbon_gco2e`

Violation entries SHOULD include:

- `doc_path`
- `doc_uuid` and/or `semantic_document_id` when available
- `rule_id` (stable identifier)
- `severity` (`warning` | `error`)
- `badge_id` (if the issue is badge-specific)
- `message` (human-readable, short)

### 3. Example telemetry entries (schematic)

~~~json
{
  "workflow": "docs-lint",
  "event_type": "badge_validation_run",
  "run_id": "docs-lint_2025-12-11T19-10-00Z",
  "schema_version": "v11.2.6",
  "docs_checked": 312,
  "violations": 4,
  "workflow_duration_sec": 41,
  "energy_wh": 1.8,
  "carbon_gco2e": 0.0007,
  "timestamp": "2025-12-11T19:10:41Z"
}
~~~

~~~json
{
  "workflow": "docs-lint",
  "event_type": "badge_validation_violation",
  "run_id": "docs-lint_2025-12-11T19-10-00Z",
  "schema_version": "v11.2.6",
  "doc_path": "docs/workflows/README.md",
  "rule_id": "badge.version_mismatch.kfm_mdp",
  "severity": "error",
  "badge_id": "KFM-MDP",
  "message": "Badge version does not match markdown_protocol_version in front-matter.",
  "timestamp": "2025-12-11T19:10:12Z"
}
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

### 1. DCAT

Badge validation telemetry can be modeled as a DCAT Dataset:

- `dct:title`: "KFM Metadata Validation Telemetry — Badges"
- `dct:description`: "Run summaries and violations produced by badge validation over KFM documentation."

Distributions include:

- `metadata-validation-badges-telemetry.json` (`application/json`)
- `badge_audit.json` (`application/json`)
- `lint_summary.json` (`application/json`)
- `summary.md` (`text/markdown`)

### 2. STAC

Optional pattern:

- Collection: `kfm-ci-metadata-validation`
- Item per run: `metadata-validation-badges-<run_id>`
- Assets reference JSON/MD outputs (`geometry: null`).

### 3. PROV-O

Treat each run as:

- Activity: `ex:BadgeValidationRun_<run_id>`
- Used Entities: doc sources at commit SHA
- Generated Entities: `badge_audit.json`, `lint_summary.json`, telemetry snapshot.

---

## 🧱 Architecture

Badge validation is intentionally simple:

- **Extractor**:
  - locates the header `<div align="center">` block,
  - parses badge elements deterministically.
- **Rule engine**:
  - checks presence, ordering, and consistency vs front-matter versions.
- **Reporter**:
  - emits JSON findings + aggregated summary,
  - telemetry exporter merges into release rollups.

No component may “fix” docs automatically inside CI. Validators report; authors edit.

---

## ⚖ FAIR+CARE & Governance

Badges must not become an ungoverned channel for policy statements.

Governance expectations:

- Badges MUST reflect documented truth:
  - license badge matches `license`,
  - version badges match front matter where applicable,
  - “status” badges align with `status` fields.
- Badges MUST NOT:
  - disclose sensitive information,
  - claim certification levels that are not governed,
  - contradict FAIR+CARE labeling.

This keeps the “at-a-glance” surface compatible with FAIR+CARE responsibilities and avoids accidental misrepresentation.

---

## 🕰️ Version History

| Version   | Date       | Author             | Summary                                                                 |
|----------:|-----------:|--------------------|-------------------------------------------------------------------------|
| v11.2.6   | 2025-12-11 | `@kfm-docs`        | Built from scratch: badge profile rules + telemetry shapes + CI wiring + catalog/provenance alignment. |
| v11.2.4   | 2025-12-06 | `@kfm-docs`        | Prior baseline guidance (superseded by v11.2.6 rewrite).                |

---

<div align="center">

🏷️ **KFM — Metadata Validation Telemetry: Badges (v11.2.6)**  
Truthful Badges · Version-Aligned Metadata · Governance-Safe Signals

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Telemetry-Badges-informational" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Aligned-gold" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-green" />

[⬅ Metadata Validation Telemetry](../README.md) ·
[⬅ Telemetry Home](../../README.md) ·
[⚙ Workflows Index](../../../workflows/README.md) ·
[🧪 Docs Lint Workflow](../../../workflows/docs-lint.yml.md) ·
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