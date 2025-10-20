---
title: "🧹 Kansas Frontier Matrix — Issue Templates"
document_type: "Repository Operations · Issue Forms Index"
version: "v3.1.0"
last_updated: "2025-10-20"
status: "Tier-Ω+∞ Certified · Production"
maturity: "Production"
license: ["MIT (code)", "CC-BY 4.0 (docs)"]
owners: ["@kfm-docs","@kfm-architecture","@kfm-security","@kfm-data","@kfm-web","@kfm-ai"]
template_version: "MCP-DL v6.3.2"
alignment:
  - MCP-DL v6.3.2
  - STAC 1.0 / DCAT 2.0
  - WCAG 2.1 AA
ci_required_checks:
  - docs-validate
  - policy-check
  - gitleaks
  - actionlint
---

<div align="center">

# 🧹 **Kansas Frontier Matrix — Issue Templates (v3.1.0 · Tier-Ω+∞ Certified)**  
`📁 .github/ISSUE_TEMPLATE/README.md`

**Mission:** Standardize issue triage across **code, data, AI/ML, UX, and governance** — ensuring every report is **traceable**, **reproducible**, **secure**, and **MCP-compliant**.  
All forms are validated via **docs-validate**, **OPA policy gates**, and **security scans**.

[![Docs · MCP-DL v6.3.2](https://img.shields.io/badge/Docs-MCP--DL%20v6.3.2-blue)](../../docs/)
[![Docs-Validate](https://img.shields.io/badge/docs-validated-brightgreen)](../workflows/docs-validate.yml)
[![Policy-as-Code](https://img.shields.io/badge/policy-OPA%2FConftest-purple)](../workflows/policy-check.yml)
[![Security](https://img.shields.io/badge/security-CodeQL%20%7C%20Trivy%20%7C%20Gitleaks-red)](../workflows/)
[![SBOM](https://img.shields.io/badge/SBOM-Syft%20%2B%20Grype-blue)](../workflows/sbom.yml)
[![License: MIT · CC-BY 4.0](https://img.shields.io/badge/License-MIT%20%7C%20CC--BY%204.0-green)](../../LICENSE)

</div>

---

<details><summary>📚 <strong>Table of Contents</strong></summary>

- [📘 Context & Scope](#-context--scope)
- [🗂️ Directory Layout](#️-directory-layout)
- [⚡ Create a New Issue (Quick Links)](#-create-a-new-issue-quick-links)
- [✅ Core Form Fields (by Template)](#-core-form-fields-by-template)
- [🏷 Auto-Labeling & Routing](#-auto-labeling--routing)
- [⚙️ Configuration: `config.yml`](#️-configuration-configyml)
- [🧩 Reusable Snippets (Drop-ins)](#-reusable-snippets-drop-ins)
- [🔐 Policy-as-Code & Quality Gates](#-policy-as-code--quality-gates)
- [📦 Artifacts & Evidence Registry](#-artifacts--evidence-registry)
- [📊 Governance Telemetry Snapshot](#-governance-telemetry-snapshot)
- [📜 Linked ADRs & SOPs](#-linked-adrs--sops)
- [♻️ Maintenance Cadence](#️-maintenance-cadence)
- [📓 MCP Compliance Matrix](#-mcp-compliance-matrix)
- [🧾 Change-Control Register](#-change-control-register)
- [📣 Contributor Quick-Links](#-contributor-quick-links)
- [🗳 Metadata & Provenance](#-metadata--provenance)
- [🕓 Version History](#-version-history)

</details>

---

## 📘 Context & Scope
This directory contains all **GitHub Issue Forms** used by the **Kansas Frontier Matrix (KFM)** project.  
Every form must:
- Capture **SemVer impact**, **provenance**, and **data ethics**.
- Automatically label and route issues to the correct domain owners.
- Validate through `docs-validate.yml`, `policy-check.yml`, and `gitleaks.yml`.  

This README is the **canonical manifest** linking templates, config, and automation for reproducible triage.

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
| Template | Essential Fields |
|:--|:--|
| `bug_report` | repro steps, env, logs, **Commit SHA**, **CI run link**, **SemVer impact** |
| `feature_request` | story, acceptance criteria, migration risk, **SemVer impact** |
| `data_request` | source link, **license**, bounds, **STAC target**, **data_ethics**, ETL plan |
| `data_correction` | evidence, **derived_from**, checksum plan, validation steps |
| `research_issue` | hypothesis, dataset, metrics |
| `accessibility_issue` | barrier, **WCAG**, repro, assistive tech, fix |
| `security_vuln` | summary (redacted), CVSS, hashes, repro (safe), mitigation |
| `governance_question` | topic, policy background, SOPs/ADRs affected |

---

## 🏷 Auto-Labeling & Routing
**Standard labels**
| Label | Purpose |
|:--|:--|
| `bug` | Code/data defect |
| `enhancement` | Feature request |
| `data-request` | New dataset |
| `documentation` | Docs or SOP edits |
| `security` | Vulnerability |
| `accessibility` | A11y issue |
| `semver:*` | Impact classification |
| `area:*` | SME domain route |

**Labeler snippet**
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

---

## ⚙️ Configuration: `config.yml`
```yaml
blank_issues_enabled: false
contact_links:
  - name: 🤠 KFM Discussions
    url: https://github.com/bartytime4life/Kansas-Frontier-Matrix/discussions
    about: Ask questions, share ideas, or request support.
  - name: 🗃️ New Dataset Proposal
    url: https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/new?template=data_request.yml
    about: Propose a new dataset for inclusion in KFM.
  - name: 🔐 Private Security Report
    url: https://github.com/bartytime4life/Kansas-Frontier-Matrix/security/advisories/new
    about: Create a private advisory for responsible disclosure.
```

---

## 🧩 Reusable Snippets (Drop-ins)
**SemVer Impact**
```yaml
- type: dropdown
  id: semver
  attributes: { label: SemVer Impact, options: ["patch","minor","major","unknown"] }
  validations: { required: true }
```

**Provenance & Repro**
```yaml
- type: input
  id: commit_sha
  attributes: { label: Commit SHA (7–40) }
  validations: { required: true }
- type: textarea
  id: repro
  attributes:
    label: Steps to Reproduce
    description: Include exact commands, inputs, and environment.
```

**Data Ethics**
```yaml
- type: dropdown
  id: data_ethics
  attributes:
    label: Data Ethics Policy
    options: ["open","restricted-derivatives","no-public-artifacts"]
  validations: { required: true }
```

**Accessibility**
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

---

## 🔐 Policy-as-Code & Quality Gates
- **docs-validate.yml** → Markdown lint, metadata, and GFM schema validation.  
- **policy-check.yml** → OPA/Conftest rules enforcing SemVer + provenance + ethics fields.  
- **gitleaks.yml** → Secret scanning for YAML/Markdown changes.  
- **actionlint** → Ensures valid YAML under `.github/**`.  
- **Retention** → All validation artifacts/logs retained ≥ 90 days for audit.

---

## 📦 Artifacts & Evidence Registry
| Artifact | Source | Purpose | Retention |
|:--|:--|:--|:--|
| `docs-validate-report.json` | `docs-validate.yml` | Form validation report | 90d |
| `policy-check.log` | `policy-check.yml` | OPA/Conftest audit results | 90d |
| `.prov.json` | sbom/slsa workflows | Provenance of template edits | Permanent |
| `labels-report.json` | optional | Label coverage metrics | 30d |

---

## 📊 Governance Telemetry Snapshot
> ![Governance Dashboard](https://metrics.kfm.ai/img/issues-dashboard-snapshot.png)  
> _Live metrics of issue form validation and label routing health._

---

## 📜 Linked ADRs & SOPs
| Document | Purpose | Status |
|:--|:--|:--|
| `docs/adr/ADR-015-issue-template-governance.md` | Defines template structure & required fields | ✅ |
| `docs/sop/issue-triage.md` | Issue triage & routing workflow | ✅ |
| `docs/sop/data-request-process.md` | Dataset submission procedure | ✅ |

---

## ♻️ Maintenance Cadence
| Cadence | Task |
|:--|:--|
| Weekly | Run `docs-validate` & `actionlint` |
| Monthly | Sync labeler rules; verify auto-label coverage |
| Quarterly | Review template fields vs SOP/ADR updates |
| Release | Align with new MCP version; bump template revision |

---

## 📓 MCP Compliance Matrix
| Principle | Verified via |
|:--|:--|
| Documentation-First | ADR links + required sections |
| Reproducibility | Steps, env, expected vs actual |
| Provenance | Commit SHA + STAC IDs |
| Open Standards | YAML + STAC + JSON Schema |
| Auditability | Labels + PR linking |
| Versioning | SemVer field |
| Security | Policy gates + secret scan |

---

## 🧾 Change-Control Register
```yaml
changes:
  - date: "2025-10-20"
    change: "Rebuilt Issue Template index — added context, telemetry, ADR links, evidence registry"
    reviewed_by: "@kfm-docs"
    pr: "#416"
```

---

## 📣 Contributor Quick-Links
- 🗂 [Open Issues](../../issues)
- 🧩 [New Issue Templates](../../issues/new/choose)
- 🚀 [Project Board](../../projects)
- 📘 [Contributing Guide](../../CONTRIBUTING.md)

---

## 🗳 Metadata & Provenance
```yaml
metadata:
  file: ".github/ISSUE_TEMPLATE/README.md"
  version: "v3.1.0"
  maintainers: ["@kfm-docs","@kfm-architecture","@kfm-security"]
  maturity: "Production"
  ci_required_checks: ["docs-validate","policy-check","gitleaks","actionlint"]
  references:
    - "../workflows/docs-validate.yml"
    - "../workflows/policy-check.yml"
    - "../../docs/standards/markdown_rules.md"
```

---

## 🕓 Version History
| Version | Date | Author | Summary |
|:--|:--|:--|:--|
| **v3.1.0** | 2025-10-20 | @kfm-docs | Added context, evidence registry, telemetry, ADR linkage, and change log |
| v3.0.0 | 2025-10-20 | @kfm-docs | Full rebuild with dropdown ToC and policy gates |
| v2.6.0 | 2025-10-18 | @kfm-docs | Added `data_ethics` field & security links |
| v2.5.0 | 2025-10-16 | @kfm-docs | Reformatted to GFM; added CLI helpers |
| v2.4.0 | 2025-10-16 | @kfm-docs | Added docs-validate integration |
| v2.0.0 | 2025-10-10 | @kfm-docs | Versioned YAML forms + STAC support |
| v1.0.0 | 2025-10-04 | Founding Team | Initial issue template README |

---

<div align="center">

**Kansas Frontier Matrix — “Clarity in Every Report · Collaboration in Every Request.”**

</div>

<!-- MCP-FOOTER-BEGIN
MCP-VERSION: v6.3.2
MCP-TIER: Ω+∞
DOC-PATH: .github/ISSUE_TEMPLATE/README.md
DOC-HASH: sha256:issue-templates-readme-v3-1-0-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
MCP-CERTIFIED: true
AUTO-DOC: true
VALIDATION-HASH: {auto.hash}
GENERATED-BY: KFM-Automation/DocsBot
LAST-VALIDATED: {build.date}
MCP-FOOTER-END -->