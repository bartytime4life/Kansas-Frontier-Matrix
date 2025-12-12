---
title: "🌱 Kansas Frontier Matrix — Soil Story Nodes (Domain Index) (KFM v11.2.6)"
path: "docs/story-nodes/domains/soil/README.md"

version: "v11.2.6"
last_updated: "2025-12-12"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Soil Systems Board · FAIR+CARE Council"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../releases/v11.2.6/storynodes-soil-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/storynodes-v11.json"
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
doc_kind: "Index"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

scope:
  domain: "story-nodes-soil"
  applies_to:
    - "docs/story-nodes/domains/soil/**"
    - "docs/story-nodes/domains/soil/templates/**"
    - "docs/story-nodes/domains/soil/examples/**"
    - ".github/workflows/storynodes-validate.yml"
    - ".github/workflows/docs-lint.yml"

fair_category: "F1-A1-I1-R2"
care_label: "Environmental · Agriculture"
sensitivity: "General (non-sensitive); individual nodes may require masking based on data source and governance"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "Soil Systems Board · KFM FAIR+CARE Council"

ttl_policy: "36 months"
sunset_policy: "Superseded by v12 soil story node standards"

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
  - "docs/story-nodes/domains/soil/README.md@v11.2.6"
provenance_requirements:
  versions_required: false
  newest_first: true
  must_reference_superseded: false
  must_reference_origin_root: false

json_schema_ref: "../../../../schemas/json/kfm-markdown-protocol-v11.2.6.schema.json"
shape_schema_ref: "../../../../schemas/shacl/kfm-markdown-protocol-v11.2.6-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:storynodes:soil:domain-index:v11.2.6"
semantic_document_id: "kfm-storynodes-soil-domain-index-v11.2.6"
event_source_id: "ledger:kfm:doc:storynodes:soil:domain-index:v11.2.6"

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
  - "narrative-fabrication"
  - "unverified-architectural-claims"
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
    - "narrative-fabrication"
    - "unverified-architectural-claims"
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
  - "sensitivity-check"

ci_integration:
  workflow: ".github/workflows/storynodes-validate.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence"
  soil: "Soil Systems · Evidence-Led · Public-Safe by Default"
  graph: "Semantics × Provenance × Stewardship"

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

# 🌱 **Kansas Frontier Matrix — Soil Story Nodes (Domain Index)**  
`docs/story-nodes/domains/soil/README.md`

**Purpose**  
Define the **soil domain contract** for KFM Story Nodes: scope, templates, vocabulary, validation expectations, and governance constraints.  
Soil Story Nodes are **public-safe by default**, but must support masking and sovereignty controls when datasets or contexts require it.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blue" />
<img src="https://img.shields.io/badge/Story_Nodes-Soil-success" />
<img src="https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen" />

</div>

---

## 📘 Overview

Soil Story Nodes are governed narrative + metadata objects that describe soil conditions, processes, and outcomes over time, such as:

- Soil health indicators (organic matter/carbon, aggregation, infiltration)
- Erosion risk and observed erosion impacts
- Salinity/sodicity signals and mitigation narratives
- Compaction and land-use driven soil change
- Soil moisture/temperature patterns (as environmental context)
- Nutrient and fertility context (high-level, non-sensitive, non-operational)
- Restoration practices and monitoring outcomes (when governance allows)

**What this domain provides**

- A **template set** for authoring soil nodes (`templates/`)
- A **controlled vocabulary** to keep tags and fields consistent (`templates/soil-vocabulary.md`)
- A **validation posture** that keeps soil nodes CI-safe, schema-valid, and governance-aligned

---

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 📁 story-nodes/
    ├── 📄 README.md                             # Global Story Nodes index (all domains)
    └── 📁 domains/
        └── 📁 soil/
            ├── 📄 README.md                     # ← Soil domain index (this file)
            ├── 📄 relation-patterns.md          # (recommended) Soil relation patterns (add when ready)
            ├── 📁 templates/
            │   ├── 📄 README.md                 # Template catalog + usage rules
            │   ├── 📄 story-node-soil.md         # Markdown authoring template (copy + fill)
            │   └── 📄 soil-vocabulary.md         # Controlled vocabulary for soil node fields/tags
            └── 📁 examples/
                └── 📄 README.md                 # (optional) Public-safe examples (add when ready)
