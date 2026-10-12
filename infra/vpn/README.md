<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/infra-vpn-readme
title: infra/vpn/ — Private Access Hold Boundary
type: per-directory-readme; infrastructure-boundary; operational-hold
version: v1.1.0
status: draft; repository-grounded; documentation-only; implementation-absent; external-state-unknown; deny-by-default; non-release; non-publication
owner: NEEDS VERIFICATION — CODEOWNERS routes /infra/ to @bartytime4life; accountable infrastructure, security, and operations stewardship remains unverified
created: 2026-07-03
updated: 2026-08-29
policy_label: repository-facing; infra; private-access; vpn; deny-by-default; least-privilege; no-public-raw-path; no-public-model-path
current_path: infra/vpn/README.md
owning_root: infra/
responsibility: document the repository-visible private-access boundary without claiming a selected VPN product, access grant, route, identity control, or deployed enforcement
truth_posture: >
  CONFIRMED same-path target; accepted Directory Rules v2 through ADR-0029; infra/ as the
  deployment, host, network, and exposure responsibility root; this README as the lane's only
  tracked file; a documentation-only review-console lane; a local governed API entry-point bind;
  a placeholder development Compose file; and an uncompleted hardening checklist / UNKNOWN any
  external VPN or overlay, product, peer, identity provider, device posture, route, ACL, firewall,
  DNS, secret store, access grant, log, monitor, environment, deployment, revocation, or recovery
  state / NEEDS VERIFICATION accountable stewards, access lifecycle, independent review, negative
  public-path proof, and operational rollback
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 2b0ea9bbbc9d9a120ea94d92fb4617d96fe7d2a0
  target_prior_blob: c15c1caa99f29eddf53f7a4befa9918e1bc8434e
  infra_readme_blob: 618f2578c4a0e00caefee7371bf83d2ee0102161
  hardening_checklist_blob: e1dffb88106ca22f82aff6fe8c67df0e34d2709f
  exposure_plan_blob: 787c68fe0bf30ad84e0ea89520e2169429097b99
  compose_blob: 8a45891700a501f6e18a921ce8d260956441e4b3
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  inspection_method: current main tree and direct file reads; no external host, VPN control plane, identity provider, device, network, secret store, access record, log, or runtime inspected
related:
  - ../README.md
  - ../compose/docker-compose.yml
  - ../firewall/README.md
  - ../hardening/CHECKLIST.md
  - ../reverse_proxy/README.md
  - ../../apps/governed-api/src/governed_api/main.py
  - ../../apps/review-console/README.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/security/EXPOSURE_PLAN.md
  - ../../docs/security/INCIDENT_RESPONSE.md
  - ../../docs/security/KEY_ROTATION.md
  - ../../.github/CODEOWNERS
tags:
  - kfm
  - infra
  - vpn
  - private-access
  - operational-hold
  - deny-by-default
  - least-privilege
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Private access hold

`infra/vpn/` is the repository lane for non-secret private-access boundary
documentation. It is currently a **documentation-only hold**, not a configured
VPN, overlay network, identity control, or access system.

The tracked repository does not select WireGuard, OpenVPN, Tailscale, ZeroTier,
or another product; define peers or groups; grant access; advertise routes;
apply ACLs; manage keys; or prove a connection. No person, device, service, or
environment should be described as privately reachable from this README.

> [!IMPORTANT]
> Repository absence does not prove that an externally managed private-access
> system is absent. External state is `UNKNOWN` until its accountable inventory,
> configuration identity, and runtime evidence are inspected through an
> authorized process.

## Current repository state

The lane contains exactly one tracked file:

| Path | Observed content | What it establishes |
|---|---|---|
| [`README.md`](README.md) | This private-access boundary | Documentation placement and hold guidance only |

The recursive repository tree contains no other path named for VPN, WireGuard,
OpenVPN, Tailscale, ZeroTier, or private access at the pinned evidence snapshot.
In particular, current GitHub evidence does not establish:

- a client, server, control plane, gateway, relay, exit node, or subnet router;
- peer, user, group, role, device, service-account, or emergency-access records;
- private address space, DNS, advertised routes, split/full-tunnel posture, ACLs,
  firewall rules, or network segmentation;
