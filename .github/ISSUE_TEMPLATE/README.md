<div align="center">

# 🧩 Kansas Frontier Matrix — Issue Templates

**Path:** `.github/ISSUE_TEMPLATE/`

**Mission:** Standardize **issue reporting, feature proposals, data requests, and governance topics** to keep KFM **reproducible, auditable, versioned, and MCP-compliant**.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../LICENSE)

</div>

---

```yaml
---
title: "KFM • Issue Templates"
version: "v2.0.0"
last_updated: "2025-10-10"
owners: ["@kfm-architecture", "@kfm-data", "@kfm-security"]
maturity: "Production"
tags: ["governance","issue-forms","triage","mcp","reproducibility","provenance"]
license: "MIT"
---
```

## 📚 Overview

`.github/ISSUE_TEMPLATE/` hosts **GitHub Issue Forms** that enforce **documentation-first**, **provenance-linked**, and **reproducibility-driven** reporting across code, data, docs, and research. Templates capture the **who/what/where/when/how** so every issue remains traceable from report → resolution → validation.

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

> **Why YAML forms?** They provide **required fields**, **labels**, **assignments**, and **structured metadata** directly in the GitHub UI.

---

## 🧾 Template Summaries

### 🐞 `bug_report.yml`

| Field                  | Purpose                                               |
| ---------------------- | ----------------------------------------------------- |
| **Summary**            | Concise description of the bug.                       |
| **Steps to Reproduce** | Deterministic steps + minimal inputs.                 |
| **Expected vs Actual** | Clarify discrepancy.                                  |
| **System Context**     | OS, Python/Node versions, workflow run IDs.           |
| **Related Workflow**   | Link to CI job URL or pipeline module.                |
| **Logs / Screenshots** | Attach evidence.                                      |
| **Proposed Fix**       | Optional suggestion or quick patch.                   |
| **Provenance**         | Affected paths, dataset IDs, STAC items, commit SHAs. |

### 💡 `feature_request.yml`

| Field                     | Purpose                                 |
| ------------------------- | --------------------------------------- |
| **Motivation / Use Case** | Problem statement & stakeholders.       |
| **Proposed Solution**     | Functional sketch + UX notes.           |
| **Alternatives**          | Solutions considered/rejected.          |
| **Dependencies**          | Tools, APIs, data, permissions.         |
| **Impact**                | Expected effects on ETL, graph, UI, CI. |
| **Acceptance Criteria**   | Testable completion definition.         |

### 🗃️ `data_request.yml`

| Field                  | Purpose                                 |
| ---------------------- | --------------------------------------- |
| **Dataset Name**       | Human-readable title.                   |
| **Source / URL**       | API, portal, or archive link.           |
| **License**            | Terms (Public domain, CC-BY-4.0, etc.). |
| **Temporal / Spatial** | Time range + bbox/CRS.                  |
| **Data Type**          | Raster, vector, tabular, text, mixed.   |
| **Provenance**         | Citation, lineage, and quality notes.   |
| **Integration Target** | ETL pipeline & STAC collection.         |

### 🧰 `data_correction.yml`

| Field                 | Purpose                                       |
| --------------------- | --------------------------------------------- |
| **Issue Description** | What’s wrong in current data/metadata.        |
| **Evidence**          | Documentation, alternate source, or QA plots. |
| **Scope**             | Items/Collections affected + version fields.  |
| **Fix Proposal**      | How to correct + validation steps.            |

### 🧪 `research_issue.yml`

| Field                     | Purpose                            |
| ------------------------- | ---------------------------------- |
| **Hypothesis / Question** | Research framing.                  |
| **Data / Methods**        | Datasets, models, SOPs, ADR links. |
| **Expected Outcome**      | Metrics, figures, or narrative.    |
| **Risks / Limitations**   | Data gaps, bias, thresholds.       |

### ♿ `accessibility_issue.yml`

| Field              | Purpose                                      |
| ------------------ | -------------------------------------------- |
| **Barrier**        | Description + affected user(s).              |
| **WCAG Ref**       | Guideline & level (e.g., 2.1 AA 1.4.3).      |
| **Repro Steps**    | Keyboard, reader, contrast evidence.         |
| **Fix Suggestion** | ARIA roles/labels, color tokens, focus mgmt. |

### 🔒 `security_vuln.yml`

| Field                 | Purpose                                        |
| --------------------- | ---------------------------------------------- |
| **Summary**           | High-level vuln description (no secrets).      |
| **Impact**            | Potential risk/severity (CVSS if known).       |
| **Repro (sanitized)** | Safe steps/logs without sensitive data.        |
| **Environment**       | Versions, image hashes, Actions refs.          |
| **Disclosure**        | Contact for private details (see SECURITY.md). |

### 🧭 `governance_question.yml`

| Field        | Purpose                              |
| ------------ | ------------------------------------ |
| **Topic**    | Process/roles/reviews/branch policy. |
| **Context**  | Where confusion arose.               |
| **Proposal** | Suggested governance tweak.          |

---

## ⚙️ Issue Forms Configuration (`config.yml`)

```yaml
blank_issues_enabled: false
contact_links:
  - name: 🧠 KFM Discussions
    url: https://github.com/bartytime4life/Kansas-Frontier-Matrix/discussions
    about: For open questions, ideation, and design dialogue.
  - name: 📬 Data Contribution Requests
    url: https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/new?template=data_request.yml
    about: Propose new datasets or integrations.

# Defaults
issue_template:
  - name: Bug Report
    about: Report a defect in code/data/metadata
    labels: ["bug","needs-triage"]
    assignees: ["@kfm-architecture"]
    body: []
```

