# 🧾 LICENSES — Branding Source Assets (Third‑Party Notices)

![scope](https://img.shields.io/badge/scope-web%2Fassets%2Fmedia%2Fbranding%2Fsource-blue)
![audit](https://img.shields.io/badge/audit-provenance--first-success)
![format](https://img.shields.io/badge/format-MD-informational)

> 📌 **Scope:** Anything stored in or referenced by `web/assets/media/branding/source/` (source design files, reference PDFs, supporting media).  
> 🎯 **Goal:** Keep every non-original asset **traceable, attributable, and license-compliant**.

---

## 🗂️ Folder map

```text
📁 web/
└─ 📁 assets/
   └─ 📁 media/
      └─ 📁 branding/
         ├─ 📁 source/         🧩 editable sources + reference material
         │  └─ 📄 LICENSES.md  🧾 this file
         └─ 📁 dist/           🖼️ exported/optimized assets used by the app (optional)
```

---

## ✅ Rules of the road

- 🧷 **If it’s not original to KFM**, it must be listed here with a license and attribution.
- 🧾 Prefer **SPDX identifiers** when possible (examples below).
- 🧠 **Ideas/inspiration** are fine, but **copying** text/figures/images is governed by the upstream license.
- 🚫 **NC (Non‑Commercial)** content must not be used in commercial distributions.
- ⛔ **ND (No‑Derivatives)** content must not be remixed/modified or embedded into derivative assets (e.g., edited figures).
- 🛑 **All Rights Reserved / Proprietary** material must not be redistributed unless you have explicit permission.

> ⚖️ **Not legal advice.** This is a practical compliance log for the repo.

---

## 🏷️ License legend

| Label | SPDX-ish | What it means (super short) |
|------:|:---------|:-----------------------------|
| ✅ CC BY | `CC-BY-4.0` | Use/modify/share with attribution |
| 🟡 CC BY‑NC | `CC-BY-NC-4.0` | Attribution, **non‑commercial only** |
| 🟠 CC BY‑NC‑ND | `CC-BY-NC-ND-4.0` | Non‑commercial, **no derivatives** |
| ✅ CC BY‑SA | `CC-BY-SA-*` | Attribution + share‑alike (version varies) |
| 🚫 Proprietary | `LicenseRef-Proprietary` | All rights reserved |
| ⚠️ Mixed | `LicenseRef-Mixed` | Bundle containing multiple licenses |
| ❓ Unknown | `LicenseRef-Unknown` | License not found in-file (needs review) |

---

## 📚 Third‑party sources & reference media tracked by this project

### ✅ Open Access (Creative Commons Attribution)

These are generally the safest “research/reference PDFs” to keep around because reuse is broadly permitted **with attribution** (but still watch for third‑party images/figures inside the work).

| File (as stored) | Type | License | Notes |
|---|---|---|---|
| `Data Spaces.pdf` | PDF (chapter/book) | `CC-BY-4.0` | Open access; attribution required. |
| `Database Performance at Scale.pdf` | PDF (book) | `CC-BY-4.0` | Open access; attribution required. |
| `Scalable Data Management for Future Hardware.pdf` | PDF (chapter) | `CC-BY-4.0` | Open access; attribution required. |
| `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf` | PDF (chapter) | `CC-BY-4.0` | Open access; attribution required. |
| `Introduction to Digital Humanism.pdf` | PDF (chapter) | `CC-BY-4.0` | Open access; attribution required. |
| `On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf` | PDF (chapter) | `CC-BY-4.0` | Open access; attribution required. |
| `Spectral Geometry of Graphs.pdf` | PDF (book) | `CC-BY-4.0` | Open access; attribution required. |
| `Generalized Topology Optimization for Structural Design.pdf` | PDF (chapter) | `CC-BY-4.0` | Open access; attribution required. |

---

### 🟡 Open Access (Non‑Commercial)

| File (as stored) | Type | License | Notes |
|---|---|---|---|
| `Understanding Statistics & Experimental Design.pdf` | PDF (chapter) | `CC-BY-NC-4.0` | Open access; **non‑commercial only**. |

---

### 🟠 Open Access (Non‑Commercial, No‑Derivatives)

> ⚠️ **ND reminder:** Do **not** lift/modify figures, diagrams, or text into branding deliverables. Keep these as *read-only reference* unless you have separate permission.

| File (as stored) | Type | License | Notes |
|---|---|---|---|
| `Archaeological 3D GIS_26_01_12_17_53_09.pdf` | PDF (book) | `CC-BY-NC-ND-4.0` | OA version is CC BY‑NC‑ND 4.0. |
| `Principles of Biological Autonomy - book_9780262381833.pdf` | PDF (book) | `LicenseRef-CC-BY-NC-ND` | CC BY‑NC‑ND stated; **also includes a “no AI training” restriction** from the publisher. Treat as strict. |

---

### ✅ Creative Commons BY‑SA (GoalKicker / Stack Overflow Documentation)

| File (as stored) | Type | License | Notes |
|---|---|---|---|
| `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf` | PDF (book) | `CC-BY-SA-*` | Text released under CC BY‑SA; images may differ; see credits in the PDF. |

---

### 🚫 Proprietary / All Rights Reserved (Do not redistribute)

These are included only if you have the legal right to store/use them. They should **not** ship with public distributions unless permitted.

<details>
<summary>📦 Click to expand proprietary list</summary>

| File (as stored) | Type | License | Notes |
|---|---|---|---|
| `python-geospatial-analysis-cookbook.pdf` | PDF (book) | `LicenseRef-Proprietary` | Packt; all rights reserved. |
| `regression-analysis-with-python.pdf` | PDF (book) | `LicenseRef-Proprietary` | Packt; all rights reserved. |
| `responsive-web-design-with-html5-and-css3.pdf` | PDF (book) | `LicenseRef-Proprietary` | Packt; all rights reserved. |
| `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf` | PDF (book) | `LicenseRef-Proprietary` | Copyright notice + all rights reserved. |
| `making-maps-a-visual-guide-to-map-design-for-gis.pdf` | PDF (book) | `LicenseRef-Proprietary` | Publisher copyright; no reproduction without permission. |
| `Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf` | PDF (book) | `LicenseRef-Proprietary` | All rights reserved. |
| `compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf` | PDF (paper/booklet) | `LicenseRef-Proprietary` | ACM Press; all rights reserved. |
| `concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf` | PDF (book) | `LicenseRef-Proprietary` | ISTE/Wiley; copyright. |
| `graphical-data-analysis-with-r.pdf` | PDF (book) | `LicenseRef-Proprietary` | Springer; copyright. |
| `Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf` | PDF (book) | `LicenseRef-Proprietary` | No Starch Press; all rights reserved. |
| `ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf` | PDF (book) | `LicenseRef-Proprietary` | EC‑Council/Cengage; all rights reserved. |
| `think-bayes-bayesian-statistics-in-python.pdf` | PDF (book) | `LicenseRef-Proprietary` | O’Reilly; all rights reserved. |
| `Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf` | PDF (book) | `LicenseRef-Proprietary` | O’Reilly; all rights reserved. |

</details>

---

### ⚠️ Mixed-license bundles (alphabetized compilations)

These PDFs appear to be **multi-book compilations**. Treat them as **mixed-license containers**; each embedded book/section may have its own terms.

| File (as stored) | Type | License | Notes |
|---|---|---|---|
| `A programming Books.pdf` | PDF (bundle) | `LicenseRef-Mixed` | Contains multiple works; licenses vary per embedded book. |
| `B-C programming Books.pdf` | PDF (bundle) | `LicenseRef-Mixed` | Contains multiple works; licenses vary per embedded book. |
| `D-E programming Books.pdf` | PDF (bundle) | `LicenseRef-Mixed` | Contains multiple works; licenses vary per embedded book. |
| `F-H programming Books.pdf` | PDF (bundle) | `LicenseRef-Mixed` | Contains multiple works; licenses vary per embedded book. |
| `I-L programming Books.pdf` | PDF (bundle) | `LicenseRef-Mixed` | Contains multiple works; licenses vary per embedded book. |
| `M-N programming Books.pdf` | PDF (bundle) | `LicenseRef-Mixed` | Contains multiple works; licenses vary per embedded book. |
| `O-R programming Books.pdf` | PDF (bundle) | `LicenseRef-Mixed` | Contains multiple works; licenses vary per embedded book. |
| `S-T programming Books.pdf` | PDF (bundle) | `LicenseRef-Mixed` | Contains multiple works; licenses vary per embedded book. |
| `U-X programming Books.pdf` | PDF (bundle) | `LicenseRef-Mixed` | Contains multiple works; licenses vary per embedded book. |

---

### 🧩 Project-authored documents (covered by repo license unless stated otherwise)

| File (as stored) | Type | License | Notes |
|---|---|---|---|
| `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf` | PDF | Repo license | No explicit in-file license found; treat as project content. |
| `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf` | PDF | Repo license | No explicit in-file license found; treat as project content. |

---

## 🔁 How to update this file (checklist)

When you add a new file to `web/assets/media/branding/source/`:

- [ ] Add an entry to the correct table above
- [ ] Record **license**, **copyright holder**, and **source**
- [ ] If **CC**: include the exact variant (BY / BY‑SA / BY‑NC / BY‑NC‑ND)
- [ ] If **Proprietary**: confirm it will **not** ship publicly
- [ ] If **Fonts/Icons**: include upstream license file if provided (OFL/MIT/etc.)

---

## 🔗 Helpful license links

- CC BY 4.0: https://creativecommons.org/licenses/by/4.0/
- CC BY‑NC 4.0: https://creativecommons.org/licenses/by-nc/4.0/
- CC BY‑NC‑ND 4.0: https://creativecommons.org/licenses/by-nc-nd/4.0/
- CC BY‑SA 3.0: https://creativecommons.org/licenses/by-sa/3.0/
- SPDX License List: https://spdx.org/licenses/
