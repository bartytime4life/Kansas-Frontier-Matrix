# `schemas/contracts/v1/sources/` — Sources Schema Compatibility Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-sources-readme
title: schemas/contracts/v1/sources/ — Sources Schema Compatibility Index
type: readme; schema-family-index; compatibility-index; source-schema-boundary
authority_class: schema-family-guardrail
version: v0.1
status: draft; plural-sources-compatibility-path; source-descriptor-scaffold-present; singular-source-lane-overlap; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Source steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Registry steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — empty README existed before v0.1 expansion
updated: 2026-07-04
policy_label: public; schemas; contracts-v1; sources; source-descriptor; compatibility-path; no-parallel-authority
tags: [kfm, schemas, contracts, v1, sources, source, SourceDescriptor, compatibility, registry, no-parallel-authority]
related:
  - ../README.md
  - ./source_descriptor.schema.json
  - ../source/README.md
  - ../source/source_descriptor.schema.json
  - ../source/source-descriptor.schema.json
  - ../../../../contracts/source/
  - ../../../../data/registry/sources/
  - ../../../../fixtures/
  - ../../../../tests/
notes:
  - "Expanded from an empty file at schemas/contracts/v1/sources/README.md."
  - "Current GitHub search surfaced source_descriptor.schema.json directly under this plural sources/ path."
  - "The inspected plural source_descriptor.schema.json is a PROPOSED empty scaffold with empty properties, additionalProperties true, and contract_doc null."
  - "The singular schemas/contracts/v1/source/README.md documents a broader source family with mixed maturity and drift risks."
  - "This plural path is a compatibility index only until source/ versus sources/ placement is resolved."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-sources-purple)
