# Municipal Legal-Status Support Envelope — Settlements / Infrastructure

> **Status:** `PROPOSED` · synthetic fixture-first semantic contract · no live source · no geometry · no policy approval · no release/publication effect

## Purpose
`MunicipalLegalStatusSupportEnvelope` is a bounded synthetic profile for one question: can a place identity explicitly typed as `Municipality` carry time-scoped administrative legal-status support while Census geography remains a separate aggregate context?

It consumes the existing `PlaceIdentityProfile` distinction without redefining place identity. It does not determine any real municipality's status, query or activate a source, resolve an EvidenceBundle, make a PolicyDecision, perform review, create a ReleaseManifest, expose a route, or publish data.

## Authority boundary
- `contracts/domains/settlements-infrastructure/place-identity.md` owns the place-family distinction.
- `schemas/contracts/v1/domains/settlements-infrastructure/place-identity.schema.json` is the existing bounded machine profile for `Municipality` versus `CensusPlace`.
- This contract adds only a synthetic support-envelope profile.
- `policy/domains/settlements-infrastructure/municipality_evidence.rego` remains an unactivated `PROPOSED` scaffold and is not modified or treated as policy authority.
- Real municipal status requires current authoritative administrative/legal evidence, rights review, source admission, EvidenceRef-to-EvidenceBundle closure, policy, review, and release controls outside this slice.

## Non-collapse rules
1. `Municipality` and `CensusPlace` are not interchangeable.
2. Legal-status support uses the `administrative` source role.
3. Census geography is contextual and uses the `aggregate` source role; it is never municipal legal proof.
4. `as_of` is evaluated against the legal evidence effective interval.
5. Missing, undated, or out-of-scope legal evidence yields `ABSTAIN`, never inference.
6. A `CensusPlace` used as the subject of a municipal legal-status claim yields `DENY`.
7. Structurally valid synthetic input faults yield `ERROR`.
8. A bounded `ANSWER` means only synthetic support completeness; it does not assert real legal status.
9. Policy, review, and release placeholders remain unresolved/unreleased and cannot be upgraded by validation.
10. No coordinate, address, parcel, facility, operator, infrastructure, protected-location, or private-property field is accepted.

## Finite outcomes
| Condition | Outcome | Reason |
|---|---|---|
| Synthetic `Municipality`; complete administrative legal evidence; `as_of` in interval | `ANSWER` | `LEGAL_STATUS_SUPPORT_PRESENT` |
| Municipality but legal evidence absent, undated, or outside interval | `ABSTAIN` | `LEGAL_STATUS_EVIDENCE_INSUFFICIENT`, `LEGAL_STATUS_EVIDENCE_UNDATED`, or `LEGAL_STATUS_EVIDENCE_OUT_OF_SCOPE` |
| Subject is `CensusPlace` | `DENY` | `CENSUS_PLACE_NOT_MUNICIPALITY` |
| Explicit synthetic input error or partial legal evidence binding | `ERROR` | `SYNTHETIC_INPUT_ERROR` or `LEGAL_EVIDENCE_PARTIAL` |

## Temporal rules
`claim.as_of`, legal `source_date`, and legal effective time are separate. Census `vintage` is separate again. Reversed legal effective intervals are invalid.

## Fixture and precision boundary
Fixtures use only `source:synthetic:*`, `evidence:synthetic:*`, and synthetic place identifiers. They contain no real municipality name, source endpoint, coordinate, facility, parcel, address, private-property link, infrastructure detail, or protected location.

## Validation boundary
A green result proves strict JSON shape, deterministic hashing, source-role separation, Municipality/CensusPlace anti-collapse behavior, temporal support logic, finite-outcome polarity, unresolved policy/review/release placeholders, and fail-closed input handling. It proves no real-world fact, source currentness or rights, EvidenceBundle closure, policy/review approval, release, deployment, or publication.

## Rollback
Before any later release adoption, rollback is ordinary code rollback: revert this bounded contract/schema/fixture/validator/test/workflow set. No source, lifecycle payload, public alias, database, tile, graph, API, or release artifact is created by this slice.
