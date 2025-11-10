---
title: "📑 Kansas Frontier Matrix — Markdown Structural & Formatting Rules"
path: "docs/standards/markdown_rules.md"
version: "v10.0.0"
last_updated: "2025-11-10"
review_cycle: "Annual / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../releases/v10.0.0/manifest.zip"
telemetry_ref: "../../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/docs-markdown-rules-v2.json"
governance_ref: "governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📑 **Kansas Frontier Matrix — Markdown Structural & Formatting Rules**
`docs/standards/markdown_rules.md`

**Purpose:** Define the mandatory structural conventions, metadata requirements, and formatting syntax for all Markdown documents within the Kansas Frontier Matrix (KFM).  
These rules support **Master Coder Protocol (MCP v6.3)** and **FAIR+CARE** compliance by enforcing documentation integrity, accessibility, and machine-readability.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](faircare.md)
[![Status: Active](https://img.shields.io/badge/Status-Enforced-success)]()

</div>

---

## 📘 Overview

The KFM documentation framework relies on structured, versioned Markdown files that are **validated automatically** via:
- `.github/workflows/docs-lint.yml`
- Pre-commit hooks
- Governance audits

These rules ensure every document is:
- **Consistent in format**
- **YAML-schema compliant**
- **Cross-compatible with FAIR+CARE metadata**
- **Readable and accessible** across all systems

---

## 🧱 1. YAML Front-Matter Requirements

Each Markdown document **must** begin with a YAML metadata block.  
This front-matter provides versioning, governance, and interoperability information.

### ✅ Required Fields

| Field | Description | Example |
|--------|-------------|----------|
| `title` | Document title (must include an emoji). | `"🏗️ Kansas Frontier Matrix — System Architecture"` |
| `path` | Repository path of the document. | `"src/ARCHITECTURE.md"` |
| `version` | Semantic version. | `"v10.0.0"` |
| `last_updated` | ISO 8601 date of last modification. | `"2025-11-10"` |
| `review_cycle` | Update frequency (Quarterly / Annual). | `"Quarterly / Autonomous"` |
| `commit_sha` | Git commit hash for provenance. | `"<latest-commit-hash>"` |
| `sbom_ref` | SPDX SBOM reference path. | `"releases/v10.0.0/sbom.spdx.json"` |
| `manifest_ref` | Manifest package for release tracking. | `"releases/v10.0.0/manifest.zip"` |
| `telemetry_ref` | Path to telemetry file. | `"releases/v10.0.0/focus-telemetry.json"` |
| `telemetry_schema` | Telemetry schema path for validation. | `"schemas/telemetry/docs-markdown-rules-v2.json"` |
| `governance_ref` | Reference to governance charter. | `"docs/standards/governance/ROOT-GOVERNANCE.md"` |
| `license` | SPDX-compatible license string. | `"CC-BY 4.0"` |
| `mcp_version` | MCP documentation version. | `"MCP-DL v6.3"` |

---

## 🧩 2. Title Block Structure

Each document’s main header must be enclosed in a `<div align="center">` container for consistency and GitHub rendering accuracy.

### Example:
```markdown
<div align="center">

# 🧩 **Kansas Frontier Matrix — Governance Architecture**
`docs/standards/governance/ROOT-GOVERNANCE.md`

**Purpose:** Define the governance charter and decision-making structure for FAIR+CARE compliance.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../README.md)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](faircare.md)

</div>
```

**Rules:**
- The first line after `<div align="center">` must be an H1 heading.
- The second line must include the file path in backticks.
- The **Purpose** line should not exceed 200 characters.
- At least two badges are required (Docs, License, FAIR+CARE).

---

## 🧮 3. Heading Hierarchy Rules

| Heading Level | Syntax | Usage |
|----------------|---------|--------|
| H1 | `#` | Document title (used once). |
| H2 | `##` | Major sections (Overview, Standards, etc.). |
| H3 | `###` | Subsections or technical elements. |
| H4 | `####` | Optional nested content (limit to short blocks). |

**Emojis Required:**  
All H1–H3 headers must include a relevant emoji for semantic tagging.

**Example Hierarchy:**
```markdown
## 📘 Overview
### ⚙️ Workflow Integration
#### 🧩 Dependencies
```

---

## 🧾 4. Section Order & Layout

All KFM documents follow a standardized sequence of sections for machine parsing and readability.

### Standard Layout:
1. YAML front-matter  
2. Centered title block  
3. Horizontal divider (`---`)  
4. Table of Contents *(if applicable)*  
5. Overview  
6. Content Sections (governance, validation, workflow, compliance, etc.)  
7. Version History table  
8. Centered license footer

---

## 🧠 5. Table Formatting Rules

- Use `|` separators for all columns.  
- Include header and bottom divider lines (`|---|---|---|`).  
- Keep tables within 100 characters width.  
- Align text left.  
- Never leave cells blank; use `—` for N/A.

### Example:
```markdown
| Field | Description | Example |
|--------|-------------|----------|
| license | SPDX-compatible identifier | "CC-BY-4.0" |
| provenance | Data origin | "USGS, NOAA" |
```

---

## ⚙️ 6. Code & Data Block Rules

| Type | Syntax | Rule |
|------|---------|------|
| **Code blocks** | Triple backticks with language tag | Always specify (`json`, `bash`, `yaml`, `markdown`). |
| **Inline code** | Single backticks | Use for file paths, variable names, or commands. |
| **JSON Examples** | Must use valid JSON (double quotes, UTF-8 encoding). |
| **Bash Commands** | Use `$` prefix for commands. |

Example:
```bash
$ make validate
```

---

## 📋 7. Lists & Bullets

- Use `-` for unordered lists.  
- Use `1.` for ordered lists.  
- Indent with **two spaces**, not tabs.  
- Keep list items single-line unless step-by-step instructions.

Example:
```markdown
1. Clone the repository.
2. Run `make setup`.
3. Execute validation pipelines.
```

---

## 🧩 8. Badges & Visuals

All documents must include at least the following badges:
- **Docs · MCP**
- **License**
- **FAIR+CARE**
- **Status**

Use Shields.io for consistency. Example:

```markdown
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](faircare.md)
```

---

## 📚 9. Version History Table

Each document must include a version history with four columns: version, date, author, and summary.

Example:
```markdown
## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|---------|----------|
| v10.0.0 | 2025-11-10 | A. Barta | Upgraded to v10.0.0; aligned telemetry + SBOM refs; added required `telemetry_schema`. |
| v9.7.0 | 2025-11-05 | A. Barta | Updated schema validation reference. |
```

---

## ⚖️ 10. Footer Requirements

Every document must end with a centered footer containing:
- Year and license statement  
- MCP, FAIR+CARE, and Diamond⁹ Ω / Crown∞Ω certification text  
- Navigation links to Documentation Index and Governance Charter

### Example Footer:
```markdown
---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Maintained under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to Standards Index](README.md) · [Root Governance Charter](governance/ROOT-GOVERNANCE.md)

</div>
```

---

## 🧩 11. Validation & Enforcement

**Automated Workflow:** `.github/workflows/docs-lint.yml`

**Checks Performed:**
1. Presence of YAML front-matter with required fields.  
2. H1 title includes emoji and boldface.  
3. Footer and version history exist.  
4. Tables and code blocks are properly formatted.  
5. Relative paths are valid.  
6. File encoding is UTF-8 with final newline.

**Failure Policy:**  
- Any violation blocks pull request merge.  
- Violations are logged in `reports/self-validation/docs/violations.ndjson`.  
- Summary published in `reports/self-validation/docs/lint_summary.json`.

---

## 🧮 12. FAIR+CARE Documentation Compliance

| Principle | Implementation |
|------------|----------------|
| **Findable** | Front-matter metadata ensures discoverability. |
| **Accessible** | Markdown and JSON readable without proprietary tools. |
| **Interoperable** | Follows DCAT, STAC, and schema.org conventions. |
| **Reusable** | Open license, provenance, and version tracking included. |
| **CARE** | Culturally aware and inclusive documentation practices enforced. |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|---------|----------|
| v10.0.0 | 2025-11-10 | A. Barta | Upgraded to v10.0.0; aligned telemetry/SBOM/manifest refs; added required `telemetry_schema` to front-matter. |
| v9.7.0 | 2025-11-05 | A. Barta | Defined authoritative Markdown structure and validation rules. |
| v9.5.0 | 2025-10-20 | A. Barta | Added footer, table, and list consistency requirements. |
| v9.0.0 | 2025-06-01 | KFM Core Team | Established foundational Markdown conventions under MCP. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Validated under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to Standards Index](README.md) · [Root Governance Charter](governance/ROOT-GOVERNANCE.md)

</div>