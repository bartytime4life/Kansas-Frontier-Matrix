<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/policy-match-scoring-people-readme
title: policy/match-scoring/people/ — Sensitive People-Scoring Hold Boundary
type: readme
version: v1.0.0
status: draft; sensitive-domain; routing-and-hold; implementation-empty; no-live-resolution; non-release; non-publication
owner: NEEDS VERIFICATION — People/DNA/Land and policy stewardship plus independent approval controls are not established
created: 2026-08-28
updated: 2026-08-28
current_path: policy/match-scoring/people/README.md
owning_root: policy/
policy_label: restricted-review; people; identity; scoring; hold; no-live-resolution; non-release; non-publication
responsibility: Prevent people-related scores from becoming identity, kinship, consent, rights, land, eligibility, release, or publication authority and route bounded synthetic historical-resolution evidence to its owning surfaces.
base_commit: f68fe0ff504562bb8d2b4aedacb3d46eb66f17f3
prior_blob: 8b137891791fe96927ad78e64b0aad7bded08bdc
truth_posture: CONFIRMED documentation-only leaf with no executable artifacts or direct consumers / CONFIRMED separate proposed fixture-only historical person-place-event resolution contract, schema, synthetic fixtures, validator, tests, and workflow / PROPOSED sensitive routing-and-hold boundary / UNKNOWN accepted people-scoring policy, live resolver, steward, evaluator, consumer, retention, appeal, release, or publication path
[/KFM_META_BLOCK_V2] -->

# Sensitive people-scoring hold boundary

`policy/match-scoring/people/` is a deny-by-default documentation boundary. It does not
authorize scoring a real person, resolve identity or kinship, infer consent, rank people,
determine eligibility, adjudicate land or title, or expose living-person or DNA/genomics
information.

> [!CAUTION]
> A high score is not a person, relationship, fact, right, reviewer decision, consent grant,
> or release approval. When the evidence cannot support a bounded claim, abstain and preserve
> the contradiction rather than forcing a match.

## Current repository evidence

At `main@f68fe0ff504562bb8d2b4aedacb3d46eb66f17f3`, this directory contains only this README
and `.gitkeep`. It has no Rego, schema, fixture, validator, test, workflow, bundle, evaluator,
decision receipt, or consumer.

The nearest executable evidence is a separate, proposed, fixture-only profile:

| Surface | Confirmed role | Does not establish |
|---|---|---|
| [Candidate contract](../../../contracts/domains/people-dna-land/historical_person_place_event_resolution.md) | Defines deterministic evidence signals, score recomputation, confidence bands, dispositions, and fail-closed scope for synthetic historical candidates | Identity, residence, migration, land ownership, patent validity, title, rights, policy, review, release, or publication |
| [JSON Schema](../../../schemas/contracts/v1/domains/people-dna-land/historical_person_place_event_resolution.schema.json) | Constrains the candidate record shape | Source truth, live identity resolution, consent, or release authority |
| [Synthetic fixtures](../../../fixtures/contracts/v1/domains/people-dna-land/historical_person_place_event_resolution/README.md) | Exercise positive, contradictory, weak, score-mismatch, living-person, private-parcel, and public-release cases | Real-person or real-parcel handling |
| [No-network validator](../../../tools/validators/validate_historical_person_place_event_resolution.py) and [tests](../../../tests/validators/test_validate_historical_person_place_event_resolution.py) | Recompute the bounded score and enforce exact fixture polarity | An accepted policy evaluator or authenticated decision |
| [Focused workflow](../../../.github/workflows/historical-person-place-event-resolution.yml) | Runs repository-owned synthetic fixtures and records bounded validation evidence | Deployment, production use, promotion, publication, or public-use authority |

The [People/DNA/Land identity model](../../../docs/domains/people-dna-land/IDENTITY_MODEL.md)
describes a proposed match-scoring stance and explicitly separates a scored candidate from a
steward-approved canonical identity and from public release. That reference is domain
documentation, not executable policy or implementation truth.

## Allowed use

This leaf may document:

