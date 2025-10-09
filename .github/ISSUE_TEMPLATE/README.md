<div align="center">

# 🧩 Kansas Frontier Matrix — Issue Templates

**Path:** `.github/ISSUE_TEMPLATE/`

**Mission:** Standardize **issue reporting, feature proposals, and data requests**
to maintain **reproducibility**, **transparency**, and **high-quality collaboration**
within the **Kansas Frontier Matrix (KFM)** project.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../LICENSE)

</div>

---

## 📚 Overview

The `.github/ISSUE_TEMPLATE/` directory defines **pre-formatted GitHub Issue templates**
that ensure **structured, auditable, and reproducible communication** across KFM domains —
including code, data, documentation, and research.

Each template follows the **Master Coder Protocol (MCP)** philosophy:
documentation-first, provenance-linked, and reproducibility-driven.

Templates enforce completeness and consistency, helping contributors provide
all necessary metadata and ensuring issues remain traceable throughout their lifecycle.

---

## 🗂️ Directory Layout

```bash
.github/ISSUE_TEMPLATE/
├── README.md
├── bug_report.md          # Report defects in code, data, or metadata
├── feature_request.md     # Propose new features or enhancements
├── data_request.md        # Suggest new datasets or integrations
└── config.yml             # GitHub Issue Forms configuration
```

> 💡 **Tip:**
> These templates leverage **GitHub Issue Forms (YAML)** for improved user experience
> and automatic metadata capture in the GitHub UI.

---

## 🧾 Template Summaries

### 🐛 Bug Report (`bug_report.md`)

| Field                   | Purpose                                                       |
| :---------------------- | :------------------------------------------------------------ |
| **Summary**             | Concise description of the bug or problem.                    |
| **Steps to Reproduce**  | Deterministic steps to replicate the issue.                   |
| **Expected vs. Actual** | Highlight discrepancy between expected and observed behavior. |
| **System Context**      | OS, Python version, workflow ID, etc.                         |
| **Related Workflow**    | Identify affected pipeline or CI process.                     |
| **Proposed Fix**        | (Optional) Suggested resolution or next steps.                |

---

### 💡 Feature Request (`feature_request.md`)

| Field                       | Purpose                                              |
| :-------------------------- | :--------------------------------------------------- |
| **Motivation / Use Case**   | Explain why this feature is valuable or needed.      |
| **Proposed Solution**       | Describe the design or functionality.                |
| **Alternatives Considered** | Note any similar solutions reviewed.                 |
| **Dependencies**            | List tools, data, or configurations required.        |
| **Impact**                  | Describe expected effects on data or code pipelines. |

---

### 🗃️ Data Request (`data_request.md`)

| Field                         | Purpose                                         |
| :---------------------------- | :---------------------------------------------- |
| **Dataset Name**              | Name of proposed dataset.                       |
| **Source / URL**              | Reference link, API endpoint, or archive.       |
| **License**                   | Usage terms or data license.                    |
| **Temporal / Spatial Scope**  | Geographic extent and time range.               |
| **Data Type**                 | Raster, vector, tabular, text, or mixed.        |
| **Intended Use**              | Describe integration purpose or output target.  |
| **Provenance Considerations** | Attribution, citation, or lineage requirements. |

---

## ⚙️ Issue Forms Configuration (`config.yml`)

GitHub allows repository-wide defaults for issue creation.

**Example Configuration:**

```yaml
blank_issues_enabled: false
contact_links:
  - name: 🧠 Kansas Frontier Matrix Discussion Forum
    url: https://github.com/bartytime4life/Kansas-Frontier-Matrix/discussions
    about: For open discussions, ideas, or general questions.
  - name: 📬 Data Contribution Requests
    url: https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/new?template=data_request.md
    about: Submit new dataset proposals or integrations.
```

---

## 🧠 Governance & MCP Alignment

| MCP Principle           | Implementation                                                 |
| :---------------------- | :------------------------------------------------------------- |
| **Documentation-first** | All issues must include context and metadata.                  |
| **Reproducibility**     | Requires deterministic reproduction or test case.              |
| **Open Standards**      | Templates use Markdown/YAML for GitHub-native workflows.       |
| **Provenance**          | Issues reference dataset, workflow, or commit IDs.             |
| **Auditability**        | Issue lifecycle tracked from report → resolution → validation. |

---

## 🧩 Contributor Workflow

1. **Choose Template:** Select *Bug Report*, *Feature Request*, or *Data Request*.
2. **Complete Fields:** Fill in all reproducibility, context, and provenance details.
3. **Submit Issue:** Auto-labeled according to template type.
4. **Review & Validation:** Core maintainers triage and assign reviewers.
5. **Close / Convert:** Issue closed or linked to corresponding pull request.

---

## 🧰 Labels & Automation

Labels are applied automatically via `.github/workflows/auto-label.yml`.

| Label           | Description                              |
| :-------------- | :--------------------------------------- |
| `bug`           | Auto-applied to bug reports.             |
| `enhancement`   | For feature or performance improvements. |
| `data-request`  | For dataset or integration proposals.    |
| `documentation` | For docs-related improvements or issues. |
| `needs-review`  | Marks items awaiting maintainer triage.  |

---

## 🧹 Maintenance

* Review templates **quarterly** for relevance and clarity.
* Update `config.yml` when adding new categories or communication links.
* Archive resolved issues periodically for long-term recordkeeping.

**Optional Makefile Target:**

```bash
make sync-templates
```

---

## 📅 Version History

| Version    | Date       | Summary                                                             |
| :--------- | :--------- | :------------------------------------------------------------------ |
| **v1.0.0** | 2025-10-04 | Initial issue template documentation (bug, feature, data requests). |
| **v1.1.0** | 2025-10-09 | Added MCP governance and auto-label workflow documentation.         |

---

<div align="center">

### 🧭 Kansas Frontier Matrix — “Clarity in Every Report. Collaboration in Every Request.”

📍 [`.github/ISSUE_TEMPLATE/`](.) · Structured, auditable issue management for KFM.

</div>
