# Denial reason projection fixtures

Synthetic, public-safe fixtures for the Explorer denial-reason projection.

- `valid/all-source-codes.json` contains the four Pass 32 source-named codes in
  non-display order so tests prove stable catalog ordering.
- `invalid/extra-field.json` proves free-form detail is rejected and not
  reflected.
- `invalid/unknown-reason.json` proves unregistered reason codes fail closed.

The references use synthetic `.invalid`-free KFM identifiers and placeholder
digests. No source payload, sensitive fact, real count, threshold, coordinate,
credential, attestation diagnostic, release artifact, or production identifier
is present. Fixtures create no policy, override, release, or publication
authority.
