# 🧾 KFM Sprite Pack — Attribution & Licensing

![License](https://img.shields.io/badge/license-MIT-success)
![Provenance](https://img.shields.io/badge/provenance-first-1f6feb)
![Maps](https://img.shields.io/badge/MapLibre-sprites-6f42c1)

> 🧭 **KFM principle:** “Citations and metadata are first-class data; nothing is a ‘black box.’”  
> This file applies that mindset to **map icons** — no “mystery sprites” ✅

---

## 🎯 Purpose

This document is the **single source of truth** for attribution and licensing of any **third‑party icon artwork** shipped in the KFM sprite sheets.

If an icon is not 100% original to KFM, it **must** be documented here so KFM can remain:
- 🧬 provenance-first
- 🧾 license-transparent
- 🧠 audit-friendly for educators, researchers, and public-sector use

---

## 🗺️ Scope

This file covers assets in:

```text
📦 web/assets/maps/sprites/kfm/
├─ 🧩 kfm.json            (sprite index: name → x/y/size)
├─ 🖼️ kfm.png             (sprite atlas 1x)
├─ 🔎 kfm@2x.png          (sprite atlas 2x / retina)
└─ 🧾 ATTRIBUTION.md      (this file)
```

These sprites are intended for MapLibre/Mapbox-style usage:
- `style.sprite` points to this directory
- layers reference icons via `icon-image: "<sprite-key>"`

---

## ✅ Attribution rules

### 🧷 Non-negotiables
- **No mystery icons:** every non-KFM-original icon must be listed in the registry below.
- **Traceable source:** include the upstream project/site and a stable link.
- **License clarity:** record the exact license (and version if relevant).
- **Modification honesty:** record edits (redraw, simplification, recolor, crop, merge, SVG→PNG, etc.).
- **License artifacts:** if an upstream license requires NOTICE / LICENSE inclusion, store it nearby (or link to where it lives in-repo).

### 🪪 UI visibility
If a license requires **visible attribution**, ensure KFM exposes it in:
- 🧾 “About / Credits” panel
- 🗺️ map legend/help overlay
- 📤 exports (PDF/PNG) footer if applicable

---

## 🧾 Icon registry

> Add **one row per icon** when importing a subset.  
> Add **one row per icon set** if importing the whole set unchanged.

| Sprite key (as used in style) | Upstream source / project | Author / org | License | Upstream link | Notes / modifications |
|---|---|---|---|---|---|
| _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ |
| _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ |

<details>
<summary>🧠 Registry tips (click to expand)</summary>

- **Sprite key** should match the entry name in `kfm.json` (e.g., `trailhead`, `fort`, `battle-site`).
- If you import a **set**, record whether it’s:
  - ✅ unchanged (one row OK), or
  - ✂️ subset (list the subset icons individually).
- For conversions, capture the pipeline (example):
  - “SVG → optimized SVG → rasterized @1x/@2x → packed into atlas”

</details>

---

## 🧑‍🎨 KFM-original artwork

Unless a sprite is explicitly listed in the registry as third-party, icons in this folder are treated as:
- 🧑‍💻 created by KFM contributors, and
- 📜 distributed under the repository’s primary license (see root `LICENSE`).

---

## 📚 Common upstream icon libraries (only if used)

> ⬇️ Check a box **only when** we actually ship icons from that source, and add the relevant registry entries above.

- ☐ 🧭 OpenStreetMap Carto symbols (`openstreetmap-carto/symbols`)
- ☐ 🧩 OpenStreetMap map-icons (`openstreetmap/map-icons`)
- ☐ 🗺️ Mapbox Maki (icons for web cartography)
- ☐ ✨ Other: ______________________________________

---

## 🛠️ Change workflow

1. 🧩 Add / update icon sources (SVG/PNG/etc.).
2. 🧰 Regenerate `kfm.png`, `kfm@2x.png`, and `kfm.json` using the project’s sprite toolchain.
3. 🧾 Update the **Icon registry** table (source + license + edits).
4. 🧪 Validate in UI (icons render at all zooms + no missing `icon-image` references).
5. 🔍 Confirm any required **visible attribution** is still satisfied.

---

## 🧷 Notes

- This file documents **icon art** only 🎨  
  Dataset/basemap attribution is tracked separately via KFM’s dataset metadata + map-layer attribution logic.

---

_Last updated: YYYY-MM-DD_ 📅
