<div align="center">

# 📚 Kansas Frontier Matrix — **Documentation Review Template**  
`docs/integration/reviews/templates/doc_review_template.md`

**Purpose:** Standardize the review of all **Markdown documentation, SOPs, and experiment logs**  
in the **Kansas Frontier Matrix (KFM)** to ensure alignment with **MCP-DL v6.3**,  
**Markdown Governance Standards**, and project-wide **reproducibility, provenance, and accessibility**  
requirements.  

[![Docs-Validate](https://img.shields.io/badge/docs-validated-brightgreen?logo=github)](../../../../../.github/workflows/docs-validate.yml)
[![Policy-as-Code](https://img.shields.io/badge/policy-OPA%2FConftest-purple)](../../../../../.github/workflows/policy-check.yml)
[![Markdown Governance](https://img.shields.io/badge/Governance-MCP--DL%20v6.3-blue)](../../../standards/markdown_rules.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../LICENSE)

</div>

```yaml
---
title: "Documentation Review Template"
document_type: "Review Template · Documentation"
version: "v1.0.0"
last_updated: "2025-10-18"
created: "2025-10-04"
owners: ["@kfm-docs","@kfm-review-board","@kfm-accessibility"]
status: "Stable"
maturity: "Production"
scope: "Docs/Integration/Reviews/Templates"
license: "CC-BY 4.0"
tags: ["review","documentation","markdown","standards","accessibility","validation"]
audit_framework: "MCP-DL v6.3"
---
````

---

## 🧭 Overview

This template is used to perform **documentation reviews** for all new or modified Markdown files
(e.g., READMEs, SOPs, experiment logs, architecture docs, model cards, etc.)
prior to integration into the main repository.

Documentation is evaluated for:

* **Compliance** with the KFM Markdown Style & Rules
* **Clarity** and reproducibility of content
* **Accessibility** for both human and AI readers
* **Metadata completeness** (YAML front matter, versioning, provenance)

> Completed templates must be saved under
> `docs/integration/reviews/logs/YYYY-MM-DD_<doc_name>_docreview.md`.

---

## 🧾 Document Information

| Field              | Description                                  | Example                                       |
| :----------------- | :------------------------------------------- | :-------------------------------------------- |
| **Document Title** | File title or top-level heading              | `Kansas Frontier Matrix — Treaty Integration` |
| **Path**           | File path in repo                            | `docs/integration/treaties.md`                |
| **Review Type**    | README / SOP / Experiment / Template / Other | `README`                                      |
| **Reviewer(s)**    | Assigned reviewers                           | `@kfm-docs`, `@kfm-accessibility`             |
| **Date**           | ISO 8601                                     | `2025-10-18`                                  |
| **CI Build ID**    | Optional                                     | `#1583`                                       |

---

## 🧩 Validation Checklist

| Check                        | Description                                                 | Status |
| :--------------------------- | :---------------------------------------------------------- | :----- |
| [ ] **Front Matter Present** | YAML header with version, owner, tags, and audit info.      |        |
| [ ] **Header Block**         | `<div align="center">` with title, badges, and path.        |        |
| [ ] **Badges**               | Includes required badges (Docs Validate, License, MCP-DL).  |        |
| [ ] **Consistent Structure** | Overview → Workflow → Validation → References.              |        |
| [ ] **Emoji Headings**       | Sections use standardized emoji-based titles.               |        |
| [ ] **Horizontal Rules**     | Section breaks use `---` consistently.                      |        |
| [ ] **Tables & Alignment**   | Properly aligned columns (no wrapping issues).              |        |
| [ ] **Mermaid Diagrams**     | Valid syntax and end marker `<!-- END OF MERMAID -->`.      |        |
| [ ] **Relative Links**       | All internal links use relative paths and render on GitHub. |        |
| [ ] **Accessibility**        | Alt-text for images, heading hierarchy correct.             |        |
| [ ] **ToC Inclusion**        | For files >800 lines, auto-generated ToC present.           |        |
| [ ] **Version Table**        | `📅 Version History` section present and updated.           |        |
| [ ] **License Footer**       | Ends with project footer & mission quote.                   |        |

---

## 🧠 Metadata & Provenance Review

| Check                       | Description                                             | Status |
| :-------------------------- | :------------------------------------------------------ | :----- |
| [ ] **Owners Declared**     | Authors and maintainers listed in YAML.                 |        |
| [ ] **Audit Framework**     | MCP-DL v6.3 cited.                                      |        |
| [ ] **Semantic Tags**       | Includes tags for ontology and workflow mapping.        |        |
| [ ] **Preservation Policy** | Mentions checksum, archival, or STAC/DCAT link.         |        |
| [ ] **Change Log**          | Versioning aligned with commit or PR.                   |        |
| [ ] **Related Docs Linked** | Cross-links to architecture, standards, templates, etc. |        |

---

## 🔍 Content Quality & Reproducibility

| Check                          | Description                                                  | Status |
| :----------------------------- | :----------------------------------------------------------- | :----- |
| [ ] **Clarity**                | Text concise, readable, and technically accurate.            |        |
| [ ] **Reproducibility**        | Commands/code blocks can be executed as written.             |        |
| [ ] **Scientific Integrity**   | Citations and data references included.                      |        |
| [ ] **Formatting Consistency** | Matches KFM Markdown style (font, spacing, lists).           |        |
| [ ] **Accessibility (WCAG)**   | Passes color contrast and heading-level checks.              |        |
| [ ] **AI Compatibility**       | Proper use of YAML, semantic tags, and metadata for parsing. |        |

---

## 🧮 Documentation Validation Commands

Run these commands locally before submission:

```bash
make docs-validate        # Validates all Markdown formatting & YAML front matter
make policy-check         # Confirms all docs meet OPA/Conftest governance policies
make link-check           # Scans for broken internal and external links
make lint                 # Runs markdownlint + yamllint checks
```

---

## 🧩 Reviewer Summary

| Field                        | Notes                                                    |
| :--------------------------- | :------------------------------------------------------- |
| **Findings**                 |                                                          |
| **Actions Required**         |                                                          |
| **Follow-up Tasks**          |                                                          |
| **Cross-References Updated** |                                                          |
| **Decision**                 | ☐ Approved  ☐ Conditional Approval  ☐ Revisions Required |

---

## 🗃 YAML Review Record (Append to Audit Log)

```yaml
document: treaties.md
review_type: documentation
reviewers: ["@kfm-docs","@kfm-accessibility"]
status: approved
validation:
  header_block: valid
  links: verified
  structure: consistent
  accessibility: pass
notes: "Documentation adheres to MCP-DL structure; internal anchors fixed."
timestamp: 2025-10-18T15:45:00Z
```

---

## 🔗 References

* [`docs/standards/markdown_guide.md`](../../../standards/markdown_guide.md) — KFM Markdown guide
* [`docs/standards/markdown_rules.md`](../../../standards/markdown_rules.md) — Markdown governance & formatting rules
* [`docs/integration/reviews/checklist.md`](../checklist.md) — Full review checklist
* [`docs/architecture/data-architecture.md`](../../../architecture/data-architecture.md) — Repository structure reference
* [`docs/standards/metadata.md`](../../../standards/metadata.md) — Metadata schemas

---

<div align="center">

### 📖 “Documentation is the map that keeps Kansas’s data frontier navigable.”

**Kansas Frontier Matrix Review Council · MCP-DL v6.3**

</div>