- authentication, MFA, SSO, device posture, enrollment, expiration, revocation,
  rotation, offboarding, audit, monitoring, alerting, or retention controls; or
- an installed configuration, running environment, connectivity test, isolation
  test, access review, incident rehearsal, or recovery record.

Adjacent repository surfaces identify design candidates, not private access:

| Surface | Confirmed repository evidence | Private-access conclusion |
|---|---|---|
| [`infra/compose/docker-compose.yml`](../compose/docker-compose.yml) | A greenfield development placeholder publishes two loopback-only port mappings | Loopback text is not VPN configuration, reachability proof, or an environment inventory |
| [Governed API entry point](../../apps/governed-api/src/governed_api/main.py) | Its direct entry point binds to loopback | A local bind does not prove an upstream, tunnel, ACL, deployment, or client path |
| [`apps/review-console/README.md`](../../apps/review-console/README.md) | A draft application boundary document exists; it explicitly leaves source, routes, auth, tests, and deployment unverified | A proposed steward surface is not reachable or authorized private access |
| [Hardening checklist](../hardening/CHECKLIST.md) | A reusable review template exists | Unchecked questions are not completed controls or validation evidence |
| [Exposure Plan](../../docs/security/EXPOSURE_PLAN.md) | Draft exposure guidance records private/admin verification gaps | Posture guidance is not network enforcement |

## Authority and scope

[Accepted ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)
adopts the [Directory Rules](../../docs/doctrine/directory-rules.md) standard.
Together with the [`infra/` index](../README.md), it places host, network,
exposure, and private-access mechanics under `infra/`. That placement does not
turn this lane into identity, application, policy, evidence, lifecycle, release,
or publication authority.

This lane may eventually hold reviewed, sanitized documentation and
implementation-bearing private-access configuration when an adopted topology
assigns those artifacts here. It must not hold:

- private keys, shared secrets, enrollment tokens, certificates, recovery
  codes, passwords, production bundles, QR codes, kubeconfigs, or credentials;
- unredacted peer, user, device, private address, hostname, route, DNS, access,
  vulnerability, or incident inventories;
- application roles, source admission, policy decisions, evidence truth,
  lifecycle data, release decisions, or publication approvals; or
- a shortcut around governed APIs, application authorization, sensitivity and
  rights controls, review state, correction, or rollback.

[`CODEOWNERS`](../../.github/CODEOWNERS) routes `infra/` changes to
`@bartytime4life`. That is a GitHub review route only. It does not establish
accountable infrastructure, security, operations, identity, data, or application
stewardship, and it does not prove that review occurred.

## Access posture

The repository can state requirements, but it cannot claim they are applied:

| Access class | Repository posture | Meaning at this snapshot |
|---|---|---|
| Public client to a private-access entry point | `DENY` required; enforcement `UNKNOWN` | Public clients must use governed public interfaces or released public-safe artifacts; no network denial was inspected |
| Steward, reviewer, administrator, or operator | `HOLD` | No verified identity, device, approval, route, application authorization, audit, expiration, or revocation chain exists |
| Model or AI runtime maintenance | `HOLD`; direct public access `DENY` required | No private maintenance path or applied public denial is established |
| RAW, WORK, or QUARANTINE access | `HOLD`; public access `DENY` required | Network membership alone must never grant lifecycle-data authority |
| Canonical/internal stores | `HOLD`; public access `DENY` required | No least-privilege grant, route, service identity, or audit evidence exists |
| Review or admin application | `HOLD` | Private transport would not replace application authentication, role checks, policy, provenance, or audit |
| Emergency access | `HOLD` | No accountable trigger, expiry, revocation, monitoring, or post-use review is established |
| Released public-safe artifact | Outside private-access authority | Release and publication remain separate governed states |

`HOLD` means the repository does not contain enough evidence to authorize or
describe an access path. It is not an applied firewall or ACL result.

Private connectivity, if later established, proves only transport reachability.
It must not be treated as permission to view restricted evidence, mutate
lifecycle state, approve a candidate, operate a model, release an artifact,
publish data, or bypass rights, privacy, sovereignty, sensitivity, and harmful
precision controls.

