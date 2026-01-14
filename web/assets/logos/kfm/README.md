---
title: "KFM Logo Assets"
version: "v1.0.0"
status: "active"
doc_kind: "Asset Readme"
last_updated: "2026-01-14"
doc_uuid: "urn:kfm:doc:web-assets:logos:kfm:readme:v1.0.0"
---

# 🧭 KFM Logo Assets (`web/assets/logos/kfm/`)

![Scope](https://img.shields.io/badge/scope-web%2Fassets%2Flogos-blue)
![Brand](https://img.shields.io/badge/brand-KFM-black)
![Format](https://img.shields.io/badge/prefer-SVG-success)
![Governance](https://img.shields.io/badge/provenance-first-important)

KFM is a **living atlas**—and the logo system should reinforce the same values the platform is built on: **clarity, trust, and traceability**. KFM’s mission emphasizes provenance-first transparency (“no black box”), and the UI is designed to surface sources and metadata to users. That same mindset applies to brand assets: every logo variant should be **intentional, auditable, and consistently named**.[^kfm-mission]

---

## 📌 Quick Rules

✅ Do
- Use **SVG** for UI wherever possible (crisp at any scale).
- Use **approved variants** (light/dark/mono) rather than recoloring.
- Add/maintain **sidecar metadata** for every exported asset (see `meta/` contract below).[^kfm-doc-governance]
- Keep filenames **stable** (treat names like identifiers, not descriptions).[^stable-identifiers]

🚫 Don’t
- Don’t stretch, skew, or add effects (shadows, strokes, glows).
- Don’t place the logo on noisy basemaps without a contrast-safe backing.
- Don’t rename core logo files without providing a compatibility alias (or updating the manifest).

---

## 🗂️ Folder Contract

This folder is the **single source of truth** for KFM logos consumed by the web UI (React/TypeScript). The web app is designed to be responsive and map-centric, so logo variants must work across desktop + mobile + map/3D contexts.[^kfm-web-arch]

Recommended structure (adapt to what’s actually present in the repo):

```text
web/
└─ assets/
   └─ logos/
      └─ kfm/
         ├─ README.md
         ├─ manifest.json
         ├─ kfm-mark.svg
         ├─ kfm-mark-dark.svg
         ├─ kfm-icon.svg
         ├─ kfm-icon-mono.svg
         ├─ raster/
         │  ├─ kfm-icon-16.png
         │  ├─ kfm-icon-32.png
         │  ├─ kfm-icon-180.png
         │  └─ kfm-og-1200x630.png
         └─ meta/
            ├─ kfm-mark.meta.json
            ├─ kfm-icon.meta.json
            └─ kfm-og.meta.json
```

> 💡 Why `manifest.json`? Because UI code should request assets by **stable logical keys**, not “whatever file happens to exist.” This mirrors KFM’s broader philosophy of making assets discoverable and governed.[^kfm-doc-library]

---

## 🧱 Naming Convention

We treat filenames as **stable identifiers**—meaning names should be:
- **unique**
- **stable**
- ideally **information-free** (don’t encode shifting info like “final_v7_revised2”)  
This aligns with the general engineering guidance around stable identifiers in long-lived systems.[^stable-identifiers]

### Pattern

`kfm-{kind}[-{variant}][-{size}].{ext}`

**Kinds**
- `icon` → square mark (favicons, app icons, map markers)
- `mark` → primary logo mark
- `wordmark` → word-only lockup (if used)
- `seal` → formal/emblem variant (if used)
- `og` → social sharing images

**Variants**
- `color` (optional default)
- `mono`
- `dark` (for dark backgrounds)
- `light` (for light backgrounds)
- `outline` (if required for map overlays)

**Sizes** (raster only)
- `16`, `32`, `48`, `64`, `180`, `192`, `512`, `1200x630`, etc.

---

## 🧾 Metadata Sidecars (`meta/*.meta.json`)

KFM treats **citations and metadata as first-class** in the platform.[^kfm-mission]  
For logo assets, we do the same: every exported logo gets a small **sidecar metadata file**.

Example `meta/kfm-mark.meta.json`:

```json
{
  "id": "urn:kfm:asset:logo:kfm:mark:v1",
  "kind": "mark",
  "variant": "color",
  "source_file": "design/kfm-logo-source.ai",
  "exported_files": [
    "kfm-mark.svg",
    "raster/kfm-mark-512.png"
  ],
  "license": "SEE_ROOT_LICENSE",
  "created_by": "KFM Contributors",
  "created_at": "2026-01-14",
  "notes": "Primary mark used in header + app shell."
}
```

If the logo is derived from a third-party source or font, record that explicitly—**the goal is “the map behind the map,” but for visual assets**.[^kfm-provenance-ui]

---

## 🎨 Variants & When to Use Them

| Variant | Use it when… | Avoid when… |
|---|---|---|
| `kfm-mark.svg` | Default app shell, docs headers, splash | Background is dark or photo-heavy |
| `kfm-mark-dark.svg` | Dark mode header, overlays on dark maps | Background is light |
| `kfm-icon.svg` | Favicons, map markers, compact UI | Needs a full wordmark for clarity |
| `kfm-icon-mono.svg` | Embedding inside charts/legends, print-like UI | Brand recognition relies on color |

> 🗺️ Map context matters: KFM’s UI is map-first (2D/3D). Always validate the logo against typical basemaps and overlays.[^kfm-web-arch]

---

## 📐 Export Specs

### SVG (preferred)
- Convert text to outlines (unless you intentionally want editable text).
- Remove editor metadata (Sketch/Figma/Illustrator cruft) during export.
- Ensure the `viewBox` is correct and the logo is centered.

### PNG/Web raster
Use when:
- Browser icons / OS icons
- Social cards (OG images)
- Email signatures (some clients)

Recommended raster set:
- `16`, `32`, `48` (favicons + tiny UI)
- `180` (Apple touch)
- `192`, `512` (PWA icons)
- `1200x630` (Open Graph)

---

## 🧩 How to Use in the Web App

KFM’s web UI is a React SPA and includes an `assets/` folder for static images.[^kfm-web-arch]

### React (simple `<img>` approach)

```tsx
export function KfmLogo() {
  return (
    <img
      src="/assets/logos/kfm/kfm-mark.svg"
      alt="Kansas Frontier Matrix"
      height={28}
    />
  );
}
```

### Decorative usage (accessibility-safe)

```tsx
<img src="/assets/logos/kfm/kfm-icon.svg" alt="" aria-hidden="true" />
```

### Map markers
If you use the icon as a marker in a map engine, prefer the `icon` variant and test at multiple zooms. (A common pattern in geospatial web examples includes keeping both original and optimized logo PNGs side-by-side for specific UI contexts.)[^logo-optimized-example]

---

## 🌐 Favicons & App Icons

Example HTML pattern for favicons:[^favicon]

```html
<link rel="icon" type="image/png" href="/assets/logos/kfm/raster/kfm-icon-32.png">
<link rel="shortcut icon" type="image/x-icon" href="/favicon.ico">
```

⚠️ Note: browsers can be stubborn about favicon caching—plan for cache-busting if you update it.[^favicon]

---

## ✅ Contribution Checklist (PR “Definition of Done”)

When adding/updating any file in this folder:

1. **Add/Update the source** (vector master) in the appropriate design source location (repo-dependent).
2. Export **SVG** + required **raster sizes**
3. Optimize outputs (SVGO / PNG optimizer / WebP where appropriate)
4. Add/update `meta/*.meta.json`
5. Update `manifest.json`
6. Validate:
   - Light mode + dark mode
   - On a map background (2D) + (if relevant) 3D/globe UI
   - At smallest supported size (16–24px)
7. Add a screenshot (optional but helpful) to the PR description

> 🧪 Reproducibility is a project theme: KFM design docs emphasize versioning, CI checks, and regenerating outputs from documented steps—apply the same mindset here.[^kfm-dvc-ci]

---

## 🧠 Brand Principle: Semantic Consistency Across Platforms

Digital cartographic systems benefit from branding that is **uniquely identifiable** and semantically consistent across platforms—logos become part of how users recognize the same entity in many contexts (web, mobile, map layers, stories).[^branding-unique]

---

## 📚 Project Reference Shelf

<details>
<summary><strong>📦 Full project library (design + engineering context)</strong> <em>(click to expand)</em></summary>

These files inform KFM’s interdisciplinary identity and implementation constraints. The logo system should remain consistent across all these domains.

### 🌍 GIS / Cartography / Remote Sensing
- `making-maps-a-visual-guide-to-map-design-for-gis.pdf`
- `Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf`
- `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf`
- `python-geospatial-analysis-cookbook.pdf`
- `Archaeological 3D GIS_26_01_12_17_53_09.pdf`

### 🌐 Web / UI / 3D Visualization
- `responsive-web-design-with-html5-and-css3.pdf`
- `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf`

### 🧱 Architecture / Data / Scale
- `Scalable Data Management for Future Hardware.pdf`
- `Database Performance at Scale.pdf`
- `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf`
- `Data Spaces.pdf`

### 📊 Data Science / Stats
- `regression-analysis-with-python.pdf`
- `Regression analysis using Python - slides-linear-regression.pdf`
- `Understanding Statistics & Experimental Design.pdf`
- `graphical-data-analysis-with-r.pdf`
- `think-bayes-bayesian-statistics-in-python.pdf`

### 🧠 Modeling / Simulation / Optimization
- `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf`
- `Generalized Topology Optimization for Structural Design.pdf`
- `Spectral Geometry of Graphs.pdf`
- `Principles of Biological Autonomy - book_9780262381833.pdf`

### ⚖️ Ethics / Society / Policy
- `Introduction to Digital Humanism.pdf`
- `On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf`

### 🔐 Security (for the broader platform)
- `ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf`
- `Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf`

### 📚 Programming Notes Compendiums
- `A programming Books.pdf`
- `B-C programming Books.pdf`
- `D-E programming Books.pdf`
- `F-H programming Books.pdf`
- `I-L programming Books.pdf`
- `M-N programming Books.pdf`
- `O-R programming Books.pdf`
- `S-T programming Books.pdf`
- `U-X programming Books.pdf`

### 🧭 Core KFM Docs
- `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf`
- `Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf`
- `Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx`

</details>

---

## 🔎 Sources (for governance + provenance)

[^kfm-mission]: KFM mission + provenance-first principles + transparency goals.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
[^kfm-web-arch]: Web UI context: React (TypeScript), `web/` structure, MapLibre GL JS + CesiumJS, responsive UI goals.  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
[^kfm-provenance-ui]: “Map behind the map” UI philosophy: surface layer sources/metadata.  [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
[^kfm-doc-governance]: Governed Markdown practices: YAML front-matter + evidence-first documentation.  [oai_citation:4‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)
[^kfm-doc-library]: Repo documentation suggests indexing references with a `docs/library/MANIFEST.yml`.  [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
[^kfm-dvc-ci]: Design doc notes DVC for large artifacts + CI for validation + reproducible regeneration workflow.  [oai_citation:6‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-ShqHKgjxCS9UT9vbcxDNzA)
[^stable-identifiers]: Engineering guidance on stable identifiers (information-free, invariant, unique).  [oai_citation:7‡F-H programming Books.pdf](file-service://file-QofzooQDG9grJwh9nFN9SY)
[^favicon]: Favicon linking patterns + caching caveat.  [oai_citation:8‡F-H programming Books.pdf](file-service://file-QofzooQDG9grJwh9nFN9SY)
[^branding-unique]: Branding supports uniqueness/identifiability and semantic consistency across interoperable mapping systems.  [oai_citation:9‡Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf](file-service://file-AkVmsLhdFzwie5Gco3zgYj)
[^logo-optimized-example]: Example geospatial web project folder structure includes `logo-32x32-optimized.png` alongside originals.  [oai_citation:10‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)

<!-- Tooling file links (keep for traceability):
 [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  [oai_citation:12‡Archaeological 3D GIS_26_01_12_17_53_09.pdf](file-service://file-6DRx5ELzDPBso9Y5Qcbqm2)
 [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  [oai_citation:14‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)  [oai_citation:15‡Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf](file-service://file-AkVmsLhdFzwie5Gco3zgYj)
 [oai_citation:16‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-ShqHKgjxCS9UT9vbcxDNzA)  [oai_citation:17‡F-H programming Books.pdf](file-service://file-QofzooQDG9grJwh9nFN9SY)  [oai_citation:18‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)
-->
