<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/policy-match-scoring-readme
title: policy/match-scoring/ — Scoring Policy Routing and Hold Boundary
type: readme
version: v1.0.0
status: draft; routing-and-hold; implementation-empty; evaluator-unbound; non-release; non-publication
owner: NEEDS VERIFICATION — policy stewardship and independent approval controls are not established
created: 2026-08-28
updated: 2026-08-28
current_path: policy/match-scoring/README.md
owning_root: policy/
policy_label: public; policy; scoring; routing; hold; non-release; non-publication
responsibility: Route scoring-related admissibility work to its owning contract, schema, policy, validator, and consumer surfaces without creating a universal scoring rule or evaluator.
base_commit: f68fe0ff504562bb8d2b4aedacb3d46eb66f17f3
prior_blob: 8b137891791fe96927ad78e64b0aad7bded08bdc
truth_posture: CONFIRMED tracked documentation-only lane with one sensitive child, no Rego, schema, fixture, validator, test, workflow, bundle, evaluator, receipt, or consumer under this directory / CONFIRMED separate scoring families in governance, Habitat, Water Planning, People-DNA-Land, and Explorer UI surfaces / PROPOSED routing-and-hold boundary / UNKNOWN accepted cross-family scoring policy, writers, readers, retention, evaluator binding, production consumers, and release significance
[/KFM_META_BLOCK_V2] -->

# Scoring policy routing and hold boundary

`policy/match-scoring/` is a documentation boundary for deciding where scoring-related
policy work belongs. It does not define a universal score, weight, threshold, confidence
band, ranking, eligibility rule, model, or evaluator.

> [!IMPORTANT]
> Current repository evidence shows several separate scoring families with different
> meanings and maturity. Do not aggregate them, compare their numeric values, or treat this
> directory as their shared authority.

## Current state

At `main@f68fe0ff504562bb8d2b4aedacb3d46eb66f17f3`, this directory contains this README,
the [`people/`](./people/) child, and no executable policy artifact. Code search finds no
consumer referencing `policy/match-scoring`.

| Surface | Confirmed role | Boundary |
|---|---|---|
| [`CoveragePriorityScorecard`](../../contracts/governance/coverage_priority_scorecard.md) | Synthetic, local workflow-triage scorecard with a schema, fixtures, validator, tests, workflow, and `HOLD`/`ABSTAIN` posture | It does not select real counties, assign work or funding, activate sources, or authorize publication. |
| [`HabitatQualityScore`](../../contracts/domains/habitat/habitat_quality_score.md) | Draft semantic contract for an evidence- and uncertainty-bounded descriptive Habitat score | Its schema and [`quality_score.rego`](../domains/habitat/quality_score.rego) remain proposed scaffolds; it is not a management instruction, regulatory designation, occurrence claim, or release authority. |
| [`ScoringMatrixVersion`](../../contracts/domains/water_planning/scoring_matrix_version.md) | Draft document-lineage envelope for a water-planning scoring-matrix version | It does not encode criteria, weights, thresholds, an application score, rank, eligibility, recommendation, award, or payment. |
| [`Historical Person-Place-Event Resolution Candidate`](../../contracts/domains/people-dna-land/historical_person_place_event_resolution.md) | Bounded, deterministic, no-network scoring profile over synthetic historical candidates | It does not establish identity, residence, migration, land ownership, title, rights, policy, release, or publication. See the sensitive [`people/`](./people/) boundary. |
| [Environmental anomaly scorecard](../../apps/explorer-web/src/features/environmental_anomaly_scorecard/README.md) | Inactive, strict Explorer projection over synthetic fixture state | It is not route-mounted and performs no anomaly computation, interpretation, policy evaluation, release, or public-use action. |

These are neighboring uses of the word “score,” not one object family. Their owning
contracts, schemas, policies, validators, tests, and consumers remain authoritative for
their bounded claims.

## What belongs here

Until an accepted policy design establishes a narrower responsibility, this lane may carry:

- documentation that routes a proposed scoring policy to its owning family;
- explicit holds on cross-family normalization, thresholding, ranking, or aggregation;
- questions about admissibility, sensitivity, fairness, review, correction, and rollback;
- a reviewed pointer to an executable policy artifact located under the correct policy
  family, if that artifact is later implemented and accepted.

