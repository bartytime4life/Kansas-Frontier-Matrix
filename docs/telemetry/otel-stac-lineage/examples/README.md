---
title: "🧪 Kansas Frontier Matrix — OTel → STAC Lineage: Examples (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/telemetry/otel-stac-lineage/examples/README.md"

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

telemetry_ref: "../../../../releases/v11.2.6/otel-stac-lineage-examples-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/otel-stac-lineage-examples-v11.2.6.json"
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
  domain: "telemetry-otel-stac-lineage-examples"
  applies_to:
    - "docs/telemetry/otel-stac-lineage/examples/**"
    - "docs/telemetry/otel-stac-lineage/specs/**"
    - "docs/telemetry/otel-stac-lineage/validators/**"
    - "schemas/telemetry/**"
    - ".github/workflows/telemetry-export.yml"
    - ".github/workflows/docs-lint.yml"

fair_category: "F1-A1-I2-R2"
care_label: "FAIR+CARE Governance Aligned"
sensitivity: "Example telemetry payloads; must not contain secrets, restricted coordinates, or identifiable individuals"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by OTel → STAC Lineage Examples v12"

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
  - "docs/telemetry/otel-stac-lineage/examples/README.md@v11.2.4"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "../../../../schemas/json/kfm-markdown-protocol-v11.2.6.schema.json"
shape_schema_ref: "../../../../schemas/shacl/kfm-markdown-protocol-v11.2.6-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:telemetry:otel-stac-lineage:examples:v11.2.6"
semantic_document_id: "kfm-telemetry-otel-stac-lineage-examples-v11.2.6"
event_source_id: "ledger:kfm:doc:telemetry:otel-stac-lineage:examples:v11.2.6"
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
  - "provenance-check"
  - "footer-check"
  - "accessibility-check"

ci_integration:
  workflow: ".github/workflows/docs-lint.yml"
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

# 🧪 **Kansas Frontier Matrix — OTel → STAC Lineage: Examples**
`docs/telemetry/otel-stac-lineage/examples/README.md`

**Purpose**  
Curated, render-safe **example payloads** demonstrating how KFM expresses **OTel lineage events** and how those events map into **STAC/DCAT/PROV** outputs.  
Examples are used for validator regression tests, documentation, onboarding, and governance auditing.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blue" />
<img src="https://img.shields.io/badge/Telemetry-Examples-informational" />
<img src="https://img.shields.io/badge/Validators-Regression_Tests-success" />
<img src="https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen" />

</div>

---

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 📁 telemetry/
    └── 📁 otel-stac-lineage/
        ├── 📄 README.md                               — Parent index (OTel → STAC lineage telemetry)
        ├── 📁 specs/
        │   └── 📄 README.md                           — Event schemas + mapping specifications
        ├── 📁 validators/
        │   └── 📄 README.md                           — Validator rules and CLI contracts
        ├── 📁 storage/
        │   └── 📄 README.md                           — Storage layout for payloads and snapshots
        └── 📁 examples/
            ├── 📄 README.md                           — ← This index
            ├── 📁 otel/
            │   ├── 📄 span_start.json                 — Minimal OTel span start event (sanitized)
            │   ├── 📄 span_end.json                   — Minimal OTel span end event (sanitized)
            │   ├── 📄 resource_attributes.json        — Resource-level attributes (service, env, runner)
            │   └── 📄 baggage_minimal.json            — Baggage example (allowed keys only)
            ├── 📁 mapping/
            │   ├── 📄 otel_to_stac_item.json          — Example STAC Item created from OTel lineage
            │   ├── 📄 otel_to_dcat_dataset.json       — Example DCAT Dataset/Distribution mapping
            │   └── 📄 otel_to_prov.json               — Example PROV-JSON mapping
            └── 📁 regression/
                ├── 📄 valid_minimal_run.json          — Minimal valid run (should PASS)
                ├── 📄 invalid_missing_run_id.json     — Missing required ID (should FAIL)
                ├── 📄 invalid_disallowed_key.json     — Contains forbidden key (should FAIL)
                └── 📄 invalid_sensitive_marker.json   — Contains sensitive marker (should FAIL)
~~~

Notes:

- Filenames and folder names are **conventions**; adjust to your repo reality, but keep the structure stable once adopted.
- Every example payload MUST be sanitized and MUST validate against the schemas described in `../specs/README.md`.

---

## 📘 Overview

Examples in this directory serve four governed purposes:

1. **Validator truth set**
   - Regression fixtures used by `docs/telemetry/otel-stac-lineage/validators/**`.

2. **Documentation and onboarding**
   - Concrete, minimal examples make the mapping rules easier to understand than prose alone.

3. **Schema evolution safety**
   - When schemas change, these fixtures catch breakage early.

4. **Governance and redaction assurance**
   - “Negative” fixtures (expected FAIL) ensure sensitive signals can’t slip into public outputs.

---

## 🧭 Context

### 1. What qualifies as a “good” example

A good example is:

- minimal (only required keys + a few meaningful optional fields),
- deterministic (stable IDs, stable timestamps patterns),
- sanitized (no secrets, no real internal URLs, no restricted coordinates),
- mapped (the example should clarify how a lineage event becomes STAC/DCAT/PROV artifacts).

### 2. Normalization and redaction boundaries

