---
title: "Screenshots Archive — 2026"
path: "web/assets/media/screenshots/_archive/2026/README.md"
version: "v1.0.0"
status: "active"
last_updated: "2026-01-18"
doc_kind: "Asset Guide"
license: "TBD"
fair_category: "FAIR+CARE"
care_label: "Public"
sensitivity: "public"
classification: "open"
jurisdiction: "US"
doc_uuid: "urn:kfm:doc:web:assets:screenshots:archive:2026:v1.0.0"
commit_sha: "TBD"
doc_integrity_checksum: "TBD"
---

# 🗃️ Screenshots Archive — 2026

![Year](https://img.shields.io/badge/year-2026-informational)
![Type](https://img.shields.io/badge/type-screenshots-blue)
![Status](https://img.shields.io/badge/status-active-brightgreen)
![Provenance](https://img.shields.io/badge/principle-provenance--first-6f42c1)
![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-enabled-0aa)

A **year-bucket archive** for UI + map-view screenshots captured in **2026**.  
Use this folder when you need **historical snapshots** for: docs, changelogs, QA regressions, UI/UX reviews, and “what changed?” comparisons 📸🧭

> [!IMPORTANT]
> This archive is **provenance-first**: screenshots are treated like evidence.  
> If a screenshot supports a claim, it must be accompanied by **metadata** (what/when/how/where + which data layer(s) + which commit).

---

## 🎯 What belongs here?

✅ **YES**
- UI/UX screenshots (navigation, panels, legends, layer toggles, timelines, search, story nodes)
- Map renders (layer comparisons, time slider states, filters applied)
- Before/after captures from PRs, fixes, refactors
- Annotated images (as long as the original is preserved)

🚫 **NO**
- Secrets (API keys, tokens, credentials)
- Personal data (emails, phone numbers, addresses, unredacted user content)
- Anything that would violate a `care_label` stronger than `Public` (unless explicitly approved & redacted)

> [!NOTE]
> If you must capture sensitive UI for debugging, **redact** first, then store it in a restricted location (not in this public archive).

---

## 🧩 Directory layout

We keep the year folder clean by grouping screenshots into **monthly folders** and **capture sets**.

```text
📁 web/assets/media/screenshots/_archive/2026/
├── 📁 01/
│   ├── 📁 2026-01-18__map__layer-compare__sid-2f3c2c7a/
│   │   ├── 🖼️ main.webp
│   │   ├── 🖼️ main@2x.webp
│   │   ├── 🧾 meta.yml
│   │   ├── 📝 notes.md
│   │   └── 🖼️ thumb.webp
│   └── 📁 2026-01-22__ui__search-panel__sid-90f1bd12/
├── 📁 02/
├── 📁 03/
├── …
└── 🧾 manifest.2026.json  (optional, but recommended)
```

---

## 🏷️ Naming conventions

### 1) Folder name (capture set)
**Format**
```
YYYY-MM-DD__<area>__<short-slug>__sid-<stable-id>/
```

**Examples**
- `2026-02-03__ui__timeline-slider__sid-7c2a19a1/`
- `2026-06-14__map__tornado-layer__sid-3b8f01d4/`
- `2026-11-30__ui__focus-mode-evidence__sid-1a0d9d72/`

**Field rules**
- `area` is one of: `ui`, `map`, `story`, `docs`, `perf`, `a11y`, `qa`
- `short-slug` is kebab-case, < 40 chars
- `sid-*` is the **stable identifier** for the set (don’t reuse it)

> [!TIP]
> Prefer an **information-light** `sid` (random UUID-like) so renames don’t break identity.  
> Human meaning goes in `short-slug` + metadata, not in the ID.

### 2) File names inside a capture set
Use **predictable, script-friendly** names:

| File | Purpose |
|---|---|
| `main.webp` | Primary screenshot (the “one to link”) |
| `main@2x.webp` | Retina version (optional) |
| `before.webp` / `after.webp` | Change comparisons (optional) |
| `annotated.webp` | Marked-up version (optional) |
| `thumb.webp` | Small thumbnail for galleries (optional) |
| `meta.yml` | Required metadata (✅ required) |
| `notes.md` | Human notes (optional) |

---

## 🧾 Metadata requirements (provenance 🔎)

Every capture set **must include** a `meta.yml`.

### ✅ `meta.yml` template

```yaml
# meta.yml — Screenshot Capture Metadata
screenshot_set:
  sid: "sid-2f3c2c7a"                 # stable ID for this capture set
  title: "Layer compare: 1870s rail vs modern roads"
  captured_at: "2026-01-18T15:42:00Z"
  captured_by: "TBD"                  # name/handle
  capture_tool: "browser-devtools"    # e.g., playwright | cypress | devtools | qgis-export
  purpose: "docs"                     # docs | qa | release-notes | design-review | bug-report

context:
  app_area: "map"                     # ui | map | story | docs | perf | a11y | qa
  route: "/map"
  viewport:
    width: 1440
    height: 900
    dpr: 2
  theme: "light"                      # light | dark
  locale: "en-US"

provenance:
  repo:
    commit_sha: "TBD"
    branch: "TBD"
    pr: "TBD"                         # PR number or URL
    issue: "TBD"                      # issue number or URL
  data_layers:
    - layer_id: "TBD"
      dataset_id: "TBD"               # internal ID, DOI, or catalog ID
      source_ref: "TBD"               # citation / url / document ref
  map_state:
    center: [-98.0, 38.5]             # lon, lat (if applicable)
    zoom: 6.2
    bearing: 0
    pitch: 0

governance:
  care_label: "Public"
  sensitivity: "public"
  redactions:
    applied: false
    notes: ""

files:
  primary: "main.webp"
  retina: "main@2x.webp"
  thumbnail: "thumb.webp"
  extras:
    - "notes.md"
```

> [!IMPORTANT]
> If the screenshot is used as **evidence** in a Story Node / report, add:
> - **exact commit SHA**
> - **dataset/layer IDs**
> - **source references** (so the UI can trace back to origins)

---

## 🧼 Quality + performance rules

### Recommended formats
- Prefer **WebP** for web delivery (`.webp`)
- Use PNG only when:
  - you need pixel-perfect UI debugging, or
  - WebP introduces artifacts around text

### Size budgets (guideline)
- `main.webp`: aim for **≤ 500 KB** (UI) / **≤ 1.5 MB** (map-heavy)
- `thumb.webp`: **≤ 80 KB**
- If bigger: re-export, compress, or consider external artifact storage.

> [!TIP]
> Automate your export/compression steps to reduce human error and keep outputs predictable. 🛠️

---

## 🧑‍🦯 Accessibility (a11y) checklist

If a screenshot will be used in docs or UI:
- Provide **alt text** in `meta.yml` (`title` + `purpose` should be descriptive)
- Avoid tiny font captures; zoom UI when needed
- If annotations are used, keep contrast high and don’t rely on color alone

---

## 🔐 Privacy + sensitive content

When in doubt:
- **blur** sensitive text (names, emails, tokens)
- crop out unrelated UI
- set `redactions.applied: true` and explain in `redactions.notes`

> [!WARNING]
> Never commit screenshots that expose secrets. Even if removed later, Git history can preserve them.

---

## 📦 Optional: yearly manifest

If we want the web UI to render a gallery or search index of screenshots, add `manifest.2026.json` at the year root.

```json
{
  "year": 2026,
  "items": [
    {
      "sid": "sid-2f3c2c7a",
      "date": "2026-01-18",
      "area": "map",
      "title": "Layer compare: 1870s rail vs modern roads",
      "path": "01/2026-01-18__map__layer-compare__sid-2f3c2c7a/main.webp"
    }
  ]
}
```

---

## ✅ Definition of Done (per capture set)

Copy/paste and tick off:

- [ ] Folder name follows convention (`YYYY-MM-DD__...__sid-...`)
- [ ] `main.webp` exists and is readable
- [ ] `meta.yml` exists and includes **commit_sha** (or `"TBD"` with a follow-up task)
- [ ] Sensitive content reviewed; redactions applied if needed
- [ ] If used as evidence: data layer IDs + source refs included
- [ ] File sizes are reasonable (compressed where possible)

---

## 🔗 Linking screenshots from docs

Use **relative paths** so links survive domain changes:

```md
![Timeline slider – dark mode](../_archive/2026/02/2026-02-03__ui__timeline-slider__sid-7c2a19a1/main.webp)
```

---

## 🧰 Maintenance & archiving tips

- Don’t reorganize old months unless you also update manifest + docs references.
- If you need a clean export of this year’s archive for a release bundle, prefer a reproducible archive step (e.g., git-based export).

---

## 🧠 Quick glossary

| Term | Meaning |
|---|---|
| **capture set** | Folder containing one “screenshot event” + metadata |
| **sid** | Stable ID for a capture set (don’t reuse) |
| **provenance** | Traceability: how/when/where the screenshot was produced + what it represents |

---
