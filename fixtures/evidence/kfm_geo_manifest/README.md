# KFMGeoManifest fixture profile

This directory contains a compact synthetic corpus for the proposed
`KFMGeoManifest` metadata profile.

## Lanes

- `valid_cases.json` — three metadata/payload pairs for a PMTiles release
  candidate, generalized COG derivative, and GeoJSON rollback target.
- `invalid_cases.json` — four closed-schema failures.
- `semantic_invalid_cases_a.json` and `semantic_invalid_cases_b.json` — eleven
  schema-valid semantic and local-byte failures with exact finding-code sets.

Each case is a harness wrapper with `name`, `manifest`, optional `payload_text`,
and expected finding codes. The wrapper is not a canonical KFM object. Only the
nested `manifest` is evaluated against the schema.

The payloads are deliberately small UTF-8 fixture bytes. They prove digest and
byte-length binding only; they are **not** valid PMTiles, COG, or production
geospatial files and must not be used to claim format conformance.

## Validation

```bash
KFM_NO_NETWORK=1 python tools/validators/evidence/validate_kfm_geo_manifest.py --fixtures

KFM_NO_NETWORK=1 python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_kfm_geo_manifest.py' \
  --verbose
```

A passing result grants no evidence, policy, review, signature, release,
deployment, publication, or public-use authority. ADR-0023 remains proposed.
