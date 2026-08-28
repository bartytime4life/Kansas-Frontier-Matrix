# `schemas/contracts/v1/` — Contract Schema v1 Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-readme
title: schemas/contracts/v1/ — Contract Schema v1 Index
type: readme; schema-root-index; contract-schema-boundary; governance-index
authority_class: schema-root-index
version: v0.2
status: draft; mixed-maturity-schema-root; child-family-indexes-present; scaffold-and-compatibility-lanes-present; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Domain stewards
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — short status stub existed before v0.2 expansion
updated: 2026-07-04
policy_label: public; schemas; contracts-v1; json-schema; schema-index; no-parallel-authority
tags: [kfm, schemas, contracts, v1, json-schema, index, governance, validation, compatibility, no-parallel-authority]
related:
  - ../../README.md
  - ../README.md
  - ./common/README.md
  - ./source/README.md
  - ./sources/README.md
  - ./evidence/README.md
  - ./runtime/README.md
  - ./policy/README.md
  - ./governance/README.md
  - ./exposure/README.md
  - ./ui/README.md
  - ./map/README.md
  - ./layers/README.md
  - ./domains/README.md
  - ./joins/README.md
  - ./relations/README.md
  - ./receipts/README.md
  - ./release/README.md
  - ./review/README.md
  - ./transport/README.md
  - ./trade-routes/README.md
  - ./spatial-foundation/README.md
  - ./stac/README.md
  - ./smoke/README.md
