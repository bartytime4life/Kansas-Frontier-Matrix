<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/soil/time-caveat-profile
title: Soil Time-Caveat Fixture Profile
type: semantic-contract; domain-profile; temporal-anti-collapse
version: v0.1.0
status: proposed; inactive; fixture-first; no-network
owners: OWNER_TBD — Soil steward · Contract steward · Validation steward · Source steward
created: 2026-08-05
updated: 2026-08-05
policy_label: public; soil; temporal; stale-state; non-publisher
related:
  - ./soil_time_caveat.md
  - ../../../schemas/contracts/v1/domains/soil/time_caveat_profile.schema.json
  - ../../../schemas/contracts/v1/domains/soil/time_caveat_candidate.schema.json
  - ../../../pipeline_specs/soil/time_caveat_profile.v1.json
  - ../../../tools/validators/domains/soil/time_caveat/validate_time_caveat_profile.py
tags: [kfm, soil, time-caveat, stale-state, fixture-first, no-network]
[/KFM_META_BLOCK_V2] -->

# Soil time-caveat fixture profile

> This inactive profile is an executable adapter for the existing
> `SoilTimeCaveat` semantic contract. It checks whether synthetic Soil
> candidates preserve source, observation, valid, retrieval, evaluation, and
> timezone distinctions. It does not replace the canonical contract, activate
> a source, decide policy, authorize release, or publish Soil truth.

## Scope

The profile is deliberately narrow:

| Dimension | Bound value |
|---|---|
| Domain | `soil` |
| Source access | None; repository fixtures only |
| Profile state | `PROPOSED_INACTIVE` |
| Hashing | Canonical JSON without `spec_hash`, then SHA-256 |
| Outcomes | `PASS`, `HOLD`, `DENY`, `ERROR` |
| Lifecycle effect | None |

It covers seven support families already named by Soil doctrine: authoritative
static survey, gridded derivative, direct station observation, reference
station observation, satellite grid, pedon/profile evidence, and derived
interpretation.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Declared support, source role, claim role, and required time axes are internally consistent. |
| `HOLD` | Required temporal support is unavailable or an otherwise valid current-condition candidate is stale. |
| `DENY` | The candidate collapses support roles, contradicts stale state, claims governance authority, or contains impossible temporal ordering. |
| `ERROR` | Profile, schema, input, JSON parsing, or validation infrastructure cannot produce a trustworthy assessment. |

No outcome is evidence, policy, review, promotion, release, publication, or
public-use authority.

## Anti-collapse rules

The profile enforces these bounded distinctions:

1. Static survey support cannot claim a current station or generalized current
   condition and cannot present itself as an observed measurement.
2. Station claims require an observation time and preserved source timezone.
3. Satellite and derived grids cannot masquerade as station observations.
4. Modeled or derivative validity windows retain `valid_from` and `valid_to`.
5. Retrieval and evaluation time do not replace observation or source time.
6. A candidate older than the declared maximum age is held; declaring it
   `FRESH` despite that age is denied.
7. Future or reversed time order is denied rather than guessed.
8. The profile and every fixture keep source, policy, release, and public-use
   authority set to false.

## Determinism and replay

`pipeline_specs/soil/time_caveat_profile.v1.json` carries a `spec_hash`.
The validator recomputes the hash after removing that field. Profile mutation
therefore requires a new digest and replay rather than silent reinterpretation.

The same profile and candidate bytes produce the same outcome and sorted
finding codes. Diagnostics expose field paths and reason codes, not candidate
values.

## Directory Rules basis

- semantic adapter meaning: `contracts/domains/soil/`;
- machine shapes: `schemas/contracts/v1/domains/soil/`;
- inactive executable profile: `pipeline_specs/soil/`;
- synthetic examples: `fixtures/domains/soil/`;
- validator: `tools/validators/domains/soil/time_caveat/`;
- enforceability proof: `tests/validators/domains/soil/time_caveat/`;
- orchestration: `.github/workflows/`;
- authoring accountability: `data/receipts/generated/`.

These are existing responsibility roots and domain lanes. The profile creates
no parallel authority home.

## Validation

```bash
python -m pytest \
  tests/validators/domains/soil/time_caveat/test_time_caveat_profile.py \
  -q --strict-config --strict-markers

python tools/validators/domains/soil/time_caveat/validate_time_caveat_profile.py \
  --fixtures
```

## Trust boundary and rollback

A green result proves only bounded fixture consistency. Evidence resolution,
rights, sensitivity, live-source admission, policy evaluation, review,
promotion, release, correction, rollback execution, API behavior, map
rendering, and AI answers remain separate.

Before merge, close the draft pull request. After an authorized merge, revert
the profile, schemas, fixtures, validator, tests, workflow, and generated
receipt together. No source or lifecycle record requires deletion.
