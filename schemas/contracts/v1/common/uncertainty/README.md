# `schemas/contracts/v1/common/uncertainty/` — Common Uncertainty Schema Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-common-uncertainty-readme
title: schemas/contracts/v1/common/uncertainty/ — Common Uncertainty Schema Index
version: v1
status: draft
policy_label: public
owners:
  - <schema-steward>
  - <contracts-steward>
  - <evidence-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, schemas, contracts, v1, common, uncertainty, confidence, provenance, json-schema]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-common-blueviolet)
![concept](https://img.shields.io/badge/concept-uncertainty-orange)
![canonical](https://img.shields.io/badge/canonical-NEEDS%20VERIFICATION-yellow)

## Purpose

`schemas/contracts/v1/common/uncertainty/` is a draft index for shared uncertainty-related schema notes.

It should help maintainers decide whether uncertainty is a reusable common schema family, a field group embedded inside other object schemas, or a compatibility path that should point to another accepted home.

This README is documentation only. It is not a schema file, not contract prose, not policy, not validator code, not runtime code, not lifecycle data, and not a release record.

## Status & authority

| Field | Value |
|---|---|
| Document type | Common uncertainty schema README |
| Owning root | `schemas/` |
| Requested path | `schemas/contracts/v1/common/uncertainty/` |
| Status | Draft |
| Authority level | Index guidance. Canonical schemas, contracts, schema registry records, validators, fixtures, tests, ADRs, and steward decisions outrank this README. |
| Path posture | Current-session evidence confirms this README was blank before this update. |
| Canonical schema home | NEEDS VERIFICATION. Current-session search did not confirm a dedicated common uncertainty schema family. |
| Default posture | Do not create canonical uncertainty schema definitions here until the schema steward confirms this family or records a migration note. |
| Required reviewers | Schema steward, contracts steward, evidence steward, and docs steward. |

## Placement basis

Current-session evidence confirms `schemas/README.md` defines `schemas/` as the root for machine-checkable shape and says schemas pair one-to-one with `contracts/`.

Current-session evidence confirms ADR-0001 says the default schema home is `schemas/contracts/v1/<family>/...`, while domain-specific schemas nest under `schemas/contracts/v1/domains/<domain>/...`.

Current-session search did not confirm a canonical uncertainty schema file or README. Search did surface uncertainty-adjacent usage in domain, source, evidence, provenance, and API documentation.

## Repo fit

```text
schemas/
├── README.md
└── contracts/
    └── v1/
        └── common/
            └── uncertainty/            # you are here; shared-schema index lane
```

## Current-session related evidence

| Evidence | Status |
|---|---|
| `schemas/contracts/v1/common/uncertainty/README.md` | Blank before this update. |
| `schemas/README.md` | Confirms `schemas/` owns machine-checkable shape and pairs with `contracts/`. |
| ADR-0001 | Confirms `schemas/contracts/v1/` as the proposed canonical schema home. |
| Search for uncertainty schema family | Did not confirm a dedicated canonical uncertainty schema family. |
| Search for uncertainty usage | Found uncertainty-adjacent references across domain, source, evidence, provenance, and API documents. |

This README does not verify schema contents, schema registry entries, fixture coverage, validator wiring, CI behavior, or whether uncertainty should be a separate common schema family.

## Common uncertainty responsibilities

| Responsibility | Expectation |
|---|---|
| Canonical-home decision | Determine whether uncertainty belongs here as a common schema family or inside specific object schemas. |
| Drift prevention | Prevent duplicate uncertainty field definitions across schema families. |
| Contract linkage | Point to paired common, evidence, provenance, or domain contract text when verified. |
| Fixture linkage | Point to valid and invalid fixtures when verified. |
| Validator linkage | Point to validators or CI checks when verified. |
| Registry linkage | Point to schema registry records when verified. |
| Vocabulary alignment | Clarify confidence, uncertainty, inference, observation, evidence strength, source reliability, and review state boundaries. |
| Review status | Mark unverified implementation claims as NEEDS VERIFICATION. |

## What belongs here

- This README.
- Short index notes that point to accepted uncertainty schema definitions once confirmed.
- Migration notes for moving uncertainty schema files into the accepted schema-home path.
- Drift notes about duplicate or stale uncertainty fields.
- Links to canonical schemas, contracts, fixtures, validators, registry records, and tests.
- Notes that help maintainers keep uncertainty metadata distinct from evidence, provenance, policy, and review state.

## What does not belong here

- New canonical uncertainty schema definitions before steward confirmation.
- Duplicate copies of canonical schema files.
- Contract prose.
- Policy rules.
- Validator implementation code.
- Runtime code.
- Lifecycle data payloads.
- EvidenceBundle contents or source records.
- Release records.
- Claims that this path is canonical without ADR, registry, or steward confirmation.

## Compatibility status values

Use finite status values where possible:

| Status | Meaning |
|---|---|
| `INDEX_ONLY` | This path only indexes candidate canonical schema locations. |
| `COMMON_FAMILY_CANDIDATE` | Uncertainty may become a common schema family. |
| `EMBEDDED_FIELD_GROUP` | Uncertainty may remain embedded in specific object schemas. |
| `TRANSITIONAL` | Content is awaiting migration to the accepted schema home. |
| `DEPRECATED` | Content should no longer receive new files. |
| `NEEDS_VERIFICATION` | Path, pairing, fixture, validator, registry, or CI support has not been verified. |

## Minimal compatibility note

```markdown
# <uncertainty-schema-note-id>

## Status
INDEX_ONLY / COMMON_FAMILY_CANDIDATE / EMBEDDED_FIELD_GROUP / TRANSITIONAL / DEPRECATED / NEEDS_VERIFICATION

## Compatibility path
<schemas/contracts/v1/common/uncertainty/... or N/A>

## Proposed canonical path
<schema path or NEEDS VERIFICATION>

## Paired contract
<contract path or N/A>

## Fixtures
<fixtures path or N/A>

## Validator
<tools/validators path or N/A>

## Vocabulary decision
<confidence / uncertainty / source reliability / review state / other / NEEDS VERIFICATION>

## Notes
<short note grounded in repo evidence>

## Follow-up
<open items or none>
```

## Review checklist

- [ ] Canonical schema path is linked or marked NEEDS VERIFICATION.
- [ ] Vocabulary decision is recorded.
- [ ] Paired contract path is linked or marked NEEDS VERIFICATION.
- [ ] Schema registry entry is linked or marked NEEDS VERIFICATION.
- [ ] Valid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Invalid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Validator path is linked or marked NEEDS VERIFICATION.
- [ ] CI/schema-test support is linked or marked NEEDS VERIFICATION.
- [ ] No duplicate canonical schema definitions are placed under this path.
- [ ] Any migration or compatibility claim cites an ADR, migration note, or verified repo evidence.

## Naming guidance

Recommended note pattern:

```text
<YYYY-MM-DD>_<schema-shortname>_uncertainty-note.md
```

Examples:

```text
2026-07-03_confidence-band_uncertainty-note.md
2026-07-03_source-reliability_uncertainty-note.md
2026-07-03_inference-quality_uncertainty-note.md
```

Use lowercase filenames and hyphenated schema short names.

## Open verification

- [ ] Confirm CODEOWNERS for `schemas/contracts/v1/common/uncertainty/`.
- [ ] Confirm whether uncertainty is a common schema family or an embedded field group.
- [ ] Confirm canonical schema home.
- [ ] Confirm paired contract paths.
- [ ] Confirm schema registry records.
- [ ] Confirm valid fixture paths.
- [ ] Confirm invalid fixture paths.
- [ ] Confirm validator paths.
- [ ] Confirm CI schema-test coverage.
- [ ] Confirm whether `schemas/README.md` should index this common lane.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | Canonical-home decision, new uncertainty schema, common schema migration, validator update, fixture update, schema registry update, ADR update, or compatibility-lane decision |
