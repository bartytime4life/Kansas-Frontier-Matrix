# ♿📊 Chart Alt-Text Exports (`web/assets/charts/exports/alt/`)

![Path](https://img.shields.io/badge/path-web%2Fassets%2Fcharts%2Fexports%2Falt-blue)
![Purpose](https://img.shields.io/badge/purpose-accessible%20chart%20exports-brightgreen)
![Conventions](https://img.shields.io/badge/conventions-provenance--first%20%2B%20contract--first-purple)

> [!IMPORTANT]
> KFM is **provenance-first**: anything that shows up in the UI should be traceable with citations/metadata — **no “black box” outputs**. Chart alt-text is part of that same trust + accessibility contract.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 📌 Overview

This directory stores **text alternatives** (short alt text + optional long descriptions) for **exported chart images** used by the KFM front-end.

- The KFM web app includes reusable UI components such as **charts** and is designed to be **responsive and accessible**.  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- KFM treats **metadata and lineage as fundamental**, with a **contract-first + provenance-first** rule: what appears in UI must be traceable, and “mystery layers”/unsourced outputs are not acceptable.  [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

Alt exports make sure every chart can be understood without sight (screen readers), **without relying on color**, and with clear pointers back to the dataset / method whenever applicable.  [oai_citation:3‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)

---

## 🗂️ Where this fits in the repo

```text
web/ 🌐
└─ assets/ 🧰
   └─ charts/ 📊
      └─ exports/ 📦
         ├─ (images: png/svg/webp/...) 🖼️
         └─ alt/ ♿  ← you are here ✅
            └─ README.md 📘
```

---

## 📦 What lives in this folder

This folder should contain **only accessibility artifacts** for exported charts.

### ✅ Recommended file types

| File | What it is | Used for |
|------|------------|----------|
| `*.alt.json` 🧾 | Machine-readable alt payload | UI consumption (tooltips, `aria-label`, `aria-describedby`) |
| `*.alt.md` 📝 | Human-readable long description | Focus panels / story narrative / deep accessibility text |
| `index.json` 🗺️ *(optional)* | Manifest of available alt exports | Fast lookups + build checks |

> [!NOTE]
> KFM documentation conventions emphasize **emoji-aided scanning**, admonitions, and citations. This README follows that style on purpose.  [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🧩 Naming conventions

### Rule of thumb: **same basename as the exported chart image**
If the exported chart image is:

- `exports/rainfall_station_0123__2020-2025.png`

Then the alt artifacts should be:

- `alt/rainfall_station_0123__2020-2025.alt.json`
- `alt/rainfall_station_0123__2020-2025.alt.md` *(optional but recommended for complex charts)*

This keeps the pipeline **deterministic** and makes it trivial to resolve `image → alt`.  [oai_citation:5‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### Allowed characters ✅
Use:
- `a-z`, `0-9`, `_`, `-`, `.`  
Avoid:
- spaces
- `#`, `?`, `&`
- mixed encodings

---

## 🧾 Alt export schema (recommended)

> [!TIP]
> KFM governance expects structured outputs to be **schema-validatable** where possible, and CI to catch broken links/references and malformed JSON. Treat `*.alt.json` as a first-class structured artifact.  [oai_citation:6‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### Minimal JSON shape (v0)
```jsonc
{
  "schema_version": "0.1.0",
  "chart_id": "rainfall_station_0123__2020-2025",
  "title": "Daily rainfall at Station 0123 (2020–2025)",

  // Keep this short: what you'd put into <img alt="...">
  "short_alt": "Line chart of daily rainfall (mm) from 2020–2025; peaks in May–June and lows in late summer.",

  // Optional, but strongly recommended for anything non-trivial:
  "long_desc_md": "## Summary\n...\n\n## Key takeaways\n- ...\n\n## Source\n- dataset_id: ...",

  "axes": {
    "x": { "label": "Date", "unit": null },
    "y": { "label": "Rainfall", "unit": "mm" }
  },

  "series": [
    { "name": "Rainfall", "role": "primary" }
  ],

  "provenance": {
    "dataset_id": "dcat:kfm:weather:stations:v1",
    "prov_ref": "prov:kfm:weather:rainfall_station_0123:daily:v1",
    "license": "SEE_DATASET_CONTRACT"
  },

  "updated_at": "2026-01-15"
}
```

### Field guidance 🧭
- `short_alt` must be understandable **without seeing the chart**.
- `long_desc_md` should contain:
  - **what the chart is**
  - **key takeaways**
  - **data caveats**
  - **source + provenance pointer**

KFM’s broader documentation practice is “**evidence-first**”: make claims traceable to sources and artifacts. Apply that here too.  [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## ✍️ Writing guidelines for chart alt text

Alt text for charts is tricky: too short becomes useless; too long becomes noise.

### ✅ Short alt (`short_alt`) should:
- Lead with **chart type + subject** (“Line chart of …”, “Bar chart comparing …”)
- Include **units** and **time range / geography** when relevant
- State the **main insight** (trend, peak, outlier)
- Avoid “*as you can see*” language
- Avoid relying on **color** (“the red line”) — use series names instead  [oai_citation:9‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)

### ✅ Long description (`long_desc_md`) should:
- Provide a structured explanation with headings (screen-reader friendly)  [oai_citation:10‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)
- Call out **notable values** (peak, min, sudden shifts) if known
- Mention **missing data**, smoothing, aggregation, or transformations
- Include a **Source / Evidence** section with dataset/provenance IDs

> [!WARNING]
> Don’t accidentally leak sensitive or identifying information in narrative descriptions. KFM governance practices include scanning for PII and sensitive content; treat alt descriptions like any other publishable output.  [oai_citation:11‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:12‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)

---

## ✅ Quality gates (Definition of Done for a new chart export)

When adding a new exported chart image, the alt artifacts are “done” when:

- [ ] `short_alt` exists and is not empty  
- [ ] Units + time range / region are included where applicable  
- [ ] No color-only references (“red/blue line”)  
- [ ] If complex: `long_desc_md` exists and has **Summary / Key Takeaways / Source**  
- [ ] Provenance pointer included (dataset id / prov ref / contract ref)  
- [ ] No PII / no sensitive coordinates / no restricted details (or properly generalized)  
- [ ] JSON is valid and (when available) passes schema checks  
- [ ] Any internal links referenced in `long_desc_md` are valid (no broken refs)  [oai_citation:13‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧪 Integration hint (UI usage pattern)

Example approach (conceptual):

- Use `short_alt` for `alt=""` / `aria-label`
- Use `long_desc_md` for `aria-describedby` or an “Explain this chart” panel

This matches KFM’s human-centered approach: assistive features should make the system more interpretable, not more opaque.  [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🔗 Related KFM docs (recommended reading)

- `docs/MASTER_GUIDE_v13.md` (contract-first + evidence-first workflow)  [oai_citation:15‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` (governed Markdown expectations)  [oai_citation:16‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- “Comprehensive Markdown Guide” (accessibility + alt text + inclusivity)  [oai_citation:17‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)

---

## 🧠 FAQ

<details>
  <summary><strong>Do we always need a <code>.alt.md</code> file?</strong></summary>

Not always. If the chart is simple and the **short alt** is sufficient, `*.alt.json` may be enough.  
If the chart communicates multiple takeaways, has multiple series, or needs caveats, add `*.alt.md`.
</details>

<details>
  <summary><strong>Can AI draft these?</strong></summary>

Yes — but treat AI output like a draft. KFM’s stance is that AI outputs should be **advisory and evidence-backed**, not autonomous or unsourced. Review + cite.  [oai_citation:18‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
</details>