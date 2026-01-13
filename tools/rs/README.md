# 🦀 tools/rs — Rust Tooling for Kansas Frontier Matrix (KFM)

<p align="center">
  <img alt="Rust" src="https://img.shields.io/badge/Rust-stable-000000?logo=rust&logoColor=white">
  <img alt="Cargo" src="https://img.shields.io/badge/Built%20with-Cargo-3b2f2f?logo=rust&logoColor=white">
  <img alt="Provenance First" src="https://img.shields.io/badge/Provenance-first-blue">
  <img alt="Geo" src="https://img.shields.io/badge/Geo-GIS%20%2B%20Remote%20Sensing-2b8a3e">
  <img alt="CLI" src="https://img.shields.io/badge/Tools-CLI%20%2B%20Libraries-6f42c1">
</p>

<p align="center">
  <b>High-performance, reproducible Rust utilities</b> for geospatial ingest, transforms, tiling, streaming, and analysis — designed to plug cleanly into KFM’s provenance-first architecture. 🌾🗺️
</p>

---

## ✨ What lives in `tools/rs/`

This folder is the **Rust sidecar** for KFM: small, sharp, composable tools that are easiest to do in Rust because we want:

- ⚡ **Speed + memory safety** (big rasters, big vectors, big graphs)
- 🔁 **Determinism + reproducibility** (stable outputs, stable ordering, stable provenance)
- 🧩 **Portability** (CLI binaries, containers, and optionally WASM modules)
- 🧾 **Provenance-first outputs** (metadata + citations are first-class artifacts)

> [!NOTE]
> The “source of truth” for platform architecture remains the KFM docs. Rust tools should **not** re-implement business rules that already live elsewhere — they should accelerate well-defined tasks behind clean interfaces. 🧼

---

## 🧭 Design principles (non-negotiables)

### 1) Provenance-first by default 🧾
Every tool MUST be able to explain:
- ✅ what went in (inputs + versions)
- ✅ what happened (steps + parameters)
- ✅ what came out (artifacts + checksums)
- ✅ how to reproduce (exact command + config)

Practical rules:
- Always emit a **machine-readable run record** (e.g., JSON/JSONL) alongside outputs.
- Prefer **content-addressing** (hashes) and **stable identifiers** for generated artifacts.
- Keep **metadata & citations** next to the data (don’t bury truth in logs).

### 2) Clean boundaries (ports & adapters) 🧩
Rust tools should behave like **well-bounded components**:
- Minimal assumptions about infrastructure
- Explicit inputs/outputs
- Replaceable backends (filesystem vs object storage, PostGIS vs files, etc.)

If you’re adding a new feature, ask: **Is it domain logic, or a tool adapter?**  
If it’s domain logic, it likely belongs outside `tools/rs`.

### 3) Human-centered + accountable outputs 🤝
KFM’s ethos is that the system should augment human understanding, not obscure it:
- Make outputs inspectable
- Make failure modes clear
- Prefer explainable diagnostics over “magic” behavior

---

## 🚀 Quick start

### ✅ Prereqs
- Rust toolchain (stable): `rustup` + `cargo`
- (Optional) System deps for geospatial backends:
  - GDAL/PROJ if you choose crates that link to them
  - Postgres client libraries if you talk directly to PostGIS

### 🧱 Build
From repo root:

```bash
cd tools/rs
cargo build --release
```

### 🧪 Test + lint
```bash
cargo test
cargo fmt --all
cargo clippy --all-targets --all-features -- -D warnings
```

### 📦 Install a local tool (example)
```bash
cargo install --path tools/rs/<crate-name>
```

> [!TIP]
> Keep tools **installable** and **discoverable**: `--help` should be excellent, and `--version` should include build metadata when possible.

---

## 🧰 Expected tool “shape” (CLI contract)

Even if we have multiple binaries, they should look and feel consistent:

### Standard flags
- `--input`, `--output`
- `--config <path>` (TOML/YAML/JSON — pick one and stick to it)
- `--format <...>` (geojson / parquet / gpkg / mbtiles / pmtiles / cog / …)
- `--dry-run` (prints plan + expected artifacts)
- `--emit-provenance <path>` (or always emit by default)

### Standard exit behavior
- `0` success
- Non-zero for validation failures, missing inputs, or runtime errors
- Errors MUST be structured and actionable

### Standard artifacts
Alongside primary outputs, prefer generating:
- `*.prov.json` or `*.run.json` (run record)
- `*.manifest.json` (artifact list + hashes)
- Optional: `*.report.md` (human-readable summary)

---

## 📦 Workspace layout (recommended)

> If this repo already has a Rust layout, follow it. If not, this is the recommended default.

```text
tools/rs/ 🦀
├─ Cargo.toml                # 🧰 workspace manifest
├─ crates/                   # 📦 Rust crates live here
│  ├─ kfm-cli/               # 🧭 unified CLI (optional)
│  ├─ kfm-geo/               # 🌍 vector/raster utilities + conversions
│  ├─ kfm-stac/              # 🗂️ STAC helpers (catalogs, validation, packing)
│  ├─ kfm-prov/              # 🧾 provenance + manifests + hashing
│  ├─ kfm-stream/            # 🌊 sensor/event stream ingestion helpers
│  ├─ kfm-graph/             # 🕸️ graph analytics helpers (optional)
│  └─ kfm-sim/               # 🧪 simulation + VVUQ helpers (optional)
├─ fixtures/                 # 🧪 small test datasets (never huge)
└─ README.md                 # 📘 you are here
```

