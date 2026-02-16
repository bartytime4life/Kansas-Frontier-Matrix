# KFM GitOps (infra/gitops)

![Governed](https://img.shields.io/badge/Governed-FAIR%2BCARE-2ea44f)
![Evidence-first](https://img.shields.io/badge/Evidence--first-cite%20or%20abstain-3b82f6)
![GitOps](https://img.shields.io/badge/GitOps-versioned%20desired%20state-111827)
![Trust%20membrane](https://img.shields.io/badge/Trust%20membrane-API%20only-critical)

Governed GitOps configuration for Kansas Frontier Matrix (KFM): **cluster + platform baselines**, **application deployments**, and **promotion mechanics**—with a bias toward **auditability**, **least privilege**, and **fail-closed** guardrails.

> [!IMPORTANT]
> **KFM trust membrane invariant:** the UI and external clients **never** access databases directly. All access is through the **governed API + policy boundary** (auth / rate limits / audit). This repo must not introduce “back doors” (e.g., public DB services, wide-open routes, privileged debug pods).

---

## Table of contents

- [What lives here](#what-lives-here)
- [GitOps principles we follow](#gitops-principles-we-follow)
- [Repository layout](#repository-layout)
- [Workflows](#workflows)
  - [Bootstrap a cluster](#bootstrap-a-cluster)
  - [Add or change a “core” platform capability](#add-or-change-a-core-platform-capability)
  - [Add an app](#add-an-app)
  - [Promote dev → stage → prod](#promote-dev--stage--prod)
  - [GitOps for data promotion](#gitops-for-data-promotion)
- [Secrets](#secrets)
- [Governance and safety gates](#governance-and-safety-gates)
- [Operational notes](#operational-notes)
- [Definition of Done](#definition-of-done)
- [Appendix: terminology](#appendix-terminology)

---

## What lives here

This directory contains **declarative desired state** for:

- **bootstrap**: the minimum set of resources needed to bring a cluster under GitOps control
- **components**: shared “GitOps plumbing” (ApplicationSets / projects / RBAC / repo credentials / policy controllers)
- **core**: platform-level cluster functionality required for KFM (namespaces, ingress/routing, observability, policy engines, etc.)
- **apps**: tenant workloads (KFM API, UI, jobs/workers, pipeline runners, etc.) deployed as Kustomize bases + env overlays

> [!NOTE]
> If you later split into a dedicated “ops repo”, this folder becomes a drop-in root candidate for that repo.

---

## GitOps principles we follow

- **Git is the source of truth** for what should be running.
- The GitOps controller is **asynchronous** and continuously reconciles desired state.
- **Promotion is promotion of manifests**, not “promotion of code.”
- Prefer **immutable artifacts** (pin images by digest in stage/prod when practical) and keep rollout intent in Git.

---

## Repository layout

This layout is optimized for:
- multiple environments (`dev` / `stage` / `prod`)
- clean separation of responsibilities (platform vs apps)
- DRY reuse via `base/` + `overlays/`

```text
infra/
  gitops/
    README.md

    bootstrap/
      base/
      overlays/
        default/          # minimal “bring cluster under GitOps” overlay

    components/
      applicationsets/     # ApplicationSet definitions (apps + core)
      argocdproj/          # Argo CD Projects (multi-tenancy boundaries)
      rbac/                # cluster/namespace RBAC (least privilege)
      policies/            # admission/policy (Gatekeeper/Kyverno/etc.)
      repo-credentials/    # *references* to repo creds (NOT plaintext secrets)

    core/
      gitops-controller/   # “manage the manager” (Argo manages itself)
      namespaces/
      networking/
      ingress/
      observability/
      storage/
      security/

    apps/
      kfm-api/
        base/
        overlays/
          dev/
          stage/
          prod/
      kfm-ui/
        base/
        overlays/
          dev/
          stage/
          prod/
      kfm-jobs/
        base/
        overlays/
          dev/
          stage/
          prod/
```

> [!TIP]
> Keep `apps/*/base` free of environment-specific values. Put only deltas in overlays.

---

## Workflows

### Bootstrap a cluster

**Goal:** install/configure your GitOps controller (e.g., Argo CD / OpenShift GitOps) and point it at the `bootstrap/overlays/default` entrypoint.

A common pattern is a single “bootstrap Application” that syncs everything else:

```yaml
# Example (Argo CD Application)
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: kfm-bootstrap
  namespace: <ARGOCD_NAMESPACE>
spec:
  project: default
  source:
    repoURL: <REPO_URL>
    targetRevision: main
    path: infra/gitops/bootstrap/overlays/default
  destination:
    server: https://kubernetes.default.svc
    namespace: <ARGOCD_NAMESPACE>
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
```

> [!IMPORTANT]
> Bootstrap should be **minimal**. Anything “optional but nice” belongs in `core/` or `apps/` so it can be promoted deliberately.

---

### Add or change a core platform capability

1. Add/modify manifests under `core/<capability>/...`
2. Ensure it’s included by whatever “core” loader you use:
   - an ApplicationSet that scans `core/*`, or
   - an explicit Argo CD Application that targets `infra/gitops/core/...`

**Examples of “core” capabilities:**
- network policies / default-deny baselines
- ingress controllers/routes
- logging/metrics/tracing stack
- namespace templates + quotas
- policy engines (OPA Gatekeeper / Kyverno) and constraints

---

### Add an app

**Preferred layout:**
- `apps/<app>/base`: Deployments/Services/ConfigMaps/etc. (generic)
- `apps/<app>/overlays/<env>`: environment-specific config, scaling, ingress hostname, resource limits

Minimal Kustomize structure:

```text
apps/myapp/
  base/
    kustomization.yaml
    deployment.yaml
    service.yaml
  overlays/
    dev/
      kustomization.yaml
    stage/
      kustomization.yaml
    prod/
      kustomization.yaml
```

Local rendering checks (recommended in PRs):

```bash
kustomize build infra/gitops/apps/myapp/overlays/dev   >/tmp/myapp-dev.yaml
kustomize build infra/gitops/apps/myapp/overlays/prod  >/tmp/myapp-prod.yaml
```

---

### Promote dev → stage → prod

Promotion should be a **Git change** (PR), typically one of these patterns:

- **Overlay promotion:** promote a change by merging the PR that updates `overlays/stage` or `overlays/prod`
- **Image promotion:** update the image reference (preferably a digest) in the target overlay

> [!NOTE]
> When a prod incident happens, rollbacks are also Git changes: revert the commit that introduced the bad desired state.

---

### GitOps for data promotion

KFM’s data lifecycle includes promotion gates (Raw → Work → Processed). One GitOps-friendly way to make data promotion auditable:

- Keep a **declarative “desired data versions” file** (or set of files) in Git.
- Promote data by PR that updates **version pointers** (digests/checksums or dataset version IDs).
- A controller/job (GitOps-managed) reacts to the desired state and performs the load/promotion.

Example conceptual file:

```yaml
# Example: desired-data.yaml (conceptual)
datasets:
  kansas-land-patents:
    version: "sha256:..."
  kshs-kansas-memory:
    version: "sha256:..."
```

> [!WARNING]
> Do **not** store sensitive dataset contents or plaintext secrets in Git. Store **references**, digests, and provenance pointers.

---

## Secrets

Plaintext secrets must **never** be committed.

Two common GitOps-safe patterns:

1. **Encrypted secrets in Git** (e.g., Sealed Secrets)
2. **External secret references in Git** (e.g., External Secrets Operator / Vault / cloud secret managers)

Guidance:

- Prefer **secret references** for production (clean separation of duties), unless governance demands Git-only portability.
- If using encrypted secrets, treat key management as a first-class operational system (rotation, recovery, access).

Suggested directory convention:

```text
components/
  secrets/
    sealedsecrets/         # SealedSecret resources (encrypted payloads only)
    externalsecrets/       # ExternalSecret + SecretStore (no sensitive values)
```

> [!IMPORTANT]
> Any secret-handling approach must be compatible with KFM governance: avoid leaking sensitive locations, credentials, or restricted metadata via logs, receipts, or debug tooling.

---

## Governance and safety gates

This repo is part of KFM’s **governed delivery pipeline**. The defaults should be “safe by default”:

- **Fail-closed** checks on PRs
- **Policy guardrails** (admission/policy engine configs treated as critical infrastructure)
- **Least privilege** RBAC (avoid cluster-admin for app deployers)
- **Auditability**: changes land via PR with reviewable diffs

Recommended CI checks for PRs:
- `kustomize build` for every changed overlay
- server-side dry run against a target cluster (when available)
- secret scanning (block merges if plaintext patterns found)
- policy tests (OPA/Conftest or Kyverno test harness) for invariants

---

## Operational notes

### GitOps controller health

In an Argo-style setup, operators typically look at:
- sync status (`Synced` / `OutOfSync`)
- health (`Healthy` / `Degraded`)
- drift/self-heal events

### Rollback philosophy

- Prefer reverting the Git commit(s) that changed the desired state.
- Avoid “hot fixes” applied directly to the cluster; they will be overwritten by reconciliation and reduce auditability.

---

## Definition of Done

For any PR changing `infra/gitops/**`:

- [ ] All affected overlays render: `kustomize build ...` succeeds
- [ ] No plaintext secrets are introduced (scan passes)
- [ ] Changes preserve the **trust membrane** (no direct DB exposure; no wide-open routes/services)
- [ ] Security posture is not weakened (RBAC/netpol/policy constraints reviewed)
- [ ] Rollback is straightforward (revert commit restores prior desired state)
- [ ] For prod-impacting changes: staged in `dev` then `stage` before `prod` (unless emergency)

---

## Appendix: terminology

**Desired state:** what Git says should be running.  
**Reconciliation:** the controller’s continuous effort to make actual state match desired state.  
**Overlay:** environment-specific Kustomize customization (`dev` / `stage` / `prod`).  
**Promotion:** a Git change that updates what a higher environment should run (manifests/images/data pointers).  
**Trust membrane:** architectural boundary where external clients never access storage directly—only via governed APIs.

---
