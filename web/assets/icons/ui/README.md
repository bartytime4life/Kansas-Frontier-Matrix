# 🎛️ UI Icons — `web/assets/icons/ui`

**Purpose:** a clean, consistent, accessible icon set for KFM’s web UI (buttons, menus, panels, layer controls, search, timeline controls, etc.).  
These icons are **UI chrome** (not map symbology). For map symbolization rules, see the “🗺️ Map vs UI iconography” section.

---

## ✅ Quick Specs

- **Primary format:** SVG (preferred)
- **Fallbacks:** PNG only when needed (e.g., complex raster or legacy compatibility)
- **Design intent:** crisp at small sizes; readable in dense map UIs
- **Accessibility:** icons must be label-safe (ARIA / text alternatives)
- **Provenance:** third‑party icons must be attributable + license-safe

> 🧭 KFM’s UI includes standard web-app elements like **layer list/catalog**, **search bar**, **legends**, and a **timeline slider**—these are exactly the surfaces these icons support.  
> **Why it matters:** the map UI gets crowded fast; icons are there to reduce friction without hiding meaning. [^kfm-ui-surfaces]

---

## 🧱 Folder Boundary: What belongs here

### ✅ Belongs in `web/assets/icons/ui/`
UI icons used for:
- navigation (menu, back, close)
- actions (add, remove, filter, download)
- map UI chrome (layers, legend, timeline, locate)
- system feedback (warning, info, success)
- Focus Mode / evidence panels helpers (sources, citations, explain, verify)

### ❌ Does **not** belong here
- **Map symbolization icons** used inside legends as **data-driven symbology** (those belong in a separate symbology set or style config)
- Large illustrations / hero graphics
- Raster tiles, textures, basemap art

---

## 🧭 Naming & Conventions

### File naming
Use **kebab-case** and keep names literal + stable:

- `ui-search.svg`
- `ui-layers.svg`
- `ui-timeline.svg`
- `ui-legend.svg`
- `ui-close.svg`
- `ui-info.svg`

**Rules**
- Prefer **nouns** for objects (`layers`, `legend`) and **verbs** for actions (`download`, `filter`)
- Avoid overloaded names (`settings` vs `preferences` — pick one and stick with it)
- Directional icons should include direction: `ui-chevron-left.svg`, `ui-arrow-up-right.svg`

### Recommended metadata sidecar (optional but strongly encouraged)
When icons come from external sources or need explicit attribution, add:

- `_meta/ui-icons.json` *(or)* `_meta/ui-icons.yml`

Suggested fields:
- `id`, `file`, `tags`, `meaning`
- `source`, `author`, `license`, `license_url`
- `modified_by`, `modified_reason`

> 🧾 Why? KFM’s governance model treats provenance as a first-class requirement—assets shouldn’t be “mystery meat.” [^prov-first]

---

## 🎨 Design Rules

### Size + grid
- Design on a **24×24** grid (default), ensure it still reads at **16×16**.
- Use a consistent optical weight across the set.
- Avoid micro-details that vanish below 20px.

### Stroke + fill
- Prefer **single-color** icons using `currentColor` so theming is automatic.
- Keep stroke widths consistent across the pack (e.g., 1.5–2px *conceptually*; choose one system and stick to it).

### Visual consistency
- Keep corners, angles, and terminal styles consistent.
- Don’t mix “rounded friendly” and “sharp technical” in the same category unless intentional.

---

## ♿ Accessibility Rules (Non‑Negotiable)

KFM’s UI aims to be **responsive and accessible**, with attention to ARIA roles and semantic markup. [^kfm-accessibility]

### When an icon is decorative
- Hide it from assistive tech:
  - `aria-hidden="true"`
  - or `role="presentation"`

### When an icon conveys meaning
- Provide an accessible name:
  - button text (preferred), or
  - `aria-label="Search"`, or
  - visually-hidden label (`.sr-only`) paired with the icon

### Color is never the only signal
If “red means danger,” add:
- shape difference,
- icon + text,
- or a status label.

