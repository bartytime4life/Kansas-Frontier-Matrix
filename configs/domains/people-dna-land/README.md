<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-domains-people-dna-land-readme
title: configs/domains/people-dna-land/ — People, DNA, and Land Configuration Boundary
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Config steward · People/DNA/Land steward · Privacy/consent reviewer · Consumer owner
created: 2026-07-13
updated: 2026-07-13
policy_label: public; config-sublane; people-dna-land; privacy-aware; consent-aware; non-secret; non-authoritative; no-live-binding
current_path: configs/domains/people-dna-land/README.md
truth_posture: CONFIRMED canonical people-dna-land slug, explicit user-authorized directory, and repository-present domain doctrine / PROPOSED future consumer-bound templates / UNKNOWN consumers and precedence / NEEDS VERIFICATION owners and executable validation
related:
  - ../README.md
  - ../../README.md
  - ../../../docs/domains/people-dna-land/README.md
  - ../../../docs/registers/DOMAIN_LANE.md
  - ../../../docs/doctrine/directory-rules.md
notes:
  - "This initial lane contains documentation only. It does not create or activate a People/DNA/Land configuration payload."
[/KFM_META_BLOCK_V2] -->

# People, DNA, and Land Domain Configuration

`configs/domains/people-dna-land/`

## Purpose

This directory defines the safe-to-commit configuration boundary for the canonical People, DNA, and Land lane. It may hold documented defaults or templates only after a real consumer, format, validation path, privacy/consent review, and rollback are verified.

## Authority level

**Configuration-supporting and non-authoritative.** Files here cannot establish identity, kinship, genealogy, DNA, consent, ownership, title, cultural rights, policy, evidence, lifecycle state, or release approval.

## Status

- `CONFIRMED`: `people-dna-land` is a canonical domain slug with a repository-present doctrine README.
- `CONFIRMED`: this README is the only payload created in this lane.
- `PROPOSED`: future templates for explicitly bound consumers.
- `UNKNOWN`: loaders, precedence, unknown-key behavior, and runtime use.
- `NEEDS VERIFICATION`: owners, schemas, validators, tests, privacy/consent enforcement, and CI.

Directory presence must not trigger discovery, source activation, person linking, network access, or publication.

## What belongs here

- this configuration-boundary README;
- non-secret templates for a verified consumer using unmistakably synthetic identities and places;
- conservative deny/hold/review defaults that cannot waive privacy or consent;
- aggregate-only example parameters without real people, DNA, parcels, or title assertions;
- config migration notes tied to a real key or path change.

## What does NOT belong here

- living-person data, DNA/genomic identifiers or segments, private genealogy, kinship, contact, consent, parcel joins, title claims, or reconstructable clues;
- real person, family, assessor, deed, court, tribal/cultural, or source payloads;
- credentials, private endpoints, workstation paths, or live deployment bindings;
- settings that treat assessor data as title truth or inference as verified identity/kinship;
- consent, cultural authority, policy, registry, schema, contract, receipt, proof, release, or publication authority.

## Inputs

Any future payload requires a named consumer, declared format/version, authoritative references, synthetic placeholders, privacy/consent/cultural-rights review, no-network validation, and rollback.

## Outputs

This lane currently outputs documentation only. A future file may support a verified consumer, but it cannot identify/link a person, expose DNA or private land context, record consent, establish title, or authorize release.

## Validation

- Markdown headings, links, and final newline resolve.
- No credentials, private endpoints, personal paths, real people, DNA, parcels, title assertions, consent records, or reconstructable clues exist.
- Assertions, life events, genealogy, DNA evidence, assessor records, title/ownership claims, and inference remain distinct.
- Living-person, DNA, private person-parcel, consent, and cultural-rights boundaries fail closed.
- Executable config validation is `NOT APPLICABLE` until a payload and consumer exist.

## Review burden

README changes require config/docs, domain, privacy/consent, and cultural-rights review. Payload changes also require consumer, validation, security, policy, legal/rights, and release reviewers.

## Related folders

- [`../README.md`](../README.md) — parent domain-config contract.
- [`../../README.md`](../../README.md) — repository-wide config boundary.
- [`../../../docs/domains/people-dna-land/README.md`](../../../docs/domains/people-dna-land/README.md) — domain doctrine.
- [`../../../docs/registers/DOMAIN_LANE.md`](../../../docs/registers/DOMAIN_LANE.md) — lane and sensitivity register.
- [`../../../docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) — placement law.
- [`../../../docs/security/SECRETS.md`](../../../docs/security/SECRETS.md) — secret-handling posture.

## ADRs

No ADR is introduced here. Privacy, consent, cultural-rights, and permanent denial boundaries cannot be relaxed by config; domain-set, authority-root, or universal config-loading changes require separate governance.

## Last reviewed

**2026-07-13**, against `main@10c82654c8ac2d039c3e6d1f7e31a1f074a3b6d1`. Review again before the first non-README payload or consumer binding.
