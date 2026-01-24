# 🐘🗺️ PostGIS Outbound Adapter (KFM Server)

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-%E2%9C%94%EF%B8%8F-316192?logo=postgresql&logoColor=white)
![PostGIS](https://img.shields.io/badge/PostGIS-%E2%9C%94%EF%B8%8F-2E7D32?logo=postgresql&logoColor=white)
![Hexagonal](https://img.shields.io/badge/Architecture-Ports%20%26%20Adapters-6A1B9A)
![Policy](https://img.shields.io/badge/Policy%20as%20Code-OPA%20%2F%20Conftest-7B1FA2)
![Metadata](https://img.shields.io/badge/Metadata-STAC%20%2B%20DCAT%20%2B%20PROV-F57C00)
![Tiles](https://img.shields.io/badge/Tiles-MVT%20%2F%20PMTiles-455A64)

> [!IMPORTANT]
> **KFM’s rule of thumb:** _PostGIS stores the geo truth 🧱 (vectors/rasters), Catalogs describe the assets 🗂️, the Graph links the context 🕸️._  
> This adapter exists so **every** PostGIS query (GeoJSON, tiles, stats, “Focus Mode” answers) runs through a single, auditable, policy-aware boundary ✅.

---

## ✨ What this adapter is for

The **PostGIS outbound adapter** lives at:

```
src/server/adapters/outbound/postgis/
```

It is the server’s “last mile” to PostGIS and is responsible for:

- 🗺️ **Geospatial queries** (bbox, intersects, within, nearest, etc.)
- 🕰️ **Spatiotemporal filtering** (timeline slider + time range endpoints)
- 🧱 **Vector tile generation (MVT)** for MapLibre/Cesium clients
- 📊 **Summary stats** (counts, histograms, aggregations) used by dashboards & Focus Mode
- 🧾 **Governance hooks**: provenance, sensitivity propagation, query auditing, and “fail-closed” behavior

> [!NOTE]
> KFM treats the UI as **read-only**. All data access must go through server routes that can enforce redaction/policy and attach provenance receipts 🧾.

---

## 🧭 Table of contents

- [🎯 Responsibilities](#-responsibilities)
- [🧩 Where it fits in the architecture](#-where-it-fits-in-the-architecture)
- [🗂️ Catalog-driven access](#️-catalog-driven-access)
- [⚙️ Configuration](#️-configuration)
- [🐳 Local development](#-local-development)
- [🧱 Schema and migrations](#-schema-and-migrations)
- [🧠 Query patterns](#-query-patterns)
  - [📦 GeoJSON feature queries](#-geojson-feature-queries)
  - [🕰️ Time range queries](#️-time-range-queries)
  - [🧩 Vector tiles (MVT)](#-vector-tiles-mvt)
  - [📊 Summary stats](#-summary-stats)
- [🛡️ Governance and security](#️-governance-and-security)
- [🚀 Performance playbook](#-performance-playbook)
- [🧪 Testing](#-testing)
- [➕ Adding a new PostGIS-backed layer](#-adding-a-new-postgis-backed-layer)
- [🧯 Troubleshooting](#-troubleshooting)
- [📚 Glossary](#-glossary)

---

## 🎯 Responsibilities

| ✅ Owns | ❌ Does *not* own |
|---|---|
| Connection + pooling 🔌 | Business/domain decisions (what a user is “allowed to ask”) |
| Parameterized SQL execution 🧷 | Direct UI-to-DB access (bypasses governance) |
| Spatial query templates 🗺️ | Arbitrary “run any SQL” endpoints |
| Vector tile SQL templates 🧩 | Cross-store joins with Neo4j inside SQL |
| Statement timeouts + safety rails ⏱️ | Long-running analytics jobs (use pipelines/batch) |
| Returning provenance envelopes 🧾 | Mutating data during read paths (unless explicitly an ingestion adapter) |

---

## 🧩 Where it fits in the architecture

```mermaid
flowchart LR
  UI[🖥️ UI<br/>MapLibre / Cesium] --> API[🧠 Server/API]
  API --> APP[🧩 Application Services<br/>Use Cases]
  APP -->|Outbound Port| PG[🐘 PostGIS Adapter]
  PG --> DB[(🗺️ PostGIS)]
  APP -->|Outbound Port| GRAPH[🕸️ Graph Adapter]
  GRAPH --> NEO[(Neo4j)]
  APP -->|Outbound Port| OBJ[📦 Object Store Adapter]
  OBJ --> STORE[(COG/PMTiles/GeoParquet)]
```

**Why this matters:** KFM intentionally uses a **hybrid storage strategy**:
- PostGIS = fast spatial + time queries and tile serving 🐘  
- Catalogs (STAC/DCAT) = authoritative metadata + access rules 🗂️  
- Graph (Neo4j) = relationships and narrative context 🕸️  

---

## 🗂️ Catalog-driven access

A core safety/design rule:

> **The adapter should not accept raw table names from user requests.**  
> It should accept a **dataset_id / layer_id**, then resolve to an allowlisted table/view using catalog configuration (STAC/DCAT), including CRS, geometry column, and sensitivity label.

### 🧠 Why?
- Prevents SQL injection-by-design 🔒  
- Prevents “bypass the catalog” access to restricted tables 🚫  
- Keeps PostGIS + repo metadata in sync for reproducibility 🧾

> [!TIP]
> Prefer querying **views** (or materialized views) that already embed redaction and row-level rules, rather than raw tables.

---

## ⚙️ Configuration

> [!NOTE]
> Names below are **recommended defaults** if your repo doesn’t already standardize env keys.

### Environment variables (recommended)

- `POSTGIS_URL` (preferred single DSN)
  - Example: `postgresql://user:pass@localhost:5432/kfm?sslmode=disable`
- Or the split form:
  - `POSTGIS_HOST`, `POSTGIS_PORT`
  - `POSTGIS_DB`, `POSTGIS_USER`, `POSTGIS_PASSWORD`
  - `POSTGIS_SSLMODE` (`disable|require|verify-full`)

### Safety/perf knobs

- `POSTGIS_POOL_MIN` / `POSTGIS_POOL_MAX`
- `POSTGIS_STATEMENT_TIMEOUT_MS` (⚠️ default to something non-infinite)
- `POSTGIS_QUERY_LOG=true|false`
- `POSTGIS_APP_NAME=kfm_server` (helps trace queries in Postgres logs)

---

## 🐳 Local development

### Option A: Docker (recommended) 🐳

```yaml
# docker-compose.postgis.yml (example)
services:
  postgis:
    image: postgis/postgis:16-3.4
    environment:
      POSTGRES_DB: kfm
      POSTGRES_USER: kfm
      POSTGRES_PASSWORD: kfm
    ports:
      - "5432:5432"
    volumes:
      - postgis_data:/var/lib/postgresql/data
volumes:
  postgis_data:
```

### Enable extensions (first-time init) 🧩

```sql
CREATE EXTENSION IF NOT EXISTS postgis;
CREATE EXTENSION IF NOT EXISTS postgis_topology;
```

> [!TIP]
> If you maintain multiple domains, use dedicated schemas like `geo`, `hydro`, `hazards`, etc. 🗂️

---

## 🧱 Schema and migrations

This adapter is the **home** for DB shape decisions that directly affect how the server serves data:

- `schema.sql` ✅ baseline bootstrapping for a new environment
- `migrations.sql` or `migrations/` ✅ forward-only changes
- optional: `seed/` scripts that load small canonical datasets

### Reproducibility rule 🧾
If a pipeline inserts data directly into PostGIS (instead of deriving solely from repo files), it should also:
- export processed artifacts (GeoJSON/Parquet/PMTiles/COG), **or**
- store “receipts” (PROV) so the database can be reconstructed by replaying the pipeline.

---

## 🧠 Query patterns

> [!IMPORTANT]
> Every query here should be **parameterized** (no string concatenation), and should return a **provenance envelope** that includes dataset_id, template id, parameters, and sensitivity label.

### 📦 GeoJSON feature queries

**Bounding box filter (pattern):**
```sql
SELECT
  feature_id,
  properties,
  ST_AsGeoJSON(ST_Transform(geom, 4326)) AS geom_geojson
FROM <view_or_table>
WHERE geom && ST_MakeEnvelope($1, $2, $3, $4, 4326)      -- bbox prefilter (index-friendly)
  AND ST_Intersects(geom, ST_MakeEnvelope($1, $2, $3, $4, 4326))
LIMIT $5;
```

**Key notes:**
- `&&` gives a fast index-backed bbox prefilter ✅
- Use `ST_AsGeoJSON` only at the edge (adapter boundary), not in upstream logic

### 🕰️ Time range queries

KFM’s timeline slider and event views rely on consistent date handling:
- Always index timestamp columns 📈
- Support `start <= t < end` patterns (half-open intervals)

```sql
SELECT *
FROM <view_or_table>
WHERE timestamp >= $1
  AND timestamp <  $2
ORDER BY timestamp DESC
LIMIT $3;
```

> [!TIP]
> Consider a “latest reading” helper query for real-time dashboards (e.g., gauges / sensors), but keep it **bounded** and **indexed**.

### 🧩 Vector tiles (MVT)

KFM supports a PostGIS-powered tile service pattern such as:

- `/tiles/<layer>/{z}/{x}/{y}.pbf` 🧩

**MVT query skeleton (typical):**
```sql
-- NOTE: this is a reference pattern; adjust SRIDs & layer fields as needed.
WITH
  bounds AS (
    SELECT ST_TileEnvelope($1, $2, $3) AS geom_3857
  ),
  mvtgeom AS (
    SELECT
      feature_id,
      class,
      ST_AsMVTGeom(
        ST_Transform(t.geom, 3857),
        bounds.geom_3857,
        4096,
        64,
        true
      ) AS geom
    FROM <view_or_table> t, bounds
    WHERE ST_Intersects(ST_Transform(t.geom, 3857), bounds.geom_3857)
  )
SELECT ST_AsMVT(mvtgeom, $4, 4096, 'geom') AS tile;
```

**Practical tips:**
- Keep tile queries “thin”: only return styling fields actually needed in the client 🎨
- Maintain layer-specific SQL templates (tiles behave differently per dataset) 🧰

### 📊 Summary stats

Focus Mode and dashboards often need:
- counts by category
- histograms
- min/max summaries
- “top N” aggregates by bbox/time

Example: **count by class in bbox**
```sql
SELECT class, COUNT(*) AS n
FROM <view_or_table>
WHERE geom && ST_MakeEnvelope($1, $2, $3, $4, 4326)
GROUP BY class
ORDER BY n DESC;
```

---

## 🛡️ Governance and security

### 🔐 Policy principles (KFM-aligned)

- **Fail-closed** by default ✅  
  If policy metadata is missing, deny or return a safe minimal response.
- **Sensitivity propagation** 🏷️  
  _“No output may be less restricted than its inputs.”_ If a dataset is restricted, derived outputs inherit restrictions.
- **No bypass paths** 🚫  
  UI never hits PostGIS directly. The adapter is a controlled boundary.

### 🧷 Parameterized SQL only

✅ Good: placeholders + bound parameters  
❌ Bad: string concatenation of user input

### 🧾 Query auditing and inference control (recommended)

For high-risk datasets (or aggregated views that could leak sensitive information):
- log queries + results summaries 🪪
- deny queries that violate thresholds (e.g., too-small population group) 🧯
- optionally apply differential privacy/noise to aggregates when policy requires it 🧪

### 🫥 Redaction patterns (examples)

Depending on policy label, use one or more:
- column suppression (don’t select sensitive fields) 🚫
- geometry generalization (snap/round/centroid) 📉
- spatial downsampling (return fewer features) 🎛️
- enforce minimum-area or minimum-count thresholds for aggregate outputs 📊

---

## 🚀 Performance playbook

### 🧱 Indexes that usually matter

- `GIST (geom)` for geometry columns 🗺️
- `BTREE (timestamp)` for time series 🕰️
- composite where useful: `(timestamp, station_id)` etc. 🔩

### 🧩 Tiling strategy

Use the right tool for the job:

- **On-the-fly MVT** ✅  
  Great for moderate-sized layers, frequently updated data, and dynamic filtering.
- **Static PMTiles** ⚡  
  Great for huge layers / heavy generalization needs. Serve as a static artifact (and keep PostGIS for query + validation).
- **GeoParquet** 📦  
  Great for analytics/offline processing and “packaged” datasets.

> [!TIP]
> If tile load becomes a bottleneck, consider:  
> 1) generalized geometry tables by zoom, 2) materialized views, or 3) generating PMTiles in pipelines.

---

## 🧪 Testing

Minimum recommended coverage:

- ✅ connection + healthcheck
- ✅ bbox query returns valid GeoJSON geometry
- ✅ tile route returns `application/x-protobuf` and non-empty bytes
- ✅ time range filtering honors bounds
- ✅ policy gate blocks restricted output if headers/roles insufficient
- ✅ performance guardrails (timeouts, max features per request)

> [!NOTE]
> Run tests against a disposable PostGIS container so CI remains deterministic 🧰.

---

## ➕ Adding a new PostGIS-backed layer

### ✅ Checklist (PR-friendly)

- [ ] Create table/view (prefer views for redaction) 🧱  
- [ ] Geometry SRID confirmed (commonly 4326 for interchange) 🌍  
- [ ] Spatial index added (`GIST`) 🗺️  
- [ ] Time index added if applicable 🕰️  
- [ ] Register dataset in catalog (STAC/DCAT) 🗂️  
- [ ] Add provenance receipt (PROV) 🧾  
- [ ] Add layer SQL template(s): GeoJSON / tile / stats 🧰  
- [ ] Add tests + fixtures 🧪  
- [ ] Confirm policy behavior for restricted data 🛡️  

### Example schema snippet (from KFM patterns)

```sql
CREATE TABLE geo_counties (
  county_id   TEXT PRIMARY KEY,
  name        TEXT,
  population  INTEGER,
  geom        Geometry(Polygon, 4326)
);

SELECT AddGeometryColumn('geo_counties', 'geom', 4326, 'POLYGON', 2);

CREATE INDEX idx_counties_geom ON geo_counties USING GIST(geom);

-- Example insert pattern
INSERT INTO geo_counties (county_id, name, population, geom)
VALUES ($1, $2, $3, ST_GeomFromGeoJSON($4));
```

---

## 🧯 Troubleshooting

### “function st_* does not exist”
- PostGIS extension not enabled (`CREATE EXTENSION postgis;`) 🧩

### Slow bbox queries
- Missing `GIST` index on `geom` 🗺️  
- bbox predicate not written in an index-friendly way (`&&` + `ST_Intersects`) 📉  
- stats out of date (`ANALYZE`) 📈

### Tiles are empty at some zooms
- Geometry SRID mismatch (4326 vs 3857 transforms) 🌍  
- Over-aggressive filters (time window too narrow) 🕰️  
- Geometry invalid (check `ST_IsValid`) 🧱

### “statement timeout”
- Your query is too expensive or missing indexes ⏱️  
- Consider returning fewer fields/features, or move to PMTiles for that layer ⚡

---

## 📚 Glossary

- **PostGIS** 🐘: PostgreSQL extension for spatial types + spatial functions
- **MVT** 🧩: Mapbox Vector Tile (protobuf) for fast map rendering
- **STAC/DCAT** 🗂️: metadata catalogs (what exists, where it came from, how to use it)
- **PROV** 🧾: provenance records (“receipts” describing what was loaded/derived)
- **RLS** 🔐: row-level security (Postgres feature for per-row access control)
- **Focus Mode** 🎯: KFM mode where AI + data queries are combined into explainable answers with citations