---

## ⚡ Implementation Patterns

### Preferred: Inline SVG (best control)
Use inline when you need:
- easy theming (`currentColor`)
- hover/focus state styling
- precise accessibility handling

### Great for simple UI: CSS background-image + sprites
If icons are static and used widely, SVGs can be implemented as background images and bundled into sprites; tooling can generate style sheets and PNG fallbacks. This is cache-friendly and simple to implement. [^svg-background]

### Avoid
- embedding giant unoptimized SVGs in critical UI
- per-page icon duplication (prefer shared components or sprites)

---

## 🧩 Theming & State

### Use `currentColor`
- default icon inherits text color
- hover/focus/active states come “for free” with CSS

### Disabled state
- never rely only on opacity; ensure contrast + clarity remain acceptable
- disabled icons should still be recognizable (avoid “ghosting” to invisibility)

---

## 🗺️ Map vs UI iconography (important distinction)

KFM is map-first, so it’s easy to blur the line:

### UI icons (this folder)
They control the **interface**:
- toggle layers, open legend, change timeline, search, open details, launch Focus Mode

### Map symbols (not this folder)
They encode **data meaning** (points/lines/areas) and follow cartographic logic:
- A symbol is a *concept + mark*, linked by convention (e.g., airports shown with airplanes). [^map-symbols]
- Qualitative vs quantitative data implies different symbolization approaches (icons/pictographs for “kind,” value/size for “amount”). [^qual-quant]

> 🔎 Practical tip:  
> If it appears in a **button**, it’s likely a UI icon.  
> If it appears in a **legend explaining data**, it’s likely map symbology.

---

## 🧾 Provenance & Governance

### Core project principle
KFM is designed so user-facing narratives and features are **grounded in data and references**, inviting verification. [^focus-mode]

### What this means for icons
- Don’t introduce third‑party icon sets without:
  - verifying license compatibility,
  - recording attribution,
  - and keeping the provenance trail.

KFM’s standards emphasize:
- **Provenance first** (assets should be registered/traceable before being used widely) [^prov-first]
- **Evidence-first narrative** (UI surfaces that present “truth claims” should be linkable to sources) [^evidence-first]
- **Consistent standards** (UI consistency is a quality gate, not a nice-to-have) [^consistent-standards]

---

## ➕ Adding a New Icon

### ✅ Definition of Done (DoD)
- [ ] Name matches convention (`ui-*.svg`)
- [ ] Exports cleanly with correct `viewBox`
- [ ] Looks good at **16/20/24px**
- [ ] Uses `currentColor` (unless a strong reason not to)
- [ ] Decorative vs meaningful accessibility handled
- [ ] Optimized SVG (remove editor metadata, unnecessary groups)
- [ ] Attribution captured (if external source)
- [ ] No duplicate/near-duplicate icon already exists
- [ ] PR includes screenshot in light + dark UI

### Suggested workflow
1. Design on the grid (24px)
2. Export SVG
3. Optimize (SVGO or equivalent)
4. Drop into `web/assets/icons/ui/`
5. Update `_meta/ui-icons.*` if applicable
6. Add or update usage in UI components

---

## 🧰 Common Icon Set (suggested baseline)

| Icon | Typical Use | Notes |
|------|-------------|------|
| `ui-layers` | open layer catalog | map UI chrome |
| `ui-legend` | show legend panel | map readability |
| `ui-timeline` | open time controls | temporal navigation |
| `ui-search` | open search | place + dataset search |
| `ui-info` | open details/help | avoid “mystery UI” |
| `ui-close` | dismiss panels | ensure big hit target |
| `ui-filter` | refine results | pairs with faceted search |
| `ui-download` | export data/screenshot | provenance-friendly exports |
| `ui-warning` | caution states | pair with text |

---

## 🧠 Reference Shelf (Project Files) 📚

<details>
<summary><strong>Click to expand the full project reference library used to shape these guidelines</strong> 📖</summary>

