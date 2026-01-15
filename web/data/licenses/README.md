# 📜 Licenses & Attribution Registry (Web Data)

![License](https://img.shields.io/badge/license-mixed-informational)
![Provenance](https://img.shields.io/badge/provenance-required-success)
![SPDX](https://img.shields.io/badge/SPDX-identifiers-blue)
![Status](https://img.shields.io/badge/status-enforced%20by%20review-orange)

This folder is the **single source of truth** for licensing + attribution of **non-code artifacts** used by the KFM web stack (datasets, map layers, images, PDFs, docs, exports, etc).

> [!IMPORTANT]
> ✅ **No asset ships in a public web build unless its license is recorded + compatible.**  
> ❌ If we can’t prove the license/provenance, we treat it as **Proprietary/Unverified** and keep it out of distribution.

---

## 🧭 Why this exists

KFM is **provenance-first**: no “mystery layers,” no unattributed assets, no unknown rights.  
This directory keeps the project honest by making license review **explicit**, **repeatable**, and **UI-ready**.

---

## 📁 Suggested folder layout

```text
web/
└─ 📦 data/
   └─ 🪪 licenses/
      ├─ ✅📄 README.md
      ├─ 🧾🗃️ registry.json              # 👈 recommended: machine-readable license manifest
      ├─ 📄 texts/                       # 📄 vendor canonical license texts (optional but helpful)
      │  ├─ 📜 MIT.txt
      │  ├─ 🧾 CC-BY-4.0.txt
      │  ├─ 🧾 CC-BY-SA-3.0.txt
      │  ├─ 🧾 CC-BY-SA-4.0.txt
      │  ├─ 🧾 CC-BY-NC-4.0.txt
      │  └─ 🧾 CC-BY-NC-ND-4.0.txt
      └─ 🧩 templates/
         ├─ 🧾✍️ ATTRIBUTION.template.md
         └─ 🧾🧬 DERIVATION.template.md
```

> [!TIP]
> Keeping canonical license texts locally avoids broken links and lets the UI show licenses offline.

---

## ✅ What every shippable dataset/asset must have

Minimum metadata (store in `registry.json` and/or alongside the asset):

- **id**: stable slug (no spaces)
- **title**: human name
- **source**: where it came from (URL or citation)
- **license**: SPDX-like identifier (e.g., `CC-BY-4.0`, `MIT`, `Proprietary`)
- **attribution**: the exact text we must show in the UI
- **redistribution**: `public | conditional | private`
- **derivatives**: `allowed | sharealike | no-derivatives | unknown`
- **ai_training**: `allowed | prohibited | unknown`

---

## 🧾 Registry format (recommended)

Create `web/data/licenses/registry.json` (or YAML if you prefer) so the frontend can render an “Attributions” drawer.

```json
{
  "version": 1,
  "assets": [
    {
      "id": "cloud-remote-sensing-gee",
      "title": "Cloud-Based Remote Sensing with Google Earth Engine (PDF)",
      "source": "Upstream publisher / DOI / canonical URL",
      "license": "CC-BY-4.0",
      "attribution": "Author(s). Title. Licensed CC BY 4.0.",
      "redistribution": "public",
      "derivatives": "allowed",
      "ai_training": "unknown",
      "notes": "Verify any third-party figures/illustrations have compatible terms."
    }
  ]
}
```

---

## 🖼️ UI attribution contract

If an asset appears in the web UI (map layer, sidebar image, chart export, downloadable bundle), the UI must show:

- **Title**
- **Creator/Publisher**
- **License**
- **Source link (if available)**
- **Any special constraints** (NC / ND / SA / AI-training restrictions)

> [!NOTE]
> “Attribution hidden in a README” doesn’t count if users interact with the asset in the UI.

---

## 🧩 License compatibility rules of thumb

- **Mixing licenses**: outputs inherit the **most restrictive** requirement in the chain (SA/NC/ND can “infect” bundles).  
- **CC BY-SA**: derivatives must remain **ShareAlike**.  
- **CC BY-NC**: **no commercial use** (treat public distribution as “conditional”).  
- **CC BY-NC-ND**: **no commercial use** + **no derivatives** (do not edit/transform the content).  
- **Proprietary / All rights reserved**: do not redistribute; keep out of public builds.
- **Unverified sources** (watermarks / mirror sites / missing rights page): treat as **not shippable** until replaced with a legally sourced copy.

---

## 📚 Current project library inventory (PDFs & bundles)

> [!WARNING]
> The files listed below are **project files currently present** (e.g., in `/mnt/data` during development).  
> This section is **not** permission to redistribute—use the “Redistribute?” column.

### ✅ Open / redistributable (with attribution)

| 📄 Asset | 🏷️ License | 🚚 Redistribute? | Notes |
|---|---:|:---:|---|
| `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf` | `CC-BY-4.0` | ✅ | Open license; still verify third‑party figures per publisher notes. |
| `Data Spaces.pdf` | `CC-BY-4.0` | ✅ | Open license; verify any third‑party material callouts. |
| `Database Performance at Scale.pdf` | `CC-BY-4.0` | ✅ | Open license; attribution required. |
| `Generalized Topology Optimization for Structural Design.pdf` | `CC-BY-4.0` | ✅ | Open license; chapter-level rights may apply. |
| `Introduction to Digital Humanism.pdf` | `CC-BY-4.0` | ✅ | Open license; attribution required. |
| `On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf` | `CC-BY-4.0` | ✅ | Open license; attribution required. |
| `Scalable Data Management for Future Hardware.pdf` | `CC-BY-4.0` | ✅ | Open license; chapter-level rights may apply. |
| `Spectral Geometry of Graphs.pdf` | `CC-BY-4.0` | ✅ | Open license; chapter-level rights may apply. |
| `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf` | `CC-BY-SA-*` | ✅ | Text is BY‑SA; images may be separately copyrighted. |
| `Regression analysis using Python - slides-linear-regression.pdf` | `CC-BY-SA-*` | ✅ | ShareAlike applies to derivatives; version not specified in file. |
| `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf` | `Project (see root)` | ✅ | Treat as project-authored unless stated otherwise. |

### ⚠️ Conditional (NonCommercial / NoDerivatives)

| 📄 Asset | 🏷️ License | 🚚 Redistribute? | Notes |
|---|---:|:---:|---|
| `Archaeological 3D GIS_26_01_12_17_53_09.pdf` | `CC-BY-NC-ND-4.0` | ⚠️ | NonCommercial + NoDerivatives. Don’t modify; confirm project distribution model. |
| `Understanding Statistics & Experimental Design.pdf` | `CC-BY-NC-4.0` | ⚠️ | NonCommercial. Treat public distribution as conditional. |
| `Principles of Biological Autonomy - book_9780262381833.pdf` | `CC-BY-NC-ND-4.0` | ⚠️ | NC+ND **and** contains an explicit AI-training restriction. |

### ❌ Proprietary / do not redistribute (reference-only)

| 📄 Asset | 🏷️ License | 🚚 Redistribute? | Notes |
|---|---:|:---:|---|
| `regression-analysis-with-python.pdf` | `Proprietary` | ❌ | Packt title (copyrighted). |
| `python-geospatial-analysis-cookbook.pdf` | `Proprietary` | ❌ | Packt title (copyrighted). |
| `responsive-web-design-with-html5-and-css3.pdf` | `Proprietary` | ❌ | Packt title; also shows mirror-site markers → replace with legally sourced copy. |
| `graphical-data-analysis-with-r.pdf` | `Proprietary` | ❌ | Taylor & Francis / CRC-style restrictions. |
| `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf` | `Proprietary` | ❌ | Copyrighted book. |
| `making-maps-a-visual-guide-to-map-design-for-gis.pdf` | `Proprietary` | ❌ | Guilford Press title (copyrighted). |
| `Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf` | `Proprietary` | ❌ | Copyrighted; not open licensed. |
| `think-bayes-bayesian-statistics-in-python.pdf` | `Proprietary` | ❌ | O’Reilly title (copyrighted). |
| `Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf` | `Proprietary` | ❌ | No Starch Press title (copyrighted). |
| `ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf` | `Proprietary` | ❌ | “All rights reserved” restrictions. |
| `concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf` | `Proprietary` | ❌ | ISTE/Wiley-style copyrighted content. |
| `compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf` | `Proprietary` | ❌ | ACM Press (copyrighted). |
| `A programming Books.pdf` | `Mixed/Unknown` | ❌ | Bundled/compiled; split + verify each embedded work before any redistribution. |
| `B-C programming Books.pdf` | `Mixed/Unknown` | ❌ | Bundled; contains proprietary content. |
| `D-E programming Books.pdf` | `Mixed/Unknown` | ❌ | Bundled; licenses vary. |
| `F-H programming Books.pdf` | `Mixed/Unknown` | ❌ | Bundled; licenses vary (some open chapters, some proprietary). |
| `I-L programming Books.pdf` | `Mixed/Unknown` | ❌ | Bundled; licenses vary. |
| `M-N programming Books.pdf` | `Mixed/Unknown` | ❌ | Bundled; licenses vary. |
| `O-R programming Books.pdf` | `Mixed/Unknown` | ❌ | Bundled; includes mirror-site markers → treat as unverified until cleaned. |
| `S-T programming Books.pdf` | `Mixed/Unknown` | ❌ | Bundled; licenses vary. |
| `U-X programming Books.pdf` | `Mixed/Unknown` | ❌ | Bundled; licenses vary. |
| `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf` | `TBD` | ⚠️ | Add an explicit license header + provenance; currently unclear. |
| `Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf` | `TBD` | ⚠️ | File not searchable here; verify license before shipping. |

---

## 🚨 Known “license risk” signals (cleanup checklist)

If you see any of these, do **not** ship the file until replaced with a legitimate source:

- Watermarks / mirror-site references (e.g., `wowebook.org`, `it-ebooks.info`, similar).
- “Personal use only” / “Not for distribution” clauses.
- No rights page + no clearly stated license.

✅ Action: replace with a legally obtained copy, or remove from distributed artifacts.

---

## 🧪 PR checklist (fast)

- [ ] Asset is listed in `registry.json` (or equivalent)
- [ ] SPDX-like license ID recorded
- [ ] Attribution text written and UI-ready
- [ ] Derivation documented if transformed
- [ ] License compatibility reviewed (NC/ND/SA flags)
- [ ] Any AI-training restriction captured explicitly
- [ ] No unverified-source markers present

---

## 🧷 Not legal advice

This is an engineering enforcement file, not legal counsel. When in doubt: **assume restrictive**, document provenance, and ask for a proper rights review.

🧱 _Provenance-first isn’t optional — it’s how KFM stays shippable._