~~~

---

## 🧭 Context

### 1. Domain boundaries (normative)

Soil Story Nodes SHOULD focus on:

- **soil properties and processes** (what changed, where, when, how we know)
- **evidence and provenance** (datasets, methods, uncertainty)
- **governed interpretation** (avoid operational prescriptions; keep narratives public-safe)

Soil Story Nodes SHOULD NOT:

- publish private farm/operator identifiers or field-level operational details
- embed sensitive coordinates for protected sites or culturally restricted places
- claim causal attribution beyond what the evidence and methods support

### 2. Typical data sources (examples, not exhaustive)

Soil nodes often reference:

- soil survey layers and derived classifications
- monitoring observations (field/lab) that are publishable
- remote sensing or model-derived soil moisture/temperature (as context)
- erosion modeling outputs (when inputs/assumptions are disclosed)
- management practice summaries (only when governance permits and non-identifying)

---

## 🧠 Story Node & Focus Mode Integration

Focus Mode uses soil Story Nodes to:

- summarize **soil conditions over time**
- link soil narratives to **STAC/DCAT assets** and **PROV activities**
- highlight **data-quality and uncertainty** without inventing numbers

Focus Mode MUST NOT:

- fabricate soil measurements, recommendations, or compliance claims
- “upgrade” precision (e.g., turning a regional story into a point location)
- infer private land management behavior from generalized data

---

## 🧪 Validation & CI/CD

Soil domain docs and derived Story Nodes are expected to pass:

- `docs-lint.yml` (KFM-MDP v11.2.6 structure, links, headings, footer)
- `storynodes-validate.yml` (Story Node schema validation for any JSON nodes)
- `sensitivity-check` (masking/precision rules when sovereignty or cultural sensitivity applies)

If you add new constraints (vocabulary terms, relation patterns), update:

- `templates/soil-vocabulary.md`
- `relation-patterns.md` (if present)
- the domain validator rules (if implemented)

---

## 📦 Data & Metadata

For all soil nodes:

- Use stable IDs (`doc_uuid`, `semantic_document_id`, story-node IDs)
- Record provenance:
  - dataset references (STAC/DCAT IDs or file paths)
  - method category (`observed`, `modeled`, `derived`, `interpreted`)
  - uncertainty notes (qualitative or quantitative)

Vocabulary for soil fields and tags is governed by:

- `templates/soil-vocabulary.md`

---

## ⚖ FAIR+CARE & Governance

Soil narratives are generally public-safe, but can become governance-sensitive when they intersect with:

- Indigenous rights and sovereignty contexts
- protected ecological zones or culturally sensitive landscapes
- private land management inference risk

When in doubt:

- reduce spatial precision
- avoid operational specificity
- prefer aggregated or administrative geometries
- reference governance policies rather than improvising new rules

---

## 🕰️ Version History

| Version   | Date       | Author        | Summary |
|----------:|------------|---------------|---------|
| v11.2.6   | 2025-12-12 | `@kfm-soil`   | Created soil domain index aligned to KFM-MDP v11.2.6; established template + vocabulary contract. |

---

<div align="center">

🌱 **Kansas Frontier Matrix — Soil Story Nodes (Domain Index) (v11.2.6)**  
Soil Systems · Governed Narratives · Public-Safe by Default

[📁 Templates](./templates/README.md) ·
[📘 Story Nodes Index](../../README.md) ·
[📚 Docs Home](../../../README.md) ·
[📏 Standards Index](../../../standards/README.md) ·
[⚖ Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[📚 Glossary](../../../glossary.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0 · MCP-DL v6.3 · KFM-MDP v11.2.6

</div>
