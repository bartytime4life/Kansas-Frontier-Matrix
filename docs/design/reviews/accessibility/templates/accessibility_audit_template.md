<div align="center">

# ♿ Kansas Frontier Matrix — Accessibility Audit Template  
`docs/design/reviews/accessibility/templates/accessibility_audit_template.md`

**Purpose:** A reproducible template for recording **accessibility compliance results**  
(WCAG 2.1 AA · Section 508 · ARIA 1.2) for each KFM UI component or feature.  
Use this during **design audits**, **pre-release reviews**, and **CI-driven accessibility testing**.

[![Accessibility](https://img.shields.io/badge/WCAG-2.1AA-yellow)](#📊-summary-results)  
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
| **Audit Tools** | Axe Core vX · Lighthouse vX · Pa11y vX |
| **WCAG Target** | AA |
| **Status** | pass / fail / needs-review |

---

## 🧩 Audit Sections

### 1️⃣ Perceivable

| Criterion | Description | Status | Notes |
|------------|--------------|:------:|-------|
| 1.1.1 | Non-text content (alt text / ARIA labels) | ☐ | |
| 1.3.1 | Info & relationships via semantic HTML | ☐ | |
| 1.4.3 | Text contrast ≥ 4.5 : 1 | ☐ | |
| 1.4.11 | Non-text contrast ≥ 3 : 1 | ☐ | |
| 1.4.12 | Text spacing adjustable | ☐ | |

---

### 2️⃣ Operable

| Criterion | Description | Status | Notes |
|------------|--------------|:------:|-------|
| 2.1.1 | Keyboard operable | ☐ | |
| 2.1.2 | No keyboard trap | ☐ | |
| 2.4.3 | Focus order logical | ☐ | |
| 2.4.7 | Focus visible | ☐ | |
| 2.5.3 | Label in name | ☐ | |

---

### 3️⃣ Understandable

| Criterion | Description | Status | Notes |
|------------|--------------|:------:|-------|
| 3.1.1 | Language of page set | ☐ | |
| 3.2.3 | Consistent navigation | ☐ | |
| 3.3.2 | Input assistance | ☐ | |

---

### 4️⃣ Robust

| Criterion | Description | Status | Notes |
|------------|--------------|:------:|-------|
| 4.1.1 | Valid HTML; unique IDs | ☐ | |
| 4.1.2 | Name · Role · Value exposed to AT | ☐ | |
| 4.1.3 | Status messages announced | ☐ | |

---

## 🧠 Testing Methods

| Method | Purpose | Tool / Command |
|---------|----------|----------------|
| **Automated** | Detect common accessibility violations | `npm run test:a11y` |
| **Manual Keyboard** | Tab / Shift+Tab / Enter / Space navigation | Physical keyboard |
| **Screen Reader** | Validate role/name/value announcements | NVDA / VoiceOver |
| **Color Contrast** | Measure text and UI contrast ratios | Chrome DevTools / Figma Plugin |
| **Motion Preferences** | Respect `prefers-reduced-motion` | Browser OS settings |

---

## 🪶 Focus and Navigation Flow

```mermaid
flowchart LR
  A["Start Focus\n(Tab from document root)"] --> B["Header\nLogo → Search → Help → Login"]
  B --> C["Main Content\nMap → Timeline → Drawer"]
  C --> D["Modal / Drawer\nFocus Trap · Escape Closes"]
  D --> E["Return Focus\nPrevious Element Restored"]

  style A fill:#E6EFFF,stroke:#0074D9,stroke-width:2px
  style B fill:#F8F8FF,stroke:#6C63FF,stroke-width:1.5px
  style C fill:#FFFDE7,stroke:#FBC02D,stroke-width:1.5px
  style D fill:#E3F2FD,stroke:#1976D2,stroke-width:1.5px
  style E fill:#E8F5E9,stroke:#2E7D32,stroke-width:1.5px

  %% END OF MERMAID
````

---

## 📊 Summary Results

| Category                  | Score (%) |     Result     | Notes                          |
| ------------------------- | --------- | :------------: | ------------------------------ |
| Perceivable               | 100 %     |        ✅       |                                |
| Operable                  | 95 %      |       ⚙️       | Focus trap improvement planned |
| Understandable            | 100 %     |        ✅       |                                |
| Robust                    | 100 %     |        ✅       |                                |
| **Overall Accessibility** | **98 %**  | ✅ AA Compliant | Minor refinements pending      |

---

## 🧩 Issues & Resolutions

| ID       | Severity | Description                           | Fix / Recommendation                |   Status  |
| -------- | -------- | ------------------------------------- | ----------------------------------- | :-------: |
| A11Y-001 | Medium   | Map zoom buttons lack `aria-label`    | Add descriptive labels              |  ✅ Fixed  |
| A11Y-002 | Low      | Timeline scrubber focus color < 3 : 1 | Update token `--kfm-focus-outline`  |  ✅ Fixed  |
| A11Y-003 | Low      | VoiceOver reads duplicate titles      | Remove redundant `title` attributes | ⚙️ Retest |

---

## ⚙️ Continuous Integration (Accessibility QA)

```yaml
# .github/workflows/a11y_component_audit.yml
on:
  pull_request:
    paths:
      - "web/src/components/**"
      - "docs/design/reviews/accessibility/templates/accessibility_audit_template.md"
jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install tools
        run: npm i -g axe-core-cli pa11y-ci
      - name: Run component a11y test
        run: pa11y-ci --config .pa11yci.component.json > a11y-component-report.json
      - name: Upload artifact
        uses: actions/upload-artifact@v4
        with:
          name: a11y-component-audit
          path: a11y-component-report.json
```

---

## 🧾 Provenance (YAML Metadata)

```yaml
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
environment:
  os: "Windows 11"
  browser: "Chrome 130"
  theme: "Dark"
```

---

## 🪪 License

Released under **Creative Commons CC-BY 4.0**
© 2025 Kansas Frontier Matrix Design Collective

---

<div align="center">

### ♿ Kansas Frontier Matrix — Accessibility Audit Template

**Structured · Reproducible · Inclusive**

</div>
