# 🎨 Legend Swatches

`type: assets` `scope: web/maps` `ui: legends` `kfm: provenance-first`

Small visual swatches (color chips, line samples, patterns, symbol thumbnails) used by the **Map Legend UI** to communicate map symbology clearly and consistently.

> [!IMPORTANT]
> In KFM, **anything that shows up in the UI must be traceable** back to cataloged sources + provable processing, and we do not allow “mystery layers.” Apply that same mindset to legend visuals: every swatch must have a clear meaning and an unambiguous link to the layer/style/dataset it represents.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🧭 Why this folder exists

Legends are not “decoration” — they are part of KFM’s trust & interpretability model:

- ✅ **Contract-first:** UI configuration should be deterministic and machine-checkable (no ad-hoc, ambiguous symbology).
- ✅ **Evidence-first:** swatches should reflect a real style token / layer meaning, not an arbitrary color someone picked “because it looked nice.”
- ✅ **Provenance-first:** users should be able to understand what a layer is and where it came from — the legend is a key entry point.  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:2‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 📁 Folder placement

This README documents the asset folder:

```text
web/
  assets/
    maps/
      legends/
        swatches/
          README.md  👈 you are here
          # (*.svg | *.png) swatch assets live alongside this file
```

> [!NOTE]
> If you later introduce subfolders (recommended once swatches grow), keep the structure semantic (by **domain** or **legend system**) rather than by file type.

---

## ✅ What belongs here (and what doesn’t)

### ✅ Belongs here
- 🟦 **Fill swatches**: solid color chips for polygons / choropleths
- ➖ **Line swatches**: representative line samples (solid/dashed/dotted)
- 🧵 **Pattern swatches**: hatching, stippling, crosshatch, “historical overlay” textures
- 📍 **Point/symbol swatches**: simplified thumbnails of point markers when the legend needs them

### 🚫 Doesn’t belong here
- Full UI icons unrelated to map legends
- Large illustrations, screenshots, or branding images
- Map sprite sheets intended for rendering in MapLibre/Mapbox (unless you explicitly use the same assets for legend previews)

---

## 🧱 Swatch design principles (KFM-aligned)

