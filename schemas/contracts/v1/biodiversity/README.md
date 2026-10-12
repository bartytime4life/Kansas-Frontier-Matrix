# `schemas/contracts/v1/biodiversity/` — Biodiversity Schema Compatibility Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-biodiversity-readme
title: schemas/contracts/v1/biodiversity/ — Biodiversity Schema Compatibility Index
version: v1
status: draft
policy_label: public
owners:
  - <schema-steward>
  - <biodiversity-steward>
  - <flora-steward>
  - <fauna-steward>
  - <habitat-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, schemas, contracts, v1, biodiversity, flora, fauna, habitat, compatibility, geoprivacy, json-schema]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![lane](https://img.shields.io/badge/lane-biodiversity-green)
![posture](https://img.shields.io/badge/posture-compatibility--index-orange)
![canonical](https://img.shields.io/badge/canonical-NEEDS%20VERIFICATION-yellow)
![sensitivity](https://img.shields.io/badge/sensitivity-geoprivacy--required-red)

## Purpose

`schemas/contracts/v1/biodiversity/` is a draft compatibility and index lane for Biodiversity schema notes.

It should help maintainers decide whether biodiversity is an accepted schema family, a cross-domain composition layer over Flora/Fauna/Habitat, or a compatibility alias that should point to owning domain schema lanes.

This README is documentation only. It is not a schema file, not contract prose, not policy, not validator code, not runtime code, not lifecycle data, and not a release record.

## Status & authority

| Field | Value |
|---|---|
| Document type | Biodiversity schema compatibility README |
| Owning root | `schemas/` |
| Requested path | `schemas/contracts/v1/biodiversity/` |
| Status | Draft |
| Authority level | Compatibility/index guidance. Canonical schemas, contracts, policy records, schema registry records, validators, fixtures, tests, ADRs, and steward decisions outrank this README. |
| Path posture | Current-session evidence confirms this README was blank before this update. |
| Canonical schema home | NEEDS VERIFICATION. Current-session search found `contracts/biodiversity/` as a compatibility/cross-domain contract lane, not a confirmed canonical biodiversity schema family. |
| Default posture | Do not create new canonical Biodiversity schema definitions directly under `schemas/contracts/v1/biodiversity/` unless an ADR or migration note explicitly confirms this schema family. |
| Sensitivity posture | Geoprivacy required where biodiversity records involve rare species, sensitive occurrence records, habitat joins, or protected locations. |
| Required reviewers | Schema steward, biodiversity steward, flora steward, fauna steward, habitat steward, sensitivity steward when applicable, and docs steward. |

## Placement basis

Current-session evidence confirms `schemas/README.md` defines `schemas/` as the root for machine-checkable shape and says schemas pair one-to-one with `contracts/`.

Current-session evidence confirms ADR-0001 says the default schema home is `schemas/contracts/v1/<family>/...`, and domain-specific schemas nest under `schemas/contracts/v1/domains/<domain>/...`.

Current-session search did not confirm a canonical `schemas/contracts/v1/biodiversity/README.md` schema family beyond this blank file. Search did confirm biodiversity-adjacent contract, package, pipeline, habitat, flora, and fauna surfaces.

Current-session evidence also confirms `contracts/biodiversity/` is a compatibility folder for cross-domain biodiversity semantic-contract documentation and does not create a sovereign biodiversity domain, schema home, policy home, data lifecycle root, or publication authority.

## Repo fit

```text
schemas/
├── README.md
└── contracts/
    └── v1/
        ├── biodiversity/               # you are here; compatibility/index lane
        └── domains/
            ├── fauna/                  # possible atomic-domain schema lane
            ├── flora/                  # possible atomic-domain schema lane
            └── habitat/                # possible atomic-domain schema lane

contracts/
└── biodiversity/                       # observed compatibility contract lane
```

## Current-session related evidence

| Evidence | Status |
|---|---|
| `schemas/contracts/v1/biodiversity/README.md` | Blank before this update. |
| `schemas/README.md` | Confirms `schemas/` owns machine-checkable shape and pairs with `contracts/`. |
| ADR-0001 | Confirms `schemas/contracts/v1/` as the proposed canonical schema home and says domain schemas nest under `schemas/contracts/v1/domains/<domain>/...`. |
| Search for Biodiversity schema family | Did not confirm a canonical biodiversity schema family in this edit. |
| `contracts/biodiversity/README.md` | Confirms biodiversity is currently treated as a compatibility/cross-domain semantic-contract folder and not a sovereign domain root. |
| Related domain lanes | Search surfaced Flora, Fauna, and Habitat materials as likely owning contexts for atomic biodiversity facts. |

This README does not verify schema contents, registry entries, fixture coverage, validator wiring, CI behavior, geoprivacy implementation, or whether `schemas/contracts/v1/biodiversity/` should remain as a compatibility path.

## Compatibility-lane responsibilities

| Responsibility | Expectation |
|---|---|
| Canonical-home decision | Determine whether biodiversity schemas belong here or under owning domain schema lanes such as Flora, Fauna, and Habitat. |
| Drift prevention | Prevent duplicate canonical schemas under `schemas/contracts/v1/biodiversity/`. |
| Cross-domain coordination | Point to owning domain schemas when biodiversity products compose domain-owned facts. |
| Migration notes | Record migration notes if compatibility files need to move. |
| Contract linkage | Point to paired biodiversity, flora, fauna, or habitat contract files when verified. |
| Fixture linkage | Point to valid, invalid, and public-safe fixtures when verified. |
| Validator linkage | Point to validators or CI checks when verified. |
| Registry linkage | Point to schema registry records when verified. |
| Sensitivity posture | Keep sensitive occurrence or location detail out of this lane and point to governed policy/review paths instead. |
| Review status | Mark unverified implementation claims as NEEDS VERIFICATION. |

## What belongs here

- This compatibility README.
- Short index notes that point to canonical Biodiversity, Flora, Fauna, or Habitat schema files once confirmed.
- Migration notes for moving Biodiversity schemas into the accepted schema-home path.
- Drift notes about duplicate or stale Biodiversity schema paths.
- Links to canonical schemas, contracts, fixtures, validators, registry records, tests, and policy/review surfaces.
- Notes that preserve cross-domain schema placement boundaries without exposing protected details.

## What does not belong here

- New canonical Biodiversity schema definitions.
- Duplicate copies of canonical schema files.
- Contract prose.
- Policy rules.
- Validator implementation code.
- Runtime code.
- Lifecycle data payloads.
- EvidenceBundle contents or source records.
- Release records.
- Rare-species exact locations or protected ecological details.
- Claims that this path is canonical without ADR, registry, or steward confirmation.

## Compatibility status values

Use finite compatibility status values where possible:

| Status | Meaning |
|---|---|
| `INDEX_ONLY` | This path only indexes candidate canonical schema locations. |
| `ALIAS_CANDIDATE` | This path may be an alias for Flora, Fauna, Habitat, or another accepted schema family. |
| `TRANSITIONAL` | Content is awaiting migration to canonical schema home. |
| `DEPRECATED` | Content should no longer receive new files. |
| `MIGRATE_TO_DOMAIN_LANE` | Content should move under an owning domain schema lane if confirmed. |
| `HELD_FOR_REVIEW` | Content needs schema, domain, geoprivacy, or sensitivity review before use. |
| `NEEDS_VERIFICATION` | Path, pairing, fixture, validator, registry, or CI support has not been verified. |

## Minimal compatibility note

```markdown
# <biodiversity-schema-compatibility-note-id>

## Status
INDEX_ONLY / ALIAS_CANDIDATE / TRANSITIONAL / DEPRECATED / MIGRATE_TO_DOMAIN_LANE / HELD_FOR_REVIEW / NEEDS_VERIFICATION

## Compatibility path
<schemas/contracts/v1/biodiversity/... or N/A>

## Proposed canonical path
<schemas/contracts/v1/domains/fauna/... / schemas/contracts/v1/domains/flora/... / schemas/contracts/v1/domains/habitat/... / NEEDS VERIFICATION>

## Paired contract
<contracts/biodiversity/... / contracts/domains/fauna/... / contracts/domains/flora/... / contracts/domains/habitat/... / N/A>

## Fixtures
<fixtures/... or N/A>

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
- [ ] Owning domain lane is explicit or marked NEEDS VERIFICATION.
- [ ] Paired contract path is linked or marked NEEDS VERIFICATION.
- [ ] Schema registry entry is linked or marked NEEDS VERIFICATION.
- [ ] Valid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Invalid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Public-safe fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Validator path is linked or marked NEEDS VERIFICATION.
- [ ] CI/schema-test support is linked or marked NEEDS VERIFICATION.
- [ ] Geoprivacy or sensitivity posture is explicit.
- [ ] No duplicate canonical schema definitions are placed under `schemas/contracts/v1/biodiversity/`.
- [ ] No sensitive occurrence or protected location details are stored here.
- [ ] Any migration or compatibility claim cites an ADR, migration note, or verified repo evidence.

## Naming guidance

Recommended compatibility-note pattern:

```text
<YYYY-MM-DD>_<schema-shortname>_compatibility-note.md
```

Examples:

```text
2026-07-03_biodiversity-index_compatibility-note.md
2026-07-03_species-richness-layer_compatibility-note.md
2026-07-03_public-safe-occurrence-summary_compatibility-note.md
```

Use lowercase filenames and hyphenated schema short names.

## Open verification

- [ ] Confirm CODEOWNERS for `schemas/contracts/v1/biodiversity/`.
- [ ] Confirm whether `schemas/contracts/v1/biodiversity/` should remain an index-only compatibility lane.
- [ ] Confirm whether biodiversity should be a schema family, cross-domain composition layer, or deprecated alias.
- [ ] Confirm canonical schema homes for biodiversity-shaped objects.
- [ ] Confirm paired Biodiversity, Flora, Fauna, and Habitat contract paths.
- [ ] Confirm Biodiversity schema registry records, if any.
- [ ] Confirm valid fixture paths.
- [ ] Confirm invalid fixture paths.
- [ ] Confirm public-safe fixture paths.
- [ ] Confirm validator paths.
- [ ] Confirm CI schema-test coverage.
- [ ] Confirm geoprivacy and sensitivity-review pointers for schema work.
- [ ] Confirm whether `schemas/README.md` should index this compatibility lane.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | Canonical-home decision, new Biodiversity schema, Flora/Fauna/Habitat schema migration, validator update, fixture update, schema registry update, ADR update, sensitivity-review update, or compatibility-lane decision |
