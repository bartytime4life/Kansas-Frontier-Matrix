[⬅️ Back to **screenshots/**](../README.md)

![Status](https://img.shields.io/badge/status-archive-lightgrey)
![Scope](https://img.shields.io/badge/scope-screenshots-blue)
![Intent](https://img.shields.io/badge/intent-history%20%26%20traceability-purple)

# 🗃️ Screenshot Archive (`_archive/`)

This folder is the **attic** for screenshots that are **no longer actively referenced** by the website/docs, but are still worth keeping for historical context, PR/issue evidence, and “how it used to work” archaeology.

---

## 📦 Where you are (folder map)

```text
web/
└─ 📁 assets/
   └─ 🎞️ media/
      └─ 📸 screenshots/
         ├─ 📄 README.md                 # 📘 Screenshot conventions (naming, sizes, redaction, and usage rules)
         └─ 🗄️ _archive/
            └─ 📄 README.md              # 👈 you are here 📌 Archived/old screenshots kept for reference (not referenced)
```

---

## ✅ Put screenshots here when…

- The screenshot is **not used anywhere “live”** (docs pages, site UI, README embeds), but still useful.
- You’re preserving **before/after** UI states for a closed PR.
- You’re keeping visual evidence for **bugs**, **design iterations**, **map-layer render changes**, etc.
- You need a long-term record of “what users saw” at a specific point in time.

---

## 🚫 Don’t put these here

- **Currently referenced** screenshots (keep them in `../` so links don’t break).
- **Sensitive** screenshots (keys/tokens, private URLs, personal data, internal dashboards).
- Huge binaries (e.g., raw videos, multi-hundred-MB exports). Use releases or external storage if needed.

> ⚠️ Rule of thumb: if it’s referenced from a doc/page that ships today, it’s **not** an archive asset.

---

## 🧭 Quick rules (so this stays useful)

1. **Don’t break links** 🔗  
   Before moving anything into `_archive/`, search the repo for references and update them.
2. **Name files so they’re searchable** 🔎  
   Use the naming convention below (dates + area + topic).
3. **Add context for “important” shots** 🧾  
   If a screenshot captures a key state, add a tiny sidecar `.md` (or `.json`) with repro details.
4. **Keep files lightweight** 🪶  
   Optimize images so the repo doesn’t balloon.

---

## 🗂️ Suggested archive structure

Organize by year (and optionally by feature) so it’s easy to browse:

```text
_archive/
├─ 📅 2024/                 # Archived screenshots grouped by year (not referenced by current docs/UI)
│  ├─ 🗺️ map/               # Old map viewer captures (historical UI/state)
│  └─ ⏳ timeline/           # Old timeline/temporal UI captures
├─ 📅 2025/                 # Archived screenshots grouped by year
│  ├─ 🗺️ map/               # Map viewer captures for 2025-era layouts/features
│  └─ 🎛️ ui/                # Misc UI surfaces (panels, dialogs, settings) from 2025
└─ 📅 2026/                 # Archived screenshots grouped by year
   ├─ 🗺️ map/               # Map viewer captures for 2026-era layouts/features
   └─ 🗂️ data-catalog/       # Data catalog screens (search/filters/metadata) from 2026
```

---

## 🏷️ Naming convention

**Pattern**

`YYYY-MM-DD__area__topic__short-desc__vNN.png`

**Recommended values**
- `area`: `map`, `timeline`, `layer-panel`, `data-catalog`, `docs`, `admin`, `a11y`
- `topic`: `bug`, `feature`, `render`, `perf`, `layout`, `hover`, `mobile`
- `vNN`: optional when you have multiple shots of the same thing (`v01`, `v02`, …)

**Examples**
- `2026-01-17__map__layer-panel__stac-metadata__v01.png`
- `2025-11-03__timeline__feature__range-slider-hover__v02.png`
- `2024-08-19__map__bug__labels-overlap-zoom12__v01.png`

---

## 🧾 Sidecar metadata (optional, but strongly recommended for “high-signal” screenshots)

If a screenshot is important enough to archive, it’s important enough to explain.

Create a file with the same basename:

- `2026-01-17__map__layer-panel__stac-metadata__v01.png`
- `2026-01-17__map__layer-panel__stac-metadata__v01.md`

<details>
<summary><b>Sidecar template</b> (copy/paste)</summary>

```md
---
title: "Layer Panel — STAC Metadata"
captured_at: "2026-01-17"
captured_by: "@your-handle"
context:
  app: "web"
  route: "/#map?..."
  viewport: "1440x900"
  browser: "Chrome 120"
  os: "macOS"
refs:
  pr: "#123"
  issue: "#456"
  commit: "abc1234"
data:
  layer_ids: ["usgs_historic_topo_1894"]
  time_range: "1894"
  bbox_wgs84: [-99.5, 38.3, -98.8, 38.9]
notes: |
  What changed, why it mattered, and how to reproduce.
---

## What this shows
- ...

## How to reproduce
1. ...
```

</details>

---

## 🧰 Archiving workflow

1. **Verify it’s not in active use**  
   Search the repo for the filename/path and confirm it’s safe to move.
2. **Move with git history**  
   Use `git mv` into `_archive/<YYYY>/...` so history stays intact.
3. **Update references if needed**  
   If anything links to it, update the link to the new location (or keep it out of the archive).
4. **Add sidecar metadata** (for important screenshots)  
   Include repro notes + related PR/issue/commit.
5. **Optimize file size**  
   Reduce PNG/WebP size while keeping UI text readable.

---

## 🔁 Restoring a screenshot from the archive

If an archived screenshot becomes “active” again:
- Copy/move it back to the active screenshots folder (`../`)
- Update any docs links
- Avoid renaming unless necessary (stability > prettiness)

---

## 🧼 File format tips

- **PNG** ✅ best for crisp UI / maps with labels
- **WebP** ✅ great for reducing size (if your docs/site support it consistently)
- Keep names **lowercase**, use `__` separators, and avoid spaces

---

## 🔒 Privacy & safety

Do **not** commit screenshots that contain:
- API keys, tokens, secrets, or private endpoints
- Personal data (names/emails/addresses) unless redacted
- Anything under non-public data sharing agreements

When in doubt: **blur/redact** first, or don’t commit it.

---

## 🔗 Related

- `../README.md` — screenshots that are current / actively referenced
- Consider adding an `_archive/INDEX.md` if this folder grows large and you want a curated “greatest hits” list 📌
