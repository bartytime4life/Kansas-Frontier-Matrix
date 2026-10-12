# County NDVI change projection fixtures

These synthetic packets exercise the app-local
`kfm.explorer.county-ndvi-change.fixture.v1` display boundary.

- `valid/candidate.json` exposes coherent candidate metrics while keeping
  evidence visibly unresolved and all authority false.
- `valid/missing.json`, `valid/denied.json`, and `valid/error.json` carry no
  county, metric, or reference detail.
- `invalid/extra-field.json` proves unknown detail fails closed without
  reflecting its canary.
- `invalid/delta-mismatch.json` proves the panel cannot display incoherent
  arithmetic.

The fixtures contain no real county geometry, raster cells, source payloads,
coordinates, live identifiers, resolved EvidenceBundles, policy decisions, or
released environmental claims. Fixture validity is not scientific, policy,
release, or publication approval.
