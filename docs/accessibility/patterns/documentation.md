---
title: "📚 Kansas Frontier Matrix — Accessible Documentation & Content Standards (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/accessibility/patterns/documentation.md"
version: "v10.4.1"
last_updated: "2025-11-16"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/a11y-documentation-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.3"
status: "Active / Enforced"
doc_kind: "Pattern"
intent: "accessible-documentation"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "KFM Documentation Council · FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "docs/accessibility/patterns/documentation.md@v10.0.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  schema_org: "CreativeWork"
  cidoc: "E31 Document"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
json_schema_ref: "../../../schemas/json/a11y-documentation.schema.json"
shape_schema_ref: "../../../schemas/shacl/a11y-documentation-shape.ttl"
doc_uuid: "urn:kfm:doc:a11y-documentation-v10.4.1"
semantic_document_id: "kfm-doc-a11y-documentation"
event_source_id: "ledger:docs/accessibility/patterns/documentation.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "policy-altering paraphrase"
  - "removal of FAIR+CARE constraints"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Documentation Standard"
jurisdiction: "Kansas / United States"
role: "a11y-pattern-documentation"
lifecycle_stage: "stable"
ttl_policy: "Quarterly review"
sunset_policy: "Superseded upon next documentation standard update"
---

<div align="center">

# 📚 **Kansas Frontier Matrix — Accessible Documentation & Content Standards**  
`docs/accessibility/patterns/documentation.md`

**Purpose:**  
Define the **inclusive writing, structure, and markup accessibility rules** used throughout the Kansas Frontier Matrix (KFM) documentation and user guides — ensuring compliance with **WCAG 2.1 AA**, **Plain Language Guidelines (ISO 24495-1)**, and **FAIR+CARE** principles for equitable information access.