---

## 🗺️ How Rust tools fit into the larger KFM pipeline

Rust tools typically accelerate the “hot path” pieces in KFM:

### 🌾 Data ingestion & normalization
- Convert formats (GeoJSON ⇄ Parquet, shapefiles, CSV → spatial)
- Validate geometry + CRS
- Generate derived layers (buffers, intersects, filters)

### 🧱 Tiles & web-ready outputs
- Produce web-friendly artifacts:
  - vector tiles (MBTiles/PMTiles)
  - raster tiles / COGs
  - tile metadata (TileJSON-like manifests)
- Keep outputs compatible with browser-first mapping stacks

### 🧠 Analysis helpers
- Feature engineering & summaries (fast)
- Graph computations (centrality, clustering, spectral-ish routines)
- Statistical primitives (only if clearly bounded and reproducible)

### 🌊 Streaming & sensor workloads
- Parse sensor/event feeds
- Windowed aggregations (time buckets, rolling stats)
- Emit append-only results + provenance logs

---

## 🧪 Reproducibility & scientific rigor checklist

When your Rust tool produces **analytical** or **simulation** outputs, include:

- ✅ **Verification** (did we build the thing right?)
- ✅ **Validation** (does output match reality / reference data where possible?)
- ✅ **Uncertainty quantification** (sensitivity / Monte Carlo / confidence intervals)
- ✅ **Experiment design metadata** (scenarios, seeds, run counts, timestep, etc.)

> [!IMPORTANT]
> If you can’t reproduce it from the run record + inputs, it’s not done.

---

## 🔒 Security & safe defaults

These tools will process untrusted files sometimes. Defaults should be safe:

- Avoid `unsafe` unless there’s a clear, benchmarked payoff
- Treat all inputs as hostile:
  - limit decompression bombs
  - validate JSON sizes
  - bound memory usage where possible
- Add CI checks:
  - `cargo audit`
  - dependency review (if available)
  - deny unknown licenses if needed

---

## 🧑‍💻 Adding a new Rust tool (starter workflow)

1) Create a crate (binary or library):
```bash
cd tools/rs
cargo new crates/<your-crate-name> --bin
```

2) Add a minimal CLI:
- `--help` with examples
- `--dry-run`
- `--emit-provenance`

3) Add a “contract test”:
- Golden file outputs (small fixtures)
- Deterministic ordering + stable formatting

4) Document in this README:
- one-line purpose
- examples
- outputs + artifacts

---

## 📚 Project library (why these tools are designed this way)

<details>
<summary><b>Click to expand 📦</b> (Project reference texts & docs)</summary>

### 🧭 KFM architecture & governance
- **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf**
- **Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf**
- **Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx**
- **Data Spaces.pdf** (architectures, services, adapters)

### 🌍 GIS, cartography, remote sensing, mapping UX
- **python-geospatial-analysis-cookbook.pdf**
- **PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf** (PostGIS + DB ops)
- **making-maps-a-visual-guide-to-map-design-for-gis.pdf**
- **Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf**
- **Archaeological 3D GIS_26_01_12_17_53_09.pdf**
- **Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf**
- **webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf**
- **responsive-web-design-with-html5-and-css3.pdf**
- **compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf**

### 📈 Statistics, modeling, simulation, inference
- **Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf**
- **Understanding Statistics & Experimental Design.pdf**
- **regression-analysis-with-python.pdf**
- **Regression analysis using Python - slides-linear-regression.pdf**
- **graphical-data-analysis-with-r.pdf**
- **think-bayes-bayesian-statistics-in-python.pdf**
- **Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf**
- **Generalized Topology Optimization for Structural Design.pdf**
- **Spectral Geometry of Graphs.pdf**
- **Principles of Biological Autonomy - book_9780262381833.pdf**

### 🧱 Systems, performance, concurrency
- **Database Performance at Scale.pdf**
- **Scalable Data Management for Future Hardware.pdf**
- **concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf**

### 🧑‍⚖️ Ethics, law, safety, security
- **Introduction to Digital Humanism.pdf**
- **On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf**
- **ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf**
- **Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf**

### 🧰 Programming reference library (compilations)
- **A programming Books.pdf**
- **B-C programming Books.pdf**
- **D-E programming Books.pdf**
- **F-H programming Books.pdf**
- **I-L programming Books.pdf**
- **M-N programming Books.pdf**
- **O-R programming Books.pdf**
- **S-T programming Books.pdf**
- **U-X programming Books.pdf**

</details>

---

## ✅ Definition of Done (for Rust tools)

- [ ] `cargo test` ✅
- [ ] `cargo fmt` ✅
- [ ] `cargo clippy` ✅ (warnings treated as errors)
- [ ] Tool has `--help` with at least **2 examples**
- [ ] Tool emits provenance artifacts (run record + manifest)
- [ ] Output is deterministic (stable ordering)
- [ ] Contract test(s) exist with small fixtures
- [ ] Docs updated (this README + crate-level README if needed)

---

### 🔗 Related
- 📁 `api/` (Python backend services)
- 🌐 `web/` (frontend + map UI)
- 🗂️ `data/` (raw/processed/catalog artifacts)

> [!NOTE]
> If you’re unsure whether something should be Rust or Python: default to **Python** unless performance, safety, portability, or determinism strongly argue for Rust. 🧠

