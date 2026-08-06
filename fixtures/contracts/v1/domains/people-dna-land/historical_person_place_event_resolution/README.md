# Historical person-place-event resolution fixtures

`fixtures/contracts/v1/domains/people-dna-land/historical_person_place_event_resolution/`

Status: **PROPOSED semantic profile / CONFIRMED synthetic fixture bytes / not released**.

This directory carries a bounded, no-network fixture profile derived from the historical
identity-resolution recipe in *New Ideas 3-11-26.pdf*, pages 25–28. The profile exercises:

- a three-point authority-match signal;
- a two-point independent same-county/time co-mention signal;
- a two-point exact GLO legal-description anchor;
- a three-point deduction for strong contradictory evidence;
- deterministic `high`, `medium`, and `low` confidence bands;
- fail-closed living-person, public-release, raw-DNA, precise-location, and private-parcel boundaries.

All records are visibly synthetic. `county_fips=99999`, `Synthetic County`, and the
`T00S/R00W/S00` legal-description sentinel cannot be treated as real geography. The
fixtures do not contain real names, real authority identifiers, real patent identifiers,
real scan identifiers, DNA/genomic material, title evidence, private parcel identifiers,
or released KFM claims.

## Expected polarity

| Lane | Expected result |
|---|---|
| `valid/high_anchor.json` | score `7`, `high`, `candidate_review` |
| `valid/conflict_hold.json` | score `4`, `medium`, `hold_for_review` |
| `valid/weak_abstain.json` | score `0`, `low`, `abstain` |
| `invalid/*.json` | deterministic rejection matching the sibling `*.expected_error.txt` code |

A valid result proves only that the fixture conforms to this candidate profile. It does not
establish identity, residence, migration, land ownership, patent validity, title, rights,
policy approval, review approval, EvidenceBundle sufficiency, release, or publication.
