# `schemas/atmosphere/` — Atmosphere Schema Compatibility Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-atmosphere-readme
title: schemas/atmosphere/ — Atmosphere Schema Compatibility Index
version: v1
status: draft
policy_label: public
owners:
  - <schema-steward>
  - <atmosphere-domain-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, schemas, atmosphere, compatibility, schemas-contracts-v1, json-schema]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![domain](https://img.shields.io/badge/domain-atmosphere-blueviolet)
![posture](https://img.shields.io/badge/posture-compatibility--index-orange)
![canonical](https://img.shields.io/badge/canonical-schemas%2Fcontracts%2Fv1-green)

## Purpose

`schemas/atmosphere/` is a draft compatibility and index lane for Atmosphere schema notes.

It should point maintainers toward the canonical Atmosphere schema home under `schemas/contracts/v1/domains/atmosphere/` and prevent this shorter path from becoming a parallel schema authority.

This README is documentation only. It is not a schema, not a contract, not policy, not validation code, and not lifecycle data.

## Status & authority

| Field | Value |
|---|---|
| Document type | Atmosphere schema compatibility README |
| Owning root | `schemas/` |
| Requested path | `schemas/atmosphere/` |
| Status | Draft |
| Authority level | Compatibility/index guidance. Canonical schemas, contracts, schema registry records, validators, fixtures, tests, ADRs, and steward decisions outrank this README. |
| Path posture | Current-session evidence confirms this README was blank before this update. |
| Canonical schema home | `schemas/contracts/v1/domains/atmosphere/` |
| Default posture | Do not create new canonical Atmosphere schema definitions directly under `schemas/atmosphere/` unless an ADR or migration note explicitly changes the schema-home rule. |
| Required reviewers | Schema steward, Atmosphere domain steward, and docs steward. |

## Placement basis

Current-session evidence confirms `schemas/README.md` defines `schemas/` as the root for machine-checkable shape and says schemas pair one-to-one with `contracts/`.

Current-session evidence also confirms ADR-0001 says the default schema home is `schemas/contracts/v1/<family>/...`, and domain-specific schemas nest under `schemas/contracts/v1/domains/<domain>/...`.

Current-session evidence confirms the Atmosphere canonical schema lane exists at `schemas/contracts/v1/domains/atmosphere/`.

## Repo fit

```text
schemas/
├── README.md
├── atmosphere/                       # you are here; compatibility/index lane
└── contracts/
    └── v1/
        └── domains/
            └── atmosphere/           # canonical Atmosphere schema lane
```

## Observed canonical Atmosphere schema lane

Current-session search found the following Atmosphere schema-family files under the canonical lane:

| Path | Status |
|---|---|
| `schemas/contracts/v1/domains/atmosphere/README.md` | Existing canonical-lane README. |
| `schemas/contracts/v1/domains/atmosphere/atmosphere_air_decision_envelope.schema.json` | Existing schema file. |
| `schemas/contracts/v1/domains/atmosphere/evidence_drawer_payload.schema.json` | Existing schema file. |
| `schemas/contracts/v1/domains/atmosphere/layer_manifest.schema.json` | Existing schema file. |
| `schemas/contracts/v1/domains/atmosphere/domain_observation.schema.json` | Existing schema file. |
| `schemas/contracts/v1/domains/atmosphere/run_receipt.schema.json` | Existing schema file. |

This README does not verify those schema contents or validator wiring. It only records current-session path evidence.

## Compatibility-lane responsibilities

| Responsibility | Expectation |
|---|---|
| Canonical pointer | Point to `schemas/contracts/v1/domains/atmosphere/`. |
| Drift prevention | Prevent duplicate canonical schemas under `schemas/atmosphere/`. |
| Migration notes | Record migration notes if legacy or compatibility files need to move. |
| Registry linkage | Point to schema registry records when verified. |
| Contract linkage | Point to paired `contracts/` files when verified. |
| Fixture linkage | Point to valid and invalid fixtures when verified. |
| Validator linkage | Point to validators or CI checks when verified. |
| Review status | Mark unverified implementation claims as NEEDS VERIFICATION. |

## What belongs here

- This compatibility README.
- Short index notes that point to canonical Atmosphere schema files.
- Migration notes for moving legacy Atmosphere schemas into `schemas/contracts/v1/domains/atmosphere/`.
- Drift notes about duplicate or stale Atmosphere schema paths.
- Links to canonical schemas, contracts, fixtures, validators, registry records, and tests.

## What does not belong here

- New canonical Atmosphere schema definitions.
- Duplicate copies of canonical schema files.
- Contract prose.
- Policy rules.
- Validator implementation code.
- Runtime code.
- Lifecycle data payloads.
- EvidenceBundle contents or source records.
- Release records.

## Compatibility status values

Use finite compatibility status values where possible:

| Status | Meaning |
|---|---|
| `INDEX_ONLY` | This path only indexes canonical schema locations. |
| `MIRROR` | Content is mirrored from canonical schema home and should not be edited directly. |
| `TRANSITIONAL` | Content is awaiting migration to canonical schema home. |
| `DEPRECATED` | Content should no longer receive new files. |
| `MIGRATE` | Content should move to `schemas/contracts/v1/domains/atmosphere/`. |
| `NEEDS_VERIFICATION` | Path, pairing, fixture, validator, or CI support has not been verified. |

## Minimal compatibility note

```markdown
# <atmosphere-schema-compatibility-note-id>

## Status
INDEX_ONLY / MIRROR / TRANSITIONAL / DEPRECATED / MIGRATE / NEEDS_VERIFICATION

## Compatibility path
<schemas/atmosphere/... or N/A>

## Canonical path
<schemas/contracts/v1/domains/atmosphere/... or N/A>

## Paired contract
<contracts/... or N/A>

## Fixtures
<fixtures/... or N/A>

## Validator
<tools/validators/... or N/A>

## Notes
<short note grounded in repo evidence>

## Follow-up
<open items or none>
```

## Review checklist

- [ ] Canonical schema path is linked.
- [ ] Paired contract path is linked or marked NEEDS VERIFICATION.
- [ ] Schema registry entry is linked or marked NEEDS VERIFICATION.
- [ ] Valid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Invalid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Validator path is linked or marked NEEDS VERIFICATION.
- [ ] CI/schema-test support is linked or marked NEEDS VERIFICATION.
- [ ] No duplicate canonical schema definitions are placed under `schemas/atmosphere/`.
- [ ] Any migration or compatibility claim cites an ADR, migration note, or verified repo evidence.

## Naming guidance

Recommended compatibility-note pattern:

```text
<YYYY-MM-DD>_<schema-shortname>_compatibility-note.md
```

Examples:

```text
2026-07-03_domain-observation_compatibility-note.md
2026-07-03_layer-manifest_compatibility-note.md
2026-07-03_run-receipt_compatibility-note.md
```

Use lowercase filenames and hyphenated schema short names.

## Open verification

- [ ] Confirm CODEOWNERS for `schemas/atmosphere/`.
- [ ] Confirm whether `schemas/atmosphere/` should remain an index-only compatibility lane.
- [ ] Confirm whether any existing or planned files should migrate into `schemas/contracts/v1/domains/atmosphere/`.
- [ ] Confirm paired contract paths for each Atmosphere schema.
- [ ] Confirm schema registry records.
- [ ] Confirm valid fixture paths.
- [ ] Confirm invalid fixture paths.
- [ ] Confirm validator paths.
- [ ] Confirm CI schema-test coverage.
- [ ] Confirm whether `schemas/README.md` should index `atmosphere/` directly as a compatibility lane.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | New Atmosphere schema, schema-home migration, validator update, fixture update, schema registry update, ADR update, or compatibility-lane decision |
