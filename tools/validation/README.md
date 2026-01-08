# 🧪 Validation Toolkit

![stage](https://img.shields.io/badge/stage-active-success)
![quality-gate](https://img.shields.io/badge/quality-gate_required-critical)
![policy](https://img.shields.io/badge/policy-OPA%20%2B%20Conftest-6f42c1)
![stac](https://img.shields.io/badge/metadata-STAC-informational)
![geo](https://img.shields.io/badge/geospatial-PostGIS%20%7C%20GDAL-orange)
![stats](https://img.shields.io/badge/validation-stats%20%7C%20ML-blue)
![security](https://img.shields.io/badge/security-defensive%20checks-important)

> ✅ **If it ships, it validates.**  
> This folder defines the *quality gates* for Kansas Frontier Matrix (KFM) data, catalogs, models, simulations, databases, and UI outputs.

---

## 📌 What this folder is for

`tools/validation/` exists to make the KFM ecosystem **provably reliable**:

- 🧾 **Traceability**: every produced asset can be traced back to inputs + pipeline version + policy decisions.
- 🧪 **Scientific rigor**: verification & validation (V&V), uncertainty thinking, reproducibility.
- 🌎 **Geospatial correctness**: CRS, bbox/extent, topology, raster/vector integrity.
- 🧠 **Model accountability**: regression/ML evaluation, drift detection, explainability artifacts.
- 🛡️ **Security posture**: defensive scanning and safe-by-default checks.
- 🧭 **Governance**: licensing, provenance, FAIR/CARE-aligned publishing, ethical constraints.

---

## 🧭 Table of contents

- [⚡ Quickstart](#-quickstart)
- [🧱 Validation layers](#-validation-layers)
- [🗂️ Directory map](#-directory-map)
- [🛰️ STAC and catalog QA](#-stac-and-catalog-qa)
- [🌍 Geospatial validation](#-geospatial-validation)
- [📈 Statistics and ML validation](#-statistics-and-ml-validation)
- [🧮 Modeling and simulation V&V](#-modeling-and-simulation-vv)
- [🗃️ Data engineering and database validation](#-data-engineering-and-database-validation)
- [🖥️ Web UI and 3D visualization validation](#-web-ui-and-3d-visualization-validation)
- [🔐 Security validation](#-security-validation)
- [📜 Governance and ethics checks](#-governance-and-ethics-checks)
- [🧩 Adding a new validator](#-adding-a-new-validator)
- [📦 Artifacts and reporting](#-artifacts-and-reporting)
- [🗺️ Reference library used by this folder](#-reference-library-used-by-this-folder)

---

## ⚡ Quickstart

Run validations from the **repo root**.

### Option A: Make targets

```bash
make validate
make validate-stac
make validate-geo
make validate-stats
make validate-ml
make validate-db
make validate-web
make validate-security
```

### Option B: Python module entrypoint

```bash
python -m tools.validation all
python -m tools.validation stac ./data/catalog
python -m tools.validation geo  ./data/derived
```

### Option C: CI lanes only

```bash
# run only checks that are mandatory for merge
python -m tools.validation ci
```

> 🧠 **Design rule:** every validator must run locally *and* in CI with identical semantics.

---

## 🧱 Validation layers

KFM validation is deliberately **layered** so failures are fast, actionable, and auditable:

1. 🧹 **Lint & Type**  
   Formatting, static analysis, typing, doc lint.
2. 📐 **Schema**  
   JSON Schema, STAC JSON Schema, DCAT/metadata schema, telemetry schema.
3. 🧩 **Policy as code**  
   OPA/Conftest rules (what we *allow* to ship).
4. 🛰️ **Catalog integrity**  
   STAC relationships, links, collections, paging, provenance chains.
5. 🌍 **Geospatial integrity**  
   CRS, extents, topology, raster metadata, no silent reprojection.
6. 📈 **Stats & Drift**  
   sanity checks, distributions, regression diagnostics, anomaly detection.
7. 🧠 **ML evaluation**  
   baselines, cross-validation, calibration, fairness flags, reproducibility.
8. 🧮 **Modeling & simulation V&V**  
   numerical checks, conservation checks, UQ, sensitivity.
9. 🗃️ **DB & performance**  
   constraints, migrations, query plans, scalability smoke tests.
10. 🖥️ **UI & viz**  
   accessibility, responsive behavior, WebGL stability, visual regression.
11. 🔐 **Security**  
   dependency scanning, secrets, SBOM, config hardening checks.
12. 📜 **Governance**  
   licenses, provenance, human-centered constraints, publish readiness.

---

## 🗂️ Directory map

> 🧩 This is the recommended layout. Adjust to match the repo, but keep the *conceptual lanes*.

```text
🧰 tools/validation/
├─ 📄 README.md                         👈 you are here
├─ 🧾 manifest.yml                      🧾 single source of truth for validators
├─ 🏃 runners/
│  ├─ 🏁 run_all.py                     🏁 orchestrator (local + CI)
│  ├─ 🛣️ run_lane.py                    🛣️ run one lane by name
│  └─ 📦 report.py                      📦 unify outputs into artifacts
├─ 🛰️ stac/
│  ├─ 🛰️ catalog_qa.py                  🛰️ fast STAC static checks
│  ├─ 📐 jsonschema_validate.py         📐 schema-based validation
│  └─ 🧪 fixtures/                      🧪 minimal reproducible catalogs
├─ 🧩 policy/
│  ├─ 🧩 stac_provenance.rego           🧩 required fields, provenance rules
│  ├─ ⚙️ faircare.rego                  ⚙️ sensitive-layer governance
│  └─ 📘 conftest.md                    📘 how to run policy gates
├─ 🌍 geo/
│  ├─ 🧭 check_crs.py                   🧭 CRS & axis sanity checks
│  ├─ 📦 check_bbox.py                  📦 bbox/extent correctness
│  ├─ 🧱 check_geometries.py            🧱 topology/validity checks
│  └─ 🗺️ check_rasters.py               🗺️ raster metadata + nodata + tiling
├─ 📈 stats/
│  ├─ 📈 drift_checks.py                📈 distribution + drift
│  ├─ 📉 regression_diagnostics.py      📉 residuals, leverage, outliers
│  └─ 📊 eda_report.R                   📊 optional R-based visual EDA report
├─ 🤖 ml/
│  ├─ 🧠 eval_baselines.py              🧠 metrics + baselines
│  ├─ 🎯 calibration.py                 🎯 calibration + uncertainty
│  └─ 🪪 model_card_check.py            🪪 model card completeness gate
├─ 🧮 sim/
│  ├─ 🧮 invariants.py                  🧮 conservation / invariants
│  ├─ 📐 convergence.py                 📐 grid/time-step convergence
│  └─ 🌫️ uq.py                          🌫️ uncertainty quantification helpers
├─ 🗃️ db/
│  ├─ 🗃️ constraints.sql                🗃️ constraints & invariants
│  ├─ 🌎 postgis_checks.sql             🌎 geometry validity & SRID checks
│  └─ ⚡ explain_guard.py               ⚡ query plan smoke tests
├─ 🖥️ web/
│  ├─ 💡 lighthouse_ci/                 💡 performance + accessibility
│  ├─ 🖼️ visual_regression/             🖼️ map layer snapshots
│  └─ 🎮 webgl_smoke/                   🎮 context + capability checks
├─ 🔐 security/
│  ├─ 🔎 secrets_scan.yml               🔎 secrets policy
│  ├─ 📦 sbom_check.py                  📦 SBOM presence & diffs
│  └─ 🧷 dependency_audit.py            🧷 dependency health checks
└─ 📦 artifacts/
   └─ 📌 .gitkeep                        📦 CI writes reports here
```

---

## 🛰️ STAC and catalog QA

KFM treats the catalog as a **product**: if the catalog lies, the UI lies.

### ✅ What we validate for STAC

- **Schema correctness**: STAC version alignment, item/collection/catalog schema validity.
- **Extensions**: required STAC extensions present (e.g., projection when we publish geospatial assets).
- **Provenance**: explicit “derived from” relationships and version tagging.
- **Links**: hrefs resolve, rel types are correct, no circular loops unless explicitly allowed.
- **Providers & license**: publishing posture is explicit.

### Example required fields pattern

```json
{
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/projection/v2.0.0/schema.json"
  ],
  "properties": {
    "kfm:mdp_version": "v11.2.6",
    "proj:epsg": 4326
  },
  "providers": [
    { "name": "Kansas Frontier Matrix", "roles": ["processor"] }
  ],
  "license": "CC-BY 4.0",
  "links": [
    {
      "rel": "derived_from",
      "href": "stac://raw/source_asset_01",
      "type": "application/json",
      "title": "Provenance chain"
    }
  ]
}
```

### Policy gate with OPA and Conftest

Use policy as code to enforce **non-negotiables**:

```bash
conftest test ./data/catalog \
  --policy tools/validation/policy \
  --namespace kfm
```

> 🧩 Policies should be small, composable, and written like contracts.

### `catalog_qa.py` fast checks

This lane is your “lint for STAC”:

- Missing required keys (`stac_version`, `stac_extensions`, `providers`, `license`)
- Broken `href` targets
- Provenance gaps (`derived_from` absent where expected)
- Version mismatches (`kfm:mdp_version`)
- Duplicate IDs, orphan items, invalid rels

---

## 🌍 Geospatial validation

Geospatial validation is split into **format**, **geometry**, and **meaning**:

### ✅ Format and metadata

- Raster:
  - CRS defined and consistent
  - nodata present and sane
  - tiling and overviews for web delivery when required
- Vector:
  - valid geometries (no self-intersections, no NaNs)
  - SRID set and consistent
  - attributes schema stable

### ✅ Spatial integrity

- bbox matches geometry/raster extent
- no accidental axis flips
- reprojection performed deliberately (and recorded)
- tolerances documented (meters vs degrees)

### ✅ Cartographic integrity

Map design and legend correctness are treated as validation targets:

- legend keys exist for every layer class
- ramps are consistent across versions
- accessibility constraints (contrast, colorblind safety) are checked in UI snapshot tests

---

## 📈 Statistics and ML validation

### Statistical sanity checks

- distribution checks (range, missingness, spikes)
- drift detection between releases
- outlier audit trails (why a point is extreme)

### Regression diagnostics

- residual behavior checks
- leverage & influence
- multicollinearity flags
- train/test leakage detectors

### Bayesian checks

- posterior predictive checks
- calibration diagnostics
- uncertainty reporting requirements (when the UI shows “confidence”)

### Deep learning checks

- learning curve artifacts
- overfitting detection gates
- reproducibility checks (seeds, deterministic ops when feasible)

---

## 🧮 Modeling and simulation V&V

We follow a NASA-grade mindset:

- ✅ **Code verification**: “did we implement the equations right?”
- ✅ **Solution verification**: “did we solve the equations accurately?”
- ✅ **Validation**: “does the model match reality for the intended use?”
- 🌫️ **Uncertainty quantification**: “how wrong might we be, and why?”

Suggested checks:

- invariants and conservation laws
- mesh/time-step convergence
- sensitivity analysis
- benchmark problems (known analytic/empirical references)

---

## 🗃️ Data engineering and database validation

### PostgreSQL and PostGIS

- constraints are enforced (NOT NULL, FK, CHECK)
- geometry validity enforced in DB
- SRID constraints checked in SQL
- migration safety checks (no destructive changes without flags)

### Scalability and performance

- benchmark queries (representative workloads)
- plan regressions (EXPLAIN guardrails)
- streaming and incremental workloads where relevant

### Data spaces mindset

When data is federated, validation must travel with it:

- interoperability checks (contracts, schemas, semantics)
- trust checks (provenance, policy compliance)
- governance checks (usage controls, licensing posture)

---

## 🖥️ Web UI and 3D visualization validation

### Responsive and accessibility

- responsive breakpoints don’t break map usability
- keyboard navigation works
- ARIA labels exist for core controls
- map legends are readable and consistent

### WebGL stability

- context creation smoke tests
- capability detection
- crash regression tests on shader changes
- performance budgets for critical scenes

### Visual regression testing

This is *mandatory* for map-heavy products:

- layer snapshots pinned per release
- legend snapshots pinned per release
- tolerance-based image diffs
- “semantic diffs” for vector symbology when possible

---

## 🔐 Security validation

Defensive checks only ✅

- secrets scanning (keys, tokens, credentials)
- dependency audits (known vulnerable versions)
- SBOM required for release artifacts
- config sanity checks (CORS, CSP, headers)

> 🛡️ **Important:** we do not ship offensive security tooling in this folder.  
> Use security references for defensive hardening and awareness.

---

## 📜 Governance and ethics checks

These checks exist because KFM is **not** just a codebase—it’s a public-facing research tool.

- license presence and correctness
- provenance chain completeness
- “sensitive layer” publishing rules
- FAIR/CARE-aligned posture (especially for hydrology and culturally sensitive content)
- AI governance checks (model cards, dataset cards, limitations, non-alert disclaimers)

---

## 🧩 Adding a new validator

A validator is considered “KFM-grade” when it has:

- ✅ deterministic behavior
- ✅ clear input contract (what it consumes)
- ✅ explicit output artifacts (what evidence it produces)
- ✅ an exit code contract (pass/fail/warn)
- ✅ a CI lane mapping (where it runs)

### Checklist

- [ ] Add your validator under the appropriate lane folder  
- [ ] Register it in `tools/validation/manifest.yml`  
- [ ] Ensure it writes artifacts under `tools/validation/artifacts/<validator-name>/`  
- [ ] Provide at least one fixture in `fixtures/`  
- [ ] Add it to CI lane runner  
- [ ] Document it in this README (one paragraph + example run)

---

## 📦 Artifacts and reporting

All validators should emit:

- `report.json` (machine-readable)
- `report.md` (human-readable summary)
- `junit.xml` (CI-friendly)
- optional: plots, snapshots, diffs, notebook exports

Recommended folder pattern:

```text
tools/validation/artifacts/
└─ <lane>/
   └─ <check>/
      ├─ report.json
      ├─ report.md
      ├─ junit.xml
      └─ extras/
```

---

## 🗺️ Reference library used by this folder

This validation suite is intentionally grounded in the project’s internal reference library 📚  
These files inform *how we define correctness* across science, geospatial, UI, security, and governance.

### Core KFM documents

- `Kansas Frontier Matrix (KFM) – Comprehensive Engineering Design.docx` 🏗️
- `Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf` 🗺️
- `Latest Ideas.docx` 💡
- `Other Ideas.docx` 🧾

### Modeling, simulation, and math

- `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf` 🚀
- `Generalized Topology Optimization for Structural Design.pdf` 🧱
- `Spectral Geometry of Graphs.pdf` 🧠

### Statistics, experiment design, and ML

- `Understanding Statistics & Experimental Design.pdf` 🧪
- `regression-analysis-with-python.pdf` 📉
- `Regression analysis using Python - slides-linear-regression.pdf` 🎓
- `think-bayes-bayesian-statistics-in-python.pdf` 🎲
- `graphical-data-analysis-with-r.pdf` 📊
- `Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf` 🤖

### Geospatial, cartography, and remote sensing

- `python-geospatial-analysis-cookbook.pdf` 🌎
- `making-maps-a-visual-guide-to-map-design-for-gis.pdf` 🎨
- `Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf` 📱
- `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf` 🛰️

### Data management and databases

- `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf` 🗃️
- `Scalable Data Management for Future Hardware.pdf` ⚡
- `Data Spaces.pdf` 🧩

### Web, visualization, and media formats

- `responsive-web-design-with-html5-and-css3.pdf` 🧱
- `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf` 🎮
- `compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf` 🖼️

### Concurrency, distributed systems, and software practice

- `concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf` 🧵
- `A programming Books.pdf` 🧰
- `B-C programming Books.pdf` 🧰
- `D-E programming Books.pdf` 🧰
- `F-H programming Books.pdf` 🧰
- `I-L programming Books.pdf` 🧰
- `M-N programming Books.pdf` 🧰
- `O-R programming Books.pdf` 🧰
- `S-T programming Books.pdf` 🧰
- `U-X programming Books.pdf` 🧰

### Governance, law, and human-centered constraints

- `Introduction to Digital Humanism.pdf` 🤝
- `On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf` ⚖️
- `Principles of Biological Autonomy - book_9780262381833.pdf` 🧬

### Security references

- `ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf` 🛡️
- `Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf` ⚠️ *(defensive awareness only)*

---

<div align="center">

**KFM Validation Toolkit** · 🧪 Evidence-driven · 🛰️ Catalog-first · 🌎 Geo-correct · 🔐 Defensive  
</div>

