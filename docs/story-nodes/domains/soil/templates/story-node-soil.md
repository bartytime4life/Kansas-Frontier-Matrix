---
title: "🌱 KFM — Soil Story Node Markdown Template (KFM-MDP v11.2.6)"
path: "docs/story-nodes/domains/soil/templates/story-node-soil.md"

version: "v11.2.6"
last_updated: "2025-12-12"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Soil Domain Board · FAIR+CARE Council"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

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
doc_kind: "Template"
intent: "kfm-soil-storynode-markdown-template"
category: "Story Nodes · Templates · Soil"

scope:
  domain: "storynodes-soil"
  applies_to:
    - "docs/story-nodes/domains/soil/**"

fair_category: "F1-A1-I1-R2"
care_label: "Environmental · Land Stewardship"
sensitivity: "General (template only; authored nodes may be higher sensitivity)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "Soil Domain Board · KFM FAIR+CARE Council"

ttl_policy: "36 months"
sunset_policy: "Superseded by v12 soil template"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "KFM Story Node v11"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/story-nodes/domains/soil/templates/story-node-soil.md@v11.2.6"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: false
  must_reference_origin_root: true

json_schema_ref: "../../../../../schemas/json/kfm-markdown-protocol-v11.2.6.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/kfm-markdown-protocol-v11.2.6-shape.ttl"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "narrative-fabrication"
  - "governance-override"

transform_registry:
  allowed:
    - summary
    - timeline-generation
    - semantic-highlighting
    - a11y-adaptations
    - metadata-extraction
  prohibited:
    - content-alteration
    - speculative-additions
    - narrative-fabrication
    - governance-override

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
  - "provenance-check"
  - "footer-check"
  - "accessibility-check"
  - "secret-scan"
  - "pii-scan"

ci_integration:
  workflow: ".github/workflows/docs-lint.yml"
  environment: "dev → staging → production"

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

# 🌱 **Soil Story Node — Markdown Authoring Template (v11.2.6)**  
`docs/story-nodes/domains/soil/templates/story-node-soil.md`

**Purpose**  
Copy this file to author a **soil Story Node narrative** with consistent structure, safe location posture, explicit uncertainty, and clean links to datasets/provenance for Focus Mode and graph ingestion.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Story_Nodes-Soil_Template-success" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Governed-gold" />

</div>

---

## 📘 Overview

### Template instructions (replace placeholders)

- Replace all `<...>` placeholders.
- Keep a strict separation between:
  - **Observation** (what the data says)
  - **Interpretation** (what it may imply)
  - **Limitations** (what it cannot support)
- If your narrative could cause harm at parcel-scale, **generalize geometry** and raise classification/sensitivity.

### Story Node identity (suggested fields)

Fill or mirror these identifiers in your JSON Story Node (if you maintain both forms):

- `story_node_id`: `urn:kfm:story-node:soil:<slug>:<version>`
- `semantic_document_id`: `kfm-storynode-soil-<slug>-<version>`
- `event_source_id`: `ledger:storynodes/soil/<slug>`

---

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 🧠 story-nodes/
    └── 📁 domains/
        └── 🌱 soil/
            ├── 📄 README.md                        — Soil domain index (rules + governance)
            └── 📁 templates/
                ├── 📄 README.md                    — Templates index
                └── 📄 story-node-soil.md           — ← This template (copy forward)
~~~

---

## 🧭 Context

### What this soil Story Node is about

**Title (fill in):** `<Soil Story Node Title>`

**One-sentence summary (fill in):**  
`<What soil system, property, or derived signal is being described, and why it matters>`

### Geographic and temporal posture (fill in)

- **Where (generalization):**
  - Region: `<Kansas region / county group / watershed / ecoregion>`
  - Geometry posture: `<null | generalized polygon | admin boundary mask>`
  - Precision statement: `<what precision is allowed and why>`

- **When (time modeling):**
  - If the node is effectively static: `<state "no meaningful temporal variation; use survey period or last-updated">`
  - If time varies (management period, drought years, erosion episode): `<start/end and why that interval is chosen>`

### Claims discipline (normative)

- Do not imply causality unless your linked sources support it.
- Do not collapse model outputs into “observed truth.”
- Explicitly state scale mismatch (e.g., map unit vs point observation).

---

## 🗺️ Diagrams

Optional conceptual flow (keep labels simple; no HTML):

~~~mermaid
flowchart LR
  A["Soil inputs"] --> B["Derived indicators"]
  B --> C["Narrative (observation vs interpretation)"]
  C --> D["Validated Story Node"]
  D --> E["Focus Mode summary and graph links"]
~~~

---

## 🧠 Story Node & Focus Mode Integration

