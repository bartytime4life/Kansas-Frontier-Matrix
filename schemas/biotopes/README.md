# `schemas/biotopes/` — Biotopes Schema Compatibility Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-biotopes-readme
title: schemas/biotopes/ — Biotopes Schema Compatibility Index
version: v1
status: draft
policy_label: public
owners:
  - <schema-steward>
  - <habitat-domain-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, schemas, biotopes, habitat, compatibility, schemas-contracts-v1, json-schema]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![domain](https://img.shields.io/badge/domain-habitat-blueviolet)
![posture](https://img.shields.io/badge/posture-compatibility--index-orange)
![canonical](https://img.shields.io/badge/canonical-NEEDS%20VERIFICATION-yellow)

## Purpose

`schemas/biotopes/` is a draft compatibility and index lane for Biotopes schema notes.

It should help maintainers decide whether `biotopes` is an accepted schema family, a Habitat sublane alias, an ecoregion/ecological-system schema concept, or a legacy/placeholder path that should migrate into a canonical `schemas/contracts/v1/...` home.

This README is documentation only. It is not a schema, not a contract, not policy, not validation code, and not lifecycle data.

## Status & authority

| Field | Value |
|---|---|
| Document type | Biotopes schema compatibility README |
| Owning root | `schemas/` |
| Requested path | `schemas/biotopes/` |
| Status | Draft |
| Authority level | Compatibility/index guidance. Canonical schemas, contracts, schema registry records, validators, fixtures, tests, ADRs, and steward decisions outrank this README. |
| Path posture | Current-session evidence confirms this README was blank before this update. |
| Canonical schema home | NEEDS VERIFICATION. ADR-0001 says domain-specific schemas should nest under `schemas/contracts/v1/domains/<domain>/...`. |
| Default posture | Do not create new canonical Biotopes schema definitions directly under `schemas/biotopes/` unless an ADR or migration note explicitly changes the schema-home rule. |
| Required reviewers | Schema steward, Habitat domain steward or relevant domain steward, and docs steward. |

## Placement basis

Current-session evidence confirms `schemas/README.md` defines `schemas/` as the root for machine-checkable shape and says schemas pair one-to-one with `contracts/`.

Current-session evidence confirms ADR-0001 says the default schema home is `schemas/contracts/v1/<family>/...`, and domain-specific schemas nest under `schemas/contracts/v1/domains/<domain>/...`.

Current-session search did not confirm a canonical `schemas/contracts/v1/domains/biotopes/` path. Search did surface Habitat ecoregions documentation that proposes a schema home under `schemas/contracts/v1/domains/habitat/ecoregions/`.

## Repo fit

```text
schemas/
├── README.md
├── biotopes/                         # you are here; compatibility/index lane
└── contracts/
    └── v1/
        └── domains/
            ├── habitat/              # possible canonical domain family; NEEDS VERIFICATION
            └── biotopes/             # not confirmed in current-session search
```

## Current-session related evidence

| Evidence | Status |
|---|---|
| `schemas/biotopes/README.md` | Blank before this update. |
| `schemas/README.md` | Confirms `schemas/` owns machine-checkable shape and pairs with `contracts/`. |
| ADR-0001 | Confirms `schemas/contracts/v1/` is the proposed canonical schema home. |
| Search for `biotopes` schemas | Did not confirm a canonical Biotopes schema directory. |
| `docs/domains/habitat/sublanes/ecoregions.md` | Confirms related Habitat/ecoregions planning and proposes `schemas/contracts/v1/domains/habitat/ecoregions/` as schema home. |

This README does not verify schema contents, schema registry entries, fixture coverage, validator wiring, CI behavior, or whether `biotopes` should be a domain, sublane, alias, or deprecated compatibility name.

## Compatibility-lane responsibilities

| Responsibility | Expectation |
|---|---|
| Canonical-home decision | Determine whether Biotopes belongs under `schemas/contracts/v1/domains/habitat/`, another domain, or a cross-cutting family. |
| Drift prevention | Prevent duplicate canonical schemas under `schemas/biotopes/`. |
| Migration notes | Record migration notes if legacy or compatibility files need to move. |
| Vocabulary alignment | Clarify whether `biotopes` is distinct from habitat, ecoregions, ecological systems, land cover, or vegetation communities. |
| Registry linkage | Point to schema registry records when verified. |
| Contract linkage | Point to paired `contracts/` files when verified. |
| Fixture linkage | Point to valid and invalid fixtures when verified. |
| Validator linkage | Point to validators or CI checks when verified. |
| Review status | Mark unverified implementation claims as NEEDS VERIFICATION. |

## What belongs here

- This compatibility README.
- Short index notes that point to the canonical Biotopes or Habitat schema home once confirmed.
- Migration notes for moving legacy Biotopes schemas into the accepted schema-home path.
- Drift notes about duplicate or stale Biotopes schema paths.
- Links to canonical schemas, contracts, fixtures, validators, registry records, and tests.
- Vocabulary notes that help stewards decide whether `biotopes` remains a valid schema family name.

## What does not belong here

- New canonical Biotopes schema definitions.
- Duplicate copies of canonical schema files.
- Contract prose.
- Policy rules.
- Validator implementation code.
- Runtime code.
- Lifecycle data payloads.
- EvidenceBundle contents or source records.
- Release records.
- Claims that `biotopes` is canonical without ADR, registry, or steward confirmation.

## Compatibility status values

Use finite compatibility status values where possible:

| Status | Meaning |
|---|---|
| `INDEX_ONLY` | This path only indexes candidate canonical schema locations. |
| `ALIAS_CANDIDATE` | `biotopes` may be an alias for another accepted schema family. |
| `TRANSITIONAL` | Content is awaiting migration to canonical schema home. |
| `DEPRECATED` | Content should no longer receive new files. |
| `MIGRATE_TO_HABITAT` | Content should move under an accepted Habitat schema lane. |
| `MIGRATE_TO_OTHER_DOMAIN` | Content should move under another accepted domain schema lane. |
| `NEEDS_VERIFICATION` | Path, pairing, fixture, validator, or CI support has not been verified. |

## Minimal compatibility note

```markdown
# <biotopes-schema-compatibility-note-id>

## Status
INDEX_ONLY / ALIAS_CANDIDATE / TRANSITIONAL / DEPRECATED / MIGRATE_TO_HABITAT / MIGRATE_TO_OTHER_DOMAIN / NEEDS_VERIFICATION

## Compatibility path
<schemas/biotopes/... or N/A>

## Proposed canonical path
<schemas/contracts/v1/... or NEEDS VERIFICATION>

## Paired contract
<contracts/... or N/A>

## Fixtures
<fixtures/... or N/A>

## Validator
<tools/validators/... or N/A>

## Vocabulary decision
<biotopes / habitat / ecoregions / ecological systems / vegetation communities / other / NEEDS VERIFICATION>

## Notes
<short note grounded in repo evidence>

## Follow-up
<open items or none>
```

## Review checklist

- [ ] Canonical schema path is linked or marked NEEDS VERIFICATION.
- [ ] Domain or sublane ownership is explicit.
- [ ] Vocabulary decision is recorded.
- [ ] Paired contract path is linked or marked NEEDS VERIFICATION.
- [ ] Schema registry entry is linked or marked NEEDS VERIFICATION.
- [ ] Valid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Invalid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Validator path is linked or marked NEEDS VERIFICATION.
- [ ] CI/schema-test support is linked or marked NEEDS VERIFICATION.
- [ ] No duplicate canonical schema definitions are placed under `schemas/biotopes/`.
- [ ] Any migration or compatibility claim cites an ADR, migration note, or verified repo evidence.

## Naming guidance

Recommended compatibility-note pattern:

```text
<YYYY-MM-DD>_<schema-shortname>_compatibility-note.md
```

Examples:

```text
2026-07-03_biotope-unit_compatibility-note.md
2026-07-03_ecological-system-alias_compatibility-note.md
2026-07-03_habitat-ecoregion-mapping_compatibility-note.md
```

Use lowercase filenames and hyphenated schema short names.

## Open verification

- [ ] Confirm CODEOWNERS for `schemas/biotopes/`.
- [ ] Confirm whether `schemas/biotopes/` should remain an index-only compatibility lane.
- [ ] Confirm whether `biotopes` is an accepted schema family, a Habitat sublane alias, or a deprecated placeholder.
- [ ] Confirm whether canonical schema home should be `schemas/contracts/v1/domains/habitat/...`, another domain lane, or a cross-cutting family.
- [ ] Confirm paired contract paths.
- [ ] Confirm schema registry records.
- [ ] Confirm valid fixture paths.
- [ ] Confirm invalid fixture paths.
- [ ] Confirm validator paths.
- [ ] Confirm CI schema-test coverage.
- [ ] Confirm whether `schemas/README.md` should index `biotopes/` directly as a compatibility lane.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | Canonical-home decision, new Biotopes schema, Habitat schema migration, validator update, fixture update, schema registry update, ADR update, or compatibility-lane decision |
