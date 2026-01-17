<!-- According to a document from 2025-12-17, this screenshot pack is aligned with KFM’s catalog-driven + provenance-first UI principles. -->

# 🗂️ Data Catalog UI Screenshots

![UI](https://img.shields.io/badge/UI-Data%20Catalog-0b7285?style=for-the-badge)
![Assets](https://img.shields.io/badge/Assets-Screenshots-343a40?style=for-the-badge)
![Principle](https://img.shields.io/badge/Principle-Provenance--First-1971c2?style=for-the-badge)

> 📌 **Purpose:** This folder contains the **canonical** screenshots for the **Data Catalog UI** — the “browse/search datasets → open dataset details → verify provenance/citations → download/preview” experience.

---

## 🎯 What belongs in this folder

✅ **Do store**
- 🖼️ **UI screenshots** (PNG/WebP) representing stable, “reference” states of the Data Catalog UI
- 🧾 Optional **sidecar metadata** describing how a screenshot was captured (route/state/dataset id)

🚫 **Do not store**
- Random ad-hoc screenshots from debugging
- Screenshots with secrets, tokens, private user info, or sensitive locations
- Duplicates (keep this set small, intentional, and up-to-date)

---

## 🧭 Why this exists (KFM-specific)

KFM is built around **catalog-first discovery** (DCAT/STAC) and **provenance-first trust** (PROV). The Data Catalog UI is where that becomes “real” to users:
- users can **find** datasets quickly,
- then **inspect metadata + sources**,
- then **trace lineage** (what it came from / how it was produced),
- and finally **use it** (preview, download, layer toggle, etc.).

This folder is the visual “truth set” for that experience.

---

## 🧱 Folder layout 🧩

```text
📦 web/
  📂 assets/
    📂 media/
      📂 screenshots/
        📂 ui/
          📂 data-catalog/
            🖼️ catalog--list@1440w.png
            🖼️ catalog--filters@1440w.png
            🖼️ dataset--detail--overview@1440w.png
            🖼️ dataset--detail--provenance@1440w.png
            🖼️ dataset--detail--download@1440w.png
            📄 README.md  👈 you are here
```

> ✨ Keep filenames stable so docs, PR templates, and issue reports don’t break.

---

## 🏷️ Naming convention (deterministic + diff-friendly)

Use **kebab-case**, and encode the important UI state:

**Pattern**
```text
<area>--<view>--<state>@<width>w.<ext>
```

**Examples**
- `catalog--list@1440w.png`
- `catalog--filters--theme-time-region@1440w.png`
- `dataset--detail--overview@1440w.png`
- `dataset--detail--provenance@1440w.png`
- `dataset--detail--stac-assets@1440w.png`
- `dataset--detail--dcat-metadata@1440w.png`
- `dataset--detail--download@1440w.png`

**Allowed extensions**
- ✅ `.png` (preferred for crisp UI text)
- ✅ `.webp` (acceptable when size matters, but ensure text stays sharp)

---

## ✅ Canonical screenshot set (minimum)

> Use this checklist as the “definition of done” for Data Catalog UI changes.

### 📚 Catalog browsing
- [ ] `catalog--list@1440w.png` — default list/grid view + dataset count visible
- [ ] `catalog--search@1440w.png` — search query applied + results updated
- [ ] `catalog--filters--theme-time-region@1440w.png` — faceted filters panel open (theme/time/region)

### 🧾 Dataset detail (trust + usability)
- [ ] `dataset--detail--overview@1440w.png` — title, description, keywords/tags, license, attribution
- [ ] `dataset--detail--dcat-metadata@1440w.png` — DCAT-style metadata section visible (publisher, distributions, etc.)
- [ ] `dataset--detail--stac-assets@1440w.png` — STAC-style asset listing / bbox / temporal extent / preview hooks
- [ ] `dataset--detail--provenance@1440w.png` — PROV/lineage panel visible (inputs → activity → outputs)
- [ ] `dataset--detail--download@1440w.png` — downloads/distributions visible (format options, API link, etc.)

### 🔎 Optional (only if the UI supports it)
- [ ] `dataset--detail--map-preview@1440w.png` — dataset preview panel/map mini-view
- [ ] `dataset--detail--citations@1440w.png` — explicit “sources/citations” area expanded
- [ ] `catalog--empty-state@1440w.png` — empty results with helpful guidance
- [ ] `catalog--error-state@1440w.png` — error UI (API down / timeout) with user-safe messaging

---

## 📸 Capture standards (quality bar)

### 🖥️ Viewport + appearance
- **Width:** 1440px (preferred) or 1280px (fallback)
- **Theme:** whichever is canonical for KFM docs (be consistent)
- **Zoom:** 100% browser zoom
- **Panels:** open the panel(s) that matter (filters / metadata / provenance) — don’t hide the important bits

### 🧼 Content hygiene
- ✅ Use **safe/demo datasets** (no private user content)
- ✅ Remove or blur: emails, API keys, tokens, personal names, internal URLs
- ✅ If any coordinates might be sensitive: prefer generalized views (and follow governance rules)

### 🧾 Provenance visibility
If a screenshot is meant to document a “trust moment,” it must show at least one of:
- source attribution
- citation/reference section
- provenance/lineage UI
- license + usage constraints

---

## 🧾 Sidecar metadata (recommended) 🔍

For each screenshot, you *may* add a small JSON file with deterministic capture notes:

**Filename**
```text
<image-name>.<ext>.shot.json
```

**Example**
```json
{
  "route": "Data Catalog",
  "ui_state": {
    "search": "tornado",
    "filters": ["theme:hazards", "time:1950-2024", "region:Kansas"]
  },
  "dataset_id": "kfm:dataset:hazards:tornado-tracks",
  "viewport": { "width": 1440, "height": 900, "zoom": 1.0 },
  "theme": "light",
  "captured_for": "docs + PR reference",
  "notes": "Provenance panel expanded; download section visible"
}
```

> 🧠 This mirrors the broader KFM idea that “anything user-facing should be traceable and repeatable.”

---

## 🔁 Updating screenshots (workflow)

1. **Identify impact**
   - If a PR changes Data Catalog layout, filters, dataset details, provenance UI, downloads, or accessibility → screenshots likely need updates.

2. **Update the minimum set**
   - Keep filenames stable when possible (to reduce doc churn).

3. **Review for consistency**
   - Compare against older screenshots (spacing, typography scale, content safety).

4. **Update this README**
   - If you add/remove a canonical screenshot, update the checklist and/or inventory below.

---

## 🧪 Quick review checklist (PR-ready)

- [ ] Text is readable at GitHub preview size
- [ ] No secrets/PII/sensitive coordinates leaked
- [ ] “Trust surfaces” are visible (license/source/provenance) where relevant
- [ ] UI state is intentional (not mid-animation, not partial render)
- [ ] Filenames follow convention
- [ ] Any new screenshot has a `.shot.json` (if your change is complex)

---

## 🗃️ Screenshot inventory (keep current)

| File | What it shows | Notes |
|------|---------------|-------|
| `catalog--list@1440w.png` | Default catalog view | Stable baseline |
| `catalog--filters--theme-time-region@1440w.png` | Faceted filters | Theme/time/region |
| `dataset--detail--overview@1440w.png` | Dataset overview | Description + license |
| `dataset--detail--provenance@1440w.png` | Lineage/provenance | Inputs → activity → outputs |
| `dataset--detail--download@1440w.png` | Downloads | Formats + link(s) |

---

## 📎 Embedding screenshots in docs

### Markdown
```md
![Data Catalog — list view](./catalog--list@1440w.png)
```

### HTML (recommended for consistent sizing)
```html
<img
  src="./dataset--detail--provenance@1440w.png"
  width="900"
  alt="Data Catalog dataset detail view with provenance/lineage panel expanded"
/>
```

---

## 🚫 Common mistakes (and fixes)

| ❌ Don’t | ✅ Do |
|---|---|
| Upload a screenshot with a random name like `Screenshot 2026-01-17.png` | Use the naming convention (`dataset--detail--overview@1440w.png`) |
| Capture UI mid-loading / skeleton-only | Wait for stable render and open the relevant panel |
| Hide provenance/citation info | Expand provenance/citations when documenting “trust moments” |
| Use real user data or leaked tokens | Use safe/demo data and scrub sensitive content |
| Dump dozens of near-duplicates | Keep a small canonical set; add only when justified |

---

💡 **Tip:** If you’re unsure whether a screenshot should be “canonical,” ask:  
**Would a future contributor use this to understand how Data Catalog is *supposed* to look?**
