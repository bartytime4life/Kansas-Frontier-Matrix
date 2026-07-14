<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-domains-hydrology-readme
title: configs/domains/hydrology/ — Hydrology Configuration Boundary
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Config steward · Hydrology steward · Consumer owner · Validation steward
created: 2026-07-13
updated: 2026-07-13
policy_label: public; config-sublane; hydrology; non-secret; non-authoritative; no-live-binding
current_path: configs/domains/hydrology/README.md
truth_posture: CONFIRMED canonical hydrology slug, explicit user-authorized directory, and repository-present domain doctrine / PROPOSED future consumer-bound templates / UNKNOWN consumers and precedence / NEEDS VERIFICATION owners and executable validation
related:
  - ../README.md
  - ../../README.md
  - ../../../docs/domains/hydrology/README.md
  - ../../../docs/registers/DOMAIN_LANE.md
  - ../../../docs/doctrine/directory-rules.md
notes:
  - "This initial lane contains documentation only. It does not create or activate a Hydrology configuration payload."
[/KFM_META_BLOCK_V2] -->

# Hydrology Domain Configuration

`configs/domains/hydrology/`

## Purpose

This directory defines the safe-to-commit configuration boundary for the canonical Hydrology lane. It may hold documented defaults or templates only after a real consumer, format, validation path, and rollback are verified.

## Authority level

**Configuration-supporting and non-authoritative.** Files here may configure a named consumer; they cannot establish hydrologic truth, source admission, warning status, policy, evidence, lifecycle state, or release approval.

## Status

- `CONFIRMED`: `hydrology` is a canonical domain slug and its doctrine README exists.
- `CONFIRMED`: this README is the only payload created in this lane.
- `PROPOSED`: future templates for explicitly bound consumers.
- `UNKNOWN`: loaders, precedence, unknown-key behavior, and runtime use.
- `NEEDS VERIFICATION`: owners, schemas, validators, tests, and CI enforcement.

Directory presence must not trigger discovery, activation, network access, or publication.

## What belongs here

- this configuration-boundary README;
- non-secret templates for a verified Hydrology consumer;
- tiny synthetic examples that preserve source roles and time context;
- conservative review, hold, or abstain defaults that cannot waive policy;
- config migration notes tied to a real key or path change.

## What does NOT belong here

- gauge observations, forecasts, flood products, source payloads, or lifecycle data;
- credentials, private endpoints, workstation paths, or live deployment bindings;
- logic that labels regulatory flood zones as observed inundation;
- emergency alerts, life-safety instructions, or current-warning authority;
- schemas, contracts, policy rules, registry rows, receipts, proofs, releases, or published products.

## Inputs

Any future payload requires a named consumer, declared format/version, authoritative contract/schema/policy references where applicable, safe placeholders, a no-network validation method, and a rollback path.

## Outputs

This lane currently outputs documentation only. A future file may support a verified consumer, but it cannot activate a source, advance lifecycle state, issue a warning, or authorize public exposure.

## Validation

- Markdown headings, links, and final newline resolve.
- Secret-like values, private endpoints, personal paths, and exact protected details are absent.
- Observed, regulatory, modeled, forecast, and historical roles remain distinct.
- Executable config validation is `NOT APPLICABLE` until a payload and consumer exist.

## Review burden

README changes require config/docs review and Hydrology-domain review. Payload changes additionally require the consumer owner and validation owner; public-safety or exposure-related settings require policy, security, and release review.

## Related folders

- [`../README.md`](../README.md) — parent domain-config contract.
- [`../../README.md`](../../README.md) — repository-wide config boundary.
- [`../../../docs/domains/hydrology/README.md`](../../../docs/domains/hydrology/README.md) — Hydrology doctrine.
- [`../../../docs/registers/DOMAIN_LANE.md`](../../../docs/registers/DOMAIN_LANE.md) — canonical lane register.
- [`../../../docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) — placement law.
- [`../../../docs/security/SECRETS.md`](../../../docs/security/SECRETS.md) — secret-handling posture.

## ADRs

No ADR is introduced here. Adding or renaming a domain, changing authority roots, or defining repository-wide config discovery/precedence remains ADR-class or separately governed work.

## Last reviewed

**2026-07-13**, against `main@10c82654c8ac2d039c3e6d1f7e31a1f074a3b6d1`. Review again before the first non-README payload or consumer binding.
