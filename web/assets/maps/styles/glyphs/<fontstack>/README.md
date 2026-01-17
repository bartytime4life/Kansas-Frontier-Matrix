# 🧩 Map Glyphs (PBF) — `<fontstack>`

![Static Asset](https://img.shields.io/badge/type-static%20asset-informational)
![Format](https://img.shields.io/badge/format-glyphs%20%2F%20.pbf-blue)
![Maps](https://img.shields.io/badge/maps-MapLibre%20GL%20JS-success)

📍 **Path:** `web/assets/maps/styles/glyphs/<fontstack>/`  
🧠 **Used by:** the KFM MapLibre-based 2D map viewer in `web/` (see `web/viewers/` in the front-end structure). [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:1‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

> [!TIP]
> If you’re reading this inside a real folder, replace `<fontstack>` in examples with **this directory name**.

---

## 🎯 What this folder is

This directory contains **pre-generated glyph ranges** for a **single MapLibre/Mapbox-GL “font stack”**.  
Glyphs are served as binary **`.pbf`** files (protobuf) so the map renderer can draw **labels** (places, roads, legends, annotations) consistently and quickly.

KFM’s front-end is designed around a web-based map viewer and relies on static assets being served efficiently from `web/assets/` (alongside other UI assets/styles). [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🗺️ Why KFM keeps glyphs here

KFM is explicitly built to run on **open libraries** and **standard web tech**, without requiring proprietary mapping services. [oai_citation:3‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw)  
Self-hosting glyphs:

- ✅ avoids vendor lock-in for fonts
- ✅ improves offline / “clone-and-run” dev workflows
- ✅ makes deployments simpler (static file hosting / CDN-friendly)

The broader KFM philosophy is also **contract-first & provenance-first** — anything that shows up in the UI should be traceable back to known sources and processing steps. [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
Even though glyphs are “UI assets,” they still affect what users see, so we track **license + provenance** here too.

---

## 📦 What should exist in this folder

Expected layout (example):

```text
📁 web/assets/maps/styles/glyphs/
   └── 📁 <fontstack>/
       ├── 📄 README.md              👈 you are here
       ├── 📄 LICENSE.txt            (recommended)
       ├── 📄 SOURCE.json            (recommended provenance metadata)
       ├── 📄 0-255.pbf
       ├── 📄 256-511.pbf
       ├── 📄 512-767.pbf
       └── 📄 ... (more ranges)
```

> [!IMPORTANT]
> `.pbf` files are **generated artifacts**. Treat them as **opaque binaries** — do not hand-edit.

---

## 🏷️ Naming rules for `<fontstack>`

### 1) The folder name must match what the renderer requests
MapLibre requests glyphs using a URL template like:

```json
{
  "glyphs": "/assets/maps/styles/glyphs/{fontstack}/{range}.pbf"
}
```

- `{fontstack}` becomes the *requested font stack string*
- `{range}` becomes the glyph range file name (e.g., `0-255`)

### 2) Font stacks often come from `text-font`
Many styles define labels with `text-font` (an array of font names). The renderer combines that into a “font stack.”

Example:

```json
"text-font": ["Noto Sans Regular", "Arial Unicode MS Regular"]
```

Your runtime `{fontstack}` may look like (varies by implementation/encoding):

- `Noto Sans Regular,Arial Unicode MS Regular`  
  or
- `Noto Sans Regular%2CArial Unicode MS Regular` (URL encoded)

> [!TIP]
> **Best practice:** open DevTools → Network tab → filter `pbf` → copy the requested path, then ensure this folder name matches the **decoded** directory name your static server exposes.

---

## 🔍 Range file conventions

Glyph ranges are usually **chunks of 256 codepoints**:

- `0-255.pbf`
- `256-511.pbf`
- `512-767.pbf`
- …

If a user sees missing glyphs (⬜ tofu boxes), the network tab often shows a 404 for a specific range file. Fix is typically:

- wrong `<fontstack>` folder name
- missing range `.pbf`
- font stack changed in the style, but glyphs weren’t regenerated

---

## 🧾 Provenance + licensing (KFM rule, applied to UI assets)

KFM emphasizes careful licensing and clear attribution to avoid legal pitfalls and support collaboration. [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
For glyphs, track *both* the original fonts and the generated output.

### ✅ Recommended files to add (next to this README)

- `LICENSE.txt` — the font license (or a pointer to it)
- `SOURCE.json` — machine-readable provenance record

Example `SOURCE.json` template:

```json
{
  "fontstack": "<fontstack>",
  "fonts": [
    {
      "name": "Example Font Regular",
      "upstream_url": "https://…",
      "version": "…",
      "license": "…",
      "license_url": "https://…",
      "sha256": "…"
    }
  ],
  "generated": {
    "tool": "…",
    "tool_version": "…",
    "generated_at": "YYYY-MM-DD",
    "notes": "Any subsetting / character coverage notes"
  }
}
```

> [!NOTE]
> The core KFM principle is that anything visible in the UI should be traceable and reproducible (no “mystery layers/assets”). [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🛠️ Regenerating glyphs

This repo treats glyphs as **static assets** that can be served efficiently (and even cached via CDN, similar to how KFM plans to offload heavy/commonly-accessed map content). [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

When you change fonts in a style (or add a new font stack), regenerate glyphs.

### Practical guidance

- Prefer **font subsets** when possible to reduce size — if you only support certain languages/character sets, subsetting can substantially shrink outputs. [oai_citation:8‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-Heg28TVM2nReDYTQ7nPhAK)
- Keep the generated folder name aligned with the exact runtime `{fontstack}` string.

> [!TODO]
> Add a repo script (e.g., `tools/maps/glyphs/build.*`) to standardize generation and preserve `README.md` + provenance files.

---

## 🧯 Troubleshooting quick hits

### ✅ Labels don’t render / tofu boxes appear
- Check DevTools → Network:
  - 404 on `/glyphs/<fontstack>/<range>.pbf` = missing file or mismatched folder name
- Verify the style JSON `glyphs` property points to the correct local template path.

### ✅ Some languages render, others fail
- Your fonts may not include needed glyphs.
- Add a fallback font to `text-font` *and* generate glyphs for that combined stack.

### ✅ Works locally, fails in deployment
- Confirm your static server sets sensible headers for `.pbf`:
  - `Content-Type: application/x-protobuf` (common)
  - caching headers for performance

---

## 🔗 Related KFM areas

- `web/` front-end application (React + MapLibre) [oai_citation:9‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- `web/viewers/` map viewer logic (MapLibre GL JS integration) [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- `web/assets/` static assets (icons, images, etc.) [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

### ✅ Checklist (when adding/changing fonts)

- [ ] Style `glyphs` points to local template (`…/{fontstack}/{range}.pbf`)
- [ ] A matching `web/assets/maps/styles/glyphs/<fontstack>/` folder exists
- [ ] Range files exist for expected coverage
- [ ] `LICENSE.txt` and `SOURCE.json` are present (or tracked elsewhere)
- [ ] No proprietary font/service dependency was introduced [oai_citation:12‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw)
