# 🧬 KFM Pipelines  
`pipelines/README.md`

**Deterministic ETL → governed catalogs → graph ingestion → APIs → UI**  
The spine of Kansas Frontier Matrix (KFM). 🧠🗺️

![Status](https://img.shields.io/badge/status-active-brightgreen)
![Contract](https://img.shields.io/badge/pipeline%20contract-KFM--PDC%20v11-blue)
![STAC](https://img.shields.io/badge/metadata-STAC%20v11-7b42f6)
![DCAT](https://img.shields.io/badge/metadata-DCAT%20v11-7b42f6)
![PROV](https://img.shields.io/badge/provenance-PROV%20v11-7b42f6)
![Governance](https://img.shields.io/badge/governance-FAIR%2BCARE-orange)

</div>

---

## 🧭 Quick Links

- 🧠 Architecture context: `docs/architecture/` (and the KFM engineering design doc)  
- 🧾 Pipeline runbooks/specs: `docs/pipelines/`  
- 🧪 Pipeline code: `src/pipelines/`  
- 🧬 Graph ingestion + search contracts: `src/graph/` + `docs/search/`  
- 🧰 Shared pipeline utilities: `src/pipelines/_shared/`  

> KFM is explicitly pipeline-driven: data moves from ETL pipelines → metadata/catalogs → knowledge graph → APIs → UI & visualization. :contentReference[oaicite:0]{index=0}

---

## 🧱 The Non‑Negotiable Ordering (Governed)

> [!IMPORTANT]
> This ordering is not “architecture preference” — it’s the governance boundary.

1) **ETL (deterministic)**  
2) **Metadata catalogs (STAC / DCAT / PROV) + validation gates**  
3) **Graph ingestion (Neo4j) via controlled ingest paths**  
4) **APIs** expose data/search safely  
5) **UI** consumes APIs (not direct DB/graph)  
6) **Story Nodes → Focus Mode** (presentation + narrative layers)

This “ETL → catalog → graph → API → UI → story layers” ordering is treated as a governed constraint in the project docs. :contentReference[oaicite:1]{index=1}

---

## 🧬 What a “Pipeline” Means in KFM

A KFM pipeline is a **replayable builder** that takes raw inputs and produces:

- 📦 **Data artifacts** (COGs, Parquet, GeoJSON, tiles, CSV, etc.)
- 🗂️ **Catalog artifacts** (STAC collections/items; DCAT distributions)
- 🧾 **Provenance artifacts** (PROV entities/activities; run manifests)
- 🧷 **Integrity artifacts** (checksums + manifest inventory)
- 📊 **Telemetry** (for audit + performance + policy review)

This “builder” model (outputs + attestations + policy gates) is an explicit pattern in KFM’s governance/security notes. :contentReference[oaicite:2]{index=2}

---

## 🗺️ One Diagram to Rule Them All

```mermaid
flowchart LR
  A[🌐 Raw Sources] --> B[🧺 Ingest & Normalize]
  B --> C[✅ Validate & Quality Gates]
  C --> D[🗂️ STAC / DCAT Outputs]
  C --> E[🧾 PROV Lineage]
  D --> F[🧠 Graph Ingest (Neo4j)]
  F --> G[🛠️ APIs]
  G --> H[🗺️ UI + 3D/2D Map]
  H --> I[📖 Story Nodes]
  I --> J[🎯 Focus Mode]
```

---

## 📁 Where Things Live

The repository’s “spine” folders (pipelines, graph, UI, etc.) are explicitly mapped in KFM docs and guides. :contentReference[oaicite:3]{index=3}:contentReference[oaicite:4]{index=4}

```text
📁 pipelines/                     — THIS folder (pipeline portal + conventions)
📁 src/
├── 📁 pipelines/                 — ETL workflows and builders
│   ├── 📁 _shared/               — shared steps (catalog update, IO helpers, validators)
│   └── 📁 <domain>/<pipeline>/   — domain pipelines (soil, hydrology, hazards, climate, etc.)
├── 📁 graph/                     — graph ingest + query layer contracts
└── 📁 ui/                        — React + MapLibre/Cesium + story layers

📁 docs/
├── 📁 pipelines/                 — pipeline docs/runbooks + SLAs + contracts
├── 📁 standards/                 — governance, FAIR+CARE, sovereignty rules
└── 📁 schemas/                   — telemetry schemas, contract schemas, validation schemas
```

