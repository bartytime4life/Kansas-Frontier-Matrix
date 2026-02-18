<!--
Path: infra/apps/dependencies/postgis/overlays/prod/README.md
Generated: 2026-02-18
-->

# PostGIS — Production Overlay (Kustomize)

![env: prod](https://img.shields.io/badge/env-prod-critical)
![kustomize: overlay](https://img.shields.io/badge/kustomize-overlay-blue)
![dependency: postgis](https://img.shields.io/badge/dependency-PostGIS-2b9348)

Production Kustomize overlay for the **PostGIS** dependency used by Kansas Frontier Matrix (KFM).

This directory is the **production-specific delta** (patches + settings) layered on top of the PostGIS
**base** manifests.

> ⚠️ **Production safety**
>
> - This overlay is intended to be applied by your GitOps controller (Argo CD / OpenShift GitOps / Flux).
> - Do **not** commit plain-text credentials.
> - Do **not** expose PostGIS publicly (no Ingress/Route to the DB).

---

## What this overlay is responsible for

**“Prod overlay” = environment deltas only.** Keep the base reusable; keep prod decisions explicit, reviewed,
and testable.

Typical responsibilities for prod:

- **Version pinning**: image tags/digests for PostgreSQL + PostGIS
- **Stateful storage**: PVC size, StorageClass, access modes
- **Resources**: requests/limits, (anti-)affinity, disruption budgets
- **Security**: NetworkPolicy, ServiceAccount/RBAC scoping, pod security context
- **Operations**: backups/restore hooks, monitoring endpoints, alerting integration
- **Policy posture**: internal-only connectivity; all access via governed APIs (trust membrane)

---

## Trust membrane and access invariants (KFM)

KFM treats PostGIS as **infrastructure** storage. Application and UI do **not** talk to the database directly.

**Invariant:** external clients and the frontend never access PostGIS. All reads/writes are mediated by the
governed API boundary (policy-as-code + audit/provenance).

```mermaid
flowchart LR
  UI[React/MapLibre UI] -->|HTTPS| API[Governed API Gateway\n(FastAPI/GraphQL)]
  API -->|SQL (internal)| PG[(PostGIS)]
  API -->|catalog/media| OBJ[(Object Storage)]
  API -->|search/graph| IDX[(Search / Graph Indices)]

  subgraph TM[Trust Membrane]
    API
  end
```

Practical implications for this overlay:

- PostGIS Service should be **ClusterIP** (internal) unless you have a *justified* private-network exception.
- NetworkPolicy should restrict ingress to **only** the namespaces/workloads that need DB access.
- Credentials must be injected via secrets tooling, not committed.

---

## Directory context

Recommended layout (illustrative):

```text
infra/apps/dependencies/postgis/
├── base/
│   ├── kustomization.yaml
│   └── (stateful workload + service + config)
└── overlays/
    ├── dev/
    ├── stage/
    └── prod/
        ├── kustomization.yaml
        └── README.md   <-- you are here
```

This overlay’s `kustomization.yaml` should reference the base and apply production-specific patches.

---

## Deploying this overlay

### GitOps (recommended)

Point your GitOps Application/ApplicationSet at:

```text
infra/apps/dependencies/postgis/overlays/prod
```

Promotion to production should be PR-driven with required checks.

### Manual (debug only)

From repo root:

```bash
kubectl apply -k infra/apps/dependencies/postgis/overlays/prod
# or (OpenShift)
oc apply -k infra/apps/dependencies/postgis/overlays/prod
```

> ✅ Tip: use `kustomize build ...` (or `kubectl kustomize ...`) in CI to validate render output.

---

## Required inputs (do not commit secrets)

You will almost always need *some* secrets externalized, such as:

- DB superuser password (or initial bootstrap secret)
- App role credentials (least-privilege)
- TLS materials (if you enable TLS-in-cluster for DB connections)

**Preferred patterns (pick one, consistently):**

- External Secrets Operator + cloud secret manager
- Sealed Secrets (Bitnami)
- SOPS + age/GPG (git-ops friendly)

This overlay should reference the secret *by name*, but not contain the secret material.

---

## PostGIS enablement and initialization

PostGIS is an **extension** that must be enabled **per database**.

If you rely on init SQL (for example, via `docker-entrypoint-initdb.d/` patterns or an operator bootstrap),
remember:

- Init scripts are commonly **one-time** and only run when the PG data directory is first initialized.
- For existing PVCs, changing init scripts usually has **no effect** unless you recreate the data directory.

Example init SQL (adapt to your schema strategy):

```sql
CREATE EXTENSION IF NOT EXISTS plpgsql;
CREATE EXTENSION IF NOT EXISTS postgis;
-- Optional:
-- CREATE EXTENSION IF NOT EXISTS postgis_raster;
-- CREATE EXTENSION IF NOT EXISTS postgis_topology;

SELECT PostGIS_Full_Version();
```

---

## Upgrade and migration notes (prod runbook pointers)

### PostGIS extension upgrade (PostGIS 3+)

After upgrading the underlying packages/container image, run the PostGIS extension upgrade helper in the
target database:

```sql
SELECT postgis_extensions_upgrade();
SELECT PostGIS_Full_Version();
```

If you need to pin a specific extension version, use `ALTER EXTENSION ... UPDATE TO ...` per PostGIS admin docs.

### PostgreSQL major upgrades

PostgreSQL major upgrades typically require `pg_upgrade`, dump/restore, or logical replication approaches.
Plan a maintenance window and validate rollback strategy.

> 🔁 **Always test restore**: a backup you haven’t restored is a hypothesis.

---

## Production hardening checklist

Use this checklist as a guide when (a) creating this overlay or (b) reviewing changes.

### Security

- [ ] **No public exposure** (no DB Ingress/Route; Service is internal)
- [ ] NetworkPolicy default-deny + explicit allow from KFM API workloads
- [ ] Least-privilege DB roles for apps (no superuser in runtime services)
- [ ] Secrets are externalized (no plaintext in Git)
- [ ] Pod security context is compatible with stateful storage and cluster policy

### Reliability

- [ ] PVC configured (size + StorageClass + access mode)
- [ ] Resource requests/limits set (CPU/memory)
- [ ] Readiness/liveness probes defined
- [ ] Backup job/operator configured + restore drill documented
- [ ] Disruption controls (PDB) and scheduling constraints (anti-affinity) as appropriate

### Operability

- [ ] Observability hooks (metrics endpoint/exporter/operator metrics)
- [ ] Log retention / rotation expectations understood
- [ ] Runbook links updated (upgrade + restore + incident response)

---

## Definition of Done for changes to this overlay

- [ ] `kustomize build infra/apps/dependencies/postgis/overlays/prod` renders cleanly
- [ ] No environment drift introduced into `base/`
- [ ] Secrets remain externalized (no raw values added)
- [ ] Network exposure remains internal-only
- [ ] Storage/backups verified for the intended failure modes
- [ ] Change is reviewed and gated (PR + CI) before promotion

---

## References

- *Kansas Frontier Matrix (KFM) – Data Source Integration Blueprint* (v1.0, 2026-02-12)
- *KFM – Software Support* (PostGIS/PG operational + version guidance)
- *Docker / GitOps / OpenShift* notes (Kustomize base/overlay patterns)