### KFM architecture & governance
- 📘 *Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf*
- 🧭 *MARKDOWN_GUIDE_v13.md.gdoc*
- 📝 *Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx*
- 🗺️ *Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf*

### UI/Web fundamentals
- 🌐 *responsive-web-design-with-html5-and-css3.pdf*
- 🧩 *webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf*

### Cartography & map communication
- 🗺️ *making-maps-a-visual-guide-to-map-design-for-gis.pdf*
- 📍 *Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf*
- 🏺 *Archaeological 3D GIS_26_01_12_17_53_09.pdf*

### Image & asset formats
- 🖼️ *compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf*

### Data, performance, and systems (for UI scalability mindset)
- ⚙️ *Scalable Data Management for Future Hardware.pdf*
- 🧠 *Data Spaces.pdf*
- 🧮 *Database Performance at Scale.pdf*
- 🐘 *PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf*
- 🛰️ *Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf*
- 🌍 *python-geospatial-analysis-cookbook.pdf*

### Statistics & modeling (for evidence/uncertainty UI thinking)
- 📈 *Understanding Statistics & Experimental Design.pdf*
- 📉 *regression-analysis-with-python.pdf*
- 📊 *Regression analysis using Python - slides-linear-regression.pdf*
- 📦 *graphical-data-analysis-with-r.pdf*
- 🎲 *think-bayes-bayesian-statistics-in-python.pdf*
- 🧪 *Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf*
- 🧱 *Generalized Topology Optimization for Structural Design.pdf*
- 🧠 *Spectral Geometry of Graphs.pdf*
- 🧬 *Principles of Biological Autonomy - book_9780262381833.pdf*

### Security & robust engineering posture
- 🛡️ *ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf*
- 🧰 *Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf*
- ☕ *concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf*

### Ethics, human factors, and trust
- 🧑‍⚖️ *On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf*
- 🤝 *Introduction to Digital Humanism.pdf*

### Programming compendiums
- 📚 *A programming Books.pdf*
- 📚 *B-C programming Books.pdf*
- 📚 *D-E programming Books.pdf*
- 📚 *F-H programming Books.pdf*
- 📚 *I-L programming Books.pdf*
- 📚 *M-N programming Books.pdf*
- 📚 *O-R programming Books.pdf*
- 📚 *S-T programming Books.pdf*
- 📚 *U-X programming Books.pdf*

> Note: *Deep Learning for Coders with fastai and PyTorch* exists in the project archive but may not be indexed in all tooling contexts.

</details>

---

## 🔗 Source Notes (Footnotes)

[^kfm-ui-surfaces]: KFM UI surfaces and asset structure are described in the KFM technical documentation.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
[^kfm-accessibility]: Accessibility + ARIA/semantic markup are explicitly called out as likely UI provisions in KFM’s documentation.  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
[^focus-mode]: Focus Mode’s “grounded in data (with references)” framing and transparency ethos.  [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
[^prov-first]: “Provenance first” is a stated invariant: published assets/data should be registered with provenance before broader use.  [oai_citation:3‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
[^evidence-first]: “Evidence-first narrative” invariant: claims should be sourced; AI text should be identified and accompanied by provenance/confidence metadata.  [oai_citation:4‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
[^svg-background]: SVG implementation advice for icons (background images, sprite tooling, PNG fallbacks, caching).  [oai_citation:5‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)
[^map-symbols]: Map symbols as concept + graphic mark tied by convention/code (cartographic symbol thinking).  [oai_citation:6‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](file-service://file-51FgWTn7uFXenxztXw29bP)
[^qual-quant]: Qualitative vs quantitative differences and symbolization approaches (icons/pictographs vs value-based encodings).  [oai_citation:7‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](file-service://file-51FgWTn7uFXenxztXw29bP)
[^consistent-standards]: Flexible software design guidance emphasizing defined/enforced consistent technical & UI standards.  [oai_citation:8‡F-H programming Books.pdf](file-service://file-QofzooQDG9grJwh9nFN9SY)

---
