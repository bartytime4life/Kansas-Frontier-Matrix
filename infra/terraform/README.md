<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/infra-terraform-readme
title: infra/terraform/ — Infrastructure-as-Code Adoption and State Hold
type: per-directory-readme; infrastructure-boundary; adoption-hold
version: v2
status: draft; repository-grounded; documentation-only; adoption-hold; non-provisioning; non-deployment; non-release; non-publication
owner: NEEDS VERIFICATION — CODEOWNERS routes /infra/ to @bartytime4life; accountable infrastructure, security, platform, state, and operations stewardship remain unverified
created: 2026-07-03
updated: 2026-08-29
policy_label: repository-facing; infra; infrastructure-as-code; terraform; state-sensitive; deny-by-default; least-privilege; rollback-aware
current_path: infra/terraform/README.md
owning_root: infra/
responsibility: document the repository boundary for any future Terraform or compatible infrastructure-as-code slice without claiming tool adoption, provider selection, backend configuration, planned or applied resources, drift control, deployment, or rollback readiness
truth_posture: >
  CONFIRMED accepted Directory Rules through ADR-0029; infra/ as the deployment and exposure
  responsibility root; this directory contains only this README; no tracked .tf file, variable file,
  provider lock, backend template, module, environment stack, Terraform/OpenTofu workflow, or
  Terraform-specific validator; CODEOWNERS routing for /infra/; and no Terraform-specific ignore
  rule in the tracked root .gitignore / UNKNOWN whether any externally managed Terraform state,
  workspace, backend, provider account, plan, apply, resource, or drift process exists / HOLD tool,
  version, providers, modules, environments, state, credentials, commands, validation, apply,
  recovery, and rollback until repository-backed inputs and accountable evidence exist
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 349d0097e5f7533abe6cd8253f4bd7a30eccd003
  base_tree: ce0ed867de0ed08fafcc2495018e9c1f16e0e410
  target_prior_blob: 0de5bd49fdbfc5bff1189f36c684eb62f8f87219
  directory_tree_blob: 5c9ca98da75dcb9a55eee2272a993750806d3799
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption: docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md; accepted
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  inspection_method: exact target read; recursive repository tree; targeted infrastructure-as-code path, command, workflow, and ignore-pattern searches; direct doctrine, infra root, CODEOWNERS, exposure, incident, and key-rotation reads; no provider account, backend, state, plan, workspace, or deployed environment inspected
related:
  - ../README.md
  - ../hardening/CHECKLIST.md
  - ../kubernetes/README.md
  - ../systemd/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/security/EXPOSURE_PLAN.md
  - ../../docs/security/INCIDENT_RESPONSE.md
  - ../../docs/security/KEY_ROTATION.md
  - ../../.github/CODEOWNERS
  - ../../.gitignore
notes:
  - "v2 removes proposal-era providers, modules, environments, state practices, object topology, reviewers, file trees, and Terraform commands that lacked repository or environment evidence."
  - "The README is a placement, state-safety, and adoption boundary; it is not configuration, a plan, an apply receipt, a state inventory, a deployment record, or a release decision."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `infra/terraform/` — Infrastructure-as-Code Adoption and State Hold

`infra/terraform/` is the established repository lane for a future, reviewed
Terraform or compatible infrastructure-as-code slice. It currently contains
this README only.

> [!IMPORTANT]
> No tracked Terraform configuration, module, environment stack, provider lock,
> backend template, plan, state, installer, or Terraform-specific validator
> exists here. Do not infer that KFM has selected Terraform, OpenTofu, a cloud
> provider, a state backend, an account, a workspace, or any managed resource.

## Current state

| Question | Repository evidence | Safe conclusion |
|---|---|---|
| What is tracked in this lane? | `infra/terraform/README.md` only | **CONFIRMED:** documentation-only lane |
| Are configuration or rendering inputs tracked? | No `.tf`, variable, backend, provider-lock, module, or environment-stack file in the repository tree | **CONFIRMED:** no repository-backed configuration |
| Is Terraform or OpenTofu selected? | No implementation-bearing decision or executable input found | **HOLD** |
| Is there an IaC validator or CI gate? | No Terraform/OpenTofu-specific test, command, or workflow found | **CONFIRMED:** validation is unestablished |
| Does the repository ignore Terraform state and working files? | No Terraform-specific pattern found in the root `.gitignore` | **CONFIRMED:** repository-specific prevention is unestablished |
| Does an external backend, workspace, plan, state, or managed environment exist? | No provider or environment evidence was inspected | **UNKNOWN** |
| Can this README authorize planning or applying? | Documentation is not an operational transition record | **No** |

The current [`infra/` root](../README.md) records Terraform adoption,
implementation-bearing payloads, applied state, and deployed behavior as
unverified. Accepted
[Directory Rules](../../docs/doctrine/directory-rules.md), adopted through
[ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md),
place infrastructure-as-code under `infra/`; they do not select a tool,
provider, backend, account, resource topology, or environment.

