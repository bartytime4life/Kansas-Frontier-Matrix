---
title: "🎞️ Kansas Frontier Matrix — Motion & Animation Accessibility Checklist (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/accessibility/checklists/motion-and-animations.md"
version: "v10.4.1"
last_updated: "2025-11-16"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/a11y-motion-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.3"
status: "Active / Enforced"
doc_kind: "Checklist"
intent: "motion-a11y-validation"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: false
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "New document created under a11y checklist expansion"
previous_version_hash: null
ontology_alignment:
  schema_org: "Checklist"
  cidoc: "E29 Design or Procedure"
  prov_o: "prov:Plan"
json_schema_ref: "../../../schemas/json/a11y-checklist-motion.schema.json"
shape_schema_ref: "../../../schemas/shacl/a11y-checklist-motion-shape.ttl"
doc_uuid: "urn:kfm:doc:a11y-motion-checklist-v10.4.1"
semantic_document_id: "kfm-doc-a11y-motion-checklist"
event_source_id: "ledger:docs/accessibility/checklists/motion-and-animations.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Accessibility · Motion · Animations"
jurisdiction: "Kansas / United States"
role: "a11y-checklist-motion"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "New version replaces prior"
---

<div align="center">

# 🎞️ **Kansas Frontier Matrix — Motion & Animation Accessibility Checklist**  
`docs/accessibility/checklists/motion-and-animations.md`

**Purpose:**  
Required pre-deployment checklist ensuring **animations, transitions, motion effects, camera movement, and dynamic UI elements** across KFM platforms adhere to **WCAG 2.1 AA**, **FAIR+CARE**, and **KFM-MDP v10.4.3** design ethics.  
Applies to **MapLibre**, **Cesium**, **Recharts**, **Focus Mode**, **Story Nodes**, dashboards, and all frontend components.

