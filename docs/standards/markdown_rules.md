```
---
title: "📑 Kansas Frontier Matrix — Markdown Structural & Formatting Rules (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/markdown_rules.md"
version: "v10.2.3"
last_updated: "2025-11-13"
review_cycle: "Annual / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/docs-markdown-rules-v2.json"
governance_ref: "governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📑 **Kansas Frontier Matrix — Markdown Structural & Formatting Rules**  
`docs/standards/markdown_rules.md`

**Purpose:**  
Define the authoritative formatting, metadata, and structural standards for *all* Markdown within the Kansas Frontier Matrix (KFM) project.  
These rules enforce **MCP v6.3**, **FAIR+CARE**, strict reproducibility, and automated validation across the KFM monorepo.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](faircare.md)
[![Status: Active](https://img.shields.io/badge/Status-Enforced-success)]()

</div>

---

## 📘 Overview

This specification defines the **mandatory Markdown formatting protocol** for every document in the KFM monorepo.  
All Markdown produced by contributors or automated systems must pass:

- `docs-lint.yml`
- `markdown-validate.yml`
- `stac-validate.yml`
- FAIR+CARE automated checks  
- MCPLint v10 series  
- Dead link scanner  
- Front-matter schema validator  

These rules ensure Markdown is:

- Structurally uniform  
- Machine-parseable  
- Indexed cleanly inside the Knowledge Graph  
- Fully versioned & ethically compliant  
- Ready for automated CI enforcement  

---

## 🧱 1. YAML Front-Matter Requirements

All KFM Markdown **must** begin with a YAML block containing **no blank lines above it**.

### 📌 Required Fields (v10.2.3)

| Field | Description |
|---|---|
| `title` | Must include emoji + full KFM title. |
| `path` | Exact file path inside repo. |
| `version` | Semantic version for the document. |
| `last_updated` | ISO date string. |
| `review_cycle` | “Quarterly / Annual / Autonomous / FAIR+CARE Council”. |
| `commit_sha` | Git SHA or `<latest-commit-hash>`. |
| `sbom_ref` | SPDX SBOM reference. |
| `manifest_ref` | Release manifest reference. |
| `telemetry_ref` | Telemetry dataset reference. |
| `telemetry_schema` | Schema governing the telemetry fields. |
| `governance_ref` | Path to governance root. |
| `license` | SPDX identifier (CC-BY 4.0 for docs). |
| `mcp_version` | “MCP-DL v6.3”. |

Failure to include any required fields results in a **CI rejection**.

---

## 🧩 2. Title Block Structure (Centered)

The centered header block is **mandatory**.

### Correct template:

```

<div align="center">

# 🧩 **Document Title**

`path/to/file.md`

**Purpose:** One–three lines max.

[![Docs · MCP](...)](...)
[![License: CC-BY 4.0](...)](...)
[![FAIR+CARE](...)](...)
[![Status: Active](...)]()

</div>
```

### Mandatory rules:

* Must appear **immediately after** YAML front-matter.
* Must include:

  * H1 Title (with emoji)
  * File path (backticks)
  * Purpose statement
  * 2–5 badges in correct order:

    1. Docs · MCP
    2. License
    3. FAIR+CARE
    4. Status
* Must be followed by **one blank line** and then `---`.

---

## 🧮 3. Heading Hierarchy

| Level | Usage          | Emoji?      |
| ----- | -------------- | ----------- |
| H1    | Title only     | Required    |
| H2    | Major sections | Required    |
| H3    | Subsections    | Recommended |
| H4    | Deep nesting   | Optional    |

### Correct:

```
## 📘 Overview
### ⚙️ Pipeline
```

### Incorrect:

```
## Overview
### Pipeline
```

---

## 🗂️ 4. Section Order

Every KFM Markdown file must follow this sequence:

1. YAML front-matter
2. Centered title block
3. Horizontal rule
4. **Overview** (H2)
5. Content sections (H2/H3)
6. **Directory Layout** (if present—must always be H3)
7. Version History
8. Footer

Documents missing any required section fail validation.

---

## 📁 5. Directory Layout Rules (Strict)

* Must be inside a fenced code block.
* Must have **no indentation before** the fence.
* Format must follow ASCII tree format exactly.
* Never place comments inside directory trees.

### Example:

````
```text
docs/
|-- standards/
|   |-- markdown_rules.md
|-- analyses/
|-- reports/
````

```

---

## 📦 6. Code & Data Block Rules

| Type | Requirements |
|---|---|
| Code blocks | Always specify language. |
| JSON | Must be valid — no comments allowed. |
| YAML | Must not include tabs. |
| Shell | Prefer `$` prefix. |
| Inline code | Required for file paths. |

Invalid JSON/YAML automatically rejects the PR.

---

## 📋 7. Tables

- Use pipe format.
- No blank rows.
- All columns require headers.
- Use `—` for N/A fields.
- Keep width under ~100 chars where possible.

---

## 🎨 8. Badges & Images

Badges:

- Follow strict order:
  1. Docs · MCP  
  2. License  
  3. FAIR+CARE  
  4. Status  
- Max 5 badges.

Images:

- Must include descriptive alt text.
- Must specify width if larger than 700px.

---

## 🧪 9. Mermaid Diagrams

Rules:

- Max 1 diagram per section.
- Only `flowchart TD` or `flowchart LR`.
- No `classDef`.
- Every node must use quoted labels.

---

## 🧩 10. Version History Section

Template:

```

## 🕰️ Version History

| Version | Date       | Author   | Summary                                                    |
| ------- | ---------- | -------- | ---------------------------------------------------------- |
| v10.2.3 | 2025-11-13 | A. Barta | Full structural rewrite, badge rules, enforcement updates. |

```

---

## ⚖️ 11. Footer Block

Footer is required and must match template:

```

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**
Validated under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified
[Back to Standards Index](README.md) · [Root Governance Charter](governance/ROOT-GOVERNANCE.md)

</div>
```

---

## 🧮 12. Validation & Enforcement Enhancements (v10.2.3)

Documents must comply with:

* MCPLint v10.2
* Markdown structural schema
* docs-lint.yml
* FAIR+CARE automated classifier
* Dead link detection
* STAC/DCAT metadata extraction

If a document fails validation, the merge is **blocked**.

---

## 🧠 13. FAIR+CARE Compliance

Markdown must support:

* Openness
* Provenance
* Machine readability
* Ethical tagging
* Indigenous Data Sovereignty
* Reproducible metadata

All sensitive data must include CARE labels.

---

## 🕰️ Version History

| Version | Date       | Author   | Summary                                                                   |
| ------- | ---------- | -------- | ------------------------------------------------------------------------- |
| v10.2.3 | 2025-11-13 | A. Barta | Full rule application and restructuring under stored memory requirements. |
| v10.2.2 | 2025-11-12 | A. Barta | Strengthened Mermaid, badge, and enforcement rules.                       |
| v10.0.0 | 2025-11-10 | A. Barta | Added telemetry_schema rules and CARE integration.                        |
| v9.7.0  | 2025-11-05 | A. Barta | Introduced formal structure, metadata blocks, and rule hierarchy.         |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**
Validated under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified
[Back to Standards Index](README.md) · [Root Governance Charter](governance/ROOT-GOVERNANCE.md)

</div>
```