### 1) Semantic color choices 🎯
Use intuitive conventions where possible (e.g., **blue = water**, **green = vegetation**, **red = heat**) and keep legends readable.  [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### 2) Legends must support correct interpretation 🗺️
For choropleths and classed data:
- “**Dark means more**” is the default expectation for most readers.
- Put **larger values at the top** of the legend.
- Prefer **non-continuous** class legends that show the **low/high** per class (avoid implying values span the full range within each class).  [oai_citation:4‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](file-service://file-51FgWTn7uFXenxztXw29bP)

For graduated symbols:
- **Classified** legends (discrete sizes per class) are easier to match to map symbols.
- **Unclassified** legends (scaled to each value) should include representative sizes.  [oai_citation:5‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](file-service://file-51FgWTn7uFXenxztXw29bP)

### 3) Accessibility first ♿
KFM explicitly targets high-contrast support and semantic/ARIA-friendly UI navigation; legends must follow suit.  [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

Practical checklist:
- [ ] Swatch + label remain understandable in **high-contrast mode**
- [ ] Do not encode meaning by color alone (add pattern/shape when needed)
- [ ] Provide proper semantics in the legend component (ARIA + meaningful labels)  [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- [ ] Test for color-vision deficiencies using simulation tools; test with screen readers as part of UI QA  [oai_citation:8‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-Heg28TVM2nReDYTQ7nPhAK)

> [!TIP]
> Progressive enhancement mindset applies here too: ensure the legend works as **simple HTML + text** first, then enhance with swatch imagery.  [oai_citation:9‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-Heg28TVM2nReDYTQ7nPhAK)

---

## 🧾 File formats & when to use them

### ✅ SVG (preferred)
Use for:
- Simple color chips
- Line samples (stroke width, dash patterns)
- Vector patterns that should remain crisp at any zoom / DPI

### ✅ PNG (allowed)
Use for:
- Complex textures or pixel-art patterns
- When you need alpha blending against varying backgrounds

PNG is **lossless** and supports an **alpha channel** for transparency (useful for overlay/pattern swatches).  [oai_citation:10‡compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf](file-service://file-Y6V94sFtV6sy3w63LDy9fi) [oai_citation:11‡compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf](file-service://file-Y6V94sFtV6sy3w63LDy9fi)

### 🚫 JPEG (avoid)
Not suited for flat-color swatches or crisp edges due to lossy compression artifacts.

### ⚖️ Palette vs true color (PNG optimization)
Swatches often use a limited set of colors; consider palette-based PNGs (indexed color) for size efficiency when appropriate.  [oai_citation:12‡compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf](file-service://file-Y6V94sFtV6sy3w63LDy9fi)

---

## 📐 Swatch “spec” (recommended defaults)

These are pragmatic UI defaults; the legend component can scale as needed:

- **Canvas size:** 24×24 px (or 20×20)  
- **Safe padding:** 2 px  
- **Border:** 1 px subtle outline if swatch could blend into the background  
- **Background:** transparent unless the meaning depends on a background

> [!NOTE]
> Keep visuals consistent across domains. Legends should feel like one system, not many unrelated mini-designs.

---

## 🏷️ Naming convention

Keep names:
- ✅ **semantic**
- ✅ **stable**
- ✅ **kebab-case**
- ✅ machine-sortable where classes exist

### Suggested pattern
`<domain>-<geometry>-<meaning>[-class-##][-variant].(svg|png)`

Examples:
- `hydrology-fill-water.svg`
- `vegetation-fill-forest.svg`
- `hazards-fill-heat-class-05.svg`
- `boundaries-line-historic-dashed.svg`
- `admin-pattern-disputed-crosshatch.png`

> [!IMPORTANT]
> If a swatch’s meaning changes, do **not** silently reuse the filename. Either:
> - add a `-variant` suffix, or  
> - create a new file and deprecate the old one.

---

## 🔗 Linking swatches to “contracts” (no mystery legend items)

KFM treats contracts (schemas/specs) as first-class artifacts across the pipeline boundaries. Apply the same idea to legend assets: swatches should be referenced from a **single source of truth** legend config (or generated from style + metadata), never sprinkled ad-hoc across UI components.  [oai_citation:13‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### Example: minimal swatch registry (illustrative)
```json
{
  "id": "hydrology-fill-water",
  "label": "Water",
  "swatch": "hydrology-fill-water.svg",
  "styleRefs": [
    { "mapStyleId": "kfm-base", "layerId": "hydrology-water" }
  ],
  "tokens": {
    "fill": "#2b83ff"
  },
  "notes": "Keep blue consistent with hydro layers."
}
```

> [!TIP]
> If you’re already generating legends from palette arrays / class breaks, treat the registry as build output and keep the inputs canonical.
> A similar “palette + label + UI box” pattern is commonly used when programmatically building legends.  [oai_citation:15‡Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf](file-service://file-JVv3nbvtonX1HcpeERi9kV)

---

## 🧩 Example usage in UI (HTML)

When the legend already includes the label text, the swatch can be decorative:

```html
<li class="LegendItem">
  <img
    class="LegendSwatch"
    src="/assets/maps/legends/swatches/hydrology-fill-water.svg"
    alt=""
    aria-hidden="true"
  />
  <span class="LegendLabel">Water</span>
</li>
```

If the swatch is the only indicator (try to avoid this), then give it meaningful alt text.

---

## 🧪 Adding a new swatch (quick workflow)

1. 🧠 **Define meaning first**  
   - What dataset/layer/class does this represent?
   - How does it map to style tokens or class breaks?

2. 🎨 **Design with legend rules**  
   - For choropleths: ordering, class breaks, “dark means more,” etc.  [oai_citation:16‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](file-service://file-51FgWTn7uFXenxztXw29bP)

3. 🧰 **Pick format**
   - SVG for simple geometry
   - PNG for complex textures / alpha blending  [oai_citation:17‡compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf](file-service://file-Y6V94sFtV6sy3w63LDy9fi)

4. 🏷️ **Name it using the convention**  
   - Keep it semantic and stable.

5. 🔗 **Register it** (or update the legend config that consumes it)  
   - Don’t create one-off references.

6. ♿ **Validate accessibility**
   - High-contrast, color-vision simulation, and semantic/ARIA checks.  [oai_citation:18‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:19‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-Heg28TVM2nReDYTQ7nPhAK)

---

## 🔎 Legend data flow (mental model)

```mermaid
flowchart LR
  A[(STAC/DCAT/PROV<br/>Dataset Metadata)] --> B[Map Style JSON<br/>(tokens/layers)]
  B --> C[Legend Config<br/>(contracted)]
  C --> D[Swatch Assets<br/>(this folder)]
  D --> E[Legend UI<br/>(accessible + auditable)]
```

KFM’s “contracts + evidence before interpretation” approach should remain visible even in UI details like legends.  [oai_citation:20‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:21‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 📚 Sources used for this README

- KFM provenance-first + contract-first rule; no “mystery layers” in UI/catalog  [oai_citation:22‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- KFM front-end cartographic best practices + accessibility (high-contrast, ARIA/semantic HTML)  [oai_citation:23‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- KFM map design notes (legends, MapLibre style JSON can define legend items)  [oai_citation:24‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- KFM master guide: contract/evidence-first philosophy across the platform  [oai_citation:25‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:26‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- Cartographic legend guidance (choropleth + classed legends; ordering/meaning)  [oai_citation:27‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](file-service://file-51FgWTn7uFXenxztXw29bP) [oai_citation:28‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](file-service://file-51FgWTn7uFXenxztXw29bP)
- PNG capabilities (lossless, alpha transparency; palette vs true color)  [oai_citation:29‡compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf](file-service://file-Y6V94sFtV6sy3w63LDy9fi) [oai_citation:30‡compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf](file-service://file-Y6V94sFtV6sy3w63LDy9fi) [oai_citation:31‡compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf](file-service://file-Y6V94sFtV6sy3w63LDy9fi)
- Progressive enhancement + accessibility testing references  [oai_citation:32‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-Heg28TVM2nReDYTQ7nPhAK) [oai_citation:33‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-Heg28TVM2nReDYTQ7nPhAK)
- Programmatic legend construction pattern (palette + labels + UI boxes)  [oai_citation:34‡Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf](file-service://file-JVv3nbvtonX1HcpeERi9kV)