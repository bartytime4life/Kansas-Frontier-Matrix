<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-domains-soil-readme
title: configs/domains/soil/ — Soil Configuration Boundary
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Config steward · Soil steward · Consumer owner · Validation steward
created: 2026-07-13
updated: 2026-07-13
policy_label: public; config-sublane; soil; non-secret; non-authoritative; no-live-binding
current_path: configs/domains/soil/README.md
truth_posture: CONFIRMED canonical soil slug, explicit user-authorized directory, and repository-present domain doctrine / PROPOSED future consumer-bound templates / UNKNOWN consumers and precedence / NEEDS VERIFICATION owners and executable validation
related:
  - ../README.md
  - ../../README.md
  - ../../../docs/domains/soil/README.md
  - ../../../docs/registers/DOMAIN_LANE.md
  - ../../../docs/doctrine/directory-rules.md
notes:
  - "This initial lane contains documentation only. It does not create or activate a Soil configuration payload."
[/KFM_META_BLOCK_V2] -->

# Soil Domain Configuration

`configs/domains/soil/`

## Purpose

This directory defines the safe-to-commit configuration boundary for the canonical Soil lane. It may hold documented defaults or templates only after a real consumer, format, validation path, and rollback are verified.

## Authority level

**Configuration-supporting and non-authoritative.** Files here may configure a named consumer; they cannot establish soil truth, interpretation suitability, source admission, policy, evidence, lifecycle state, or release approval.

## Status

- `CONFIRMED`: `soil` is a canonical domain slug and its doctrine README exists.
- `CONFIRMED`: this README is the only payload created in this lane.
- `PROPOSED`: future templates for explicitly bound consumers.
- `UNKNOWN`: loaders, precedence, unknown-key behavior, and runtime use.
- `NEEDS VERIFICATION`: owners, schemas, validators, tests, and CI enforcement.

Directory presence must not trigger discovery, activation, network access, or publication.

## What belongs here

- this configuration-boundary README;
- non-secret templates for a verified Soil consumer;
- tiny synthetic examples that preserve survey, component, horizon, gridded, station, and interpretation-support distinctions;
- conservative review or abstain defaults;
- config migration notes tied to a real key or path change.

## What does NOT belong here

- soil survey records, profiles, property grids, model outputs, or lifecycle data;
- credentials, private endpoints, workstation paths, or live deployment bindings;
- settings that present suitability or capability interpretations as observed fact;
- private producer, parcel, or land-context detail;
- schemas, contracts, policy rules, registry rows, receipts, proofs, releases, or published products.

## Inputs

Any future payload requires a named consumer, declared format/version, authoritative references where applicable, safe placeholders, a no-network validation method, and a rollback path.

## Outputs

This lane currently outputs documentation only. A future file may support a verified consumer, but it cannot activate a source, reinterpret evidence, advance lifecycle state, or authorize public exposure.

## Validation

- Markdown headings, links, and final newline resolve.
- Secret-like values, private endpoints, personal paths, and protected land/producer context are absent.
- Survey, gridded, station, modeled, and interpretation-support roles remain distinct.
- Executable config validation is `NOT APPLICABLE` until a payload and consumer exist.

## Review burden

README changes require config/docs review and Soil-domain review. Payload changes additionally require the consumer and validation owners; land/privacy-sensitive settings require security, policy, and release review.

## Related folders

- [`../README.md`](../README.md) — parent domain-config contract.
- [`../../README.md`](../../README.md) — repository-wide config boundary.
- [`../../../docs/domains/soil/README.md`](../../../docs/domains/soil/README.md) — Soil doctrine.
- [`../../../docs/registers/DOMAIN_LANE.md`](../../../docs/registers/DOMAIN_LANE.md) — canonical lane register.
- [`../../../docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) — placement law.
- [`../../../docs/security/SECRETS.md`](../../../docs/security/SECRETS.md) — secret-handling posture.

## ADRs

No ADR is introduced here. Domain-set, authority-root, or repository-wide config discovery/precedence changes remain separately governed.

## Last reviewed

**2026-07-13**, against `main@10c82654c8ac2d039c3e6d1f7e31a1f074a3b6d1`. Review again before the first non-README payload or consumer binding.
