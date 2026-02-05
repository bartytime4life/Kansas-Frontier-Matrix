# 🗺️ Map Textures (KFM Web UI)

> **Path:** `web/src/assets/textures/map/`  
> **Role:** Small, UI-friendly textures used by the **web map** (patterns, overlays, lightweight terrain helpers).  
> **Not** the primary delivery path for big basemaps / imagery (those are served as tiles via the platform).

![KFM](https://img.shields.io/badge/KFM-living%20atlas%20of%20Kansas-2b6cb0)
![Scope](https://img.shields.io/badge/scope-map%20textures-4a5568)
![Preferred](https://img.shields.io/badge/prefer-.webp%20%7C%20.png-2f855a)
![Governance](https://img.shields.io/badge/evidence-first%20%7C%20license-required-c53030)

---

## 🎯 Why this folder exists

KFM’s UI is map-centric (2D + 3D). Most “real” map imagery and layers should be **streamed** as raster/vector tiles from governed services. This folder exists for **small, reusable textures** that improve cartography + UX:

✅ **Good fits**
- Seamless **fill patterns** (e.g., crosshatch, stipple, dotted grid)
- Transparent **overlays** (e.g., parchment/vignette for “historic mode”)
- Tiny **helper textures** for 3D/terrain styling (e.g., subtle normal-map details)
- UI embellishments tied to map rendering (not app icons — those live elsewhere)

❌ **Not a fit**
- Full **tile pyramids** / basemap caches
- Large raster datasets (satellite mosaics, county-scale imagery exports)
- Anything that should be governed as a dataset (STAC/DCAT/PROV) rather than bundled UI assets

> 💡 Rule of thumb: if it’s **data**, it belongs in the data pipeline + tile service.  
> If it’s **presentation**, it can live here.

---

## 🧩 Where this fits in the KFM “truth path”

KFM follows a strict pipeline: **ETL → catalogs → graph → APIs → UI**.  
This directory is firmly in the **UI** stage.

That means:
- Textures **must not** smuggle in untracked data decisions.
- Textures **must** have licensing + provenance, even if they’re “just visuals.”

---

## 🗂️ Suggested folder layout

> This is a recommended structure. Use what exists today, but keep things **predictable**.

```text
📁 web/src/assets/textures/map/
├── 📄 README.md
├── 📄 manifest.textures.json              # optional: registry of textures (recommended)
├── 📁 patterns/                           # seamless fill-patterns for polygons/areas
│   ├── crosshatch.webp
│   ├── stipple.webp
│   └── contour-lines.webp
├── 📁 overlays/                           # transparent rasters (UI overlays)
│   ├── parchment.webp
│   └── vignette.webp
├── 📁 terrain/                            # small helper maps for 3D styling
│   ├── ks_terrain_detail_normal.webp
│   └── ks_terrain_detail_height.png
└── 📁 experimental/                       # WIP / not yet shipped (keep clean!)
    └── _README.md
```

---

## 🏷️ Naming conventions

Consistency matters for usability and teamwork:

✅ **Do**
- `kebab-case` filenames
- include a **purpose hint**: `parchment-overlay.webp`, `stipple-fill.webp`
- include **version suffix** when it matters: `crosshatch-v2.webp`

❌ **Avoid**
- random names like `texture1.png`
- ambiguous names like `bg.webp`
- spaces / mixed casing

> 🧭 If you can’t guess the texture’s role from the filename, rename it.

---

## 📦 Size & performance budgets

Because these assets live under `src/`, bundlers typically treat them as part of the build output. Keep textures lean to avoid bloating the web payload.

**Budgets (strongly recommended):**
- **Patterns:** ≤ 64 KB each (ideally smaller)
- **Overlays:** ≤ 256 KB each
- **Terrain helpers:** ≤ 512 KB each (only if truly needed)

If an asset can’t meet budgets:
- move it out of the bundle path (e.g., served from a static host/CDN), **or**
- rethink the approach (tiles/service-driven visualization)

---

## 🧾 Provenance & licensing (non-negotiable)

Every texture needs:
1) **A license you can prove**
2) **Attribution info** (when required)
3) A “how it was made” note if it’s derived from something else

### ✅ Sidecar metadata (recommended pattern)

For each texture file, add a sibling metadata file:

- `crosshatch.webp`
- `crosshatch.webp.meta.json`

Example schema (keep it simple but complete):

```json
{
  "id": "crosshatch-v1",
  "title": "Crosshatch Fill Pattern",
  "type": "pattern",
  "version": "1.0.0",
  "format": "webp",
  "created_by": "KFM Team",
  "created_at": "2026-02-05",
  "license": "CC-BY-4.0",
  "attribution": "If required, put it here.",
  "source": {
    "kind": "original",
    "url": null,
    "notes": "Designed from scratch for KFM."
  },
  "usage": {
    "intended_for": ["maplibre.fill-pattern", "legend.swatch"],
    "notes": "Designed to be subtle at multiple zoom levels."
  }
}
```

> 🧠 **If you can’t write a clean license + source story, don’t commit the file.**

---

## 🎨 Cartography notes for textures

Textures are powerful — and easy to overdo.

- Prefer **subtle** patterns that don’t overpower data layers.
- Avoid visually noisy textures that create shimmer / moiré at multiple zoom levels.
- Match the texture “feel” to what it represents (e.g., don’t use a brick-like pattern to symbolize glass).

---

## 🧪 Usage examples

### MapLibre / Map overlays (pattern fills)

> Exact implementation may vary by component, but this shows the intent.

```ts
import crosshatch from "@/assets/textures/map/patterns/crosshatch.webp";

// Example: attach to a style image registry (MapLibre-style approach)
// map.addImage("crosshatch", imageBitmapOrHtmlImageEl);
// layer.paint = { "fill-pattern": "crosshatch" };
```

### React usage (simple overlay UI)

```tsx
import parchment from "@/assets/textures/map/overlays/parchment.webp";

export function HistoricOverlay() {
  return (
    <div
      aria-hidden="true"
      style={{
        pointerEvents: "none",
        position: "absolute",
        inset: 0,
        backgroundImage: `url(${parchment})`,
        backgroundRepeat: "repeat",
        opacity: 0.18
      }}
    />
  );
}
```

---

## ✅ Add-a-texture checklist (PR gate)

Before committing a new file:

- [ ] Filename follows convention (`kebab-case`, descriptive)
- [ ] File is compressed (`.webp` preferred for photographic/gradient; `.png` for crisp alpha)
- [ ] Seamless tiling confirmed (if pattern)
- [ ] Size budget met
- [ ] `*.meta.json` sidecar added (license + attribution + source)
- [ ] Visual QA on light + dark basemap modes (if applicable)

---

## 🧯 Troubleshooting

**My pattern looks “busy” or flickers while zooming**
- Reduce contrast
- Increase pattern cell size
- Test at multiple zoom levels
- Prefer fewer high-frequency details

**The bundle got huge**
- Audit texture sizes
- Replace PNGs with WebP where safe
- Move heavy imagery out of `src/` bundle paths

---

## 🔗 Related (project docs)

📚 If you’re unsure whether something is a **texture** or a **dataset**, start here:
- `docs/MASTER_GUIDE_v13.md` (pipeline + structure)
- `docs/architecture/` (system overview, mapping UI)
- `src/server/api/README.md` (tiles + APIs)

---

## 🧠 Philosophy: “the map behind the map”

Even UI assets should support KFM’s core promise: transparency, provenance, and trust.  
When someone asks “why does this map look like this?”, we should be able to answer.
