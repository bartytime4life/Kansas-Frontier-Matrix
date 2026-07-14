<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-domains-geology-readme
title: configs/domains/geology/ — Geology Configuration Boundary
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Config steward · Geology steward · Consumer owner · Validation steward
created: 2026-07-13
updated: 2026-07-13
policy_label: public; config-sublane; geology; sensitivity-aware; non-secret; non-authoritative; no-live-binding
current_path: configs/domains/geology/README.md
truth_posture: CONFIRMED canonical geology slug, explicit user-authorized directory, and repository-present domain doctrine / PROPOSED future consumer-bound templates / UNKNOWN consumers and precedence / NEEDS VERIFICATION owners and executable validation
related:
  - ../README.md
  - ../../README.md
  - ../../../docs/domains/geology/README.md
  - ../../../docs/registers/DOMAIN_LANE.md
  - ../../../docs/doctrine/directory-rules.md
notes:
  - "This initial lane contains documentation only. It does not create or activate a Geology configuration payload."
[/KFM_META_BLOCK_V2] -->

# Geology Domain Configuration

`configs/domains/geology/`

## Purpose

This directory defines the safe-to-commit configuration boundary for the canonical Geology lane. It may hold documented defaults or templates only after a real consumer, format, validation path, and rollback are verified.

## Authority level

**Configuration-supporting and non-authoritative.** Files here cannot establish geologic truth, resource estimates, extraction/permit status, source admission, policy, evidence, lifecycle state, or release approval.

## Status

- `CONFIRMED`: `geology` is a canonical domain slug with a repository-present doctrine README.
- `CONFIRMED`: this README is the only payload created in this lane.
- `PROPOSED`: future templates for explicitly bound consumers.
- `UNKNOWN`: loaders, precedence, unknown-key behavior, and runtime use.
- `NEEDS VERIFICATION`: owners, schemas, validators, tests, sensitivity enforcement, and CI.

Directory presence must not trigger discovery, source activation, network access, or publication.

## What belongs here

- this configuration-boundary README;
- non-secret templates for a verified Geology consumer;
- synthetic examples that preserve occurrence, unit, deposit, estimate, extraction, permit, and model roles;
- conservative review/hold defaults;
- config migration notes tied to a real key or path change.

## What does NOT belong here

- real borehole, occurrence, deposit, resource, permit, infrastructure, or source payloads;
- sensitive resource/extraction detail or reconstructable infrastructure clues;
- credentials, private endpoints, workstation paths, or live deployment bindings;
- settings that present estimates, interpretations, or synthetic surfaces as observations;
- policy, registry, schema, contract, receipt, proof, release, or publication authority.

## Inputs

Any future payload requires a named consumer, declared format/version, authoritative references, synthetic placeholders, resource/infrastructure sensitivity review, no-network validation, and rollback.

## Outputs

This lane currently outputs documentation only. A future file may support a verified consumer, but it cannot admit a source, establish a resource claim, expose sensitive detail, or authorize release.

## Validation

- Markdown headings, links, and final newline resolve.
- No credentials, private endpoints, personal paths, restricted resource detail, or infrastructure clues exist.
- Occurrence, deposit, estimate, extraction, permit, interpretation, and model roles remain distinct.
- Executable config validation is `NOT APPLICABLE` until a payload and consumer exist.

## Review burden

README changes require config/docs and Geology review. Payload changes require consumer, validation, resource/infrastructure sensitivity, policy, rights, and release reviewers as applicable.

## Related folders

- [`../README.md`](../README.md) — parent domain-config contract.
- [`../../README.md`](../../README.md) — repository-wide config boundary.
- [`../../../docs/domains/geology/README.md`](../../../docs/domains/geology/README.md) — Geology doctrine.
- [`../../../docs/registers/DOMAIN_LANE.md`](../../../docs/registers/DOMAIN_LANE.md) — lane and sensitivity register.
- [`../../../docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) — placement law.
- [`../../../docs/security/SECRETS.md`](../../../docs/security/SECRETS.md) — secret-handling posture.

## ADRs

No ADR is introduced here. Domain-set, resource-sensitivity, authority-root, or universal config-loading changes require separate governance.

## Last reviewed

**2026-07-13**, against `main@10c82654c8ac2d039c3e6d1f7e31a1f074a3b6d1`. Review again before the first non-README payload or consumer binding.
