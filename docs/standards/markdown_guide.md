---
title: "🧾 Kansas Frontier Matrix — Markdown Styling & Documentation Guide"
path: "docs/standards/markdown_guide.md"
version: "v9.7.0"
last_updated: "2025-11-05"
review_cycle: "Annual / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v9.7.0/sbom.spdx.json"
manifest_ref: "../../releases/v9.7.0/manifest.zip"
telemetry_ref: "../../releases/v9.7.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/docs-markdown-guide-v1.json"
governance_ref: "governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 🧾 **Kansas Frontier Matrix — Markdown Styling & Documentation Guide**
`docs/standards/markdown_guide.md`

**Purpose:** Establish consistent formatting, layout, and stylistic conventions for all documentation in the Kansas Frontier Matrix (KFM).  
These rules align with **Master Coder Protocol (MCP v6.3)**, **Platinum README Template v7.1**, and **FAIR+CARE** standards to ensure clarity, accessibility, and interoperability across all Markdown documents.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](faircare.md)
[![Status: Stable](https://img.shields.io/badge/Status-Stable-success)]()

</div>

---

## 📘 Overview

All Markdown documentation in KFM follows the **GitHub-Flavored Markdown (GFM)** specification with standardized **YAML front-matter**, **emoji-enhanced headers**, and **table-based clarity**.  
This ensures documents render consistently across GitHub, Zenodo, and machine-parsed FAIR+CARE metadata extractors.

Every file:
- Begins with a **YAML metadata header**
- Follows a predictable **section hierarchy**
- Includes **badges and contextual metadata**
- Ends with a **version history** and **© footer**

---

## 🧱 Structure of a KFM Document

Each document begins with a **YAML Front-Matter Block** and a **center-aligned heading**.

### Example Header Format
```yaml
---
title: "🏗️ Kansas Frontier Matrix — System Architecture"
path: "src/ARCHITECTURE.md"
version: "v9.7.0"
last_updated: "2025-11-05"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "releases/v9.7.0/sbom.spdx.json"
manifest_ref: "releases/v9.7.0/manifest.zip"
telemetry_ref: "releases/v9.7.0/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/system-architecture-v1.json"
governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
---
```

### Title Block
Each document must begin with:
- `<div align="center">` wrapper
- A **primary title (`#`)** with emoji and bold name
- A **path identifier** in backticks
- A **purpose statement**
- Optional **badges** for documentation version and governance status

Example:
```markdown
<div align="center">

# 🧩 **Kansas Frontier Matrix — Governance Architecture**
`docs/standards/governance/ROOT-GOVERNANCE.md`

**Purpose:** Define the ethical and technical governance structure for KFM, aligned with FAIR+CARE and MCP frameworks.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../README.md)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](faircare.md)

</div>
```

---

## 🧩 Section Hierarchy

| Level | Markdown Symbol | Purpose | Example |
|--------|------------------|----------|----------|
| H1 | `#` | Title of document (used once per file). | `# 🏗️ Kansas Frontier Matrix — Architecture` |
| H2 | `##` | Major sections (Overview, Standards, etc.). | `## 📘 Overview` |
| H3 | `###` | Subsections or technical detail. | `### ⚙️ Workflow Integration` |
| H4 | `####` | Optional nested subsections (avoid overuse). | `#### 🧩 Dependencies` |

All section headers should include a **relevant emoji** for visual navigation and semantic context.

---

## 🧾 Markdown Formatting Rules

| Element | Rule | Example |
|----------|------|----------|
| **Lists** | Use `-` for unordered lists and maintain consistent indentation. | `- Item One` |
| **Code Blocks** | Always specify language for syntax highlighting. | ```json ... ``` |
| **Inline Code** | Use backticks for paths, filenames, or commands. | `data/sources/manifest.json` |
| **Links** | Prefer relative paths for intra-repo linking. | `[see architecture](../../src/ARCHITECTURE.md)` |
| **Tables** | Use minimal borders and consistent spacing. | `| Header | Data |` |
| **Quotes** | Use `>` for guidance or notable statements. | `> Example best practice` |
| **Dividers** | Use `---` between major sections. | `---` |
| **Emojis** | Include semantic emojis before major headings. | `## ⚙️ Configuration` |
| **Footers** | Every document ends with an aligned copyright footer. | See below |

---

## 🧮 YAML Front-Matter Requirements

Every KFM Markdown file must contain a front-matter header with specific metadata fields.  
These are used by validation tools, governance dashboards, and FAIR+CARE audits.

| Field | Description | Required |
|--------|-------------|-----------|
| `title` | Document title with emoji. | ✅ |
| `path` | Relative repository path. | ✅ |
| `version` | Semantic version tag. | ✅ |
| `last_updated` | ISO 8601 date string. | ✅ |
| `review_cycle` | Frequency of document review (Quarterly, Annual). | ✅ |
| `commit_sha` | Git commit hash for provenance. | ✅ |
| `sbom_ref` | Link to SBOM SPDX manifest. | ⚙️ |
| `manifest_ref` | Link to release manifest. | ⚙️ |
| `telemetry_ref` | Link to telemetry log or metrics. | ⚙️ |
| `governance_ref` | Link to governance charter. | ✅ |

---

## 🧠 Visual Conventions

| Component | Style | Example |
|------------|-------|----------|
| **File Path** | Always in backticks and lowercase. | `` `docs/standards/README.md` `` |
| **Bold Keywords** | Use for emphasis on important terms. | **FAIR+CARE**, **MCP v6.3** |
| **Emojis** | Always precede major headers. | `## ⚖️ Governance` |
| **Badges** | Use Shields.io with consistent colors. | `[![License](https://img.shields.io/badge/License-CC--BY%204.0-green)]` |
| **Center Alignment** | Only for document titles and footers. | `<div align="center"> ... </div>` |

---

## 🧩 Footer Requirements

All documents end with a **versioned governance footer** to reinforce open licensing and audit status.

### Example Footer
```markdown
---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Maintained under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to Documentation Index](../README.md) · [Root Governance Charter](governance/ROOT-GOVERNANCE.md)

</div>
```

---

## ⚙️ Linting & Validation

**Automated Workflow:** `.github/workflows/docs-lint.yml`

**Validation Rules Include:**
1. Presence and correctness of YAML front-matter.
2. Compliance with section hierarchy and emoji prefixes.
3. Proper license badge and copyright footer.
4. Consistent heading and table syntax.
5. Relative path verification for internal links.

**Outputs:**
- `reports/self-validation/docs/lint_summary.json`
- `reports/self-validation/docs/violations.ndjson`

---

## ⚖️ FAIR+CARE Compliance in Documentation

| Principle | Documentation Implementation |
|------------|-------------------------------|
| **Findable** | All documents indexed in telemetry and manifest references. |
| **Accessible** | Markdown written in plain, readable English with semantic emojis. |
| **Interoperable** | YAML headers machine-readable for governance APIs. |
| **Reusable** | Openly licensed (CC-BY 4.0) and version-tracked. |
| **CARE** | Inclusive language and culturally respectful representation. |

---

## 🧮 Example: Valid README Template

```markdown
---
title: "🌾 Kansas Frontier Matrix — Overview"
path: "README.md"
version: "v9.7.0"
last_updated: "2025-11-05"
review_cycle: "Quarterly / Autonomous"
commit_sha: "abc123def456"
sbom_ref: "releases/v9.7.0/sbom.spdx.json"
manifest_ref: "releases/v9.7.0/manifest.zip"
telemetry_ref: "releases/v9.7.0/focus-telemetry.json"
governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 🌾 **Kansas Frontier Matrix — Open Historical Data System**
`README.md`

**Purpose:** Provide an overview of the Kansas Frontier Matrix repository and its governance architecture.  
Follows **MCP v6.3** · **FAIR+CARE** · **Open Data**.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](docs/README.md)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](docs/standards/faircare.md)

</div>

## 📘 Overview
Kansas Frontier Matrix is an open data initiative that unites Kansas’s historical, cultural, and environmental archives into a geospatial knowledge platform.

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|---------|----------|
| v9.7.0 | 2025-11-05 | A. Barta | Example of compliant Markdown under MCP v6.3. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Maintained under **Master Coder Protocol v6.3** · FAIR+CARE Certified  
[Back to Documentation Index](docs/README.md)

</div>
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|---------|----------|
| v9.7.0 | 2025-11-05 | A. Barta | Added complete Markdown style and linting guide for FAIR+CARE documentation. |
| v9.5.0 | 2025-10-20 | A. Barta | Expanded rules for YAML headers and versioned footers. |
| v9.0.0 | 2025-06-01 | KFM Core Team | Established Markdown documentation baseline. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Governed under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to Standards Index](README.md) · [Root Governance Charter](governance/ROOT-GOVERNANCE.md)

</div>
