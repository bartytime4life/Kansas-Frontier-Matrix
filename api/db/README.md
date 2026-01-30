# 🗄️ `api/db` — Database Layer

> **Goal:** keep database access **boring, testable, and governable**.  
> This folder holds the **infrastructure adapters** that talk to PostGIS + Neo4j so the rest of the backend can stay clean.

---

## 🧭 The contract (how KFM is *supposed* to flow)

✅ **Data is born in pipelines, not in the API.**  
The “happy path” looks like:

```text
data/raw → pipelines → data/processed → data/catalog + data/provenance → database → api → web
```

🛡️ **Important rule:** the UI should never talk directly to databases. The API is the gateway where validation & governance happen.

---

## 🧩 What goes where

### 🗺️ PostGIS (PostgreSQL + PostGIS)
Use PostGIS for:
- spatial layers (points/lines/polygons)
- attribute tables + spatial indexes
- spatial queries (within, intersects, buffers, bounding boxes)
- (optional) raster + time-partitioned layers

### 🕸️ Neo4j (Graph)
Use Neo4j for:
- story graphs (story nodes ↔ events ↔ places ↔ sources)
- relationship-first queries (traversals, “related to”, “connected via”)
- linking narrative context to spatial features (via shared IDs)

✅ **Rule of thumb:**  
- **geometry + spatial filtering** → PostGIS  
- **relationships + narrative traversal** → Neo4j

---

## 📁 Expected layout

> Exact filenames can vary, but keep the responsibilities consistent.

```text
api/
└── db/
    ├── README.md            # 👈 you are here
    ├── postgis.py           # 🗺️ PostGIS repository / adapter (SQL + spatial queries)
    ├── neo4j.py             # 🕸️ Neo4j adapter (Cypher queries)
    ├── repositories.py      # 🧱 (optional) interfaces / abstract base classes
    ├── models/              # 🧬 (optional) ORM models (if you use one)
    ├── migrations/          # 🧱 (optional) schema migrations (if you use them)
    └── seeds/               # 🌱 (optional) seed loaders for dev/demo
```

---

## 🔌 How the API should use this folder

### ✅ Preferred calling pattern
- **Routes** should not contain SQL/Cypher.
- **Services** should call repository/adapters here.
- **Adapters** should be small, explicit, and easy to test.

```text
api/routes/*  →  service layer  →  api/db/*  →  PostGIS / Neo4j
```

### 🧼 “Clean adapter” checklist
- ✅ Parameterized queries only (no string-built SQL)
- ✅ Explicit input/output (Pydantic models or typed dicts)
- ✅ No business rules (those belong in services)
- ✅ Centralized connection/session handling
- ✅ Easy to mock for unit tests

---

## 🚀 Local development (Docker Compose)

### 1) Configure environment
Create a `.env` in the repo root (or use the project’s template if provided). Typical variables:

```bash
# PostGIS
POSTGRES_USER=...
POSTGRES_PASSWORD=...
POSTGRES_DB=...

# Neo4j
NEO4J_AUTH=neo4j/your_password

# Optional host overrides (inside compose network)
POSTGRES_HOST=db
NEO4J_HOST=graph
```

<details>
<summary>🧠 Notes on hostnames</summary>

Inside the Docker Compose network, services can usually reach each other by **service name**:
- PostGIS: `db`
- Neo4j: `graph`

From your host machine, you’ll typically use `localhost` + mapped ports.
</details>

### 2) Start the stack
```bash
docker-compose up --build
```

### 3) Quick verification checks

**PostGIS**
```bash
docker-compose exec db psql -U "$POSTGRES_USER" -d "$POSTGRES_DB"
```

**Neo4j**
- Open Neo4j Browser at: `localhost:7474`
- Login with: `neo4j / <your password>`

**API**
- Swagger docs typically at: `localhost:8000/docs`

---

## 🧱 Schema + migrations (recommended discipline)

Even if you’re iterating fast, treat schema changes as real changes:

### PostGIS
- Keep extensions consistent (`postgis`, possibly `uuid-ossp`, etc.)
- Use indexes intentionally (spatial indexes matter)
- Prefer additive migrations (don’t silently mutate prod tables)

### Neo4j
- Add constraints & indexes early (IDs, uniqueness, lookup speed)
- Keep node labels & relationship types consistent (document them)

<details>
<summary>🌱 Seeding strategy (dev)</summary>

For a clean dev experience, seeds should be:
- idempotent (safe to run multiple times)
- traceable (point back to processed + provenance metadata)
- minimal (enough to demo features without “mystery meat data”)
</details>

---

## 🧬 Provenance-first expectations (non-negotiable vibes)

When you add new persistence logic, assume you must answer:
- **Where did this data come from?**
- **Which processed artifact produced it?**
- **What transformation created it?**
- **What license/visibility applies?**

Practical implementation options:
- store `dataset_id` / `prov_activity_id` on records
- keep a registry table that maps “DB objects ↔ catalog/prov files”
- enforce “fail-closed” defaults (no missing provenance, no publish)

---

## 🧪 Testing

### Unit tests
- Mock adapters or run against an ephemeral test DB
- Assert queries are parameterized
- Validate “governance inputs” exist (dataset IDs, visibility flags, etc.)

### Integration tests (recommended)
Run tests against the compose stack:

```bash
docker-compose exec api pytest
```

---

## 🧯 Troubleshooting

### Port conflicts
If you already run Postgres locally, `5432` may be taken. Fix by:
- stopping local Postgres, **or**
- changing the host port mapping in `docker-compose.yml`

### Neo4j is empty
That’s normal on first boot. If no seed/load has run, the browser will look blank.

### Containers feel slow / crash
- Increase Docker memory allocation
- Large datasets can overwhelm default settings

---

## ✅ Contribution checklist (DB work)

- [ ] Add method to the correct adapter (`postgis.py` or `neo4j.py`)
- [ ] Keep the adapter thin (no business logic)
- [ ] Add tests (unit at minimum)
- [ ] Ensure provenance/citation linkage is preserved
- [ ] Update docs if you introduce new tables/labels/relationships

---

## 📚 Related project docs (recommended reading)

- `docs/architecture/system_overview.md` (system boundaries, flow)
- `docs/governance/*` (policies, visibility, compliance)
- `pipelines/` (how data gets shaped before databases see it)