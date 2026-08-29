<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/infra-kubernetes-readme
title: infra/kubernetes/ — Kubernetes Adoption Hold and Cluster Boundary
type: per-directory-readme; infrastructure-boundary; adoption-hold
version: v2
status: draft; repository-grounded; documentation-only; adoption-hold; non-deployment; non-release; non-publication
owner: NEEDS VERIFICATION — CODEOWNERS routes /infra/ to @bartytime4life; accountable infrastructure, security, platform, and operations stewardship remain unverified
created: 2026-07-03
updated: 2026-08-29
policy_label: repository-facing; infra; kubernetes; cluster; deny-by-default; least-privilege; rollback-aware
current_path: infra/kubernetes/README.md
owning_root: infra/
responsibility: document the repository boundary for any future Kubernetes deployment slice without claiming cluster selection, manifest adoption, applied state, runtime health, or exposure enforcement
truth_posture: >
  CONFIRMED accepted Directory Rules through ADR-0029; infra/ as the deployment and exposure
  responsibility root; this directory contains only this README; no tracked Kubernetes manifest,
  Kustomize file, Helm chart, cluster configuration, installer, or Kubernetes-specific validator;
  CODEOWNERS routing for /infra/; one governed API local entry point; and placeholder Compose
  loopback mappings / UNKNOWN whether any external Kubernetes cluster, namespace, workload, service,
  ingress, gateway, policy, identity, volume, secret integration, or release exists / HOLD cluster
  product, provider, convention, object names, commands, credentials, routes, storage, admission,
  deployment, validation, and rollback until repository-backed files and review evidence exist
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 83ace64d7451eca641cbe9f3b6fe86eb0867cb0e
  target_prior_blob: ab53d648803e653d7c533441c23125973a9cbc78
  directory_tree_blob: 8ff325690544ebfa32618ad67d335e7488efaa2a
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption: docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md; accepted
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  compose_blob: 8a45891700a501f6e18a921ce8d260956441e4b3
  governed_api_entrypoint_blob: 4eb335c7c0b27f62c7419c478542e8fe40e1ff38
  inspection_method: exact target read; recursive repository tree; repository searches for Kubernetes commands and manifest markers; direct doctrine, infra root, CODEOWNERS, Compose, application entrypoint, hardening, and exposure-plan reads; no cluster or deployed environment inspected
related:
  - ../README.md
  - ../compose/docker-compose.yml
  - ../hardening/CHECKLIST.md
  - ../systemd/README.md
  - ../../apps/governed-api/src/governed_api/main.py
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/security/EXPOSURE_PLAN.md
  - ../../docs/security/INCIDENT_RESPONSE.md
  - ../../.github/CODEOWNERS
notes:
  - "v2 removes proposal-era Services, ingress topology, namespaces, policies, roles, storage, object names, reviewers, file trees, and kubectl commands that lacked repository or cluster evidence."
  - "The README is a placement and adoption boundary; it is not a manifest, cluster inventory, applied-state observation, release record, or publication decision."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `infra/kubernetes/` — Kubernetes Adoption Hold and Cluster Boundary

`infra/kubernetes/` is the established repository lane for a future,
reviewed Kubernetes deployment slice. It currently contains this README only.

> [!IMPORTANT]
> No tracked manifest, Kustomize file, Helm chart, cluster configuration,
> installation procedure, or Kubernetes-specific validator exists here. Do not
> infer that KFM has selected Kubernetes, created a cluster, applied resources,
> exposed a route, deployed a workload, or published an artifact.

## Current state

| Question | Repository evidence | Safe conclusion |
|---|---|---|
| What is tracked in this lane? | `infra/kubernetes/README.md` only | **CONFIRMED:** documentation-only lane |
| Are Kubernetes objects or rendering inputs tracked? | No manifest, Kustomize, or Helm files in the repository tree or targeted searches | **CONFIRMED:** no repository-backed object set |
| Is there a Kubernetes validator or CI gate? | No Kubernetes-specific command, test, or workflow found | **CONFIRMED:** validation is unestablished |
| Has KFM selected a distribution, provider, or manifest convention? | No decision or implementation-bearing file found | **HOLD** |
| Does any KFM cluster or namespace exist? | No cluster inventory or runtime evidence was inspected | **UNKNOWN** |
| Are workloads, Services, ingress, RBAC, policies, or volumes applied? | No cluster evidence exists in the repository | **UNKNOWN** |
| Can this README authorize deployment? | Documentation is not an operational transition record | **No** |

