<!--
KFM GOVERNED ARTIFACT ⚖️
- This README documents how *environment overlays* for the Search dependency work.
- Treat changes here as production-impacting: review via PR, validate with CI, and keep it reproducible.
-->

![Governed](https://img.shields.io/badge/Governed-YES-2ea44f)
![Kustomize](https://img.shields.io/badge/Kustomize-overlays-blue)
![Dependency](https://img.shields.io/badge/Dependency-Search%20%2B%20Vector%20Index-orange)

# Search dependency — K8s overlays

This directory contains **Kustomize overlays** for deploying the **KFM Search dependency** into Kubernetes.

KFM’s architecture expects a search subsystem that supports:
- **full‑text search** for unstructured text (docs, narrative content, dataset descriptions, etc.)
- **vector/semantic search** (embeddings) for similarity retrieval that powers evidence-first experiences (e.g., Focus Mode)

> [!IMPORTANT]
> **Trust membrane rule:** the **frontend must not** talk to Search directly. Search is a *dependency* used behind governed APIs and policy checks. Expose access only through the backend services that enforce KFM governance and authorization.

---

## Directory layout

From repo root:

```text
infra/
  apps/
    dependencies/
      search/
        k8s/
          base/
            # shared manifests for the Search engine (engine choice + core resources)
          overlays/
            README.md            # ← you are here
            dev/                 # environment-specific deltas
            stage/               # (optional)
            prod/                # environment-specific deltas
```

> [!NOTE]
> Kustomize is designed around **bases** + **overlays**:
> - `base/` contains the reusable core manifests
> - `overlays/<env>/` contains only the deltas for that environment (patches, config, scaling, storage, exposure)

---

## Quick start

### Build (render) manifests

```bash
kustomize build infra/apps/dependencies/search/k8s/overlays/dev
```

### Diff against cluster

```bash
kubectl diff -k infra/apps/dependencies/search/k8s/overlays/dev
```

### Apply

```bash
kubectl apply -k infra/apps/dependencies/search/k8s/overlays/dev
```

### Delete (use with care)

```bash
kubectl delete -k infra/apps/dependencies/search/k8s/overlays/dev
```

---

## What belongs in an overlay?

Overlays should contain **only the environment deltas**. Keep common logic in `../base`.

| Concern | Base | Overlay (dev/stage/prod) |
|---|---:|---:|
| Workload kind (Deployment/StatefulSet), Services | ✅ | 🚫 (only patch if necessary) |
| Container image + version pin | ✅ | ⚠️ Patch only for env-specific testing |
| Resource requests/limits | ✅ default | ✅ tune per env |
| Replicas, anti-affinity, PDB | ✅ defaults | ✅ tune per env |
| StorageClass, PVC size, retention | ✅ defaults | ✅ tune per env |
| Ingress/Route exposure | 🚫 or minimal | ✅ enable/disable per env |
| NetworkPolicies | ✅ baseline | ✅ tighten per env |
| Secrets wiring (names/refs) | ✅ contract | ✅ env-specific secret name refs |
| Observability toggles (exporters, scraping labels) | ✅ baseline | ✅ enable/patch per env |

---

## Governance + security guardrails

> [!WARNING]
> Search indexes can contain *derived text* (snippets, extracted metadata, embeddings). That means:
> - **policy tags must be queryable** (so the API can filter/deny results before exposure)
> - sensitive/withheld content **must not** be retrievable by unauthorized users

### Minimum guardrails per overlay

- **No public ingress by default** (prefer ClusterIP).  
- **NetworkPolicy**: allow traffic only from approved namespaces/workloads (e.g., API gateway, indexer jobs).  
- **Pod Security**: run as non-root, drop Linux capabilities, read-only root FS where feasible.  
- **Secrets**: never commit plaintext credentials or TLS keys into overlays.

> [!TIP]
> If your org uses SOPS/SealedSecrets/ExternalSecrets, overlays should reference the *secret name*, not embed secret data.

### Policy-aware indexing

If your Search schema/mappings include governance fields (recommended), ensure overlays do **not** remove them.
Examples of commonly policy-relevant fields (names are illustrative; follow the canonical catalog/provenance model in KFM):
- license / rights
- sensitivity tier / exposure intent
- CARE / consent metadata fields

---

## Operational notes

### Persistence vs rebuildability
Search is typically **rebuildable** from source-of-truth stores (catalog/provenance + stored artifacts), but teams often still use PVCs for:
- faster restarts
- reduced warm-up time
- retaining cluster-level index state

Document your stance **per environment**:
- `dev`: may accept ephemeral storage
- `prod`: usually requires persistent storage + snapshot/restore plan

### Scaling expectations
If you scale replicas/shards:
- ensure you also scale storage and resources appropriately
- ensure disruption budgets and anti-affinity rules make sense for your cluster topology

### Upgrades
Prefer upgrades via:
1. pinning a new version in `base/` (preferred)
2. using a short-lived overlay patch for canaries (if needed), then promoting into base

---

## Adding a new overlay

Create `overlays/<name>/` with a `kustomization.yaml` that references the base:

```yaml
# overlays/<name>/kustomization.yaml
resources:
  - ../../base

patches:
  # add your patches here
  - path: patch-resources.yaml
```

Recommended: keep patches small and named by intent:
- `patch-resources.yaml`
- `patch-storage.yaml`
- `patch-networkpolicy.yaml`
- `patch-exposure.yaml`

---

## Definition of Done

- [ ] `kustomize build infra/apps/dependencies/search/k8s/overlays/<env>` succeeds
- [ ] `kubectl diff -k ...` shows only intended changes
- [ ] Overlay does **not** contain plaintext secrets
- [ ] Network exposure is explicit (either intentionally internal-only or intentionally routed)
- [ ] NetworkPolicy present (or explicitly waived with a justification comment)
- [ ] Resource sizing and storage sizing are documented in the overlay
- [ ] Changes reviewed via PR (promotion is real)

---

## Troubleshooting checklist

- **Pods CrashLooping**: check resources (OOM), storage binding, and engine bootstrap logs
- **PVC Pending**: verify StorageClass exists and allows requested access modes
- **No traffic allowed**: check NetworkPolicies + namespace labels/selectors
- **Search reachable from outside** unexpectedly: check Ingress/Route patches in overlays

---

## Provenance notes

This README aligns with KFM’s governed architecture principle that Search supports **fast discovery** in a **multi-model storage** platform (spatial + graph + search) and that search should support both **keyword** and **semantic** retrieval.

If you change the operational model (engine choice, exposure model, or what is indexed), treat it as a governed decision and record it in the appropriate architecture/governance docs.
