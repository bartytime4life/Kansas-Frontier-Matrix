---
title: "♿ Kansas Frontier Matrix — Accessibility Compliance Checklists (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Official, MCP-compliant accessibility checklists for validating UIs, documents, datasets, and workflows across KFM with WCAG 2.1 AA and FAIR+CARE alignment."
path: "docs/accessibility/checklists/README.md"
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · FAIR+CARE Accessibility Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x a11y-checklist-compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../releases/v11.2.3/a11y-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/a11y-checklists-v2.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
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
    - "web-ui"
    - "maplibre-cesium"
    - "story-nodes"
    - "focus-mode"
    - "docs-and-pdfs"
    - "dataset-metadata"

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
sunset_policy: "Supersedes v10.4.0 accessibility checklist standard"

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
  - "docs/accessibility/checklists/README.md@v10.4.0"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/docs-accessibility-checklists-v11.2.3.schema.json"
shape_schema_ref: "schemas/shacl/docs-accessibility-checklists-v11.2.3-shape.ttl"
story_node_refs: []

immutability_status: "mutable"

doc_uuid: "urn:kfm:doc:accessibility:checklists:v11.2.3"
semantic_document_id: "kfm-accessibility-checklists-standard-v11.2.3"
event_source_id: "ledger:kfm:doc:accessibility:checklists:v11.2.3"

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

# ♿ Kansas Frontier Matrix — Accessibility Compliance Checklists  

`docs/accessibility/checklists/README.md`

