# KFM Platform Namespaces

This folder defines the **namespace (Kubernetes) / project (OpenShift)** boundaries used to deploy the Kansas Frontier Matrix (KFM) platform.

Namespaces are *not* the trust membrane by themselves, but they are a **critical enforcement surface** for:
- RBAC least-privilege boundaries
- network isolation defaults
- resource quotas / blast-radius control
- policy-as-code attach points (labels/annotations → enforcement)

> [!IMPORTANT]
> **KFM non‑negotiables this folder must support**
>
> - **Trust membrane:** UI/external clients never access databases directly; all access goes through the governed API + policy boundary.
> - **Fail‑closed policies:** if policy evaluation fails, requests must be denied.
> - **Evidence-first:** user-visible outputs must resolve evidence and be auditable (especially Focus Mode outputs).

---

## Folder layout

> This is the **recommended** layout for this directory. If your repo differs, update this table first.

| Path | What belongs here | Notes |
|---|---|---|
| `infra/platform/namespaces/base/` | Baseline namespaces + guardrails | Common labels, default deny network, baseline quotas |
| `infra/platform/namespaces/base/namespaces/` | `Namespace` / `Project` manifests | One file per namespace |
| `infra/platform/namespaces/base/policy/` | Default NetworkPolicies + Pod Security defaults | “deny by default” starter set |
| `infra/platform/namespaces/base/rbac/` | Shared RBAC building blocks | ServiceAccounts, Roles, RoleBindings (cluster-level RBAC lives elsewhere) |
| `infra/platform/namespaces/base/quotas/` | ResourceQuota + LimitRange profiles | “small/med/large” profiles with patching |
| `infra/platform/namespaces/overlays/` | Environment overlays | `dev/`, `stage/`, `prod/` (or per-cluster overlays) |
| `infra/platform/namespaces/overlays/<env>/` | Env-specific patches | Quota sizes, allowed egress, image registry, etc. |

<details>
<summary><strong>Suggested kustomize skeleton (example)</strong></summary>

```text
infra/
  platform/
    namespaces/
      README.md
      base/
        kustomization.yaml
        namespaces/
          kfm-platform.yaml
          kfm-ui.yaml
          kfm-data.yaml
          kfm-pipelines.yaml
          kfm-observability.yaml
        quotas/
          quota-default.yaml
          limitrange-default.yaml
        policy/
          netpol-default-deny.yaml
          netpol-allow-dns.yaml
        rbac/
          serviceaccounts.yaml
          rolebindings.yaml
      overlays/
        dev/
          kustomization.yaml
          patches/
            quota-patch.yaml
            labels-patch.yaml
        prod/
          kustomization.yaml
          patches/
            quota-patch.yaml
            labels-patch.yaml
```

</details>

---

## Namespace model

### 1) Naming conventions

**Preferred convention (proposed):**

- `kfm-<capability>` for single-environment clusters  
- `kfm-<capability>-<env>` for shared clusters with multiple environments

Examples:
- `kfm-platform` / `kfm-platform-prod`
- `kfm-data` / `kfm-data-prod`

> [!NOTE]
> If you deploy **one environment per cluster**, omit the `-<env>` suffix and track environment at the cluster level.

### 2) Required labels and annotations

These labels are used by policy-as-code, cost allocation, and operational tooling.

| Key | Example | Required | Purpose |
|---|---:|:---:|---|
| `app.kubernetes.io/part-of` | `kfm` | ✅ | Global grouping |
| `kfm.io/environment` | `dev` / `stage` / `prod` | ✅ | Policy + resource profiles |
| `kfm.io/plane` | `ui` / `platform` / `data` / `pipelines` / `observability` | ✅ | Operational intent |
| `kfm.io/data-sensitivity` | `public` / `restricted` / `sensitive-location` | ✅ | Enforcement input (redaction / access / egress) |
| `kfm.io/owner` | `platform-team` | ✅ | On-call + accountability |
| `kfm.io/change-control` | `gitops` | ✅ | Must be GitOps-managed |

---

## Suggested initial namespace registry

> This list is a **starting scaffold**. Adjust to match your actual component boundaries and governance.