### Focus Mode expectations (author notes)

Focus Mode will typically:

- extract your overview and key findings as a “card”
- surface dataset references (STAC/DCAT) as supporting evidence
- show uncertainty/limitations if clearly stated

To help that:

- use short paragraphs
- keep lists for key properties
- provide stable IDs and clear provenance references

---

## 🧪 Validation & CI/CD

### Expected checks

Your derived soil Story Node narrative SHOULD pass:

- Markdown protocol checks (front-matter, approved H2s, footer links)
- Diagram checks (if Mermaid is present)
- Secret/PII scans (no tokens, no personal identifiers)

If a JSON Story Node exists alongside this narrative:

- it MUST validate against the Story Node schema
- it MUST satisfy domain masking/classification constraints

### What must fail (normative)

CI should fail if the authored node includes:

- precise coordinates when the posture requires generalization
- parcel identifiers, landowner names, or other PII
- restricted Indigenous cultural knowledge or disallowed location hints

---

## 📦 Data & Metadata

### Soil properties (fill in what you actually have)

**Observed / mapped properties (examples — choose only what applies):**

- Map unit / soil class: `<...>`
- Drainage class: `<...>`
- Texture class: `<...>`
- Restrictive layer depth: `<...>`
- Available water capacity proxy: `<...>`
- Erosion susceptibility proxy: `<...>`
- Salinity/sodicity indicators (if applicable): `<...>`

### Derived indicators (if used)

List derived values with explicit provenance:

- Indicator name: `<...>`
- Computation method: `<brief method>`
- Inputs used: `<datasets + version>`
- Limitations: `<...>`

### Uncertainty & limitations (required)

- Spatial scale limitation: `<...>`
- Temporal limitation: `<...>`
- Measurement/model limitation: `<...>`
- Interpretive risk: `<what could be misread and how you prevent that>`

---

## 🌐 STAC, DCAT & PROV Alignment

### Dataset references (fill in)

- STAC Collection/Item IDs: `<...>`
- DCAT Dataset identifiers: `<...>`
- PROV activity/entity references:
  - `prov:used`: `<input datasets / configs>`
  - `prov:wasGeneratedBy`: `<pipeline run or workflow>`
  - `prov:wasAssociatedWith`: `<agent/team/bot>`

### Evidence linking (recommended)

Include a short “Evidence” list:

- Evidence 1: `<dataset / report / artifact>` — `<what it supports>`
- Evidence 2: `<dataset / report / artifact>` — `<what it supports>`

---

## 🧱 Architecture

### Narrative structure (recommended prompts)

Use the following prompts to build a clean soil Story Node narrative:

1. **What is being described?**  
   `<soil system / property / indicator>`

2. **What is directly observed or mapped?**  
   `<observations>`

3. **What is interpreted and why?**  
   `<interpretation + rationale + citations to datasets>`

4. **What is the spatial extent and why is it safe?**  
   `<generalization + masking statement>`

5. **What are the limitations?**  
   `<uncertainty + scale mismatch + data gaps>`

6. **What else is it connected to?**  
   - Hydrology: `<link or related node>`
   - Climate: `<link or related node>`
   - Landcover/ecology: `<link or related node>`
   - Agriculture: `<link or related node (generalized)>`

---

## ⚖ FAIR+CARE & Governance

### Classification and masking (required)

- `classification`: `<Public | Generalized / Public-Safe | Restricted>`
- `sensitivity_level`: `<None | Low | Medium | High>`
- `indigenous_rights_flag`: `<true/false with justification>`

### Stewardship notes (required)

- Potential harms if misunderstood: `<...>`
- Mitigations (generalization, disclaimers, scope): `<...>`
- Governance references:
  - Root Governance Charter
  - FAIR+CARE Guide
  - Indigenous Data Protection Policy

---

## 🕰️ Version History

| Version | Date       | Author        | Summary                                                   |
|--------:|------------|---------------|-----------------------------------------------------------|
| v11.2.6 | 2025-12-12 | `@kfm-soil`   | Initial soil Story Node Markdown template (governed).     |

---

<div align="center">

🌱 **Soil Story Node — Markdown Authoring Template (v11.2.6)**  
Structured Narrative · Evidence-Led · Public-Safe by Default

[⬅ Soil Templates Index](./README.md) ·
[⬅ Soil Domain Index](../README.md) ·
[🧠 Story Nodes Index](../../../README.md) ·
[📑 Markdown Protocol](../../../../standards/kfm_markdown_protocol_v11.2.6.md) ·
[🏛️ Governance Charter](../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0 · MCP-DL v6.3 · KFM-MDP v11.2.6

</div>
