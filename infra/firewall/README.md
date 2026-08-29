<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://infra/firewall/readme
title: Firewall infrastructure
type: README; infrastructure-boundary; exposure-control-index
version: v1.1
status: repository-grounded draft; documentation-only lane; enforcement absent
owners: NEEDS VERIFICATION — infrastructure, security, operations, governed API, and release stewards
updated: 2026-08-29
policy_label: restricted-review; deny-by-default-intent; no-deployment-authority
current_path: infra/firewall/README.md
truth_posture: >
  CONFIRMED directory placement, two-file Markdown-only inventory, loopback-bound
  placeholder Compose services, placeholder container/reverse-proxy surfaces, and
  bounded application-source deny workflow / UNKNOWN deployed firewall, ingress,
  egress, network zones, service bindings, operators, monitoring, and rollback /
  HOLD public exposure and production reliance
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: 2b0ea9bbbc9d9a120ea94d92fb4617d96fe7d2a0
  prior_blob: 6651354b43a291fa79b4b2b96c428caba29bfac6
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  deny_posture_blob: 48c7ac05b3e98e59c8ee9513bd5a3f9b2f06147e
  compose_blob: 8a45891700a501f6e18a921ce8d260956441e4b3
  deny_workflow_blob: a8ed744ff643a0a89e74988e6769fb1d5078a93e
  boundary_test_blob: 4035e537e6c52194928df5ab8ceb41a35f5f30ca
  method: complete target read plus exact subtree, adjacent infrastructure, workflow, test, doctrine, and open-PR inspection
related:
  - deny_by_default.md
  - ../README.md
  - ../compose/README.md
  - ../compose/docker-compose.yml
  - ../docker/README.md
  - ../reverse_proxy/README.md
  - ../hardening/CHECKLIST.md
  - ../../apps/governed-api/
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/security/EXPOSURE_PLAN.md
  - ../../.github/workflows/deny-test.yml
notes:
  - "This same-path documentation correction adds no firewall rule and changes no host, network, route, listener, deployment, release, or publication state."
  - "Repository absence of firewall payloads does not prove absence of controls in external systems; those systems were not inspected."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Firewall infrastructure

`infra/firewall/` is the repository home for firewall and network
exposure-control material. It currently contains documentation only. It does not
contain an enforceable firewall rule, deployment binding, completed review
record, or runtime verification result.

> [!WARNING]
> **Current state: `HOLD / NOT ENFORCED BY THIS LANE`.** The phrase
> “deny by default” is an intended security posture. Do not represent it as a
> deployed or tested firewall until exact rules, targets, review evidence,
> probes, monitoring, and rollback are present.