## What does not belong here

- semantic contracts or machine schemas;
- scoring methods, model weights, thresholds, fixtures, validators, or tests;
- model outputs, rankings, decisions, EvidenceBundles, receipts, proofs, or release records;
- source data, applicant records, person records, DNA or genomics material, precise private
  locations, or sensitive habitat geometry;
- UI projections, runtime adapters, caches, lifecycle data, or published artifacts.

Directory Rules make placement an authority claim. Put each artifact under the
responsibility that owns it; do not copy a score into this directory to imply policy
activation.

## Required decision boundary

A future scoring-policy proposal must stay fail-closed until it identifies, at minimum:

1. the exact scored subject and object family;
2. the score meaning, direction, unit or category, method, and version;
3. inputs, source roles, rights, sensitivity, temporal scope, missingness, uncertainty, and
   contradiction handling;
4. accepted thresholds and the evidence supporting them;
5. finite outcomes and stable reason codes;
6. reviewer roles, separation of duties, appeal or correction path, and rollback target;
7. the executable rule, bundle identity, evaluator, fixtures, negative tests, consumers, and
   decision-receipt binding;
8. whether the result is only descriptive, supports triage, or has any consequential effect;
9. release and public-exposure constraints, including harmful-precision controls.

Absent that closure, the safe result is `HOLD`, `ABSTAIN`, or `DENY` according to the
owning profile. A numerical value is never self-authorizing.

## Failure cases

Fail closed when a proposal:

- compares or combines scores from different families without an accepted crosswalk;
- hides missingness, uncertainty, negative evidence, source-role concentration, or a changed
  counterfactual ranking;
- treats a model, map, UI, AI explanation, green test, or workflow as score truth;
- uses a score as identity, consent, eligibility, title, regulatory status, funding,
  management, release, or publication authority;
- exposes a living person, DNA/genomics relationship, private parcel join, sensitive species
  location, applicant record, reviewer note, or deliberative material;
- lacks a correction path or cannot invalidate downstream reliance after inputs, methods,
  thresholds, or policy change.

## Focused evidence checks

Run only the checks for the owning family. The following current commands exercise two
implemented synthetic profiles; they do not validate this documentation lane or activate a
policy:

```bash
python tools/validators/governance/validate_coverage_priority_scorecard.py --fixtures
python -m pytest -q -p no:cacheprovider \
  tests/validators/governance/test_coverage_priority_scorecard.py

python tools/validators/validate_historical_person_place_event_resolution.py --fixtures
python -m pytest -q -p no:cacheprovider \
  tests/validators/test_validate_historical_person_place_event_resolution.py
```

A passing result proves only deterministic conformance for the tested repository-owned
fixtures at that revision. It creates no accepted threshold, authenticated policy decision,
review, release, deployment, promotion, publication, or public-use authority.

## Maintenance

Update this boundary when a scoring family is added, moved, accepted, retired, or gains an
actual policy consumer. Preserve family-specific ownership and link to the exact contract,
schema, rule, validator, test, and consumer evidence. Do not report broader maturity from a
single bounded profile.

Before merge, rollback is to close the draft pull request and abandon its branch. After
merge, use a focused revert or corrective pull request. Reverting documentation does not
reverse a score, policy decision, release, or external reliance.

## Open questions

- Does this directory have an accepted responsibility beyond routing and holds?
- Which verified steward and independent reviewer own a future cross-family scoring policy?
- Are any production or external consumers expected to resolve this path?
- What retention, audit, appeal, correction, and replay requirements apply to consequential
  scores?
- Should an accepted ADR retain, narrow, alias, migrate, or retire this path?

## Related

- [`policy/`](../) — canonical policy root and current maturity inventory.
- [`policy/thresholds/`](../thresholds/) — inactive threshold-slot candidate registry; it
  does not supply values to this lane.
- [`policy/decision/`](../decision/) — policy decision boundary; not evidence that a scoring
  result is bound to an accepted evaluator.
- [Accepted Directory Rules decision](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)
  and [adopted Directory Rules bytes](../../docs/doctrine/directory-rules.md).

