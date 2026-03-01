<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/c4e6a92f-1db7-4933-979f-e18061ef4567
title: Threat Model Checklist
type: checklist
version: v1
status: draft
owners: kfm-core (TBD)
created: 2026-03-01
updated: 2026-03-01
policy_label: public
related:
  - ./README.md
  - ../security/README.md
tags: [kfm, quality, security, threat-model, checklist]
[/KFM_META_BLOCK_V2] -->

# Threat Model Checklist

Use this checklist when introducing or changing APIs, data flows, or policy enforcement paths.

## Scope and assets

- [ ] Threat model scope is defined (component, boundary, data classes).
- [ ] Sensitive assets and trust boundaries are identified.
- [ ] Data-flow diagram is updated or linked.

## Trust membrane controls

- [ ] Clients cannot bypass governed APIs.
- [ ] Policy decisions are enforced at request time.
- [ ] Evidence resolution is required for user-facing claims.
- [ ] Error payloads avoid leaking restricted metadata.

## Identity, authorization, and abuse resistance

- [ ] AuthN/AuthZ assumptions are documented.
- [ ] Deny-by-default behavior is verified for unknown cases.
- [ ] Rate limiting / abuse controls are documented where relevant.
- [ ] Privileged operations are auditable.

## Data protection and integrity

- [ ] Sensitive fields are redacted/generalized per policy.
- [ ] Artifact hashes/digests are verified where required.
- [ ] Input validation covers schema and boundary conditions.
- [ ] Supply-chain dependencies are reviewed for critical risk.

## Operational readiness

- [ ] Security-relevant logs and receipts are emitted.
- [ ] Alerting/triage ownership is clear.
- [ ] Rollback or kill-switch path is documented.
- [ ] Residual risks and accepted risks are listed with approvers.
