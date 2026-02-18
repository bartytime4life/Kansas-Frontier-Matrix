# PostGIS (Stage overlay)

![KFM](https://img.shields.io/badge/KFM-governed%20infra-2ea44f)
![Component](https://img.shields.io/badge/component-PostGIS%20%2F%20PostgreSQL-4c1)
![Kustomize](https://img.shields.io/badge/kustomize-overlay-blue)
![Environment](https://img.shields.io/badge/environment-stage-orange)

> [!IMPORTANT]
> This directory is a **Kustomize overlay** for the **stage** environment.
> It should only contain *deltas* from the PostGIS **base** (patches, stage sizing, stage policies).
>
> **Trust membrane rule:** the KFM UI and external clients **must not** talk to PostGIS directly.
> Access is only via governed APIs (policy boundary + audit logging).

---

## What this overlay is for

Stage is the shared “pre-prod” environment used to validate:

- schema migrations and extension upgrades
- ingestion pipeline writes (bulk load, COPY, partitioning)
- API query patterns (spatial indexes, time filters)
- backup/restore and disaster-recovery drills
- security controls (secrets, network policy, least privilege)

Stage should be **close to production**, but it may use smaller resource requests/limits and less-expensive storage.

---

## Directory layout

```text
infra/apps/dependencies/postgis/
├── base/
│   └── ...
└── overlays/
    └── stage/
        ├── kustomization.yaml
        ├── patches/                 # strategic merge / json6902 patches (recommended)
        ├── config/                  # stage configmaps (recommended)
        ├── secrets/                 # external secret refs ONLY (no plaintext)
        └── README.md
```

> [!NOTE]
> The exact filenames above may differ. Treat this README as the intent/spec.
> Confirm the actual resources by inspecting `kustomization.yaml` in this directory.

---

## How to deploy (kubectl / kustomize)

### Prerequisites

- `kubectl` configured for the **stage** cluster/context
- `kustomize` (optional; `kubectl apply -k` is enough for most workflows)
- A secrets mechanism (External Secrets Operator / SealedSecrets / Vault) wired for stage

### Apply

```bash
# from repo root
kubectl apply -k infra/apps/dependencies/postgis/overlays/stage
```

### Diff (recommended in PRs)

```bash
kubectl kustomize infra/apps/dependencies/postgis/overlays/stage | kubectl diff -f -
```

### Rollback (GitOps preferred)

If you’re using GitOps (recommended), rollback should be done by reverting the commit or pinning the last known-good revision.

---

## Expected resources (stage)

The base + stage overlay typically produce some combination of:

| Kind | Example name | Purpose |
|---|---|---|
| `StatefulSet` (or Operator CR) | `postgis` | Database process + stable identity |
| `Service` | `postgis` | Cluster-internal access on `5432` |
| `PersistentVolumeClaim` | `postgis-data` | Durable storage |
| `ConfigMap` | `postgis-config` | Non-secret configuration |
| `Secret` (external ref) | `postgis-auth` | Credentials (NEVER plaintext in git) |
| `NetworkPolicy` | `postgis-deny-all` / `postgis-allow-api` | Enforce trust membrane |

> [!WARNING]
> **Do not** expose PostGIS via a public `LoadBalancer` in stage.
> Use `ClusterIP` + controlled ingress (port-forward / bastion / VPN) for admin access.

---

## Configuration knobs

> [!TIP]
> Keep stage configuration changes **small** and **reviewable**. If a change is needed in all environments, it belongs in `base/`.

Common stage-only overrides:

| Concern | Stage intent | Where to implement |
|---|---|---|
| Resources | smaller requests/limits than prod | patch `StatefulSet` / operator CR |
| StorageClass | stage storage class / size | PVC patch |
| Backups | enable scheduled logical backups | `CronJob` in overlay or operator setting |
| Extensions | ensure PostGIS is enabled in target DBs | init SQL or migration job |
| Network | only allow API + pipeline namespaces | `NetworkPolicy` in overlay |
| Maintenance | allow controlled restart windows | annotations / GitOps sync waves |

---

## Access patterns

### In-cluster DNS

From any pod in the allowed namespace(s):

```bash
# replace namespace if needed
psql "postgresql://$POSTGRES_USER:$POSTGRES_PASSWORD@postgis.<namespace>.svc.cluster.local:5432/<db>"
```

### Port-forward (admin only)

```bash
kubectl -n <namespace> port-forward svc/postgis 5432:5432
psql "postgresql://<user>:<pass>@localhost:5432/<db>"
```

> [!IMPORTANT]
> Admin access should be treated as **break-glass** and audited.

---

## Security and governance (stage is still governed)

Even in stage, assume data can be sensitive.

### Secrets

- ✅ Use **external secrets** (ESO/Vault/SealedSecrets) and reference them here.
- ❌ Never commit plaintext credentials.

### Least privilege

Minimum recommended roles (conceptual):

- **owner/admin**: migrations, extension install/upgrade (restricted)
- **writer**: ingestion pipelines (COPY/INSERT), no DDL
- **reader**: API query account (SELECT only)

> [!NOTE]
> If Row Level Security (RLS) is used, document policies in the schema/migrations repo.
> (RLS details are not confirmed in repo.)

### Network policy

Stage should enforce the trust membrane at the network layer:

- deny all ingress by default
- allow ingress only from:
  - governed API namespace(s)
  - ingestion/ETL namespace(s) as required

```mermaid
flowchart LR
  UI["UI / Clients"] -->|"HTTPS"| API["Governed API Gateway"]
  API -->|"SQL (internal)"| PG["PostGIS"]
  UI -. "no direct DB access" .-> PG
```

---

## Operations

### Backups

Stage should regularly test:

- logical backups (`pg_dump`) for portability
- restore drills to a new PVC / new cluster

> [!TIP]
> If production uses volume snapshots or an operator-managed backup system, stage should mirror the same mechanism.

### Upgrades

- PostgreSQL major upgrades require a formal plan (`pg_upgrade` / dump-restore / replication cutover).
- PostGIS upgrades require backups and version checks.

> [!NOTE]
> PostGIS must be enabled **per database** (`CREATE EXTENSION postgis;`).
> If you create new databases in stage, ensure extensions are applied consistently.

---

## Validation gates

### Pre-merge checklist

- [ ] `kubectl kustomize ... | kubeconform` (or equivalent) passes
- [ ] Secrets are references only (no plaintext)
- [ ] NetworkPolicy denies-by-default and only allows intended namespaces
- [ ] Resource requests/limits are set (no “best effort” pods)
- [ ] Storage class and PVC size match stage constraints

### Post-deploy smoke checks

```bash
# pods ready
kubectl -n <namespace> get pods -l app=postgis

# service exists
kubectl -n <namespace> get svc postgis

# simple query (via port-forward)
psql -c "SELECT version();"
psql -c "SELECT PostGIS_Full_Version();"
```

---

## Troubleshooting

<details>
<summary><strong>Pods crashloop / init failures</strong></summary>

- Check PVC binding and storage class
- Confirm secrets exist in the namespace and keys match the deployment
- Inspect init container logs (if present)

```bash
kubectl -n <namespace> describe pod <pod>
kubectl -n <namespace> logs <pod> -c <container>
```
</details>

<details>
<summary><strong>Cannot connect from API</strong></summary>

- Verify `NetworkPolicy` allows API namespace -> PostGIS `5432`
- Confirm service DNS name and port
- Confirm credentials + database name

</details>

---

## Ownership and change control

- Changes to this overlay are **production-adjacent** and require review.
- Prefer small commits with clear diffs.
- Record any stage-only deviations from prod in this README.

---

## Assumptions to verify (not confirmed in repo)

- Whether PostGIS is deployed as a raw `StatefulSet` vs a Postgres operator (e.g., CloudNativePG).
- The exact namespace name(s) used for stage.
- The secrets mechanism in use (ESO/Vault/SealedSecrets).
- Whether a `NetworkPolicy` baseline exists in `base/`.

If any of these assumptions are wrong, update this README to match reality (don’t let docs drift).

