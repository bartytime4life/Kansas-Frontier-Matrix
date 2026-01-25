# 🛣️ Road Decal Textures (3D)

**📍 Location:** `web/assets/3d/shared/textures/decals/road/`

Transparent road-marking / surface-detail textures used as *decals* in the **Kansas Frontier Matrix (KFM)** web client.

> [!NOTE]
> KFM’s `web/` front-end integrates **MapLibre GL JS** (2D) and **CesiumJS** (3D globe/terrain) and uses the **3D Tiles** standard for streaming 3D geospatial content. These files live in `web/assets/` as static client-side assets. :contentReference[oaicite:0]{index=0}

---

## 📌 Table of contents
- [🧭 Quick rules](#-quick-rules)
- [📦 What belongs here](#-what-belongs-here)
- [🧾 Provenance and licensing](#-provenance-and-licensing)
- [🗂️ Suggested folder layout](#️-suggested-folder-layout)
- [🧱 Texture standards](#-texture-standards)
- [🏷️ Naming conventions](#️-naming-conventions)
- [🗺️ Geospatial placement tips](#️-geospatial-placement-tips)
- [🧩 Using decals in the web client](#-using-decals-in-the-web-client)
- [📉 Performance and offline readiness](#-performance-and-offline-readiness)
- [♿ UX clarity and accessibility](#-ux-clarity-and-accessibility)
- [🤖 Governance and automation](#-governance-and-automation)
- [✅ Add-a-decal checklist](#-add-a-decal-checklist)
- [🔗 Project references](#-project-references)

---

## 🧭 Quick rules

- ✅ **Localized** stamps/markings (crosswalks, arrows, patches, lane stripes) belong here.
- ❌ **Infinitely tiling** materials (repeating asphalt/concrete) do *not* belong here.
- 🧾 Every decal must ship with **license + provenance metadata** so UI attribution stays accurate. :contentReference[oaicite:1]{index=1}:contentReference[oaicite:2]{index=2}

---

## 📦 What belongs here

### ✅ Good candidates
- **Lane markings:** dashed/solid stripes, stop bars, edge lines
- **Crosswalks:** zebra, ladder
- **Symbols:** turn arrows, bike lane stencils (only if licensed)
- **Construction:** temporary lines & markings
- **Wear & tear:** cracks, patches, pothole fill, oil stains, skid marks
- **Hardware:** manholes, drains, reflectors (as decals)

### 🚫 Not a good fit
- Large photo-based road surfaces intended to be **baked into 3D Tiles materials**
- UI icons/sprites for buttons & menus (those live under general `web/assets/`) :contentReference[oaicite:3]{index=3}

---

## 🧾 Provenance and licensing

KFM is **provenance-first**: anything shown in the UI should be traceable and governable, with clear metadata and licensing. :contentReference[oaicite:4]{index=4}:contentReference[oaicite:5]{index=5}

For *road decals*, provenance typically means:
- **Who** made it (human/tool)
- **When** it was created/updated
- **License** (and any required attribution)
- **Source** (if derived from another asset/dataset)
- **AI disclosure** if generated or heavily assisted by AI (model + prompt reference):contentReference[oaicite:6]{index=6}

> [!TIP]
> If a decal is derived from real data (orthophoto snippets, scanned maps, etc.), treat it like data: keep a reproducible chain (STAC/DCAT/PROV) and/or attach a provenance manifest to the artifact. :contentReference[oaicite:7]{index=7}:contentReference[oaicite:8]{index=8}

> [!IMPORTANT]
> If you introduce a build step (atlas generation, compression, etc.), treat it like a pipeline: **deterministic, config-driven, reproducible**—no hidden manual edits. :contentReference[oaicite:9]{index=9}

### Suggested companion files (per decal)

| File | Required | Purpose |
|------|----------|---------|
| `rd_<...>__color.png` | ✅ | RGBA decal (alpha = cutout mask) |
| `rd_<...>__normal.png` | ◻️ | Optional normal detail |
| `rd_<...>__orm.png` | ◻️ | Optional packed Occlusion/Roughness/Metallic |
| `rd_<...>.meta.json` | ✅ | Size in meters, tags, category, usage hints |
| `rd_<...>.source.json` | ✅ | License + provenance (human/AI/source) |

Example `rd_cw_zebra.meta.json`:
```json
{
  "id": "rd_cw_zebra",
  "category": "crosswalk",
  "size_m": { "w": 4.0, "h": 10.0 },
  "tags": ["road", "marking", "pedestrian"],
  "recommended": {
    "clamp": true,
    "mipmaps": true,
    "anisotropy": "max"
  }
}
```

Example `rd_cw_zebra.source.json`:
```json
{
  "title": "Zebra Crosswalk (Generic)",
  "created_by": "kfm-art",
  "created_at": "2026-01-25",
  "license": "CC0-1.0",
  "attribution": null,
  "derived_from": [],
  "faircare_notes": "No community-specific content.",
  "ai": {
    "generated": false,
    "notes": null
  }
}
```

> [!NOTE]
> KFM metadata often includes ethical context (FAIR/CARE) for cultural neutrality, collective benefit, etc. If a decal encodes culturally sensitive content, document it. :contentReference[oaicite:10]{index=10}

---

## 🗂️ Suggested folder layout

You can keep everything flat, but once the decal count grows, a tidy layout helps:

```text
📁 road/
  📁 lane_markings/        # dashed, solid, stop bars
  📁 crosswalks/           # zebra, ladder
  📁 symbols/              # arrows, bike stencils
  📁 wear/                 # cracks, patches, skid marks
  📁 hardware/             # manholes, drains, reflectors
  📁 atlases/              # optional generated atlases + indices
  📄 README.md             # you are here ✅
```

---

## 🧱 Texture standards

### 📐 Size and resolution
- Prefer **power-of-two** dimensions (512, 1024, 2048) to keep GPU pipelines simple and mipmap-friendly.
- Keep decals **tight** (trim unused transparent space) but leave **2–8px padding** to prevent sampling bleed.
- If you need multiple sizes, use explicit variants:
  - `...__1x.png` and `...__2x.png` (or `...@2x.png`)

### 🎨 Color space
- `__color` / albedo: treat as **sRGB**
- `__normal`, `__orm`, `__mask`: treat as **linear / non-color**

### 🌫️ Alpha rules (avoid halos)
- Use **straight alpha** in PNG, with edge pixels *dilated* into the transparent region (avoids dark outlines).
- Avoid semi-transparent colored pixels on edges unless the decal is intentionally feathered.

### 🧩 Filtering defaults
- Decals are often viewed at shallow angles (roads), so prefer:
  - mipmaps ✅
  - anisotropic filtering ✅
  - clamp-to-edge wrapping ✅ (decals should not repeat)

---

## 🏷️ Naming conventions

We want names that are:
- deterministic
- sortable
- easy to reference in code
- reproducible (no “final_final2.png”)

This aligns with KFM’s broader reproducibility expectations (organized naming + no silent overwrites). :contentReference[oaicite:11]{index=11}

### Category codes (suggested)

| Code | Meaning | Examples |
|------|---------|----------|
| `lm` | lane marking | dashed, solid, stop bar |
| `cw` | crosswalk | zebra, ladder |
| `sym` | symbol/stencil | arrows, bike stencil |
| `wear` | wear & tear | cracks, patches, skid |
| `hw` | hardware | manhole, drain |

### Recommended pattern

`rd_<cat>_<slug>__w-<W>m__h-<H>m__v<semver>__<map>.<ext>`

- Use `p` as a decimal separator inside numbers (`0p10m` = `0.10m`)
- Always include `__v<semver>` when pixels change in a meaningful way

Examples:
- `rd_lm_dashed_white__w-0p10m__h-3p00m__v1.0__color.png`
- `rd_cw_zebra__w-4p00m__h-10p00m__v1.0__color.png`
- `rd_wear_patch_asphalt__w-2p00m__h-2p00m__v1.1__color.png`

---

## 🗺️ Geospatial placement tips

Road decals usually get placed from **road geometry** (centerlines/polygons). Road data is often messy; prep matters.

- Split lines at intersections when building networks / segmentation workflows.
- Validate geometry before deriving placement positions.

The included geospatial cookbook notes that working with road data is “tricky” and often requires splitting/segmentizing at intersections for useful tasks. :contentReference[oaicite:12]{index=12}

Also note: KFM’s standards expect **WGS84 geometry conventions** in catalogs and related workflows—keep your placement pipeline consistent. :contentReference[oaicite:13]{index=13}

---

## 🧩 Using decals in the web client

KFM’s `web/` app contains viewer components that integrate MapLibre (2D) and Cesium (3D). These textures are served as static assets and referenced by path. :contentReference[oaicite:14]{index=14}

### Common approaches
1. **Draped polygon/material on terrain** (Cesium)
2. **Projected decal on a road mesh** (custom WebGL / Three.js demo)
3. **Baked into road materials** for streamed 3D Tiles content (when authoring tiles)

<details>
<summary>🧪 Example (Three.js-style) loader snippet</summary>

```js
// Pseudo-example — adapt to the project’s viewer abstraction.
const url =
  "/assets/3d/shared/textures/decals/road/rd_cw_zebra__w-4p00m__h-10p00m__v1.0__color.png";

const tex = await new THREE.TextureLoader().loadAsync(url);
tex.wrapS = THREE.ClampToEdgeWrapping;
tex.wrapT = THREE.ClampToEdgeWrapping;
tex.generateMipmaps = true;
tex.anisotropy = renderer.capabilities.getMaxAnisotropy();
```

The included geospatial cookbook references browser-based 3D visualization workflows using Three.js for geodata. :contentReference[oaicite:15]{index=15}
</details>

---

## 📉 Performance and offline readiness

- Prefer smaller decals + reuse where possible (avoid dozens of unique 4K PNGs)
- Trim transparency borders (but keep padding)
- Consider an **atlas** if many decals are used together (reduces texture binds)
- Keep offline usage in mind: KFM includes “offline pack” ideas for bundling key content for disconnected use. :contentReference[oaicite:16]{index=16}

---

## ♿ UX clarity and accessibility

Decals can look “authoritative” at a glance. Don’t accidentally mislead.

- If a decal represents a *historical* or *hypothetical* marking, make sure the **layer naming/legend** communicates that clearly.
- Keep contrast readable across basemaps and lighting.

KFM’s UI documentation emphasizes accessibility and transparency (visualizations linked to source data, designed for user trust). :contentReference[oaicite:17]{index=17}:contentReference[oaicite:18]{index=18}

---

## 🤖 Governance and automation

KFM’s automation stack includes policy gates and an agent workflow (Watcher → Planner → Executor) to keep changes safe and auditable. Apply the same spirit here: assets should be reviewable, testable, and metadata-complete. 

Practical repo-friendly enforcement ideas (recommended):
- CI check: every `rd_*.png` must have matching `*.meta.json` and `*.source.json`
- CI check: `license` field required, no empty provenance
- Optional: image lint (dimensions, alpha presence, max size)

---

## ✅ Add-a-decal checklist

Before committing:
- [ ] File(s) follow naming convention
- [ ] `*.meta.json` exists and includes **size in meters**
- [ ] `*.source.json` exists and includes **license + provenance**
- [ ] Alpha edge looks clean (no halos)
- [ ] Tested at multiple zoom levels / camera angles
- [ ] No trademarks/logos unless explicitly licensed
- [ ] Version bumped if pixel appearance changed

---

## 🔗 Project references

Core KFM docs (context + governance):
- KFM UI System Overview :contentReference[oaicite:20]{index=20} :contentReference[oaicite:21]{index=21}
- KFM Data Intake – Technical & Design Guide :contentReference[oaicite:22]{index=22} :contentReference[oaicite:23]{index=23}
- KFM Comprehensive Technical Documentation :contentReference[oaicite:24]{index=24} :contentReference[oaicite:25]{index=25}
- KFM Architecture, Features, and Design :contentReference[oaicite:26]{index=26}
- KFM AI System Overview :contentReference[oaicite:27]{index=27}
- Innovative Concepts to Evolve KFM :contentReference[oaicite:28]{index=28} :contentReference[oaicite:29]{index=29}
- Latest Ideas & Future Proposals :contentReference[oaicite:30]{index=30}
- Additional Project Ideas :contentReference[oaicite:31]{index=31}
- Pulse Threads / UI narrative refinements :contentReference[oaicite:32]{index=32}

Reference libraries (PDF portfolio containers):
- Maps / WebGL / Virtual Worlds portfolio :contentReference[oaicite:33]{index=33} (container):contentReference[oaicite:34]{index=34}
- AI Concepts library :contentReference[oaicite:35]{index=35} (container)
- Programming languages & resources library :contentReference[oaicite:37]{index=37} (container)
- Data management + theory library :contentReference[oaicite:39]{index=39} (container):contentReference[oaicite:40]{index=40}

