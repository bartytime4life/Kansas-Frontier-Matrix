# Vector Dependency — `base/` (Kustomize)  
![governance](https://img.shields.io/badge/governance-evidence--first%20%7C%20fail--closed-blue?style=flat-square)
![layer](https://img.shields.io/badge/layer-infra%20%2F%20apps%20%2F%20dependencies-111827?style=flat-square)
![gitops](https://img.shields.io/badge/deploy-GitOps%20%2B%20Kustomize-informational?style=flat-square)
![trust](https://img.shields.io/badge/trust%20membrane-no%20direct%20client%20store%20access-critical?style=flat-square)

> [!IMPORTANT]
> This folder is the **environment-agnostic Kustomize base** for KFM’s **Vector** runtime dependency.
>
> **Base means:** reusable defaults + security posture + stable service contract.  
> **Overlays mean:** dev/stage/prod deltas (image pin, replicas, storage class, resources, auth/TLS, etc.).

---

## Governance header

| Field | Value |
|---|---|
| Document | `infra/apps/dependencies/vector/base/README.md` |
| Status | **Governed draft** |
| Version | `v1.0.0-draft` |
| Effective date | `2026-02-18` (America/Chicago) |
| Applies to | base manifests + service contract + security posture + ops expectations |
| Owners | `.github/CODEOWNERS` *(required; if missing, governance gap)* |
| Review triggers | anything affecting network exposure, persistence, auth/TLS, policy labels, or index rebuild semantics |

> [!WARNING]
> **Fail-closed rule:** if required enforcement surfaces are missing (policy checks, secrets pattern, network boundaries, provenance fields),
> treat this as **not ready to promote**.

---

## What this directory is

`vector/base/` is the **lowest common denominator** deployment layer for the vector index service that supports:

- **Focus Mode retrieval** (semantic similarity / RAG context assembly)
- **Hybrid retrieval pipelines** (vector + metadata filters)
- **Derived “serving index” acceleration** (not a system-of-record)

> [!NOTE]
> The repo’s local dev compose stack currently wires the API to a **Qdrant** default via `KFM_VECTOR_URL=http://qdrant:6333`.
> This base should therefore default to a **stable internal service DNS contract** that matches that expectation.

---

## Non-negotiables

### 1) Trust membrane (KFM-C0)

- **No browser / external client may connect to the vector service directly.**
- Vector is **cluster-internal** and called only by the governed API boundary and/or internal indexer jobs.
- NetworkPolicy (or equivalent) must make “accidental bypass” hard (UI → Vector denied).

> [!CAUTION]
> “It’s inside the cluster” is not a guarantee. If there is an ingress/route, a public service type, or permissive network policy,
> assume the trust membrane is **broken**.

### 2) Vector is derived, not authoritative

- The vector store is a **derived index** built from **processed artifacts + catalogs/provenance**.
- The system-of-record remains: processed artifacts + catalogs (DCAT/STAC/PROV) + governed stores.
- Treat loss of the vector index as **recoverable** via rebuild (though backups may still be valuable).

### 3) Fail-closed behavior at the boundary

If vector retrieval is unavailable or policy inputs are missing:

- **Focus Mode must abstain or degrade safely** (never “guess” without evidence).
- The **API boundary** must filter/shape results using policy labels and redaction rules before returning anything to users.

---

## Expected directory layout

> [!TIP]
> Keep `base/` small, readable, and reusable. Push environment specifics into `overlays/`.

```text
infra/
└─ apps/
   └─ dependencies/
      └─ vector/
         ├─ README.md                 # dependency-level contract + ops notes (recommended)
         ├─ base/
         │  ├─ README.md              # you are here
         │  ├─ kustomization.yaml     # base entrypoint
         │  ├─ statefulset.yaml       # or deployment.yaml (if ephemeral)
         │  ├─ service.yaml           # ClusterIP internal service
         │  ├─ pvc.yaml               # persistent storage claim (if stateful)
         │  ├─ configmap.yaml         # non-secret config (optional)
         │  ├─ networkpolicy.yaml     # default deny + explicit callers (recommended)
         │  ├─ pdb.yaml               # optional
         │  └─ servicemonitor.yaml    # optional (if Prometheus operator)
         └─ overlays/
            ├─ dev/
            │  └─ kustomization.yaml  # small deltas (replicas/resources/debug)
            ├─ stage/
            │  └─ kustomization.yaml
            └─ prod/
               └─ kustomization.yaml  # strictest posture (pins, HA, storage, egress)
```

---

## Base resource expectations

Your `base/` manifests should normally include:

| Resource | Why it exists | Notes |
|---|---|---|
| `StatefulSet` (preferred) | durable index storage | Vector indexes are typically stateful |
| `Service` (ClusterIP) | stable internal DNS | Avoid `LoadBalancer`/public routes by default |
| `PVC` | persistence | StorageClass is usually overlay-specific |
| `NetworkPolicy` | trust membrane enforcement | Restrict to API/indexer namespaces/selectors |
| Probes | safe rollout | liveness/readiness must not leak internals |
| Resource requests/limits | predictable scheduling | set sane defaults; tune in overlays |

> [!NOTE]
> If you intentionally choose an **ephemeral** vector index (no PVC), document the rebuild strategy and blast radius explicitly.

---

## Service contract

### Internal DNS + port

To minimize drift between local dev and cluster deploys, use:

- **Service name (recommended):** `qdrant`
- **Internal URL:** `http://qdrant:6333`
- **API env var contract:** `KFM_VECTOR_URL=http://qdrant:6333`

If you must use a different service name:

- update `KFM_VECTOR_URL` in the API deployment overlays, and
- document the change in `infra/apps/dependencies/vector/README.md` (or equivalent).

### Auth/TLS posture

- **Dev:** auth/TLS may be disabled for ease of iteration (document explicitly).
- **Prod:** prefer enabling auth and restricting callers via NetworkPolicy even if auth exists.

> [!WARNING]
> Do not rely on “security by obscurity” (cluster-only) for production.

---

## Data + provenance contract (metadata must travel with vectors)

Vector similarity results are **not publishable evidence** unless every returned item can be traced back to governed artifacts.

Minimum metadata fields to store (names are illustrative; map to your DB’s schema):

| Field | Purpose |
|---|---|
| `kfm_id` / `chunk_id` | stable identity + dedupe |
| `dataset_id` / `version_id` | ties result to a governed dataset version |
| `artifact_ref` (digest/URI) | points to processed artifact used for embedding |
| `provenance_ref` | points to PROV lineages / receipts |
| `license` / `rights` | prevents unlawful reuse |
| `sensitivity` label(s) | policy filtering / redaction obligations |
| `time_start` / `time_end` | temporal filter + timeline UI support |
| `bbox` (optional) | coarse spatial filter |

> [!IMPORTANT]
> **No “mystery vectors.”** If a point cannot be traced to a catalog/provenance reference, it must not be served to users.

---

## How this base is applied

### Render (local sanity check)

```bash
# From repo root
kubectl kustomize infra/apps/dependencies/vector/base
```

### Apply (prefer overlays)

```bash
# dev example (recommended)
kubectl apply -k infra/apps/dependencies/vector/overlays/dev
```

> [!TIP]
> Base-only apply is usually for smoke tests. Real deployments should flow through an overlay (even if it’s identical initially).

---

## Ops expectations

### Backup / restore

Even if the vector index is derived, backups can be useful for:

- fast restore after cluster loss
- debugging retrieval drift
- rollback safety during upgrades

Recommended posture:

- nightly snapshots to the object store (if supported by the implementation)
- retention aligned with audit/debug needs
- periodic restore drills in non-prod

### Rebuild strategy

A rebuild must be:

- **reproducible** (inputs pinned to processed artifacts + versions)
- **receipted** (emit a run record/receipt that points to index build inputs/outputs)
- **policy-safe** (only index what is allowed; store labels needed for filtering)

---

## Security & supply-chain checklist (base-level)

> [!DANGER]
> Never ship dependency runtime with mutable tags (`:latest`) outside local dev.

- [ ] Image references are pinned (version, and preferably digest in prod overlays)
- [ ] Runs as non-root; drops Linux capabilities where feasible
- [ ] Read-only root filesystem where feasible
- [ ] No public ingress/route created by default
- [ ] NetworkPolicy restricts callers (API + indexers only)
- [ ] No plaintext secrets committed (use ExternalSecrets/SealedSecrets patterns)
- [ ] Logs do not leak sensitive metadata (sensitivity applies to telemetry too)

---

## Definition of Done (for this folder)

- [ ] `kustomize build` succeeds for base and each overlay
- [ ] Service is **cluster-internal only** (no external exposure by default)
- [ ] Stable service contract documented (`KFM_VECTOR_URL`, DNS, port)
- [ ] Persistence posture is explicit (PVC + storage assumptions documented)
- [ ] Metadata/provenance fields are required for served results (contract documented)
- [ ] Basic ops notes exist (backup/restore, rebuild, troubleshooting)
- [ ] PR includes a rollback plan (“git revert” + any data/index considerations)

---

## Cross-links (repo-relative)

- `infra/README.md` — platform invariants, trust membrane, GitOps model  
- `infra/apps/README.md` — workload/overlay conventions  
- `infra/apps/dependencies/README.md` — dependency conventions + supply-chain rules  
- `docker-compose.yml` + `.env.example` — local dev defaults (`KFM_VECTOR_URL`, `qdrant:6333`)  
- `infra/apps/dependencies/search/README.md` — retrieval/index “derived store” philosophy

---

