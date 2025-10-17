<div align="center">

# 🧹 **Kansas Frontier Matrix — Issue Templates**

`📁 .github/ISSUE_TEMPLATE/README.md`

**Mission:** Standardize issue triage across code, data, UX, and governance — ensuring **traceable**, **reproducible**, and **MCP-compliant** communication.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../LICENSE)

</div>

---

## 📚 Overview

KFM leverages **GitHub Issue Forms** to:

* Capture provenance (paths, STAC, commit SHA)
* Document reproducible steps
* Assess impact (SemVer)
* Auto-label issues for routing (e.g. `area:data`, `priority:p1`, `semver:minor`)

---

## 🗂️ Template Directory

```bash
.github/ISSUE_TEMPLATE/
├── README.md
├── bug_report.yml
├── feature_request.yml
├── data_request.yml
├── data_correction.yml
├── research_issue.yml
├── accessibility_issue.yml
├── security_vuln.yml
├── governance_question.yml
└── config.yml
```

---

## ⚡ Create New Issue

| Type             | Template                                          |
| ---------------- | ------------------------------------------------- |
| 🐞 Bug           | `?template=bug_report.yml`                        |
| 💡 Feature       | `?template=feature_request.yml`                   |
| 🗃️ Data Request | `?template=data_request.yml`                      |
| 🧰 Data Fix      | `?template=data_correction.yml`                   |
| 🧪 Research      | `?template=research_issue.yml`                    |
| ♿ Accessibility  | `?template=accessibility_issue.yml`               |
| 🔐 Security      | `?template=security_vuln.yml` *(see SECURITY.md)* |
| 🧭 Governance    | `?template=governance_question.yml`               |

→ Use full URL base: `https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/new`

---

## ✅ Core Form Fields

| Template              | Key Fields                                                              |
| --------------------- | ----------------------------------------------------------------------- |
| `bug_report`          | repro steps, logs, SHA, SemVer impact, CI link                          |
| `feature_request`     | use case, solution sketch, dependencies, acceptance criteria            |
| `data_request`        | source link, license, time/space bounds, ETL/STAC target, provenance    |
| `data_correction`     | what's wrong, evidence, fix plan, impact, validation steps              |
| `research_issue`      | hypothesis, methods, expected result, risks                             |
| `accessibility`       | barrier, WCAG reference, keyboard steps, fix proposal                   |
| `security_vuln`       | summary (safe), CVSS, image hashes, repro (redacted), secure disclosure |
| `governance_question` | topic, context, suggested change                                        |

---

## 🧠 Issue Routing & Auto-Labeling

| Label           | Purpose                       |
| --------------- | ----------------------------- |
| `bug`           | Code/data/metadata defect     |
| `enhancement`   | Feature or flow improvement   |
| `data-request`  | Propose new external dataset  |
| `documentation` | Docs, SOPs, metadata edits    |
| `security`      | Vulnerabilities & fixes       |
| `accessibility` | UI/UX usability or WCAG issue |
| `semver:patch`  | Bug fix (no interface change) |
| `semver:minor`  | New feature                   |
| `semver:major`  | Breaking change               |
| `area:ci`       | GitHub Actions or governance  |

### Example `.github/labeler.yml`

```yaml
area:data:
  - 'data/**'
area:web:
  - 'web/**'
area:etl:
  - 'src/**'
area:ci:
  - '.github/**'
```

### Example `auto-label.yml`

```yaml
name: Auto Label
on:
  pull_request_target:
    types: [opened, synchronize]
jobs:
  label:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/labeler@v5
        with:
          repo-token: ${{ secrets.GITHUB_TOKEN }}
```

---

## 🧾 config.yml Highlights

```yaml
blank_issues_enabled: false
contact_links:
  - name: 🤠 KFM Discussions
    url: https://github.com/bartytime4life/Kansas-Frontier-Matrix/discussions
  - name: 📬 Propose New Dataset
    url: https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/new?template=data_request.yml
```

---

## ♻️ Maintenance Schedule

| Cadence   | Task                                         |
| --------- | -------------------------------------------- |
| Monthly   | Sync labeler rules + review auto-label       |
| Quarterly | Audit template coverage (bugs/features/data) |
| Release   | Align template fields with updated SOPs      |

```bash
# Optional: utility script
make sync-templates
```

---

## 📓 MCP Compliance Matrix

| ✅ Principle         | Verified via...                             |
| ------------------- | ------------------------------------------- |
| Documentation-First | Required form fields, references, links     |
| Reproducibility     | Steps + env + expected/actual               |
| Provenance          | Commit SHA, STAC item, metadata             |
| Open Standards      | YAML Forms · STAC · CSV/JSON                |
| Auditability        | Labels, lifecycle, triage, PR cross-linking |
| Versioning          | SemVer impact field per form                |

---

## 🕓 Version History

| Version | Date       | Summary                                          |
| ------- | ---------- | ------------------------------------------------ |
| v2.4.0  | 2025-10-16 | Layout reformat · GFM tables · CLI examples      |
| v2.3.1  | 2025-10-15 | MCP-DL v6.3 alignment · link + label config docs |
| v2.3.0  | 2025-10-13 | Acceptance criteria & provenance hardened        |
| v2.0.0  | 2025-10-10 | Versioned YAML forms + STAC-aware templates      |
| v1.0.0  | 2025-10-04 | Initial Issue Template spec + forms              |

---

<div align="center">

### 🧭 Kansas Frontier Matrix — “Clarity in Every Report. Collaboration in Every Request.”

</div>
