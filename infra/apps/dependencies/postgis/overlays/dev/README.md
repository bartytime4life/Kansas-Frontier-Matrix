# PostGIS Dev Overlay

![env](https://img.shields.io/badge/env-dev-blue)
![dependency](https://img.shields.io/badge/dependency-PostGIS-336791)
![gitops](https://img.shields.io/badge/GitOps-Kustomize-informational)
![scope](https://img.shields.io/badge/scope-infra%2Fdependencies-lightgrey)

> **Path:** `infra/apps/dependencies/postgis/overlays/dev`  
> **Purpose:** Development overlay (Kustomize) for the **PostGIS** dependency used by Kansas Frontier Matrix (KFM).

---

<details>
<summary><strong>Table of contents</strong></summary>

- [Overview](#overview)
- [Design rules](#design-rules)
- [Directory layout](#directory-layout)
- [Deploy](#deploy)
- [Validate](#validate)
- [Connect](#connect)
- [Reset](#reset)
- [Secrets and credentials](#secrets-and-credentials)
- [Governance and security](#governance-and-security)
- [Change checklist](#change-checklist)
- [Troubleshooting](#troubleshooting)

</details>

---

## Overview

This directory contains the **dev** Kustomize overlay for deploying PostGIS as a **cluster-internal dependency**.

It is intended for:
- local/dev clusters
- preview namespaces
- CI ephemeral environments
- developer debugging and schema iteration

It is **not** intended for:
- production use
- high-availability, multi-replica DB patterns
- public exposure via Route/Ingress

> [!NOTE]
> In GitOps/Kustomize workflows, the **base** contains the shared manifests and this overlay should contain only the **dev-specific deltas** (resource sizing, storage class/size, image tag pinning, dev-only policies).

---

## Design rules

| Rule | Why it matters | What to do in this overlay |
|---|---|---|
| Keep deltas small | Reviewable PRs, fewer drift bugs | Patch only what differs from `../../base` |
| No plaintext secrets in Git | Prevent credential leakage | Use External Secrets / sealed secrets / out-of-band secret creation |
| No public DB exposure | Protect governed data | Avoid `Route`, `Ingress`, or `LoadBalancer` for PostGIS |
| Default-deny mindset | Trust membrane + least privilege | Prefer NetworkPolicy and scoped ServiceAccounts |
| Easy teardown | Dev should be disposable | Make reset steps explicit and safe |

---

## Directory layout

This overlay is expected to sit on top of the PostGIS **base**:

```text
infra/
└─ apps/
   └─ dependencies/
      └─ postgis/
         ├─ base/
         │  ├─ kustomization.yaml
         │  └─ ... base manifests ...
         └─ overlays/
            ├─ dev/
            │  ├─ kustomization.yaml
            │  ├─ README.md
            │  └─ patches/
            │     ├─ ...patch files...
            ├─ stage/
            └─ prod/
```

> [!TIP]
> If you’re unsure what’s being patched, run `kubectl kustomize` for this directory to see the final rendered YAML.

---

## Deploy

### Render

```bash
kubectl kustomize infra/apps/dependencies/postgis/overlays/dev > /tmp/postgis.dev.rendered.yaml
```

### Apply

```bash
kubectl apply -k infra/apps/dependencies/postgis/overlays/dev
```

### Delete

```bash
kubectl delete -k infra/apps/dependencies/postgis/overlays/dev
```

### GitOps controller usage

If you use a GitOps controller (Argo CD / Flux), point it to **this directory** as the desired state for the dev environment.

<details>
<summary><strong>Example Argo CD Application</strong></summary>

> Replace placeholders with your repo URL, namespace, and project conventions.

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: postgis-dev
spec:
  project: default
  source:
    repoURL: https://example.com/your-org/your-repo.git
    targetRevision: main
    path: infra/apps/dependencies/postgis/overlays/dev
  destination:
    server: https://kubernetes.default.svc
    namespace: kfm-dev
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
      - CreateNamespace=true
```

</details>

---

## Validate

Recommended validation steps (local or CI):

```bash
# 1) YAML renders
kubectl kustomize infra/apps/dependencies/postgis/overlays/dev >/dev/null

# 2) Server-side dry run (catches schema / admission issues)
kubectl apply --dry-run=server -k infra/apps/dependencies/postgis/overlays/dev

# 3) Ensure pods come up
kubectl get pods -n <namespace>

# 4) Ensure service exists
kubectl get svc -n <namespace>
```

---

## Connect

> [!IMPORTANT]
> Direct DB access is for **developer debugging only**. KFM’s normal access path should be **API → policy boundary → storage**.

### Option A: Port-forward the Service

1) Identify the service name:

```bash
kubectl get svc -n <namespace>
```

2) Port-forward:

```bash
kubectl -n <namespace> port-forward svc/<postgis-service-name> 5432:5432
```

3) Connect with `psql`:

```bash
psql "host=localhost port=5432 dbname=<db> user=<user>"
```

### Option B: Exec into the DB pod

```bash
kubectl -n <namespace> get pods
kubectl -n <namespace> exec -it <postgis-pod-name> -- psql -U <user> -d <db>
```

### Quick sanity checks

```sql
SELECT version();
SELECT PostGIS_Version();
```

---

## Reset

> [!WARNING]
> Resetting typically destroys the database contents. Use only in dev.

### Soft reset

- Delete only the workload (keeps PVC):
  - `kubectl delete -k ...` then `kubectl apply -k ...`

### Hard reset

- Delete the PVC (destroys data), then re-apply the overlay:

```bash
kubectl -n <namespace> get pvc
kubectl -n <namespace> delete pvc <pvc-name>

kubectl apply -k infra/apps/dependencies/postgis/overlays/dev
```

> [!NOTE]
> Many Postgres/PostGIS images run initialization logic only when the data directory is empty. If you changed init SQL or bootstrap settings and don’t see them taking effect, a **hard reset** is often required.

---

## Secrets and credentials

> [!IMPORTANT]
> **Never** commit plaintext DB credentials to Git.

Recommended patterns:
1) **External Secrets**: store secrets in a vault/secret manager and sync into the cluster.
2) **Sealed Secrets**: commit encrypted secrets (cluster key required to decrypt).
3) **Out-of-band dev secret**: create the secret manually in the dev cluster namespace.

Minimum expectation for this overlay:
- reference a `Secret` by name (do not inline credentials)
- keep the secret name stable across environments if possible
- document the expected keys (example: `username`, `password`, `database`, `host`, `port`)

Example key contract (adjust to match your base manifests):

| Secret key | Meaning |
|---|---|
| `POSTGRES_USER` | DB username |
| `POSTGRES_PASSWORD` | DB password |
| `POSTGRES_DB` | Default database name |

---

## Governance and security

> [!WARNING]
> KFM’s governed architecture assumes a **trust membrane**: clients and UIs do not talk to storage directly. DB access should be mediated by governed APIs that apply authentication, policy evaluation, redaction, and audit/provenance logging.

Dev overlay security posture:
- Keep PostGIS **cluster-internal** (ClusterIP Service)
- Avoid Route/Ingress/LoadBalancer for DB
- Prefer NetworkPolicy restricting ingress to:
  - KFM API pods
  - KFM pipeline/worker pods
  - trusted dev tools namespaces (if absolutely necessary)

Data handling reminders:
- Do not load production sensitive datasets into dev without explicit governance approval.
- Treat dev snapshots as potentially sensitive unless proven otherwise.

---

## Change checklist

Use this list when changing anything under this overlay:

- [ ] `kubectl kustomize infra/apps/dependencies/postgis/overlays/dev` renders successfully
- [ ] `kubectl apply --dry-run=server -k ...` passes
- [ ] No credentials are committed in manifests, patches, or README
- [ ] No DB public exposure resources added (Route/Ingress/LoadBalancer)
- [ ] Storage settings are explicitly dev-appropriate (size/class)
- [ ] Resource requests/limits are dev-appropriate
- [ ] Reset instructions still match the rendered resources (PVC name, labels, selectors)
- [ ] Any new knobs are documented in this README

---

## Troubleshooting

<details>
<summary><strong>Pod stuck in CrashLoopBackOff</strong></summary>

1) Check events:
```bash
kubectl -n <namespace> describe pod <pod>
```

2) Check logs:
```bash
kubectl -n <namespace> logs <pod>
```

Common causes:
- missing secret keys referenced by env vars
- PVC not bound / wrong storage class
- permission issues on mounted volume (security context mismatch)

</details>

<details>
<summary><strong>PVC not bound</strong></summary>

```bash
kubectl -n <namespace> get pvc
kubectl -n <namespace> describe pvc <pvc>
```

Look for:
- storage class name mismatch
- insufficient capacity / quota
- provisioner errors

</details>

<details>
<summary><strong>Cannot connect from another pod</strong></summary>

```bash
kubectl -n <namespace> get svc,endpoints
kubectl -n <namespace> get networkpolicy
```

Check:
- Service selector matches pod labels
- NetworkPolicy allows ingress on 5432 from the caller namespace/labels

</details>

