<div align="center">

# 🧹 **Kansas Frontier Matrix — Issue Templates**

**Path:** `.github/ISSUE_TEMPLATE/`
**Mission:** Standardize **issue reporting, feature proposals, data requests, and governance topics** to keep KFM **reproducible, auditable, versioned, and MCP-compliant**.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../LICENSE)

</div>

---

## 📚 Overview

`.github/ISSUE_TEMPLATE/` hosts **GitHub Issue Forms** enforcing **documentation-first**, **provenance-linked**, and **reproducibility-driven** reporting across code, data, docs, and research.
Forms capture the **who / what / where / when / how** so every issue stays traceable from **report → triage → resolution → validation**.

All forms:

* require **provenance** (paths, STAC item IDs, commit SHAs)
* ask for **repro steps** and **environment**
* include **SemVer impact** and **acceptance criteria** (when relevant)
* auto-label for routing (`area:*`, `priority:*`, `semver:*`)

---

## 🗂️ Directory Layout

```bash
.github/ISSUE_TEMPLATE/
├── README.md
├── bug_report.yml           # Report defects in code, data, or metadata
├── feature_request.yml      # Propose features/enhancements
├── data_request.yml         # Suggest datasets/integrations
├── data_correction.yml      # Correct existing datasets/metadata
├── research_issue.yml       # Research/hypothesis/ADR input
├── accessibility_issue.yml  # UI/UX accessibility (WCAG/ARIA)
├── security_vuln.yml        # Vulnerability disclosure (redacted details)
├── governance_question.yml  # Governance/process clarification
└── config.yml               # Issue Forms configuration + defaults
```

> **Why YAML forms?** Required fields, labels, and metadata are captured **at creation time** in the GitHub UI — keeping issues consistent and audit-ready.

---

## ⚡ Quick Links (New Issue)

* 🐞 **Bug Report:** `…/issues/new?template=bug_report.yml`
* 💡 **Feature Request:** `…/issues/new?template=feature_request.yml`
* 🗃️ **Data Request:** `…/issues/new?template=data_request.yml`
* 🧰 **Data Correction:** `…/issues/new?template=data_correction.yml`
* 🧪 **Research Issue:** `…/issues/new?template=research_issue.yml`
* ♿ **Accessibility Issue:** `…/issues/new?template=accessibility_issue.yml`
* 🔐 **Security Vulnerability:** `…/issues/new?template=security_vuln.yml` (see `SECURITY.md`)
* 🧭 **Governance Question:** `…/issues/new?template=governance_question.yml`

> Replace `…` with `https://github.com/bartytime4life/Kansas-Frontier-Matrix`.

---

## 🧓 Template Summaries

### 🐞 `bug_report.yml`

| Field                   | Purpose                                             |
| ----------------------- | --------------------------------------------------- |
| **Summary**             | Concise description of the bug                      |
| **Steps to Reproduce**  | Deterministic steps + minimal inputs                |
| **Expected vs Actual**  | Clarify discrepancy                                 |
| **System Context**      | OS, Python/Node versions, container digest, run URL |
| **Related Workflow**    | Link CI job URL or pipeline module                  |
| **Logs / Screenshots**  | Evidence                                            |
| **Proposed Fix**        | Optional sketch / patch                             |
| **Provenance**          | Paths, dataset IDs, STAC items, commit SHAs         |
| **SemVer Impact**       | `none` / `patch` / `minor` / `major`                |
| **Acceptance Criteria** | Testable confirmation of the fix                    |

### 💡 `feature_request.yml`

| Field                     | Purpose                                   |
| ------------------------- | ----------------------------------------- |
| **Motivation / Use Case** | Problem statement & stakeholders          |
| **Proposed Solution**     | Functional sketch + UX notes              |
| **Alternatives**          | Options considered / rejected             |
| **Dependencies**          | Tools, APIs, data, permissions            |
| **Impact**                | Effects on ETL, graph, UI, CI, governance |
| **SemVer Impact**         | `none` / `patch` / `minor` / `major`      |
| **Acceptance Criteria**   | Testable completion definition            |

