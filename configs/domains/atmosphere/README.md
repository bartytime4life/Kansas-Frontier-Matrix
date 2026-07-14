<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-domains-atmosphere-readme
title: configs/domains/atmosphere/ — Atmosphere Configuration Boundary
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Config steward · Atmosphere steward · Consumer owner · Validation steward
created: 2026-07-13
updated: 2026-07-13
policy_label: public; config-sublane; atmosphere; non-alert; non-secret; non-authoritative; no-live-binding
current_path: configs/domains/atmosphere/README.md
truth_posture: CONFIRMED canonical atmosphere slug, explicit user-authorized directory, and repository-present domain doctrine / PROPOSED future consumer-bound templates / UNKNOWN consumers and precedence / NEEDS VERIFICATION owners and executable validation
related:
  - ../README.md
  - ../../README.md
  - ../../../docs/domains/atmosphere/README.md
  - ../../../docs/registers/DOMAIN_LANE.md
  - ../../../docs/doctrine/directory-rules.md
notes:
  - "This initial lane contains documentation only. It does not create or activate an Atmosphere configuration payload."
[/KFM_META_BLOCK_V2] -->

# Atmosphere Domain Configuration

`configs/domains/atmosphere/`

## Purpose

This directory defines the safe-to-commit configuration boundary for the canonical Atmosphere lane. It may hold documented defaults or templates only after a real consumer, format, validation path, and rollback are verified.

## Authority level

**Configuration-supporting and non-authoritative.** Files here cannot establish weather, climate, air-quality, observation, forecast, warning, policy, evidence, lifecycle, or release truth.

## Status

- `CONFIRMED`: `atmosphere` is a canonical domain slug with a repository-present doctrine README.
- `CONFIRMED`: this README is the only payload created in this lane.
- `PROPOSED`: future templates for explicitly bound consumers.
- `UNKNOWN`: loaders, precedence, unknown-key behavior, and runtime use.
- `NEEDS VERIFICATION`: owners, schemas, validators, tests, and CI enforcement.

Directory presence must not trigger discovery, live-source access, network calls, alerts, or publication.

## What belongs here

- this configuration-boundary README;
- non-secret templates for a verified Atmosphere consumer;
- synthetic examples preserving observed, regulatory, modeled, forecast, climatological, and aggregate roles;
- conservative review/hold defaults;
- config migration notes tied to a real key or path change.

## What does NOT belong here

- real observations, forecasts, air-quality records, alerts, model output, or source payloads;
- credentials, private endpoints, workstation paths, or live deployment bindings;
- settings that present forecasts/models/climatology as current observations;
- emergency or life-safety instructions, alert authority, or silent stale-data fallback;
- policy, registry, schema, contract, receipt, proof, release, or publication authority.

## Inputs

Any future payload requires a named consumer, declared format/version, authoritative references, synthetic placeholders, temporal/source-role checks, no-network validation, and rollback.

## Outputs

This lane currently outputs documentation only. A future file may support a verified consumer, but it cannot activate a live source, issue an alert, relabel source roles, or authorize release.

## Validation

- Markdown headings, links, and final newline resolve.
- No credentials, private endpoints, personal paths, live bindings, or life-safety instructions exist.
- Observed, regulatory, modeled, forecast, climatological, and aggregate roles remain distinct and time-bounded.
- Executable config validation is `NOT APPLICABLE` until a payload and consumer exist.

## Review burden

README changes require config/docs and Atmosphere review. Payload changes require consumer, validation, temporal/source-role, policy, security, and release reviewers as applicable.

## Related folders

- [`../README.md`](../README.md) — parent domain-config contract.
- [`../../README.md`](../../README.md) — repository-wide config boundary.
- [`../../../docs/domains/atmosphere/README.md`](../../../docs/domains/atmosphere/README.md) — Atmosphere doctrine.
- [`../../../docs/registers/DOMAIN_LANE.md`](../../../docs/registers/DOMAIN_LANE.md) — canonical lane register.
- [`../../../docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) — placement law.
- [`../../../docs/security/SECRETS.md`](../../../docs/security/SECRETS.md) — secret-handling posture.

## ADRs

No ADR is introduced here. Domain-set, public-safety, authority-root, or universal config-loading changes require separate governance.

## Last reviewed

**2026-07-13**, against `main@10c82654c8ac2d039c3e6d1f7e31a1f074a3b6d1`. Review again before the first non-README payload or consumer binding.
