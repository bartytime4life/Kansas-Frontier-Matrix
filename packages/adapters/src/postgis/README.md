<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/7b3d11c1-1c35-4ca2-8f3a-9c7b23e5b3d6
title: PostGIS Adapter
type: standard
version: v1
status: draft
owners: ["kfm-platform", "data-platform"]
created: 2026-02-25
updated: 2026-02-25
policy_label: internal
related:
  - TODO: kfm://doc/<adapter-contract>
  - TODO: ../../../README.md
  - TODO: ../README.md
  - TODO: ../../../../infra/postgres
  - TODO: ../../../../docs/governance
  - TODO: ../../../../docs/policy
tags: [kfm, adapters, postgis, storage]
notes:
  - This README is intentionally conservative: it avoids claiming specific module names/APIs until wired to the repo.
  - Replace TODO links once the monorepo paths are confirmed.
[/KFM_META_BLOCK_V2] -->

# PostGIS Adapter

> **Purpose:** PostgreSQL/PostGIS-backed storage + query adapter used *behind* KFM governed APIs (never directly by UI clients).

![Status](https://img.shields.io/badge/status-draft-yellow)
![Package](https://img.shields.io/badge/package-TODO-lightgrey)
![CI](https://img.shields.io/badge/CI-TODO-lightgrey)
![Coverage](https://img.shields.io/badge/coverage-TODO-lightgrey)
![License](https://img.shields.io/badge/license-TODO-lightgrey)

**Owners:** `kfm-platform`, `data-platform`  
**Location:** `packages/adapters/src/postgis`

---

## Quick nav

- [What this adapter does](#what-this-adapter-does)
- [Architecture](#architecture)
- [Capabilities matrix](#capabilities-matrix)
- [Configuration](#configuration)
- [Usage](#usage)
- [Governance & safety](#governance--safety)
- [Development](#development)
- [Troubleshooting](#troubleshooting)
- [Directory notes](#directory-notes)

---

## What this adapter does

This adapter is the **bridge** between application code and a Postgres database with the PostGIS extension.

**In scope** (typical responsibilities):

- Connection management (pooling, retries, timeouts)
- Parameterized query execution
- Spatial helpers (SRID handling, geometry encoding/decoding)
- Migration hooks for schema + PostGIS extensions
- Health checks (readiness/liveness style queries)
- Audit-friendly query instrumentation (latency, row counts, query tags)

**Out of scope** (by design):

- Direct use by UI, map client, or “Story UI” code
- Policy decisions (redaction, row-level security rules, dataset promotion rules)
- Business logic (domain transforms should live above the adapter)

> [!WARNING]
> **Trust membrane rule:** callers must reach PostGIS **only** through a governed API boundary.  
> If you’re importing this adapter from UI/client code, that’s a layering violation.

[Back to top](#postgis-adapter)

---

## Architecture

```mermaid
flowchart TB
  UI[Map and Story UI]
  API[Governed APIs\npolicy enforcement]
  UC[Use cases\ndomain workflows]
  AD[PostGIS adapter]
  DB[(PostgreSQL\nPostGIS)]

  UI -->|HTTP| API
  API --> UC
  UC --> AD
  AD --> DB

  classDef boundary stroke-width:2px,stroke:#333;
  class API boundary;
```

### Key invariants (CI-enforced targets)

- [ ] UI clients never connect to databases directly.
- [ ] Adapter never applies data policy by itself; it accepts policy decisions from the boundary.
- [ ] All queries are parameterized.
- [ ] All writes (if enabled) emit an audit record (who/what/when/why + inputs/outputs).

[Back to top](#postgis-adapter)

---

## Capabilities matrix

> This is the *intended* capability set for a KFM PostGIS adapter. Check off as implemented.

| Category | Examples | Status |
|---|---|---|
| Connectivity | pool, timeouts, retry/backoff | ⬜ |
| Read queries | bbox queries, point-in-polygon, nearest feature | ⬜ |
| Write queries | insert/update with audit hooks | ⬜ |
| Spatial I/O | GeoJSON, WKB/WKT encoding helpers | ⬜ |
| Index support | GiST/SP-GiST guidance + smoke checks | ⬜ |
| Migrations | extension enablement, schema migrations | ⬜ |
| Observability | query timing, tags, structured logs | ⬜ |
| Safety helpers | simplification, bounding, RLS-friendly predicates | ⬜ |

[Back to top](#postgis-adapter)

---

## Configuration

> **Repo specifics are intentionally marked TODO.** Replace these with the project’s actual conventions once confirmed.

### Environment variables

| Variable | Example | Notes |
|---|---|---|
| `POSTGIS_DATABASE_URL` | `postgresql://user:pass@host:5432/db` | Preferred single-URL config. |
| `POSTGIS_POOL_MAX` | `10` | Connection pool size. |
| `POSTGIS_STATEMENT_TIMEOUT_MS` | `30000` | Abort long-running queries. |
| `POSTGIS_SSL_MODE` | `require` | If running on managed Postgres. |
| `POSTGIS_APP_NAME` | `kfm-postgis-adapter` | Helps identify DB sessions. |

### Required DB capabilities

At minimum, the DB instance must have:

- The **PostGIS extension** installed/enabled.
- A role/user with least privileges required for your workload (read-only vs read-write).

Example (DB-side):

```sql
-- run as a superuser/admin role
CREATE EXTENSION IF NOT EXISTS postgis;
CREATE EXTENSION IF NOT EXISTS postgis_topology;
-- optional extras:
-- CREATE EXTENSION IF NOT EXISTS postgis_raster;
```

[Back to top](#postgis-adapter)

---

## Usage

Because the exact TypeScript exports and interfaces are **not confirmed in this repo**, treat this section as a template.

### Typical call pattern (pseudocode)

```ts
// PSEUDOCODE ONLY: update names once the adapter contract is confirmed.

const adapter = await createPostgisAdapter({
  url: process.env.POSTGIS_DATABASE_URL,
  poolMax: Number(process.env.POSTGIS_POOL_MAX ?? 10),
  statementTimeoutMs: Number(process.env.POSTGIS_STATEMENT_TIMEOUT_MS ?? 30_000),
});

// Always parameterize.
const rows = await adapter.query(
  `select id, st_asgeojson(geom) as geom_geojson
   from places
   where st_intersects(geom, st_makeenvelope($1, $2, $3, $4, 4326))`,
  [minX, minY, maxX, maxY]
);
```

### Spatial conventions

**Strongly recommended:**

- Store geometries in a consistent SRID (commonly `EPSG:4326` or a local projected SRID) and be explicit about transforms.
- Normalize geometry validity on ingest (`ST_MakeValid`) when appropriate.
- For map delivery, return simplified geometries where appropriate (`ST_SimplifyPreserveTopology`), **but only when policy allows**.

> [!TIP]
> If your map UI expects WGS84 (`EPSG:4326`) but you store in a projected SRID, agree on one place to transform.  
> A common pattern is: store projected for analytics, transform to 4326 at the API boundary for delivery.

[Back to top](#postgis-adapter)

---

## Governance & safety

This adapter lives below the policy boundary, but it must **support** governance requirements.

### Data lifecycle zones

If your system uses lifecycle zones (Raw → Work/Quarantine → Processed → Published), the adapter should:

- Keep schemas/namespaces separated by zone (or separate databases) **(policy decision; not owned here)**.
- Support integrity checks (checksums, row counts) as queryable metadata.
- Support provenance/audit emission hooks.

### Sensitive locations

If your data includes vulnerable/private/culturally restricted locations:

- Do **not** expose exact coordinates from this layer by default.
- Prefer returning coarse geometries (simplified, buffered, or aggregated) only when explicitly requested by an authorized policy decision.

> [!NOTE]
> Exact redaction rules are **policy**, not adapter logic.  
> The adapter’s job is to make safe-by-default execution easy (e.g., helpers for simplification, bounding, and RLS-friendly predicates).

[Back to top](#postgis-adapter)

---

## Development

### Local PostGIS via Docker (example)

```yaml
# docker-compose.yml (example)
services:
  postgis:
    image: postgis/postgis:16-3.4
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: kfm
    ports:
      - "5432:5432"
```

### Minimal smoke checks

```sql
select postgis_full_version();
select st_srid(st_setsrid(st_point(0,0), 4326));
```

### Test checklist

- [ ] Unit tests: query parameterization, error mapping, retry policy.
- [ ] Integration tests: schema migration, extension presence, SRID transforms.
- [ ] Performance tests: typical tile/bbox queries, index usage.

[Back to top](#postgis-adapter)

---

## Troubleshooting

### “function st_* does not exist”

- PostGIS extension not enabled in the target DB.
- Verify with: `select postgis_full_version();`.

### Slow bbox / tile queries

- Confirm spatial index exists (GiST / SP-GiST depending on geometry).
- Confirm you’re not forcing sequential scans (check query plans).
- Consider simplifying geometries for map delivery.

### SRID mismatch / weird offsets

- Verify stored SRID: `select distinct st_srid(geom) from <table>;`
- Transform explicitly: `ST_Transform(geom, 4326)`.

[Back to top](#postgis-adapter)

---

## Directory notes

### Where it fits

This directory contains **only** the PostGIS adapter implementation and its small, focused helpers.

### Directory tree (illustrative)

> Update this tree once the actual files exist.

```text
packages/adapters/src/postgis/
  README.md
  TODO: index.ts
  TODO: client.ts
  TODO: sql/
  TODO: migrations/
  TODO: __tests__/
```

### Acceptable inputs

- Adapter configuration (connection info, timeouts)
- Query helpers and SQL fragments that are:
  - parameterized
  - unit-tested
  - free of domain policy

### Exclusions

- No UI code
- No domain logic
- No policy rules
- No dataset-specific SQL that belongs in a pipeline or a domain repository

---

## Appendix: “unknowns” to resolve (convert draft → confirmed)

- [ ] Confirm the adapter interface (types, method names, return shapes).
- [ ] Confirm the repo’s config convention and env var names.
- [ ] Confirm migration ownership (this package vs centralized migrations).
- [ ] Link to the system’s policy docs and promotion gates.