### 🗃️ `data_request.yml`

| Field                   | Purpose                                   |
| ----------------------- | ----------------------------------------- |
| **Dataset Name**        | Human-readable title                      |
| **Source / URL**        | API, portal, or archive link              |
| **License**             | Terms (PD, CC-BY-4.0, etc.)               |
| **Temporal / Spatial**  | Time range + bbox/CRS                     |
| **Data Type**           | Raster, vector, tabular, text, mixed      |
| **Provenance**          | Citation, lineage, quality notes          |
| **Integration Target**  | ETL pipeline, STAC collection, layer tags |
| **Acceptance Criteria** | What defines successful integration       |

### 🧰 `data_correction.yml`

| Field                   | Purpose                                    |
| ----------------------- | ------------------------------------------ |
| **Issue Description**   | What’s wrong in current data/metadata      |
| **Evidence**            | Docs, alternate source, QA plots           |
| **Scope**               | Items/Collections affected + versions      |
| **Fix Proposal**        | How to correct + validation steps          |
| **SemVer Impact**       | `none` / `patch` / `minor` / `major`       |
| **Acceptance Criteria** | Post-fix checks (checksums, STAC validate) |

### 🧪 `research_issue.yml`

| Field                     | Purpose                           |
| ------------------------- | --------------------------------- |
| **Hypothesis / Question** | Research framing                  |
| **Data / Methods**        | Datasets, models, SOPs, ADR links |
| **Expected Outcome**      | Metrics, figures, or narrative    |
| **Risks / Limitations**   | Data gaps, bias, thresholds       |
| **Provenance**            | Prior work and sources            |

### ♿ `accessibility_issue.yml`

| Field              | Purpose                                |
| ------------------ | -------------------------------------- |
| **Barrier**        | Description + affected user(s)         |
| **WCAG Ref**       | Guideline & level (e.g., 2.1 AA 1.4.3) |
| **Repro Steps**    | Keyboard, reader, contrast evidence    |
| **Fix Suggestion** | ARIA roles/labels, color tokens, focus |

### 🔐 `security_vuln.yml`

| Field                   | Purpose                                  |
| ----------------------- | ---------------------------------------- |
| **Summary**             | High-level vuln description (no secrets) |
| **Impact**              | Potential risk/severity (CVSS if known)  |
| **Repro (sanitized)**   | Safe steps/logs w/o sensitive data       |
| **Environment**         | Versions, image hashes, Actions refs     |
| **Disclosure**          | Private contact (see `SECURITY.md`)      |
| **Acceptance Criteria** | Criteria to consider risk resolved       |

### 🧭 `governance_question.yml`

| Field        | Purpose                             |
| ------------ | ----------------------------------- |
| **Topic**    | Process/roles/reviews/branch policy |
| **Context**  | Where confusion arose               |
| **Proposal** | Suggested governance tweak          |

---

## ⚙️ Issue Forms Configuration (`config.yml`)

```yaml
blank_issues_enabled: false
contact_links:
  - name: 🤠 KFM Discussions
    url: https://github.com/bartytime4life/Kansas-Frontier-Matrix/discussions
    about: For open questions, ideation, and design dialogue.
  - name: 📬 Data Contribution Request
    url: https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/new?template=data_request.yml
    about: Propose new datasets or integrations.

issue_template:
  - name: "🐞 Bug Report"
    about: "Report a defect in code/data/metadata"
    labels: ["bug","needs-triage"]
    assignees: ["@kfm-architecture"]
  - name: "💡 Feature Request"
    about: "Propose a feature or improvement"
    labels: ["enhancement","needs-triage"]
```

> **Auto-Labeling:** Pair with `/.github/workflows/auto-label.yml` to add domain labels (e.g., `area:data`, `area:web`) based on changed paths.

