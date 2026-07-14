<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-domains-hazards-readme
title: configs/domains/hazards/ — Hazards Configuration Boundary
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Config steward · Hazards steward · Public-safety reviewer · Consumer owner
created: 2026-07-13
updated: 2026-07-13
policy_label: public; config-sublane; hazards; never-alert-authority; non-secret; non-authoritative; no-live-binding
current_path: configs/domains/hazards/README.md
truth_posture: CONFIRMED canonical hazards slug, explicit user-authorized directory, and repository-present domain doctrine / PROPOSED future consumer-bound templates / UNKNOWN consumers and precedence / NEEDS VERIFICATION owners and executable validation
related:
  - ../README.md
  - ../../README.md
  - ../../../docs/domains/hazards/README.md
  - ../../../docs/registers/DOMAIN_LANE.md
  - ../../../docs/doctrine/directory-rules.md
notes:
  - "This initial lane contains documentation only. It does not create or activate a Hazards configuration payload."
[/KFM_META_BLOCK_V2] -->

# Hazards Domain Configuration

`configs/domains/hazards/`

## Purpose

This directory defines the safe-to-commit configuration boundary for the canonical Hazards lane. It may hold documented defaults or templates only after a real consumer, format, validation path, and rollback are verified.

## Authority level

**Configuration-supporting and non-authoritative. KFM is never an emergency-alert or incident-command authority.** Files here cannot issue warnings, direct response, establish event truth, or approve release.

## Status

- `CONFIRMED`: `hazards` is a canonical domain slug with a repository-present doctrine README.
- `CONFIRMED`: this README is the only payload created in this lane.
- `PROPOSED`: future templates for explicitly bound contextual consumers.
- `UNKNOWN`: loaders, precedence, unknown-key behavior, and runtime use.
- `NEEDS VERIFICATION`: owners, schemas, validators, tests, public-safety review, and CI.

Directory presence must not trigger discovery, live-source access, warnings, response actions, network calls, or publication.

## What belongs here

- this configuration-boundary README;
- non-secret templates for a verified contextual Hazards consumer;
- synthetic examples preserving event, observation, warning/advisory context, declaration, exposure, and model roles;
- conservative inactive/hold defaults;
- config migration notes tied to a real key or path change.

## What does NOT belong here

- current alerts, warnings, evacuation instructions, emergency actions, or incident-command material;
- real event/observation/source payloads or operational facility/resource details;
- credentials, private endpoints, workstation paths, or live deployment bindings;
- permissive fallbacks that hide stale, missing, or failed source state;
- policy, registry, schema, contract, receipt, proof, release, or publication authority.

## Inputs

Any future payload requires a named consumer, declared format/version, authoritative official-source references, synthetic placeholders, stale/error behavior, no-network validation, and rollback.

## Outputs

This lane currently outputs documentation only. A future file may support cited historical/contextual display, but it cannot warn, recommend action, activate a source, or authorize release.

## Validation

- Markdown headings, links, and final newline resolve.
- No credentials, private endpoints, operational detail, current instructions, or live bindings exist.
- Event, observation, official warning context, declaration, exposure, and modeled roles remain distinct.
- The permanent non-alert-authority boundary remains explicit.
- Executable config validation is `NOT APPLICABLE` until a payload and consumer exist.

## Review burden

README changes require config/docs, Hazards, and public-safety review. Payload changes also require consumer, validation, official-source, policy, security, and release reviewers.

## Related folders

- [`../README.md`](../README.md) — parent domain-config contract.
- [`../../README.md`](../../README.md) — repository-wide config boundary.
- [`../../../docs/domains/hazards/README.md`](../../../docs/domains/hazards/README.md) — Hazards doctrine.
- [`../../../docs/registers/DOMAIN_LANE.md`](../../../docs/registers/DOMAIN_LANE.md) — lane and sensitivity register.
- [`../../../docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) — placement law.
- [`../../../docs/security/SECRETS.md`](../../../docs/security/SECRETS.md) — secret-handling posture.

## ADRs

No ADR is introduced here. The non-alert boundary cannot be relaxed by configuration; domain-set, authority-root, or universal config-loading changes require separate governance.

## Last reviewed

**2026-07-13**, against `main@10c82654c8ac2d039c3e6d1f7e31a1f074a3b6d1`. Review again before the first non-README payload or consumer binding.
