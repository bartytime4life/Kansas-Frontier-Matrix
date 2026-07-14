<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-domains-archaeology-readme
title: configs/domains/archaeology/ — Archaeology Configuration Boundary
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Config steward · Archaeology steward · Cultural/sovereignty reviewer · Consumer owner
created: 2026-07-13
updated: 2026-07-13
policy_label: public; config-sublane; archaeology; sovereignty-aware; sensitive-location-aware; non-secret; non-authoritative; no-live-binding
current_path: configs/domains/archaeology/README.md
truth_posture: CONFIRMED canonical archaeology slug, explicit user-authorized directory, and repository-present domain doctrine / PROPOSED future consumer-bound templates / UNKNOWN consumers and precedence / NEEDS VERIFICATION owners and executable validation
related:
  - ../README.md
  - ../../README.md
  - ../../../docs/domains/archaeology/README.md
  - ../../../docs/registers/DOMAIN_LANE.md
  - ../../../docs/doctrine/directory-rules.md
notes:
  - "This initial lane contains documentation only. It does not create or activate an Archaeology configuration payload."
[/KFM_META_BLOCK_V2] -->

# Archaeology Domain Configuration

`configs/domains/archaeology/`

## Purpose

This directory defines the safe-to-commit configuration boundary for the canonical Archaeology lane. It may hold documented defaults or templates only after a real consumer, format, validation path, cultural/sovereignty review, and rollback are verified.

## Authority level

**Configuration-supporting and non-authoritative.** Files here cannot establish archaeological/cultural truth, cultural authority, site status, consent, sensitivity, policy, evidence, lifecycle state, or release approval.

## Status

- `CONFIRMED`: `archaeology` is a canonical domain slug with a repository-present doctrine README.
- `CONFIRMED`: this README is the only payload created in this lane.
- `PROPOSED`: future templates for explicitly bound consumers.
- `UNKNOWN`: loaders, precedence, unknown-key behavior, and runtime use.
- `NEEDS VERIFICATION`: owners, schemas, validators, tests, sovereignty/cultural review, and CI.

Directory presence must not trigger discovery, source activation, network access, site exposure, or publication.

## What belongs here

- this configuration-boundary README;
- non-secret templates for a verified Archaeology consumer;
- synthetic examples without real sites, coordinates, cultural identifiers, or source payloads;
- conservative deny/hold/review defaults that cannot lower sensitivity;
- config migration notes tied to a real key or path change.

## What does NOT belong here

- exact or reconstructable archaeological sites, burials, human remains, sacred places, looting-risk detail, or culturally restricted knowledge;
- real survey records, site identifiers, private land context, oral histories, or source payloads;
- credentials, private endpoints, workstation paths, or live deployment bindings;
- settings that override cultural authority, sovereignty, consent, or restriction decisions;
- policy, registry, schema, contract, receipt, proof, release, or publication authority.

## Inputs

Any future payload requires a named consumer, declared format/version, authoritative references, synthetic placeholders, cultural/sovereignty and sensitivity review, no-network validation, and rollback.

## Outputs

This lane currently outputs documentation only. A future file may support a verified consumer, but it cannot reveal a site, lower sensitivity, override cultural authority, or authorize release.

## Validation

- Markdown headings, links, and final newline resolve.
- No credentials, private endpoints, personal paths, real site data, cultural identifiers, or reconstructable clues exist.
- Observed site, survey, interpretation, candidate, reconstruction, and cultural-authority roles remain distinct.
- Human remains and sacred-site denial boundaries are not configurable away.
- Executable config validation is `NOT APPLICABLE` until a payload and consumer exist.

## Review burden

README changes require config/docs, Archaeology, and cultural/sovereignty review. Payload changes also require consumer, validation, sensitivity, rights, policy, security, and release reviewers.

## Related folders

- [`../README.md`](../README.md) — parent domain-config contract.
- [`../../README.md`](../../README.md) — repository-wide config boundary.
- [`../../../docs/domains/archaeology/README.md`](../../../docs/domains/archaeology/README.md) — Archaeology doctrine.
- [`../../../docs/registers/DOMAIN_LANE.md`](../../../docs/registers/DOMAIN_LANE.md) — lane and sensitivity register.
- [`../../../docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) — placement law.
- [`../../../docs/security/SECRETS.md`](../../../docs/security/SECRETS.md) — secret-handling posture.

## ADRs

No ADR is introduced here. Cultural authority and permanent denial boundaries cannot be relaxed by config; domain-set, authority-root, or universal config-loading changes require separate governance.

## Last reviewed

**2026-07-13**, against `main@10c82654c8ac2d039c3e6d1f7e31a1f074a3b6d1`. Review again before the first non-README payload or consumer binding.
