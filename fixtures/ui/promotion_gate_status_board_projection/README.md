# Promotion gate status board projection fixtures

Synthetic, no-network fixtures for the read-only Explorer promotion-gate status board.

- `valid/hold.json` shows passed, held, and not-run components and derives `HOLD`.
- `valid/ready-for-review.json` shows six projected passes while retaining no promotion or release authority.
- `valid/missing.json`, `valid/denied.json`, and `valid/error.json` prove bounded negative states carry no candidate detail.
- `invalid/extra-field.json` proves unknown fields and canary detail fail closed.
- `invalid/summary-mismatch.json` proves displayed counts and board state are recomputed rather than trusted.

These fixtures are not monitor results, scorecards, validation reports, policy decisions, attestations, release manifests, reviews, promotion decisions, or publication artifacts.
