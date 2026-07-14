<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-domains-agriculture-readme
title: configs/domains/agriculture/ — Agriculture Configuration Boundary
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Config steward · Agriculture steward · Privacy steward · Consumer owner
created: 2026-07-13
updated: 2026-07-13
policy_label: public; config-sublane; agriculture; privacy-aware; non-secret; non-authoritative; no-live-binding
current_path: configs/domains/agriculture/README.md
truth_posture: CONFIRMED canonical agriculture slug, explicit user-authorized directory, and repository-present domain doctrine / PROPOSED future consumer-bound templates / UNKNOWN consumers and precedence / NEEDS VERIFICATION owners and executable validation
related:
  - ../README.md
  - ../../README.md
  - ../../../docs/domains/agriculture/README.md
  - ../../../docs/registers/DOMAIN_LANE.md
  - ../../../docs/doctrine/directory-rules.md
notes:
  - "This initial lane contains documentation only. It does not create or activate an Agriculture configuration payload."
[/KFM_META_BLOCK_V2] -->

# Agriculture Domain Configuration

`configs/domains/agriculture/`

## Purpose

This directory defines the safe-to-commit configuration boundary for the canonical Agriculture lane. It may hold documented defaults or templates only after a real consumer, format, validation path, and rollback are verified.

## Authority level

**Configuration-supporting and non-authoritative.** Files here cannot establish crop, livestock, production, land-use, ownership, or producer truth; admit sources; decide privacy; or approve release.

## Status

- `CONFIRMED`: `agriculture` is a canonical domain slug with a repository-present doctrine README.
- `CONFIRMED`: this README is the only payload created in this lane.
- `PROPOSED`: future templates for explicitly bound consumers.
- `UNKNOWN`: loaders, precedence, unknown-key behavior, and runtime use.
- `NEEDS VERIFICATION`: owners, schemas, validators, tests, aggregation/privacy enforcement, and CI.

Directory presence must not trigger discovery, source activation, network access, or publication.

## What belongs here

- this configuration-boundary README;
- non-secret templates for a verified Agriculture consumer;
- tiny synthetic aggregate examples without real producer, parcel, field, or facility identifiers;
- conservative review/hold defaults that cannot waive privacy or aggregation requirements;
- config migration notes tied to a real key or path change.

## What does NOT belong here

- private producer data, person-parcel joins, field-level exposure, ownership claims, or reconstructable clues;
- real crop, livestock, yield, irrigation, facility, survey, or source payloads;
- credentials, private endpoints, workstation paths, or live deployment bindings;
- settings that present estimates/models as observations or assessor data as title truth;
- policy, registry, schema, contract, receipt, proof, release, or publication authority.

## Inputs

Any future payload requires a named consumer, declared format/version, authoritative references, synthetic placeholders, privacy/aggregation review, no-network validation, and rollback.

## Outputs

This lane currently outputs documentation only. A future file may support a verified consumer, but it cannot admit a source, identify a producer, waive aggregation, or authorize release.

## Validation

- Markdown headings, links, and final newline resolve.
- No credentials, private endpoints, personal paths, producer-identifying data, parcel joins, or protected facility detail exists.
- Aggregate, field-candidate, survey, modeled, and private roles remain distinct.
- Executable config validation is `NOT APPLICABLE` until a payload and consumer exist.

## Review burden

README changes require config/docs and Agriculture review. Payload changes require consumer, validation, privacy/aggregation, rights, policy, and release reviewers as applicable.

## Related folders

- [`../README.md`](../README.md) — parent domain-config contract.
- [`../../README.md`](../../README.md) — repository-wide config boundary.
- [`../../../docs/domains/agriculture/README.md`](../../../docs/domains/agriculture/README.md) — Agriculture doctrine.
- [`../../../docs/registers/DOMAIN_LANE.md`](../../../docs/registers/DOMAIN_LANE.md) — lane and sensitivity register.
- [`../../../docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) — placement law.
- [`../../../docs/security/SECRETS.md`](../../../docs/security/SECRETS.md) — secret-handling posture.

## ADRs

No ADR is introduced here. Domain-set, privacy/aggregation, authority-root, or universal config-loading changes require separate governance.

## Last reviewed

**2026-07-13**, against `main@10c82654c8ac2d039c3e6d1f7e31a1f074a3b6d1`. Review again before the first non-README payload or consumer binding.
