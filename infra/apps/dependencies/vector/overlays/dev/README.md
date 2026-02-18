<!--
KFM / INFRA README (dev overlay)

Component: dependencies/vector
Overlay: dev
Intent: Provide a human+CI friendly guide for deploying the *vector search dependency* in the dev environment.

NOTE: This README is written to be implementation-agnostic (OpenSearch/Elasticsearch vectors, pgvector, or a specialized vector DB).
Verify the actual engine by inspecting ../../base.
-->

# 🧭 Vector (Dev Overlay)

![env](https://img.shields.io/badge/env-dev-blue)
![kustomize](https://img.shields.io/badge/kustomize-overlay-informational)
![gitops](https://img.shields.io/badge/gitops-Argo%20CD%20friendly-success)
![scope](https://img.shields.io/badge/scope-internal%20only-lightgrey)

This directory contains the **Kustomize overlay** for deploying the **Vector Search / Embeddings Store dependency** in the **dev** environment.

In KFM, this dependency supports **semantic retrieval** (vector similarity search) used by Focus Mode and other retrieval features. It is *not* a system of record; it is a derived index built from governed artifacts (documents/catalog entries/data products).

> [!IMPORTANT]
> **Trust membrane rule:** do **not** expose the vector store directly to browsers or external clients.
> All access must go through governed APIs/policy boundaries.

---

## 📌 What this overlay is for

This overlay exists to make the vector-store deployment **developer-friendly** while keeping the same GitOps/Kustomize pattern used across environments:

- smaller resources than production (CPU/memory/storage)
- simplified scaling (often single-replica, if the engine allows)
- environment-specific namespaces, labels, and/or storage classes
- safer defaults for exposure (ClusterIP only + port-forward for debugging)

> [!NOTE]
> The *actual* vector engine (OpenSearch/Elasticsearch vectors, pgvector, Qdrant/Weaviate/etc.) should be defined in `../../base`.
> This overlay should only contain **environment-specific patches**.

---

## 🗂️ Directory layout

```text
infra/
└── apps/
    └── dependencies/
        └── vector/
            ├── base/
            │   └── kustomization.yaml
            └── overlays/
                └── dev/
                    ├── kustomization.yaml
                    └── README.md  👈 you are here
```

---

## 🔧 What changes in `dev` vs `base`

Typical overlay changes you should expect (or add) in `overlays/dev/kustomization.yaml`:

| Area | Dev overlay intent | Guidance |
|---|---|---|
| Replicas | 1 (where safe) | Keep dev simple; scale only if dev workloads demand it |
| Resources | Lower requests/limits | Avoid starving the cluster; prevent noisy-neighbor issues |
| Storage | Smaller PVC or ephemeral (if acceptable) | If embeddings/index must persist across restarts, keep PVC |
| Exposure | ClusterIP only | Prefer `kubectl/oc port-forward` for local debugging |
| Security | Non-root, least-privilege | Don’t weaken PodSecurity defaults “just for dev” |
| Secrets | Use Secret objects | Do not embed credentials in manifests or ConfigMaps |

---

## 🚀 Deploy (manual / local validation)

Even if GitOps is the normal path, it’s useful to validate locally:

### Render (no cluster changes)

```bash
kubectl kustomize infra/apps/dependencies/vector/overlays/dev > /tmp/vector-dev.rendered.yaml
```

### Apply (to a cluster)

```bash
kubectl apply -k infra/apps/dependencies/vector/overlays/dev
```

For OpenShift:

```bash
oc apply -k infra/apps/dependencies/vector/overlays/dev
```

### Remove

```bash
kubectl delete -k infra/apps/dependencies/vector/overlays/dev
```

---

## ✅ Verify

> Replace placeholders (`<namespace>`, `<labels>`) with the actual values defined in `kustomization.yaml`.

```bash
kubectl -n <namespace> get all
kubectl -n <namespace> get pods
kubectl -n <namespace> get pvc
kubectl -n <namespace> describe pod <pod-name>
kubectl -n <namespace> logs <pod-name> --tail=200
```

Health checks are implementation-specific; if your base defines a readiness/liveness probe, use:

```bash
kubectl -n <namespace> get pod <pod-name> -o wide
kubectl -n <namespace> describe pod <pod-name> | sed -n '/Readiness/,/Conditions/p'
```

---

## 🔌 Access patterns (dev-safe)

### Preferred: port-forward for debugging

This avoids exposing the service to the wider network.

```bash
# Example pattern — update svc name + ports to match your engine
kubectl -n <namespace> port-forward svc/<vector-service> 8080:8080
```

<details>
<summary>Why port-forward instead of NodePort/Route?</summary>

- Port-forward only exists on your workstation, and stops when the command stops.
- NodePort/Route exposure is broader and easier to misconfigure.
</details>

---

## 🔐 Secrets & sensitive config

> [!WARNING]
> Do **not** pass credentials via environment variables unless the underlying engine *requires* it and you’ve confirmed logs/error pages cannot leak them.
> Prefer Kubernetes `Secret` objects and mount them as files or use secretKeyRefs with care.

Recommended dev patterns:

- `Secret` committed via a secure mechanism (e.g., sealed secrets / external secrets)  
- network policies limiting access to only the backend services that need it  
- disable public ingress/route by default

---

## 🧪 Indexing & embeddings notes

The vector store is only half of “semantic retrieval”:

- **Embeddings creation** (model choice, normalization, dimensions) usually happens in pipeline jobs or backend services.
- **Index build parameters** (HNSW/IVF tuning, distance metric, etc.) depend on the chosen engine.

Suggested dev hygiene:

- Keep an “embedding manifest” (model ID, dimension, normalization, metric) in the *pipeline* layer.
- If you change the embedding model or dimensionality, plan on **re-indexing**.

---

## 🧭 Governance notes (KFM)

- Treat indexed text snippets and embeddings as **derived artifacts**.
- Do not index restricted or culturally sensitive materials into a shared dev cluster without a governance review.
- The vector store should not become the “source of truth.” Catalogs/receipts remain canonical.

> [!TIP]
> If you’re unsure whether a dataset is safe for dev indexing, use synthetic/test corpora or a redacted subset.

---

## 🛠️ Troubleshooting checklist

### Pod won’t start / CrashLoopBackOff
- check image pull errors
- check resource requests/limits
- check mounted secrets/config files
- check storage permissions (fsGroup / runAsUser)

### PVC Pending
- check StorageClass availability
- check requested size vs cluster quotas
- if dev can tolerate it, consider ephemeral storage (engine permitting)

### Queries time out
- increase memory limits
- verify readiness probe isn’t too aggressive
- confirm the backend service is using the internal ClusterIP, not an external route

---

## 🔁 Change management

**Rule of thumb:**

- Put implementation-agnostic manifests and defaults in `../../base`
- Put dev-only tuning and shortcuts in `./overlays/dev`
- Promote changes by copying patches forward to `stage`/`prod` overlays intentionally (don’t “just reuse dev”)

### Definition of Done (DoD) ✅

- [ ] `kubectl kustomize` renders without error
- [ ] apply succeeds on a dev cluster
- [ ] pods become Ready
- [ ] no public Route/Ingress unless explicitly required
- [ ] credentials are handled via Secrets (not ConfigMaps)
- [ ] README updated if behavior/assumptions changed

---

## 📎 Notes for maintainers

If you’re adding a new patch:

1. Prefer a small `patches/*.yaml` target (Deployment/StatefulSet/PVC).
2. Avoid duplicating `base` resources in the overlay.
3. Keep naming consistent across overlays to simplify promotion.

