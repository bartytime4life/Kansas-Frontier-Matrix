---
title: "UI Tokens (Sample)"
status: "sample"
subsystem: "web"
kfm_version: "v13"
audience: ["design", "frontend", "docs"]
last_updated: "2026-01-18"
---

# 🎛️ UI Tokens (Samples)

![KFM](https://img.shields.io/badge/KFM-v13-black)
![subsystem](https://img.shields.io/badge/subsystem-web%2FUI-blue)
![artifact](https://img.shields.io/badge/artifact-design%20tokens-orange)
![scope](https://img.shields.io/badge/scope-samples-lightgrey)

> A small, **copy-friendly** sample set of design tokens for the KFM Web UI — meant for demos, docs, and UI prototyping. 🎨🧩

---

## ✨ What are “UI tokens” here?

Design tokens are the **atomic UI contract**: named values for things like:

- 🎨 **Colors** (surface, text, borders, semantic states)
- 🔤 **Typography** (font stacks, sizes, weights, line heights)
- 📏 **Spacing & sizing** (layout rhythm, component padding)
- 🟦 **Radii & shadows** (shape + elevation)
- 🎛️ **Motion** (durations, easing)
- 🗺️ **Map UI affordances** (legend swatches, overlay styling, focus rings)

In KFM, the Web UI is the place where people interact with:
- map layers and viewers (2D/3D),
- story panels / guided narratives,
- timeline + legends,
- search and data catalog surfaces.

Tokens keep these surfaces consistent and make them easier to theme and audit. ✅

---

## 🧭 Where this fits in the KFM pipeline

KFM treats the UI as a governed stage in a larger pipeline. Tokens live squarely in the **UI** stage: they should be “safe,” deterministic, and never become a side-channel that leaks restricted details.

```mermaid
flowchart LR
  ETL[ETL] --> CAT[Catalogs<br/>STAC/DCAT/PROV]
  CAT --> GRAPH[Graph]
  GRAPH --> API[API]
  API --> UI[UI<br/>(Tokens live here)]
  UI --> STORY[Story Nodes]
  STORY --> FOCUS[Focus Mode]
```

**Rule of thumb:** tokens style the experience — they should not encode sensitive content, and they shouldn’t allow UI behavior that bypasses governance (redactions, safety rules, provenance constraints). 🔒

---

## 📦 What’s in this folder

This folder is intentionally under:

📁 `web/assets/samples/ui/tokens/`

Meaning:

- ✅ **Sample-first**: safe examples to copy into experiments, docs, or tests
- ✅ **Readable-first**: simple formats over clever tooling
- 🚫 **Not necessarily canonical**: production theming may live elsewhere in `web/` (e.g., a `theme/` or `styles/` area)

If you “graduate” a token set from here into production usage, treat it like a real contract:
- lock naming,
- add schema validation,
- add lint/CI checks,
- ensure accessibility and governance requirements hold. ✅

---

## 🧱 Token taxonomy

A practical structure that scales:

### 1) 🧱 Base tokens (raw values)
Low-level primitives:
- `color.base.*` (palette ramps)
- `space.*` (spacing scale)
- `radius.*`, `shadow.*`, `font.*`

### 2) 🧠 Semantic tokens (meaning)
UI intent and semantics:
- `color.semantic.surface.default`
- `color.semantic.text.muted`
- `color.semantic.intent.danger`
- `motion.duration.fast`

Semantic tokens should be stable; you can swap base values per theme without changing component code.

### 3) 🧩 Component tokens (optional)
Only if needed for complex components:
- `component.button.primary.background`
- `component.panel.border`
- `component.legend.swatchRadius`

If you find yourself creating many component tokens, consider whether your semantic layer is missing concepts. 🧠

---

## 🧾 Naming & formatting conventions

### ✅ Recommended naming rules
- **JSON keys:** `lowerCamelCase` OR `dot.path` style (pick one and stay consistent)
- **CSS variables:** `--kfm-*` (kebab-case)
- Prefer **semantic** names over “looks like” names:
  - ✅ `color.semantic.intent.warning`
  - ❌ `color.orange500`

### 📐 Units
- Typography: `rem` (preferred) or `px` if required by map/UI library constraints
- Spacing: `rem` (preferred) or `px` if the UI is strictly pixel-grid aligned
- Durations: `ms`

---

## 📁 Suggested sample layout

> This is a recommended layout for samples (feel free to adapt as the repo evolves).

```text
📁 web/assets/samples/ui/tokens/
├── 📄 README.md
├── 🎛️ tokens.sample.json
├── 🌞 theme.light.sample.json
├── 🌚 theme.dark.sample.json
└── 🎨 tokens.sample.css
```

---

## 🧪 Sample token file (JSON)

<details>
<summary><strong>tokens.sample.json</strong> (click to expand) 📦</summary>

```json
{
  "meta": {
    "name": "KFM UI Tokens (Sample)",
    "version": "0.1.0",
    "notes": "Sample-only token set. Do not treat as canonical without schema + CI."
  },
  "color": {
    "base": {
      "slate": {
        "0": "#ffffff",
        "50": "#f8fafc",
        "100": "#f1f5f9",
        "200": "#e2e8f0",
        "600": "#475569",
        "900": "#0f172a"
      },
      "blue": {
        "100": "#dbeafe",
        "600": "#2563eb",
        "700": "#1d4ed8"
      },
      "red": {
        "100": "#fee2e2",
        "600": "#dc2626"
      }
    },
    "semantic": {
      "surface": {
        "default": "{color.base.slate.0}",
        "raised": "{color.base.slate.50}",
        "sunken": "{color.base.slate.100}"
      },
      "text": {
        "default": "{color.base.slate.900}",
        "muted": "{color.base.slate.600}",
        "inverse": "{color.base.slate.0}"
      },
      "border": {
        "default": "{color.base.slate.200}",
        "focus": "{color.base.blue.600}"
      },
      "intent": {
        "info": "{color.base.blue.700}",
        "danger": "{color.base.red.600}"
      }
    }
  },
  "typography": {
    "font": {
      "body": "system-ui, -apple-system, Segoe UI, Roboto, sans-serif",
      "mono": "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"
    },
    "size": {
      "sm": "0.875rem",
      "md": "1rem",
      "lg": "1.125rem"
    },
    "weight": {
      "regular": 400,
      "medium": 500,
      "bold": 700
    },
    "lineHeight": {
      "tight": 1.25,
      "normal": 1.5
    }
  },
  "space": {
    "0": "0",
    "1": "0.25rem",
    "2": "0.5rem",
    "3": "0.75rem",
    "4": "1rem",
    "6": "1.5rem",
    "8": "2rem"
  },
  "radius": {
    "sm": "0.25rem",
    "md": "0.5rem",
    "lg": "0.75rem"
  },
  "shadow": {
    "sm": "0 1px 2px rgba(0,0,0,0.08)",
    "md": "0 6px 16px rgba(0,0,0,0.12)"
  },
  "motion": {
    "duration": {
      "fast": "120ms",
      "normal": "180ms",
      "slow": "240ms"
    },
    "easing": {
      "standard": "cubic-bezier(0.2, 0, 0, 1)",
      "emphasized": "cubic-bezier(0.2, 0, 0, 1.2)"
    }
  }
}
```

</details>

**Notes on `{...}` references:** This sample uses simple aliasing syntax to show intent. Your actual build pipeline may resolve aliases differently — the important part is maintaining a clean separation between **base** and **semantic** values. 🧠

---

## 🎨 Sample CSS variable output

<details>
<summary><strong>tokens.sample.css</strong> (click to expand) 🎨</summary>

```css
:root {
  /* surfaces */
  --kfm-color-surface-default: #ffffff;
  --kfm-color-surface-raised: #f8fafc;
  --kfm-color-surface-sunken: #f1f5f9;

  /* text */
  --kfm-color-text-default: #0f172a;
  --kfm-color-text-muted: #475569;
  --kfm-color-text-inverse: #ffffff;

  /* borders */
  --kfm-color-border-default: #e2e8f0;
  --kfm-color-border-focus: #2563eb;

  /* spacing */
  --kfm-space-2: 0.5rem;
  --kfm-space-4: 1rem;

  /* radius */
  --kfm-radius-md: 0.5rem;

  /* motion */
  --kfm-motion-fast: 120ms;
  --kfm-ease-standard: cubic-bezier(0.2, 0, 0, 1);
}
```

</details>

---

## 🧩 Using tokens in UI code

### 🧵 CSS usage
```css
.kfm-panel {
  background: var(--kfm-color-surface-raised);
  color: var(--kfm-color-text-default);
  border: 1px solid var(--kfm-color-border-default);
  border-radius: var(--kfm-radius-md);
  padding: var(--kfm-space-4);
}
```

### ⚛️ React usage (conceptual)
```tsx
export function Panel({ children }: { children: React.ReactNode }) {
  return <section className="kfm-panel">{children}</section>;
}
```

---

## ♿ Accessibility and UX guardrails

When modifying tokens, treat accessibility as **non-negotiable**:

- 🔎 Ensure readable contrast for:
  - text on surfaces
  - focus rings
  - map overlays + legends
- ⌨️ Focus states must remain visible (especially on map canvas + overlays)
- 🧭 Motion should be subtle and respect user preferences (e.g., reduced motion)

If a token change breaks focus visibility or contrast, it’s a regression even if “it looks nicer.” ✅

---

## 🔒 Governance & safety guardrails

Even though tokens are “just UI,” they still influence how data is revealed.

**Do not:**
- 🚫 bake sensitive coordinates, identifiers, or dataset-specific secrets into token files
- 🚫 add API keys / access tokens anywhere in this directory (tokens ≠ secrets)
- 🚫 introduce styling that encourages bypassing redaction rules (e.g., map affordances that imply restricted zoom/detail is available)

**Do:**
- ✅ keep tokens purely presentational
- ✅ prefer semantic tokens that can be reviewed for intent (“danger”, “focus”, “muted”)
- ✅ keep any sensitive behavior enforcement in the governed API + UI logic, not in “styling hacks”

---

## 🧪 Validation and “Definition of Done” ✅

When promoting tokens beyond “samples,” aim for contract-grade hygiene:

- [ ] Token JSON validates against a schema (recommended: `schemas/ui/…`)
- [ ] No secrets, credentials, or hidden identifiers in token files
- [ ] Contrast and focus checks pass (basic accessibility)
- [ ] Map UI overlays (legends, popups, panels) remain readable in both light/dark contexts
- [ ] Any docs referencing tokens have valid links/citations
- [ ] Visual review confirms no accidental “semantic drift” (e.g., warning now looks like success)

---

## 🔗 Related repo references 📚

These are useful for understanding how tokens fit into KFM’s governed repo structure and validation:

- 📘 `../../../../../docs/MASTER_GUIDE_v13.md`
- 🧾 `../../../../../docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md`
- 🧱 `../../../../../docs/standards/KFM_REPO_STRUCTURE_STANDARD.md`
- ✅ `../../../../../schemas/ui/` (recommended home for UI JSON schemas)

---

## 🧠 Quick philosophy (why this exists)

KFM’s UI is expected to be:
- responsive 📱💻
- accessible ♿
- safe and governance-respecting 🔒
- consistent across maps, story panels, and catalog workflows 🗺️📚

Tokens are the smallest building blocks that help us enforce that consistently. ✅