---

## 🤠 MCP & Governance Alignment

| MCP Principle           | Implementation                                                               |
| ----------------------- | ---------------------------------------------------------------------------- |
| **Documentation-First** | Required fields capture story, context, and rationale                        |
| **Reproducibility**     | Steps, environment, expected/actual results mandated                         |
| **Open Standards**      | Markdown + **YAML Issue Forms**; STAC links for dataset issues               |
| **Provenance**          | Commit SHAs, STAC item IDs, dataset IDs required                             |
| **Auditability**        | Lifecycle tracked; cross-linked to PRs and workflow runs                     |
| **Versioning**          | Forms ask for **SemVer impact** + STAC `properties.version` where applicable |

---

## 🤵 Contributor Workflow

1. **Choose Template** — Bug, Feature, Data Request, Data Correction, Research, Accessibility, Security, Governance.
2. **Complete Required Fields** — Include reproducible steps and provenance.
3. **Submit** — Templates auto-label (`bug`, `enhancement`, `data-request`, etc.).
4. **Triage** — Maintainers add `priority:` and `area:` labels, assign reviewers, set milestone.
5. **Resolve** — Link to PR(s), validate in CI, close with summary + references.

---

## 🌿 Labels & Automation

**Suggested labels** (and auto-label rules via `actions/labeler`):

| Label                            | Purpose                       |
| -------------------------------- | ----------------------------- |
| `bug`                            | Defects in code/data/docs     |
| `enhancement`                    | New features or improvements  |
| `data-request`                   | Dataset/integration proposals |
| `documentation`                  | Docs & governance updates     |
| `security`                       | Vulnerabilities & hardening   |
| `accessibility`                  | UI/UX compliance issues       |
| `needs-triage`                   | Awaiting maintainer review    |
| `priority:p0/p1/p2`              | Urgency levels                |
| `semver:none/patch/minor/major`  | Declared impact               |
| `area:data/web/api/etl/graph/ci` | Domain routing                |

**Example labeler rules** (`.github/labeler.yml`):

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

**Auto-label workflow** (`.github/workflows/auto-label.yml`):

```yaml
name: Auto Label
on:
  pull_request_target:
    types: [opened, synchronize]
permissions:
  contents: read
  pull-requests: write
jobs:
  label:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/labeler@v5
        with:
          repo-token: ${{ secrets.GITHUB_TOKEN }}
```

---

## ♻️ Maintenance

* **Quarterly:** Review templates for clarity; retire/add fields as needed.
* **Monthly:** Sync labels with governance (`.github/labels.yml` if used).
* **Security:** Keep `security_vuln.yml` aligned with `SECURITY.md` contacts and SLA.
* **Accessibility:** Update contrast tokens/ARIA guidance when the design system evolves.

```bash
# Optional utility
make sync-templates   # lints YAML forms, checks references, syncs defaults
```

---

## 🕓 Version History

| Version | Date       | Summary                                                                                                     |
| ------: | ---------- | ----------------------------------------------------------------------------------------------------------- |
|  v2.3.1 | 2025-10-15 | MCP-DL v6.3 alignment · quick-links section · clarified auto-label & config examples                        |
|  v2.3.0 | 2025-10-13 | Hardened forms (acceptance criteria, SemVer options, provenance & environment)                              |
|  v2.0.0 | 2025-10-10 | Versioned YAML Issue Forms · new templates (data correction, research, accessibility, security, governance) |
|  v1.1.0 | 2025-10-09 | Added MCP governance & auto-label docs                                                                      |
|  v1.0.0 | 2025-10-04 | Initial issue template documentation (bug, feature, data request)                                           |

---

<div align="center">

### 🧭 Kansas Frontier Matrix — “Clarity in Every Report. Collaboration in Every Request.”

📍 [`.github/ISSUE_TEMPLATE/`](.) · Structured, auditable issue management for KFM.

</div>