![A11y](https://img.shields.io/badge/A11y-WCAG_2.1_AA-blue)
![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)
![Status](https://img.shields.io/badge/Status-Required-success)

</div>

---

## 📘 Overview

Motion and animation can enhance understanding—but can also cause **vestibular discomfort**, **cognitive overload**, or **involuntary startle reactions** if not properly managed.  
This checklist guarantees:

- Predictable and user-controlled interactions  
- Respect for **reduced-motion preferences**  
- Clear ARIA patterns for dynamic updates  
- Ethical, non-coercive visual communication  
- Stable designs compatible with screen readers, switch devices, and older hardware

This document is **mandatory** for any feature containing animation, camera motion, auto-play content, or real-time updates.

---

## ✅ Section 1 — Global Motion Rules

### ✔️ Required
- [ ] All animations respect `prefers-reduced-motion: reduce`.
- [ ] No animation exceeds **3 flashes per second** (WCAG 2.3.1).
- [ ] User can **pause, stop, or hide** any animated element (WCAG 2.2.2).
- [ ] Camera movements (MapLibre, Cesium) **never auto-pan** without explicit user action.
- [ ] Motion used **only to aid comprehension**, not decoration.
- [ ] No sudden high-velocity zooms, pans, rotations, or bounces.
- [ ] Avoid parallax unless fully opt-in.
- [ ] Hover animations ≤ 120ms; minimal displacement.

### ⚠️ Prohibited
- [ ] Auto-scrolling text marquees.
- [ ] Looping animations with no controls.
- [ ] Screen shake or strobe-like feedback.
- [ ] Unannounced camera fly-throughs or transitions.

---

## ✅ Section 2 — Focus Mode & Story Nodes

### ✔️ Focus Mode Requirements
- [ ] Cognitive load reduced: max 5 visual clusters.
- [ ] Animation speed controlled by `focusmode.animation.speed` token.
- [ ] Explanations appear via fade/slide ≤ 120ms.
- [ ] No motion during AI suggestion events unless user-triggered.
- [ ] Context shifts only after **explicit confirmation**.

### ✔️ Story Node Patterns
- [ ] Historical/temporal transitions fade smoothly (<150ms).
- [ ] 3D timeline scrubbing provides **no auto-play**.
- [ ] Animated overlays (climate, hydrology) require toggle + textual equivalent.

---

## ✅ Section 3 — Geospatial Motion (MapLibre, Cesium, 3D Scenes)

### ✔️ Required
- [ ] All map motions respect reduced-motion preference.
- [ ] Damped/slow transitions (<400ms) when zooming/panning.
- [ ] User-triggered navigation only—never on page load.
- [ ] No rotating globes, spinning symbols, or wobbling markers.
- [ ] Animated layers include textual summaries (ARIA + captions).
- [ ] Flight paths, migration routes, and space weather arcs animate only on command.

### ⚠️ Camera Motion Checklist
- [ ] No orbital rotations without user intent.
- [ ] Minimize Z-axis oscillations in Cesium.
- [ ] Provide “Reset View” button with stable snap.

---

## ✅ Section 4 — Data Visualizations (Charts, D3, Recharts)

### ✔️ Required for All Charts
- [ ] Animation duration ≤ 300ms.
- [ ] Reduced-motion disables tweening/curves entirely.
- [ ] Tooltip motion anchored; no drifting tooltips.
- [ ] Live updates use **soft fades** instead of slide/shift.
- [ ] Provide accessible data tables for non-visual users.

### ⚠️ Avoid
- [ ] Auto-animating bars/lines on every filter change.
- [ ] Pulsing or bouncing markers.

---

## ✅ Section 5 — Alerts, Toasts & UI Feedback

### ✔️ Required
- [ ] Toasts fade in/out ≤ 120ms.
- [ ] Toasts do **not** slide from offscreen unless user-triggered.
- [ ] Loading indicators rotate < 1 full turn per 120ms.
- [ ] No shaking error animations—replace with color + ARIA alert.

### ⚠️ Ethical Messaging
- [ ] Ensure FAIR+CARE tone: no fear-based or escalatory animation cues.

---

## ✅ Section 6 — Media, Video & Time-Based Playback

### ✔️ Video/3D Requirements
- [ ] All auto-play disabled by default.
- [ ] Users must grant consent for motion-heavy content.
- [ ] Closed captions required for narrated animations.
- [ ] Provide frame-by-frame or slow-motion mode when applicable.

### ✔️ Animated GIF/SVG
- [ ] GIFs replaced with `<video>` + controls whenever possible.
- [ ] SVG animations tied to user action only.

---

## 🧪 Validation & CI Integration

| Workflow                      | Scope                                        | Output Path |
|------------------------------|----------------------------------------------|-------------|
| `motion-scan.yml`            | Detects high-motion sequences, disallowed FX | `reports/ui/motion-validation.json` |
| `accessibility_scan.yml`     | Validates ARIA + WCAG motion rules           | `reports/self-validation/web/a11y_motion.json` |
| `faircare-visual-audit.yml`  | Ensures ethical and calm motion patterns     | `reports/faircare/visual-motion.json` |

All merges to `main` **blocked** without passing these checks.

---

## 🧠 References

- WCAG 2.1 — 2.2.2 Pause/Stop/Hide, 2.3.1 Seizures, 2.3.3 Motion  
- WAI-ARIA 1.2 Live Regions  
- ISO 9241-210 Human-Centered Design  
- FAIR+CARE Governance Charter  
- KFM Design Tokens (`web/src/theme/tokens.json`)  
- KFM Motion Standards (`docs/accessibility/patterns/focus-mode.md`)  

---

## 🕰️ Version History

| Version | Date       | Author                     | Summary |
|--------:|------------|----------------------------|---------|
| v10.4.1 | 2025-11-16 | KFM A11y Council           | Initial motion accessibility checklist; aligned with full pattern library and MDP v10.4.3. |

---

<div align="center">

© 2025 Kansas Frontier Matrix · Master Coder Protocol v6.3  
**FAIR+CARE Certified · Motion-Safe Design Verified**

[⬅ Back to Accessibility Checklists](README.md)

</div>