**Quick navigation:** [Authority](#authority-and-scope) ·
[Inventory](#current-repository-inventory) · [Boundary](#what-this-lane-may-own) ·
[Evidence](#what-current-evidence-does-and-does-not-prove) ·
[Required packet](#minimum-enforcement-packet) · [Validation](#validation) ·
[Response](#exposure-response) · [Open items](#open-verification-register)

## Authority and scope

Accepted [Directory Rules](../../docs/doctrine/directory-rules.md) assign
deployment, network, exposure, hardening, and provisioning material to
`infra/`. That placement determines responsibility; it does not establish that
a control is active.

This lane may describe or hold:

- reviewed host, container, cluster, cloud, or reverse-proxy firewall rules;
- ingress, egress, network-zone, port, protocol, and intended-consumer maps;
- environment-specific allowlists and default-deny configuration;
- safe validation and rollback procedures for those exact controls;
- redacted evidence references for rule application and negative probes.

This lane does not decide evidence truth, source admission, policy outcome,
rights, sensitivity, release, deployment approval, promotion, or publication.
It must not contain secrets, credentials, private keys, private hostnames,
production certificates, sensitive payloads, or unredacted internal topology.

## Current repository inventory

At the pinned base, `infra/firewall/` contains exactly:

| Path | Classification | Current effect |
|---|---|---|
| [`README.md`](README.md) | Human documentation and lane index | No rule application or verification |
| [`deny_by_default.md`](deny_by_default.md) | Intended-posture and hold boundary | No rule application or verification |

No UFW, nftables, iptables, cloud security-group, Kubernetes network-policy,
service-mesh, reverse-proxy allowlist, or equivalent rule payload is committed
in this lane.

That bounded repository result does **not** prove that external deployment
systems have no controls. External hosts, clouds, VPNs, routers, container
platforms, secret stores, and managed firewalls were not inspected.

### Adjacent implementation signals

| Surface | Current repository signal | Safe interpretation |
|---|---|---|
| [`infra/compose/docker-compose.yml`](../compose/docker-compose.yml) | Greenfield placeholder; binds governed API to `127.0.0.1:8080` and Explorer to `127.0.0.1:5173` | Loopback intent for that file only; not a firewall or deployment proof |
| [`infra/docker/Dockerfile.governed-api`](../docker/Dockerfile.governed-api) | Security-review placeholder with no application payload, listener, `CMD`, or `ENTRYPOINT` | Image-hardening scaffold, not a running API |
| [`infra/docker/Dockerfile.explorer-web`](../docker/Dockerfile.explorer-web) | Security-review placeholder with no application payload, listener, `CMD`, or `ENTRYPOINT` | Image-hardening scaffold, not a running Explorer |
| [`infra/reverse_proxy/caddy.example.caddyfile`](../reverse_proxy/caddy.example.caddyfile) | One-line Greenfield placeholder | No active proxy route, allowlist, TLS, or denial behavior |
| [`infra/hardening/CHECKLIST.md`](../hardening/CHECKLIST.md) | Draft review template with unchecked fields | Review method, not a completed review or sign-off |
| [`.github/workflows/deny-test.yml`](../../.github/workflows/deny-test.yml) | Runs named governed-API source and route checks | Application-boundary evidence only; no packet, listener, host, egress, or deployment probe |

## What this lane may own

### In scope

- exact rule templates whose environment and consumer are declared;
- public, private, loopback, VPN-only, steward-only, and denied zone maps;
- inbound and outbound requirements with protocol and port;
- references to the owning app, service, proxy, deployment, and rollback path;
- negative tests that exercise the configured boundary without exposing
  sensitive topology.

### Out of scope

- application authorization or admissibility rules, which belong under
  [`policy/`](../../policy/);
- application route behavior, which belongs with the owning
  [`apps/`](../../apps/) surface;
- semantic contracts or machine schemas;
- source, lifecycle, evidence, proof, receipt, or release records;
- production secrets or incident working data;
- claims that a repository rule was applied to an external target.

## What current evidence does and does not prove

The current deny workflow checks:

- unknown governed-API routes return a safe `404` envelope;
- non-`GET` methods on the scaffolded routes return a safe `405` envelope;
- the governed API route manifest remains bounded;
- named internal-store path literals are absent from governed-API source;
- named direct MapLibre, Cesium, and Ollama import prefixes are absent from
  governed-API Python source.

A passing workflow does not prove:

- host or cloud ingress is denied;
- unexpected ports or processes are absent;
- container, cluster, VPN, proxy, DNS, TLS, CORS, or security-group posture;
- egress to models, sources, or other endpoints is blocked;
- RAW, WORK, QUARANTINE, internal stores, admin surfaces, or model runtimes are
  unreachable at runtime;
- logs, caches, generated artifacts, databases, or external services are safe;
- a deployment, review, release, promotion, or publication occurred.

## Minimum enforcement packet

Do not promote this lane from documentation-only until a reviewed packet binds
all material fields:

| Required element | Minimum evidence |
|---|---|
| Target identity | Environment, host/cluster/account reference, deployment revision, and responsible service |
| Default action | Explicit ingress and egress defaults, including IPv4/IPv6 scope where applicable |
| Allowlist | Protocol, port, source/destination zone, intended consumer, purpose, and expiration/review trigger |
| Denials | RAW/WORK/QUARANTINE, canonical/internal stores, direct model runtime, admin/review surfaces, and unpublished artifacts |
| Application boundary | Governed public interface or released public-safe artifact route; no internal-store bypass |
| Sensitive-data posture | Rights, privacy, sovereignty, harmful precision, and restricted-geometry treatment |
| Validation | Configuration parser/linter, applied-state readback, listener inventory, and positive/negative reachability probes |
| Monitoring | Redacted denial/alert evidence, retention, escalation, and safe audit access |
| Rollback | Prior known-safe rule identity, restore command/procedure, readback, and rehearsal evidence |
| Review | Accountable infrastructure/security review; CI or CODEOWNERS alone is insufficient |

Store secrets and sensitive operational evidence outside Git. Link only to
approved, access-controlled, redacted evidence.

## Validation

### Repository-only inspection

Run from the repository root:

```bash
find infra/firewall -maxdepth 1 -type f -print | sort
git grep -nE '(^|[[:space:]])(EXPOSE|ports:|listen|reverse_proxy)' -- \
  infra apps runtime configs
```

These commands inventory committed text only. They do not inspect an applied
firewall, open sockets, external infrastructure, or production routing.

### Bounded application checks

The current workflow runs repository-owned tests equivalent to:

```bash
PYTHONPATH=apps/governed-api/src \
python -m pytest -q --strict-config --strict-markers \
  apps/governed-api/tests/test_boundary_guards.py
```

Interpret a pass using the limits in
[What current evidence does and does not prove](#what-current-evidence-does-and-does-not-prove).

### Applied-control validation

No repository-supported applied-firewall command exists at the pinned base.
Do not invent or paste host-modifying commands into this README. A future
environment-specific runbook must name its target, prerequisites, safe access
path, change window, validation, rollback, and lockout recovery before any
operator applies a rule.

## Exposure response

If a public or unintended path to a sensitive surface is suspected:

1. Treat the condition as `UNKNOWN / HOLD`; do not claim containment from
   repository prose or CI.
2. Preserve operator access and follow the approved environment-specific
   isolation procedure; none is currently established in this lane.
3. Disable or narrow the exposed route through separately authorized
   infrastructure control.
4. Record the affected target, time window, route/service, and redacted
   evidence without copying secrets or sensitive payloads into Git.
5. Inspect source, data, evidence, logs, caches, credentials, and published
   artifacts for exposure within their owning processes.
6. Rotate credentials and invoke incident, correction, withdrawal, release, or
   rollback procedures when their own evidence requires it.
7. Revalidate applied state and negative reachability before representing the
   condition as contained.

See the repository [security exposure plan](../../docs/security/EXPOSURE_PLAN.md)
for the broader response boundary.

## Maintenance

Update both firewall Markdown files when:

- a rule payload or environment-specific runbook is added;
- an intended listener, port, protocol, route, network zone, or egress need
  changes;
- a validation or monitoring surface becomes executable;
- the external deployment binding is established or retired;
- an incident or rehearsal changes the safe isolation or rollback procedure.

Keep intended, committed, validated, applied, monitored, and released states
distinct. A merge is not application; application is not validation; validation
is not review, release, deployment approval, promotion, or publication.

## Open verification register

| Item | Status | Evidence required |
|---|---:|---|
| Accountable lane ownership | `NEEDS VERIFICATION` | Named infrastructure, security, operations, API, and release authorities |
| Deployed firewall technology and target | `UNKNOWN` | Environment binding and applied-state readback |
| Ingress rule set | `UNKNOWN / HOLD` | Default action, allowlist, denials, listeners, probes |
| Egress rule set | `UNKNOWN / HOLD` | Destination/port requirements, default action, probes |
| IPv4/IPv6 parity | `UNKNOWN` | Applied rules and negative probes for both stacks |
| Proxy, VPN, cluster, and cloud controls | `UNKNOWN` | Current configuration and target-specific validation |
| Monitoring and retention | `UNKNOWN` | Redacted alerts/logs, access control, retention, escalation |
| Isolation and lockout recovery | `UNKNOWN / HOLD` | Reviewed operator procedure and rehearsal |
| Rollback target and rehearsal | `UNKNOWN / HOLD` | Known-safe rules, restore evidence, negative probes |
| Public readiness | `DENY BY DEFAULT` | Applied controls plus policy, evidence, review, release, and deployment records |

## Evidence and lineage

This correction uses current GitHub files as implementation evidence. Connected
Google Drive material was read only as proposed security and private-binding
lineage. Notion was read only for current coordination state. Neither source
establishes an active firewall, deployed target, approval, or review.

[Back to top](#top)
