# 🧩 UI Illustrations

![Scope](https://img.shields.io/badge/scope-web%20ui-0ea5e9) ![Assets](https://img.shields.io/badge/type-illustrations-22c55e) ![Governance](https://img.shields.io/badge/guardrails-provenance%E2%80%91first-f97316) ![Formats](https://img.shields.io/badge/formats-svg%20%7C%20png%20%7C%20webp-64748b)

Static **UI-only** illustrations for the KFM web client (React / Map UI). 🎛️🗺️  
Use these for onboarding, empty states, help overlays, and “how-to-use-the-interface” visuals — **not** for evidence, datasets, or story content.

---

## 📦 Location

```text
📁 web/
  📁 assets/
    📁 media/
      📁 illustrations/
        📁 ui/
          📄 README.md  👈 you are here
```

---

> [!IMPORTANT]
> **This folder is for UI visuals only.**  
> If an image contains **data**, **maps**, **charts**, **historical claims**, or anything that could be read as **evidence**, it does **not** belong here. That content must live with governed narrative/evidence workflows (Story Nodes + catalogs/provenance) — not as “random static UI art.”

---

## 🧭 Quick links

- [✅ What belongs here](#-what-belongs-here)
- [🚫 What does not belong here](#-what-does-not-belong-here)
- [🛡️ Governance guardrails](#️-governance-guardrails)
- [📝 Naming rules](#-naming-rules)
- [🖼️ Formats & optimization](#️-formats--optimization)
- [🧩 Using in React](#-using-in-react)
- [🏷️ Metadata & licensing](#️-metadata--licensing)
- [✅ PR checklist](#-pr-checklist)
- [🔗 Related docs](#-related-docs)

---

## ✅ What belongs here

UI illustrations that are **generic** and **non-evidentiary**, such as:

- 🧭 **Onboarding**: “how to use the map”, “how to open the layer catalog”, “how to filter”
- 🫥 **Empty states**: “no results”, “no layers selected”, “offline”
- 🆘 **Help** / “learn the UI” overlays
- 🧰 **System states**: loading, error, permission denied (generic)
- 🎨 **Decorative** UI polish that does **not** assert facts

---

## 🚫 What does not belong here

| 🚫 Don’t put this here | ✅ Put it instead |
|---|---|
| Evidence images (scans, photos, historical maps) | `data/processed/**` + catalog records (STAC/DCAT/PROV) |
| Map screenshots that imply real claims (“X happened here”) | Story Node assets + citations/provenance |
| Charts/plots from real datasets | Generated artifacts treated as evidence + catalogs + API |
| Story-specific illustrations tied to a narrative | `docs/reports/story_nodes/**/assets/` (governed) |
| Anything that must be “true” | Anywhere governed by provenance + review gates |

> [!TIP]
> If you *feel like you should cite it*, it probably doesn’t belong in this folder. 📌

---

## 🛡️ Governance guardrails

KFM has a strict “pipeline ordering” and **the UI must not bypass the API/data provenance boundaries**.  
This folder is intentionally **boring**: it’s for UI support visuals, not content that carries truth-claims.

**Rules of thumb:**
- ✅ UI illustrations may **explain controls** (buttons, panels, gestures).
- ❌ UI illustrations may not **introduce new facts** about Kansas history, people, events, locations, or datasets.
- ✅ If you need a map/image/chart in the UI, it should typically be **served from cataloged data via the API**, not shipped as a static file here.
- ✅ If you must ship a static image that’s “content,” treat it like content: governed, cited, and versioned (Story Nodes).

---

## 📝 Naming rules

Keep names **predictable**, **grep-able**, and **stable**. 🧠

### ✅ File naming pattern

```text
ui-<category>--<slug>--<variant>@<scale>.<ext>
```

**Where:**
- `<category>` = `onboarding` | `empty-state` | `help` | `system`
- `<slug>` = short kebab-case intent (`no-results`, `select-layer`, `offline`)
- `<variant>` = `light` | `dark` | `mono` | `illustrated` | `wireframe` (use only if needed)
- `<scale>` = omit for SVG; for raster: `@1x`, `@2x`, `@3x`

### 📌 Examples

- `ui-empty-state--no-results--light.svg`
- `ui-onboarding--open-layer-catalog--dark.svg`
- `ui-system--offline--illustrated@2x.webp`

> [!NOTE]
> If you introduce variants (dark/light, mobile/desktop), do so intentionally and keep the set small. 🌙☀️📱🖥️

---

## 🖼️ Formats & optimization

### Preferred formats ✅
- **SVG** 🧬 for most UI illustrations (scales cleanly, theme-friendly)
- **WebP** 🪶 for raster illustrations when SVG is not appropriate
- **PNG** 🧱 only when transparency is required and WebP isn’t viable

### Avoid 🚫
- Large uncompressed PNG/JPG
- Text-heavy images (prefer real HTML text for accessibility + i18n)
- “Evidence-looking” visuals in a UI folder (maps, documents, charts)

### Optimization expectations ⚡
- Keep file size as small as reasonable:
  - SVG: remove editor metadata, simplify paths
  - Raster: export at intended size, compress, provide @2x only when needed
- Strip junk: hidden layers, unused defs, embedded bitmaps in SVG unless justified

<details>
  <summary><strong>🧪 Suggested optimization commands (optional)</strong></summary>

```bash
# SVG (example)
npx svgo --multipass ./web/assets/media/illustrations/ui/**/*.svg

# Raster (example)
# Use your repo’s preferred tooling (imagemin/sharp/etc.) if available
```

</details>

---

## 🧩 Using in React

### ✅ Decorative illustration (no meaning)
```tsx
<img
  src={new URL("./ui-empty-state--no-results--light.svg", import.meta.url).toString()}
  alt=""
  aria-hidden="true"
  loading="lazy"
/>
```

### ✅ Informative illustration (user needs it)
```tsx
<img
  src={new URL("./ui-onboarding--open-layer-catalog--dark.svg", import.meta.url).toString()}
  alt="Illustration showing how to open the layer catalog."
  loading="lazy"
/>
```

### 🎛️ Theme switching
If you ship both `--light` and `--dark` variants, switch via theme state (don’t auto-invert assets).

---

## 🏷️ Metadata & licensing

Even though these are “UI assets,” we still treat attribution seriously. 🧾✅

### When you MUST add metadata
Add metadata (sidecar or manifest entry) if the illustration is:
- sourced from anywhere outside the repo 📎
- AI-assisted/generated 🤖
- derived from a screenshot or a third-party UI kit 🧩
- non-trivial / likely to be reused in multiple places 🔁

### Recommended metadata approaches
Pick one project-wide and stay consistent:

1) **Sidecar file** per asset  
`ui-empty-state--no-results--light.svg.meta.json`

2) **Single manifest** for this folder  
`manifest.ui-illustrations.json` (or `.yml`)

#### Example sidecar (minimal)
```json
{
  "id": "ui-empty-state--no-results--light",
  "title": "Empty state: No results",
  "purpose": "UI empty state illustration",
  "source": {
    "type": "figma",
    "ref": "Figma file / frame reference here"
  },
  "license": "Internal / CC-BY-4.0 / etc",
  "attribution": "Author or source attribution here",
  "notes": "Anything a future maintainer will thank you for."
}
```

> [!WARNING]
> Do **not** add assets with unclear licensing. If you can’t explain “where it came from and under what terms,” it’s not merge-ready. 🚫⚖️

---

## ✅ PR checklist

Before merging new UI illustrations:

- [ ] 🧭 **Correct folder** (`ui/` only; not story/evidence)
- [ ] 🏷️ **Name follows pattern** and is descriptive
- [ ] ⚡ **Optimized** (SVGO/compressed; no editor cruft)
- [ ] ♿ **Accessible** usage (alt text or `alt=""` + `aria-hidden`)
- [ ] 🌙 **Theme-safe** (works in light/dark or has explicit variants)
- [ ] 🧾 **License/attribution included** if not purely original
- [ ] 🔍 **No factual claims embedded** (no “evidence by illustration”)

---

## 🔗 Related docs

- 📘 `docs/MASTER_GUIDE_v13.md` — canonical pipeline + invariants  
- 🧱 `docs/standards/` — profiles & governed standards (STAC/DCAT/PROV, etc.)
- ⚖️ `docs/governance/` — ethics, sovereignty, review triggers
- 📰 `docs/reports/story_nodes/` — governed story content + story assets (draft/published)

---

🧠 **Design intent:** keep UI visuals lightweight, reusable, and clearly separated from evidence-bearing media — so KFM stays trustworthy and provenance-clean. ✅
