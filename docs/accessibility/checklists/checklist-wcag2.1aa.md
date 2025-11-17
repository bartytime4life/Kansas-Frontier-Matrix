---
title: "♿ Kansas Frontier Matrix — WCAG 2.1 AA Master Compliance Checklist (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/accessibility/checklists/checklist-wcag2.1aa.md"
version: "v10.4.1"
last_updated: "2025-11-16"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.1/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.1/manifest.zip"
telemetry_ref: "../../../releases/v10.4.1/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/a11y-wcag2.1aa-checklist-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.3"
status: "Active / Enforced"
doc_kind: "Checklist"
intent: "wcag-2-1-aa-validation"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: false
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "Checklist compiled for full WCAG 2.1 AA conformance validation"
ontology_alignment:
  schema_org: "Checklist"
  cidoc: "E29 Design or Procedure"
  prov_o: "prov:Plan"
json_schema_ref: "../../../schemas/json/a11y-checklist-wcag21.schema.json"
shape_schema_ref: "../../../schemas/shacl/a11y-checklist-wcag21.ttl"
doc_uuid: "urn:kfm:doc:a11y-wcag21-checklist-v10.4.1"
semantic_document_id: "kfm-doc-a11y-wcag21-checklist"
event_source_id: "ledger:docs/accessibility/checklists/checklist-wcag2.1aa.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
machine_extractable: true
classification: "Accessibility · WCAG · Compliance · Standards"
jurisdiction: "Kansas / United States"
role: "a11y-checklist-wcag21"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded by future versions"
---

<div align="center">

# ♿ **Kansas Frontier Matrix — WCAG 2.1 AA Master Compliance Checklist**  
`docs/accessibility/checklists/checklist-wcag2.1aa.md`

**Purpose:**  
Authoritative WCAG 2.1 AA compliance checklist for **every Kansas Frontier Matrix (KFM) interface**, including web UI, data visualizations, maps, AI outputs, Focus Mode, dashboards, archives, and telemetry-driven applications.  
All checkpoints integrate **FAIR+CARE ethics**, **KFM design tokens**, **ARIA standards**, and **MCP-DL v6.3** documentation rules.

