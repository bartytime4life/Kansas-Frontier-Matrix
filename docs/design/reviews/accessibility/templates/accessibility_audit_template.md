<div align="center">

# ♿ Kansas Frontier Matrix — Accessibility Audit Template  
`docs/design/reviews/accessibility/templates/accessibility_audit_template.md`

**Purpose:** A reproducible template for recording accessibility compliance results (WCAG 2.1 AA · Section 508 · ARIA 1.2) for each KFM UI component or feature.  
Use this form during design and pre-release audits.

[![Accessibility](https://img.shields.io/badge/WCAG-2.1AA-yellow)](#audit-summary)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../)
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY--4.0-lightgrey)](../../../../../LICENSE)

</div>

---

## 🧭 Component Metadata

| Field | Value |
|--------|--------|
| **Component Name** | `{{ component_name }}` |
| **Path** | `web/src/components/{{ path }}` |
| **Version** | `{{ version }}` |
| **Mockup Ref** | [Figma Frame ID / Link] |
| **Audit Date** | `{{ ISO8601_DATE }}` |
| **Reviewer(s)** | `@handle1`, `@handle2` |
| **Commit** | `{{ GIT_COMMIT }}` |
| **Audit Tooling** | Axe Core vX · Lighthouse vX · Pa11y vX |
| **WCAG Level Target** | AA |
| **Status** | pass / fail / needs-review |

---

## 🧩 Audit Sections

### 1️⃣ Perceivable

| Criterion | Description | Pass ✅ / Fail ❌ / N/A | Notes |
|------------|--------------|-------------------------|-------|
| 1.1.1 | Non-text content (alt text / ARIA labels) | | |
| 1.3.1 | Info & relationships via semantic HTML | | |
| 1.4.3 | Text contrast ≥ 4.5 : 1 | | |
| 1.4.11 | Non-text contrast ≥ 3 : 1 | | |
| 1.4.12 | Text spacing adjustable | | |

### 2️⃣ Operable

| Criterion | Description | Pass ✅ / Fail ❌ / N/A | Notes |
|------------|--------------|-------------------------|-------|
| 2.1.1 | Keyboard operable | | |
| 2.1.2 | No keyboard trap | | |
| 2.4.3 | Focus order logical | | |
| 2.4.7 | Focus visible | | |
| 2.5.3 | Label in name | | |

### 3️⃣ Understandable

| Criterion | Description | Pass ✅ / Fail ❌ / N/A | Notes |
|------------|--------------|-------------------------|-------|
| 3.1.1 | Language of page set | | |
| 3.2.3 | Consistent navigation | | |
| 3.3.2 | Input assistance | | |

### 4️⃣ Robust

| Criterion | Description | Pass ✅ / Fail ❌ / N/A | Notes |
|------------|--------------|-------------------------|-------|
| 4.1.1 | Valid HTML; unique IDs | | |
| 4.1.2 | Name · Role · Value exposed to AT | | |
| 4.1.3 | Status messages announced | | |

---

## 🧠 Testing Methods

| Method | Purpose | Tool / Command |
|---------|----------|----------------|
| Automated | Detect common violations | `npm run test:a11y` |
| Manual Keyboard | Tab/Shift + Tab / Enter / Space navigation | Physical keyboard |
| Screen Reader | Verify role/name/value announcements | NVDA / VoiceOver |
| Color Contrast | Measure contrast ratios | Chrome DevTools / Figma Contrast Grid |
| Motion Preferences | Respect `prefers-reduced-motion` | Browser Settings |

---

## 🪶 Focus and Navigation Flow

```mermaid
flowchart LR
  A["Start Focus\n(Tab from document root)"] --> B["Header\nlogo → search → help → login"]
  B --> C["Main Content\nmap → timeline → drawer"]
  C --> D["Modal / Drawer\nfocus trap → Escape closes"]
  D --> E["Return Focus\n(previous element)"]
<!-- END OF MERMAID -->


⸻

📊 Summary Results

Category	Score (%)	Result	Notes
Perceivable	100 %	✅	
Operable	95 %	⚙️ Focus trap improvement planned	
Understandable	100 %	✅	
Robust	100 %	✅	
Overall Accessibility	98 %	✅ AA Compliant	


⸻

🧩 Issues & Resolutions

ID	Severity	Description	Fix / Recommendation	Status
A11Y-001	Medium	Map zoom buttons lack aria-label	Add descriptive labels	✅ Fixed
A11Y-002	Low	Timeline scrubber focus color < 3 : 1	Update token --kfm-focus-outline	✅ Fixed
A11Y-003	Low	VoiceOver reads duplicate titles	Remove redundant title attribute	⚙️ Pending retest


⸻

🧾 Provenance

audit_id: "a11y_{{ component_name }}_{{ version }}"
reviewed_by:
  - "@accessibility-team"
  - "@design-lead"
date: "{{ ISO8601_DATE }}"
commit: "{{ GIT_COMMIT }}"
wcag_level: "AA"
result: "pass"
tools:
  - "Axe Core v4.10"
  - "Lighthouse CI v12"
  - "Pa11y v7"
  - "NVDA 2023.3"


⸻

🪪 License

Released under Creative Commons CC-BY 4.0
© 2025 Kansas Frontier Matrix Design Collective

⸻



