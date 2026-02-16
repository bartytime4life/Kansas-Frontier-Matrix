# ApplicationSets 🧩 (KFM GitOps)

![GitOps](https://img.shields.io/badge/GitOps-Git%20is%20the%20source%20of%20truth-blue)
![Argo CD](https://img.shields.io/badge/Argo%20CD-ApplicationSet-orange)
![KFM](https://img.shields.io/badge/KFM-governed%20by%20design-brightgreen)

This folder contains **Argo CD `ApplicationSet`** manifests used to generate and manage Argo CD `Application` resources for the Kansas Frontier Matrix (KFM) platform.

> [!IMPORTANT]
> **ApplicationSets have high blast-radius.**
> A small change can create/update **many** `Application` resources across namespaces (and possibly clusters).
> Treat every change here as a **governed production change**.

---

## Contents

- [What belongs here](#what-belongs-here)
- [GitOps flow](#gitops-flow)
- [Directory layout](#directory-layout)
- [Common ApplicationSet categories](#common-applicationset-categories)
- [Conventions](#conventions)
- [Governance and safety rails](#governance-and-safety-rails)
- [How to add or change an ApplicationSet](#how-to-add-or-change-an-applicationset)
- [Validation gates](#validation-gates)
- [Troubleshooting](#troubleshooting)
- [Glossary](#glossary)
- [References](#references)

---

## What belongs here

**✅ Put here**
- `ApplicationSet` YAML manifests (usually `*.yaml`) that define:
  - **Generators** (git/dir/list/cluster/etc.)
  - The `Application` **template**
  - How apps are **grouped** and **promoted** across environments

**🚫 Do not put here**
- Raw application manifests / Kustomize bases for workloads (those should live in the workload trees your ApplicationSets point at)
- Secrets (encrypted *secret references* are fine; raw secrets are not)
- “One-off” manual `Application` objects unless you have a clear reason (prefer ApplicationSets so the system stays DRY and repeatable)

---

## GitOps flow

```mermaid
flowchart LR
  Dev[Pull Request / Review] --> CI[CI Policy Gates<br/>Lint + Policy-as-Code + Tests]
  CI --> Git[Merge to Git (Desired State)]
  Git --> AS[Argo CD ApplicationSet Controller]
  AS --> Apps[Argo CD Applications]
  Apps --> K8s[Kubernetes / OpenShift Cluster]
  K8s --> Runtime[Running KFM Services]
  Runtime --> UI[UI / Clients]
  Runtime --> API[Governed APIs]
```

**Key idea:** GitOps declares desired state in Git, and Argo CD continuously reconciles the live environment to match it (reducing drift and improving auditability).

---

## Directory layout

This repository uses:

```text
infra/
  gitops/
    applicationsets/
      README.md          <-- you are here
      *.yaml             <-- one or more ApplicationSets
```

> [!NOTE]
> A common GitOps reference structure places ApplicationSets under `components/applicationsets/` alongside `argocdproj/` and `bootstrap/` directories.  
> KFM keeps the same concept, but nests it under `infra/gitops/…` to align with infrastructure ownership boundaries and repo ergonomics.

---

## Common ApplicationSet categories

The exact set of ApplicationSets depends on your environment(s) and organizational boundaries, but the following **categories are common**:

| Category (typical) | What it manages | Primary owners (typical) | Blast radius |
|---|---|---:|---:|
| `cluster-config` | Cluster-level configuration (namespaces, RBAC, operators, base policies) | Platform / SRE / Security | 🔥 Very high |
| `core-components` | “Core functionality” needed for the cluster/platform to work (ingress, certs, observability, gitops controller self-management, etc.) | Platform / SRE | 🔥 High |
| `tenants` / `apps` | Application workloads (namespaced apps; env overlays; team-owned workloads) | App teams / Release engineers | ⚠️ Medium–low |

> [!WARNING]
> Always ensure **AppProjects** and generator scopes prevent a “deploy anywhere” ApplicationSet.

---

## Conventions

### Naming

Use a name that clearly communicates scope and blast radius:

- `kfm-cluster-config-appset.yaml`
- `kfm-core-components-appset.yaml`
- `kfm-tenants-appset.yaml`

**Recommended pattern:**  
`kfm-<scope>-appset.yaml` where `<scope>` is one of: `cluster-config`, `core-components`, `tenants`, `apps`, `tools`, etc.

### Labels and metadata (recommended)

Add consistent metadata for governance, ownership, and filtering:

| Field | Example | Why |
|---|---|---|
| `metadata.labels.kfm.io/scope` | `core-components` | Search + auditing |
| `metadata.labels.kfm.io/owner` | `platform` | Accountability |
| `metadata.labels.kfm.io/governed` | `true` | Signals higher review bar |
| `metadata.annotations.kfm.io/change-note` | `Explains intent` | Review clarity |

> [!NOTE]
> If your repo already defines label keys elsewhere, use those as the source of truth.

---

## Governance and safety rails

KFM operates with a **trust membrane** and evidence-first governance:

> [!IMPORTANT]
> **Trust membrane:** frontend and external clients must never access databases/object stores directly; access must flow through the governed API boundary.  
> Infrastructure changes must not bypass or weaken this boundary.

Additional rails:

- **Policy-as-code gates** must be **merge-blocking** for governed changes.
- **Fail-closed** behavior is preferred for promotion/publish decisions.
- Avoid changes that expand exposure without explicit review (routes, ingresses, network policies, IAM/RBAC widening, etc.).

---

## How to add or change an ApplicationSet

### 1) Pick the right scope boundary

Before writing YAML, decide:

- Is this **cluster-config**, **core**, or **tenant/app** scope?
- Which boundary/team owns review and approval?
- What is the **worst-case blast radius** if the generator expands unexpectedly?

### 2) Create or edit the `ApplicationSet` YAML

Create a new file in this directory (or edit an existing one).

#### Minimal example (directory generator)

```yaml
apiVersion: argoproj.io/v1alpha1
kind: ApplicationSet
metadata:
  name: kfm-tenants
  namespace: argocd
  labels:
    kfm.io/scope: tenants
    kfm.io/governed: "true"
spec:
  generators:
    - git:
        repoURL: https://github.com/<org>/<repo>.git
        revision: main
        directories:
          - path: apps/*/overlays/prod
  template:
    metadata:
      name: '{{path.basename}}-prod'
    spec:
      project: tenants
      source:
        repoURL: https://github.com/<org>/<repo>.git
        targetRevision: main
        path: '{{path}}'
      destination:
        server: https://kubernetes.default.svc
        namespace: '{{path.basename}}'
      syncPolicy:
        automated:
          prune: true
          selfHeal: true
```

> [!CAUTION]
> The generator (`directories:`) is where accidental blast-radius usually happens.  
> Keep it narrow, versioned, and reviewed.

### 3) Ensure the AppProject / destination constraints are correct

At minimum, confirm:

- `spec.project` exists and enforces allowed source repos + destinations
- destination namespaces are constrained (or created intentionally)
- cross-namespace / cluster-wide permissions are **not** granted unintentionally

### 4) Submit via PR

- Changes must go through PR review
- Include a human-readable “what changes in the cluster” note in the PR description
- Prefer a “preview first” approach for high-risk changes when feasible

---

## Validation gates

### Local checks (recommended)

Run a small “pre-flight” before opening PR:

- YAML lint / schema validation for Kubernetes objects
- Render any referenced Kustomize overlays
- Confirm generator matches only the intended directories

### CI gates (expected for governed changes)

The repo should enforce:

- **Policy-as-code** checks (e.g., Conftest/OPA) for:
  - required metadata/labels
  - destination/repo allowlists
  - exposure controls (ingress/route/netpol)
  - licensing/sensitivity constraints where applicable
- Merge-blocking failures for missing required governance fields

> [!TIP]
> Keep deny messages explainable: they should point to the missing field/constraint and how to fix it.

---

## Troubleshooting

<details>
<summary><strong>ApplicationSet created zero Applications</strong></summary>

Checklist:
- Confirm the generator path(s) exist at the target revision
- Check for typos in generator keys (`directories`, `files`, `path`, etc.)
- Inspect ApplicationSet controller logs
- Verify repo authentication / repo credentials in Argo CD
</details>

<details>
<summary><strong>ApplicationSet created too many Applications</strong></summary>

Checklist:
- Tighten the generator (narrow directory glob patterns)
- Add explicit allowlists (list generator) for production scopes
- Add policy gate to block wildcard expansions for protected scopes
- Consider splitting into smaller ApplicationSets by domain/team
</details>

<details>
<summary><strong>Argo CD shows drift / keeps re-syncing</strong></summary>

Checklist:
- Confirm the rendered manifests are deterministic (avoid timestamps/random names)
- Ensure admission controllers/mutators aren’t rewriting managed fields unexpectedly
- If a resource is expected to be mutated by the cluster, consider:
  - ignoreDifferences rules (carefully)
  - or managing only the stable subset of fields
</details>

---

## Glossary

- **ApplicationSet:** Argo CD CRD that generates one or more Argo CD `Application` objects from a generator + template.
- **Application:** Argo CD object representing a deployable unit (source repo/path + destination).
- **AppProject:** Argo CD policy boundary for multi-tenancy: restricts which repos and destinations an app may use.
- **Generator:** ApplicationSet mechanism for enumerating targets (directories, clusters, lists, SCM providers, etc.).
- **Blast radius:** The scope of impact if a change is wrong (e.g., “deploy everywhere”).

---

## References

- Argo CD docs: ApplicationSet controller and generators
- GitOps design guidance: repo structures, boundaries, and DRY layouts
- KFM governance principles: trust membrane + policy gates

(External links intentionally omitted here to keep this README stable if link-checking is strict; add links if your repo supports them.)
