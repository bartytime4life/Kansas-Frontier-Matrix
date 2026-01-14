# 🦀 tools/rs — Rust Tooling for Kansas Frontier Matrix (KFM)

<p align="center">
  <img alt="Rust" src="https://img.shields.io/badge/Rust-stable-000000?logo=rust&logoColor=white">
  <img alt="Cargo" src="https://img.shields.io/badge/Built%20with-Cargo-3b2f2f?logo=rust&logoColor=white">
  <img alt="Deterministic" src="https://img.shields.io/badge/Deterministic-outputs-success">
  <img alt="Provenance First" src="https://img.shields.io/badge/Provenance-first-blue">
  <img alt="Geo" src="https://img.shields.io/badge/Geo-GIS%20%2B%20Remote%20Sensing-2b8a3e">
  <img alt="Safe Defaults" src="https://img.shields.io/badge/Security-safe%20defaults-orange">
  <img alt="Ports & Adapters" src="https://img.shields.io/badge/Architecture-ports%20%26%20adapters-6f42c1">
</p>

<p align="center">
  <b>High-performance, reproducible Rust utilities</b> for geospatial ingest, transforms, tiling, streaming, and analysis — designed to plug cleanly into KFM’s <b>provenance-first</b> + <b>clean architecture</b> pipeline. 🌾🗺️
</p>

---

## 🧭 Quick nav

