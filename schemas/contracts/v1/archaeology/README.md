# `schemas/contracts/v1/archaeology/` — Archaeology Schema Compatibility Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-archaeology-readme
title: schemas/contracts/v1/archaeology/ — Archaeology Schema Compatibility Index
version: v1
status: draft
policy_label: public
owners:
  - <schema-steward>
  - <archaeology-domain-steward>
  - <cultural-review-steward>
  - <contract-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, schemas, contracts, v1, archaeology, cultural-heritage, compatibility, sensitive-domain, json-schema]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![domain](https://img.shields.io/badge/domain-archaeology-purple)
![posture](https://img.shields.io/badge/posture-compatibility--index-orange)
![canonical](https://img.shields.io/badge/canonical-NEEDS%20VERIFICATION-yellow)
![sensitivity](https://img.shields.io/badge/sensitivity-fail--closed-red)

## Purpose

`schemas/contracts/v1/archaeology/` is a draft compatibility and index lane for Archaeology schema notes.

It should help maintainers decide whether this shorter path remains an index, migrates into `schemas/contracts/v1/domains/archaeology/`, or is deprecated once canonical Archaeology schema placement is confirmed.

This README is documentation only. It is not a schema file, not contract prose, not policy, not validator code, not runtime code, not lifecycle data, and not a release record.

## Status & authority

| Field | Value |
|---|---|
| Document type | Archaeology schema compatibility README |
| Owning root | `schemas/` |
| Requested path | `schemas/contracts/v1/archaeology/` |
| Status | Draft |
| Authority level | Compatibility/index guidance. Canonical schemas, contracts, policy records, schema registry records, validators, fixtures, tests, ADRs, cultural/steward review decisions, and release records outrank this README. |
| Path posture | Current-session evidence confirms this README was blank before this update. |
| Canonical schema home | NEEDS VERIFICATION. ADR-0001 says domain-specific schemas should nest under `schemas/contracts/v1/domains/<domain>/...`; Archaeology docs reference `schemas/contracts/v1/domains/archaeology/`, but current-session search did not confirm that path exists. |
| Default posture | Do not create new canonical Archaeology schema definitions directly under `schemas/contracts/v1/archaeology/` unless an ADR or migration note explicitly changes the schema-home rule. |
| Sensitivity posture | Fail closed. Do not store precise archaeological location, protected cultural detail, private-owner detail, or sensitive candidate detail here. |
| Required reviewers | Schema steward, Archaeology domain steward, cultural-review steward, contract steward, and docs steward. |

## Placement basis

Current-session evidence confirms `schemas/README.md` defines `schemas/` as the root for machine-checkable shape and says schemas pair one-to-one with `contracts/`.

Current-session evidence confirms ADR-0001 says the default schema home is `schemas/contracts/v1/<family>/...`, and domain-specific schemas nest under `schemas/contracts/v1/domains/<domain>/...`.

Current-session search did not confirm a canonical `schemas/contracts/v1/domains/archaeology/README.md` path during this edit. Search did confirm Archaeology surfaces under contracts, fixtures, packages, governed API routes, catalog, registry, and validation pipelines.

Current-session evidence also confirms the Archaeology domain documentation references `schemas/contracts/v1/domains/archaeology/` as a related path and states that exact-location release defaults fail closed pending appropriate review and release support.

## Repo fit

```text
schemas/
├── README.md
└── contracts/
    └── v1/
        ├── archaeology/                # you are here; compatibility/index lane
        └── domains/
            └── archaeology/            # referenced domain lane; NEEDS VERIFICATION

contracts/
├── archaeology/                        # observed contract surface
└── domains/
    └── archaeology/                    # observed domain contract surface

fixtures/
└── domains/
    ├── archaeology/
    └── archaeology-public-safe/
```

## Current-session related evidence

| Evidence | Status |
|---|---|
| `schemas/contracts/v1/archaeology/README.md` | Blank before this update. |
| `schemas/README.md` | Confirms `schemas/` owns machine-checkable shape and pairs with `contracts/`. |
| ADR-0001 | Confirms `schemas/contracts/v1/` as the proposed canonical schema home and says domain schemas nest under `schemas/contracts/v1/domains/<domain>/...`. |
| Search for canonical Archaeology schema lane | Did not confirm `schemas/contracts/v1/domains/archaeology/README.md` in this edit. |
| Search for Archaeology surfaces | Found Archaeology contracts, fixtures, package, API, registry, catalog, and pipeline surfaces outside this path. |
| Archaeology domain documentation | References `schemas/contracts/v1/domains/archaeology/` and sets a fail-closed posture for exact-location and culturally sensitive release cases. |

This README does not verify schema contents, registry entries, fixture coverage, validator wiring, CI behavior, cultural-review workflow, or whether `schemas/contracts/v1/archaeology/` should remain as a compatibility path.

## Compatibility-lane responsibilities

| Responsibility | Expectation |
|---|---|
| Canonical-home decision | Determine whether canonical Archaeology schemas belong under `schemas/contracts/v1/domains/archaeology/`. |
| Drift prevention | Prevent duplicate canonical schemas under `schemas/contracts/v1/archaeology/`. |
| Migration notes | Record migration notes if compatibility files need to move. |
| Contract linkage | Point to paired Archaeology contract files when verified. |
| Fixture linkage | Point to valid, invalid, and public-safe fixtures when verified. |
| Validator linkage | Point to validators or CI checks when verified. |
| Registry linkage | Point to schema registry records when verified. |
| Sensitivity posture | Keep sensitive records out of this lane and point to governed policy/review paths instead. |
| Review status | Mark unverified implementation claims as NEEDS VERIFICATION. |

## What belongs here

- This compatibility README.
- Short index notes that point to canonical Archaeology schema files once confirmed.
- Migration notes for moving Archaeology schemas into the accepted schema-home path.
- Drift notes about duplicate or stale Archaeology schema paths.
- Links to canonical schemas, contracts, fixtures, validators, registry records, tests, and policy/review surfaces.
- Notes that preserve public-safe schema placement boundaries without exposing protected details.

## What does not belong here

- New canonical Archaeology schema definitions.
- Duplicate copies of canonical schema files.
- Contract prose.
- Policy rules.
- Validator implementation code.
- Runtime code.
- Lifecycle data payloads.
- EvidenceBundle contents or source records.
- Release records.
- Precise archaeological locations or protected cultural details.
- Claims that this path is canonical without ADR, registry, or steward confirmation.

## Compatibility status values

Use finite compatibility status values where possible:

| Status | Meaning |
|---|---|
| `INDEX_ONLY` | This path only indexes candidate canonical schema locations. |
| `ALIAS_CANDIDATE` | This path may be an alias for `schemas/contracts/v1/domains/archaeology/`. |
| `TRANSITIONAL` | Content is awaiting migration to canonical schema home. |
| `DEPRECATED` | Content should no longer receive new files. |
| `MIGRATE_TO_DOMAINS_ARCHAEOLOGY` | Content should move under `schemas/contracts/v1/domains/archaeology/` if that lane is confirmed. |
| `HELD_FOR_REVIEW` | Content needs schema, domain, cultural-review, or sensitivity review before use. |
| `NEEDS_VERIFICATION` | Path, pairing, fixture, validator, registry, or CI support has not been verified. |

## Minimal compatibility note

```markdown
# <archaeology-schema-compatibility-note-id>

## Status
INDEX_ONLY / ALIAS_CANDIDATE / TRANSITIONAL / DEPRECATED / MIGRATE_TO_DOMAINS_ARCHAEOLOGY / HELD_FOR_REVIEW / NEEDS_VERIFICATION

## Compatibility path
<schemas/contracts/v1/archaeology/... or N/A>

## Proposed canonical path
<schemas/contracts/v1/domains/archaeology/... or NEEDS VERIFICATION>

## Paired contract
<contracts/archaeology/... / contracts/domains/archaeology/... / N/A>

## Fixtures
<fixtures/domains/archaeology... or N/A>

## Validator
<tools/validators/... or N/A>

## Sensitivity posture
<public-safe / generalized / held / denied / NEEDS VERIFICATION>

## Notes
<short note grounded in repo evidence>

## Follow-up
<open items or none>
```

## Review checklist

- [ ] Canonical schema path is linked or marked NEEDS VERIFICATION.
- [ ] Paired contract path is linked or marked NEEDS VERIFICATION.
- [ ] Schema registry entry is linked or marked NEEDS VERIFICATION.
- [ ] Valid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Invalid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Public-safe fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Validator path is linked or marked NEEDS VERIFICATION.
- [ ] CI/schema-test support is linked or marked NEEDS VERIFICATION.
- [ ] Cultural-review or sensitivity posture is explicit.
- [ ] No duplicate canonical schema definitions are placed under `schemas/contracts/v1/archaeology/`.
- [ ] No protected location or sensitive cultural details are stored here.
- [ ] Any migration or compatibility claim cites an ADR, migration note, or verified repo evidence.

## Naming guidance

Recommended compatibility-note pattern:

```text
<YYYY-MM-DD>_<schema-shortname>_compatibility-note.md
```

Examples:

```text
2026-07-03_archaeology-site_compatibility-note.md
2026-07-03_public-safe-summary_compatibility-note.md
2026-07-03_sensitivity-transform_compatibility-note.md
```

Use lowercase filenames and hyphenated schema short names.

## Open verification

- [ ] Confirm CODEOWNERS for `schemas/contracts/v1/archaeology/`.
- [ ] Confirm whether `schemas/contracts/v1/archaeology/` should remain an index-only compatibility lane.
- [ ] Confirm whether canonical schema home should be `schemas/contracts/v1/domains/archaeology/`.
- [ ] Confirm whether `schemas/contracts/v1/domains/archaeology/README.md` should be created or already exists elsewhere.
- [ ] Confirm paired Archaeology contract paths.
- [ ] Confirm Archaeology schema registry records.
- [ ] Confirm valid fixture paths.
- [ ] Confirm invalid fixture paths.
- [ ] Confirm public-safe fixture paths.
- [ ] Confirm validator paths.
- [ ] Confirm CI schema-test coverage.
- [ ] Confirm cultural-review and sensitivity-review pointers for schema work.
- [ ] Confirm whether `schemas/README.md` should index this compatibility lane.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | Canonical-home decision, new Archaeology schema, Archaeology schema migration, validator update, fixture update, schema registry update, ADR update, sensitivity-review update, or compatibility-lane decision |