**Purpose:**  
Define the **official, MCP-compliant Accessibility Compliance Checklists** for validating user interfaces, documents, datasets, and workflows across the **Kansas Frontier Matrix (KFM)**.  
These checklists enforce WCAG 2.1 AA, ISO 9241-210, FAIR+CARE ethics, and v11.x accessibility telemetry requirements.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../README.md) ·
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../standards/faircare/FAIRCARE-GUIDE.md) ·
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE) ·
[![Status: Active](https://img.shields.io/badge/Status-Active-success)](../../../releases/v11.2.3/manifest.zip)

</div>

---

## 📘 1. Overview

The **Accessibility Compliance Checklists** standardize evaluation of KFM systems for:

- **Web UI accessibility** (MapLibre, timeline, panels, controls)  
- **Documentation accessibility** (Markdown/HTML/PDF outputs, Story Nodes, Focus Mode)  
- **Dataset accessibility** (metadata integrity, alt text, semantic labeling)  
- **AI-governed accessibility** (Focus Mode narratives, explainability, ARIA compliance)  

These checklists are aligned with:

- **WCAG 2.1 AA**  
- **ISO 9241-210 Human-Centered Design**  
- **FAIR+CARE Ethics**  
- **MCP-DL v6.3 Documentation-First Protocol**  
- **KFM-MDP v11.2.2 Markdown Structural Rules**  

They are validated continuously through:

- `accessibility_scan.yml`  
- `storybook-a11y.yml`  
- `faircare-visual-audit.yml`  
- `docs-lint.yml`  

All failures MUST be resolved or explicitly waived under governance before merging to governed branches.

---

## 🧳 2. Directory Layout

~~~text
docs/accessibility/checklists/
├── 📄 README.md                  # Index and governance for all accessibility checklists
├── 📄 checklist-wcag2.1aa.md     # Core WCAG 2.1 AA compliance checklist
├── 📄 focus-navigation.md        # Keyboard and focus behavior verification
├── 📄 contrast-and-color.md      # Color contrast and semantic token validation
├── 📄 motion-and-animations.md   # Motion reduction and sensory safety checklist
└── 📄 document-accessibility.md  # Documentation & narrative accessibility checklist
~~~

| File                       | Description                                                       |
|----------------------------|-------------------------------------------------------------------|
| `README.md`                | Index and governance for all accessibility checklists (this file).|
| `checklist-wcag2.1aa.md`   | Core WCAG 2.1 AA compliance checklist.                           |
| `focus-navigation.md`      | Keyboard and focus behavior verification.                        |
| `contrast-and-color.md`    | Color contrast and semantic token validation.                    |
| `motion-and-animations.md` | Motion reduction and sensory safety checklist.                   |
| `document-accessibility.md`| Documentation structure, headings, tables, and alt text checks.  |

Each checklist MUST:

- Use stable headings and tables for machine extraction.  
- Reference this README in its front matter as the domain standard.  

---

## 🧑‍🦽 3. Core Accessibility Categories

| Checklist                    | Purpose                                 | Scope                                      |
|-----------------------------|-----------------------------------------|-------------------------------------------|
| **WCAG 2.1 AA**             | Baseline accessibility conformance      | Entire platform (UI, docs, datasets)      |
| **Keyboard & Focus**        | Focus order, visibility, no traps       | Web app, map/timeline, dialogs            |
| **Color & Contrast**        | Semantic tokens, ≥ 4.5:1 contrast       | UI themes, map overlays, legends          |
| **Motion & Sensory Safety** | Honors motion prefs & avoids triggers   | Animations, transitions, auto-play        |
| **Documentation Accessibility** | Semantic structure, alt text, link clarity | All Markdown/PDF outputs & Story Nodes |

Each checklist file formalizes:

- Test cases  
- Acceptance criteria  
- Expected CI / telemetry hooks  

---

## 🧠 4. FAIR+CARE Ethical Alignment

| FAIR+CARE Principle   | Accessibility Implementation                                                       |
|-----------------------|------------------------------------------------------------------------------------|
| **Collective Benefit**   | Ensures equitable access to historical and scientific knowledge for all users.  |
| **Authority to Control** | Users can configure motion, contrast, and text preferences where supported.     |
| **Responsibility**       | Issues discovered in audits must be logged, triaged, and remediated with owners.|
| **Ethics**               | Avoids exclusionary patterns; respects culturally sensitive content and language.|

Accessibility audits and checklists **must** include a FAIR+CARE section summarizing ethical findings and remediation plans.

---

## 🧾 5. WCAG 2.1 AA Checklist (Excerpt)

| Criterion                        | Requirement                                      | Status | Notes                                                    |
|----------------------------------|--------------------------------------------------|--------|----------------------------------------------------------|
| **1.1.1 Non-text Content**      | All images/maps have alt text or ARIA labels.    | ✅     | Map layers and icons labeled.                           |
| **1.3.1 Info & Relationships**  | Structure defined by semantic HTML.              | ✅     | Landmarks (`<header>`, `<main>`, `<nav>`, `<footer>`).  |
| **1.4.3 Contrast (Minimum)**    | Text contrast ≥ 4.5:1.                           | ⚠️     | Re-validate hover/focus states after theme changes.     |
| **2.1.1 Keyboard**              | All functions operable via keyboard.             | ✅     | Map + timeline fully navigable.                         |
| **2.4.7 Focus Visible**         | Focus indicator always visible.                  | ✅     | Uses `focus.outline.color` tokens.                      |
| **3.3.3 Error Suggestion**      | Errors include suggestions & are announced.      | ✅     | Screen readers read error text and field context.       |

Full details and extended matrix live in `checklist-wcag2.1aa.md`.

---

## 🔍 6. Focus Navigation Checklist (Excerpt)

| Test                    | Description                                           | Pass | Notes                                      |
|-------------------------|-------------------------------------------------------|------|--------------------------------------------|
| **Sequential Order**    | Tab order matches visual flow & logical DOM.         | ✅   | Verified for primary flows.                |
| **No Focus Traps**      | Users can always tab out of dialogs/overlays.        | ✅   | Escape routes documented.                  |
| **Escape Key Behavior** | ESC closes modals, restores previous focus.          | ✅   | Covered in Storybook a11y tests.           |
| **Skip Links**          | “Skip to content/navigation” links present & visible.| ⚠️   | Improve styling in dark theme.             |
| **Keyboard Shortcuts**  | Arrow keys and shortcuts documented and discoverable.| ✅   | Timeline and map keyboard help overlay.    |

Full test matrix lives in `focus-navigation.md`.

---

## 🧩 7. Motion & Sensory Safety Checklist (Excerpt)

| Test                        | Description                                      | Pass | Notes                                 |
|-----------------------------|--------------------------------------------------|------|---------------------------------------|
| **prefers-reduced-motion** | Honor OS/user motion preference.                | ✅   | Non-essential animations disabled.    |
| **Animation Duration**      | Default transitions ≤ 200ms.                    | ✅   | Tokenized durations to avoid drift.   |
| **Flashing Content**        | No flashing > 3Hz.                              | ✅   | Confirmed in visualization library.   |
| **Parallax & Auto-scroll**  | Requires explicit user initiation.              | ✅   | No auto-scrolling scenes enabled.     |

See `motion-and-animations.md` for full procedures and edge cases.

---

## ⚙️ 8. Accessibility Validation Workflows

| Workflow                    | Function                                            | Output Artifact                                   |
|----------------------------|-----------------------------------------------------|---------------------------------------------------|
| `accessibility_scan.yml`   | Runs axe-core and Lighthouse audits on key flows.  | `reports/self-validation/web/a11y_summary.json`   |
| `storybook-a11y.yml`       | Executes component-level a11y tests in Storybook.  | `reports/ui/a11y_component_audits.json`           |
| `faircare-visual-audit.yml`| Evaluates inclusive design & ethical visuals.      | `reports/faircare/visual_validation.json`         |
| `docs-lint.yml`            | Validates documentation structure, headings, alts. | `reports/docs/a11y_doc_validation.json`           |

All four workflows MUST pass for any release tagged as **Diamond⁹ Ω / Crown∞Ω** for accessibility.

---

## 📊 9. Accessibility KPI Metrics

| Metric                        | Target                                 | Verified By                  |
|-------------------------------|----------------------------------------|------------------------------|
| **WCAG 2.1 AA Compliance**   | 100% of applicable success criteria.   | CI + Accessibility Council   |
| **Keyboard Operability**     | 100% of core user journeys.            | Storybook + end-to-end tests |
| **Color Contrast**           | ≥ 4.5:1 for all text/UI elements.      | Design token validator       |
| **Motion Preference Adherence** | 100% compliance with user settings. | Automated checks + manual QA |
| **FAIR+CARE Ethics Score**   | ≥ 95% in quarterly audits.             | FAIR+CARE Council            |

These KPIs are tracked in accessibility telemetry and surfaced in transparency dashboards.

---

## 🧮 10. Checklist Lifecycle & Governance

~~~mermaid
flowchart LR
    A[Define / Update Checklists] --> B[FAIR+CARE Accessibility Council Review]
    B --> C[Automated a11y + Docs CI]
    C --> D[Manual Spot Checks & Usability Testing]
    D --> E[Telemetry Logging & KPI Review]
    E --> F[Quarterly Transparency Report]
    F --> A
~~~

Accessibility governance is cyclic and data-driven: telemetry, user feedback, and ethics reviews feed into the next revision of each checklist.

---

## 🕰️ 11. Version History

| Version  | Date       | Author                         | Summary                                                                                 |
|----------|------------|--------------------------------|-----------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-02 | FAIR+CARE Accessibility Council | Upgraded to KFM-MDP v11.2.2; added governance metadata and telemetry v11.2.3; aligned workflows. |
| v10.4.0  | 2025-11-17 | FAIR+CARE Accessibility Council | Updated for KFM-MDP v10.4; added telemetry schema v2; refined directory layout & links. |
| v10.0.0  | 2025-11-10 | FAIR+CARE Accessibility Council | Initial Diamond⁹ Ω / Crown∞Ω accessibility checklist framework.                        |

---

<div align="center">

♿ **Kansas Frontier Matrix — Accessibility Compliance Checklists**  
Inclusive Design · FAIR+CARE Governance · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Accessibility Index](../README.md) · [Audits →](../audits/README.md) · [⚖ Governance](../../standards/governance/ROOT-GOVERNANCE.md)

</div>