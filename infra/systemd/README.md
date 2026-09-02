<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/infra-systemd-readme
title: infra/systemd/ — systemd Adoption Hold and Service-Manager Boundary
type: per-directory-readme; infrastructure-boundary; adoption-hold
version: v2
status: draft; repository-grounded; documentation-only; adoption-hold; non-deployment; non-release; non-publication
owner: NEEDS VERIFICATION — CODEOWNERS routes /infra/ to @bartytime4life; accountable infrastructure, security, and operations stewardship remain unverified
created: 2026-07-03
updated: 2026-08-29
policy_label: repository-facing; infra; systemd; service-manager; deny-by-default; least-privilege; rollback-aware
current_path: infra/systemd/README.md
owning_root: infra/
responsibility: document the repository boundary for any future systemd units without claiming host installation, service activation, deployment, or exposure enforcement
truth_posture: >
  CONFIRMED accepted Directory Rules through ADR-0029; infra/ as the deployment and exposure
  responsibility root; this directory contains only this README; no tracked service, socket, timer,
  drop-in, environment template, installer, or systemd-specific validator; CODEOWNERS routing for
  /infra/; one governed API local entry point; and placeholder Compose loopback mappings / UNKNOWN
  whether any external host uses systemd for KFM, which units or identities exist, what is installed,
  enabled, active, reachable, monitored, retained, backed up, or recoverable / HOLD adoption of unit
  names, commands, dependencies, host paths, credentials, listeners, timers, hardening directives,
  deployment steps, and rollback until repository-backed files and review evidence exist
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: c00096f904c66053938355e52f4a5cb9402be6a4
  target_prior_blob: c88efd5d11a512cdd0ea47a6b7adb305af99a02f
  directory_tree_blob: 2c67bd9da9ea3e29ecaac123f88a6bb19f74bf2a
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption: docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md; accepted
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  compose_blob: 8a45891700a501f6e18a921ce8d260956441e4b3
  governed_api_entrypoint_blob: 4eb335c7c0b27f62c7419c478542e8fe40e1ff38
  inspection_method: exact target read; recursive repository tree; repository code search; direct doctrine, infra root, CODEOWNERS, Compose, application entrypoint, and exposure-plan reads; no host or deployed environment inspected
related:
  - ../README.md
  - ../compose/docker-compose.yml
  - ../hardening/CHECKLIST.md
  - ../../apps/governed-api/src/governed_api/main.py
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/security/EXPOSURE_PLAN.md
  - ../../docs/security/INCIDENT_RESPONSE.md
  - ../../.github/CODEOWNERS
notes:
  - "v2 removes proposal-era unit names, topology, reviewers, file trees, and host commands that lacked repository or environment evidence."
  - "The README is a placement and adoption boundary; it is not a unit file, deployment recipe, host observation, release record, or publication decision."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `infra/systemd/` — systemd Adoption Hold and Service-Manager Boundary

`infra/systemd/` is the established repository lane for a future, reviewed
systemd deployment slice. It currently contains this README only.

> [!IMPORTANT]
> No tracked unit, drop-in, environment template, installation procedure, or
> systemd-specific validator exists here. Do not infer that KFM is installed,
> enabled, running, healthy, hardened, monitored, deployed, or published on a
> systemd host.

## Current state

| Question | Repository evidence | Safe conclusion |
|---|---|---|
| What is tracked in this lane? | `infra/systemd/README.md` only | **CONFIRMED:** documentation-only lane |
| Are service, socket, or timer units tracked? | No matching files in the repository tree | **CONFIRMED:** no repository-backed unit set |
| Is there a systemd validator or CI gate? | No systemd-specific command, test, or workflow found | **CONFIRMED:** validation is unestablished |
| Does KFM run under systemd on any host? | No host inventory or runtime evidence was inspected | **UNKNOWN** |
| Are any units installed, enabled, active, or healthy? | No host evidence exists in the repository | **UNKNOWN** |
| Is public or private exposure enforced by systemd? | No unit or socket configuration exists here | **HOLD** |
| Can this README authorize deployment? | Documentation is not an operational transition record | **No** |

The current [`infra/` root](../README.md) likewise records the systemd unit
set as unestablished. Accepted [Directory Rules](../../docs/doctrine/directory-rules.md),
adopted through [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md),
place host and deployment configuration under `infra/`; they do not establish
that any particular service manager or unit has been adopted.

## Evidence boundaries

Repository-adjacent surfaces do not close this lane:

- [`apps/governed-api/src/governed_api/main.py`](../../apps/governed-api/src/governed_api/main.py)
  exposes a local Python entry point with a `127.0.0.1:8000` default. It does
  not define a systemd command, working directory, identity, environment,
  dependency, readiness check, or deployed listener.
- [`infra/compose/docker-compose.yml`](../compose/docker-compose.yml) is a
  Greenfield placeholder with loopback port mappings. Compose rendering and
  placeholder image builds do not prove a systemd deployment or provide unit
  semantics.
- [`infra/hardening/CHECKLIST.md`](../hardening/CHECKLIST.md) is a review
  checklist. Unchecked controls are not observed host hardening.
- The [exposure plan](../../docs/security/EXPOSURE_PLAN.md) defines a
  deny-by-default trust boundary, while its local deployment controls remain
  proposed or need verification. A desired posture is not deployed enforcement.
- [`CODEOWNERS`](../../.github/CODEOWNERS) routes `/infra/` review to
  `@bartytime4life`. This is repository review routing, not evidence of an
  accountable operations team, host custody, or deployment approval.

Externally managed hosts may exist, but their state is **UNKNOWN**, not absent.
Private hostnames, addresses, credentials, journal contents, and sensitive
deployment details must not be added merely to close this documentation gap.

## Lane contract

