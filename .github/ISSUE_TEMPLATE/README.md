---
title: "🧹 Kansas Frontier Matrix — Issue Templates"
document_type: "Repository Operations · Issue Forms Index"
version: "v3.0.0"
last_updated: "2025-10-20"
status: "Tier-Ω+∞ Certified · Stable"
license: ["MIT (code)", "CC-BY 4.0 (docs)"]
owners: ["@kfm-docs","@kfm-architecture","@kfm-security","@kfm-data","@kfm-web","@kfm-ai"]
template_version: "MCP-DL v6.3.2"
---

<div align="center">

# 🧹 **Kansas Frontier Matrix — Issue Templates**  
`📁 .github/ISSUE_TEMPLATE/README.md`

**Mission:** Standardize issue triage across **code, data, AI/ML, UX, and governance** — ensuring **traceable**, **reproducible**, **secure**, and **MCP-compliant** communication.

[![Docs · MCP-DL v6.3.2](https://img.shields.io/badge/Docs-MCP--DL%20v6.3.2-blue)](../../docs/)
[![Docs-Validate](https://img.shields.io/badge/docs-validated-brightgreen)](../workflows/docs-validate.yml)
[![Policy-as-Code](https://img.shields.io/badge/policy-OPA%2FConftest-purple)](../workflows/policy-check.yml)
[![Security](https://img.shields.io/badge/security-CodeQL%20%7C%20Trivy%20%7C%20Gitleaks-red)](../workflows/)
[![SBOM](https://img.shields.io/badge/SBOM-Syft%20%2B%20Grype-blue)](../workflows/sbom.yml)
[![License: MIT · CC-BY 4.0](https://img.shields.io/badge/License-MIT%20%7C%20CC--BY%204.0-green)](../../LICENSE)

</div>

---

<details><summary>📚 <strong>Table of Contents</strong></summary>

- [📘 Overview](#-overview)
- [🗂️ Directory Layout](#️-directory-layout)
- [⚡ Create a New Issue (Quick Links)](#-create-a-new-issue-quick-links)
- [✅ Core Form Fields (by Template)](#-core-form-fields-by-template)
- [🏷 Auto-Labeling & Routing](#-auto-labeling--routing)
- [⚙️ Configuration: `config.yml`](#️-configuration-configyml)
- [🧩 Reusable Snippets (Drop-ins)](#-reusable-snippets-dropins)
- [🔐 Policy-as-Code & Quality Gates](#-policy-as-code--quality-gates)
- [♻️ Maintenance Cadence](#️-maintenance-cadence)
- [📓 MCP Compliance Matrix](#-mcp-compliance-matrix)
- [🗳 Metadata & Provenance](#-metadata--provenance)
- [🕓 Version History](#-version-history)

</details>

---

## 📘 Overview
KFM uses **GitHub Issue Forms** (YAML) to collect **complete, machine-parseable** reports and requests.  
Forms enforce **provenance**, **reproducibility**, **SemVer impact**, and **ethics/security** details, and are checked by:
- **docs-validate** (format, links, metadata)  
- **OPA/Conftest** (required fields, policy)  
- **Gitleaks** (no secrets)  

> **Rule of thumb:** If an action can be automated or validated, the form *asks for it*.

---

## 🗂️ Directory Layout
```bash
.github/ISSUE_TEMPLATE/
├── README.md                    # (this file)
├── bug_report.yml               # Defects in code/data/docs
├── feature_request.yml          # New features or enhancements
├── data_request.yml             # New dataset integration
├── data_correction.yml          # Data/STAC/lineage fix
├── research_issue.yml           # Research tasks & hypotheses
├── accessibility_issue.yml      # WCAG & usability barriers
├── security_vuln.yml            # Vulnerability reports (public triage)
├── governance_question.yml      # Policy/SOP/ADR queries
└── config.yml                   # Global options & contact links
```
> When adding templates: **update `config.yml`**, ensure **labels/milestones exist**, and run `make validate`.

---

## ⚡ Create a New Issue (Quick Links)
> Base: `https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/new`

| Type | Template |
|:--|:--|
| 🐞 Bug | `?template=bug_report.yml` |
| 💡 Feature | `?template=feature_request.yml` |
| 🗃️ Data Request | `?template=data_request.yml` |
| 🧰 Data Fix | `?template=data_correction.yml` |
| 🧪 Research | `?template=research_issue.yml` |
| ♿ Accessibility | `?template=accessibility_issue.yml` |
| 🔐 Security | Use **private advisory** → `/security/advisories/new` |
| 🧭 Governance | `?template=governance_question.yml` |

---

## ✅ Core Form Fields (by Template)

| Template | Essential Fields (excerpt) |
|:--|:--|
| `bug_report` | repro steps; environment; logs; **Commit SHA**; **CI run link**; **SemVer impact**; screenshots |
| `feature_request` | user story; acceptance criteria; dependencies; migration risk; **SemVer impact** |
| `data_request` | source URL; **license**; spatial/temporal bounds; **STAC target**; **data_ethics**; ETL/validation plan |
| `data_correction` | error summary; evidence; **derived_from** updates; checksum re-gen plan; validation steps |
| `research_issue` | hypothesis; datasets; methods; success metrics; risks |
| `accessibility_issue` | barrier; **WCAG** reference; keyboard repro; assistive tech; fix proposal |
| `security_vuln` | summary (redacted); CVSS; affected versions/hashes; safe repro; mitigation; **coordinated disclosure** |
| `governance_question` | topic/policy; background; proposed change; affected SOPs/ADRs |

---

## 🏷 Auto-Labeling & Routing

**Canonical labels**

| Label | Purpose |
|:--|:--|
| `bug` | Code/data/metadata defect |
| `enhancement` | Feature or flow improvement |
| `data-request` | Propose new external dataset |
| `documentation` | Docs, SOPs, metadata |
| `security` | Vulnerabilities & fixes |
| `accessibility` | WCAG & usability |
| `semver:patch` / `semver:minor` / `semver:major` | Impact classification |
| `area:ci` / `area:data` / `area:web` / `area:etl` | Routing to SMEs |

**Example `.github/labeler.yml`**
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

**Example auto-label workflow**
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

## ⚙️ Configuration: `config.yml`
```yaml
blank_issues_enabled: false
contact_links:
  - name: 🤠 KFM Discussions
    url: https://github.com/bartytime4life/Kansas-Frontier-Matrix/discussions
    about: Ask questions, share ideas, and get help from the community.
  - name: 🗃️ Propose a New Dataset
    url: https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/new?template=data_request.yml
    about: Request adding a new open dataset (include license & provenance).
  - name: 🔐 Report a Security Issue (Private)
    url: https://github.com/bartytime4life/Kansas-Frontier-Matrix/security/advisories/new
    about: Create a private advisory to coordinate responsible disclosure.
```

---

## 🧩 Reusable Snippets (Drop-ins)

**SemVer Impact (all templates)**
```yaml
- type: dropdown
  id: semver
  attributes:
    label: SemVer Impact
    options: ["patch", "minor", "major", "unknown"]
  validations: { required: true }
```

**Provenance & Repro (bugs/data)**
```yaml
- type: input
  id: commit_sha
  attributes: { label: Commit SHA (7–40), description: Commit reproducing the issue }
  validations: { required: true }
- type: input
  id: stac_id
  attributes: { label: STAC Item/Collection ID (if applicable) }
- type: textarea
  id: repro
  attributes:
    label: Steps to Reproduce
    description: Include exact commands, inputs, and environment details.
  validations: { required: true }
```

**Data Ethics (data_request / data_correction)**
```yaml
- type: dropdown
  id: data_ethics
  attributes:
    label: Data Ethics Policy
    description: Ethical handling for sensitive/Indigenous data.
    options: ["open","restricted-derivatives","no-public-artifacts"]
  validations: { required: true }
```

**Accessibility (UI issues)**
```yaml
- type: checkboxes
  id: a11y_checks
  attributes:
    label: Accessibility checks attempted
    options:
      - { label: Keyboard-only repro }
      - { label: Screen reader repro }
      - { label: Contrast inspected (≥4.5:1) }
```

**Security (security_vuln)**
```yaml
- type: input
  id: cvss
  attributes: { label: CVSS (optional) }
- type: textarea
  id: safe_repro
  attributes:
    label: Safe Repro Steps
    description: Do not post secrets or active exploit details.
```

---

## 🔐 Policy-as-Code & Quality Gates
- **docs-validate.yml** — lint, links, metadata, and GFM checks on all templates.  
- **policy-check.yml** (OPA/Conftest) — blocks missing: SemVer impact, provenance (commit SHA), license/ethics for data.  
- **gitleaks.yml** — prevents secrets in forms.  
- **actionlint** — validates workflow changes under `.github/**`.  
- **Retention** — CI enforces logs/artifacts retention ≥ 90 days for audit.

---

## ♻️ Maintenance Cadence

| Cadence | Task |
|:--|:--|
| Weekly | Run `docs-validate` & `actionlint` on `.github/**` |
| Monthly | Sync labeler rules; audit auto-label coverage |
| Quarterly | Review templates scope & fields vs SOP/ADR updates |
| Release | Align forms with updated MCP-DL/standards; bump template version |

```bash
# Utilities (optional)
make sync-templates
```

---

## 📓 MCP Compliance Matrix

| Principle | Verified via… |
|:--|:--|
| Documentation-First | Required form sections; ADR/README links |
| Reproducibility | Repro steps, env, expected vs. actual |
| Provenance | Commit SHA, STAC IDs, `derived_from` |
| Open Standards | YAML Issue Forms, STAC, CSV/JSON |
| Auditability | Labels, lifecycle, PR cross-linking |
| Versioning | SemVer impact field on each form |
| Security | OPA gates, Gitleaks, private advisories |

---

## 🗳 Metadata & Provenance
```yaml
metadata:
  file: ".github/ISSUE_TEMPLATE/README.md"
  version: "v3.0.0"
  owners: ["@kfm-docs","@kfm-architecture","@kfm-security","@kfm-data","@kfm-web","@kfm-ai"]
  ci_required_checks: ["docs-validate","policy-check","gitleaks"]
  references:
    - "../workflows/docs-validate.yml"
    - "../workflows/policy-check.yml"
    - "../../docs/standards/markdown_rules.md"
```

---

## 🕓 Version History

| Version | Date | Author | Summary |
|:--|:--|:--|:--|
| **v3.0.0** | 2025-10-20 | @kfm-docs | Full rebuild: dropdown ToC, quick links, snippets, policy gates, MCP matrix |
| v2.6.0 | 2025-10-18 | @kfm-docs | Added data_ethics field; security links |
| v2.5.0 | 2025-10-16 | @kfm-docs | Reformat; GFM tables; CLI examples |
| v2.4.0 | 2025-10-16 | @kfm-docs | docs-validate integration; labeler docs |
| v2.3.0 | 2025-10-13 | @kfm-docs | Acceptance criteria & provenance fields |
| v2.0.0 | 2025-10-10 | @kfm-docs | Versioned YAML forms; STAC-aware templates |
| v1.0.0 | 2025-10-04 | Founding Team | Initial Issue Forms index |

---

<div align="center">

**Kansas Frontier Matrix — “Clarity in every report. Collaboration in every request.”**

</div>

<!-- MCP-FOOTER-BEGIN
MCP-VERSION: v6.3.2
MCP-TIER: Ω+∞
DOC-PATH: .github/ISSUE_TEMPLATE/README.md
DOC-HASH: sha256:issue-templates-readme-v3-0-0-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
MCP-CERTIFIED: true
VALIDATION-HASH: {auto.hash}
GENERATED-BY: KFM-Automation/DocsBot
LAST-VALIDATED: {build.date}
MCP-FOOTER-END -->