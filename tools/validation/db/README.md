# 🧪🗄️ DB Validation Toolkit

![DB](https://img.shields.io/badge/DB-PostgreSQL%20%2B%20PostGIS-blue)
![Scope](https://img.shields.io/badge/scope-schema%20%7C%20data%20%7C%20security%20%7C%20performance-purple)
![CI](https://img.shields.io/badge/CI-quality%20gate-critical)
![Output](https://img.shields.io/badge/reports-json%20%7C%20junit%20%7C%20markdown-informational)

> **Path:** `tools/validation/db/`  
> Contract-first, provenance-first **database** quality gates for Kansas Frontier Matrix (KFM). ✅

---

## 🧭 TL;DR

- **Run DB checks** before merging, releasing, or ingesting new datasets.
- Catch issues early: **schema drift**, **broken constraints**, **invalid geometries**, **missing provenance**, **unsafe privileges**, **perf regressions**.
- Produce CI-friendly reports (JSON/JUnit/Markdown) with consistent **exit codes**.

> [!NOTE]
> This folder focuses on **database-layer** validation. It complements higher-level validation (catalog/manifest checks, API contract checks, etc.).

---

## 🧩 Where this fits in the KFM pipeline

KFM is designed around **contract-first** + **provenance-first** delivery. DB validation is one of the “hard stops” that prevents silent data drift from reaching the UI, analytics, or narratives.

```mermaid
flowchart LR
  A[📥 Raw Sources] --> B[🧰 Ingest / ETL]
  B --> C[(🗄️ Postgres/PostGIS)]
  C --> D[🧪 tools/validation/db]
  D -->|pass ✅| E[📡 API / Services]
  D -->|fail ❌| F[🧯 Block CI / Release]
  E --> G[🗺️ UI / WebGL / Maps]
  E --> H[📊 Analytics / Models]
```

---

## ✅ What gets validated

### 1) 🧱 Schema & Migration Integrity
- Required extensions installed (e.g., PostGIS)
- Expected schemas/tables/views exist
- Column types match contracts (no accidental `text` vs `uuid` drift)
- Primary keys / foreign keys present and enforceable
- “No surprise” DDL changes (detected via schema snapshot)

### 2) 🔗 Relational Integrity
- PK uniqueness (no duplicate IDs)
- FK referential integrity (no orphan rows)
- `NOT NULL` expectations honored
- Domain constraints (enumerations, ranges, regex rules)
- Deduplication rules (canonical uniqueness constraints)

### 3) 🧬 Provenance & Metadata Completeness
- Every “published” record is traceable to a **source** and an **ingest run**
- Required lineage fields populated (`source_id`, `ingested_at`, `license`, etc.)
- Dataset/collection identifiers are stable and present
- Optional governance fields present where applicable (classification, consent, retention)

### 4) 🌍 Geospatial Validity (PostGIS)
- Geometry validity (e.g., `ST_IsValid`)
- Consistent SRID / coordinate reference system expectations
- Bounding boxes inside expected world/region envelopes
- Topology checks for specific layers (no self-intersections, overlaps, etc.)
- Raster policy enforcement: **store footprints + metadata** instead of stuffing huge rasters into DB

### 5) 🛡️ Security & Access Controls
- Least privilege for application roles
- No accidental `PUBLIC` grants on sensitive schemas
- Default privileges sane for new tables
- Optional: RLS policies enabled where required
- Sensitive columns labeled/guarded (depending on KFM governance tier)

### 6) ⚡ Performance & Operational Guardrails
- Missing index detection for critical access paths
- Table/index bloat warnings (threshold-based)
- Query plan sanity checks for “golden queries”
- Backup/restore smoke tests (where safe to run)
- Replication/connection pool sanity (if applicable in environment)

---

## 🚀 Quickstart

> [!TIP]
> In CI, run **core + security + geospatial** at minimum. Add **performance** checks on nightly / release branches.

### 0) Set your DB connection

```bash
export DATABASE_URL="postgresql://USER:PASSWORD@HOST:5432/DBNAME"
# Optional:
export DB_SCHEMA="public"
export KFM_ENV="dev"   # dev|ci|staging|prod
```

### 1) Run the validator

Pick the runner style that matches your repo wiring:

#### Option A — Python module runner (recommended pattern)
```bash
python -m tools.validation.db validate \
  --packs core,geospatial,security \
  --format pretty
```

#### Option B — Make target wrapper (if present)
```bash
make validate-db
```

#### Option C — Docker Compose (if your services run in containers)
```bash
docker compose run --rm api \
  python -m tools.validation.db validate --packs core,geospatial
```

---

## ⚙️ Configuration

### Environment variables

| Variable | Purpose | Example |
|---|---|---|
| `DATABASE_URL` | Connection string | `postgresql://...` |
| `DB_SCHEMA` | Target schema(s) | `public` |
| `KFM_ENV` | Enables env-specific thresholds | `ci` |
| `VALIDATION_PACKS` | Default packs if CLI omits | `core,security` |
| `VALIDATION_STRICT` | Treat warnings as failures | `1` |

### Profiles & thresholds

Recommended: store profiles in `tools/validation/db/config/`:

- `dev.yml` → relaxed thresholds, verbose output
- `ci.yml` → strict correctness checks, minimal logs
- `staging.yml` → adds backup/restore + perf smoke tests
- `prod.yml` → read-only checks unless explicitly allowed

---

## 📦 Check packs

| Pack | Purpose | Typical severity |
|---|---|---|
| `core` | schema + constraints + invariants | ❌ blocker/error |
| `geospatial` | PostGIS validity + SRID + topology | ❌ blocker/error |
| `provenance` | lineage + metadata completeness | ❌ error / ⚠️ warn |
| `security` | grants + roles + default privileges | ❌ blocker/error |
| `performance` | index coverage + regression heuristics | ⚠️ warn / ❌ error (release) |
| `simulation` | reproducibility + run metadata + UQ fields | ⚠️ warn / ❌ error (publish) |
| `stats` | distribution sanity + drift + missingness | ⚠️ warn |

> [!IMPORTANT]
> Packs are meant to be composable: start small, add domain checks as datasets mature.

---

## 📁 Folder layout (expected)

```text
tools/validation/db/
├── 📘 README.md
├── 🧠 runner/                 # orchestration (python/ts/etc.)
│   ├── __init__.py
│   ├── cli.py
│   ├── engine.py
│   └── reporters/
├── ✅ checks/
│   ├── core/
│   ├── geospatial/
│   ├── provenance/
│   ├── security/
│   ├── performance/
│   ├── simulation/
│   └── stats/
├── 🧾 sql/                    # raw SQL checks (optional)
├── ⚙️ config/                 # profiles, thresholds, allowlists
└── 🧪 fixtures/               # tiny seed DBs / snapshots for tests
```

> If your repo uses a different layout, keep the **concepts** the same:
> checks are modular, declarative where possible, and CI-friendly.

---

## 🧾 Output format

### JSON (machine-friendly)
Example record:
```json
{
  "id": "geospatial.geom_valid",
  "pack": "geospatial",
  "severity": "error",
  "status": "fail",
  "summary": "Found 12 invalid geometries in public.parcels",
  "evidence": {
    "table": "public.parcels",
    "invalid_count": 12,
    "sample_ids": ["..."]
  }
}
```

### JUnit (CI-friendly)
- Each check becomes a testcase.
- Any `error`/`blocker` failure fails the suite.

### Markdown (human-friendly)
- Great for PR comments and audit trails.

---

## 🚦 Exit codes & CI behavior

| Code | Meaning |
|---:|---|
| `0` | All checks passed (or only allowed warnings) ✅ |
| `1` | At least one check failed ❌ |
| `2` | Misconfiguration / cannot connect to DB 🧯 |

Recommended gating rule:
- `blocker` + `error` → **fail CI**
- `warn` → fail only under `--strict` or in release workflows

---

## ➕ Adding a new DB check

### ✅ Design rules
- **Deterministic:** same DB state ⇒ same result
- **Fast by default:** avoid full scans unless behind a flag
- **Actionable output:** include table/column and sample IDs
- **Safe:** prefer read-only queries; guard any write tests behind `--allow-writes`

### Suggested check contract (declarative)
Create a file like:
- `checks/geospatial/geom_valid.yml`
- `sql/geospatial/geom_valid.sql`

`geom_valid.yml`:
```yaml
id: geospatial.geom_valid
pack: geospatial
severity: error
description: "All geometries must be ST_IsValid()"
sql: sql/geospatial/geom_valid.sql
expect:
  fail_if_rows_gt: 0
```

`geom_valid.sql`:
```sql
SELECT id
FROM public.parcels
WHERE geom IS NOT NULL
  AND NOT ST_IsValid(geom)
LIMIT 50;
```

> [!TIP]
> Store “why this check exists” right next to the check (short + direct). Future you will thank you. 🙏

---

## 🌍 PostGIS validation patterns (grab bag)

Use these patterns to build checks:

- Validity: `ST_IsValid(geom)`
- SRID: `ST_SRID(geom) = 4326` (or your canonical SRID)
- Intersections / containment: `ST_Intersects`, `ST_Within`
- Reprojection: `ST_Transform`
- Buffers: `ST_Buffer` (use carefully; it can be expensive)

---

## 🔐 Security validation patterns (PostgreSQL)

Common checks:
- Ensure `PUBLIC` doesn’t have broad privileges on schemas/tables.
- Ensure default privileges are explicit.
- Ensure app role has only what it needs.

---

## 🧪 Simulation & model-result validation (optional but recommended)

If the DB stores simulation/model outputs:
- Every run should be traceable to:
  - code version / commit hash
  - input dataset versions
  - parameter set ID
  - random seed(s) if stochastic
- Store **uncertainty quantification (UQ)** fields where relevant (CI for “publishable” runs).
- Validate required run metadata before results become “published”.

---

## 🧯 Troubleshooting

<details>
<summary>🔌 “Cannot connect to database”</summary>

- Confirm `DATABASE_URL` is set and reachable.
- Confirm SSL requirements (if any).
- Confirm network access from CI runner / container.

</details>

<details>
<summary>🧩 “PostGIS functions missing”</summary>

- Ensure PostGIS extension is installed in the target DB:
  - `CREATE EXTENSION postgis;` (admin only)
- Ensure your validation user can `SELECT` from `geometry_columns` / `spatial_ref_sys` if needed.

</details>

<details>
<summary>🐢 “Checks are slow”</summary>

- Move expensive checks into the `performance` pack.
- Add sampling / `LIMIT` and evidence queries.
- Add indexes (and validate their existence to prevent regressions).

</details>

---

## 📚 Project reference library (why these checks exist)

<details>
<summary>📖 Show project files that inform DB validation</summary>

### 🧠 Core architecture & documentation
- `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf`
- `MARKDOWN_GUIDE_v13.md.gdoc`

### 🗄️ Databases & performance
- `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf`
- `Database Performance at Scale.pdf`
- `Scalable Data Management for Future Hardware.pdf`
- `Data Spaces.pdf`

### 🌍 Geospatial, GIS, cartography, remote sensing
- `python-geospatial-analysis-cookbook.pdf`
- `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf`
- `making-maps-a-visual-guide-to-map-design-for-gis.pdf`
- `Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf`
- `Archaeological 3D GIS_26_01_12_17_53_09.pdf`

### 🧪 Modeling, simulation, statistics, ML
- `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf`
- `Scientific Method _ Research _ Master Coder Protocol Documentation.pdf`
- `Understanding Statistics & Experimental Design.pdf`
- `regression-analysis-with-python.pdf`
- `Regression analysis using Python - slides-linear-regression.pdf`
- `think-bayes-bayesian-statistics-in-python.pdf`
- `graphical-data-analysis-with-r.pdf`
- `Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf` *(library reference)*

### 🕸️ Graphs & optimization
- `Spectral Geometry of Graphs.pdf`
- `Generalized Topology Optimization for Structural Design.pdf`

### 🔐 Security mindset (defensive use)
- `ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf`
- `Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf`

### 🧑‍⚖️ Governance, law, human factors
- `Introduction to Digital Humanism.pdf`
- `On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf`
- `Principles of Biological Autonomy - book_9780262381833.pdf`

### 🧰 Build & UI references (supporting ecosystem)
- `responsive-web-design-with-html5-and-css3.pdf`
- `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf`
- `compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf`

### 📦 Programming compendiums (general reference shelf)
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

## ✅ Definition of Done (for DB validation work)

A DB validation change is “done” when:
- [ ] New checks have clear IDs, severity, and pack ownership
- [ ] Checks are deterministic + safe by default
- [ ] CI runs them (or they’re explicitly gated behind a profile)
- [ ] Failures include actionable evidence (table, column, sample IDs)
- [ ] Docs updated (this README + check-local docs if needed)

---

⬅️ Back: `../README.md` (tools/validation)  
🏠 Repo root: `../../../README.md`
