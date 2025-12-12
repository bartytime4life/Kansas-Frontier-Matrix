---
title: "🌱 Kansas Frontier Matrix — Soil Story Node Templates (KFM v11.2.6)"
path: "docs/story-nodes/domains/soil/templates/README.md"

version: "v11.2.6"
last_updated: "2025-12-12"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Soil Systems Board · FAIR+CARE Council"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
signature_ref: "../../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../../releases/v11.2.6/storynodes-soil-templates-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/storynodes-v11.json"
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
doc_kind: "Template Directory README"
intent: "kfm-soil-storynode-templates"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

scope:
  domain: "storynodes-soil-templates"
  applies_to:
    - "docs/story-nodes/domains/soil/templates/**"
    - "docs/story-nodes/domains/soil/relation-patterns.md"
    - "docs/story-nodes/domains/soil/examples/**"
    - "schemas/storynodes/**"
    - ".github/workflows/storynodes-validate.yml"
    - ".github/workflows/docs-lint.yml"

fair_category: "F1-A2-I2-R2"
care_label: "Environmental · Stewardship-Aligned"
sensitivity: "General (public-safe; no PII; no landowner identifiers; sovereignty masking rules apply)"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "Soil Systems Board · KFM FAIR+CARE Council"

ttl_policy: "36 months"
sunset_policy: "Superseded by v12 soil templates"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "KFM Story Node v11"
  - "STAC 1.0.0 (references)"
  - "DCAT 3.0 (references)"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/story-nodes/domains/soil/templates/README.md@v11.2.6"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: false
  must_reference_origin_root: true

json_schema_ref: "../../../../../schemas/json/kfm-markdown-protocol-v11.2.6.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/kfm-markdown-protocol-v11.2.6-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:storynodes:soil:templates:v11.2.6"
semantic_document_id: "kfm-storynodes-soil-templates-v11.2.6"
event_source_id: "ledger:storynodes/soil/templates:v11.2.6"
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
  - "layout-normalization"
ai_transform_prohibited:
  - "content-alteration"
  - "inventing-compliance-status"
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
    - "layout-normalization"
  prohibited:
    - "content-alteration"
    - "inventing-compliance-status"
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
  - "storynodes-schema-check"
  - "sensitivity-check"

ci_integration:
  workflow: ".github/workflows/storynodes-validate.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence"
  soil: "Soil Systems · Stewardship · Evidence-Led"
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

# 🌱 **Soil Story Node Templates (KFM v11.2.6)**  
`docs/story-nodes/domains/soil/templates/README.md`

**Purpose**  
Provide the **canonical authoring templates**, **JSON skeletons**, and **soil-domain prompting patterns**  
for building soil Story Nodes that are **schema-valid**, **public-safe**, **provenance-ready**, and **Focus Mode v3 compatible**.

<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Story_Nodes-Templates-success" />
<img src="https://img.shields.io/badge/Domain-Soil-informational" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

</div>

---

## 📘 Overview

This directory contains the **official Soil domain template set** used to author Soil Story Nodes.

Soil Story Nodes typically represent:

- soil properties and gradients (texture, pH, SOC, salinity, bulk density, AWC)  
- soil health and land stewardship signals (erosion risk, infiltration, compaction)  
- classification and mapping context (taxonomy, map units, horizons, uncertainty)  
- temporal change narratives (management impacts, drought legacy, restoration timelines)  
- data-to-narrative explainers (why a map shows what it shows; what uncertainty means)

These templates are designed so that:

- **Humans** can author clear, structured, public-safe narratives.  
- **Validators** can enforce schema + domain rules deterministically.  
- **Catalogs/graph** can ingest Story Nodes as first-class, provenance-aware assets.  
- **Focus Mode** can summarize and navigate without inventing facts or policy.

---

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 📁 story-nodes/
    ├── 📄 README.md
    └── 📁 domains/
        └── 📁 soil/
            ├── 📄 README.md
            ├── 📄 relation-patterns.md
            ├── 📁 templates/
            │   ├── 📄 README.md
            │   ├── 📄 story-node-soil.md
            │   ├── 🧾 story-node-soil.json
            │   └── 📄 soil-vocabulary.md
            └── 📁 examples/
                ├── 📄 README.md
                └── 🧾 <public-safe-example>.json
~~~

**Template catalog (this directory)**

- `story-node-soil.md` — Markdown authoring template (human-first)  
- `story-node-soil.json` — schema-aligned JSON skeleton (machine-first)  
- `soil-vocabulary.md` — recommended controlled terms, units, and soil-specific field guidance

---

## 🧭 Context

Soil Story Nodes sit at the intersection of:

- **Environmental layers** (soil, landcover, hydrology, climate, terrain)  
- **STAC/DCAT** catalog assets (rasters, vectors, tables, derived products)  
- **PROV-O** lineage (pipelines, transforms, model inference, validation steps)  
- **Focus Mode v3** narrative overlays (summaries, compare views, timelines)

Soil templates are intentionally conservative about claims:

- clearly separate **observations**, **derived products**, and **interpretation**  
- include explicit **uncertainty** and **data coverage** prompts  
- avoid overconfident attribution (especially for management or climate drivers)

---

## 🗺️ Diagrams

High-level authoring flow for Soil Story Nodes (templates → validation → publish):

~~~mermaid
flowchart LR
  A["Author uses soil templates"] --> B["Validate Story Node schema"]
  B --> C["Apply soil domain rules"]
  C --> D["Docs lint and metadata checks"]
  D --> E["Catalog + graph ingest"]
  E --> F["Focus Mode + Story Nodes UI"]
~~~

---

## 🧠 Story Node & Focus Mode Integration