The current [`infra/` root](../README.md) likewise records the Kubernetes
convention and manifests as unestablished. Accepted
[Directory Rules](../../docs/doctrine/directory-rules.md), adopted through
[ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md),
place deployment and exposure configuration under `infra/`; they do not
select Kubernetes or establish any cluster state.

## Evidence boundaries

Repository-adjacent surfaces do not close this lane:

- [`apps/governed-api/src/governed_api/main.py`](../../apps/governed-api/src/governed_api/main.py)
  exposes a local Python entry point with a `127.0.0.1:8000` default. It does
  not define an image, Pod, Deployment, Service, probe, namespace, identity,
  configuration source, or cluster listener.
- [`infra/compose/docker-compose.yml`](../compose/docker-compose.yml) is a
  Greenfield placeholder with loopback port mappings. Compose rendering and
  placeholder image builds do not select Kubernetes or provide cluster object
  semantics.
- [`infra/systemd/README.md`](../systemd/README.md) is a separate
  documentation-only adoption hold. It is not a workload definition or
  evidence that Kubernetes should wrap a host service.
- [`infra/hardening/CHECKLIST.md`](../hardening/CHECKLIST.md) is a review
  checklist. Unchecked Kubernetes questions are not cluster enforcement.
- The [exposure plan](../../docs/security/EXPOSURE_PLAN.md) defines a
  deny-by-default trust boundary while local deployment controls remain
  proposed or need verification. Desired posture is not NetworkPolicy,
  ingress, RBAC, admission, or storage enforcement.
- [`CODEOWNERS`](../../.github/CODEOWNERS) routes `/infra/` review to
  `@bartytime4life`. Repository routing does not establish a platform team,
  cluster custody, deployment approval, or operational access.

Externally managed clusters may exist, but their state is **UNKNOWN**, not
absent. Kubeconfigs, tokens, private endpoints, tenant names, credentials,
unredacted object dumps, and sensitive topology must not be committed to
manufacture implementation proof.

## Lane contract

Future portable Kubernetes material may live here when a concrete deployment
slice exists. Appropriate content includes:

- reviewed manifests or one declared canonical render source;
- non-secret Kustomize overlays, Helm templates or values, and configuration
  key templates after the convention is selected;
- exact installation, rendering, validation, recovery, and rollback
  instructions tied to those files;
- sanitized evidence describing workload identity, namespace and service
  accounts, routes, policy, storage, probes, logging, and failure behavior.

This lane must not contain:

- application, policy, schema, evidence, lifecycle, or runtime implementation;
- real Secrets, kubeconfigs, certificates, private keys, tokens, passwords, or
  production environment values;
- private cluster endpoints, internal address inventories, tenant identifiers,
  or raw diagnostics;
- generated manifests whose canonical input and regeneration command are
  unknown;
- release, promotion, publication, source-admission, or correction decisions;
- object names, namespaces, providers, commands, routes, identities, or
  storage presented as current before their defining files and deployment
  evidence exist.

## Adoption packet

Keep Kubernetes adoption on **HOLD** until one reviewable packet establishes
all applicable items below.

| Required item | Evidence needed |
|---|---|
| Adoption decision | Why Kubernetes is required for the selected workload and what simpler deployment path it supersedes or complements |
| Cluster identity | Distribution/provider, version policy, environment class, custody, upgrade boundary, and supported API set |
| Canonical source | Plain manifests, Kustomize, Helm, Terraform, or another single declared render authority; generated-file relationship explicit |
| Workload identity | Repository-backed image or executable, immutable reference strategy, purpose, inputs, outputs, and finite failure behavior |
| Object identity | Exact namespaces, workloads, Services, accounts, roles, bindings, policies, routes, jobs, and storage objects |
| Isolation | Namespace and tenant boundaries, Pod security posture, admission controls, and cross-workload trust assumptions |
| Network | CNI and NetworkPolicy behavior, ingress/Gateway controller, DNS, egress, public/private routes, and negative reachability checks |
| Identity and RBAC | Service accounts, least-privilege verbs/resources/namespaces, workload identity, admin separation, and escalation checks |
| Configuration and secrets | Non-secret keys, external secret mechanism, rotation, encryption, access, and missing-secret behavior |
| Storage | Storage classes, claims, mount modes, backup/restore, retention, sensitivity, lifecycle-phase access, and deletion behavior |
| Health and resources | Startup/readiness/liveness meaning, graceful termination, disruption behavior, requests/limits, and capacity assumptions |
| Jobs and automation | Job/CronJob idempotency, concurrency, retry, duplicate-run, receipt, and lifecycle-authority boundaries |
| Observability | Redaction, identifiers, logs, metrics, audit events, access, retention, alerts, and sensitive-output handling |
| Supply chain | Image source, digest/signature policy, scanner boundary, base-image updates, and provenance evidence |
| Operations | Render, inspect, install, update, wait, diagnose, rollback, uninstall, and orphan-resource handling for the exact objects |
| Validation | Schema/render checks, client/server dry run where safe, policy/RBAC/route/storage tests, and sanitized cluster observation |
| Rollback | Prior known-good objects or removal target, data compatibility, traffic containment, verification, and recovery owner |
| Review | CODEOWNERS review plus accountable platform, security, workload, data, release, and operations decisions as applicable |

