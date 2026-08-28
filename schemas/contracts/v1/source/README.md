# `schemas/contracts/v1/source/` — Source Schema Family Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-source-readme
title: schemas/contracts/v1/source/ — Source Schema Family Index
type: readme; schema-family-index; source-schema-boundary
authority_class: schema-family-index
version: v0.2
status: draft; source-family-present; mixed-maturity-files-present; descriptor-path-drift-present; placeholder-files-present; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Source steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Registry steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — short stub existed before v0.2 expansion
updated: 2026-07-04
policy_label: public; schemas; contracts-v1; source; source-descriptor; registry-aware; no-parallel-authority
tags: [kfm, schemas, contracts, v1, source, SourceDescriptor, source-registry, descriptor, ingest-receipt, doctrine-artifact, no-parallel-authority]
related:
  - ../README.md
  - ./source_descriptor.schema.json
  - ./source-descriptor.schema.json
  - ./source_descriptor.json
  - ./source-descriptor.json
  - ./source-intake-record.json
  - ./source-activation-decision.json
  - ./ingest_receipt.schema.json
  - ./run_receipt.schema.json
  - ./drift-summary.json
  - ./doctrine_artifact_descriptor.schema.json
  - ./doctrine_artifact_preflight_summary.schema.json
  - ../../../../contracts/source/
  - ../../../../data/registry/sources/
  - ../../../../fixtures/
  - ../../../../tests/
  - ../../../../tools/validators/
notes:
  - "Expanded from a short stub at schemas/contracts/v1/source/README.md."
  - "Current GitHub search surfaced concrete schemas, empty scaffolds, and non-.schema.json placeholder files under this folder."
  - "source_descriptor.schema.json is the most complete inspected SourceDescriptor schema, but its metadata points to a plural sources/ canonical path while this file lives under singular source/."
  - "source-descriptor.schema.json is a separate PROPOSED empty scaffold, creating hyphen/underscore descriptor drift."
  - "This folder defines source object shapes only; registry records and emitted records live outside this folder."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-source-purple)
