# PMTiles range diagnostics projection fixtures

Synthetic, no-network fixtures for the read-only Explorer PMTiles range-diagnostics panel.

- `valid/available.json` represents the existing partial-read compatibility result as `STRUCTURAL_HOLD`.
- `valid/missing.json`, `valid/denied.json`, and `valid/error.json` prove bounded negative states carry no artifact detail.
- `invalid/extra-field.json` proves unknown fields and canary detail fail closed.
- `invalid/crypto-overclaim.json` proves the UI projection cannot claim cryptographic verification while the current compatibility lane leaves it unresolved.

These fixtures are not archive bytes, signatures, trusted sidecars, policy decisions, health declarations, release records, or publication artifacts.
