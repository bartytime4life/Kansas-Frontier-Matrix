---
title: "📑 Kansas Frontier Matrix — Accessibility Audit Templates & Checklists (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed, reusable templates and checklists for KFM accessibility audits, ensuring reproducibility, FAIR+CARE alignment, and WCAG 2.1 AA compliance."
path: "docs/accessibility/audits/templates/README.md"
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Accessibility Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x a11y-template-compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.3/a11y-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/a11y-audit-templates-v2.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Standard"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "accessibility"
  applies_to:
    - "accessibility-audits"
    - "focus-mode-a11y"
    - "story-node-a11y"
    - "docs-and-pdfs"
    - "a11y-telemetry"

semantic_intent:
  - "standard"
  - "governance"
  - "quality-assurance"
category: "Documentation · Standard · Accessibility"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: false

data_steward: "FAIR+CARE Accessibility Council"
ttl_policy: "24 months"
sunset_policy: "Supersedes v10.4.0 accessibility audit templates standard"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/accessibility/audits/templates/README.md@v10.4.0"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/docs-accessibility-audit-templates-v11.2.3.schema.json"
shape_schema_ref: "schemas/shacl/docs-accessibility-audit-templates-v11.2.3-shape.ttl"
story_node_refs: []

immutability_status: "mutable"

doc_uuid: "urn:kfm:doc:accessibility:audit-templates:v11.2.3"
semantic_document_id: "kfm-accessibility-audit-templates-standard-v11.2.3"
event_source_id: "ledger:kfm:doc:accessibility:audit-templates:v11.2.3"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "footer-check"
  - "accessibility-check"
  - "diagram-check"
  - "metadata-check"
  - "provenance-check"
---

<div align="center">

# 📑 Kansas Frontier Matrix — Accessibility Audit Templates & Checklists  

`docs/accessibility/audits/templates/README.md`

