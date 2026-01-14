<!-- 📄 File: web/assets/icons/domain/README.md -->

# 🧭 Domain Icons

![format](https://img.shields.io/badge/format-SVG%20first-2ea44f)
![usage](https://img.shields.io/badge/usage-UI%20%2B%20Map%20Legend-blue)
![quality](https://img.shields.io/badge/quality-a11y%20%2B%20perf%20%2B%20provenance-orange)

> ✅ **Aligned with KFM Master Guide v13.0.0 (2025-12-28)** and the KFM “provenance-first, evidence-backed” design principles.  [oai_citation:0‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

This folder contains **domain-level icons** used across the KFM web experience (map UI, layer catalog, filters, story nodes, and legends). The goal is consistent, low-noise iconography that helps users *navigate domains* — not “prove” or “score” anything.  [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## ✨ What “domain” means here

In KFM, a **domain** is a knowledge/data area (e.g., historical archives, societal dimensions, environmental systems like water/air/hazards/ecology, agriculture, and key events/timeline).  [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

Domains overlap and connect (e.g., precipitation → runoff → floods → infrastructure impacts → migration), so icons must remain **simple, conventional, and non-distracting** — signposts, not cartoons.  [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🗂️ Folder layout

```text
web/
  assets/
    icons/
      domain/
        README.md   👈 you are here
        domain-*.svg
        domain-*.png            (optional fallback)
        icons.manifest.json     (recommended)
        sprite.domain.svg       (optional build artifact)
```

> The web app’s `/assets/` directory is expected to host things like images/icons and should remain **responsive + accessible**.  [oai_citation:6‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-Heg28TVM2nReDYTQ7nPhAK)

---

## 🧩 Canonical domain keys and filenames

### ✅ Naming convention
- **Prefix:** `domain-`
- **Case:** `kebab-case`
- **File type:** `*.svg` (primary), `*.png` (fallback only)
- **Examples:**  
  - `domain-historical.svg`  
  - `domain-water.svg`  
  - `domain-hazards.svg`

### 🎯 Recommended “baseline set”
These align to the domain sections described in the KFM documentation (and their common subdomains).  [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

| Domain key | Icon filename | UI label | Notes |
|---|---|---|---|
| `historical` | `domain-historical.svg` | Historical | Archives, maps, records |
| `societal` | `domain-societal.svg` | Society | People, communities, infrastructure |
| `water` | `domain-water.svg` | Water | Hydrology, aquifers, rivers |
| `air` | `domain-air.svg` | Air | Weather, wind, air quality |
| `hazards` | `domain-hazards.svg` | Hazards | Flood, drought, severe weather |
| `ecology` | `domain-ecology.svg` | Ecology | Land cover, habitat, biodiversity |
| `agriculture` | `domain-agriculture.svg` | Agriculture | Crops, soils, farming |
| `events` | `domain-events.svg` | Events | Timeline & key events |

<details>
<summary>🧠 Extended / optional domains (add when the product needs them)</summary>

These appear as dedicated capabilities or recurring layers in the KFM system (remote sensing, modeling/analytics, 3D GIS, etc.).  [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

- `remote-sensing` → `domain-remote-sensing.svg` 🛰️  
- `gis` → `domain-gis.svg` 🗺️  
- `modeling` → `domain-modeling.svg` 📈  
- `archaeology` → `domain-archaeology.svg` 🏺  
- `infrastructure` → `domain-infrastructure.svg` 🛤️  

</details>

---

## 🎨 Icon style guide

### 1) Be conventional, not cute 😄➡️😐
Map symbols work best when they’re **recognizable by convention** and don’t steal attention. Overly pictographic symbols can become “cute and distracting,” especially in serious contexts. 

### 2) Treat domain as **nominal data**
Domains are categories (nominal), so icons should communicate **difference in kind**, not magnitude. Prefer differences in **shape / pattern**, not size. 

### 3) Recommended geometry
- **Artboard:** 24×24 (or 32×32 if your UI standard is 32)
- **SVG viewBox:** `0 0 24 24` (or `0 0 32 32`)
- **Stroke:** consistent thickness across the set
- **Corners:** consistent radii (don’t mix “sharp” + “rounded” styles)
- **Avoid:** tiny gaps, hairlines, and micro-details that vanish at 16–20px

---

## 🧷 SVG rules (required)

### ✅ Use `viewBox` correctly
The `viewBox` defines the coordinate system and scaling behavior for SVGs.  [oai_citation:9‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)

### ✅ Prefer theming with `currentColor`
Icons should inherit color from CSS (so dark mode / theme switching works).

✅ Good:
```svg
<path fill="currentColor" d="..." />
```

🚫 Avoid:
```svg
<path fill="#00FF00" d="..." />
```

### ✅ Keep SVGs clean + build-friendly
Some authoring tools add extra namespaces/metadata; keep exports minimal and stable for diffs.  [oai_citation:10‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)

---

## ♿ Accessibility

### `title` / `desc` guidance
SVG supports `title` (tooltip + screen reader name) and `desc` (long description). Use them **when the icon is meaningful**, and skip them when the icon is purely decorative.  [oai_citation:11‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)

Recommended:
- Decorative icon: `aria-hidden="true"` and **no** redundant `title`
- Meaningful icon: `role="img"` with `aria-label="..."` (or an internal `<title>`)

---

## 🧪 Security notes (SVG is code-like!)

SVG can carry risky payloads (scripts, external refs, etc.). Treat icon assets as *inputs* and keep them sanitized — especially because web application attack surfaces include XSS, script injection, and parser-related issues.  [oai_citation:12‡S-T programming Books.pdf](file-service://file-NT32tqqzGW9RvfcNZmMH1K)

**Rules:**
- 🚫 No `<script>` tags
- 🚫 No external references (`href="http..."`, remote fonts, external entities)
- ✅ Prefer a safe subset: `<svg>`, `<path>`, `<circle>`, `<rect>`, `<g>`, `<defs>`, `<symbol>`
- ✅ Run an SVG sanitizer/optimizer as part of CI

---

## ⚡ Performance notes

KFM aims for a clean modular architecture and strong UX; icons should not become death-by-a-thousand-requests.  [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

Recommended strategies:
- **SVG sprite** for the baseline set (reduces requests)
- **HTTP caching** for standalone icons
- **Optimize** with SVGO (or equivalent) in build

---

## 🧰 Usage patterns

### Option A: SVG sprite (`<defs>` + `<use>`) ✅
SVG `<defs>` is designed to hold reusable content (gradients, symbols, etc.), and keeps the DOM tidy.  [oai_citation:14‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)

```html
<!-- 1) Hidden sprite -->
<svg aria-hidden="true" style="position:absolute;width:0;height:0;overflow:hidden">
  <defs>
    <symbol id="domain-water" viewBox="0 0 24 24">
      <path fill="currentColor" d="..." />
    </symbol>
  </defs>
</svg>

<!-- 2) Use it -->
<svg class="kfm-icon" role="img" aria-label="Water">
  <use href="#domain-water"></use>
</svg>
```

### Option B: Inline SVG
Inline SVG is often the simplest approach when you need styling/interaction.  [oai_citation:15‡O-R programming Books.pdf](file-service://file-M6zCNBGmJbot7A2aaUUy9M)

### Option C: External SVG via `<img>`
Using `<img src="...svg">` is great for caching, but you can’t reach into the SVG to style/animate it with CSS/JS (unlike inline/object).  [oai_citation:16‡O-R programming Books.pdf](file-service://file-M6zCNBGmJbot7A2aaUUy9M)

---

## 🧾 Provenance and governance

KFM treats **citations + metadata** as first-class, and insists that nothing becomes a black box. Icons should follow the same ethos: every icon should be traceable to intent, authoring, and license.  [oai_citation:17‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### Recommended: `icons.manifest.json`
Create/maintain a manifest so UI can map domain keys to icon files and track provenance.

```json
[
  {
    "key": "water",
    "label": "Water",
    "file": "domain-water.svg",
    "license": "CC0-1.0",
    "source": "KFM (original)",
    "tags": ["hydrology", "aquifer", "river"],
    "lastModified": "2026-01-14"
  }
]
```

> Treat this like a governed artifact: clear documentation + organization memory matter.  [oai_citation:18‡Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf](file-service://file-LuWF23hffNAZJaZm2Gzvcd)

---

## 🧭 Domain expansion workflow (when you add a new domain)

The Master Guide defines a “Domain Expansion Pattern” (new datasets, new layers, new UI hooks, etc.). New domain icons should follow the same workflow: add domain, add icon, connect mapping, update docs.  [oai_citation:19‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

Also, keep evidence artifacts consistent (e.g., if a domain icon appears on a story node, the node should still link back to evidence artifacts).  [oai_citation:20‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## ✅ Contribution checklist

- [ ] Add `domain-<key>.svg` (SVG-first)
- [ ] Confirm `viewBox` + grid alignment (24×24 or 32×32)
- [ ] Ensure `fill="currentColor"` (themeable)
- [ ] Ensure no scripts / external refs (sanitize!)
- [ ] Update `icons.manifest.json`
- [ ] If using sprites: update `sprite.domain.svg`
- [ ] Update the domain table in this README

---

## 🧠 Design rationale (why we’re strict)

- **Human-centered & agency-first:** iconography should empower understanding, not manipulate.  [oai_citation:21‡F-H programming Books.pdf](file-service://file-QofzooQDG9grJwh9nFN9SY)
- **Interoperable + governed systems:** KFM leans on strong standards and governance patterns; icons should be consistent and metadata-backed.  [oai_citation:22‡Data Spaces.pdf](file-service://file-7UnZyJ7eCK1egnsyuYJaFq) [oai_citation:23‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- **Avoid false conclusions:** correlation ≠ causation, and visuals can mislead — icons are navigation, not inference.  [oai_citation:24‡Understanding Statistics & Experimental Design.pdf](file-service://file-SdX6LMgi1uDRk5kd4H4Bg3)

---

## 📚 Project references used here

> These are included to keep the icon system grounded in the same “engineering + research” backbone as the rest of the repo.

- KFM Comprehensive Technical Documentation  [oai_citation:25‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- KFM Master Guide v13  [oai_citation:26‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- Responsive Web Design (SVG usage + a11y)  [oai_citation:27‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)  
- Making Maps (symbolization principles)  [oai_citation:28‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](file-service://file-51FgWTn7uFXenxztXw29bP)  
- HTML5 Notes (inline vs external SVG)  [oai_citation:29‡F-H programming Books.pdf](file-service://file-QofzooQDG9grJwh9nFN9SY)  
- Data Spaces (governance + interoperability framing)  [oai_citation:30‡Data Spaces.pdf](file-service://file-7UnZyJ7eCK1egnsyuYJaFq)  
- Digital Humanism (human agency framing)  [oai_citation:31‡Introduction to Digital Humanism.pdf](file-service://file-HC311tLjkcn1yRbyTBLJQQ)  
- NASA-grade modeling guide (governance/documentation mindset)  [oai_citation:32‡Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf](file-service://file-LuWF23hffNAZJaZm2Gzvcd)  
- Web app security testing (injection awareness)  [oai_citation:33‡S-T programming Books.pdf](file-service://file-NT32tqqzGW9RvfcNZmMH1K)  

<details>
<summary>📦 Extra project library (available, relevant for future icon work)</summary>

- WebGL Programming Guide  [oai_citation:34‡Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf](file-service://file-AkVmsLhdFzwie5Gco3zgYj)  
- Python Geospatial Analysis Cookbook  [oai_citation:35‡python-geospatial-analysis-cookbook.pdf](file-service://file-HT14njz1MhrTZCE7Pwm5Cu)  
- Cloud-Based Remote Sensing with Google Earth Engine  [oai_citation:36‡Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf](file-service://file-JVv3nbvtonX1HcpeERi9kV)  
- Archaeological 3D GIS  [oai_citation:37‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)  
- Database Performance at Scale  [oai_citation:38‡Database Performance at Scale.pdf](file-service://file-36z8qyiVJRtrSs6QG7Epen)  
- Regression Analysis with Python (full book)  [oai_citation:39‡Spectral Geometry of Graphs.pdf](file-service://file-DWxRbQDZGktGtiWtzAQxs8)  
- Graphical Data Analysis with R  [oai_citation:40‡Spectral Geometry of Graphs.pdf](file-service://file-DWxRbQDZGktGtiWtzAQxs8)  
- Think Bayes  [oai_citation:41‡think-bayes-bayesian-statistics-in-python.pdf](file-service://file-LXwJApPMVhRZgyqLb9eg7c)  
- Spectral Geometry of Graphs  [oai_citation:42‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)  
- Topology Optimization  [oai_citation:43‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)  
- Mobile Mapping  [oai_citation:44‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)  
- Compressed Image File Formats  [oai_citation:45‡concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf](file-service://file-Y45SvXbmLoZL1MNmrcyqz6)  
- Gray Hat Python  [oai_citation:46‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)  
- Ethical Hacking & Countermeasures  [oai_citation:47‡Regression analysis using Python - slides-linear-regression.pdf](file-service://file-Ekbky5FwpaPHfZC2ttv6xR)  
- AI Law foundations  [oai_citation:48‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)  

</details>

---

## 🔗 Legacy citation markers (keep for continuity)

-  [oai_citation:49‡Database Performance at Scale.pdf](file-service://file-36z8qyiVJRtrSs6QG7Epen)  
-  [oai_citation:50‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
-  [oai_citation:51‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)  