![posture](https://img.shields.io/badge/posture-compatibility-orange)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/v1/sources/` is a plural-path compatibility index for source-related schema placement.
>
> **One-line boundary.** This path defines schema shape only if accepted. It does not replace `schemas/contracts/v1/source/`, store registry records, store emitted records, or resolve source placement by itself.

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes. It was empty before this expansion. | **CONFIRMED** |
| Are schema files present directly under this plural path? | Yes. Current search surfaced `source_descriptor.schema.json`. | **CONFIRMED path presence** |
| Is the plural-path schema field-complete? | Not proven. The inspected schema is a PROPOSED empty scaffold with empty `properties`, `additionalProperties: true`, and `contract_doc: null`. | **CONFIRMED scaffold / NEEDS VERIFICATION** |
| Is there a related singular source lane? | Yes. `schemas/contracts/v1/source/README.md` documents the singular source lane with mixed maturity and drift risks. | **CONFIRMED** |
| Is source/sources placement resolved? | No. The singular README records source-vs-sources placement as a migration-sensitive open question. | **NEEDS VERIFICATION** |
| Can this folder store registry records or emitted records? | No. This folder is under `schemas/` and may only define machine-checkable shape. | **CONFIRMED boundary** |

---

## Authority and placement

This folder is under the schema responsibility root:

```text
schemas/contracts/v1/sources/
```

Current placement posture:

```text
schemas/contracts/v1/sources/                 # this plural compatibility lane
schemas/contracts/v1/sources/source_descriptor.schema.json
schemas/contracts/v1/source/                  # singular source schema-family lane
schemas/contracts/v1/source/source_descriptor.schema.json
schemas/contracts/v1/source/source-descriptor.schema.json
```

Adjacent authority remains separate:

- `contracts/source/` owns semantic meaning.
- `data/registry/sources/` owns source registry records where accepted.
- `fixtures/` and `tests/` prove examples and behavior where present.
- `tools/validators/` owns validator implementation where present.
- `data/` and `release/` own emitted lifecycle and release records where present.

This README does not amend ADR-0001, Directory Rules, schema-home decisions, source registry governance, validators, or release gates.

---

## Repo fit

```text
schemas/
└── contracts/
    └── v1/
        ├── sources/
        │   ├── README.md
        │   └── source_descriptor.schema.json      # PROPOSED empty scaffold
        └── source/
            ├── README.md                         # broader source-family index
            ├── source_descriptor.schema.json      # detailed PROPOSED schema
            └── source-descriptor.schema.json      # empty PROPOSED scaffold

contracts/source/
data/registry/sources/
fixtures/
tests/
tools/validators/
```

---

## Current inventory

| File | Current posture | Shape maturity | Notes |
|---|---|---|---|
| `README.md` | **CONFIRMED present** | Compatibility index | Empty file expanded by this README. |
| `source_descriptor.schema.json` | **PROPOSED** | Empty scaffold | Draft 2020-12 object; `$id` is `kfm://schemas/contracts/v1/sources/source_descriptor.schema.json`; `properties` is empty; `additionalProperties: true`; `contract_doc: null`. |

---

## Drift risks

| Risk | Evidence signal | Required posture |
|---|---|---|
| Singular vs plural path | Both `schemas/contracts/v1/source/` and `schemas/contracts/v1/sources/` exist. | **Needs migration decision** |
| Scaffold vs detailed schema | Plural `sources/source_descriptor.schema.json` is empty, while singular `source/source_descriptor.schema.json` is detailed. | **Do not treat plural scaffold as authoritative replacement** |
| Descriptor aliases | The singular lane also has hyphen and underscore descriptor forms. | **Resolve filename convention before promotion** |
| Registry separation | Schema paths are not registry record homes. | **Keep roots separate** |

---

## What belongs here

- This README.
- Compatibility notes for the plural `sources/` path.
- Migration notes if this path is retained, retired, or made canonical.
- Future schema files only after accepted placement review.
- Links to paired source contracts, registry homes, fixtures, validators, and tests.

---

## What does not belong here

- Source registry records or descriptor instances.
- Lifecycle data, raw source payloads, catalog records, proof outputs, emitted records, release records, public artifacts, dashboards, screenshots, or generated summaries.
- Validator code, packages, pipelines, runtime code, UI/API implementation, or map artifacts.
- Claims that a source object is complete or ready for downstream use merely because it validates against a schema in this folder.

---

## Promotion checklist

This plural path should not advance beyond compatibility posture unless:

- [ ] Singular `source/` vs plural `sources/` placement is resolved.
- [ ] Descriptor filename convention is resolved.
- [ ] Paired semantic contract exists or approved profile is documented.
- [ ] `$id` namespace convention is settled.
- [ ] Required fields are defined and fixture-tested if schemas remain here.
- [ ] Registry storage path is documented separately from schema shape.
- [ ] Valid fixtures exist.
- [ ] Invalid fixtures exist.
- [ ] Validators exist and paths are correct.
- [ ] Migration notes exist for duplicate or overlapping schema surfaces.

---

## Validation

```bash
find schemas/contracts/v1/sources -maxdepth 3 -type f | sort

find schemas/contracts/v1/source schemas/contracts/v1/sources -maxdepth 3 -type f \
  | sort

find schemas/contracts/v1/sources -name '*.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

python tools/validate_all.py || true
pytest tests/schemas tests/contract || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/sources/README.md`.

Future schema rollback must restore `$id`, `$ref`, contracts, fixtures, validators, registry records, CI paths, and downstream consumers.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Should the canonical path be `source/` or `sources/`? | **NEEDS VERIFICATION / migration-sensitive** | Schema steward + Source steward |
| Should the plural scaffold be promoted, migrated, or retired? | **NEEDS VERIFICATION** | Source steward + Validation steward |
| Which fixtures prove descriptor behavior if this plural path remains? | **NEEDS VERIFICATION** | Validation steward |

---

## Maintainer notes

- Keep this folder in compatibility posture until source-path placement is resolved.
- Do not treat the plural empty scaffold as a replacement for the more detailed singular source descriptor schema.
- Keep registry records, emitted records, validators, and release records outside this folder.
