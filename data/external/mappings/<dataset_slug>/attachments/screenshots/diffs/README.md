# 🖼️ Screenshot Diffs (Visual QA Evidence)

![Evidence-First](https://img.shields.io/badge/Evidence--First-%F0%9F%94%8E-blue?style=flat-square)
![Provenance-Friendly](https://img.shields.io/badge/Provenance-%F0%9F%94%97-blue?style=flat-square)
![Reviewer-Ready](https://img.shields.io/badge/PR--Review-%E2%9C%85-blue?style=flat-square)

**Purpose:** This folder holds **visual “before → after” evidence** for changes to a mapping dataset (georeferencing, tiling, styling, layer logic, clipping, labeling, etc.). It exists to make reviews faster and regressions obvious. 🧪🗺️

> [!NOTE]
> Treat these diffs like “visual provenance” — they should be *repeatable* and *traceable* (same view, same layers, clear explanation).

---

## 🧭 Quick Links

- ⬆️ Back to **screenshots/**: `../`
- ⬆️ Back to **attachments/**: `../../`
- ⬆️ Back to **dataset root**: `../../../`

---

## 📦 What belongs here?

Use this folder when a change:
- ✅ alters **visual output** (alignment, rendering, styling, transparency, labels, symbology)
- ✅ affects **what users see** (UI layer toggles, defaults, legend/attribution, visible extents)
- ✅ changes **map accuracy** (rubber-sheeting, control points, projection fixes)

Avoid adding screenshots here when:
- ❌ nothing changes visually (use normal text diffs + metadata logs)
- ❌ screenshots include sensitive data or credentials (sanitize first 🔒)

---

## 🗂️ Folder Contract

Keep `diffs/` tidy by grouping each change into its own subfolder:

```text
📁 diffs/
├─ README.md                           👈 you are here
├─ 📁 YYYY-MM-DD__from__to__short-title/
│  ├─ before.png
│  ├─ after.png
│  ├─ diff.png                         (optional but recommended)
│  ├─ side-by-side.png                 (optional)
│  ├─ manifest.yml                      ⭐ recommended
│  └─ notes.md                          (optional)
└─ 📁 YYYY-MM-DD__from__to__short-title__zoom-12/
   ├─ before.png
   ├─ after.png
   └─ manifest.yml
```

> [!TIP]
> Prefer **many small, well-labeled diff sets** over one giant dump of images.

---

## 🏷️ Naming Conventions

**Diff set folder name format:**

```
YYYY-MM-DD__<from>__to__<to>__<short-title>
```

Where:
- `YYYY-MM-DD` = capture date
- `<from>` / `<to>` = commit SHA, dataset version, or pipeline run ID (pick one and be consistent)
- `<short-title>` = kebab-case summary (e.g., `georef-fix`, `tile-edges`, `labeling-update`)

Examples:
- `2026-01-29__a1b2c3d__to__d4e5f6a__georef-fix`
- `2026-01-29__v1.2__to__v1.3__style-ramp-adjustment`

---

## 📸 Capture Standards (so diffs are comparable)

To make diffs meaningful, keep the capture setup consistent:

### ✅ Always keep identical
- **BBox / center / zoom**
- **Visible layers + ordering**
- **Basemap** (if any) and opacity
- **Theme** (light/dark), UI scale, and font settings (if applicable)

### 🧩 Recommended views to capture
- 🌎 **Overview** (full extent)
- 🔍 **2–3 zoomed checks** (known landmarks / boundaries / seam edges)
- 🧷 **Edge cases** (tile boundaries, labels collision zones, coastline/river alignment, etc.)

> [!IMPORTANT]
> If the “before” screenshot cannot be re-created, the diff set must clearly explain why (e.g., upstream source removed, rendering engine changed).

---

## 🧾 Minimal `manifest.yml` (recommended)

Add a `manifest.yml` to every diff set so reviewers can trace the “what/where/how” quickly:

```yaml
dataset_slug: "<dataset_slug>"
created_at: "YYYY-MM-DD"
author: "@your-handle"

from:
  ref: "a1b2c3d"           # commit SHA OR dataset version OR pipeline run id
  artifact: "path/or/url/to/before/output"  # optional but ideal

to:
  ref: "d4e5f6a"
  artifact: "path/or/url/to/after/output"

view:
  bbox: [west, south, east, north]   # optional but great
  zoom: 12                           # optional
  layers:
    - "<layer-id-1>"
    - "<layer-id-2>"
  notes: "Same view settings for before/after."

files:
  before: "before.png"
  after: "after.png"
  diff: "diff.png"                   # optional
  side_by_side: "side-by-side.png"   # optional

summary:
  change: "Shifted control points; improved alignment near county boundary."
  expected_visual_effect:
    - "Road overlay aligns with river bend"
    - "Boundary line no longer drifts at tile seams"
```

---

## 🧪 Optional: how to create a `diff.png`

If you produce a pixel-level diff image, prefer a **high-contrast overlay** and ensure the legend (if any) is explained in `notes.md`.

> [!TIP]
> If you can’t generate a pixel diff reliably (e.g., label randomness), use **side-by-side** images and call out the exact areas to inspect.

---

## 🗜️ File Formats & Repo Hygiene

- ✅ Use **PNG** for UI/text clarity.
- ✅ Use **JPG** for photo-like imagery if size is an issue.
- ✅ Keep files reasonably sized (crop to ROI when possible).
- ✅ Name files predictably: `before.png`, `after.png`, `diff.png`.

> [!CAUTION]
> Don’t commit huge binaries unnecessarily. Prefer compression, cropping, or (if your repo uses it) a large-file strategy (e.g., LFS).

---

## 🔗 Embedding screenshots in other docs

Use **relative paths** so links work on GitHub and offline:

```md
![Before: alignment near <place>](./2026-01-29__a1b2c3d__to__d4e5f6a__georef-fix/before.png)
![After: corrected alignment](./2026-01-29__a1b2c3d__to__d4e5f6a__georef-fix/after.png)
```

> [!NOTE]
> Always include meaningful **alt text** for accessibility ♿️

---

## ✅ Reviewer Checklist

- [ ] Folder name follows `YYYY-MM-DD__from__to__title`
- [ ] `before` and `after` are the **same view** (bbox/zoom/layers)
- [ ] Changes are obvious or clearly annotated in `notes.md`
- [ ] `manifest.yml` exists (or equivalent metadata exists)
- [ ] No sensitive info is visible
- [ ] Screenshots are cropped/compressed appropriately

---

## 🧼 Cleanup Policy

If a diff set becomes obsolete:
- Prefer keeping it if it documents an important fix or decision history 🧠
- If removing, ensure the related PR/issue retains enough context elsewhere

---

## ✨ Golden Rule

If a future maintainer asks, *“Why did this map change?”*  
A good diff set lets them answer that question in **under 60 seconds**. ⏱️✅
