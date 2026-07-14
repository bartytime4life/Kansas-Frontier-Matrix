<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-domains-settlements-infrastructure-readme
title: configs/domains/settlements-infrastructure/ — Settlements and Infrastructure Configuration Boundary
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Config steward · Settlements/Infrastructure steward · Security reviewer · Consumer owner
created: 2026-07-13
updated: 2026-07-13
policy_label: public; config-sublane; settlements-infrastructure; critical-asset-aware; non-secret; non-authoritative; no-live-binding
current_path: configs/domains/settlements-infrastructure/README.md
truth_posture: CONFIRMED canonical settlements-infrastructure slug, explicit user-authorized directory, and repository-present domain doctrine / PROPOSED future consumer-bound templates / UNKNOWN consumers and precedence / NEEDS VERIFICATION owners and executable validation
related:
  - ../README.md
  - ../../README.md
  - ../../../docs/domains/settlements-infrastructure/README.md
  - ../../../docs/registers/DOMAIN_LANE.md
  - ../../../docs/doctrine/directory-rules.md
notes:
  - "This initial lane contains documentation only. It does not create or activate a Settlements/Infrastructure configuration payload."
[/KFM_META_BLOCK_V2] -->

# Settlements and Infrastructure Domain Configuration

`configs/domains/settlements-infrastructure/`

## Purpose

This directory defines the safe-to-commit configuration boundary for the canonical Settlements and Infrastructure lane. It may hold documented defaults or templates only after a real consumer, format, validation path, and rollback are verified.

## Authority level

**Configuration-supporting and non-authoritative.** Files here cannot establish settlement/jurisdiction identity, facility status, service areas, dependencies, critical-asset sensitivity, policy, or release approval.

## Status

- `CONFIRMED`: `settlements-infrastructure` is a canonical domain slug with a repository-present doctrine README.
- `CONFIRMED`: this README is the only payload created in this lane.
- `PROPOSED`: future templates for explicitly bound consumers.
- `UNKNOWN`: loaders, precedence, unknown-key behavior, and runtime use.
- `NEEDS VERIFICATION`: owners, schemas, validators, tests, critical-asset review, and CI.

Directory presence must not trigger discovery, live-source access, network calls, operational exposure, or publication.

## What belongs here

- this configuration-boundary README;
- non-secret templates for a verified consumer;
- synthetic examples preserving settlement, jurisdiction, facility, service-area, dependency, and critical-asset roles;
- conservative review/hold defaults;
- config migration notes tied to a real key or path change.

## What does NOT belong here

- critical-asset internals, dependencies, condition, vulnerability, access, or exact restricted facility detail;
- private facility/operator data, operational feeds, or source payloads;
- credentials, private endpoints, workstation paths, or live deployment bindings;
- settings that present administrative boundaries or generalized footprints as operational truth;
- policy, registry, schema, contract, receipt, proof, release, or publication authority.

## Inputs

Any future payload requires a named consumer, declared format/version, authoritative references, synthetic placeholders, critical-asset/security review, no-network validation, and rollback.

## Outputs

This lane currently outputs documentation only. A future file may support a verified consumer, but it cannot expose a critical asset, direct operations, redefine jurisdiction, or authorize release.

## Validation

- Markdown headings, links, and final newline resolve.
- No credentials, private endpoints, personal paths, restricted facility details, dependencies, or vulnerabilities exist.
- Settlement, jurisdiction, facility, service-area, dependency, and critical-asset roles remain distinct.
- Executable config validation is `NOT APPLICABLE` until a payload and consumer exist.

## Review burden

README changes require config/docs and domain review. Payload changes require consumer, validation, infrastructure/security, policy, rights, and release reviewers as applicable.

## Related folders

- [`../README.md`](../README.md) — parent domain-config contract.
- [`../../README.md`](../../README.md) — repository-wide config boundary.
- [`../../../docs/domains/settlements-infrastructure/README.md`](../../../docs/domains/settlements-infrastructure/README.md) — domain doctrine.
- [`../../../docs/registers/DOMAIN_LANE.md`](../../../docs/registers/DOMAIN_LANE.md) — lane and sensitivity register.
- [`../../../docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) — placement law.
- [`../../../docs/security/SECRETS.md`](../../../docs/security/SECRETS.md) — secret-handling posture.

## ADRs

No ADR is introduced here. Domain-set, critical-asset sensitivity, authority-root, or universal config-loading changes require separate governance.

## Last reviewed

**2026-07-13**, against `main@10c82654c8ac2d039c3e6d1f7e31a1f074a3b6d1`. Review again before the first non-README payload or consumer binding.
