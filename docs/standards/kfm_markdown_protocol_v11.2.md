---
title: "📑 Kansas Frontier Matrix — Markdown Authoring Protocol (KFM-MDP) v11.2"
path: "docs/standards/kfm_markdown_protocol_v11.2.md"
version: "v11.2.0"
last_updated: "2025-11-25"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · FAIR+CARE Council & Focus Mode Board"
commit_sha: "<latest-commit-hash>"
signature_ref: "releases/v11.2.0/signature.sig"
attestation_ref: "releases/v11.2.0/slsa-attestation.json"
sbom_ref: "releases/v11.2.0/sbom.spdx.json"
manifest_ref: "releases/v11.2.0/manifest.zip"
telemetry_ref: "releases/v11.2.0/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/markdown-protocol-v11.2.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-v2.json"
governance_ref: "../governance/ROOT-GOVERNANCE.md"
ethics_ref: "../faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.0"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
status: "Active / Enforced"
doc_kind: "Standard"
intent: "markdown-governance"
category: "Documentation · Protocol · Standards"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
classification: "Public"
jurisdiction: "Kansas / United States"
ttl_policy: "24 months"
sunset_policy: "Supersedes KFM-MDP v11.0.1 upon adoption"
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
  - "docs/standards/kfm_markdown_protocol_v11.md@v11.0.1"
  - "docs/standards/markdown_rules.md@v10.4.3"
  - "docs/standards/markdown_rules.md@v10.4.0"
json_schema_ref: "schemas/json/kfm-markdown-protocol-v11.2.schema.json"
shape_schema_ref: "schemas/shacl/kfm-markdown-protocol-v11.2-shape.ttl"
story_node_refs: []
immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:standards:markdown-protocol:v11.2.0"
semantic_document_id: "kfm-markdown-protocol-v11.2"
event_source_id: "ledger:kfm-markdown-protocol-v11.2"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "3d-context-render"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"
validation_profiles:
  - "docs-lint-v11"
  - "schema-lint-v11"
  - "lineage-audit-v11"
  - "governance-audit-v11"
ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"
---

<div align="center">

# 📑 **Kansas Frontier Matrix — Markdown Authoring Protocol v11.2**  
`docs/standards/kfm_markdown_protocol_v11.2.md`

