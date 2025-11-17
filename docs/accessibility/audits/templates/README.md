---
title: "📑 Kansas Frontier Matrix — Accessibility Audit Templates & Checklists (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/accessibility/audits/templates/README.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/a11y-audit-templates-v2.json"
governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Standard"
intent: "accessibility-audit-templates"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 📑 **Kansas Frontier Matrix — Accessibility Audit Templates & Checklists**  
`docs/accessibility/audits/templates/README.md`

**Purpose:**  
Provide reusable **templates and standardized checklists** for performing accessibility audits in the **Kansas Frontier Matrix (KFM)** — ensuring reproducibility, FAIR+CARE alignment, and compliance with **WCAG 2.1 AA**, **WAI-ARIA 1.2**, and **ISO 9241-210** under **MCP-DL v6.3**.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../README.md)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../../standards/faircare.md)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)  
[![Status: Active](https://img.shields.io/badge/Status-Active-success)](../../../../releases/v10.4.0/manifest.zip)

</div>

---

## 📘 Overview

This directory contains the **official templates** for manual and automated accessibility audits governed by the **FAIR+CARE Council** and the **Master Coder Protocol (MCP)**.

Templates are designed to guarantee:

- Consistent audit data capture across teams and cycles  
- Explicit mapping to **WCAG 2.1 AA** success criteria  
- Embedded **CARE**-aligned ethics review fields  
- Compatible export to CI and telemetry (`accessibility_scan.yml`, `faircare-audit.yml`)  
- Traceability and provenance for all audits in the Governance Ledger

---

## 🗂️ Directory Layout

~~~text
docs/accessibility/audits/templates/
├── README.md
├── audit-template.md
├── checklist-wcag2.1aa.md
├── ethics-review-template.md
└── summary-template.json
~~~

| Template File | Purpose | Use Cycle |
|---|---|---|
| `README.md` | Describes all audit templates and governance requirements | Reference |
| `audit-template.md` | Manual audit form for documenting environment, scope, and findings | Each quarterly cycle |
| `checklist-wcag2.1aa.md` | Human-readable WCAG 2.1 AA checklist by success criterion | Continuous reference |
| `ethics-review-template.md` | CARE-aligned tone, representation, and narrative ethics review | Biannual FAIR+CARE review |
| `summary-template.json` | Machine-readable summary for pipelines and telemetry | After each audit run |

---

## 📋 Required Metadata Fields (All Templates)

| Field | Description | Example |
|---|---|---|
| `audit_id` | Unique audit identifier | `A11Y-2025-Q2-001` |
| `auditor` | Responsible reviewer or team | `A. Barta / FAIR+CARE Council` |
| `date` | Audit execution date (ISO 8601) | `2025-06-15` |
| `toolset` | Tool versions used | `Lighthouse 11.2, axe-core 4.8, NVDA 2025.1` |
| `scope` | App section or component(s) tested | `FocusPanel / MapView` |
| `wcag_score` | WCAG 2.1 AA pass percentage | `97.5` |
| `faircare_score` | Ethical compliance result | `PASS` / `NEEDS_REVIEW` |
| `issues_found` | Count & severity summary | `3 minor contrast issues, 1 ARIA landmark missing` |
| `actions_required` | Follow-up remediation plan | `Update tokens; add aria-labels to nav` |

These fields must appear in all completed audit reports and JSON summaries.

---

## 🧩 Example — Manual Audit Template (Markdown)

~~~markdown
# Accessibility Audit — Q2 2025

**Audit ID:** A11Y-2025-Q2-001  
**Date:** 2025-06-15  
**Auditor:** J. Barta (FAIR+CARE Council)  
**Scope:** MapView / FocusPanel interactions  
**Tools:** Lighthouse 11.2, axe-core 4.8, NVDA 2025.1  

## WCAG 2.1 AA Findings

| Criterion | Status | Notes |
|---|---|---|
| 1.1.1 Non-text Content | ✅ | All icons have `aria-label`. |
| 1.4.3 Contrast Minimum | ⚠️ | Buttons in dark mode need improved contrast. |
| 2.1.1 Keyboard | ✅ | All interactive elements operable via keyboard. |
| 4.1.2 Name, Role, Value | ✅ | Proper ARIA roles implemented. |

## CARE Principles Review

| Principle | Pass | Notes |
|---|---|---|
| Collective Benefit | ✅ | UI usable across devices and assistive tools. |
| Authority to Control | ✅ | Consent dialogs accessible and respectful. |
| Responsibility | ✅ | Previous issues resolved in this cycle. |
| Ethics | ⚠️ | Narrative tone flagged (term "primitive" in AI summary). |

**Action Items**

1. Adjust color tokens for button contrast.  
2. Replace flagged terminology with neutral equivalents.  
3. Retest after patch deployment.

**Final Score**  
WCAG Compliance: **97%** · FAIR+CARE Review: **PASS**
~~~

---

## ⚙️ JSON Summary Template (Automation Example)

~~~json
{
  "audit_id": "A11Y-2025-Q2-001",
  "date": "2025-06-15",
  "auditor": "FAIR+CARE Council",
  "scope": ["MapView", "FocusPanel"],
  "results": {
    "wcag_score": 97.5,
    "faircare_score": "PASS",
    "issues_found": 4,
    "critical_issues": 0,
    "warnings": 1
  },
  "artifacts": {
    "report_file": "docs/accessibility/audits/2025-Q2_a11y_report.json",
    "ci_summary": "reports/self-validation/web/a11y_summary.json"
  }
}
~~~

This structure is enforced by `telemetry_schema` and used by CI and dashboards.

---

## ⚖️ FAIR+CARE Integration

| CARE Principle | Template Representation |
|---|---|
| **Collective Benefit** | Section ensures documented benefits and user impact of fixes |
| **Authority to Control** | Fields for consent and cultural data handling policies |
| **Responsibility** | Auditor declaration and regression tracking references |
| **Ethics** | Narrative tone and representation review section in `ethics-review-template.md` |

Templates must be completed in full for any audit to be considered valid.

---

## 📊 CI/CD Integration

The following workflows consume or validate audit templates:

| Workflow | Purpose | Output |
|---|---|---|
| `accessibility_scan.yml` | Merges automated scan results into manual reports | `reports/self-validation/web/a11y_summary.json` |
| `faircare-audit.yml` | Verifies CARE fields and ethics checks are completed | `reports/faircare-validation.json` |
| `release-audit-export.yml` | Bundles quarterly audits into release artifacts | `releases/v10.4.0/faircare-report.md` |

Templates must remain backward-compatible with these workflows.

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.4.0 | 2025-11-17 | A11y & FAIR+CARE Council | Upgraded to KFM-MDP v10.4; updated telemetry schema; replaced inner backtick fences with tildes to prevent box-breaking issues |
| v10.0.0 | 2025-11-10 | A11y & FAIR+CARE Council | Established unified audit templates and JSON schema for reproducible governance and automation |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Created under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Accessibility Audits](../README.md) • [Checklist →](checklist-wcag2.1aa.md)

</div>