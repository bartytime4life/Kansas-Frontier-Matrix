---
title: "📑 Kansas Frontier Matrix — Markdown Authoring Protocol (KFM-MDP) v11.2.2"
path: "docs/standards/kfm_markdown_protocol_v11.2.2.md"
version: "v11.2.2"
last_updated: "2025-11-27"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · FAIR+CARE Council & Focus Mode Board"
content_stability: "stable"
commit_sha: "<latest-commit-hash>"
signature_ref: "releases/v11.2.2/signature.sig"
attestation_ref: "releases/v11.2.2/slsa-attestation.json"
sbom_ref: "releases/v11.2.2/sbom.spdx.json"
manifest_ref: "releases/v11.2.2/manifest.zip"
telemetry_ref: "releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/markdown-protocol-v11.2.2.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-v2.json"
governance_ref: "../governance/ROOT-GOVERNANCE.md"
ethics_ref: "../faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
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
semantic_intent:
  - "governance"
  - "authoring"
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
sunset_policy: "Supersedes KFM-MDP v11.2.1"
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
  - "docs/standards/kfm_markdown_protocol_v11.2.1.md@v11.2.1"
  - "docs/standards/kfm_markdown_protocol_v11.2.md@v11.2.0"
  - "docs/standards/kfm_markdown_protocol_v11.md@v11.0.1"
  - "docs/standards/markdown_rules.md@v10.4.3"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
json_schema_ref: "schemas/json/kfm-markdown-protocol-v11.2.2.schema.json"
shape_schema_ref: "schemas/shacl/kfm-markdown-protocol-v11.2.2-shape.ttl"
story_node_refs: []
immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:standards:markdown-protocol:v11.2.2"
semantic_document_id: "kfm-markdown-protocol-v11.2.2"
event_source_id: "ledger:kfm-markdown-protocol-v11.2.2"
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
deprecated_fields:
  - "old_markdown_standard_v10.4"
---

<div align="center">

# 📑 **Kansas Frontier Matrix — Markdown Authoring Protocol v11.2.2**  
`docs/standards/kfm_markdown_protocol_v11.2.2.md`

