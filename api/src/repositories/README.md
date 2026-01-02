# 📦 Repositories (Data Access Layer)

![Layer](https://img.shields.io/badge/layer-repositories-0ea5e9?style=flat-square)
![Pattern](https://img.shields.io/badge/pattern-Repository-8b5cf6?style=flat-square)
![Boundary](https://img.shields.io/badge/boundary-UseCases%20%E2%86%94%20DataSources-22c55e?style=flat-square)
![Rule](https://img.shields.io/badge/rule-No%20Business%20Logic%20Here-f97316?style=flat-square)

> **TL;DR** 🧭  
> This folder is the **data-access boundary** for the API. Repositories hide databases + external services behind **small, stable contracts** so the rest of the system stays clean, testable, and swappable.

---

<details>
<summary>📚 Table of contents</summary>

- [✨ What this folder is](#-what-this-folder-is)
- [✅ What belongs here](#-what-belongs-here)
- [🚫 What does not belong here](#-what-does-not-belong-here)
- [🧠 Architectural rule of thumb](#-architectural-rule-of-thumb)
- [📁 Suggested layout](#-suggested-layout)
- [🧩 Designing repository contracts](#-designing-repository-contracts)
- [🏗️ Implementations (adapters)](#️-implementations-adapters)
- [🗺️ Geospatial + GIS notes](#️-geospatial--gis-notes)
- [📈 Performance, reliability, and safety](#-performance-reliability-and-safety)
- [🔍 Observability](#-observability)
- [🧪 Testing strategy](#-testing-strategy)
- [🧰 Example (TypeScript-ish)](#-example-typescript-ish)
- [🧾 “Add a new repository” checklist](#-add-a-new-repository-checklist)
- [❓ FAQ](#-faq)

</details>

---

## ✨ What this folder is

Repositories are **adapters** that translate between:

- 🧠 **Use-cases / services** (what the system *does*)
- 🧱 **Data sources** (how the system *gets/stores data*): Postgres/PostGIS, files, queues, external APIs (remote sensing services, Earth Engine, etc.)

The goal is to keep everything above this layer **framework-agnostic** and **easy to swap**.

---

## ✅ What belongs here

- 🗃️ Database access (Postgres/PostGIS, MySQL, SQLite, etc.)
- 🌐 External service clients (remote sensing APIs, Earth Engine adapters, third-party services)
- 🧾 Query builders / SQL / ORM usage (but *contained*)
- 🧼 Mapping raw records → **domain entities** / internal DTOs
- 🧪 In-memory / fake repositories for tests and local dev
- 🧰 Transaction helpers and “unit-of-work” boundaries *when needed*

---

## 🚫 What does not belong here

- ❌ Business rules, scoring logic, decision logic, “recommendations”
- ❌ Request/response shaping (HTTP status codes, headers, Express/Nest handlers, serializers)
- ❌ UI formatting (GeoJSON presentation choices, map styling, legends)
- ❌ Cross-cutting orchestration (multi-step workflows)  
  👉 that belongs in **use-cases/services**, not in a repository method

---

## 🧠 Architectural rule of thumb

**Use-cases call repositories via small contracts.**  
Repositories should feel like “a tiny set of verbs” the use-case needs — not a full ORM surface area.

```mermaid
flowchart LR
  A[Controller / Route Handler] --> B[Use-Case / Service]
  B -->|calls contract| C[Repository Interface (Port)]
  C --> D[Repository Implementation (Adapter)]
  D --> E[(Database / PostGIS)]
  D --> F[(External API)]
```

---

## 📁 Suggested layout

> This is a *recommended* structure. Use what matches the project — the key is consistency. 🧩

```text
api/src/repositories/
├── 📄 README.md
├── 📁 contracts/                # "Ports": interfaces/types used by use-cases
│   └── 📄 *.ts
├── 📁 postgres/                 # Postgres/PostGIS implementations
│   └── 📄 *.repo.ts
├── 📁 external/                 # External APIs (Earth Engine, remote sensing, etc.)
│   └── 📄 *.client.ts
├── 📁 memory/                   # In-memory fakes (tests/dev)
│   └── 📄 *.memory.repo.ts
└── 📄 index.ts                  # Barrel exports (optional)
```

---

## 🧩 Designing repository contracts

**Keep contracts:**
- 🎯 **Use-case driven** (only what’s needed)
- 🧱 **Stable** (don’t leak DB schema details)
- 🧼 **Domain-friendly** (return entities/DTOs the domain understands)
- 🧪 **Testable** (easy to fake/mock)

### Contract design tips 💡

- Prefer intention-revealing methods:
  - ✅ `getSoilSamples(fieldId, timeRange)`
  - ✅ `listMapLayers({ bbox, year, theme })`
  - ❌ `findMany({ where: {...}, include: {...} })` (ORM leakage)

- Keep paging explicit for list endpoints:
  - `limit`, `cursor`, `offset` (choose one strategy and standardize)

- Encode uncertainty & metadata **when it matters**:
  - sensor accuracy, timestamps, CRS/SRID, provenance IDs, etc.

---

## 🏗️ Implementations (adapters)

Implementations are free to use whatever is best:
- raw SQL
- query builders
- ORMs
- HTTP SDKs
- queues / RPC calls

…but implementations must **not** force those choices onto the use-cases.

### Naming convention 🏷️

- Interfaces: `XRepository`
- Implementations: `PostgresXRepository`, `EarthEngineXRepository`, `InMemoryXRepository`

---

## 🗺️ Geospatial + GIS notes

When repositories touch geospatial data (PostGIS, GeoJSON, COG catalogs, tiles, etc.):

- 🌍 **Be explicit about CRS/SRID** at the boundary.
- 🧭 Prefer returning geometry in a **standard internal shape** (e.g., GeoJSON Geometry) and keep presentation decisions elsewhere.
- 🗺️ Push heavy spatial operations down to the database when appropriate (buffer, intersects, distance filters, bbox queries).
- 🧱 Ensure spatial indexes exist for query patterns (bbox + time is common).

---

## 📈 Performance, reliability, and safety

### Performance 🚀
- Use connection pooling (DB)
- Batch reads/writes where possible
- Avoid N+1 patterns by design (fetch “what the use-case needs”)
- Cache *carefully* (read-heavy, slow external calls), but define invalidation rules

### Reliability 🛡️
- Use timeouts for external calls
- Add retries *only* where safe (idempotent operations)
- Wrap multi-statement writes in transactions when atomicity matters

### Safety 🔐
- Always parameterize queries (no string concatenation)
- Don’t log secrets or raw tokens
- Consider redaction rules (precision coordinates, sensitive attributes) — usually applied at service/presenter level, but be mindful of what leaves the repository

---

## 🔍 Observability

Repositories are where you can cheaply add:
- ⏱️ query duration metrics
- 🧾 structured logs with correlation IDs
- 📉 counts (rows returned, cache hits)

**But:** avoid logging raw payloads when sensitive.

---

## 🧪 Testing strategy

### Unit tests ✅
- Test use-cases with **in-memory repos** or mocks
- Keep repo contracts small so mocks stay easy

### Integration tests 🧫
- Validate Postgres/PostGIS repos with a real test database
- Include a minimal seed dataset and verify:
  - geospatial filters
  - time filters
  - pagination
  - transactional behavior

### Contract tests 📜
- If multiple implementations exist (Postgres + InMemory + External), add a shared test suite that asserts the **contract behavior** is consistent.

---

## 🧰 Example (TypeScript-ish)

> ⚠️ Example only — adapt to your DB client / framework.

### 1) Contract (Port)

```ts
// contracts/soil-data.repository.ts
export interface SoilDataRepository {
  getSoilSamplesByFieldId(fieldId: string): Promise<SoilSample[]>;
}

export type SoilSample = {
  id: string;
  fieldId: string;
  collectedAt: string; // ISO
  moisture: number;
  location: { type: "Point"; coordinates: [number, number] }; // GeoJSON
};
```

### 2) Implementation (Adapter)

```ts
// postgres/postgres-soil-data.repo.ts
import type { SoilDataRepository, SoilSample } from "../contracts/soil-data.repository";

export class PostgresSoilDataRepository implements SoilDataRepository {
  constructor(private readonly db: { query: (sql: string, params: unknown[]) => Promise<{ rows: any[] }> }) {}

  async getSoilSamplesByFieldId(fieldId: string): Promise<SoilSample[]> {
    const sql = `
      SELECT id, field_id, collected_at, moisture, ST_AsGeoJSON(location)::json AS location
      FROM soil_samples
      WHERE field_id = $1
      ORDER BY collected_at DESC
    `;
    const { rows } = await this.db.query(sql, [fieldId]);
    return rows.map((r) => ({
      id: r.id,
      fieldId: r.field_id,
      collectedAt: new Date(r.collected_at).toISOString(),
      moisture: Number(r.moisture),
      location: r.location,
    }));
  }
}
```

### 3) Use-case consumes the contract (not the implementation)

```ts
// use-cases/get-soil-samples.ts
import type { SoilDataRepository } from "../repositories/contracts/soil-data.repository";

export class GetSoilSamples {
  constructor(private readonly soilRepo: SoilDataRepository) {}

  async execute(fieldId: string) {
    return this.soilRepo.getSoilSamplesByFieldId(fieldId);
  }
}
```

---

## 🧾 “Add a new repository” checklist

1. 🧠 **Start with the use-case**: what data does it *actually* need?
2. 🧩 Define/extend a **small contract** in `contracts/`
3. 🏗️ Add an implementation in the right adapter folder (db/external/memory)
4. 🧼 Map data → domain DTO/entity (don’t leak DB/SDK shapes)
5. 🧪 Add:
   - unit tests (use-case + mock)
   - integration tests (real DB) if applicable
   - contract tests if multiple implementations exist
6. 🔍 Add minimal logging/metrics hooks (duration, error count)
7. 📚 Update this README if you introduce a new category/pattern

---

## ❓ FAQ

### “Is this the same as a Git repository?”
Nope 😄 — this is the **Repository pattern** (data-access boundary), not version control.

### “Can a repository call another repository?”
Prefer **no**. If you need composition, do it in a use-case/service so dependencies stay clear.

### “Where do I put caching?”
If caching is purely a data-access concern (e.g., memoizing slow external reads), a repository decorator/adapter is fine.  
If caching changes business behavior (e.g., “use stale data if…”) it belongs in the use-case.

---

