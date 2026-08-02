# NHDPlus waterbody identifier crosswalk

Status: **PROPOSED bounded executable contract**

This contract normalizes the USGS crosswalk between NHDPlus High Resolution
waterbody Permanent Identifiers and NHDPlus Version 2 waterbody COMIDs. It is a
version-bound lookup profile, not a general replacement for flowline, reach,
HUC12, catchment, or geometry identity.

The source release is the USGS data release
[`10.5066/P13N85SW`](https://doi.org/10.5066/P13N85SW), published 2026-02-26.
USGS describes spatially overlapping waterbody polygons and explicitly notes
that one-to-many relationships may occur in either direction. The release is
marked CC0 1.0. KFM fixtures remain synthetic and contain no copied source
rows.

## Observable behavior

A conforming document:

- identifies the exact USGS release and `NHDPlusHR_NHDPlusV2.csv` source file;
- limits its feature class to `waterbody` and its relation basis to
  `spatial_overlap`;
- preserves every Permanent Identifier/COMID pair instead of forcing a
  one-to-one join;
- classifies each row as `exact`, `split`, `merge`, or `complex` from the full
  document cardinality;
- returns `ANSWER` only for an exact one-to-one pair and `ABSTAIN` for every
  multi-match row;
- records positive NHDPlus HR area, NHDPlusV2 area, and shared overlap area,
  without asserting geometry equality;
- sorts records deterministically, rejects duplicate pairs, and binds the
  document with a canonical SHA-256 `spec_hash`.

`split`, `merge`, and `complex` rows remain inspectable mapping candidates.
They cannot be silently collapsed into a single public answer.

## Responsibility and lifecycle

| Concern | Canonical home |
|---|---|
| Semantic meaning | `contracts/domains/hydrology/nhdplus_waterbody_crosswalk.md` |
| Machine shape | `schemas/contracts/v1/domains/hydrology/nhdplus_waterbody_crosswalk.schema.json` |
| Synthetic fixtures | `fixtures/domains/hydrology/nhdplus_waterbody_crosswalk/` |
| Validator | `tools/validators/domains/hydrology/validate_nhdplus_waterbody_crosswalk.py` |
| Tests | `tests/domains/hydrology/test_nhdplus_hr_ambiguity.py` |

This profile validates synthetic fixture and candidate shape only. It does not
fetch USGS bytes, admit a source, generate RAW or WORK data, resolve evidence,
approve policy, establish scientific equivalence, promote an artifact, or
publish a lookup product.

## Compatibility and rollback

The profile is additive. It does not change `ReachIdentity`, the proposed
COMID-to-HUC12 family, or existing source descriptors. Consumers must not use
it for flowlines or substitute its overlap relationship for identity equality.

Rollback is a clean revert of the contract, schema, fixtures, validator, tests,
documentation, workflow wiring, and generated receipt. No lifecycle data or
released state is migrated.
