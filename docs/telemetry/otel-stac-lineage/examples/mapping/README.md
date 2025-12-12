---
title: "🧭 Kansas Frontier Matrix — OTel → STAC Lineage: Mapping Examples (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/telemetry/otel-stac-lineage/examples/mapping/README.md"

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

telemetry_ref: "../../../../../releases/v11.2.6/otel-stac-lineage-mapping-examples-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/otel-stac-lineage-mapping-examples-v11.2.6.json"
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
  domain: "telemetry-otel-stac-lineage-mapping-examples"
  applies_to:
    - "docs/telemetry/otel-stac-lineage/examples/mapping/**"
    - "docs/telemetry/otel-stac-lineage/specs/**"
    - "docs/telemetry/otel-stac-lineage/validators/**"
    - "schemas/telemetry/**"

fair_category: "F1-A1-I2-R2"
care_label: "FAIR+CARE Governance Aligned"
sensitivity: "Mapping examples; sanitized; no secrets, restricted coordinates, or identifiable individuals"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by OTel → STAC Lineage Mapping Examples v12"

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
  - "docs/telemetry/otel-stac-lineage/examples/mapping/README.md@v11.2.4"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "../../../../../schemas/json/kfm-markdown-protocol-v11.2.6.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/kfm-markdown-protocol-v11.2.6-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:telemetry:otel-stac-lineage:examples:mapping:v11.2.6"
semantic_document_id: "kfm-telemetry-otel-stac-lineage-examples-mapping-v11.2.6"
event_source_id: "ledger:kfm:doc:telemetry:otel-stac-lineage:examples:mapping:v11.2.6"
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

# 🧭 **Kansas Frontier Matrix — OTel → STAC Lineage: Mapping Examples**
`docs/telemetry/otel-stac-lineage/examples/mapping/README.md`

**Purpose**  
Provide **paired mapping fixtures** showing how KFM converts **OTel lineage events** into **STAC Items**, **DCAT Datasets/Distributions**, and **PROV records**.  
These mappings are the contract examples used by validators, tests, and governance review.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blue" />
<img src="https://img.shields.io/badge/Mapping-STAC_%7C_DCAT_%7C_PROV-informational" />
<img src="https://img.shields.io/badge/Examples-Regression_Fixtures-success" />
<img src="https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen" />

</div>

---

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 📁 telemetry/
    └── 📁 otel-stac-lineage/
        └── 📁 examples/
            ├── 📄 README.md                           — Examples index (fixtures + conventions)
            ├── 📁 otel/                               — Raw OTel-shaped lineage examples
            ├── 📁 regression/                         — PASS/FAIL validator fixtures
            └── 📁 mapping/
                ├── 📄 README.md                       — ← This index
                ├── 📄 otel_to_stac_item.json          — OTel lineage → STAC Item mapping example
                ├── 📄 otel_to_dcat_dataset.json       — OTel lineage → DCAT dataset/distribution example
                ├── 📄 otel_to_prov.json               — OTel lineage → PROV-JSON mapping example
                └── 📄 mapping_manifest.json           — Index linking input fixture(s) → output fixture(s)
~~~

---

## 📘 Overview

Mapping examples in this directory answer a single governance question:

> “Given this lineage event, what exact STAC/DCAT/PROV records should be emitted — and why?”

They are used for:

- validator regression tests (ensure mappings remain stable),
- schema evolution safety (catch breaking changes),
- onboarding (make mapping rules concrete),
- auditability (prove what gets emitted and what is intentionally excluded).

---

## 🧭 Context

### 1. What “mapping” means in KFM

A mapping fixture is a **pair (or trio)** of deterministic, sanitized outputs:

- **Input:** OTel lineage event (or a small bundle of events)
- **Output A:** STAC Item (non-spatial allowed; geometry may be `null`)
- **Output B:** DCAT Dataset/Distribution
- **Output C:** PROV record (PROV-JSON or PROV-friendly JSON)

Mappings MUST demonstrate:

- stable identifiers,
- provenance linkage,
- checksum placeholders,
- governance labels and sensitivity handling.

### 2. Guardrails for mapping examples

Mapping examples MUST NOT include:

- secrets, tokens, credentials,
- internal hostnames or private service URLs,
- sensitive site coordinates or restricted dataset IDs,
- any information that could turn an example into a real operational trace.

---

## 🗺️ Diagrams

### Mapping Flow (Conceptual)

~~~mermaid
flowchart LR
  IN["OTel lineage event (example)"] --> MAP["Mapping rules (specs)"]
  MAP --> STAC["STAC Item fixture"]
  MAP --> DCAT["DCAT Dataset/Distribution fixture"]
  MAP --> PROV["PROV fixture"]
  STAC --> VAL["Validators + schema-lint"]
  DCAT --> VAL
  PROV --> VAL
~~~

---

## 🧪 Validation & CI/CD

### 1. Required validations

These files SHOULD be validated by:

- schema checks in `schema-lint.yml`
- example checks in `otel-stac-lineage` validator tooling (see `../../validators/README.md`)

### 2. Expected invariants

A mapping fixture set SHOULD satisfy:

- **ID stability:** output `id`s derived from `run_id` and/or `trace_id` deterministically
- **Linkage:** STAC/DCAT/PROV must reference each other via stable IDs or resolvable links
- **Checksums:** if checksums are included, use placeholders (`<sha256>`) or deterministic test values
- **Governance:** include classification/care_tag fields only where allowed by schemas

---

## 📦 Data & Metadata

### 1. Recommended mapping_manifest.json structure

`mapping_manifest.json` SHOULD explicitly describe pairings:

~~~json
{
  "schema_version": "v11.2.6",
  "kind": "mapping_manifest",
  "mappings": [
    {
      "input": "../otel/span_end.json",
      "outputs": {
        "stac_item": "./otel_to_stac_item.json",
        "dcat": "./otel_to_dcat_dataset.json",
        "prov": "./otel_to_prov.json"
      },
      "notes": "Minimal end-of-span lineage mapped to non-spatial STAC/DCAT/PROV."
    }
  ]
}
~~~

### 2. Minimal STAC item (schematic)

Keep STAC fixtures minimal and non-controversial:

~~~json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "kfm-ci-run_20251211_a1b2c3",
  "geometry": null,
  "properties": {
    "datetime": "2025-12-11T00:00:00Z",
    "kfm:run_id": "run_20251211_a1b2c3",
    "kfm:workflow": "telemetry-export",
    "kfm:classification": "Public"
  },
  "links": [
    { "rel": "self", "href": "<href>" }
  ],
  "assets": {
    "telemetry": {
      "href": "<href>",
      "type": "application/json",
      "title": "OTel lineage telemetry snapshot",
      "roles": ["data"]
    }
  }
}
~~~

### 3. Minimal DCAT (schematic)

~~~json
{
  "@context": "<dcat-context>",
  "@type": "dcat:Dataset",
  "dct:title": "KFM Lineage Export — run_20251211_a1b2c3",
  "dct:identifier": "kfm-lineage-run_20251211_a1b2c3",
  "dct:license": "CC-BY 4.0",
  "dcat:distribution": [
    {
      "@type": "dcat:Distribution",
      "dct:title": "Telemetry snapshot",
      "dcat:mediaType": "application/json",
      "dcat:downloadURL": "<href>",
      "spdx:checksum": { "spdx:algorithm": "spdx:checksumAlgorithm_sha256", "spdx:checksumValue": "<sha256>" }
    }
  ]
}
~~~

### 4. Minimal PROV (schematic)

~~~json
{
  "entity": {
    "ex:TelemetrySnapshot_run_20251211_a1b2c3": {
      "prov:type": "ex:TelemetrySnapshot"
    }
  },
  "activity": {
    "ex:LineageExport_run_20251211_a1b2c3": {
      "prov:type": "ex:WorkflowRun"
    }
  },
  "wasGeneratedBy": {
    "_:wgb1": {
      "prov:entity": "ex:TelemetrySnapshot_run_20251211_a1b2c3",
      "prov:activity": "ex:LineageExport_run_20251211_a1b2c3"
    }
  }
}
~~~

These are examples of *shape*, not a substitute for your authoritative schemas.

---

## 🌐 STAC, DCAT & PROV Alignment

Mapping fixtures SHOULD make alignment explicit:

- STAC `properties.kfm:*` is the bridge to governance tags and run metadata
- DCAT is the catalog-friendly view (datasets + distributions)
- PROV is the lineage-native view (entities, activities, agents)

When possible, include stable cross-references:

- STAC Item `id` ↔ DCAT `dct:identifier` ↔ PROV entity/activity IDs

---

## 🧱 Architecture

This directory is intentionally simple:

- specs define mapping rules
- validators enforce mapping rules
- mapping examples prove mapping rules

If you add a new mapping type, you MUST add:

- a schema change (if required),
- at least one new mapping example,
- at least one regression fixture validating it.

---

## ⚖ FAIR+CARE & Governance

Mapping examples are part of governance evidence:

- they demonstrate what KFM emits publicly,
- they demonstrate what KFM refuses to emit (by omission and by negative fixtures),
- they keep the telemetry system safe for sensitive contexts.

If an example needs to depict a sensitive workflow:

- represent sensitivity using a category label (not raw data),
- keep geometry `null`,
- keep dataset identifiers abstract.

---

## 🕰️ Version History

| Version | Date       | Author           | Summary                                                                 |
|--------:|------------|------------------|-------------------------------------------------------------------------|
| v11.2.6 | 2025-12-11 | `@kfm-telemetry` | Built from scratch: defines mapping fixture patterns and minimal STAC/DCAT/PROV shapes for OTel lineage examples. |
| v11.2.4 | 2025-12-06 | `@kfm-telemetry` | Prior baseline mapping examples guidance (superseded by v11.2.6 rewrite). |

---

<div align="center">

🧭 **KFM — OTel → STAC Lineage: Mapping Examples (v11.2.6)**  
Deterministic Fixtures · Contract Clarity · Governance-Safe Mappings

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blue" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Aligned-gold" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-green" />

[⬅ Examples](../README.md) ·
[⬅ OTel STAC Lineage Telemetry](../../README.md) ·
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

