<!--
Path: infra/apps/dependencies/vector/overlays/prod/README.md
Scope: Production Kustomize overlay for the "vector" dependency used by KFM.
Governance: Treat this README + overlay manifests as governed artifacts (they affect system behavior).
-->

# Vector dependency — prod overlay (Kustomize)

> [!IMPORTANT]
> **Trust membrane enforcement (non-negotiable):** this service must **not** be directly reachable by the UI or the public internet.
> All access must be mediated by **governed APIs** (auth, policy, audit, rate limits).  
> *(Aligned with KFM’s architecture & governance rules.)*  

> [!NOTE]
> This README is intentionally **engine-agnostic** because the repo may swap implementations (e.g., different vector engines).  
> Confirm the actual engine/image/env-vars in `../../base/` manifests. If anything below conflicts with live manifests, treat it as **(not confirmed in repo)** and update this README to match reality.

---

## What this directory is

This directory contains the **production** overlay for the Vector dependency:

- **Base:** `infra/apps/dependencies/vector/base/`
- **Overlay:** `infra/apps/dependencies/vector/overlays/prod/` (this folder)

This overlay should follow GitOps/Kustomize best-practices:

- Keep **shared** config in `base/`
- Keep **environment deltas** (prod-only settings) as patches here
- Avoid “copy-paste YAML” drift; use patches/overlays for differences

---

## Quick facts

| Item | Prod intent |
|---|---|
| Availability | HA posture where supported (replicas + anti-affinity + PDB) |
| Durability | Persistent storage enabled (PVC) unless the chosen engine is explicitly stateless |
| Exposure | **Cluster-internal only** (no public Route/Ingress unless governance approves) |
| Secrets | Never commit plaintext secrets; use sealed/external secret references |
| Rebuildability | Vector index is **reconstructible** from governed datasets/catalogs (no “mystery state”) |

---

## Directory map

```text
infra/
└─ apps/
   └─ dependencies/
      └─ vector/
         ├─ base/
         │  ├─ kustomization.yaml
         │  └─ ... (deploy/service/pvc/etc.)
         └─ overlays/
            └─ prod/
               ├─ kustomization.yaml
               ├─ README.md   👈 you are here
               ├─ patches/    (recommended)
               └─ ...         (prod-only resources)
```

> [!TIP]
> If you add new files under `prod/`, prefer putting them in a `patches/` subfolder and referencing them from `kustomization.yaml`.
> This keeps the overlay readable and review-friendly.

---

## What “prod” should change (and what it should not)

### ✅ Typical prod deltas (recommended)
- Increase **replicas** (if supported)
- Tighten **resource requests/limits**
- Add **PodDisruptionBudget** (PDB) and **anti-affinity**
- Enforce **NetworkPolicy** (allow only API namespace(s))
- Enable/size **PVC** and configure backup hooks
- Enable **metrics** endpoints / ServiceMonitor (if used in the cluster)
- Enable **TLS-in-cluster** if supported (mTLS/service mesh or app-level TLS)
- Harden security context (runAsNonRoot, readOnlyRootFilesystem, etc.)

### ❌ What prod should not do
- Do **not** expose the Vector service directly to the public internet
- Do **not** store plaintext credentials in Git
- Do **not** bypass the policy boundary by letting random workloads talk to this service

---

## Deployment model

### GitOps (preferred)
This overlay is intended to be applied by your GitOps controller (e.g., Argo CD / OpenShift GitOps).

**Operational rule:** *Git is the source of truth.* Production changes happen through PRs, reviews, and policy gates — not `kubectl apply` to prod.

### Local render (debug only)
Use this only for *rendering/validation* in a dev environment, not for pushing changes directly into prod.

```bash
# From this directory:
kustomize build . > /tmp/vector-prod.yaml

# Optional: client-side inspection
cat /tmp/vector-prod.yaml | less

# Optional: server-side dry-run in a non-prod cluster/namespace you control
kubectl apply --dry-run=server -f /tmp/vector-prod.yaml
```

> [!WARNING]
> Directly applying to production from a workstation breaks auditability and undermines GitOps rollback.
> If you must emergency-fix, still follow your org’s break-glass process and backfill a PR immediately.

---

## Configuration contract (prod expectations)

Because the actual engine may vary, treat this as a **minimum contract** the prod overlay should satisfy.

### 1) Authentication & authorization
- The service should require auth **if the engine supports it**
- Credentials are provided via **Secret** references or external secret controllers
- No credentials in ConfigMaps

### 2) NetworkPolicy (trust membrane enforcement)
Recommended posture:
- **Default deny** ingress
- Allow ingress only from:
  - KFM backend API namespace(s)
  - Optional: jobs namespace for index rebuilders
  - Optional: observability namespace for scraping metrics (if metrics are separate)

> [!NOTE]
> If the repo already defines a cluster-wide network policy baseline, this overlay should *conform to it* rather than duplicating it.