---

## ⚙️ Running Pipelines Locally

> [!NOTE]
> Commands below show the intended ergonomics. Prefer the project’s `Makefile` tasks when available.

### ✅ Recommended: `make` entrypoints

```bash
# list what exists (example)
make pipelines-list

# run a pipeline (example)
make pipeline RUN=soil/sda-weekly ENV=dev

# validate catalogs only (example)
make catalog-qa
```

### 🐍 Direct execution (Python module style)

```bash
python -m src.pipelines.soil.sda_weekly.run --env dev
python -m src.pipelines.hazards.refresh.run --since "2026-01-01T00:00:00Z"
```

### 🧱 Minimum env vars (typical)

| Variable | Purpose |
|---|---|
| `KFM_ENV` | `dev|stage|prod` |
| `KFM_DATA_ROOT` | working storage root |
| `KFM_STAC_ROOT` | STAC output root |
| `KFM_DCAT_ROOT` | DCAT output root |
| `KFM_PROV_ROOT` | provenance output root |
| `KFM_NEO4J_URI` | graph ingest endpoint (if enabled) |
| `KFM_TELEMETRY_ROOT` | run telemetry output root |

---

## 🧾 Pipeline Documentation Contract

Every pipeline SHOULD have a doc page under `docs/pipelines/<domain>/<pipeline>/README.md` including:

- 🎯 Purpose, scope, SLA cadence
- 🧺 Inputs (source URLs, datasets, access requirements)
- 🧪 Validation gates
- 🧷 Integrity model (hashing / manifests / idempotency)
- 🗂️ STAC/DCAT mapping
- 🧾 PROV lineage mapping
- 💥 Failure modes + replay rules + kill switch

A concrete example of this “doc metadata header” style is used across KFM docs. :contentReference[oaicite:5]{index=5}

---

## 🌾 Featured Pipelines & Patterns

> [!TIP]
> If you’re adding a new pipeline, match one of these patterns first.

### 1) 🌪️ Hazards Refresh (Full Refresh + Governed Ingest)

- **Type:** full refresh + incremental where supported  
- **Design:** “fully automated ETL pipeline,” with steps to detect stale data, fetch, normalize, build STAC, validate checksums, and sync into Neo4j on schedule or on-demand. :contentReference[oaicite:6]{index=6}
- **Tech notes:** mentions a YAML/LangGraph flow & automatic scheduling. :contentReference[oaicite:7]{index=7}

### 2) 💧 Hydrology ETL (Raster/Vector + Topology Validation)

- **Type:** classic geospatial ETL  
- **Tools:** explicitly references **GDAL + WhiteboxTools**, topology validation, and publishing **COG rasters + Parquet summaries** into a STAC Collection/Items. :contentReference[oaicite:8]{index=8}

### 3) 🌱 Soil Differential Updates (Delta + WAL + Idempotency)

- **Type:** differential updates (preferred for large tilesets)  
- **Core rule:** join on `(tile_id, src_checksum)` to detect new/changed tiles; log applied diffs to a WAL to support replay safety. :contentReference[oaicite:9]{index=9}
- **Ops rule:** pipeline emits tile-level deltas, then updates STAC and re-indexes. :contentReference[oaicite:10]{index=10}

### 4) 🌡️ Climate Basemap Exporter (STAC‑Heavy Publisher)

- **Type:** “exporter/publisher” that produces STAC collections/items with detailed asset typing (COG, Cloud‑optimized NetCDF, vector tiles), including STAC extension fields like `proj:epsg` and temporal coverage. :contentReference[oaicite:11]{index=11}

### 5) 🌬️ Air Quality Ingest (Conditional Fetch + Station‑Day Index)

- **Type:** incremental ingest (conditional GET)  
- **Pattern:** use `ETag`/`Last-Modified`, normalize to a station‑centric schema, create **STAC items per station‑day**, and emit PROV lineage. :contentReference[oaicite:12]{index=12}

