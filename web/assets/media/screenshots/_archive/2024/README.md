<a id="top"></a>

# 📸 Screenshot Archive — 2024

![Archive Year](https://img.shields.io/badge/archive-2024-blue)
![Asset Type](https://img.shields.io/badge/type-ui%20%2B%20map%20screenshots-orange)
![Practice](https://img.shields.io/badge/provenance-first-success)
![Rule](https://img.shields.io/badge/rule-do%20not%20overwrite%20files-critical)

> 🧭 **Path:** `web/assets/media/screenshots/_archive/2024/`  
> This directory preserves **immutable UI + map screenshots captured during 2024** for **Kansas Frontier Matrix (KFM)**.  
> Screenshots here are treated as **visual evidence** to support KFM’s goals of being searchable, mappable, auditable, and modelable — with **transparency + provenance** as first-class citizens.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## ✨ Why this exists

KFM is built around **provenance-first** principles: users should be able to inspect what they’re seeing (source, metadata, processing context), and screenshots used in documentation should preserve that spirit.  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

This folder is a **time capsule** for anything captured in **calendar year 2024**, including:
- Docs screenshots (tutorials, guides, READMEs)
- Release/change visuals (before/after UI changes)
- Storytelling assets (historical maps, layer overlays, timeline views)
- Research/report snapshots where “how it looked in 2024” matters

---

## ✅ What belongs here

- 🗺️ **Map UI screenshots** (layer lists, legends, tooltips, time sliders, etc.)
- 🧩 **Feature UI screenshots** (search, dataset cards, inspector panels, focus/analysis panels)
- 🧾 **Audit/provenance UI screenshots** (anything showing citations, metadata, lineage, source links)
- 🧪 **Experiment/report screenshots** that were captured in 2024 and referenced in docs

---

## 🚫 What does *not* belong here

- 🔐 Anything with **secrets** (API keys, tokens), credentials, internal URLs
- 🧍 Any **personal data** (emails, phone numbers, private addresses, private account names)
- 📦 Huge binary dumps (videos, full exports) — keep this folder “screenshot-only”
- 🧨 “Temporary” images meant for quick chat sharing (use a scratch folder elsewhere)

---

## 🔒 Archive rules (treat this as read-only)

1. **Never overwrite** an existing file.  
   ✅ Add a new version instead (`__v2`, `__v3`, …).
2. **Never rename** files once committed.  
   Filenames act as stable identifiers for docs/history.
3. **Don’t “clean up”** old screenshots to make them prettier.  
   Historical accuracy > aesthetic refactors.
4. If a screenshot is **wrong** (bad data, wrong UI state), create a replacement file + update references.

> ⚠️ If you *must* deprecate an image: keep it, but add a note in the **Index** section (below) explaining what replaced it.

---

## 🗂️ Suggested organization (flexible, but consistent)

You can keep images flat, or optionally group them by month/feature if this folder grows.

```text
📁 web/assets/media/screenshots/_archive/2024/
├── 📄 README.md
├── 🖼️ 2024-01-15__map__layer-inspector__light__1440x900.webp
├── 🖼️ 2024-01-15__map__layer-inspector__light__1440x900__v2.webp
├── 🧾 2024-01-15__map__layer-inspector__light__1440x900.meta.json
└── 📁 2024-06/
    ├── 🖼️ 2024-06-02__focus-mode__citations-panel__dark__1440x900.webp
    └── 🧾 2024-06-02__focus-mode__citations-panel__dark__1440x900.meta.json
```

> 💡 Tip: If you introduce subfolders (like `2024-06/`), keep the **filename date** anyway — it stays searchable even when moved.

---

## 🏷️ Naming convention (recommended)

Use a human-readable, grep-friendly filename that encodes “what + where + how”.

### ✅ Pattern

```text
YYYY-MM-DD__surface__subject__state__theme__WIDTHxHEIGHT[__vN].ext
```

### 🧩 Field meanings

- `YYYY-MM-DD` → capture date (local)
- `surface` → `map` | `ui` | `focus-mode` | `dataset` | `story` | `pipeline` (pick from a small set)
- `subject` → what feature/page is shown (`layer-inspector`, `search-results`, `timeline-filter`, …)
- `state` → important UI state (`hover-tooltip`, `selected-feature`, `error-state`, …)
- `theme` → `light` | `dark`
- `WIDTHxHEIGHT` → viewport size (helps reproduce)
- `__vN` → only when you intentionally replace/iterate (never overwrite)

### ✅ Examples

- `2024-03-14__map__tornado-tracks__timeline-filter__light__1440x900.webp`
- `2024-07-01__ui__dataset-card__expanded__dark__1440x900.png`
- `2024-11-22__focus-mode__citations__open__light__1920x1080__v2.webp`

---

## 🧾 Metadata sidecar (recommended for provenance)

KFM treats **metadata + citations** as first-class. Screenshots should follow the same ethos.  [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

For any screenshot used in docs/reports, add a sidecar:

- Same basename, extension `.meta.json` (or `.md` if you prefer prose)
- Example:  
  `2024-03-14__map__tornado-tracks__timeline-filter__light__1440x900.meta.json`

### ✅ Minimal `.meta.json` template

```json
{
  "title": "Timeline filtering tornado tracks (Map view)",
  "captured_at": "2024-03-14",
  "surface": "map",
  "route_or_context": "/map?layers=tornado_tracks&year=1950-1960",
  "viewport": { "width": 1440, "height": 900 },
  "theme": "light",

  "kfm": {
    "git_commit": "PUT_COMMIT_HASH_HERE",
    "build_or_version": "optional"
  },

  "provenance": {
    "datasets": [
      {
        "id": "dataset-id-or-slug",
        "source": "source link or catalog reference",
        "license": "license name or identifier",
        "citation": "short citation string (or pointer to dataset metadata)"
      }
    ],
    "notes": "Any important context needed to interpret this screenshot"
  },

  "redaction": {
    "performed": false,
    "notes": ""
  }
}
```

> 🧠 Rule of thumb: If someone asks “what data is that?” or “what build was this?” → the `.meta.json` should answer.

---

## 📷 Capture checklist (quality + reproducibility)

- [ ] Capture at a **consistent viewport** (prefer `1440x900` or `1920x1080`)
- [ ] Use **sRGB** color profile (default for web)
- [ ] Ensure **key UI context is visible** (legend, layer list, active filters)
- [ ] If screenshot supports provenance: keep **citations/metadata panel visible** or reference it in `.meta.json`  [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- [ ] Remove noise:
  - [ ] close unrelated devtools
  - [ ] hide debug overlays unless relevant
  - [ ] avoid “random” cursor hover states unless that hover is the point
- [ ] Verify no secrets/PII are present (see redaction rules below)

---

## 🗜️ File formats & size budget

**Preferred:**
- ✅ `.webp` for most UI screenshots (great compression)
- ✅ `.png` if you need **pixel-perfect text** or **transparency**

**Avoid:**
- ❌ `.jpg` for UI (can introduce text artifacts)
- ❌ `.bmp` / raw formats (too large)

**Size guideline (soft):**
- Aim for **< 1 MB** per screenshot when possible.
- If it must be larger (dense map, lots of labels), justify it in metadata.

---

## 🧼 Redaction & safety rules

If a screenshot contains anything sensitive:
- 🔒 redact first (blur/cover), then commit
- 🧾 set `"redaction.performed": true` in metadata
- 📝 describe what was redacted in `"redaction.notes"`

**Common redaction targets**
- API keys, tokens, auth headers
- Private dataset URLs or signed URLs
- User identifiers, emails, phone numbers
- Internal hostnames / non-public endpoints

> ✅ Best practice: If you’re unsure whether something is sensitive — treat it as sensitive.

---

## 🔗 How to reference screenshots in Markdown

Use **relative paths** so docs work locally and on GitHub.  [oai_citation:4‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)

```md
![Timeline filtering tornado tracks (1950–1960)](./2024-03-14__map__tornado-tracks__timeline-filter__light__1440x900.webp)
```

If you have a metadata sidecar, link it near the image:

```md
- Screenshot metadata: [`2024-03-14__map__tornado-tracks__timeline-filter__light__1440x900.meta.json`](./2024-03-14__map__tornado-tracks__timeline-filter__light__1440x900.meta.json)
```

---

## 🧾 Optional: Index (add entries for doc-facing screenshots)

If a screenshot is referenced in docs, add an entry here so we can find it later without searching the entire tree.

| Date | Screenshot | Surface | What it shows | Used in | Notes |
|---:|---|---|---|---|---|
| 2024-03-14 | `2024-03-14__map__tornado-tracks__timeline-filter__light__1440x900.webp` | map | Timeline filtering tornado tracks | `docs/...` | Includes `.meta.json` |

---

## 📚 References

- Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation  [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- MARKDOWN_GUIDE_v13.md.gdoc  [oai_citation:6‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx  [oai_citation:7‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)

---

⬆️ [Back to top](#top)
