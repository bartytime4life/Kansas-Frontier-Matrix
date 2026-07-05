# `schemas/contracts/` — Versioned Contract Schema Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-readme
title: schemas/contracts/ — Versioned Contract Schema Index
type: readme; schema-parent-index; versioned-schema-root; contract-schema-boundary
authority_class: schema-parent-index
version: v0.1
status: draft; versioned-schema-parent; v1-present; mixed-maturity-child-root; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — empty README existed before v0.1 expansion
updated: 2026-07-04
policy_label: public; schemas; contracts; versioned-schemas; json-schema; no-parallel-authority
tags: [kfm, schemas, contracts, versioned-schemas, json-schema, v1, index, governance, validation]
related:
  - ../README.md
  - ./v1/README.md
  - ../../contracts/
  - ../../policy/
  - ../../fixtures/
  - ../../tests/
  - ../../tools/validators/
notes:
  - "Expanded from an empty file at schemas/contracts/README.md."
  - "schemas/README.md defines schemas as machine-checkable shape and says it pairs one-to-one with contracts/."
  - "schemas/contracts/v1/README.md is the current inspected v1 child index and records mixed maturity across many schema families."
  - "This README routes versioned schema roots; it does not duplicate every v1 family entry or prove child schemas complete."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2Fcontracts-blue)
