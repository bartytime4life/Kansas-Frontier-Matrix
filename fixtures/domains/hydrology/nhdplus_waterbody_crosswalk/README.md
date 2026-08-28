# Synthetic NHDPlus waterbody crosswalk fixtures

This lane contains compact, deterministic examples for the bounded
`NHDPlusHR Permanent Identifier -> NHDPlusV2 COMID` waterbody crosswalk
profile.

- `valid/exact.json` demonstrates one unambiguous overlap and `ANSWER`.
- `valid/many_to_many.json` preserves split, merge, and complex cardinality
  with `ABSTAIN`.
- `invalid/` covers ambiguity collapse, duplicate pairs, false geometry
  equality, hash mismatch, impossible overlap area, and flowline-scope drift.

Every identifier and measurement is synthetic. These files do not contain
USGS source rows, actual waterbody locations, source bytes, or source-artifact
digests. They are test inputs only and cannot be promoted or published.

Validation:

```bash
KFM_NO_NETWORK=1 PYTHONDONTWRITEBYTECODE=1 \
python tools/validators/domains/hydrology/validate_nhdplus_waterbody_crosswalk.py --fixtures
```
