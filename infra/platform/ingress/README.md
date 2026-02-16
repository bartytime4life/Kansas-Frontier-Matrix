# KFM Platform Ingress 🌐🛡️

![Governed](https://img.shields.io/badge/Governed-Yes-brightgreen)
![GitOps](https://img.shields.io/badge/GitOps-Declarative%20in%20Git-blue)
![Kubernetes](https://img.shields.io/badge/Targets-Kubernetes%20%7C%20OpenShift-informational)
![Trust%20Membrane](https://img.shields.io/badge/Trust%20Membrane-Enforced-critical)

> [!IMPORTANT]
> **This directory is the authoritative definition of how traffic enters KFM.**
> - Public traffic **must** enter through the **governed API gateway / policy boundary** (the trust membrane).
> - **Never** expose databases (PostGIS, Neo4j), object stores, or internal services directly to the internet.
> - Changes here are **production-impacting** and should be treated as governed infrastructure.

---

## Why this exists

This folder holds the **platform ingress** layer: the Kubernetes/OpenShift resources that connect the outside world to KFM services **without bypassing governance**.

KFM’s platform posture is evidence-first and fail-closed:
- If governance prerequisites are missing, the system should **block promotion by default** (fail closed).
- Public access must remain **auditable**, **policy-enforced**, and **stable** across environments.

---

## Scope

### ✅ In scope (what lives here)
- Public entrypoint resources:
  - OpenShift **Routes**
  - Kubernetes **Gateway API** objects (GatewayClass/Gateway/Routes), when available
  - **Legacy Ingress** only when unavoidable
- Host/path routing rules and conventions
- TLS termination strategy (edge vs re-encrypt), redirect rules
- Edge-oriented guardrails (rate limits, headers) *when supported by the chosen controller*
- GitOps-friendly packaging (Kustomize bases/overlays)

### ❌ Out of scope (what must not live here)
- Application logic
- Authorization/policy decisions (those live in the **governed API gateway**)
- Database exposure (no Postgres/Neo4j routes)
- Secrets committed to Git (use secret stores / sealed workflows per project policy)

---

## Trust membrane alignment

KFM’s trust membrane expects:
- Authentication and policy evaluation at the **governed gateway**
- Query shaping / redaction before data leaves the platform
- Audit and provenance logging for client interactions

**Ingress must only route to the trust membrane entrypoints** (e.g., the API gateway, UI, and other explicitly approved public services).

---

## Reference architecture

```mermaid
flowchart LR
  user[Public Clients\n(browsers, API clients)] --> dns[DNS / External LB]
  dns --> edge[Cluster Edge\n(Route / Gateway / Ingress)]

  edge --> ui[UI Service\n(static + app shell)]
  edge --> gw[Governed API Gateway\n(authn/authz + policy + redaction)]

  gw --> api[API Services\n(REST/GraphQL adapters)]
  api --> catalog[(Catalog Store)]
  api --> graph[(Graph DB)]
  api --> postgis[(PostGIS)]
  api --> obj[(Object Storage)]

  gw --> audit[Audit & Provenance Logs\n(append-only outputs)]
```

> [!NOTE]
> The diagram is conceptual. Controller specifics (OpenShift Router, Envoy Gateway, service mesh ingress, etc.) are environment-dependent.

---

## Supported ingress patterns

### Pattern A — OpenShift Route (OpenShift-native)

OpenShift **Route** resources provide external DNS names and load-balanced access to internal Services via the cluster Router (commonly HAProxy-based).  
Use this pattern when deploying on OpenShift and Routes are the standard.

**When to use:**
- You are on OpenShift and want the platform-native L7 entrypoint.

**Key rule:**
- Route targets must be **only** the **API gateway** and other explicitly approved public services (e.g., UI).

<details>
<summary><strong>Example: Route (edge TLS termination + redirect)</strong></summary>

```yaml
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: kfm-api
  labels:
    kfm.io/component: ingress
spec:
  host: api.example.org
  to:
    kind: Service
    name: kfm-api-gateway
  port:
    targetPort: http
  tls:
    termination: edge
    insecureEdgeTerminationPolicy: Redirect
```
</details>

---

### Pattern B — Kubernetes Gateway API (preferred for new features)

Kubernetes Ingress is widely used, but the API is considered **“frozen”** and Kubernetes recommends the **Gateway API** for new traffic-management features. Gateway API is role-oriented:
- `GatewayClass`
- `Gateway`
- `HTTPRoute` / `TLSRoute` / etc.

**When to use:**
- Your cluster supports Gateway API and has a controller installed that provides a `GatewayClass`.

<details>
<summary><strong>Example: HTTPRoute (Gateway API)</strong></summary>

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: kfm-api
  labels:
    kfm.io/component: ingress
spec:
  parentRefs:
    - name: kfm-public
  hostnames:
    - api.example.org
  rules:
    - matches:
        - path:
            type: PathPrefix
            value: /
      backendRefs:
        - name: kfm-api-gateway
          port: 80
```
</details>

> [!WARNING]
> Gateway API requires:
> - The CRDs installed
> - A controller implementing a `GatewayClass`
> These details are **environment-specific** and must be verified in cluster docs/runbooks.

---

### Pattern C — Legacy Kubernetes Ingress (compatibility only)

Use only when:
- A platform constraint forces it, or
- A controller feature is required and the environment does not support Gateway API.

If using Ingress:
- Treat it as legacy / lowest-common-denominator routing.
- Keep migration notes toward Gateway API.

---

## Directory layout

This folder is intended to be **GitOps-friendly**. A recommended layout mirrors Kustomize “bases + overlays”.

```text
infra/platform/ingress/
├─ README.md
├─ base/                         # reusable, env-agnostic manifests
│  ├─ openshift-route/           # Route objects (OpenShift)
│  ├─ gateway-api/               # Gateway/HTTPRoute objects (K8s Gateway API)
│  ├─ shared/                    # common labels/annotations/policies
│  └─ kustomization.yaml
└─ overlays/                     # env-specific deltas (hostnames, cert refs, limits)
   ├─ dev/
   │  └─ kustomization.yaml
   ├─ stage/
   │  └─ kustomization.yaml
   └─ prod/
      └─ kustomization.yaml
```

> [!NOTE]
> If the repo already has a different canonical layout, keep the canonical layout and treat the above as a mapping guide.

---

## Endpoint registry

Maintain a simple, reviewable registry of public endpoints. This table should be updated with each new entrypoint.

| Endpoint | Public host | Kind | Backend Service | Auth required | Data class | Notes |
|---|---|---:|---|---:|---|---|
| UI | `app.example.org` | Route/Gateway | `kfm-ui` | ✅ | public | Static + app shell |
| API | `api.example.org` | Route/Gateway | `kfm-api-gateway` | ✅ | governed | Trust membrane entry |
| Tiles | `tiles.example.org` | Route/Gateway | `kfm-tiles-gateway` | ✅ | governed | Prefer caching + throttles |

> [!TIP]
> Treat “Data class” as a governance label (e.g., public / internal / sensitive / restricted). If unknown → **fail closed** until classified.

---

## Adding a new public entrypoint

1. **Confirm it belongs on the public surface**
   - Is it required for UI/API consumption?
   - Is there a safer internal-only alternative?

2. **Route it through governance**
   - If it serves governed data, it must go through the **API gateway / policy boundary**.

3. **Implement the resource**
   - OpenShift: `Route`
   - Kubernetes: `HTTPRoute` (Gateway API) preferred

4. **TLS + redirects**
   - HTTPS required
   - Redirect HTTP → HTTPS

5. **Update the endpoint registry**
   - Add the new host/endpoint row above

6. **Validation gates**
   - Kustomize render must succeed
   - Policy tests must pass (OPA/Conftest or equivalent)
   - No new direct exposure of internal-only services

---

## Deploying (GitOps workflow)

KFM uses declarative manifests stored in Git, then promoted through environments using overlays.

### Render / dry-run

```bash
# render manifests for inspection (no cluster needed)
kubectl kustomize infra/platform/ingress/overlays/dev
```

### Apply to cluster

```bash
# Kubernetes
kubectl apply -k infra/platform/ingress/overlays/dev

# OpenShift (oc is kubectl-compatible for apply)
oc apply -k infra/platform/ingress/overlays/dev
```

> [!NOTE]
> Kustomize’s base/overlay structure is the recommended approach for minimizing duplicated YAML across environments.

---

## Security notes (edge-facing)

### TLS and session security
If auth/session cookies are issued at the gateway:
- Prefer **HttpOnly + Secure** cookies for long-lived secrets
- Avoid long-lived access tokens in browser storage when possible
- Ensure strong XSS defenses (e.g., CSP) so tokens are not exposed to injected scripts

### Operational guardrails (recommended)
- Rate limiting for anonymous endpoints
- Request size limits (protect upload endpoints)
- Strict security headers (HSTS, CSP) where the edge/controller supports it
- Access logs retained and correlated with audit/provenance streams

---

## Definition of Done for ingress changes ✅

- [ ] Endpoint added to registry table (host/kind/backend/auth/classification)
- [ ] TLS enforced; HTTP redirect enabled
- [ ] Backend is **only** a permitted public service (e.g., API gateway, UI)
- [ ] No direct datastore exposure (PostGIS/Neo4j/object store) added
- [ ] Kustomize renders cleanly for all overlays
- [ ] Policy checks pass (fail closed for missing governance labels)
- [ ] Rollback path documented (revert commit / GitOps sync rollback)

---

## Troubleshooting quick hits

| Symptom | Likely cause | First checks |
|---|---|---|
| Host resolves but 503/404 | Route/Route target mismatch | Service exists? endpoints ready? correct targetPort? |
| TLS handshake fails | cert/termination mismatch | TLS termination config + cert secret refs |
| Works in dev, fails in prod | overlay delta error | diff rendered manifests dev vs prod |
| Auth works locally, fails on ingress | header/cookie handling | forwarded headers, cookie domain/path, HTTPS redirect |

---

## References (project docs)

- **KFM Masterpiece Vision** (trust membrane + governance posture)
- **KFM Pulse → Integration Kit** (platform invariants + fail-closed patterns)
- **KFM Software Support** (Gateway API vs Ingress guidance)
- **OpenShift networking references** (Routes + router behavior)

> [!TIP]
> Add concrete links to the repo’s canonical architecture docs once those paths are confirmed.
