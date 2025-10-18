<div align="center">

# 🧹 **Kansas Frontier Matrix — Issue Templates**

`📁 .github/ISSUE_TEMPLATE/README.md`

**Mission:** Standardize issue triage across code, data, AI/ML, UX, and governance — ensuring **traceable**, **reproducible**, **secure**, and **MCP-compliant** communication.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../LICENSE)
[![Docs-Validate](https://img.shields.io/badge/docs-validated-brightgreen)](../../workflows/docs-validate.yml)
[![Policy-as-Code](https://img.shields.io/badge/policy-OPA%2FConftest-purple)](../../workflows/policy-check.yml)
[![Security](https://img.shields.io/badge/security-CodeQL%20%7C%20Trivy%20%7C%20Gitleaks-red)](../../workflows/)
[![SBOM](https://img.shields.io/badge/SBOM-Syft%20%2B%20Grype-blue)](../../workflows/sbom.yml)

</div>

---

## 📚 Overview

KFM leverages **GitHub Issue Forms** to:

- Capture **provenance** (paths, STAC, commit SHA, environment)
- Document **reproducible steps** (inputs, commands, expected vs. actual)
- Assess **impact** (SemVer matrix)
- **Auto-label** issues for routing (e.g., `area:data`, `priority:p1`, `semver:minor`)
- Enforce **MCP-DL** & **Docs-as-Code** quality gates

> All forms are YAML-based, validated by **docs-validate** and policy gates (OPA/Conftest).

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

> ⚠️ When adding new templates, update `config.yml` and ensure labels/milestones exist.

---

## ⚡ Create New Issue

| Type             | Template                                          |
|------------------|---------------------------------------------------|
| 🐞 Bug           | `?template=bug_report.yml`                        |
| 💡 Feature       | `?template=feature_request.yml`                   |
| 🗃️ Data Request | `?template=data_request.yml`                      |
| 🧰 Data Fix      | `?template=data_correction.yml`                   |
| 🧪 Research      | `?template=research_issue.yml`                    |
| ♿ Accessibility  | `?template=accessibility_issue.yml`               |
| 🔐 Security      | `?template=security_vuln.yml` *(see SECURITY.md)* |
| 🧭 Governance    | `?template=governance_question.yml`               |

→ Base URL: `https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/new`

---

## ✅ Core Form Fields

| Template              | Key Fields (excerpt)                                                                                                 |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------|
| `bug_report`          | repro steps, env, logs, **Commit SHA**, **CI run link**, **SemVer impact**, screenshots                                |
| `feature_request`     | user story, acceptance criteria, dependencies, migration risk, **SemVer impact**                                      |
| `data_request`        | source link, **license**, time/space bounds, **STAC target**, **data_ethics**, ETL plan, validation checks             |
| `data_correction`     | error summary, evidence, **derived_from** fixes, checksum regeneration plan, test steps                               |
| `research_issue`      | hypothesis, datasets, methods, success metrics, risks                                                                 |
| `accessibility_issue` | barrier, **WCAG** reference, keyboard steps, assistive tech used, fix proposal                                        |
| `security_vuln`       | summary (redacted), CVSS, affected versions/hashes, repro (safe), mitigation, **coordinated disclosure** preference   |
| `governance_question` | policy/topic, background, proposed change, affected SOPs/ADRs                                                         |

---

## 🧠 Issue Routing & Auto-Labeling

| Label           | Purpose                         |
|-----------------|---------------------------------|
| `bug`           | Code/data/metadata defect       |
| `enhancement`   | Feature or flow improvement     |
| `data-request`  | Propose new external dataset    |
| `documentation` | Docs, SOPs, metadata edits      |
| `security`      | Vulnerabilities & fixes         |
| `accessibility` | WCAG / usability reports        |
| `semver:patch`  | Bug fix (no interface change)   |
| `semver:minor`  | New feature / non-breaking      |
| `semver:major`  | Breaking change                 |
| `area:ci`       | Actions & governance            |
| `area:data`     | STAC/ETL/datasets               |
| `area:web`      | Frontend                        |
| `area:etl`      | Pipelines                       |

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

## 🧾 `config.yml` Highlights (Issue Forms)

```yaml
blank_issues_enabled: false
contact_links:
  - name: 🤠 KFM Discussions
    url: https://github.com/bartytime4life/Kansas-Frontier-Matrix/discussions
  - name: 📬 Propose New Dataset
    url: https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/new?template=data_request.yml
  - name: 🔐 Report a Security Issue (Private)
    url: https://github.com/bartytime4life/Kansas-Frontier-Matrix/security/advisories/new
```

---

## 🧩 Template Snippets (Drop-in Fields)

### SemVer Impact (all templates)

```yaml
- type: dropdown
  id: semver
  attributes:
    label: SemVer Impact
    options: ["patch", "minor", "major", "unknown"]
  validations:
    required: true
```

### Provenance & Repro Fields (bugs/data)

```yaml
- type: input
  id: commit_sha
  attributes:
    label: Commit SHA (7–40)
    description: The commit hash reproducing the issue.
- type: input
  id: stac_id
  attributes:
    label: STAC Item/Collection ID (if applicable)
- type: textarea
  id: repro
  attributes:
    label: Steps to Reproduce
    description: Include exact commands, inputs, and environment.
```

### Data Ethics (data_request / data_correction)

```yaml
- type: dropdown
  id: data_ethics
  attributes:
    label: Data Ethics
    description: Ethical handling of sensitive/Indigenous data
    options: ["open", "restricted-derivatives", "no-public-artifacts"]
  validations:
    required: true
```

### Accessibility Confirmation (UI issues)

```yaml
- type: checkboxes
  id: a11y_checks
  attributes:
    label: A11y checks attempted
    options:
      - label: Keyboard-only repro
      - label: Screen reader repro
      - label: Contrast inspected (≥4.5:1)
```

### Security (security_vuln)

```yaml
- type: input
  id: cvss
  attributes:
    label: CVSS Score (optional)
- type: textarea
  id: safe_repro
  attributes:
    label: Safe Repro Steps
    description: Do not post secrets or active exploit details.
```

---

## 🔐 Policy-as-Code & Quality Gates

- **docs-validate:** Lints Markdown + checks links & metadata in issue templates  
- **OPA/Conftest:** Blocks forms missing critical fields (SemVer, provenance, license)  
- **Gitleaks:** Secret scanning on new/edited templates  
- **Actionlint:** Validates any changes under `.github/**`  
- **Retention:** CI ensures artifacts/logs retained ≥90d for auditability

---

## ♻️ Maintenance Schedule

| Cadence   | Task                                            |
|-----------|--------------------------------------------------|
| Weekly    | Validate forms with docs-validate & actionlint   |
| Monthly   | Sync labeler rules + audit auto-label coverage   |
| Quarterly | Review template scope (bug/feature/data/security)|
| Release   | Align fields with updated SOPs / MCP standards   |

```bash
# Utilities
make sync-templates     # Optional helper target
```

---

## 📓 MCP Compliance Matrix

| ✅ Principle         | Verified via...                               |
|---------------------|-----------------------------------------------|
| Documentation-First | Required form sections + ADR/README links     |
| Reproducibility     | Steps + env + expected/actual                 |
| Provenance          | Commit SHA, STAC IDs, derived_from fields     |
| Open Standards      | YAML Forms · STAC · CSV/JSON                  |
| Auditability        | Labels, lifecycle states, PR cross-linking    |
| Versioning          | SemVer impact field on every form             |
| Security            | OPA policy checks · Gitleaks · private advisories |

---

## 🕓 Version History

| Version | Date       | Summary                                                           |
|---------|------------|-------------------------------------------------------------------|
| v2.6.0  | 2025-10-18 | Added policy gates, data_ethics field, security contact links     |
| v2.5.0  | 2025-10-16 | Layout reformat · GFM tables · CLI examples                      |
| v2.4.0  | 2025-10-16 | Docs-validate integration · labeler/auto-label docs               |
| v2.3.1  | 2025-10-15 | MCP-DL v6.3 alignment · link + label config updates              |
| v2.3.0  | 2025-10-13 | Acceptance criteria & provenance hardened                        |
| v2.0.0  | 2025-10-10 | Versioned YAML forms + STAC-aware templates                      |
| v1.0.0  | 2025-10-04 | Initial Issue Template spec + forms                              |

---

<div align="center">

### 🧭 Kansas Frontier Matrix — “Clarity in Every Report. Collaboration in Every Request.”

</div>