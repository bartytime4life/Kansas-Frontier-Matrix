<!--
📌 Notebooks are KFM’s “lab bench”: exploration + prototypes + evidence drafts.
🗓️ Last reviewed: 2026-01-09
🔐 Reminder: anything that influences decisions must become a governed artifact (catalog + provenance), not stray notebook outputs.
-->

# 📓 Notebooks — Kansas Frontier Matrix (KFM)

<p align="left">
  <img alt="Jupyter" src="https://img.shields.io/badge/Jupyter-Notebooks-orange" />
  <img alt="Python" src="https://img.shields.io/badge/Python-3.11%2B-blue" />
  <img alt="GIS" src="https://img.shields.io/badge/GIS-Geospatial-success" />
  <img alt="Remote Sensing" src="https://img.shields.io/badge/Remote%20Sensing-GEE%20%26%20EO-informational" />
  <img alt="Docker" src="https://img.shields.io/badge/Docker-Recommended-2496ED" />
  <img alt="Reproducible" src="https://img.shields.io/badge/Reproducible-Preferred-brightgreen" />
  <img alt="Artifacts" src="https://img.shields.io/badge/Artifacts-_artifacts%2F%20%2B%20_runs%2F%20gitignored-lightgrey" />
  <img alt="Catalogs" src="https://img.shields.io/badge/Catalogs-STAC%20%7C%20DCAT%20%7C%20PROV-845ef7" />
  <img alt="Safety" src="https://img.shields.io/badge/Safety-no%20secrets%20%7C%20no%20PII-critical" />
</p>

Welcome to the **KFM notebooks workspace** 🧭 — a practical lab for:

- 🧪 exploratory research & rapid prototyping  
- 🗺️ geospatial + remote sensing experiments  
- 📊 statistics, modeling, validation, and “don’t fool yourself” checks  
- 🤖 ML/AI baselines, agent-style decision logic, and model eval  
- 🌐 map/UI visualization spikes (responsive design, WebGL, map styling)  
- 🧱 architecture proof-of-concepts before graduating into `src/` pipelines/services + tests ✅  

> [!IMPORTANT]
> ✅ Notebooks are for exploration and learning.  
> 🏭 Anything that becomes “real” must **graduate** into canonical code + tests + governed artifacts:
>
> **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode** 🧾🗂️

---

## 🔗 Quick links
- 🧩 Executable boundary: `../src/README.md`
- 📦 Data + metadata boundary: `../data/README.md`
- 📓 MCP (experiments + run receipts): `../mcp/README.md`
- 🧰 Toolchain + validators: `../tools/README.md`
- 🧪 Tests + CI gates: `../tests/README.md`
- 🌐 Web UI boundary: `../web/README.md` *(if present)*

---

