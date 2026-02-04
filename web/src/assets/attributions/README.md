# 🧾 Attributions & Licenses — `web/src/assets/**`

![Attribution Required](https://img.shields.io/badge/attribution-required-success?style=flat-square)
![Provenance First](https://img.shields.io/badge/provenance-first-blue?style=flat-square)
![Fail-safe Defaults](https://img.shields.io/badge/policy-fail--safe%20defaults-informational?style=flat-square)

> ✅ **Rule:** If it ships in the UI, it **cites**.  
> 🧭 KFM is *evidence-first* — every visual should have a “**map behind the map**” 🗺️🔎

---

## 🎯 Purpose

This folder exists to keep **third‑party and non-original frontend assets** properly credited, licensed, and auditable.

KFM governance treats missing provenance as a **hard stop** (i.e., “not publishable”). This README applies the same mindset to UI assets:  
**No attribution record = no merge** 🚫

---

## 📦 Scope: What belongs here?

Track **anything committed under** `web/src/assets/**` that is not fully authored by the KFM team, including:

- 🖼️ Images (hero images, backgrounds, photos, scanned maps)
- 🧩 Icons / illustrations / SVG packs
- 🔤 Fonts (including variable fonts)
- 🗺️ Map styles, sprites, glyphs, static tiles, raster overlays
- 🧪 Demo/sample datasets shipped with the UI (GeoJSON, TopoJSON, CSV used client-side)
- 🎞️ Animations, Lottie JSON, audio clips, etc.

### 🚫 What does *not* belong here?
- 📦 **NPM dependencies** (React, Map tooling, etc.) — those are tracked via `package.json` and their upstream licenses.
  - Still: if we build a **Credits** screen, we can auto-generate dependency credits separately (see “Automation” below).

---

## 🧠 Non‑negotiables (policy-gate mindset) ✅

**Every third‑party asset must have:**
- 🔗 **Source** (URL or archive reference)
- 👤 **Creator/Publisher**
- 📜 **License name + license link**
- 🧾 **Attribution text** (exact wording if required)
- 🛠️ **Modifications** (what changed, if anything)
- 📍 **Repo path** (where the asset lives)
- 🧷 (Recommended) **Checksum** (sha256) for integrity

> ⚠️ **If the license is unknown or unclear:** treat it as **copyrighted** and **do not ship it**.  
> ✅ Prefer “block” over “unguarded allow.”

---

## 🗂️ Folder layout

Recommended structure (adjust if the repo evolves):

```text
web/
└── src/
    └── assets/
        ├── attributions/
        │   ├── README.md                👈 you are here
        │   ├── credits.json             (optional) machine-readable credits for UI
        │   ├── licenses/                (optional) full license texts when required
        │   │   └── <license-or-asset>.txt
        │   └── <asset-id>.md            one record per asset (or asset bundle)
        ├── images/
        ├── icons/
        ├── fonts/
        └── map/
            ├── styles/
            ├── sprites/
            └── glyphs/
```

---

## 🧾 Attribution record format

We keep one Markdown record per asset (or per bundle) in:

📄 `web/src/assets/attributions/<asset-id>.md`

### ✅ Required fields (minimum)

| Field | Required | Notes |
|------|----------|-------|
| `id` | ✅ | stable slug (`kebab-case`) |
| `title` | ✅ | human-friendly name |
| `type` | ✅ | image / icon / font / map-style / data / other |
| `path` | ✅ | repo-relative path to the actual asset |
| `source` | ✅ | canonical URL or archive reference |
| `creator` | ✅ | author / publisher / org |
| `license` | ✅ | SPDX-ish if possible (e.g., CC-BY-4.0) |
| `license_url` | ✅ | direct link to license terms |
| `attribution` | ✅ | attribution statement (exact wording if required) |
| `modified` | ✅ | true/false |
| `modifications` | ✅ | describe edits (crop, recolor, simplify, etc.) |
| `retrieved` | ✅ | ISO date (`YYYY-MM-DD`) |

> 🧩 For map/design assets, also include: projection/CRS if applicable, style origin, and whether it is a derivative.

---

## 🧷 Copy/Paste Template

<details>
<summary>📄 <b>Attribution record template</b> (click to expand)</summary>

```markdown
# 🧾 <Title of Asset>

- **ID:** `<asset-id>`
- **Type:** `image | icon | font | map-style | data | other`
- **Asset Path:** `web/src/assets/.../...`
- **Source:** `<https://...>`
- **Creator / Publisher:** `<name>`
- **Retrieved:** `YYYY-MM-DD`

## 📜 License
- **License:** `<e.g., CC-BY-4.0>`
- **License URL:** `<https://...>`
- **Local License File (if needed):** `web/src/assets/attributions/licenses/<file>.txt`

## 🧾 Required Attribution
> `<Exact attribution text required by the license/author (if any).>`

## 🛠️ Modifications
- **Modified:** `true | false`
- **What changed:** `<cropped, resized, color-corrected, converted to .webp, simplified paths, etc.>`

## 🧷 Integrity (recommended)
- **SHA256:** `<hash>`
```
</details>

---

## ✅ PR Checklist (assets)

Before merging any new file under `web/src/assets/**`:

- [ ] Added the asset file(s) under the correct folder (`images/`, `icons/`, `fonts/`, `map/`, etc.)
- [ ] Added `web/src/assets/attributions/<asset-id>.md`
- [ ] License is **compatible** with project distribution
- [ ] If required, included full license text under `attributions/licenses/`
- [ ] Attribution requirements are satisfied in UI (Credits modal/page/footer if needed)
- [ ] Recorded modifications + retrieval date
- [ ] (Recommended) Added checksum

---

## 🤖 Optional: machine‑readable credits for the UI

If we want a **Credits** screen (recommended), keep a simple registry:

📄 `web/src/assets/attributions/credits.json`

Example shape:

```json
[
  {
    "id": "example-asset",
    "title": "Example Asset",
    "type": "image",
    "path": "web/src/assets/images/example.webp",
    "source": "https://example.com/original",
    "creator": "Example Creator",
    "license": "CC-BY-4.0",
    "license_url": "https://creativecommons.org/licenses/by/4.0/",
    "attribution": "© Example Creator (CC-BY-4.0). Changes: cropped.",
    "retrieved": "YYYY-MM-DD",
    "modified": true
  }
]
```

> 💡 Keep the JSON minimal and link out to the full per‑asset Markdown file for detailed notes.

---

## 🗺️ Relationship to KFM datasets (STAC/DCAT/PROV)

Most **data-layer** attribution should live in the **catalog metadata** (STAC/DCAT) and lineage (PROV).  
This `web/src/assets/attributions/` folder is specifically for **frontend-shipped static assets**.

✅ Use *both* when appropriate:
- If a dataset is tracked in `data/**` **and** we ship a static snapshot in `web/src/assets/**`, then:
  - dataset provenance belongs in STAC/DCAT/PROV
  - the shipped snapshot also gets an entry here

---

## 🧯 Common “gotchas” (don’t step on these)

- 🧾 **Creative Commons** often requires: credit + license link + “changes were made”
- 🗺️ **Maps & cartography**: the *representation* (styles, symbols, linework) can be copyrighted even when the *facts/data* are not
- 🧠 **Unknown source** = **no-go**. If we can’t cite it, we can’t ship it.
- 🧩 **Icon packs** sometimes require attribution in an About/Credits page even if modified
- 🔤 **Fonts** can have embedding constraints — verify before bundling

---

## 📚 Related KFM docs (internal)

- 📁 `docs/governance/REVIEW_GATES.md` — policy gates & publish rules
- 📁 `docs/standards/` — STAC / DCAT / PROV profiles
- 📁 `docs/architecture/` — UI/AI “truth path” expectations
- 📄 `CITATION.cff` — how to cite KFM as a project (separate from asset licensing)

---

## 🧾 Attribution Index

> 🟦 **Status:** Add entries as assets are introduced. Keep alphabetical by `id`.

- *(none listed yet — add `web/src/assets/attributions/<asset-id>.md` when introducing assets)* ✅