---
title: "🧾 Kansas Frontier Matrix — OTel → STAC Lineage: OTel Example Fixtures (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/telemetry/otel-stac-lineage/examples/otel/README.md"

version: "v11.2.6"
last_updated: "2025-12-11"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"

signature_ref: "../../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../../releases/v11.2.6/otel-stac-lineage-otel-examples-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/otel-stac-lineage-otel-examples-v11.2.6.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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
  domain: "telemetry-otel-stac-lineage-otel-examples"
  applies_to:
    - "docs/telemetry/otel-stac-lineage/examples/otel/**"
    - "docs/telemetry/otel-stac-lineage/examples/mapping/**"
    - "docs/telemetry/otel-stac-lineage/validators/**"
    - "docs/telemetry/otel-stac-lineage/specs/**"
    - "schemas/telemetry/**"

fair_category: "F1-A1-I2-R2"
care_label: "FAIR+CARE Governance Aligned"
sensitivity: "Sanitized OTel examples; no secrets; no private URLs; no sensitive coordinates"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by OTel Example Fixtures v12"

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
  - "docs/telemetry/otel-stac-lineage/examples/otel/README.md@v11.2.4"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "../../../../../schemas/json/kfm-markdown-protocol-v11.2.6.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/kfm-markdown-protocol-v11.2.6-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:telemetry:otel-stac-lineage:examples:otel:v11.2.6"
semantic_document_id: "kfm-telemetry-otel-stac-lineage-examples-otel-v11.2.6"
event_source_id: "ledger:kfm:doc:telemetry:otel-stac-lineage:examples:otel:v11.2.6"
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

# 🧾 **Kansas Frontier Matrix — OTel → STAC Lineage: OTel Example Fixtures**
`docs/telemetry/otel-stac-lineage/examples/otel/README.md`

**Purpose**  
Provide **sanitized OpenTelemetry (OTel) example events** used as canonical fixtures for:  
**mapping** (OTel → STAC/DCAT/PROV), **validators**, and **regression tests** across the Kansas Frontier Matrix (KFM).

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blue" />
<img src="https://img.shields.io/badge/Examples-OTel_Fixtures-success" />
<img src="https://img.shields.io/badge/Lineage-OTel_%E2%86%92_STAC%2FDCAT%2FPROV-informational" />
<img src="https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen" />

</div>

---

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 📁 telemetry/
    └── 📁 otel-stac-lineage/
        ├── 📄 README.md                                — Root index for OTel → STAC lineage
        ├── 📁 diagrams/                                — Mermaid + architecture diagrams
        ├── 📁 specs/                                   — Normative mapping and schema specs
        ├── 📁 validators/                              — Validator rules + CLI usage
        ├── 📁 storage/                                 — Storage layout + retention conventions
        └── 📁 examples/
            ├── 📄 README.md                            — Examples index (fixtures + conventions)
            ├── 📁 otel/                                — ← This folder (raw OTel-shaped fixtures)
            │   ├── 📄 README.md                        — This file
            │   ├── 📄 otel_bundle_minimal.json         — Minimal bundle (resource + span + log)
            │   ├── 📄 resource_kfm_ci.json             — Resource example (service, env, versions)
            │   ├── 📄 span_start_minimal.json          — Span start (minimal fields)
            │   ├── 📄 span_end_minimal.json            — Span end (minimal fields)
            │   ├── 📄 span_end_with_attributes.json    — Span end with KFM attributes
            │   ├── 📄 log_event_minimal.json           — Log record example (sanitized)
            │   └── 📄 otel_examples_manifest.json      — Index describing each fixture + intent
            ├── 📁 mapping/                              — Paired outputs (STAC/DCAT/PROV fixtures)
            └── 📁 regression/                           — PASS/FAIL examples for validator tests
~~~

**Notes**

- Filenames shown above are the **canonical naming pattern** for v11.2.6.
- If your repo uses different filenames today, align to these names during the next governed cleanup,
  and keep backwards-compatibility via manifest aliases (not by duplicating fixtures).

---

## 📘 Overview

OTel fixtures in this directory are intentionally small, readable, and governance-safe.

They exist so that KFM can answer (deterministically):

- What minimum telemetry we require to claim a “workflow run” happened
- How we represent lineage consistently (trace/span/log/resource)
- What attributes are mapped into STAC/DCAT/PROV and which are intentionally excluded

**Core rule (normative):**

> Examples here are *fixtures*, not operational exports.  
> They MUST remain sanitized and MUST NOT contain secrets, internal URLs, or sensitive coordinates.

---

## 🧭 Context

### 1. Why “raw OTel” examples matter

KFM maps telemetry into governance-friendly records. That mapping is only as stable as:

- the raw OTel event shapes we accept
- the attribute naming conventions we enforce
- the redaction/sanitization rules we apply before publishing artifacts

Therefore:

- `examples/otel/` provides **inputs**
- `examples/mapping/` provides **expected outputs**
- `examples/regression/` provides **validator PASS/FAIL cases**

### 2. What “OTel” means here

These fixtures represent the *shape* of OTel data KFM consumes:

- Resource (service identity, environment, versions)
- Span(s) (activity boundaries, start/end timestamps, status)
- Log record(s) (events: warnings, audit actions, governance gates)

KFM does not require every OTel field; it requires a governed minimum set.

---

## 🗺️ Diagrams

### Fixture → Mapping → Validation (Conceptual)

~~~mermaid
flowchart LR
  OTEL["OTel fixtures (examples/otel)"] --> MAP["Mapping layer (specs)"]
  MAP --> OUT["Expected outputs (examples/mapping)"]
  OTEL --> VAL["Validators (validators)"]
  OUT --> VAL
  VAL --> CI["CI checks (docs-lint / schema-lint)"]
