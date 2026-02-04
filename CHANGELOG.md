# 📌 CHANGELOG — Kansas Matrix System 🗺️🧠

![Keep a Changelog](https://img.shields.io/badge/keep%20a%20changelog-1.1.0-orange)
![SemVer-ish](https://img.shields.io/badge/versioning-SemVer--style%20%2B%20draft-blue)
![Governed](https://img.shields.io/badge/governance-contract--first%20%7C%20evidence--first-brightgreen)

> [!IMPORTANT]
> This changelog is **governance-critical**. Any change that impacts **schemas**, **API contracts**, **pipeline order**, **directory canonical homes**, or **review gates** must be recorded here. ✅

---

## 🧾 Conventions

- **Format:** [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
- **Dates:** `YYYY-MM-DD`
- **Versions:** SemVer-style with a `-draft` prerelease label when the repository/spec is still in governed draft mode.
- **Where to write changes first:** `## [Unreleased]`

---

## 🧭 Non‑Negotiables (don’t regress) 🧱

- 🧩 **Contract-first:** schemas + API contracts are first-class artifacts; edits trigger strict versioning/compatibility review.
- 🧪 **Deterministic pipeline:** ETL transforms are idempotent, config-driven, and fully logged for reproducibility.
- 🧾 **Evidence-first:** catalog + provenance come *before* narrative or UI claims.
- 🔗 **Canonical pipeline order (hard rule):**  
  `ETL → STAC/DCAT/PROV catalogs → Graph → APIs → React/Map UI → Story Nodes → Focus Mode`

---

## [Unreleased] 🚧

### ✨ Added
- 📝 Created `CHANGELOG.md` to standardize versioned change tracking.
- 📚 Documented a **Reference Library inventory** (see below) to anchor future design + implementation decisions.

### 🔁 Changed
- TBD

### 🐛 Fixed
- TBD

### 🔒 Security
- TBD

### 🗺️ Roadmap / Proposed
- ⏱️ Near real-time ingestion + update cadence for event-driven layers (e.g., flood mapping).
- 🧪 Simulation modules + validation harness.
- 🕶️ Immersive modes (3D/AR exploration) as optional UI layers.
- 🧠 Federated / multi-model AI extensions + feedback loops to improve evidence-backed Q&A.

---

## [13.0.0-draft] - 2025-12-28 🧱

### ✨ Added
- 📁 New governed top-level subsystem homes:
  - `schemas/` ✅ (STAC/DCAT/PROV + StoryNodes + UI + telemetry schemas)
  - `releases/` ✅ (versioned release artifacts)
  - `data/prov/` ✅ (provenance roots)
  - `data/catalog/dcat/` ✅ (DCAT roots)

### 🔁 Changed
- 🧭 Enforced **one canonical directory per subsystem** (resolved duplicate/mystery folders).
- 🧩 Enforced **contract-first** across schema + API changes.
- 🧾 Enforced **evidence-first** (catalog before narrative).
- 🗺️ Reorganized Story Nodes under: `docs/reports/story_nodes/`  
  with a governed workflow: `draft/` → `published/`.
- ✅ Updated profile references (STAC/DCAT/PROV v11) and CI/validation gates.
- 🔄 Declared v13 as the successor to v12 (v13 supersedes v12 guide).

### ⚠️ Breaking
- Story content paths moved into the governed `docs/reports/story_nodes/` structure — update any tooling/scripts that read legacy locations.

---

## [12.0.1-draft] - 2025-12-27 🧹

### 🔁 Changed
- 🧾 Refined the Master Guide to align with the Universal Doc template.
- 🧭 Clarified canonical paths, invariants, and contract-first/evidence-first boundaries.

---

## [12.0.0-draft] - 2025-12-17 🌱

### ✨ Added
- 🏗️ Initial scaffolding for the v12 Master Guide:
  - Established baseline pipeline ordering
  - Established governance structure

---

## 🗂️ Expected Repo Layout (v13 snapshot)

<details>
<summary>📁 Click to expand the governed directory map</summary>

```text
📁 data/
├── 📁 <domain>/
│   ├── 📁 raw/          (read-only sources)
│   ├── 📁 work/         (intermediate outputs)
│   ├── 📁 processed/    (final outputs)
│   ├── 📁 mappings/     (dataset → STAC/DCAT/PROV docs, optional)
│   └── 📄 README.md
└── 📄 README.md

📁 docs/
├── 📄 MASTER_GUIDE_v12.md
├── 📄 MASTER_GUIDE_v13.md
├── 📄 glossary.md
├── 📁 architecture/
├── 📁 standards/
├── 📁 templates/
├── 📁 governance/
└── 📁 reports/
    └── 📁 story_nodes/
        ├── 📁 templates/
        ├── 📁 draft/
        └── 📁 published/

📁 mcp/
📁 schemas/
📁 src/
├── 📁 pipelines/
├── 📁 graph/
└── 📁 server/
📁 web/
📁 releases/
📁 tests/
📁 tools/

📄 README.md
📄 LICENSE
📄 CITATION.cff
📄 CHANGELOG.md
📄 CONTRIBUTING.md
📄 SECURITY.md
📄 docker-compose.yml
📄 .env.example
```

</details>

---

## 🏷️ Release & Data Versioning Notes

- 🧷 The repo can be treated as a **catalog of record**: tags/commits represent reproducible snapshots.
- 📌 For *major dataset milestones*, consider time-based tags like `v2025.1` (or SemVer tags) and ensure `CITATION.cff` points to the release tag so downstream users can cite the exact snapshot.

---

## 📚 Reference Library Inventory

<details>
<summary>📚 Click to expand the current reference library list</summary>

### 🗺️ GIS & Mapping
- `making-maps-a-visual-guide-to-map-design-for-gis.pdf`
- `GIS-Mapping-Topology.pdf`
- `Mapping Urban Spaces.pdf`
- `Archaeological 3D GIS.pdf`

### 📊 R / Data Visualization
- `graphical-data-analysis-with-r.pdf`
- `R-Python-Ruby-Various.pdf`

### 🤖 AI / ML
- `Neural Nerworks-Build Ai-Statistical Learning-Deep Learing-AI Safety-Linear Regression-bayesian.pdf`
- `Artificial Intelligence & Machine Learning in Health Care & Medical Sciences.pdf`

### 🌐 Web / UI
- `Web Design.pdf`
- `professional-web-design-techniques-and-templates.pdf`
- `learn-to-code-html-and-css-develop-and-style-websites.pdf`
- `CSS-HTML-JAVA-WebDesign.pdf`
- `Node.js-React-CSS-HTML.pdf`

### 🧰 DevOps / Security / Performance
- `Database-Docker-CI-Pipeline-DevOps-Security-Git-Shell-PowerShell.pdf`
- `foundations-of-software-and-system-performance-engineering-process-performance-modeling-requirements-testing-scalability-and-practice.pdf`

### 🧮 Scientific Computing
- `MATLAB-PyTorch-Numpy-SciPy-Statisctics-Programming Science Tools.pdf`
- `Applications from Engineering with MATLAB Concepts.pdf`
- `Hands-On Accelerator Physics Using MATLAB.pdf`

### 🧠 General Programming / Creativity
- `Various Programming Concepts.pdf`
- `Programming Design-Flexibility-Machine Learning-Test Development-Verilog-Software Qualify Assurance.pdf`
- `ssoar-2022-zipp-Programming_Creativity_Semantics_and_Organisation.pdf`
- `Data Science-Data Engineering-Machine Learing-Steganography-Bilogical Atonomy-PYthon Scripting-Sine Cosine Algorithm-People Anylitics-Experimental Design-Visualizations of Time-Oriented Data-Creativity.pdf`

</details>

---

## 🔗 Links (fill in your repo URL)

- [Unreleased]: `<REPO_URL>/compare/v13.0.0-draft...HEAD`
- [13.0.0-draft]: `<REPO_URL>/compare/v12.0.1-draft...v13.0.0-draft`
- [12.0.1-draft]: `<REPO_URL>/compare/v12.0.0-draft...v12.0.1-draft`
- [12.0.0-draft]: `<REPO_URL>/releases/tag/v12.0.0-draft`