<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/infra-hardening-readme
title: infra/hardening/README.md — Infrastructure Hardening Evidence Boundary
type: standard
version: v2
status: repository-grounded; review-only; non-enforcement; non-deployment
owners:
  - "NEEDS VERIFICATION — CODEOWNERS routes /infra/ to @bartytime4life; operational stewardship and approval authority are not established here"
created: 2026-07-03
updated: 2026-08-29
policy_label: public
related:
  - infra/README.md
  - infra/hardening/CHECKLIST.md
  - infra/docker/README.md
  - infra/compose/README.md
  - infra/firewall/README.md
  - infra/reverse_proxy/README.md
  - infra/vpn/README.md
  - infra/systemd/README.md
  - infra/kubernetes/README.md
  - infra/terraform/README.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/security/EXPOSURE_PLAN.md
  - docs/security/INCIDENT_RESPONSE.md
tags:
  - kfm
  - infra
  - hardening
  - evidence
  - review
  - deny-by-default
notes:
  - "This lane contains documentation and a review checklist, not deployed hardening controls."
  - "Repository checks named here have bounded static or image-build scope and are not operational enforcement evidence."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Infrastructure Hardening Evidence Boundary

This directory defines how to review infrastructure-hardening evidence without
turning a checklist or a passing repository check into a claim about deployed
controls. It does not configure a host, network, proxy, VPN, service manager,
cluster, cloud account, secret store, backup system, or monitoring service.

> [!IMPORTANT]
> Current disposition: **HOLD** for any claim of deployed or effective
> infrastructure hardening. The repository contains this README and an
> uncompleted review checklist in this lane. Bounded Docker and Compose checks
> exist elsewhere, but no aggregate hardening validator or deployed-environment
> evidence is present here.

## Authority and scope

[Directory Rules](../../docs/doctrine/directory-rules.md) and
[ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)
place deployment, host, network, and exposure mechanics under `infra/`.
Machine-enforceable policy belongs under `policy/`; schemas and contracts belong
under their canonical roots; release decisions and rollback artifacts belong
under `release/`.

Within that boundary, `infra/hardening/` may hold:

- repository-grounded hardening review guidance;
- checklists that point to evidence owned by an implementation lane; and
- redacted validation notes that do not expose secrets or private topology.

This directory must not become a parallel home for firewall rules, proxy
configuration, credentials, service units, cluster manifests, Terraform state,
policy bundles, release approvals, or incident working data.

## Repository evidence snapshot

The following state was confirmed on `main` at
`977cd78c127e297317ca0806b2e95b69458b256e`:

| Evidence | Confirmed repository fact | What it does not prove |
|---|---|---|
| [`README.md`](README.md) and [`CHECKLIST.md`](CHECKLIST.md) | These are the only files in `infra/hardening/`. | That any checklist item was reviewed, approved, applied, or monitored. |
| [Infrastructure root](../README.md) | `infra/` is the responsibility root for deployment and exposure mechanics. | The existence or state of any deployed environment. |
| [Compose file](../compose/docker-compose.yml) | Two placeholder services build from checked-in Dockerfiles and publish loopback-only ports. | Service startup, health, application behavior, network isolation, or public reachability. |
| [Static Compose tests](../../tests/infra/test_compose_static.py) | The checked-in placeholder has resolvable build paths, final non-root users, loopback port bindings, and none of the enumerated sensitive mounts or privileged escape strings. | Runtime identity, kernel confinement, filesystem permissions, egress denial, secret handling, or deployed configuration. |
| [Docker security-overlay tests](../../tests/infra/test_docker_security_overrides.py) | Exact Explorer review-image dependency overrides, lock integrity, and Dockerfile assertions are checked. | The absence of all vulnerabilities, provenance of a deployed image, registry custody, or runtime hardening. |
| [`infra-compose-smoke` workflow](../../.github/workflows/infra-compose-smoke.yml) | CI renders the Compose file and builds placeholder images without starting services. | Deployment, release, publication, health checks, governed API behavior, or effective network controls. |
| [CODEOWNERS](../../.github/CODEOWNERS) | `/infra/` review requests route to `@bartytime4life`. | Operational ownership, required approval, independent review, or separation of duties. |

