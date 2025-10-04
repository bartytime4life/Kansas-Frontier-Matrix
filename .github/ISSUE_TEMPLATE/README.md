<div align="center">

# 🧩 Kansas Frontier Matrix — Issue Templates  
`.github/ISSUE_TEMPLATE/`

**Mission:** Standardize **issue reporting, feature proposals, and data requests**  
to maintain reproducibility, transparency, and high-quality collaboration  
within the Kansas Frontier Matrix (KFM) project.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue)](../../../LICENSE)

</div>

---

## 📚 Overview

The `.github/ISSUE_TEMPLATE/` directory defines **pre-formatted issue templates**  
used for structured communication across all KFM project domains — code, data, documentation, and research.

Templates ensure that **every submission is reproducible, documented, and auditable**,  
following the **Master Coder Protocol (MCP)** documentation-first philosophy.

Each template guides contributors to include essential metadata,  
minimizing ambiguity and ensuring traceability through the repository’s lifecycle.

---

## 🗂️ Directory Layout

```bash
.github/ISSUE_TEMPLATE/
├── README.md
├── bug_report.md          # For reporting defects in code, data, or metadata
├── feature_request.md     # For proposing enhancements or new features
├── data_request.md        # For requesting integration of new datasets
└── config.yml             # GitHub Issue Forms configuration
````

> **Note:**
> These templates use **GitHub Issue Forms (YAML)** when available for better UX
> and metadata capture directly through the GitHub UI.

---

## 🧾 Template Summaries

### 🐛 Bug Report (`bug_report.md`)

| Field                            | Purpose                                       |
| :------------------------------- | :-------------------------------------------- |
| **Summary**                      | Short description of the bug or issue.        |
| **Steps to Reproduce**           | Deterministic steps to replicate the problem. |
| **Expected vs. Actual Behavior** | Clear comparison for debugging.               |
| **System Context**               | OS, Python version, workflow ID, etc.         |
| **Related Workflow**             | Affected CI/CD or ETL pipeline.               |
| **Proposed Fix / Next Steps**    | Optional recommendations from reporter.       |

---

### 💡 Feature Request (`feature_request.md`)

| Field                       | Purpose                                                |
| :-------------------------- | :----------------------------------------------------- |
| **Motivation / Use Case**   | Why this feature or enhancement is needed.             |
| **Proposed Solution**       | Detailed description of the idea or workflow.          |
| **Alternatives Considered** | Any similar features or approaches tested.             |
| **Dependencies**            | External tools, data, or configuration files required. |
| **Impact**                  | Expected outcome on data architecture or pipelines.    |

---

### 🗃️ Data Request (`data_request.md`)

| Field                          | Purpose                                      |
| :----------------------------- | :------------------------------------------- |
| **Dataset Name**               | Name of the proposed dataset.                |
| **Data Source / URL**          | Reference link or API endpoint.              |
| **License**                    | Licensing information or terms of use.       |
| **Temporal / Spatial Scope**   | Years and geographic coverage.               |
| **Data Type**                  | Raster, vector, tabular, text, or mixed.     |
| **Intended Use / Integration** | Where it fits in the KFM ecosystem.          |
| **Provenance Considerations**  | Any limitations or attribution requirements. |

---

## ⚙️ Issue Forms Configuration (`config.yml`)

The optional `config.yml` file defines repository-wide defaults for issue creation.

**Example:**

```yaml
blank_issues_enabled: false
contact_links:
  - name: 🧠 Kansas Frontier Matrix Discussion Forum
    url: https://github.com/bartytime4life/Kansas-Frontier-Matrix/discussions
    about: Please use Discussions for general questions or brainstorming.
  - name: 📬 Data Contribution Requests
    url: https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/new?template=data_request.md
    about: Use this form to propose adding new datasets.
```

---

## 🧠 Governance & MCP Alignment

| MCP Principle           | Implementation                                                      |
| :---------------------- | :------------------------------------------------------------------ |
| **Documentation-first** | Every issue must include reproducible metadata and context.         |
| **Reproducibility**     | Bug reports and requests require deterministic reproduction steps.  |
| **Open Standards**      | Templates written in Markdown/YAML for GitHub-native compatibility. |
| **Provenance**          | All issues link back to dataset, workflow, or commit references.    |
| **Auditability**        | Issues tracked end-to-end from report → fix → validation.           |

---

## 🧩 Contributor Workflow

1. **Choose Template:** Select “Bug Report,” “Feature Request,” or “Data Request.”
2. **Complete Fields:** Provide all reproducibility details and links.
3. **Submit:** The issue auto-labels by category (`bug`, `enhancement`, `data-request`).
4. **Review & Validation:** Core maintainers triage and assign reviewers.
5. **Close or Convert:** Once addressed, issue is closed or converted into a pull request.

---

## 🧰 Labels & Automation

GitHub labels are automatically applied via `.github/workflows/auto-label.yml`:

| Label           | Description                                       |
| :-------------- | :------------------------------------------------ |
| `bug`           | Automatically added to bug reports.               |
| `enhancement`   | For feature requests or performance improvements. |
| `data-request`  | For proposed new datasets or source integrations. |
| `documentation` | For documentation issues or suggestions.          |
| `needs-review`  | Added to issues awaiting triage by maintainers.   |

---

## 🧹 Maintenance

* Review issue templates **quarterly** for relevance and clarity.
* Update `config.yml` when new categories or discussion channels are added.
* Archive or migrate resolved issues periodically for long-term recordkeeping.

**Makefile Target (Optional):**

```bash
make sync-templates
```

---

## 📅 Version History

| Version | Date       | Summary                                                             |
| :------ | :--------- | :------------------------------------------------------------------ |
| v1.0    | 2025-10-04 | Initial issue template documentation (bug, feature, data requests). |

---

<div align="center">

**Kansas Frontier Matrix** — *“Clarity in Every Report. Collaboration in Every Request.”*
📍 [`.github/ISSUE_TEMPLATE/`](.) · Standardized reporting and feedback system for Kansas Frontier Matrix.

</div>
