<!-- Path: web/src/assets/_meta/README.md -->

# 🧾 Asset Metadata Registry (`web/src/assets/_meta`)

![Evidence-first](https://img.shields.io/badge/Evidence--first-✅-brightgreen)
![Provenance](https://img.shields.io/badge/Provenance-🧬%20required-blue)
![Licensing](https://img.shields.io/badge/Licensing-⚖️%20no%20mystery%20files-yellow)
![Contract-first](https://img.shields.io/badge/Contract--first-📜-informational)

> **Rule of thumb:** if we ship an asset, we must be able to answer **(1) where it came from**, **(2) what license allows us to ship it**, and **(3) what we changed**.

This folder is the **UI-side metadata layer** for static assets under `web/src/assets/`:
- ✅ icons, images, fonts, sprites, map-style resources, UI illustrations
- ✅ any “bundled” files that end up inside the built frontend
- ❌ *not* the canonical metadata home for datasets (that’s handled by STAC/DCAT/PROV + the API)

---

## 🔎 TL;DR

For every asset file in `web/src/assets/**`, create a matching metadata file in `web/src/assets/_meta/**`:

- **Asset:** `web/src/assets/icons/compass.svg`
- **Meta:**  `web/src/assets/_meta/icons/compass.svg.meta.json`

The `_meta/` tree should **mirror** the `assets/` tree.

---

## 🎯 Why `_meta` exists

KFM is built around:
- **contract-first** boundaries (UI consumes APIs; it doesn’t “smuggle” data around), and
- **evidence/provenance** guardrails (no unsourced additions, no untraceable artifacts).

In that spirit, `_meta/` exists to prevent:
- 🕳️ **mystery files** (unknown origin)
- ⚖️ **license risk** (unclear redistribution rights)
- 🧩 **broken attributions** (icons/images/fonts with no credit trail)
- 🧪 **unreproducible transforms** (edits with no record)

---

## 🗂️ Recommended layout

```text
📁 web/
└── 📁 src/
    └── 📁 assets/
        ├── 📁 icons/
        │   ├── 🖼️ compass.svg
        │   └── 🖼️ timeline.svg
        ├── 📁 images/
        │   └── 🖼️ hero-kansas.webp
        ├── 📁 fonts/
        │   └── 🔤 inter-var.woff2
        └── 📁 _meta/
            ├── 📄 README.md   👈 you are here
            ├── 📁 icons/
            │   ├── 📄 compass.svg.meta.json
            │   └── 📄 timeline.svg.meta.json
            ├── 📁 images/
            │   └── 📄 hero-kansas.webp.meta.json
            ├── 📁 fonts/
            │   └── 📄 inter-var.woff2.meta.json
            └── 📁 licenses/   (optional: stored license texts)
                └── 📄 OFL.txt
```

> 💡 **Mirror rule:** if you create `assets/<path>/<file>`, create `_meta/<path>/<file>.meta.json`.

---

## ✅ What belongs in `web/src/assets/`

### ✅ Yes
- UI icons (SVG), UI illustrations, logos
- Map sprites / glyphs / style companion files (when bundled)
- Fonts you ship with the app
- Small static images used by components (e.g., empty states, onboarding)

### ❌ No
- “Real data” (GeoJSON/tilesets/csv/parquet) that bypasses the governed pipeline
- Anything big enough that it should be hosted/served elsewhere (object storage, tiles API, etc.)
- Anything with unknown or incompatible redistribution terms

---

## 📜 Metadata contract (`*.meta.json`)

### Naming
- `asset.ext` → `asset.ext.meta.json`
- Keep extensions in the meta filename to avoid collisions:
  - `logo.svg` and `logo.png` can co-exist cleanly.

### Minimal required fields (v1)
Below is the **v1 contract** we use for asset metadata. Keep it simple, but complete.

| Field | Required | Type | Notes |
|---|---:|---|---|
| `schema_version` | ✅ | string | e.g. `"asset-meta@1"` |
| `id` | ✅ | string | stable ID used by code/UI (kebab or dot style) |
| `file` | ✅ | string | asset path relative to `web/src/assets/` |
| `kind` | ✅ | string | `icon`, `image`, `font`, `sprite`, `map-style`, `other` |
| `title` | ✅ | string | human name |
| `description` | ✅ | string | why it exists / where it appears |
| `attribution` | ✅ | string | what we show in UI credit lists |
| `license` | ✅ | object | must include at least `spdx` **or** `name` and `url` |
| `source` | ✅ | object | origin + retrieval details |
| `created_at` | ✅ | string | ISO date/time |
| `checksums.sha256` | ✅ | string | integrity + reproducibility |
| `transformations` | ✅ | array | even if empty (`[]`) |
| `sensitivity` | ✅ | object | defaults to public unless flagged |

### Optional (but strongly recommended)
- `alt` (for images/icons used as `<img>` content)
- `tags` (for search / filtering)
- `related.datasets[]` (dataset IDs that this asset represents)
- `related.story_nodes[]` (story slugs if used in narrative UI)
- `ui.usage[]` (components/routes where it’s used)

---

## 🧩 Example metadata file

```json
{
  "schema_version": "asset-meta@1",
  "id": "ui.icon.compass",
  "file": "icons/compass.svg",
  "kind": "icon",
  "title": "Compass icon",
  "description": "Used in the map controls to re-center / re-orient the view.",
  "alt": "Compass",

  "source": {
    "name": "Example Icon Set",
    "url": "https://example.com/icons/compass",
    "retrieved_at": "2026-02-05",
    "retrieved_by": "KFM dev"
  },

  "license": {
    "spdx": "MIT",
    "url": "https://example.com/license",
    "text_file": "licenses/MIT.txt"
  },

  "attribution": "Example Icon Set (MIT) — modified by KFM",

  "checksums": {
    "sha256": "REPLACE_WITH_SHA256"
  },

  "transformations": [
    {
      "at": "2026-02-05",
      "tool": "svgo",
      "notes": "Optimized paths; removed editor metadata."
    }
  ],

  "sensitivity": {
    "class": "public",
    "notes": ""
  },

  "related": {
    "datasets": [],
    "story_nodes": []
  },

  "tags": ["map", "control", "ui"]
}
```

> ✅ If you touched the asset (resize, crop, color change, cleanup, font-subset, sprite generation), **record it** in `transformations[]`.

---

## 🧠 How the app should use `_meta`

### 1) Attributions UI (recommended)
Use `_meta` to power:
- 📜 “Credits / Licenses” screen
- 🗺️ Layer legend credits (for icons + style assets)
- 🧩 Contextual attribution tooltips

### 2) Stable IDs (important)
Bundlers often rewrite asset filenames (hashing, inlining, etc.). The `id` in metadata is the **stable handle** you can reference even if the output file name changes.

---

## 🧰 Add-an-asset checklist

When adding or updating an asset:

- [ ] Put file in the right place under `web/src/assets/`
- [ ] Create matching `*.meta.json` under `web/src/assets/_meta/`
- [ ] Confirm **license** allows redistribution
- [ ] Add **attribution** text suitable for UI display
- [ ] Record **transformations** (or explicitly `[]`)
- [ ] Compute & paste **SHA-256**
- [ ] If culturally sensitive / restricted: set `sensitivity.class` accordingly and follow governance review

---

## 🚧 Guardrails (non-negotiable)

### ✅ Shipping rule
If an asset does not have:
- **source**, **license**, and **attribution**
then it **does not ship**.

### ✅ “Don’t bypass the pipeline” rule
If an “asset” is actually a dataset (or derived dataset), it must live in the governed data pipeline (ETL → catalog → API). Don’t park it here just because it “works in the UI”.

---

## 🧪 Validation (recommended automation)

Suggested CI/dev checks:
- 🔍 verify every `assets/**` file has a matching `_meta/**.meta.json`
- 🧾 validate metadata files against a JSON Schema (`asset-meta@1`)
- 🔐 verify `checksums.sha256` matches the file
- ⚖️ fail if license fields are incomplete

> Future-friendly pattern: generate a single `registry.json`/`registry.ts` at build-time so UI can import one canonical list of asset metadata.

---

## 🧯 Common pitfalls

- **Renaming the asset but not the meta** → breaks credit lists
- **Copying icons from the internet** → license ambiguity
- **Using a font without including its license** → attribution/legal problems
- **Embedding data files as “assets”** → bypasses governance + provenance controls

---

## 🔗 Related docs (repo-level)

- `../../../../docs/MASTER_GUIDE_v13.md` (canonical structure + pipeline)
- `../../../../docs/standards/` (STAC/DCAT/PROV profiles)
- `../../../../data/provenance/` (dataset lineage logs)
- `../../../../docs/governance/REVIEW_GATES.md` (when something needs review)

---

## ✍️ Conventions

- Filenames: `kebab-case.ext`
- IDs: `dot.separated.ids` **or** `kebab-case` — pick one and be consistent
- Dates: ISO 8601 (`YYYY-MM-DD` or full timestamp)
- Keep assets small; push heavy media to a proper delivery path

---

## 🧩 Questions?

If you’re not sure whether something is an “asset” or “data,” assume it’s **data** and route it through the pipeline (catalog → API → UI). This folder is for **presentation artifacts**, not for bypassing contracts.
