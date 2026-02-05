<div align="center">

# 📚 Story Icons

_Iconography for **Story Nodes** + **Focus Mode** — built to communicate trust, provenance, and narrative intent at a glance._

![KFM](https://img.shields.io/badge/KFM-Story%20Icons-0b7285?style=flat)
![React](https://img.shields.io/badge/React-UI-61DAFB?logo=react&logoColor=000&style=flat)
![TypeScript](https://img.shields.io/badge/TypeScript-safe%20imports-3178C6?logo=typescript&logoColor=fff&style=flat)
![SVG](https://img.shields.io/badge/Format-SVG%20preferred-FFB300?logo=svg&logoColor=000&style=flat)

</div>

---

## 🎯 What lives here?

This folder holds **Story UI icons** used across the KFM web frontend (React + TypeScript) wherever the interface needs to visually communicate:

- 🧾 **Story Node structure** (story, section, citation, entity link, etc.)
- 🧭 **Map + timeline narrative cues** (scrollytelling / “Next” / “jump to time”)
- 🛡️ **Trust & governance states** (provenance-linked, AI-labeled, restricted, sensitive/blurred)

KFM’s frontend is organized under `web/src/` and includes UI components like a StoryPanel alongside mapping and timeline controls, with static assets (including icons) living in the same front-end codebase.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🧠 Why these icons are “trust-critical”

KFM treats Story Nodes as **machine-ingestible storytelling**: a Story Node is a Markdown document with semantic annotations + citations, designed so claims can be traced back to evidence.  [oai_citation:1‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

Focus Mode (the reading experience that pairs story with map + timeline context) enforces strict rules to preserve trust — including:

- ✅ **Only provenance-linked content** is allowed to appear (hard gate).
- 🤖 **AI content must be opt-in + clearly labeled**, with uncertainty/confidence.
- 🗺️ **No sensitive location leaks** — the map should generalize/omit restricted locations.  [oai_citation:2‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

These icons are part of that contract: **they are UI signals that reinforce the rules**.

> 🔎 Rule-of-thumb: Focus Mode operationalizes “no new narrative without sources, no data without provenance.”  [oai_citation:3‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🗂️ Folder layout

Recommended structure (adapt as needed to match the repo’s current state):

```text
web/src/assets/icons/story/
├── README.md                 # 👈 you are here
├── index.ts                  # 📦 barrel exports (recommended)
├── registry.ts               # 🧭 semantic mapping (recommended)
├── ai-*.svg                  # 🤖 AI-related affordances
├── cite-*.svg                # 🧾 citations / evidence / provenance
├── entity-*.svg              # 🧍 people / 🧭 places / 📜 documents / 🗓️ events
├── nav-*.svg                 # ⏭️ next / back / jump / scroll cues
└── status-*.svg              # 🔒 restricted / ⚠️ warning / 🫥 redacted
```

---

## 🧩 Icon design spec

### ✅ Preferred format
- **SVG first** (crisp at any scale, small payload, theme-friendly).
- Use raster images only when SVG is genuinely inappropriate (rare).

### 📐 Grid & geometry
- Target a **24×24** coordinate system:
  - `viewBox="0 0 24 24"`
- Avoid hardcoding pixel dimensions (`width`/`height`) unless required by tooling.

### 🎨 Color & theming
- Prefer `currentColor` so icons inherit text color:
  - `fill="currentColor"` **or** `stroke="currentColor"`
- Avoid “brand colors” inside the SVG unless the icon is explicitly a badge/label.

### 🧼 Keep SVGs clean
- No embedded rasters.
- Minimal paths.
- Remove editor metadata (Illustrator/Inkscape cruft).

---

## 🏷️ Naming conventions

Use **kebab-case** and lead with intent:

- `cite-source.svg` ✅
- `ai-generated.svg` ✅
- `status-locked.svg` ✅
- `entity-place.svg` ✅
- `nav-next.svg` ✅

If an icon is **specifically tied to a KFM trust rule**, encode that in the name:

- `status-provenance-ok.svg`
- `status-provenance-missing.svg`
- `status-sensitive-blurred.svg`

---

## ♿ Accessibility rules

Icons are either:

### 1) Decorative (most common)
- Must not be announced by screen readers:
  - `aria-hidden="true"`
  - `focusable="false"` (helps in some SVG contexts)

### 2) Informative (rare)
- If the icon conveys meaning by itself (e.g., a lock meaning restricted), it needs a label:
  - `role="img"`
  - `aria-label="Restricted"`

✅ Example (decorative icon next to visible text):

```tsx
import { ReactComponent as CiteSourceIcon } from "./cite-source.svg";

export function EvidenceChip() {
  return (
    <span className="EvidenceChip">
      <CiteSourceIcon aria-hidden="true" focusable="false" />
      <span>Has citations</span>
    </span>
  );
}
```

✅ Example (icon-only button):

```tsx
import { ReactComponent as NavNextIcon } from "./nav-next.svg";

export function NextButton() {
  return (
    <button type="button" aria-label="Next section">
      <NavNextIcon aria-hidden="true" focusable="false" />
    </button>
  );
}
```

---

## 🧭 Semantic icon groups

These groups reflect how KFM’s story system works (Story Nodes + Focus Mode):

### 🧾 Provenance & evidence
Use these when representing:
- citations / references
- “provenance-linked only” gating (hard rule)  [oai_citation:4‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

Suggested files:
- `cite-source.svg`
- `cite-footnote.svg`
- `status-provenance-ok.svg`
- `status-provenance-missing.svg` (⚠️ should be rare in production UI)

### 🤖 AI (opt-in + transparent)
AI indicators should only appear when the user explicitly opts in, and should be clearly labeled.  [oai_citation:5‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

Suggested files:
- `ai-generated.svg`
- `ai-summary.svg`
- `ai-suggestion.svg`

### 🔒 Governance & sensitivity
KFM supports CARE-aware restrictions and expects the UI to reflect that (e.g., restricted/withdrawn content, content warnings).  [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

Suggested files:
- `status-locked.svg`
- `status-warning.svg`
- `status-redacted.svg`
- `status-sensitive-blurred.svg` (paired with map generalization behavior)  [oai_citation:7‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### 🗺️ Narrative navigation
Used for scrollytelling / “Next” / jump-to-map / jump-to-time patterns.

Suggested files:
- `nav-next.svg`
- `nav-prev.svg`
- `nav-jump-to-map.svg`
- `nav-jump-to-time.svg`

---

## 🧱 Recommended exports

Create a barrel export for ergonomic imports (tree-shake friendly in most modern bundlers):

```ts
// web/src/assets/icons/story/index.ts
export { ReactComponent as CiteSourceIcon } from "./cite-source.svg";
export { ReactComponent as AiGeneratedIcon } from "./ai-generated.svg";
export { ReactComponent as StatusLockedIcon } from "./status-locked.svg";
```

Optionally maintain a semantic registry (so UI code depends on meaning, not filenames):

```ts
// web/src/assets/icons/story/registry.ts
import { CiteSourceIcon, AiGeneratedIcon, StatusLockedIcon } from "./index";

export const StoryIcons = {
  provenance: {
    cited: CiteSourceIcon,
  },
  ai: {
    generated: AiGeneratedIcon,
  },
  status: {
    locked: StatusLockedIcon,
  },
} as const;
```

---

## ➕ Adding a new icon

1. ✅ Add the SVG to this folder using the naming rules above.
2. 🧼 Optimize it (SVGO recommended):
   - `npx svgo your-icon.svg`
3. 📦 Export it in `index.ts`.
4. 🧭 If it’s semantic (AI / provenance / restricted), add it to `registry.ts`.
5. 🧪 Validate at common UI sizes (16/20/24).
6. 🛡️ If it signals a trust/gov rule (AI or sensitive), ensure the UI behavior matches the rule:
   - AI must be **opt-in + labeled**  [oai_citation:8‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
   - Sensitive locations must be **generalized/omitted** (icon alone is not enough)  [oai_citation:9‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## ✅ Review checklist (PR-ready)

- [ ] SVG uses `viewBox="0 0 24 24"` (or documented alternative).
- [ ] Uses `currentColor` (or documented reason not to).
- [ ] No inline editor metadata / embedded rasters.
- [ ] Works on light/dark backgrounds.
- [ ] Decorative icons are `aria-hidden`.
- [ ] Icon meaning is consistent with Focus Mode rules (trust cues are not decorative).  [oai_citation:10‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

<details>
<summary>📚 Project grounding (why this README is shaped this way)</summary>

- Story Nodes are Markdown-based narrative artifacts with semantic annotations + citations, and must include provenance for claims.  [oai_citation:11‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- Focus Mode enforces provenance-only display, opt-in AI labeling, and safeguards against sensitive location leakage.  [oai_citation:12‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- The KFM web frontend lives under `web/` as a React + TypeScript app with story/mapping UI components and static assets (like icons).  [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- CARE-aware restrictions and UI signaling (e.g., locks/warnings) are part of KFM’s governance expectations.  [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

</details>
