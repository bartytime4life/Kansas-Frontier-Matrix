# 🎨 UI Illustrations (Web)

> 📍 **Path:** `web/assets/media/illustrations/ui/`  
> 🧭 **Purpose:** Friendly, lightweight illustrations for the **KFM** web interface (onboarding, empty-states, helper diagrams, etc.).

---

## 🧩 What this folder is for

This directory contains **non-map UI illustrations** used throughout the Kansas Frontier Matrix (KFM) web app—think:

- 🫧 **Empty states** (no results, no layers selected, missing filters)
- 🧭 **Onboarding / walkthrough** visuals (layers → timeline → provenance → stories)
- 🧠 **Feature explainers** (Focus Mode, citations, evidence panels)
- 🧱 **Light UI diagrams** (high-level conceptual visuals — *not* data charts)

> ✅ **Rule of thumb:** If it’s an illustration that supports the UI experience (without being “the UI itself”), it belongs here.

---

## 🚫 What does *not* belong here

Please keep this folder clean and predictable:

- 🧷 **Icons / pictograms** used in buttons, toolbars, map markers  
  → put them in an **icons** folder (e.g., `web/assets/media/icons/`), not here.
- 🗺️ **Map symbology sprites** (pins, cluster icons, layer glyphs)  
  → keep separate from illustrations to avoid mixing concerns.
- 🖼️ **Screenshots** of the product UI  
  → use docs/media folders (or README assets) so they don’t ship to prod by accident.
- 🎬 **Videos / heavy animations**  
  → use a dedicated media folder (and keep bundle size sane).
- 📚 **Story Node-specific images**  
  → live with Story Nodes under `docs/reports/story_nodes/**/assets/` (so they remain tied to narrative/evidence context).

---

## 🗂️ Suggested organization

If/when this folder grows, prefer predictable subfolders:

```text
📁 web/assets/media/illustrations/ui/
├── 📁 empty-states/         # no-results, no-data, not-found, etc.
├── 📁 onboarding/           # walkthrough steps, “getting started”
├── 📁 feature-explainers/   # provenance, Focus Mode, citations, etc.
├── 📁 system-states/        # error, success, loading (illustrative)
├── 📄 manifest.json         # optional: provenance/license metadata for assets
└── 📄 README.md             # you are here ✨
```

> 🧠 If you don’t need subfolders yet, keep it flat—but keep naming consistent.

---

## 🏷️ Naming conventions

Keep names **kebab-case**, descriptive, and stable:

✅ Good:
- `empty-state.no-results.svg`
- `onboarding.layers-timeline.svg`
- `feature.provenance-inspector.svg`
- `system.error-generic.svg`

🚫 Avoid:
- `final_v7_REAL.svg`
- `Illustration 3.svg`
- `noResults(2).png`

### 🌗 Theme variants

If an illustration must differ between themes, use suffixes:

- `…​.light.svg`
- `…​.dark.svg`

Example:
- `feature.provenance-inspector.light.svg`
- `feature.provenance-inspector.dark.svg`

If the artwork can theme via CSS variables (preferred for SVG), do that instead.

---

## 🖼️ File formats

| Format | Use it for | Notes |
|---|---|---|
| **SVG** ✅ | Most UI illustrations | Preferred. Crisp at any size, smallest when optimized. |
| **PNG** | Complex raster art / textures | Use only when SVG isn’t practical. Export @2x for retina if needed. |
| **WebP** | Raster illustrations for web | Great compression; verify browser support in target stack. |
| **Lottie (JSON)** | Small looping motion | Only if we’re already using Lottie and the file stays small. |

---

## ⚡ Performance budgets (keep the UI fast)

Illustrations ship with the web app, so treat them like code:

- 🎯 **Target size:**  
  - SVG: aim for **≤ 100–200 KB** each  
  - PNG/WebP: aim for **≤ 300–500 KB** each (lower is better)
- 🧹 **Optimize:** remove metadata, simplify paths, compress raster exports.
- 🔁 **Avoid duplicates:** reuse common empty-state base art where possible.

> 🧭 When in doubt, prioritize *clarity + speed* over decoration.

---

## ♿ Accessibility rules

Every illustration must be either:

### 1) Decorative 🫧
- Mark as decorative so it doesn’t add noise to screen readers.
- Example: `alt=""` and `aria-hidden="true"` (implementation depends on framework)

### 2) Informative 🧠
- Provide meaningful alt text (what it communicates, not what it looks like).
- Example: `"No layers selected — open the layer catalog to add data."`

> ✅ If the illustration is the *only* cue for a state, it is **informative**.

---

## 🔎 Provenance & licensing (non-negotiable)

KFM’s UI is **trust-centered**. Even for artwork, we must be able to answer:

- Who created it?
- What license allows us to ship it?
- Is it derived from third-party work? (and if so, where’s the attribution?)

### 📄 Recommended: `manifest.json`

Add (or maintain) a lightweight asset manifest for this folder:

```json
[
  {
    "id": "empty-state.no-results",
    "file": "empty-states/empty-state.no-results.svg",
    "purpose": "Shown when a search returns no datasets or story nodes.",
    "source": "In-house design",
    "author": "KFM Design Team",
    "license": "CC0-1.0 OR Project-License-Compatible",
    "notes": "SVG optimized; supports dark mode via CSS vars."
  }
]
```

> 🛡️ Do **not** add assets with unclear licensing or unknown origin.

---

## 🧩 Using illustrations in the web app

Common patterns (adjust to your bundler/framework):

### ✅ Import as a URL (safe default)
```ts
import noResultsUrl from "@/assets/media/illustrations/ui/empty-states/empty-state.no-results.svg";

export function EmptyState() {
  return (
    <img
      src={noResultsUrl}
      alt="No results — try adjusting your search or filters."
      loading="lazy"
    />
  );
}
```

### ✅ Inline SVG as a component (when you need styling)
```ts
import { ReactComponent as ProvenanceExplainer } from "@/assets/media/illustrations/ui/feature-explainers/feature.provenance-inspector.svg";

export function HelpPanel() {
  return (
    <div aria-label="How provenance works">
      <ProvenanceExplainer />
    </div>
  );
}
```

> 🌗 If you inline SVGs, prefer CSS variables and avoid hardcoded colors that break dark mode.

---

## ✅ Definition of Done (DoD) checklist

- [ ] File named using the conventions above
- [ ] SVG/raster is optimized (no giant exports)
- [ ] Dark mode handled (variant files or CSS-variable theming)
- [ ] Accessibility covered (decorative vs informative)
- [ ] Provenance + license recorded (manifest or sidecar metadata)
- [ ] No sensitive info (no real coordinates, no private datasets, no screenshots)

---

## 🔗 Related (project) docs

- `docs/MASTER_GUIDE_v13.md` 📘 (canonical pipeline + invariants)
- `docs/standards/` 🧾 (profiles, governance, metadata expectations)
- `docs/reports/story_nodes/**/assets/` 🎬 (story-scoped visuals live with their narrative)

---

<details>
<summary>💡 Illustration ideas that map well to KFM UI</summary>

- 🗂️ “No layers selected” → gently point to the layer catalog  
- 🕰️ “Set a time range” → show timeline slider concept  
- 🧾 “View provenance” → show “source → processing → output” concept  
- 🧠 “Focus Mode” → show story + map + evidence working together  
- 🧭 “Search tips” → show filters, tags, bounding box

</details>