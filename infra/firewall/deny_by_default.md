<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://infra/firewall/deny-by-default
title: Deny-by-default network posture
type: infrastructure-posture; enforcement-hold
version: v1.0
status: intended posture; repository enforcement absent; deployment state unknown
owners: NEEDS VERIFICATION — infrastructure, security, operations, governed API, and release stewards
updated: 2026-08-29
policy_label: restricted-review; fail-closed; no-deployment-authority
current_path: infra/firewall/deny_by_default.md
truth_posture: >
  CONFIRMED KFM exposure intent and bounded repository application-source checks /
  UNKNOWN external and deployed network controls / HOLD public exposure,
  production reliance, and claims of enforcement
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: 2b0ea9bbbc9d9a120ea94d92fb4617d96fe7d2a0
  prior_blob: 48c7ac05b3e98e59c8ee9513bd5a3f9b2f06147e
  firewall_parent_blob: 6651354b43a291fa79b4b2b96c428caba29bfac6
  compose_blob: 8a45891700a501f6e18a921ce8d260956441e4b3
  deny_workflow_blob: a8ed744ff643a0a89e74988e6769fb1d5078a93e
related:
  - README.md
  - ../compose/docker-compose.yml
  - ../hardening/CHECKLIST.md
  - ../../apps/governed-api/
  - ../../docs/security/EXPOSURE_PLAN.md
  - ../../.github/workflows/deny-test.yml
notes:
  - "This document states an intended boundary and explicit hold. It is not a firewall rule, deployment record, validation receipt, approval, or release artifact."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Deny-by-default network posture

KFM intends to deny every ingress and egress path unless the path is required,
bounded, reviewed, and validated for an identified target. Public clients
should reach governed interfaces or released public-safe artifacts—not direct
model endpoints, RAW/WORK/QUARANTINE data, canonical internal stores, steward
surfaces, or unpublished candidates.

> [!CAUTION]
> **Enforcement status: `UNKNOWN / HOLD`.** At the pinned repository base,
> `infra/firewall/` contains no enforceable rule payload. Do not claim that a
> host, cloud, cluster, proxy, VPN, container network, or deployment is
> deny-by-default from this document.

## Required default

Until an environment-specific enforcement packet is approved and applied:

- public ingress is `DENY` except for separately governed and released routes;
- direct browser-to-model and public-to-internal-store paths are `DENY`;
- public access to RAW, WORK, QUARANTINE, proofs, receipts, source credentials,
  admin/review surfaces, and unpublished release material is `DENY`;
- unknown listeners, routes, ports, protocols, network zones, and consumers
  remain `HOLD`;
- outbound access from runtime, connectors, workers, and automation remains
  `HOLD` unless the destination and purpose are declared and constrained;
- IPv4 and IPv6 must be evaluated separately rather than assuming parity;
- repository prose, a loopback bind, static source scanning, or a green
  workflow cannot substitute for applied-state readback and reachability probes.

These statements constrain interpretation. They do not apply a rule.

## Current evidence boundary

Current GitHub evidence confirms:

- the placeholder Compose file binds two placeholder services to loopback;
- placeholder Dockerfiles contain no application payload or listener command;
- the reverse-proxy example is not implemented;
- the deny workflow checks selected governed-API route behavior, source-path
  literals, and forbidden import prefixes.

It does not confirm:

- an applied ingress or egress default;
- a complete listener, port, route, DNS, TLS, CORS, or network-zone inventory;
- runtime isolation of data stores, model endpoints, admin surfaces, logs,
  caches, databases, or generated artifacts;
- deployment monitoring, alerting, isolation, rollback, or lockout recovery.

See the [firewall lane README](README.md) for the exact inventory, validation
limits, minimum enforcement packet, exposure response, and open verification
register.

## Promotion condition

Represent this posture as enforced only when an exact target has:

1. versioned rule/configuration identity;
2. explicit ingress and egress defaults;
3. reviewed allowlists and required denials;
4. applied-state readback;
5. listener inventory and positive/negative reachability probes;
6. monitoring and safe audit evidence;
7. tested isolation, rollback, and access-recovery procedures;
8. accountable infrastructure and security review.

Even then, network validation does not establish source admission, evidence
truth, rights or sensitivity clearance, policy approval, release, deployment
approval, promotion, or publication.

[Back to top](#top)
