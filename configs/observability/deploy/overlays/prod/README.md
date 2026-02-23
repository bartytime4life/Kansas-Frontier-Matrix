<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/c3327716-6663-4356-beed-0557c0e88ce0
title: Observability Deploy Overlay — prod
type: standard
version: v1
status: draft
owners: platform-observability (TBD)
created: 2026-02-23
updated: 2026-02-23
policy_label: restricted
related:
  - ../README.md
  - ../../base/README.md
tags: [kfm, observability, deploy, kustomize, overlay, prod]
notes:
  - Directory-level contract for the production observability overlay.
  - Update owners/related links once confirmed in-repo.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Observability — prod overlay (Kustomize)

![status](https://img.shields.io/badge/status-draft-lightgrey)
![env](https://img.shields.io/badge/env-prod-blue)
![policy](https://img.shields.io/badge/policy-restricted-orange)
![kustomize](https://img.shields.io/badge/kustomize-overlay-informational)
![kubernetes](https://img.shields.io/badge/kubernetes-manifests-informational)
<!-- TODO: Add CI badges once workflow paths are confirmed (lint, kustomize build, policy gates). -->

**Purpose:** Production-specific Kustomize overlay for deploying KFM observability into the **prod** Kubernetes environment.

**Status / ownership:** Draft · Owners: **platform-observability (TBD)** · Change policy: **PR-only** (no direct edits to prod).

---

## Quick navigation

- [Overview](#overview)
- [Where this fits](#where-this-fits)
- [Directory contract](#directory-contract)
- [How to deploy](#how-to-deploy)
- [Telemetry contract](#telemetry-contract)
- [Verification](#verification)
- [Rollback](#rollback)
- [Troubleshooting](#troubleshooting)
- [Appendix](#appendix)

---

## Overview

This directory is intended to hold the **production deltas** for the observability stack, layered on top of the shared base (typically `../../base`).

Common reasons for a `prod` overlay:

- **Sizing**: higher resource requests/limits, HA replicas, PodDisruptionBudgets.
- **Retention & storage**: longer retention, persistent volumes, compaction settings.
- **Ingress / auth**: prod hostnames, SSO, tighter network policies.
- **Hardening**: tighter RBAC, restricted PSP/PSa profiles, anti-affinity, node selectors.
- **Telemetry contract**: enforce canonical labels/attributes and `kfm.env=prod`.

> WARNING  
> Treat everything deployed from this overlay as **production-grade**. Avoid “quick fixes” applied directly to the cluster. Prefer GitOps reconciliation (revert/roll back through Git).

---

## Where this fits

Expected high-level layout (example):

```text
configs/observability/
  deploy/
    base/
    overlays/
      dev/
      stage/
      prod/   <-- you are here
```

This overlay should contain only **environment-specific patches/config**, while shared resources live in `deploy/base`.

---

## Directory contract

### What belongs here

**Allowed / expected artifacts (examples):**

- `kustomization.yaml` that composes the base + prod-only deltas.
- Patch files (strategic merge or JSON6902), e.g.:
  - `patch-resources.yaml`
  - `patch-retention.yaml`
  - `patch-ingress.yaml`
  - `patch-rbac.yaml`
- Kustomize generators for prod-only config:
  - `configMapGenerator` inputs
  - `vars` / replacements
- Small README updates documenting:
  - *why* the prod delta exists
  - *what* risk it introduces
  - *how* to verify the change

### What must NOT go here

- **Secrets** (tokens, passwords, client secrets, kubeconfigs, private keys).
- **One-off hotfix YAML** that bypasses the base/overlay model.
- **Cluster bootstrap** concerns (CRD installs, GitOps controller install) unless this repo explicitly defines prod bootstrap here.
- **Sensitive endpoints** or internal-only hostnames unless policy permits (default: keep them out of README; encode in manifests and restrict access).

> NOTE  
> If you must reference a secret, reference a **secret name** that is provisioned by your approved secret mechanism (e.g., external secret operator), but do not commit the secret value.

---

## How to deploy

### Preferred: GitOps reconciliation

Production should be reconciled by your GitOps controller (Argo CD / Flux / equivalent). This overlay path should be used as the **source path** in the prod GitOps application definition.

### Local render (safe)

```bash
# From repo root
kustomize build configs/observability/deploy/overlays/prod > /tmp/observability-prod.yaml

# Or (kubectl includes kustomize support in many distros)
kubectl kustomize configs/observability/deploy/overlays/prod > /tmp/observability-prod.yaml
```

### Diff against the cluster (recommended)

```bash
kubectl diff -k configs/observability/deploy/overlays/prod
```

### Apply (break-glass only)

```bash
kubectl apply -k configs/observability/deploy/overlays/prod
```

> WARNING  
> “Break-glass apply” should be exceptional. If you do it, immediately open a PR that makes Git match cluster state (or revert the break-glass change and let GitOps re-assert).

---

## Telemetry contract

Production observability must preserve **cross-system traceability**. The goal: a pipeline run can be joined across:

- metrics (Prometheus-style labels),
- traces (OpenTelemetry attributes),
- catalogs (STAC/DCAT),
- provenance (PROV).

### Canonical keys to enforce

The prod overlay should ensure the runtime collectors/exporters (or relabeling rules) preserve these keys consistently:

| Meaning | OpenTelemetry attribute | Prometheus label | Notes |
|---|---|---|---|
| Run ID | `kfm.job.run_id` | `job_run_id` | UUID/ULID |
| Commit SHA | `kfm.git.commit_sha` | `commit_sha` | 7–40 hex |
| Status | `kfm.job.status` | `status` | `scheduled\|running\|succeeded\|failed\|canceled` |
| Started at | `kfm.job.started_at` | `started_at` | RFC3339 + unix seconds |
| Ended at | `kfm.job.ended_at` | `ended_at` | RFC3339 + unix seconds |
| Dataset ID | `kfm.dataset.id` | `dataset_id` | STAC/DCAT id |
| Pipeline name | `kfm.pipeline.name` | `pipeline` | Stable slug |
| Environment | `kfm.env` | `env` | `dev\|staging\|prod` (**prod overlay MUST emit `prod`**) |

**Timestamp rule:** emit timestamps twice:
- RFC3339 strings (best for traces + catalog metadata)
- unix seconds (best for Prometheus math)

### Catalog linkage expectations

This overlay should not just “collect telemetry”; it should support the governance loop:

- Write run identifiers into **STAC Item properties** (e.g., `kfm:run_id`, `commit_sha`, `status`).
- Model the run as a **`prov:Activity`** in PROV and attach times/agents.
- Use `dataset_id` to connect dashboards to catalog pages / Focus Mode evidence.

---

## Verification

Minimal smoke checks after a prod change (adapt to your actual stack resources):

1. **Render + validate**
   ```bash
   kustomize build configs/observability/deploy/overlays/prod >/tmp/out.yaml
   # Optional: schema validation if you have kubeconform/kubeval
   ```

2. **Workload health**
   ```bash
   kubectl get ns
   kubectl get pods -A | grep -i observ
   ```

3. **Telemetry contract spot-check**
   - Pick one known pipeline run.
   - Confirm the dashboards/metrics include `job_run_id`, `commit_sha`, `dataset_id`, `env=prod`.
   - Confirm traces show `kfm.job.run_id` and correlate to the same run ID.

4. **Access control**
   - Confirm only intended roles can access dashboards/logs/traces.
   - Confirm prod ingress endpoints (if any) are protected (SSO, IP allowlists, etc.).

---

## Rollback

Preferred rollback path:

1. Revert the PR (or roll back the GitOps “target revision”).
2. Let GitOps reconcile the cluster back to the prior known-good state.
3. Confirm health + telemetry contract is restored.

Break-glass (last resort): use your platform standard for rollback (e.g., `kubectl rollout undo`), then immediately reconcile Git to match.

---

## Troubleshooting

### `kustomize build` fails

- Check patch targets (kind/name/namespace mismatch).
- Check for missing CRDs referenced by resources (ServiceMonitor, PodMonitor, etc.).
- Check generator inputs (missing files, wrong relative paths).

### Resources apply but pods crashloop

- Review resource requests/limits in prod patches.
- Validate config maps / env vars were generated as expected.
- Check storage classes / PVC provisioning (prod often differs).

### Telemetry labels/attributes missing

- Verify the collector/exporter relabel rules in prod overlay.
- Ensure `kfm.env=prod` is enforced.
- Ensure timestamps are present in both formats where required.

---

## Appendix

<details>
<summary>Example GitOps application template (edit to match your controller)</summary>

```yaml
# NOTE: Template only. Do not apply as-is.
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: observability-prod
  namespace: argocd
spec:
  project: default
  source:
    repoURL: <REPO_URL>
    targetRevision: <BRANCH_TAG_OR_SHA>
    path: configs/observability/deploy/overlays/prod
  destination:
    server: https://kubernetes.default.svc
    namespace: <OBSERVABILITY_NAMESPACE>
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
```

</details>

---

<a id="back-to-top"></a>
[Back to top](#top)