notes:
  - "Expanded from a short parent status stub that listed only common, source, evidence, runtime, policy, and governance as real-shape families and still treated ui/* as a remaining stub."
  - "Current GitHub search/fetch evidence shows this parent root is now a mixed-maturity schema index with many child README guardrails, compatibility paths, scaffolds, and some more detailed schema families."
  - "This README is a routing and boundary document; it does not prove field completeness, validator wiring, fixture coverage, CI coverage, release readiness, or canonical status of every child schema."
  - "When child README evidence conflicts with this parent snapshot, the child README, schema file, paired contract, ADR, validator, fixture, and steward decision should be checked before acting."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![version](https://img.shields.io/badge/contracts-v1-informational)
![maturity](https://img.shields.io/badge/maturity-mixed-orange)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/v1/` is the v1 machine-checkable schema index for KFM contract-backed object families.
>
> **One-line boundary.** This root owns JSON Schema shape. It does not own semantic prose, policy rules, lifecycle data, emitted records, fixtures, validator code, runtime code, public UI behavior, catalog records, release decisions, or proof that a child family is complete.

---

## Quick jumps

[Authority](#authority) · [Status snapshot](#status-snapshot) · [Repo fit](#repo-fit) · [Family routing](#family-routing) · [Compatibility and drift watch](#compatibility-and-drift-watch) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Validation](#validation) · [Promotion checklist](#promotion-checklist) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Authority

`schemas/contracts/v1/` is part of the `schemas/` responsibility root. The repository-level `schemas/README.md` defines `schemas/` as the machine-checkable shape root and says it pairs one-to-one with `contracts/`.

This parent README does not outrank:

- actual schema files;
- paired semantic contracts under `contracts/`;
- accepted ADRs and Directory Rules;
- child family README files;
- fixtures, validators, tests, and schema registry records;
- policy, evidence, review, release, correction, rollback, and publication records.

Use this file as a router and status snapshot, not as proof that a schema family is canonical, complete, validated, or released.

---

## Status snapshot

| Question | Answer | Truth label |
|---|---|---|
| Does this parent README path exist? | Yes. It was a short status stub before this expansion. | **CONFIRMED** |
| Is `schemas/contracts/v1/` a single-maturity root? | No. Child lanes include detailed schemas, empty scaffolds, compatibility indexes, domain lanes, join/relation lanes, and README-only guardrails. | **CONFIRMED mixed maturity** |
| Are all child schema families complete? | No. Many child READMEs and schema files mark status as **PROPOSED** or **NEEDS VERIFICATION**. | **CONFIRMED posture** |
| Is `ui/*` still only a remaining stub? | No. `ui/README.md` now documents nine direct UI schema files with mixed maturity. | **CONFIRMED update** |
| Are domain schema homes fully resolved? | No. Several child lanes record flat-path vs domain-path or slug conflicts. | **NEEDS VERIFICATION / ADR-sensitive** |
| Can this root store data, policy, runtime code, validator code, fixtures, release records, or public artifacts? | No. This root is for machine-checkable schema shape and schema-family documentation only. | **CONFIRMED boundary** |

---

## Repo fit

```text
schemas/
├── README.md                                      # schema root doctrine and validation notes
└── contracts/
    └── v1/
        ├── README.md                              # this file; v1 parent index
        ├── common/                                # shared schema families
        ├── source/                                # source-family schema lane
        ├── sources/                               # plural source compatibility lane
        ├── evidence/                              # evidence-support schemas
        ├── runtime/                               # runtime-support schemas
        ├── policy/                                # policy-support schemas
        ├── governance/                            # governance-support schemas
        ├── exposure/                              # exposure-shape guardrail
        ├── ui/                                    # governed UI schema family
        ├── map/                                   # map-facing schema family
        ├── layers/                                # layer schema family
        ├── domains/                               # domain-specific schema homes
        ├── joins/                                 # join schema lanes
        ├── relations/                             # relation schema lanes
        ├── receipts/                              # receipt schema lanes
        ├── release/                               # release-support schema lanes
        ├── review/                                # review-support schema lanes
        ├── transport/                             # flat compatibility lane
        ├── trade-routes/                          # flat compatibility guardrail
        ├── spatial-foundation/                    # README-only spatial guardrail
        ├── stac/                                  # STAC profile schema lane
        └── smoke/                                 # smoke/validation placeholder guardrail

contracts/                                        # semantic meaning; not JSON Schema
policy/                                           # policy rules and posture; not schema root
fixtures/                                         # examples; not schema root
tests/                                            # test code and schema tests; not schema root
tools/validators/                                # validator code; not schema root
data/                                             # lifecycle records and emitted artifacts; not schema root
release/                                          # release/correction/rollback authority; not schema root
```

---

## Family routing

| Family / lane | Current posture | Notes |
|---|---|---|
| `common/` | Draft shared-schema index | Shared reusable shapes; should not become a catch-all for domain-specific schemas. |
| `source/` | Mixed maturity source-family index | Contains detailed and scaffold source-related schema surfaces; tracks source/sources and filename drift. |
| `sources/` | Compatibility index | Plural path with `source_descriptor.schema.json` scaffold; do not treat as replacement for `source/` without migration review. |
| `evidence/` | Schema family index | Evidence-support shapes; EvidenceBundle/EvidenceRef still outrank generated language. |
| `runtime/` | Mixed maturity runtime-family index | Runtime schemas define shape only; they do not execute runtime behavior or approve AI output. |
| `policy/` | Policy-support schema family | Machine shapes only; policy decisions and rules live outside this folder. |
| `governance/` | Governance-support schema family | Machine shapes only; governance decisions and steward review remain outside schema shape. |
| `exposure/` | README-only or sparse guardrail | Exposure is policy-significant; schema-valid exposure payloads are not permission to expose. |
| `ui/` | Mixed maturity UI schema family | Contains nine direct UI schema files; UI schema validation does not render UI or approve public display. |
| `map/` | Map-facing schema family | Contains map manifests/scaffolds; not MapLibre runtime, tile storage, or release authority. |
| `layers/` | Layer schema family | Contains layer schema scaffolds and overlaps with domain layer profiles. |
| `domains/` | Domain schema parent | Domain-specific homes; many child lanes are PROPOSED and need fixture/validator review. |
| `joins/` | Join schema parent | Join lanes should not replace canonical domain truth. |
| `relations/` | Relation schema parent | Relation lanes should not replace evidence or source-bound domain claims. |
| `receipts/` | Receipt schema parent | Receipt shapes are not emitted receipt records. |
| `release/` | Release-support schema parent | Release schemas are not release decisions. |
| `review/` | Review-support schema parent | Review schemas are not steward decisions. |
| `transport/` | Flat compatibility index | Contains `roads_rail_decision_envelope.schema.json` scaffold; overlaps Roads/Rail/Trade domain lane. |
| `trade-routes/` | Flat compatibility guardrail | Points back to `domains/roads-rail-trade/`; no direct schema files found in current search. |
| `spatial-foundation/` | README-only guardrail | No direct schema files found in current search; placement remains **NEEDS VERIFICATION**. |
| `stac/` | Minimal STAC schema placeholder | Contains `kfm-profile-v1.schema.json` scaffold; catalog records live under `data/catalog/stac/`. |
| `smoke/` | Minimal validation placeholder | README-only placeholder unless future placement review accepts schemas there. |

---

## Compatibility and drift watch

| Drift area | Current signal | Required posture |
|---|---|---|
| Flat lanes vs domain lanes | `transport/`, `trade-routes/`, `soil/`, `settlement/`, `settlements-infrastructure/`, and similar flat paths can overlap `domains/<domain>/`. | Keep as compatibility indexes unless ADR/migration says otherwise. |
| `source/` vs `sources/` | Both paths exist and contain descriptor-related surfaces. | Resolve singular/plural path before promotion. |
| Hyphen vs underscore filenames | Several families contain hyphen/underscore variants. | Pick canonical names or document aliases before promotion. |
| Map vs layers | `map/` and `layers/` both include layer-related surfaces. | Use profile/ADR strategy to prevent parallel authority. |
| UI vs runtime/exposure/map | UI schemas overlap evidence drawer, focus/runtime, and map context shapes. | Resolve placement before treating UI schemas as public surfaces. |
| Empty scaffolds | Many schema files are `PROPOSED` with empty `properties` or `additionalProperties: true`. | Do not imply validator-ready schema maturity. |
| Namespace drift | `$id` values use mixed `kfm://...` and `https://schemas.kfm.local/...` forms. | Resolve namespace convention before promotion. |

---

## What belongs here

- This parent README.
- Child schema-family folders and README indexes.
- JSON Schema draft 2020-12 files.
- Schema-family migration notes.
- Schema placement, drift, and compatibility notes.
- Links to paired semantic contracts, fixtures, validators, policy references, evidence references, release references, correction references, rollback references, and tests.

---

## What does not belong here

- Semantic contract prose beyond README boundary notes.
- Policy rules or policy decisions.
- Source registry records, EvidenceBundles, emitted receipts, proof records, catalog records, lifecycle data, release records, correction records, rollback records, published artifacts, dashboards, screenshots, generated summaries, or runtime records.
- Validator implementation code, packages, pipelines, UI/API implementation, MapLibre code, map tiles, fixture payloads, or test code.
- Claims that an object is true, reviewed, policy-safe, release-approved, public-ready, or complete merely because it validates against a schema.

---

## Validation

Recommended local validation sequence:

```bash
# Inventory v1 schema files and README indexes.
find schemas/contracts/v1 -maxdepth 4 -type f | sort

# Separate schema files from README and placeholder JSON files.
find schemas/contracts/v1 -maxdepth 5 -type f \
  | awk '/\.schema\.json$/ {print "schema", $0; next} /README\.md$/ {print "readme", $0; next} /\.json$/ {print "json", $0}' \
  | sort

# Validate JSON syntax for schema-family JSON files.
find schemas/contracts/v1 -name '*.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

# Run project validators when available.
python tools/validate_all.py || true
pytest tests/schemas tests/contract || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed for the affected family.

---

## Promotion checklist

A child schema family should not advance beyond `PROPOSED` unless:

- [ ] The owning root and path are resolved.
- [ ] Flat-path vs domain-path conflicts are documented or migrated.
- [ ] Paired semantic contract or approved profile exists.
- [ ] `$id` namespace convention is settled.
- [ ] Required fields are defined.
- [ ] Valid fixtures exist.
- [ ] Invalid fixtures exist.
- [ ] Validators exist and paths are correct.
- [ ] CI/schema-test coverage exists.
- [ ] Policy, evidence, review, release, correction, and rollback references are included where material.
- [ ] Migration notes exist for duplicate or overlapping schema surfaces.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/README.md`.

Rollback for schema-family changes must also check:

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
| Which child schema families are field-complete enough to be called active rather than PROPOSED? | **NEEDS VERIFICATION** | Schema steward + Validation steward |
| Which flat compatibility lanes should be retired, redirected, or promoted? | **NEEDS VERIFICATION / ADR-sensitive** | Schema steward + Directory steward |
| What is the canonical `$id` namespace convention for v1 schemas? | **NEEDS VERIFICATION** | Schema steward + ADR steward |
| Which child families have verified valid/invalid fixtures and CI coverage? | **NEEDS VERIFICATION** | Validation steward |
| Which parent index entries should be generated from a manifest rather than hand-maintained? | **PROPOSED** | Schema steward + Docs steward |

---

## Maintainer notes

- Keep this parent index conservative; child READMEs and schema files carry the most specific evidence.
- Do not convert compatibility lanes into canonical schema homes without ADR or migration notes.
- Keep data, policy, release, runtime, validator code, fixtures, and public artifacts outside `schemas/`.
