---
title: "📜 Kansas Frontier Matrix — Accessible Legal, Treaty, and Archival Text Standards (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/accessibility/patterns/legal-archives.md"
version: "v10.4.1"
last_updated: "2025-11-16"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/a11y-legal-archives-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.3"
status: "Active / Enforced"
doc_kind: "Pattern"
intent: "a11y-legal-archives"
fair_category: "F1-A1-I1-R1"
care_label: "High-Sensitivity / Cultural-Historical"
sensitivity_level: "High"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "KFM Accessibility Council · FAIR+CARE Council · Tribal Historic Preservation Offices (THPOs)"
risk_category: "High"
redaction_required: true
previous_version_hash: "<previous-sha256>"
provenance_chain:
  - "docs/accessibility/patterns/legal-archives.md@v10.0.0"
ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "ArchiveComponent"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"
json_schema_ref: "../../../schemas/json/a11y-legal-archives.schema.json"
shape_schema_ref: "../../../schemas/shacl/a11y-legal-archives-shape.ttl"
doc_uuid: "urn:kfm:doc:a11y-legal-archives-v10.4.1"
semantic_document_id: "kfm-doc-a11y-legal-archives"
event_source_id: "ledger:docs/accessibility/patterns/legal-archives.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "modernization-of-historical-language"
  - "speculative content"
  - "alteration of treaty terms"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Culturally Sensitive Document"
jurisdiction: "Kansas / United States / Tribal Nations"
role: "a11y-pattern-legal-archives"
lifecycle_stage: "stable"
ttl_policy: "Quarterly review"
sunset_policy: "Superseded upon next treaty/archival accessibility standard update"
---

<div align="center">

# 📜 **Kansas Frontier Matrix — Accessible Legal, Treaty, and Archival Text Standards**  
`docs/accessibility/patterns/legal-archives.md`

**Purpose:**  
Define FAIR+CARE-governed accessibility, semantic encoding, and ethical stewardship standards for **treaties**, **legal documents**, **archival texts**, and **historical manuscripts** within the Kansas Frontier Matrix (KFM).  
Ensures all archival materials — including sensitive tribal records — are digitized, annotated, described, and contextualized with rigorous WCAG accessibility, TEI metadata, and cultural consent protocols.