![WCAG 2.1 AA](https://img.shields.io/badge/WCAG-2.1_AA-blue)
![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)
![Status](https://img.shields.io/badge/Status-Enforced-brightgreen)

</div>

---

# 📘 Overview

This document lists **all WCAG 2.1 AA success criteria** as **actionable KFM validation items**, aligned with:

- **WCAG 2.1 AA**  
- **WAI-ARIA 1.2 Authoring Practices**  
- **KFM Design Tokens v10.4**  
- **KFM A11y Pattern Library**  
- **FAIR+CARE Ethical Communication Standards**

Every KFM UI must pass all relevant items before deployment.

---

# 🧩 WCAG 2.1 AA Success Criteria — KFM-Aligned Checklist

Each item includes a checkbox for implementers and applies to **all product surfaces**.

---

## 1.0 — Perceivable

### 1.1 Text Alternatives
- [ ] **1.1.1** All non-text content has alt text or ARIA label.  
- [ ] Decorative images use `alt=""`.  
- [ ] Complex graphics include long description or data table.

### 1.2 Time-Based Media
- [ ] **1.2.1** Audio-only media has transcript.  
- [ ] **1.2.2** Video has synchronized captions.  
- [ ] **1.2.3** Audio description available for pre-recorded video.  
- [ ] **1.2.4** Live captions present for live streams.  
- [ ] **1.2.5** Extended audio description available where necessary.

### 1.3 Adaptable
- [ ] **1.3.1** Proper semantic structure (headings, lists, tables).  
- [ ] **1.3.2** Meaningful sequence preserved.  
- [ ] **1.3.3** Instructions independent of shape, color, sound.

### 1.4 Distinguishable
- [ ] **1.4.1** Color not sole means of conveying information.  
- [ ] **1.4.2** Audio can be paused/controlled.  
- [ ] **1.4.3** Text contrast ≥ 4.5:1.  
- [ ] **1.4.4** Text resizable to 200% without loss.  
- [ ] **1.4.5** No images of text unless essential.  
- [ ] **1.4.10** Reflow supported at 320px width.  
- [ ] **1.4.11** Non-text contrast ≥ 3:1.  
- [ ] **1.4.12** Hover/focus content persistent, dismissible.  
- [ ] **1.4.13** Tooltips & popovers accessible.

---

## 2.0 — Operable

### 2.1 Keyboard Accessible
- [ ] **2.1.1** All functionality available via keyboard.  
- [ ] **2.1.2** No keyboard traps.  
- [ ] **2.1.4** Character key shortcuts inactive without focus.

### 2.2 Enough Time
- [ ] **2.2.1** User can turn off, adjust, or extend time limits.  
- [ ] **2.2.2** Pause/stop/hide for moving/auto-updating content.

### 2.3 Seizures and Physical Reactions
- [ ] **2.3.1** No flashing above 3 Hz.  
- [ ] **2.3.2** Animations disable with `prefers-reduced-motion`.

### 2.4 Navigable
- [ ] **2.4.1** Bypass blocks (skip links).  
- [ ] **2.4.2** Descriptive page titles.  
- [ ] **2.4.3** Focus order logical & predictable.  
- [ ] **2.4.4** Link purpose clear.  
- [ ] **2.4.5** Multiple ways to find pages.  
- [ ] **2.4.6** Headings/labels descriptive.  
- [ ] **2.4.7** Visible focus indicator.  
- [ ] **2.4.11** Character key shortcuts adjustable.

### 2.5 Input Modalities
- [ ] **2.5.1** Pointer gestures have alternatives.  
- [ ] **2.5.2** Pointer cancellation supported.  
- [ ] **2.5.3** Label-in-name alignment.  
- [ ] **2.5.4** Motion actuation optional.  
- [ ] **2.5.8** Target size adequate.

---

## 3.0 — Understandable

### 3.1 Readable
- [ ] **3.1.1** Language declared.  
- [ ] **3.1.2** Language changes indicated.  
- [ ] **3.1.5** Reading level supported with plain-language summaries.

### 3.2 Predictable
- [ ] **3.2.1** No unexpected context changes.  
- [ ] **3.2.2** UI behaves consistently.  
- [ ] **3.2.3** Navigation remains consistent.  
- [ ] **3.2.4** Consistent component identification.

### 3.3 Input Assistance
- [ ] **3.3.1** Errors identified clearly.  
- [ ] **3.3.2** Labels/instructions provided.  
- [ ] **3.3.3** Suggestions for error correction.  
- [ ] **3.3.4** Prevent irreversible actions with confirmation.

---

## 4.0 — Robust

### 4.1 Compatibility
- [ ] **4.1.1** Valid HTML & correct ARIA usage.  
- [ ] **4.1.2** Proper name/role/value for all UI components.  
- [ ] **4.1.3** Status messages conveyed without focus shift.

---

# 🧩 FAIR+CARE Ethical Alignment Add-Ons (KFM-Specific)

### Consent & Cultural Protections
- [ ] All sensitive datasets gated behind `data-fair-consent`.  
- [ ] Indigenous knowledge layers masked unless authorized.  
- [ ] Tone checked for neutrality via FAIR+CARE audit.

### AI & Automation
- [ ] AI explanations provided in plain language.  
- [ ] All models disclose provenance + bias review.  
- [ ] AI suggestions labeled with `data-ai-source`.

### Sustainability & Transparency
- [ ] Provenance shown for every dataset.  
- [ ] Energy + carbon metrics (ISO 50001/14064) visible where relevant.

---

# 🧪 Automated Validation Pipelines (Required)

| Workflow | Scope | Output |
|----------|--------|--------|
| `accessibility_scan.yml` | Axe-core + Lighthouse | `reports/self-validation/web/a11y_summary.json` |
| `storybook-a11y.yml` | Component-level a11y tests | `reports/ui/a11y_components.json` |
| `faircare-language.yml` | Tone, ethics, cultural safety | `reports/faircare/language.json` |
| `telemetry-a11y.yml` | Interaction logging + focus checks | `reports/self-validation/web/telemetry.json` |

All CI must pass before merge.

---

# 🕰️ Version History

| Version | Date | Author | Summary |
|---------|------------|---------|----------|
| v10.4.1 | 2025-11-16 | KFM A11y Guild | Full WCAG 2.1 AA alignment + MDP v10.4.3 formatting. |

---

<div align="center">

© 2025 Kansas Frontier Matrix · Master Coder Protocol v6.3  
**FAIR+CARE Certified · WCAG 2.1 AA Verified**

[⬅ Back to Accessibility Checklists](README.md)

</div>