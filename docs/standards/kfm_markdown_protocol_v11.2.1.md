---
title: "📑 Kansas Frontier Matrix — Markdown Authoring Protocol (KFM-MDP) v11.2.1"
path: "docs/standards/kfm_markdown_protocol_v11.2.1.md"
version: "v11.2.1"
last_updated: "2025-11-26"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · FAIR+CARE Council & Focus Mode Board"
commit_sha: "<latest-commit-hash>"
signature_ref: "releases/v11.2.1/signature.sig"
attestation_ref: "releases/v11.2.1/slsa-attestation.json"
sbom_ref: "releases/v11.2.1/sbom.spdx.json"
manifest_ref: "releases/v11.2.1/manifest.zip"
telemetry_ref: "releases/v11.2.1/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/markdown-protocol-v11.2.1.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-v2.json"
governance_ref: "../governance/ROOT-GOVERNANCE.md"
ethics_ref: "../faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.1"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
status: "Active / Enforced"
doc_kind: "Standard"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"
scope:
  domain: "documentation"
  applies_to:
    - "all-markdown"
category: "Documentation · Protocol · Standards"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
ttl_policy: "24 months"
sunset_policy: "Supersedes KFM-MDP v11.2.0"
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
  - "docs/standards/kfm_markdown_protocol_v11.2.md@v11.2.0"
  - "docs/standards/kfm_markdown_protocol_v11.md@v11.0.1"
  - "docs/standards/markdown_rules.md@v10.4.3"
  - "docs/standards/markdown_rules.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
json_schema_ref: "schemas/json/kfm-markdown-protocol-v11.2.1.schema.json"
shape_schema_ref: "schemas/shacl/kfm-markdown-protocol-v11.2.1-shape.ttl"
story_node_refs: []
immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:standards:markdown-protocol:v11.2.1"
semantic_document_id: "kfm-markdown-protocol-v11.2.1"
event_source_id: "ledger:kfm-markdown-protocol-v11.2.1"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "3d-context-render"
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
    - summary
    - timeline-generation
    - semantic-highlighting
    - 3d-context-render
    - a11y-adaptations
    - diagram-extraction
    - metadata-extraction
  prohibited:
    - content-alteration
    - speculative-additions
    - unverified-architectural-claims
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
    - "🧱 Architecture"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"
test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "footer-check"
  - "accessibility-check"
  - "diagram-check"
  - "metadata-check"
  - "provenance-check"
ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"
branding_registry:
  standard: "Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence"
  architecture: "Designed for Longevity · Governed for Integrity"
  analysis: "Research-Driven · Evidence-Led · FAIR+CARE Grounded"
  data-spec: "Open Data × Responsible Stewardship"
  pipeline: "Deterministic Pipelines · Explainable AI · Open Provenance"
  telemetry: "Transparent Systems · Ethical Metrics · Sustainable Intelligence"
  graph: "Semantics × Provenance × Spatial Intelligence"
---

<div align="center">

# 📑 **Kansas Frontier Matrix — Markdown Authoring Protocol v11.2.1**  
`docs/standards/kfm_markdown_protocol_v11.2.1.md`

