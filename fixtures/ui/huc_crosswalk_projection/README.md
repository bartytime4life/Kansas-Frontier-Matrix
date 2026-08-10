# HUC crosswalk projection fixtures

Synthetic, public-safe fixtures for the Explorer HUC crosswalk projection.

- `valid/verified-exact.json` carries two sorted digest-bound station references
  behind a digest-bound crosswalk and validation-receipt reference.
- `valid/ambiguous.json` proves an ambiguous crosswalk yields `ABSTAIN` and no
  station references.
- `invalid/extra-field.json` proves source detail is rejected and not reflected.
- `invalid/outcome-status-mismatch.json` proves finite status, outcome, and
  reason code cannot drift apart.

The fixtures contain synthetic identifiers and placeholder digests only. They
contain no source rows, real observations, flow values, geometry, counts,
thresholds, credentials, signatures, internal lifecycle references, release
artifact, or production identifier. They create no hydrology, evidence,
policy, review, release, publication, or public-use authority.
