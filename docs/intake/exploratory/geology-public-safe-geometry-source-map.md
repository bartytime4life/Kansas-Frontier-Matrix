# Geology public-safe geometry implementation source map

Status: **PROPOSED implementation mapping**

Implementation authority: **NONE**

## Evidence inspected

| Evidence | Truth label | What it supports |
|---|---|---|
| Private research corpus used for candidate discovery | `INTERNAL`; identifiers and content withheld from public provenance | Candidate selection only. It grants no repository, policy, review, release, or publication authority and is not a public citation. |
| `docs/domains/geology/POLICY.md`, `docs/domains/geology/SENSITIVITY.md`, and `data/registry/sensitivity/geology/README.md` | `CONFIRMED` repository evidence; underlying profiles remain draft where labeled | Exact subsurface, sample, private-well, and extraction-targetable geometry is restricted or generalized by default and requires separate transform, policy, review, and release support. |
| `tools/validators/geology/borehole_rights/README.md` and `schemas/contracts/v1/domains/geology/geoprivacy_transform_receipt.schema.json` | `CONFIRMED` repository evidence | The validator lane already names fail-closed exact-location and receipt requirements, while the receipt schema remains a permissive scaffold rather than executable proof. |
| `docs/doctrine/directory-rules.md` | `CONFIRMED` repository governance | Semantic contracts, canonical schemas, fixtures, validators, workflows, and generated authoring receipts remain in their owning roots. |
| Current repository inventory at base commit `149af17075f7f12d716aa14de439ea22ee6a343e` | `CONFIRMED` by inspection | The public-safe geometry test is a one-line placeholder; the specialized validator lane is documentation-only; the existing geoprivacy receipt schema is an open permissive scaffold. |

## Implemented mapping

| Source idea | Repository artifact | Boundary |
|---|---|---|
| Public-safe geometry preflight | `contracts/domains/geology/public_safe_geometry_assessment.md` | Defines a fixture-only assessment, not Geology truth or policy. |
| Closed machine shape | `schemas/contracts/v1/domains/geology/public_safe_geometry_assessment.schema.json` | Denies undeclared fields and coordinate material; grants no authority. |
| Positive and negative cases | `fixtures/contracts/v1/domains/geology/public_safe_geometry/cases.json` | Synthetic opaque references only; no real locations or geometry bytes. |
| Deterministic checker | `tools/validators/geology/public_safe_geometry/validate_public_safe_geometry.py` | Computes `HOLD` or `DENY`; performs no transform or network access. |
| Regression coverage | `tests/domains/geology/test_public_safe_geometry.py` | Freezes schema closure, case polarity, no-network behavior, identity, and non-effects. |
| CI execution | `.github/workflows/domain-geology.yml` | Runs the bounded profile while retaining broader evidence, proof, and release holds. |

## Deliberately deferred

- a canonical `GeologyRedactionReceipt` or `GeoprivacyTransformReceipt` contract;
- any geometry library, coordinate parsing, simplification, aggregation, or
  topology operation;
- live source, rights, sensitivity, policy, or review resolution;
- lifecycle writes, EvidenceBundle or ProofPack production;
- release-manifest creation, map/API/export serving, and publication;
- authoritative expansion beyond the five frozen fixture object families.

The existing permissive
`schemas/contracts/v1/domains/geology/geoprivacy_transform_receipt.schema.json`
is intentionally not activated or treated as evidence. A future receipt design
requires its own contract, fixtures, validator, review, and authority decision.

## Verification posture

The repository safety posture and implementation gap are `CONFIRMED`. The
exact field names, finding codes, frozen object-family mapping, and assessment
profile are `PROPOSED` until reviewed. Private discovery materials are neither
copied nor treated as public evidence. Nothing in this slice is a policy,
review, release, or publication decision.
