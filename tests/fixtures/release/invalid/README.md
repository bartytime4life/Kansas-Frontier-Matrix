# Invalid release fixtures

These files intentionally violate required release fields so validators and tests can
assert specific failure modes.

## Files

- `missing_provenance_ref.release-manifest.json` — artifact omits required
  `provenance_ref`.
- `unresolved_artifact.release-manifest.json` — artifact points to a non-existent local
  publication path.
- `missing_closure_status.publish-receipt.json` — publish receipt plan omits
  `closure_status`.