~~~

---

## 🧪 Validation & CI/CD

### 1. Required checks

These example files SHOULD be checked by:

- `docs-lint.yml` (structure + front-matter rules on READMEs)
- `schema-lint.yml` (schemas referenced by validators/specs)
- OTel fixture validator (project-local) to ensure:
  - required fields exist
  - IDs are well-formed
  - timestamps are ISO-8601 UTC
  - prohibited content is absent

### 2. What should fail CI

CI SHOULD fail if any fixture contains:

- secrets/tokens (even fake-looking tokens that match secret patterns)
- private hostnames, internal IPs, internal repository URLs
- real person identifiers (names/emails) unless explicitly allowed and sanitized
- precise coordinates or site identifiers for sensitive contexts

---

## 📦 Data & Metadata

### 1. Fixture naming conventions

Use descriptive names with predictable suffixes:

- `*_minimal.json` — smallest accepted payload for a category
- `*_with_attributes.json` — demonstrates KFM-specific attributes
- `*_bundle_*.json` — multi-record bundles for end-to-end tests
- `*_manifest.json` — index file linking fixture → purpose → expected mappings

### 2. Recommended otel_examples_manifest.json shape

`otel_examples_manifest.json` SHOULD document each fixture:

~~~json
{
  "schema_version": "v11.2.6",
  "kind": "otel_examples_manifest",
  "examples": [
    {
      "id": "span_end_minimal",
      "path": "./span_end_minimal.json",
      "category": "span",
      "intent": "minimum acceptable end-of-span event",
      "expected_mapping_refs": [
        "../mapping/otel_to_stac_item.json",
        "../mapping/otel_to_prov.json"
      ],
      "notes": "No sensitive attributes; safe for public repo."
    }
  ]
}
~~~

### 3. Minimal span end example (sanitized, schematic)

This is an example of the *shape* these fixtures should use (your spec may be stricter):

~~~json
{
  "resource": {
    "service.name": "kfm-ci",
    "deployment.environment": "dev",
    "service.version": "v11.2.6"
  },
  "span": {
    "trace_id": "00000000000000000000000000000001",
    "span_id": "0000000000000001",
    "parent_span_id": "0000000000000000",
    "name": "workflow.run",
    "kind": "INTERNAL",
    "start_time": "2025-12-11T00:00:00Z",
    "end_time": "2025-12-11T00:00:05Z",
    "status": { "code": "OK" },
    "attributes": {
      "kfm.run_id": "run_20251211_a1b2c3",
      "kfm.workflow": "telemetry-export",
      "kfm.classification": "Public",
      "kfm.care_tag": "public"
    }
  }
}
~~~

**Sanitization notes**

- IDs are deterministic test values, not real trace IDs.
- `kfm.run_id` is a placeholder, not a real GitHub run ID.
- No URLs or tokens are present.

---

## 🌐 STAC, DCAT & PROV Alignment

These fixtures are designed to support deterministic mapping:

- **STAC**: span and log attributes become `properties.kfm:*` and `assets.*` (as allowed)
- **DCAT**: resource identity and run metadata become dataset/distribution descriptors
- **PROV**: spans map naturally to `prov:Activity`, artifacts to `prov:Entity`, services to `prov:Agent`

If a fixture cannot map cleanly, it belongs in:

- `examples/regression/` (negative cases), or
- `specs/` (if the spec needs to evolve), not here.

---

## 🧱 Architecture

The OTel example set is intentionally layered:

- **raw OTel fixtures** demonstrate input contracts
- **mapping fixtures** demonstrate expected output contracts
- **regression fixtures** test strictness and failure modes

This separation keeps examples easy to review and safe to publish.

---

## ⚖ FAIR+CARE & Governance

OTel examples are governance artifacts. They must:

- demonstrate ethical defaults (no unnecessary identifiers)
- show how classification and CARE tags are carried through
- remain publishable under KFM’s public documentation posture

When demonstrating sensitive scenarios:

- do it via labels and flags (e.g., `kfm.care_tag: "restricted"`)
- do not include the sensitive payload itself

---

## 🕰️ Version History

| Version | Date       | Author           | Summary                                                                 |
|--------:|------------|------------------|-------------------------------------------------------------------------|
| v11.2.6 | 2025-12-11 | `@kfm-telemetry` | Built from scratch: establishes canonical OTel fixture naming, manifest expectations, and governance-safe content rules. |
| v11.2.4 | 2025-12-06 | `@kfm-telemetry` | Prior baseline examples guidance (superseded by v11.2.6 rewrite).       |

---

<div align="center">

🧾 **KFM — OTel → STAC Lineage: OTel Example Fixtures (v11.2.6)**  
Sanitized Inputs · Deterministic Contracts · Governance-Safe Telemetry

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blue" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Aligned-gold" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-green" />

[⬅ Examples](../README.md) ·
[⬅ OTel STAC Lineage Telemetry](../../README.md) ·
[🧩 Mapping Examples](../mapping/README.md) ·
[🧪 Regression Fixtures](../regression/README.md) ·
[🧾 Specs](../../specs/README.md) ·
[🧪 Validators](../../validators/README.md) ·
[📦 Storage](../../storage/README.md) ·
[🗺️ Diagrams](../../diagrams/README.md) ·
[⚙ Workflows Index](../../../../workflows/README.md) ·
[⚙ Telemetry Export Workflow](../../../../workflows/telemetry-export.yml.md) ·
[📘 Docs Root](../../../../README.md) ·
[📘 Markdown Protocol](../../../../standards/kfm_markdown_protocol_v11.2.6.md) ·
[⚖ Governance Charter](../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[📚 Glossary](../../../../glossary.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω

</div>

