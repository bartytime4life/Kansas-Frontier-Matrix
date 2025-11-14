Here is your **updated file**, **in one single copy-and-paste markdown block**, exactly following **your Markdown Output Protocol** and **your provided metadata** — **no extra text outside the box**:

```markdown
---
title: "📑 Kansas Frontier Matrix — Markdown Structural & Formatting Rules (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/markdown_rules.md"
version: "v10.2.8"
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
Define the mandatory Markdown conventions for all KFM documentation, ensuring MCP v6.3 compliance, FAIR+CARE alignment, reproducibility, machine readability, and full CI validation.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../README.md)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](faircare.md)  
[![Status: Active](https://img.shields.io/badge/Status-Enforced-success)]()

</div>

---

## 📘 Overview
This document defines the **authoritative** Markdown output protocol for the Kansas Frontier Matrix (KFM).  
All Markdown must pass:

- `make docs-validate`
- `docs-lint.yml`
- `markdown-validate.yml`
- `stac-validate.yml`
- FAIR+CARE classifier
- MCPLint v10.2+
- CI schema and link validation

Markdown files not passing validation are **rejected by CI**.

---

## 🧱 YAML Front-Matter Requirements

All KFM Markdown files must:

- Begin with a full YAML front-matter block  
- Contain **no blank lines above** the YAML block  

### 🧩 Required Fields

| Field | Requirement |
|---|---|
| `title` | Must contain emoji + descriptive title. |
| `path` | Exact file path. |
| `version` | Semantic version. |
| `last_updated` | ISO date. |
| `review_cycle` | Review frequency label. |
| `commit_sha` | Git SHA or `<latest-commit-hash>`. |
| `sbom_ref` | SPDX SBOM reference path. |
| `manifest_ref` | Release manifest path. |
| `telemetry_ref` | Telemetry dataset path. |
| `telemetry_schema` | Telemetry schema path. |
| `governance_ref` | Governance charter path. |
| `license` | SPDX license identifier. |
| `mcp_version` | MCP documentation layer version. |

> ⚠️ Missing or malformed YAML = **automatic CI failure**.

---

## 🧩 Centered Title Block Structure

~~~~~markdown
<div align="center">

# 🧩 **Document Title**  
`path/to/file.md`

**Purpose:**  
A one–three sentence summary of the document’s intent.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](...)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](...)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](...)
[![Status: Active](https://img.shields.io/badge/Status-Enforced-success)]()

</div>
~~~~~

### 🔒 Title Block Rules
- No blank lines between YAML and title block  
- Must be wrapped in `<div align="center">`  
- Badge order (MANDATORY):  
  1. Docs · MCP  
  2. License  
  3. FAIR+CARE  
  4. Status  
- Followed by **one blank line** and `---`

---

## 🧮 Heading Hierarchy (Strict)

| Level | Purpose | Emoji |
|---|---|---|
| H1 | Document title | Required |
| H2 | Major sections | Required |
| H3 | Subsections | Required |
| H4 | Optional nested content | Optional |

Correct:
~~~~~markdown
## 📘 Overview
### ⚙️ Workflow
~~~~~

Incorrect:
~~~~~markdown
## Overview
~~~~~

---

## 🗂️ Section Order (Strict)

1. YAML front-matter  
2. Centered Title Block  
3. `---`  
4. Overview  
5. Main content  
6. Directory Layout (H3)  
7. Version History  
8. Footer  

Any deviation = CI FAILURE.

---

## 📁 Directory Layout Rules

~~~~~text
docs/
|-- standards/
|   |-- markdown_rules.md
|-- analyses/
|-- reports/
~~~~~

Rules:
- Must be under `### 📁 Directory Layout`
- ASCII tree only, no comments
- Must be in fenced code block with **no leading spaces**

---

## 📦 Code & Data Block Requirements

| Element | Rules |
|---|---|
| Code blocks | Must specify language |
| JSON | Valid only, no comments |
| YAML | Spaces only |
| Bash | Use `$` for commands |
| Inline code | Required for paths & commands |

Invalid blocks = CI failure.

---

## 📋 Table Rules
- Pipe format only  
- Must include header row  
- Avoid empty rows  
- Use `—` for missing values  

---

## 🎨 Images & Badges

### ✔️ Badge Order
1. Docs · MCP  
2. License  
3. FAIR+CARE  
4. Status  
5. Optional

### 🖼 Image Rules
- Alt text required  
- Width required if >700px  

---

## 🧪 Mermaid Diagram Rules

~~~~~mermaid
flowchart LR
  A["Start"] --> B["Finish"]
~~~~~

Rules:
- Only `flowchart LR` or `flowchart TD`
- Node labels MUST be quoted
- One diagram per section

---

## 🧩 Version History Requirement

~~~~~markdown
## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.2.8 | 2025-11-13 | A. Barta | Regenerated file using tilde-fence system to prevent GitHub rendering collisions. |
~~~~~

---

## ⚖️ Footer (Mandatory)

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
| v10.2.8 | 2025-11-13 | A. Barta | Converted ALL example blocks to tilde-fence system to guarantee literal rendering. |
| v10.2.7 | 2025-11-13 | A. Barta | Applied 5-backtick fencing (superseded by tilde standard). |
| v10.2.6 | 2025-11-13 | A. Barta | Fixed example rendering edge cases. |
| v10.2.5 | 2025-11-13 | A. Barta | Adjusted nested fences. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Validated under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to Standards Index](README.md) · [Root Governance Charter](governance/ROOT-GOVERNANCE.md)

</div>
```
