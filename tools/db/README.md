# 🗄️ tools/db — Database Tooling (KFM)

![DB](https://img.shields.io/badge/DB-PostgreSQL%20%2B%20PostGIS-336791?logo=postgresql&logoColor=white)
![Graph](https://img.shields.io/badge/Graph-Neo4j-008CC1?logo=neo4j&logoColor=white)
![Ops](https://img.shields.io/badge/Ops-Migrations%20%2B%20Backups%20%2B%20Validation-orange)
![Governance](https://img.shields.io/badge/Governance-Contract%20%2B%20Provenance%20First-6f42c1)
![Style](https://img.shields.io/badge/Style-Idempotent%20%26%20Repeatable-brightgreen)

This directory is the **operational runbook + tooling home** for databases in Kansas Frontier Matrix (KFM):  
**bring up local DBs**, **apply migrations**, **seed test data**, **validate geodata**, and **backup/restore** reliably. 🧰

> [!NOTE]
> This folder is intentionally “boring.” It should contain **repeatable DB operations**, not business logic.

---

## 🎯 What this folder owns (and what it doesn’t)

✅ Owns:
- 🧱 **Schema & migrations** (Postgres/PostGIS + graph migrations if applicable)
- 🧪 **Validation** (geometry validity, CRS checks, metadata gates)
- 💾 **Backups / restores** (dev + ops playbooks)
- 📦 **Local dev orchestration** (Docker Compose, init scripts, seed fixtures)
- 📈 **Performance hygiene** (indexes, analyze/vacuum helpers, benchmark harness)

🚫 Does **not** own:
- 🧠 Domain/business rules (belongs in your domain layer / services)
- 🖥️ UI-to-DB access paths (UI must go through the governed API boundary)
- 🗺️ “Mystery layers” (anything not traceable to catalogs + provenance)

---

## 🧱 Datastores in KFM (mental model)

KFM treats **data + metadata + provenance** as first-class citizens.

- 🐘 **Postgres/PostGIS**: spatial indexing + queries; vector footprints; query-time joins; routing/network analysis when needed.
- 🕸️ **Neo4j (graph)**: relationships + semantic linking (**references back to catalogs**, not bulky payload storage).
- 🧊 **Object storage / filesystem**: large assets (e.g., COGs, documents, imagery) with **catalog references**.

```mermaid
flowchart LR
  A[📦 Raw Sources] --> B[🧪 ETL + Normalization]
  B --> C[🧾 Catalogs<br/>STAC + DCAT + PROV]
  C --> P[🐘 Postgres/PostGIS<br/>indexes + spatial query]
  C --> G[🕸️ Neo4j Graph<br/>relationships + refs]
  P --> API[🔌 Governed API<br/>contracts + redaction]
  G --> API
  API --> UI[🗺️ Map UI<br/>React · MapLibre · (optional) Cesium]
  UI --> N[🧠 Story Nodes / Focus Mode<br/>provenance-linked narrative]
```

---

## 📁 Suggested layout

If a folder doesn’t exist yet, create it when you add the capability (keep it tidy ✨):

```text
tools/db/
  📁 bin/                 # tiny CLIs: migrate, backup, restore, validate
  📁 docker/              # compose files + init scripts for local dev
  📁 migrations/
  │   ├─ 📁 postgres/      # SQL/Alembic migrations for Postgres/PostGIS
  │   └─ 📁 graph/         # Neo4j/graph migrations (if you version them)
  📁 sql/                 # idempotent admin scripts (indexes, extensions)
  📁 seed/                # seed fixtures for dev/tests (small + deterministic)
  📁 bench/               # micro-benchmarks / load test harness
  📝 README.md
```

---

## ⚡ Quickstart (local dev)

> [!TIP]
> Prefer **Docker Compose** for onboarding: one command to get a clean, reproducible environment.

### 1) Start the databases 🐳
Example (adjust filenames to match your repo):
```bash
docker compose -f tools/db/docker/docker-compose.yml up -d
```

### 2) Create extensions + schemas (PostGIS-first) 🧩
Run once per database (migration-friendly approach):

```sql
CREATE EXTENSION IF NOT EXISTS postgis;
CREATE EXTENSION IF NOT EXISTS pgcrypto; -- optional, but handy for UUID/crypto utilities
CREATE SCHEMA IF NOT EXISTS geodata;
```

> [!NOTE]
> Keeping spatial tables in a separate schema like `geodata` makes organization cleaner and can simplify backup/restore boundaries.

### 3) Apply migrations 🧱
Recommended CLI shape (implement however you like):
```bash
./tools/db/bin/migrate up
```

### 4) Run validation gates ✅
```bash
./tools/db/bin/validate all
```

---

## 🔐 Environment variables

These names are intentionally conventional—use what your stack prefers, but keep it consistent.

| Variable | Example | Used for |
|---|---:|---|
| `DATABASE_URL` | `postgresql://user:pass@localhost:5432/kfm` | App + tooling connection string |
| `PGHOST` / `PGPORT` | `localhost` / `5432` | CLI-friendly overrides |
| `PGUSER` / `PGPASSWORD` | `kfm` / `***` | Local dev auth |
| `PGDATABASE` | `kfm` | Target DB name |
| `NEO4J_URI` | `bolt://localhost:7687` | Graph tooling |
| `NEO4J_USER` / `NEO4J_PASSWORD` | `neo4j` / `***` | Graph auth |

---

## 🧾 Common operations

### Connect (psql) 🐘
```bash
psql "$DATABASE_URL"
```

### Backup (binary format) 💾
Keep backups timestamped and **test restores** periodically.
```bash
mkdir -p backups
pg_dump -Fc -f "backups/kfm_$(date +%F).dump" "$DATABASE_URL"
```

### Restore (into an empty DB) ♻️
```bash
pg_restore -d "$DATABASE_URL" "backups/kfm_2026-01-14.dump"
```

> [!WARNING]
> Restores overwrite reality fast. For safety: restore into a fresh DB name first, then swap.

---

## 🧪 Validation patterns (geospatial)

### Geometry validity checks (PostGIS) 🧭
Use PostGIS validity checks before “publishing” a dataset into the pipeline:

```sql
-- Find invalid geometries
SELECT id, ST_IsValid(geom) AS is_valid
FROM geodata.my_layer
WHERE NOT ST_IsValid(geom);

-- Get details on *why* it's invalid (helpful for fixes)
SELECT id, (ST_IsValidDetail(geom)).*
FROM geodata.my_layer
WHERE NOT ST_IsValid(geom);
```

### CRS sanity (rule-of-thumb) 🌍
- Pick a canonical CRS for storage (commonly **EPSG:4326**), and transform on ingest.
- Validate bounds if you store lon/lat (lon ∈ [-180, 180], lat ∈ [-90, 90]).

---

## 🧩 Migrations: conventions that scale

### Postgres/PostGIS migrations
- ✅ **Forward-only** is simplest (rollbacks optional, but don’t rely on them).
- ✅ Prefer **small, composable migrations**.
- ✅ Add indexes intentionally (GiST for geometry, B-tree for lookups).
- ✅ Migrations should be reproducible on clean DB and safe on existing DBs.

Suggested naming:
- `YYYYMMDDHHMMSS__short_description.sql`  
  Example: `20260114093000__add_layer_bounds_index.sql`

### Graph migrations (if used)
Keep graph changes versioned too:
- constraints / indexes
- ontology label/property conventions
- relationship type changes

> [!TIP]
> Treat “schema” broadly: Postgres schema + graph constraints + metadata profiles all evolve together.

---

## 📦 Metadata + provenance are the “real interface”

KFM’s pipeline is governed by **boundary artifacts**:
- 🧾 STAC (assets + spatial/temporal indexing)
- 🗂️ DCAT (dataset discovery + distributions)
- 🧬 PROV (lineage: inputs → activities → outputs)

The DB is an implementation detail **behind** those contracts.  
DB tools should therefore:
- enforce validators locally (pre-commit / CI),
- reject “publish” operations without complete catalogs,
- keep DB rows linkable to stable catalog identifiers.

---

## 📈 Performance & reliability playbook

Even “routine” operations can affect end-user experience:
- backups
- vacuum/analyze
- index creation
- compaction or large deletes
- replication catch-up (if applicable)

Practical habits:
- 🧪 benchmark representative workloads (read/write mix matters)
- 📊 track tail latency (p95/p99), not only averages
- 🕰️ schedule heavy operations, or run them in lower-traffic windows
- 🧰 keep a “restore drill” script so disaster recovery stays real

---

## 🧷 Federation & “data spaces” mindset

If KFM needs to **connect to external datasets** (without copying everything), use “data space” patterns:
- federated access
- strong governance + trust rules
- metadata-first interoperability

Postgres tip (optional): FDWs can help with **read-only federation** (treat remote sources as connectors, not “magic tables”).

---

## 🧠 Analytics & modeling support

KFM is not only a map viewer—it’s a research platform. DB tooling should make it easy to:
- export clean analysis datasets (CSV/Parquet)
- snapshot training datasets for regression/Bayesian modeling
- support reproducible simulation/optimization runs with traceable inputs/outputs

Example export:
```sql
COPY (
  SELECT * FROM analytics.v_dataset_for_model
) TO STDOUT WITH CSV HEADER;
```

---

## 🧯 Troubleshooting (fast hits)

| Symptom | Likely cause | Fix |
|---|---|---|
| `psql: connection refused` | DB container not running / wrong port | `docker ps`, check mapped ports |
| `permission denied for schema` | role lacks privileges | grant schema/table privileges; avoid using `postgres` everywhere |
| `extension "postgis" does not exist` | PostGIS not installed in image | use a PostGIS-enabled image or install packages |
| slow spatial queries | missing GiST index | add GiST index on geometry column |
| migrations fail in CI only | hidden state / non-idempotent scripts | ensure migrations run on clean DB in CI |
| invalid geometries | bad source data / wrong CRS | run `ST_IsValidDetail`, fix at ingest stage |

---

## 🤝 Contributing

When you add/change DB behavior:
1. 🧱 Add a migration (`tools/db/migrations/...`)
2. ✅ Add/extend validators (geometry + metadata + contract checks)
3. 🧾 Ensure STAC/DCAT/PROV references remain valid
4. 📈 Add an index or benchmark if it impacts query patterns
5. 📝 Update this README if the operator workflow changed

---

## 📚 Project Reference Library (the docs powering our conventions)

<details>
<summary><strong>Click to expand 📖</strong> (kept here so DB conventions stay aligned with the project’s “source library”)</summary>

### Core KFM docs (architecture + governance)
- 🧭 **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation**
- 🧱 **MARKDOWN_GUIDE_v13** (contract-first + pipeline ordering + governance invariants)
- 🗺️ **Kansas-Frontier-Matrix — Open-Source Geospatial Historical Mapping Hub Design**

### Databases, data management, and performance
- 🐘 **PostgreSQL Notes for Professionals**
- 📈 **Database Performance at Scale**
- 🧊 **Scalable Data Management for Future Hardware**
- 🧩 **Data Spaces** (federation, governance, trust)

### Geospatial + mapping stack
- 🧭 **python-geospatial-analysis-cookbook**
- 🗺️ **making-maps-a-visual-guide-to-map-design-for-gis**
- 📱 **Mobile Mapping: Space, Cartography and the Digital**
- 🏛️ **Archaeological 3D GIS**

### Analytics, stats, and modeling (what DB exports should enable)
- 📉 **regression-analysis-with-python**
- 📊 **Understanding Statistics & Experimental Design**
- 📈 **graphical-data-analysis-with-r**
- 🧠 **think-bayes-bayesian-statistics-in-python**
- 🛰️ **Cloud-Based Remote Sensing with Google Earth Engine**
- 🧪 **Scientific Modeling and Simulation (NASA-grade guide)**
- 🧮 **Generalized Topology Optimization for Structural Design**
- 🕸️ **Spectral Geometry of Graphs**
- 📚 **Regression analysis using Python (slides)**

### Engineering & platform concerns
- 🧵 **concurrent-real-time-and-distributed-programming-in-java** (systems thinking: concurrency + reliability)
- 🖼️ **compressed-image-file-formats-jpeg-png-gif-xbm-bmp** (assets, storage, distribution)
- 🧑‍💻 **responsive-web-design-with-html5-and-css3** (UI constraints influence API/DB shaping)
- 🌐 **webgl-programming-guide** (3D visualization influences tiling + query patterns)

### Security + ethics + governance (defensive posture)
- 🔐 **ethical-hacking-and-countermeasures-secure-network-infrastructures**
- 🧯 **Gray Hat Python** (treat as defensive learning / threat modeling)
- ⚖️ **On the path to AI Law’s prophecies…** (data governance, ML-era considerations)
- 🧭 **Introduction to Digital Humanism**
- 🧬 **Principles of Biological Autonomy**

### “Programming Books” collections (grab-bag references)
- 📦 **A programming Books**
- 📦 **B-C programming Books**
- 📦 **D-E programming Books**
- 📦 **F-H programming Books**
- 📦 **I-L programming Books**
- 📦 **M-N programming Books**
- 📦 **O-R programming Books**
- 📦 **S-T programming Books**
- 📦 **U-X programming Books**

</details>

