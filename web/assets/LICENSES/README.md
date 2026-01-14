# 📜 Third‑Party Licenses & Attributions (web/assets)

![Scope](https://img.shields.io/badge/scope-web%2Fassets-blue)
![Purpose](https://img.shields.io/badge/purpose-third--party%20notices-informational)
![Reminder](https://img.shields.io/badge/do%20not%20ship-proprietary%20books-critical)

This folder documents **what third‑party content** (PDFs, icons, datasets, etc.) may exist under `web/assets/` and what we must do to **redistribute it legally** (attribution, license text, UI credits, etc.).

> ⚠️ Not legal advice. This is an engineering checklist + attribution index.

---

## 🎯 What counts as “web/assets” here?

Anything that can be **served to browsers** (bundled or downloadable) — e.g. PDFs, images, icons, fonts, sample datasets, offline tiles, etc.

- ✅ If it’s **shipped** → it must be in this inventory
- 🚫 If it’s **not redistributable** → it must **not** be shipped, even if it exists in the repo

---

## 🧭 Legend

- ✅ **Shippable** (with required attribution/notice)
- ⚠️ **Conditional** (NonCommercial / NoDerivatives / ShareAlike — often incompatible with open redistribution)
- 🚫 **Do not ship** (proprietary / personal-use-only / unclear license)
- 🧩 **First‑party** (owned by this project; see root repo license)

---

## 🗂️ Expected folder layout

```text
📁 web/
  📁 assets/
    📁 LICENSES/
      📄 README.md  👈 you are here
      📄 CC-BY-4.0.txt
      📄 CC-BY-SA-4.0.txt
      📄 CC-BY-NC-4.0.txt
      📄 CC-BY-NC-ND-4.0.txt
      📄 ODbL-1.0.txt
      📄 THIRD_PARTY_NOTICES.optional.md
      📄 manifest.assets-licenses.json (optional)
```

> 💡 Keep the **full license texts** in this folder (or point to them in a stable way). The README is the index.

---

## 🗺️ Runtime attributions (must show in UI, not just in repo)

Some things require **on‑screen** attribution (e.g., map data). If we use these in the web UI, ensure there is a visible “Credits / Attribution” control:

- **OpenStreetMap data** → show: `© OpenStreetMap contributors` + link to OSM copyright page
- **Basemap styles/symbol sets** (if sourced from OSM Carto / map icon packs) → include required credit and/or license notice as applicable
- **3D globe imagery/terrain** → verify provider terms (some default services are not “free to redistribute”)

---

## 📚 Asset inventory (by license)

<details>
<summary><strong>✅ Open Access — Creative Commons Attribution 4.0 (CC BY 4.0)</strong> (8 files)</summary>

These are generally the safest to ship in an open project **if we keep attribution** and include the CC BY 4.0 license text.

- 📄 `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf` — edited by Jeffrey A. Cardille, Morgan A. Crowley, David Saah, Nicholas E. Clinton — **CC BY 4.0** ✅  
- 📄 `Data Spaces.pdf` — edited by Edward Curry, Simon Scerri, Tuomo Tuikka — **CC BY 4.0** ✅  
- 📄 `Database Performance at Scale.pdf` — Felipe Cardeneti Mendes, Piotr Sarna, Pavel Emelyanov, Cynthia Dunlop — **CC BY 4.0** ✅  
- 📄 `Generalized Topology Optimization for Structural Design.pdf` — Yi Min Xie — **CC BY 4.0** ✅  
- 📄 `Introduction to Digital Humanism.pdf` — edited by Hannes Werthner, Carlo Ghezzi, Jeff Kramer, Julian Nida‑Rümelin, Bashar Nuseibeh, Erich Prem, Allison Stanger — **CC BY 4.0** ✅  
- 📄 `On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf` — Thomas D. Grant, Damon J. Wischik — **CC BY 4.0** ✅  
- 📄 `Scalable Data Management for Future Hardware.pdf` — edited by Kai‑Uwe Sattler, Alfons Kemper, Thomas Neumann, Jens Teubner — **CC BY 4.0** ✅  
- 📄 `Spectral Geometry of Graphs.pdf` — Pavel Kurasov — **CC BY 4.0** ✅  

**Notes**
- Even in CC BY works, **some third‑party figures/images** can be excluded (check figure credit lines).
- Add `CC-BY-4.0.txt` to this folder.

</details>

---

<details>
<summary><strong>✅/⚠️ Creative Commons Attribution–ShareAlike (CC BY‑SA)</strong> (2 direct files + more inside compilations)</summary>

Ship only if we are comfortable with **ShareAlike** implications (derivatives must remain BY‑SA).

- 📄 `Regression analysis using Python - slides-linear-regression.pdf` — Eric Marsden — **CC BY‑SA** ✅  
- 📄 `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf` — GoalKicker — **Text: CC BY‑SA** ✅ / ⚠️ images may be separately copyrighted  

**Notes**
- Add `CC-BY-SA-4.0.txt` (or the version specified by the asset) to this folder.
- GoalKicker notes usually state: **text is CC BY‑SA**, but **images may not be**. Treat images/figures carefully.

</details>

---

<details>
<summary><strong>⚠️ Creative Commons Attribution–NonCommercial (CC BY‑NC 4.0)</strong> (1 file)</summary>

**NonCommercial** is frequently incompatible with open redistribution because downstream users may use the repo commercially.

- 📄 `Understanding Statistics & Experimental Design.pdf` — Michael H. Herzog, Gregory Francis, Aaron Clarke — **CC BY‑NC 4.0** ⚠️  

**Recommendation**
- Prefer linking to the official source instead of bundling in `web/assets/` for public releases.

</details>

---

<details>
<summary><strong>⚠️ Creative Commons Attribution–NonCommercial–NoDerivatives (CC BY‑NC‑ND 4.0)</strong> (2 files + content embedded in a compilation)</summary>

**NC‑ND** is the most restrictive CC flavor here: **no commercial use** and **no derivatives** (including edits/rewrites/repackaging).

- 📄 `Archaeological 3D GIS_26_01_12_17_53_09.pdf` — Nicolò Dell’Unto, Giacomo Landeschi — **CC BY‑NC‑ND 4.0** ⚠️  
- 📄 `Principles of Biological Autonomy - book_9780262381833.pdf` — Francisco J. Varela (annotated edition) — **CC BY‑NC‑ND 4.0** ⚠️  
  - includes an additional restriction notice about **not using content to train AI systems** without permission  

**Recommendation**
- Do not ship these in an open public build. Prefer “external link + attribution” unless the distribution is strictly non‑commercial and unchanged.

</details>

---

<details>
<summary><strong>🚫 Proprietary / All Rights Reserved / Permission Required</strong> (13 files + more embedded in compilations)</summary>

These should **not** be shipped in `web/assets/` (public). Keep them out of builds/releases.

- 📄 `Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf` — (O’Reilly) — 🚫  
- 📄 `Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf` — Justin Seitz — 🚫  
- 📄 `Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf` — 🚫  
- 📄 `compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf` — 🚫  
- 📄 `concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf` — © ISTE Ltd (Wiley/ISTE) — 🚫  
- 📄 `ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf` — 🚫  
- 📄 `graphical-data-analysis-with-r.pdf` — 🚫  
- 📄 `making-maps-a-visual-guide-to-map-design-for-gis.pdf` — 🚫  
- 📄 `python-geospatial-analysis-cookbook.pdf` — (Packt) — 🚫  
- 📄 `regression-analysis-with-python.pdf` — (Packt) — 🚫  
- 📄 `responsive-web-design-with-html5-and-css3.pdf` — (Packt) — 🚫  
- 📄 `think-bayes-bayesian-statistics-in-python.pdf` — Allen B. Downey — 🚫  
- 📄 `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf` — (Pearson/Addison‑Wesley) — 🚫  

**Hard rule**
- If any of the above are meant for “reference only”, they must live outside public web assets (or be excluded by build tooling).

</details>

---

<details>
<summary><strong>🚫 Mixed / Compilation PDFs (multiple works, multiple licenses)</strong> (9 files)</summary>

These “programming Books” PDFs appear to be **multi‑book bundles** containing a mixture of:
- CC BY‑SA text (GoalKicker notes)
- Open access excerpts
- and **proprietary books** (explicitly “All rights reserved” / “personal use only”)

**Do not ship these as‑is.** If we need any content from them:
1) split into individual documents  
2) verify each document’s license  
3) ship only what is redistributable  

