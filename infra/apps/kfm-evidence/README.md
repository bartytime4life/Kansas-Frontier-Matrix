# 🧾 kfm-evidence — Evidence Resolver (GitOps app)

![Governance](https://img.shields.io/badge/governance-fail--closed-red)
![Trust membrane](https://img.shields.io/badge/architecture-trust%20membrane-blue)
![Policy](https://img.shields.io/badge/policy-OPA%2FRego-informational)
![GitOps](https://img.shields.io/badge/deploy-GitOps%20%2B%20Kustomize-success)
![Status](https://img.shields.io/badge/status-governed%20infrastructure-yellow)

> [!IMPORTANT]
> This directory is **infrastructure-as-code** for deploying **KFM’s Evidence Resolver** (“kfm-evidence”).
> It is part of the **Trust Membrane**: it helps make every citation and claim **auditable, policy-checked, and reproducible**.

---

## What lives here

This folder **deploys** the `kfm-evidence` service into a Kubernetes/OpenShift cluster using a GitOps-friendly layout (base + overlays).

**Primary job:** resolve a citation reference (e.g., `stac://...`, `prov://...`) into:

- ✅ **Human-readable evidence view** (what the UI shows in the Evidence Drawer)
- ✅ **Machine-readable metadata** (catalog identifiers, digests, provenance pointers)
- ✅ **Access decision + redaction obligations** (policy-safe outcomes)

---

## Non-negotiable invariants

These are *system-level guarantees*, not “best practices”.

### ✅ Evidence resolution must be bounded
- **Every citation reference must be resolvable**
- Resolution must complete in **≤ 2 API calls per citation** (bounded hops)

### ✅ Fail-closed posture
- Default posture is **deny on uncertainty**
- Policy evaluation must occur on every request path that could expose restricted information

### ✅ Auditability
- Every governed response path must emit an **`audit_ref`**
- Evidence resolution must be traceable (correlation IDs, request IDs)

### ✅ Safety & rights
- **Sensitive-location** data must never leak precise coordinates (generalize/redact)
- **Rights/license** metadata must be enforced in downstream export/download behaviors

> [!WARNING]
> If a change risks making citations non-resolvable, bypassing policy, or reducing audit fidelity, it is a **blocking governance issue**.

---

## Architecture position

```mermaid
flowchart LR
  UI[Web UI / Focus Mode / Story Nodes] --> API[Governed API Gateway]
  API --> EVID[kfm-evidence (Evidence Resolver)]
  API --> OPA[OPA / Rego PDP]
  API --> AUD[Audit Ledger]
  EVID --> OPA
  EVID --> CAT[Catalogs: DCAT / STAC / PROV]
  EVID --> OBJ[Object Store / Bundle Store]
  EVID --> AUD
```

**Trust membrane rule:** the UI (and any external client) must not talk to storage/indexes directly.

---

## Directory layout

This app directory is intended to follow a GitOps structure that supports multiple environments.

```text
infra/
└── apps/
    └── kfm-evidence/
        ├── README.md
        ├── base/                      # common manifests (no environment-specific values)
        │   ├── kustomization.yaml
        │   ├── deployment.yaml
        │   ├── service.yaml
        │   ├── networkpolicy.yaml
        │   ├── pdb.yaml               # optional
        │   └── route-or-ingress.yaml  # optional (platform-specific)
        └── overlays/
            ├── dev/
            │   ├── kustomization.yaml
            │   └── patch-env.yaml
            ├── stage/
            │   ├── kustomization.yaml
            │   └── patch-env.yaml
            └── prod/
                ├── kustomization.yaml
                └── patch-env.yaml
```

> [!NOTE]
> If some of the above files/folders don’t exist yet, treat this README as the **target contract** for how this app should be structured.

---

## Deploying (GitOps-friendly)

### Kustomize render (local validation)
```bash
# from repo root
kustomize build infra/apps/kfm-evidence/overlays/dev > /tmp/kfm-evidence.dev.yaml
```

### Apply (direct kubectl / oc)
```bash
kubectl apply -f /tmp/kfm-evidence.dev.yaml
# or (OpenShift)
oc apply -f /tmp/kfm-evidence.dev.yaml
```

### GitOps controller (recommended)
In a GitOps controller model (e.g., Argo CD / OpenShift GitOps), this directory is typically referenced by an **Application** or **ApplicationSet** that points at:

- `infra/apps/kfm-evidence/overlays/dev`
- `infra/apps/kfm-evidence/overlays/stage`
- `infra/apps/kfm-evidence/overlays/prod`

---

## Configuration contract

> [!IMPORTANT]
> **No secrets in Git.** Secrets must be injected by an approved mechanism (External Secrets Operator, Vault integration, SealedSecrets, etc.). *(Exact mechanism not confirmed in repo.)*

### Suggested config surface (examples)
The exact env var names must match your service implementation, but these are the **expected categories**.

| Category | Examples | Notes |
|---|---|---|
| Runtime | `KFM_ENV`, `LOG_LEVEL` | Prefer structured logs |
| Policy | `OPA_URL`, `OPA_BUNDLE_REV` | Default-deny; policy must be consistent with CI semantics |
| Audit | `AUDIT_LEDGER_URL` / DSN | Emit `audit_ref` + correlation IDs |
| Catalog resolution | `CATALOG_BASE_URL` | Used to resolve DCAT/STAC/PROV identifiers |
| Bundle/object access | `BUNDLE_STORE_URL`, `OBJECT_STORE_URL` | Do **not** leak restricted object URLs |
| Security | `PUBLIC_BASE_URL`, `CORS_ORIGINS` | Keep CORS tight; TLS termination handled by platform |

> [!TIP]
> Treat config as **contractual**: if you rename a variable, update overlays + docs + contract tests in the same PR.

---

## Evidence Resolver API contract

This is the **minimum implementable contract** this app is expected to satisfy.

### Reference schemes
The resolver should support stable citation schemes, such as:

- `prov://...` (provenance objects / run receipts)
- `stac://...` (STAC collections/items/assets)
- `dcat://...` (dataset/distribution metadata)
- `doc://...` (document snippets / extracted text evidence)
- `graph://...` (graph paths, entity relationships)
- `oci://...` (optional; digest-pinned evidence bundles)

### Endpoint shape (minimum)
```http
GET /api/v1/evidence/resolve?ref=<scheme://...>
```

### Response shape (minimum, illustrative)
```json
{
  "ref": "stac://collection/kansas_counties",
  "decision": {
    "allowed": true,
    "redactions": [],
    "obligations": ["display_rights_badge", "display_sensitivity_badge"]
  },
  "human_view": {
    "format": "markdown",
    "content": "### Kansas Counties (STAC Collection)\n…"
  },
  "machine_view": {
    "kind": "stac.collection",
    "ids": {
      "stac_id": "kansas_counties",
      "dataset_id": "kfm.dataset.123"
    },
    "digests": {
      "bundle": "sha256:…",
      "artifact": "sha256:…"
    },
    "links": [
      {"rel": "dcat", "href": "dcat://dataset/kfm.dataset.123"},
      {"rel": "prov", "href": "prov://run_receipt/sha256:…"}
    ]
  },
  "audit_ref": "audit_01H…"
}
```

### Error handling (policy-safe)
- `403` for denied access **without leaking restricted metadata**
- `404` for unknown refs (or properly scoped “not found”)

> [!IMPORTANT]
> A contract test must assert: every `citation.ref` produced by Focus Mode / Story Nodes resolves successfully **or** returns the correct `403/404` without information leakage.

---

## Optional: digest-pinned bundle resolver

If KFM adopts OCI evidence bundles, the resolver should support digest-based resolution.

### Endpoint (proposal)
```http
GET /api/v1/bundles/{sha256_digest}
```

This supports “resolve-by-digest” workflows where **the digest is the canonical address**.

---

## Observability expectations

### Logs
- Structured logs (JSON recommended)
- Correlation IDs propagated end-to-end (API gateway → kfm-evidence → downstream)
- Never log secrets, access tokens, or restricted coordinates

### Metrics & tracing
- OpenTelemetry spans for:
  - request duration
  - downstream catalog lookup duration
  - policy evaluation duration
  - bundle/object fetch duration
- Counters for:
  - resolves by scheme
  - denied requests (by rule / reason code)
  - 404s and malformed refs

---

## Security & governance controls

### Hard requirements
- TLS everywhere (edge termination allowed, but internal traffic should be protected per platform norms)
- NetworkPolicy (or OpenShift equivalent) to restrict:
  - inbound: only from API gateway / trusted namespaces
  - outbound: only to OPA + catalogs + bundle/object endpoints
- Rate limiting at the edge (or in the gateway) to prevent enumeration of refs
- Cache only policy-safe objects; never cache restricted payloads in a shared layer

---

## CI expectations for this directory

At minimum, PRs touching `infra/apps/kfm-evidence/**` should pass:

- `kustomize build` for each overlay (dev/stage/prod)
- policy-as-code checks (Conftest) for:
  - missing NetworkPolicy
  - missing resource limits
  - images pinned by digest (if required by org policy)
  - no Secrets committed
- smoke tests in staging validating:
  - `/healthz` (if present)
  - at least one known-good `ref` resolves
  - at least one known-denied `ref` returns `403` policy-safe

---

## Change management checklist

- [ ] Does this change preserve **≤2-hop resolvability**?
- [ ] Does it preserve **default-deny** behavior?
- [ ] Does it preserve **audit_ref emission**?
- [ ] Does it avoid leaking **sensitive-location** or rights-restricted details?
- [ ] Are Kustomize overlays updated consistently?
- [ ] Are contract tests updated (or added) for any new ref scheme/endpoints?

---

## Troubleshooting quick hits

```bash
# find pods
kubectl -n <ns> get pods -l app=kfm-evidence

# logs
kubectl -n <ns> logs deploy/kfm-evidence

# describe
kubectl -n <ns> describe deploy/kfm-evidence

# render what GitOps will apply
kustomize build infra/apps/kfm-evidence/overlays/prod | head
```

---

## Provenance for this README

This README is written to align with KFM’s published invariants:
- Trust Membrane separation (UI never directly accesses stores)
- Evidence Resolver contract (bounded resolution, policy-safe behavior)
- Fail-closed policy posture, sensitive-location handling, and rights enforcement
- GitOps/Kustomize environment overlays

If implementation details differ, the **manifests are the source of truth**, but the invariants above must remain true.
