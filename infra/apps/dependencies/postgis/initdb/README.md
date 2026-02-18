# PostGIS initdb (KFM)

![KFM](https://img.shields.io/badge/KFM-governed%20infra-2ea44f)
![Dependency](https://img.shields.io/badge/dependency-PostGIS-blue)
![Scope](https://img.shields.io/badge/scope-initdb%2Fbootstrap-lightgrey)

Bootstrap scripts executed by the PostGIS container entrypoint on **first initialization** (i.e., when the database volume is empty).
These scripts exist to make local development, CI, and ephemeral environments reproducible.

> [!IMPORTANT]
> **Keep this directory data-free.**
> - ✅ OK: extensions, roles, schemas, permissions, and small deterministic seed metadata (rare)
> - ❌ Not OK: loading real datasets, shapefiles/rasters, or anything requiring governed provenance & licensing
>
> KFM ingestion happens through governed pipelines + catalogs; initdb is only the *minimum structural bootstrap*.

> [!NOTE]
> **Trust membrane reminder:** PostGIS is an internal dependency. Frontend/external clients never connect directly; access flows through governed APIs.

---

## What runs, when, and why

Most Postgres/PostGIS container images support an *initdb hook directory* (commonly mounted at `/docker-entrypoint-initdb.d`).
On **first startup only**, the entrypoint:

1. Creates the database cluster (PGDATA).
2. Creates the configured database/user.
3. Executes scripts in the initdb directory in filename order.

Because initdb scripts are only executed when PGDATA is empty, you get:

- deterministic one-time bootstrap for brand new environments
- safety from accidentally reapplying destructive setup on existing persistent volumes

---

## Directory layout

```text
infra/
└─ apps/
   └─ dependencies/
      └─ postgis/
         ├─ initdb/
         │  ├─ README.md
         │  ├─ 00_extensions.sql        # (recommended)
         │  ├─ 10_roles.sql             # (recommended)
         │  ├─ 20_schemas.sql           # (recommended)
         │  ├─ 30_privileges.sql        # (recommended)
         │  └─ 90_smoke_test.sql        # (optional)
         └─ ...
```

> [!TIP]
> Use numeric prefixes (`00_`, `10_`, …) to make ordering obvious and stable.

---

## Script conventions

### ✅ Required conventions

- **Idempotent when feasible**
  - Even though initdb is “first run only,” idempotency helps during manual replays and debugging.
  - Prefer `IF NOT EXISTS` and guard blocks.
- **Fail fast**
  - SQL should stop on error (avoid “half-configured” databases).
- **No secrets**
  - No passwords, tokens, API keys, or connection strings in scripts.
  - Use environment variables + platform secret management.
- **No dataset loading**
  - Schema bootstrap only.

### ✅ Recommended naming

| File | Purpose | Notes |
|---|---|---|
| `00_extensions.sql` | Create required extensions | `postgis`, `pgcrypto` (recommended) |
| `10_roles.sql` | Create application roles | Avoid granting superuser |
| `20_schemas.sql` | Create base schemas | Keep `public` locked down |
| `30_privileges.sql` | Grants + default privileges | Prefer least privilege |
| `90_smoke_test.sql` | Optional sanity checks | Assert required objects exist |

> [!WARNING]
> Avoid putting DDL for evolving application tables here. Use a migrations workflow (Flyway/Liquibase/etc.)
> so schema changes are versioned, reviewed, and rolled out intentionally.

---

## Baseline bootstrap spec

This is the **minimum expected outcome** of initdb scripts.
Anything marked **(proposed)** is a default suggestion until confirmed elsewhere in the repo.

### Extensions

- `postgis` (required)
- `pgcrypto` (recommended; enables `gen_random_uuid()`)
- `postgis_topology` (optional; only if topology features are used)

### Schemas

Recommended baseline (**proposed**):

- `kfm` — primary application schema
- `raw` — raw-ish tables (still governed; not a dumping ground)
- `staging` — transient transforms
- `curated` — validated/served datasets
- `provenance` — lineage, citations, run logs

### Roles

Recommended baseline (**proposed**):

| Role | Intended use | Should be able to… |
|---|---|---|
| `kfm_owner` | schema owner / migrations runner | create/alter/drop in KFM schemas |
| `kfm_app_rw` | API service runtime | read/write in allowed schemas |
| `kfm_app_ro` | read-only service / analytics | read-only access |
| `kfm_auditor` | governance review | read provenance/audit metadata |

> [!IMPORTANT]
> Keep runtime roles *least-privilege*. Do not grant `CREATEDB`, `CREATEROLE`, or superuser to app roles.

---

## Example: minimal extension bootstrap

```sql
-- 00_extensions.sql
CREATE EXTENSION IF NOT EXISTS postgis;
CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- Optional
-- CREATE EXTENSION IF NOT EXISTS postgis_topology;
```

---

## Wiring it up

### Docker Compose / Podman Compose

Mount this directory into the container’s initdb hook directory.

```yaml
services:
  postgis:
    # image: <your chosen postgis image>
    volumes:
      - ./infra/apps/dependencies/postgis/initdb:/docker-entrypoint-initdb.d:ro
      - postgis-data:/var/lib/postgresql/data

volumes:
  postgis-data:
```

> [!TIP]
> Init scripts won’t re-run if `postgis-data` already contains a database.
> To replay initdb locally, stop the container and remove the volume.

### Kubernetes / OpenShift

Typical patterns:

- **ConfigMap mount** into `/docker-entrypoint-initdb.d` (good for small SQL scripts)
- **Init container** that copies scripts from an image or git-synced volume into the correct path

<details>
<summary>Example (sketch): ConfigMap-mounted init scripts</summary>

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: kfm-postgis-initdb
data:
  00_extensions.sql: |
    CREATE EXTENSION IF NOT EXISTS postgis;
    CREATE EXTENSION IF NOT EXISTS pgcrypto;
---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: postgis
spec:
  template:
    spec:
      containers:
        - name: postgis
          volumeMounts:
            - name: initdb
              mountPath: /docker-entrypoint-initdb.d
      volumes:
        - name: initdb
          configMap:
            name: kfm-postgis-initdb
```

</details>

---

## Validation gates

Run these checks in CI after the database starts.

### Quick SQL checks

```sql
-- Verify PostGIS is installed
SELECT PostGIS_Full_Version();

-- Verify schema(s) exist (adjust if you rename)
SELECT schema_name
FROM information_schema.schemata
WHERE schema_name IN ('kfm','raw','staging','curated','provenance');

-- Verify runtime roles exist
SELECT rolname
FROM pg_roles
WHERE rolname IN ('kfm_owner','kfm_app_rw','kfm_app_ro','kfm_auditor');
```

### Suggested CI/DoD checklist

- [ ] Init scripts execute cleanly on a fresh volume
- [ ] PostGIS extension is present
- [ ] No secrets committed (grep for `PASSWORD`, `TOKEN`, etc.)
- [ ] Roles follow least privilege (no unexpected elevated perms)
- [ ] Scripts are deterministic and reviewed like production code

---

## Troubleshooting

- **“My scripts didn’t run.”**
  - Most often: the DB volume already existed. Init scripts only run when PGDATA is empty.
- **“Permission denied / scripts skipped.”**
  - Ensure files are readable by the container user.
  - Ensure shell scripts (if any) are executable.
- **“PostGIS functions missing.”**
  - Confirm the `postgis` extension was created in the correct database.

---

## Governance notes

- Treat schema + privilege changes as *production changes*.
- Keep bootstrap minimal; anything affecting data semantics should be a versioned migration.
- If you introduce any tables related to sensitive locations or culturally restricted knowledge:
  - prefer to implement protections at the API/policy layer
  - and consider DB-level controls (RLS, views, or schema separation) as defense-in-depth

