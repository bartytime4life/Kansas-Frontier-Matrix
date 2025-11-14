---
title: "📑 Kansas Frontier Matrix — Markdown Output Protocol (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/kfm_markdown_output_protocol.md"
version: "v10.3.0"
last_updated: "2025-11-13"
review_cycle: "Annual / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/docs-markdown-protocol-v1.json"
governance_ref: "governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📑 **Kansas Frontier Matrix — Markdown Output Protocol**  
`docs/standards/kfm_markdown_output_protocol.md`  
**Diamond⁹ Ω / Crown∞Ω Ultimate Certified**

**Purpose:**  
Define the *authoritative, required, and CI-enforced* Markdown authoring standards for the Kansas Frontier Matrix (KFM). These rules cover structural formatting, metadata, headings, examples, ethics, governance, FAIR+CARE compliance, ontology alignment, and cross-repository consistency.  
Every KFM Markdown file **must** comply with this protocol.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../faircare.md)
[![Status: Active](https://img.shields.io/badge/Status-Enforced-success)]()

</div>

---

## 📘 Overview

This protocol governs **all Markdown files** produced for the Kansas Frontier Matrix (KFM).  
It merges:

- The original KFM Markdown requirements  
- All repository-wide style patterns  
- FAIR+CARE ethical rules  
- MCP v6.3 documentation mandates  
- STAC/DCAT metadata practices  
- Focus Mode / Story Node documentation rules  
- Knowledge Graph integration conventions  
- Domain-specific emoji standards  
- Directory README requirements  
- Extended validation and CI gating rules  
- Tilde-fence standard for literal code examples  

All Markdown generated in KFM must be:

- **CI-valid**  
- **FAIR+CARE compliant**  
- **Machine-parseable**  
- **Ontology-aligned**  
- **Rendering-safe on GitHub**  
- **Structurally identical across the repo**  
- **Fully reproducible and documented**  

Any Markdown not meeting the rules is **blocked from merge**.

---

## 🧱 YAML Front-Matter Requirements

Every Markdown file **must begin** with a complete YAML block.

No blank lines may appear above the block.

### Required YAML Fields

| Field | Requirement |
|---|---|
| `title` | Must include emoji + descriptive title. |
| `path` | Exact repository path. |
| `version` | Semantic version string. |
| `last_updated` | ISO 8601 date. |
| `review_cycle` | Review requirement. |
| `commit_sha` | Git SHA or `<latest-commit-hash>`. |
| `sbom_ref` | SPDX SBOM reference. |
| `manifest_ref` | Release manifest reference. |
| `telemetry_ref` | Telemetry bundle path. |
| `telemetry_schema` | Telemetry schema reference. |
| `governance_ref` | Path to governance root. |
| `license` | SPDX license. |
| `mcp_version` | MCP documentation layer version. |

> ⚠️ Missing or malformed YAML = **CI failure**.

---

## 🧩 Centered Title Block

The centered header must follow the canonical structure.

To ensure literal rendering, all examples use **tilde-fences**.

~~~~~markdown
<div align="center">

# 🧩 **Document Title**  
`path/to/file.md`  
**Diamond⁹ Ω / Crown∞Ω Ultimate Certified**

**Purpose:**  
One–three sentences describing the document’s role.

[![Docs · MCP](...)](...)
[![License: CC-BY 4.0](...)](...)
[![FAIR+CARE](...)](...)
[![Status: Active](...)]()

</div>
~~~~~

### Title Block Rules

- Must follow the YAML block immediately  
- Must include:
  - H1 title with emoji  
  - Certification line  
  - File path  
  - Purpose block  
  - Badge row  
- Must be followed by:
  - One blank line  
  - A horizontal rule (`---`)  

---

## 🧮 Heading Hierarchy (Strict)

| Level | Usage | Emoji |
|---|---|---|
| H1 | Title only | Required |
| H2 | Major sections | Required |
| H3 | Subsections | Required for Directory Layout |
| H4 | Optional deeper sections | Optional |

### Correct

~~~~~markdown
## 📘 Overview
### ⚙️ Pipeline
~~~~~

### Incorrect

~~~~~markdown
## Overview     ← Incorrect
~~~~~

---

## 🗂️ Mandatory Section Order

Every KFM Markdown file **must** follow:

1. YAML front-matter  
2. Centered Title Block  
3. Horizontal rule  
4. **Overview**  
5. (Optional) Purpose / Scope / Dependencies  
6. Main Content  
7. Directory Layout (H3 only)  
8. Validation Section  
9. Governance & Ethics Section  
10. Knowledge Graph Integration Section  
11. STAC/DCAT Metadata (if relevant)  
12. Focus Mode Integration (if relevant)  
13. Version History  
14. Footer  

Any deviation = **CI rejection**.

---

## 🧱 Domain Emoji Dictionary (Standardized)

| Domain | Emoji |
|---|---|
| Archaeology | 🏺 |
| AI / Focus Mode | 🧠 |
| Story Nodes | 🧩 |
| Climate | 🌦️ |
| Hydrology | 💧 |
| Geology | ⛰️ |
| GIS / Maps | 🗺️ |
| Architecture | 🏗️ |
| Accessibility | ♿ |
| Analysis | 📘 |
| Data / Pipelines | ⚙️ |
| Tools | 🛠️ |
| Documentation | 📖 |
| Computation | 🧮 |

All titles must use the correct domain emoji.

---

## 📁 Directory Layout Rules

Required for all top-level READMEs and any doc describing folder contents.

### Requirements

- Must use ASCII tree format  
- Must appear under `### 📁 Directory Layout`  
- Must use tilde-fenced block  
- No leading spaces before fence  
- No comments inside tree  

### Example

~~~~~text
docs/
|-- standards/
|   |-- kfm_markdown_output_protocol.md
|-- reports/
|-- analyses/
~~~~~

---

## 🧪 Validation Section (Mandatory)

All spec-style documents MUST include a validation section.

Components:

- Schema validation  
- CI workflow references  
- FAIR+CARE checks  
- Governance rules  
- Data contract compliance  

---

## 🧬 Knowledge Graph Integration (If Applicable)

Documents related to schemas, metadata, or data sources must define:

- CIDOC-CRM entity mappings  
- OWL-Time temporal properties  
- GeoSPARQL geometry usage  
- Neo4j node/edge examples  
- Relationship semantics  

---

## 🛰️ STAC/DCAT Metadata (If Applicable)

Datasets, symbol catalogs, and map layers must include:

- STAC Item example  
- STAC Collection reference  
- Asset roles (data, legend, thumbnail)  
- Scientific extension fields  
- DCAT dataset mapping  

---

## 🧠 Focus Mode Integration (If Applicable)

Docs used by Focus Mode must include:

- Narrative generation rules  
- SHAP/LIME explainability availability  
- Symbol usage  
- Relationship mappings  
- CARE-safe narrative guidelines  

---

## 📋 Table Rules

- Use pipe syntax  
- Include headers  
- No blank rows  
- Use `—` for N/A  
- Keep line width <100 chars where possible  

---

## 📦 Example Block Rules (Tilde Standard)

All complex example blocks MUST use **tilde fences**:

~~~~~markdown
~~~~~json
{ "example": "literal" }
~~~~~
~~~~~

This ensures GitHub never prematurely closes the block.

---

## 🎨 Image & Badge Rules

Badges must follow this order:

1. Docs · MCP  
2. License  
3. FAIR+CARE  
4. Status  
5. Optional CI badges  

Images must:

- Contain `alt` text  
- Specify width if >700px  

---

## 🔒 Governance & Ethics Section (Mandatory for Sensitive Data)

Must include:

- Sensitivity classification  
- CARE principles  
- Indigenous data sovereignty statements  
- Restrictions on display  
- Ethical handling guidelines  

---

## 🧯 Link Consistency Rules

All links must:

- Be relative  
- Be verified by CI  
- Avoid broken or absolute paths  
- Use correct directory depth  

---

## ⚖️ Footer Block (Required)

~~~~~markdown
---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Validated under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to Standards Index](README.md) · [Root Governance Charter](governance/ROOT-GOVERNANCE.md)

</div>
~~~~~

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.3.0 | 2025-11-13 | A. Barta | Unified KFM Markdown Output Protocol with 15 repository-wide additions + tilde-fence example rendering standard. |
| v10.2.8 | 2025-11-13 | A. Barta | Added tilde-fence pattern to prevent rendering issues. |
| v10.2.7 | 2025-11-13 | A. Barta | Initial fix for nested example rendering. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Validated under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to Standards Index](README.md) · [Root Governance Charter](governance/ROOT-GOVERNANCE.md)

</div>