Examples MUST demonstrate:

- normalized ID patterns (`run_id`, `trace_id`, `span_id`),
- a stable `service.name` / `service.version` approach,
- a clear distinction between:
  - safe public metadata (pipeline name, artifact class),
  - restricted metadata (exact location, sensitive dataset IDs),
  - forbidden metadata (secrets, tokens, raw credentials).

---

## 🧠 Story Node & Focus Mode Integration

Examples support story-node generation without fabricating facts:

- a Story Node may reference an example fixture as:
  - “the canonical minimal representation of an OTel lineage event”
- Focus Mode MAY:
  - summarize fixture intent and how it maps to STAC/DCAT/PROV
- Focus Mode MUST NOT:
  - treat examples as real operational telemetry
  - infer real run outcomes from fixtures

---

## 🧪 Validation & CI/CD

### 1. Expected CI checks

These example files SHOULD be tested by:

- `schema-lint.yml`
  - validates example JSON payloads against declared schemas
- `docs-lint.yml`
  - validates this README’s structure and front-matter
- `telemetry-export.yml` (or a dedicated validator workflow)
  - runs validator CLI over:
    - `examples/regression/valid_*.json` (expect PASS)
    - `examples/regression/invalid_*.json` (expect FAIL)

### 2. Fixture pass/fail conventions

Regression fixtures SHOULD follow a naming convention:

- `valid_*.json` → validator MUST pass
- `invalid_*.json` → validator MUST fail, and failure reason SHOULD match fixture name

This keeps regressions obvious and reviewable.

---

## 📦 Data & Metadata

### 1. Example payload requirements (normative)

All example payloads MUST:

- be valid JSON (no trailing commas),
- include only allowed keys for the schema version,
- use placeholder-safe identifiers:
  - `run_id`: `run_YYYYMMDD_<shortid>`
  - `trace_id`: `00000000000000000000000000000000`-style hex
  - `span_id`: `0000000000000000`-style hex
- use timestamps that are realistic but non-sensitive:
  - ISO-8601 UTC, e.g. `2025-12-11T00:00:00Z`
- exclude:
  - secrets, tokens, passwords,
  - private URLs or internal hostnames,
  - restricted coordinates and sensitive site markers

### 2. Minimal example (sanitized)

This is a **schematic** minimal OTel-like lineage event (adapt field names to your actual schema):

~~~json
{
  "schema_version": "v11.2.6",
  "event_kind": "otel.lineage.span_end",
  "run_id": "run_20251211_a1b2c3",
  "trace_id": "00000000000000000000000000000000",
  "span_id": "0000000000000000",
  "parent_span_id": "0000000000000000",
  "service": {
    "name": "kfm-etl",
    "version": "11.2.6"
  },
  "environment": "dev",
  "timestamp": "2025-12-11T00:00:00Z",
  "attributes": {
    "pipeline.name": "geospatial_lidar_glo",
    "artifact.class": "stac.item",
    "artifact.role": "output"
  }
}
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

Examples SHOULD include mapping fixtures that demonstrate:

- STAC Item mapping:
  - `id`, `datetime`, `assets`, and checksum placeholders
- DCAT mapping:
  - dataset title/identifier, distributions, media types
- PROV mapping:
  - `Activity` (run), `Entity` (artifact), `Agent` (service/runner)

Where feasible, keep mapping fixtures paired:

- `otel/*.json` → raw lineage
- `mapping/*.json` → expected derived records

---

## 🧱 Architecture

The examples directory is part of a four-part contract:

- `specs/` defines what is valid
- `validators/` enforces what is valid
- `examples/` proves what is valid (and invalid)
- `storage/` defines how runtime payloads are stored

Examples are the “living unit tests” for telemetry governance.

---

## ⚖ FAIR+CARE & Governance

Even though these are “just examples,” they are governance-sensitive:

- examples must not leak sensitive data patterns,
- negative fixtures must demonstrate that governance gates work,
- reviewers must treat example updates as contract changes when they affect validation outcomes.

If an example needs to depict a sensitive scenario:

- represent it abstractly (category-level),
- use redaction placeholders,
- ensure it remains safe for `classification: Public`.

---

## 🕰️ Version History

| Version | Date       | Author        | Summary                                                                 |
|--------:|------------|---------------|-------------------------------------------------------------------------|
| v11.2.6 | 2025-12-11 | `@kfm-telemetry` | Built from scratch: establishes example fixture conventions and governance-safe payload rules for OTel → STAC lineage. |
| v11.2.4 | 2025-12-06 | `@kfm-telemetry` | Prior baseline examples guidance (superseded by v11.2.6 rewrite).        |

---

<div align="center">

🧪 **KFM — OTel → STAC Lineage: Examples (v11.2.6)**  
Sanitized Fixtures · Validator Truth Set · Governance-Safe Telemetry

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blue" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Aligned-gold" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-green" />

[⬅ OTel STAC Lineage Telemetry](../README.md) ·
[⬅ Telemetry Home](../../README.md) ·
[🧾 Specs](../specs/README.md) ·
[🧪 Validators](../validators/README.md) ·
[📦 Storage](../storage/README.md) ·
[🗺️ Diagrams](../diagrams/README.md) ·
[⚙ Workflows Index](../../../workflows/README.md) ·
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