---

## ✅ Quality Gates (What “Done” Means)

A pipeline is “done” only when the following are true:

- ✅ **Schema-valid** outputs (domain schemas + STAC validation)
- ✅ **Catalog QA passes** (links, assets, projections, time ranges, etc.)
- ✅ **Integrity checks** (checksums in manifests; optional sidecars)
- ✅ **Telemetry emitted** (run summary + timing + gate outcomes)
- ✅ **Policy gates visible** (FAIR+CARE / sovereignty outcomes recorded)

KFM docs explicitly treat provenance/telemetry as governance outputs. :contentReference[oaicite:13]{index=13}

### Local test patterns

Some KFM docs/patterns include targeted validation tasks (example: hydrology legends) to ensure metadata correctness. :contentReference[oaicite:14]{index=14}

```bash
# example style used in docs
make test-legends-hydrology
make test-legends-climate
```

---

## 🔭 Performance & Scaling Playbook

When pipelines grow, we scale in **chunks** and **breakers**:

- 📦 **Chunked execution / morsels** for parallel processing
- 🧱 **Pipeline breakers** where materialization is necessary
- 🔁 **Replay safety** (idempotency keys + WAL)
- 🧊 **Caching** where outputs are reused

These patterns align with modern “push-based / morsel-driven / task pool” execution approaches described in the scalable data management literature. :contentReference[oaicite:15]{index=15}

---

## 🔐 Security & Governance (Pipelines Are Part of the Threat Model)

Pipelines touch external data + dependencies, so they are governed like production services:

- 🔒 Prefer policy-gated promotion (builders + attestations + policy checks)  
- 🧾 Maintain **SBOM + manifest + attestations** for governed releases  
- ✍️ Sign artifacts where feasible (cosign/sigstore patterns)  

KFM’s supply-chain and release artifact expectations are spelled out as normative guidance in project notes. :contentReference[oaicite:16]{index=16}

Also: graph/search layers must be safe-by-design:
- no unbounded traversals
- parameterized queries
- deterministic ordering + limits
- no sensitive leakage

These are explicitly written as “non-negotiables (governed)” in KFM docs. :contentReference[oaicite:17]{index=17}

---

## 🧩 Adding a New Pipeline

> [!TIP]
> Start with a template and keep the first version boring and deterministic.

### ✅ Checklist

- [ ] Pick a **domain** (`soil`, `hydrology`, `hazards`, `climate`, `air_quality`, …)
- [ ] Create code folder: `src/pipelines/<domain>/<pipeline_name>/`
- [ ] Define outputs & schemas first (what does “correct” look like?)
- [ ] Implement ingest + normalization (deterministic)
- [ ] Add STAC/DCAT/PROV emitters
- [ ] Add integrity (checksums, manifest, idempotency)
- [ ] Add tests + QA targets
- [ ] Add docs page: `docs/pipelines/<domain>/<pipeline_name>/README.md`
- [ ] Wire into scheduler/orchestrator (if applicable)
- [ ] Ensure graph ingest is downstream of catalog validation

### 🧱 Suggested skeleton

```text
src/pipelines/<domain>/<pipeline_name>/
├── run.py
├── pipeline.yml
├── config/
├── schemas/
├── validators/
├── tests/
└── README.md (developer-facing)
```

---

## 📚 Project Library Index (Used to Inform Pipeline Standards)

These project files are part of the **shared “pipeline brain”** — use them as design references when building new workflows.

### 🛰️ Geospatial & Mapping
- 📘 *Python Geospatial Analysis Cookbook* — PostGIS, overlays, routing, web mapping patterns  
- 🗺️ *Making Maps: A Visual Guide to Map Design for GIS* — cartography, legend design, perceptual rules  
- 📱 *Mobile Mapping: Space, Cartography and the Digital* — field/mobile constraints & UX  
- 🌍 *Cloud-Based Remote Sensing with Google Earth Engine* — scalable remote sensing ETL patterns  
- 🧊 *Compressed Image File Formats (JPEG/PNG/GIF/BMP…)* — imagery ingestion + storage strategy  

