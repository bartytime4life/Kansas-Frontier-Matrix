# `infra/bootstrap/overlays` — Cluster Bootstrap Overlays

![Kustomize](https://img.shields.io/badge/Kustomize-supported-blue)
![GitOps](https://img.shields.io/badge/GitOps-bootstrap-informational)
![KFM](https://img.shields.io/badge/KFM-governed%20infra-critical)

> [!IMPORTANT]
> This folder is **cluster bootstrap**. Changes here can affect **cluster-wide behavior**. Treat edits like production changes (PR review, validation, and audit notes).

---

## What lives here

This directory contains **Kustomize overlays** used to bootstrap a Kubernetes/OpenShift cluster for KFM.

**Conceptual split (pattern):**
- `infra/bootstrap/base/` → shared bootstrap install YAML (baseline)
- `infra/bootstrap/overlays/<overlay>/` → overlay deltas that tailor bootstrap to a cluster/environment (GitOps controller configuration, bootstrap wiring, etc.)

This mirrors a common GitOps repo pattern where:
- the **base** holds the common install configuration, and  
- the **overlay** holds the controller/environment deltas.

---

## Directory layout

```text
infra/
└── bootstrap/
    ├── base/                      # shared bootstrap install YAML (baseline)
    └── overlays/
        ├── README.md              # you are here
        ├── default/               # minimal/typical bootstrap overlay
        │   ├── kustomization.yaml
        │   └── patches/           # optional (recommended) overlay-only changes
        └── <cluster-or-env>/      # additional overlays (dev/prod OR per-cluster)
            ├── kustomization.yaml
            └── patches/
```

### Overlay naming conventions

| Overlay name | Use when | Notes |
|---|---|---|
| `default` | smallest viable bootstrap | keep it minimal; good “template” |
| `dev`, `stage`, `prod` | environment-based divergence | preferred if multiple clusters share env config |
| `<cluster-id>` | cluster-specific divergence | use if cluster differs materially (OIDC, domain, RBAC groups, etc.) |

> [!NOTE]
> Prefer expressing differences in **directories (overlays)** rather than branching strategy. Overlays are the unit of divergence.

---

## Quick start

### Prerequisites ✅
- `kubectl` configured for the target cluster
- Correct context selected: `kubectl config current-context`
- Permissions to create the bootstrap resources (often requires cluster-admin for initial bootstrap)
- Optional: `kustomize` CLI for local rendering (kubectl has Kustomize support built in)

### Render (recommended) 👀

```bash
# From repo root:
kubectl kustomize infra/bootstrap/overlays/<overlay> > /tmp/kfm-bootstrap.rendered.yaml

# Quick sanity checks:
wc -l /tmp/kfm-bootstrap.rendered.yaml
head -n 40 /tmp/kfm-bootstrap.rendered.yaml
```

### Apply 🚀

```bash
# Optional: server-side dry-run (best “will it apply?” check)
kubectl apply --dry-run=server -f /tmp/kfm-bootstrap.rendered.yaml

# Apply via -k
kubectl apply -k infra/bootstrap/overlays/<overlay>
```

### Rollback / undo ♻️

```bash
# Typical GitOps rollback: revert the commit, then re-apply.
# For bootstrap specifically (before the controller is healthy), re-apply the previous known-good overlay.
kubectl apply -k infra/bootstrap/overlays/<previous-overlay-or-reverted-state>
```

---

## How an overlay should be structured

Each overlay directory MUST include a `kustomization.yaml` that composes the shared base plus overlay deltas:

- Include the shared base (`../../base`)
- Apply deltas via `patches`, `patchesStrategicMerge`, or `patchesJson6902`
- Keep cluster/environment-specific values **in the overlay** (not in base)

> [!TIP]
> Prefer `resources:` over `bases:` in modern Kustomize, but be consistent with the Kustomize version used in your toolchain.

### Minimal example

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

resources:
  - ../../base

patches:
  - path: patches/gitops-controller-config.yaml
```

### What belongs in an overlay

Overlay-only deltas often include:

- Ingress / route / domain values
- Identity provider / OIDC settings (non-secret references only)
- Git repository endpoints for the controller to watch
- Cluster-specific RBAC bindings (groups/users)
- Resource sizing/tuning for the controller
- Network policy deltas needed for the cluster

Keep **shared** items in `../base/`.

---

## Adding a new overlay

1. Copy `default/` to a new overlay directory:
   - `dev/`, `stage/`, `prod/`, or a cluster ID.
2. Edit the new overlay’s `kustomization.yaml`:
   - ensure it includes `../../base`
   - add patches under `patches/`
3. Render + validate:
   - `kubectl kustomize infra/bootstrap/overlays/<name> > /tmp/rendered.yaml`
   - `kubectl apply --dry-run=server -f /tmp/rendered.yaml`
4. PR requirements:
   - describe what changed
   - include risk + rollback notes
   - include validation output (render count + dry-run success)

### Definition of Done ✅

- [ ] Overlay renders: `kubectl kustomize infra/bootstrap/overlays/<name>` succeeds
- [ ] Server-side dry-run succeeds: `kubectl apply --dry-run=server -f …`
- [ ] No plaintext `Secret` objects committed
- [ ] Cluster-wide resources (CRDs, ClusterRoles, admission policies, webhooks) are explicitly called out in the PR
- [ ] Any policy checks / linters used by infra CI pass (if present)

---

## Governance & security guardrails

> [!WARNING]
> **Do not commit plaintext Kubernetes `Secret` objects** to Git.
>
> Use encrypted/sealed secrets or store only references to external secret managers.

Additional guidance:
- Treat this directory as **privileged infrastructure** (review required).
- Prefer least-privilege RBAC; avoid wildcard `ClusterRole` grants unless justified.
- Keep sensitive environment details out of the repo when possible (especially credentials).

---

## Troubleshooting

<details>
<summary><strong>Common failures & quick fixes</strong></summary>

### “accumulating resources” / missing file
- Check relative paths in `kustomization.yaml` (paths are resolved from the overlay directory).

### “no matches for kind …”
- The cluster may not have a required CRD yet.
- Bootstrap sequencing may need to install CRDs before applying CRs.

### Output is unexpectedly huge
- Ensure the overlay isn’t pulling in unrelated directories via `resources:`.

</details>

---

## References

- Kustomize docs: https://kubectl.docs.kubernetes.io/references/kustomize/
- `kubectl apply -k`: https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/
