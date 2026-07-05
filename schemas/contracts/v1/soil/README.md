# `schemas/contracts/v1/soil/` — Soil Schema Compatibility Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-soil-readme
title: schemas/contracts/v1/soil/ — Soil Schema Compatibility Index
type: readme; compatibility-index; schema-boundary; soil-path-guardrail
authority_class: schema-family-guardrail
version: v0.1
status: draft; flat-soil-compatibility-path; canonical-domain-lane-present; no-current-flat-schema-files-found; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Soil domain steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — empty README existed before v0.1 expansion
updated: 2026-07-04
policy_label: public; schemas; contracts-v1; soil; compatibility-path; evidence-bound; policy-aware; release-gated; no-parallel-authority
tags: [kfm, schemas, contracts, v1, soil, compatibility, canonical-domain-lane, ssurgo, gssurgo, soil-map-unit, soil-moisture, no-parallel-authority]
related:
  - ../README.md
  - ../domains/soil/README.md
  - ../evidence/README.md
  - ../policy/README.md
  - ../review/README.md
  - ../release/README.md
  - ../../../../contracts/domains/soil/README.md
  - ../../../../docs/domains/soil/README.md
  - ../../../../docs/domains/soil/CANONICAL_PATHS.md
  - ../../../../fixtures/domains/soil/
  - ../../../../tests/domains/soil/
