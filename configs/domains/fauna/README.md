<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-domains-fauna-readme
title: configs/domains/fauna/ — Fauna Configuration Boundary
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Config steward · Fauna steward · Sensitivity steward · Consumer owner
created: 2026-07-13
updated: 2026-07-13
policy_label: public; config-sublane; fauna; sensitive-location-aware; non-secret; non-authoritative; no-live-binding
current_path: configs/domains/fauna/README.md
truth_posture: CONFIRMED canonical fauna slug, explicit user-authorized directory, and repository-present domain doctrine / PROPOSED future consumer-bound templates / UNKNOWN consumers and precedence / NEEDS VERIFICATION owners and executable validation
related:
  - ../README.md
  - ../../README.md
  - ../../../docs/domains/fauna/README.md
  - ../../../docs/registers/DOMAIN_LANE.md
  - ../../../docs/doctrine/directory-rules.md
notes:
  - "This initial lane contains documentation only. It does not create or activate a Fauna configuration payload."
[/KFM_META_BLOCK_V2] -->

# Fauna Domain Configuration

`configs/domains/fauna/`

## Purpose

This directory defines the safe-to-commit configuration boundary for the canonical Fauna lane. It may hold documented defaults or templates only after a real consumer, format, validation path, and rollback are verified.

## Authority level

**Configuration-supporting and non-authoritative.** Files here cannot establish occurrence truth, taxonomy, source admission, geoprivacy, sensitivity, policy, evidence, lifecycle state, or release approval.

## Status

- `CONFIRMED`: `fauna` is a canonical domain slug with a repository-present doctrine README.
- `CONFIRMED`: this README is the only payload created in this lane.
- `PROPOSED`: future templates for explicitly bound consumers.
- `UNKNOWN`: loaders, precedence, unknown-key behavior, and runtime use.
- `NEEDS VERIFICATION`: owners, schemas, validators, tests, geoprivacy enforcement, and CI.

Directory presence must not trigger discovery, source activation, network access, or publication.

## What belongs here

- this configuration-boundary README;
- non-secret templates for a verified Fauna consumer;
- synthetic examples without real occurrence, observer, media, or location data;
- conservative review/hold defaults that cannot lower sensitivity;
- config migration notes tied to a real key or path change.

## What does NOT belong here

- real occurrences, telemetry, nests, dens, roosts, hibernacula, spawning/breeding sites, or reconstructable clues;
- observer/private-person information or rights-restricted media metadata;
- credentials, private endpoints, workstation paths, or live deployment bindings;
- settings that upgrade modeled/range/candidate context into observed fact;
- geoprivacy, taxonomy, policy, registry, schema, contract, receipt, proof, release, or publication authority.

## Inputs

Any future payload requires a named consumer, declared format/version, authoritative references, synthetic placeholders, sensitivity/geoprivacy review, no-network validation, and rollback.

## Outputs

This lane currently outputs documentation only. A future file may support a verified consumer, but it cannot admit a source, reveal a location, lower a sensitivity tier, or authorize release.

## Validation

- Markdown headings, links, and final newline resolve.
- No credentials, private endpoints, personal paths, real occurrence data, or reconstructable protected-location clues exist.
- Source role, taxonomy uncertainty, geoprivacy, and sensitivity remain explicit and fail closed.
- Executable config validation is `NOT APPLICABLE` until a payload and consumer exist.

## Review burden

README changes require config/docs and Fauna review. Payload changes require consumer, validation, sensitivity/geoprivacy, rights, policy, and release reviewers as applicable.

## Related folders

- [`../README.md`](../README.md) — parent domain-config contract.
- [`../../README.md`](../../README.md) — repository-wide config boundary.
- [`../../../docs/domains/fauna/README.md`](../../../docs/domains/fauna/README.md) — Fauna doctrine.
- [`../../../docs/registers/DOMAIN_LANE.md`](../../../docs/registers/DOMAIN_LANE.md) — lane and sensitivity register.
- [`../../../docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) — placement law.
- [`../../../docs/security/SECRETS.md`](../../../docs/security/SECRETS.md) — secret-handling posture.

## ADRs

No ADR is introduced here. Domain-set, sensitivity-tier, authority-root, or universal config-loading changes require separate governance.

## Last reviewed

**2026-07-13**, against `main@10c82654c8ac2d039c3e6d1f7e31a1f074a3b6d1`. Review again before the first non-README payload or consumer binding.
