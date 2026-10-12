# ClassificationRelease fixture profile

This directory contains a compact base-plus-mutation fixture matrix for the inactive `kfm.common.classification-release.v1` candidate.

## Scope

The fixture set proves:

- four coherent lineage states: `CURRENT`, `CORRECTED`, `SUPERSEDED`, and `CONFLICTED`;
- classification source-role and derived-classification support boundaries;
- broad spatial scale rather than point-observation collapse;
- distinct data-cutoff, validity, source-release, retrieval, correction, and supersession times;
- geometry resolution rules;
- canonical references and class codes;
- all-false source/evidence/policy/promotion/release/publication effects;
- deterministic `spec_hash` and `classification_release_id`.

The committed fixtures are synthetic. Names resembling a real product are vocabulary examples only and are not current source data, evidence, policy, review, release, or public guidance.

## Matrix

`cases.json` holds one reusable base and eight exact cases:

| Expected outcome | Count |
|---|---:|
| `PASS` | 4 |
| `DENY` | 3 |
| `ERROR` | 1 |

Each semantic-negative case recomputes identity after its isolated mutation. The identity-corruption case intentionally retains a mismatched spec hash.

## Exclusions

The fixtures perform no network access, source activation, source-rights decision, EvidenceBundle resolution, lifecycle write, promotion, release, deployment, publication, map rendering, API delivery, or AI interpretation.

The existing soil DomainObservation fixture remains the observation-side proof. `tests/cross_domain/test_classification_observation_boundary.py` verifies that the station candidate and the ClassificationRelease candidate cannot substitute for each other.