- the hold separating a synthetic historical candidate score from identity and release;
- routing to the exact contract, schema, fixture, validator, test, workflow, consent,
  sensitivity, geoprivacy, evidence, review, correction, and release surfaces;
- requirements for an eventual, separately reviewed policy design.

It must not store real-person records, names, contact details, raw DNA or genomic material,
vendor kit identifiers, inferred kinship, private person-parcel joins, precise residence or
movement, applicant or eligibility records, reviewer notes, credentials, or live-source
payloads.

## Fail-closed rules

Hold or deny any proposal that:

1. includes or attempts to resolve a living person;
2. treats DNA/genomics similarity, shared segments, surnames, household co-occurrence,
   authority identifiers, or map proximity as identity or kinship truth;
3. treats a person-place score as residence, migration, ownership, title, legal status,
   entitlement, eligibility, risk, worth, or trustworthiness;
4. exposes a private parcel, precise sensitive location, raw source payload, or public-release
   flag;
5. drops negative evidence, contradiction, missingness, uncertainty, provenance, temporal
   scope, or source-role limits;
6. substitutes automation for steward review, separation of duties, consent, rights review,
   or appeal and correction;
7. lacks a bounded purpose, reversible output, retention rule, invalidation path, and rollback
   target;
8. attempts publication from a contract, fixture, validator result, workflow, map, AI output,
   commit, merge, or pull request.

The existing synthetic profile also denies living-person, raw-DNA, precise-location,
private-parcel, and public-release claims. This README does not broaden that profile.

## Inputs and outputs

This documentation lane accepts only repository references and proposed policy questions.
It emits no score, match, canonical identity, relationship, policy decision, EvidenceBundle,
ReviewRecord, ReleaseManifest, correction, or published artifact.

Any future executable policy must receive a governed, minimal, purpose-bound input rather
than canonical internal person or DNA stores. It must expose finite outcomes and stable
reasons, avoid unnecessary sensitive fields, authenticate the evaluator and decision record,
support appeal and correction, and invalidate downstream derivatives when consent, evidence,
identity, or policy changes.

## Focused synthetic validation

From the repository root:

```bash
python tools/validators/validate_historical_person_place_event_resolution.py --fixtures
python -m pytest -q -p no:cacheprovider \
  tests/validators/test_validate_historical_person_place_event_resolution.py
```

Passing these commands means only that repository-owned synthetic candidates conform to the
bounded profile at the tested revision. Do not run live-source access or place real people,
DNA/genomics data, private parcels, or sensitive locations into the fixtures.

## Policy routing

- [`policy/consent/people/`](../../consent/people/) owns consent-boundary documentation.
- [`policy/sensitivity/`](../../sensitivity/) and [`policy/geoprivacy/`](../../geoprivacy/)
  own sensitivity and harmful-precision boundaries.
- [`policy/identity/`](../../identity/) and [`policy/genealogy/`](../../genealogy/) carry
  neighboring policy boundaries; their prose does not create a live resolver.
- [`policy/review/`](../../review/), [`policy/rights/`](../../rights/), and
  [`policy/release/`](../../release/) remain distinct review, rights, and release surfaces.
- The parent [`policy/match-scoring/`](../) prevents cross-family scoring collapse.

## Maintenance and rollback

Update this README when the synthetic resolver changes or when an accepted people-scoring
policy, evaluator, consumer, retention rule, appeal path, or release binding is implemented.
Verify every new claim against current repository evidence and preserve explicit holds for
living persons, DNA/genomics, private land, sovereignty, harmful precision, and public
exposure.

Before merge, rollback is to close the draft pull request and abandon its branch. After
merge, use a focused revert or corrective pull request. Reverting this documentation neither
deletes sensitive data nor revokes an external decision; those require their owning
correction, consent, retention, and release procedures.

## Open questions

- Is this leaf intended to remain a hold, or should an accepted ADR narrow, migrate, or
  retire it?
- Which verified stewards and independent reviewers would own any consequential people-
  scoring policy?
- What lawful purpose, consent basis, retention limit, appeal process, fairness review, and
  correction service would be required before any non-synthetic evaluation?
- Can a future design avoid people scoring entirely and use evidence comparison plus human
  review instead?