![maturity](https://img.shields.io/badge/maturity-mixed-orange)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/v1/source/` is the machine-checkable schema family for source-related object shapes.
>
> **One-line boundary.** Source schemas define object shape only. They do not store source registry records, emitted records, lifecycle data, validator code, or release records.

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes: `schemas/contracts/v1/source/README.md`. It was a short stub before this expansion. | **CONFIRMED** |
| Are source-family files present in this folder? | Yes. Search surfaced descriptor files, receipt files, doctrine-artifact files, and placeholder JSON files. | **CONFIRMED path presence** |
| Are all files mature schemas? | No. The folder mixes detailed schemas, empty scaffolds, and non-`.schema.json` placeholder JSON files. | **CONFIRMED mixed maturity** |
| Is SourceDescriptor naming settled? | Not fully. Hyphenated and underscored descriptor files both exist, and detailed metadata points to a plural `sources/` path while the inspected file lives under singular `source/`. | **NEEDS VERIFICATION / migration-sensitive** |
| Can this folder store registry records or emitted records? | No. This folder is under `schemas/` and may only define machine-checkable shape. | **CONFIRMED boundary** |

---

## Authority and placement

This folder is under the schema responsibility root:

```text
schemas/contracts/v1/source/
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
        └── source/
            ├── README.md
            ├── source_descriptor.schema.json       # detailed PROPOSED schema; underscore form
            ├── source-descriptor.schema.json       # empty PROPOSED scaffold; hyphen form
            ├── source_descriptor.json              # non-.schema JSON; needs inspection
            ├── source-descriptor.json              # non-.schema JSON; needs inspection
            ├── source-intake-record.json           # placeholder JSON
            ├── source-activation-decision.json     # placeholder JSON
            ├── drift-summary.json                  # placeholder JSON
            ├── ingest_receipt.schema.json          # concrete PROPOSED schema
            ├── run_receipt.schema.json             # empty PROPOSED scaffold
            ├── doctrine_artifact_descriptor.schema.json
            └── doctrine_artifact_preflight_summary.schema.json

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
| `source_descriptor.schema.json` | **PROPOSED** | Detailed schema | Rich SourceDescriptor schema with required fields and x-kfm links to contract, fixtures, validator, policy, and registry home; metadata also names a plural `sources/` canonical path. |
| `source-descriptor.schema.json` | **PROPOSED** | Empty scaffold | Empty `properties`, `additionalProperties: true`, `contract_doc: null`. |
| `source_descriptor.json` | **NEEDS VERIFICATION** | Non-`.schema.json` file | Present by search; not inspected in this pass. |
| `source-descriptor.json` | **NEEDS VERIFICATION** | Non-`.schema.json` file | Present by search; not inspected in this pass. |
| `ingest_receipt.schema.json` | **PROPOSED** | Concrete schema | Requires id, source_id, run_id, start/end times, outcome, bytes_in, and digests; `additionalProperties: false`. |
| `run_receipt.schema.json` | **PROPOSED** | Empty scaffold | Empty `properties`, `additionalProperties: true`, `contract_doc: null`. |
| `source-intake-record.json` | **PROPOSED placeholder** | Non-schema placeholder | Placeholder with status, path, source_docs, and notes. |
| `source-activation-decision.json` | **PROPOSED placeholder** | Non-schema placeholder | Placeholder with status, path, source_docs, and notes. |
| `drift-summary.json` | **PROPOSED placeholder** | Non-schema placeholder | Placeholder with status, path, source_docs, and notes. |
| `doctrine_artifact_descriptor.schema.json` | **PROPOSED** | Concrete schema | Requires doc_id, filename, sha256, provenance, authority_status, admitted_at, and steward_signoff_ref. |
| `doctrine_artifact_preflight_summary.schema.json` | **PROPOSED** | Concrete schema | Detailed preflight/check summary schema with required return codes and presence input. |

---

## Drift risks

| Risk | Evidence signal | Required posture |
|---|---|---|
| Singular vs plural path | Detailed descriptor metadata points to `schemas/contracts/v1/sources/source_descriptor.schema.json`, while the inspected file is under `source/`. | **Needs migration decision** |
| Hyphen vs underscore descriptor | Both `source_descriptor.schema.json` and `source-descriptor.schema.json` exist with different maturity. | **Pick canonical filename before promotion** |
| Schema vs placeholder JSON | Several files are JSON placeholders, not `.schema.json` schemas. | **Do not treat placeholders as validators** |
| Registry separation | Source schemas may reference registry homes, but registry records live outside `schemas/`. | **Keep roots separate** |

---

## What belongs here

- This README.
- JSON Schema files for source-family object shapes when accepted.
- Source-family index notes and drift notes.
- Migration notes for singular/plural and hyphen/underscore naming.
- Links to paired source contracts, registry homes, fixtures, validators, and tests.

---

## What does not belong here

- Source registry records or descriptor instances.
- Lifecycle data, raw source payloads, catalog records, proof outputs, emitted records, release records, public artifacts, dashboards, screenshots, or generated summaries.
- Validator code, packages, pipelines, runtime code, UI/API implementation, or map artifacts.
- Claims that a source object is complete or ready for downstream use merely because it validates against a schema.

---

## Promotion checklist

A source schema should not advance beyond `PROPOSED` unless:

- [ ] Singular `source/` vs plural `sources/` placement is resolved.
- [ ] Hyphen vs underscore descriptor naming is resolved.
- [ ] Paired semantic contract exists or approved profile is documented.
- [ ] `$id` namespace convention is settled.
- [ ] Required fields are defined and fixture-tested.
- [ ] Placeholder JSON files are converted, retired, or documented as non-schema records.
- [ ] Registry storage path is documented separately from schema shape.
- [ ] Valid fixtures exist.
- [ ] Invalid fixtures exist.
- [ ] Validators exist and paths are correct.
- [ ] CI/schema-test coverage exists.
- [ ] Migration notes exist for duplicate or overlapping schema surfaces.

---

## Validation

```bash
find schemas/contracts/v1/source -maxdepth 3 -type f | sort

find schemas/contracts/v1/source -maxdepth 3 -type f \
  | awk '/\.schema\.json$/ {print "schema", $0; next} /\.json$/ {print "json", $0}' \
  | sort

find schemas/contracts/v1/source -name '*.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

python tools/validate_all.py || true
pytest tests/schemas tests/contract || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/source/README.md`.

Future schema rollback must restore `$id`, `$ref`, contracts, fixtures, validators, registry records, CI paths, and downstream consumers.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Should the canonical path be `source/` or `sources/`? | **NEEDS VERIFICATION / migration-sensitive** | Schema steward + Source steward |
| Should SourceDescriptor use hyphenated or underscored filenames? | **NEEDS VERIFICATION / slug-sensitive** | Source steward + Contract steward |
| Which placeholder JSON files should become schemas, move elsewhere, or be retired? | **NEEDS VERIFICATION** | Source steward + Validation steward |
| Which fixtures prove descriptor and receipt behavior? | **NEEDS VERIFICATION** | Validation steward |

---

## Maintainer notes

- Keep this folder focused on source-family schema shape.
- Resolve path and filename drift before promoting SourceDescriptor or descriptor aliases.
- Keep registry records, emitted records, validators, and release records outside this folder.
