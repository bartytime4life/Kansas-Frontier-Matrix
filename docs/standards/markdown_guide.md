---
title: "🧾 Kansas Frontier Matrix — Markdown Styling & Documentation Guide"
path: "docs/standards/markdown_guide.md"
version: "v10.0.0"
last_updated: "2025-11-10"
review_cycle: "Annual / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../releases/v10.0.0/manifest.zip"
telemetry_ref: "../../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/docs-markdown-guide-v2.json"
governance_ref: "governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
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
version: "v10.0.0"
last_updated: "2025-11-10"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "releases/v10.0.0/sbom.spdx.json"
manifest_ref: "releases/v10.0.0/manifest.zip"
telemetry_ref: "releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/system-architecture-v2.json"
governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---
```

### Title Block
Each document must begin with:
- `<div align="center">` wrapper  
- A **primary title (`#`)** with emoji and bold name  
- A **path identifier** in backticks  
- A **purpose statement**  
- Badges (Docs · MCP, License, FAIR+CARE, Status)

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
|------:|------------------|---------|---------|
| H1 | `#` | Title of document (used once per file). | `# 🏗️ Kansas Frontier Matrix — Architecture` |
| H2 | `##` | Major sections (Overview, Standards, etc.). | `## 📘 Overview` |
| H3 | `###` | Subsections or technical detail. | `### ⚙️ Workflow Integration` |
| H4 | `####` | Optional nested subsections (avoid overuse). | `#### 🧩 Dependencies` |

All section headers should include a **relevant emoji** for visual navigation and semantic context.

---

## 🧾 Markdown Formatting Rules

| Element | Rule | Example |
|--------|------|---------|
| **Lists** | Use `-` for unordered lists and maintain consistent two-space indentation. | `- Item One` |
| **Code Blocks** | Always specify language for syntax highlighting. | ```json ... ``` |
| **Inline Code** | Use backticks for paths, filenames, or commands. | `data/sources/manifest.json` |
| **Links** | Prefer relative paths for intra-repo linking. | `[see architecture](../../src/ARCHITECTURE.md)` |
| **Tables** | Minimum three columns; use `—` for N/A; ≤100 chars width. | `| Field | Desc | Example |` |
| **Quotes** | Use `>` for guidance or notable statements. | `> Example best practice` |
| **Dividers** | Use `---` between major sections. | `---` |
| **Emojis** | Prefix major headings (H1–H3) with semantic emojis. | `## ⚙️ Configuration` |
| **Footers** | Every document ends with a centered governance footer. | See footer example |

---

## 🧮 YAML Front-Matter Requirements

These fields are validated by **docs-lint** and governance pipelines.

| Field | Description | Required |
|------|-------------|---------|
| `title` | Document title with emoji. | ✅ |
| `path` | Relative repository path. | ✅ |
| `version` | Semantic version tag. | ✅ |
| `last_updated` | ISO 8601 date string. | ✅ |
| `review_cycle` | Frequency of review (Quarterly, Annual). | ✅ |
| `commit_sha` | Git commit hash for provenance. | ✅ |
| `sbom_ref` | SPDX SBOM path. | ⚙️ |
| `manifest_ref` | Release manifest path. | ⚙️ |
| `telemetry_ref` | Telemetry ledger path. | ⚙️ |
| `telemetry_schema` | Telemetry schema path. | ⚙️ |
| `governance_ref` | Governance charter path. | ✅ |
| `license` | SPDX license id. | ✅ |
| `mcp_version` | MCP documentation version string. | ✅ |

---

## 🧠 Visual Conventions

| Component | Style | Example |
|----------|-------|---------|
| **File Path** | Always in backticks and lower-case. | `` `docs/standards/README.md` `` |
| **Bold Keywords** | For emphasis on key terms. | **FAIR+CARE**, **MCP v6.3** |
| **Badges** | Use Shields.io with consistent colors. | Docs (blue), License (green), FAIR+CARE (orange), Status (brightgreen) |
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
1. Presence and correctness of YAML front-matter (all required keys).  
2. Compliance with section hierarchy and emoji prefixes.  
3. Proper license badge and centered footer.  
4. Consistent heading, list, and table syntax.  
5. Relative path verification for internal links.  
6. UTF-8 file encoding and final newline.

**Outputs:**
- `reports/self-validation/docs/lint_summary.json`
- `reports/self-validation/docs/violations.ndjson`

---

## ⚖️ FAIR+CARE Compliance in Documentation

| Principle | Documentation Implementation |
|----------|-------------------------------|
| **Findable** | Front-matter metadata ensures discoverability. |
| **Accessible** | Markdown written in plain English; semantic emojis aid scanning. |
| **Interoperable** | YAML headers machine-readable for governance APIs (DCAT/STAC alignment). |
| **Reusable** | Open license, provenance, and version tracking included. |
| **CARE** | Inclusive language and culturally respectful representation enforced via lint rules. |

---

## 🧮 Example: Valid README Template

```markdown
---
title: "🌾 Kansas Frontier Matrix — Overview"
path: "README.md"
version: "v10.0.0"
last_updated: "2025-11-10"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "releases/v10.0.0/sbom.spdx.json"
manifest_ref: "releases/v10.0.0/manifest.zip"
telemetry_ref: "releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/docs-readme-v2.json"
governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
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
| v10.0.0 | 2025-11-10 | A. Barta | Example of compliant Markdown under MCP v6.3 (v10 telemetry & SBOM refs). |

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
| v10.0.0 | 2025-11-10 | A. Barta | Upgraded to v10.0.0; aligned telemetry/SBOM/manifest refs; added `telemetry_schema` to required fields. |
| v9.7.0 | 2025-11-05 | A. Barta | Added complete Markdown style and linting guide for FAIR+CARE documentation. |
| v9.5.0 | 2025-10-20 | A. Barta | Expanded rules for YAML headers and versioned footers. |
| v9.0.0 | 2025-06-01 | KFM Core Team | Established Markdown documentation baseline. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Governed under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to Standards Index](README.md) · [Root Governance Charter](governance/ROOT-GOVERNANCE.md)

</div>