**Purpose:**  
Provide reusable **templates and standardized checklists** for performing accessibility audits in the **Kansas Frontier Matrix (KFM)** — ensuring reproducibility, FAIR+CARE alignment, and compliance with **WCAG 2.1 AA**, **WAI-ARIA 1.2**, and **ISO 9241-210** under **MCP-DL v6.3**.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../../README.md) ·
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE) ·
[![Status: Active](https://img.shields.io/badge/Status-Active-success)](../../../../releases/v11.2.3/manifest.zip)

</div>

---

## 📘 1. Overview

This directory contains the **official templates** for manual and automated accessibility audits governed by the **FAIR+CARE Accessibility Council** and the **Master Coder Protocol (MCP)**.

Templates are designed to guarantee:

- Consistent audit data capture across teams and cycles.  
- Explicit mapping to **WCAG 2.1 AA** success criteria.  
- Embedded **CARE**-aligned ethics review fields.  
- Compatible export to CI and telemetry (`accessibility_scan.yml`, `faircare-audit.yml`).  
- Traceability and provenance for all audits in the Governance Ledger.

This standard defines the **shape and required fields** for all template files under `docs/accessibility/audits/templates/`.

---

## 🗂️ 2. Directory Layout

~~~text
docs/accessibility/audits/templates/
├── 📄 README.md                    # This file (template governance)
├── 📄 audit-template.md            # Manual audit form (env, scope, findings)
├── 📄 checklist-wcag2.1aa.md       # Human-readable WCAG 2.1 AA checklist
├── 📄 ethics-review-template.md    # CARE-aligned narrative ethics review form
└── 📄 summary-template.json        # Machine-readable audit summary schema
~~~

| Template File            | Purpose                                                    | Use Cycle                    |
|--------------------------|------------------------------------------------------------|------------------------------|
| `README.md`              | Describes all audit templates and governance requirements. | Reference                    |
| `audit-template.md`      | Manual audit form for environment, scope, and findings.    | Each quarterly cycle         |
| `checklist-wcag2.1aa.md` | WCAG 2.1 AA checklist by success criterion.                | Continuous reference         |
| `ethics-review-template.md` | CARE-aligned tone, representation, and narrative ethics review. | Biannual FAIR+CARE review |
| `summary-template.json`  | Machine-readable summary for pipelines and telemetry.      | After each audit run         |

All new templates in this directory MUST:

- Declare required metadata fields (see section 3).  
- Remain backward-compatible with `telemetry_schema`.  
- Be validated under **KFM-MDP v11.2.2** and associated schema checks.

---

## 📋 3. Required Metadata Fields (All Templates)

The following logical fields MUST be present (either as front-matter, header block, or JSON keys) in all completed audit artifacts derived from these templates:

| Field             | Description                                | Example                                              |
|-------------------|--------------------------------------------|------------------------------------------------------|
| `audit_id`        | Unique audit identifier                    | `A11Y-2025-Q2-001`                                   |
| `auditor`         | Responsible reviewer or team               | `A. Barta / FAIR+CARE Council`                       |
| `date`            | Audit execution date (ISO 8601)            | `2025-06-15`                                         |
| `toolset`         | Tool names and versions used               | `Lighthouse 11.2, axe-core 4.8, NVDA 2025.1`         |
| `scope`           | App section(s) or component(s) tested      | `FocusPanel / MapView`                               |
| `wcag_score`      | WCAG 2.1 AA pass percentage (0–100)        | `97.5`                                               |
| `faircare_score`  | Ethical compliance result                  | `PASS` / `NEEDS_REVIEW`                              |
| `issues_found`    | Count & severity summary                   | `3 minor contrast issues, 1 ARIA landmark missing`   |
| `actions_required`| Planned remediation actions                | `Update tokens; add aria-labels to nav`              |

When serialized to JSON using `summary-template.json`, these fields MUST map cleanly to the schema defined by `telemetry_schema`.

---

## 🧩 4. Example — Manual Audit Template (Markdown)

~~~markdown
# Accessibility Audit — Q2 2025

**Audit ID:** A11Y-2025-Q2-001  
**Date:** 2025-06-15  
**Auditor:** J. Barta (FAIR+CARE Council)  
**Scope:** MapView / FocusPanel interactions  
**Tools:** Lighthouse 11.2, axe-core 4.8, NVDA 2025.1  

## WCAG 2.1 AA Findings

| Criterion                  | Status | Notes                                         |
|---------------------------|--------|-----------------------------------------------|
| 1.1.1 Non-text Content    | ✅     | All icons have `aria-label`.                  |
| 1.4.3 Contrast Minimum    | ⚠️     | Buttons in dark mode need improved contrast.  |
| 2.1.1 Keyboard            | ✅     | All interactive elements operable by keyboard.|
| 4.1.2 Name, Role, Value   | ✅     | Proper ARIA roles implemented.                |

## CARE Principles Review

| Principle          | Pass | Notes                                                      |
|--------------------|------|------------------------------------------------------------|
| Collective Benefit | ✅   | UI usable across devices and assistive tools.             |
| Authority to Control | ✅ | Consent dialogs accessible and respectful.                |
| Responsibility     | ✅   | Previous issues resolved this cycle.                      |
| Ethics             | ⚠️   | Narrative tone flagged (term "primitive" in AI summary).  |

## Action Items

1. Adjust color tokens for button contrast.  
2. Replace flagged terminology with neutral equivalents.  
3. Retest after patch deployment.

**Final Score**  
WCAG Compliance: **97%** · FAIR+CARE Review: **PASS**
~~~

Templates like this MUST:

- Preserve headings and table structure for machine extraction.  
- Align field names with the JSON summary schema wherever practical.

---

## ⚙️ 5. JSON Summary Template (Automation Example)

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

This structure is enforced by `telemetry_schema` and consumed by:

- CI workflows (`accessibility_scan.yml`, `faircare-audit.yml`).  
- A11y dashboards and governance reports.  
- Provenance/lineage ingestion into the Governance Ledger.

---

## ⚖️ 6. FAIR+CARE Integration

| CARE Principle       | Template Representation                                                  |
|----------------------|-------------------------------------------------------------------------|
| **Collective Benefit**  | Sections capturing user impact and benefits of fixes.               |
| **Authority to Control**| Fields for consent, cultural data handling, and data sovereignty.   |
| **Responsibility**      | Auditor identity, regression references, and remediation status.    |
| **Ethics**              | Narrative tone, imagery, and representation review sections in `ethics-review-template.md`. |

For any audit to be considered **valid**, its completed templates MUST:

- Include CARE-related sections.  
- Document any ethical concerns and remediation actions.  

---

## 📊 7. CI/CD Integration

The following workflows consume or validate audit templates and their outputs:

| Workflow                  | Purpose                                            | Output Artifact                                  |
|---------------------------|----------------------------------------------------|--------------------------------------------------|
| `accessibility_scan.yml`  | Merges automated scan results into manual reports. | `reports/self-validation/web/a11y_summary.json`  |
| `faircare-audit.yml`      | Verifies CARE fields and ethics checks completeness.| `reports/faircare-validation.json`              |
| `release-audit-export.yml`| Bundles quarterly audits into release artifacts.   | `releases/<version>/faircare-report.md`         |

Template changes MUST remain compatible with these workflows and the schemas they rely on.

---

## 🕰️ 8. Version History

| Version  | Date       | Author                    | Summary                                                                                       |
|----------|------------|---------------------------|-----------------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-02 | A11y & FAIR+CARE Council  | Upgraded to KFM-MDP v11.2.2; added governance metadata; aligned telemetry and CI integration.|
| v10.4.0  | 2025-11-17 | A11y & FAIR+CARE Council  | Updated telemetry schema; replaced inner backtick fences with tildes to prevent box-breaking.|
| v10.0.0  | 2025-11-10 | A11y & FAIR+CARE Council  | Established unified audit templates and JSON schema for reproducible governance and automation.|

---

<div align="center">

📑 **Kansas Frontier Matrix — Accessibility Audit Templates & Checklists**  
Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Accessibility Audits](../README.md) · [Checklist →](checklist-wcag2.1aa.md) · [⚖ Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>