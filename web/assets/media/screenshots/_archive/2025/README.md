# 📸 Screenshots Archive — 2025

![Year](https://img.shields.io/badge/Year-2025-blue) ![Status](https://img.shields.io/badge/Status-Archived-lightgrey) ![Media](https://img.shields.io/badge/Media-Screenshots-success) ![Scope](https://img.shields.io/badge/Scope-KFM%20Web%20UI%20%2B%20Docs-6f42c1)

⬅️ Back to **[Archive Index](../README.md)**

> [!IMPORTANT]
> This folder is an **append-only, provenance-friendly archive** for **calendar year 2025**.  
> Prefer **adding** new evidence over **renaming/deleting** existing evidence (old links + audits should never break).

---

## 🧭 Quick Nav

- [✨ Purpose](#-purpose)
- [📦 What belongs here](#-what-belongs-here)
- [🗂️ Folder layout](#️-folder-layout)
- [🏷️ Naming convention](#️-naming-convention)
- [🧾 Metadata sidecars](#-metadata-sidecars)
- [🖥️ Capture matrix](#️-capture-matrix)
- [🛡️ Redaction & safety](#️-redaction--safety)
- [🔗 Embedding screenshots in docs](#-embedding-screenshots-in-docs)
- [✅ Contribution checklist](#-contribution-checklist)
- [🧹 Maintenance](#-maintenance)

---

## ✨ Purpose

This directory preserves **2025 snapshots** of KFM’s UI and map outputs as **evidence artifacts** 🧾.

Typical uses:
- 🧪 **UI regression** (“what changed?” side-by-side comparisons)
- 🧾 **Audit trails** (what the UI displayed at a point in time)
- 🧰 **Docs & Storytelling** (stable screenshots for guides, Story Nodes, release notes)
- 🧯 **Incident response** (“what did users actually see?”)

> [!NOTE]
> If a screenshot is still “current” and actively referenced by documentation/pages, it may belong in a non-archived screenshots folder.  
> This folder is specifically for **2025 historical retention**.

---

## 📦 What belongs here

✅ **Do**
- UI states that matter: map layers panel, legend, timeline, Focus Mode context, search results, error states
- Before/after comparisons for PRs and releases
- Known-good reference screens for regression tests
- Screens that show provenance panels / citations / source drawers (when relevant)

❌ **Don’t**
- Secrets (API keys, tokens), internal-only URLs, private dashboards
- PII (emails, phone numbers, addresses), unless **explicitly redacted**
- Sensitive locations that should not be disclosed (blur/generalize first)
- Random “Screenshot (123).png” with no context

---

## 🗂️ Folder layout

> [!TIP]
> Keep it **predictable**. Humans browse it, but machines may index it later.

Recommended (works well even if the archive grows large):

```text
📁 web/assets/media/screenshots/_archive/2025/
├── 📄 README.md  👈 you are here
├── 📁 01/        # January
├── 📁 02/        # February
├── 📁 03/
├── ...
├── 📁 12/        # December
└── 📄 manifest.2025.json (optional)  # machine index (if/when we add it)
```

Inside each month:
```text
📁 03/
├── 🖼️ 2025-03-14__ui-map__layer-picker-open__1440x900@2x__dark.png
├── 🧾 2025-03-14__ui-map__layer-picker-open__1440x900@2x__dark.meta.json
└── 🖼️ ...
```

> [!WARNING]
> If you must move/rename old files, treat it like a migration: add a short note in this README (or a `MIGRATION.md`) explaining **what changed and why**.

---

## 🏷️ Naming convention

**Goal:** filenames should be **sortable**, **searchable**, and **stable**.

### ✅ Format

```text
YYYY-MM-DD__<area>__<slug>__<WxH>@<DPR>x__<theme>__<lang>__<optional-tags>.png
```

- `area` examples: `ui-map`, `ui-focus`, `ui-search`, `ui-admin`, `api-error`
- `slug` examples: `legend-visible`, `time-slider-scrub`, `layer-source-drawer-open`
- `theme`: `light` | `dark`
- `lang`: `en` | `es` | etc.
- `optional-tags` examples: `before`, `after`, `bug-123`, `pr-456`

### ✅ Examples

- `2025-01-08__ui-map__legend-visible__1365x768@1x__light__en.png`
- `2025-06-22__ui-focus__citations-panel-open__1440x900@2x__dark__en__pr-812.png`
- `2025-10-03__ui-search__no-results-state__390x844@3x__light__en__after.png`

> [!TIP]
> Prefer **kebab-case** in slugs and tags. Avoid spaces and punctuation beyond `_` and `-`.

---

## 🧾 Metadata sidecars

Screenshots are most valuable when they’re *traceable*.

For any screenshot that:
- documents a UI change,
- appears in docs/storytelling,
- or might be used as evidence later…

…add a sidecar file with the same base name:

- `… .meta.json` (recommended)
- `… .meta.md` (acceptable when narrative is more important than structure)

### ✅ Minimal `*.meta.json` template

```json
{
  "captured_at": "2025-06-22T18:42:11Z",
  "capture_type": "manual",
  "area": "ui-focus",
  "description": "Focus Mode showing citations panel opened for a curated Story Node.",
  "source_context": {
    "route": "/focus/<story_slug>",
    "query": "optional",
    "commit": "optional-git-sha",
    "pr": "optional-pr-number"
  },
  "viewport": { "width": 1440, "height": 900, "dpr": 2 },
  "environment": {
    "browser": "chromium",
    "os": "macOS",
    "build": "dev|staging|prod"
  },
  "map_state": {
    "center": [-98.0, 38.5],
    "zoom": 6.2,
    "bearing": 0,
    "pitch": 0,
    "active_layers": ["<stac_item_id_or_layer_id_1>", "<stac_item_id_or_layer_id_2>"],
    "time": "optional-iso-date-or-range"
  },
  "redaction": {
    "contains_pii": false,
    "contains_sensitive_locations": false,
    "notes": "If redacted, describe method (blur/crop/generalize)."
  }
}
```

> [!IMPORTANT]
> If the screenshot shows **a dataset/layer**, include its stable identifier(s) (`STAC/DCAT/PROV IDs` if available).  
> That’s how screenshots become *click-through evidence* instead of “random pictures”.

---

## 🖥️ Capture matrix

To keep screenshots comparable, capture a small set of standard viewports.

| Target | CSS viewport | DPR | Notes |
|---|---:|---:|---|
| 📱 Mobile | 390×844 | 3x | common modern phone |
| 📱 Small mobile | 360×800 | 2–3x | stress layout |
| 📲 Tablet | 768×1024 | 2x | portrait |
| 💻 Laptop | 1366×768 | 1x | baseline desktop layout |
| 🖥️ Desktop | 1920×1080 | 1–2x | wide layout |

Recommended states to capture (when relevant):
- 🧭 Default map view (no panels)
- 🧩 Layer picker open + a layer toggled
- 🧾 Source/provenance drawer open
- 🕰️ Timeline/time slider in-use
- 🔎 Search results
- ⚠️ Error/empty states

---

## 🛡️ Redaction & safety

> [!WARNING]
> Screenshots are **data**. Treat them like datasets.

Before committing:
- ✅ remove/blur tokens, emails, usernames, internal URLs
- ✅ generalize or omit sensitive locations if policy requires
- ✅ verify no hidden side-panels contain private data
- ✅ prefer staging/demo data when capturing UI

If you redacted:
- keep the **original out of git** (unless governance explicitly allows it)
- document the redaction method in the `*.meta.json` (or `*.meta.md`)

---

## 🔗 Embedding screenshots in docs

Use **relative links** so screenshots render in GitHub and in local clones.

### ✅ Basic embed

```md
![Layer picker open showing hillshade enabled](./03/2025-03-14__ui-map__layer-picker-open__1440x900@2x__dark.png)
```

### ✅ Large images (collapsible)

<details>
<summary>Click to expand screenshot</summary>

```md
![Focus Mode citations panel](./06/2025-06-22__ui-focus__citations-panel-open__1440x900@2x__dark__en.png)
```

</details>

> [!TIP]
> Always write **meaningful alt text** (what the reader should notice), not “screenshot”.

---

## ✅ Contribution checklist

When adding screenshots to the 2025 archive:

- [ ] Filename follows convention (`YYYY-MM-DD__...`)
- [ ] Placed under correct month folder (`01`–`12`)
- [ ] Added `*.meta.json` or `*.meta.md` for anything important
- [ ] No secrets / PII / sensitive locations (or properly redacted + documented)
- [ ] If tied to a PR: include PR number in metadata and/or filename tag
- [ ] If tied to a Story Node: include story slug + relevant IDs in metadata

---

## 🧹 Maintenance

- 🗓️ **Monthly sweep:** ensure new files are in the correct month folder
- 🧾 **Metadata hygiene:** backfill sidecars for high-value screenshots
- 🧱 **Stability:** avoid renames/deletes; if necessary, document the migration
- 📦 **(Optional) Manifest:** if we add `manifest.2025.json`, keep it updated for fast indexing/search

---

> [!NOTE]
> Want to improve this archive? Consider adding:
> - a tiny `manifest` generator in `tools/` 📜
> - a CI check enforcing naming + sidecar presence ✅
> - an image optimizer step for WebP derivatives 🧰