> **Auto-Labeling:** Pair with a simple workflow (e.g., `.github/workflows/auto-label.yml`) that adds domain labels (e.g., `area:data`, `area:web`) based on file changes.

---

## 🧠 MCP & Governance Alignment

| MCP Principle           | Implementation                                                              |
| ----------------------- | --------------------------------------------------------------------------- |
| **Documentation-First** | Required fields capture story, context, and rationale.                      |
| **Reproducibility**     | Steps, environment, expected/actual results mandated.                       |
| **Open Standards**      | Markdown + YAML Issue Forms; STAC links for dataset issues.                 |
| **Provenance**          | Commit SHAs, STAC items, dataset IDs required.                              |
| **Auditability**        | Lifecycle tracked; cross-linked to PRs and workflow runs.                   |
| **Versioning**          | Issues ask for **SemVer impact** and **STAC `properties.version`** changes. |

---

## 🧱 Contributor Workflow

1. **Choose Template** — Bug, Feature, Data Request, Data Correction, Research, Accessibility, Security, Governance.
2. **Fill Required Fields** — Provide reproducible steps, provenance links, and impact.
3. **Submit** — Templates auto-label (`bug`, `enhancement`, `data-request`, etc.).
4. **Triage** — Maintainers assign reviewers, add `priority:` and `area:` labels, and set milestone.
5. **Resolve** — Link to PR(s), validate in CI, close with summary + references.

---

## 🏷️ Labels & Automation

**Auto-labels** via `auto-label.yml` (or Dependabot defaults):

| Label                            | Purpose                            |
| -------------------------------- | ---------------------------------- |
| `bug`                            | Defects in code/data/docs.         |
| `enhancement`                    | New features or improvements.      |
| `data-request`                   | New dataset/integration proposals. |
| `documentation`                  | Docs and governance updates.       |
| `security`                       | Vulnerability & hardening.         |
| `accessibility`                  | UI/UX compliance issues.           |
| `needs-triage`                   | Awaiting maintainer review.        |
| `priority:p0/p1/p2`              | Urgency levels.                    |
| `semver:patch/minor/major`       | Proposed version impact.           |
| `area:data/web/api/etl/graph/ci` | Domain routing.                    |

---

## 🧰 Example: Issue Form (Bug)

```yaml
name: "🐞 Bug Report"
description: "Report a defect in code, data, or metadata"
labels: ["bug","needs-triage"]
assignees: ["@kfm-architecture"]
body:
  - type: textarea
    id: summary
    attributes: { label: "Summary", placeholder: "What happened?" }
    validations: { required: true }
  - type: textarea
    id: steps
    attributes:
      label: "Steps to Reproduce"
      description: "Include deterministic steps and minimal inputs"
      placeholder: |
        1) …
        2) …
        3) …
    validations: { required: true }
  - type: input
    id: expected
    attributes: { label: "Expected Result" }
    validations: { required: true }
  - type: input
    id: actual
    attributes: { label: "Actual Result" }
    validations: { required: true }
  - type: input
    id: context
    attributes:
      label: "System Context"
      description: "OS, Python/Node, workflow run URL, container/image hash"
  - type: textarea
    id: provenance
    attributes:
      label: "Provenance"
      description: "Paths, STAC items, dataset IDs, commit SHA(s)"
    validations: { required: true }
  - type: textarea
    id: logs
    attributes: { label: "Logs / Screenshots" }
  - type: dropdown
    id: semver
    attributes:
      label: "SemVer Impact"
      options: ["none","patch","minor","major"]
      default: 0
```

> Use similar YAML for other templates; keep **required** fields for reproducibility & provenance.

---

## 🔧 Triage & Automation Hooks

* **Auto-Label**: map changed paths to `area:*` labels (e.g., `data/**` → `area:data`).
* **Project Assignment**: workflow assigns issues to project board columns (e.g., *Triage*, *In Progress*, *Done*).
* **Stale Bot (optional)**: mark inactive issues with `status:stale` after N days; auto-close after grace period.
* **Discussion Converter**: convert general questions to Discussions.

---

## ♻️ Maintenance

* **Quarterly**: Review templates for clarity & add/remove fields as needed.
* **Monthly**: Sync labels with governance (`.github/labels.yml` if used).
* **Security**: Keep `security_vuln.yml` aligned with `SECURITY.md` contacts and SLA.
* **Accessibility**: Update contrast tokens/ARIA guidance if design system evolves.

```bash
# Optional utility
make sync-templates   # lints YAML forms, checks references, syncs defaults
```

---

## 🕓 Version History

| Version | Date       | Summary                                                                                                                                                  |
| ------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| v2.0.0  | 2025-10-10 | Added **versioned** YAML Issue Forms, new templates (data correction, research, accessibility, security, governance), SemVer impact & provenance fields. |
| v1.1.0  | 2025-10-09 | Added MCP governance & auto-label docs.                                                                                                                  |
| v1.0.0  | 2025-10-04 | Initial issue template documentation (bug, feature, data request).                                                                                       |

---

<div align="center">

### 🧭 Kansas Frontier Matrix — “Clarity in Every Report. Collaboration in Every Request.”

📍 [`.github/ISSUE_TEMPLATE/`](.) · Structured, auditable issue management for KFM.

</div>
