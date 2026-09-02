# Synthetic HUC12-COMID Crosswalk Manifest Fixtures

These no-network fixtures prove only the proposed manifest shape, canonical hash, digest binding, time ordering, append-only transition rules, and material-change hold semantics.

- `valid/`: independently valid candidate manifests.
- `invalid/`: malformed or semantically inconsistent manifests that must fail closed.
- `hold/`: a valid prior slice plus valid candidates whose NHD snapshot or crosswalk digest changed; these produce `HOLD`, never `PASS`.

All identifiers, hashes, counts, times, and references are synthetic. No fixture is source admission, real hydrologic evidence, policy approval, release, or publication authority.