The snapshot is repository evidence, not a statement about a machine or service
outside the repository. Re-check it against the review head whenever the files
or workflows above change.

## Evidence states

Use these labels in a hardening review:

| State | Meaning |
|---|---|
| `CONFIRMED` | The cited repository path or redacted environment record directly supports the claim at an identified revision or observation time. |
| `PROPOSED` | A desired control or design exists, but adoption or implementation is not established. |
| `UNKNOWN` | The repository does not contain enough evidence to determine the state. |
| `NEEDS VERIFICATION` | A named check must be performed against a specific repository revision or environment. |
| `HOLD` | Do not claim enforcement, exposure safety, deployment readiness, or rollback readiness until required evidence resolves. |

A checklist answer is not self-validating. `PASS` is meaningful only when each
applicable item links to evidence with a defined scope and observation point.
Unchecked items, placeholders, missing evidence, or unverifiable external state
remain `HOLD`.

## Control-evidence matrix

| Control area | Current repository evidence | Required evidence before an enforcement claim |
|---|---|---|
| Host baseline | No host configuration is present in this lane. | Identified hosts or image class, applied configuration, versioned baseline, inspection output, exception handling, and tested recovery. |
| Firewall and network policy | The [firewall lane](../firewall/README.md) documents a posture boundary. | Versioned rules tied to an environment, ingress and egress inventories, negative tests, monitoring, change authority, and rollback rehearsal. |
| Public edge, TLS, and CORS | The [reverse-proxy lane](../reverse_proxy/README.md) documents a routing hold. | Provider and domain identity, versioned routes, upstream bindings, certificates, headers, negative route tests, observation evidence, and rollback. |
| Private access | The [VPN lane](../vpn/README.md) documents a private-access hold. | Product and control-plane identity, routes, ACLs, identity lifecycle, revocation test, monitoring, recovery, and accountable stewardship. |
| Service management | The [systemd lane](../systemd/README.md) contains no adopted unit inventory. | Versioned units, target hosts, least-privilege settings, dependency and restart behavior, logs, install/disable procedure, and rollback rehearsal. |
| Containers and Compose | Dockerfiles, a bounded Compose placeholder, static tests, and an image-build workflow exist. | Immutable image identity, scan and provenance records, runtime configuration, secret and capability controls, service-start/health evidence, network behavior, and operational rollback. |
| Kubernetes | The [Kubernetes lane](../kubernetes/README.md) is an adoption hold. | Cluster identity, versioned manifests, namespaces, RBAC, network policy, storage, admission controls, observed rollout, and rollback rehearsal. |
| Terraform | The [Terraform lane](../terraform/README.md) is an adoption and state-safety hold. | Selected tool/provider, versioned configuration, backend and state custody, reviewed plan, apply authority, drift detection, recovery, and rollback evidence. |
| Secrets and keys | Repository doctrine says not to commit secrets; no secret store or custody is established here. | Named secret-store boundary, identities and access controls, redacted retrieval/rotation evidence, leak response, audit records, and verified owners. |
| Logging and monitoring | No deployed sink, retention rule, alert, or dashboard is established by this lane. | Event inventory, redaction tests, sink and access controls, retention, detection route, alert ownership, and incident exercise evidence. |
| Backup and restore | No backup target or restore exercise is established by this lane. | Protected asset inventory, backup identity and access, retention, integrity checks, tested restore, recovery objective, and recorded exercise result. |
| Incident containment | Draft security guidance is linked below. | Environment-specific detection and containment procedure, reachable escalation path, redacted exercise record, and tested restoration path. |

An artifact may satisfy one row without satisfying another. For example, a
Dockerfile ending with a non-root `USER` does not prove host hardening, firewall
enforcement, application authorization, or safe publication.

## Review procedure

1. Record the exact base, head, affected paths, and environment scope. If no
   environment is in scope, say `repository-only`.
2. Identify the implementation lane that owns each claimed control. Do not use
   this README as substitute evidence for that lane.
3. Complete a review copy of [`CHECKLIST.md`](CHECKLIST.md). Replace every
   placeholder, mark non-applicable items with a reason, and link redacted
   evidence for every checked item.
