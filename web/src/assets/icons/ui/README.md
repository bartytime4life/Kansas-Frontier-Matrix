# 🧩 UI Icons

![Scope](https://img.shields.io/badge/scope-UI%20icons-blue)
![Format](https://img.shields.io/badge/format-SVG-informational)
![Theming](https://img.shields.io/badge/theming-currentColor-success)
![A11y](https://img.shields.io/badge/a11y-required-critical)
![Provenance](https://img.shields.io/badge/provenance-tracked-9cf)

> [!NOTE]
> This folder is for **domain-neutral UI chrome icons** (navigation, actions, status, layout controls).  
> Keep these icons consistent so the app feels like **one product**, even when a domain applies an accent theme.

---

## 📍 Location

`web/src/assets/icons/ui/`

```text
🗂️ web/
└── 🗂️ src/
    └── 🗂️ assets/
        └── 🗂️ icons/
            ├── 🗂️ ui/            👈 you are here
            ├── 🗂️ domains/       (optional) domain-motif icons (Weather/History/etc)
            └── 🗂️ map/           (optional) map markers/symbols (if separated)
```

---

## 🧭 What belongs in `ui/`

Use this folder when the icon is **generic UI** and could appear anywhere:

- 🧭 Navigation: `menu`, `chevron-*`, `arrow-*`, `home`, `back`
- ✨ Actions: `add`, `edit`, `delete`, `download`, `share`, `copy`
- 🔎 Utility: `search`, `filter`, `settings`, `help`, `info`
- ✅ Status: `check`, `warning`, `error`, `loading`
- 🪟 Layout: `panel`, `collapse`, `expand`, `fullscreen`

**Not** a great fit for `ui/`:

- 🌦️ Domain-specific motifs (ex: a “temperature” icon with weather styling) → prefer `icons/domains/<domain>/`
- 🗺️ Map symbology (markers, pins, layer glyphs) → prefer a map-specific folder or style system

---

## ⚡ Golden Rules

- ✅ **SVG only** (vector, crisp at any zoom)
- 🎨 **No hard-coded colors** (use `currentColor`)
- 📐 **Consistent geometry** (same `viewBox` + baseline alignment)
- ♿ **Accessible by default** (decorative vs informative is explicit)
- 🧾 **License & source tracked** (no mystery icons)

---

## 📐 SVG “Contract” (Design + Tech)

| Rule ✅ | Why it matters 🎯 | Quick check 🔍 |
|---|---|---|
| `viewBox="0 0 24 24"` (recommended) | predictable sizing & alignment | icons snap to same grid |
| `stroke="currentColor"` / `fill="currentColor"` | theme + dark mode “just works” | no `#000`, no `rgb()` |
| avoid inline `style=""` | prevents theming bugs | prefer attrs + CSS |
| minimal groups/paths | smaller bundles + easier diffs | optimize with SVGO |
| no embedded rasters | keeps icons truly scalable | no `<image>` tags |
| consistent stroke style | cohesive look across UI | same cap/join rules |

> [!TIP]
> If the icon is line-based, prefer `stroke="currentColor"` and let the **button/text color** drive the icon color.

---

## 🏷️ Naming Convention

- ✅ `kebab-case.svg`
- ✅ short + semantic + UI-focused
- ✅ avoid synonyms (“trash” vs “delete” → pick one)

Examples:
- `chevron-down.svg`
- `arrow-left.svg`
- `download.svg`
- `settings.svg`
- `warning-triangle.svg`

> [!IMPORTANT]
> Treat filenames as a **public contract**. Renaming icons breaks imports.

---

## 🎨 Theming & Domain Accents

KFM uses **contextual theming** (domain accent colors) while keeping core components consistent.

**How that translates to icons:**
- 🧱 UI chrome icons stay **neutral** → they inherit `currentColor`.
- 🎯 Domain accents apply through:
  - CSS variables on containers (`--kfm-accent`)
  - domain-level component styles
  - (optional) domain-motif icon sets stored outside `ui/`

Example CSS idea (adjust to your design tokens):
```css
/* Example only: apply domain accent to “active” nav items */
.navItem--active {
  color: var(--kfm-accent);
}
```

---

## ♿ Accessibility (A11y)

### Decorative icons
If the icon is purely visual (button already has text, or label is elsewhere):

```tsx
<Icon aria-hidden="true" focusable="false" />
```

### Informative icons
If the icon conveys meaning on its own (rare; prefer icon + text):

```tsx
<Icon role="img" aria-label="Warning" />
```

### Icon-only buttons
Prefer labeling the **button**, not the SVG:

```tsx
<button type="button" aria-label="Open settings">
  <SettingsIcon aria-hidden="true" focusable="false" />
</button>
```

> [!NOTE]
> Don’t rely on color alone. If it’s important, back it with **text or an accessible label**.

---

## 🧰 Usage Patterns in React

Different bundlers handle SVGs differently — pick the pattern your `web/` build uses.

### Option A: SVG → React Component (SVGR-style)
```tsx
import { ReactComponent as DownloadIcon } from "@/assets/icons/ui/download.svg";

export function DownloadButton() {
  return (
    <button aria-label="Download">
      <DownloadIcon aria-hidden="true" focusable="false" />
    </button>
  );
}
```

### Option B: SVG as URL (image tag)
```tsx
import downloadUrl from "@/assets/icons/ui/download.svg";

export function DownloadButton() {
  return <img src={downloadUrl} alt="" aria-hidden="true" />;
}
```

> [!TIP]
> Prefer **Option A** for theming with `currentColor` (when available), and **Option B** only when you truly need an `<img>`.

---

## ⚙️ Optimization (Keep icons light)

When adding or updating icons:

- ✂️ remove unused layers
- 🧼 normalize to `currentColor`
- 🧯 run an SVG optimizer (example with `svgo`)

```bash
# Example (adjust paths/config to your repo)
npx svgo --multipass web/src/assets/icons/ui/*.svg
```

---

## 🧾 Provenance & Licensing

KFM is provenance-first — icons must be attributable too.

### ✅ Required for any non-original icon
Add a short provenance header at the top of the SVG file:

```svg
<!--
name: download
source: <where it came from>
license: <license name + version>
changes: <what you modified>
-->
```

> [!IMPORTANT]
> If an icon’s license is unclear → **do not commit it**.

---

## ➕ Adding a New Icon (Checklist)

- [ ] 🧭 Confirm it belongs in `ui/` (domain-neutral)
- [ ] 🏷 Name it in `kebab-case.svg`
- [ ] 📐 Normalize `viewBox` (recommend 24×24)
- [ ] 🎨 Use `currentColor` (no hard-coded palette)
- [ ] 🧼 Optimize SVG (SVGO or equivalent)
- [ ] ♿ Confirm a11y behavior (decorative vs labeled)
- [ ] 🧾 Add provenance header if not original
- [ ] 🧪 Verify in light/dark/high-contrast modes
- [ ] 🔁 Reuse instead of duplicating near-identical icons

---

## 🧪 Review “Gotchas”

| ✅ Do | ❌ Don’t |
|---|---|
| keep geometry consistent | mix random viewBox sizes |
| use `currentColor` | bake in `#000000` |
| label icon-only controls | ship unlabeled icon buttons |
| optimize before commit | commit giant unoptimized SVGs |
| track source/license | add “unknown origin” assets |

---

## 🗺️ Mini Flow (from idea → shipped icon)

```mermaid
flowchart LR
A[🎨 Design / Source] --> B[📐 Normalize SVG Contract]
B --> C[🧼 Optimize (SVGO)]
C --> D[📁 Save in ui/]
D --> E[🧱 Use in Component]
E --> F[♿ A11y + Theme QA]
```

---

## 🔗 Related Docs

- 📘 Master Guide: `../../../../../docs/MASTER_GUIDE_v13.md`
- 🧱 Architecture: `../../../../../docs/architecture/`
- ⚖ Governance / Ethics: `../../../../../docs/governance/ETHICS.md`
- 🧭 Repo structure standard: `../../../../../docs/standards/KFM_REPO_STRUCTURE_STANDARD.md`
- 📝 Markdown work protocol: `../../../../../docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md`