## Evidence boundaries

Repository-adjacent surfaces do not close this lane:

- [`infra/kubernetes/README.md`](../kubernetes/README.md) and
  [`infra/systemd/README.md`](../systemd/README.md) are documentation-only
  adoption holds. They do not establish resources for Terraform to create.
- [`infra/hardening/CHECKLIST.md`](../hardening/CHECKLIST.md) provides review
  questions, not provider, backend, state, IAM, network, storage, or drift
  enforcement.
- The [exposure plan](../../docs/security/EXPOSURE_PLAN.md) defines a
  deny-by-default trust boundary while concrete infrastructure controls remain
  proposed or need verification. Desired posture is not a planned or applied
  resource graph.
- [`CODEOWNERS`](../../.github/CODEOWNERS) routes `/infra/` review to
  `@bartytime4life`. Repository routing does not establish provider custody,
  state access, apply approval, separation of duties, or operational ownership.
- The root [`.gitignore`](../../.gitignore) contains no Terraform-specific
  state, plan, variable, lock, or working-directory rule. This observation does
  not prove that sensitive state has been committed; it means this repository
  has not established a Terraform-specific ignore boundary.

Externally managed infrastructure may exist, but its state is **UNKNOWN**, not
absent. Credentials, state, private endpoints, account or tenant identifiers,
resource inventories, unredacted plans, and sensitive outputs must not be
committed to manufacture implementation proof.

## Lane contract

Future portable infrastructure-as-code material may live here when a concrete
provisioning slice exists. Appropriate content includes:

- one declared canonical configuration and module convention;
- non-secret provider, backend, variable, and environment templates;
- an intentionally reviewed dependency lock when the selected tool supports
  one;
- exact format, initialization, validation, plan-review, apply, drift,
  recovery, destroy, and rollback instructions tied to tracked files;
- sanitized evidence describing resource identity, exposure, IAM, storage,
  state custody, plan disposition, and finite failure behavior.

This lane must not contain:

- KFM policy, schema, evidence, lifecycle, application, runtime, release, or
  publication implementation;
- live credentials, tokens, certificates, private keys, kubeconfigs, provider
  configuration with secrets, or production variable values;
- state, state backups, working directories, crash logs, saved plans, or
  outputs whose sensitivity and retention are unresolved;
- private account, tenant, subscription, project, host, address, route, or
  resource inventories;
- generated configuration whose canonical source and regeneration procedure
  are unknown;
- provider, module, environment, resource, command, or backend names presented
  as current before their defining files and operational evidence exist.

## Adoption packet

Keep infrastructure-as-code adoption on **HOLD** until one reviewable packet
establishes all applicable items below.

| Required item | Evidence needed |
|---|---|
| Adoption decision | Why Terraform, OpenTofu, or another tool is required for the selected resource slice and what manual or existing mechanism it supersedes |
| Tool identity | Product, exact version policy, installation source, compatibility boundary, and upgrade ownership |
| Canonical source | Configuration root, module layout, environment strategy, generated-file relationship, and formatting convention |
| Provider identity | Exact providers, version constraints, permission needs, account/environment classes, and provider-custody boundary |
| Resource identity | Exact resource purposes, dependencies, inputs, outputs, consumers, sensitivity, and lifecycle |
| State custody | Backend type, encryption, locking, access, backup, retention, recovery, migration, and deletion behavior |
| Credentials | External credential mechanism, workload identity, rotation, revocation, missing-credential behavior, and log/output redaction |
| Isolation and network | Public/private boundaries, DNS, ingress, egress, firewall rules, denied surfaces, and negative reachability checks |
| IAM | Least-privilege plan/apply/read identities, administrative separation, exception handling, and escalation checks |
| Storage and data | Public-safe versus internal stores, encryption, retention, backup/restore, harmful-precision constraints, and deletion semantics |
| Planning | Initialization boundary, dependency resolution, refresh behavior, plan storage, redaction, review, expiry, and stale-plan rejection |
| Apply control | Accountable authorization, exact plan binding, concurrency, locks, timeouts, partial failure, receipts, and post-apply verification |
| Drift | Detection scope, cadence, refresh-only behavior, alerting, remediation authority, and unmanaged-resource handling |
| Validation | Format, initialize, validate, static policy, secrets, plan semantics, IAM, network, storage, and negative-access checks |
| Recovery | State restoration, import/move/remove procedures, provider outage behavior, data compatibility, and orphan handling |
| Rollback | Prior known-good configuration or forward-fix target, state/data consequences, traffic containment, verification, and recovery owner |
| Review | CODEOWNERS review plus accountable infrastructure, security, data, release, and operations decisions as applicable |

