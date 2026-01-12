# 🗄️ Database Scripts — `api/scripts/db`

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791?logo=postgresql&logoColor=white)
![PostGIS](https://img.shields.io/badge/PostGIS-Spatial%20SQL-2E7D32)
![Neo4j](https://img.shields.io/badge/Neo4j-Knowledge%20Graph-008CC1?logo=neo4j&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)
![STAC/DCAT/PROV](https://img.shields.io/badge/Metadata-STAC%20%7C%20DCAT%20%7C%20PROV-7B1FA2)
![Idempotent](https://img.shields.io/badge/Scripts-Idempotent%20by%20default-success)

> According to a document from **January 12, 2026**, KFM’s DB layer centers on **PostGIS** (fast bounding-box queries & spatial indexing) plus **tile generation/caching** for web mapping. :contentReference[oaicite:0]{index=0}

---

## 🎯 What this folder is

This directory is the **DB runbook + automation toolbox** for Kansas Frontier Matrix (KFM). It’s where we keep scripts that:

- 🧱 **Provision** local/dev/test databases (and optionally staging)
- 🧬 **Enable extensions** (PostGIS, etc.) and create schemas
- 🧰 **Apply migrations** and keep schema evolution repeatable
- 🌱 **Seed** baseline reference tables (domains, vocabularies, system defaults)
- 🗺️ **Load spatial layers** into PostGIS (vector/raster metadata where relevant)
- 🧪 **Validate** data quality (geometry validity, foreign keys, provenance links)
- 🕸️ **Export / refresh graph references** used by Neo4j (graph = relationships, not payload) :contentReference[oaicite:1]{index=1}
- 💾 **Backup/restore** (pg_dump, snapshots, and smoke tests)

> KFM also uses **Neo4j** for semantic/relationship queries aligned with standards like CIDOC-CRM, GeoSPARQL, and OWL-Time. :contentReference[oaicite:2]{index=2}

---

## 🧭 Table of contents

- [🚦 Safety first](#-safety-first)
- [📦 Folder layout](#-folder-layout)
- [⚙️ Prerequisites](#️-prerequisites)
- [🔐 Configuration](#-configuration)
- [🚀 Quickstart workflows](#-quickstart-workflows)
- [🗺️ PostGIS patterns we rely on](#️-postgis-patterns-we-rely-on)
- [🧾 Metadata + provenance contract](#-metadata--provenance-contract)
- [🕸️ Neo4j graph refresh](#️-neo4j-graph-refresh)
- [🧪 Testing + QA](#-testing--qa)
- [🛡️ Security notes](#️-security-notes)
- [⚡ Performance notes](#-performance-notes)
- [📚 Project library](#-project-library)

---

## 🚦 Safety first

> [!WARNING]
> Many DB scripts are **destructive** (drop/reset). Never point them at production unless you *explicitly* mean to.

Recommended guardrails:
- Require `--yes-really` for destructive actions
- Require `ENV=local|test|staging|prod` and refuse `prod` unless `ALLOW_PROD=1`
- Print the resolved connection string **host + dbname** before doing anything
- Default to **idempotent** operations (e.g., `CREATE EXTENSION IF NOT EXISTS`, `CREATE TABLE IF NOT EXISTS`)

---

## 📦 Folder layout

> This is the **recommended** structure for this directory (adjust to match what exists in the repo).

```text
📂 api/scripts/db/
├── 📄 README.md                         # 👈 you are here
├── 📂 docker/                           # 🐳 local containers (optional)
│   └── 📄 compose.db.yml
├── 📂 postgres/                         # 🐘 Postgres/PostGIS SQL
│   ├── 📄 00_extensions.sql             # 🧩 postgis, pgcrypto, pg_stat_statements...
│   ├── 📄 01_roles.sql                  # 👥 least-privilege roles
│   ├── 📄 02_schemas.sql                # 🏗️ catalog / geodata / audit / app
│   ├── 📄 03_tables.sql                 # 🧱 core tables
│   ├── 📄 04_indexes.sql                # ⚡ spatial + btree + gin
│   ├── 📄 05_views.sql                  # 👓 read models
│   ├── 📄 06_functions.sql              # 🧠 helpers, triggers, utilities
│   └── 📂 seeds/                        # 🌱 deterministic seeds
│       ├── 📄 00_reference.sql
│       └── 📄 10_demo_data.sql
├── 📂 migrations/                       # 🔁 alembic/flyway/sql-based migrations
│   └── 📄 ...                           # (tool-specific)
├── 📂 neo4j/                            # 🕸️ graph constraints/imports (optional)
│   ├── 📄 00_constraints.cypher         # 🔒 uniqueness constraints
│   ├── 📄 10_import_nodes.cypher
│   ├── 📄 20_import_edges.cypher
│   └── 📄 99_post_import.cypher
├── 📂 qa/                               # 🧪 validation + smoke checks
│   ├── 📄 00_smoke.sql                  # ✅ quick health checks
│   ├── 📄 10_geometry_validity.sql      # 🧭 ST_IsValid checks
│   ├── 📄 20_catalog_links.sql          # 🔗 STAC/DCAT/PROV referential checks
│   └── 📄 validate_catalogs.py          # 🧾 metadata sanity checks (no secrets)
└── 📂 tools/                            # 🛠️ CLI wrappers / runbooks
    ├── 📄 db_up.sh                      # ▶️ start local DBs
    ├── 📄 db_down.sh                    # ⏹️ stop local DBs
    ├── 📄 db_reset.sh                   # 💥 drop + recreate (guarded)
    ├── 📄 db_migrate.sh                 # 🔁 apply migrations
    ├── 📄 db_seed.sh                    # 🌱 seed reference data
    ├── 📄 db_load_geodata.sh            # 🗺️ import processed layers
    ├── 📄 db_backup.sh                  # 💾 pg_dump
    └── 📄 db_restore.sh                 # ♻️ restore
```

---

## ⚙️ Prerequisites

- 🐳 Docker + Docker Compose (recommended for local/dev)
- 🐘 `psql` + `pg_dump` (PostgreSQL client tooling)
- 🧭 PostGIS-enabled PostgreSQL (local container is easiest)
- 🕸️ Neo4j (optional, only if you’re running the graph layer locally)

---

## 🔐 Configuration

Typical env vars (adapt to your `.env` conventions):

| Variable | Example | Notes |
|---|---:|---|
| `DATABASE_URL` | `postgresql://kfm_app:pass@localhost:5432/kfm` | Prefer a single URL |
| `POSTGRES_HOST` | `localhost` | If not using `DATABASE_URL` |
| `POSTGRES_DB` | `kfm` |  |
| `POSTGRES_USER` | `kfm_app` | App role |
| `POSTGRES_PASSWORD` | `...` | Don’t commit |
| `NEO4J_URI` | `bolt://localhost:7687` | Optional |
| `NEO4J_USER` | `neo4j` | Optional |
| `NEO4J_PASSWORD` | `...` | Optional |
| `KFM_DATA_DIR` | `./data` | Used for loading assets |

> [!NOTE]
> If your repo follows KFM’s metadata contract, your DB loads should treat **`data/processed/**`** as the stable output location, with catalogs written to `data/stac/`, `data/catalog/dcat/`, and `data/prov/`. :contentReference[oaicite:3]{index=3}

---

## 🚀 Quickstart workflows

### 1) Bring up local DBs 🐳
```bash
# recommended
./tools/db_up.sh
```

### 2) Initialize core schema 🧱
```bash
# enable extensions + schemas + base tables
psql "$DATABASE_URL" -f postgres/00_extensions.sql
psql "$DATABASE_URL" -f postgres/02_schemas.sql
psql "$DATABASE_URL" -f postgres/03_tables.sql
psql "$DATABASE_URL" -f postgres/04_indexes.sql
```

> If you prefer a dedicated schema (instead of dumping everything into `public`), that’s a common PostGIS workflow: `CREATE EXTENSION postgis; CREATE SCHEMA ...;` :contentReference[oaicite:4]{index=4}

### 3) Apply migrations 🔁
```bash
./tools/db_migrate.sh
```

### 4) Seed reference data 🌱
```bash
./tools/db_seed.sh
```

### 5) Load processed geodata 🗺️
```bash
# loads from data/processed/** and registers metadata links
./tools/db_load_geodata.sh
```

### 6) Validate everything ✅
```bash
psql "$DATABASE_URL" -f qa/00_smoke.sql
psql "$DATABASE_URL" -f qa/10_geometry_validity.sql
python qa/validate_catalogs.py
```

---

## 🗺️ PostGIS patterns we rely on

### Spatial indexing + bbox queries
KFM’s API expects **fast “what’s in this map view?”** queries (bbox / viewport). PostGIS provides spatial indexing and SQL patterns for this. :contentReference[oaicite:5]{index=5}

**Example (viewport bbox):**
```sql
-- bbox in WGS84 (EPSG:4326) for example purposes
SELECT id, name, geom
FROM geodata.features
WHERE geom && ST_MakeEnvelope(:min_lon, :min_lat, :max_lon, :max_lat, 4326)
  AND ST_Intersects(geom, ST_MakeEnvelope(:min_lon, :min_lat, :max_lon, :max_lat, 4326));
```

**Index to support it:**
```sql
CREATE INDEX IF NOT EXISTS idx_features_geom_gist
ON geodata.features
USING GIST (geom);
```

### Tiles (vector tiles / caching)
For web mapping, KFM mentions generating vector tiles and caching for performance. :contentReference[oaicite:6]{index=6}

Where DB scripts fit:
- precompute / refresh tile sources (views/materialized views)
- ensure geometry is valid + simplified appropriately per zoom level
- keep “tile-ready” queries stable and versioned

---

## 🧾 Metadata + provenance contract

KFM treats metadata artifacts as **boundary contracts** between pipelines → graph → API → UI. The required trio:

- **STAC** (Collections + Items) for geospatial assets
- **DCAT** dataset entry for discovery
- **PROV** for lineage (inputs → steps → outputs) :contentReference[oaicite:7]{index=7}

Cross-linking expectations include:
- STAC Items link to actual assets in `data/processed/**` (or stable storage) :contentReference[oaicite:8]{index=8}
- DCAT distributions point to STAC or data resources :contentReference[oaicite:9]{index=9}
- PROV records connect raw → work → processed and capture run/config identifiers :contentReference[oaicite:10]{index=10}

### DB implication 🧩
Your DB scripts should **not** “silently ingest” data:
- every load/import should record:
  - dataset IDs (STAC collection/item IDs)
  - provenance IDs (PROV bundle identifiers)
  - license + source attribution pointers (DCAT fields)

> If your KFM profiles include project-specific fields (e.g., provenance references & uncertainty indicators), DB scripts should validate those exist before “publishing” an asset. :contentReference[oaicite:11]{index=11}

---

## 🕸️ Neo4j graph refresh

**Graph rule of thumb:** the graph stores **relationships + references** (IDs/links), not bulky payloads. :contentReference[oaicite:12]{index=12}

### Typical workflow
1. DB exports a “graph-ready” dataset:
   - nodes (entities)
   - edges (relationships)
   - references back to STAC/DCAT/PROV IDs
2. Neo4j scripts ingest those datasets
3. Post-import scripts build derived relationships / constraints

> If you’re using Cypher imports or py2neo merges, make your scripts idempotent and constrain uniqueness so reruns don’t duplicate nodes. (See examples of `MERGE`-like patterns.) :contentReference[oaicite:13]{index=13}

---

## 🧪 Testing + QA

KFM highlights integration-style tests that simulate: **API request → DB query → response** and verify correctness & performance. :contentReference[oaicite:14]{index=14}

Recommended QA checks in `qa/`:
- ✅ DB can connect + required extensions exist
- ✅ required schemas/tables/views exist
- ✅ `ST_IsValid(geom)` for all spatial tables
- ✅ “catalog link” checks:
  - every loaded layer has STAC Item ID
  - every dataset has DCAT + PROV pointers
- ✅ sample bbox query returns within a threshold

---

## 🛡️ Security notes

- Always use parameterized queries from the API layer.
- Sanitize + validate any inputs that land in SQL (including admin scripts).
- SQL injection is real even in “internal” tools—don’t concatenate strings into statements. :contentReference[oaicite:15]{index=15}

---

## ⚡ Performance notes

### Caching & reuse
For expensive queries, **reuse** can matter (materialized views, cached intermediate outputs, etc.). Caching intermediate results can improve repeated-query workloads. :contentReference[oaicite:16]{index=16}

Where to reflect this in scripts:
- `postgres/05_views.sql` → build stable read models
- optional `postgres/05_materialized_views.sql` → refresh policies
- `tools/db_refresh_views.sh` → on-demand refresh

### Keep structure vs process distinct 🧠
Treat the DB schema as the **structure model** and ETL loads as **process**. This separation helps keep responsibilities clean and scripts composable. :contentReference[oaicite:17]{index=17}

---

## 🧩 Scaling + future-proofing (roadmap)

The project’s “future proposals” emphasize scaling, federation/sharding, caching, and containerized deployment. :contentReference[oaicite:18]{index=18}

DB script implications:
- migration strategy that works across multiple environments
- reproducible seeds and fixtures for CI
- export/import tooling that can target partitions/shards later
- “data product” boundaries (datasets with IDs + metadata) rather than monolithic loads

---

## 📚 Project library

### Core KFM docs (high signal)
- 📘 KFM Comprehensive Technical Documentation :contentReference[oaicite:19]{index=19}
- 💡 KFM Latest Ideas & Future Proposals :contentReference[oaicite:20]{index=20}
- 🧾 Metadata + repo standards (STAC/DCAT/PROV) :contentReference[oaicite:21]{index=21}

### System design + reproducibility
- 🏗️ Open-Source Geospatial Historical Mapping Hub Design (includes DVC plan + repo structure) :contentReference[oaicite:22]{index=22}

### Engineering & implementation references
- 🐘 PostgreSQL notes (practical SQL/ops) :contentReference[oaicite:23]{index=23}
- 🧭 Geospatial analysis cookbook (PostGIS workflows) :contentReference[oaicite:24]{index=24}
- 🕸️ Data Spaces (polyglot storage + graph DB context) :contentReference[oaicite:25]{index=25}

### “Project bundles” (programming & applied math) — used as shared reference shelf
> These are here so contributors can align patterns, style, and tooling across the repo.

- 🧠 Implementing Programming Languages :contentReference[oaicite:26]{index=26}  
- 📐 MATLAB Notes for Professionals :contentReference[oaicite:27]{index=27}  
- 🐚 Bash Notes for Professionals :contentReference[oaicite:28]{index=28}  
- 🤖 Understanding Machine Learning (theory ↔ practice) :contentReference[oaicite:29]{index=29}  
- ➗ Linear Algebra / ML math reference :contentReference[oaicite:30]{index=30}  

---

## ✅ Contribution checklist for DB scripts

> [!TIP]
> If you add or modify scripts here, aim for “clone → run → reproduce”.

- [ ] Script is idempotent (or clearly marked destructive)
- [ ] Script prints the target DB host/dbname before acting
- [ ] Script supports `--help` and reads config from env
- [ ] If it loads data, it also records/validates STAC/DCAT/PROV links :contentReference[oaicite:31]{index=31}
- [ ] QA checks added/updated in `qa/`
- [ ] CI-friendly (non-interactive mode available)

---

💬 **If you’re wiring new DB scripts:** keep them small, composable, and “pipeline-safe” so they can be called from Make/CI without surprises. 🧩