**Purpose:**  
Define the authoritative Markdown authoring standard for KFM v11.2, ensuring every document is **stable**, **machine-readable**, **FAIR+CARE aligned**, **ontology-compatible**, **WCAG-accessible**, **AI-governed**, and **GitHub-render-safe**.  
This protocol governs metadata, headings, diagrams, footers, and CI/CD validation across the monorepo.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![KFM-MDP v11.2](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2-informational)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold)]()  
[![Accessibility WCAG 2.1 AA+](https://img.shields.io/badge/Accessibility-WCAG_2.1_AA%2B-blueviolet)]()  
[![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen)]()

</div>

---

## 📘 Overview

KFM-MDP v11.2 establishes the **uniform Markdown ruleset** used across the entire Kansas Frontier Matrix monorepo.

This protocol defines:

- A layered YAML metadata model  
- Required heading and section structure  
- Directory tree formatting (Option B)  
- Approved Mermaid diagram usage  
- Accessibility requirements (WCAG 2.1 AA+)  
- AI transform and Focus Mode governance  
- Semantic extractability requirements  
- CI/CD validation hooks  
- A context-aware footer system  

---

## 🧱 1. Required Document Structure

All KFM Markdown documents MUST follow the structure:

1. YAML front matter  
2. Centered header block  
3. Horizontal rule  
4. `## 📘 Overview`  
5. `## 🗂️ Directory Layout / 🧭 Context`  
6. Main content (`##`, `###`, `####` only)  
7. `## 🗺️ Diagrams`  
8. `## 🧠 Story Node & Focus Mode Integration`  
9. `## 🕰️ Version History`  
10. Footer block  

### Structural Rules:
- Exactly **one H1**  
- Only **H1–H4** allowed  
- No heading level skipping  
- Emojis strongly encouraged  
- No bare URLs  
- No nested fences inside top-level fences  
- Must pass CI lint rules  

---

## 🗂️ 2. Directory Layout Standard (Option B)

Directory layouts MUST use:

- ASCII connectors (`│`, `├──`, `└──`)  
- 4 spaces for indentation  
- No fenced code blocks in ChatGPT output (indentation only)  
- In the repository, directory trees may use fenced `text` but MUST not break GitHub render

**Example (using indentation to avoid double fences):**

    docs/
        ├── standards/                     # Standards & governance
        │   ├── kfm_markdown_protocol_v11.2.md
        │   └── governance/
        ├── architecture/
        ├── analyses/
        └── templates/

This is the **ONLY approved directory tree format**.

---

## 🗺️ 3. Diagram Specification (Mermaid Rules)

Mermaid diagrams ARE allowed and encouraged.

### Valid Use Cases:
- ETL & LangGraph flows  
- CI/CD pipelines  
- Ontology or graph visualizations  
- Timelines  
- State machines  

### Requirements:
- Under a `## 🗺️ Diagrams` section  
- Must include a caption  
- Must include a text explanation  
- Use **LR** for pipelines  
- Use **TB** for timelines  
- Keep diagrams readable (no >20 nodes)  

---

## 🧠 4. Story Node & Focus Mode Integration

Documents MAY declare Story Node IDs:

```yaml
story_node_refs: []
```

Rules:

- Narrative blocks must be extractable  
- Avoid pronoun ambiguity  
- Use ISO-8601 for dates  
- Use resolvable place/entity names  
- Optional Focus Summary blocks allowed  

Example:

> **Focus Summary:** This protocol defines how all Markdown documents in KFM v11.2 are authored, validated, governed, and interpreted.

---

## 🧩 5. YAML Metadata Layer Specification

v11.2 uses a **layered metadata model**:

### Layer 1 — Core Identity  
### Layer 2 — Governance & Risk  
### Layer 3 — Supply Chain & Telemetry  
### Layer 4 — Ontology & Schema Alignment  
### Layer 5 — Runtime & Stack  
### Layer 6 — AI Governance  
### Layer 7 — Integrity & Identity  
### Layer 8 — Provenance Chain  
### Layer 9 — Story Node Links  

Each field MUST conform to its schema in `json_schema_ref` and `shape_schema_ref`.

---

## ♿ 6. Accessibility Requirements (WCAG 2.1 AA+)

All KFM documents MUST:

- Provide alt-text for images  
- Provide text equivalents for Mermaid diagrams  
- Avoid color-only indications  
- Maintain hierarchical heading order  
- Use descriptive link text  
- Define jargon or link to the glossary  

Accessibility failures block CI merge.

---

## 🔐 7. AI Governance Requirements

The AI governance block expresses allowed & disallowed transforms:

### Allowed:
- `summary`  
- `timeline-generation`  
- `semantic-highlighting`  
- `3d-context-render`  
- `a11y-adaptations`  

### Prohibited:
- `content-alteration`  
- `speculative-additions`  
- `unverified-architectural-claims`  

Focus Mode v3 MUST obey these constraints.

`machine_extractable: true` indicates the document is safe for NLP parsing.

---

## 🧪 8. CI/CD Enforcement

All documents must pass:

- YAML schema validation  
- Markdown linting  
- Link checking  
- Accessibility audit  
- FAIR+CARE scan  
- STAC/DCAT schema validation  
- Telemetry reference validation  
- Provenance integrity checks  
- Footer correctness checks  

A failed validation **blocks merge**.

---

## 🕰️ Version History

| Version | Date       | Summary                                                                                              |
|--------:|------------|------------------------------------------------------------------------------------------------------|
| v11.2.0 | 2025-11-25 | Added adaptive footer system, directory-tree indentation fix, layered metadata model, AI governance. |
| v11.0.1 | 2025-11-20 | Previous major version; merged into v11.2 lineage.                                                   |
| v10.4.x | 2025-11-14 | Original ruleset adopted under MCP v6.3.                                                             |

---

<div align="center">

**Kansas Frontier Matrix**  
*Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence*  

[⬅ Back to Standards Index](../README.md) ·  
[📜 Governance Charter](../governance/ROOT-GOVERNANCE.md) ·  
[🛰 Telemetry Overview](../../telemetry/README.md)

</div>