These templates are “Focus Mode safe” by design:

- stable sections enable predictable summaries  
- IDs and provenance fields enable deep linking and lineage views  
- permissions constrain what AI/agents may do

**Focus Mode MAY:**

- summarize the node and highlight key soil properties  
- generate a timeline from `spacetime.when`  
- extract dataset references (STAC/DCAT) and provenance activities (PROV)

**Focus Mode MUST NOT:**

- fabricate field measurements, management actions, or causal claims  
- invent compliance status (“certified”, “audited”, “approved”)  
- override governance / sovereignty labels

---

## 🧪 Validation & CI/CD

Expected validation checks for template updates and downstream nodes:

- `docs-lint.yml`  
  - verifies this README’s front-matter, headings, footer links, diagram fencing  
- `storynodes-validate.yml`  
  - validates JSON nodes against Story Node v11 schema  
  - enforces soil domain constraints (required fields, allowed relations, masking rules)  
- `schema-lint` / `metadata-check`  
  - ensures required metadata keys exist and are correctly typed  
- `sensitivity-check`  
  - blocks PII, landowner identifiers, and restricted location detail where policy applies

Template changes are treated as contract updates and SHOULD be reviewed by the Soil Systems Board.

---

## 📦 Data & Metadata

### Recommended soil context fields (guidance)

Soil Story Nodes should capture three layers of meaning:

1. **What is being described (phenomenon)**  
   - property names, units, depth/horizon context, scale/resolution

2. **How it was produced (method)**  
   - observation, survey, lab, interpolation, model, fusion, derived index  
   - uncertainty and coverage notes

3. **How it links (references and relations)**  
   - dataset IDs, pipeline IDs, and prov activities

### Minimal JSON skeleton (schematic)

Adapt the keys to your Story Node v11 schema implementation (this is intentionally conservative):

~~~json
{
  "schema_version": "v11",
  "type": "story-node",
  "domain": "soil",
  "id": "urn:kfm:story-node:soil:<slug>",
  "title": "Soil narrative title",
  "summary": "Public-safe summary of what this soil node explains.",
  "classification": "Public",
  "spacetime": {
    "when": { "start": "2025-01-01", "end": "2025-12-31", "precision": "day" },
    "geometry": null,
    "geometry_precision": "generalized"
  },
  "soil": {
    "properties": [
      { "name": "soil_organic_carbon", "unit": "g/kg", "depth_cm": [0, 30] },
      { "name": "ph", "unit": "pH", "depth_cm": [0, 30] }
    ],
    "method": { "kind": "derived", "notes": "Describe survey/model/source and uncertainty." }
  },
  "links": {
    "stac": [],
    "dcat": [],
    "docs": [],
    "telemetry": []
  },
  "relations": [],
  "provenance": []
}
~~~

### Soil vocabulary + units

Use controlled terms and units wherever possible (see `soil-vocabulary.md`) to keep ingestion deterministic:

- property names: prefer consistent, machine-friendly identifiers  
- units: explicit (avoid implicit “percent” or “ppm” without a declared unit)  
- depth: always declare depth/horizon meaning (topsoil vs subsoil)  
- uncertainty: describe method limitations, not just confidence language

---

## 🌐 STAC, DCAT & PROV Alignment

Soil Story Nodes often reference raster and vector products that are best modeled as STAC assets:

- STAC Items/Collections for:
  - gridded soil properties  
  - map unit polygons  
  - derived indices (erosion risk, salinity risk)  
- DCAT for:
  - catalog records and distributions (public release posture)  
- PROV-O for:
  - workflows that produced the layer  
  - inputs (source datasets) and agents (pipelines, boards, services)

The Story Node remains the **narrative + semantic layer** that binds these assets together.

---

## 🧱 Architecture

This template set supports three complementary authoring modes:

1. **Markdown-first authoring** (`story-node-soil.md`)  
   - best for narrative writing and review  
   - can be transformed into JSON by tooling (where supported)

2. **JSON-first authoring** (`story-node-soil.json`)  
   - best for programmatic generation and strict schema compliance

3. **Vocabulary guidance** (`soil-vocabulary.md`)  
   - reduces drift and improves interoperability across nodes and datasets

---

## ⚖ FAIR+CARE & Governance

Soil narratives must remain stewardship-aligned:

- no PII or landowner-specific detail  
- avoid claims that exceed the evidence in linked datasets  
- when Indigenous rights may be implicated:
  - follow the sovereignty policy
  - reduce precision and prefer generalized extents
  - reference governance docs instead of embedding sensitive policy judgments

Any governance waivers or exceptions must be recorded in the appropriate governance ledger artifacts, not embedded as narrative claims inside Story Nodes.

---

## 🕰️ Version History

| Version   | Date       | Author       | Summary                                                                 |
|----------:|------------|--------------|-------------------------------------------------------------------------|
| v11.2.6   | 2025-12-12 | `@kfm-soil`  | Initial Soil template directory README aligned to KFM-MDP v11.2.6; added template catalog, validation flow, and STAC/DCAT/PROV guidance. |

---

<div align="center">

🌱 **Soil Story Node Templates (v11.2.6)**  
Schema-Valid · Public-Safe · Stewardship-Aligned · Focus Mode Ready

[⬅ Soil Domain Index](../README.md) ·
[📁 Soil Examples](../examples/README.md) ·
[🧠 Story Nodes Home](../../../README.md) ·
[📘 Docs Home](../../../../README.md) ·
[📏 Standards Index](../../../../standards/README.md) ·
[📑 Markdown Protocol](../../../../standards/kfm_markdown_protocol_v11.2.6.md) ·
[⚖ Governance Charter](../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[📚 Glossary](../../../../glossary.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6

</div>
