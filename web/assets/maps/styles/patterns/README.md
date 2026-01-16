# 🧩 Map Pattern Tiles (Textures) — KFM

![KFM](https://img.shields.io/badge/KFM-Living%20Atlas%20Platform-1f6feb?style=flat)
![Maps](https://img.shields.io/badge/Maps-Styles%20%26%20Symbology-2b8a3e?style=flat)
![MapLibre](https://img.shields.io/badge/Renderer-MapLibre%20GL%20JS-0b7285?style=flat)
![Assets](https://img.shields.io/badge/Asset%20Type-Pattern%20Tiles-7950f2?style=flat)

**Path:** `web/assets/maps/styles/patterns/` 📁🗺️🎨

Tileable textures (hatch, dots, stipple, etc.) used by **KFM’s web map styles** to communicate meaning beyond color (categories, uncertainty, emphasis, “historic overlay”, etc.). Patterns are especially helpful for **legends**, **overlapping layers**, and **accessibility**.

> [!NOTE]
> KFM’s UI and AI outputs are designed to be **provenance-first**: users should be able to inspect “what is this?” and trace it back to sources/choices. Treat these symbology assets the same way—no mystery textures.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 📚 Table of Contents

- [🧭 Where patterns fit in KFM](#-where-patterns-fit-in-kfm)
- [✅ What belongs in this folder](#-what-belongs-in-this-folder)
- [🧱 Technical requirements](#-technical-requirements)
- [🏷️ Naming conventions](#️-naming-conventions)
- [🧾 Provenance & licensing](#-provenance--licensing)
- [➕ Adding a new pattern](#-adding-a-new-pattern)
- [🗺️ Using patterns in MapLibre styles](#️-using-patterns-in-maplibre-styles)
- [🧪 QA checklist](#-qa-checklist)
- [🛠️ Troubleshooting](#️-troubleshooting)
- [📎 References](#-references)

---

## 🧭 Where patterns fit in KFM

KFM’s **web front-end** includes a map viewer powered by **MapLibre GL JS** (2D) and may also integrate 3D visualization elsewhere (e.g., Cesium). Patterns in this folder are intended for the **2D MapLibre style system**, where they show up as part of the map’s symbology and legends.  [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

A related design document also describes the `web/` frontend as browser-based and using open mapping libraries like MapLibre/Leaflet.  [oai_citation:4‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)

---

## ✅ What belongs in this folder

Put **tileable pattern source assets** here—small repeating textures intended for map styling:

- ✅ Polygon fill textures (e.g., farmland hatch, “uncertain extent” stipple)
- ✅ Line textures (rare; often better as `line-dasharray`, but sometimes `line-pattern` is useful)
- ✅ Neutral “legend swatch” textures that match map rendering

Do **not** put here:

- ❌ Point icons / POI markers (those belong with sprite/icon assets, not patterns)
- ❌ Large illustrations, banners, photos (not tileable; not patterns)

---

## 🧱 Technical requirements

Patterns are only valuable if they render **cleanly**, **repeat seamlessly**, and **don’t bloat** map assets.

### Recommended formats
- **Preferred source:** `SVG` (easy to edit + can generate crisp sprites)
- **Also acceptable:** `PNG` (when pixel-perfect is required)

### Recommended tile sizes (pick one)
- **32×32** (small, subtle textures)
- **64×64** (default “safe” size)
- **128×128** (use sparingly; can create visual noise at low zooms)

> [!TIP]
> If a pattern must scale by zoom level, consider providing **small/medium/large** variants and switching using a zoom expression in the style JSON (example below).

### Visual rules (keep things readable)
- Seamless edges: **left edge must match right edge**, top must match bottom.
- Avoid “almost seamless” anti-aliased edges that create faint seams at certain zooms.
- Prefer **simple geometry** (lines/dots) over complex textures—maps are information-dense.
- Keep file size small; patterns add up quickly once packed into sprites.

---

## 🏷️ Naming conventions

Use **kebab-case**, and name patterns by **meaning**, not appearance.

### Base rule
`pat-<semantic-name>.<ext>`

Examples:
- `pat-uncertainty-stipple.svg`
- `pat-farmland-hatch.svg`
- `pat-wetlands-dots.png`

### Optional variants (when needed)
If you provide multiple scales:
- `pat-farmland-hatch-s.svg`
- `pat-farmland-hatch-m.svg`
- `pat-farmland-hatch-l.svg`

If you provide theme variants:
- `pat-uncertainty-stipple-light.svg`
- `pat-uncertainty-stipple-dark.svg`

> [!IMPORTANT]
> Pattern *filenames* are not automatically what MapLibre uses. MapLibre references **sprite IDs** (the packed name inside the sprite). The build step should preserve stable IDs.

---

## 🧾 Provenance & licensing

KFM is explicitly designed so that **citations and metadata are first-class** and that the UI lets users inspect sources—this applies to visual semantics too.  [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

Also, KFM emphasizes careful license handling to foster trust and collaboration.  [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### ✅ Required: metadata sidecar per pattern

For every `pat-*.svg|png`, add a sibling `pat-*.meta.json`.

Example:
- `pat-farmland-hatch.svg`
- `pat-farmland-hatch.meta.json`

<details>
<summary>📄 <b>Metadata template (copy/paste)</b></summary>

```json
{
  "id": "pat-farmland-hatch",
  "title": "Farmland hatch",
  "description": "Diagonal hatch used to indicate cultivated / agricultural land (when color alone is insufficient).",
  "tags": ["landuse", "agriculture", "hatch", "legend"],
  "intended_use": ["fill-pattern", "legend-swatch"],

  "author": "KFM Contributors",
  "created": "YYYY-MM-DD",
  "modified": "YYYY-MM-DD",

  "license": "CC0-1.0",
  "source": {
    "type": "original",
    "source_url": null,
    "attribution": null
  },

  "rendering": {
    "tile_px": 64,
    "notes": "Seamless tile. 1px strokes. Avoid moiré at z5–z12."
  }
}
```
</details>

### “No mystery assets” rule (KFM-aligned)
KFM’s data model disallows unsourced “mystery layers” and requires traceability for anything shown in the UI. Apply the same standard here: **if it affects what the user sees, it needs provenance + license clarity.**  [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## ➕ Adding a new pattern

1. **Design the tile**
   - Make it seamless
   - Pick a standard tile size (32/64/128)
   - Keep it subtle

2. **Create metadata**
   - Add `pat-xyz.meta.json`
   - Include license + source attribution (or declare it original)

3. **Add/Update sprite build**
   - Patterns must be available to MapLibre via the style’s **sprite**.
   - If your workflow generates sprites, make sure this pattern is included.

<details>
<summary>🧰 <b>Suggested sprite workflow (example)</b></summary>

KFM’s docs describe a modern web front-end and assets pipeline; the exact sprite tooling may vary by repo.  [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

A common open workflow is:
- Keep pattern sources here (`patterns/`)
- Pack them into a sprite atlas referenced by a MapLibre style JSON

Example commands (adjust paths/tooling to your setup):

```bash
# Example only — pick the sprite tool used by this repo
# Generate sprite.png + sprite.json
npx spritezero ./sprites/kfm ./patterns

# If using retina sprites:
npx spritezero --retina ./sprites/kfm ./patterns
```

Outputs typically include:
- `kfm.png`, `kfm.json`
- `kfm@2x.png`, `kfm@2x.json`
</details>

4. **Reference it in style JSON**
   - Add `fill-pattern` / `line-pattern` using the sprite ID
   - Update legend mappings if the legend is config-driven

5. **Verify in the UI**
   - Patterns should appear correctly in the layer + legend
   - Check common zoom levels and dark/light basemaps

---

## 🗺️ Using patterns in MapLibre styles

### 1) Simple polygon pattern fill

```json
{
  "id": "landuse_farmland_pattern",
  "type": "fill",
  "source": "kfm",
  "source-layer": "landuse",
  "filter": ["==", ["get", "class"], "farmland"],
  "paint": {
    "fill-pattern": "pat-farmland-hatch",
    "fill-opacity": 0.70
  }
}
```

### 2) Themeable “base color + pattern overlay” (recommended)

Since patterns are image-based, you often get better theming control by **stacking layers**:

```json
[
  {
    "id": "landuse_farmland_base",
    "type": "fill",
    "source": "kfm",
    "source-layer": "landuse",
    "filter": ["==", ["get", "class"], "farmland"],
    "paint": { "fill-color": "#b8c08a", "fill-opacity": 0.55 }
  },
  {
    "id": "landuse_farmland_overlay_pattern",
    "type": "fill",
    "source": "kfm",
    "source-layer": "landuse",
    "filter": ["==", ["get", "class"], "farmland"],
    "paint": { "fill-pattern": "pat-farmland-hatch", "fill-opacity": 0.35 }
  }
]
```

### 3) Zoom-dependent pattern switching

```json
{
  "id": "uncertainty_extent_pattern",
  "type": "fill",
  "source": "kfm",
  "source-layer": "boundaries",
  "filter": ["==", ["get", "status"], "uncertain"],
  "paint": {
    "fill-pattern": [
      "step",
      ["zoom"],
      "pat-uncertainty-stipple-s",
      9, "pat-uncertainty-stipple-m",
      12, "pat-uncertainty-stipple-l"
    ],
    "fill-opacity": 0.55
  }
}
```

---

## 🧪 QA checklist

Before merging a new/updated pattern:

- [ ] Seamless repeat (no visible seams at typical zooms)
- [ ] Looks good on both light and dark basemaps
- [ ] Doesn’t overpower labels/lines (subtle texture)
- [ ] Filename follows naming conventions
- [ ] `*.meta.json` present and complete
- [ ] License/source recorded (no surprises later)  [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- [ ] Sprite build updated (if applicable), and UI verifies correctly
- [ ] Legend swatch updated (if the pattern is user-facing)  [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🛠️ Troubleshooting

**Pattern not rendering**
- Confirm it exists in the **sprite** referenced by the active style JSON.
- Confirm the ID used in `fill-pattern` matches the sprite ID exactly.

**Looks blurry**
- Use SVG sources (preferred) or higher-resolution tiles.
- Ensure retina sprite generation is correct (if used).

**Seams appear**
- Re-check edge pixels/vectors; avoid near-edge anti-aliasing.
- Ensure the tile is truly periodic (exact symmetry across edges).

**Pattern too noisy**
- Increase tile size (or simplify geometry).
- Reduce stroke thickness / dot density.
- Reduce `fill-opacity`.

---

## 📎 References

Project architecture + design principles informing this folder:

- **KFM mission & provenance-first UI expectations**  [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- **Contract-first / no “mystery” artifacts approach**  [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- **Web front-end + MapLibre viewer context**  [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- **Web UI includes legends + timeline controls**  [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- **Repo design notes describing web mapping stack**  [oai_citation:15‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)

Source PDFs (project files):
- Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf  [oai_citation:16‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf  [oai_citation:17‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)  