Names such as `apps-governed-api`, `kfm-runtime-model`, `kfm-public`, or
`kfm-internal` are not reserved or adopted by this README. Select identities
only with the manifests, consumers, and cluster evidence that make them real.

## Trust and sensitivity requirements

Any future Kubernetes slice must preserve KFM's governed boundary:

- Public clients use governed interfaces or released public-safe artifacts.
- Public ingress cannot reach RAW, WORK, QUARANTINE, canonical/internal
  stores, source credentials, model runtimes, or review/admin surfaces.
- A Pod, controller, role, policy, route, volume, or scheduled job does not
  gain evidence, policy, lifecycle, release, or publication authority.
- Workload and storage access is narrow, phase-specific, and least-privilege.
- Logs, events, probes, status, metrics, and diagnostics exclude secrets, raw
  payloads, living-person data, restricted geometry, culturally sensitive
  locations, harmful precision, prompts, and full sensitive evidence bodies.
- Jobs do not silently admit sources, promote lifecycle state, publish,
  release, correct, withdraw, or bypass review.
- Missing rights, sensitivity, provenance, identity, policy, storage,
  dependency, or rollback evidence keeps the deployment slice on hold.

## Repository inspection

The following commands inspect tracked repository state only. They do not
render objects, contact a cluster, or validate a deployment.

```bash
git ls-tree -r --name-only HEAD -- infra/kubernetes
git grep -n -E 'kubectl|kustomize|helm|apiVersion:|kind: (Deployment|StatefulSet|DaemonSet|Service|Ingress|Gateway|NetworkPolicy|ServiceAccount|Role|RoleBinding)' HEAD -- infra apps docs .github
```

At the pinned evidence snapshot, the first command lists only this README and
the repository search finds no implementation-bearing Kubernetes command or
object set.

Do not publish generic `kubectl apply`, `kubectl auth can-i`,
`kubectl kustomize`, or Helm commands as executable runbook steps until exact
inputs, tool versions, cluster scope, authentication, safe output handling, and
prerequisites exist. A successful render or dry run cannot by itself prove
applied state, reachability, authorization, isolation, health, rollback, or
operational safety.

## Failure, correction, and rollback

If a proposed Kubernetes slice cannot establish its canonical inputs,
workloads, identities, policies, routes, storage, credentials boundary,
negative access checks, or rollback, do not apply it.

If repository documentation overstates Kubernetes adoption:

1. correct the claim against current repository and sanitized cluster evidence;
2. keep operational state **UNKNOWN** where cluster evidence is unavailable;
3. do not expose private cluster details to manufacture proof;
4. close or revert the unmerged documentation change if the correction is
   wrong.

If a future applied object violates the trust boundary, contain traffic and
workloads according to an approved operational runbook, preserve sanitized
evidence, and follow the
[incident-response process](../../docs/security/INCIDENT_RESPONSE.md). A Git
revert alone does not change cluster state or restore data.

## Open verification

- [ ] Decide whether Kubernetes is an adopted KFM deployment mechanism.
- [ ] Identify the first exact workload and canonical manifest/render source.
- [ ] Establish cluster/provider/version custody and environment boundaries.
- [ ] Establish namespaces, workload identities, RBAC, policies, routes,
      configuration, secrets, storage, probes, resources, and observability.
- [ ] Establish sanitized applied-state and negative-access evidence without
      committing sensitive operational details.
- [ ] Bind rendering, policy, authorization, storage, route, and workload tests
      to exact files and cluster scope.
- [ ] Establish update, traffic containment, rollback, uninstall, data
      recovery, and orphan cleanup.
- [ ] Confirm accountable platform, security, workload, data, release, and
      operations review beyond repository routing.

Until those items close, this directory remains a documentation-only adoption
hold. A merged README, passing render, dry run, or draft manifest does not imply
cluster creation, applied state, deployment, release, promotion, or publication.

