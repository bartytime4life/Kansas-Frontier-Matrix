# `schemas/contracts/v1/common/` — Common Schema Family Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-common-readme
title: schemas/contracts/v1/common/ — Common Schema Family Index
version: v1
status: draft
policy_label: public
owners:
  - <schema-steward>
  - <contracts-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, schemas, contracts, v1, common, shared-schema, json-schema]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-common-blueviolet)
![posture](https://img.shields.io/badge/posture-shared--schema-orange)
![canonical](https://img.shields.io/badge/canonical-NEEDS%20VERIFICATION-yellow)

## Purpose

`schemas/contracts/v1/common/` is the draft index lane for shared schema families that are reused across KFM object families.

Common schemas should be small, stable, reusable shape definitions. They should not become a catch-all for domain-specific schemas, policy decisions, lifecycle data, runtime code, or release records.

This README is documentation only. It is not itself a schema file, contract prose, policy, validator code, runtime code, lifecycle data, or release authority.

## Status & authority

| Field | Value |
|---|---|
| Document type | Common schema family README |
| Owning root | `schemas/` |
| Requested path | `schemas/contracts/v1/common/` |
| Status | Draft |
| Authority level | Index guidance. Canonical schema files, paired contracts, schema registry records, validators, fixtures, tests, ADRs, and steward decisions outrank this README. |
| Path posture | Current-session evidence confirms this README existed as a minimal stub before this update. |
| Canonical status | NEEDS VERIFICATION for individual common subfamilies until schema files, registry entries, validators, fixtures, and CI support are verified. |
| Default posture | Use this lane only for cross-cutting reusable shapes. Domain-specific shapes belong under their accepted domain schema homes. |
| Required reviewers | Schema steward, contracts steward, affected object-family steward, and docs steward. |

## Placement basis

Current-session evidence confirms `schemas/README.md` defines `schemas/` as the root for machine-checkable shape and says schemas pair one-to-one with `contracts/`.

Current-session evidence confirms ADR-0001 says the default schema home is `schemas/contracts/v1/<family>/...`, while domain-specific schemas nest under `schemas/contracts/v1/domains/<domain>/...`.

Current-session evidence confirms `schemas/contracts/v1/common/uncertainty/README.md` exists as a draft shared-schema index lane with canonical status still NEEDS VERIFICATION.

Current-session search also found a common semantic contract at `contracts/common/temporal_window.md`, which may be relevant to future common schema pairing but has not been verified here as a schema-backed object family.

## Repo fit

```text
schemas/
├── README.md
└── contracts/
    └── v1/
        ├── common/                    # you are here
        │   └── uncertainty/           # existing shared-schema index lane
        └── domains/                   # domain-specific schema families
```

## Current-session related evidence

| Evidence | Status |
|---|---|
| `schemas/contracts/v1/common/README.md` | Minimal stub before this update. |
| `schemas/README.md` | Confirms `schemas/` owns machine-checkable shape and pairs with `contracts/`. |
| ADR-0001 | Confirms `schemas/contracts/v1/` as the proposed canonical schema home and separates common families from domain-specific homes. |
| `schemas/contracts/v1/common/uncertainty/README.md` | Existing child index lane for uncertainty-related shared schema notes. |
| Search for common schema surfaces | Found `contracts/common/temporal_window.md`; schema pairing remains NEEDS VERIFICATION. |

This README does not verify schema contents, schema registry entries, fixture coverage, validator wiring, CI behavior, or whether any proposed common subfamily is canonical.

## Common-lane responsibilities

| Responsibility | Expectation |
|---|---|
| Common-family index | List shared schema subfamilies and their status. |
| Drift prevention | Prevent domain-specific schema definitions from being placed in `common/` for convenience. |
| Contract linkage | Point to paired `contracts/common/` or other paired contract files when verified. |
| Fixture linkage | Point to valid and invalid fixtures when verified. |
| Validator linkage | Point to validators or CI checks when verified. |
| Registry linkage | Point to schema registry records when verified. |
| Version discipline | Keep shared schema changes stable and reviewable because many families may depend on them. |
| Review status | Mark unverified implementation claims as NEEDS VERIFICATION. |

## Current child lanes

| Path | Status | Notes |
|---|---|---|
| `schemas/contracts/v1/common/uncertainty/` | Draft / NEEDS VERIFICATION | Shared uncertainty-related schema index; canonical schema files not verified in this session. |

## Candidate common schema concepts

These are not confirmed as schema files in this session. Treat them as candidates until each has a schema, paired contract, registry record, fixture coverage, validator support, and review decision.

| Candidate | Possible purpose | Status |
|---|---|---|
| `uncertainty` | Shared uncertainty, confidence, or inference-quality shape support. | Draft child lane exists. |
| `temporal_window` | Shared time-window shape paired with common contract terminology. | NEEDS VERIFICATION. |
| `evidence_ref` | Shared evidence pointer shape if not already owned elsewhere. | NEEDS VERIFICATION. |
| `provenance_ref` | Shared provenance pointer shape if not already owned elsewhere. | NEEDS VERIFICATION. |
| `review_state` | Shared review-state enum or field group if not owned by release/review contracts. | NEEDS VERIFICATION. |
| `sensitivity_label` | Shared sensitivity label shape if not owned by policy/release schema lanes. | NEEDS VERIFICATION. |

## What belongs here

- This README.
- Shared-schema family indexes.
- Notes pointing to accepted common schema files.
- Migration notes for shared schema family placement.
- Drift notes about common schema duplication.
- Links to canonical schemas, paired contracts, fixtures, validators, registry records, and tests.

## What does not belong here

- Domain-specific schema definitions.
- Duplicate copies of schema files owned elsewhere.
- Contract prose.
- Policy rules.
- Validator implementation code.
- Runtime code.
- Lifecycle data payloads.
- EvidenceBundle contents or source records.
- Release records.
- Claims that a common subfamily is canonical without schema, registry, validator, fixture, or steward confirmation.

## Common schema status values

Use finite status values where possible:

| Status | Meaning |
|---|---|
| `INDEX_ONLY` | The path only indexes candidate common schema locations. |
| `COMMON_FAMILY_CANDIDATE` | The subfamily may become a shared schema family. |
| `ACTIVE_COMMON_FAMILY` | The subfamily has accepted schema files and review support. |
| `EMBEDDED_FIELD_GROUP` | The concept should remain embedded inside specific object schemas. |
| `MIGRATE_TO_DOMAIN` | The concept belongs under a domain schema home. |
| `MIGRATE_TO_OTHER_FAMILY` | The concept belongs under another cross-cutting family. |
| `DEPRECATED` | The path should no longer receive new files. |
| `NEEDS_VERIFICATION` | Path, pairing, fixture, validator, registry, or CI support has not been verified. |

## Minimal common-family note

```markdown
# <common-schema-family-note-id>

## Status
INDEX_ONLY / COMMON_FAMILY_CANDIDATE / ACTIVE_COMMON_FAMILY / EMBEDDED_FIELD_GROUP / MIGRATE_TO_DOMAIN / MIGRATE_TO_OTHER_FAMILY / DEPRECATED / NEEDS_VERIFICATION

## Common family
<family name>

## Proposed canonical path
<schemas/contracts/v1/common/... or NEEDS VERIFICATION>

## Paired contract
<contracts/common/... or N/A>

## Fixtures
<fixtures path or N/A>

## Validator
<tools/validators path or N/A>

## Downstream consumers
<object families or N/A>

## Notes
<short note grounded in repo evidence>

## Follow-up
<open items or none>
```

## Review checklist

- [ ] Common family purpose is clear.
- [ ] Canonical schema path is linked or marked NEEDS VERIFICATION.
- [ ] Paired contract path is linked or marked NEEDS VERIFICATION.
- [ ] Schema registry entry is linked or marked NEEDS VERIFICATION.
- [ ] Valid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Invalid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Validator path is linked or marked NEEDS VERIFICATION.
- [ ] CI/schema-test support is linked or marked NEEDS VERIFICATION.
- [ ] Downstream object families are identified or marked NEEDS VERIFICATION.
- [ ] Domain-specific fields are not placed here for convenience.
- [ ] Any migration or compatibility claim cites an ADR, migration note, or verified repo evidence.

## Naming guidance

Recommended note pattern:

```text
<YYYY-MM-DD>_<common-family>_common-schema-note.md
```

Examples:

```text
2026-07-03_uncertainty_common-schema-note.md
2026-07-03_temporal-window_common-schema-note.md
2026-07-03_sensitivity-label_common-schema-note.md
```

Use lowercase filenames and hyphenated family names.

## Open verification

- [ ] Confirm CODEOWNERS for `schemas/contracts/v1/common/`.
- [ ] Confirm accepted common schema subfamilies.
- [ ] Confirm paired `contracts/common/` paths.
- [ ] Confirm schema registry records.
- [ ] Confirm valid fixture paths.
- [ ] Confirm invalid fixture paths.
- [ ] Confirm validator paths.
- [ ] Confirm CI schema-test coverage.
- [ ] Confirm whether `uncertainty/` remains a child common-family index or becomes an active schema family.
- [ ] Confirm whether `schemas/README.md` should index this common lane.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing minimal stub |
| Next review trigger | New common schema family, schema-home migration, validator update, fixture update, schema registry update, ADR update, or compatibility-lane decision |