![Docs](https://img.shields.io/badge/Docs-MCP_v6.3-blue)
![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)
![License](https://img.shields.io/badge/License-CC--BY%204.0-green)
![Status](https://img.shields.io/badge/Status-Active-success)

</div>

---

## 📘 Overview

Treaties, statutes, correspondence, and historical archives represent some of the most **culturally sensitive and legally important documents** within KFM.  
This pattern ensures that:

- Texts are **machine- and human-readable**
- Cultural contexts are explicitly surfaced
- Accessibility is guaranteed via semantic markup, ARIA tags, and content structure
- Provenance and custodial metadata preserve legal and tribal authority
- Reproduction of documents is handled with respect, transparency, and accuracy

---

## 🗂️ Directory Context

```text
docs/accessibility/
│
├── README.md
├── testing-guide.md
├── tokens.md
└── patterns/
    ├── legal-archives.md                 # This file
    ├── legal-governance-policy.md
    ├── localization.md
    ├── media.md
    ├── map-controls.md
    ├── navigation.md
    ├── ...
```

---

## 🧩 Accessibility & Metadata Standards

| Requirement             | Description                                                       | Standard Reference |
|-------------------------|-------------------------------------------------------------------|--------------------|
| Semantic Encoding       | TEI XML or semantic Markdown with `<persName>`, `<placeName>`     | TEI P5             |
| Descriptive Metadata    | Provenance, custodian, language, versioning, cultural context     | FAIR F-2 / PROV-O  |
| Transcript Readability  | OCR-corrected, human-reviewed transcription                       | WCAG 3.1.5         |
| Keyboard Navigation     | Footnotes, references, glossary, and appendices must be keyboard operable | WCAG 2.1.1 |
| Contrast & Typography   | Minimum 4.5:1 contrast; serif options allowed for facsimile mode  | WCAG 1.4.3         |
| Ethical Context Flags   | Sensitive or colonial language must be contextualized via notes   | CARE E-1           |

---

## 🧭 Example TEI Implementation (Treaty Excerpt)

~~~xml
<TEI xmlns="http://www.tei-c.org/ns/1.0">
  <teiHeader>
    <fileDesc>
      <titleStmt>
        <title>Treaty with the Kaw (Kansas) Tribe, 1825</title>
        <respStmt>
          <resp>Digitized by</resp>
          <name>Kansas Frontier Matrix</name>
        </respStmt>
      </titleStmt>
      <publicationStmt>
        <publisher>NARA (National Archives and Records Administration)</publisher>
        <availability>
          <licence target="https://creativecommons.org/licenses/by/4.0/">CC-BY 4.0</licence>
        </availability>
      </publicationStmt>
    </fileDesc>
  </teiHeader>

  <text>
    <body>
      <p>
        Article 1. The 
        <placeName>Kansas Tribe</placeName>
        hereby cede all claims to lands east of the 
        <placeName>Missouri River</placeName>.
      </p>

      <note type="context">
        Historical terminology preserved verbatim; language reflects 19th-century U.S. federal legal framing and may diverge from current tribal governance terminology.
      </note>
    </body>
  </text>
</TEI>
~~~

---

## 🧾 Ethical & Accessibility Metadata Schema

| Field                   | Description                                       | Example |
|-------------------------|---------------------------------------------------|---------|
| data-origin             | Custodian or tribal source                        | "Kaw Nation Archives" |
| data-language           | Original + translation languages                  | "English; Kaw (kkw)" |
| data-provenance         | Chain of custody                                 | "NARA → Kaw Nation → KFM" |
| data-ethics-reviewed    | FAIR+CARE review flag                             | true |
| data-fair-consent       | Consent for digital access                        | "approved" |
| data-sensitive          | Sensitivity classification                        | "High / Cultural" |

### Example JSON

~~~json
{
  "data-origin": "Kaw Nation Archives",
  "data-language": "English; Kaw (kkw)",
  "data-provenance": "NARA → Kaw Nation → KFM",
  "data-ethics-reviewed": true,
  "data-fair-consent": "approved",
  "data-sensitive": "High / Cultural"
}
~~~

---

## ⚙️ Interactions & Visual Standards

| Feature               | Implementation                                                | Notes |
|----------------------|----------------------------------------------------------------|--------|
| Hyperlinked References | Cross-links to signatories, places, and archival IDs        | TEI `@ref` |
| Language Toggle       | Original + translation toggle with ARIA controls             | `aria-controls="translation"` |
| Facsimile Alt Text    | Full description of document seals, marks, scanning context  | Required |
| Keyboard Shortcuts    | `[→]` next article, `[←]` previous article                   | Optional but recommended |
| ARIA Labels           | Article and section labels such as `aria-label="Article 3"`  | Required |

---

## 🧪 Validation Workflow

| Tool                    | Purpose                                      | Output |
|-------------------------|----------------------------------------------|--------|
| TEI Validator           | Checks schema/tag integrity                   | `tei_schema_check.json` |
| axe-core                | WCAG + ARIA compliance                        | `a11y_legal_archives.json` |
| Faircare Audit Script   | Historical bias review + cultural safety      | `ethics_review.json` |
| Manual QA               | Tribal language and context review            | Governance ledger entry |

---

## ⚖️ FAIR+CARE Integration

| Principle            | Implementation |
|----------------------|----------------|
| Collective Benefit   | Digitization increases public access to treaty history. |
| Authority to Control | Tribal custodians determine visibility, redaction, and reproduction rights. |
| Responsibility       | All provenance and consent metadata recorded in immutable governance ledgers. |
| Ethics               | Contextual notes provided for harmful or colonial terminology in archival texts. |

---

## 🕰️ Version History

| Version | Date       | Author             | Summary |
|--------:|------------|--------------------|---------|
| v10.4.1 | 2025-11-16 | Accessibility Council | Upgraded to MDP v10.4.3; added high-sensitivity metadata, TEI governance alignment, and one-box formatting guarantee. |
| v10.0.0 | 2025-11-11 | FAIR+CARE Council  | Initial archival/treaty accessibility pattern with TEI + FAIR+CARE schema. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Developed under **Master Coder Protocol v6.3** • Reviewed by **FAIR+CARE Council**  
[⬅ Back to Accessibility Index](README.md)

</div>