![Docs](https://img.shields.io/badge/Docs-MCP_v6.3-blue)
![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)
![License](https://img.shields.io/badge/License-CC--BY%204.0-green)
![Status](https://img.shields.io/badge/Status-Stable-success)

</div>

---

## 📘 Overview

Accessible documentation ensures that **every user, researcher, and contributor** can navigate and understand the KFM knowledge base, regardless of:

- Reading level or cognitive profile  
- Assistive technology usage  
- Language, culture, or technical background  

This pattern governs structure, typography, and tone for documentation across:

- `/docs/` — Standards, guides, and reports  
- `/web/` — Frontend docs and in-app help  
- `/src/` — Code-level documentation and comments  
- `/data/` — Dataset descriptions and metadata notes  

---

## 🗂️ Directory Context

```text
docs/
│
├── accessibility/
│   └── patterns/
│       ├── documentation.md   # This file
│       └── ...
└── standards/
    └── markdown_rules.md
```

---

## 🧩 Structural Standards

| Element    | Rule                                          | Example                                  |
|-----------|-----------------------------------------------|------------------------------------------|
| Headings  | Single `<h1>` per file; descending levels     | `# Title`, `## Overview`, `### Details`  |
| Tables    | Header row + caption; use `<th>` + `scope`    | `<th scope="col">Field</th>`             |
| Lists     | Use proper ordered/unordered lists            | `- item` or `1. item`                    |
| Links     | Descriptive text (no “click here”)            | `[Governance Charter](...)`              |
| Code      | Fenced blocks with language identifier        | ```json { "key": "value" } ```          |
| Images    | Meaningful `alt` or explicit decorative mark  | `alt="KFM architecture diagram"`         |
| Diagrams  | Provide text alternative or link to narrative | “[Diagram description](diagram.md)”      |

---

## ♿ Language & Tone Guidelines

| Category          | Best Practice                                      | FAIR+CARE Rationale                     |
|-------------------|----------------------------------------------------|-----------------------------------------|
| Plain Language    | Short sentences; define technical terms            | Supports equitable understanding        |
| Cultural Neutrality| Avoid slang, idioms, culturally bound metaphors   | Promotes global readability             |
| Consistency       | Use shared glossary & terminology                  | Reduces cognitive load + translation cost|
| Tone              | Calm, factual, non-sensational                     | Respects diverse audiences              |
| Pronouns          | Prefer gender-neutral phrasing                     | CARE-aligned inclusivity                |
| Localization      | Avoid text baked into images; use ISO language codes| Enables robust localization pipelines  |

---

## 🧭 Markdown & Semantic Accessibility Rules

| Feature         | Implementation                                      | Compliance      |
|-----------------|-----------------------------------------------------|-----------------|
| Headings        | No skipped levels; logical document outline         | WCAG 2.4.6      |
| Links           | Contextual link text; avoid generic labels          | WCAG 2.4.4      |
| Alt Text        | Concise, descriptive; omit “image of…”              | WCAG 1.1.1      |
| Tables          | `<th>` with `scope="col"` or `scope="row"`          | WCAG 1.3.1      |
| Lists           | Semantic lists (`<ul>`, `<ol>`), not manual numbers | WCAG 1.3.1      |
| Color Usage     | Never convey meaning via color alone                | WCAG 1.4.1      |
| Keyboard Focus  | All interactive elements must be focusable          | WCAG 2.1.1      |

---

## 🧾 FAIR+CARE Editorial Workflow

| Stage          | Action                                            | Artifact                                 |
|----------------|----------------------------------------------------|------------------------------------------|
| Authoring      | Draft content using plain language + a11y patterns | Markdown (`.md`)                         |
| Validation     | Run `docs-lint.yml` + markdown a11y CI             | `docs_lint.json`, `a11y_docs.json`       |
| Council Review | FAIR+CARE language audit and bias review          | `faircare_language.json`                 |
| Approval       | Commit tagged with version + reviewer ID           | `governance-ledger.json` record          |

---

## ⚙️ CI Validation Pipeline

| Workflow                 | Scope                                       | Output                                      |
|--------------------------|---------------------------------------------|---------------------------------------------|
| `docs-lint.yml`          | Heading order, links, alt text, code fences | `docs_lint.json`                            |
| `markdown-a11y.yml`      | Semantic structure & screen reader checks   | `a11y_docs.json`                            |
| `faircare-language.yml`  | Tone, bias, and ethics scanning             | `faircare_language.json`                    |
| `translation-validate.yml` | Checks `lang` tags and localization tokens| `l10n_validation.json`                      |

---

## 📐 Content Authoring Checklist

- [ ] Single H1; logical heading structure  
- [ ] All images have alt text or are marked decorative  
- [ ] Tables use `<th>` and `scope` attributes  
- [ ] No meaning conveyed exclusively via color or emoji  
- [ ] All links are descriptive and unique within context  
- [ ] No unexplained acronyms; define on first use  
- [ ] Plain language summary at top of long documents  

---

## ⚖️ FAIR+CARE Integration

| Principle           | Implementation                                                                       |
|---------------------|----------------------------------------------------------------------------------------|
| Collective Benefit  | Documentation designed for public reuse and educational uptake.                       |
| Authority to Control| Community and governance stakeholders can propose edits through documented workflows. |
| Responsibility      | Revisions tracked in governance ledgers with reviewer attribution.                    |
| Ethics              | Language reviewed to avoid bias, harm, or misrepresentation of people or communities. |

---

## 🔗 Key Resources

- WCAG 2.1 Quick Reference  
- Plain Language ISO 24495-1  
- KFM Markdown Rules (`docs/standards/markdown_rules.md`)  
- FAIR+CARE Governance Charter (`../../standards/governance/ROOT-GOVERNANCE.md`)  

---

## 🕰️ Version History

| Version | Date       | Author                 | Summary                                                                                  |
|--------:|------------|------------------------|------------------------------------------------------------------------------------------|
| v10.4.1 | 2025-11-16 | Documentation Council  | Upgraded to KFM-MDP v10.4.3; added metadata, CI mapping table, and clarified tone rules. |
| v10.0.0 | 2025-11-11 | FAIR+CARE A11y Council | Initial accessible documentation standard; introduced CI workflows and editorial process.|

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Curated under **Master Coder Protocol v6.3** · Verified by **FAIR+CARE Council**  
[⬅ Back to A11y Patterns Index](../README.md)

</div>