Names such as `local`, `staging`, `production`, `network`, `compute`,
`artifact-hosting`, AWS, Azure, GCP, Kubernetes, or a particular backend are not
reserved or adopted by this README. Select them only with the files, consumers,
accounts, and evidence that make them real.

## State and trust requirements

Any future infrastructure-as-code slice must preserve KFM's governed boundary:

- Public clients use governed interfaces or released public-safe artifacts.
- Planned or applied resources do not gain evidence, policy, lifecycle,
  admission, correction, release, or publication authority.
- Public routes and storage cannot expose RAW, WORK, QUARANTINE,
  canonical/internal stores, source credentials, model runtimes, review/admin
  surfaces, or unpublished candidates.
- State is sensitive by default because it can contain identifiers, addresses,
  outputs, relationships, and secret-adjacent values even when configuration
  contains no literal secret.
- Plans, logs, outputs, and drift reports exclude secrets, raw payloads,
  living-person data, restricted geometry, culturally sensitive locations,
  harmful precision, and full sensitive evidence bodies.
- Apply automation does not silently admit sources, promote lifecycle state,
  publish, release, correct, withdraw, or bypass review.
- Missing rights, sensitivity, provenance, identity, backend, credential,
  dependency, policy, plan, state, recovery, or rollback evidence keeps the
  provisioning slice on hold.

Follow the [incident-response process](../../docs/security/INCIDENT_RESPONSE.md)
and [key-rotation guidance](../../docs/security/KEY_ROTATION.md) if credentials,
state, saved plans, or sensitive outputs are exposed. Do not commit additional
sensitive material as evidence of the incident.

## Repository inspection

These commands inspect tracked repository state only. They do not initialize a
provider, read state, refresh resources, create a plan, contact an account, or
change infrastructure.

```bash
git ls-tree -r --name-only HEAD -- infra/terraform
git ls-files -- 'infra/terraform/*.tf' 'infra/terraform/**/*.tf' \
  'infra/terraform/*.tfvars*' 'infra/terraform/**/*.tfvars*'
git grep -n -E 'terraform (fmt|init|validate|plan|apply)|tofu (fmt|init|validate|plan|apply)' \
  HEAD -- .github tools tests Makefile pyproject.toml package.json
```

At the pinned evidence snapshot, the first command lists only this README; the
configuration pathspec and executable-command search return no implementation
surface.

Do not publish generic `terraform init`, `terraform validate`, `terraform
plan`, `terraform apply`, `terraform destroy`, or OpenTofu equivalents as
executable runbook steps until exact inputs, versions, backend behavior,
authentication, environment scope, safe output handling, approval, and
rollback prerequisites exist. `-backend=false` is not a universal safe mode,
and a successful format, validation, or plan result does not prove correct
state, authorization, isolation, apply safety, runtime health, recovery, or
rollback.

## Failure, correction, and rollback

If a proposed infrastructure slice cannot establish canonical inputs,
provider and resource identities, state custody, credentials, negative-access
checks, accountable apply control, recovery, or rollback, do not plan against
live state or apply it.

If repository documentation overstates Terraform adoption:

1. correct the claim against current repository and sanitized provider/state
   evidence;
2. keep operational state **UNKNOWN** where provider evidence is unavailable;
3. do not expose state, credentials, private topology, or account identifiers
   to manufacture proof;
4. close or revert the unmerged documentation change if the correction is
   wrong.

If future managed infrastructure violates the trust boundary, contain traffic
and credentials according to an approved operational runbook, preserve
sanitized evidence, and follow incident response. A Git revert does not roll
back an apply, restore state or data, destroy resources, revoke credentials, or
remove external exposure.

## Open verification

- [ ] Decide whether Terraform, OpenTofu, or another infrastructure-as-code
      mechanism is adopted by KFM.
- [ ] Identify the first exact resource slice and canonical configuration root.
- [ ] Establish tool, provider, account, environment, and resource identities.
- [ ] Establish backend locking, encryption, access, backup, retention,
      recovery, migration, and deletion behavior.
- [ ] Establish credential sourcing, least-privilege identities, rotation,
      revocation, and redaction.
- [ ] Establish repository ignore and secret/state/plan prevention controls.
- [ ] Bind formatting, initialization, validation, policy, plan, IAM, network,
      storage, and negative-access checks to exact files and environments.
- [ ] Establish accountable plan review, apply authorization, concurrency,
      receipts, post-apply verification, drift handling, and partial-failure
      recovery.
- [ ] Establish rollback or forward-fix, state/data recovery, orphan cleanup,
      credential containment, and provider-outage behavior.
- [ ] Confirm accountable infrastructure, security, data, release, and
      operations review beyond repository routing.

Until those items close, this directory remains a documentation-only adoption
and state hold. A merged README, successful format, validation, plan, or policy
scan does not imply provider selection, resource creation, applied state,
deployment, release, promotion, publication, or rollback readiness.