**Purpose:**  
Establish the canonical, enforceable Markdown authoring rules for Kansas Frontier Matrix (KFM) v11.2.2.  
This version adds profile systems, heading registries, semantic intent, transform registries, provenance hardening, stability tiers, anti-pattern rules, crosslinking guidance, macro conventions, and example appendices.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]() ·
[![KFM-MDP v11.2.2](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.2-informational)]() ·
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold)]() ·
[![WCAG AA+](https://img.shields.io/badge/Accessibility-WCAG_2.1_AA%2B-blueviolet)]() ·
[![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen)]()

</div>

---

## 📘 Overview

[normative]

This protocol defines the unified Markdown rules for KFM documentation, ensuring:

- structural consistency  
- stable rendering  
- machine extractability  
- FAIR+CARE alignment  
- accessibility  
- AI and Focus Mode governance  
- provenance integrity  
- diagram semantics  
- crosslink reliability  

[informative]

This version expands upon v11.2.1 by adding semantic layers, profile systems, anti-pattern rules, macro guidelines, and example appendices.

---

## 🧱 1. Required Document Structure

[normative]

All governed Markdown files MUST contain:

1. YAML metadata  
2. Centered header block  
3. Horizontal rule  
4. `📘 Overview`  
5. Directory or context section  
6. Main content sections using approved headings  
7. Diagrams section (if diagrams present)  
8. Story Node & Focus Mode Integration  
9. Validation & CI/CD  
10. Version History  
11. Footer (profile-based)  

### Additional Requirements  
- One H1 only  
- Use H1–H4 only  
- Heading registry enforced  
- No nested fences  
- Use indentation mode for directory trees  

---

## 🗂️ 2. Directory Layout Standard

[normative]

Directory trees MUST use the indentation-only, ASCII connector format:

    docs/
        ├── standards/
        │   ├── kfm_markdown_protocol_v11.2.2.md
        │   └── governance/
        ├── architecture/
        ├── analyses/
        └── templates/

---

## 🧭 3. Document Kind Matrix

[normative]

This matrix defines required metadata layers per `doc_kind`:

    Kind            Core  Gov  Telemetry  Ontology  AI Gov  Provenance  HeaderProf  FooterProf
    ------------------------------------------------------------------------------------------
    Standard        ✔     ✔      ✔         ✔        ✔         ✔          standard    standard
    Architecture    ✔     ✔      ✔         ✔        ✔         ✔        architecture architecture
    Analysis        ✔     ◑      ◑         ◑        ✔         ✔          analysis   analysis
    Data-Spec       ✔     ✔      ✔         ✔        ✔         ✔         data-spec   data-spec
    Pipeline        ✔     ✔      ✔         ◑        ✔         ✔          pipeline   pipeline
    Telemetry       ✔     ✔      ✔         ◑        ✔         ✔         telemetry   telemetry
    Graph/Ontology  ✔     ✔      ✔         ✔        ✔         ✔            graph      graph

✔ Required  
◑ Recommended  

---

## 🧠 4. Story Node & Focus Mode Integration

[normative]

Documents SHOULD include Story Node references where semantically relevant:

    story_node_refs:
      - "urn:kfm:story-node:example"

Focus Mode uses these for semantic linking.

---

## 🗺️ 5. Diagram Specification

[normative]

Allowed Diagram Types:

    pipeline-flow  
    ci-flow  
    entity-relationship-slice  
    timeline  
    sequence  

Every diagram MUST include:

- Title  
- Caption  
- Summary paragraph  
- Profile reference in YAML  

---

## 📦 6. Data & Metadata Rules

[normative]

Metadata MUST comply with:

- STAC 1.0  
- DCAT 3.0  
- FAIR+CARE  
- PROV-O  

Ontology alignment MUST be declared where relevant.

---

## ⚖ FAIR+CARE & Governance

[normative]

All documents must adhere to:

- CARE sovereignty  
- FAIR transparency  
- Masking of sensitive info  
- AI transform prohibitions  

---

## 🧪 Validation & CI/CD

[normative]

Test profiles MUST pass:

    markdown-lint  
    schema-lint  
    footer-check  
    accessibility-check  
    diagram-check  
    metadata-check  
    provenance-check  

Failures block merge.

---

## 🚫 7. Anti-Patterns (Forbidden)

[normative]

The following MUST NOT appear:

- Nested fences inside fenced blocks  
- H5/H6 headings  
- Bare URLs  
- Directory trees using fenced blocks in ChatGPT outputs  
- Images without alt-text  
- Non-ASCII filenames  
- Duplicate headings  
- Emoji-free section headers (for standards)  
- External links without descriptive text  

---

## 🧩 8. Macro System (Optional)

[informative]

Documents MAY use macro tokens for automated generation:

    {{kfm.header.standard}}
    {{kfm.footer.standard}}
    {{kfm.diagram.section}}
    {{kfm.directory.example}}

Macros render during CI.

---

## 🧬 9. Semantic Crosslinking Rules

[normative]

Crosslinks MUST:

- use relative paths  
- link to ontology, data, or standards documents where relevant  
- never point to deprecated paths  
- resolve to existing docs  

---

## 📚 10. Glossary (Key Terms)

[informative]

- **Header Profile** — determines title layout  
- **Footer Profile** — determines footer links and branding  
- **Diagram Profile** — defines diagram semantics  
- **Transform Registry** — governs allowed AI transformations  
- **Anti-Pattern** — a forbidden structure  
- **Stability Tier** — how volatile the content is  

---

## 🧪 Appendix A — Minimal Header Profile Example

[informative]

    ---
    title: "🌾 Simple KFM Note"
    path: "docs/notes/simple.md"
    version: "v0.1.0"
    last_updated: "2025-11-27"
    license: "CC-BY 4.0"
    header_profile: "minimal"
    ---

---

## 📘 Appendix B — Standard Document Example (Short)

[informative]

    ---
    title: "📦 KFM Data Contract v11"
    path: "docs/standards/data/kfm_data_contract_v11.md"
    version: "v11.0.0"
    header_profile: "standard"
    footer_profile: "data-spec"
    ---

---

## 🕰️ Version History

| Version | Date       | Summary                                                                                              |
|--------:|------------|------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-27 | Added semantic intent, stability tiers, macro system, anti-pattern registry, doc-kind matrix, examples. |
| v11.2.1 | 2025-11-26 | Added profiles, registries, provenance hardening.                                                    |
| v11.2.0 | 2025-11-25 | Major structural overhaul, adaptive footers, metadata layers, diagram rules.                         |

---

<div align="center">

**Kansas Frontier Matrix**  
*Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence*  

[⬅ Back to Standards Index](../README.md) ·  
[📜 Governance Charter](../governance/ROOT-GOVERNANCE.md) ·  
[🛰 Telemetry Overview](../../telemetry/README.md)

</div>
