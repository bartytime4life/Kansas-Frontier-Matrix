# 🆔 KFM `tools/id` — Stable Identifiers & Provenance Anchors

![Status](https://img.shields.io/badge/status-draft-blue)
![Scope](https://img.shields.io/badge/scope-cross--stack%20IDs%20%2B%20provenance-informational)
![Philosophy](https://img.shields.io/badge/provenance-first-success)
![Design](https://img.shields.io/badge/clean--architecture-aligned-8A2BE2)

> [!IMPORTANT]
> **IDs are not just primary keys.** In KFM, they’re the *anchors* that make maps, datasets, models, and AI outputs **searchable, auditable, and reproducible** across time.

---

## 🧭 Why this tool exists

Kansas Frontier Matrix (KFM) treats **citations + metadata as first-class** and keeps every dataset/layer/answer **traceable to sources and processing steps**. This only works if every “thing” can be referenced with a **stable identifier** that doesn’t change when names, schemas, vendors, or UIs change.

This tool standardizes:

- ✅ **Stable identity** for core entities (parcels, features, people, events, maps, sensors, models…)
- ✅ **Provenance linking** (sources ↔ transformations ↔ artifacts ↔ outputs)
- ✅ **Cross-language & cross-service interop** (frontend, backend, pipelines, CLI)
- ✅ **Performance-aware storage** (DB indexing, distributed ingestion)
- ✅ **Security-aware exposure** (public APIs shouldn’t leak enumerability)

---

## 🧱 Design principles

### 1) Identity ≠ Meaning
Stable identifiers should be **unique, invariant, and “meaningless”** (no embedded business semantics). Names and codes belong in *attributes*, not in *IDs*.

### 2) Separate internal IDs from external IDs
External systems (archives, agencies, sensors, vendors, legacy databases) have their own IDs. **We never trust them as our system’s identity.**  
We store them as **external references** mapped to internal stable IDs.

### 3) Provenance-first by default
Every derived artifact must know:
- which inputs it came from
- which pipeline/version produced it
- what parameters + environment were used
- when it was produced
- what its content hash is (optional but recommended)

### 4) Deterministic IDs for derived artifacts (when it helps)
Some objects are best identified by **content** or **recipe** (hash-based), not by “first time created.”

### 5) Cross-boundary compatibility
IDs must work across:
- 🗺️ GIS formats (GeoJSON / vector tiles / rasters / STAC-like metadata)
- 🧪 modeling & simulation pipelines
- 🧠 ML experiment tracking
- 🧰 CLIs + scripting (Bash)
- 🌐 UI + WebGL visualization assets

---

## 🧩 What “needs an ID” in KFM

<details>
<summary><strong>📌 Expand: KFM ID coverage map</strong></summary>

### 🗺️ Geospatial + Archives
- `layer_id` — map layer identity (vector/raster/tiles)
- `feature_id` — stable identity per feature (not just row index)
- `map_scan_id` — scanned historical map asset
- `georef_job_id` — georeferencing run
- `annotation_id` — human notes, OCR corrections, digitized traces

### 📡 Sensors + Time Series
- `sensor_id` — device identity
- `reading_id` — observation identity (often derived)
- `stream_id` — logical data stream identity

### 🧪 Modeling + Simulation
- `sim_run_id` — run identity for reproducibility
- `model_id` — model identity (code + weights + version)
- `mesh_id` / `graph_id` — structural objects used in computation

### 🧠 ML / Stats / Experiments
- `dataset_id` — logical dataset identity
- `dataset_version_id` — immutable version identity
- `experiment_id` — experiment tracking (hyperparams, splits, seeds)
- `result_id` — derived outputs (plots, reports, metrics)

### 🌐 Frontend + UX
- `ui_ref_id` — stable references used for deep links, map selections, permalinks
- `asset_id` — WebGL textures/meshes/shaders if persisted/cached

</details>

---

## 🧪 ID taxonomy

| ID Type | Purpose | Characteristics | Example Use |
|---|---|---|---|
| **Opaque ID** | Pure identity | random, non-meaningful, non-guessable | Entity primary keys |
| **Sortable ID** | Identity with rough ordering | time-sortable; may leak creation time | ingestion pipelines, logs |
| **Derived ID** | Identity from content/recipe | deterministic; same input ⇒ same ID | artifacts, cached computations |
| **External Ref** | Link to outside system | *not* stable; stored as data | archive catalog numbers |
| **Run/Trace ID** | Reproducibility & audit | ties artifacts to execution | simulations, ML runs |

---

## 🧾 Canonical string formats

### ✅ Recommended: KFM URN wrapper
Use a URI/URN-like wrapper when IDs cross boundaries (API, files, exports):

```text
urn:kfm:<kind>:<id>
```

Examples:
```text
urn:kfm:layer:01J4K9J0Z9V8KX2J6P2J0G8N1Q
urn:kfm:dataset:6b4a6f6f-8d47-4b22-9df8-2dbd9fe8c82b
urn:kfm:run:01J4K9R8T4YB9E7E2XQWQ3P6H0
```

### `<kind>` conventions
Prefer a tight, controlled vocabulary:
- `layer`, `feature`, `map`, `scan`, `sensor`, `reading`, `dataset`, `artifact`, `run`, `model`, `person`, `event`, `place`, `citation`

> [!TIP]
> Keep `<kind>` stable. If you rename a domain concept, alias it—but don’t break IDs in the wild.

---

## 🧠 Strategy selection guide

> [!NOTE]
> This tool supports multiple strategies. Choose per domain *intentionally*.

### Opaque IDs (default)
Use when:
- ID is exposed publicly
- you need “meaningless” identity
- security + non-enumerability matters

Common options:
- UUIDv4
- random 128-bit IDs

### Sortable IDs
Use when:
- you ingest a lot of records and care about index locality
- you need rough chronological ordering by ID
- the ID is mostly internal (or you accept timestamp leakage)

Common options:
- ULID
- UUIDv7 (if your stack supports it)

### Derived IDs
Use when:
- you want deduplication (same content → same ID)
- you want stable caching keys
- you identify “the same thing” by recipe/input content

Common inputs:
- normalized metadata JSON
- content hash (bytes)
- ordered list of input IDs + parameter hash

---

## 🔧 API (reference contract)

> These are the stable *behaviors* expected from implementations (TypeScript/Python/etc.).

### Core functions
- `new_id(kind, strategy="opaque") -> str`
- `to_urn(kind, id) -> str`
- `parse_urn(urn) -> { kind, id }`
- `is_valid_id(id) -> bool`
- `is_valid_urn(urn) -> bool`

### Deterministic derivation
- `derive_id(namespace, payload_bytes) -> str`
- `derive_from_json(namespace, obj, canonicalize=true) -> str`

### Safety & hygiene
- `normalize_external_ref(system, value) -> str`
- `validate_kind(kind) -> bool`

---

## 🧰 CLI (expected commands)

```bash
# Create a new ID (opaque)
kfm-id new --kind layer

# Create a sortable ID (ULID/UUIDv7)
kfm-id new --kind run --strategy sortable

# Wrap/unwrap URNs
kfm-id urn --kind feature 01J4K9J0Z9V8KX2J6P2J0G8N1Q
kfm-id parse urn:kfm:feature:01J4K9J0Z9V8KX2J6P2J0G8N1Q

# Validate
kfm-id check 6b4a6f6f-8d47-4b22-9df8-2dbd9fe8c82b
kfm-id check urn:kfm:dataset:6b4a6f6f-8d47-4b22-9df8-2dbd9fe8c82b

# Derive a stable ID from JSON or file bytes
kfm-id derive --ns artifact --file ./tiles/14/4823/6162.pbf
kfm-id derive --ns model --json ./model_card.json
```

---

## 🗃️ PostgreSQL patterns

### ✅ Preferred table shape (stable internal ID + optional externals)
```sql
create table kfm_layer (
  id uuid primary key,
  created_at timestamptz not null default now(),

  -- human-friendly label (mutable)
  name text not null,

  -- provenance anchors
  source_id uuid null,
  pipeline_run_id uuid null,

  -- external refs (mutable; unique per system)
  external_system text null,
  external_id text null,

  unique (external_system, external_id)
);
```

### Index notes
- Put **stable ID** as the primary key.
- Add `created_at` if you need time ordering without time-encoding the ID.
- Use partial indexes for common filters (e.g. `where external_system is not null`).

> [!IMPORTANT]
> Don’t encode business meaning into the primary key “because it’s convenient today.”  
> That convenience becomes tomorrow’s migration nightmare.

---

## 🧾 Provenance payload example

Store provenance as explicit, inspectable metadata:

```json
{
  "id": "urn:kfm:layer:01J4K9J0Z9V8KX2J6P2J0G8N1Q",
  "title": "1878 County Boundaries (digitized)",
  "sources": [
    "urn:kfm:citation:5f3a2e0c-2d7e-4e61-a1f7-1ef24f0f1f12"
  ],
  "pipeline": {
    "run_id": "urn:kfm:run:01J4K9R8T4YB9E7E2XQWQ3P6H0",
    "name": "vectorize_boundaries",
    "version": "2026.01.14+git.abcdef"
  },
  "artifacts": {
    "content_hash": "blake3:9d5f...c1a2",
    "parameters_hash": "blake3:11aa...88ff"
  },
  "generated_at": "2026-01-14T00:00:00Z"
}
```

---

## 🗺️ GIS export rules

### GeoJSON
- Prefer `Feature.id` if supported by your tooling
- Or store at `properties["kfm:id"] = "urn:kfm:feature:..."`

### Tiles / caches
- Cache keys should be **derived IDs** (input IDs + params → deterministic key)
- Avoid cache keys that depend on mutable names

### 3D assets (WebGL / 3D GIS)
- Persisted meshes/textures should have:
  - `asset_id` (opaque)
  - optional `content_hash` (derived)
  - link back to `source_id` and `pipeline_run_id`

---

## 🔐 Security considerations

- **Never** accept an ID string and interpolate it into SQL/paths without strict validation.
- Prefer **opaque IDs** for public-facing endpoints to avoid enumeration patterns.
- If using time-sortable IDs publicly, treat timestamp leakage as **a privacy decision**.

---

## 🧪 Testing & quality gates

✅ Minimum test suite:
- round-trip: `id → urn → parse → id`
- validation: rejects malformed IDs and unknown kinds
- collision sanity checks (property-based)
- deterministic derivation stability:
  - same canonical JSON → same derived ID
  - re-ordered keys → same derived ID (if canonicalize=true)
- fuzz parsing (`parse_urn`) with random inputs

---

## 🗂️ Suggested folder layout

```text
tools/ 🧰
└─ 🆔 id/                         # identity + IDs toolkit
   ├─ 📦 src/                     # source implementations
   │  ├─ 🟦 ts/                   # frontend + node usage
   │  └─ 🐍 py/                   # pipelines + backend usage
   ├─ ✅ tests/                   # unit/integration tests
   ├─ 🧪 fixtures/                # test data + golden outputs
   └─ 📘 README.md                # you are here
```

---

## 🧭 Roadmap

- [ ] Decide canonical default: **UUIDv4 opaque** vs **UUIDv7 sortable** for each domain
- [ ] Implement reference libs: TypeScript + Python
- [ ] Add `derive_id()` canonical JSON hashing rules (documented & frozen)
- [ ] Add DB helpers (Postgres schema snippets, migrations)
- [ ] Add adapters for exports (GeoJSON/STAC-like metadata)
- [ ] Add “ID policy linting” (detect embedded meaning, enforce kind vocab)

---

## 📚 Project sources & influences

> [!NOTE]
> These documents inform the design philosophy of `tools/id` (stability, provenance, interoperability, performance, and human-centered accountability).

### Core KFM + identity foundations
- Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation :contentReference[oaicite:0]{index=0}  
- Flexible Software Design (stable identifiers, long-lived systems) :contentReference[oaicite:1]{index=1}  
- Database Performance at Scale (practical DB performance constraints) :contentReference[oaicite:2]{index=2}  
- Archaeological 3D GIS (cross-modal, 3D + geo-linked identity needs) :contentReference[oaicite:3]{index=3}  

### Modeling, ML, and reproducible computation
- Understanding Machine Learning (theory → algorithms; experiment identity) :contentReference[oaicite:4]{index=4}  
- Data Mining (knowledge extraction + traceability concerns) :contentReference[oaicite:5]{index=5}  
- SciPy Lecture Notes (scientific computing workflows) :contentReference[oaicite:6]{index=6}  

### Cross-language & implementation reality
- Implementing Programming Languages (parsing/ASTs/compilers → stable references) :contentReference[oaicite:7]{index=7}  
- Objective-C Notes for Professionals (interop reality across stacks) :contentReference[oaicite:8]{index=8}  
- MATLAB Notes for Professionals (scientific workflows + IDs) :contentReference[oaicite:9]{index=9}  
- Bash Notes for Professionals + Linear Algebra materials (CLI glue + data math) :contentReference[oaicite:10]{index=10}  

### 📦 Full project library index (for this repo)
<details>
<summary><strong>📚 Expand: All bundled project PDFs (ingested/consulted)</strong></summary>

- `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf`
- `Understanding Statistics & Experimental Design.pdf`
- `regression-analysis-with-python.pdf`
- `Regression analysis using Python - slides-linear-regression.pdf`
- `think-bayes-bayesian-statistics-in-python.pdf`
- `graphical-data-analysis-with-r.pdf`
- `making-maps-a-visual-guide-to-map-design-for-gis.pdf`
- `python-geospatial-analysis-cookbook.pdf`
- `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf`
- `Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf`
- `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf`
- `responsive-web-design-with-html5-and-css3.pdf`
- `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf`
- `Scalable Data Management for Future Hardware.pdf`
- `Data Spaces.pdf`
- `Database Performance at Scale.pdf`
- `Archaeological 3D GIS_26_01_12_17_53_09.pdf`
- `Introduction to Digital Humanism.pdf`
- `On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf`
- `Principles of Biological Autonomy - book_9780262381833.pdf`
- `Generalized Topology Optimization for Structural Design.pdf`
- `Spectral Geometry of Graphs.pdf`
- `compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf`
- `ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf`
- `Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf`
- `concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf`
- `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf`
- `A programming Books.pdf`
- `B-C programming Books.pdf`
- `D-E programming Books.pdf`
- `F-H programming Books.pdf`
- `I-L programming Books.pdf`
- `M-N programming Books.pdf`
- `O-R programming Books.pdf`
- `S-T programming Books.pdf`
- `U-X programming Books.pdf`

</details>

---

## ✅ Quick policy checklist

- [x] IDs are stable and never reused  
- [x] External IDs are stored separately and can change  
- [x] Derived artifacts can be reproduced via run + hashes  
- [x] URN wrapper standardizes cross-boundary referencing  
- [x] Validation is strict and centralized  
- [x] Performance and security tradeoffs are explicit  

---

## 🤝 Contributing

If you add a new ID kind:
1. Update the `<kind>` vocabulary in this README
2. Add validation + tests
3. Add at least one example URN
4. Ensure existing exports remain backwards compatible

> [!TIP]
> When in doubt: **add a new field, don’t mutate identity.**  
> Identity should outlive schema changes, renames, and migrations.


