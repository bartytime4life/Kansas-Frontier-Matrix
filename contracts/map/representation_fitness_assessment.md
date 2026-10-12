# RepresentationFitnessAssessment

Status: PROPOSED_INACTIVE  
Profile: `kfm.map.representation-fitness.v1`

`RepresentationFitnessAssessment` is a deterministic, fixture-only assessment of whether a representation's declared scale, temporal coverage, source role, fidelity, and geometry character are compatible with one declared use.

It complements `RepresentationReceipt`; it does not replace that receipt, EvidenceBundle, policy, review, release, or publication authority.

## Intended uses

- `BROWSE`: orientation and visual exploration.
- `CONTEXT`: contextual interpretation where generalized or modeled carriers may be acceptable if declared.
- `ANALYSIS`: analytical use requiring evidence binding and non-synthetic support.
- `MEASUREMENT`: quantitative use requiring `OBSERVATION`, `EXACT` fidelity, `EXACT` geometry, and temporal coverage.
- `DECISION_SUPPORT`: non-authoritative decision support requiring evidence binding and excluding contextual-only or synthetic support.

## Outcomes

- `FIT`: all declared constraints are compatible with the declared use.
- `HOLD`: the representation is structurally valid but one or more use constraints are not satisfied.
- `ERROR`: malformed, inconsistent, non-deterministic, or authority-overreaching candidate.

## Boundary

A `FIT` result is not evidence truth, policy approval, professional advice, release readiness, or public-use authorization. It means only that the declared representation metadata is internally compatible with the bounded rules in this profile.
