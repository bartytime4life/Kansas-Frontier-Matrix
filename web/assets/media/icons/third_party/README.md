# 🧩 Third‑Party Icons (Vendor Assets)

<p align="center">
  <img alt="Provenance-first" src="https://img.shields.io/badge/Provenance-First-1f6feb?style=for-the-badge" />
  <img alt="Third-party assets" src="https://img.shields.io/badge/Assets-third__party-f97316?style=for-the-badge" />
  <img alt="SVG preferred" src="https://img.shields.io/badge/SVG-Preferred-22c55e?style=for-the-badge" />
</p>

> [!IMPORTANT]
> **No “mystery icons.”** Anything in the UI must be **traceable** to a source + license (KFM provenance-first principle applied to assets).  
> If we can’t attribute it, **we don’t ship it**. ✅

---

## 📌 What this folder is

This directory contains **third-party icon packs** used by the web UI.

- ✅ Allowed: open-licensed icon packs (per-pack licensing + attribution included)
- ❌ Not allowed: unlicensed icons, “found on Google,” ripped app assets, or anything with unclear origin
- ⚠️ Special care: brand/logos (trademark rules can apply even if the SVG is licensed)

---

## 🧭 Rules of the road (non‑negotiables)

Each icon pack **MUST** live in its own folder and include:

| Required file | Why it exists |
|---|---|
| `LICENSE` | Preserve upstream license text verbatim |
| `ATTRIBUTION.md` | Human-readable credit + usage notes |
| `pack.meta.yml` | Machine-readable provenance “asset contract” |
| `svg/` (or `png/`) | Actual icon files |
| `CHANGES.md` *(only if modified)* | Exactly what we changed + why |

> [!TIP]
> Treat filenames like a public API. Renaming icons breaks imports and UI references.

---

## 🗂️ Recommended layout

```text
📁 web/assets/media/icons/third_party/
├─ 📁 <pack-name>/
│  ├─ 📄 LICENSE
│  ├─ 📄 ATTRIBUTION.md
│  ├─ 📄 pack.meta.yml
│  ├─ 📄 CHANGES.md            # only if we modified upstream icons
│  └─ 📁 svg/                  # preferred
│     ├─ 🧩 map-pin.svg
│     ├─ 🧩 layers.svg
│     └─ 🧩 timeline.svg
└─ 📄 README.md                # ← you are here
```

**Naming suggestion:** `<pack-name>` should be `kebab-case` and stable (e.g., `heroicons`, `tabler-icons`, etc.).

---

## 🧾 `pack.meta.yml` template (asset contract)

Use this file to make the pack auditable and automatable (credits page, build-time checks, etc.):

```yaml
# pack.meta.yml
pack_name: "REPLACE_ME"
pack_version: "REPLACE_ME"          # upstream version/tag/commit if known
license_spdx: "REPLACE_ME"          # e.g., MIT, Apache-2.0, CC0-1.0, CC-BY-4.0
license_file: "LICENSE"

upstream:
  source_name: "REPLACE_ME"         # site/repo name
  source_url: "REPLACE_ME"          # where we got it from
  retrieved_at: "YYYY-MM-DD"        # when it was pulled into the repo
  upstream_ref: "REPLACE_ME"        # release tag / commit sha / archive name

attribution:
  authors: ["REPLACE_ME"]
  required_notice: "REPLACE_ME"     # short license notice if required
  modifications: false

constraints:
  allow_modifications: true         # must be true if we edit svgs
  allow_redistribution: true        # must be true to ship with app
  trademark_notes: "REPLACE_ME"     # optional
```

> [!NOTE]
> If the license is **not SPDX-identifiable**, put the best-known label in `license_spdx` and explain in `ATTRIBUTION.md`.

---

## 🧷 `ATTRIBUTION.md` template

```md
# Attribution — <pack-name>

- Pack: <pack-name>
- Upstream: <source>
- License: <license>
- Retrieved: YYYY-MM-DD
- Notes: <any required attribution text + placement requirements>

## Included icons
- map-pin.svg
- layers.svg
- timeline.svg

## Modifications
- None
```

---

## 🔤 Icon naming & stability

### ✅ Do
- Use `kebab-case` (`map-pin.svg`, `layer-stack.svg`)
- Keep names short and semantic
- Prefer “concept names” over UI-specific names

### ❌ Don’t
- Rename icons casually
- Mix multiple packs inside one folder
- Commit icons without provenance files

### If you must rename
- Keep the old file for one release cycle (if possible)
- Create a mapping note in `CHANGES.md`

---

## 🎨 Format, quality, and optimization

### Preferred
- ✅ **SVG** (small, scalable, themeable)
- ✅ Simple paths + a clean `viewBox`

### Avoid
- ❌ Embedded raster images inside SVG
- ❌ Inline CSS that depends on external classes
- ❌ Overly complex filters unless required

### Optimization suggestions
- Run an SVG optimizer (e.g., SVGO) before committing
- Ensure `fill="currentColor"` if the icon should inherit theme color
- Keep strokes consistent within a pack

---

## 🧪 Add-a-pack checklist (Definition of Done)

- [ ] Pack is in its own `third_party/<pack-name>/` folder 📁  
- [ ] `LICENSE` included verbatim 📄  
- [ ] `ATTRIBUTION.md` filled with required notices 🧾  
- [ ] `pack.meta.yml` completed (source + version + license) 🔎  
- [ ] Icons are optimized + render correctly at common sizes (16/20/24/32) ✅  
- [ ] Any modifications are documented in `CHANGES.md` 🧷  
- [ ] No unused bulk assets (only include what we ship) 🚯  

---

## 🧠 Why so strict?

KFM is designed to be **provenance-first**: if it appears in the product, we can explain **where it came from** and **under what terms we can use it**.  
That philosophy applies to icons as much as datasets. 🧭✨
