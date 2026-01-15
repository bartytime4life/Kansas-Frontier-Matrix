# 🗺️ Map Metadata Icons (`web/assets/icons/map/meta/`)

![Scope](https://img.shields.io/badge/scope-map%20metadata%20UI-blue)
![Assets](https://img.shields.io/badge/type-static%20assets-informational)
![Preferred](https://img.shields.io/badge/preferred-SVG-success)
![Principle](https://img.shields.io/badge/principle-provenance--first-2ea44f)

A small, **purpose-built icon set** for representing **map layer metadata** (source, license, time, provenance, QA, sensitivity, citations, etc.) in the web UI. These icons are not “map symbols” (legend symbology) — they’re **metadata badges** meant to keep trust & attribution visible at-a-glance. 🧾✅

---

## 🎯 What lives here?

This folder should contain icons used anywhere we render **metadata chips / badges / rows** for:

- 🧱 **Data layers** (catalog cards, layer panels)
- 📍 **Feature popups** (attribute + provenance summary)
- 📚 **Story Nodes** (attribution + evidence cues)
- 🧠 **Focus Mode** (AI outputs that must be labeled + cite-backed)

---

## 🧭 Folder context

```text
web/ 🌐
└─ assets/ 🗃️
   └─ icons/ ✨
      └─ map/ 🗺️
         ├─ meta/ 🧾   ← you are here
         ├─ legend/ 🧩  (if present: symbology/legend glyphs)
         └─ ui/ 🧰      (if present: map controls, tools, etc.)
```

---

## 🧩 Meta icon tokens

> **Rule of thumb:** A meta icon must map to a *real* field in a contract/catalog/graph response. No “mystery meaning,” no “decorative provenance.” 🧬🔍

Below is a recommended baseline set. Use these filenames as **stable tokens** wherever possible.

| Token (filename) | Meaning 🧠 | Typical backing field(s) 🧾 | UI expectation 👀 |
|---|---|---|---|
| `source.svg` | Original data source / provider | STAC `providers`, DCAT `dct:source` | Click → source record |
| `license.svg` | Usage rights / license | STAC `license`, DCAT `dct:license` | Tooltip → license text |
| `cite.svg` | Citations/evidence available | `citations[]`, story footnotes | Click → citations drawer |
| `provenance.svg` | Processing lineage / derivation | PROV links, `processing_steps[]` | Click → lineage view |
| `time.svg` | Temporal extent / timestamp | STAC `extent.temporal`, `datetime` | Show min–max / date |
| `space.svg` | Spatial extent / CRS | `bbox`, `proj:epsg` | Tooltip → EPSG/bounds |
| `process.svg` | Pipeline/transform info | `pipeline`, `processing_steps[]` | Click → pipeline trace |
| `qa.svg` | Validation / QA status | `qa.status`, checksums | Badge state (ok/warn) |
| `sensitive.svg` | Sensitive/restricted/redacted | `access.classification`, redaction flags | Lock + disable actions |
| `ai.svg` | AI-generated summary marker | `generated_by: ai`, focus mode | Always paired w/ `cite` |

---

## 🎨 Design rules (keep them consistent)

### ✅ Do
- Use **simple pictograms** that remain readable at **16–24px**.
- Prefer **shape-based** meaning (category cues), not color-only meaning.
- Use `currentColor` for `fill`/`stroke` so icons theme cleanly (dark/light).
- Add an accessible label via:
  - inline SVG: `<title>` + `<desc>`
  - component wrapper: `aria-label="..."`

### ❌ Don’t
- Don’t bake in hard-coded colors (no fixed black/white unless required).
- Don’t include text inside the icon (too small + localization headache).
- Don’t create multiple icons for the same concept (token drift = UX drift).

---

## 📐 SVG spec (recommended)

<details>
  <summary><b>Click to expand SVG specs</b> 📏</summary>

- **Format:** SVG (preferred)  
- **ViewBox:** `0 0 24 24` (preferred baseline)  
- **Strokes:** consistent thickness (e.g., 1.5–2px)  
- **Fills:** prefer `fill="none"` + `stroke="currentColor"` (or `fill="currentColor"` if glyph style)  
- **Alignment:** snap to pixel grid where possible for crisp rendering  
- **Weight:** keep visual weight consistent across the set  
- **Size budget:** keep icons lightweight (avoid massive paths)  

</details>

---

## 🧪 QA checklist (before committing)

- [ ] Looks good at **16px** and **24px** (no mushy details)
- [ ] Works in **light + dark** backgrounds
- [ ] Uses `currentColor` (or follows the app’s theming convention)
- [ ] Has an accessible label (`title/desc` or `aria-label`)
- [ ] Token is added/updated in the **icon registry** (wherever the UI maps meta fields → icons)
- [ ] If icon is third-party: **license + attribution recorded** (see below)

---

## 🧰 Usage patterns (React-friendly)

> These examples are intentionally generic — follow the project’s existing import pattern (SVGR, URL import, or Icon component wrapper).

### Option A: SVG as component (SVGR-style)
```tsx
import SourceIcon from "@/assets/icons/map/meta/source.svg";

export function LayerSourceBadge() {
  return (
    <span className="MetaBadge" aria-label="Source">
      <SourceIcon aria-hidden="true" />
      <span className="MetaBadge__label">Source</span>
    </span>
  );
}
```

### Option B: SVG as URL (img)
```tsx
import sourceUrl from "@/assets/icons/map/meta/source.svg";

export function LayerSourceBadge() {
  return <img src={sourceUrl} width={16} height={16} alt="Source" />;
}
```

---

## 🧾 Licensing & attribution

KFM is strict about **license clarity** — icons are part of the deliverable surface area.  
If any icon is sourced from an external library, add attribution in one of:

- `web/assets/icons/NOTICE.md` (preferred central record), or  
- `web/assets/icons/map/meta/NOTICE.md` (if you want it local)

Include: **origin**, **license**, **modifications**, **link to upstream**.

---

## 🔗 Related docs (recommended cross-links)

- 📦 Data contracts / metadata schemas (STAC / DCAT / PROV)
- 🧠 Focus Mode labeling + citation rules
- 🗺️ UI layer + provenance requirements (map overlays must cite sources)

> Tip: When you add a new meta token, update the docs that define the underlying field so the UI and data contracts stay aligned. 🔄✅