---
title: "Kansas Frontier Matrix (KFM) — CHANGELOG"
doc_type: "changelog"
status: "living"
version: "v1.0.0-draft+1"
last_updated: "2026-01-11"
governance:
  fair_care: true
  care: true
  sovereignty: "TBD"
notes:
  - "This file is human-readable and not a replacement for Git history."
---

# 🧾 CHANGELOG

[![Changelog](https://img.shields.io/badge/CHANGELOG-KFM-2ea44f?style=flat-square)](#-changelog)
[![Keep a Changelog](https://img.shields.io/badge/keepachangelog-1.1-blue?style=flat-square)](https://keepachangelog.com/en/1.1.0/)
[![SemVer](https://img.shields.io/badge/semver-2.0-orange?style=flat-square)](https://semver.org/)

> [!IMPORTANT]
> **Scope note:** This changelog is seeded from the **project documentation bundle** (Master Guide v12/v13 drafts, Markdown guide, architecture/governance docs, and the provided reference library).  
> It is **not** a replacement for Git history. Treat Git commits/tags as the source of truth for code-level diffs.

---

## 🧭 Quick links

- [🕰️ Changelog](#️-changelog)
- [🧩 Conventions](#-changelog-conventions-recommended)
- [🗂️ Repo layout](#️-repo-layout)
- [📚 Project file bundle snapshot](#-project-file-bundle-snapshot)
- [✅ Updating this file](#-updating-this-file)
- [🔗 References](#-references)

---

## 🧩 Changelog conventions (recommended)

Use these headings inside each release entry:

- **Added** ➕ (new capability, new doc/standard, new directory)
- **Changed** 🔁 (behavior/contract updates, moved paths, updated invariants)
- **Deprecated** 🧓 (still works, but planned removal)
- **Removed** 🗑️ (deleted or no longer supported)
- **Fixed** 🩹 (bugfixes)
- **Security / Governance** 🛡️ (FAIR+CARE, sovereignty, access boundary changes)

> [!TIP]
> If a change affects **contracts, schemas, directory structure, governance rules, or release behavior**, it belongs here.

---

## 🕰️ Changelog

### [Unreleased] 🚧

#### Added ➕
- Added YAML front-matter metadata to align with governed-doc expectations.
- Added quick navigation + GitHub alert blocks to improve readability.

#### Changed 🔁
- Refreshed **Project file bundle snapshot** to match the currently supplied bundle (see appendix).
- Moved the repo skeleton and bundle snapshot into clearly labeled appendix sections.

#### Fixed 🩹
- Tightened wording around “seeded from docs” vs “Git is source of truth” to reduce ambiguity.

---

### 2025-12-31 — CHANGELOG seed (v1.0.0-draft) 🌱

#### Added ➕
- Created `CHANGELOG.md` as the repo-level changelog file.
- Added a “Project file bundle snapshot” section listing the currently supplied project files (to support audits and reproducibility).

#### Notes 📝
- Dates and version labels in older entries below reflect **documented version history** in the Master Guide / Markdown standards docs, and may not correspond to Git tags unless explicitly tagged.

---

### 2025-12-30 — Documentation standard milestone: KFM Markdown Formatting Guide (v1.0.0, draft) 🧷

#### Added ➕
- Drafted/updated Markdown governance rules:
  - YAML front-matter requirements (including FAIR+CARE labels)
  - Section/heading standards (emoji-anchored registry)
  - Citation requirements and AI attribution notes
  - Validation expectations for governed docs

---

### 2025-12-28 — Master Guide milestone: v13.0.0-draft (v13 redesign) 🧱

#### Added ➕
- v13 “one canonical home per subsystem” structure (contract-first + evidence-first framing).
- Expected repository roots called out explicitly in v13:
  - `schemas/` (contracts: JSON Schemas for catalogs/story/ui/telemetry)
  - `releases/` (release artifacts + auditables, e.g., SBOM/attestations)
  - `data/prov/` and `data/catalog/dcat/` as first-class metadata/lineage roots

#### Changed 🔁
- Story content expected under governed path:
  - `docs/reports/story_nodes/` with `draft/` vs `published/` workflow.
- Profiles references updated to the v11 family (STAC/DCAT/PROV), and CI/validation “gates” enumerated as required expectations.

#### Notes 📝
- This milestone supersedes v12 guide structure.

---

### 2025-12-27 — Master Guide milestone: v12.0.1-draft 🧰

#### Changed 🔁
- Refined doc structure to align with the universal doc template conventions.
- Clarified canonical paths, invariants, and the contract-first / evidence-first boundary language.

---

### 2025-12-17 — Master Guide milestone: v12.0.0-draft 🏗️

#### Added ➕
- Initial scaffolding for Master Guide v12:
  - Established pipeline ordering conceptually
  - Introduced governance structure baseline

---

## 🗂️ Repo layout

> [!NOTE]
> **Repo layout is defined by the Master Guide.** The skeleton below is illustrative for a v13-style structure.

<details>
  <summary><strong>📁 Typical v13-style skeleton (click to expand)</strong></summary>

- 📁 `data/`
  - 📁 `<domain>/`
    - 📁 `raw/`
    - 📁 `work/`
    - 📁 `processed/`
    - 📁 `mappings/`
    - 📄 `README.md`
  - 📄 `README.md`
- 📁 `docs/`
  - 📄 `MASTER_GUIDE_v12.md`
  - 📄 `MASTER_GUIDE_v13.md`
  - 📄 `glossary.md`
  - 📁 `architecture/`
  - 📁 `standards/`
  - 📁 `templates/`
  - 📁 `governance/`
  - 📁 `reports/`
    - 📁 `story_nodes/`
      - 📁 `templates/`
      - 📁 `draft/`
      - 📁 `published/`
- 📁 `schemas/`
- 📁 `src/`
  - 📁 `pipelines/`
  - 📁 `graph/`
  - 📁 `server/`
- 📁 `web/`
- 📁 `releases/`
- 📁 `tests/`
- 📁 `tools/`
- 📄 `README.md`
- 📄 `LICENSE`
- 📄 `CITATION.cff`
- 📄 `CHANGELOG.md`
- 📄 `CONTRIBUTING.md`
- 📄 `SECURITY.md`
- 📄 `.editorconfig`
- 📄 `.pre-commit-config.yaml`
- 📄 `docker-compose.yml`
- 📄 `.env.example`

</details>

---

## 📚 Project file bundle snapshot

This section records the **currently supplied project files** used to seed this changelog (helpful for audit/repro).

> [!IMPORTANT]
> This is a snapshot of the **ingested bundle** (e.g., uploaded docs) and may differ from what exists in the actual repo.

### 📦 Snapshot summary (current bundle)

| Category | Count | Notes |
|---|---:|---|
| 🧠 Core KFM docs (governing / architectural) | 2 | Present in current bundle |
| 📚 Reference library (supporting, non-normative) | 24 | Present in current bundle |
| 🧩 Programming mega-bundles (A…X) | 9 | Aggregated PDFs |
| ⚠️ Special/odd filenames | 1 | Present but may require renaming/indexing |

**Total files in current bundle:** **36**

---

### 🧠 Core KFM docs (governing / architectural)

- `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx`
- `🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx`

---

### 📚 Reference library (supporting, non-normative)

#### 🧪 Modeling / Simulation / Math
- `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf`
- `Understanding Statistics & Experimental Design.pdf`
- `think-bayes-bayesian-statistics-in-python.pdf`
- `regression-analysis-with-python.pdf`
- `Regression analysis using Python - slides-linear-regression.pdf`
- `graphical-data-analysis-with-r.pdf`

#### 🗺️ Geo / Remote Sensing / Cartography
- `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf`
- `python-geospatial-analysis-cookbook.pdf`
- `making-maps-a-visual-guide-to-map-design-for-gis.pdf`
- `Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf`

#### 🧱 Systems / Data / Architecture
- `Scalable Data Management for Future Hardware.pdf`
- `Data Spaces.pdf`
- `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf`

#### 🧬 Biology / Humanism / Law + AI
- `Principles of Biological Autonomy - book_9780262381833.pdf`
- `Introduction to Digital Humanism.pdf`
- `On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf`

#### 🖥️ Web / Graphics / Media
- `responsive-web-design-with-html5-and-css3.pdf`
- `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf`
- `compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf`
- `Spectral Geometry of Graphs.pdf`
- `Generalized Topology Optimization for Structural Design.pdf`

#### 🛡️ Security / Systems Programming
- `ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf`
- `Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf`
- `concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf`

---

### 🧩 Programming mega-bundles (multi-book compilations)

- `A programming Books.pdf`
- `B-C programming Books.pdf`
- `D-E programming Books.pdf`
- `F-H programming Books.pdf`
- `I-L programming Books.pdf`
- `M-N programming Books.pdf`
- `O-R programming Books.pdf`
- `S-T programming Books.pdf`
- `U-X programming Books.pdf`

---

### ⚠️ Special / filename hygiene (verify)

- `Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf`
  - ⚙️ Recommended follow-up: normalize extension (likely `.pdf`) and confirm indexing/tooling compatibility.

---

### 🔍 Referenced in docs but not present in this bundle (verify in repo)

- `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` (referenced; not included here)
- `Kansas Frontier Matrix – Unified Template Reference.docx` (referenced; not included here)
- `Kansas Frontier Matrix – Master Reference Index.docx` (referenced; not included here)

> [!NOTE]
> The earlier draft snapshot listed additional references (e.g., GIS basics, Google Maps API cookbooks, extra ML/statistics texts).  
> If those are still part of the repo’s intended reference set, re-attach them and bump this snapshot entry.

---

## ✅ Updating this file

When you make a PR that changes **contracts, schemas, directory structure, governance rules, or release behavior**, update `CHANGELOG.md` under **[Unreleased]** (or add a dated entry if cutting a release).

If the change is breaking:
- include **Changed** + **Security/Governance** notes as applicable 🛡️
- link to the governing doc(s) or ADR(s) that justify the break 🔗
- ensure corresponding schema/contract versions are bumped 📌

<details>
  <summary><strong>🧪 Release entry template (copy/paste)</strong></summary>

```markdown
### YYYY-MM-DD — <Release title> (vX.Y.Z)
#### Added ➕
- ...

#### Changed 🔁
- ...

#### Deprecated 🧓
- ...

#### Removed 🗑️
- ...

#### Fixed 🩹
- ...

#### Security / Governance 🛡️
- ...
```

</details>

---

## 🔗 References

- Master Guide v13: `docs/MASTER_GUIDE_v13.md`
- Markdown rules: `docs/standards/KFM_MARKDOWN_FORMATTING_STYLE_GUIDE.md` (and/or Markdown Work Protocol)
- Repo templates: `docs/templates/`
- Governance: `docs/governance/`