4. Separate repository evidence from environment evidence. Include revision,
   artifact digest, environment identity, and observation time where relevant.
5. Run only the validators that exist and record their exact scope. A green
   check must not be summarized more broadly than the check itself.
6. Classify missing, stale, inaccessible, or conflicting evidence as
   `UNKNOWN`, `NEEDS VERIFICATION`, or `HOLD`; do not infer the safer state.
7. Record correction and rollback paths separately. Reverting a documentation
   commit is not operational rollback.

Do not paste credentials, private keys, tokens, internal IPs, private hostnames,
restricted routes, exploit payloads, sensitive logs, or exact sensitive
locations into Markdown, pull requests, or workflow output. Use an approved
restricted evidence store and link only a redacted reference when one exists.

## Bounded repository checks

These commands inspect the checked-out repository; they do not contact or
inspect a deployed environment:

```bash
git ls-tree -r --name-only HEAD -- infra/hardening
git grep -n -E \
  'infra-compose-smoke|test_compose_static|test_docker_security_overrides' \
  HEAD -- .github tests Makefile infra
python -m unittest discover \
  --start-directory tests/infra \
  --pattern 'test_compose_static.py' \
  --verbose
python -m unittest discover \
  --start-directory tests/infra \
  --pattern 'test_docker_security_overrides.py' \
  --verbose
docker compose -f infra/compose/docker-compose.yml config --quiet
```

The two Python profiles are static, no-network checks. The Compose render
requires Docker Compose. Image builds are performed by the linked workflow, but
services are deliberately not started there. A missing tool or inaccessible
environment is `NOT_RUN` or `UNAVAILABLE`, never a pass.

Do not publish generic `iptables`, `nft`, proxy, VPN, `systemctl`, `kubectl`, or
`terraform` commands here. Operational commands require an adopted technology,
exact versioned files, an identified environment, authorization, validation,
and a tested recovery path.

## Trust and exposure requirements

The [Exposure Plan](../../docs/security/EXPOSURE_PLAN.md) describes desired
deny-by-default and governed-interface posture. Until environment evidence
exists, treat it as a requirement to verify, not proof that the requirement is
enforced.

Any hardening review that touches data or public surfaces must keep the
following boundaries visible:

- public clients use governed interfaces or released public-safe artifacts,
  not RAW, WORK, QUARANTINE, internal stores, credentials, or direct model
  runtimes;
- rights, privacy, sovereignty, provenance, consent, and harmful precision are
  fail-closed inputs to exposure decisions;
- generated language, maps, dashboards, indexes, and passing tests are not
  sovereign truth; and
- review, merge, release, deployment, and publication are distinct states.

## Failure, correction, and rollback

Stop the review and retain `HOLD` when evidence is missing, the observation
scope is unclear, a result cannot be reproduced, a control conflicts with
current repository doctrine, or sensitive material would need to be disclosed
to substantiate the claim.

For a repository-documentation defect, correct the file in a new reviewable
change or revert the unmerged branch. For a suspected exposure or operational
failure, follow the scoped containment path in
[Incident Response](../../docs/security/INCIDENT_RESPONSE.md); do not assume a
Git revert changes live infrastructure. Key or credential compromise requires
separately verified rotation and containment procedures; the draft
[Key Rotation Policy](../../docs/security/KEY_ROTATION.md) is guidance, not
evidence that rotation infrastructure or custody exists.

## Open verification backlog

- [ ] Confirm operational stewardship and accountable approval authority.
- [ ] Decide whether `CHECKLIST.md` should be revised to encode evidence states
      and the repository-only/deployed-environment distinction.
- [ ] Identify any deployed environments and the authoritative inventory for
      each one.
- [ ] Bind every claimed control to versioned implementation and observation
      evidence.
- [ ] Establish aggregate hardening validation only after the underlying lanes
      expose reliable, scoped checks.
- [ ] Verify secret custody, logging, monitoring, incident escalation, backup,
      restore, and operational rollback.
- [ ] Rehearse recovery without publishing sensitive topology or credentials.

[Back to top](#top)
