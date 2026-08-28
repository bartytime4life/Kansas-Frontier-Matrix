# `schemas/contracts/v1/crossings/` — Crossings Schema Compatibility Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-crossings-readme
title: schemas/contracts/v1/crossings/ — Crossings Schema Compatibility Index
version: v1
status: draft
policy_label: public
owners:
  - <schema-steward>
  - <roads-rail-trade-domain-steward>
  - <hydrology-domain-steward>
  - <settlements-infrastructure-steward>
  - <contract-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, schemas, contracts, v1, crossings, roads-rail-trade, transport, hydrology, compatibility, json-schema]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![lane](https://img.shields.io/badge/lane-crossings-blueviolet)
![posture](https://img.shields.io/badge/posture-compatibility--index-orange)
![canonical](https://img.shields.io/badge/canonical-NEEDS%20VERIFICATION-yellow)

## Purpose

`schemas/contracts/v1/crossings/` is a draft compatibility and index lane for crossing-related schema notes.

Current-session evidence points to `Crossing` as a Roads / Rail / Trade Routes object concept, with related bridge, ferry, river crossing, route event, status event, road segment, rail segment, and network-edge contract surfaces. This path should not become a parallel schema authority unless a steward decision, ADR, registry entry, or migration note confirms it as the accepted schema family.

This README is documentation only. It is not a schema file, contract prose, policy, validator code, runtime code, lifecycle data, graph output, release record, or publication authority.

## Status & authority

| Field | Value |
|---|---|
| Document type | Crossings schema compatibility README |
| Owning root | `schemas/` |
| Requested path | `schemas/contracts/v1/crossings/` |
| Status | Draft |
| Authority level | Compatibility/index guidance. Canonical schemas, paired contracts, schema registry records, validators, fixtures, tests, ADRs, domain stewards, and release records outrank this README. |
| Path posture | Current-session evidence confirms this README was blank before this update. |
| Canonical status | NEEDS VERIFICATION. This edit did not confirm a canonical `schemas/contracts/v1/crossings/` schema family. |
| Likely owning domain lane | Roads / Rail / Trade Routes, because current-session search and contract evidence found `contracts/domains/roads-rail-trade/crossing.md`. |
| Expected schema path from paired contract | `schemas/contracts/v1/domains/roads-rail-trade/crossing.schema.json`, but the paired contract says that schema was not found in its task. |
| Default posture | Do not create canonical crossing schema definitions directly under `schemas/contracts/v1/crossings/` until placement is confirmed. |
| Required reviewers | Schema steward, Roads / Rail / Trade Routes steward, Hydrology steward where water crossings are involved, Settlements/Infrastructure steward where infrastructure identity is involved, contract steward, and docs steward. |

## Placement basis

Current-session evidence confirms `schemas/README.md` defines `schemas/` as the root for machine-checkable shape and says schemas pair one-to-one with `contracts/`.

Current-session evidence confirms ADR-0001 says the default schema home is `schemas/contracts/v1/<family>/...`, and domain-specific schemas nest under `schemas/contracts/v1/domains/<domain>/...`.

Current-session search found Roads / Rail / Trade Routes contract surfaces for `bridge.md`, `crossing.md`, and `river_crossing.md`.

Current-session evidence from `contracts/domains/roads-rail-trade/crossing.md` identifies `Crossing` as a Roads / Rail / Trade Routes object term, references `schemas/contracts/v1/domains/roads-rail-trade/crossing.schema.json`, and states that the paired schema was not found in that task.

## Repo fit

```text
schemas/
├── README.md
└── contracts/
    └── v1/
        ├── crossings/                         # you are here; compatibility/index lane
        └── domains/
            └── roads-rail-trade/              # likely owning domain schema lane; NEEDS VERIFICATION
                └── crossing.schema.json       # referenced by contract; existence NEEDS VERIFICATION

contracts/
└── domains/
    └── roads-rail-trade/
        ├── crossing.md
        ├── bridge.md
        └── river_crossing.md
```

## Current-session related evidence

| Evidence | Status |
|---|---|
| `schemas/contracts/v1/crossings/README.md` | Blank before this update. |
| `schemas/README.md` | Confirms `schemas/` owns machine-checkable shape and pairs with `contracts/`. |
| ADR-0001 | Confirms `schemas/contracts/v1/` as the proposed canonical schema home and says domain schemas nest under `schemas/contracts/v1/domains/<domain>/...`. |
| Search for crossings | Found Roads / Rail / Trade Routes crossing, bridge, and river crossing contract surfaces. |
| `contracts/domains/roads-rail-trade/crossing.md` | Paired semantic contract for `Crossing`; marks schema posture as missing / NEEDS VERIFICATION. |

This README does not verify schema contents, schema registry entries, fixture coverage, validator wiring, CI behavior, public API behavior, map rendering, graph behavior, or whether `schemas/contracts/v1/crossings/` should remain as a compatibility path.

## Compatibility-lane responsibilities

| Responsibility | Expectation |
|---|---|
| Canonical-home decision | Determine whether crossing schemas belong here, under `schemas/contracts/v1/domains/roads-rail-trade/`, or under another accepted family. |
| Drift prevention | Prevent duplicate canonical crossing schemas under this compatibility path. |
| Domain ownership | Keep transport-side crossing semantics with Roads / Rail / Trade Routes unless an ADR or steward decision says otherwise. |
| Related-domain linkage | Link Hydrology or Settlements/Infrastructure schema lanes only where those domains own the relevant facts. |
| Contract linkage | Point to paired crossing, bridge, ferry, river crossing, event, or network contract files when verified. |
| Fixture linkage | Point to valid, invalid, and edge-case fixtures when verified. |
| Validator linkage | Point to validators or CI checks when verified. |
| Registry linkage | Point to schema registry records when verified. |
| Review status | Mark unverified implementation claims as NEEDS VERIFICATION. |

## What belongs here

- This compatibility README.
- Short index notes that point to accepted crossing schema files once confirmed.
- Migration notes for moving crossing schemas into the accepted schema-home path.
- Drift notes about duplicate or stale crossing schema paths.
- Links to canonical schemas, paired contracts, fixtures, validators, registry records, policy references, release references, and tests.
- Notes that preserve domain ownership and avoid turning crossing shape notes into graph truth, routing behavior, infrastructure identity, hydrology truth, or publication approval.

## What does not belong here

- New canonical crossing schema definitions before steward confirmation.
- Duplicate copies of canonical schema files.
- Contract prose.
- Policy rules.
- Validator implementation code.
- Runtime code.
- Lifecycle data payloads.
- EvidenceBundle contents or source records.
- Release records.
- Graph outputs or generated topology as source truth.
- Claims that this path is canonical without ADR, registry, migration note, or steward confirmation.

## Compatibility status values

Use finite compatibility status values where possible:

| Status | Meaning |
|---|---|
| `INDEX_ONLY` | This path only indexes candidate canonical schema locations. |
| `FAMILY_CANDIDATE` | Crossings may become an accepted schema family. |
| `DOMAIN_FAMILY_CANDIDATE` | Crossings may belong under a domain schema lane. |
| `TRANSITIONAL` | Content is awaiting migration to the accepted schema home. |
| `DEPRECATED` | Content should no longer receive new files. |
| `MIGRATE_TO_ROADS_RAIL_TRADE` | Content should move under the Roads / Rail / Trade Routes schema lane. |
| `HELD_FOR_REVIEW` | Content needs schema, domain, policy, or release review before use. |
| `NEEDS_VERIFICATION` | Path, pairing, fixture, validator, registry, or CI support has not been verified. |

## Minimal compatibility note

```markdown
# <crossings-schema-compatibility-note-id>

## Status
INDEX_ONLY / FAMILY_CANDIDATE / DOMAIN_FAMILY_CANDIDATE / TRANSITIONAL / DEPRECATED / MIGRATE_TO_ROADS_RAIL_TRADE / HELD_FOR_REVIEW / NEEDS_VERIFICATION

## Compatibility path
<schemas/contracts/v1/crossings/... or N/A>

## Proposed canonical path
<schemas/contracts/v1/domains/roads-rail-trade/... / schemas/contracts/v1/crossings/... / NEEDS VERIFICATION>

## Paired contract
<contract path or N/A>

## Related domain facts
<roads-rail-trade / hydrology / settlements-infrastructure / other / NEEDS VERIFICATION>

## Fixtures
<fixtures path or N/A>

## Validator
<tools/validators path or N/A>

## Policy references
<policy path or N/A>

## Release references
<release path or N/A>

## Notes
<short note grounded in repo evidence>

## Follow-up
<open items or none>
```

## Review checklist

- [ ] Canonical schema path is linked or marked NEEDS VERIFICATION.
- [ ] Owning domain lane is explicit or marked NEEDS VERIFICATION.
- [ ] Paired contract path is linked or marked NEEDS VERIFICATION.
- [ ] Related-domain boundaries are identified where material.
- [ ] Schema registry entry is linked or marked NEEDS VERIFICATION.
- [ ] Valid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Invalid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Validator path is linked or marked NEEDS VERIFICATION.
- [ ] CI/schema-test support is linked or marked NEEDS VERIFICATION.
- [ ] No duplicate canonical schema definitions are placed under this path.
- [ ] Any migration or compatibility claim cites an ADR, migration note, or verified repo evidence.

## Naming guidance

Recommended compatibility-note pattern:

```text
<YYYY-MM-DD>_<schema-shortname>_crossings-schema-note.md
```

Examples:

```text
2026-07-03_crossing_crossings-schema-note.md
2026-07-03_river-crossing_crossings-schema-note.md
2026-07-03_crossings-path-decision_crossings-schema-note.md
```

Use lowercase filenames and hyphenated schema short names.

## Open verification

- [ ] Confirm CODEOWNERS for `schemas/contracts/v1/crossings/`.
- [ ] Confirm whether crossings is an accepted schema family or compatibility alias.
- [ ] Confirm canonical crossing schema home.
- [ ] Confirm whether `schemas/contracts/v1/domains/roads-rail-trade/crossing.schema.json` exists or is planned.
- [ ] Confirm paired Roads / Rail / Trade Routes contract paths.
- [ ] Confirm related Hydrology and Settlements/Infrastructure boundaries.
- [ ] Confirm schema registry records.
- [ ] Confirm valid fixture paths.
- [ ] Confirm invalid fixture paths.
- [ ] Confirm validator paths.
- [ ] Confirm CI schema-test coverage.
- [ ] Confirm whether `schemas/README.md` should index this compatibility lane.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | Canonical-home decision, new crossing schema, migration note, validator update, fixture update, registry update, ADR update, Roads / Rail / Trade Routes contract update, or compatibility-lane decision |