Future portable systemd materials may live here when a concrete deployment
slice exists. Appropriate content includes:

- reviewed `*.service`, `*.socket`, and `*.timer` files;
- non-secret drop-ins and environment-key templates;
- installation, verification, recovery, and rollback instructions tied to
  those exact files;
- sanitized evidence describing service identity, access boundaries,
  listeners, dependencies, readiness, logging, and failure behavior.

This lane must not contain:

- application or runtime implementation;
- real secrets, credentials, certificates, private keys, or production
  environment files;
- host-specific private paths, addresses, inventories, or raw journal dumps;
- policy, evidence, release, promotion, publication, or source-admission
  decisions;
- unit names, commands, users, groups, ports, or directories presented as
  current before their defining repository files and deployment evidence exist.

## Adoption packet

Keep systemd adoption on **HOLD** until one reviewable packet establishes all
applicable items below.

| Required item | Evidence needed |
|---|---|
| Workload identity | Exact repository-backed executable or command, purpose, inputs, outputs, and finite failure behavior |
| Unit identity | Exact filenames and unit names; system versus user scope; service, socket, and timer relationships |
| Process identity | Dedicated user/group decision, privilege rationale, and any bounded capabilities |
| Paths | Working directory, read-only inputs, writable state, runtime directories, mounts, and explicit denied paths |
| Configuration | Non-secret variable names, secret-reference mechanism, credential rotation boundary, and missing-config behavior |
| Dependencies | Ordering and requirement edges supported by the actual workload, not an invented boot diagram |
| Network | Bind address, port or socket, intended callers, firewall/proxy/VPN handoff, and negative reachability expectations |
| Lifecycle safety | Restart, timeout, shutdown, idempotency, duplicate-run, and partial-write behavior |
| Readiness | Workload-specific readiness/health meaning; a listening process alone is insufficient |
| Logging | Redaction, identifiers, access, retention, failure visibility, and handling of sensitive geometry or evidence |
| Hardening | Reviewed systemd directives and the minimum filesystem, device, namespace, and network access required |
| Operations | Install, enable, start, stop, update, reload-or-restart, inspect, and uninstall steps for the exact units |
| Validation | Static unit verification, workload tests, least-privilege checks, negative access tests, and sanitized host observation |
| Rollback | Prior known-good files or removal target, stop/disable behavior, state compatibility, verification, and recovery owner |
| Review | CODEOWNERS review plus accountable infrastructure, security, workload, and operations decisions as applicable |

Service names such as `kfm-governed-api.service`, `kfm-worker.service`, or
`kfm-runtime-model.service` are not reserved or adopted by this README. Select
names only with the unit files and consumer/deployment evidence that make them
real.

## Trust and sensitivity requirements

Any future unit must preserve KFM's governed boundary:

- Public clients use governed interfaces or released public-safe artifacts.
- Direct public access to RAW, WORK, QUARANTINE, canonical/internal stores,
  source credentials, model runtimes, and review/admin surfaces is denied.
- Filesystem access is narrow and stage-specific; a service-manager unit does
  not grant lifecycle, policy, release, or publication authority.
- Logs and status output exclude secrets, raw payloads, living-person data,
  restricted geometry, culturally sensitive locations, harmful precision,
  prompts, and full sensitive evidence bodies.
- Timers do not silently admit sources, promote lifecycle state, publish,
  release, correct, withdraw, or bypass review.
- Missing rights, sensitivity, provenance, dependency, or rollback evidence
  keeps the deployment slice on hold.

## Repository inspection

The following commands inspect tracked repository state only. They do not
inspect a host or validate a deployment.

```bash
git ls-tree -r --name-only HEAD -- infra/systemd
git grep -n -E 'systemd-analyze|systemctl|journalctl|\.(service|socket|timer)([^[:alnum:]_]|$)' HEAD -- infra apps docs .github
```

At the pinned evidence snapshot, the first command lists only this README and
the repository search finds documentation references rather than a tracked
systemd implementation.

Do not publish generic `systemctl`, `journalctl`, or `systemd-analyze verify`
commands as executable runbook steps until exact units, target scope, safe
output handling, and prerequisites exist. Once unit files are present,
`systemd-analyze verify` may become one static check; it cannot prove that a
unit is installed, enabled, active, correctly isolated, or operationally safe.

## Failure, correction, and rollback

If a proposed unit cannot establish its executable, identity, paths,
credentials boundary, listener, dependencies, negative access checks, or
rollback, do not install or activate it.

If repository documentation overstates systemd adoption:

1. correct the claim against current repository and sanitized host evidence;
2. keep operational state **UNKNOWN** where host evidence is unavailable;
3. do not expose private host details to manufacture proof;
4. close or revert the unmerged documentation change if the correction is
   wrong.

If a future deployed unit violates the trust boundary, stop or isolate the
affected service according to an approved operational runbook, preserve
sanitized evidence, and follow the
[incident-response process](../../docs/security/INCIDENT_RESPONSE.md). A Git
revert alone does not roll back host state.

## Open verification

- [ ] Decide whether systemd is an adopted KFM deployment mechanism.
- [ ] Identify the first exact workload and repository-backed unit set.
- [ ] Establish system/user scope, process identities, paths, configuration,
      dependencies, listeners, readiness, logging, and hardening.
- [ ] Establish sanitized host inventory and installed/enabled/active-state
      evidence without committing sensitive operational details.
- [ ] Bind validation and negative access checks to exact files and hosts.
- [ ] Establish install, update, disable, uninstall, and state-recovery steps.
- [ ] Confirm accountable infrastructure, security, workload, and operations
      review beyond repository routing.

Until those items close, this directory remains a documentation-only adoption
hold. A merged README, passing check, or draft unit proposal does not imply
installation, activation, deployment, release, promotion, or publication.