## Adoption packet

Before this lane describes an operational private-access system, one coherent
review packet must bind:

1. **Decision and scope** — product or provider, architecture decision,
   accountable maintainers, configuration authority, environments, intended
   users and services, and explicit non-goals.
2. **Identity and device controls** — verified identities, groups, MFA/SSO or
   equivalent, enrollment and recovery, device posture where applicable,
   service accounts, separation of duties, and application-level authorization.
3. **Route and trust inventory** — sanitized address and DNS classes, ingress
   and egress intent, advertised routes, split/full-tunnel posture, gateway and
   relay roles, ACL/firewall bindings, and explicit denied surfaces.
4. **Access lifecycle** — request, approval, provisioning, purpose, least
   privilege, start, expiry, periodic review, suspension, revocation,
   offboarding, emergency use, and shared-material rotation.
5. **Secrets and privacy** — secret-system references, key custody and rotation,
   recovery handling, log redaction, peer/device privacy, retention, and
   prohibition on sensitive topology in public review artifacts.
6. **Validation** — configuration identity, native syntax or plan result,
   authorized connectivity tests, unauthorized and public-path denial tests,
   route containment, DNS behavior, application authorization, logging, and
   evidence from each intended environment.
7. **Operations and recovery** — health, monitoring, alerting, incident path,
   rapid isolation, lockout recovery, prior configuration identity, rollback or
   forward-fix procedure, rehearsal, and post-change verification.

Do not add setup commands for an unselected product. Product adoption must pin
commands to the reviewed configuration format and supported version without
committing access material or exposing sensitive topology.

## Repository-only inspection

These commands inspect tracked repository evidence only; they do not contact or
test a VPN, identity system, device, host, or network:

```bash
git ls-tree -r --name-only HEAD -- infra/vpn
git grep -n -E 'vpn|wireguard|openvpn|tailscale|zerotier|private[-_ ]access' HEAD -- \
  infra apps docs .github
```

A passing documentation, security, deny-path, or application test remains
bounded to what it executes. It cannot prove tunnel reachability, public
isolation, identity assurance, route containment, access revocation, or an
external control plane without the corresponding configuration and environment
evidence.

## Exposure or credential response

If private-access material or an unintended route is exposed:

1. use the separately authorized operational path to isolate the affected
   access, route, identity, device, or environment;
2. revoke or rotate affected credentials and keys through their responsible
   secret and identity systems;
3. preserve configuration identities and redacted audit evidence without
   copying secrets, personal device details, private topology, or harmful
   precision into GitHub;
4. determine affected users, services, data classes, environments, and time
   bounds through accountable incident review;
5. verify public denial, route containment, application authorization, log
   hygiene, and revocation before restoration; and
6. record incident, correction, recovery, and follow-up evidence in their
   governing systems.

Use the repository's [incident-response](../../docs/security/INCIDENT_RESPONSE.md)
and [key-rotation](../../docs/security/KEY_ROTATION.md) guidance as review inputs;
their presence does not prove an operational responder, secret store, or
completed action.

This README cannot authorize access, revocation, rotation, isolation,
restoration, release, deployment, promotion, publication, or production
rollback.

## Open verification

- [ ] Identify any externally managed VPN or private-access system, or confirm
  through accountable review that none is in scope.
- [ ] Select and record the product, configuration authority, environments,
  owners, identity model, device posture, and secret system.
- [ ] Establish a sanitized route, DNS, ACL, firewall, and denied-surface
  inventory without committing sensitive topology.
- [ ] Establish request, approval, least-privilege, expiry, review, revocation,
  offboarding, emergency-access, and shared-material rotation procedures.
- [ ] Establish positive connectivity, unauthorized/public denial, route
  containment, application authorization, log-redaction, and revocation tests.
- [ ] Establish monitoring, alerts, retention, incident isolation, lockout
  recovery, rollback, and rehearsal evidence.
- [ ] Verify accountable infrastructure, security, operations, identity,
  application, data, and release review responsibilities.

Closing an item requires direct evidence. A document, pull request, merge,
access grant, network connection, release, deployment, promotion, and publication
are distinct states.
