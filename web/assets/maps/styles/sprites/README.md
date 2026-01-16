# 🧩 Map Sprites (Icon Atlas)

`License: MIT` · `Format: PNG + JSON` · `Map renderer: MapLibre/Mapbox-style sprites` · `KFM standard: provenance-first`

Sprites are the tiny map icons (POIs, markers, legend symbols, UI glyphs) used by our web map styles. They ship as a **PNG atlas** plus a **JSON index** that tells the renderer where each icon lives inside the atlas.

This folder supports KFM’s “trustable map UI” goal: the interface should be clear, consistent, and auditable (down to the visual language we use to represent layers and features). [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 📦 What lives in this folder

Typical sprite set layout (names vary by style/theme):

```text
📁 web/
  📁 assets/
    📁 maps/
      📁 styles/
        📁 sprites/
          📄 README.md
          🖼️ <sprite>.png
          🧾 <sprite>.json
          🖼️ <sprite>@2x.png
          🧾 <sprite>@2x.json
          📁 src/ (optional but recommended)
            📁 svg/ (source icons)
            📁 meta/ (licenses, notes, provenance)
```

### ✅ Expected outputs (runtime files)
- **`<sprite>.png`** — the 1× atlas image
- **`<sprite>.json`** — index of icon names → `{x,y,width,height,(optional) sdf}`
- **`<sprite>@2x.png`** — the 2× (retina) atlas
- **`<sprite>@2x.json`** — index for retina atlas (often identical dimensions scaled, depending on build tool)

> [!NOTE]
> This directory is under `web/assets/...` because KFM’s visualization layer is browser-based and uses open web mapping libraries (e.g., MapLibre GL / Leaflet). [oai_citation:1‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw)

---

## 🗺️ How the map loads sprites (so you can debug fast)

In a MapLibre/Mapbox style JSON, the `sprite` property is a **base path** (no extension). The renderer requests:

- `<sprite>.json` and `<sprite>.png`
- `<sprite>@2x.json` and `<sprite>@2x.png` on high-DPI screens

Example (conceptual):

```json
{
  "version": 8,
  "name": "KFM Base",
  "sprite": "/assets/maps/styles/sprites/kfm",
  "sources": {},
  "layers": []
}
```

And an icon is referenced in layers by its **sprite name**:

```json
{
  "id": "poi-historic-sites",
  "type": "symbol",
  "source": "pois",
  "layout": {
    "icon-image": "poi-historic-site",
    "icon-size": 1
  }
}
```

---

## 🧭 Naming & design conventions (keep icons consistent)

### 🏷️ Naming
- Use **kebab-case**: `poi-trailhead`, `marker-selected`, `event-battle`
- Use **stable semantic names**, not visual ones:
  - ✅ `poi-courthouse`
  - ❌ `blue-pin`, `small-circle`

### 📐 Sizing
Pick one consistent “canvas” per icon family and stick to it:
- Common defaults: **24×24** (1×) and **48×48** (2×)
- Keep a **1–2 px safe padding** so strokes don’t clip

### 🎨 Visual style
- Prefer **simple silhouettes** and avoid tiny text (unreadable on maps)
- Keep **stroke weight consistent** across the set
- Use transparency; never bake a background box unless it’s part of the design language

### 🧊 SDF vs non-SDF (coloring behavior)
If your renderer/tooling supports it:
- **SDF icons** (signed distance fields) → can be recolored in style (`icon-color`, halos, etc.)
- **Non-SDF icons** → render with baked colors (use sparingly; harder to theme)

> [!TIP]
> If we want the icon to change color by layer/category, make it monochrome + SDF-friendly.

---

## 🧾 Provenance & licensing rules (KFM-grade)

KFM treats **citations + metadata as first-class** and avoids “black box” UI elements. That philosophy applies to icons too: sprites communicate meaning, and meaning must be traceable. [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### ✅ Required: track icon sources & licenses
KFM explicitly tracks licensing and usage terms across assets and outputs; where multiple sources combine, the **most restrictive license governs** the combined output. [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

**So for sprites:**
- If **any** icon comes from a third party, add an attribution record (recommended file: `src/meta/ATTRIBUTION.md` or `src/meta/licenses.yml`)
- If icons are derived from datasets/brands, record:
  - source
  - author/organization
  - license
  - modifications (if any)

#### 📋 Attribution table template
Create/maintain something like:

| Icon name | Source | License | Notes |
|---|---|---|---|
| `poi-historic-site` | (describe origin) | (license) | edited: stroke normalized |
| `poi-water` | (describe origin) | (license) | original + recolor |

> [!IMPORTANT]
> **No output artifact can be less restricted than its inputs**. That’s a core KFM invariant (classification + restrictions propagate). [oai_citation:4‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### 🧿 Sensitive-location semantics
KFM has an explicit policy of **not showing precise sensitive locations without permission** and supports UI safeguards like **generalizing/blurring** sensitive map content. [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:6‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

**For sprites, that means:**
- Don’t introduce “tempting” icons for restricted layers that shouldn’t surface publicly (e.g., “sacred-site-pin”) without corresponding policy + UI gating
- Prefer neutral icons when a feature’s representation might imply precision or certainty we don’t have

---

## 🛠️ Workflow: add/update an icon (recommended)

> [!NOTE]
> Tooling varies by repo setup. If you see a build script in the frontend toolchain, use it. If not, you can generate MapLibre-compatible sprites with standard sprite builders (e.g., spritezero-style tooling) and drop the outputs here.

### 1) Add the source icon (recommended structure)
- Put original **SVG**s in: `web/assets/maps/styles/sprites/src/svg/`
- Keep source SVGs **clean**:
  - no embedded rasters
  - strokes aligned to pixel grid when possible
  - consistent viewBox

### 2) Update attribution metadata
- Add a row for the new icon in `src/meta/ATTRIBUTION.md` (or equivalent)

### 3) Rebuild the atlas
Generate:
- `<sprite>.png` + `<sprite>.json`
- `<sprite>@2x.png` + `<sprite>@2x.json`

> [!TIP]
> If the UI seems unchanged after updating sprites, it’s often **cache**. Consider versioning the sprite base name (e.g., `kfm-v2`) when making larger updates.

### 4) Verify in the UI
- Confirm the style’s `sprite` path points to the correct base name
- Load a symbol layer that references your icon name
- Check both standard and retina displays (or device emulation)

---

## ✅ PR checklist (fast CI sanity)

- [ ] Icon name is **kebab-case** and semantically stable
- [ ] Icon is readable at 1× and 2×
- [ ] Atlas rebuilt (PNG + JSON, both 1× and 2×)
- [ ] Attribution/License record updated (if applicable) [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- [ ] No icon implies restricted/sensitive precision without UI/policy support [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:9‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧯 Troubleshooting

### “Icon not found” / blank symbol
- The `icon-image` value must exactly match a key in `<sprite>.json`
- Confirm the map style’s `sprite` base path is correct
- Make sure the sprite assets are actually served by the web server (correct static path)

### Icons look blurry
- Ensure `@2x` files exist and were generated correctly
- Avoid fractional icon sizes unless you intend interpolation (`icon-size: 0.75` can blur)
- Check your SVG source aligns well to pixel boundaries

### Wrong colors / can’t recolor
- If the sprite entry isn’t SDF-capable, `icon-color` won’t behave as expected
- Decide: **SDF monochrome** (themeable) vs **full-color** (fixed appearance)

---

## 🔗 Related KFM principles (why this folder matters)

- **Provenance-first UI**: Users should be able to inspect sources behind what they see. [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- **API boundary & governance**: UI should not “shortcut” governed layers (policy + access controls live behind APIs). [oai_citation:11‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- **Sovereignty & classification propagation**: Restrictions follow data and derivatives end-to-end; UI safeguards apply too. [oai_citation:12‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)