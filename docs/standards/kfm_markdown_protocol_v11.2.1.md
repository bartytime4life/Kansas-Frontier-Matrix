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

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![KFM-MDP v11.2.1](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.1-informational)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold)]()  
[![Accessibility WCAG 2.1 AA+](https://img.shields.io/badge/Accessibility-WCAG_2.1_AA%2B-blueviolet)]()  
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

Every governed Markdown file MUST follow the v11.2.1 structure:

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
- Headings must come from the **heading_registry**  
- Directory trees use **4-space indents**, NOT fenced blocks  
- No nested fences inside large fences  
- Emojis strongly recommended  

---

## 🗂️ 2. Directory Layout Standard (Indentation Mode)

Directory trees MUST follow this format:

- ASCII connector characters only  
- 4-space indentation  
- No fenced code blocks inside fenced contexts  

**Example (safe indentation mode):**

    docs/
        ├── standards/
        │   ├── kfm_markdown_protocol_v11.2.1.md
        │   └── governance/
        ├── architecture/
        ├── analyses/
        └── templates/

This is the ONLY approved directory layout format.

---

## 🗺️ 3. Diagram Specification (Mermaid + Diagram Profiles)

Mermaid diagrams are permitted, but MUST follow the v11.2.1 profile rules:

### Allowed diagram types:
- pipeline-flow  
- ci-flow  
- entity-relationship-slice  
- timeline  
- sequence  

### Requirements:
- MUST appear under `## 🗺️ Diagrams`  
- MUST include:
  - Diagram title  
  - Caption  
  - Summary paragraph (for accessibility)  
- MUST be referenced by a diagram profile in metadata  

### Accessibility:
- Every diagram MUST have a text equivalent  
- Screen-reader compatibility required  

---

## 🧠 4. Story Node & Focus Mode Integration

Documents MAY reference Story Nodes:

    story_node_refs:
      - "urn:kfm:story-node:example"

Rules:

- Avoid ambiguous pronouns  
- Use ISO-8601 dates  
- Use resolvable GNIS/KFM entities  
- Optionally provide Focus Summary blocks  

---

## 🧩 5. YAML Metadata Layer Model

v11.2.1 formalizes a **profile-based metadata system**:

### Metadata layers:
- Core Identity  
- Governance & Risk  
- Supply Chain & Telemetry  
- Ontology & Schema  
- Runtime & Stack  
- AI Governance  
- Integrity & Identity  
- Provenance Chain  
- Story Node Links  
- Header & Footer Profiles  
- Diagram Profiles  
- Branding Registry  

All keys are schema-validated via `json_schema_ref`.

---

## ♿ 6. Accessibility Requirements (WCAG 2.1 AA+)

All documents MUST:

- Provide alt-text  
- Provide diagram text equivalents  
- Maintain logical heading order  
- Use descriptive links  
- Avoid color-only indicators  
- Define jargon or link to glossary  

The **accessibility-check** test profile enforces this.

---

## 🔐 7. AI Governance & Transform Registry

The v11.2.1 Transform Registry defines ALL allowed and prohibited transforms.

### Allowed:
- summary  
- timeline-generation  
- semantic-highlighting  
- 3d-context-render  
- a11y-adaptations  
- diagram-extraction  
- metadata-extraction  

### Prohibited:
- content-alteration  
- speculative-additions  
- unverified-architectural-claims  
- narrative-fabrication  
- governance-override  

Focus Mode MUST enforce the registry.

---

## 🧪 8. Validation & CI/CD Requirements

Each governed doc must pass:

- markdown-lint  
- schema-lint  
- footer-check  
- accessibility-check  
- diagram-check  
- metadata-check  
- provenance-check  

A failure blocks merge.

---

## 🕰️ Version History

| Version | Date       | Summary                                                                                              |
|--------:|------------|------------------------------------------------------------------------------------------------------|
| v11.2.1 | 2025-11-26 | Added header/footer/diagram profiles, transform registry, heading registry, provenance hardening.    |
| v11.2.0 | 2025-11-25 | Major structural overhaul, adaptive footers, metadata layers, diagram rules, accessibility.          |
| v11.0.1 | 2025-11-20 | Previous major version.                                                                               |

---

<div align="center">

**Kansas Frontier Matrix**  
*Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence*  

[⬅ Back to Standards Index](../README.md) ·  
[📜 Governance Charter](../governance/ROOT-GOVERNANCE.md) ·  
[🛰 Telemetry Overview](../../telemetry/README.md)

</div>
