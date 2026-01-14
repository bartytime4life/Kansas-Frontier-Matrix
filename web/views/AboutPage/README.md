# 🧭 AboutPage (KFM)

![View](https://img.shields.io/badge/view-AboutPage-2563eb) ![UX](https://img.shields.io/badge/ux-trust%20%26%20provenance-0ea5e9) ![Docs](https://img.shields.io/badge/docs-contract--first-7c3aed) ![AI](https://img.shields.io/badge/AI-advisory%20%2B%20cited-22c55e) ![A11y](https://img.shields.io/badge/a11y-keyboard%20%2B%20screenreaders-f97316) ![License](https://img.shields.io/badge/license-MIT%20(code)-000000)

> The **About page is KFM’s trust anchor**: mission, provenance, governance, licensing, and how to cite what you’re seeing.  
> If someone only visits one non-map page, it should be this one. ✅

---

## 📍 Where this lives

- 📁 **Path:** `web/views/AboutPage/`
- 🧭 **Route:** typically `/about` (exact route depends on your router)

### Suggested local layout (keep it boring + scalable)

```text
📁 web/
  📁 views/
    📁 AboutPage/
      📄 README.md   ← you are here ✅
      📄 AboutPage.tsx (or .jsx / .vue / etc.)
      📁 sections/
        📄 HeroSection.*
        📄 PillarsSection.*
        📄 HowItWorksSection.*
        📄 ProvenanceSection.*
        📄 FocusModeSection.*
        📄 LicensingSection.*
        📄 ContributeSection.*
        📄 ReferencesSection.*
      📁 content/
        📄 about.en.md
        📄 about.es.md (optional)
        📄 references.json
      📁 assets/
        🖼️ kfm-mark.svg
        🖼️ provenance-diagram.svg
```

> [!TIP]
> **Treat copy as data**: keep long-form copy in `content/` so it can be reviewed, versioned, localized, and validated—without rewriting UI code.

---

## 🎯 What AboutPage must accomplish

### The “jobs” of this page ✅

1. 🧠 **Explain what KFM is** (in plain language, no insider jargon).
2. 🔎 **Explain how to trust KFM**  
   - what provenance means  
   - how citations work  
   - why there are *no “mystery layers”*
3. 🧱 **Show how the system works** at a high level (sources → pipelines → catalog → UI/API).
4. 🤝 **Set expectations for Focus Mode (AI assistant)**  
   - what it can/can’t do  
   - how citations are shown  
   - how users verify claims
5. ⚖️ **Clarify licensing**  
   - code license  
   - data licensing varies by dataset  
   - how attribution is generated
6. 🛡️ **Communicate privacy + security posture** (high-level, user-facing).
7. 🌱 **Invite participation** (contribute data, stories, validation, code).

---

## 🧱 Page pillars (non‑negotiables)

> [!IMPORTANT]
> AboutPage content is **not marketing copy**. It’s a *governed explanation* of how the platform works and how to audit it.

### Pillar 1 — 🧾 Provenance-first
- Every layer, dataset, and narrative claim should point back to a **cataloged source**.
- The page should teach users to click through to **metadata / lineage**.

### Pillar 2 — 📑 Contract-first (data contracts)
- Datasets enter the system only when metadata requirements are satisfied (source, license, extent, processing steps, etc.).
- AboutPage should introduce this concept without over-explaining schemas.

### Pillar 3 — 🧑‍🤝‍🧑 Human-centered / Digital Humanism
- Be transparent about tradeoffs (automation vs. accountability, efficiency vs. trust).
- Explicitly describe how humans remain responsible for interpretation and use.

### Pillar 4 — 🌐 Open standards + interoperability
- Help users understand “Why open formats matter” (portability, reuse, citation).
- Mention that KFM is designed to integrate into larger ecosystems.

### Pillar 5 — ⚡ Performance + scalability (don’t brag—explain)
- Explain that heavy processing happens in pipelines/jobs, not in the browser.
- Keep this section factual and short.

### Pillar 6 — 🛡️ Security + privacy (user-facing, not exploit-facing)
- Communicate the principle: *protect users, protect data, protect infrastructure*.
- Avoid implementation details that could be abused.

---

## 🧩 UX + content blueprint (recommended sections)

<details>
<summary><strong>🗺️ Expand: Suggested section order + intent</strong></summary>

1. **Hero (what KFM is)**
   - 1–2 sentence purpose statement  
   - “Start exploring” buttons (Map / Catalog / Stories / Docs)

2. **Why KFM exists**
   - what problem it solves  
   - who it’s for (researchers, educators, public, decision-makers)

3. **How it works (system overview)**
   - sources → pipelines → catalog → API → UI  
   - one diagram, minimal text

4. **Provenance & transparency**
   - show how users verify data  
   - explain “map behind the map” concept  
   - link to dataset contracts / provenance viewer

5. **Focus Mode (AI assistant)**
   - advisory / summarized  
   - must cite sources  
   - how users check citations

6. **Data & licensing**
   - code license  
   - dataset licensing varies  
   - automatic attribution / credits

7. **Governance & contribution**
   - how to contribute data, stories, QA checks  
   - code of conduct / contribution guidelines

8. **Acknowledgements & references**
   - public references + internal design library (if appropriate)

</details>

---

## 🔁 “How it works” diagram (Mermaid)

```mermaid
flowchart LR
  S[(📚 Source archives<br/>agencies • libraries • remote sensing • community)]
  P[🧪 Pipelines / Jobs<br/>clean • georeference • validate • transform]
  C[(🗂️ Catalog + Contracts<br/>metadata • license • extent • provenance)]
  A[🧩 APIs<br/>REST/OpenAPI • GraphQL]
  U[🗺️ Web UI<br/>map • timeline • story nodes]
  F[🤖 Focus Mode (AI)<br/>advisory summaries + citations]

  S --> P --> C --> A --> U
  C --> F
  U --> F
```

> [!NOTE]
> Keep this diagram aligned with real architecture. If the architecture evolves, update this diagram first—then the rest of the page.

---

## 🧑‍💻 Implementation notes (for the view)

### 1) Keep AboutPage mostly static 🧊
- Prefer **build-time** or **static** content loading.
- Avoid calling heavy endpoints from AboutPage (no giant graph queries, no tile pulls, no full-catalog fetch).
- If you must query: fetch *small summaries* (counts, latest build hash, etc.) and cache aggressively.

### 2) Separate “content” from “layout” ✍️
- Put copy in `content/about.en.md` (or MDX if supported).
- Put structured info (links, references, footnotes, metrics) in `content/references.json`.
- The view should only:
  - render content
  - provide navigation
  - support accessibility + responsive layout

### 3) Progressive enhancement for visuals 🧩
If you embed:
- 🗺️ a mini map preview
- 🌎 a 3D globe
- 📈 interactive charts

…then:
- lazy-load it
- respect `prefers-reduced-motion`
- render a static fallback (image/diagram) first

---

## 🧾 Copy rules (provenance-first editing)

> [!IMPORTANT]
> **No significant claim without an evidence path.** If the About page says it, we should be able to prove it.

### ✅ Good patterns
- “KFM catalogs datasets with licenses, spatial/temporal extent, and processing steps.”
- “Focus Mode provides AI-generated summaries with citations and is clearly labeled as a synthesis.”

### 🚫 Avoid
- “World-class accuracy” / “guaranteed correctness”
- “All data is open” (often false—licenses vary)
- “AI is unbiased” (never claim this)

### Citation / evidence patterns (pick one and standardize)

**Option A — Footnotes**
- Add short footnotes to claims that warrant proof.

**Option B — Evidence blocks**
- Each section ends with a “🔎 Evidence” block listing dataset IDs, docs, or links.

**Option C — “Show sources” UI**
- In the UI, the About page surfaces a mini “Sources” drawer linking to public docs + dataset contracts.

---

## 🤖 Focus Mode (AI) messaging checklist

### User-facing truth statements ✅
- It’s **optional**
- It provides **summaries, not authority**
- It should **cite sources**
- Users can **click citations** to inspect underlying records

### UI/UX requirements ✅
- Distinct visual treatment (badge, icon, label like “AI summary”)
- “Show citations” affordance always visible
- Clear failure modes:
  - “No sources available”
  - “Out of scope”
  - “Insufficient evidence”

> [!CAUTION]
> Never present AI text in the same visual style as primary data, maps, or official records.

---

## ♿ Accessibility + responsive design

### Minimum a11y bar
- One `<h1>` on the page, logical heading order.
- Full keyboard navigation (tab order sane, no focus traps).
- Links are descriptive (“View dataset contract” vs “Click here”).
- Color is never the only signal (icons + labels).

### Responsive rules (mobile-first)
- Prefer a single-column layout under small breakpoints.
- Pillars become a vertical stack.
- Diagrams scale and remain readable (or collapse into `<details>`).

---

## 🖼️ Media + asset rules (AboutPage is a performance trap)

- Favor **SVG** for diagrams/marks when possible.
- Avoid huge background images.
- Compress raster images and set explicit dimensions to reduce layout shift.
- If you add photos:
  - JPEG for photos
  - PNG only when transparency is needed
  - Keep file size budgets tight

> [!TIP]
> If this page feels “slow”, users will (rightfully) doubt the credibility of everything else.

---

## 🔐 Security + privacy (high-level, safe to publish)

- Avoid describing internal defenses in detail.
- Stick to statements like:
  - “We minimize data collection.”
  - “We validate and review new datasets before they appear in the catalog.”
  - “We design for least privilege and safe defaults.”

---

## ✅ Definition of Done (DoD) for changes to AboutPage

- [ ] Copy reviewed for clarity (non-experts can understand it)
- [ ] Every major claim has an evidence path (doc, dataset ID, contract link, or provenance record)
- [ ] Focus Mode section clearly labels AI summaries + cites sources
- [ ] Lighthouse/A11y checks pass (or issues tracked)
- [ ] Page loads fast on mobile (no heavy map/3D until user opts in)
- [ ] Links validated (no broken internal routes)
- [ ] Licensing section reviewed (no blanket claims)

---

## 📚 Project library → how it informs this page

> [!WARNING]
> Some items in this library are **copyrighted**.  
> ✅ Use them as *internal references* (design + engineering guidance).  
> 🚫 Do not commit restricted PDFs to a public repo unless you have explicit redistribution rights.

### Recommended practice for references
- Store internal references outside the public repo, or behind authenticated storage.
- In public docs, cite **public URLs**, **DOIs**, or **dataset contracts** instead.

<details>
<summary><strong>📖 Expand: All project reference files + AboutPage role</strong></summary>

| Category | 📄 File (project reference) | ✅ AboutPage usage (what it informs) |
|---|---|---|
| 🧠 Core system | Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf | Canonical source for mission, architecture, provenance-first rules, Focus Mode behavior, UI concepts (timeline/story nodes). |
| 🧾 Doc governance | Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx | Evidence-first documentation patterns, front-matter governance ideas, “Definition of Done” for docs. |
| 🌐 Data ecosystems | Data Spaces.pdf | How KFM fits as a data ecosystem: interoperability, governance, federation mindset. |
| 🧑‍🤝‍🧑 Human-centered | Introduction to Digital Humanism.pdf | Framing for transparency, accountability, and trust; how to discuss automation responsibly. |
| ⚖️ AI + society | On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf | How to word AI disclaimers, accountability, and the “don’t overclaim” posture. |
| 🗺️ Cartography | making-maps-a-visual-guide-to-map-design-for-gis.pdf | How we explain legends, visual hierarchy, and map-reading literacy on AboutPage. |
| 📱 Cartography & culture | Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf | Context for mobile mapping and why UX + trust matters on small screens. |
| 🧭 3D / GIS | Archaeological 3D GIS_26_01_12_17_53_09.pdf | Guidance for describing 3D GIS + web visualization interoperability (without overselling). |
| 🧩 Web graphics | webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf | Progressive enhancement advice for any WebGL/3D preview embedded on AboutPage. |
| 📐 Web layout | responsive-web-design-with-html5-and-css3.pdf | Mobile-first layout, responsive patterns, and safe performance defaults. |
| 🖼️ Media perf | compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf | Image format decisions, compression rationale for AboutPage assets. |
| 🛰️ Remote sensing | Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf | How to describe remote sensing workflows, legends, time-series interaction (in plain language). |
| 🧭 Geospatial Python | python-geospatial-analysis-cookbook.pdf | Reference for geospatial processing concepts we summarize on AboutPage. |
| 🗃️ Database | PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf | Practical grounding for describing Postgres/PostGIS-style data stewardship (high-level). |
| ⚡ DB performance | Database Performance at Scale.pdf | Why AboutPage stays mostly static; performance principles and “don’t query everything.” |
| 🧱 Future data systems | Scalable Data Management for Future Hardware.pdf | Language for scalability without hype; background on modern query engines + analytics constraints. |
| 📊 Modeling | Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf | How we talk about modeling rigor, reproducibility, and simulation outputs responsibly. |
| 📐 Experimental design | Understanding Statistics & Experimental Design.pdf | How to communicate uncertainty, causal vs correlational claims, and “what the data supports.” |
| 📈 Regression | regression-analysis-with-python.pdf | Reference for regression explanations and examples shown elsewhere; informs “methods” wording. |
| 📉 Regression slides | Regression analysis using Python - slides-linear-regression.pdf | Quick visual framing for educational sections (if AboutPage links to tutorials). |
| 📊 EDA | graphical-data-analysis-with-r.pdf | Exploratory analysis mindset; supports “we visualize first, then model.” |
| 🎲 Bayesian | think-bayes-bayesian-statistics-in-python.pdf | Uncertainty + priors framing; supports “confidence / evidence” language. |
| 🤖 Deep learning | Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf | If AboutPage mentions ML features, keep it grounded and practical; avoids mystique. |
| 🧠 ML theory | Understanding Machine Learning: From Theory to Algorithms.pdf | Helps keep AI explanations precise; supports “constraints + assumptions” messaging. |
| 🧬 Systems thinking | Principles of Biological Autonomy - book_9780262381833.pdf | Language for complex systems, feedback loops, and why context matters in interpretation. |
| 🕸️ Graph theory | Spectral Geometry of Graphs.pdf | If referencing knowledge graphs/network analysis, keep terminology correct and non-misleading. |
| 🏗️ Optimization | Generalized Topology Optimization for Structural Design.pdf | Background if we mention optimization workflows; helps avoid sloppy claims. |
| 🔐 Security (defense) | ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf | Security awareness framing; informs high-level “safe defaults” language (no exploit detail). |
| 🔐 Security (defense) | Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf | Defensive awareness only; do not surface operational details on AboutPage. |
| 🧵 Concurrency | concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf | Helps explain why background jobs/pipelines exist; concurrency concepts inform architecture wording. |
| 📦 Language refs | A programming Books.pdf | Broad language reference library used by the project; influences dev ergonomics, not user copy. |
| 📦 Language refs | B-C programming Books.pdf | Broad language reference library. |
| 📦 Language refs | D-E programming Books.pdf | Broad language reference library. |
| 📦 Language refs | F-H programming Books.pdf | Broad language reference library. |
| 📦 Language refs | I-L programming Books.pdf | Broad language reference library. |
| 📦 Language refs | M-N programming Books.pdf | Broad language reference library. |
| 📦 Language refs | O-R programming Books.pdf | Broad language reference library. |
| 📦 Language refs | S-T programming Books.pdf | Broad language reference library. |
| 📦 Language refs | U-X programming Books.pdf | Broad language reference library. |

</details>

---

## 🧾 Changelog (optional but recommended)

| Date | Change | Notes |
|---|---|---|
| YYYY‑MM‑DD | Created AboutPage README | Initial blueprint + DoD + reference mapping |

---

### 🧠 Quick reminder (the AboutPage “north star”)

> **If a user is skeptical, this page should help them verify—not persuade.**  
> Trust comes from **traceability**, **clarity**, and **humility**. ✅