Files:
- 📄 `A programming Books.pdf` — 🚫 mixed
- 📄 `B-C programming Books.pdf` — 🚫 mixed
- 📄 `D-E programming Books.pdf` — 🚫 mixed
- 📄 `F-H programming Books.pdf` — 🚫 mixed
- 📄 `I-L programming Books.pdf` — 🚫 mixed
- 📄 `M-N programming Books.pdf` — 🚫 mixed
- 📄 `O-R programming Books.pdf` — 🚫 mixed
- 📄 `S-T programming Books.pdf` — 🚫 mixed
- 📄 `U-X programming Books.pdf` — 🚫 mixed

</details>

---

<details>
<summary><strong>🧩 First‑party project docs (not third‑party)</strong> (2 files)</summary>

These are treated as **project‑owned** documentation (covered by the repo’s main license unless stated otherwise):

- 📄 `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf` 🧩  
- 📄 `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf` 🧩  

> If these docs embed third‑party figures/tables/quotes, add a note here (or create a sub‑entry) with the original source + license.

</details>

---

## 🧾 Attribution templates (copy/paste)

### CC BY 4.0 (recommended default)
```text
“{Title}” by {Author(s)/Editor(s)}. Source: {URL or publisher page}.
Licensed under CC BY 4.0. Changes: {none | describe}.
```

### CC BY-SA (ShareAlike)
```text
“{Title}” by {Author(s)}. Licensed under CC BY-SA {version}.
Changes: {none | describe}. If modified, the derivative must remain CC BY-SA.
```

### CC BY-NC (NonCommercial)
```text
“{Title}” by {Author(s)}. Licensed under CC BY-NC 4.0.
This asset must not be included in distributions intended for commercial use.
```

### CC BY-NC-ND (NonCommercial + NoDerivatives)
```text
“{Title}” by {Author(s)}. Licensed under CC BY-NC-ND 4.0.
No derivatives: do not edit/transform. NonCommercial only.
```

### OpenStreetMap (ODbL)
```text
Map data © OpenStreetMap contributors. Licensed under ODbL 1.0.
```

---

## ✅ Release checklist

Before any public release that serves `web/assets/`:

1. 🔎 Confirm **no 🚫 assets** are present in the deployed `web/assets/` output
2. 📄 Include required license texts in `web/assets/LICENSES/`
3. 🧾 Verify runtime attributions appear in the UI (maps/tiles/data providers)
4. 🧪 If any asset’s license is unclear → treat as 🚫 until verified

---

## 🛠️ Maintenance (how to update this file)

When adding or changing an asset:
- add it to the correct section above
- store the full license text in `web/assets/LICENSES/` (if not already present)
- add any runtime attribution requirements
- if it’s a multi‑work bundle → split it before shipping

---

❤️ Keep it boring, accurate, and complete.