## 🧭 Quick navigation
- [🧾 Doc metadata](#-doc-metadata)
- [🧭 Where this fits](#-where-this-fits-in-the-repo)
- [🗂️ Suggested folder layout](#️-suggested-folder-layout)
- [🧩 Notebook tracks](#-notebook-tracks-what-to-expect)
- [🚀 Quick start](#-quick-start)
- [✅ Notebook conventions](#-notebook-conventions-kfm-standard)
- [🧾 Run manifests](#-run-manifests-highly-recommended)
- [🧭 Reproducibility tiers](#-reproducibility-tiers-what-counts-as-real)
- [🧬 Lifecycle: notebook → production](#-lifecycle-notebook--production)
- [🧪 Testing notebooks](#-testing-notebooks-optional-but-powerful)
- [🔐 Data, licensing, and ethics](#-data-licensing-and-ethics-notes)
- [📚 Reference library](#-reference-library-all-project-files)
- [🕰️ Version history](#️-version-history)

---

## 🧾 Doc metadata

| Field | Value |
|---|---|
| Folder | `notebooks/` |
| Role | 📓 research + prototyping workspace (non-production) |
| Audience | analysts · researchers · maintainers · collaborators |
| Last updated | **2026-01-09** |
| Default output policy | `_artifacts/` + `_runs/` are **gitignored** |
| Evidence policy | decision-influencing outputs must become **cataloged + provenance-linked** |
| Canonical order | **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story → Focus** |

---

## 🧭 Where this fits in the repo

- ✅ **Production code:** `src/` (and `api/` if present) — not here.
- ✅ **Notebooks:** sandbox + research journal with repeatable runs.
- ✅ **Local artifacts:** export to `_artifacts/` (**gitignored**) so notebooks stay light.
- ✅ **Run manifests:** export to `_runs/` (**gitignored**) so you can reproduce quickly.
- ✅ **Evidence artifacts:** if output becomes a dataset → move to `data/processed/...` and **catalog it** (STAC/DCAT/PROV).
- ✅ **Decisions + receipts:** if results matter → write MCP entries (EXP + RUN) in `mcp/`.

> [!IMPORTANT]
> If a notebook output influences decisions, it must become a **governed evidence artifact** (STAC/DCAT + PROV + classification), not a stray file saved inside a notebook cell.

---

## 🗂️ Suggested folder layout

> Keep this boring & predictable so collaborators can jump in fast. 🧭

```text
📓 notebooks/
├─ 📘 README.md
├─ 🧩 _templates/               # notebook templates (EDA, GIS, RS, modeling, sim, report)
├─ 🚫 _data/                    # local-only datasets (gitignored)
├─ 📦 _artifacts/               # exported plots/tables/models (gitignored)
├─ 🧾 _runs/                    # run manifests + params (gitignored)
├─ 🖼️ _figures/                 # committed figures used in docs (small + stable)
├─ 🧭 00_orientation/           # KFM context + glossary + invariants
├─ 🧰 01_tooling/               # env, Docker, reproducibility helpers
├─ 🗺️ 02_gis_core/              # CRS, overlays, vector/raster workflows
├─ 🛰️ 03_remote_sensing/        # EO/GEE, composites, change detection
├─ 📊 04_stats/                 # EDA, regression, Bayes, inference checks
├─ 🤖 05_ml_agents/             # baselines, eval, decision logic
├─ 🧪 06_simulation_optimization/# V&V, sensitivity, optimization runs
├─ 🌐 07_web_mapping_viz/        # map styles, responsive/UI spikes, WebGL demos
├─ 🧬 08_language_tools/         # DSL sketches, schemas, parsing experiments
└─ 🧠 09_human_factors/          # governance, ethics, human-centered notes
```

> [!TIP]
> If a notebook depends on “real” infra (PostGIS/Neo4j/object storage), capture it in a run manifest and prefer containers for reproducibility. 🐳✅

---

## 🧩 Notebook tracks (what to expect)

| Track | Folder | Focus | Typical outputs |
|---|---|---|---|
| 🧭 Foundations | `00_orientation/` | KFM context, glossary, system invariants | notes + diagrams |
| 🧰 Tooling | `01_tooling/` | env setup, Docker workflows, reproducible runs | run manifests |
| 🗺️ GIS Core | `02_gis_core/` | vector/raster ops, CRS sanity, geoprocessing | GeoJSON/GeoPackage, small COG |
| 🛰️ Remote Sensing | `03_remote_sensing/` | time-series, composites, change detection | quicklooks + draft STAC |
| 📊 Statistics | `04_stats/` | EDA, regression, Bayes, experimental design | diagnostics + metrics |
| 🤖 ML + Agents | `05_ml_agents/` | baselines, eval, decision logic (human-in-loop) | eval tables + draft model cards |
| 🧪 Simulation + Optimization | `06_simulation_optimization/` | V&V, uncertainty, sensitivity, optimization | run bundles + checks |
| 🌐 Web Maps + Viz | `07_web_mapping_viz/` | cartography, responsive UI spikes, WebGL | small assets + demos |
| 🧬 Language Tools | `08_language_tools/` | DSL sketches, parsers, schema ideas | schemas + mini compilers |
| 🧠 Human Factors | `09_human_factors/` | ethics, autonomy, governance, policy notes | decision memos |

---

## 🚀 Quick start

### Option A — Local (fastest) ⚡
```bash
cd notebooks
python -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

### Option B — Docker (recommended) 🐳
```bash
docker compose up --build
```

> [!CAUTION]
> 🔐 Never bake secrets into images. Use `.env` + environment variables and keep `.env` out of git.

---

## ✅ Notebook conventions (KFM standard)

### 🏷️ Naming
Use a **two-digit prefix** + verb-first slug:

- `00_intro_kfm_context.ipynb`
- `02_vector_overlay_clip.ipynb`
- `03_gee_ndvi_timeseries.ipynb`
- `04_regression_baseline_diagnostics.ipynb`
- `06_simulation_sensitivity_sweep.ipynb`

### 🧱 Standard notebook header (required for shareable work)
Start every notebook with:

1) 🎯 **Purpose** (what question are we answering?)  
2) 📥 **Inputs** (datasets/sources, assumptions, classification)  
3) 📤 **Outputs** (where artifacts will be written)  
4) 🎛️ **Parameters cell** (AOI, dates, EPSG, seeds, thresholds)  
5) 🧰 **Environment cell** (versions; optional lock snapshot)  

> [!TIP]
> If you can’t list inputs/assumptions, the notebook is still “scratch mode.” That’s fine — just don’t ship it.

### ✂️ Keep notebooks diff-friendly (recommended)
- avoid giant embedded outputs (save to `_artifacts/`)
- clear noisy outputs before committing (or use output-stripping tooling)
- prefer deterministic ordering and stable sort keys

---

## 🧾 Run manifests (highly recommended)

For any notebook producing outputs worth keeping, write a run manifest to `_runs/`.

**Suggested path:** `_runs/<notebook_slug>/<timestamp>/run.manifest.json`

Minimal example:
```json
{
  "run_id": "kfm.nb.03_gee_ndvi_timeseries.2026-01-09T12:00:00Z",
  "notebook": "03_remote_sensing/03_gee_ndvi_timeseries.ipynb",
  "params": {
    "aoi": "ks_bbox",
    "start": "2020-01-01",
    "end": "2020-12-31",
    "epsg": "EPSG:4326",
    "seed": 42
  },
  "inputs": [
    { "type": "catalog", "id": "stac://<collection_or_item_id>", "classification": "public" }
  ],
  "outputs": [
    { "type": "plot", "path": "_artifacts/ndvi_timeseries.png" },
    { "type": "draft_stac_item", "path": "_artifacts/stac/item.json" }
  ],
  "warnings": []
}
```

### 🧼 Repro checklist ✅
- [ ] Parameters cell at top (AOI, EPSG, dates, seeds)
- [ ] Deterministic seeds recorded (if stochastic)
- [ ] Environment captured (lockfile or snapshot)
- [ ] Outputs written to `_artifacts/` (gitignored) **or** promoted to `data/processed/...`
- [ ] Inline outputs kept small (save files instead of giant cell outputs)
- [ ] No secrets/tokens/internal endpoints in cells, outputs, or logs

---

## 🧭 Reproducibility tiers (what counts as “real”)

KFM notebook work moves through tiers to prevent “cool demo” from becoming “trusted truth.”

| Tier | Name | Allowed behavior | Not allowed |
|---|---|---|---|
| 🟠 Tier 0 | Scratch | quick exploration, messy cells | decision claims, publishing |
| 🟡 Tier 1 | Shareable | header + params + basic outputs | hidden inputs, unclear licenses |
| 🟢 Tier 2 | Evidence-ready | run manifest + stable outputs + provenance pointers | mystery data, unlabeled derivations |
| 🔵 Tier 3 | Productionized | logic moved to `src/` + tests + catalogs | notebook-only business logic |

> [!IMPORTANT]
> Any Tier 2+ output must be traceable: **inputs → transforms → outputs → catalogs → provenance** 🧾🧬

---

## 🧬 Lifecycle: notebook → production

```mermaid
flowchart LR
  A[🧪 Notebook experiment] --> B[📦 Local artifacts<br/>_artifacts/]
  A --> R[🧾 Run manifest<br/>_runs/]
  A --> C[🧾 Findings + notes]
  C --> D[🏗️ Extract core logic<br/>src/ (pipelines/services)]
  D --> E[✅ Tests + fixtures]
  E --> F[🔁 Pipeline/service integration]
  F --> G[🗂️ STAC/DCAT/PROV<br/>+ validation gates]
  G --> H[🌐 UI + Story/Focus evidence bundle]
```

🏁 Graduation checklist
- [ ] Extract functions into `src/` (no notebook-only globals)
- [ ] Add tests (unit + integration/contract as needed)
- [ ] Define/validate contracts (schemas, CRS, expected columns)
- [ ] If evidence: store in `data/processed/...` + STAC/DCAT + PROV
- [ ] Confirm classification & redaction are correct

---

## 🧪 Testing notebooks (optional but powerful)

If notebooks become Tier 2+, consider:
- ✅ smoke-running critical notebooks automatically (parameterized)
- ✅ asserting outputs exist and meet schema expectations
- ✅ failing fast on silent drift (CRS mismatch, missing columns, empty exports)

> [!TIP]
> Notebook tests should validate **contracts** and **invariants**, not pixel-perfect plots.

---

## 🔐 Data, licensing, and ethics notes

- 📜 Don’t commit licensing-unclear data/documents publicly
- 🔒 Treat outputs as decision-influencing: document assumptions + uncertainty
- 🧷 Redact sensitive fields/locations when required (sovereignty-aware)
- 🤖 Label AI involvement; keep AI outputs provenance-linked and advisory
- 🔐 Keep secrets out of notebooks (tokens, internal endpoints, credentials)

---

## 📚 Reference library (all project files)

> These files shape notebook templates, sanity checks, and how we reason about uncertainty, maps, systems, and governance.

<details>
<summary><strong>🧭 Core KFM design & engineering spine</strong></summary>

- 📄 `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx` — platform boundaries, governed ordering, catalog-first posture

</details>

<details>
<summary><strong>🛰️ Remote sensing & Earth observation</strong></summary>

- 📄 `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf` — time-series workflows, exports, parameter capture

</details>

<details>
<summary><strong>🗺️ GIS, cartography, and mapping UX</strong></summary>

- 📄 `python-geospatial-analysis-cookbook.pdf` — CRS hygiene, vector/raster IO, PostGIS patterns  
- 📄 `making-maps-a-visual-guide-to-map-design-for-gis.pdf` — cartographic honesty, legend design, perceptual pitfalls  
- 📄 `Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf` — mobile/offline constraints & map meaning

</details>

<details>
<summary><strong>📊 Statistics, EDA, regression & Bayesian reasoning</strong></summary>

- 📄 `Understanding Statistics & Experimental Design.pdf` — assumptions, bias, design discipline  
- 📄 `graphical-data-analysis-with-r.pdf` — EDA instincts, anomaly spotting  
- 📄 `regression-analysis-with-python.pdf` — baseline regression workflows + diagnostics  
- 📄 `Regression analysis using Python - slides-linear-regression.pdf` — consistent reporting shape  
- 📄 `think-bayes-bayesian-statistics-in-python.pdf` — uncertainty, priors/posteriors, credible intervals

</details>

<details>
<summary><strong>🧪 Simulation, verification & optimization</strong></summary>

- 📄 `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf` — verification/validation, sensitivity analysis, UQ discipline  
- 📄 `Generalized Topology Optimization for Structural Design.pdf` — objective/constraint clarity, reproducible optimization runs

</details>

<details>
<summary><strong>🕸️ Graphs & structure</strong></summary>

- 📄 `Spectral Geometry of Graphs.pdf` — graph metrics intuition and careful interpretation

</details>

<details>
<summary><strong>🗄️ Data systems & scaling</strong></summary>

- 📄 `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf` — SQL hygiene + operational patterns  
- 📄 `Scalable Data Management for Future Hardware.pdf` — partitions, locality, throughput thinking  
- 📄 `Data Spaces.pdf` — federation & interoperability mindset (IDs + catalogs over ad-hoc files)

</details>

<details>
<summary><strong>🌐 Web, WebGL, and media correctness</strong></summary>

- 📄 `responsive-web-design-with-html5-and-css3.pdf` — responsive constraints that shape notebook exports  
- 📄 `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf` — coordinate sanity for WebGL spikes  
- 📄 `compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf` — small, correct figures and quicklooks

</details>

<details>
<summary><strong>🤖 ML practice & AI governance</strong></summary>

- 📄 `Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf` — baseline-first ML workflow, evaluation artifacts  
- 📄 `On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf` — labeling, accountability framing for AI outputs

</details>

<details>
<summary><strong>🛡️ Security, adversarial thinking & concurrency</strong></summary>

- 📄 `ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf` — defensive posture, threat modeling for data tooling  
- 📄 `Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf` — hostile-input awareness for parsers  
- 📄 `concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf` — concurrency discipline and determinism warnings

</details>

<details>
<summary><strong>🧠 Human factors & systems thinking</strong></summary>

- 📄 `Introduction to Digital Humanism.pdf` — human-centered governance and accountability  
- 📄 `Principles of Biological Autonomy - book_9780262381833.pdf` — systems/feedback metaphors for stable workflows

</details>

<details>
<summary><strong>📚 Programming reference shelves</strong></summary>

- 📄 `A programming Books.pdf`  
- 📄 `B-C programming Books.pdf`  
- 📄 `D-E programming Books.pdf`  
- 📄 `F-H programming Books.pdf`  
- 📄 `I-L programming Books.pdf`  
- 📄 `M-N programming Books.pdf`  
- 📄 `O-R programming Books.pdf`  
- 📄 `S-T programming Books.pdf`  
- 📄 `U-X programming Books.pdf`

</details>

---

## 🕰️ Version history

| Version | Date | Summary | Author |
|---:|---|---|---|
| v1.2.0 | 2026-01-09 | Updated repo boundary links, standardized pipeline order framing, added emoji folder map, clarified run manifests + tiers + graduation checklist, and enumerated all project reference files. | KFM Engineering |
| v1.1.0 | 2026-01-07 | Prior iteration: notebook lab-bench framing, track layout, run manifest pattern, graduation rules. | KFM Engineering |

---

🧪 Explore fast.  
🧾 Record assumptions.  
🏷️ Promote evidence properly.  
🛡️ Keep it governed. ✅
