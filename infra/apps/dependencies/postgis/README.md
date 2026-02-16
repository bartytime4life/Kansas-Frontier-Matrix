# PostGIS (PostgreSQL + PostGIS) — KFM Infra Dependency

![Status](https://img.shields.io/badge/status-governed-informational)
![Layer](https://img.shields.io/badge/layer-infrastructure-orange)
![Database](https://img.shields.io/badge/db-PostGIS-blue)
![GitOps](https://img.shields.io/badge/gitops-kustomize-success)

> [!IMPORTANT]
> **PostGIS runs behind the KFM trust membrane.**
> - 🚫 **Never** expose PostGIS directly to the public Internet.
> - 🚫 **Never** allow the frontend (UI) to connect to the database.
> - ✅ All access must traverse the **governed API boundary** (auth → policy → redaction/query shaping → audit/provenance logging).

---

## 0) What this directory is

This folder documents and (typically) houses the Kubernetes/OpenShift deployment assets for **PostGIS**, used as a governed spatial runtime store for the Kansas Frontier Matrix (KFM).

PostGIS is part of KFM’s **Infrastructure layer**. It backs query-time spatial needs (places, geometries, spatial joins, tile-generation queries, etc.) and supports KFM’s evidence-first UX through governed APIs.

> [!NOTE]
> Some repository specifics (exact filenames, whether you use CloudNativePG vs a StatefulSet, secret tooling, etc.) may differ.  
> Where something is uncertain, it is explicitly marked **(not confirmed in repo)** and should be adjusted to match your actual infra patterns.

---

## 1) Governance + architecture constraints (non-negotiable)

### Trust membrane rule

KFM’s trust membrane is the enforced boundary where governance happens. Every request that causes reads/writes must be:

- authenticated
- policy-evaluated (OPA policy-as-code)
- query-shaped / redacted as required
- audited and linked to provenance references

This is a build invariant and must remain test-enforced.

### Runtime store vs source-of-truth

KFM distinguishes between:
- **Artifact stores** (raw/work/processed zones; immutable/derivable truth path)
- **Runtime stores** (PostGIS + graph + search), which are *operational* stores and should be recoverable/rebuildable from processed artifacts (while still having backups and restore drills)

---

## 2) Where PostGIS fits in the KFM system

```mermaid
flowchart LR
  UI[Web UI / MapLibre] -->|HTTPS| GW[Governed API Gateway<br/>(FastAPI/GraphQL)]
  GW -->|Auth + OPA Policy<br/>Query shaping/redaction<br/>Audit + PROV refs| PG[(PostGIS)]
  GW --> OBJ[Object Storage<br/>(Raw/Work/Processed artifacts)]
  GW --> GS[Graph/Search Index]
  ETL[Ingest/ETL Jobs] -->|write via governed interfaces| GW
  ETL -->|load/refresh derived tables| PG
```

**Design intent:** PostGIS is not a “public database.” It is a controlled dependency used by backends and governed jobs.

---

## 3) Suggested repo layout (GitOps-friendly)

This follows the Kustomize base/overlay model (recommended for GitOps) **(not confirmed in repo)**:

```text
infra/
└── apps/
    └── dependencies/
        └── postgis/
            ├── README.md
            ├── base/
            │   ├── kustomization.yaml
            │   ├── service.yaml
            │   ├── statefulset.yaml              # or operator CR (CloudNativePG)
            │   ├── pvc.yaml
            │   ├── configmap.yaml                # postgresql.conf / init settings (if used)
            │   └── networkpolicy.yaml            # REQUIRED in hardened clusters
            ├── overlays/
            │   ├── dev/
            │   │   ├── kustomization.yaml
            │   │   └── patch-*.yaml
            │   ├── stage/
            │   │   ├── kustomization.yaml
            │   │   └── patch-*.yaml
            │   └── prod/
            │       ├── kustomization.yaml
            │       └── patch-*.yaml
            └── initdb/                           # mounted to /docker-entrypoint-initdb.d (container pattern)
                ├── 00_extensions.sql
                ├── 01_roles.sql
                └── 02_schemas.sql
```

> [!TIP]
> Keep secrets out of Git (plaintext). Prefer sealed secrets / SOPS / external secret stores **(not confirmed in repo)**.

---

## 4) Version targets (align image/operator choices)

KFM support docs track two practical “rails” for production planning:

| Track | PostgreSQL | PostGIS | Use when |
|------:|------------|--------:|----------|
| Latest stable | 18.x | 3.6.1 | you actively patch and track latest |
| Conservative | 17.x or 16.x | 3.5.x | you want a longer runway / wider deploy base |

> [!NOTE]
> Pin exact versions in production (image tags/operator config) and document the upgrade cadence in your platform runbook.

---

## 5) Deploying to Kubernetes/OpenShift (GitOps or manual)

### Option A — Kustomize overlays (default expectation)

> **Dev**
```bash
kubectl apply -k infra/apps/dependencies/postgis/overlays/dev
```

> **Stage**
```bash
kubectl apply -k infra/apps/dependencies/postgis/overlays/stage
```

> **Prod**
```bash
kubectl apply -k infra/apps/dependencies/postgis/overlays/prod
```

**Recommended preflight:**
```bash
kustomize build infra/apps/dependencies/postgis/overlays/dev | kubectl apply --dry-run=client -f -
```

### Option B — Operator-managed Postgres (CloudNativePG, etc.) (not confirmed in repo)

If you use an operator, the “base” typically contains the operator CR (e.g., Cluster) and the overlays adjust:
- instance count / HA settings
- storage class + PVC size
- backup integration
- resource requests/limits
- network policy and namespaces

### Required: network policy posture

Regardless of deployment style, you should enforce:
- DB service only reachable from API namespace(s) and controlled job runners
- no direct ingress
- no cross-namespace wildcard access

---

## 6) Local development (Docker Compose pattern)

KFM’s comprehensive blueprint expects local containerized development flows **(exact compose path not confirmed in repo)**.

### Common pitfalls
- **Port 5432 already in use** (local Postgres installed): change your host mapping or stop the other process.
- **Env var changes**: restart the stack (`docker compose down && docker compose up`) to apply.

### Minimal compose snippet (example pattern)
```yaml
services:
  postgis:
    image: postgis/postgis:17-3.5
    ports:
      - "5432:5432"
    environment:
      POSTGRES_DB: kfm
      POSTGRES_USER: kfm
      POSTGRES_PASSWORD: kfm
    volumes:
      - postgis-data:/var/lib/postgresql/data
      - ./infra/apps/dependencies/postgis/initdb:/docker-entrypoint-initdb.d:ro

volumes:
  postgis-data:
```

> [!IMPORTANT]
> Postgres/official-image style init scripts only run on **first** init (when the data directory is empty).  
> Treat `initdb/` as bootstrap — use migrations for ongoing changes.

---

## 7) Bootstrap SQL: enabling PostGIS + baseline roles

### 7.1 Enable extensions (per database)

PostGIS is an extension and must be enabled in each DB that needs it.

**`initdb/00_extensions.sql` (pattern)**
```sql
CREATE EXTENSION IF NOT EXISTS plpgsql;
CREATE EXTENSION IF NOT EXISTS postgis;

-- Optional modules (enable only if you truly need them)
CREATE EXTENSION IF NOT EXISTS postgis_raster;
CREATE EXTENSION IF NOT EXISTS postgis_topology;

-- Sanity check
SELECT PostGIS_Full_Version();
```

### 7.2 Least-privilege role pattern (recommended)

**`initdb/01_roles.sql` (pattern)**
```sql
-- Non-login role for read-only access
CREATE ROLE geo_readonly NOLOGIN;

-- Example: grant usage/select on a schema (adjust schema name)
GRANT USAGE ON SCHEMA geo TO geo_readonly;
GRANT SELECT ON ALL TABLES IN SCHEMA geo TO geo_readonly;
ALTER DEFAULT PRIVILEGES IN SCHEMA geo GRANT SELECT ON TABLES TO geo_readonly;

-- Login role used by the API (password managed via secret tooling)
CREATE ROLE app_user LOGIN PASSWORD 'REPLACE_ME';
GRANT geo_readonly TO app_user;
```

> [!WARNING]
> Extension creation is typically restricted (often requires superuser unless “trusted”).  
> Decide explicitly who/what is allowed to run `CREATE EXTENSION` and keep it out of app-level roles.

---

## 8) Operations runbook (minimum viable)

### Health checks
```sql
SELECT 1;
SELECT PostGIS_Full_Version();
```

### Backups: what to back up, and why

KFM’s operating model expects **two layers of backups**:
1) **Artifact backups** (raw + processed truth path; immutable snapshots + checksums)
2) **Runtime store backups** (PostGIS, etc.) — valuable for recovery speed, but treated as rebuildable from processed artifacts in worst case

**Practical baseline (logical backup)**
```bash
pg_dump -Fc -d kfm -f kfm_$(date +%F).dump
```

**Restore drill (non-prod)**
```bash
pg_restore -d kfm --clean --if-exists kfm_2026-02-16.dump
```

> [!IMPORTANT]
> Schedule restore drills. “We have backups” is not real until restore is rehearsed.

### Upgrades: PostGIS and PostgreSQL

#### PostGIS extension upgrades (soft upgrade, PostGIS 3+)
```sql
SELECT postgis_extensions_upgrade();
```

#### PostgreSQL major upgrades
Plan for a major-version workflow (pg_upgrade or dump/restore). Treat this as a change-managed platform event.

---

## 9) Performance & schema patterns (for correctness + speed)

> [!TIP]
> Spatial indexes are not optional at scale. Use GiST indexes on geometry columns and prefer index-aware operators/functions.

<details>
<summary><strong>Example schema pattern (geometry + SRID + GiST)</strong></summary>

```sql
CREATE SCHEMA IF NOT EXISTS geo;

CREATE TABLE geo.places (
  place_id bigserial PRIMARY KEY,
  name text NOT NULL,
  geom geometry(Point, 4326) NOT NULL,
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX places_geom_gix ON geo.places USING GIST (geom);
CREATE INDEX places_name_btree ON geo.places (name);
```

</details>

<details>
<summary><strong>Example: KNN search using <code>&lt;-&gt;</code> (index-assisted)</strong></summary>

```sql
WITH q AS (
  SELECT ST_SetSRID(ST_Point(-87.6298, 41.8781), 4326) AS p
)
SELECT place_id, name
FROM geo.places
CROSS JOIN q
ORDER BY geom <-> q.p
LIMIT 10;
```

</details>

---

## 10) Change control + CI expectations (Definition of Done)

When changing **PostGIS infrastructure** or **DB bootstrap/migrations**, your PR should satisfy:

- [ ] `kustomize build` (all overlays) succeeds
- [ ] No plaintext secrets committed
- [ ] NetworkPolicy enforced (no public DB access)
- [ ] Migration/upgrade plan included (if schema/extension/version changes)
- [ ] Integration tests that exercise PostGIS queries pass (spin up PostGIS in CI if required)
- [ ] Backup/restore drill steps updated if operational behavior changed
- [ ] Any governance/policy implications called out (OPA rules, redaction rules, audit fields)

---

## 11) References (internal + external)

### Internal KFM references (governed)
- **KFM – Data Source Integration Blueprint (v1.0, 2026-02-12)**: clean layers + trust membrane + promotion gates
- **KFM – Software Support (Advanced PostGIS Guide Blueprint, 2026-02-10)**: operational recipes (extensions, upgrades, security, backups)
- **GitOps/Kustomize references** (Path to GitOps / OpenShift GitOps patterns)

### External references (primary)
- PostGIS docs (administration, extensions upgrade, function reference)
- PostgreSQL docs (backup/restore, pg_upgrade)
- Postgres official Docker image docs (init semantics)
- CloudNativePG PostGIS guide (if operator-managed)

---