### 3) Storage & backups
- PVC enabled for stateful engines
- Backup strategy is documented below and automated where possible

### 4) Observability
- Liveness/readiness probes defined
- Metrics exposed internally (if supported)
- Logs to stdout/stderr (cluster logging)

---

## Secrets handling

> [!IMPORTANT]
> Never commit plaintext Secrets. Prefer storing **references** (ExternalSecret, SealedSecret, Vault-backed, etc.) and have the cluster materialize the real Secret at runtime.

**Prod must define** (as applicable):
- Admin/API key secret reference
- TLS secret reference (if using app-level TLS)
- Any engine-specific credentials/config secrets

**Checklist**
- [ ] No `kind: Secret` with inline base64 values committed in this overlay
- [ ] Secret names are stable (so Deployments don’t churn)
- [ ] Secret rotation procedure documented (see below)

---

## Index rebuild philosophy (KFM governance)

KFM is designed so outputs remain **auditable and reproducible**. The Vector dependency is an **index** — not the canonical source-of-truth.

Recommended invariants:
- The vector index can be **rebuilt** from:
  - governed datasets + catalogs/provenance
  - deterministic embedding model versions
  - recorded job receipts/manifests (if your pipeline emits them)

> [!NOTE]
> If you discover prod-only state that cannot be reproduced from governed artifacts, flag it for governance review.
> That is a system risk: it breaks “rebuildability” and complicates incident response.

---

## SRE runbook

### Health checks
```bash
# namespace and labels depend on manifests — examples only:
kubectl -n <namespace> get pods -l app=vector
kubectl -n <namespace> describe deploy/<vector-deploy>
kubectl -n <namespace> logs deploy/<vector-deploy> --tail=200
```

### Scaling (if supported)
```bash
kubectl -n <namespace> scale deploy/<vector-deploy> --replicas=3
```

### Rolling restart
```bash
kubectl -n <namespace> rollout restart deploy/<vector-deploy>
kubectl -n <namespace> rollout status deploy/<vector-deploy>
```

---

## Backups & disaster recovery

> [!WARNING]
> Backup/restore steps are **engine-specific**. Replace placeholders below with the actual commands once confirmed in `base/`.

### Backup: required guarantees
- **RPO target:** define for your environment (e.g., daily)
- **RTO target:** define for your environment
- Backups are encrypted at rest (handled by platform or tooling)

### Restore: minimum procedure
1. Provision PVC / storage class as required
2. Restore snapshot into the PVC (or run engine restore tool)
3. Bring pods up
4. Run post-restore validation:
   - connectivity from backend API
   - sample query returns expected results
   - index rebuild job (optional) reconciles state

---

## Upgrade policy (prod)

**Golden rule:** upgrades are PR-based and reversible.

### Recommended upgrade sequence
1. Update image tag/version in `base/` or in this overlay (depending on repo policy)
2. Validate render (`kustomize build`)
3. Run contract tests (API can query vector)
4. Merge + GitOps sync
5. Observe:
   - rollout health
   - latency/error rate changes in API
   - resource usage

### Rollback
- Revert the PR (or roll back the GitOps Application revision)
- Confirm data compatibility (some engines change on-disk formats)

---

## Validation gates (CI expectations)

These are **minimum** CI checks recommended for production overlays:

- [ ] YAML renders (`kustomize build` succeeds)
- [ ] Server-side schema validation (`kubectl --dry-run=server` or equivalent)
- [ ] Policy gates pass (deny-by-default where applicable)
- [ ] No plaintext secrets committed
- [ ] NetworkPolicy present (or explicitly waived with justification + approval)
- [ ] Resource requests/limits set (avoid BestEffort pods in prod)

---

## Troubleshooting FAQ

### “Pods crashloop after deploy”
- Check missing secrets/config first:
  - `kubectl -n <ns> describe pod/<pod>`
- Verify PVC binding:
  - `kubectl -n <ns> get pvc`
- Confirm the configured ports match the Service

### “Backend API can’t connect”
- Confirm NetworkPolicy allows backend namespace → vector namespace
- Confirm Service name/port
- Confirm DNS within cluster:
  - `kubectl -n <backend-ns> exec -it <pod> -- nslookup <vector-svc>`

### “Latency spiked”
- Check CPU/memory throttling
- Check storage latency (if stateful)
- If applicable, run controlled index rebuild and compare

---

## Ownership & change control

- **Owners:** see repo `CODEOWNERS` or owning team docs *(not confirmed in repo)*
- **Change policy:** production overlay changes require review + CI gates + GitOps sync
- **Sensitive changes:** exposing services, changing auth posture, or weakening NetworkPolicy requires governance review

---

## Changelog notes (optional)

Add a short note per material prod change:

- YYYY-MM-DD — What changed / why / linked PR