**Purpose:**  
Define the canonical, enforceable Markdown standard for the Kansas Frontier Matrix (KFM) v11.2.1, governing structure, metadata, diagrams, accessibility, AI governance, provenance, and CI/CD compliance across the entire monorepo.  
This update adds profile systems (header, footer, diagram), heading registry, transform registry, provenance hardening, and directory-tree indentation rules.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]() ·
[![KFM-MDP v11.2.1](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.1-informational)]() ·
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold)]() ·
[![WCAG AA+](https://img.shields.io/badge/Accessibility-WCAG_2.1_AA%2B-blueviolet)]() ·
[![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen)]()

</div>

---

## 📘 Overview

KFM-MDP v11.2.1 is the **refinement release** of the v11.2 protocol.  
It establishes:

- A **profile-based system** for headers, footers, and diagrams  
- A **registry for approved headings**, ensuring documentation uniformity  
- A **transform vocabulary registry**, defining all allowed/disallowed AI transforms  
- A **document scope model**, enabling semantic filtering  
- Hardened provenance rules (ordered chain, superseded refs, root lineage)  
- A **directory-tree indentation standard** preventing nested-fence breakage  
- Additional CI test profiles for diagram quality, footer correctness, and metadata validation  

All governed Markdown in KFM MUST comply.

---

## 🧱 1. Required Document Structure

Every governed Markdown file MUST follow this structure:

1. YAML metadata  
2. Centered header block  
3. Horizontal rule  
4. `## 📘 Overview`  
5. `## 🗂️ Directory Layout` or `## 🧭 Context`  
6. Main content sections using **approved headings**  
7. `## 🗺️ Diagrams` (if diagrams appear)  
8. `## 🧠 Story Node & Focus Mode Integration`  
9. `## 🧪 Validation & CI/CD`  
10. `## 🕰️ Version History`  
11. Footer (profile-based)  

### Additional structural constraints:

- Exactly **one H1** inside the header block  
- Only **H1–H4**; no H5/H6  
- Headings SHOULD come from the **heading_registry** for standards  
- Directory trees use **4-space indents**, not fenced blocks inside fenced contexts  
- Emojis strongly encouraged  
- No bare URLs  
- No nested fences inside top-level fences in ChatGPT-generated content  

---

## 🗂️ 2. Directory Layout Standard (Indentation Mode)

Directory trees MUST follow this format:

- ASCII connector characters (│, ├──, └──)  
- 4-space indentation  
- No fenced blocks inside the main fence in templates  

Example (safe indentation mode):

    docs/
        ├── standards/
        │   ├── kfm_markdown_protocol_v11.2.1.md
        │   └── governance/
        ├── architecture/
        ├── analyses/
        └── templates/

This is the ONLY approved directory layout format for KFM documentation.

---

## 🗺️ 3. Diagram Specification (Mermaid + Diagram Profiles)

Mermaid diagrams are encouraged, but they MUST follow v11.2.1 diagram profiles.

### Allowed diagram semantic types:

- pipeline-flow  
- ci-flow  
- entity-relationship-slice  
- timeline  
- sequence  

Each diagram MUST:

- Appear under `## 🗺️ Diagrams`  
- Include:
  - Title (as text near the diagram)  
  - Caption  
  - Summary paragraph for accessibility  
- Be logically tied to a `diagram_profiles` entry in YAML  

Accessibility:

- Every diagram MUST have a text description  
- Diagrams MUST NOT be the only source of normative rules  

---

## 🧠 4. Story Node & Focus Mode Integration

Documents MAY reference story nodes:

    story_node_refs:
      - "urn:kfm:story-node:example"

Rules:

- Avoid ambiguous pronouns in normative sections  
- Use ISO-8601 for dates  
- Refer to entities using graph-resolvable IDs or names  
- Optionally provide Focus Summary blocks for Focus Mode:

> **Focus Summary:** This protocol defines how all KFM Markdown documents are authored, structured, and validated in v11.2.1, including AI governance, provenance, and accessibility rules.

Focus Mode v3 uses this information for guided exploration.

---

## 🧩 5. YAML Metadata Layer Model

v11.2.1 uses a layered and profile-based metadata model:

- **Header profiles** (`header_profile`) for identity & layout  
- **Footer profiles** (`footer_profile`) for navigation & branding  
- **Diagram profiles** (`diagram_profiles`) for diagram semantics  
- **Transform registry** (`transform_registry`) for AI behavior  
- **Heading registry** (`heading_registry`) for heading conformity  
- **Test profiles** (`test_profiles`) for validation requirements  

All metadata MUST comply with `json_schema_ref`/`shape_schema_ref`.

---

## ♿ 6. Accessibility Requirements (WCAG 2.1 AA+)

All documents MUST:

- Provide alt-text on images  
- Provide text equivalents for diagrams  
- Use descriptive link text  
- Maintain logical heading hierarchy  
- Avoid color-only indications  
- Define jargon or link to a glossary  

The `accessibility-check` test profile enforces these rules.

---

## 🔐 7. AI Governance & Transform Registry

The AI governance block and `transform_registry` define:

- Which transforms are allowed  
- Which transforms are prohibited  
- How Focus Mode and other AI tools may interact with the document  

Allowed transforms (examples):

- summary  
- timeline-generation  
- semantic-highlighting  
- 3d-context-render  
- a11y-adaptations  
- diagram-extraction  
- metadata-extraction  

Prohibited transforms (examples):

- content-alteration  
- speculative-additions  
- unverified-architectural-claims  
- narrative-fabrication  
- governance-override  

Focus Mode MUST obey this registry.

---

## 🧪 8. Validation & CI/CD Requirements

Each governed Markdown document MUST pass the `test_profiles` declared in this spec:

- markdown-lint  
- schema-lint  
- footer-check  
- accessibility-check  
- diagram-check  
- metadata-check  
- provenance-check  

A failing profile blocks merge to main. This ensures:

- Structural correctness  
- Schema alignment  
- Footer and navigation integrity  
- Accessibility  
- Diagram semantics and text pairing  
- Metadata completeness  
- Provenance correctness  

---

## 🕰️ Version History

| Version | Date       | Summary                                                                                              |
|--------:|------------|------------------------------------------------------------------------------------------------------|
| v11.2.1 | 2025-11-26 | Added header/footer/diagram profiles, transform registry, heading registry, provenance hardening.    |
| v11.2.0 | 2025-11-25 | Major structural overhaul, adaptive footers, metadata layers, diagram rules, accessibility.          |
| v11.0.1 | 2025-11-20 | Previous major Markdown protocol version.                                                            |

---

<div align="center">

**Kansas Frontier Matrix**  
*Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence*  

[⬅ Back to Standards Index](../README.md) ·  
[📜 Governance Charter](../governance/ROOT-GOVERNANCE.md) ·  
[🛰 Telemetry Overview](../../telemetry/README.md)

</div>
