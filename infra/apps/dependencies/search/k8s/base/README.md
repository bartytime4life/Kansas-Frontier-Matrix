# Search — Kubernetes Base (`k8s/base/`) 🔎
![status](https://img.shields.io/badge/status-governed%20draft-blue?style=flat-square)
![delivery](https://img.shields.io/badge/delivery-kustomize%20base-success?style=flat-square)
![membrane](https://img.shields.io/badge/trust%20membrane-NON--NEGOTIABLE-111827?style=flat-square)
![exposure](https://img.shields.io/badge/exposure-internal%20only-critical?style=flat-square)

> **Purpose:** This directory defines the **environment-agnostic Kubernetes “base”** for the **Search** dependency (text search; optionally hybrid retrieval).
>
> **Read first:** [`infra/apps/dependencies/search/README.md`](../../README.md) — overall Search contract, governance expectations, and integration notes.

---

## Governance header

| Field | Value |
|---|---|
| Document | `infra/apps/dependencies/search/k8s/base/README.md` |
| Status | **Governed draft** |
| Version | `v0.1.0-draft` |
| Effective date | **2026-02-18** (America/Chicago) |
| Owners | `.github/CODEOWNERS` *(required; if missing → governance gap)* |
| Applies to | Search dependency cluster deployment posture (networking, storage, secrets, observability) |
| Runtime impact | Changes MAY affect cluster access paths and policy surfaces (treat as production-impacting) |

> [!IMPORTANT]
> **Trust membrane rule (non-negotiable):**
> - The **browser/UI and external clients MUST NOT** access Search directly.
> - Search is reachable **only** from KFM backends and controlled job runners (indexers), through the governed API boundary + policy/audit controls.

---

## What this `base/` is

### ✅ This is (base responsibilities)

The **Kustomize base** is meant to be:
- **Engine deployment primitives** (Deployment/StatefulSet, Service, PVCs, ConfigMaps)
- **Security posture defaults** (NetworkPolicy, PodSecurity settings, RBAC)
- **Operational hooks** (health probes, resource defaults, metrics endpoints if present)

### ❌ This is not

- Not environment sizing/HA details → those belong in `k8s/overlays/{dev,stage,prod}`
- Not app integration docs → see the parent Search README
- Not a public ingress surface → **do not** add Ingress/Route here unless it is strictly operator-only and policy-reviewed

---

## Repo reality check (engine choice)

There is a **known drift** inside the repo today:

- Local dev Compose defaults `KFM_SEARCH_URL` to a **Meilisearch** service (`http://meili:7700`).  
  See: `/docker-compose.yml` and `/.env.example`.
- The parent Search dependency README contains **OpenSearch-oriented examples** (ports/terminology).

> [!NOTE]
> This `k8s/base/` README is intentionally written to support **either**:
> 1) **Meilisearch** (text search; minimal ops), or  
> 2) **OpenSearch** (text + potential hybrid/vector; heavier ops).
>
> **Minimal verification step:** decide which engine is “real” for cluster use, then ensure:
> - manifests match the engine,
> - the API adapter matches the engine,
> - the service name + `KFM_SEARCH_URL` are documented consistently in *one place*.

---

## Expected directory layout

> [!TIP]
> Keep the tree **self-explanatory** so on-call can operate Search from this folder alone.

```text
infra/apps/dependencies/search/k8s/
├─ README.md                     # (optional) k8s-level overview (base + overlays)
├─ base/
│  ├─ README.md                  # (this file)
│  ├─ kustomization.yaml         # REQUIRED (create if missing)
│  ├─ service.yaml               # ClusterIP Service (internal only)
│  ├─ deployment.yaml            # Meilisearch (typical) OR
│  ├─ statefulset.yaml           # OpenSearch (typical)
│  ├─ pvc.yaml                   # persistent storage (recommended)
│  ├─ configmap.yaml             # engine config (optional)
│  ├─ secret.yaml                # NEVER plaintext (prefer ExternalSecrets / SOPS / SealedSecrets)
│  ├─ networkpolicy.yaml         # REQUIRED for trust membrane enforcement
│  ├─ pdb.yaml                   # (recommended) PodDisruptionBudget
│  └─ servicemonitor.yaml        # (optional) Prometheus Operator
└─ overlays/
   ├─ dev/
   │  ├─ kustomization.yaml
   │  └─ patch-*.yaml            # resources, replicas, storage size (dev)
   ├─ stage/
   │  ├─ kustomization.yaml
   │  └─ patch-*.yaml
   └─ prod/
      ├─ kustomization.yaml
      └─ patch-*.yaml            # HA, TLS, backups, strict NP, SLOs
```

> [!CAUTION]
> If `kustomization.yaml` or `networkpolicy.yaml` is missing, treat that as an **infra governance gap** (trust membrane may be unenforceable by default).

---

## Minimum secure-by-default posture

### Networking
- **Service type MUST be `ClusterIP`**
- No public Ingress/Route by default
- **NetworkPolicy MUST** restrict ingress to only:
  - the governed API namespace/workload(s)
  - pipeline/indexer workload(s) (if separate namespace)
  - observability stack (metrics scraping), if needed

### Secrets
- Master keys / admin creds **MUST NOT** be committed in plaintext
- Prefer one of:
  - ExternalSecrets operator (Vault/Cloud secret manager)
  - SOPS-encrypted manifests (repo-dependent)
  - SealedSecrets (repo-dependent)

### Storage
- Dev MAY run with smaller PVCs (or ephemeral if explicitly accepted)
- Stage/Prod SHOULD use PVCs
- Even though Search is a **derived index**, persistent storage reduces recovery time and supports rollback debugging

---

## Engine tracks

<details>
<summary><strong>Track A — Meilisearch (text search)</strong> ✅</summary>

### Default ports
- HTTP API: `7700`

### Typical K8s shape
- `Deployment` (single replica in dev; scale as needed)
- `Service` named consistently (recommended: `search` or `meili`)
- `PVC` mounted at `/meili_data` (default for the official image)

### Required secret(s)
- `MEILI_MASTER_KEY` (use dev-only key in dev; strong secret in prod)

### Health checks (examples)
- `GET /health` → should return OK

### Notes
- Keep Meilisearch **internal-only**; do not expose it to browsers.
- Access control and sensitivity filtering still belong at the API boundary.
</details>

<details>
<summary><strong>Track B — OpenSearch (hybrid-ready)</strong> 🧱</summary>

### Default ports
- REST: `9200`
- Dashboards (optional): `5601` *(operator-only; never public by default)*

### Typical K8s shape
- `StatefulSet` (storage-backed)
- `Service` (ClusterIP) + headless service if multi-node
- TLS/auth strongly recommended in prod

### Node/sysctl requirements
OpenSearch/Elasticsearch-like engines commonly require OS-level tuning (e.g., `vm.max_map_count`).
On restricted platforms (e.g., OpenShift), plan this as a **platform prerequisite** (not a “quick patch”).

### Health checks (examples)
- `GET /_cluster/health?pretty`

### Notes
- If you use OpenSearch for vector/hybrid, treat embedding model + dimension changes as **breaking** (requires rebuild + provenance).
</details>

---

## Deploying (GitOps / manual)

> [!IMPORTANT]
> Prefer applying **overlays**, not the raw base.

### Kustomize preflight
```bash
kustomize build infra/apps/dependencies/search/k8s/overlays/dev \
  | kubectl apply --dry-run=client -f -
```

### Apply (example)
```bash
kubectl apply -k infra/apps/dependencies/search/k8s/overlays/dev
```

### GitOps (Argo CD / OpenShift GitOps)
Point your Application/ApplicationSet at one of:
- `infra/apps/dependencies/search/k8s/overlays/dev`
- `infra/apps/dependencies/search/k8s/overlays/stage`
- `infra/apps/dependencies/search/k8s/overlays/prod`

---

## Post-deploy smoke tests

> Pick the track that matches your engine.

### Common checks
```bash
kubectl get pods -A | grep -i search
kubectl get svc  -A | grep -i search
```

### Meilisearch (example)
```bash
kubectl port-forward svc/search 7700:7700
curl -sS http://localhost:7700/health
```

### OpenSearch (example)
```bash
kubectl port-forward svc/search 9200:9200
curl -sS http://localhost:9200/_cluster/health?pretty
```

---

## Definition of Done ✅

- [ ] Base defines an **internal-only** Service (ClusterIP) and **no public ingress**
- [ ] NetworkPolicy enforces the trust membrane (UI/external cannot reach Search)
- [ ] Secrets are managed safely (no plaintext in Git)
- [ ] Health probes exist and pods become Ready
- [ ] Storage posture documented (PVC sizes in overlays; backup posture stated)
- [ ] Observability hooks are present or explicitly deferred (metrics/logging)
- [ ] A minimal runbook exists (this README + troubleshooting notes)
- [ ] Documentation is consistent with the engine actually deployed (no OpenSearch/Meili drift)

---

## References (repo-local)

- Search dependency contract: [`infra/apps/dependencies/search/README.md`](../../README.md)  
- Local dev stack defaults: [`/docker-compose.yml`](/docker-compose.yml), [`/.env.example`](/.env.example)  
- Infra governance + trust membrane: [`infra/README.md`](/infra/README.md)

