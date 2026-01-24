# 🧪🗄️ DB Test Harness — PostGIS + Neo4j (KFM)

![DB Tests](https://img.shields.io/badge/DB%20Tests-deterministic%20%26%20governed-brightgreen)
![PostGIS](https://img.shields.io/badge/PostGIS-spatial%20SQL-blue?logo=postgresql)
![Neo4j](https://img.shields.io/badge/Neo4j-knowledge%20graph-green?logo=neo4j)
![Evidence First](https://img.shields.io/badge/STAC%20%2B%20DCAT%20%2B%20PROV-evidence--first-orange)
![Policy Gates](https://img.shields.io/badge/OPA%20%2F%20Conftest-policy%20gates-purple)

This folder contains **database-focused tests** that keep Kansas Frontier Matrix’s **hybrid datastore** (🗺️ PostGIS + 🧠 Neo4j) *correct*, *auditable*, and *safe* as the platform evolves.

KFM’s design emphasizes **provenance-first intake**, **time as a first-class filter**, and **governance-aware map delivery**—so DB tests don’t just check “does SQL run?”… they enforce the **platform invariants** that the UI + API + AI depend on. :contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}:contentReference[oaicite:2]{index=2}

---

## 🧭 What these tests protect

### ✅ Core invariants (must never break)
- **Evidence-first ingestion**: processed data is only considered “publishable” if its **STAC/DCAT/PROV** artifacts exist and pass validation/QA gates. :contentReference[oaicite:3]{index=3}:contentReference[oaicite:4]{index=4}
- **Hybrid store consistency**: PostGIS is used for spatial “heavy lifting”, while Neo4j models semantic relationships & lineage. Tests verify IDs and joins stay stable across both stores. :contentReference[oaicite:5]{index=5}:contentReference[oaicite:6]{index=6}
- **Temporal correctness**: the system treats **time as a first-class filter**; DB queries must support time-range filtering alongside spatial filters (ISO 8601). :contentReference[oaicite:7]{index=7}:contentReference[oaicite:8]{index=8}
- **Governance + sensitivity**: sensitive datasets may be hidden or generalized (e.g., archaeological points become coarse areas). Tests ensure metadata flags + redaction/generalization rules are honored. :contentReference[oaicite:9]{index=9}:contentReference[oaicite:10]{index=10}
- **Reproducible packaging**: deterministic artifacts (e.g., **GeoParquet + PMTiles**) are traceable via hashes; optionally stored as OCI artifacts with signatures. :contentReference[oaicite:11]{index=11}:contentReference[oaicite:12]{index=12}

---

## ⚡ Quickstart

> [!IMPORTANT]
> **Never point these tests at production.**  
> Use ephemeral/local containers and a dedicated test database name (e.g., `kfm_test`). 🔒

### 1) Start ephemeral DBs (recommended: Docker)
```bash
# From repo root
docker compose -f tests/db/docker-compose.yml up -d
```

### 2) Provide connection env vars
```bash
# PostGIS
export POSTGIS_URL="postgresql://postgres:postgres@localhost:5432/kfm_test"

# Neo4j
export NEO4J_URI="bolt://localhost:7687"
export NEO4J_USER="neo4j"
export NEO4J_PASSWORD="neo4j_test_password"
```

### 3) Run DB tests
```bash
# Python example (common pattern)
pytest -q tests/db

# Or: run only DB-marked tests (if markers are used)
pytest -q -m db
```

> [!TIP]
> If your repo uses a task runner, consider adding:
> ```bash
> make db-up && make test-db && make db-down
> ```
> (Names vary by repo—this README defines *the intent*.)

---

## 🗂️ Suggested folder layout (adjust to repo reality)

```text
tests/ 🧪
  db/ 🗄️
    README.md 📘 (you are here)

    docker-compose.yml 🐳
    .env.example 🔧

    postgis/ 🗺️
      migrations/ 🧱
      schema.sql 📜
      seed.sql 🌱
      tests/ ✅
        test_schema.sql
        test_spatial.sql
        test_time_filtering.sql

    neo4j/ 🧠
      constraints.cypher 🔗
      seed.cypher 🌱
      tests/ ✅
        test_constraints.cypher
        test_lineage.cypher

    fixtures/ 📦
      stac/ 🛰️
      dcat/ 🗂️
      prov/ 🧾
      sample_data/ 🧪
```

---

## 🔁 Test flow (mental model)

```mermaid
flowchart TD
  A[🐳 Boot ephemeral DBs] --> B[🧱 Apply migrations / constraints]
  B --> C[🌱 Seed minimal fixtures]
  C --> D[✅ Run PostGIS tests]
  C --> E[✅ Run Neo4j tests]
  D --> F[🔄 Cross-store consistency checks]
  E --> F
  F --> G[🧹 Teardown]
```

---

## 🧪 What we test (by category)

### 🗺️ PostGIS suite
Focus: **geospatial correctness + performance + time filtering**

Examples of checks:
- **Schema + constraints** exist for served tables (types, NOT NULLs, keys).
- **Indexes** exist for spatial + temporal filtering (e.g., GiST on geometry; indexes on date fields). :contentReference[oaicite:13]{index=13}:contentReference[oaicite:14]{index=14}
- **Geometry validity** (no invalid geometries in “published” layers). PostGIS supports validity checks (e.g., `ST_IsValid`). :contentReference[oaicite:15]{index=15}
- **Projection expectations**: internal consistency for web delivery (often WGS84), while tracking original CRS in metadata. :contentReference[oaicite:16]{index=16}
- **Raster strategy**: avoid stuffing huge rasters in DB; store/serve as COGs and keep DB for metadata/footprints. :contentReference[oaicite:17]{index=17}

**Sample SQL assertions**
```sql
-- Geometry index exists
SELECT indexname
FROM pg_indexes
WHERE tablename = 'geo_counties'
  AND indexdef ILIKE '%USING gist%';

-- Time fields are indexable + used (example pattern)
EXPLAIN ANALYZE
SELECT county_id
FROM geo_counties
WHERE valid_from <= DATE '1935-01-01'
  AND valid_to   >= DATE '1935-01-01'
  AND ST_Intersects(geom, ST_MakeEnvelope(-102, 36, -94, 40, 4326));
```

---

### 🧠 Neo4j suite
Focus: **semantic integrity + lineage + retrieval readiness**

Examples of checks:
- **Uniqueness constraints** for node IDs (Dataset/Place/Event/etc.).
- **No dangling edges** after CSV imports (relationship references must point to existing nodes). :contentReference[oaicite:18]{index=18}
- **Lineage paths** exist between datasets and their provenance relationships (graph should remain queryable for AI + UI recommendations). :contentReference[oaicite:19]{index=19}:contentReference[oaicite:20]{index=20}

**Sample Cypher assertions**
```cypher
// Example: ensure Dataset nodes have unique IDs
MATCH (d:Dataset)
WITH d.id AS id, count(*) AS c
WHERE c > 1
RETURN id, c;

// Example: no relationships to missing nodes (pattern depends on import approach)
MATCH ()-[r]->()
WHERE r.source_id IS NOT NULL AND r.target_id IS NOT NULL
RETURN count(r);
```

---

### 🔄 Cross-store consistency suite
Focus: **stable IDs + predictable joins**

Examples of checks:
- PostGIS primary keys (e.g., `county_id`) match Neo4j node keys used for “semantic enrichment.” :contentReference[oaicite:21]{index=21}
- A dataset present in catalogs produces:
  - a PostGIS table (if spatial-serving)
  - a Neo4j Dataset node + relationships
  - consistent dataset identifiers across all systems. :contentReference[oaicite:22]{index=22}:contentReference[oaicite:23]{index=23}

---

### 🔐 Governance & privacy suite
Focus: **sensitivity enforcement + query auditing patterns**

Checks inspired by KFM governance goals:
- Sensitive layers must be **flagged** and optionally **generalized** for public map delivery (e.g., hexagon/area instead of exact point). :contentReference[oaicite:24]{index=24}:contentReference[oaicite:25]{index=25}
- Optional pattern: **query auditing / inference control** for sensitive outputs (deny queries that enable disclosure). :contentReference[oaicite:26]{index=26}

> [!NOTE]
> Even if you don’t implement full differential privacy, DB tests can still enforce:
> - audit log rows exist for protected endpoints
> - “restricted” datasets can’t be fetched at raw precision by unauthorized roles
> - coarse/generalized views exist for map display

---

### 📦 Packaging & reproducibility suite
Focus: **determinism + hashes + artifact integrity**

Checks include:
- For “dual-format” packages (GeoParquet + PMTiles), ensure:
  - both artifacts exist
  - hashes match what catalogs claim
  - STAC/DCAT records reference the produced artifacts. :contentReference[oaicite:27]{index=27}
- Optional: if using OCI registries, verify artifacts can be fetched **by digest** and validated by **Cosign signatures**. :contentReference[oaicite:28]{index=28}

---

## 🧰 Writing a new DB test (golden path)

### ✅ When you add a new dataset/layer
1. Add **fixtures** (minimal but representative):
   - 1–2 features for geometry correctness
   - 2–3 timestamps for time filtering
   - 1 “edge case” geometry (multipolygon, hole, etc.)
2. Ensure the dataset has **STAC/DCAT/PROV** boundary artifacts (even for test data). :contentReference[oaicite:29]{index=29}
3. Add:
   - a PostGIS schema/migration assertion
   - a Neo4j constraint/relationship assertion (if it participates in graph context)
4. Add cross-store ID checks (if UI/AI expects semantic enrichment).

### ✅ Test naming conventions
- `test_schema_*` → structure & constraints
- `test_spatial_*` → geometry, bbox, joins, validity
- `test_time_*` → ISO 8601 ranges + performance for time-slicing
- `test_governance_*` → sensitivity, redaction/generalization
- `test_repro_*` → hashes, packaging determinism

---

## 🤖 Why DB tests matter for Focus Mode (AI)

KFM’s AI system relies on **hybrid retrieval**:
- Neo4j graph queries for relationships and multi-hop context
- PostGIS queries for spatial filtering and performant lookup  
This is essentially a Retrieval-Augmented Generation workflow over **structured stores**, not just text. :contentReference[oaicite:30]{index=30}

So if DB invariants break, Focus Mode breaks in subtle ways (wrong joins, missing lineage paths, incorrect time slices).

---

## 🧩 Project doc anchors (useful when expanding test coverage)

> [!TIP]
> If you’re unsure what to test next, scan these docs first—they define the contracts DB tests should enforce.

- 📚 **KFM Data Intake — provenance-first, deterministic ETL, policy gates** :contentReference[oaicite:31]{index=31}  
  DB tests align to the “raw is immutable + deterministic outputs + validate before publish” model. :contentReference[oaicite:32]{index=32}:contentReference[oaicite:33]{index=33}
- 🧠 **KFM AI System Overview — Neo4j + PostGIS retrieval for Focus Mode** :contentReference[oaicite:34]{index=34}  
  Neo4j graph queries + hybrid retrieval shape what integrity tests must protect. :contentReference[oaicite:35]{index=35}
- 🗺️ **KFM UI System Overview — governance-aware map delivery + 2D/3D** :contentReference[oaicite:36]{index=36}  
  Sensitive layers may be hidden/generalized; 3D tiles appear in Cesium mode—DB + metadata must support this. :contentReference[oaicite:37]{index=37}:contentReference[oaicite:38]{index=38}
- 🧱 **KFM Architecture/Features — time is first-class + offline packs** :contentReference[oaicite:39]{index=39}  
  Time-range filtering and tile caching contracts influence index/performance tests; offline packs imply reproducible tile bundles. :contentReference[oaicite:40]{index=40}:contentReference[oaicite:41]{index=41}
- 🌟 **Latest Ideas & Future Proposals — timeline MVP + GeoParquet/PMTiles + hashes** :contentReference[oaicite:42]{index=42}  
  Strengthens “packaging determinism” and “time slider correctness” test requirements. :contentReference[oaicite:43]{index=43}
- 📘 **Comprehensive Technical Documentation — WGS84 norms + sensitive handling + DB roles** :contentReference[oaicite:44]{index=44}  
  Reinforces projection/validity tests and sensitive data policies. :contentReference[oaicite:45]{index=45}:contentReference[oaicite:46]{index=46}
- 📦 **Additional Project Ideas — OCI artifacts + Cosign/ORAS** :contentReference[oaicite:47]{index=47}  
  Guides reproducibility + integrity tests for packaged tiles/data artifacts. :contentReference[oaicite:48]{index=48}
- 🧠✨ **AI Concepts & more (portfolio)** :contentReference[oaicite:49]{index=49}  
  Background AI references that inform retrieval & governance thinking. 
- 🗺️🌐 **Maps/Virtual Worlds/WebGL (portfolio)** :contentReference[oaicite:51]{index=51}  
  Background mapping + 3D/virtual world references that shape future DB + tile/asset tests. :contentReference[oaicite:52]{index=52}
- 🧑‍💻📦 **Programming languages & resources (portfolio)** :contentReference[oaicite:53]{index=53}  
  Supports polyglot tooling expectations (SQL/Cypher/Python/etc.) for the DB test harness. :contentReference[oaicite:54]{index=54}
- 🧮📚 **Data management/Bayesian methods (portfolio)** :contentReference[oaicite:55]{index=55}  
  Data governance + reproducibility + auditing concepts influencing test design. :contentReference[oaicite:56]{index=56}
- 💡 **Innovative Concepts — 3D storytelling + immersive experiences** :contentReference[oaicite:57]{index=57}  
  Reinforces future-facing tests for 3D tiles/scene assets + their provenance. :contentReference[oaicite:58]{index=58}:contentReference[oaicite:59]{index=59}

### 📎 Bonus extracted references (from the portfolios)
- 🔍 **Query auditing + inference control** (privacy/security pattern)  
  Useful if we add “restricted layer” query guards. :contentReference[oaicite:60]{index=60}
- 🧰 **PostGIS best practices** (extensions, schema separation, geometry validity checks)  
  Useful for schema + validity tests. :contentReference[oaicite:61]{index=61}:contentReference[oaicite:62]{index=62}

---

## 🆘 Troubleshooting (fast fixes)

- **Ports already in use**: change mapped ports in `tests/db/docker-compose.yml`.
- **PostGIS extension missing**: ensure the container image includes PostGIS; in bare Postgres, `CREATE EXTENSION postgis;` must succeed. :contentReference[oaicite:63]{index=63}
- **Neo4j auth failures**: reset `NEO4J_PASSWORD` / check auth config in compose.
- **Time filter tests flaky**: enforce UTC timestamps and consistent ISO 8601 parsing (store as `timestamptz` where appropriate).
- **Geometry validity failures**: inspect invalid rows and fix in pipeline; tests should block publish if invalid. :contentReference[oaicite:64]{index=64}

---

## ✅ Definition of Done (DoD) for DB changes
Before merging any DB-related change, ensure:
- [ ] migrations run clean on empty DB
- [ ] seeds/fixtures load deterministically
- [ ] PostGIS tests pass (schema + spatial + time)
- [ ] Neo4j tests pass (constraints + lineage)
- [ ] governance checks pass (sensitivity/redaction where applicable)
- [ ] (optional) artifact integrity checks pass (hashes / Cosign verification)

---

### 🧾 Appendix: KFM pipeline context (why “DB tests” aren’t isolated)

```mermaid
flowchart LR
  A["📥 Raw Sources"] --> B["🧪 ETL + Normalization"]
  B --> C["🛰️ STAC Items + Collections"]
  C --> D["🗂️ DCAT Dataset Views"]
  C --> E["🧾 PROV Lineage Bundles"]
  C --> G["🧠 Neo4j Graph (references catalogs)"]
  G --> H["🧩 API Layer (contracts + redaction)"]
  H --> I["🗺️ Map UI — React · MapLibre · (optional) Cesium"]
  I --> J["📚 Story Nodes (governed narratives)"]
  J --> K["🤖 Focus Mode (provenance-linked context)"]
```

DB tests sit inside this flow and ensure the pipeline remains **traceable** end-to-end. :contentReference[oaicite:65]{index=65}:contentReference[oaicite:66]{index=66}:contentReference[oaicite:67]{index=67}