### 🧪 Modeling, Simulation, Optimization
- 🚀 *Scientific Modeling & Simulation (NASA‑grade guide)* — verification/validation, uncertainty discipline  
- 🧱 *Generalized Topology Optimization for Structural Design* — optimization workflows & constraints  
- 🧩 *Spectral Geometry of Graphs* — graph metrics/embeddings intuition (graph QA + analytics)  

### 📈 Statistics, ML, and Validation
- 📉 *Regression Analysis with Python* + 📊 *(Slides)* — diagnostics, assumptions, robust modeling  
- 🧪 *Understanding Statistics & Experimental Design* — proper validation, measurement design  
- 🎲 *Think Bayes* — uncertainty, posterior thinking for risk scoring  
- 📊 *Graphical Data Analysis with R* — EDA, QC plots, anomaly spotting  
- 🧠 *Understanding Machine Learning (Theory → Algorithms)* — model governance, generalization sanity

### 🗄️ Data Systems & Scaling
- 🧱 *PostgreSQL Notes for Professionals* — operational SQL patterns, tuning, reliability  
- 🧩 *Data Spaces* — federation + sharing + interoperability patterns  
- ⚡ *Scalable Data Management for Future Hardware* — pipelines, task pools, compilation, throughput

### 🌐 UI / Web / 3D
- 🧑‍🎨 *Responsive Web Design with HTML5 & CSS3* — frontend ergonomics for map UIs  
- 🧊 *WebGL Programming Guide* — GPU-accelerated layers, 3D storytelling

### 🔐 Security, Safety, and Governance
- 🛡️ *Ethical Hacking & Countermeasures* — threat modeling for data services/pipelines  
- 🐍 *Gray Hat Python* — secure tooling awareness (defensive posture)  
- 🧵 *Concurrent Real‑Time & Distributed Programming in Java* — concurrency patterns (when needed)  
- ⚖️ *AI Law’s Prophecies…* — governance framing for ML + decision systems

### 🧭 Human Systems & Ethics
- 🌱 *Principles of Biological Autonomy* — resilience thinking, adaptive systems metaphors  
- 🤝 *Introduction to Digital Humanism* — human-centered governance and accountability

### 📚 Language & Reference Collections (Quick Lookup)
- 🧷 `A programming Books.pdf`  
- 🧷 `B-C programming Books.pdf`  
- 🧷 `D-E programming Books.pdf`  
- 🧷 `F-H programming Books.pdf`  
- 🧷 `I-L programming Books.pdf`  
- 🧷 `M-N programming Books.pdf`  
- 🧷 `O-R programming Books.pdf`  
- 🧷 `S-T programming Books.pdf`  
- 🧷 `U-X programming Books.pdf`  

---

## 🧾 Source Anchors Used for This README

- Pipeline-driven KFM flow (ETL → catalogs → graph → APIs → UI): :contentReference[oaicite:18]{index=18}  
- Governed “non-negotiable ordering”: :contentReference[oaicite:19]{index=19}  
- Repo layout & key folders (`src/pipelines/`, `src/graph/`, etc.): :contentReference[oaicite:20]{index=20}  
- Hazards refresh pipeline design notes: :contentReference[oaicite:21]{index=21}  
- Hydrology ETL (GDAL + WhiteboxTools, STAC outputs): :contentReference[oaicite:22]{index=22}  
- Soil differential update mechanics (tile checksum join + WAL): :contentReference[oaicite:23]{index=23}  
- Air quality ingest flow (ETag/Last‑Modified, station‑day STAC + PROV): :contentReference[oaicite:24]{index=24}  
- Release artifacts, manifests/SBOM/attestations, policy-gated promotion: :contentReference[oaicite:25]{index=25}  
- Scaling note (morsel/task-pool, push-based pipelines): :contentReference[oaicite:26]{index=26}  

---

<div align="center">

**© 2026 Kansas Frontier Matrix** · CC‑BY 4.0 (project docs)  
🧬 FAIR+CARE · 🪶 Sovereignty-aware · 🛡️ Policy-gated builds

</div>

