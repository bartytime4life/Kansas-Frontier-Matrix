> According to a document from **2025-11-13**, the Kansas Matrix System (KFM) runs on a **one-directional pipeline** (ETL → STAC/DCAT/PROV → Graph/DB → API → UI) and treats `tools/` as the governed place where that pipeline is executed, checked, and reproducibly rebuilt. ✅

<div align="center">

# 🛠️ `tools/` — Kansas Matrix System Toolbox

**Deterministic • Provenance-aware • CI-friendly • “Build it once, verify it forever”**

![Python](https://img.shields.io/badge/Python-3.11%2B-informational)
![Node](https://img.shields.io/badge/Node-18%2B-informational)
![Docker](https://img.shields.io/badge/Docker-Required%20for%20some%20tools-informational)
![STAC](https://img.shields.io/badge/STAC-Catalog%20%2B%20Items-blue)
![DCAT](https://img.shields.io/badge/DCAT-Metadata-blue)
![PROV](https://img.shields.io/badge/PROV-Run%20Records-blue)
![FAIR+CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Policy%20Aligned-success)
![MCP-DL](https://img.shields.io/badge/MCP--DL-v6.3-8A2BE2)

</div>

---

## 🧭 Quick navigation

- [What belongs in `tools/`](#-what-belongs-in-tools)
- [Core principles](#-core-principles)
- [Expected folder layout](#-expected-folder-layout)
- [Common workflows](#-common-workflows)
- [Validation & QA gates](#-validation--qa-gates)
- [Provenance, SBOM, and attestations](#-provenance-sbom-and-attestations)
- [Geo + mapping utilities](#-geo--mapping-utilities)
- [Contributing a new tool](#-contributing-a-new-tool)
- [📚 Project reference library (all project files)](#-project-reference-library-all-project-files)

---

## 🎯 What belongs in `tools/`

`tools/` is the **toolbox** for building and verifying KFM data products and runtime artifacts.

✅ Put here:
- **ETL + ingestion** CLIs (download → normalize → derive → stage)
- **Catalog generation** (STAC / DCAT) + **run records** (PROV)
- **Validators** (schema checks, link checks, expectations suites, policy tests)
- **Graph/DB loaders** (Neo4j, PostGIS, search indices)
- **Map/UI build helpers** (tiles, styles, overlays, story packaging)
- **Security + supply chain** tooling (SBOM generation, signing, policy enforcement)

🚫 Don’t put here:
- Long-lived services (APIs, daemons) — those live in app/runtime folders
- One-off local scripts with unclear inputs/outputs (promote them properly or keep them in a sandbox)
- Anything that can’t run non-interactively in CI

---

## 🧱 Core principles

### 1) Deterministic by default 🎲❌
Same inputs + same config + same versions ⇒ **same outputs** (byte-for-byte whenever feasible).

### 2) Idempotent & restartable 🔁
Re-running should not corrupt state. Tools should be safe to re-execute after interruption.

### 3) “Fail closed” quality gates 🚦
If a gate can’t prove correctness (schema, checksums, links, policy), it **fails**.

### 4) Provenance is a first-class artifact 🧬
Every pipeline run should emit:
- a **PROV run record** (JSON-LD recommended)
- **checksums** for outputs
- tool version + dependency fingerprints (ideally an SBOM reference)

### 5) Governance is executable ✅📜
FAIR + CARE alignment, licensing constraints, and security policy should be enforced via:
- validators
- OPA/Conftest policies
- CI workflows

---

## 📦 Expected folder layout

> This is the *canonical* layout described by the project design docs. If your repo differs, treat this as the target structure.

```text
tools/ 🧰
├── README.md 📘                # you are here
├── ingest/ 🧲                  # ingestion + ETL entrypoints
│   ├── ingest.py
│   └── requirements.txt
├── generate/ 🏗️                # metadata + catalog generators
│   ├── emit_stac_dcat_prov.js
│   └── templates/
├── id/ 🆔                       # deterministic ID + hashing utilities
│   └── compute.js
├── validation/ ✅               # fast, repeatable quality gates
│   ├── catalog_qa/             # STAC/DCAT quick gate
│   │   └── run_catalog_qa.py
│   ├── rego/                   # OPA policies (Konstraint, etc.)
│   ├── run_ge.py               # Great Expectations runner
│   └── stac-check.sh
├── graph/ 🧠                    # Neo4j loaders, graph QA
├── db/ 🗄️                       # PostGIS helpers, migrations, query packs
├── geo/ 🗺️                      # GDAL/WhiteboxTools helpers, reprojection, tiling
├── routing/ 🚗                  # routing graph/tile builds (e.g., Valhalla)
├── web/ 🌐                      # MapLibre/Cesium/WebGL build helpers
├── attest/ 🔏                   # provenance + signing helpers
└── policy/ 🛡️                   # high-level policy bundles (if separated from validation/)
```

---

## 🔁 Common workflows

### A) Ingest → stage → validate → catalog
**Goal:** turn raw sources into processed artifacts and metadata that can be loaded into graph/DB and served to UI.

Typical phases:
1) **Ingest** raw sources (download/collect)
2) **ETL** to normalized outputs (COG / Parquet / GeoJSON / JSON)
3) **Validate** structure + domain expectations + policy
4) **Generate** STAC + DCAT + PROV
5) **Load** graph/DB indices

Example (illustrative):
```bash
# 1) ingest & process (python)
python tools/ingest/ingest.py --help
python tools/ingest/ingest.py \
  --source "..." \
  --out "data/staging/processed/<dataset_slug>"

# 2) quick catalog QA gate (python)
python tools/validation/catalog_qa/run_catalog_qa.py \
  --root data/staging/processed/<dataset_slug>

# 3) Great Expectations suites (python)
python tools/validation/run_ge.py \
  --suite suites/<dataset_slug>.yml \
  --data  data/staging/processed/<dataset_slug>

# 4) generate catalog artifacts (node)
node tools/generate/emit_stac_dcat_prov.js \
  --in  data/staging/processed/<dataset_slug> \
  --out data/catalog/<dataset_slug>
```

---

### B) “Catalog QA quick gate” (STAC/DCAT health check) ⚡
This gate is designed to run quickly on PRs:
- STAC structure checks (Items/Collections)
- Link resolution and basic integrity checks
- Minimum required properties for KFM extensions (where applicable)

```bash
python tools/validation/catalog_qa/run_catalog_qa.py --help
```

---

### C) Policy enforcement (OPA/Conftest) 🛡️
For hard rules (licensing, required fields, prohibited patterns), use **Rego** policies and test them against the staged artifacts:

```bash
conftest test \
  -p tools/validation/rego \
  data/staging/processed/<dataset_slug> \
  --all-namespaces
```

---

### D) Graph/DB sync (Neo4j + PostGIS) 🧠🗄️
**PostGIS** powers spatial search and geometry operations; tools may rely on standard PostGIS primitives such as:
- `ST_Buffer(...)` for proximity envelopes
- `ST_Within(...)` for containment queries

**Neo4j** holds linked entities and relationships across sources. Graph loaders should:
- accept a **catalog root** (STAC as the discovery layer)
- produce a **load report** + QA summary

---

### E) Routing tiles build (Valhalla pattern) 🚗🧱
The design includes a reproducible routing build/serve setup (commonly Docker-based). Expect:
- a build container that produces tiles
- a serve container that exposes routing endpoints
- CI smoke tests to verify tile integrity

---

### F) Story Nodes / Focus Mode build chain 🧭✨
Tools may support:
- **Story Node** packaging (narrative + assets + overlays)
- **Focus Transformer** outputs (summaries, caches, derived references)
- **telemetry exports** (for auditability and UX iteration)

---

## ✅ Validation & QA gates

A good KFM toolchain has multiple “rings”:

### Ring 0: Structure
- JSON schema validation (STAC, DCAT, extensions)
- required files exist
- link resolution + media existence

### Ring 1: Semantics
- field ranges and units
- CRS/projection correctness
- geometry validity (self-intersections, empty geoms)
- time coverage sanity checks

### Ring 2: Domain expectations
- Great Expectations suites
- drift checks (histograms, quantiles, missingness)

### Ring 3: Governance & safety
- FAIR + CARE checks (metadata completeness, contact, license, sensitive fields)
- policy rules (OPA)
- security posture checks (secrets, dependency vulnerabilities)

---

## 🔏 Provenance, SBOM, and attestations

Tools should emit or reference:
- **PROV run record** (JSON-LD recommended)
- **SBOM** (for tool deps and/or produced artifacts)
- **signed attestations** for build outputs

### Minimal PROV run record (example shape)
```json
{
  "@context": ["https://www.w3.org/ns/prov.jsonld"],
  "type": "prov:Activity",
  "prov:startedAtTime": "2026-01-08T00:00:00Z",
  "prov:endedAtTime": "2026-01-08T00:05:00Z",
  "prov:used": ["<source_ref_1>", "<source_ref_2>"],
  "prov:generated": ["<output_ref_1>", "<output_ref_2>"],
  "kfm:checksums": {
    "<output_ref_1>": "sha256:...",
    "<output_ref_2>": "sha256:..."
  },
  "kfm:tool": {
    "name": "tools/ingest/ingest.py",
    "version": "<git_sha_or_semver>"
  }
}
```

> 💡 Tip: Keep provenance small, link out to full manifests, and store “heavy” logs in `reports/` or an artifact store.

---

## 🗺️ Geo + mapping utilities

This repo leans heavily into:
- **COG** (Cloud Optimized GeoTIFF) pipelines
- **vector/attribute** pipelines (GeoJSON / Parquet)
- **reprojection + standardization**
- **cartographic quality** (legends, color ramps, generalization, overlays)

Expected helpers in `tools/geo/` and `tools/web/`:
- CRS normalization + projection extension handling
- tile generation / packaging
- style linting (MapLibre style JSON rules)
- 3D asset prep (Cesium-friendly)

Also consider:
- image optimization utilities in `tools/images/` (PNG/JPEG/GIF/BMP/XBM cases)
- overlay validators: legends, attribution, alt text, and “safe-to-render” checks

---

## 🧩 Contributing a new tool

### ✅ “Definition of Done” for a tool
A tool is “real” when it has:
- an entrypoint (`.py`, `.js`, `.sh`, etc.) with `--help`
- documented **inputs/outputs**
- deterministic defaults (stable ordering, seeded randomness)
- structured logs (human + machine readable)
- emits a run record (or writes enough metadata to reproduce one)
- a CI target (even a lightweight smoke test)
- a clear home in the folder map

### Suggested tool interface contract
Every tool should support at least:
- `--help`
- `--version`
- `--input` / `--output` (or equivalent)
- `--config <file>`
- `--dry-run`
- `--log-json` (optional, but recommended)

### Tool manifest idea (recommended)
Add a `tool.yaml` next to complex tools:
- name, owner, inputs, outputs
- determinism notes
- resource hints (RAM/CPU)
- policy gates required
- references to schemas/expectations suites

---

## 📚 Project reference library (all project files)

> These files are treated as the *design + research shelf* for how our tools are built (modeling rigor, statistics, geospatial methods, web rendering, databases, governance, and security).  
> ⚠️ If the repo is public: confirm you have redistribution rights, or store large/third‑party PDFs in private storage / Git LFS.

<details>
<summary><strong>📖 Expand full library list</strong></summary>

### 🧪 Modeling, simulation, and verification
- **Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf** (model credibility, V&V, UQ)
- **Generalized Topology Optimization for Structural Design.pdf** (structural optimization workflows)
- **Spectral Geometry of Graphs.pdf** (graph analytics foundations)

### 📈 Statistics, experiments, and ML
- **Understanding Statistics & Experimental Design.pdf** (study design + inference discipline)
- **regression-analysis-with-python.pdf** (regression tool patterns + evaluation)
- **Regression analysis using Python - slides-linear-regression.pdf** (teaching/evaluation scaffolding)
- **think-bayes-bayesian-statistics-in-python.pdf** (Bayesian workflows for uncertain data)
- **Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf** (deep learning practice)

### 🗺️ Geospatial, cartography, and remote sensing
- **python-geospatial-analysis-cookbook.pdf** (PostGIS, overlays, routing, geodata pipelines)
- **making-maps-a-visual-guide-to-map-design-for-gis.pdf** (map design + cartographic choices)
- **Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf** (mobile map context + UX)
- **Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf** (GEE workflows + exports)

### 🧠 Data, databases, and architectures
- **PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf** (SQL + Postgres operations)
- **Scalable Data Management for Future Hardware.pdf** (throughput/perf patterns)
- **Data Spaces.pdf** (interoperability + data federation thinking)

### 🌐 Web, rendering, and media
- **responsive-web-design-with-html5-and-css3.pdf** (front-end build & responsive patterns)
- **webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf** (WebGL mental model + GPU rendering)
- **compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf** (media pipeline correctness)

### 🔐 Security (defensive use only)
- **ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf** (threat models + controls)
- **Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf** (reverse engineering context)

### 🧭 Governance, ethics, and society
- **Introduction to Digital Humanism.pdf** (value-sensitive design + responsibility)
- **Principles of Biological Autonomy - book_9780262381833.pdf** (systems/autonomy framing)
- **On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf** (legal/conceptual grounding)

### 🧰 Language & platform cookbooks
- **A programming Books.pdf**
- **B-C programming Books.pdf**
- **D-E programming Books.pdf**
- **F-H programming Books.pdf**
- **I-L programming Books.pdf**
- **M-N programming Books.pdf**
- **O-R programming Books.pdf**
- **S-T programming Books.pdf**
- **U-X programming Books.pdf**

### 📄 Project design docs
- **Kansas Frontier Matrix (KFM) – Comprehensive Engineering Design.docx**
- **Latest Ideas.docx**
- **Other Ideas.docx**

</details>

---

## 🧾 Metadata (KFM-MDP style)

```yaml
title: "tools/ — Kansas Matrix System Toolbox"
path: "tools/README.md"
version: "v0.1.0"
last_updated: "2026-01-08"
review_cycle: "90 days"
mcp_version: "MCP-DL v6.3"
governance: "FAIR + CARE aligned"
```