- [✨ What lives in `tools/rs/`](#-what-lives-in-toolsrs)
- [🧱 Non-negotiables](#-non-negotiables)
- [🧬 KFM pipeline placement](#-kfm-pipeline-placement)
- [📑 Data + metadata contracts](#-data--metadata-contracts)
- [🧰 CLI contract](#-cli-contract)
- [🚀 Quick start](#-quick-start)
- [🧪 Testing strategy](#-testing-strategy)
- [🔁 Reproducible builds](#-reproducible-builds)
- [⚡ Performance at scale](#-performance-at-scale)
- [🔒 Security defaults](#-security-defaults)
- [🧑‍⚖️ Ethics & governance](#-ethics--governance)
- [🧑‍💻 Adding a new Rust tool](#-adding-a-new-rust-tool)
- [📦 Workspace layout](#-workspace-layout)
- [✅ Definition of Done](#-definition-of-done-for-rust-tools)
- [📚 Project library](#-project-library-why-these-tools-are-designed-this-way)
- [🔗 Related](#-related)

---

## ✨ What lives in `tools/rs/`

This folder is the **Rust sidecar** for KFM: small, sharp, composable tools that are easiest to do in Rust because we want:

- ⚡ **Speed + memory safety** (big rasters, big vectors, big graphs)
- 🔁 **Determinism + reproducibility** (stable outputs, stable ordering, stable provenance)
- 🧩 **Portability** (CLI binaries, containers, and optionally WASM modules)
- 🧾 **Provenance-first outputs** (metadata + citations are first-class artifacts)
- 🧱 **Clean architecture boundaries** (Rust as adapters/accelerators, not domain “truth”)

> [!NOTE]
> The “source of truth” for platform architecture remains KFM’s governed docs. Rust tools should **not** re-implement business rules already defined elsewhere — they should accelerate well-defined tasks behind clean interfaces. 🧼

---

## 🧱 Non-negotiables

### 1) Provenance-first by default 🧾
Every Rust tool MUST be able to explain:

- ✅ **what went in** (inputs + versions + hashes)
- ✅ **what happened** (steps + parameters + environment)
- ✅ **what came out** (artifacts + checksums + schema)
- ✅ **how to reproduce** (exact command + config + seeds)

Practical rules:

- Always emit a **machine-readable run record** (JSON/JSONL) alongside outputs.
- Always emit an **artifact manifest** (file list + hashes).
- Prefer **content addressing** (hashes) and **stable identifiers** for generated artifacts.
- Keep **metadata & citations next to the data** (don’t bury truth in logs).

> [!TIP]
> Treat provenance like a **data product**, not a debug feature.

---

### 2) Pipeline ordering is absolute 🧱➡️🗂️➡️🕸️➡️🧠➡️🖥️
KFM has a strict pipeline invariant:

**ETL → Catalogs (STAC/DCAT/PROV) → Graph → API → UI → Story Nodes → Focus Mode**

Rust tools live primarily in:
- 🧱 **ETL/processing**
- 🗂️ **Catalog/metadata generation + validation**
- 🌊 **Ingest/stream normalization**

Rust tools MUST NOT:
- ❌ publish anything to the graph/UI without catalog + provenance
- ❌ embed “story” narrative as if it were data truth
- ❌ bypass the governed API boundary (UI never hits the graph directly)

> [!IMPORTANT]
> If it isn’t cataloged + provenanced, it doesn’t exist (for KFM). ✅

---

### 3) Deterministic + idempotent transformations 🔁
KFM tools must behave like “rerunnable science”:

- Same inputs + same config + same seed ⇒ **bitwise-stable outputs** (where feasible)
- Re-running a pipeline should be **safe** (no surprise mutations; avoid side effects)

**Do this:**
- Stable sorting of features/rows
- Canonical JSON output (sorted keys, consistent formatting)
- Explicit RNG seeding (`--seed`, recorded in provenance)
- Explicit CRS/units/timezones (never “guess”)

---

### 4) Stable identifiers (meaning-free) 🆔
Identifiers are **not a place to store meaning**. Avoid IDs that embed “Kansas-2026-County-05”.

Recommended patterns:
- **Dataset IDs**: stable, human-friendly slug + version (in catalog)
- **Artifact IDs**: hash-based (sha256/blake3) for content addressing
- **Run IDs**: UUIDv7 (time-sortable) or hash of (inputs+params+tool version)

> [!TIP]
> A name can change. A stable ID shouldn’t.

---

### 5) Clean boundaries (ports & adapters) 🧩
Rust tools should behave like **well-bounded components**:

- Minimal assumptions about infrastructure
- Explicit inputs/outputs
- Replaceable backends (filesystem vs object storage, PostGIS vs files, etc.)
- Data contracts > “magic behavior”

If you’re adding a new feature, ask:

**Is this domain logic, or a tool adapter/accelerator?**  
If it’s domain logic, it likely belongs outside `tools/rs`.

---

### 6) Human-centered + accountable outputs 🤝
KFM’s ethos: tools should **augment human understanding**, not obscure it.

- Make outputs inspectable (small summaries, optional `.report.md`)
- Make failure modes clear (structured errors)
- Prefer explainable diagnostics over “it failed” logs

---

## 🧬 KFM pipeline placement

Rust tools are “engines” that produce **governed artifacts** for the rest of the system.

### 🧱 ETL + Processing
- Convert formats (GeoJSON ⇄ GeoParquet, Shapefile/GPKG → Parquet)
- Validate geometry + CRS
- Produce derived layers (buffers, intersects, filters)
- Compute dataset stats for cataloging (bbox, counts, min/max, histograms)

### 🗂️ Catalog + provenance
- Generate/update STAC/DCAT metadata
- Emit PROV lineage records (or a KFM run record that can be mapped to PROV)
- Validate license + schema compliance before publish

### 🕸️ Graph pre-ingest helpers
- Produce normalized node/edge tables (CSV/Parquet) for graph ingestion jobs
- Never “write to graph directly” from Rust (keep the boundary clean)

### 🧠 Analysis accelerators (bounded)
- Feature engineering primitives
- Graph computations (centrality, clustering, spectral-ish routines)
- Statistical primitives (only when scoped + reproducible)

### 🌊 Streaming & sensor workloads
- Parse sensor/event feeds
- Windowed aggregations (time buckets, rolling stats)
- Emit append-only results + provenance logs

---

## 📑 Data + metadata contracts

### Preferred data formats (KFM-friendly) 📦
Pick formats that scale, stream, and validate:

- 🧊 **Vectors (large):** GeoParquet / Parquet (+ Geo metadata)
- 🗺️ **Vectors (small):** GeoJSON (debug/samples only)
- 🧱 **Rasters:** Cloud-Optimized GeoTIFF (COG)
- 🧩 **Tiles:** PMTiles / MBTiles (vector tiles) + TileJSON-like metadata
- 🧾 **Tabular/time series:** Parquet (preferred), CSV (ingest-only), JSONL (events)
- 🧠 **Graph interchange:** edge/node tables in Parquet/CSV with stable IDs

> [!NOTE]
> “Small and friendly” formats (GeoJSON, CSV) are great for fixtures/tests — not for canonical big data outputs.

---

### Standard artifacts (every tool output) 🧾
Alongside primary outputs, generate:

| Artifact | Purpose |
|---|---|
| `*.run.json` or `*.prov.json` | machine-readable run record (inputs → steps → outputs) |
| `*.manifest.json` | artifact list + hashes + sizes |
| `*.report.md` (optional) | human-readable summary + sanity checks |
| `*.stac.json` / catalog entry (when applicable) | dataset discoverability + governance fields |

---

### Provenance run record (recommended schema) 🧾
Keep it boring and predictable. Example:

```json
{
  "run_id": "01J2ZK0YH9GQ8K2K3Z3E6J2C9A",
  "tool": {
    "name": "kfm-geo-convert",
    "version": "0.3.0",
    "git_commit": "abc1234",
    "rustc": "stable",
    "target": "x86_64-unknown-linux-gnu"
  },
  "started_at": "2026-01-14T18:22:10Z",
  "ended_at": "2026-01-14T18:22:14Z",
  "command": ["kfm-geo-convert", "--input", "raw/roads.gpkg", "--output", "processed/roads.parquet"],
  "config": { "path": "pipelines/roads/config.toml", "sha256": "..." },
  "inputs": [
    { "path": "raw/roads.gpkg", "sha256": "...", "media_type": "application/geopackage+sqlite3" }
  ],
  "parameters": {
    "crs_out": "EPSG:4326",
    "stable_sort": true
  },
  "outputs": [
    { "path": "processed/roads.parquet", "sha256": "...", "role": "primary" },
    { "path": "processed/roads.manifest.json", "sha256": "...", "role": "manifest" }
  ],
  "stats": { "features": 124812, "bbox": [-101.2, 36.9, -94.6, 40.0] },
  "warnings": [],
  "errors": []
}
```

> [!TIP]
> If your run record can’t recreate the run, it’s a log — not provenance. 🧾

---

### Naming + versioning conventions 🏷️
- Prefer `dataset_id` + `version` in filenames and directories
- Record all versions in metadata:
  - tool version
  - schema version
  - dataset version
  - source version (URL + retrieval date + hash when possible)

Examples:
- `data/processed/<dataset_id>/<version>/...`
- `data/catalog/<dataset_id>/<version>.json`
- `data/prov/<dataset_id>/<version>/<run_id>.run.json`

---

## 🧰 CLI contract

Even if we have multiple binaries, they should feel consistent.

### Standard flags
- `--input <path|url>`
- `--output <path>`
- `--config <path>` (✅ default: **TOML**)
- `--format <...>` (geojson / parquet / gpkg / pmtiles / mbtiles / cog / …)
- `--dry-run` (prints plan + expected artifacts)
- `--emit-provenance <path|dir>` (or emit by default next to output)
- `--seed <u64>` (if randomness exists at all)
- `--threads <n>` (only if parallelism affects determinism; otherwise auto)

### Standard exit behavior
- `0` success
- Non-zero for validation failures, missing inputs, or runtime errors
- Errors MUST be structured and actionable (print “what + how to fix”)

### Output expectations
- `--help` contains:
  - one-line purpose
  - at least **2 examples**
  - artifact list (“what files will be written”)

---

## 🚀 Quick start

### ✅ Prereqs
- Rust toolchain (stable): `rustup` + `cargo`
- (Optional) native deps depending on chosen crates:
  - GDAL/PROJ (if linking)
  - GEOS (if using GEOS-backed ops)
  - Postgres client libs (if connecting to PostGIS)

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

### 🔍 Supply chain + license checks (recommended)
```bash
cargo audit
# Optional (if adopted):
# cargo deny check
# cargo vet
```

### 📦 Install a local tool (example)
```bash
cargo install --path tools/rs/crates/<crate-name>
```

---

## 🧪 Testing strategy

Rust tools touch real-world messy data. Test like it.

### ✅ Required test layers
- **Unit tests**: pure logic, parsing, normalization
- **Integration tests**: run CLI against `fixtures/`
- **Contract/golden tests**: compare outputs to checked-in “goldens”
- **Property tests** (optional but strong): geometry invariants, round-trips
- **Fuzzing** (recommended for parsers): `cargo fuzz` for untrusted inputs
- **Benchmarks** (when performance matters): `cargo bench` + dataset notes

> [!IMPORTANT]
> Golden tests must be deterministic. If floating point or parallelism causes drift, fix it or record it explicitly.

---

## 🔁 Reproducible builds

### Build reproducibility
- Commit `Cargo.lock` for binaries (workspace policy)
- Prefer `cargo build --locked` in CI
- Record `git_commit`, tool version, target triple in `--version` output
- Consider `--remap-path-prefix` for path-stable builds (advanced)

### Runtime reproducibility
- Stable ordering for any collection output
- Canonical serialization for JSON
- Explicit CRS and axis order (never “guess”)
- Explicit seed handling
- Capture environment details in provenance

---

## ⚡ Performance at scale

Rust is here because “fast enough” matters — but only if it stays correct.

### Practical performance rules
- Stream I/O (don’t load entire datasets unless required)
- Chunked processing for rasters and very large vectors
- Use columnar formats (Parquet/Arrow) for scan-heavy work
- Avoid row-by-row DB patterns:
  - batch inserts
  - COPY when appropriate
  - use indexes intentionally (and measure)

### Parallelism without nondeterminism
- Parallelize **pure** workloads where ordering doesn’t matter
- If you must reduce floats in parallel:
  - use stable reduction strategies
  - document acceptable tolerance
  - record it in run record

### “Future hardware” mindset 🧠⚙️
Design tools so we can adopt:
- more cores / SIMD
- persistent memory / new storage tiers
- JIT compilation for hot query paths (where justified)
- GPU acceleration (via separate adapter/service if needed)

---

## 🔒 Security defaults

These tools will process untrusted files. Default posture: **assume hostile input**.

- Avoid `unsafe` unless benchmarked + reviewed
- Validate sizes/limits:
  - decompression bombs (ZIP, TIFF, PNG)
  - JSON depth/size
  - geometry complexity (self-intersections, pathological rings)
- Safe path handling:
  - never overwrite unless `--force`
  - write temp → fsync → atomic rename
- Add CI checks (recommended):
  - `cargo audit`
  - dependency review
  - license allowlist/denylist

> [!TIP]
> Parsers are attack surfaces. Fuzz them.

---

## 🧑‍⚖️ Ethics & governance

KFM’s “digital humanism” stance means:
- We favor transparency over opacity
- We avoid black-box automation in high-stakes contexts
- We preserve accountability (who ran what, when, on which evidence)

Rust tooling implications:
- Never emit “authoritative interpretations” without evidence references
- Prefer **evidence-first outputs** (data + provenance), not narrative claims
- When tools compute model outputs:
  - document limitations
  - include uncertainty where feasible
  - make assumptions explicit in metadata/report

---

## 🧑‍💻 Adding a new Rust tool

1) Create a crate (binary or library):

```bash
cd tools/rs
cargo new crates/<your-crate-name> --bin
```

2) Implement the **KFM contract**:
- `--help` with examples
- `--dry-run`
- deterministic output
- run record + manifest

3) Add tests:
- fixtures (small)
- golden outputs
- CI-friendly runtime (fast)

4) Document:
- one-line purpose
- examples
- input/output formats
- artifacts emitted

> [!NOTE]
> Default to **Python** unless performance, portability, safety, or determinism strongly argue for Rust. 🧠

---

## 📦 Workspace layout

> If the repo already has a Rust layout, follow it. If not, this is the recommended default.

```text
tools/rs/ 🦀
├─ 🧰 Cargo.toml                    # workspace manifest
├─ 🧷 rust-toolchain.toml           # pinned toolchain (recommended)
├─ 📦 crates/                       # Rust crates live here
│  ├─ 🧭 kfm-cli/                   # unified CLI (optional)
│  ├─ 🧾 kfm-prov/                  # run records + manifests + hashing + IDs
│  ├─ 🗂️ kfm-catalog/               # STAC/DCAT helpers + metadata validation
│  ├─ 🌍 kfm-geo/                   # vector/raster utilities + conversions
│  ├─ 🧱 kfm-tiles/                 # PMTiles/MBTiles/COG/tiling helpers
│  ├─ 🌊 kfm-stream/                # sensor/event ingestion + windowing
│  ├─ 🕸️ kfm-graph/                 # graph analytics helpers (optional)
│  └─ 🧪 kfm-sim/                   # simulation + VVUQ helpers (optional)
├─ 🧪 fixtures/                     # small test datasets (never huge)
├─ 📐 schemas/                      # JSON schemas / contracts (optional, recommended)
└─ 📘 README.md                     # you are here
```

---

## 🧪 Reproducibility & scientific rigor checklist

When your Rust tool produces **analytical** or **simulation** outputs, include:

- ✅ **Verification** (did we build the thing right?)
- ✅ **Validation** (does output match reality / reference data where possible?)
- ✅ **Uncertainty quantification** (sensitivity / Monte Carlo / confidence intervals)
- ✅ **Experiment design metadata** (scenarios, seeds, run counts, timestep, etc.)
- ✅ **Graph + catalog compatibility** (results are ingestible and evidence-linked)

> [!IMPORTANT]
> If you can’t reproduce it from the run record + inputs, it’s not done.

---

## ✅ Definition of Done for Rust tools

- [ ] `cargo test` ✅
- [ ] `cargo fmt` ✅
- [ ] `cargo clippy` ✅ (warnings treated as errors)
- [ ] Tool has `--help` with at least **2 examples**
- [ ] Deterministic outputs (stable ordering)
- [ ] Tool emits provenance artifacts (run record + manifest)
- [ ] Contract test(s) exist with small fixtures
- [ ] Security checks considered (`cargo audit` minimum)
- [ ] Docs updated (this README + crate README if needed)

---

## 📚 Project library (why these tools are designed this way)

<details>
<summary><b>Click to expand 📦</b> (Project reference texts & docs)</summary>

### 🧭 KFM architecture, standards, governance
- **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf**
- **MARKDOWN_GUIDE_v13.md.gdoc** (pipeline invariants, governed docs structure, evidence-first rules)
- **Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx**
- **Data Spaces.pdf** (ports/adapters, microservices, data ecosystems)

### 🌍 GIS, cartography, remote sensing, mapping UX
- **python-geospatial-analysis-cookbook.pdf**
- **PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf** (PostGIS + DB ops)
- **Database Performance at Scale.pdf** (workload patterns + performance strategy)
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
- **Generalized Topology Optimization for Structural Design.pdf**
- **Spectral Geometry of Graphs.pdf**
- **Understanding Machine Learning: From Theory to Algorithms.pdf**

### 🧱 Systems, performance, concurrency
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

## 🔗 Related

- 📁 `api/` (Python backend services)
- 🌐 `web/` (frontend + map UI)
- 🗂️ `data/` (raw/processed/catalog artifacts)
- 🧾 `docs/standards/` (metadata profiles & governance, if present)

> [!TIP]
> When in doubt: keep Rust tools small, explicit, testable, and provenance-complete. 🌾🧾
