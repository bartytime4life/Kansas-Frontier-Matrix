# `schemas/contracts/v1/domains/agriculture/hydrology-ext/` — Agriculture Hydrology Extension Schema Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-domains-agriculture-hydrology-ext-readme
title: schemas/contracts/v1/domains/agriculture/hydrology-ext/ — Agriculture Hydrology Extension Schema Index
version: v1
status: draft
policy_label: public
owners:
  - <schema-steward>
  - <agriculture-domain-steward>
  - <hydrology-domain-steward>
  - <contract-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, schemas, contracts, v1, domains, agriculture, hydrology-ext, extension, json-schema]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![domain](https://img.shields.io/badge/domain-agriculture-green)
![extension](https://img.shields.io/badge/extension-hydrology--ext-blueviolet)
![posture](https://img.shields.io/badge/posture-extension--index-orange)
![canonical](https://img.shields.io/badge/canonical-NEEDS%20VERIFICATION-yellow)

## Purpose

`schemas/contracts/v1/domains/agriculture/hydrology-ext/` is a draft Agriculture-owned schema extension lane for agriculture objects that need bounded Hydrology references.

This path should describe Agriculture-side extension shapes only. It must not replace Hydrology-owned schemas, Hydrology source-role rules, Hydrology evidence posture, Hydrology policy, or Hydrology release decisions.

This README is documentation only. It is not a schema file, contract prose, policy, validator code, lifecycle data, registry data, proof output, or release authority.

## Status & authority

| Field | Value |
|---|---|
| Document type | Agriculture Hydrology extension schema README |
| Owning root | `schemas/` |
| Requested path | `schemas/contracts/v1/domains/agriculture/hydrology-ext/` |
| Status | Draft |
| Authority level | Extension/index guidance. Canonical schemas, paired contracts, registry records, validators, fixtures, tests, ADRs, domain stewards, and release records outrank this README. |
| Path posture | Current-session evidence confirms this README was blank before this update. |
| Agriculture schema lane | `schemas/contracts/v1/domains/agriculture/` exists as a PROPOSED domain schema lane. |
| Hydrology schema lane | Hydrology contracts reference `schemas/contracts/v1/domains/hydrology/` as the Hydrology machine-shape lane; concrete Hydrology schema coverage remains NEEDS VERIFICATION in this edit. |
| Extension posture | Agriculture-owned extension lane; not a Hydrology schema home and not a cross-domain root. |
| Default posture | Do not add canonical extension schema files here until paired contracts, fixtures, validator behavior, registry records, and steward review are confirmed. |
| Required reviewers | Schema steward, Agriculture steward, Hydrology steward, contract steward, validation steward where applicable, and docs steward. |

## Placement basis

Current-session evidence confirms `schemas/README.md` defines `schemas/` as the root for machine-checkable shape and says schemas pair one-to-one with `contracts/`.

Current-session evidence confirms ADR-0001 says domain-specific schemas nest under `schemas/contracts/v1/domains/<domain>/...`, while `contracts/` retains object meaning and `schemas/` owns machine-checkable shape.

Current-session evidence confirms `schemas/contracts/v1/domains/agriculture/README.md` exists as a PROPOSED Agriculture domain schema lane.

Current-session evidence confirms `schemas/contracts/v1/agriculture/README.md` is a shorter Agriculture compatibility index and points to `schemas/contracts/v1/domains/agriculture/` as the likely canonical domain lane.

Current-session evidence from Agriculture canonical paths identifies `schemas/contracts/v1/domains/agriculture/` as the Agriculture machine-shape location while noting Agriculture-specific paths are PROPOSED until verified.

Current-session evidence from Hydrology contracts identifies `schemas/contracts/v1/domains/hydrology/` as the Hydrology machine-shape lane. This extension path must reference Hydrology-owned shape, not duplicate it.

## Repo fit

```text
schemas/
├── README.md
└── contracts/
    └── v1/
        ├── agriculture/                         # shorter compatibility index
        └── domains/
            ├── agriculture/
            │   ├── README.md                    # Agriculture domain schema lane
            │   └── hydrology-ext/               # you are here; Agriculture-owned extension index
            └── hydrology/                       # Hydrology-owned schema lane; separate authority

contracts/
└── domains/
    ├── agriculture/
    └── hydrology/
```

## Current-session related evidence

| Evidence | Status |
|---|---|
| `schemas/contracts/v1/domains/agriculture/hydrology-ext/README.md` | Blank before this update. |
| `schemas/README.md` | Confirms `schemas/` owns machine-checkable shape and pairs with `contracts/`. |
| ADR-0001 | Confirms domain schemas nest under `schemas/contracts/v1/domains/<domain>/...`. |
| `schemas/contracts/v1/domains/agriculture/README.md` | Existing Agriculture domain schema lane; status PROPOSED. |
| `schemas/contracts/v1/agriculture/README.md` | Existing shorter Agriculture compatibility index. |
| `docs/domains/agriculture/CANONICAL_PATHS.md` | Agriculture path doctrine; lists Agriculture schema lane as PROPOSED and path-only. |
| `contracts/domains/hydrology/README.md` | Hydrology contract root; identifies Hydrology machine-shape lane and source-role boundaries. |

This README does not verify extension schema files, schema registry entries, fixture coverage, validator wiring, CI behavior, policy behavior, release integration, or runtime behavior.

## Extension-lane responsibilities

| Responsibility | Expectation |
|---|---|
| Agriculture ownership | Keep the extension Agriculture-owned and scoped to Agriculture object shapes. |
| Hydrology reference discipline | Reference Hydrology-owned identifiers, observations, or context without redefining Hydrology semantics. |
| Contract pairing | Link each extension schema to paired Agriculture or cross-domain contract text when verified. |
| Drift prevention | Prevent duplicate Hydrology schemas from being placed under Agriculture. |
| Fixture linkage | Point to valid and invalid fixtures when verified. |
| Validator linkage | Point to validators or CI checks when verified. |
| Registry linkage | Point to schema registry records when verified. |
| Review status | Mark unverified implementation claims as NEEDS VERIFICATION. |

## What belongs here

- This README.
- Agriculture-owned extension schema files once placement is confirmed.
- Short schema-family index notes.
- Migration notes for agriculture-hydrology extension placement.
- Drift notes about duplicate or stale extension schema paths.
- Links to paired contracts, fixtures, validators, schema registry records, policy references, release references, and tests.
- Notes that preserve Agriculture ownership and Hydrology reference boundaries.

## What does not belong here

- Hydrology-owned canonical schemas.
- Duplicate copies of Hydrology schemas.
- Agriculture schemas that do not need Hydrology references.
- Cross-domain schemas that belong under a cross-domain lane.
- Contract prose.
- Policy rules.
- Validator implementation code.
- Runtime code.
- Lifecycle data payloads.
- Registry records.
- Proof outputs.
- Release records.
- Claims that this extension is complete without fixtures, validators, registry records, and review support.

## Extension status values

Use finite status values where possible:

| Status | Meaning |
|---|---|
| `INDEX_ONLY` | This path only indexes candidate extension schema locations. |
| `EXTENSION_CANDIDATE` | The extension may become an accepted Agriculture schema subfamily. |
| `DRAFT_SCHEMA` | Extension schema exists but still needs review and test support. |
| `ACTIVE_EXTENSION` | Extension schema has accepted pairing, fixtures, validator support, registry record, and review status. |
| `MIGRATE_TO_AGRICULTURE_ROOT` | Content belongs directly under the Agriculture schema lane. |
| `MIGRATE_TO_HYDROLOGY` | Content belongs under the Hydrology schema lane. |
| `MIGRATE_TO_CROSS` | Content belongs under a cross-domain schema lane. |
| `DEPRECATED` | Content should no longer receive new consumers. |
| `NEEDS_VERIFICATION` | Pairing, fixture, validator, registry, or CI support has not been verified. |

## Minimal extension note

```markdown
# <agriculture-hydrology-extension-note-id>

## Status
INDEX_ONLY / EXTENSION_CANDIDATE / DRAFT_SCHEMA / ACTIVE_EXTENSION / MIGRATE_TO_AGRICULTURE_ROOT / MIGRATE_TO_HYDROLOGY / MIGRATE_TO_CROSS / DEPRECATED / NEEDS_VERIFICATION

## Extension path
<schemas/contracts/v1/domains/agriculture/hydrology-ext/... or N/A>

## Proposed canonical path
<schemas/contracts/v1/domains/agriculture/hydrology-ext/... / schemas/contracts/v1/domains/agriculture/... / schemas/contracts/v1/domains/hydrology/... / schemas/contracts/v1/cross/... / NEEDS VERIFICATION>

## Paired contract
<contract path or N/A>

## Agriculture-owned fields
<field list or NEEDS VERIFICATION>

## Hydrology references
<reference list or N/A>

## Fixtures
<fixtures path or N/A>

## Validator
<tools/validators path or N/A>

## Notes
<short note grounded in repo evidence>

## Follow-up
<open items or none>
```

## Review checklist

- [ ] Canonical extension schema path is linked or marked NEEDS VERIFICATION.
- [ ] Agriculture-owned fields are identified.
- [ ] Hydrology references are links or references, not copied Hydrology schema definitions.
- [ ] Paired contract path is linked or marked NEEDS VERIFICATION.
- [ ] Schema registry entry is linked or marked NEEDS VERIFICATION.
- [ ] Valid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Invalid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Validator path is linked or marked NEEDS VERIFICATION.
- [ ] CI/schema-test support is linked or marked NEEDS VERIFICATION.
- [ ] No duplicate Hydrology canonical schemas are placed under this path.
- [ ] Any migration or compatibility claim cites an ADR, migration note, or verified repo evidence.

## Open verification

- [ ] Confirm CODEOWNERS for `schemas/contracts/v1/domains/agriculture/hydrology-ext/`.
- [ ] Confirm whether `hydrology-ext/` is an accepted Agriculture schema subfamily.
- [ ] Confirm whether any files here should instead live under `schemas/contracts/v1/cross/`.
- [ ] Confirm paired Agriculture contract paths.
- [ ] Confirm paired Hydrology reference paths.
- [ ] Confirm schema registry records.
- [ ] Confirm valid fixture paths.
- [ ] Confirm invalid fixture paths.
- [ ] Confirm validator paths.
- [ ] Confirm CI schema-test coverage.
- [ ] Confirm whether `schemas/contracts/v1/domains/agriculture/README.md` should index this extension lane.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | Extension-home decision, new agriculture hydrology extension schema, migration note, validator update, fixture update, schema registry update, ADR update, Agriculture contract update, Hydrology contract update, or compatibility-lane decision |
