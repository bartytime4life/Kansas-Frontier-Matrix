---
title: "🧾 Kansas Frontier Matrix — GitHub Issue Templates (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: ".github/ISSUE_TEMPLATE/README.md"
version: "v9.3.2"
last_updated: "2025-10-28"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v9.3.2/sbom.spdx.json"
manifest_ref: "../../../releases/v9.3.2/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 🧾 Kansas Frontier Matrix — **GitHub Issue Templates**
`.github/ISSUE_TEMPLATE/README.md`

**Purpose:** Standardized issue creation and governance workflows for the Kansas Frontier Matrix repository.  
These templates ensure that every issue, whether technical, data-related, or ethical, adheres to **Master Coder Protocol (MCP-DL v6.3)** and **FAIR+CARE** principles.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../../docs/architecture/repo-focus.md)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold)](../../../docs/standards/faircare-validation.md)
[![Governance Ledger](https://img.shields.io/badge/Governance-Linked-blueviolet)](../../../docs/standards/governance/)
[![Automation](https://img.shields.io/badge/Automation-GitHub%20Actions%20Integrated-cyan)](../../workflows/README.md)

</div>

---

## 📚 Overview

This directory defines all GitHub **Issue Templates** used for structured collaboration, reproducible bug tracking, data submissions, governance audits, and ethical reviews.  
Each template enforces KFM’s **FAIR+CARE-aligned reporting structure**, ensuring that issues are logged with full metadata, provenance, and compliance details.

Templates include:
- 🐛 **Bug Report** — For technical, validation, or data pipeline issues.  
- 💡 **Feature Request** — For proposing enhancements or new integrations.  
- ⚖️ **Governance Review** — For ethical, FAIR+CARE, or documentation reviews.  
- 🧭 **Data Submission** — For submitting new datasets, ETL sources, or schema updates.  

All issues automatically integrate into GitHub Actions workflows (`.github/workflows/`) for validation, tagging, and provenance logging.

---

## 🗂️ Directory Layout

```plaintext
.github/ISSUE_TEMPLATE/
├── README.md                     # This file — overview of issue template system
│
├── bug_report.yml                # Template for reporting technical issues or broken workflows
├── feature_request.yml           # Template for suggesting new enhancements or functionality
├── governance_review.yml         # Template for FAIR+CARE compliance and ethical reviews
└── data_submission.yml           # Template for new dataset ingestion or metadata registration
```

> **In summary:**  
> This directory standardizes community interaction and governance workflows for KFM’s GitHub repository, ensuring every issue aligns with ethical data principles and reproducible science.

---

## ⚙️ Issue Workflow Integration

```mermaid
flowchart TD
A[Contributor Opens Issue] --> B[Select Template Type]
B --> C[Auto-Populate Metadata Fields]
C --> D[Trigger FAIR+CARE Validation (via Actions)]
D --> E[Governance Review · Ethics / Technical Audit]
E --> F[Issue Linked to Ledger + STAC Updates]
F --> G[Close / Merge / Archive]
```

Each issue type initiates an **automated CI/CD validation chain**, guaranteeing consistency, documentation completeness, and governance traceability.

---

## 🧩 Issue Templates Summary

| Template | Purpose | Required Fields | Workflow Link |
|-----------|----------|-----------------|----------------|
| `bug_report.yml` | Report bugs in ETL, AI, or UI workflows | Steps to reproduce, environment info, logs | `.github/workflows/codeql.yml` |
| `feature_request.yml` | Propose new features, data layers, or visualization tools | Rationale, implementation plan, dependencies | `.github/workflows/site.yml` |
| `governance_review.yml` | Request ethical or FAIR+CARE board reviews | FAIR+CARE metadata, risk assessment | `.github/workflows/faircare-validate.yml` |
| `data_submission.yml` | Submit new datasets or schema changes | Source, license, spatial coverage, metadata links | `.github/workflows/stac-validate.yml` |

---

## 🧠 FAIR+CARE Governance Fields

All issue templates include the following **required governance fields**:

| Field | Description |
|--------|-------------|
| `Dataset Source` | Original dataset name or API endpoint. |
| `License / Access Rights` | Legal terms and open-access status. |
| `Ethical Review Status` | “Pending”, “Approved”, or “N/A”. |
| `Metadata File` | Linked STAC or JSON schema reference. |
| `Reviewer` | Responsible FAIR+CARE board member. |

> **Note:** The governance metadata collected through issues populates the provenance ledger (`reports/audit/ai_hazards_ledger.json`) and FAIR compliance reports (`reports/fair/`).

---

## 🧾 Governance & Provenance Integration

All issue forms automatically link to:
- `docs/standards/governance/ROOT-GOVERNANCE.md`
- `data/stac/` for metadata traceability
- `reports/audit/` for provenance chain logging
- `releases/v9.3.2/focus-telemetry.json` for Focus Mode integration

Upon issue submission, GitHub Actions:
1. Validate metadata syntax.  
2. Trigger FAIR+CARE compliance check.  
3. Generate audit logs and hash verifications.  
4. Notify relevant maintainers or governance board members.

---

## 🧩 FAIR+CARE Compliance

FAIR Principles:
- **Findable:** Issues and metadata are categorized and indexed by type and domain.  
- **Accessible:** All templates use open GitHub YAML format and require public documentation links.  
- **Interoperable:** Metadata aligns with STAC/DCAT standards.  
- **Reusable:** Issues serve as reproducible provenance records for project decisions.  

CARE Principles:
- **Collective Benefit:** Encourages open community contribution with ethical oversight.  
- **Authority to Control:** Maintains project governance via designated reviewers.  
- **Responsibility:** Ensures contributors document data sensitivity and usage ethics.  
- **Ethics:** Governance templates enforce compliance with KFM’s ethical standards.

---

## 🧾 Version History

| Version | Date       | Author             | Summary |
|----------|------------|--------------------|----------|
| v9.3.2   | 2025-10-28 | @kfm-architecture  | Added full governance metadata and workflow mapping. |
| v9.3.1   | 2025-10-27 | @bartytime4life    | Integrated FAIR+CARE compliance fields and automation triggers. |
| v9.3.0   | 2025-10-26 | @kfm-etl-ops       | Established standardized issue templates for KFM monorepo. |

---

<div align="center">

**Kansas Frontier Matrix** · *FAIR+CARE Governance × Open Collaboration × Provenance Integrity*  
[🔗 Repository](https://github.com/bartytime4life/Kansas-Frontier-Matrix) • [⚙️ Workflows](../../workflows/README.md) • [🧭 Governance Docs](../../../docs/standards/governance/)

</div>