# 🕸️ Neo4j Adapter (Graph Context Layer)

![Neo4j](https://img.shields.io/badge/Neo4j-Graph%20DB-008CC1?logo=neo4j&logoColor=white)
![Cypher](https://img.shields.io/badge/Cypher-Query%20Language-222222?logo=neo4j&logoColor=white)
![Python](https://img.shields.io/badge/Python-API%20Adapter-3776AB?logo=python&logoColor=white)
![Architecture](https://img.shields.io/badge/Clean%20Architecture-Integration%20Layer-6E56CF?logo=azuredevops&logoColor=white)

> 🔌 This folder contains the **Neo4j integration adapter** used by the backend API to query the **knowledge graph** (relationships, provenance-linked context, and cross-entity navigation).

---

## 🎯 Purpose

This adapter provides a **single, governed entry point** for graph operations used by the API:

- ✅ Connect to Neo4j (Bolt) and manage driver/session lifecycle  
- ✅ Run **parameterized Cypher** queries (no string-building injections)  
- ✅ Convert Neo4j records → API/domain-friendly structures  
- ✅ Keep the rest of the system independent from Neo4j specifics (drivers, query syntax, auth)

---

## 🧭 Where it sits in the system

KFM/Kansas-Matrix follows a strict boundary rule: **UI never talks to databases directly**—only the API may access Neo4j/PostGIS/etc.

```text
🖥️ UI (web)
   |
   v
🧠 API (FastAPI)
   |
   v
🕸️ Neo4jAdapter  --->  🗃️ Neo4j (Graph)
```

---

## 🧱 Non‑negotiables (Adapter Rules)

> [!IMPORTANT]
> If you change the adapter, keep these invariants intact.

- 🔐 **No secrets in code**: credentials come from env/config only  
- 🧼 **Always parameterize** Cypher (`$param`)  
- 🧩 **Queries separated from logic** (keep Cypher in dedicated query modules/files)  
- 🔁 Prefer **idempotent writes** (`MERGE`) for loaders and upserts  
- 🧾 Return deterministic shapes (stable keys/fields) so services/UI don’t break  
- 🚫 Adapter does *not* decide governance/policy—services do. Adapter only fetches/updates data.

---

## ⚙️ Configuration

### Environment variables (recommended)

> These names are conventional; match them to your project’s settings module if it differs.

```bash
# Bolt endpoint (inside docker compose network often looks like: bolt://neo4j:7687)
NEO4J_URI=bolt://localhost:7687

# Auth (use least-privilege where possible)
NEO4J_USER=neo4j
NEO4J_PASSWORD=changeme

# Optional (Neo4j v4+)
NEO4J_DATABASE=neo4j
```

### Docker Compose credential format

If you run Neo4j via Docker, you’ll commonly see:

```bash
NEO4J_AUTH=neo4j/changeme
```

---

## 🧪 Local Development Quickstart

### 1) Start services (recommended)

From repo root:

```bash
docker compose up --build
```

### 2) Open Neo4j Browser UI 🌐

```text
http://localhost:7474
```

### 3) Verify Bolt is reachable

Default Bolt port:

```text
bolt://localhost:7687
```

> [!TIP]
> If ports conflict, update mappings in `docker-compose.yml` and restart.

---

## 🧑‍💻 Usage Pattern

This adapter is meant to be called from **services/use-cases**, not directly from API routes.

### Minimal driver pattern (Python)

```python
from neo4j import GraphDatabase

def build_driver(uri: str, user: str, password: str):
    return GraphDatabase.driver(uri, auth=(user, password))

def close_driver(driver):
    driver.close()
```

### Example: read query (parameterized)

```python
def get_related_events(driver, place_id: str, database: str | None = None):
    cypher = """
    MATCH (p:Place {id: $place_id})-[:HAS_EVENT]->(e:HistoricalEvent)
    RETURN e
    ORDER BY e.date ASC
    """
    with driver.session(database=database) as session:
        result = session.run(cypher, place_id=place_id)
        return [record["e"] for record in result]
```

> [!NOTE]
> Your real implementation should map Neo4j node/relationship properties into typed models (Pydantic/dataclasses) in the service layer or in a thin mapper module.

---

## 🗂️ Recommended Folder Shape

If you’re expanding this adapter, keep concerns separated:

```text
api/
  adapters/
    neo4j/
      README.md              👈 you are here
      client.py              🔌 driver/session construction
      adapter.py             🧠 public adapter interface used by services
      queries/
        places.cypher        🗺️ place-centric traversals
        events.cypher        🗓️ event-centric traversals
        lineage.cypher       🧾 provenance/lineage traversal helpers
      mappers/
        nodes.py             🔁 Neo4j -> domain model mapping
      schema/
        constraints.cypher   🔒 uniqueness/constraints/indexes
```

> [!TIP]
> Even if you keep queries in `.py` constants initially, graduate to `queries/*.cypher` once they grow or start being shared.

---

## 🧬 Graph Modeling Conventions (Practical)

### IDs
- Prefer a stable `id` property (UUID, catalog ID, or deterministic hash)
- Use constraints so `(:Label {id})` is unique

### Labels & relationships
Keep labels semantic and relationships directional:

- `(:Place)-[:HAS_EVENT]->(:HistoricalEvent)`
- `(:Dataset)-[:DERIVED_FROM]->(:Dataset)`
- `(:StoryNode)-[:CITES]->(:EvidenceItem)`
- `(:Place)-[:MENTIONED_IN]->(:Document)`

> [!CAUTION]
> Don’t encode policy/classification logic into relationship types. Keep that in metadata/provenance and enforce decisions in the service/governance layer.

---

## 🧰 Schema / Constraints (Suggested)

Run once during provisioning:

```cypher
CREATE CONSTRAINT place_id_unique IF NOT EXISTS
FOR (p:Place) REQUIRE p.id IS UNIQUE;

CREATE CONSTRAINT event_id_unique IF NOT EXISTS
FOR (e:HistoricalEvent) REQUIRE e.id IS UNIQUE;
```

---

## 🧪 Testing Strategy

✅ Recommended approaches:

- **Unit tests**: mock adapter boundary & validate query-building/parameter usage  
- **Integration tests**: run Neo4j in CI with Docker and load a tiny fixture graph  
- **Contract tests**: ensure adapter returns stable shapes expected by services

```bash
# example (adjust to your tooling)
pytest -k neo4j
```

---

## 🧯 Troubleshooting

### “Connection refused” / can’t connect
- Neo4j not running
- Wrong host inside Docker network (`localhost` vs service name like `neo4j`)
- Bolt port not exposed

### “Unauthorized” / auth failures
- Check `NEO4J_AUTH` (container) vs `NEO4J_USER/NEO4J_PASSWORD` (app)
- Neo4j may force password change on first login depending on config

### Query performance issues
- Add constraints & indexes for common lookup keys
- Use `UNWIND` for batch writes
- Avoid returning whole subgraphs unless necessary (return IDs then hydrate selectively)

---

## 🚀 Contributing Checklist

When adding/changing Neo4j access:

- [ ] Query is parameterized (no string concat)
- [ ] Query lives in `queries/` (or is clearly isolated)
- [ ] Adapter returns deterministic shape
- [ ] Tests updated (unit + at least one integration path)
- [ ] If schema changes: update `schema/constraints.cypher` and provisioning docs

---

## 📚 Helpful References (Neo4j)

- Neo4j Python Driver docs
- Cypher manual
- Neo4j Browser & Bolt configuration

> Keep links here up to date as the stack evolves.