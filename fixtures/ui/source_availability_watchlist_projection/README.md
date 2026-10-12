# Source availability watchlist projection fixtures

Synthetic, no-network fixtures for the Explorer read-only `SourceAvailabilityWatchlist` projection.

- `valid/available.json` shows stable and review-routed sources.
- `valid/held.json` shows unresolved availability without guessing.
- `valid/denied.json` and `valid/error.json` prove fixed negative states carry no source detail.
- `invalid/extra-field.json` proves unknown fields and canary detail fail closed.
- `invalid/candidate-binding.json` proves review routing cannot omit the separately referenced candidate-work record.

These fixtures are not source evidence, source-health observations, candidate work, policy decisions, release records, or publication artifacts.