![versioning](https://img.shields.io/badge/versioned-yes-informational)
![maturity](https://img.shields.io/badge/maturity-mixed-orange)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/` is the parent index for versioned, contract-backed JSON Schema families.
>
> **One-line boundary.** This folder routes machine-checkable schema versions. It does not own semantic contract prose, policy rules, data, fixtures, validator code, tests, release records, or proof that any child schema family is complete.

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes. It was empty before this expansion. | **CONFIRMED** |
| Is there an inspected versioned child root? | Yes. `schemas/contracts/v1/README.md` is the inspected v1 index. | **CONFIRMED** |
| Is v1 fully mature? | Not proven. The v1 index records mixed maturity, compatibility paths, scaffolds, and child families marked **PROPOSED** or **NEEDS VERIFICATION**. | **CONFIRMED mixed maturity** |
| Is this folder semantic contract authority? | No. Semantic meaning belongs under `contracts/`; this folder belongs under `schemas/`. | **CONFIRMED boundary** |
| Can this folder store data, policy, fixtures, validators, tests, or release records? | No. Those belong in their own responsibility roots. | **CONFIRMED boundary** |

---

## Authority

This folder sits beneath the schema responsibility root:

```text
schemas/contracts/
```

The repository-level `schemas/README.md` states that schemas provide machine-checkable shape for KFM object families and pair one-to-one with `contracts/`. It also says semantic prose belongs in `contracts/`, policy rules in `policy/`, and data/code outside `schemas/`.

This README is a version router. It does not outrank:

- actual schema files;
- `schemas/contracts/v1/README.md` and other future version indexes;
- paired semantic contracts under `contracts/`;
- accepted ADRs and Directory Rules;
- fixtures, validators, tests, and schema registry records;
- policy, evidence, review, release, correction, rollback, and publication records.

---

## Repo fit

```text
schemas/
├── README.md                                      # schema root doctrine and validation notes
└── contracts/
    ├── README.md                                  # this file; versioned schema parent
    └── v1/
        ├── README.md                              # v1 schema-family index
        ├── common/
        ├── source/
        ├── evidence/
        ├── runtime/
        ├── policy/
        ├── governance/
        ├── ui/
        ├── map/
        ├── layers/
        ├── domains/
        ├── joins/
        ├── relations/
        ├── receipts/
        ├── release/
        ├── review/
        └── ...

contracts/                                        # semantic meaning; not JSON Schema
policy/                                           # policy rules and posture; not schema root
fixtures/                                         # examples; not schema root
tests/                                            # test code and schema tests; not schema root
tools/validators/                                # validator code; not schema root
data/                                             # lifecycle records and emitted artifacts; not schema root
release/                                          # release/correction/rollback authority; not schema root
```

---

## Version routing

| Version root | Current posture | Notes |
|---|---|---|
| `v1/` | **CONFIRMED present / mixed maturity** | Current inspected version root. Contains child family indexes, concrete schemas, scaffolds, compatibility lanes, and README-only guardrails. |
| Future version roots | **PROPOSED / not confirmed** | Add only with ADR or migration note covering compatibility, `$id` namespace, fixtures, validators, tests, and downstream consumers. |

---

## What belongs here

- This README.
- Version root folders such as `v1/` when accepted.
- Version-level README indexes.
- Version migration notes.
- Cross-version compatibility notes.
- Links to schema registry records, validators, fixtures, tests, paired contracts, ADRs, and release/migration references.

---

## What does not belong here

- Semantic contract prose beyond README boundary notes.
- Policy rules or policy decisions.
- Source registry records, EvidenceBundles, emitted receipts, proof records, catalog records, lifecycle data, release records, correction records, rollback records, published artifacts, dashboards, screenshots, generated summaries, or runtime records.
- Validator implementation code, packages, pipelines, UI/API implementation, MapLibre code, map tiles, fixture payloads, or test code.
- Claims that a schema family is canonical, complete, policy-safe, release-approved, or public-ready merely because it lives under a versioned schema folder.

---

## Versioning rules

| Rule | Requirement |
|---|---|
| Version roots are governance surfaces | Adding `v2/` or another version requires migration reasoning, not just copying `v1/`. |
| Shape pairs with meaning | Every accepted schema needs paired semantic contract or approved profile. |
| `$id` stays stable | Version changes must preserve or explicitly migrate `$id` and `$ref` targets. |
| Fixtures prove examples | Valid and invalid fixtures should be versioned or explicitly compatibility-tested. |
| Validators follow versions | Validator paths and CI checks must know which version they enforce. |
| No parallel authority | Equivalent schemas must not drift across versions, flat paths, domain lanes, and compatibility lanes without migration notes. |

---

## Validation

```bash
# Inventory version roots and files.
find schemas/contracts -maxdepth 3 -type f | sort

# Inventory all schema JSON files under versioned contract schemas.
find schemas/contracts -name '*.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

# Compare schema files, README indexes, and placeholder JSON files.
find schemas/contracts -maxdepth 5 -type f \
  | awk '/\.schema\.json$/ {print "schema", $0; next} /README\.md$/ {print "readme", $0; next} /\.json$/ {print "json", $0}' \
  | sort

# Run project validators when available.
python tools/validate_all.py || true
pytest tests/schemas tests/contract || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed for the affected schema version.

---

## Promotion checklist

A new or materially changed version root should not advance beyond `PROPOSED` unless:

- [ ] Version scope is documented.
- [ ] Migration path from prior version is documented.
- [ ] `$id` and `$ref` strategy is settled.
- [ ] Paired semantic contracts or profiles are linked.
- [ ] Valid fixtures exist.
- [ ] Invalid fixtures exist.
- [ ] Validators and CI coverage are version-aware.
- [ ] Compatibility or breaking-change notes exist.
- [ ] Downstream consumers are identified.
- [ ] Rollback path is documented.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/README.md`.

Rollback for version-root changes must also check:

1. `$id` and `$ref` targets.
2. Paired contracts.
3. Fixtures and validators.
4. CI paths.
5. Registry, evidence, policy, review, release, correction, and rollback references.
6. API/UI/runtime/map consumers where applicable.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Should version indexes be generated from a manifest rather than hand-maintained? | **PROPOSED** | Schema steward + Docs steward |
| What is the canonical `$id` namespace convention across versions? | **NEEDS VERIFICATION** | Schema steward + ADR steward |
| Which v1 families are ready to become active rather than PROPOSED? | **NEEDS VERIFICATION** | Schema steward + Validation steward |
| What criteria would justify creating `v2/`? | **NEEDS VERIFICATION** | Schema steward + Contract steward |

---

## Maintainer notes

- Keep this README focused on version routing and root boundaries.
- Put per-family details in the version child README, currently `schemas/contracts/v1/README.md`.
- Keep data, policy, release, runtime, validator code, fixtures, and public artifacts outside `schemas/contracts/`.