notes:
  - "Expanded from an empty file at schemas/contracts/v1/soil/README.md."
  - "Current GitHub search did not surface schema files directly under schemas/contracts/v1/soil/ beyond this README."
  - "The populated Soil schema lane inspected in this edit is schemas/contracts/v1/domains/soil/."
  - "The domains/soil README identifies that lane as the draft Soil domain schema lane and machine-checkable JSON Schema home for Soil object shapes."
  - "This flat soil path is a compatibility guardrail only and must not become parallel canonical schema authority without ADR or migration review."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![domain](https://img.shields.io/badge/domain-soil-8B4513)
![posture](https://img.shields.io/badge/posture-compatibility-orange)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/v1/soil/` is a flat compatibility index for Soil schema placement.
>
> **One-line boundary.** This path defines schema-placement guidance only. It does not replace `schemas/contracts/v1/domains/soil/`, store data, publish artifacts, or prove Soil claims.

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes. It was empty before this expansion. | **CONFIRMED** |
| Are schema files present directly under this flat path? | Not found in the current GitHub search beyond this README. | **NEEDS VERIFICATION / search-limited** |
| Is there a populated Soil domain schema lane? | Yes. `schemas/contracts/v1/domains/soil/README.md` is the inspected Soil domain schema index. | **CONFIRMED path evidence** |
| Is the domain lane production-ready? | Not proven. The inspected README says its schema maturity remains **NEEDS VERIFICATION** and opened examples are field-empty PROPOSED scaffolds. | **CONFIRMED scaffold / NEEDS VERIFICATION** |
| Can this flat folder store lifecycle data, emitted records, proofs, catalog records, release records, public API behavior, or map artifacts? | No. This is a schema compatibility folder and may only define machine-checkable shape if accepted here. | **CONFIRMED boundary** |

---

## Authority and placement

Current placement posture:

```text
schemas/contracts/v1/soil/                  # this flat compatibility guardrail
schemas/contracts/v1/domains/soil/          # inspected Soil domain schema lane
contracts/domains/soil/                     # semantic meaning; not JSON Schema
docs/domains/soil/                          # domain doctrine and architecture
fixtures/domains/soil/                      # examples and validator inputs where present
tests/domains/soil/                         # validation and behavior tests where present
```

This README does not amend ADR-0001, Directory Rules, schema-home decisions, Soil domain ownership, policy, validators, or release gates.

---

## Repo fit

```text
schemas/
└── contracts/
    └── v1/
        ├── soil/
        │   └── README.md                         # this file; flat compatibility guardrail
        └── domains/
            └── soil/
                ├── README.md                     # populated Soil schema lane
                └── *.schema.json                 # Soil machine shapes where present

contracts/
└── domains/
    └── soil/                                     # semantic meaning

docs/
└── domains/
    └── soil/                                     # domain docs

fixtures/
tests/
policy/
release/
data/
```

---

## Current inventory

| Path | Current posture | Notes |
|---|---|---|
| `schemas/contracts/v1/soil/README.md` | **CONFIRMED present** | Empty file expanded by this README. |
| `schemas/contracts/v1/soil/*.schema.json` | **Not found in current search** | Do not create here without placement review. |
| `schemas/contracts/v1/domains/soil/README.md` | **CONFIRMED populated domain schema index** | Identifies `domains/soil/` as the draft Soil domain schema lane. |
| `schemas/contracts/v1/domains/soil/*.schema.json` | **CONFIRMED path presence from inspected README inventory** | Path presence does not prove field completeness, fixture coverage, validator wiring, CI coverage, or release readiness. |

---

## What belongs here

- This README.
- Compatibility notes for the flat Soil path.
- Migration notes if this path is retained, retired, or made a profile lane.
- Pointers to the domain Soil schema lane and paired contract/docs/test/fixture surfaces.
- Future schema files only after accepted ADR or migration review.

---

## What does not belong here

- New canonical Soil schema families while `domains/soil/` remains the active domain schema lane.
- Semantic contract prose beyond README boundary notes.
- Lifecycle data, source records, emitted receipts, proof outputs, catalog records, release records, correction records, rollback records, policy decisions, EvidenceBundles, public artifacts, dashboards, screenshots, or generated summaries.
- Soil survey payloads, gridded derivatives, station readings, pedon/profile payloads, source payloads, or domain data.
- Validator code, packages, pipelines, runtime code, UI/API implementation, map tiles, or public display behavior.
- Claims that a Soil object is true, reviewed, policy-safe, release-approved, or public-ready merely because it validates against a schema in this folder.

---

## Compatibility rules

| Rule | Requirement |
|---|---|
| Keep domain lane visible | Prefer `schemas/contracts/v1/domains/soil/` unless an ADR or migration note changes placement. |
| Shape is not truth | Schema validation constrains object shape; it does not prove Soil claims. |
| Roots remain separate | Schemas, contracts, policy, evidence, review, release, data, fixtures, tests, and pipelines keep separate authority. |
| No parallel authority | Equivalent Soil shapes must not drift across flat, domain, source, receipt, proof, release, and policy lanes without migration notes. |

---

## Promotion checklist

This flat Soil path should not advance beyond compatibility posture unless:

- [ ] Placement is resolved.
- [ ] Relationship to `schemas/contracts/v1/domains/soil/` is documented.
- [ ] Paired semantic contracts exist or approved profiles are documented.
- [ ] Required fields are defined for any schema added here.
- [ ] Valid and invalid fixtures exist.
- [ ] Validators and CI coverage exist.
- [ ] Migration notes exist for overlapping surfaces.

---

## Validation

```bash
find schemas/contracts/v1/soil -maxdepth 4 -type f | sort

find schemas/contracts/v1/domains/soil -maxdepth 4 -type f | sort

find schemas/contracts/v1/soil -name '*.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

python tools/validate_all.py || true
pytest tests/schemas tests/contract tests/domains/soil || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/soil/README.md`.

Future schema rollback must restore `$id`, `$ref`, contracts, fixtures, validators, registry records, CI paths, and downstream consumers.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Should this flat path remain empty, become a redirect/index, host shared profiles, or be retired? | **NEEDS VERIFICATION / ADR-sensitive** | Soil steward + Schema steward |
| Should canonical Soil schemas live only under `schemas/contracts/v1/domains/soil/`? | **NEEDS VERIFICATION** | Soil steward + Schema steward |
| Which flat-path references, if any, need migration notes? | **NEEDS VERIFICATION** | Docs steward + Directory steward |

---

## Maintainer notes

- Keep this folder in compatibility posture until schema-home placement is resolved.
- Do not add canonical schemas here while `domains/soil/` remains the active Soil schema lane unless ADR or migration notes explicitly allow it.
- Keep emitted records and release records outside `schemas/`.
