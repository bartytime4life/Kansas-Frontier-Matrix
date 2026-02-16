# KFM Web UI — `kfm-web` (Infra App)

![Status](https://img.shields.io/badge/status-governed-blue)
![Surface](https://img.shields.io/badge/surface-web%20ui%20%2B%20map%20%2B%20timeline-informational)
![Trust%20Membrane](https://img.shields.io/badge/trust%20membrane-enforced-critical)

> [!IMPORTANT]
> This directory is **infrastructure-as-code** for the KFM Web UI (`kfm-web`).  
> It should contain **deployment artifacts** (Kubernetes/OpenShift manifests, Kustomize overlays, GitOps wiring), **not** business logic.
>
> If you are looking for the **frontend source code**, search the repo for `package.json`, `vite.config.*`, `next.config.*`, or `src/` (source location is **not confirmed** here).

---

## What this app is

`kfm-web` is the primary browser UI for **Kansas Frontier Matrix (KFM)**:
- map-first exploration + time controls (timeline / scrubber)
- **Focus Mode** chat panel (evidence-backed, cite-or-abstain behavior)
- provenance/citation drawer, audit/explain affordances
- Story Mode surfaces (narrative rail, scenes, keyframes, checkpoints) *(if enabled in your build)*

This folder documents and deploys the **web UI runtime** (typically a static SPA served by a small web server container, or an SSR app if KFM chooses that approach).

---

## Non‑negotiables (governance + trust membrane)

> [!WARNING]
> The Web UI is **never** allowed to bypass KFM governance.

**Trust membrane rules**
- Browsers/clients **do not** access databases or internal stores directly.
- All data access flows through the **governed API layer** (gateway + policy boundary).
- No “direct-to-storage” shortcuts (tiles, documents, datasets) unless they are served via a governed, policy-aware edge/tile service.

**Focus Mode UI guarantees (must be supported by the UI)**
- The UI must support inline citations and a click-through experience to view the cited evidence.
- The UI must support policy-governed outcomes (redactions/refusals) and show them clearly to users.
- The UI should expose an “Audit / Explain” view for power users when returned by the API.

**Story/Provenance UI guarantees (must be supported by the UI when story/provenance features are enabled)**
- Citations must carry dataset identifiers and resolvable evidence links.
- If sensitive fields are generalized, the UI must surface a privacy/sensitivity indicator.

---

## GitOps / deployment approach

> [!TIP]
> Prefer “Don’t Repeat YAML”: keep a reusable base and use overlays/patches per environment.

This directory is designed to work with GitOps tools (e.g., Argo CD) and Kustomize overlays.

---

## Directory layout

> [!NOTE]
> Filenames below are **expected** patterns (adjust to match the repo’s actual manifests).

```text
infra/
└── apps/
    └── kfm-web/
        ├── README.md
        ├── base/
        │   ├── kustomization.yaml
        │   ├── deployment.yaml            # or deploymentconfig.yaml (OpenShift)
        │   ├── service.yaml
        │   ├── route.yaml                 # OpenShift (optional)
        │   ├── ingress.yaml               # Kubernetes (optional alternative to Route)
        │   ├── configmap-runtime.yaml     # non-secret runtime config (public)
        │   ├── secret.yaml                # only if strictly required (avoid for SPAs)
        │   ├── hpa.yaml                   # optional autoscaling
        │   └── networkpolicy.yaml         # optional (meaningful mainly for SSR/proxy)
        └── overlays/
            ├── dev/
            │   ├── kustomization.yaml
            │   ├── patch-image.yaml
            │   └── patch-hostname.yaml
            ├── stage/
            │   ├── kustomization.yaml
            │   └── patches...
            └── prod/
                ├── kustomization.yaml
                └── patches...
```

---

## Deploy (manual CLI)

### Prereqs
- `kubectl` (Kubernetes) **or** `oc` (OpenShift)
- `kustomize` (or `kubectl apply -k ...` if your kubectl bundles it)
- Cluster access to the target namespace/project

### Apply an overlay
```bash
# Kubernetes-style:
kubectl apply -k infra/apps/kfm-web/overlays/dev

# OpenShift-style (works similarly if oc supports -k in your setup):
oc apply -k infra/apps/kfm-web/overlays/dev
```

### Build manifests without applying
```bash
kustomize build infra/apps/kfm-web/overlays/dev > /tmp/kfm-web.dev.yaml
```

---

## GitOps (recommended)

> [!IMPORTANT]
> In GitOps, the cluster reconciler (e.g., Argo CD) applies these manifests.  
> Humans should **not** “hot-edit” in-cluster resources except during incident response.

Typical flow:
1. CI builds a new image for `kfm-web` and publishes it (tag = git SHA).
2. A PR updates the overlay image reference (or an ImageUpdateAutomation does).
3. GitOps reconciles; rollout happens; monitoring validates; rollback is a git revert.

---

## Runtime configuration (public, non-secret)

> [!WARNING]
> **Never** embed secrets in a browser bundle. If a value must be secret, it must be handled server-side.

Common patterns:
- **Runtime `config.json`** mounted from a ConfigMap and fetched by the SPA at startup.
- **Nginx `envsubst`** at container start (less ideal; still public for SPAs).
- **SSR runtime env** (only if you are running SSR; treat carefully).

### Suggested keys (examples; verify actual app expectations)
```json
{
  "apiBaseUrl": "https://api.<env>.kfm.example",
  "realtimeUrl": "wss://api.<env>.kfm.example/v1/realtime",
  "tiles": {
    "styleUrl": "https://tiles.<env>.kfm.example/styles/kfm/style.json",
    "attribution": "KFM / providers"
  },
  "features": {
    "focusMode": true,
    "storyMode": false,
    "provenanceDrawer": true
  }
}
```

---

## Security controls to enforce at the edge

Recommended headers for the `kfm-web` response (configure in your web server, route, or ingress):
- `Content-Security-Policy` (CSP)  
- `Referrer-Policy: no-referrer` (or stricter as needed)
- `X-Content-Type-Options: nosniff`
- `Permissions-Policy` (lock down sensors, camera, etc. unless required)
- `Cross-Origin-Opener-Policy` / `Cross-Origin-Embedder-Policy` *(only if needed for advanced perf features; test carefully)*

> [!NOTE]
> Map rendering libraries may require worker-related CSP allowances. If you harden CSP, validate map loads and worker behavior in all supported browsers.

---

## Observability + supportability

### Correlation IDs
- If the API returns correlation IDs, the UI should display them in:
  - error toast/details
  - Focus Mode audit/explain drawer
  - “Report a problem” flows

### Client-side error reporting (optional but recommended)
- Capture uncaught errors + unhandled promise rejections.
- Redact sensitive fields from logs by default.
- Prefer sampling + rate limits to avoid log storms.

---

## Rollout, rollback, and safety

**Rollout**
- Prefer canary/gradual rollout for UI versions that change:
  - auth flows
  - policy interpretation and citation rendering
  - map/tile fetching behavior

**Rollback**
- Rollback should be a git revert of:
  - image tag changes, and/or
  - overlay patches

---

## Troubleshooting

<details>
<summary><strong>Route/Ingress returns 404</strong></summary>

- Confirm the Service exists and selects pods:
  - `kubectl get svc,pods`
  - `oc get svc,pods`
- Confirm Route/Ingress host matches expected DNS and points to the service.
- Confirm container listens on the port your Service targets.
</details>

<details>
<summary><strong>Map loads but tiles don’t render</strong></summary>

- Check browser devtools → Network:
  - are tile/style requests blocked by CORS?
  - are they blocked by CSP?
  - are you missing auth cookies/headers?
- Confirm `apiBaseUrl` / `styleUrl` values in runtime config are correct for the environment.
</details>

<details>
<summary><strong>Focus Mode shows answers without citations</strong></summary>

- Treat as a governance failure:
  - ensure the API is enforcing “cite or abstain”
  - ensure the UI is rendering returned citation blocks and not hiding them
</details>

---

## Change checklist (Definition of Done)

### Manifest correctness
- [ ] `kustomize build overlays/<env>` succeeds
- [ ] `kubectl apply --dry-run=server -k overlays/<env>` succeeds (where supported)
- [ ] Namespaces, labels, selectors, ports are consistent

### Governance + safety
- [ ] No secrets embedded into SPA config/bundle
- [ ] UI does not introduce any direct-to-storage or direct-to-DB behavior
- [ ] Focus Mode UI renders citations and policy outcomes clearly

### Operational readiness
- [ ] Liveness/readiness probes defined (as applicable)
- [ ] Resource requests/limits defined
- [ ] Rollback path documented (git revert)

---

## Architecture sketch (request paths)

```mermaid
flowchart LR
  U[User Browser] -->|HTTPS| W[kfm-web Route/Ingress\n(static UI)]
  U -->|HTTPS / WSS| G[Governed API Gateway\n(policy + audit)]
  G --> S[(KFM Services)]
  G --> T[Tile/Feature Services\n(policy aware)]
```

---

## Ownership

- **Product surface:** KFM Web UI (`kfm-web`)
- **Infra folder:** `infra/apps/kfm-web`
- **Owner(s):** *(add CODEOWNERS or list team here — not confirmed in repo)*
- **On-call / escalation:** *(add here — not confirmed in repo)*