| Namespace | Plane | Primary workloads | Default stance |
|---|---|---|---|
| `kfm-platform` | platform | API gateway, policy engine (OPA), auth, evidence resolver | locked down; only ingress from `kfm-ui` |
| `kfm-ui` | ui | React/MapLibre UI, static content delivery | internet-facing; no direct DB access |
| `kfm-data` | data | PostGIS, Neo4j, search index, object storage adapters | no public ingress; only from governed API |
| `kfm-pipelines` | pipelines | ingestion jobs, schedulers, ETL workers | controlled egress; write to Raw/Work/Processed storage |
| `kfm-observability` | observability | metrics, logs, traces, dashboards | privileged read of cluster telemetry |

---

## Guardrails applied to every namespace

### Network isolation

**Default rule:** deny all inbound + deny all cross-namespace traffic, then explicitly allow required flows.

Recommended minimum:
- allow DNS (to cluster DNS)
- allow ingress to publicly exposed namespaces (typically only `kfm-ui`)
- allow `kfm-ui → kfm-platform` (HTTPS)
- allow `kfm-platform → kfm-data` (DB/graph/search ports as needed)
- block everything else

> [!WARNING]
> Some OpenShift/Kubernetes network topologies are permissive by default. Do **not** assume namespaces are isolated unless you enforce it (NetworkPolicy and/or cluster network segmentation).

### RBAC

RBAC expectations:
- Devs get **namespace-scoped** access only.
- CI/CD bots get **only** the verbs/resources required.
- Data-plane namespaces (`kfm-data`) should have restricted write permissions.

Minimum objects per namespace:
- `ServiceAccount` for app workloads
- `Role` / `RoleBinding` for app-level permissions
- No cluster-admin bindings in this folder

### Resource limits

Every namespace must have:
- `ResourceQuota` (CPU/memory/pods/services)
- `LimitRange` (default requests/limits)

This prevents runaway workloads from impacting the whole cluster.

---

## GitOps workflow

This folder is intended to be deployed via GitOps (or an equivalent controlled deployment path):

1. PR changes to `base/` or an `overlays/<env>/`
2. CI validates:
   - kustomize build succeeds
   - policy checks (deny-by-default) succeed
   - required labels present
3. GitOps controller syncs to cluster

### Apply locally (for development clusters only)

```bash
# Kubernetes
kubectl apply -k infra/platform/namespaces/overlays/dev

# OpenShift (works similarly)
oc apply -k infra/platform/namespaces/overlays/dev
```

Verify:

```bash
kubectl get ns | grep '^kfm-'
kubectl -n kfm-platform get networkpolicy
kubectl -n kfm-platform describe resourcequota
```

---

## Adding a new namespace

> Treat namespace additions as **platform changes**.

### Checklist (Definition of Done)

- [ ] Namespace manifest added with required labels
- [ ] `ResourceQuota` + `LimitRange` applied (or explicitly patched)
- [ ] Default-deny NetworkPolicy applied
- [ ] Only required allow-rules added (documented)
- [ ] RBAC bindings created for:
  - [ ] workload ServiceAccounts
  - [ ] human roles (read-only / edit / admin) as applicable
- [ ] CI policy checks updated (if needed)
- [ ] Ownership recorded: `kfm.io/owner`
- [ ] Security review note added if `kfm.io/data-sensitivity != public`

---

## Common pitfalls

- **“Namespace isolation” assumption:** without NetworkPolicy and/or cluster network segmentation, pods may talk across namespaces.
- **Quota drift:** namespaces created manually without quotas become operational debt.
- **RBAC creep:** avoid “temporary admin” rolebindings that never get removed.
- **Bypassing the trust membrane:** even if network allows it, **UI must not reach databases**.

---

## Governance notes

- Namespaces that handle **restricted data or sensitive locations** must be reviewed for:
  - network egress controls
  - logging/redaction constraints
  - least-privilege service accounts
- If you are unsure whether a dataset/category is sensitive, default to **restricted** and escalate for governance review.

---

## References

This README implements KFM’s architecture and governance requirements in the **infrastructure layer** (namespaces/projects, RBAC, network, quotas) so the platform can uphold:
- policy-as-code enforcement
- trust membrane invariants
- auditable evidence-first behavior

Update this section with internal repo links as your docs stabilize (e.g., `docs/architecture/trust-membrane.md`, `docs/security/policy-as-code.md`).
